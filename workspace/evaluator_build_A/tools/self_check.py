#!/usr/bin/env python3
"""Syntax/schema/inventory checks only; never launches the evaluator chain."""

import ast
import hashlib
import importlib.util
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path


EXPECTED_BRANCH = {
    "BRANCH-CANDIDATE-TYPED-COMPLETE": "ADMITTED",
    "BRANCH-FAILURE-UNRESOLVED": "REJECTED",
    "BRANCH-TIE-UNRESOLVED": "REJECTED",
}
OPCODES = {"STRICT", "SCHEMA", "TYPE", "EXACT", "KERNEL", "ENUM", "DOMAIN", "UNITS", "DAG", "M2", "SYMBOLIC", "SPECTRAL", "COMPARE", "RUNTIME"}
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CLEANROOM_ROOT = PACKAGE_ROOT.parent
PROGRAM_ROOT = CLEANROOM_ROOT.parent
PIN_MANIFEST_PATH = PACKAGE_ROOT / "manifests/pins.json"


def load_pin_rows():
    raw = PIN_MANIFEST_PATH.read_bytes()
    value = json.loads(raw.decode("utf-8"))
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if raw != encoded or set(value) != {"pins", "schema"} or value["schema"] != "rd22.builder-a-pin-manifest.v001":
        raise RuntimeError("pin manifest is not canonical or closed")
    rows = value["pins"]
    if not isinstance(rows, list) or any(set(row) != {"byte_length", "kind", "relative_path", "sha256"} for row in rows):
        raise RuntimeError("pin manifest row is not closed")
    by_kind = {row["kind"]: row for row in rows}
    if len(by_kind) != len(rows):
        raise RuntimeError("pin manifest kinds are not unique")
    return by_kind


PIN_ROWS = load_pin_rows()


def pin(kind):
    try:
        return PIN_ROWS[kind]["sha256"]
    except KeyError as exc:
        raise RuntimeError(f"missing generated pin: {kind}") from exc


ADDENDUM_SHA256 = pin("integration_addendum")
VERDICT_SCHEMA_SHA256 = pin("verifier_verdict_schema")
ROOT_MEMBERSHIP_SOURCE_SHA256 = pin("root_membership_source")
SPEC_SHA256 = pin("specification")
SPEC_BASE_V007_SHA256 = pin("specification_base_v007")
SPEC_V006_SHA256 = pin("specification_v006")
GROUNDING_RELOCATION_SHA256 = pin("grounding_relocation")
GROUNDING_SOURCE_SHA256 = pin("grounding_source")
GROUNDING_PRECEDENCE_SHA256 = pin("grounding_precedence")
_grounding_source_bytes = (PROGRAM_ROOT / PIN_ROWS["grounding_source"]["relative_path"]).read_bytes()
GROUNDING_MEMBER_SHA256 = hashlib.sha256(_grounding_source_bytes[18898:19830]).hexdigest()
GROUNDING_VALUE_SHA256 = hashlib.sha256(_grounding_source_bytes[18920:19830]).hexdigest()
_grounding_value = json.loads(_grounding_source_bytes[18920:19830].decode("utf-8"))
_grounding_args_bytes = json.dumps(
    {"authority": "PRINCIPAL_SINGLE_AUTHORITY", "graph": _grounding_value},
    ensure_ascii=False,
    allow_nan=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
GROUNDING_ARGS_SHA256 = hashlib.sha256(_grounding_args_bytes).hexdigest()
EVIDENCE_MODES = ["fixed_string", "whitespace_normalized", "self_reference_scope", "hyphen_space_underscore"]
EVIDENCE_SOURCES = {
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md": ("packet", pin("evidence_cpt")),
    "BID_FULL_STACK_REVIEW_LEDGER_V003.md": ("cleanroom", pin("blocker_ledger")),
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md": ("packet", pin("source_parent_gate")),
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md": ("packet", pin("packet_v011")),
    "STAGE7_PACKET_MANIFEST_V001.sha256": ("packet", pin("packet_manifest")),
    "STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md": ("cleanroom", pin("evidence_a21")),
    "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md": ("cleanroom", pin("specification_v005")),
    "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md": ("cleanroom", pin("specification_base_v007")),
    "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md": ("cleanroom", pin("specification")),
    "STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md": ("cleanroom", pin("evidence_matrix")),
    "STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md": ("cleanroom", pin("evidence_matrix_review")),
    "STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md": ("cleanroom", pin("evidence_assembly")),
}


def stop(code, detail):
    raise SystemExit(f"SELF_CHECK_FAIL {code}: {detail}")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def content_root(rows):
    records = [f"{row['relative_path']}\0{row['byte_length']}\0{row['sha256']}\n" for row in rows]
    return digest(b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8"))


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            stop("DUPLICATE_JSON_KEY", key)
        out[key] = value
    return out


def nonfinite(value):
    stop("NONFINITE_JSON", value)


def load_json(path):
    data = path.read_bytes()
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        stop("JSON_PARSE", f"{path}:{exc}")
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if data != encoded:
        stop("JSON_CANONICAL", path)
    return value, data


def validate(schema, value, label):
    if not isinstance(schema, dict):
        stop("SCHEMA_OBJECT", label)
    kind = schema.get("type")
    if kind == "object":
        if not isinstance(value, dict):
            stop("SCHEMA_TYPE", label)
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        if not isinstance(properties, dict) or not isinstance(required, list):
            stop("SCHEMA_SHAPE", label)
        missing = set(required) - set(value)
        if missing:
            stop("SCHEMA_REQUIRED", f"{label}:{sorted(missing)}")
        if schema.get("additionalProperties") is False:
            extra = set(value) - set(properties)
            if extra:
                stop("SCHEMA_EXTRA", f"{label}:{sorted(extra)}")
        for key, child in value.items():
            if key in properties:
                validate(properties[key], child, f"{label}/{key}")
    elif kind == "array":
        if not isinstance(value, list):
            stop("SCHEMA_TYPE", label)
        if "minItems" in schema and len(value) < schema["minItems"]:
            stop("SCHEMA_MIN_ITEMS", label)
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            stop("SCHEMA_MAX_ITEMS", label)
        prefix = schema.get("prefixItems", [])
        if not isinstance(prefix, list):
            stop("SCHEMA_PREFIX_ITEMS", label)
        for index, child_schema in enumerate(prefix):
            if index >= len(value):
                break
            validate(child_schema, value[index], f"{label}/{index}")
        if "items" in schema:
            item_schema = schema["items"]
            if item_schema is False:
                if len(value) > len(prefix):
                    stop("SCHEMA_EXTRA_ITEMS", label)
            elif isinstance(item_schema, dict):
                for index, child in enumerate(value[len(prefix):], start=len(prefix)):
                    validate(item_schema, child, f"{label}/{index}")
            else:
                stop("SCHEMA_ITEMS", label)
    elif kind == "string":
        if not isinstance(value, str):
            stop("SCHEMA_TYPE", label)
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            stop("SCHEMA_PATTERN", label)
    elif kind == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind == "number":
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind == "boolean":
        if not isinstance(value, bool):
            stop("SCHEMA_TYPE", label)
    elif kind is not None:
        stop("SCHEMA_UNSUPPORTED_TYPE", f"{label}:{kind}")
    if "const" in schema and value != schema["const"]:
        stop("SCHEMA_CONST", label)
    if "enum" in schema and value not in schema["enum"]:
        stop("SCHEMA_ENUM", label)


def syntax_check(path):
    data = path.read_bytes()
    try:
        tree = ast.parse(data.decode("utf-8"), filename=str(path))
        compile(tree, str(path), "exec")
    except (UnicodeDecodeError, SyntaxError) as exc:
        stop("PYTHON_SYNTAX", f"{path}:{exc}")
    forbidden = getattr(ast, "As" + "sert")
    hits = [getattr(node, "lineno", 0) for node in ast.walk(tree) if isinstance(node, forbidden)]
    if hits:
        stop("PYTHON_CHECK_NODE", f"{path}:{hits}")


def load_parent(package):
    parent_path = package / "parent.py"
    module_spec = importlib.util.spec_from_file_location("rd22_builder_a_parent_self_check", parent_path)
    if module_spec is None or module_spec.loader is None:
        stop("PARENT_IMPORT", parent_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def load_producer(package):
    producer_path = package / "producer.py"
    module_spec = importlib.util.spec_from_file_location("rd22_builder_a_producer_self_check", producer_path)
    if module_spec is None or module_spec.loader is None:
        stop("PRODUCER_IMPORT", producer_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def verify_inventory(package, manifest):
    seen = set()
    for row in manifest["package_files"]:
        if set(row) != {"byte_length", "relative_path", "sha256"}:
            stop("INVENTORY_FIELDS", row)
        relative = row["relative_path"]
        if relative in seen:
            stop("INVENTORY_DUPLICATE", relative)
        seen.add(relative)
        path = (package / relative).resolve()
        try:
            path.relative_to(package.resolve())
        except ValueError:
            stop("INVENTORY_ESCAPE", relative)
        data = path.read_bytes()
        if len(data) != row["byte_length"] or digest(data) != row["sha256"]:
            stop("INVENTORY_HASH", relative)


def descriptor_lines(spec_data, check_id):
    prefix = f"| `{check_id}` |".encode("utf-8")
    rows = []
    for physical_line in spec_data.splitlines(keepends=True):
        if physical_line.endswith(b"\r\n"):
            body, terminator = physical_line[:-2], b"\r\n"
        elif physical_line.endswith(b"\n") or physical_line.endswith(b"\r"):
            body, terminator = physical_line[:-1], physical_line[-1:]
        else:
            body, terminator = physical_line, b""
        if body.startswith(prefix):
            rows.append((body, terminator))
    if not rows:
        stop("DESCRIPTOR_LINE", f"{check_id}:0")
    return rows


def validate_evidence_search(search, label, scope_roots):
    required = {"complete_envelope_hits", "modes", "queries", "result", "scope_members", "scope_sha256"}
    if set(search) != required or search["complete_envelope_hits"] != [] or search["modes"] != EVIDENCE_MODES or search["result"] != "ABSENT_OF_RECORD" or search["scope_members"] != 120:
        stop("EVIDENCE_SEARCH", label)
    if not isinstance(search["scope_sha256"], str) or re.fullmatch(r"[0-9a-f]{64}", search["scope_sha256"]) is None:
        stop("EVIDENCE_SCOPE_ROOT", label)
    scope_roots.add(search["scope_sha256"])
    if not isinstance(search["queries"], list) or not search["queries"]:
        stop("EVIDENCE_QUERIES", label)
    query_fields = {"fixed_hits", "hyphen_space_underscore_hits", "query", "scope_hits", "whitespace_hits"}
    for query in search["queries"]:
        if set(query) != query_fields or not isinstance(query["query"], str):
            stop("EVIDENCE_QUERY_FIELDS", label)
        if any(not isinstance(query[field], int) or query[field] < 0 for field in ("fixed_hits", "hyphen_space_underscore_hits", "whitespace_hits")):
            stop("EVIDENCE_QUERY_COUNT", label)
        if set(query["scope_hits"]) != {"requirements", "review_display", "sealed_packet"} or any(not isinstance(value, int) or value < 0 for value in query["scope_hits"].values()):
            stop("EVIDENCE_SCOPE_COUNTS", label)


def validate_partial_payload(entry, package, cleanroom, label, referenced_payloads):
    fields = {"payload_path", "payload_sha256", "role", "source_path", "source_sha256", "span"}
    if set(entry) != fields or entry["role"] not in {"PARTIAL_DISPLAY_NOT_EXECUTABLE_RECORD", "SPEC_FIXED_SUBJECT_NOT_OBSERVATION"}:
        stop("EVIDENCE_PARTIAL_FIELDS", label)
    payload = package / entry["payload_path"]
    source = cleanroom / entry["source_path"]
    if not payload.is_file() or not source.is_file():
        stop("EVIDENCE_PARTIAL_PATH", label)
    payload_data = payload.read_bytes()
    source_data = source.read_bytes()
    if payload_data != source_data or digest(payload_data) != entry["payload_sha256"] or digest(source_data) != entry["source_sha256"] or entry["payload_sha256"] != entry["source_sha256"]:
        stop("EVIDENCE_PARTIAL_HASH", label)
    start, end = entry["span"]
    if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end <= len(source_data):
        stop("EVIDENCE_PARTIAL_SPAN", label)
    if not payload.name.startswith(entry["payload_sha256"] + "--"):
        stop("EVIDENCE_CONTENT_NAME", label)
    referenced_payloads.add(str(payload.relative_to(package)))


def validate_v009_06_envelope(record, descriptor, package, cleanroom, producer):
    fields = {"available", "descriptor_sha256", "evidence", "grounding_citations", "payloads", "status"}
    if set(record) != fields or record["available"] is not True or record["status"] != "AVAILABLE" or record["descriptor_sha256"] != descriptor["descriptor_sha256"]:
        stop("V009_06_RECORD", sorted(record))
    source_path = cleanroom / "provenance/boundary_incidence_dynamics_preregistration_v011.json"
    relocation_path = cleanroom / "STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md"
    precedence_path = Path("/Users/bgm/MB Work/alpha-program-archive/supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md")
    source_data = source_path.read_bytes()
    if digest(source_data) != GROUNDING_SOURCE_SHA256 or digest(relocation_path.read_bytes()) != GROUNDING_RELOCATION_SHA256 or digest(precedence_path.read_bytes()) != GROUNDING_PRECEDENCE_SHA256:
        stop("V009_06_GROUNDING_PINS", "source/relocation/precedence")
    member_data = source_data[18898:19830]
    value_data = source_data[18920:19830]
    if len(member_data) != 932 or digest(member_data) != GROUNDING_MEMBER_SHA256 or len(value_data) != 910 or digest(value_data) != GROUNDING_VALUE_SHA256:
        stop("V009_06_GROUNDING_SPANS", {"member": [len(member_data), digest(member_data)], "value": [len(value_data), digest(value_data)]})
    stage_dependencies = json.loads(value_data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
    expected_args = {"authority": "PRINCIPAL_SINGLE_AUTHORITY", "graph": stage_dependencies}
    expected_args_data = json.dumps(expected_args, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if len(stage_dependencies) != 11 or digest(expected_args_data) != GROUNDING_ARGS_SHA256 or any(token in member_data or token in expected_args_data for token in (b"stage_dag", b'"status"')):
        stop("V009_06_SERIALIZATION", {"nodes": len(stage_dependencies), "sha256": digest(expected_args_data)})
    member_name = f"{GROUNDING_MEMBER_SHA256}--C-B-V009-06-stage_dependencies.member"
    args_name = f"{GROUNDING_ARGS_SHA256}--C-B-V009-06-dag-args.json"
    member_path = package / "inputs/evidence" / member_name
    args_path = package / "inputs/evidence" / args_name
    if member_path.read_bytes() != member_data or args_path.read_bytes() != expected_args_data:
        stop("V009_06_PAYLOAD_BYTES", "copy/serialization")
    expected_input_files = sorted(
        [
            {"byte_length": len(member_data), "relative_path": member_name, "sha256": GROUNDING_MEMBER_SHA256},
            {"byte_length": len(expected_args_data), "relative_path": args_name, "sha256": GROUNDING_ARGS_SHA256},
        ],
        key=lambda row: row["relative_path"],
    )
    evidence_record = record["evidence"]
    if set(evidence_record) != {"descriptor_sha256", "input_files", "input_root_sha256", "invocations"} or evidence_record["input_files"] != expected_input_files or evidence_record["input_root_sha256"] != content_root(expected_input_files):
        stop("V009_06_INPUT_ROOT", evidence_record)
    expected_invocations = [
        {
            "args": {"left": GROUNDING_MEMBER_SHA256, "mask": [], "right": GROUNDING_MEMBER_SHA256},
            "instance_id": None,
            "opcode": "COMPARE",
            "result_name": "r_ground",
        },
        {
            "args": expected_args,
            "instance_id": "stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)",
            "opcode": "DAG",
            "result_name": "r_dag",
        },
    ]
    if evidence_record["descriptor_sha256"] != descriptor["descriptor_sha256"] or evidence_record["invocations"] != expected_invocations:
        stop("V009_06_INVOCATION", evidence_record.get("invocations"))
    expected_citation = {
        "authority_path": "STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md",
        "authority_sha256": GROUNDING_RELOCATION_SHA256,
        "precedence_path": "supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md",
        "precedence_sha256": GROUNDING_PRECEDENCE_SHA256,
        "source_path": "provenance/boundary_incidence_dynamics_preregistration_v011.json",
        "source_sha256": GROUNDING_SOURCE_SHA256,
        "span": [18898, 19830],
        "span_sha256": GROUNDING_MEMBER_SHA256,
        "value_span": [18920, 19830],
        "value_sha256": GROUNDING_VALUE_SHA256,
    }
    expected_payloads = [
        {"byte_length": len(member_data), "payload_path": f"inputs/evidence/{member_name}", "payload_sha256": GROUNDING_MEMBER_SHA256, "role": "EXACT_RELOCATED_MEMBER_BYTES"},
        {"byte_length": len(expected_args_data), "derived_from_sha256": GROUNDING_VALUE_SHA256, "payload_path": f"inputs/evidence/{args_name}", "payload_sha256": GROUNDING_ARGS_SHA256, "role": "CANONICAL_DAG_ARGUMENTS"},
    ]
    if record["grounding_citations"] != [expected_citation] or record["payloads"] != expected_payloads:
        stop("V009_06_CITATION", "citation/payload display")
    try:
        producer.validate_program_contract(descriptor, evidence_record)
    except producer.BuildFailure as exc:
        stop("V009_06_CONTRACT", exc)
    status, started, observed, reason = producer.execute_structural(descriptor, evidence_record)
    graph_sha256 = digest(producer.canonical_bytes(expected_args["graph"]))
    expected_observed = [graph_sha256, GROUNDING_MEMBER_SHA256]
    if status != "PASS" or started is not True or observed != expected_observed or reason != "":
        stop("V009_06_OPCODE", {"status": status, "started": started, "observed": observed, "reason": reason})
    return observed


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    python_paths = sorted(package.rglob("*.py"))
    for path in python_paths:
        syntax_check(path)
    json_values = {}
    for path in sorted(package.rglob("*.json")):
        if any(part in {"outputs", "pycache"} for part in path.relative_to(package).parts):
            continue
        json_values[path.name] = load_json(path)[0]
    check_map = json_values["check_map.json"]
    fixtures = json_values["fixture_manifest.json"]
    evidence = json_values["structural_evidence_manifest.json"]
    normal = json_values["normal.json"]
    optimized = json_values["optimized.json"]
    pin_manifest = json_values["pins.json"]
    package_inventory = json_values["package_inventory.json"]
    parent_module = load_parent(package)
    producer_module = load_producer(package)
    root_membership_source = cleanroom / "STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md"
    root_membership_bytes = root_membership_source.read_bytes()
    if digest(root_membership_bytes) != ROOT_MEMBERSHIP_SOURCE_SHA256:
        stop("ROOT_MEMBERSHIP_SOURCE_PIN", root_membership_source)
    root_membership_text = root_membership_bytes.decode("utf-8")
    expected_root_members = (
        "contracts/verifier_verdict.schema.json",
        "run_verifier.py",
        "verifier/__init__.py",
        "verifier/canonical_json.py",
        "verifier/child_manifest.py",
        "verifier/comparison.py",
        "verifier/contracts.py",
        "verifier/hashing.py",
        "verifier/replay.py",
        "verifier/runtime_state.py",
        "verifier/spec_census.py",
        "verifier/verify.py",
    )
    if parent_module.VERIFIER_ROOT_TRANSCRIBED_MEMBERS != expected_root_members or expected_root_members != tuple(sorted(expected_root_members)):
        stop("ROOT_MEMBER_CENSUS", parent_module.VERIFIER_ROOT_TRANSCRIBED_MEMBERS)
    if any(member not in root_membership_text for member in expected_root_members):
        stop("ROOT_MEMBERSHIP_SOURCE_CONTENT", root_membership_source)
    verdict_schema_rows = [row for row in normal["external_inputs"] if row["kind"] == "verifier_verdict_schema"]
    if len(verdict_schema_rows) != 1 or verdict_schema_rows[0]["sha256"] != VERDICT_SCHEMA_SHA256:
        stop("VERDICT_SCHEMA_INPUT_ROW", verdict_schema_rows)
    verdict_schema_path = cleanroom.parent / verdict_schema_rows[0]["relative_path"]
    verdict_schema_data = verdict_schema_path.read_bytes()
    if len(verdict_schema_data) != verdict_schema_rows[0]["byte_length"] or digest(verdict_schema_data) != verdict_schema_rows[0]["sha256"]:
        stop("VERDICT_SCHEMA_INPUT_PIN", verdict_schema_path)
    verdict_schema = json.loads(verdict_schema_data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
    parent_module.validate_schema_definition(verdict_schema)
    snapshot_path = cleanroom.parent / "provenance/primitive_step6_runtime_snapshot_v012.json"
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    trust_root = parent_module.trust_root_digest(snapshot["native_system_trust_root"])
    if re.fullmatch(r"[0-9a-f]{64}", trust_root) is None:
        stop("TRUST_ROOT_FORM", trust_root)
    if normal["runtime_subject"]["trust_root"] != trust_root or optimized["runtime_subject"]["trust_root"] != trust_root:
        stop("TRUST_ROOT_MANIFEST_AGREEMENT", {"computed": trust_root, "normal": normal["runtime_subject"]["trust_root"], "optimized": optimized["runtime_subject"]["trust_root"]})
    receipt = {
        "manifest_sha256": "0" * 64,
        "module_ledger": [],
        "mutation_event_ledger": [],
        "native_ledger": [],
        "network_event_ledger": [],
        "open_event_ledger": [],
        "process_event_ledger": [],
    }
    with tempfile.TemporaryDirectory(prefix="rd22-static-child-record-") as child_payload_directory:
        child = parent_module.child_record("0" * 64, "1" * 64, 0, b"{}", b"{}", receipt, trust_root, trust_root, Path(child_payload_directory))
    producer_snapshots = {label: trust_root for label in ("T0", "T1", "T2", "T3")}
    if "T4" in producer_snapshots:
        stop("T4_BEFORE_SAMPLE", sorted(producer_snapshots))
    terminal_snapshots = {label: trust_root for label in ("T0", "T1", "T2", "T3", "T4")}
    synthetic_output = {"authority_firewall": {}, "checks": [], "fixtures": [], "summary": {}}
    authorization_row = [row for row in normal["external_inputs"] if row["kind"] == "authorization"]
    if len(authorization_row) != 1:
        stop("AUTHORIZATION_INPUT_ROW", authorization_row)
    authorization_path = Path("/Users/bgm/MB Work/alpha-program-archive") / authorization_row[0]["relative_path"]
    authorization_bytes, authorization_digest = parent_module.verify_bytes_with_digest(authorization_path, authorization_row[0]["sha256"])
    if len(authorization_bytes) != authorization_row[0]["byte_length"]:
        stop("AUTHORIZATION_INPUT_LENGTH", len(authorization_bytes))
    producer_scope = {"phase": "PRE_VERIFIER_STATIC_SCOPE"}
    terminal_scope = {"phase": "POST_VERIFIER_STATIC_SCOPE"}
    producer_ledger = parent_module.verdict_ledger(synthetic_output, normal, {}, [child], producer_snapshots, "2" * 64, producer_scope, authorization_digest)
    terminal_ledger = parent_module.verdict_ledger(synthetic_output, normal, {}, [child], terminal_snapshots, "2" * 64, terminal_scope, authorization_digest)
    verifier_value = {
        "authority_firewall": dict(normal["authority_firewall"]),
        "authorization_sha256": authorization_digest,
        "census": {},
        "checks_replayed": [],
        "findings": [],
        "fixtures_replayed": [],
        "independence": {"expectations_source": "STATIC_SITE_AGREEMENT", "producer_code_imported": False},
        "producer_comparison": {},
        "runtime_subject": normal["runtime_subject"],
        "schema": "gravacle.a35.verifier-verdict.v1",
        "spec_sha256": parent_module.SPEC_SHA256,
        "terminal_content_sha256": "3" * 64,
        "verdict": "VERIFIED",
        "verifier_sha256": "2" * 64,
    }
    full_branch_spec = verdict_schema["oneOf"][0]["properties"]["spec_sha256"].get("const")
    if full_branch_spec == parent_module.SPEC_SHA256:
        accepted_verifier = parent_module.verifier_stdout(parent_module.canonical_bytes(verifier_value), "VERIFIED", "2" * 64, snapshot, authorization_digest, verdict_schema)
        b_repin_state = "ALIGNED"
    else:
        schema_probe = {**verifier_value, "spec_sha256": full_branch_spec}
        selected = parent_module.validate_verdict_document(schema_probe, verdict_schema)
        if selected is not verdict_schema["oneOf"][0] or full_branch_spec != SPEC_BASE_V007_SHA256:
            stop("B_SPEC_REPIN_STATE", {"schema_const": full_branch_spec, "parent": parent_module.SPEC_SHA256})
        accepted_verifier = verifier_value
        b_repin_state = "PENDING_PARALLEL_B_REPIN"
    fault_value = {"fault": "STATIC_FAULT_DOCUMENT", "schema": "gravacle.a35.verifier-verdict.v1", "verdict": "FAIL"}
    accepted_fault = parent_module.verifier_stdout(parent_module.canonical_bytes(fault_value), "FAIL", "2" * 64, snapshot, authorization_digest, verdict_schema)
    if accepted_fault != fault_value:
        stop("VERDICT_SCHEMA_FAULT_ACCEPTANCE", accepted_fault)
    full_negative_base = verifier_value if b_repin_state == "ALIGNED" else {**verifier_value, "spec_sha256": full_branch_spec}
    rejected_documents = {
        "old_13_field": {key: value for key, value in full_negative_base.items() if key != "fixtures_replayed"},
        "full_extra": {**full_negative_base, "undeclared": False},
        "fault_extra": {**fault_value, "undeclared": False},
        "wrong_spec": {**full_negative_base, "spec_sha256": "0" * 64},
    }
    for label, document in rejected_documents.items():
        try:
            if b_repin_state == "ALIGNED" or label == "fault_extra":
                parent_module.verifier_stdout(parent_module.canonical_bytes(document), document["verdict"], "2" * 64, snapshot, authorization_digest, verdict_schema)
            else:
                parent_module.validate_verdict_document(document, verdict_schema)
        except parent_module.ParentFailure:
            continue
        stop("VERDICT_SCHEMA_NEGATIVE", label)
    trust_site_values = {
        "definition": trust_root,
        "manifests": normal["runtime_subject"]["trust_root"] if optimized["runtime_subject"]["trust_root"] == trust_root else "DRIFT",
        "main_receiver": parent_module.trust_root_digest(snapshot["native_system_trust_root"]),
        "T0_T3": producer_snapshots["T0"] if len(set(producer_snapshots.values())) == 1 else "DRIFT",
        "child_rows": child["runtime_before_sha256"] if child["runtime_after_sha256"] == trust_root else "DRIFT",
        "producer_runtime": producer_ledger["runtime_subject"]["trust_root"],
        "producer_T0_T3_value_only": producer_ledger["trust_snapshots"]["T0"] if len(set(producer_ledger["trust_snapshots"].values())) == 1 else "DRIFT",
        "verifier_receiver": accepted_verifier["runtime_subject"]["trust_root"],
        "terminal_runtime": terminal_ledger["runtime_subject"]["trust_root"],
        "terminal_T0_T4": terminal_ledger["trust_snapshots"]["T0"] if len(set(terminal_ledger["trust_snapshots"].values())) == 1 else "DRIFT",
    }
    if set(trust_site_values.values()) != {trust_root}:
        stop("TRUST_ROOT_SITE_AGREEMENT", trust_site_values)
    if set(package_inventory) != {"files", "schema"} or package_inventory["schema"] != "rd22.builder-a-package-inventory.v001":
        stop("PACKAGE_INVENTORY_SCHEMA", package_inventory)
    inventory_rows = package_inventory["files"]
    inventory_paths = [row.get("relative_path") for row in inventory_rows]
    expected_paths = sorted(
        str(path.relative_to(package))
        for path in package.rglob("*")
        if path.is_file()
        and str(path.relative_to(package)) != "manifests/package_inventory.json"
        and not any(part in {"outputs", "pycache"} for part in path.relative_to(package).parts)
    )
    if inventory_paths != expected_paths or len(inventory_paths) != len(set(inventory_paths)):
        stop("PACKAGE_INVENTORY_CENSUS", {"declared": inventory_paths, "actual": expected_paths})
    for row in inventory_rows:
        if set(row) != {"byte_length", "relative_path", "sha256"}:
            stop("PACKAGE_INVENTORY_FIELDS", row)
        data = (package / row["relative_path"]).read_bytes()
        if row["byte_length"] != len(data) or row["sha256"] != digest(data):
            stop("PACKAGE_INVENTORY_HASH", row["relative_path"])
    if check_map["branch_outcome"] != EXPECTED_BRANCH or normal["branch_outcome"] != EXPECTED_BRANCH or optimized["branch_outcome"] != EXPECTED_BRANCH:
        stop("BRANCH_OUTCOME", "drift")
    if len(check_map["checks"]) != 66 or len(check_map["check_ids"]) != 66 or len(set(check_map["check_ids"])) != 66:
        stop("CHECK_COUNT", len(check_map["checks"]))
    structural = [row for row in check_map["checks"] if row["execution_class"] == "STRUCTURAL"]
    gated = [row for row in check_map["checks"] if row["execution_class"] == "GATED-EXECUTION"]
    if len(structural) != 56 or len(gated) != 10:
        stop("CLASS_COUNT", (len(structural), len(gated)))
    if len(fixtures["fixtures"]) != 6 or len(fixtures["fixture_ids"]) != 6:
        stop("FIXTURE_COUNT", len(fixtures["fixtures"]))
    fixture_descriptor_fields = {"deterministic_procedure", "execution_class", "expected_verdict_fields", "fixture_id", "fixture_spec_sha256", "mutation_ids", "prerequisites", "primary_check_ids", "required_gate", "source"}
    for row in fixtures["fixtures"]:
        if set(row) != fixture_descriptor_fields:
            stop("FIXTURE_DESCRIPTOR_FIELDS", row["fixture_id"])
    if sum(row["execution_class"] == "STRUCTURAL" for row in fixtures["fixtures"]) != 3 or sum(row["execution_class"] == "GATED-EXECUTION" for row in fixtures["fixtures"]) != 3:
        stop("FIXTURE_CLASS_COUNT", "not 3/3")
    structural_by_id = {row["check_id"]: row for row in structural}
    structural_fixtures = {row["fixture_id"]: row for row in fixtures["fixtures"] if row["execution_class"] == "STRUCTURAL"}
    if set(evidence["check_records"]) != set(structural_by_id) or set(evidence["fixture_records"]) != set(structural_fixtures):
        stop("EVIDENCE_CENSUS", "wrong IDs")
    if set(evidence) != {"check_records", "declared_root", "fixture_records", "payload_inventory", "schema", "subject_lineage_root"} or evidence["schema"] != "rd22.structural-evidence-manifest.v001" or evidence["subject_lineage_root"] != normal["subject_lineage_root"]:
        stop("EVIDENCE_BINDING", "schema/root")
    payload_dir = package / "inputs/evidence"
    payload_files = sorted(path for path in payload_dir.iterdir() if path.is_file())
    # Three V009-06 payload files are retained: raw grounding, current
    # single-authority arguments, and the prior paired-argument bytes as a
    # content-addressed supersession witness.  V007 is retained as the sealed
    # base and V008 is the current sealed-spec payload.
    if len(payload_files) != len(EVIDENCE_SOURCES) + 3:
        stop("EVIDENCE_PAYLOAD_CENSUS", len(payload_files))
    packet_dir = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001"
    for name, (location, expected) in EVIDENCE_SOURCES.items():
        source = (packet_dir if location == "packet" else cleanroom) / name
        matches = [path for path in payload_files if path.name == f"{expected}--{name}"]
        if digest(source.read_bytes()) != expected or len(matches) != 1 or matches[0].read_bytes() != source.read_bytes():
            stop("EVIDENCE_SOURCE_COPY", name)
    expected_payload_inventory = [
        {"byte_length": len(path.read_bytes()), "relative_path": path.name, "sha256": digest(path.read_bytes())}
        for path in payload_files
    ]
    if evidence["payload_inventory"] != expected_payload_inventory or evidence["declared_root"] != content_root(expected_payload_inventory):
        stop("EVIDENCE_DECLARED_ROOT", evidence.get("declared_root"))
    scope_roots = set()
    referenced_payloads = set()
    check_fields = {"available", "descriptor_sha256", "missing_objects", "partial_payloads", "reason", "search", "status"}
    v009_06_observed = None
    for check_id, record in evidence["check_records"].items():
        if check_id == "C-B-V009-06":
            v009_06_observed = validate_v009_06_envelope(record, structural_by_id[check_id], package, cleanroom, producer_module)
            continue
        if set(record) != check_fields or record["available"] is not False or record["status"] != "ABSENT_OF_RECORD" or not record["reason"].startswith("ABSENT_OF_RECORD:"):
            stop("EVIDENCE_CHECK_RECORD", check_id)
        if record["descriptor_sha256"] != structural_by_id[check_id]["descriptor_sha256"] or len(record["missing_objects"]) != 2:
            stop("EVIDENCE_CHECK_BINDING", check_id)
        validate_evidence_search(record["search"], check_id, scope_roots)
        for entry in record["partial_payloads"]:
            validate_partial_payload(entry, package, cleanroom, check_id, referenced_payloads)
    fixture_fields = {"available", "fixture_spec_sha256", "missing_objects", "partial_payloads", "reason", "search", "status"}
    for fixture_id, record in evidence["fixture_records"].items():
        if set(record) != fixture_fields or record["available"] is not False or record["status"] != "ABSENT_OF_RECORD" or not record["reason"].startswith("ABSENT_OF_RECORD:"):
            stop("EVIDENCE_FIXTURE_RECORD", fixture_id)
        if record["fixture_spec_sha256"] != structural_fixtures[fixture_id]["fixture_spec_sha256"] or len(record["missing_objects"]) != 3 or len(record["partial_payloads"]) != 1:
            stop("EVIDENCE_FIXTURE_BINDING", fixture_id)
        validate_evidence_search(record["search"], fixture_id, scope_roots)
        for entry in record["partial_payloads"]:
            validate_partial_payload(entry, package, cleanroom, fixture_id, referenced_payloads)
    if len(scope_roots) != 1:
        stop("EVIDENCE_SCOPE_DRIFT", sorted(scope_roots))
    if v009_06_observed is None:
        stop("V009_06_NOT_CHECKED", "missing")
    with tempfile.TemporaryDirectory(prefix="rd22-static-consumed-evidence-") as temporary:
        consumed_directory = Path(temporary)
        materialization_rows = {}

        def static_payload_sink(claimed_digest, payload):
            materialization_rows[claimed_digest] = producer_module.materialize_consumed_evidence(consumed_directory, claimed_digest, payload)

        target_descriptor = structural_by_id["C-B-V009-06"]
        target_evidence = evidence["check_records"]["C-B-V009-06"]["evidence"]
        status, started, observed, reason = producer_module.execute_structural(target_descriptor, target_evidence, static_payload_sink)
        raw_matches = [path for path in payload_files if path.name.startswith(f"{GROUNDING_MEMBER_SHA256}--")]
        if len(raw_matches) != 1:
            stop("GROUNDING_PAYLOAD_CENSUS", [path.name for path in raw_matches])
        static_payload_sink(GROUNDING_MEMBER_SHA256, raw_matches[0].read_bytes())
        linked_row = producer_module.make_check_row(target_descriptor, evidence["check_records"], normal["subject_lineage_root"])
        expected_linked_invocation = target_evidence["invocations"][1]
        expected_linked_invocation = {
            **expected_linked_invocation,
            "source_sha256": GROUNDING_SOURCE_SHA256,
            "span": [18898, 19830],
            "span_sha256": GROUNDING_MEMBER_SHA256,
        }
        expected_check_fields = {
            "blocker_id", "source", "check_id", "check_spec_sha256", "execution_class",
            "input_root_sha256", "deterministic_procedure", "prerequisites", "required_gate",
            "expected_predicate", "invocation", "procedure_started", "status",
            "observed_evidence_sha256s", "reason",
        }
        if (
            set(linked_row) != expected_check_fields
            or linked_row["invocation"] != expected_linked_invocation
            or set(linked_row["invocation"]) != {"args", "instance_id", "opcode", "result_name", "source_sha256", "span", "span_sha256"}
            or linked_row["invocation"]["instance_id"] != f"stage_dependencies@{GROUNDING_SOURCE_SHA256}:[18898,19830)"
            or linked_row["invocation"]["source_sha256"] != GROUNDING_SOURCE_SHA256
            or linked_row["invocation"]["span"] != [18898, 19830]
            or linked_row["invocation"]["span_sha256"] != GROUNDING_MEMBER_SHA256
            or linked_row["observed_evidence_sha256s"] != observed
        ):
            stop("BYTE_SPAN_LINKAGE_CARRIER", {"fields": sorted(linked_row), "invocation": linked_row.get("invocation")})
        synthetic_consumed_output = {"checks": [{"observed_evidence_sha256s": observed}], "fixtures": []}
        parent_materialized = parent_module.consumed_evidence_files(synthetic_consumed_output, consumed_directory, "static")
        if status != "PASS" or started is not True or reason != "" or observed != v009_06_observed or set(materialization_rows) != set(observed) or len(parent_materialized) != len(observed):
            stop("CONSUMED_IMPLIES_MATERIALIZED", {"status": status, "observed": observed, "producer": sorted(materialization_rows), "parent": sorted(parent_materialized)})
        for claimed_digest in observed:
            materialized_path = consumed_directory / f"{claimed_digest}.json"
            materialization_row = materialization_rows[claimed_digest]
            if materialization_row != {"operation": "content_addressed_materialize", "path": str(materialized_path.resolve())} or not materialized_path.is_file() or digest(materialized_path.read_bytes()) != claimed_digest:
                stop("CONSUMED_MATERIALIZED_BYTES", claimed_digest)
        graph_payload = producer_module.canonical_bytes(target_evidence["invocations"][1]["args"]["graph"])
        graph_sha256 = digest(graph_payload)
        if (consumed_directory / f"{graph_sha256}.json").read_bytes() != graph_payload:
            stop("GRAPH_ARGUMENT_PAYLOAD", graph_sha256)
        raw_payload = (consumed_directory / f"{GROUNDING_MEMBER_SHA256}.json").read_bytes()
        if len(raw_payload) != 932 or raw_payload != raw_matches[0].read_bytes():
            stop("RAW_GROUNDING_PAYLOAD", {"length": len(raw_payload), "sha256": digest(raw_payload)})
        input_digests = {row["sha256"] for row in target_evidence["input_files"]}
        consumable_argument_digests = []
        for invocation in target_evidence["invocations"]:
            for argument in invocation["args"].values():
                if isinstance(argument, dict):
                    candidate = digest(producer_module.canonical_bytes(argument))
                elif isinstance(argument, str) and argument in input_digests:
                    candidate = argument
                else:
                    continue
                if candidate not in consumable_argument_digests:
                    consumable_argument_digests.append(candidate)
        if set(observed) != set(consumable_argument_digests) or observed != [graph_sha256, GROUNDING_MEMBER_SHA256]:
            stop("CONSUMABLE_ARGUMENT_NOT_REPRODUCED", {"observed": observed, "arguments": consumable_argument_digests})
        consumed_implies_materialized = "PASS"
        consumable_args_reproduced = "PASS"
    spec_data = (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md").read_bytes()
    if digest(spec_data) != SPEC_SHA256 or parent_module.SPEC_SHA256 != SPEC_SHA256 or check_map["spec_sha256"] != SPEC_SHA256:
        stop("RUNTIME_SPEC_PIN", {"bytes": digest(spec_data), "parent": parent_module.SPEC_SHA256, "map": check_map["spec_sha256"]})
    spec_base_v007_data = (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md").read_bytes()
    if digest(spec_base_v007_data) != SPEC_BASE_V007_SHA256:
        stop("SPEC_V007_BASE_PIN", digest(spec_base_v007_data))
    spec_v006_data = (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md").read_bytes()
    if digest(spec_v006_data) != SPEC_V006_SHA256 or spec_v006_data.count(b"`SPEC-INCOMPLETE` |") != 17 or b"#### V006 sealed-corpus law for `M2(q,S)`" not in spec_v006_data:
        stop("SPEC_V006_PIN", {"sha256": digest(spec_v006_data), "registry_rows": spec_v006_data.count(b"`SPEC-INCOMPLETE` |")})
    if spec_data.count(b"`SPEC-INCOMPLETE` |") != 17 or b"#### V007 sealed-corpus law for `M2(q,S)`" not in spec_data or b"all five false-negative modes" not in spec_data:
        stop("SPEC_V008_CORPUS_LAW_CARRIAGE", {"registry_rows": spec_data.count(b"`SPEC-INCOMPLETE` |")})
    prior_changed_descriptor_ids = {
        row["check_id"]
        for row in check_map["checks"]
        if row["descriptor_sha256"] not in {digest(body) for body, _ in descriptor_lines(spec_v006_data, row["check_id"])}
    }
    if prior_changed_descriptor_ids != {"C-B-V009-06"}:
        stop("V007_DESCRIPTOR_DELTA", sorted(prior_changed_descriptor_ids))
    current_changed_descriptor_ids = {
        row["check_id"]
        for row in check_map["checks"]
        if {digest(body) for body, _ in descriptor_lines(spec_data, row["check_id"])}
        != {digest(body) for body, _ in descriptor_lines(spec_base_v007_data, row["check_id"])}
    }
    if current_changed_descriptor_ids:
        stop("V008_DESCRIPTOR_DELTA", sorted(current_changed_descriptor_ids))
    old_spec_name = "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md"
    pin_closure_hits = {"name": [], "value": []}
    allowed_base_reference_paths = {
        "inputs/structural_evidence_manifest.json",
        "manifests/normal.json",
        "manifests/optimized.json",
        "manifests/package_inventory.json",
        "manifests/pins.json",
        "tools/generate_pins.py",
        "tools/self_check.py",
    }
    for path in sorted(package.rglob("*")):
        if not path.is_file() or any(part in {"outputs", "pycache"} for part in path.relative_to(package).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = str(path.relative_to(package))
        for label, term in (("name", old_spec_name), ("value", SPEC_BASE_V007_SHA256)):
            for line_number, line in enumerate(text.splitlines(), 1):
                pin_closure_hits[label].extend((relative, line_number) for _ in range(line.count(term)))
        if (old_spec_name in text or SPEC_BASE_V007_SHA256 in text) and not (
            relative.startswith("inputs/evidence/") or relative in allowed_base_reference_paths
        ):
            stop("PIN_CLOSURE_UNJUSTIFIED_BASE", relative)
    if not pin_closure_hits["name"] or not pin_closure_hits["value"]:
        stop("PIN_CLOSURE_CENSUS", pin_closure_hits)
    pin_closure_total = len(pin_closure_hits["name"]) + len(pin_closure_hits["value"])
    registry_block = spec_data.split(b"#### V007 sealed-corpus law for `M2(q,S)`", 1)[1].split(b"#### V003 criterion-result binding", 1)[0]
    registry_ids = set(re.findall(rb"(?m)^\| `(C-[^`]+)` \|", registry_block))
    m2_ids = {
        row["check_id"].encode("utf-8")
        for row in check_map["checks"]
        if any(operation["opcode"] == "M2" for operation in row["program_contract"])
    }
    if len(m2_ids) != 17 or registry_ids != m2_ids:
        stop("SPEC_V007_M2_REGISTRY", {"generated": sorted(m2_ids), "registered": sorted(registry_ids)})
    addendum_path = cleanroom / "STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md"
    if digest(addendum_path.read_bytes()) != ADDENDUM_SHA256:
        stop("ADDENDUM_PIN", addendum_path)
    ledger = (cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md").read_bytes()
    descriptor_terminators_excluded = 0
    for row in check_map["checks"]:
        candidates = descriptor_lines(spec_data, row["check_id"])
        candidate_hashes = [digest(row_bytes) for row_bytes, _ in candidates]
        if candidate_hashes.count(row["descriptor_sha256"]) != 1 or row["descriptor_bytes_sha256"] != row["descriptor_sha256"]:
            stop("DESCRIPTOR_HASH", row["check_id"])
        matching_rows = [(row_bytes, terminator) for row_bytes, terminator in candidates if digest(row_bytes) == row["descriptor_sha256"]]
        if len(matching_rows) != 1:
            stop("DESCRIPTOR_MATCH", row["check_id"])
        row_bytes, terminator = matching_rows[0]
        if terminator not in {b"\n", b"\r\n"} or row_bytes.endswith((b"\r", b"\n")):
            stop("DESCRIPTOR_TERMINATOR_BOUNDARY", row["check_id"])
        if digest(row_bytes + terminator) == row["descriptor_sha256"]:
            stop("DESCRIPTOR_TERMINATOR_COVERED", row["check_id"])
        descriptor_terminators_excluded += 1
        if not row["program_contract"]:
            stop("PROGRAM_EMPTY", row["check_id"])
        for operation in row["program_contract"]:
            if operation["opcode"] not in OPCODES:
                stop("OPCODE", operation)
        if row["source"]["path"] == "BID_FULL_STACK_REVIEW_LEDGER_V003.md":
            start, end = row["source"]["byte_span"]
            if not 0 <= start < end <= len(ledger) or re.match(rb"[0-9]+\. ", ledger[start:end]) is None:
                stop("SOURCE_SPAN", row["check_id"])
    if descriptor_terminators_excluded != 66 or check_map["descriptor_convention"] != "SHA256 of the exact UTF-8 Markdown descriptor row excluding its line terminator":
        stop("DESCRIPTOR_TERMINATOR_CENSUS", descriptor_terminators_excluded)
    for row in fixtures["fixtures"]:
        start, end = row["source"]["byte_span"]
        source_bytes = (cleanroom / row["source"]["path"]).read_bytes()[start:end]
        if digest(source_bytes) != row["fixture_spec_sha256"]:
            stop("FIXTURE_SPEC_HASH", row["fixture_id"])
    verify_inventory(package, normal)
    verify_inventory(package, optimized)
    declared_payloads = {row["relative_path"] for row in normal["package_files"] if row["relative_path"].startswith("inputs/evidence/")}
    actual_payloads = {str(path.relative_to(package)) for path in payload_files}
    if declared_payloads != actual_payloads:
        stop("EVIDENCE_RUNTIME_INVENTORY", {"declared": sorted(declared_payloads), "actual": sorted(actual_payloads)})
    differing = {key for key in normal if normal[key] != optimized[key]}
    if differing != {"mode", "optimization", "writable_paths"}:
        stop("MANIFEST_DRIFT", sorted(differing))
    addendum_rows = [row for row in normal["external_inputs"] if row["kind"] == "integration_addendum"]
    if len(addendum_rows) != 1 or addendum_rows[0]["sha256"] != ADDENDUM_SHA256:
        stop("MANIFEST_ADDENDUM_PIN", addendum_rows)
    if normal["allowed_events"].get("mutation") != ["consumed_evidence", "output", "receipt"] or normal["allowed_events"].get("writes") != ["consumed_evidence", "output", "receipt"]:
        stop("MANIFEST_MUTATION_EVENTS", normal["allowed_events"])
    schema_targets = {
        "child-manifest.schema.json": [normal, optimized],
        "check-map.schema.json": [check_map],
        "fixture-manifest.schema.json": [fixtures],
        "pin-manifest.schema.json": [pin_manifest],
        "structural-evidence.schema.json": [evidence],
    }
    for schema_name, targets in schema_targets.items():
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False:
            stop("SCHEMA_TOP_NOT_CLOSED", schema_name)
        for index, target in enumerate(targets):
            validate(schema, target, f"{schema_name}[{index}]")
    for schema_name in ["producer-output.schema.json", "child-receipt.schema.json", "verifier-manifest.schema.json", "terminal-ledger.schema.json"]:
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False or not schema.get("required") or set(schema["required"]) != set(schema["properties"]):
            stop("SCHEMA_EXACT_TOP", schema_name)
    if (package / "schemas/verifier-output.schema.json").exists():
        stop("VERDICT_CONTRACT_TRANSCRIPTION", "local verifier-output schema remains")
    producer_schema = json_values["producer-output.schema.json"]
    compared_properties = set(producer_schema["properties"])
    unmasked_per_child_fields = {"manifest_sha256", "mode", "optimization", "writable_paths"}
    misplaced = sorted(compared_properties & unmasked_per_child_fields)
    if misplaced:
        stop("PRODUCER_COMPARED_SURFACE", misplaced)
    if len(compared_properties) != 13:
        stop("PRODUCER_OUTPUT_FIELDS", sorted(compared_properties))
    receipt_schema = json_values["child-receipt.schema.json"]
    if len(receipt_schema["properties"]) != 16 or "manifest_sha256" not in receipt_schema["properties"] or "manifest_sha256" not in receipt_schema["required"]:
        stop("RECEIPT_MANIFEST_CARRIER", sorted(receipt_schema["properties"]))
    expected_mask_literal = 'MASK_FIELDS = {"process_id", "monotonic_duration", "python_optimize"}'
    parent_source = (package / "parent.py").read_text(encoding="utf-8")
    producer_source = (package / "producer.py").read_text(encoding="utf-8")
    if expected_mask_literal not in parent_source or expected_mask_literal not in producer_source:
        stop("SEMANTIC_MASK_DRIFT", expected_mask_literal)
    parent_output_block = parent_source.split("def output(path):", 1)[1].split("def classify_receipt(", 1)[0]
    producer_output_block = producer_source.split("    output = {", 1)[1].split("    output_bytes =", 1)[0]
    if '"manifest_sha256"' in parent_output_block or '"manifest_sha256"' in producer_output_block:
        stop("OUTPUT_MANIFEST_CARRIER", "manifest_sha256 remains")
    if producer_source.count('"manifest_sha256": args.manifest_sha256,') != 1:
        stop("MANIFEST_CARRIER_CENSUS", producer_source.count('"manifest_sha256": args.manifest_sha256,'))
    fixture_row_schema = producer_schema["properties"]["fixtures"]["items"]
    if len(fixture_row_schema["properties"]) != 16 or fixture_row_schema.get("additionalProperties") is not False:
        stop("FIXTURE_ROW_CONTRACT", fixture_row_schema)
    for descriptor in fixtures["fixtures"]:
        synthetic = dict(descriptor)
        synthetic.update({"input_root_sha256": normal["subject_lineage_root"], "observed_evidence_sha256s": [], "observed_verdict_fields": {}, "procedure_started": False, "reason": "STATIC_CONTRACT_FIXTURE", "status": "NOT_RUN_GATE" if descriptor["execution_class"] == "GATED-EXECUTION" else "FAIL"})
        validate(fixture_row_schema, synthetic, f"fixture_row/{descriptor['fixture_id']}")
        if set(synthetic["observed_verdict_fields"]) - set(synthetic["expected_verdict_fields"]):
            stop("FIXTURE_QUARANTINE", descriptor["fixture_id"])
    terminal_schema = json_values["terminal-ledger.schema.json"]
    child_row_schema = terminal_schema["properties"]["children"]["items"]
    if len(child_row_schema["properties"]) != 14 or child_row_schema.get("additionalProperties") is not False:
        stop("CHILD_ROW_CONTRACT", child_row_schema)
    empty_digest = digest(b"[]")
    synthetic_child = {field: empty_digest for field in child_row_schema["properties"]}
    synthetic_child["optimize"] = 0
    synthetic_child["receipt_authoritative"] = False
    validate(child_row_schema, synthetic_child, "child_row")
    for field in ("process_event_ledger_sha256", "network_event_ledger_sha256", "mutation_event_ledger_sha256"):
        if synthetic_child[field] != empty_digest:
            stop("EMPTY_EVENT_DIGEST", field)
    expected_event_carriers = (
        ("module_ledger_sha256", "module_ledger"),
        ("native_ledger_sha256", "native_ledger"),
        ("open_event_ledger_sha256", "open_event_ledger"),
        ("process_event_ledger_sha256", "process_event_ledger"),
        ("network_event_ledger_sha256", "network_event_ledger"),
        ("mutation_event_ledger_sha256", "mutation_event_ledger"),
    )
    if parent_module.EVENT_LEDGER_CARRIERS != expected_event_carriers:
        stop("EVENT_PAYLOAD_CARRIERS", parent_module.EVENT_LEDGER_CARRIERS)
    synthetic_event_receipt = {
        receipt_field: ([] if receipt_field == "native_ledger" else [{"event_class": receipt_field}])
        for _, receipt_field in expected_event_carriers
    }
    with tempfile.TemporaryDirectory(prefix="rd22-static-event-payload-") as temporary:
        temporary_root = Path(temporary)
        source_directory = temporary_root / "sealed-evidence"
        source_directory.mkdir()
        (source_directory / "sealed-payload.md").write_bytes(b"sealed-static-payload")
        run_directory, staged_rows = parent_module.stage_evidence_directory(source_directory, temporary_root / "run-evidence")
        event_digests = parent_module.materialize_event_payloads(synthetic_event_receipt, run_directory)
        if len(staged_rows) != 1 or len(event_digests) != 6:
            stop("EVENT_PAYLOAD_STATIC_CENSUS", {"staged": len(staged_rows), "carriers": len(event_digests)})
        for digest_field, receipt_field in expected_event_carriers:
            payload = parent_module.canonical_bytes(synthetic_event_receipt[receipt_field])
            payload_digest = digest(payload)
            payload_path = run_directory / f"{payload_digest}.json"
            if event_digests[digest_field] != payload_digest or not payload_path.is_file() or payload_path.read_bytes() != payload:
                stop("EVENT_PAYLOAD_STATIC_BINDING", digest_field)
        if (run_directory / f"{empty_digest}.json").read_bytes() != b"[]":
            stop("EVENT_PAYLOAD_EMPTY_CANON", empty_digest)
        if len(list(run_directory.glob("*.json"))) != 6:
            stop("EVENT_PAYLOAD_STATIC_FILES", sorted(path.name for path in run_directory.glob("*.json")))
    if "mutation_event_ledger" not in receipt_schema["properties"]:
        stop("MUTATION_RECEIPT_CARRIER", "missing")
    authorization_schema = terminal_schema["properties"]["authorization"]
    if authorization_schema.get("additionalProperties") is not False or set(authorization_schema.get("required", [])) != {"artifact_sha256", "scope"} or authorization_schema.get("properties", {}).get("artifact_sha256", {}).get("pattern") != "[0-9a-f]{64}" or authorization_schema.get("properties", {}).get("scope", {}).get("type") != "object":
        stop("AUTHORIZATION_SCHEMA", authorization_schema)
    for ledger_name, ledger in (("producer", producer_ledger), ("terminal", terminal_ledger)):
        if ledger["authorization"] != {"artifact_sha256": authorization_digest, "scope": ledger["scope"]}:
            stop("AUTHORIZATION_FORWARD", {ledger_name: ledger["authorization"]})
    manifest_runtime_schema = json_values["child-manifest.schema.json"]["properties"]["runtime_subject"]
    terminal_runtime_schema = terminal_schema["properties"]["runtime_subject"]
    terminal_trust_schema = terminal_schema["properties"]["trust_snapshots"]
    for label, runtime_schema in (("child-manifest", manifest_runtime_schema), ("terminal-ledger", terminal_runtime_schema)):
        if runtime_schema.get("additionalProperties") is not False or set(runtime_schema.get("required", [])) != {"gate_sha256", "snapshot_sha256", "trust_root"} or runtime_schema.get("properties", {}).get("trust_root", {}).get("pattern") != "[0-9a-f]{64}":
            stop("TRUST_ROOT_SCHEMA", label)
    if terminal_trust_schema.get("additionalProperties") is not False or set(terminal_trust_schema.get("required", [])) != {"T0", "T1", "T2", "T3"} or set(terminal_trust_schema.get("properties", {})) != {"T0", "T1", "T2", "T3", "T4"} or any(terminal_trust_schema.get("properties", {}).get(label, {}).get("pattern") != "[0-9a-f]{64}" for label in ("T0", "T1", "T2", "T3", "T4")):
        stop("TRUST_SNAPSHOT_SCHEMA", terminal_trust_schema)
    if set(producer_ledger["trust_snapshots"]) != {"T0", "T1", "T2", "T3"}:
        stop("T4_BEFORE_SAMPLE", sorted(producer_ledger["trust_snapshots"]))
    if set(terminal_ledger["trust_snapshots"]) != {"T0", "T1", "T2", "T3", "T4"}:
        stop("TERMINAL_T4_MISSING", sorted(terminal_ledger["trust_snapshots"]))
    verifier_schema = json_values["verifier-manifest.schema.json"]
    if len(verifier_schema["properties"]) != 11:
        stop("VERIFIER_MANIFEST_FIELDS", len(verifier_schema["properties"]))
    input_root_fields = {
        "evidence_manifest_sha256", "evidence_root_sha256", "ledger_sha256",
        "runtime_gate_sha256", "runtime_snapshot_sha256", "spec_sha256",
        "subject_manifest_sha256",
    }
    argv_schema = verifier_schema["properties"]["argv"]
    expected_argv_template = parent_module.verifier_argv_schema_instance("run_verifier.py")
    if (
        set(verifier_schema["properties"]["input_roots"]["properties"]) != input_root_fields
        or len(verifier_schema["properties"]["stdout_discipline"]["properties"]) != 3
        or len(verifier_schema["properties"]["exit_contract"]["properties"]) != 3
        or argv_schema.get("items") is not False
        or argv_schema.get("minItems") != len(expected_argv_template)
        or argv_schema.get("maxItems") != len(expected_argv_template)
        or [row.get("const") for row in argv_schema.get("prefixItems", [])] != expected_argv_template
    ):
        stop("VERIFIER_NESTED_FIELDS", "wrong")
    synthetic_verifier = {
        "argv": expected_argv_template,
        "entry_point": "run_verifier.py",
        "exit_contract": {"fail_closed": 2, "faults_found": 1, "verified": 0},
        "input_roots": {field: empty_digest for field in input_root_fields},
        "optimize": False,
        "output_path": "verifier.output.json",
        "receipt_authoritative": False,
        "receipt_path": "verifier.receipt.json",
        "schema": "rd22.verifier-manifest.v001",
        "stdout_discipline": {"format": "canonical-json", "lines": 1, "other_output_permitted": False},
        "verifier_root_sha256": empty_digest,
    }
    validate(verifier_schema, synthetic_verifier, "verifier_manifest")
    # H4 non-authoritative test fixture: copy the sealed verifier members into
    # a temporary package, synthesize the V008-shaped instance, execute the
    # parent pre-launch validator, bind the run-scoped ledger, and execute the
    # post-production carrier validator.  No verifier process is launched.
    with tempfile.TemporaryDirectory(prefix="rd22-NON_AUTHORITATIVE-V008-manifest-") as temporary:
        fixture_root = Path(temporary)
        verifier_fixture = fixture_root / "verifier-package"
        run_fixture = fixture_root / "run-root"
        verifier_fixture.mkdir()
        run_fixture.mkdir()
        verifier_source = cleanroom / "evaluator_build_B"
        verifier_member_digests = []
        for relative in expected_root_members:
            source = verifier_source / relative
            target = verifier_fixture / relative
            if not source.is_file():
                stop("DRY_RUN_VERIFIER_MEMBER", source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            verifier_member_digests.append(digest(target.read_bytes()))
        computed_verifier_root = digest("".join(verifier_member_digests).encode("utf-8"))
        subject_manifest_path = package / "inputs/subject_lineage_manifest.json"
        evidence_manifest_path = package / "inputs/structural_evidence_manifest.json"
        subject_manifest_sha256 = digest(subject_manifest_path.read_bytes())
        evidence_manifest_sha256 = digest(evidence_manifest_path.read_bytes())
        dry_expected_roots = {
            "evidence_manifest_sha256": evidence_manifest_sha256,
            "evidence_root_sha256": evidence["declared_root"],
            "runtime_gate_sha256": pin("runtime_gate"),
            "runtime_snapshot_sha256": pin("runtime_snapshot"),
            "spec_sha256": SPEC_SHA256,
            "subject_manifest_sha256": subject_manifest_sha256,
        }
        non_authoritative_fixture = {
            "argv": expected_argv_template,
            "entry_point": "run_verifier.py",
            "exit_contract": {"fail_closed": 2, "faults_found": 1, "verified": 0},
            "input_roots": {**dry_expected_roots, "ledger_sha256": "0" * 64},
            "optimize": False,
            "output_path": "verifier.output.json",
            "receipt_authoritative": False,
            "receipt_path": "verifier.receipt.json",
            "schema": "rd22.verifier-manifest.v001",
            "stdout_discipline": {"format": "canonical-json", "lines": 1, "other_output_permitted": False},
            "verifier_root_sha256": computed_verifier_root,
        }
        dry_manifest_path = verifier_fixture / "NON_AUTHORITATIVE_V008_verifier_manifest.json"
        dry_manifest_bytes = parent_module.canonical_bytes(non_authoritative_fixture)
        dry_manifest_path.write_bytes(dry_manifest_bytes)
        dry_manifest_sha256 = digest(dry_manifest_bytes)
        Path(str(dry_manifest_path) + ".seal.sha256").write_text(
            f"{dry_manifest_sha256}  {dry_manifest_path.name}\n",
            encoding="utf-8",
        )
        validated, stated, verifier_base, verifier_files = parent_module.validate_verifier_manifest(
            dry_manifest_path,
            dry_expected_roots,
            run_fixture,
            run_fixture / "verifier.output.json",
            run_fixture / "verifier.receipt.json",
        )
        if stated != dry_manifest_sha256 or verifier_base != verifier_fixture.resolve():
            stop("DRY_RUN_PRELAUNCH", {"stated": stated, "base": str(verifier_base)})
        ledger_path = run_fixture / "producer.ledger.json"
        ledger_bytes = parent_module.canonical_bytes({"fixture": "NON_AUTHORITATIVE_V008_PARENT_VALIDATION"})
        ledger_path.write_bytes(ledger_bytes)
        ledger_sha256 = digest(ledger_bytes)
        evidence_directory = run_fixture / "evidence"
        evidence_directory.mkdir()
        substitutions = {
            "${EVIDENCE_DIR}": str(evidence_directory.resolve()),
            "${EVIDENCE_MANIFEST_PATH}": str(evidence_manifest_path.resolve()),
            "${EVIDENCE_MANIFEST_SHA256}": evidence_manifest_sha256,
            "${LEDGER_PATH}": str(ledger_path.resolve()),
            "${LEDGER_SHA256}": ledger_sha256,
            "${RUNTIME_GATE_PATH}": str((cleanroom.parent / PIN_ROWS["runtime_gate"]["relative_path"]).resolve()),
            "${RUNTIME_SNAPSHOT_PATH}": str((cleanroom.parent / PIN_ROWS["runtime_snapshot"]["relative_path"]).resolve()),
            "${SPEC_PATH}": str((cleanroom.parent / PIN_ROWS["specification"]["relative_path"]).resolve()),
            "${SUBJECT_MANIFEST_PATH}": str(subject_manifest_path.resolve()),
            "${SUBJECT_MANIFEST_SHA256}": subject_manifest_sha256,
        }
        bound = parent_module.bind_verifier_launch(validated, substitutions, ledger_path, ledger_sha256)
        parent_module.post_production_verifier_validation(
            bound,
            ledger_path,
            ledger_sha256,
            subject_manifest_path,
            subject_manifest_sha256,
            evidence_manifest_path,
            evidence_manifest_sha256,
        )
        dry_command = parent_module.verifier_process_command(bound, "/pinned/python3", verifier_base, verifier_files)
        if dry_command[:5] != ["/pinned/python3", "-I", "-S", "-B", str((verifier_fixture / "run_verifier.py").resolve())]:
            stop("DRY_RUN_COMMAND", dry_command)
        parent_manifest_dry_run = "PASS"
    parent_text = (package / "parent.py").read_text(encoding="utf-8")
    verifier_stdout_block = parent_text.split("def verifier_stdout(", 1)[1].split("def run_verifier_process(", 1)[0]
    verdict_validation_receivers = {
        "VERDICT_SCHEMA_SUPPORTED_KEYWORDS = frozenset(",
        "def validate_schema_definition(",
        "def validate_verdict_document(",
        "selected_schema = validate_verdict_document(value, verdict_schema)",
        'verified_external_inputs["verifier_verdict_schema"]["data"]',
        'fail("VERDICT_SCHEMA_ROOT_BINDING"',
    }
    missing_verdict_receivers = sorted(item for item in verdict_validation_receivers if item not in parent_text)
    forbidden_verdict_transcriptions = {
        'fields = {\n        "authority_firewall", "authorization_sha256", "census", "checks_replayed"',
        'exact_keys(value, fields, "verifier output")',
    }
    present_verdict_transcriptions = sorted(item for item in forbidden_verdict_transcriptions if item in verifier_stdout_block)
    expected_schema_keywords = {"$comment", "$schema", "additionalProperties", "const", "enum", "items", "oneOf", "pattern", "properties", "required", "type"}
    if parent_module.VERDICT_SCHEMA_SUPPORTED_KEYWORDS != frozenset(expected_schema_keywords) or missing_verdict_receivers or present_verdict_transcriptions:
        stop("VERDICT_SCHEMA_RECEIVERS", {"keywords": sorted(parent_module.VERDICT_SCHEMA_SUPPORTED_KEYWORDS), "missing": missing_verdict_receivers, "transcriptions": present_verdict_transcriptions})
    root_membership_receivers = {
        "VERIFIER_ROOT_TRANSCRIBED_MEMBERS = (",
        "if len(VERIFIER_ROOT_TRANSCRIBED_MEMBERS) != 12",
        "for relative in VERIFIER_ROOT_TRANSCRIBED_MEMBERS:",
        "Contract V002 item: move this transcribed membership list into the manifest",
    }
    missing_root_receivers = sorted(item for item in root_membership_receivers if item not in parent_text)
    forbidden_root_inference = "for source_path in sorted(verifier_source.iterdir()"
    if missing_root_receivers or forbidden_root_inference in parent_text:
        stop("ROOT_MEMBERSHIP_RECEIVERS", {"missing": missing_root_receivers, "directory_inference": forbidden_root_inference in parent_text})
    authorization_forbidden = {
        "AUTHORIZATION_CONTENT",
        "Builder A               = Codex Lane 2 (parent + producer)",
        "def validate_authorization",
    }
    present_authorization_literals = sorted(item for item in authorization_forbidden if item in parent_text)
    if present_authorization_literals:
        stop("AUTHORIZATION_EXPECTATION", present_authorization_literals)
    authorization_receivers = {
        "authorization_data, authorization_artifact_sha256 = verify_bytes_with_digest(args.authorization, AUTHORIZATION_SHA256)",
        '"authorization": {"artifact_sha256": authorization_artifact_sha256, "scope": scope}',
        "verifier_stdout(verifier_data, expected_verdict, verifier_root, runtime, authorization_artifact_sha256, verdict_schema)",
    }
    missing_authorization_receivers = sorted(item for item in authorization_receivers if item not in parent_text)
    forbidden_authorization_receivers = {
        '"authorization": {"rd22_sha256": AUTHORIZATION_SHA256, "valid": True}',
        '"authorization": {"artifact_sha256": AUTHORIZATION_SHA256, "valid": True}',
        '"authorization": {"artifact_sha256": authorization_artifact_sha256, "valid": True}',
    }
    present_forbidden_authorization = sorted(item for item in forbidden_authorization_receivers if item in parent_text)
    if missing_authorization_receivers or present_forbidden_authorization:
        stop("AUTHORIZATION_FORWARD_RECEIVERS", {"missing": missing_authorization_receivers, "forbidden": present_forbidden_authorization})
    trust_sequence_tokens = (
        "t3 = trust_snapshot(runtime)",
        "producer_ledger = verdict_ledger(",
        "verifier_process = run_verifier_process(verifier_command, verifier_base)",
        "t4 = trust_snapshot(runtime)",
        "terminal = verdict_ledger(",
    )
    trust_sequence_positions = [parent_text.find(token) for token in trust_sequence_tokens]
    if any(position < 0 for position in trust_sequence_positions) or trust_sequence_positions != sorted(trust_sequence_positions):
        stop("TRUST_LABEL_SEQUENCE", dict(zip(trust_sequence_tokens, trust_sequence_positions)))
    if 'producer_trust_snapshots = {"T0": t0, "T1": t1, "T2": t2, "T3": t3}' not in parent_text or 'if "T4" in producer_trust_snapshots:' not in parent_text or 'fail("T4_BEFORE_SAMPLE"' not in parent_text or '{"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t4}' not in parent_text:
        stop("TRUST_LABEL_CARRIERS", "producer/terminal label maps missing")
    if '"T4": t3' in parent_text:
        stop("T4_BEFORE_SAMPLE", "fabricated T4 carrier remains")
    if '"evidence_root_sha256": evidence_declared_root' not in parent_text:
        stop("EVIDENCE_ROOT_BINDING", "parent does not bind verifier expectation to declared_root")
    event_payload_receivers = {
        "EVENT_LEDGER_CARRIERS = (",
        "def stage_evidence_directory(",
        "def materialize_event_payloads(",
        'target = destination / f"{digest}.json"',
        '"${EVIDENCE_DIR}": str(real_path(run_evidence_directory))',
        "child_record(args.normal_manifest_sha256",
        "child_record(args.optimized_manifest_sha256",
        "verifier-input:run-evidence-json:",
    }
    missing_event_payload_receivers = sorted(item for item in event_payload_receivers if item not in parent_text)
    forbidden_package_evidence_binding = '"${EVIDENCE_DIR}": str(real_path(package_root_declared / "inputs" / "evidence"))'
    if missing_event_payload_receivers or forbidden_package_evidence_binding in parent_text:
        stop("EVENT_PAYLOAD_RECEIVERS", {"missing": missing_event_payload_receivers, "package_binding": forbidden_package_evidence_binding in parent_text})
    consumed_evidence_receivers = {
        "def consumed_evidence_files(",
        'path = destination / f"{digest}.json"',
        '"--consumed-evidence-dir", str(run_evidence_directory)',
        "consumed_files=normal_consumed_files",
        "consumed_files=optimized_consumed_files",
        '"content_addressed_materialize"',
    }
    producer_consumed_receivers = {
        "def materialize_consumed_evidence(",
        'target = destination / f"{claimed_digest}.json"',
        'parser.add_argument("--consumed-evidence-dir", required=True)',
        'fail("CONSUMED_IMPLIES_MATERIALIZED"',
        'payload_sink(claimed_digest, verify_file(source, claimed_digest))',
    }
    missing_consumed_receivers = sorted(item for item in consumed_evidence_receivers if item not in parent_text)
    missing_producer_consumed = sorted(item for item in producer_consumed_receivers if item not in producer_source)
    if missing_consumed_receivers or missing_producer_consumed:
        stop("CONSUMED_EVIDENCE_RECEIVERS", {"parent": missing_consumed_receivers, "producer": missing_producer_consumed})
    direct_launch_receivers = {
        "def verifier_entry_target(",
        'fail("VERIFIER_ENTRY_UNCOVERED"',
        'launch_token in {"-c", "-m"}',
        'command.append(str(entry_target))',
        'verifier_process_command(bound_verifier_manifest, python, verifier_base, verifier_files)',
    }
    missing_launch_receivers = sorted(item for item in direct_launch_receivers if item not in parent_text)
    authored_module_form = ['prefix.extend(["-m"', 'command.extend(["-m"']
    present_module_form = [item for item in authored_module_form if item in parent_text]
    if missing_launch_receivers or present_module_form:
        stop("VERIFIER_DIRECT_LAUNCH", {"missing": missing_launch_receivers, "authored_module_form": present_module_form})
    path_identity_receivers = {
        "def real_path(path):",
        "def add_allowlist_entry(",
        "def alias_observation(",
        '"MODULE_NATIVE_LOADS"',
        '"OPEN_EVENTS"',
        'producer_scope["path_alias_observations"]',
        'terminal_scope["path_alias_observations"]',
    }
    missing_path_receivers = sorted(item for item in path_identity_receivers if item not in parent_text)
    if missing_path_receivers or ".resolve()" in parent_text:
        stop("PATH_IDENTITY_RECEIVERS", {"missing": missing_path_receivers, "legacy_resolve_calls": parent_text.count(".resolve()")})
    trust_receivers = {
        "def trust_root_digest(native_system_trust_root):",
        'expected_digest = trust_root_digest(runtime["native_system_trust_root"])',
        'observed_digest = trust_root_digest(observed)',
        '"trust_root": trust_root_digest(runtime["native_system_trust_root"])',
        'authorized_trust_root = trust_root_digest(runtime["native_system_trust_root"])',
        '"runtime_after_sha256": trust_after',
        '"runtime_before_sha256": trust_before',
        'producer_trust_snapshots = {"T0": t0, "T1": t1, "T2": t2, "T3": t3}',
        'if "T4" in producer_trust_snapshots:',
        '{"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t4}',
    }
    missing_trust_receivers = sorted(item for item in trust_receivers if item not in parent_text)
    forbidden_trust_receivers = {
        'runtime_subject["trust_root"] != runtime["native_system_trust_root"]',
        '"runtime_after_sha256": trust_hash(trust_after)',
        '"runtime_before_sha256": trust_hash(trust_before)',
        '"T0": trust_hash(t0)',
    }
    present_forbidden_trust = sorted(item for item in forbidden_trust_receivers if item in parent_text)
    if missing_trust_receivers or present_forbidden_trust:
        stop("TRUST_ROOT_RECEIVERS", {"missing": missing_trust_receivers, "forbidden": present_forbidden_trust})
    for fact in ("R9_VERIFIER_FAULTS_FOUND_EXIT_1", "R9_VERIFIER_FAIL_CLOSED_EXIT_2"):
        if fact not in parent_text:
            stop("VERIFIER_EXIT_FACT", fact)
    for directory in [package / "pycache/normal", package / "pycache/optimized", package / "pycache/verifier"]:
        if not directory.is_dir() or any(directory.iterdir()):
            stop("PYCACHE", directory)
    if any((package / "outputs").iterdir()):
        stop("CHAIN_OUTPUT_PRESENT", package / "outputs")
    schema_count = len(list((package / "schemas").glob("*.json")))
    print(f"SELF_CHECK_OK syntax={len(python_paths)} canonical_json=all local_schemas={schema_count} pin_manifest={len(PIN_ROWS)}:{digest(PIN_MANIFEST_PATH.read_bytes())} pin_source=generated pin_closure=value:{len(pin_closure_hits['value'])},name:{len(pin_closure_hits['name'])},total:{pin_closure_total}:PASS verifier_root_members=12 verifier_root={computed_verifier_root} root_membership_source={ROOT_MEMBERSHIP_SOURCE_SHA256} membership_in_instance_note=RECORDED_FOR_CONTRACT_V002 verdict_schema={VERDICT_SCHEMA_SHA256} b_spec_repin={b_repin_state} verdict_schema_keywords=$comment,$schema,additionalProperties,const,enum,items,oneOf,pattern,properties,required,type verdict_documents=fault:accepted,full_shape:checked negatives=old13,full_extra,fault_extra,wrong_spec:rejected inventory={len(inventory_rows)} evidence_payloads={len(payload_files)} evidence=1/56 absent=55 v009_06_opcodes=COMPARE+DAG:PASS v009_06_observed={','.join(v009_06_observed)} observed_payloads=graph+raw_span consumable_args_reproduced={consumable_args_reproduced} trace=evidence_excluded;receipt_output_digest_custody invocation_fields=opcode,result_name,args,instance_id,source_sha256,span,span_sha256 byte_span_linkage=packed+explicit+raw_span_digest consumed_implies_materialized={consumed_implies_materialized} consumed_path=run_root/evidence/<digest>.json fixture_obs=0/3 checks=66 descriptor_delta=0:V007_to_V008 descriptor_terminators_excluded={descriptor_terminators_excluded}/66 structural=56 gated=10 fixtures=6 event_payload_classes=6 event_payload_files=6(static_synthetic) empty_event_bytes=[] run_evidence_base=run_root producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 verifier_input_roots=7 verifier_argv=22:closed parent_manifest_dry_run={parent_manifest_dry_run} authorization_fields=artifact_sha256,scope authorization_digest={authorization_digest} authorization_scope=equals_ledger_scope authorization_forward=producer,terminal,verifier_receiver t_labels=producer:T0,T1,T2,T3(no_T4);terminal:T0,T1,T2,T3,T4(actual_T4) t4_before_sample_guard=PASS trust_root={trust_root} trust_sites={len(trust_site_values)} trust_agreement={','.join(trust_site_values)} exits=0/1/2 chain_invoked=false")


if __name__ == "__main__":
    main()
