#!/usr/bin/env python3
"""Materialize Builder A's closed maps, fixtures, schemas, and manifests."""

import hashlib
import json
import re
import sys
from pathlib import Path


SPEC_SHA = "f8d1a7dc02798229f0ea22b0e855d1d09bb4a5b7eea9069c419357a56b6a067b"
AUTH_SHA = "ff84c4a8ba5c7f8eabfbcc587475d3a5050c21d758a2788c5b9e28b7ee022340"
LEDGER_SHA = "c09f2c246c48ddfd0df127da26a22f08ba9ffd44f5c2118c178a0a5eba5d00e8"
PACKET_SHA = "9d35f4ed7831411961d61002f09afe02c9703f80b84aa05158e39b7f49b1a311"
SNAPSHOT_SHA = "50a6fc141a45451678aa7543e4f267ce26beb6e53182170b478acb6fb0e0f5bb"
GATE_SHA = "2ad7f72a88184c11e1253f2c47598fca11e60d05e8e71a26db4e19b16bf98d42"
ADDENDUM_SHA = "d17c5e79986bea431dec0b572019096f9c059bcc43876fda9134abc96ce0f260"
V011_SHA = "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a"
SOURCE_GATE_SHA = "5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf"
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


def file_row(path, relative):
    data = path.read_bytes()
    return {"byte_length": len(data), "relative_path": relative, "sha256": sha(data)}


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
            source = {"byte_span": [start, start + len((raw + "\n").encode("utf-8"))], "path": "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md", "sha256": SPEC_SHA}
        procedure = cells[3]
        expected = cells[4]
        gate = "RD22_STRUCTURAL_ONLY"
        if execution_class == "GATED-EXECUTION":
            match = re.search(r"after ([^:]+):", procedure, flags=re.IGNORECASE)
            gate = match.group(1).strip() if match else "PHYSICAL_GATE"
        row_bytes = (raw + "\n").encode("utf-8")
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
                "source": {"byte_span": [start, start + len(row_bytes)], "path": "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md", "sha256": SPEC_SHA},
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
    source = closed({"byte_span": {"items": integer, "type": "array"}, "path": string, "sha256": digest})
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
    verifier_input_roots = closed({"evidence_root_sha256": digest, "ledger_sha256": digest, "runtime_gate_sha256": digest, "runtime_snapshot_sha256": digest, "spec_sha256": digest})
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
        "runtime_subject": object_value,
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
        "producer-output.schema.json": {
            "$id": "rd22.producer-output.v001", "additionalProperties": False,
            "properties": {"authority_firewall": object_value, "check_map_sha256": digest, "checks": object_array, "fixture_manifest_sha256": digest, "fixtures": {"items": fixture_row, "type": "array"}, "manifest_sha256": digest, "monotonic_duration": {"type": "number"}, "process_id": integer, "python_optimize": integer, "schema": {"const": "rd22.producer-output.v001", "type": "string"}, "scope": object_value, "spec_sha256": digest, "subject_lineage_root": digest, "summary": object_value},
            "required": ["authority_firewall", "check_map_sha256", "checks", "fixture_manifest_sha256", "fixtures", "manifest_sha256", "monotonic_duration", "process_id", "python_optimize", "schema", "scope", "spec_sha256", "subject_lineage_root", "summary"], "type": "object",
        },
        "child-receipt.schema.json": {
            "$id": "rd22.child-receipt.v001", "additionalProperties": False,
            "properties": {"authority": {"const": False, "type": "boolean"}, "environment_event_ledger": object_array, "manifest_sha256": digest, "module_ledger": object_array, "monotonic_duration": {"type": "number"}, "mutation_event_ledger": object_array, "native_ledger": object_array, "network_event_ledger": object_array, "open_event_ledger": object_array, "optimize": {}, "output_sha256": digest, "process_event_ledger": object_array, "process_id": integer, "schema": {"const": "rd22.child-receipt.v001", "type": "string"}, "target_sha256": digest, "write_event_ledger": object_array},
            "required": ["authority", "environment_event_ledger", "manifest_sha256", "module_ledger", "monotonic_duration", "mutation_event_ledger", "native_ledger", "network_event_ledger", "open_event_ledger", "optimize", "output_sha256", "process_event_ledger", "process_id", "schema", "target_sha256", "write_event_ledger"], "type": "object",
        },
        "verifier-manifest.schema.json": {
            "$id": "rd22.verifier-manifest.v001", "additionalProperties": False,
            "properties": {"argv": string_array, "entry_point": string, "exit_contract": exit_contract, "input_roots": verifier_input_roots, "optimize": {"type": "boolean"}, "output_path": string, "receipt_authoritative": {"const": False, "type": "boolean"}, "receipt_path": string, "schema": {"const": "rd22.verifier-manifest.v001", "type": "string"}, "stdout_discipline": stdout_discipline, "verifier_root_sha256": digest},
            "required": ["argv", "entry_point", "exit_contract", "input_roots", "optimize", "output_path", "receipt_authoritative", "receipt_path", "schema", "stdout_discipline", "verifier_root_sha256"], "type": "object",
        },
        "verifier-output.schema.json": {
            "$id": "gravacle.a35.verifier-verdict.v1", "additionalProperties": False,
            "properties": {"authority_firewall": object_value, "authorization_sha256": digest, "census": object_value, "checks_replayed": object_array, "findings": object_array, "independence": closed({"expectations_source": string, "producer_code_imported": {"const": False, "type": "boolean"}}), "producer_comparison": object_value, "runtime_subject": closed({"gate_sha256": digest, "snapshot_sha256": digest, "trust_root": digest}), "schema": {"const": "gravacle.a35.verifier-verdict.v1", "type": "string"}, "spec_sha256": digest, "terminal_content_sha256": digest, "verdict": {"enum": ["VERIFIED", "FAIL"], "type": "string"}, "verifier_sha256": digest},
            "required": ["authority_firewall", "authorization_sha256", "census", "checks_replayed", "findings", "independence", "producer_comparison", "runtime_subject", "schema", "spec_sha256", "terminal_content_sha256", "verdict", "verifier_sha256"], "type": "object",
        },
        "terminal-ledger.schema.json": {
            "$id": "rd22.terminal-ledger.v001", "additionalProperties": False,
            "properties": {"authorization": object_value, "authority_firewall": object_value, "check_map_sha256": digest, "checks": object_array, "children": {"items": child_row, "type": "array"}, "fixture_manifest_sha256": digest, "fixtures": {"items": fixture_row, "type": "array"}, "producer_comparison": object_value, "runner_sha256": digest, "runtime_subject": object_value, "schema": {"const": "rd22.terminal-ledger.v001", "type": "string"}, "scope": object_value, "spec_sha256": digest, "subject_lineage": object_value, "summary": object_value, "terminal_content_sha256": digest, "trust_snapshots": object_value, "verifier_sha256": digest},
            "required": ["authorization", "authority_firewall", "check_map_sha256", "checks", "children", "fixture_manifest_sha256", "fixtures", "producer_comparison", "runner_sha256", "runtime_subject", "schema", "scope", "spec_sha256", "subject_lineage", "summary", "terminal_content_sha256", "trust_snapshots", "verifier_sha256"], "type": "object",
        },
    }


def content_root(entries):
    records = [f"{row['relative_path']}\0{row['byte_length']}\0{row['sha256']}\n" for row in entries]
    return sha(b"A35-CONTENT-ROOT-v1\0" + "".join(sorted(records)).encode("utf-8"))


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    program = cleanroom.parent
    spec_path = cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md"
    ledger_path = cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md"
    packet_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256"
    v011_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
    source_gate_path = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_SOURCE_PARENT_CLOSURE_GATE_V003.md"
    runtime_snapshot_path = program / "provenance/primitive_step6_runtime_snapshot_v012.json"
    runtime_gate_path = program / "primitive_step6_content_addressed_runtime_gate_v010.md"
    addendum_path = cleanroom / "STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md"
    authorization_path = Path("/Users/bgm/MB Work/alpha-program-archive/supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md")
    pins = [(spec_path, SPEC_SHA), (addendum_path, ADDENDUM_SHA), (ledger_path, LEDGER_SHA), (packet_path, PACKET_SHA), (v011_path, V011_SHA), (source_gate_path, SOURCE_GATE_SHA), (runtime_snapshot_path, SNAPSHOT_SHA), (runtime_gate_path, GATE_SHA), (authorization_path, AUTH_SHA)]
    for path, expected in pins:
        actual = sha(path.read_bytes())
        if actual != expected:
            die("PIN", f"{path}:{actual}")
    rows = descriptors(spec_path.read_bytes(), ledger_path.read_bytes())
    check_map = {
        "branch_outcome": BRANCH_OUTCOME,
        "check_ids": [row["check_id"] for row in rows],
        "checks": rows,
        "descriptor_convention": "SHA256 of the exact UTF-8 Markdown descriptor row including one trailing LF",
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
    structural_ids = [row["check_id"] for row in rows if row["execution_class"] == "STRUCTURAL"]
    structural_fixture_ids = [row["fixture_id"] for row in fixtures if row["execution_class"] == "STRUCTURAL"]
    evidence_dir = package / "inputs/evidence"
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
        if evidence["schema"] != "rd22.structural-evidence-manifest.v001" or evidence["subject_lineage_root"] != subject["declared_root"] or evidence["payload_inventory"] != payload_inventory or evidence["declared_root"] != declared_evidence_root:
            die("EVIDENCE_BINDING", "schema/subject root")
    else:
        evidence = {
            "check_records": {check_id: {"available": False, "reason": "NO_CONTENT_ADDRESSED_EVIDENCE_RECORD_PRESENT_IN_GOVERNING_INPUT_SET"} for check_id in structural_ids},
            "declared_root": declared_evidence_root,
            "fixture_records": {fixture_id: {"available": False, "reason": "NO_CONTENT_ADDRESSED_FIXTURE_OBSERVATION_PRESENT_IN_GOVERNING_INPUT_SET"} for fixture_id in structural_fixture_ids},
            "payload_inventory": payload_inventory,
            "schema": "rd22.structural-evidence-manifest.v001",
            "subject_lineage_root": subject["declared_root"],
        }
    write_json(package / "inputs/structural_evidence_manifest.json", evidence)
    evidence_payload_relatives = [f"inputs/evidence/{row['relative_path']}" for row in payload_inventory]
    runtime_relatives = [
        "parent.py", "producer.py", "checks/check_map.json", "fixtures/fixture_manifest.json",
        "inputs/structural_evidence_manifest.json", "inputs/subject_lineage_manifest.json",
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
    ]
    trust_root = json.loads(runtime_snapshot_path.read_text(encoding="utf-8"))["native_system_trust_root"]
    common = {
        "allowed_events": {"environment": [], "mutation": ["output", "receipt"], "network": [], "process": [], "writes": ["output", "receipt"]},
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
    normal = {**common, "mode": "normal", "optimization": 0, "writable_paths": ["normal.output.json", "normal.receipt.json"]}
    optimized = {**common, "mode": "optimized", "optimization": 1, "writable_paths": ["optimized.output.json", "optimized.receipt.json"]}
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
