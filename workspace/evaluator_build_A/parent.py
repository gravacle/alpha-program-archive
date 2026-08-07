#!/usr/bin/env python3
"""Fresh RD-22 parent for Builder A producer and Builder B verifier."""

import argparse
import ast
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from pathlib import Path


SPEC_SHA256 = "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b"
AUTHORIZATION_SHA256 = "ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340"
RUNTIME_SNAPSHOT_SHA256 = "50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb"
RUNTIME_GATE_SHA256 = "2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42"
INTEGRATION_ADDENDUM_SHA256 = "d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260"
MASK_FIELDS = {"process_id", "monotonic_duration", "python_optimize"}
EXPECTED_IDS = 66
EXPECTED_STRUCTURAL = 56
EXPECTED_GATED = 10
EXPECTED_FIXTURES = 6


class ParentFailure(Exception):
    pass


def fail(code, detail):
    raise ParentFailure(f"{code}: {detail}")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(path):
    try:
        return Path(path).read_bytes()
    except OSError as exc:
        fail("READ_FAILED", f"{path}: {exc}")


def verify_bytes(path, expected):
    data = read_bytes(path)
    actual = sha256_bytes(data)
    if actual != expected:
        fail("HASH_MISMATCH", f"{path}: expected {expected}, got {actual}")
    return data


def reject_constant(value):
    fail("STRICT_JSON_NONFINITE", value)


def reject_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            fail("STRICT_JSON_DUPLICATE_KEY", key)
        out[key] = value
    return out


def strict_json(data, label):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("STRICT_JSON_UTF8", f"{label}: {exc}")
    try:
        return json.loads(text, object_pairs_hook=reject_pairs, parse_constant=reject_constant)
    except (json.JSONDecodeError, ParentFailure) as exc:
        fail("STRICT_JSON_PARSE", f"{label}: {exc}")


def canonical_bytes(value):
    try:
        text = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":"))
    except (TypeError, ValueError) as exc:
        fail("CANONICAL_JSON", str(exc))
    return (text + "\n").encode("utf-8")


def exact_keys(value, keys, label):
    if not isinstance(value, dict):
        fail("SCHEMA_TYPE", f"{label} not object")
    actual = set(value)
    wanted = set(keys)
    if actual != wanted:
        fail("SCHEMA_FIELDS", f"{label}: missing={sorted(wanted-actual)}, extra={sorted(actual-wanted)}")


def safe_resolve(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        fail("RELATIVE_PATH", repr(relative))
    base = Path(root).resolve()
    target = (base / relative).resolve()
    try:
        target.relative_to(base)
    except ValueError:
        fail("PATH_ESCAPE", relative)
    return target


def exclusive_write(path, data):
    target = Path(path)
    if not target.parent.is_dir():
        fail("OUTPUT_PARENT", str(target.parent))
    try:
        fd = os.open(str(target), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except OSError as exc:
        fail("EXCLUSIVE_CREATE", f"{target}: {exc}")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except OSError as exc:
        fail("WRITE", f"{target}: {exc}")


def no_python_check_nodes(source_bytes, label):
    try:
        tree = ast.parse(source_bytes.decode("utf-8"), filename=label)
    except (UnicodeDecodeError, SyntaxError) as exc:
        fail("SOURCE_PARSE", f"{label}: {exc}")
    forbidden_type = getattr(ast, "As" + "sert")
    hits = [getattr(node, "lineno", 0) for node in ast.walk(tree) if isinstance(node, forbidden_type)]
    if hits:
        fail("PYTHON_CHECK_NODE", f"{label}:{hits}")


def parse_manifest(path, expected_sha, mode):
    data = verify_bytes(path, expected_sha)
    if canonical_bytes(strict_json(data, str(path))) != data:
        fail("MANIFEST_NOT_CANONICAL", str(path))
    manifest = strict_json(data, str(path))
    required = {
        "allowed_events",
        "authority_firewall",
        "branch_outcome",
        "check_ids",
        "check_map_sha256",
        "evidence_manifest_sha256",
        "external_inputs",
        "fixture_ids",
        "fixture_manifest_sha256",
        "mode",
        "optimization",
        "package_files",
        "runtime_subject",
        "schema",
        "specification_sha256",
        "subject_lineage_root",
        "writable_paths",
    }
    exact_keys(manifest, required, f"{mode} manifest")
    if manifest["schema"] != "rd22.child-manifest.v001" or manifest["mode"] != mode:
        fail("MANIFEST_MODE", mode)
    wanted_opt = 0 if mode == "normal" else 1
    if manifest["optimization"] != wanted_opt:
        fail("MANIFEST_OPTIMIZATION", mode)
    return manifest, data


def verify_package_inventory(package_root, manifest):
    rows = manifest["package_files"]
    if not isinstance(rows, list):
        fail("PACKAGE_INVENTORY", "not list")
    seen = set()
    values = {}
    for row in rows:
        exact_keys(row, {"byte_length", "relative_path", "sha256"}, "package row")
        relative = row["relative_path"]
        if relative in seen:
            fail("DUPLICATE_PACKAGE_PATH", relative)
        seen.add(relative)
        target = safe_resolve(package_root, relative)
        data = verify_bytes(target, row["sha256"])
        if len(data) != row["byte_length"]:
            fail("BYTE_LENGTH", relative)
        values[relative] = (target, data)
    required = {
        "parent.py",
        "producer.py",
        "checks/check_map.json",
        "fixtures/fixture_manifest.json",
        "inputs/structural_evidence_manifest.json",
        "schemas/child-receipt.schema.json",
        "schemas/producer-output.schema.json",
        "schemas/terminal-ledger.schema.json",
        "schemas/verifier-manifest.schema.json",
        "schemas/verifier-output.schema.json",
    }
    if not required.issubset(seen):
        fail("PACKAGE_REQUIRED_FILES", sorted(required-seen))
    return values


def verify_external_inputs(program_root, authorization_path, manifest):
    external = manifest["external_inputs"]
    if not isinstance(external, list):
        fail("EXTERNAL_INPUTS", "not list")
    seen = set()
    for row in external:
        exact_keys(row, {"byte_length", "kind", "relative_path", "sha256"}, "external row")
        kind = row["kind"]
        if kind in seen:
            fail("EXTERNAL_KIND_DUPLICATE", kind)
        seen.add(kind)
        if kind == "authorization":
            target = Path(authorization_path).resolve()
        else:
            target = safe_resolve(program_root, row["relative_path"])
        data = verify_bytes(target, row["sha256"])
        if len(data) != row["byte_length"]:
            fail("EXTERNAL_BYTE_LENGTH", kind)
    required = {"authorization", "blocker_ledger", "integration_addendum", "packet_manifest", "runtime_gate", "runtime_snapshot", "specification"}
    if seen != required:
        fail("EXTERNAL_KIND_SET", f"missing={sorted(required-seen)}, extra={sorted(seen-required)}")


def validate_runtime(snapshot_data, gate_data):
    snapshot = strict_json(snapshot_data, "runtime snapshot")
    required = {
        "allowed_optimization_levels",
        "alpha_computed",
        "builder_path",
        "builder_sha256",
        "bundled_site_packages_files",
        "bundled_site_packages_root",
        "execution_assurance_scope",
        "forbidden_startup_modes",
        "gate_path",
        "gate_sha256",
        "launcher_direct_execution_required",
        "launcher_invocation_mode",
        "launcher_path",
        "launcher_sha256",
        "libpython_path",
        "libpython_sha256",
        "native_system_trust_root",
        "prelaunch_python_execution_resistance_claimed",
        "python_executable",
        "python_executable_sha256",
        "python_runtime_files",
        "python_runtime_root",
        "python_version",
        "required_flags",
        "schema",
        "source_only_pycache_initially_empty",
        "source_only_pycache_root",
        "source_only_required_option",
        "workspace_site_packages_files",
        "workspace_site_packages_root",
    }
    exact_keys(snapshot, required, "runtime snapshot")
    if snapshot["schema"] != "gravacle.content-addressed-runtime.v012":
        fail("RUNTIME_SCHEMA", snapshot["schema"])
    if snapshot["gate_sha256"] != RUNTIME_GATE_SHA256 or snapshot["required_flags"] != ["-I", "-S", "-B"]:
        fail("RUNTIME_CONTRACT", "pin/flags")
    if snapshot["allowed_optimization_levels"] != [0, 1]:
        fail("RUNTIME_OPTIMIZATION", snapshot["allowed_optimization_levels"])
    if snapshot["launcher_invocation_mode"] != "direct-script-no-c-no-m":
        fail("RUNTIME_LAUNCH_MODE", snapshot["launcher_invocation_mode"])
    python_path = Path(snapshot["python_executable"]).resolve()
    verify_bytes(python_path, snapshot["python_executable_sha256"])
    if Path(sys.executable).resolve() != python_path:
        fail("RUNTIME_INTERPRETER", f"{sys.executable} != {python_path}")
    if "fresh" not in gate_data.decode("utf-8").casefold():
        fail("RUNTIME_GATE_CONTENT", "fresh missing")
    return snapshot


def trust_snapshot(runtime):
    try:
        sw = subprocess.run(["/usr/bin/sw_vers"], check=True, capture_output=True, env={}).stdout.decode("utf-8")
        sip_run = subprocess.run(["/usr/bin/csrutil", "status"], check=False, capture_output=True, env={})
        sip = (sip_run.stdout + sip_run.stderr).decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        fail("TRUST_COMMAND", str(exc))
    observed = {
        "csrutil_status": sip,
        "machine": platform.machine(),
        "platform": platform.platform(),
        "policy": runtime["native_system_trust_root"]["policy"],
        "sw_vers": sw,
    }
    expected = runtime["native_system_trust_root"]
    if observed != expected:
        fail("TRUST_DRIFT", {"expected": expected, "observed": observed})
    return observed


def trust_hash(value):
    return sha256_bytes(canonical_bytes(value))


def ensure_empty_directory(path):
    target = Path(path)
    if not target.is_dir() or target.is_symlink():
        fail("PYCACHE_ROOT", str(target))
    entries = list(target.iterdir())
    if entries:
        fail("PYCACHE_NOT_EMPTY", [str(item) for item in entries])


def ensure_absent(paths):
    present = [str(path) for path in paths if Path(path).exists() or Path(path).is_symlink()]
    if present:
        fail("OUTPUT_PREEXISTS", present)


def run_child(command, label):
    try:
        completed = subprocess.run(command, check=False, capture_output=True, env={})
    except OSError as exc:
        fail("CHILD_LAUNCH", f"{label}: {exc}")
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace")[-4000:]
        stdout = completed.stdout.decode("utf-8", errors="replace")[-4000:]
        fail("CHILD_EXIT", f"{label}:{completed.returncode}:stdout={stdout}:stderr={stderr}")


def receipt(path):
    data = read_bytes(path)
    if canonical_bytes(strict_json(data, str(path))) != data:
        fail("RECEIPT_NOT_CANONICAL", str(path))
    value = strict_json(data, str(path))
    keys = {
        "authority",
        "environment_event_ledger",
        "manifest_sha256",
        "module_ledger",
        "monotonic_duration",
        "mutation_event_ledger",
        "native_ledger",
        "network_event_ledger",
        "open_event_ledger",
        "optimize",
        "output_sha256",
        "process_event_ledger",
        "process_id",
        "schema",
        "target_sha256",
        "write_event_ledger",
    }
    exact_keys(value, keys, "receipt")
    if value["schema"] != "rd22.child-receipt.v001" or value["authority"] is not False:
        fail("RECEIPT_AUTHORITY", str(path))
    return value, data


def output(path):
    data = read_bytes(path)
    value = strict_json(data, str(path))
    if canonical_bytes(value) != data:
        fail("OUTPUT_NOT_CANONICAL", str(path))
    keys = {
        "authority_firewall",
        "check_map_sha256",
        "checks",
        "fixture_manifest_sha256",
        "fixtures",
        "manifest_sha256",
        "monotonic_duration",
        "process_id",
        "python_optimize",
        "schema",
        "scope",
        "spec_sha256",
        "subject_lineage_root",
        "summary",
    }
    exact_keys(value, keys, "producer output")
    if value["schema"] != "rd22.producer-output.v001":
        fail("OUTPUT_SCHEMA", value["schema"])
    return value, data


def classify_receipt(value, expected_manifest_sha, expected_target_sha, optimize, output_sha, output_path, receipt_path, runtime, extra_module_root=None, stdout_output=False):
    if value["manifest_sha256"] != expected_manifest_sha or value["target_sha256"] != expected_target_sha:
        fail("RECEIPT_PIN", optimize)
    if value["optimize"] != optimize or value["output_sha256"] != output_sha:
        fail("RECEIPT_OUTPUT", optimize)
    if value["process_event_ledger"] or value["network_event_ledger"] or value["environment_event_ledger"]:
        fail("RECEIPT_FORBIDDEN_EVENT", optimize)
    writes = value["write_event_ledger"]
    expected_writes = []
    if not stdout_output:
        expected_writes.append({"operation": "exclusive_create", "path": str(Path(output_path).resolve())})
    expected_writes.append({"operation": "exclusive_create", "path": str(Path(receipt_path).resolve())})
    if writes != expected_writes:
        fail("RECEIPT_WRITE_SET", {"expected": expected_writes, "actual": writes})
    if value["mutation_event_ledger"] != expected_writes:
        fail("RECEIPT_MUTATION_SET", {"expected": expected_writes, "actual": value["mutation_event_ledger"]})
    runtime_root = Path(runtime["python_runtime_root"]).resolve()
    system_prefixes = [Path("/System/Library"), Path("/usr/lib")]
    for row in value["module_ledger"]:
        exact_keys(row, {"kind", "module", "path", "sha256"}, "module row")
        path = row["path"]
        if path is None:
            if row["kind"] != "builtin_or_frozen":
                fail("MODULE_ORIGIN", row)
            continue
        target = Path(path).resolve()
        if target.suffix == ".pyc":
            fail("BYTECODE_MODULE", path)
        if row["sha256"] is None or sha256_bytes(read_bytes(target)) != row["sha256"]:
            fail("MODULE_REHASH", path)
        permitted = False
        try:
            target.relative_to(runtime_root)
            permitted = True
        except ValueError:
            permitted = any(str(target).startswith(str(prefix)) for prefix in system_prefixes)
        if not permitted and extra_module_root is not None:
            try:
                target.relative_to(Path(extra_module_root).resolve())
                permitted = True
            except ValueError:
                permitted = False
        if not permitted:
            fail("MODULE_UNSEALED", path)
    for row in value["native_ledger"]:
        if row["sha256"] is None:
            fail("NATIVE_UNHASHED", row)


def mask_process_fields(value):
    if isinstance(value, dict):
        return {key: mask_process_fields(child) for key, child in sorted(value.items()) if key not in MASK_FIELDS}
    if isinstance(value, list):
        return [mask_process_fields(child) for child in value]
    return value


def compare_producers(normal, optimized):
    if canonical_bytes(mask_process_fields(normal)) != canonical_bytes(mask_process_fields(optimized)):
        fail("PRODUCER_SEMANTIC_DRIFT", "normal/optimized")
    checks = normal["checks"]
    fixtures = normal["fixtures"]
    if len(checks) != EXPECTED_IDS or len(fixtures) != EXPECTED_FIXTURES:
        fail("OUTPUT_COUNTS", {"checks": len(checks), "fixtures": len(fixtures)})
    ids = [row.get("check_id") for row in checks]
    if len(ids) != len(set(ids)):
        fail("OUTPUT_DUPLICATE_CHECK", ids)
    structural = sum(row.get("execution_class") == "STRUCTURAL" for row in checks)
    gated = sum(row.get("execution_class") == "GATED-EXECUTION" for row in checks)
    if (structural, gated) != (EXPECTED_STRUCTURAL, EXPECTED_GATED):
        fail("OUTPUT_CLASS_COUNTS", (structural, gated))
    for row in checks:
        if row.get("execution_class") == "GATED-EXECUTION":
            if row.get("status") != "NOT_RUN_GATE" or row.get("procedure_started") is not False:
                fail("GATE_DISCIPLINE", row.get("check_id"))
    fixture_fields = {
        "deterministic_procedure", "execution_class", "expected_verdict_fields",
        "fixture_id", "fixture_spec_sha256", "input_root_sha256", "mutation_ids",
        "observed_evidence_sha256s", "observed_verdict_fields", "prerequisites",
        "primary_check_ids", "procedure_started", "reason", "required_gate",
        "source", "status",
    }
    for row in fixtures:
        exact_keys(row, fixture_fields, f"fixture row {row.get('fixture_id')}")
        unexpected = set(row["observed_verdict_fields"]) - set(row["expected_verdict_fields"])
        if unexpected:
            fail("FIXTURE_QUARANTINE", {"fixture_id": row["fixture_id"], "unexpected": sorted(unexpected)})
        if row["execution_class"] == "GATED-EXECUTION":
            if row["status"] != "NOT_RUN_GATE" or row["procedure_started"] is not False:
                fail("FIXTURE_GATE_DISCIPLINE", row["fixture_id"])
    return {
        "equal_after_mask": True,
        "mask": sorted(MASK_FIELDS),
        "normal_semantic_sha256": sha256_bytes(canonical_bytes(mask_process_fields(normal))),
        "optimized_semantic_sha256": sha256_bytes(canonical_bytes(mask_process_fields(optimized))),
    }


def parse_sidecar(path):
    text = read_bytes(path).decode("utf-8").strip()
    match = re.fullmatch(r"([0-9a-f]{64})(?:\s+.+)?", text)
    if match is None:
        fail("SIDECAR_FORMAT", str(path))
    return match.group(1)


def validate_verifier_manifest(path, expected, expected_output, expected_receipt):
    base = Path(path).resolve().parent
    sidecar = Path(str(path) + ".seal.sha256")
    if not sidecar.is_file():
        fail("VERIFIER_SIDECAR", str(sidecar))
    stated = parse_sidecar(sidecar)
    data = verify_bytes(path, stated)
    if canonical_bytes(strict_json(data, "verifier manifest")) != data:
        fail("VERIFIER_MANIFEST_NOT_CANONICAL", str(path))
    value = strict_json(data, "verifier manifest")
    top_fields = {
        "argv", "entry_point", "exit_contract", "input_roots", "optimize",
        "output_path", "receipt_authoritative", "receipt_path", "schema",
        "stdout_discipline", "verifier_root_sha256",
    }
    exact_keys(value, top_fields, "verifier manifest")
    if value["schema"] != "rd22.verifier-manifest.v001":
        fail("VERIFIER_MANIFEST", value.get("schema"))
    if not isinstance(value["verifier_root_sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", value["verifier_root_sha256"]) is None:
        fail("VERIFIER_ROOT", value["verifier_root_sha256"])
    if not isinstance(value["entry_point"], str) or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*", value["entry_point"]) is None:
        fail("VERIFIER_ENTRY_POINT", value["entry_point"])
    if not isinstance(value["argv"], list) or any(not isinstance(item, str) for item in value["argv"]):
        fail("VERIFIER_ARGV", value["argv"])
    if not isinstance(value["optimize"], bool):
        fail("VERIFIER_OPTIMIZE", value["optimize"])
    exact_keys(value["input_roots"], {"evidence_root_sha256", "ledger_sha256", "runtime_gate_sha256", "runtime_snapshot_sha256", "spec_sha256"}, "verifier input_roots")
    for field, wanted in expected.items():
        if value["input_roots"].get(field) != wanted:
            fail("VERIFIER_INPUT_ROOT", {"field": field, "expected": wanted, "actual": value["input_roots"].get(field)})
    if not isinstance(value["input_roots"]["ledger_sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", value["input_roots"]["ledger_sha256"]) is None:
        fail("VERIFIER_LEDGER_ROOT", value["input_roots"]["ledger_sha256"])
    exact_keys(value["stdout_discipline"], {"format", "lines", "other_output_permitted"}, "verifier stdout_discipline")
    if value["stdout_discipline"] != {"format": "canonical-json", "lines": 1, "other_output_permitted": False}:
        fail("VERIFIER_STDOUT_CONTRACT", value["stdout_discipline"])
    exact_keys(value["exit_contract"], {"fail_closed", "faults_found", "verified"}, "verifier exit_contract")
    if value["exit_contract"] != {"fail_closed": 2, "faults_found": 1, "verified": 0}:
        fail("VERIFIER_EXIT_CONTRACT", value["exit_contract"])
    if value["receipt_authoritative"] is not False:
        fail("VERIFIER_RECEIPT_AUTHORITY", value["receipt_authoritative"])
    declared_output = Path(value["output_path"])
    declared_receipt = Path(value["receipt_path"])
    if not declared_output.is_absolute():
        declared_output = base / declared_output
    if not declared_receipt.is_absolute():
        declared_receipt = base / declared_receipt
    if declared_output.resolve() != Path(expected_output).resolve() or declared_receipt.resolve() != Path(expected_receipt).resolve():
        fail("VERIFIER_OUTPUT_CONTRACT", {"output": value["output_path"], "receipt": value["receipt_path"]})
    ledger_matches = []
    for token in value["argv"]:
        candidate = Path(token)
        if not candidate.is_absolute():
            candidate = base / candidate
        if candidate.is_file() and sha256_bytes(read_bytes(candidate)) == value["input_roots"]["ledger_sha256"]:
            ledger_matches.append(str(candidate.resolve()))
    if len(set(ledger_matches)) != 1:
        fail("VERIFIER_LEDGER_INPUT", ledger_matches)
    return value, stated, base


def verifier_stdout(data, expected_verdict, verifier_root, runtime):
    if data.count(b"\n") != 1 or not data.endswith(b"\n"):
        fail("VERIFIER_STDOUT_LINES", data.decode("utf-8", errors="replace")[-4000:])
    value = strict_json(data, "verifier stdout")
    if canonical_bytes(value) != data:
        fail("VERIFIER_STDOUT_CANONICAL", "one canonical JSON line required")
    fields = {
        "authority_firewall", "authorization_sha256", "census", "checks_replayed",
        "findings", "independence", "producer_comparison", "runtime_subject",
        "schema", "spec_sha256", "terminal_content_sha256", "verdict",
        "verifier_sha256",
    }
    exact_keys(value, fields, "verifier output")
    if value["schema"] != "gravacle.a35.verifier-verdict.v1" or value["verdict"] != expected_verdict:
        fail("VERIFIER_VERDICT", value.get("verdict"))
    if value["authorization_sha256"] != AUTHORIZATION_SHA256 or value["spec_sha256"] != SPEC_SHA256:
        fail("VERIFIER_AUTHORITY_PIN", "authorization/spec")
    if value["verifier_sha256"] != verifier_root:
        fail("VERIFIER_SELF_PIN", value["verifier_sha256"])
    exact_keys(value["independence"], {"expectations_source", "producer_code_imported"}, "verifier independence")
    if value["independence"]["producer_code_imported"] is not False:
        fail("VERIFIER_INDEPENDENCE", value["independence"])
    exact_keys(value["runtime_subject"], {"gate_sha256", "snapshot_sha256", "trust_root"}, "verifier runtime_subject")
    expected_runtime = {"gate_sha256": RUNTIME_GATE_SHA256, "snapshot_sha256": RUNTIME_SNAPSHOT_SHA256, "trust_root": trust_hash(runtime["native_system_trust_root"])}
    if value["runtime_subject"] != expected_runtime:
        fail("VERIFIER_RUNTIME_PIN", value["runtime_subject"])
    firewall = value["authority_firewall"]
    for field in ("CORE_RESULT_SEAL", "FINAL_CLAIM_SEAL", "SPEC_SEAL", "alpha_computed", "kappa_record_computed", "proof_authorized"):
        if firewall.get(field) is not False:
            fail("VERIFIER_FIREWALL", field)
    if expected_verdict == "VERIFIED" and value["findings"]:
        fail("VERIFIER_FINDINGS_ON_SUCCESS", value["findings"])
    return value


def run_verifier_process(command, cwd):
    try:
        return subprocess.run(command, check=False, capture_output=True, env={}, cwd=str(cwd))
    except OSError as exc:
        fail("VERIFIER_LAUNCH", str(exc))


def child_record(manifest_sha, target_sha, optimize, out_data, receipt_data, receipt_value, trust_before, trust_after):
    return {
        "manifest_sha256": manifest_sha,
        "module_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["module_ledger"])),
        "native_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["native_ledger"])),
        "open_event_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["open_event_ledger"])),
        "process_event_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["process_event_ledger"])),
        "network_event_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["network_event_ledger"])),
        "mutation_event_ledger_sha256": sha256_bytes(canonical_bytes(receipt_value["mutation_event_ledger"])),
        "optimize": optimize,
        "output_sha256": sha256_bytes(out_data),
        "receipt_authoritative": False,
        "receipt_sha256": sha256_bytes(receipt_data),
        "runtime_after_sha256": trust_hash(trust_after),
        "runtime_before_sha256": trust_hash(trust_before),
        "target_sha256": target_sha,
    }


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--package-root", required=True)
    parser.add_argument("--program-root", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--normal-manifest", required=True)
    parser.add_argument("--normal-manifest-sha256", required=True)
    parser.add_argument("--optimized-manifest", required=True)
    parser.add_argument("--optimized-manifest-sha256", required=True)
    parser.add_argument("--verifier-manifest", required=True)
    parser.add_argument("--run-root", required=True)
    return parser.parse_args()


def main():
    if sys.flags.isolated != 1 or sys.flags.no_site != 1 or sys.flags.dont_write_bytecode != 1 or sys.flags.optimize != 0:
        fail("R0_FLAGS", repr(sys.flags))
    args = parse_args()
    package_root = Path(args.package_root).resolve()
    program_root = Path(args.program_root).resolve()
    run_root = Path(args.run_root).resolve()
    if not package_root.is_dir() or not program_root.is_dir() or not run_root.is_dir() or run_root.is_symlink():
        fail("R0_ROOT", "missing or symlink root")
    normal_manifest, normal_manifest_data = parse_manifest(args.normal_manifest, args.normal_manifest_sha256, "normal")
    optimized_manifest, optimized_manifest_data = parse_manifest(args.optimized_manifest, args.optimized_manifest_sha256, "optimized")
    if normal_manifest["package_files"] != optimized_manifest["package_files"]:
        fail("R1_PACKAGE_DRIFT", "normal/optimized")
    for field in ("branch_outcome", "check_ids", "check_map_sha256", "evidence_manifest_sha256", "external_inputs", "fixture_ids", "fixture_manifest_sha256", "runtime_subject", "specification_sha256", "subject_lineage_root"):
        if normal_manifest[field] != optimized_manifest[field]:
            fail("R1_MANIFEST_DRIFT", field)
    if normal_manifest["specification_sha256"] != SPEC_SHA256:
        fail("R1_SPEC", normal_manifest["specification_sha256"])
    if len(normal_manifest["check_ids"]) != EXPECTED_IDS or len(normal_manifest["fixture_ids"]) != EXPECTED_FIXTURES:
        fail("R1_COUNTS", "IDs")
    package = verify_package_inventory(package_root, normal_manifest)
    parent_data = read_bytes(Path(__file__).resolve())
    if sha256_bytes(parent_data) != normal_manifest_file_hash(normal_manifest, "parent.py"):
        fail("R0_SELF_HASH", str(Path(__file__).resolve()))
    no_python_check_nodes(parent_data, "parent.py")
    no_python_check_nodes(package["producer.py"][1], "producer.py")
    verify_bytes(args.authorization, AUTHORIZATION_SHA256)
    verify_external_inputs(program_root, args.authorization, normal_manifest)
    runtime_snapshot_path = external_path(program_root, normal_manifest, "runtime_snapshot")
    runtime_gate_path = external_path(program_root, normal_manifest, "runtime_gate")
    runtime = validate_runtime(read_bytes(runtime_snapshot_path), read_bytes(runtime_gate_path))
    runtime_subject = normal_manifest["runtime_subject"]
    exact_keys(runtime_subject, {"gate_sha256", "snapshot_sha256", "trust_root"}, "runtime subject")
    if runtime_subject["snapshot_sha256"] != RUNTIME_SNAPSHOT_SHA256 or runtime_subject["gate_sha256"] != RUNTIME_GATE_SHA256 or runtime_subject["trust_root"] != runtime["native_system_trust_root"]:
        fail("RUNTIME_SUBJECT_AMBIGUOUS", runtime_subject)
    check_map_path = package["checks/check_map.json"][0]
    fixture_path = package["fixtures/fixture_manifest.json"][0]
    evidence_path = package["inputs/structural_evidence_manifest.json"][0]
    producer_path = package["producer.py"][0]
    producer_sha = normal_manifest_file_hash(normal_manifest, "producer.py")
    pycache_normal = package_root / "pycache" / "normal"
    pycache_optimized = package_root / "pycache" / "optimized"
    pycache_verifier = package_root / "pycache" / "verifier"
    for directory in (pycache_normal, pycache_optimized, pycache_verifier):
        ensure_empty_directory(directory)
    normal_output = run_root / "normal.output.json"
    normal_receipt = run_root / "normal.receipt.json"
    optimized_output = run_root / "optimized.output.json"
    optimized_receipt = run_root / "optimized.receipt.json"
    verifier_out = run_root / "verifier.output.json"
    verifier_receipt_path = run_root / "verifier.receipt.json"
    terminal_path = run_root / "terminal.ledger.json"
    ensure_absent([normal_output, normal_receipt, optimized_output, optimized_receipt, verifier_out, verifier_receipt_path, terminal_path])
    verifier_expected_roots = {
        "evidence_root_sha256": normal_manifest["evidence_manifest_sha256"],
        "runtime_gate_sha256": RUNTIME_GATE_SHA256,
        "runtime_snapshot_sha256": RUNTIME_SNAPSHOT_SHA256,
        "spec_sha256": SPEC_SHA256,
    }
    verifier_manifest, verifier_manifest_sha, verifier_base = validate_verifier_manifest(
        args.verifier_manifest,
        verifier_expected_roots,
        verifier_out,
        verifier_receipt_path,
    )
    verifier_root = verifier_manifest["verifier_root_sha256"]
    python = runtime["python_executable"]
    common = [
        "--check-map", str(check_map_path), "--check-map-sha256", normal_manifest["check_map_sha256"],
        "--fixtures", str(fixture_path), "--fixtures-sha256", normal_manifest["fixture_manifest_sha256"],
        "--evidence", str(evidence_path), "--evidence-sha256", normal_manifest["evidence_manifest_sha256"],
    ]
    t0 = trust_snapshot(runtime)
    normal_command = [python, "-I", "-S", "-B", str(producer_path), "--manifest", str(Path(args.normal_manifest).resolve()), "--manifest-sha256", args.normal_manifest_sha256] + common + ["--output", str(normal_output), "--receipt", str(normal_receipt)]
    run_child(normal_command, "normal")
    t1 = trust_snapshot(runtime)
    if t1 != t0:
        fail("R4_TRUST", "T1")
    optimized_command = [python, "-I", "-S", "-B", "-O", str(producer_path), "--manifest", str(Path(args.optimized_manifest).resolve()), "--manifest-sha256", args.optimized_manifest_sha256] + common + ["--output", str(optimized_output), "--receipt", str(optimized_receipt)]
    run_child(optimized_command, "optimized")
    t2 = trust_snapshot(runtime)
    if t2 != t1:
        fail("R6_TRUST", "T2")
    normal_value, normal_data = output(normal_output)
    optimized_value, optimized_data = output(optimized_output)
    normal_receipt_value, normal_receipt_data = receipt(normal_receipt)
    optimized_receipt_value, optimized_receipt_data = receipt(optimized_receipt)
    classify_receipt(normal_receipt_value, args.normal_manifest_sha256, producer_sha, 0, sha256_bytes(normal_data), normal_output, normal_receipt, runtime)
    classify_receipt(optimized_receipt_value, args.optimized_manifest_sha256, producer_sha, 1, sha256_bytes(optimized_data), optimized_output, optimized_receipt, runtime)
    comparison = compare_producers(normal_value, optimized_value)
    t3 = trust_snapshot(runtime)
    verifier_command = [python, "-I", "-S", "-B"]
    if verifier_manifest["optimize"]:
        verifier_command.append("-O")
    verifier_command.extend(["-m", verifier_manifest["entry_point"]])
    verifier_command.extend(verifier_manifest["argv"])
    verifier_process = run_verifier_process(verifier_command, verifier_base)
    t4 = trust_snapshot(runtime)
    if t4 != t3 or t4 != t2:
        fail("R9_TRUST", "T4")
    if verifier_process.returncode == verifier_manifest["exit_contract"]["fail_closed"]:
        detail = verifier_process.stderr.decode("utf-8", errors="replace")[-4000:]
        fail("R9_VERIFIER_FAIL_CLOSED_EXIT_2", detail)
    if verifier_process.returncode not in {verifier_manifest["exit_contract"]["verified"], verifier_manifest["exit_contract"]["faults_found"]}:
        fail("R9_VERIFIER_UNDECLARED_EXIT", verifier_process.returncode)
    expected_verdict = "VERIFIED" if verifier_process.returncode == verifier_manifest["exit_contract"]["verified"] else "FAIL"
    verifier_data = verifier_process.stdout
    verifier_value = verifier_stdout(verifier_data, expected_verdict, verifier_root, runtime)
    exclusive_write(verifier_out, verifier_data)
    if verifier_process.returncode == verifier_manifest["exit_contract"]["faults_found"]:
        fail("R9_VERIFIER_FAULTS_FOUND_EXIT_1", verifier_value["findings"])
    verifier_receipt_value, verifier_receipt_data = receipt(verifier_receipt_path)
    classify_receipt(verifier_receipt_value, verifier_manifest_sha, verifier_root, verifier_manifest["optimize"], sha256_bytes(verifier_data), verifier_out, verifier_receipt_path, runtime, verifier_base, True)
    children = [
        child_record(args.normal_manifest_sha256, producer_sha, 0, normal_data, normal_receipt_data, normal_receipt_value, t0, t1),
        child_record(args.optimized_manifest_sha256, producer_sha, 1, optimized_data, optimized_receipt_data, optimized_receipt_value, t1, t2),
        child_record(verifier_manifest_sha, verifier_root, verifier_manifest["optimize"], verifier_data, verifier_receipt_data, verifier_receipt_value, t3, t4),
    ]
    terminal = {
        "authorization": {"rd22_sha256": AUTHORIZATION_SHA256, "valid": True},
        "authority_firewall": normal_value["authority_firewall"],
        "check_map_sha256": normal_manifest["check_map_sha256"],
        "checks": normal_value["checks"],
        "children": children,
        "fixture_manifest_sha256": normal_manifest["fixture_manifest_sha256"],
        "fixtures": normal_value["fixtures"],
        "producer_comparison": comparison,
        "runner_sha256": normal_manifest_file_hash(normal_manifest, "parent.py"),
        "runtime_subject": runtime_subject,
        "schema": "rd22.terminal-ledger.v001",
        "scope": normal_value["scope"],
        "spec_sha256": SPEC_SHA256,
        "subject_lineage": {"root_sha256": normal_manifest["subject_lineage_root"]},
        "summary": normal_value["summary"],
        "terminal_content_sha256": "",
        "trust_snapshots": {"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t4},
        "verifier_sha256": verifier_root,
    }
    terminal["terminal_content_sha256"] = sha256_bytes(canonical_bytes(terminal))
    exclusive_write(terminal_path, canonical_bytes(terminal))
    return 0


def normal_manifest_file_hash(manifest, relative):
    matches = [row["sha256"] for row in manifest["package_files"] if row["relative_path"] == relative]
    if len(matches) != 1:
        fail("MANIFEST_FILE_HASH", relative)
    return matches[0]


def external_path(program_root, manifest, kind):
    matches = [row for row in manifest["external_inputs"] if row["kind"] == kind]
    if len(matches) != 1:
        fail("EXTERNAL_PATH", kind)
    return safe_resolve(program_root, matches[0]["relative_path"])


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ParentFailure as exc:
        sys.stderr.write(f"RD22_PARENT_FAIL {exc}\n")
        raise SystemExit(2)
