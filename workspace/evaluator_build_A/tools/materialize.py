#!/usr/bin/env python3
"""Materialize Builder A's closed maps, fixtures, schemas, and manifests."""

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PIN_MANIFEST_PATH = PACKAGE_ROOT / "manifests/pins.json"


def load_pins():
    data = PIN_MANIFEST_PATH.read_bytes()
    value = json.loads(data.decode("utf-8"))
    encoded = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if encoded != data or set(value) != {"pins", "schema"} or value["schema"] != "rd22.builder-a-pin-manifest.v001":
        raise SystemExit(f"MATERIALIZE_FAIL PIN_MANIFEST: {PIN_MANIFEST_PATH}")
    rows = value["pins"]
    if not isinstance(rows, list) or rows != sorted(rows, key=lambda row: row.get("kind", "")):
        raise SystemExit("MATERIALIZE_FAIL PIN_ORDER")
    by_kind = {}
    for row in rows:
        if set(row) != {"byte_length", "kind", "relative_path", "sha256"} or row["kind"] in by_kind:
            raise SystemExit(f"MATERIALIZE_FAIL PIN_ROW: {row}")
        if re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) is None:
            raise SystemExit(f"MATERIALIZE_FAIL PIN_DIGEST: {row['kind']}")
        by_kind[row["kind"]] = row
    return by_kind


PIN_ROWS = load_pins()


def pin(kind):
    row = PIN_ROWS.get(kind)
    if row is None:
        raise SystemExit(f"MATERIALIZE_FAIL PIN_KIND: {kind}")
    return row["sha256"]


SPEC_SHA = pin("specification")
AUTH_SHA = pin("authorization")
LEDGER_SHA = pin("blocker_ledger")
PACKET_SHA = pin("packet_manifest")
SNAPSHOT_SHA = pin("runtime_snapshot")
GATE_SHA = pin("runtime_gate")
ADDENDUM_SHA = pin("integration_addendum")
V011_SHA = pin("packet_v011")
SOURCE_GATE_SHA = pin("source_parent_gate")
VERDICT_SCHEMA_SHA = pin("verifier_verdict_schema")
GROUNDING_RELOCATION_SHA = pin("grounding_relocation")
GROUNDING_SOURCE_SHA = pin("grounding_source")
GROUNDING_PRECEDENCE_SHA = pin("grounding_precedence")
OPEN_CODES = ["STRICT", "SCHEMA", "TYPE", "EXACT", "KERNEL", "ENUM", "DOMAIN", "UNITS", "DAG", "M2", "SYMBOLIC", "SPECTRAL", "COMPARE", "RUNTIME"]
BRANCH_OUTCOME = {
    "BRANCH-CANDIDATE-TYPED-COMPLETE": "ADMITTED",
    "BRANCH-FAILURE-UNRESOLVED": "REJECTED",
    "BRANCH-TIE-UNRESOLVED": "REJECTED",
}


def die(code, detail):
    raise SystemExit(f"MATERIALIZE_FAIL {code}: {detail}")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def write_json(path, value):
    path.write_bytes(canonical(value))


def parent_trust_root_digest(package, native_system_trust_root):
    parent_path = package / "parent.py"
    module_spec = importlib.util.spec_from_file_location("rd22_builder_a_parent_static", parent_path)
    if module_spec is None or module_spec.loader is None:
        die("PARENT_IMPORT", parent_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    digest = module.trust_root_digest(native_system_trust_root)
    if re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        die("TRUST_ROOT_DIGEST", digest)
    return digest


def file_row(path, relative):
    data = path.read_bytes()
    return {"byte_length": len(data), "relative_path": relative, "sha256": sha(data)}


def generated_verifier_members(cleanroom):
    """Generate the V009 root-member carrier from the two sealed disclosures."""
    root_source = cleanroom / "STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md"
    integration_report = cleanroom / "STAGE8_TASK6_V008_INTEGRATION_DARIO_V001.md"
    verifier_instance = cleanroom / "evaluator_build_B/rd22.verifier-manifest.v001.json"
    verifier_package = cleanroom / "evaluator_build_B"
    for kind, path in (
        ("root_membership_source", root_source),
        ("verifier_v008_integration_report", integration_report),
        ("verifier_manifest_v008", verifier_instance),
    ):
        row = PIN_ROWS[kind]
        data = path.read_bytes()
        if len(data) != row["byte_length"] or sha(data) != row["sha256"]:
            die("VERIFIER_MEMBER_SOURCE_PIN", kind)
    root_text = root_source.read_text(encoding="utf-8")
    try:
        member_block = root_text.split("### 1.2 The member list — 12, package-relative, sorted", 1)[1].split("```text", 1)[1].split("```", 1)[0]
    except IndexError:
        die("VERIFIER_BASE_MEMBER_BLOCK", root_source)
    base_members = []
    for line in member_block.splitlines():
        match = re.match(r"^(contracts/[^ ]+|run_verifier\.py|verifier/[^ ]+\.py)", line.strip())
        if match is not None:
            base_members.append(match.group(1))
    if len(base_members) != 12 or base_members != sorted(base_members):
        die("VERIFIER_BASE_MEMBER_CENSUS", base_members)
    report_text = integration_report.read_text(encoding="utf-8")
    disclosed = sorted(set(re.findall(r"verifier/preconditions\.py", report_text)))
    if disclosed != ["verifier/preconditions.py"] or "root MEMBERSHIP 12 -> 13" not in report_text:
        die("VERIFIER_MEMBER_ADDITION_DISCLOSURE", disclosed)
    members = sorted(base_members + disclosed)
    if len(members) != 13 or len(set(members)) != 13:
        die("VERIFIER_MEMBER_CENSUS", members)
    rows = []
    for relative in members:
        path = verifier_package / relative
        if not path.is_file():
            die("VERIFIER_MEMBER_MISSING", relative)
        rows.append(file_row(path, relative))
    root = sha("".join(row["sha256"] for row in rows).encode("utf-8"))
    instance_data = verifier_instance.read_bytes()
    instance = json.loads(instance_data.decode("utf-8"))
    if canonical(instance) != instance_data or instance.get("verifier_root_sha256") != root:
        die("VERIFIER_GENERATED_ROOT", {"generated": root, "declared": instance.get("verifier_root_sha256")})
    return {"members": rows, "schema": "rd22.verifier-root-members.v001", "verifier_root_sha256": root}


def split_row(line):
    if not line.startswith("|") or not line.rstrip().endswith("|"):
        return []
    cells = []
    current = []
    escaped = False
    in_code = False
    for char in line[1:-1]:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "`":
            current.append(char)
            in_code = not in_code
        elif char == "|" and not in_code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip())
    return cells


def code_id(cell):
    value = cell.replace("**", "").strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value


def section(text, heading, next_heading):
    start = text.find(heading)
    if start < 0:
        die("SECTION", heading)
    end = text.find(next_heading, start + len(heading)) if next_heading else len(text)
    if end < 0:
        end = len(text)
    return start, end


def numbered_spans(data, start, end, count):
    chunk = data[start:end]
    starts = [match.start() + start for match in re.finditer(rb"(?m)^[0-9]+\. ", chunk)]
    if len(starts) < count:
        die("NUMBERED_SPANS", f"wanted {count}, got {len(starts)}")
    starts = starts[:count]
    spans = []
    for index, item_start in enumerate(starts):
        item_end = starts[index + 1] if index + 1 < len(starts) else end
        while item_end > item_start and data[item_end - 1:item_end] in (b"\n", b"\r"):
            item_end -= 1
        spans.append([item_start, item_end])
    return spans


def blocker_span_map(ledger_data):
    text = ledger_data.decode("utf-8")
    groups = [
        ("B-V008", 11, "## V008 immutable snapshot", "## V009 repair map"),
        ("B-V009", 13, "## V009 immutable snapshot", "## V010 repair map"),
        ("B-V010", 14, "## V010 immutable failed snapshot", "## V011 repair contract"),
        ("B-V011-MR", 9, "## V011 pre-evaluation many-record audit", "## V011 source-parent hostile audit"),
        ("B-V011-SP1", 9, "## V011 source-parent hostile audit", "## V011 source-parent second-round regression additions"),
        ("B-V011-SP2", 7, "## V011 source-parent second-round regression additions", "## Current V011 authorization"),
    ]
    out = {}
    for prefix, count, first, last in groups:
        start, end = section(text, first, last)
        spans = numbered_spans(ledger_data, start, end, count)
        for index, span in enumerate(spans, 1):
            out[f"{prefix}-{index:02d}"] = span
    if len(out) != 63:
        die("BLOCKER_SPANS", len(out))
    return out


def program_contract(procedure):
    assignment = re.compile(r"\b(r_[A-Za-z0-9_]+)\s*:=\s*([A-Z][A-Z0-9_]*)\s*\(")
    found = list(assignment.finditer(procedure))
    contracts = []
    if found:
        for match in found:
            name, opcode = match.group(1), match.group(2)
            prefix = procedure[:match.start()].lower()
            last_for = prefix.rfind("for every")
            last_break = max(prefix.rfind(";"), prefix.rfind(". "))
            repeatable = last_for > last_break
            contracts.append({"opcode": opcode, "repeatable": repeatable, "result_name": name})
    else:
        sequence = re.compile(r"\b(" + "|".join(OPEN_CODES) + r")\b")
        for index, match in enumerate(sequence.finditer(procedure), 1):
            opcode = match.group(1)
            contracts.append({"opcode": opcode, "repeatable": "every" in procedure.lower(), "result_name": f"r_auto_{index:02d}_{opcode.lower()}"})
    unique = []
    seen = set()
    for row in contracts:
        key = (row["result_name"], row["opcode"])
        if key not in seen:
            seen.add(key)
            unique.append(row)
    if not unique:
        die("PROGRAM_CONTRACT", procedure)
    for row in unique:
        if row["opcode"] not in OPEN_CODES:
            die("OPCODE", row)
    return unique


def descriptors(spec_data, ledger_data):
    span_map = blocker_span_map(ledger_data)
    spec_text = spec_data.decode("utf-8")
    rows = []
    seen = set()
    byte_cursor = 0
    line_offsets = {}
    for line in spec_text.splitlines(keepends=True):
        line_offsets[line.rstrip("\r\n")] = byte_cursor
        byte_cursor += len(line.encode("utf-8"))
    for raw in spec_text.splitlines():
        cells = split_row(raw)
        if len(cells) != 5:
            continue
        check_id = code_id(cells[0])
        if not check_id.startswith("C-") or check_id in seen:
            continue
        execution_class = code_id(cells[1])
        if execution_class not in {"STRUCTURAL", "GATED-EXECUTION"}:
            continue
        seen.add(check_id)
        if check_id.startswith("C-B-"):
            blocker_id = check_id[2:]
            source = {"byte_span": span_map[blocker_id], "path": "BID_FULL_STACK_REVIEW_LEDGER_V003.md", "sha256": LEDGER_SHA}
        else:
            blocker_id = check_id[2:]
            start = line_offsets[raw]
            source = {"byte_span": [start, start + len(raw.encode("utf-8"))], "path": "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md", "sha256": SPEC_SHA}
        procedure = cells[3]
        expected = cells[4]
        gate = "RD22_STRUCTURAL_ONLY"
        if execution_class == "GATED-EXECUTION":
            match = re.search(r"after ([^:]+):", procedure, flags=re.IGNORECASE)
            gate = match.group(1).strip() if match else "PHYSICAL_GATE"
        row_bytes = raw.encode("utf-8")
        rows.append(
            {
                "blocker_id": blocker_id,
                "check_id": check_id,
                "descriptor_bytes_sha256": sha(row_bytes),
                "descriptor_sha256": sha(row_bytes),
                "deterministic_procedure": procedure,
                "execution_class": execution_class,
                "expected_predicate": expected,
                "inputs": cells[2],
                "program_contract": program_contract(procedure),
                "required_gate": gate,
                "source": source,
            }
        )
    if len(rows) != 66 or len(seen) != 66:
        die("DESCRIPTOR_COUNT", len(rows))
    if sum(row["execution_class"] == "STRUCTURAL" for row in rows) != 56:
        die("STRUCTURAL_COUNT", "not 56")
    if sum(row["execution_class"] == "GATED-EXECUTION" for row in rows) != 10:
        die("GATED_COUNT", "not 10")
    return rows


def fixture_rows(spec_data, check_rows):
    definitions = [
        ("FX-A35-01-V010-ZERO-STIFFNESS", ["C-B-V010-01"], "GATED-EXECUTION", ["POST_HOC_L2", "POST_HOC_L4", "POST_HOC_VOLUME"], {"after_the_fact_factor_accepted": False, "competitor_reproduced": True, "physical_response_accepted": False}),
        ("FX-A35-02-ROOT-SURVIVAL-ZERO", ["C-B-V011-MR-08"], "GATED-EXECUTION", ["AUTO_SUBSTITUTION"], {"alternate_amplitude_auto_selected": False, "response_subject_accepted": False, "zero_reproduced": True}),
        ("FX-A35-03-C-FAMILY", ["C-B-V010-02"], "STRUCTURAL", ["C_EQUALS_ONE_SELECTION"], {"c_equals_one_selected": False, "family_admitted": True}),
        ("FX-A35-04-TAU-FAMILY", ["C-B-V010-03"], "STRUCTURAL", ["TAU_EQUALS_ONE_SELECTION"], {"family_admitted": True, "tau_equals_one_derived": False}),
        ("FX-A35-05-PRIMITIVE-THOMSON-CONFLATION", ["C-B-V010-04"], "STRUCTURAL", ["PRIMITIVE_TO_THOMSON_FIELD"], {"competitor_accepted": False, "primitive_and_Thomson_fields_remain_distinct": True, "type_violation_detected": True}),
        ("FX-A35-06-NONZERO-INDEX-CONTROL", ["C-B-V011-SP1-04", "C-B-V011-SP2-03", "C-D-A35-01-ZERO-INDEX"], "GATED-EXECUTION", ["REPHASING", "HAND_INSERTED_PAIRING"], {"axial_sign_equivalence": False, "control_rejected": True, "hand_inserted_pairing_mutation_fails": True, "rephasing_mutation_fails": True}),
    ]
    by_check = {row["check_id"]: row for row in check_rows}
    spec_text = spec_data.decode("utf-8")
    offsets = {}
    cursor = 0
    for raw in spec_text.splitlines(keepends=True):
        line = raw.rstrip("\r\n")
        offsets.setdefault(line, cursor)
        cursor += len(raw.encode("utf-8"))
    out = []
    for fixture_id, primary_ids, execution_class, mutation_ids, expected in definitions:
        prefix = f"| `{fixture_id}` |"
        matches = [line for line in spec_text.splitlines() if line.startswith(prefix)]
        if len(matches) != 1:
            die("FIXTURE_SOURCE_ROW", f"{fixture_id}:{len(matches)}")
        row_text = matches[0]
        row_bytes = (row_text + "\n").encode("utf-8")
        start = offsets[row_text]
        primary = [by_check[item] for item in primary_ids]
        gates = sorted({item["required_gate"] for item in primary})
        out.append(
            {
                "deterministic_procedure": " ; ".join(f"{item['check_id']}:{item['deterministic_procedure']}" for item in primary),
                "execution_class": execution_class,
                "expected_verdict_fields": expected,
                "fixture_id": fixture_id,
                "fixture_spec_sha256": sha(row_bytes),
                "mutation_ids": mutation_ids,
                "prerequisites": ["P0"],
                "primary_check_ids": primary_ids,
                "required_gate": "RD22_STRUCTURAL_ONLY" if execution_class == "STRUCTURAL" else " AND ".join(gates),
                "source": {"byte_span": [start, start + len(row_bytes)], "path": "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md", "sha256": SPEC_SHA},
            }
        )
    return out


def schemas():
    string = {"type": "string"}
    integer = {"type": "integer"}
    digest = {"pattern": "[0-9a-f]{64}", "type": "string"}
    object_value = {"type": "object"}
    string_array = {"items": string, "type": "array"}
    object_array = {"items": object_value, "type": "array"}

    def closed(properties):
        return {"additionalProperties": False, "properties": properties, "required": sorted(properties), "type": "object"}

    payload_row = closed({"byte_length": {"minimum": 0, "type": "integer"}, "relative_path": string, "sha256": digest})
    pin_row = closed({"byte_length": {"minimum": 0, "type": "integer"}, "kind": string, "relative_path": string, "sha256": digest})
    verifier_member_row = closed({"byte_length": {"minimum": 0, "type": "integer"}, "relative_path": string, "sha256": digest})
    subject_resolution = closed({
        "evidence_payload_path": string,
        "evidence_payload_sha256": digest,
        "subject_byte_length": {"minimum": 0, "type": "integer"},
        "subject_relative_path": string,
        "subject_sha256": digest,
    })
    source = closed({"byte_span": {"items": integer, "type": "array"}, "path": string, "sha256": digest})
    invocation = {
        "oneOf": [
            {"type": "null"},
            closed(
                {
                    "args": object_value,
                    "instance_id": string,
                    "opcode": string,
                    "result_name": string,
                    "source_sha256": digest,
                    "span": {"items": integer, "maxItems": 2, "minItems": 2, "type": "array"},
                    "span_sha256": digest,
                }
            ),
        ]
    }
    check_row = closed(
        {
            "blocker_id": string,
            "check_id": string,
            "check_spec_sha256": digest,
            "deterministic_procedure": string,
            "execution_class": {"enum": ["STRUCTURAL", "GATED-EXECUTION"], "type": "string"},
            "expected_predicate": string,
            "input_root_sha256": digest,
            "invocation": invocation,
            "observed_evidence_sha256s": {"items": digest, "type": "array"},
            "prerequisites": string_array,
            "procedure_started": {"type": "boolean"},
            "reason": string,
            "required_gate": string,
            "source": source,
            "status": {"enum": ["PASS", "FAIL", "NOT_RUN_GATE", "ERROR"], "type": "string"},
        }
    )
    fixture_descriptor = closed(
        {
            "deterministic_procedure": string,
            "execution_class": {"enum": ["STRUCTURAL", "GATED-EXECUTION"], "type": "string"},
            "expected_verdict_fields": object_value,
            "fixture_id": string,
            "fixture_spec_sha256": digest,
            "mutation_ids": string_array,
            "prerequisites": string_array,
            "primary_check_ids": string_array,
            "required_gate": string,
            "source": source,
        }
    )
    fixture_row = closed(
        {
            "deterministic_procedure": string,
            "execution_class": {"enum": ["STRUCTURAL", "GATED-EXECUTION"], "type": "string"},
            "expected_verdict_fields": object_value,
            "fixture_id": string,
            "fixture_spec_sha256": digest,
            "input_root_sha256": digest,
            "mutation_ids": string_array,
            "observed_evidence_sha256s": {"items": digest, "type": "array"},
            "observed_verdict_fields": object_value,
            "prerequisites": string_array,
            "primary_check_ids": string_array,
            "procedure_started": {"type": "boolean"},
            "reason": string,
            "required_gate": string,
            "source": source,
            "status": {"enum": ["PASS", "FAIL", "NOT_RUN_GATE", "ERROR"], "type": "string"},
        }
    )
    child_row = closed(
        {
            "manifest_sha256": digest,
            "module_ledger_sha256": digest,
            "mutation_event_ledger_sha256": digest,
            "native_ledger_sha256": digest,
            "network_event_ledger_sha256": digest,
            "open_event_ledger_sha256": digest,
            "optimize": {},
            "output_sha256": digest,
            "process_event_ledger_sha256": digest,
            "receipt_authoritative": {"const": False, "type": "boolean"},
            "receipt_sha256": digest,
            "runtime_after_sha256": digest,
            "runtime_before_sha256": digest,
            "target_sha256": digest,
        }
    )
    runtime_subject = closed({"gate_sha256": digest, "snapshot_sha256": digest, "trust_root": digest})
    trust_snapshots = {
        "additionalProperties": False,
        "properties": {"T0": digest, "T1": digest, "T2": digest, "T3": digest, "T4": digest},
        "required": ["T0", "T1", "T2", "T3"],
        "type": "object",
    }
    authorization_record = closed({"artifact_sha256": digest, "scope": object_value})
    verifier_input_roots = closed({"evidence_manifest_sha256": digest, "evidence_root_sha256": digest, "ledger_sha256": digest, "runtime_gate_sha256": digest, "runtime_snapshot_sha256": digest, "spec_sha256": digest, "subject_manifest_sha256": digest})
    verifier_argv = {
        "items": False,
        "maxItems": 22,
        "minItems": 22,
        "prefixItems": [
            {"const": "python3"}, {"const": "run_verifier.py"},
            {"const": "--spec"}, {"const": "${SPEC_PATH}"},
            {"const": "--ledger"}, {"const": "${LEDGER_PATH}"},
            {"const": "--ledger-sha256"}, {"const": "${LEDGER_SHA256}"},
            {"const": "--evidence-dir"}, {"const": "${EVIDENCE_DIR}"},
            {"const": "--runtime-snapshot"}, {"const": "${RUNTIME_SNAPSHOT_PATH}"},
            {"const": "--runtime-gate"}, {"const": "${RUNTIME_GATE_PATH}"},
            {"const": "--subject-manifest"}, {"const": "${SUBJECT_MANIFEST_PATH}"},
            {"const": "--subject-manifest-sha256"}, {"const": "${SUBJECT_MANIFEST_SHA256}"},
            {"const": "--evidence-manifest"}, {"const": "${EVIDENCE_MANIFEST_PATH}"},
            {"const": "--evidence-manifest-sha256"}, {"const": "${EVIDENCE_MANIFEST_SHA256}"},
        ],
        "type": "array",
    }
    stdout_discipline = closed({"format": {"const": "canonical-json", "type": "string"}, "lines": {"const": 1, "type": "integer"}, "other_output_permitted": {"const": False, "type": "boolean"}})
    exit_contract = closed({"fail_closed": {"const": 2, "type": "integer"}, "faults_found": {"const": 1, "type": "integer"}, "verified": {"const": 0, "type": "integer"}})
    manifest_fields = {
        "allowed_events": object_value,
        "authority_firewall": object_value,
        "branch_outcome": object_value,
        "check_ids": string_array,
        "check_map_sha256": digest,
        "evidence_manifest_sha256": digest,
        "external_inputs": object_array,
        "fixture_ids": string_array,
        "fixture_manifest_sha256": digest,
        "mode": {"enum": ["normal", "optimized"], "type": "string"},
        "optimization": integer,
        "package_files": object_array,
        "runtime_subject": runtime_subject,
        "schema": {"const": "rd22.child-manifest.v001", "type": "string"},
        "specification_sha256": digest,
        "subject_lineage_root": digest,
        "writable_paths": string_array,
    }
    return {
        "child-manifest.schema.json": {
            "$id": "rd22.child-manifest.v001", "additionalProperties": False,
            "properties": manifest_fields, "required": sorted(manifest_fields), "type": "object",
            "x-nested-exact-fields-enforced-by": "parent.py:parse_manifest and verify_package_inventory",
        },
        "check-map.schema.json": {
            "$id": "rd22.check-map.v001", "additionalProperties": False,
            "properties": {"branch_outcome": object_value, "check_ids": {"items": string, "type": "array"}, "checks": {"items": object_value, "type": "array"}, "descriptor_convention": string, "schema": string, "spec_sha256": digest},
            "required": ["branch_outcome", "check_ids", "checks", "descriptor_convention", "schema", "spec_sha256"], "type": "object",
        },
        "fixture-manifest.schema.json": {
            "$id": "rd22.fixture-manifest.v001", "additionalProperties": False,
            "properties": {"fixture_ids": string_array, "fixtures": {"items": fixture_descriptor, "type": "array"}, "schema": {"const": "rd22.fixture-manifest.v001", "type": "string"}, "spec_sha256": digest},
            "required": ["fixture_ids", "fixtures", "schema", "spec_sha256"], "type": "object",
        },
        "structural-evidence.schema.json": {
            "$id": "rd22.structural-evidence-manifest.v001", "additionalProperties": False,
            "properties": {"check_records": object_value, "declared_root": digest, "fixture_records": object_value, "payload_inventory": {"items": payload_row, "type": "array"}, "schema": string, "subject_lineage_root": digest},
            "required": ["check_records", "declared_root", "fixture_records", "payload_inventory", "schema", "subject_lineage_root"], "type": "object",
        },
        "pin-manifest.schema.json": {
            "$id": "rd22.builder-a-pin-manifest.v001", "additionalProperties": False,
            "properties": {"pins": {"items": pin_row, "type": "array"}, "schema": {"const": "rd22.builder-a-pin-manifest.v001", "type": "string"}},
            "required": ["pins", "schema"], "type": "object",
        },
        "subject-resolution.schema.json": {
            "$id": "rd22.subject-evidence-resolution.v001", **subject_resolution,
        },
        "verifier-root-members.schema.json": {
            "$id": "rd22.verifier-root-members.v001", "additionalProperties": False,
            "properties": {"members": {"items": verifier_member_row, "minItems": 1, "type": "array"}, "schema": {"const": "rd22.verifier-root-members.v001", "type": "string"}, "verifier_root_sha256": digest},
            "required": ["members", "schema", "verifier_root_sha256"], "type": "object",
        },
        "producer-output.schema.json": {
            "$id": "rd22.producer-output.v001", "additionalProperties": False,
            "properties": {"authority_firewall": object_value, "check_map_sha256": digest, "checks": {"items": check_row, "type": "array"}, "fixture_manifest_sha256": digest, "fixtures": {"items": fixture_row, "type": "array"}, "monotonic_duration": {"type": "number"}, "process_id": integer, "python_optimize": integer, "schema": {"const": "rd22.producer-output.v001", "type": "string"}, "scope": object_value, "spec_sha256": digest, "subject_lineage_root": digest, "summary": object_value},
            "required": ["authority_firewall", "check_map_sha256", "checks", "fixture_manifest_sha256", "fixtures", "monotonic_duration", "process_id", "python_optimize", "schema", "scope", "spec_sha256", "subject_lineage_root", "summary"], "type": "object",
        },
        "child-receipt.schema.json": {
            "$id": "rd22.child-receipt.v001", "additionalProperties": False,
            "properties": {"authority": {"const": False, "type": "boolean"}, "environment_event_ledger": object_array, "manifest_sha256": digest, "module_ledger": object_array, "monotonic_duration": {"type": "number"}, "mutation_event_ledger": object_array, "native_ledger": object_array, "network_event_ledger": object_array, "open_event_ledger": object_array, "optimize": {}, "output_sha256": digest, "process_event_ledger": object_array, "process_id": integer, "schema": {"const": "rd22.child-receipt.v001", "type": "string"}, "target_sha256": digest, "write_event_ledger": object_array},
            "required": ["authority", "environment_event_ledger", "manifest_sha256", "module_ledger", "monotonic_duration", "mutation_event_ledger", "native_ledger", "network_event_ledger", "open_event_ledger", "optimize", "output_sha256", "process_event_ledger", "process_id", "schema", "target_sha256", "write_event_ledger"], "type": "object",
        },
        "verifier-manifest.schema.json": {
            "$id": "rd22.verifier-manifest.v001", "additionalProperties": False,
            "properties": {"argv": verifier_argv, "entry_point": string, "exit_contract": exit_contract, "input_roots": verifier_input_roots, "optimize": {"type": "boolean"}, "output_path": string, "receipt_authoritative": {"const": False, "type": "boolean"}, "receipt_path": string, "schema": {"const": "rd22.verifier-manifest.v001", "type": "string"}, "stdout_discipline": stdout_discipline, "verifier_root_members": {"items": verifier_member_row, "minItems": 1, "type": "array"}, "verifier_root_sha256": digest},
            "required": ["argv", "entry_point", "exit_contract", "input_roots", "optimize", "output_path", "receipt_authoritative", "receipt_path", "schema", "stdout_discipline", "verifier_root_members", "verifier_root_sha256"], "type": "object",
        },
        "terminal-ledger.schema.json": {
            "$id": "rd22.terminal-ledger.v001", "additionalProperties": False,
            "properties": {"authorization": authorization_record, "authority_firewall": object_value, "check_map_sha256": digest, "checks": object_array, "children": {"items": child_row, "type": "array"}, "fixture_manifest_sha256": digest, "fixtures": {"items": fixture_row, "type": "array"}, "producer_comparison": object_value, "runner_sha256": digest, "runtime_subject": runtime_subject, "schema": {"const": "rd22.terminal-ledger.v001", "type": "string"}, "scope": object_value, "spec_sha256": digest, "subject_lineage": object_value, "summary": object_value, "terminal_content_sha256": digest, "trust_snapshots": trust_snapshots, "verifier_sha256": digest},
            "required": ["authorization", "authority_firewall", "check_map_sha256", "checks", "children", "fixture_manifest_sha256", "fixtures", "producer_comparison", "runner_sha256", "runtime_subject", "schema", "scope", "spec_sha256", "subject_lineage", "summary", "terminal_content_sha256", "trust_snapshots", "verifier_sha256"], "type": "object",
        },
    }


def content_root(entries):
    records = [f"{row['relative_path']}\0{row['byte_length']}\0{row['sha256']}\n" for row in entries]
    return sha(b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8"))


def build_v009_06_record(evidence_dir, source_path, descriptor):
    source_data = source_path.read_bytes()
    if sha(source_data) != GROUNDING_SOURCE_SHA:
        die("V009_06_SOURCE_PIN", sha(source_data))
    member_span = [18898, 19830]
    value_span = [18920, 19830]
    member_data = source_data[member_span[0]:member_span[1]]
    value_data = source_data[value_span[0]:value_span[1]]
    member_sha = sha(member_data)
    value_sha = sha(value_data)
    if len(member_data) != 932:
        die("V009_06_MEMBER", {"length": len(member_data), "sha256": sha(member_data)})
    if len(value_data) != 910:
        die("V009_06_VALUE", {"length": len(value_data), "sha256": sha(value_data)})
    try:
        stage_dependencies = json.loads(value_data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        die("V009_06_PARSE", exc)
    if not isinstance(stage_dependencies, dict) or len(stage_dependencies) != 11:
        die("V009_06_GRAPH", type(stage_dependencies).__name__)
    dag_args = {"authority": "PRINCIPAL_SINGLE_AUTHORITY", "graph": stage_dependencies}
    dag_args_data = canonical(dag_args)
    args_sha = sha(dag_args_data)
    if set(dag_args) != {"authority", "graph"}:
        die("V009_06_ARGS", sha(dag_args_data))
    if b"stage_dag" in member_data or b"status" in member_data or b"stage_dag" in dag_args_data or b"status" in dag_args_data:
        die("V009_06_BARRED_FIELD", "alternate encoding or status")
    member_name = f"{member_sha}--C-B-V009-06-stage_dependencies.member"
    args_name = f"{args_sha}--C-B-V009-06-dag-args.json"
    member_path = evidence_dir / member_name
    args_path = evidence_dir / args_name
    member_path.write_bytes(member_data)
    args_path.write_bytes(dag_args_data)
    input_files = sorted(
        [file_row(member_path, member_name), file_row(args_path, args_name)],
        key=lambda row: row["relative_path"],
    )
    evidence = {
        "descriptor_sha256": descriptor["descriptor_sha256"],
        "input_files": input_files,
        "input_root_sha256": content_root(input_files),
        "invocations": [
            {
                "args": {"left": member_sha, "mask": [], "right": member_sha},
                "instance_id": None,
                "opcode": "COMPARE",
                "result_name": "r_ground",
            },
            {
                "args": dag_args,
                "instance_id": "stage_dependencies@13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd:[18898,19830)",
                "opcode": "DAG",
                "result_name": "r_dag",
            }
        ],
    }
    return {
        "available": True,
        "descriptor_sha256": descriptor["descriptor_sha256"],
        "evidence": evidence,
        "grounding_citations": [
            {
                "authority_path": "STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md",
                "authority_sha256": GROUNDING_RELOCATION_SHA,
                "precedence_path": "supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md",
                "precedence_sha256": GROUNDING_PRECEDENCE_SHA,
                "source_path": "provenance/boundary_incidence_dynamics_preregistration_v011.json",
                "source_sha256": GROUNDING_SOURCE_SHA,
                "span": member_span,
                "span_sha256": member_sha,
                "value_span": value_span,
                "value_sha256": value_sha,
            }
        ],
        "payloads": [
            {"byte_length": len(member_data), "payload_path": f"inputs/evidence/{member_name}", "payload_sha256": member_sha, "role": "EXACT_RELOCATED_MEMBER_BYTES"},
            {"byte_length": len(dag_args_data), "derived_from_sha256": value_sha, "payload_path": f"inputs/evidence/{args_name}", "payload_sha256": args_sha, "role": "CANONICAL_DAG_ARGUMENTS"},
        ],
        "status": "AVAILABLE",
    }


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    program = cleanroom.parent
    spec_path = cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md"
    ledger_path = cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md"
    packet_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256"
    v011_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
    source_gate_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_SOURCE_PARENT_CLOSURE_GATE_V003.md"
    runtime_snapshot_path = program / "provenance/primitive_step6_runtime_snapshot_v012.json"
    runtime_gate_path = program / "primitive_step6_content_addressed_runtime_gate_v010.md"
    addendum_path = cleanroom / "STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md"
    relocation_path = cleanroom / "STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md"
    grounding_source_path = cleanroom / "provenance/boundary_incidence_dynamics_preregistration_v011.json"
    precedence_path = Path("/Users/bgm/MB Work/alpha-program-archive/supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md")
    authorization_path = Path("/Users/bgm/MB Work/alpha-program-archive/supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md")
    verdict_schema_path = cleanroom / "evaluator_build_B/contracts/verifier_verdict.schema.json"
    pin_sources = {
        "specification": spec_path,
        "integration_addendum": addendum_path,
        "grounding_relocation": relocation_path,
        "grounding_source": grounding_source_path,
        "grounding_precedence": precedence_path,
        "blocker_ledger": ledger_path,
        "packet_manifest": packet_path,
        "packet_v011": v011_path,
        "source_parent_gate": source_gate_path,
        "runtime_snapshot": runtime_snapshot_path,
        "runtime_gate": runtime_gate_path,
        "authorization": authorization_path,
        "verifier_verdict_schema": verdict_schema_path,
    }
    for kind, path in pin_sources.items():
        row = PIN_ROWS[kind]
        data = path.read_bytes()
        if len(data) != row["byte_length"] or sha(data) != row["sha256"]:
            die("PIN", f"{kind}:{path}:{sha(data)}")
    rows = descriptors(spec_path.read_bytes(), ledger_path.read_bytes())
    check_map = {
        "branch_outcome": BRANCH_OUTCOME,
        "check_ids": [row["check_id"] for row in rows],
        "checks": rows,
        "descriptor_convention": "SHA256 of the exact UTF-8 Markdown descriptor row excluding its line terminator",
        "schema": "rd22.check-map.v001",
        "spec_sha256": SPEC_SHA,
    }
    write_json(package / "checks/check_map.json", check_map)
    fixtures = fixture_rows(spec_path.read_bytes(), rows)
    fixture_manifest = {"fixture_ids": [row["fixture_id"] for row in fixtures], "fixtures": fixtures, "schema": "rd22.fixture-manifest.v001", "spec_sha256": SPEC_SHA}
    write_json(package / "fixtures/fixture_manifest.json", fixture_manifest)
    for name, value in schemas().items():
        write_json(package / "schemas" / name, value)
    subject_entries = []
    subject_paths = [
        spec_path,
        ledger_path,
        packet_path,
        v011_path,
        source_gate_path,
        addendum_path,
    ]
    for path in subject_paths:
        relative = str(path.relative_to(program))
        subject_entries.append(file_row(path, relative))
    subject = {"declared_root": content_root(subject_entries), "files": sorted(subject_entries, key=lambda item: item["relative_path"]), "schema": "rd22.subject-lineage-manifest.v001"}
    write_json(package / "inputs/subject_lineage_manifest.json", subject)
    verifier_members = generated_verifier_members(cleanroom)
    write_json(package / "inputs/verifier_root_members.generated.json", verifier_members)
    structural_ids = [row["check_id"] for row in rows if row["execution_class"] == "STRUCTURAL"]
    structural_fixture_ids = [row["fixture_id"] for row in fixtures if row["execution_class"] == "STRUCTURAL"]
    evidence_dir = package / "inputs/evidence"
    spec_payload_name = f"{SPEC_SHA}--STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md"
    (evidence_dir / spec_payload_name).write_bytes(spec_path.read_bytes())
    addendum_payload_name = f"{ADDENDUM_SHA}--{addendum_path.name}"
    (evidence_dir / addendum_payload_name).write_bytes(addendum_path.read_bytes())
    row_by_id = {row["check_id"]: row for row in rows}
    v009_06_record = build_v009_06_record(evidence_dir, grounding_source_path, row_by_id["C-B-V009-06"])
    payload_inventory = [file_row(path, path.name) for path in sorted(evidence_dir.iterdir()) if path.is_file()]
    declared_evidence_root = content_root(payload_inventory)
    evidence_path = package / "inputs/structural_evidence_manifest.json"
    if evidence_path.is_file():
        evidence_data = evidence_path.read_bytes()
        evidence = json.loads(evidence_data.decode("utf-8"))
        if canonical(evidence) != evidence_data:
            die("EVIDENCE_CANONICAL", evidence_path)
        if set(evidence) != {"check_records", "declared_root", "fixture_records", "payload_inventory", "schema", "subject_lineage_root"}:
            die("EVIDENCE_FIELDS", sorted(evidence))
        if set(evidence["check_records"]) != set(structural_ids) or set(evidence["fixture_records"]) != set(structural_fixture_ids):
            die("EVIDENCE_CENSUS", "check/fixture IDs")
        for check_id in structural_ids:
            evidence["check_records"][check_id]["descriptor_sha256"] = row_by_id[check_id]["descriptor_sha256"]
        fixture_by_id = {row["fixture_id"]: row for row in fixtures}
        for fixture_id in structural_fixture_ids:
            fixture_record = evidence["fixture_records"][fixture_id]
            fixture = fixture_by_id[fixture_id]
            fixture_record["fixture_spec_sha256"] = fixture["fixture_spec_sha256"]
            fixture_record["partial_payloads"] = [
                {
                    "payload_path": f"inputs/evidence/{spec_payload_name}",
                    "payload_sha256": SPEC_SHA,
                    "role": "SPEC_FIXED_SUBJECT_NOT_OBSERVATION",
                    "source_path": "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md",
                    "source_sha256": SPEC_SHA,
                    "span": fixture["source"]["byte_span"],
                }
            ]
        if evidence["schema"] != "rd22.structural-evidence-manifest.v001":
            die("EVIDENCE_BINDING", "schema")
    else:
        evidence = {
            "check_records": {check_id: {"available": False, "reason": "NO_CONTENT_ADDRESSED_EVIDENCE_RECORD_PRESENT_IN_GOVERNING_INPUT_SET"} for check_id in structural_ids},
            "declared_root": declared_evidence_root,
            "fixture_records": {fixture_id: {"available": False, "reason": "NO_CONTENT_ADDRESSED_FIXTURE_OBSERVATION_PRESENT_IN_GOVERNING_INPUT_SET"} for fixture_id in structural_fixture_ids},
            "payload_inventory": payload_inventory,
            "schema": "rd22.structural-evidence-manifest.v001",
            "subject_lineage_root": subject["declared_root"],
        }
    evidence["check_records"]["C-B-V009-06"] = v009_06_record
    evidence["declared_root"] = declared_evidence_root
    evidence["payload_inventory"] = payload_inventory
    evidence["subject_lineage_root"] = subject["declared_root"]
    write_json(package / "inputs/structural_evidence_manifest.json", evidence)
    evidence_payload_relatives = [f"inputs/evidence/{row['relative_path']}" for row in payload_inventory]
    runtime_relatives = [
        "parent.py", "producer.py", "checks/check_map.json", "fixtures/fixture_manifest.json",
        "inputs/structural_evidence_manifest.json", "inputs/subject_lineage_manifest.json", "inputs/verifier_root_members.generated.json", "manifests/pins.json",
    ] + evidence_payload_relatives + [f"schemas/{name}" for name in sorted(schemas())]
    package_rows = [file_row(package / relative, relative) for relative in runtime_relatives]
    external = [
        {**file_row(authorization_path, "supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md"), "kind": "authorization"},
        {**file_row(ledger_path, str(ledger_path.relative_to(program))), "kind": "blocker_ledger"},
        {**file_row(addendum_path, str(addendum_path.relative_to(program))), "kind": "integration_addendum"},
        {**file_row(packet_path, str(packet_path.relative_to(program))), "kind": "packet_manifest"},
        {**file_row(runtime_gate_path, str(runtime_gate_path.relative_to(program))), "kind": "runtime_gate"},
        {**file_row(runtime_snapshot_path, str(runtime_snapshot_path.relative_to(program))), "kind": "runtime_snapshot"},
        {**file_row(spec_path, str(spec_path.relative_to(program))), "kind": "specification"},
        {**file_row(verdict_schema_path, str(verdict_schema_path.relative_to(program))), "kind": "verifier_verdict_schema"},
    ]
    native_system_trust_root = json.loads(runtime_snapshot_path.read_text(encoding="utf-8"))["native_system_trust_root"]
    trust_root = parent_trust_root_digest(package, native_system_trust_root)
    common = {
        "allowed_events": {"environment": [], "mutation": ["consumed_evidence", "output", "receipt"], "network": [], "process": [], "writes": ["consumed_evidence", "output", "receipt"]},
        "authority_firewall": {"CORE_RESULT_SEAL": False, "FINAL_CLAIM_SEAL": False, "SPEC_SEAL": False, "alpha_computed": False, "authorization_claimed": False, "executed": False, "implemented": True, "kappa_record_computed": False, "proof_authorized": False},
        "branch_outcome": BRANCH_OUTCOME,
        "check_ids": check_map["check_ids"],
        "check_map_sha256": sha((package / "checks/check_map.json").read_bytes()),
        "evidence_manifest_sha256": sha((package / "inputs/structural_evidence_manifest.json").read_bytes()),
        "external_inputs": external,
        "fixture_ids": fixture_manifest["fixture_ids"],
        "fixture_manifest_sha256": sha((package / "fixtures/fixture_manifest.json").read_bytes()),
        "package_files": package_rows,
        "runtime_subject": {"gate_sha256": GATE_SHA, "snapshot_sha256": SNAPSHOT_SHA, "trust_root": trust_root},
        "schema": "rd22.child-manifest.v001",
        "specification_sha256": SPEC_SHA,
        "subject_lineage_root": subject["declared_root"],
    }
    normal = {**common, "mode": "normal", "optimization": 0, "writable_paths": ["evidence/<observed_sha256>.json", "normal.output.json", "normal.receipt.json"]}
    optimized = {**common, "mode": "optimized", "optimization": 1, "writable_paths": ["evidence/<observed_sha256>.json", "optimized.output.json", "optimized.receipt.json"]}
    write_json(package / "manifests/normal.json", normal)
    write_json(package / "manifests/optimized.json", optimized)
    inventory_files = []
    for path in sorted(package.rglob("*")):
        if path.is_file() and not any(part in {"outputs", "pycache"} for part in path.relative_to(package).parts):
            if path.relative_to(package).as_posix() == "manifests/package_inventory.json":
                continue
            inventory_files.append(file_row(path, str(path.relative_to(package))))
    inventory = {"files": inventory_files, "schema": "rd22.builder-a-package-inventory.v001"}
    write_json(package / "manifests/package_inventory.json", inventory)
    print(json.dumps({"checks": len(rows), "gated": 10, "structural": 56, "fixtures": len(fixtures), "subject_lineage_root": subject["declared_root"], "normal_sha256": sha((package / "manifests/normal.json").read_bytes()), "optimized_sha256": sha((package / "manifests/optimized.json").read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
