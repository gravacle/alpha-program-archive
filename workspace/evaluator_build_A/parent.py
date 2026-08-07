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
UNBOUND_ROOT_SENTINEL = "0" * 64
VERIFIER_SUBSTITUTION_TOKENS = {
    "${EVIDENCE_DIR}",
    "${LEDGER_PATH}",
    "${LEDGER_SHA256}",
    "${RUNTIME_GATE_PATH}",
    "${RUNTIME_SNAPSHOT_PATH}",
    "${SPEC_PATH}",
}
PATH_IDENTITY_SITES = (
    "R0_ROOTS",
    "SUBJECT_EVIDENCE_SAFE_RESOLVE",
    "RUNTIME_INTERPRETER",
    "VERIFIER_RUN_OUTPUTS",
    "POST_PRODUCTION_LEDGER",
    "RECEIPT_WRITE_MUTATION",
    "MODULE_NATIVE_LOADS",
    "OPEN_EVENTS",
)


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
    return text.encode("utf-8")


def exact_keys(value, keys, label):
    if not isinstance(value, dict):
        fail("SCHEMA_TYPE", f"{label} not object")
    actual = set(value)
    wanted = set(keys)
    if actual != wanted:
        fail("SCHEMA_FIELDS", f"{label}: missing={sorted(wanted-actual)}, extra={sorted(actual-wanted)}")


def content_root(entries, label):
    if not isinstance(entries, list):
        fail("CONTENT_ROOT_ROWS", f"{label}: not list")
    records = []
    seen = set()
    for row in entries:
        exact_keys(row, {"byte_length", "relative_path", "sha256"}, f"{label} row")
        relative = row["relative_path"]
        if not isinstance(relative, str) or not relative or re.fullmatch(r"[^/\\\x00]+", relative) is None:
            fail("CONTENT_ROOT_PATH", f"{label}: {relative!r}")
        if relative in seen:
            fail("CONTENT_ROOT_DUPLICATE", f"{label}: {relative}")
        seen.add(relative)
        length = row["byte_length"]
        digest = row["sha256"]
        if not isinstance(length, int) or isinstance(length, bool) or length < 0:
            fail("CONTENT_ROOT_LENGTH", f"{label}: {relative}")
        if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
            fail("CONTENT_ROOT_DIGEST", f"{label}: {relative}")
        records.append(f"{relative}\0{length}\0{digest}\n")
    payload = b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8")
    return sha256_bytes(payload)


def lexical_absolute(path):
    """Return an absolute normalized spelling without resolving aliases."""
    return Path(os.path.abspath(os.fspath(path)))


def real_path(path):
    """Return the filesystem identity used for every path comparison."""
    return Path(os.path.realpath(os.fspath(lexical_absolute(path))))


def path_within(path, root):
    target = real_path(path)
    base = real_path(root)
    try:
        target.relative_to(base)
        return True
    except ValueError:
        return False


def add_allowlist_entry(allowlist, declared_path, expected_sha256, source):
    if not isinstance(expected_sha256, str) or re.fullmatch(r"[0-9a-f]{64}", expected_sha256) is None:
        fail("ALLOWLIST_DIGEST", f"{source}: {expected_sha256!r}")
    declared = lexical_absolute(declared_path)
    canonical = real_path(declared)
    key = str(canonical)
    row = {
        "declared_path": str(declared),
        "realpath": key,
        "sha256": expected_sha256,
        "source": source,
    }
    prior = allowlist.get(key)
    if prior is not None and prior["sha256"] != expected_sha256:
        fail("ALLOWLIST_COLLISION", {"prior": prior, "new": row})
    if prior is None:
        allowlist[key] = row
    return canonical


def alias_observation(child, surface, declared_path, observed_path, digest):
    declared = lexical_absolute(declared_path)
    observed = lexical_absolute(observed_path)
    declared_real = real_path(declared)
    observed_real = real_path(observed)
    if declared_real != observed_real:
        fail("PATH_IDENTITY", {"declared": str(declared), "observed": str(observed)})
    if str(declared) == str(observed):
        return None
    return {
        "child": child,
        "declared_path": str(declared),
        "observed_path": str(observed),
        "realpath": str(declared_real),
        "sha256": digest,
        "surface": surface,
    }


def safe_resolve(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        fail("RELATIVE_PATH", repr(relative))
    declared_base = lexical_absolute(root)
    declared_target = lexical_absolute(declared_base / relative)
    base = real_path(declared_base)
    target = real_path(declared_target)
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
    allowlist = {}
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
        add_allowlist_entry(allowlist, lexical_absolute(package_root) / relative, row["sha256"], f"package:{relative}")
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
    return values, allowlist


def validate_evidence_manifest(data, package):
    value = strict_json(data, "structural evidence manifest")
    if canonical_bytes(value) != data:
        fail("EVIDENCE_MANIFEST_NOT_CANONICAL", "structural evidence manifest")
    exact_keys(
        value,
        {"check_records", "declared_root", "fixture_records", "payload_inventory", "schema", "subject_lineage_root"},
        "structural evidence manifest",
    )
    if value["schema"] != "rd22.structural-evidence-manifest.v001":
        fail("EVIDENCE_MANIFEST_SCHEMA", value["schema"])
    rows = value["payload_inventory"]
    if not isinstance(rows, list) or rows != sorted(rows, key=lambda row: row.get("relative_path", "") if isinstance(row, dict) else ""):
        fail("EVIDENCE_INVENTORY_ORDER", "not canonical relative_path order")
    actual_root = content_root(rows, "evidence payload inventory")
    if value["declared_root"] != actual_root:
        fail("EVIDENCE_DECLARED_ROOT", {"declared": value["declared_root"], "actual": actual_root})
    prefix = "inputs/evidence/"
    supplied = {}
    for relative, (_, payload) in package.items():
        if not relative.startswith(prefix):
            continue
        name = relative[len(prefix):]
        if not name or "/" in name or name in supplied:
            fail("EVIDENCE_PACKAGE_PATH", relative)
        supplied[name] = payload
    declared_names = {row["relative_path"] for row in rows}
    if declared_names != set(supplied):
        fail("EVIDENCE_PAYLOAD_CENSUS", {"declared": sorted(declared_names), "supplied": sorted(supplied)})
    for row in rows:
        payload = supplied[row["relative_path"]]
        if len(payload) != row["byte_length"] or sha256_bytes(payload) != row["sha256"]:
            fail("EVIDENCE_PAYLOAD_ROW", row["relative_path"])
    return value["declared_root"]


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
            target = real_path(authorization_path)
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
    python_path = real_path(snapshot["python_executable"])
    verify_bytes(python_path, snapshot["python_executable_sha256"])
    if real_path(sys.executable) != python_path:
        fail("RUNTIME_INTERPRETER", f"{sys.executable} != {python_path}")
    if "fresh" not in gate_data.decode("utf-8").casefold():
        fail("RUNTIME_GATE_CONTENT", "fresh missing")
    return snapshot


def runtime_allowlist(runtime):
    rows = runtime["python_runtime_files"]
    if not isinstance(rows, dict):
        fail("RUNTIME_FILE_INVENTORY", "not object")
    allowlist = {}
    declared_root = lexical_absolute(runtime["python_runtime_root"])
    for relative, digest in rows.items():
        if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
            fail("RUNTIME_FILE_PATH", repr(relative))
        target = safe_resolve(declared_root, relative)
        add_allowlist_entry(allowlist, declared_root / relative, digest, f"runtime:{relative}")
        if str(target) not in allowlist:
            fail("RUNTIME_ALLOWLIST_IDENTITY", relative)
    return allowlist


def trust_hash(value):
    return sha256_bytes(canonical_bytes(value))


def trust_root_digest(native_system_trust_root):
    digest = trust_hash(native_system_trust_root)
    if re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        fail("TRUST_ROOT_DIGEST", digest)
    return digest


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
    expected_digest = trust_root_digest(runtime["native_system_trust_root"])
    observed_digest = trust_root_digest(observed)
    if observed_digest != expected_digest:
        fail("TRUST_DRIFT", {"expected_sha256": expected_digest, "observed_sha256": observed_digest})
    return observed_digest


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


def classify_receipt(
    value,
    expected_manifest_sha,
    expected_target_sha,
    optimize,
    output_sha,
    output_path,
    receipt_path,
    runtime,
    runtime_files,
    package_files,
    child_manifest_path,
    child,
    extra_files=None,
    stdout_output=False,
):
    if value["manifest_sha256"] != expected_manifest_sha or value["target_sha256"] != expected_target_sha:
        fail("RECEIPT_PIN", optimize)
    if value["optimize"] != optimize or value["output_sha256"] != output_sha:
        fail("RECEIPT_OUTPUT", optimize)
    if value["process_event_ledger"] or value["network_event_ledger"] or value["environment_event_ledger"]:
        fail("RECEIPT_FORBIDDEN_EVENT", optimize)
    allowed = {}
    for source in (runtime_files, package_files, extra_files or {}):
        for entry in source.values():
            add_allowlist_entry(allowed, entry["declared_path"], entry["sha256"], entry["source"])
    add_allowlist_entry(allowed, child_manifest_path, expected_manifest_sha, "child-manifest")
    add_allowlist_entry(allowed, output_path, output_sha, "child-output")
    receipt_sha = sha256_bytes(read_bytes(real_path(receipt_path)))
    add_allowlist_entry(allowed, receipt_path, receipt_sha, "child-receipt")
    alias_rows = []

    def record_alias(surface, entry, observed, digest):
        row = alias_observation(child, surface, entry["declared_path"], observed, digest)
        if row is not None:
            alias_rows.append(row)

    def verify_observed_file(observed, claimed_digest, surface):
        target = real_path(observed)
        key = str(target)
        entry = allowed.get(key)
        actual = sha256_bytes(read_bytes(target))
        if claimed_digest is not None and claimed_digest != actual:
            fail(f"{surface}_REHASH", {"path": str(observed), "claimed": claimed_digest, "actual": actual})
        if entry is None:
            system_roots = (Path("/System/Library"), Path("/usr/lib"))
            if not any(path_within(target, root) for root in system_roots):
                fail(f"{surface}_UNSEALED", str(observed))
            return actual
        if entry["sha256"] != actual:
            fail(f"{surface}_ALLOWLIST_DIGEST", {"entry": entry, "actual": actual})
        record_alias(surface.lower(), entry, observed, actual)
        return actual

    expected_writes = []
    if not stdout_output:
        expected_writes.append((output_path, output_sha, "output"))
    expected_writes.append((receipt_path, receipt_sha, "receipt"))

    def verify_write_rows(rows, label):
        if not isinstance(rows, list) or len(rows) != len(expected_writes):
            fail(label, {"expected_count": len(expected_writes), "actual": rows})
        for row, (declared, digest, name) in zip(rows, expected_writes):
            exact_keys(row, {"operation", "path"}, f"{label} row")
            if row["operation"] != "exclusive_create" or not isinstance(row["path"], str):
                fail(label, row)
            if real_path(row["path"]) != real_path(declared):
                fail(label, {"expected": str(declared), "actual": row["path"]})
            entry = allowed[str(real_path(declared))]
            if sha256_bytes(read_bytes(real_path(row["path"]))) != digest:
                fail(f"{label}_DIGEST", name)
            record_alias(label.lower(), entry, row["path"], digest)

    verify_write_rows(value["write_event_ledger"], "RECEIPT_WRITE_SET")
    verify_write_rows(value["mutation_event_ledger"], "RECEIPT_MUTATION_SET")
    for row in value["module_ledger"]:
        exact_keys(row, {"kind", "module", "path", "sha256"}, "module row")
        path = row["path"]
        if path is None:
            if row["kind"] != "builtin_or_frozen" or row["sha256"] is not None:
                fail("MODULE_ORIGIN", row)
            continue
        if not isinstance(path, str) or not isinstance(row["sha256"], str):
            fail("MODULE_ROW", row)
        target = real_path(path)
        if target.suffix == ".pyc":
            fail("BYTECODE_MODULE", path)
        verify_observed_file(path, row["sha256"], "MODULE")
    for row in value["native_ledger"]:
        exact_keys(row, {"kind", "module", "path", "sha256"}, "native row")
        if row["kind"] != "native" or not isinstance(row["path"], str) or not isinstance(row["sha256"], str):
            fail("NATIVE_UNHASHED", row)
        verify_observed_file(row["path"], row["sha256"], "NATIVE")
    for row in value["open_event_ledger"]:
        exact_keys(row, {"args", "event"}, "open row")
        if row["event"] != "open" or not isinstance(row["args"], list) or not row["args"]:
            fail("OPEN_EVENT_ROW", row)
        opened = row["args"][0]
        if isinstance(opened, str):
            verify_observed_file(opened, None, "OPEN")
        elif not isinstance(opened, int) or isinstance(opened, bool):
            fail("OPEN_EVENT_PATH", row)
    unique = {canonical_bytes(row): row for row in alias_rows}
    return [unique[key] for key in sorted(unique)]


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


def verifier_entry_target(manifest, verifier_base, verifier_files):
    entry = manifest.get("entry_point")
    pattern = r"[A-Za-z_][A-Za-z0-9_]*(?:/[A-Za-z_][A-Za-z0-9_]*)*\.py"
    if not isinstance(entry, str) or re.fullmatch(pattern, entry) is None:
        fail("VERIFIER_ENTRY_POINT", entry)
    target = safe_resolve(verifier_base, entry)
    covered = verifier_files.get(str(target))
    if covered is None:
        fail("VERIFIER_ENTRY_UNCOVERED", {"entry_point": entry, "realpath": str(target)})
    verify_bytes(target, covered["sha256"])
    return target


def validate_verifier_manifest(path, expected, run_root, expected_output, expected_receipt):
    manifest_path = lexical_absolute(path)
    manifest_base_declared = manifest_path.parent
    manifest_base = real_path(manifest_base_declared)
    run_base = real_path(run_root)
    sidecar = Path(str(manifest_path) + ".seal.sha256")
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
    verifier_source_declared = manifest_base_declared / "verifier"
    verifier_source = real_path(verifier_source_declared)
    if not verifier_source.is_dir():
        fail("VERIFIER_SOURCE_ROOT", str(verifier_source_declared))
    verifier_files = {}
    entry = value.get("entry_point")
    entry_pattern = r"[A-Za-z_][A-Za-z0-9_]*(?:/[A-Za-z_][A-Za-z0-9_]*)*\.py"
    if not isinstance(entry, str) or re.fullmatch(entry_pattern, entry) is None:
        fail("VERIFIER_ENTRY_POINT", entry)
    entry_target = safe_resolve(manifest_base_declared, entry)
    if not entry_target.is_file():
        fail("VERIFIER_ENTRY_FILE", entry)
    source_members = {
        entry: (manifest_base_declared / entry, entry_target),
    }
    for source_path in sorted(verifier_source.iterdir(), key=lambda item: item.name):
        if not source_path.is_file() or source_path.suffix != ".py":
            continue
        relative = f"verifier/{source_path.name}"
        source_members[relative] = (verifier_source_declared / source_path.name, source_path)
    source_digests = []
    for relative in sorted(source_members):
        declared_source, source_path = source_members[relative]
        target = safe_resolve(manifest_base_declared, relative)
        if target != real_path(source_path):
            fail("VERIFIER_ROOT_MEMBER_IDENTITY", relative)
        digest = sha256_bytes(read_bytes(source_path))
        source_digests.append(digest)
        add_allowlist_entry(verifier_files, declared_source, digest, f"verifier:{relative}")
    computed_verifier_root = sha256_bytes("".join(source_digests).encode("utf-8"))
    if not source_digests or computed_verifier_root != value["verifier_root_sha256"]:
        fail("VERIFIER_ROOT_DIGEST", {"declared": value["verifier_root_sha256"], "computed": computed_verifier_root})
    verifier_entry_target(value, manifest_base_declared, verifier_files)
    if not isinstance(value["argv"], list) or any(not isinstance(item, str) for item in value["argv"]):
        fail("VERIFIER_ARGV", value["argv"])
    if not isinstance(value["optimize"], bool):
        fail("VERIFIER_OPTIMIZE", value["optimize"])
    exact_keys(value["input_roots"], {"evidence_root_sha256", "ledger_sha256", "runtime_gate_sha256", "runtime_snapshot_sha256", "spec_sha256"}, "verifier input_roots")
    for field, wanted in expected.items():
        if value["input_roots"].get(field) != wanted:
            fail("VERIFIER_INPUT_ROOT", {"field": field, "expected": wanted, "actual": value["input_roots"].get(field)})
    authored_ledger_root = value["input_roots"]["ledger_sha256"]
    if not isinstance(authored_ledger_root, str) or re.fullmatch(r"[0-9a-f]{64}", authored_ledger_root) is None:
        fail("VERIFIER_LEDGER_ROOT_FORM", authored_ledger_root)
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
    if declared_output.is_absolute() or declared_receipt.is_absolute():
        fail("VERIFIER_ABSOLUTE_RUN_PATH", {"output": value["output_path"], "receipt": value["receipt_path"]})
    declared_output = safe_resolve(run_base, value["output_path"])
    declared_receipt = safe_resolve(run_base, value["receipt_path"])
    if declared_output != real_path(expected_output) or declared_receipt != real_path(expected_receipt):
        fail("VERIFIER_OUTPUT_CONTRACT", {"output": value["output_path"], "receipt": value["receipt_path"]})
    return value, stated, manifest_base, verifier_files


def bind_verifier_launch(manifest, substitutions, ledger_path, ledger_sha256):
    if not isinstance(ledger_sha256, str) or re.fullmatch(r"[0-9a-f]{64}", ledger_sha256) is None or ledger_sha256 == UNBOUND_ROOT_SENTINEL:
        fail("VERIFIER_LEDGER_BINDING", ledger_sha256)
    if set(substitutions) != VERIFIER_SUBSTITUTION_TOKENS:
        fail("VERIFIER_SUBSTITUTION_SET", sorted(substitutions))
    if real_path(substitutions["${LEDGER_PATH}"]) != real_path(ledger_path) or substitutions["${LEDGER_SHA256}"] != ledger_sha256:
        fail("VERIFIER_LEDGER_SUBSTITUTION", substitutions)
    bound = strict_json(canonical_bytes(manifest), "verifier manifest binding copy")
    bound["input_roots"]["ledger_sha256"] = ledger_sha256
    counts = {token: 0 for token in VERIFIER_SUBSTITUTION_TOKENS}
    argv = []
    for item in bound["argv"]:
        if item in substitutions:
            counts[item] += 1
            argv.append(substitutions[item])
        else:
            argv.append(item)
    if any(counts[token] != 1 for token in counts):
        fail("VERIFIER_SUBSTITUTION_COUNT", counts)
    unresolved = [item for item in argv if isinstance(item, str) and re.search(r"\$\{[^}]+\}", item)]
    if unresolved:
        fail("VERIFIER_SUBSTITUTION_UNRESOLVED", unresolved)
    bound["argv"] = argv
    return bound


def post_production_verifier_validation(manifest, ledger_path, ledger_sha256):
    if manifest["input_roots"]["ledger_sha256"] != ledger_sha256 or ledger_sha256 == UNBOUND_ROOT_SENTINEL:
        fail("VERIFIER_LEDGER_NOT_BOUND", manifest["input_roots"]["ledger_sha256"])
    argv = manifest["argv"]
    if argv.count("--ledger") != 1 or argv.count("--ledger-sha256") != 1:
        fail("VERIFIER_LEDGER_ARGV_FLAGS", argv)
    ledger_index = argv.index("--ledger")
    digest_index = argv.index("--ledger-sha256")
    if ledger_index + 1 >= len(argv) or digest_index + 1 >= len(argv):
        fail("VERIFIER_LEDGER_ARGV_VALUE", argv)
    declared_path = Path(argv[ledger_index + 1])
    if not declared_path.is_absolute():
        fail("VERIFIER_LEDGER_PATH_NOT_ABSOLUTE", argv[ledger_index + 1])
    declared_path = real_path(declared_path)
    expected_path = real_path(ledger_path)
    if declared_path != expected_path or argv[digest_index + 1] != ledger_sha256:
        fail("VERIFIER_LEDGER_ARGV_BINDING", {"path": str(declared_path), "sha256": argv[digest_index + 1]})
    if not declared_path.is_file() or sha256_bytes(read_bytes(declared_path)) != ledger_sha256:
        fail("VERIFIER_LEDGER_INPUT", {"path": str(declared_path), "sha256": ledger_sha256})


def verifier_process_command(manifest, pinned_python, verifier_base, verifier_files):
    declared = manifest["argv"]
    prefix = ["python3"]
    if manifest["optimize"]:
        prefix.append("-O")
    launch_index = len(prefix)
    if len(declared) <= launch_index:
        fail("VERIFIER_ARGV_PREFIX", {"expected_entry": manifest["entry_point"], "actual": declared})
    launch_token = declared[launch_index]
    if launch_token in {"-c", "-m"} or launch_token.startswith("-"):
        fail("VERIFIER_ARGV_FORBIDDEN_LAUNCH_FORM", launch_token)
    prefix.append(manifest["entry_point"])
    if declared[:len(prefix)] != prefix:
        fail("VERIFIER_ARGV_PREFIX", {"expected": prefix, "actual": declared[:len(prefix)]})
    entry_target = verifier_entry_target(manifest, verifier_base, verifier_files)
    command = [pinned_python, "-I", "-S", "-B"]
    if manifest["optimize"]:
        command.append("-O")
    command.append(str(entry_target))
    command.extend(declared[len(prefix):])
    return command


def verifier_stdout(data, expected_verdict, verifier_root, runtime):
    if not data:
        fail("VERIFIER_STDOUT_EMPTY", "missing canonical JSON value")
    value = strict_json(data, "verifier stdout")
    if canonical_bytes(value) != data:
        fail("VERIFIER_STDOUT_CANONICAL", "one tight canonical JSON value required")
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
    expected_runtime = {"gate_sha256": RUNTIME_GATE_SHA256, "snapshot_sha256": RUNTIME_SNAPSHOT_SHA256, "trust_root": trust_root_digest(runtime["native_system_trust_root"])}
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
    if receipt_value["manifest_sha256"] != manifest_sha:
        fail("CHILD_RECORD_MANIFEST", {"launch": manifest_sha, "receipt": receipt_value["manifest_sha256"]})
    if any(not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None for value in (trust_before, trust_after)):
        fail("CHILD_RECORD_TRUST_DIGEST", {"before": trust_before, "after": trust_after})
    return {
        "manifest_sha256": receipt_value["manifest_sha256"],
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
        "runtime_after_sha256": trust_after,
        "runtime_before_sha256": trust_before,
        "target_sha256": target_sha,
    }


def verdict_ledger(normal_value, normal_manifest, comparison, children, trust_snapshots, verifier_root, scope):
    value = {
        "authorization": {"rd22_sha256": AUTHORIZATION_SHA256, "valid": True},
        "authority_firewall": normal_value["authority_firewall"],
        "check_map_sha256": normal_manifest["check_map_sha256"],
        "checks": normal_value["checks"],
        "children": children,
        "fixture_manifest_sha256": normal_manifest["fixture_manifest_sha256"],
        "fixtures": normal_value["fixtures"],
        "producer_comparison": comparison,
        "runner_sha256": normal_manifest_file_hash(normal_manifest, "parent.py"),
        "runtime_subject": normal_manifest["runtime_subject"],
        "schema": "rd22.terminal-ledger.v001",
        "scope": scope,
        "spec_sha256": SPEC_SHA256,
        "subject_lineage": {"root_sha256": normal_manifest["subject_lineage_root"]},
        "summary": normal_value["summary"],
        "terminal_content_sha256": "",
        "trust_snapshots": trust_snapshots,
        "verifier_sha256": verifier_root,
    }
    value["terminal_content_sha256"] = sha256_bytes(canonical_bytes(value))
    return value


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
    package_root_declared = lexical_absolute(args.package_root)
    program_root_declared = lexical_absolute(args.program_root)
    run_root_declared = lexical_absolute(args.run_root)
    package_root = real_path(package_root_declared)
    program_root = real_path(program_root_declared)
    run_root = real_path(run_root_declared)
    if not package_root.is_dir() or not program_root.is_dir() or not run_root.is_dir() or run_root_declared.is_symlink():
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
    package, package_files = verify_package_inventory(package_root_declared, normal_manifest)
    evidence_declared_root = validate_evidence_manifest(package["inputs/structural_evidence_manifest.json"][1], package)
    parent_data = read_bytes(real_path(__file__))
    if sha256_bytes(parent_data) != normal_manifest_file_hash(normal_manifest, "parent.py"):
        fail("R0_SELF_HASH", str(real_path(__file__)))
    no_python_check_nodes(parent_data, "parent.py")
    no_python_check_nodes(package["producer.py"][1], "producer.py")
    verify_bytes(args.authorization, AUTHORIZATION_SHA256)
    verify_external_inputs(program_root_declared, args.authorization, normal_manifest)
    runtime_snapshot_path = external_path(program_root_declared, normal_manifest, "runtime_snapshot")
    runtime_gate_path = external_path(program_root_declared, normal_manifest, "runtime_gate")
    specification_path = external_path(program_root_declared, normal_manifest, "specification")
    runtime = validate_runtime(read_bytes(runtime_snapshot_path), read_bytes(runtime_gate_path))
    runtime_files = runtime_allowlist(runtime)
    runtime_subject = normal_manifest["runtime_subject"]
    exact_keys(runtime_subject, {"gate_sha256", "snapshot_sha256", "trust_root"}, "runtime subject")
    authorized_trust_root = trust_root_digest(runtime["native_system_trust_root"])
    if runtime_subject["snapshot_sha256"] != RUNTIME_SNAPSHOT_SHA256 or runtime_subject["gate_sha256"] != RUNTIME_GATE_SHA256 or runtime_subject["trust_root"] != authorized_trust_root:
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
    normal_output = run_root_declared / "normal.output.json"
    normal_receipt = run_root_declared / "normal.receipt.json"
    optimized_output = run_root_declared / "optimized.output.json"
    optimized_receipt = run_root_declared / "optimized.receipt.json"
    verifier_out = run_root_declared / "verifier.output.json"
    verifier_receipt_path = run_root_declared / "verifier.receipt.json"
    producer_ledger_path = run_root_declared / "producer.ledger.json"
    bound_verifier_manifest_path = run_root_declared / "verifier.manifest.bound.json"
    terminal_path = run_root_declared / "terminal.ledger.json"
    ensure_absent([normal_output, normal_receipt, optimized_output, optimized_receipt, verifier_out, verifier_receipt_path, producer_ledger_path, bound_verifier_manifest_path, terminal_path])
    verifier_expected_roots = {
        "evidence_root_sha256": evidence_declared_root,
        "runtime_gate_sha256": RUNTIME_GATE_SHA256,
        "runtime_snapshot_sha256": RUNTIME_SNAPSHOT_SHA256,
        "spec_sha256": SPEC_SHA256,
    }
    verifier_manifest, verifier_manifest_sha, verifier_base, verifier_files = validate_verifier_manifest(
        args.verifier_manifest,
        verifier_expected_roots,
        run_root_declared,
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
    normal_command = [python, "-I", "-S", "-B", str(producer_path), "--manifest", str(real_path(args.normal_manifest)), "--manifest-sha256", args.normal_manifest_sha256] + common + ["--output", str(normal_output), "--receipt", str(normal_receipt)]
    run_child(normal_command, "normal")
    t1 = trust_snapshot(runtime)
    if t1 != t0:
        fail("R4_TRUST", "T1")
    optimized_command = [python, "-I", "-S", "-B", "-O", str(producer_path), "--manifest", str(real_path(args.optimized_manifest)), "--manifest-sha256", args.optimized_manifest_sha256] + common + ["--output", str(optimized_output), "--receipt", str(optimized_receipt)]
    run_child(optimized_command, "optimized")
    t2 = trust_snapshot(runtime)
    if t2 != t1:
        fail("R6_TRUST", "T2")
    normal_value, normal_data = output(normal_output)
    optimized_value, optimized_data = output(optimized_output)
    normal_receipt_value, normal_receipt_data = receipt(normal_receipt)
    optimized_receipt_value, optimized_receipt_data = receipt(optimized_receipt)
    normal_aliases = classify_receipt(
        normal_receipt_value, args.normal_manifest_sha256, producer_sha, 0,
        sha256_bytes(normal_data), normal_output, normal_receipt, runtime,
        runtime_files, package_files, args.normal_manifest, "normal",
    )
    optimized_aliases = classify_receipt(
        optimized_receipt_value, args.optimized_manifest_sha256, producer_sha, 1,
        sha256_bytes(optimized_data), optimized_output, optimized_receipt, runtime,
        runtime_files, package_files, args.optimized_manifest, "optimized",
    )
    comparison = compare_producers(normal_value, optimized_value)
    t3 = trust_snapshot(runtime)
    producer_children = [
        child_record(args.normal_manifest_sha256, producer_sha, 0, normal_data, normal_receipt_data, normal_receipt_value, t0, t1),
        child_record(args.optimized_manifest_sha256, producer_sha, 1, optimized_data, optimized_receipt_data, optimized_receipt_value, t1, t2),
    ]
    authored_ledger_root = verifier_manifest["input_roots"]["ledger_sha256"]
    producer_scope = dict(normal_value["scope"])
    producer_scope["path_alias_observations"] = normal_aliases + optimized_aliases
    producer_scope["verifier_ledger_binding"] = {
        "authored_ledger_sha256": authored_ledger_root,
        "binding_phase": "POST_PRODUCTION_HASH_THEN_BIND",
        "sentinel_lawful": authored_ledger_root == UNBOUND_ROOT_SENTINEL,
    }
    producer_ledger = verdict_ledger(
        normal_value,
        normal_manifest,
        comparison,
        producer_children,
        {"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t3},
        verifier_root,
        producer_scope,
    )
    producer_ledger_data = canonical_bytes(producer_ledger)
    exclusive_write(producer_ledger_path, producer_ledger_data)
    produced_ledger_sha = sha256_bytes(producer_ledger_data)
    substitutions = {
        "${EVIDENCE_DIR}": str(real_path(package_root_declared / "inputs" / "evidence")),
        "${LEDGER_PATH}": str(real_path(producer_ledger_path)),
        "${LEDGER_SHA256}": produced_ledger_sha,
        "${RUNTIME_GATE_PATH}": str(real_path(runtime_gate_path)),
        "${RUNTIME_SNAPSHOT_PATH}": str(real_path(runtime_snapshot_path)),
        "${SPEC_PATH}": str(real_path(specification_path)),
    }
    bound_verifier_manifest = bind_verifier_launch(verifier_manifest, substitutions, producer_ledger_path, produced_ledger_sha)
    post_production_verifier_validation(bound_verifier_manifest, producer_ledger_path, produced_ledger_sha)
    bound_verifier_manifest_data = canonical_bytes(bound_verifier_manifest)
    bound_verifier_manifest_sha = sha256_bytes(bound_verifier_manifest_data)
    exclusive_write(bound_verifier_manifest_path, bound_verifier_manifest_data)
    verifier_command = verifier_process_command(bound_verifier_manifest, python, verifier_base, verifier_files)
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
    add_allowlist_entry(verifier_files, specification_path, SPEC_SHA256, "verifier-input:specification")
    add_allowlist_entry(verifier_files, runtime_snapshot_path, RUNTIME_SNAPSHOT_SHA256, "verifier-input:runtime-snapshot")
    add_allowlist_entry(verifier_files, runtime_gate_path, RUNTIME_GATE_SHA256, "verifier-input:runtime-gate")
    add_allowlist_entry(verifier_files, producer_ledger_path, produced_ledger_sha, "verifier-input:producer-ledger")
    verifier_aliases = classify_receipt(
        verifier_receipt_value, bound_verifier_manifest_sha, verifier_root,
        bound_verifier_manifest["optimize"], sha256_bytes(verifier_data),
        verifier_out, verifier_receipt_path, runtime, runtime_files,
        package_files, bound_verifier_manifest_path, "verifier", verifier_files,
        True,
    )
    verifier_child = child_record(bound_verifier_manifest_sha, verifier_root, bound_verifier_manifest["optimize"], verifier_data, verifier_receipt_data, verifier_receipt_value, t3, t4)
    children = producer_children + [verifier_child]
    terminal_scope = dict(normal_value["scope"])
    terminal_scope["path_alias_observations"] = normal_aliases + optimized_aliases + verifier_aliases
    terminal_scope["verifier_ledger_binding"] = {
        "authored_ledger_sha256": authored_ledger_root,
        "authored_manifest_sha256": verifier_manifest_sha,
        "bound_ledger_sha256": produced_ledger_sha,
        "bound_manifest_sha256": bound_verifier_manifest_sha,
        "producer_ledger_relative_path": producer_ledger_path.name,
        "sentinel_lawful": authored_ledger_root == UNBOUND_ROOT_SENTINEL,
        "transition": "UNBOUND_SENTINEL_TO_BOUND_POST_PRODUCTION",
        "verifier_child_manifest_sha256": verifier_child["manifest_sha256"],
    }
    terminal = verdict_ledger(
        normal_value,
        normal_manifest,
        comparison,
        children,
        {"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t4},
        verifier_root,
        terminal_scope,
    )
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
