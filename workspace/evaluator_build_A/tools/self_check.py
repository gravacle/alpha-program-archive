#!/usr/bin/env python3
"""Syntax/schema/inventory checks only; never launches the evaluator chain."""

import ast
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


EXPECTED_BRANCH = {
    "BRANCH-CANDIDATE-TYPED-COMPLETE": "ADMITTED",
    "BRANCH-FAILURE-UNRESOLVED": "REJECTED",
    "BRANCH-TIE-UNRESOLVED": "REJECTED",
}
OPCODES = {"STRICT", "SCHEMA", "TYPE", "EXACT", "KERNEL", "ENUM", "DOMAIN", "UNITS", "DAG", "M2", "SYMBOLIC", "SPECTRAL", "COMPARE", "RUNTIME"}
ADDENDUM_SHA256 = "d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260"
EVIDENCE_MODES = ["fixed_string", "whitespace_normalized", "self_reference_scope", "hyphen_space_underscore"]
EVIDENCE_SOURCES = {
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md": ("packet", "0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98"),
    "BID_FULL_STACK_REVIEW_LEDGER_V003.md": ("cleanroom", "c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8"),
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md": ("packet", "5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf"),
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md": ("packet", "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a"),
    "STAGE7_PACKET_MANIFEST_V001.sha256": ("packet", "9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311"),
    "STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md": ("cleanroom", "414067e25dbae39f7767d57144c953a0f98bb11d4c34178ec70097efabc0ebf7"),
    "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md": ("cleanroom", "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b"),
    "STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md": ("cleanroom", "bc6c3e496ffd6e8d06cc3237e47a6a02b76faaa88b63b0ffb38684971c2d1362"),
    "STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md": ("cleanroom", "a83289e67615d6faa2c1c942105ee6b595034f78d31fcf4e16ac5366fd1d7743"),
    "STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md": ("cleanroom", "76589e94bb4af318880c61c3d677dc2518add8480100a7afaf675e4dd3a394a8"),
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
        if "items" in schema:
            for index, child in enumerate(value):
                validate(schema["items"], child, f"{label}/{index}")
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


def descriptor_lines(spec, check_id):
    prefix = f"| `{check_id}` |"
    lines = [line for line in spec.splitlines() if line.startswith(prefix)]
    if not lines:
        stop("DESCRIPTOR_LINE", f"{check_id}:0")
    return [(line + "\n").encode("utf-8") for line in lines]


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


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    for path in sorted(package.rglob("*.py")):
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
    package_inventory = json_values["package_inventory.json"]
    parent_module = load_parent(package)
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
    child = parent_module.child_record("0" * 64, "1" * 64, 0, b"{}", b"{}", receipt, trust_root, trust_root)
    snapshots = {label: trust_root for label in ("T0", "T1", "T2", "T3", "T4")}
    synthetic_output = {"authority_firewall": {}, "checks": [], "fixtures": [], "summary": {}}
    producer_ledger = parent_module.verdict_ledger(synthetic_output, normal, {}, [child], snapshots, "2" * 64, {})
    terminal_ledger = parent_module.verdict_ledger(synthetic_output, normal, {}, [child], snapshots, "2" * 64, {})
    verifier_value = {
        "authority_firewall": {field: False for field in ("CORE_RESULT_SEAL", "FINAL_CLAIM_SEAL", "SPEC_SEAL", "alpha_computed", "kappa_record_computed", "proof_authorized")},
        "authorization_sha256": parent_module.AUTHORIZATION_SHA256,
        "census": {},
        "checks_replayed": [],
        "findings": [],
        "independence": {"expectations_source": "STATIC_SITE_AGREEMENT", "producer_code_imported": False},
        "producer_comparison": {},
        "runtime_subject": normal["runtime_subject"],
        "schema": "gravacle.a35.verifier-verdict.v1",
        "spec_sha256": parent_module.SPEC_SHA256,
        "terminal_content_sha256": "3" * 64,
        "verdict": "VERIFIED",
        "verifier_sha256": "2" * 64,
    }
    accepted_verifier = parent_module.verifier_stdout(parent_module.canonical_bytes(verifier_value), "VERIFIED", "2" * 64, snapshot)
    trust_site_values = {
        "definition": trust_root,
        "manifests": normal["runtime_subject"]["trust_root"] if optimized["runtime_subject"]["trust_root"] == trust_root else "DRIFT",
        "main_receiver": parent_module.trust_root_digest(snapshot["native_system_trust_root"]),
        "T0_T4": snapshots["T0"] if len(set(snapshots.values())) == 1 else "DRIFT",
        "child_rows": child["runtime_before_sha256"] if child["runtime_after_sha256"] == trust_root else "DRIFT",
        "producer_runtime": producer_ledger["runtime_subject"]["trust_root"],
        "producer_T0_T4": producer_ledger["trust_snapshots"]["T0"] if len(set(producer_ledger["trust_snapshots"].values())) == 1 else "DRIFT",
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
    if len(payload_files) != len(EVIDENCE_SOURCES):
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
    for check_id, record in evidence["check_records"].items():
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
    spec = (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md").read_text(encoding="utf-8")
    addendum_path = cleanroom / "STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md"
    if digest(addendum_path.read_bytes()) != ADDENDUM_SHA256:
        stop("ADDENDUM_PIN", addendum_path)
    ledger = (cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md").read_bytes()
    for row in check_map["checks"]:
        candidate_hashes = [digest(row_bytes) for row_bytes in descriptor_lines(spec, row["check_id"])]
        if candidate_hashes.count(row["descriptor_sha256"]) != 1 or row["descriptor_bytes_sha256"] != row["descriptor_sha256"]:
            stop("DESCRIPTOR_HASH", row["check_id"])
        if not row["program_contract"]:
            stop("PROGRAM_EMPTY", row["check_id"])
        for operation in row["program_contract"]:
            if operation["opcode"] not in OPCODES:
                stop("OPCODE", operation)
        if row["source"]["path"] == "BID_FULL_STACK_REVIEW_LEDGER_V003.md":
            start, end = row["source"]["byte_span"]
            if not 0 <= start < end <= len(ledger) or re.match(rb"[0-9]+\. ", ledger[start:end]) is None:
                stop("SOURCE_SPAN", row["check_id"])
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
    if normal["allowed_events"].get("mutation") != ["output", "receipt"]:
        stop("MANIFEST_MUTATION_EVENTS", normal["allowed_events"])
    schema_targets = {
        "child-manifest.schema.json": [normal, optimized],
        "check-map.schema.json": [check_map],
        "fixture-manifest.schema.json": [fixtures],
        "structural-evidence.schema.json": [evidence],
    }
    for schema_name, targets in schema_targets.items():
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False:
            stop("SCHEMA_TOP_NOT_CLOSED", schema_name)
        for index, target in enumerate(targets):
            validate(schema, target, f"{schema_name}[{index}]")
    for schema_name in ["producer-output.schema.json", "child-receipt.schema.json", "verifier-manifest.schema.json", "verifier-output.schema.json", "terminal-ledger.schema.json"]:
        schema = json_values[schema_name]
        if schema.get("additionalProperties") is not False or not schema.get("required") or set(schema["required"]) != set(schema["properties"]):
            stop("SCHEMA_EXACT_TOP", schema_name)
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
    if "mutation_event_ledger" not in receipt_schema["properties"]:
        stop("MUTATION_RECEIPT_CARRIER", "missing")
    manifest_runtime_schema = json_values["child-manifest.schema.json"]["properties"]["runtime_subject"]
    terminal_runtime_schema = terminal_schema["properties"]["runtime_subject"]
    terminal_trust_schema = terminal_schema["properties"]["trust_snapshots"]
    for label, runtime_schema in (("child-manifest", manifest_runtime_schema), ("terminal-ledger", terminal_runtime_schema)):
        if runtime_schema.get("additionalProperties") is not False or set(runtime_schema.get("required", [])) != {"gate_sha256", "snapshot_sha256", "trust_root"} or runtime_schema.get("properties", {}).get("trust_root", {}).get("pattern") != "[0-9a-f]{64}":
            stop("TRUST_ROOT_SCHEMA", label)
    if terminal_trust_schema.get("additionalProperties") is not False or set(terminal_trust_schema.get("required", [])) != {"T0", "T1", "T2", "T3", "T4"} or any(terminal_trust_schema.get("properties", {}).get(label, {}).get("pattern") != "[0-9a-f]{64}" for label in ("T0", "T1", "T2", "T3", "T4")):
        stop("TRUST_SNAPSHOT_SCHEMA", terminal_trust_schema)
    verifier_schema = json_values["verifier-manifest.schema.json"]
    if len(verifier_schema["properties"]) != 11:
        stop("VERIFIER_MANIFEST_FIELDS", len(verifier_schema["properties"]))
    if len(verifier_schema["properties"]["input_roots"]["properties"]) != 5 or len(verifier_schema["properties"]["stdout_discipline"]["properties"]) != 3 or len(verifier_schema["properties"]["exit_contract"]["properties"]) != 3:
        stop("VERIFIER_NESTED_FIELDS", "wrong")
    synthetic_verifier = {
        "argv": ["python3", "run_verifier.py", "--ledger", "/sealed/ledger.json"],
        "entry_point": "run_verifier.py",
        "exit_contract": {"fail_closed": 2, "faults_found": 1, "verified": 0},
        "input_roots": {"evidence_root_sha256": empty_digest, "ledger_sha256": empty_digest, "runtime_gate_sha256": empty_digest, "runtime_snapshot_sha256": empty_digest, "spec_sha256": empty_digest},
        "optimize": False,
        "output_path": "/run/verifier.output.json",
        "receipt_authoritative": False,
        "receipt_path": "/run/verifier.receipt.json",
        "schema": "rd22.verifier-manifest.v001",
        "stdout_discipline": {"format": "canonical-json", "lines": 1, "other_output_permitted": False},
        "verifier_root_sha256": empty_digest,
    }
    validate(verifier_schema, synthetic_verifier, "verifier_manifest")
    parent_text = (package / "parent.py").read_text(encoding="utf-8")
    authorization_forbidden = {
        "AUTHORIZATION_CONTENT",
        "Builder A               = Codex Lane 2 (parent + producer)",
        "def validate_authorization",
    }
    present_authorization_literals = sorted(item for item in authorization_forbidden if item in parent_text)
    if present_authorization_literals:
        stop("AUTHORIZATION_EXPECTATION", present_authorization_literals)
    if "verify_bytes(args.authorization, AUTHORIZATION_SHA256)" not in parent_text:
        stop("AUTHORIZATION_HASH_PIN", "missing")
    if '"evidence_root_sha256": evidence_declared_root' not in parent_text:
        stop("EVIDENCE_ROOT_BINDING", "parent does not bind verifier expectation to declared_root")
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
        '{"T0": t0, "T1": t1, "T2": t2, "T3": t3, "T4": t3}',
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
    print(f"SELF_CHECK_OK syntax=5 canonical_json=all schemas=9 inventory={len(inventory_rows)} evidence_payloads={len(payload_files)} evidence=0/56 absent=56 fixture_obs=0/3 checks=66 structural=56 gated=10 fixtures=6 producer_fields=13 receipt_fields=16 fixture_fields=16 child_fields=14 verifier_manifest_fields=11 trust_root={trust_root} trust_sites={len(trust_site_values)} trust_agreement={','.join(trust_site_values)} exits=0/1/2 chain_invoked=false")


if __name__ == "__main__":
    main()
