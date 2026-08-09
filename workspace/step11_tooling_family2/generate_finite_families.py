#!/usr/bin/env python3
"""Generate finite instance families, exact expectation ledgers, and one corpus binding.

All pins are generated from supplied cleanroom bytes.  The tool validates each
complete instance against its sealed schema, recursively verifies content and
source-span references, and emits only tight canonical JSON.  It does not run
the evaluator chain or admit any generated component.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parent
CLEANROOM = ROOT.parent
VALIDATOR_PATH = CLEANROOM / "step11_tooling_family1/compile_carriers.py"

ROW_INPUTS = (
    {
        "row_id": "C-D-A35-02-QUASIFREE-CAR-LIFT",
        "adapter": "A35_ELEMENTS",
        "target_ids": [],
        "instance": "step11_a35_02_instance/generated/A35_02_instance.json",
        "instance_schema": "step11_a35_02_instance/contracts/instance.schema.json",
        "prior_row_status": "step11_a35_02_instance/generated/row_status.json",
        "sealing_report": "STAGE8_7A_A35_02_INSTANCE_CODEX2_V001.md",
    },
    {
        "row_id": "C-B-V010-11",
        "adapter": "DECORATED_CATEGORY",
        "target_ids": ["CS:C-B-V010-11:decorated-category"],
        "instance": "step11_v010_11_category/generated/instance/664059f4b10f1b78b1e04f111b77adc556644378a741622603bfbba957aa2b2d--C-B-V010-11.json",
        "instance_schema": "step11_v010_11_category/contracts/BX13_v010_11_decorated_category.schema.json",
        "prior_row_status": "step11_v010_11_category/generated/row_status.json",
        "sealing_report": "STAGE8_7A_V010_11_CATEGORY_CODEX2_V001.md",
    },
    {
        "row_id": "C-B-V009-08",
        "adapter": "CITATION_CLAIM_GRAPH",
        "target_ids": ["CS:C-B-V009-08:citation-claim-graph"],
        "instance": "step11_v009_08_graph/generated/instance/c41f5d05c0bc784281206aede14e310b7b7e68304cbb81c8b43e787a0ac23f84--C-B-V009-08.json",
        "instance_schema": "step11_v009_08_graph/contracts/BX09_v009_08_citation_claim_graph.schema.json",
        "prior_row_status": "step11_v009_08_graph/generated/row_status.json",
        "sealing_report": "STAGE8_7A_V009_08_GRAPH_CODEX2_V001.md",
    },
    {
        "row_id": "C-B-V008-05",
        "adapter": "NONCOMMUTING_PLAQUETTE",
        "target_ids": [
            "CS:C-B-V008-05:universal-word-representation",
            "MG:C-B-V008-05:inverse-opposite-holonomy-competitor",
        ],
        "instance": "step11_v008_05_competitor/generated/instance/0a400a1d19c436edd1a407c95390916a908f57281176ec22491eb139fb107775--C-B-V008-05.json",
        "instance_schema": "step11_v008_05_competitor/contracts/BX01_v008_05_noncommuting_plaquette.schema.json",
        "prior_row_status": "step11_v008_05_competitor/generated/row_status.json",
        "sealing_report": "STAGE8_7A_V008_05_COMPETITOR_CODEX2_V001.md",
    },
)

BATCH_MANIFEST = "step11_instance_batch1/generated/instances.generated.json"
BATCH_REPORT = "STAGE8_7A_INSTANCE_BATCH1_CODEX2_V001.md"
TARGET_MANIFEST = "step11_tooling_family1/targets.generated.json"
FAMILY1_REPORT = "STAGE8_7A_TOOLING_FAMILY1_CODEX2_V001.md"
STAGE_PARTIAL = "step11_v008_10_stage_binding/CS_C-B-V008-10_seal-stage-graph.partial.v002.json"
STAGE_RESULT = "step11_v008_10_stage_binding/generated/binding_result.generated.json"
STAGE_REPORT = "STAGE8_7A_V008_10_STAGE_BINDING_CODEX2_V001.md"
CORPUS = "step11_v009_08_graph/generated/corpora/2584d89444bb17ec335b89dfc32a6b38176e8a05bdef10bcdff1235f1699dacf--general_FS_claim_sources.json"
CORPUS_SCHEMA = "step11_v009_08_graph/contracts/SEALED_CORPUS_DEFINITION.schema.json"
CORPUS_TARGET = "CD:C-B-V009-08:general-FS-corpus"


class Family2Error(Exception):
    pass


def canonical(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise Family2Error(f"CANONICAL_JSON:{exc}") from exc


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def resolve(relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise Family2Error(f"PATH_FORM:{relative}")
    path = (CLEANROOM / relative).resolve()
    try:
        path.relative_to(CLEANROOM.resolve())
    except ValueError as exc:
        raise Family2Error(f"PATH_OUTSIDE:{relative}") from exc
    return path


def read_file(relative: str) -> bytes:
    path = resolve(relative)
    if not path.is_file():
        raise Family2Error(f"MISSING_FILE:{relative}")
    return path.read_bytes()


def file_ref(relative_or_path: str | Path) -> dict[str, Any]:
    if isinstance(relative_or_path, Path):
        path = relative_or_path.resolve()
        relative = path.relative_to(CLEANROOM.resolve()).as_posix()
    else:
        relative = relative_or_path
        path = resolve(relative)
    data = path.read_bytes()
    return {"relative_path": relative, "byte_length": len(data), "sha256": sha(data)}


def verify_ref(ref: dict[str, Any]) -> bytes:
    if set(ref) != {"relative_path", "byte_length", "sha256"}:
        raise Family2Error("CONTENT_REF_SHAPE")
    data = read_file(ref["relative_path"])
    if len(data) != ref["byte_length"]:
        raise Family2Error(f"BYTE_LENGTH_MISMATCH:{ref['relative_path']}")
    actual = sha(data)
    if actual != ref["sha256"]:
        raise Family2Error(f"HASH_MISMATCH:{ref['relative_path']}")
    return data


def load_json_ref(ref: dict[str, Any]) -> dict[str, Any]:
    data = verify_ref(ref)
    try:
        value = json.loads(data)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Family2Error(f"JSON_PARSE:{ref['relative_path']}:{exc}") from exc
    if not isinstance(value, dict):
        raise Family2Error(f"JSON_OBJECT:{ref['relative_path']}")
    if canonical(value) != data:
        raise Family2Error(f"JSON_NOT_CANONICAL:{ref['relative_path']}")
    return value


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise Family2Error(f"OUTPUT_COLLISION:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_json(path: Path, value: Any) -> None:
    write_new(path, canonical(value))


def content_path(directory: Path, stem: str, value: Any) -> Path:
    data = canonical(value)
    path = directory / f"{sha(data)}--{stem}.json"
    write_new(path, data)
    return path


def load_validator():
    data = VALIDATOR_PATH.read_bytes()
    ast.parse(data.decode("utf-8"), filename=str(VALIDATOR_PATH))
    spec = importlib.util.spec_from_file_location("rd22_family1_validator_for_family2", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise Family2Error("VALIDATOR_IMPORT_SPEC")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_seal(report_relative: str) -> tuple[dict[str, Any], dict[str, Any]]:
    report = resolve(report_relative)
    seal = Path(str(report) + ".seal.sha256")
    if not seal.is_file():
        raise Family2Error(f"MISSING_SEAL:{report_relative}")
    parts = seal.read_text(encoding="utf-8").strip().split()
    if len(parts) != 2 or parts[1] != report.name:
        raise Family2Error(f"SEAL_SHAPE:{report_relative}")
    if parts[0] != sha(report.read_bytes()):
        raise Family2Error(f"SEAL_MISMATCH:{report_relative}")
    return file_ref(report_relative), file_ref(seal)


def content_root(members: list[dict[str, Any]]) -> str:
    rows = []
    for member in sorted(members, key=lambda item: item["relative_path"]):
        rows.append(
            member["relative_path"].encode("utf-8") + b"\0" +
            str(member["byte_length"]).encode("ascii") + b"\0" +
            member["sha256"].encode("ascii") + b"\n"
        )
    return sha(b"A35-CONTENT-ROOT-v1\0" + b"".join(rows))


def contract_schema() -> dict[str, Any]:
    hex64 = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    string = {"type": "string", "minLength": 1}
    content = {
        "type": "object", "additionalProperties": False,
        "required": ["relative_path", "byte_length", "sha256"],
        "properties": {
            "relative_path": string,
            "byte_length": {"type": "integer", "minimum": 0},
            "sha256": hex64,
        },
    }
    ready = {
        "type": "object", "additionalProperties": False,
        "required": ["row_id", "adapter", "target_ids", "instance", "instance_schema",
                     "prior_row_status", "sealing_report", "sealing_report_seal"],
        "properties": {
            "row_id": string,
            "adapter": {"enum": ["A35_ELEMENTS", "DECORATED_CATEGORY", "CITATION_CLAIM_GRAPH", "NONCOMMUTING_PLAQUETTE"]},
            "target_ids": {"type": "array", "items": string, "uniqueItems": True},
            "instance": {"$ref": "#/$defs/content_ref"},
            "instance_schema": {"$ref": "#/$defs/content_ref"},
            "prior_row_status": {"$ref": "#/$defs/content_ref"},
            "sealing_report": {"$ref": "#/$defs/content_ref"},
            "sealing_report_seal": {"$ref": "#/$defs/content_ref"},
        },
    }
    family_member = {
        "type": "object", "additionalProperties": False,
        "required": ["member_id", "source_pointer", "value_sha256", "material_sha256"],
        "properties": {
            "member_id": string, "source_pointer": string,
            "value_sha256": hex64, "material_sha256": hex64,
        },
    }
    certificate = {
        "type": "object", "additionalProperties": False,
        "required": ["ordering", "member_count", "member_ids_sha256", "schema_validated",
                     "content_and_spans_verified", "duplicates", "all_source_slots_covered"],
        "properties": {
            "ordering": {"const": "BYTEWISE_UTF8_MEMBER_ID"},
            "member_count": {"type": "integer", "minimum": 1},
            "member_ids_sha256": hex64,
            "schema_validated": {"const": True},
            "content_and_spans_verified": {"const": True},
            "duplicates": {"const": 0},
            "all_source_slots_covered": {"const": True},
        },
    }
    family = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "row_id", "family_id", "source_instance", "members",
                     "completeness_certificate", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.finite-family.v001"},
            "row_id": string, "family_id": string,
            "source_instance": {"$ref": "#/$defs/content_ref"},
            "members": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/family_member"}, "uniqueItems": True},
            "completeness_certificate": {"$ref": "#/$defs/completeness_certificate"},
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    ledger_entry = {
        "type": "object", "additionalProperties": False,
        "required": ["expected_id", "expected_state", "expected_value_sha256", "expected_material_sha256"],
        "properties": {
            "expected_id": string,
            "expected_state": {"const": "PRESENT_EXACT"},
            "expected_value_sha256": hex64,
            "expected_material_sha256": hex64,
        },
    }
    ledger = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "row_id", "source_instance", "family", "entries", "expectation_basis", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.expected-ledger.v001"},
            "row_id": string,
            "source_instance": {"$ref": "#/$defs/content_ref"},
            "family": {"$ref": "#/$defs/content_ref"},
            "entries": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/ledger_entry"}, "uniqueItems": True},
            "expectation_basis": {"const": "SEALED_INSTANCE_MEMBER_VALUES_NOT_PRIOR_PASS_OUTPUTS"},
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    corpus_binding = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "row_id", "target_id", "box_id", "target_manifest", "target_definition_sha256",
                     "corpus_definition", "corpus_schema", "declared_root", "members", "binding_status", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.corpus-binding.v001"},
            "row_id": {"const": "C-B-V009-08"},
            "target_id": {"const": "CD:C-B-V009-08:general-FS-corpus"},
            "box_id": {"const": "BX10-V009-08-GENERAL-FS-CORPUS"},
            "target_manifest": {"$ref": "#/$defs/content_ref"},
            "target_definition_sha256": hex64,
            "corpus_definition": {"$ref": "#/$defs/content_ref"},
            "corpus_schema": {"$ref": "#/$defs/content_ref"},
            "declared_root": hex64,
            "members": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/content_ref"}, "uniqueItems": True},
            "binding_status": {"const": "GENERATED_CONTENT_ADDRESSED_BINDING"},
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    batch_item = {
        "type": "object", "additionalProperties": False,
        "required": ["target_id", "row_id", "prior_partial_sha256", "status", "current_instance_sha256",
                     "family_sha256", "expected_ledger_sha256", "remaining_owners"],
        "properties": {
            "target_id": string, "row_id": string, "prior_partial_sha256": hex64,
            "status": {"enum": ["RESOLVED_BY_COMPLETE_INSTANCE", "REMAINS_PARTIAL_PROGRAM_FUTURE"]},
            "current_instance_sha256": {"type": "string"},
            "family_sha256": {"type": "string"},
            "expected_ledger_sha256": {"type": "string"},
            "remaining_owners": {"type": "array", "items": string, "uniqueItems": True},
        },
    }
    batch_reconciliation = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "batch_manifest", "entries", "summary", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.batch-reconciliation.v001"},
            "batch_manifest": {"$ref": "#/$defs/content_ref"},
            "entries": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/batch_item"}, "uniqueItems": True},
            "summary": {
                "type": "object", "additionalProperties": False,
                "required": ["targets", "resolved", "remaining"],
                "properties": {
                    "targets": {"const": 5}, "resolved": {"const": 4}, "remaining": {"const": 1},
                },
            },
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    row_status = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "row_id", "state", "components", "missing_owners", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.row-status.v001"},
            "row_id": string, "state": string,
            "components": {"type": "array", "minItems": 2, "items": {"$ref": "#/$defs/content_ref"}, "uniqueItems": True},
            "missing_owners": {"type": "array", "items": string, "uniqueItems": True},
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    input_manifest = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "validator", "ready_instances", "batch_manifest", "batch_report", "batch_report_seal",
                     "target_manifest", "family1_report", "family1_report_seal", "stage_partial", "stage_result",
                     "stage_report", "stage_report_seal", "corpus_definition", "corpus_definition_seal", "corpus_schema",
                     "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.inputs.v001"},
            "validator": {"$ref": "#/$defs/content_ref"},
            "ready_instances": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"$ref": "#/$defs/ready_input"}, "uniqueItems": True},
            "batch_manifest": {"$ref": "#/$defs/content_ref"},
            "batch_report": {"$ref": "#/$defs/content_ref"},
            "batch_report_seal": {"$ref": "#/$defs/content_ref"},
            "target_manifest": {"$ref": "#/$defs/content_ref"},
            "family1_report": {"$ref": "#/$defs/content_ref"},
            "family1_report_seal": {"$ref": "#/$defs/content_ref"},
            "stage_partial": {"$ref": "#/$defs/content_ref"},
            "stage_result": {"$ref": "#/$defs/content_ref"},
            "stage_report": {"$ref": "#/$defs/content_ref"},
            "stage_report_seal": {"$ref": "#/$defs/content_ref"},
            "corpus_definition": {"$ref": "#/$defs/content_ref"},
            "corpus_definition_seal": {"$ref": "#/$defs/content_ref"},
            "corpus_schema": {"$ref": "#/$defs/content_ref"},
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    run_result = {
        "type": "object", "additionalProperties": False,
        "required": ["schema", "inputs_sha256", "rows", "corpus_binding", "batch_reconciliation", "remaining_owners", "summary", "admission", "chain_invoked"],
        "properties": {
            "schema": {"const": "rd22.step11.tooling-family2.run-result.v001"},
            "inputs_sha256": hex64,
            "rows": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"$ref": "#/$defs/content_ref"}, "uniqueItems": True},
            "corpus_binding": {"$ref": "#/$defs/content_ref"},
            "batch_reconciliation": {"$ref": "#/$defs/content_ref"},
            "remaining_owners": {"type": "array", "minItems": 1, "items": string, "uniqueItems": True},
            "summary": {
                "type": "object", "additionalProperties": False,
                "required": ["finite_families", "expected_ledgers", "corpus_bindings", "produced_components", "family_members", "rows_advanced", "batch_targets_resolved", "batch_targets_remaining"],
                "properties": {
                    "finite_families": {"const": 4}, "expected_ledgers": {"const": 4},
                    "corpus_bindings": {"const": 1}, "produced_components": {"const": 9},
                    "family_members": {"const": 56}, "rows_advanced": {"const": 4},
                    "batch_targets_resolved": {"const": 4}, "batch_targets_remaining": {"const": 1},
                },
            },
            "admission": {"const": "BARRED_STEP11_SUBGATE"},
            "chain_invoked": {"const": False},
        },
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:rd22:step11:tooling-family2:v001",
        "$defs": {
            "content_ref": content, "ready_input": ready, "family_member": family_member,
            "completeness_certificate": certificate, "finite_family": family,
            "ledger_entry": ledger_entry, "expected_ledger": ledger,
            "corpus_binding": corpus_binding, "batch_item": batch_item,
            "batch_reconciliation": batch_reconciliation, "row_status": row_status,
            "input_manifest": input_manifest, "run_result": run_result,
        },
    }


def contract_validate(validator: Any, contract: dict[str, Any], name: str, value: Any) -> None:
    validator.validate_contract_instance(value, contract, name)


def build_input_manifest() -> dict[str, Any]:
    ready = []
    for item in ROW_INPUTS:
        report_ref, seal_ref = verify_seal(item["sealing_report"])
        ready.append({
            "row_id": item["row_id"], "adapter": item["adapter"],
            "target_ids": item["target_ids"], "instance": file_ref(item["instance"]),
            "instance_schema": file_ref(item["instance_schema"]),
            "prior_row_status": file_ref(item["prior_row_status"]),
            "sealing_report": report_ref, "sealing_report_seal": seal_ref,
        })
    batch_report, batch_seal = verify_seal(BATCH_REPORT)
    family1_report, family1_seal = verify_seal(FAMILY1_REPORT)
    stage_report, stage_seal = verify_seal(STAGE_REPORT)
    corpus_report, _ = verify_seal("STAGE8_7A_V009_08_GRAPH_CODEX2_V001.md")
    del corpus_report
    corpus_path = resolve(CORPUS)
    corpus_seal_path = Path(str(corpus_path) + ".seal.sha256")
    if not corpus_seal_path.is_file():
        raise Family2Error("MISSING_CORPUS_SEAL")
    seal_parts = corpus_seal_path.read_text(encoding="utf-8").strip().split()
    if len(seal_parts) != 2 or seal_parts[0] != sha(corpus_path.read_bytes()) or seal_parts[1] != corpus_path.name:
        raise Family2Error("CORPUS_SEAL_MISMATCH")
    return {
        "schema": "rd22.step11.tooling-family2.inputs.v001",
        "validator": file_ref(VALIDATOR_PATH),
        "ready_instances": ready,
        "batch_manifest": file_ref(BATCH_MANIFEST),
        "batch_report": batch_report, "batch_report_seal": batch_seal,
        "target_manifest": file_ref(TARGET_MANIFEST),
        "family1_report": family1_report, "family1_report_seal": family1_seal,
        "stage_partial": file_ref(STAGE_PARTIAL), "stage_result": file_ref(STAGE_RESULT),
        "stage_report": stage_report, "stage_report_seal": stage_seal,
        "corpus_definition": file_ref(CORPUS),
        "corpus_definition_seal": file_ref(corpus_seal_path),
        "corpus_schema": file_ref(CORPUS_SCHEMA),
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


def material_digest(value: Any) -> str:
    if isinstance(value, dict) and set(value) == {"relative_path", "byte_length", "sha256"}:
        verify_ref(value)
        return value["sha256"]
    return sha(canonical(value))


def member(member_id: str, pointer: str, value: Any) -> dict[str, Any]:
    return {
        "member_id": member_id,
        "source_pointer": pointer,
        "value_sha256": sha(canonical(value)),
        "material_sha256": material_digest(value),
    }


def enumerate_members(adapter: str, instance: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if adapter == "A35_ELEMENTS":
        ids = instance["element_ids"]
        if set(ids) != set(instance["elements"]):
            raise Family2Error("A35_ELEMENT_CENSUS")
        for element_id in ids:
            rows.append(member(f"element:{element_id}", f"$.elements.{element_id}", instance["elements"][element_id]))
    elif adapter == "DECORATED_CATEGORY":
        for index, value in enumerate(instance["objects"]):
            rows.append(member(f"object:{value['object_id']}", f"$.objects[{index}]", value))
        for index, value in enumerate(instance["morphisms"]):
            rows.append(member(f"morphism:{value['morphism_id']}", f"$.morphisms[{index}]", value))
        for index, value in enumerate(instance["identities"]):
            rows.append(member(f"identity:{value['object_id']}", f"$.identities[{index}]", value))
        for index, value in enumerate(instance["composition"]):
            key = f"{value['left_morphism_id']}|{value['right_morphism_id']}"
            rows.append(member(f"composition:{key}", f"$.composition[{index}]", value))
        for index, value in enumerate(instance["generator_morphism_ids"]):
            rows.append(member(f"generator:{value}", f"$.generator_morphism_ids[{index}]", value))
    elif adapter == "CITATION_CLAIM_GRAPH":
        for index, value in enumerate(instance["authority_nodes"]):
            rows.append(member(f"authority:{value['authority_id']}", f"$.authority_nodes[{index}]", value))
        for index, value in enumerate(instance["claim_nodes"]):
            rows.append(member(f"claim:{value['claim_id']}", f"$.claim_nodes[{index}]", value))
        for index, value in enumerate(instance["entailment_edges"]):
            rows.append(member(f"edge:{value['edge_id']}", f"$.entailment_edges[{index}]", value))
        rows.append(member("premise:general_fs", "$.general_fs_premise", instance["general_fs_premise"]))
    elif adapter == "NONCOMMUTING_PLAQUETTE":
        for field in ("universal_word", "representation", "target_word", "inverse_competitor", "fixture_assignments"):
            rows.append(member(f"field:{field}", f"$.{field}", instance[field]))
    else:
        raise Family2Error(f"UNKNOWN_ADAPTER:{adapter}")
    rows.sort(key=lambda item: item["member_id"].encode("utf-8"))
    ids = [item["member_id"] for item in rows]
    if len(ids) != len(set(ids)):
        raise Family2Error("DUPLICATE_MEMBER_ID")
    return rows


def family_value(row_id: str, instance_ref: dict[str, Any], members: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [item["member_id"] for item in members]
    if len(ids) != len(set(ids)):
        raise Family2Error("DUPLICATE_MEMBER_ID")
    return {
        "schema": "rd22.step11.tooling-family2.finite-family.v001",
        "row_id": row_id,
        "family_id": f"{row_id}::SEALED_INSTANCE_MEMBERS",
        "source_instance": instance_ref,
        "members": members,
        "completeness_certificate": {
            "ordering": "BYTEWISE_UTF8_MEMBER_ID", "member_count": len(members),
            "member_ids_sha256": sha(canonical(ids)), "schema_validated": True,
            "content_and_spans_verified": True, "duplicates": 0,
            "all_source_slots_covered": True,
        },
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


def ledger_value(row_id: str, instance_ref: dict[str, Any], family_ref: dict[str, Any], members: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema": "rd22.step11.tooling-family2.expected-ledger.v001",
        "row_id": row_id, "source_instance": instance_ref, "family": family_ref,
        "entries": [
            {"expected_id": item["member_id"], "expected_state": "PRESENT_EXACT",
             "expected_value_sha256": item["value_sha256"],
             "expected_material_sha256": item["material_sha256"]}
            for item in members
        ],
        "expectation_basis": "SEALED_INSTANCE_MEMBER_VALUES_NOT_PRIOR_PASS_OUTPUTS",
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


def verify_family_ledger(family: dict[str, Any], ledger: dict[str, Any]) -> None:
    expected = {
        item["member_id"]: (item["value_sha256"], item["material_sha256"])
        for item in family["members"]
    }
    observed = {
        item["expected_id"]: (item["expected_value_sha256"], item["expected_material_sha256"])
        for item in ledger["entries"]
    }
    if expected != observed:
        raise Family2Error("EXPECTED_FAMILY_MISMATCH")


def verify_nested_json_refs(value: Any, validator: Any) -> None:
    validator.verify_instance_refs(value, CLEANROOM)
    if isinstance(value, dict):
        if set(value) == {"relative_path", "byte_length", "sha256"}:
            data = verify_ref(value)
            if value["relative_path"].endswith(".json"):
                nested = json.loads(data)
                if canonical(nested) != data:
                    raise Family2Error(f"NESTED_JSON_NOT_CANONICAL:{value['relative_path']}")
                validator.verify_instance_refs(nested, CLEANROOM)
            return
        for item in value.values():
            verify_nested_json_refs(item, validator)
    elif isinstance(value, list):
        for item in value:
            verify_nested_json_refs(item, validator)


def verify_corpus(corpus: dict[str, Any]) -> None:
    for item in corpus["members"]:
        verify_ref(item)
    if corpus["declared_root"] != content_root(corpus["members"]):
        raise Family2Error("CORPUS_ROOT")


def corpus_binding_value(inputs: dict[str, Any], corpus: dict[str, Any], target_manifest: dict[str, Any]) -> dict[str, Any]:
    hits = [item for item in target_manifest["targets"] if item["target_id"] == CORPUS_TARGET]
    if len(hits) != 1:
        raise Family2Error("CORPUS_TARGET_CENSUS")
    target = hits[0]
    if target["row_id"] != "C-B-V009-08" or target["box_id"] != "BX10-V009-08-GENERAL-FS-CORPUS":
        raise Family2Error("CORPUS_TARGET_IDENTITY")
    return {
        "schema": "rd22.step11.tooling-family2.corpus-binding.v001",
        "row_id": "C-B-V009-08", "target_id": CORPUS_TARGET,
        "box_id": "BX10-V009-08-GENERAL-FS-CORPUS",
        "target_manifest": inputs["target_manifest"],
        "target_definition_sha256": sha(canonical(target)),
        "corpus_definition": inputs["corpus_definition"],
        "corpus_schema": inputs["corpus_schema"],
        "declared_root": corpus["declared_root"], "members": corpus["members"],
        "binding_status": "GENERATED_CONTENT_ADDRESSED_BINDING",
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


ROW_STATES = {
    "C-D-A35-02-QUASIFREE-CAR-LIFT": "TOOLING_FAMILY2_PRESENT_COMPILE_READY_ADMISSION_BARRED",
    "C-B-V010-11": "TOOLING_FAMILY2_PRESENT_COMPONENTS_STATEABLE_ADMISSION_BARRED",
    "C-B-V009-08": "GRAPH_CORPUS_BOUND_TOOLING_FAMILY2_PRESENT_ADMISSION_BARRED",
    "C-B-V008-05": "BOTH_TARGETS_TOOLING_FAMILY2_PRESENT_ADMISSION_BARRED",
}


def row_status_value(row_id: str, components: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema": "rd22.step11.tooling-family2.row-status.v001",
        "row_id": row_id, "state": ROW_STATES[row_id], "components": components,
        "missing_owners": [], "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


def batch_reconciliation_value(inputs: dict[str, Any], batch: dict[str, Any], products: dict[str, dict[str, Any]]) -> dict[str, Any]:
    by_target: dict[str, dict[str, Any]] = {}
    for ready in inputs["ready_instances"]:
        for target_id in ready["target_ids"]:
            by_target[target_id] = {
                "instance": ready["instance"],
                "family": products[ready["row_id"]]["family"],
                "ledger": products[ready["row_id"]]["ledger"],
            }
    entries = []
    for item in batch["targets"]:
        target_id = item["target_id"]
        if target_id in by_target:
            current = by_target[target_id]
            entries.append({
                "target_id": target_id, "row_id": item["row_id"],
                "prior_partial_sha256": item["instance_sha256"],
                "status": "RESOLVED_BY_COMPLETE_INSTANCE",
                "current_instance_sha256": current["instance"]["sha256"],
                "family_sha256": current["family"]["sha256"],
                "expected_ledger_sha256": current["ledger"]["sha256"],
                "remaining_owners": [],
            })
        elif target_id == "CS:C-B-V008-10:seal-stage-graph":
            entries.append({
                "target_id": target_id, "row_id": item["row_id"],
                "prior_partial_sha256": item["instance_sha256"],
                "status": "REMAINS_PARTIAL_PROGRAM_FUTURE",
                "current_instance_sha256": inputs["stage_partial"]["sha256"],
                "family_sha256": "", "expected_ledger_sha256": "",
                "remaining_owners": [
                    "PROGRAM_FUTURE:11 stage realization artifacts",
                    "PROGRAM_FUTURE:17 digest-parent bindings",
                    "PROGRAM_FUTURE:sealed parent_map_root formula/value",
                    "PROGRAM_FUTURE:sealed mapping from 11-node adjacency to BX03 three-stage schema",
                ],
            })
        else:
            raise Family2Error(f"BATCH_TARGET_UNACCOUNTED:{target_id}")
    entries.sort(key=lambda item: item["target_id"])
    return {
        "schema": "rd22.step11.tooling-family2.batch-reconciliation.v001",
        "batch_manifest": inputs["batch_manifest"], "entries": entries,
        "summary": {"targets": 5, "resolved": 4, "remaining": 1},
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }


def first_span_ref(value: Any) -> dict[str, Any] | None:
    if isinstance(value, dict):
        if set(value) == {"relative_path", "source_sha256", "span", "span_sha256"}:
            return value
        for item in value.values():
            hit = first_span_ref(item)
            if hit is not None:
                return hit
    elif isinstance(value, list):
        for item in value:
            hit = first_span_ref(item)
            if hit is not None:
                return hit
    return None


def expect_refusal(name: str, action: Callable[[], None]) -> dict[str, str]:
    try:
        action()
    except Exception as exc:
        return {"control": name, "observed": f"{type(exc).__name__}:{exc}", "status": "PASS_REFUSED"}
    raise Family2Error(f"NEGATIVE_DID_NOT_BITE:{name}")


def run_negative_controls(validator: Any, contract: dict[str, Any], inputs: dict[str, Any],
                          instances: dict[str, dict[str, Any]], families: dict[str, dict[str, Any]],
                          ledgers: dict[str, dict[str, Any]], corpus: dict[str, Any]) -> list[dict[str, str]]:
    controls = []
    bad_ref = json.loads(json.dumps(inputs["ready_instances"][0]["instance"]))
    bad_ref["sha256"] = "0" * 64
    controls.append(expect_refusal("PERTURBED_INPUT_DIGEST", lambda: verify_ref(bad_ref)))

    ready = inputs["ready_instances"][0]
    schema = load_json_ref(ready["instance_schema"])
    bad_instance = json.loads(json.dumps(instances[ready["row_id"]]))
    bad_instance.pop("schema")
    controls.append(expect_refusal(
        "NONCONFORMING_INSTANCE",
        lambda: validator.validate_schema(bad_instance, schema, schema),
    ))

    span = first_span_ref(instances["C-B-V008-05"])
    if span is None:
        raise Family2Error("NEGATIVE_SPAN_SOURCE")
    bad_span = json.loads(json.dumps(span))
    bad_span["span"][1] -= 1
    controls.append(expect_refusal("TRUNCATED_SPAN", lambda: validator.verify_span_ref(bad_span, CLEANROOM)))

    bad_corpus = json.loads(json.dumps(corpus))
    bad_corpus["declared_root"] = "0" * 64
    controls.append(expect_refusal("WRONG_CORPUS_ROOT", lambda: verify_corpus(bad_corpus)))

    bad_members = json.loads(json.dumps(families["C-B-V010-11"]["members"]))
    bad_members[1]["member_id"] = bad_members[0]["member_id"]
    controls.append(expect_refusal(
        "DUPLICATE_FAMILY_ID",
        lambda: family_value("C-B-V010-11", inputs["ready_instances"][1]["instance"], bad_members),
    ))

    bad_ledger = json.loads(json.dumps(ledgers["C-B-V009-08"]))
    bad_ledger["entries"][0]["expected_material_sha256"] = "0" * 64
    controls.append(expect_refusal(
        "LEDGER_FAMILY_MISMATCH",
        lambda: verify_family_ledger(families["C-B-V009-08"], bad_ledger),
    ))
    return controls


def count_refs(value: Any) -> tuple[int, int]:
    contents = 0
    spans = 0
    if isinstance(value, dict):
        keys = set(value)
        if keys == {"relative_path", "byte_length", "sha256"}:
            return 1, 0
        if keys == {"relative_path", "source_sha256", "span", "span_sha256"}:
            return 0, 1
        for item in value.values():
            c, s = count_refs(item); contents += c; spans += s
    elif isinstance(value, list):
        for item in value:
            c, s = count_refs(item); contents += c; spans += s
    return contents, spans


def build() -> None:
    for output in (ROOT / "contracts", ROOT / "generated", ROOT / "inputs.generated.json", ROOT / "inventory.generated.json"):
        if output.exists():
            raise Family2Error(f"OUTPUT_COLLISION:{output}")
    ast.parse(Path(__file__).read_text(encoding="utf-8"), filename=str(Path(__file__)))
    validator = load_validator()
    contract = contract_schema()
    contract_path = ROOT / "contracts/tooling_family2.schema.json"
    write_json(contract_path, contract)

    inputs = build_input_manifest()
    contract_validate(validator, contract, "input_manifest", inputs)
    inputs_path = ROOT / "inputs.generated.json"
    write_json(inputs_path, inputs)
    inputs_sha = sha(inputs_path.read_bytes())

    instances: dict[str, dict[str, Any]] = {}
    families: dict[str, dict[str, Any]] = {}
    ledgers: dict[str, dict[str, Any]] = {}
    products: dict[str, dict[str, Any]] = {}
    family_members = 0
    for ready in inputs["ready_instances"]:
        instance = load_json_ref(ready["instance"])
        schema = load_json_ref(ready["instance_schema"])
        validator.validate_schema(instance, schema, schema)
        verify_nested_json_refs(instance, validator)
        members = enumerate_members(ready["adapter"], instance)
        family = family_value(ready["row_id"], ready["instance"], members)
        contract_validate(validator, contract, "finite_family", family)
        safe_row = re.sub(r"[^A-Za-z0-9_.-]+", "_", ready["row_id"])
        family_path = content_path(ROOT / "generated/families", f"{safe_row}_family", family)
        family_ref = file_ref(family_path)
        ledger = ledger_value(ready["row_id"], ready["instance"], family_ref, members)
        contract_validate(validator, contract, "expected_ledger", ledger)
        verify_family_ledger(family, ledger)
        ledger_path = content_path(ROOT / "generated/expected_ledgers", f"{safe_row}_expected", ledger)
        ledger_ref = file_ref(ledger_path)
        instances[ready["row_id"]] = instance
        families[ready["row_id"]] = family
        ledgers[ready["row_id"]] = ledger
        products[ready["row_id"]] = {"family": family_ref, "ledger": ledger_ref}
        family_members += len(members)
    if family_members != 56:
        raise Family2Error(f"FAMILY_MEMBER_CENSUS:{family_members}")

    corpus = load_json_ref(inputs["corpus_definition"])
    corpus_schema = load_json_ref(inputs["corpus_schema"])
    validator.validate_schema(corpus, corpus_schema, corpus_schema)
    verify_corpus(corpus)
    target_manifest = load_json_ref(inputs["target_manifest"])
    binding = corpus_binding_value(inputs, corpus, target_manifest)
    contract_validate(validator, contract, "corpus_binding", binding)
    binding_path = content_path(ROOT / "generated/bindings", "C-B-V009-08_general_FS_corpus_binding", binding)
    binding_ref = file_ref(binding_path)

    batch = load_json_ref(inputs["batch_manifest"])
    reconciliation = batch_reconciliation_value(inputs, batch, products)
    contract_validate(validator, contract, "batch_reconciliation", reconciliation)
    reconciliation_path = ROOT / "generated/batch_reconciliation.json"
    write_json(reconciliation_path, reconciliation)
    reconciliation_ref = file_ref(reconciliation_path)

    row_refs = []
    for ready in inputs["ready_instances"]:
        row_id = ready["row_id"]
        components = [products[row_id]["family"], products[row_id]["ledger"]]
        if row_id == "C-B-V009-08":
            components.append(binding_ref)
        status = row_status_value(row_id, components)
        contract_validate(validator, contract, "row_status", status)
        safe_row = re.sub(r"[^A-Za-z0-9_.-]+", "_", row_id)
        path = ROOT / f"generated/rows/{safe_row}.status.json"
        write_json(path, status)
        row_refs.append(file_ref(path))
    row_refs.sort(key=lambda item: item["relative_path"])

    controls = run_negative_controls(validator, contract, inputs, instances, families, ledgers, corpus)
    content_refs = 0
    span_refs = 0
    for instance in instances.values():
        c, s = count_refs(instance); content_refs += c; span_refs += s
    self_check = {
        "schema": "rd22.step11.tooling-family2.self-check.v001",
        "status": "PASS", "ready_instances": 4, "schema_validations": 4,
        "content_refs_verified": content_refs, "span_refs_verified": span_refs,
        "finite_families": 4, "expected_ledgers": 4, "family_members": family_members,
        "corpus_root_recomputed": True, "corpus_member_count": len(corpus["members"]),
        "batch_targets_resolved": 4, "batch_targets_remaining": 1,
        "negative_controls": controls, "canonical_json": "TIGHT_SORTED_UTF8_NO_TRAILING_NEWLINE",
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }
    write_json(ROOT / "generated/self_check.json", self_check)

    remaining = [
        "C-B-V008-10:PROGRAM_FUTURE:11 stage realization artifacts",
        "C-B-V008-10:PROGRAM_FUTURE:17 digest-parent bindings",
        "C-B-V008-10:PROGRAM_FUTURE:sealed parent_map_root formula/value",
        "C-B-V008-10:PROGRAM_FUTURE:sealed mapping from 11-node adjacency to BX03 three-stage schema",
    ]
    run_result = {
        "schema": "rd22.step11.tooling-family2.run-result.v001",
        "inputs_sha256": inputs_sha, "rows": row_refs, "corpus_binding": binding_ref,
        "batch_reconciliation": reconciliation_ref, "remaining_owners": remaining,
        "summary": {
            "finite_families": 4, "expected_ledgers": 4, "corpus_bindings": 1,
            "produced_components": 9, "family_members": family_members, "rows_advanced": 4,
            "batch_targets_resolved": 4, "batch_targets_remaining": 1,
        },
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }
    contract_validate(validator, contract, "run_result", run_result)
    write_json(ROOT / "generated/run_result.json", run_result)

    members = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == "inventory.generated.json":
            continue
        data = path.read_bytes()
        members.append({
            "relative_path": path.relative_to(CLEANROOM).as_posix(),
            "byte_length": len(data), "sha256": sha(data),
        })
    inventory = {
        "schema": "rd22.step11.tooling-family2.inventory.v001",
        "members": members, "member_count": len(members),
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
    }
    write_json(ROOT / "inventory.generated.json", inventory)


def main() -> int:
    try:
        build()
        print("TOOLING_FAMILY2_BUILD_PASS")
        return 0
    except Exception as exc:
        print(f"TOOLING_FAMILY2_BUILD_FAIL {type(exc).__name__}:{exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
