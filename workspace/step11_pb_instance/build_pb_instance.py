#!/usr/bin/env python3
"""Build and compile the principal-ruled P-B V009-01 rooted-star instance.

The output contains no coordinate basis, scalar trivialization, or unit
representative.  Four line subobjects and three abstract unitary morphisms are
content-addressed from sealed source bytes and checked against a closed schema.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parent
CLEANROOM = ROOT.parent
ARCHIVE = Path("/Users/bgm/MB Work/alpha-program-archive")
SOURCE_ROOT = CLEANROOM

DECISION_SOURCE = ARCHIVE / "supervision/DECISION_V009_01_CARRIER_PB_2026-08-08.md"
GATE3_SPEC_SOURCE = ARCHIVE / "cleanroom_output/36_GATE3_HILBERT_FUNCTOR_SPEC_V001.md"
GATE3_RESULT_SOURCE = ARCHIVE / "cleanroom_output/38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md"
V011_SOURCE = CLEANROOM / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
U7_SOURCE = CLEANROOM / "STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md"
BOX_DELTA_SOURCE = CLEANROOM / "STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json"

EXPECTED = {
    DECISION_SOURCE: "1741cdb311def6263d3ab333c6f7d4280e80f862bdf2208276f94a1f4297e870",
    GATE3_SPEC_SOURCE: "953e875b5080a24fee0d8515c0ec7c2d93b644c1ec8b53acc121bcd99d7a330b",
    GATE3_RESULT_SOURCE: "ea707b3a5e5a93297c793c9f4227b456b97d7f8e184da95d96436299076915da",
    V011_SOURCE: "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    U7_SOURCE: "0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d",
    BOX_DELTA_SOURCE: "b52e66b79787a55bad1553c05dfa8df52e7b11153879589d9627073a8e06bba9",
}


class BuildError(Exception):
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
        raise BuildError(f"CANONICAL_JSON:{exc}") from exc


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(path: Path, expected: str) -> bytes:
    if not path.is_file():
        raise BuildError(f"MISSING_SOURCE:{path}")
    data = path.read_bytes()
    actual = digest(data)
    if actual != expected:
        raise BuildError(f"HASH_MISMATCH:{path}:{expected}:{actual}")
    return data


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise BuildError(f"OUTPUT_COLLISION:{path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def content_ref(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "byte_length": len(data),
        "relative_path": str(path.relative_to(CLEANROOM)),
        "sha256": digest(data),
    }


def line_span(path: Path, first: int, last: int) -> dict[str, Any]:
    data = path.read_bytes()
    lines = data.splitlines(keepends=True)
    if first < 1 or last < first or last > len(lines):
        raise BuildError(f"SPAN_LINES:{path}:{first}:{last}")
    start = sum(len(item) for item in lines[: first - 1])
    end = sum(len(item) for item in lines[:last])
    return {
        "relative_path": str(path.relative_to(CLEANROOM)),
        "source_sha256": digest(data),
        "span": [start, end],
        "span_sha256": digest(data[start:end]),
    }


def mirror_source(source: Path, expected: str) -> Path:
    data = verify(source, expected)
    target = ROOT / "sources" / f"{expected}--{source.name}"
    write_new(target, data)
    return target


def schema_document() -> dict[str, Any]:
    hex64 = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    content_ref_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["byte_length", "relative_path", "sha256"],
        "properties": {
            "byte_length": {"type": "integer", "minimum": 0},
            "relative_path": {"type": "string", "minLength": 1},
            "sha256": hex64,
        },
    }
    span_ref_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["relative_path", "source_sha256", "span", "span_sha256"],
        "properties": {
            "relative_path": {"type": "string", "minLength": 1},
            "source_sha256": hex64,
            "span": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "prefixItems": [
                    {"type": "integer", "minimum": 0},
                    {"type": "integer", "minimum": 0},
                ],
                "items": False,
            },
            "span_sha256": hex64,
        },
    }
    line_ref_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["line_id", "payload"],
        "properties": {
            "line_id": {"enum": ["L_r", "L_pM", "L_pQ", "L_pG"]},
            "payload": {"$ref": "#/$defs/content_ref"},
        },
    }

    def exact_line_ref(line_id: str) -> dict[str, Any]:
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["line_id", "payload"],
            "properties": {
                "line_id": {"const": line_id},
                "payload": {"$ref": "#/$defs/content_ref"},
            },
        }
    transport_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "transport_id",
            "edge_id",
            "label",
            "domain_line_id",
            "codomain_line_id",
            "map_kind",
            "unitary_relations",
            "coordinate_scalar_present",
        ],
        "properties": {
            "transport_id": {"enum": ["U_eM", "U_eQ", "U_eG"]},
            "edge_id": {"enum": ["e_M", "e_Q", "e_G"]},
            "label": {"enum": ["M", "Q", "G"]},
            "domain_line_id": {"const": "L_r"},
            "codomain_line_id": {"enum": ["L_pM", "L_pQ", "L_pG"]},
            "map_kind": {"const": "ABSTRACT_UNITARY_HERMITIAN_LINE_MORPHISM"},
            "unitary_relations": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "uniqueItems": True,
                "items": {"type": "string", "minLength": 1},
            },
            "coordinate_scalar_present": {"const": False},
        },
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:rd22:step11:v009-01:pb-line-rooted-star:v001",
        "title": "BX-line / C-B-V009-01 P-B rooted-star instance",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "schema",
            "box_id",
            "row_id",
            "source_bindings",
            "ruling",
            "gate3_form",
            "topology",
            "line_subobjects",
            "edge_transports",
            "endpoint_carrier",
            "licenses",
        ],
        "properties": {
            "schema": {"const": "rd22.step11.v009-01.pb-line-rooted-star.v001"},
            "box_id": {"const": "BX-LINE-V009-01-PB"},
            "row_id": {"const": "C-B-V009-01"},
            "source_bindings": {
                "type": "array",
                "minItems": 5,
                "items": {"$ref": "#/$defs/span_ref"},
            },
            "ruling": {"$ref": "#/$defs/content_ref"},
            "gate3_form": {
                "type": "object",
                "additionalProperties": False,
                "required": ["spec", "result", "form_id", "degree", "equivalence", "coordinate_basis_licensed"],
                "properties": {
                    "spec": {"$ref": "#/$defs/content_ref"},
                    "result": {"$ref": "#/$defs/content_ref"},
                    "form_id": {"const": "GATE3_M0_IDENTITY_FIBER_FORM"},
                    "degree": {"const": 0},
                    "equivalence": {"const": "UNIQUE_MODULO_OVERALL_CONGRUENCE"},
                    "coordinate_basis_licensed": {"const": False},
                },
            },
            "topology": {
                "type": "object",
                "additionalProperties": False,
                "required": ["complex_id", "root_vertex_id", "vertices", "edges"],
                "properties": {
                    "complex_id": {"const": "K_open_PB"},
                    "root_vertex_id": {"const": "r"},
                    "vertices": {
                        "type": "array",
                        "minItems": 4,
                        "maxItems": 4,
                        "prefixItems": [
                            {"const": "r"}, {"const": "p_M"}, {"const": "p_Q"}, {"const": "p_G"}
                        ],
                        "items": False,
                    },
                    "edges": {
                        "type": "array",
                        "minItems": 3,
                        "maxItems": 3,
                        "prefixItems": [
                            {"const": {"edge_id": "e_M", "label": "M", "source": "r", "target": "p_M"}},
                            {"const": {"edge_id": "e_Q", "label": "Q", "source": "r", "target": "p_Q"}},
                            {"const": {"edge_id": "e_G", "label": "G", "source": "r", "target": "p_G"}},
                        ],
                        "items": False,
                    },
                },
            },
            "line_subobjects": {
                "type": "array",
                "minItems": 4,
                "maxItems": 4,
                "prefixItems": [
                    exact_line_ref("L_r"),
                    exact_line_ref("L_pM"),
                    exact_line_ref("L_pQ"),
                    exact_line_ref("L_pG"),
                ],
                "items": False,
            },
            "edge_transports": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": {"$ref": "#/$defs/transport"},
            },
            "endpoint_carrier": {
                "type": "object",
                "additionalProperties": False,
                "required": ["carrier_id", "direct_sum_order", "canonical_summand_inclusions"],
                "properties": {
                    "carrier_id": {"const": "E_open_PB"},
                    "direct_sum_order": {
                        "const": ["L_r", "L_pM", "L_pQ", "L_pG"]
                    },
                    "canonical_summand_inclusions": {
                        "const": ["iota_L_r", "iota_L_pM", "iota_L_pQ", "iota_L_pG"]
                    },
                },
            },
            "licenses": {
                "const": {
                    "basis": False,
                    "scalar_trivialization": False,
                    "unit_representative": False,
                }
            },
        },
        "$defs": {
            "content_ref": content_ref_schema,
            "span_ref": span_ref_schema,
            "line_ref": line_ref_schema,
            "transport": transport_schema,
        },
    }


def resolve_ref(schema: dict[str, Any], ref: str) -> dict[str, Any]:
    prefix = "#/$defs/"
    if not ref.startswith(prefix):
        raise BuildError(f"SCHEMA_REF:{ref}")
    name = ref[len(prefix):]
    result = schema.get("$defs", {}).get(name)
    if not isinstance(result, dict):
        raise BuildError(f"SCHEMA_REF:{ref}")
    return result


def type_ok(value: Any, expected: str) -> bool:
    choices = {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
    }
    return choices.get(expected, False)


def validate(value: Any, rule: dict[str, Any], root: dict[str, Any], path: str = "$") -> None:
    if "$ref" in rule:
        validate(value, resolve_ref(root, rule["$ref"]), root, path)
        remaining = {key: item for key, item in rule.items() if key != "$ref"}
        if remaining:
            validate(value, remaining, root, path)
        return
    if "const" in rule and value != rule["const"]:
        raise BuildError(f"SCHEMA_CONFORMANCE:{path}:const")
    if "enum" in rule and value not in rule["enum"]:
        raise BuildError(f"SCHEMA_CONFORMANCE:{path}:enum")
    expected = rule.get("type")
    if expected is not None and not type_ok(value, expected):
        raise BuildError(f"SCHEMA_CONFORMANCE:{path}:type:{expected}")
    if isinstance(value, dict):
        required = rule.get("required", [])
        missing = sorted(set(required) - set(value))
        if missing:
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:missing:{missing}")
        properties = rule.get("properties", {})
        if rule.get("additionalProperties") is False:
            extra = sorted(set(value) - set(properties))
            if extra:
                raise BuildError(f"SCHEMA_CONFORMANCE:{path}:extra:{extra}")
        for key, item in value.items():
            if key in properties:
                validate(item, properties[key], root, f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:minItems")
        if "maxItems" in rule and len(value) > rule["maxItems"]:
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:maxItems")
        prefix = rule.get("prefixItems", [])
        for index, item_rule in enumerate(prefix):
            if index < len(value):
                validate(value[index], item_rule, root, f"{path}[{index}]")
        tail = rule.get("items")
        if tail is False and len(value) > len(prefix):
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:tuple-tail")
        if isinstance(tail, dict):
            start = len(prefix) if prefix else 0
            for index in range(start, len(value)):
                validate(value[index], tail, root, f"{path}[{index}]")
        if rule.get("uniqueItems"):
            encoded = [canonical(item) for item in value]
            if len(encoded) != len(set(encoded)):
                raise BuildError(f"SCHEMA_CONFORMANCE:{path}:uniqueItems")
    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0):
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:minLength")
        pattern = rule.get("pattern")
        if pattern == "^[0-9a-f]{64}$" and (len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value)):
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:pattern")
    if isinstance(value, int) and not isinstance(value, bool):
        if value < rule.get("minimum", value):
            raise BuildError(f"SCHEMA_CONFORMANCE:{path}:minimum")


def verify_ref(ref: dict[str, Any]) -> None:
    path = (SOURCE_ROOT / ref["relative_path"]).resolve()
    try:
        path.relative_to(SOURCE_ROOT.resolve())
    except ValueError as exc:
        raise BuildError(f"PATH_ESCAPE:{ref['relative_path']}") from exc
    data = path.read_bytes()
    if "byte_length" in ref:
        if len(data) != ref["byte_length"] or digest(data) != ref["sha256"]:
            raise BuildError(f"CONTENT_REF_MISMATCH:{ref['relative_path']}")
    else:
        if digest(data) != ref["source_sha256"]:
            raise BuildError(f"SPAN_SOURCE_MISMATCH:{ref['relative_path']}")
        start, end = ref["span"]
        if start > end or end > len(data) or digest(data[start:end]) != ref["span_sha256"]:
            raise BuildError(f"SPAN_REF_MISMATCH:{ref['relative_path']}:{start}:{end}")


def line_schema() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "urn:rd22:step11:gate3-line-subobject:v001",
        "type": "object",
        "additionalProperties": False,
        "required": [
            "schema", "line_id", "cell_id", "dimension", "ambient_carrier_id",
            "inclusion", "induced_hermitian_form", "gate3_form", "licenses",
        ],
        "properties": {
            "schema": {"const": "rd22.step11.gate3-line-subobject.v001"},
            "line_id": {"enum": ["L_r", "L_pM", "L_pQ", "L_pG"]},
            "cell_id": {"enum": ["r", "p_M", "p_Q", "p_G"]},
            "dimension": {"const": 1},
            "ambient_carrier_id": {"const": "C_0(K_open_PB;L)"},
            "inclusion": {
                "type": "object",
                "additionalProperties": False,
                "required": ["map_id", "domain", "codomain", "image_summand"],
                "properties": {
                    "map_id": {"type": "string", "minLength": 1},
                    "domain": {"type": "string", "minLength": 1},
                    "codomain": {"const": "C_0(K_open_PB;L)"},
                    "image_summand": {"type": "string", "minLength": 1},
                },
            },
            "induced_hermitian_form": {
                "type": "object",
                "additionalProperties": False,
                "required": ["form_id", "definition", "expression", "source_form_id"],
                "properties": {
                    "form_id": {"type": "string", "minLength": 1},
                    "definition": {"const": "PULLBACK_ALONG_SUBOBJECT_INCLUSION"},
                    "expression": {"type": "string", "minLength": 1},
                    "source_form_id": {"const": "GATE3_M0_IDENTITY_FIBER_FORM"},
                },
            },
            "gate3_form": {
                "type": "object",
                "additionalProperties": False,
                "required": ["result_sha256", "result_span_sha256"],
                "properties": {
                    "result_sha256": {"const": EXPECTED[GATE3_RESULT_SOURCE]},
                    "result_span_sha256": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                },
            },
            "licenses": {
                "const": {"basis": False, "scalar_trivialization": False, "unit_representative": False}
            },
        },
    }


def make_line(line_id: str, cell_id: str, gate3_span_sha: str) -> dict[str, Any]:
    return {
        "schema": "rd22.step11.gate3-line-subobject.v001",
        "line_id": line_id,
        "cell_id": cell_id,
        "dimension": 1,
        "ambient_carrier_id": "C_0(K_open_PB;L)",
        "inclusion": {
            "map_id": f"iota_{line_id}",
            "domain": line_id,
            "codomain": "C_0(K_open_PB;L)",
            "image_summand": cell_id,
        },
        "induced_hermitian_form": {
            "form_id": f"h_{line_id}",
            "definition": "PULLBACK_ALONG_SUBOBJECT_INCLUSION",
            "expression": f"h_{line_id}=iota_{line_id}^* M_0 iota_{line_id}",
            "source_form_id": "GATE3_M0_IDENTITY_FIBER_FORM",
        },
        "gate3_form": {
            "result_sha256": EXPECTED[GATE3_RESULT_SOURCE],
            "result_span_sha256": gate3_span_sha,
        },
        "licenses": {"basis": False, "scalar_trivialization": False, "unit_representative": False},
    }


def check_line_semantics(value: dict[str, Any], expected_id: str, expected_cell: str) -> None:
    if value["line_id"] != expected_id or value["cell_id"] != expected_cell:
        raise BuildError(f"LINE_IDENTITY:{expected_id}")
    inclusion = value["inclusion"]
    if inclusion["domain"] != expected_id or inclusion["image_summand"] != expected_cell:
        raise BuildError(f"LINE_INCLUSION:{expected_id}")
    if any(value["licenses"].values()):
        raise BuildError(f"UNLICENSED_COORDINATE:{expected_id}")
    form = value["induced_hermitian_form"]
    expected_expression = f"h_{expected_id}=iota_{expected_id}^* M_0 iota_{expected_id}"
    if form["expression"] != expected_expression:
        raise BuildError(f"FORM_BINDING:{expected_id}")


def check_instance_semantics(value: dict[str, Any], line_payloads: dict[str, dict[str, Any]]) -> None:
    expected_lines = ["L_r", "L_pM", "L_pQ", "L_pG"]
    observed_lines = [item["line_id"] for item in value["line_subobjects"]]
    if observed_lines != expected_lines or len(set(observed_lines)) != 4:
        raise BuildError("DISTINCT_LINE_IDS")
    for item in value["line_subobjects"]:
        ref = item["payload"]
        verify_ref(ref)
        payload_path = SOURCE_ROOT / ref["relative_path"]
        payload = json.loads(payload_path.read_text("utf-8"))
        if payload != line_payloads[item["line_id"]]:
            raise BuildError(f"LINE_PAYLOAD_IDENTITY:{item['line_id']}")
    expected_inclusions = [line_payloads[line_id]["inclusion"]["map_id"] for line_id in expected_lines]
    if value["endpoint_carrier"]["canonical_summand_inclusions"] != expected_inclusions:
        raise BuildError("ENDPOINT_INCLUSION_BINDING")
    expected_transports = {
        "U_eM": ("e_M", "M", "L_pM"),
        "U_eQ": ("e_Q", "Q", "L_pQ"),
        "U_eG": ("e_G", "G", "L_pG"),
    }
    if {item["transport_id"] for item in value["edge_transports"]} != set(expected_transports):
        raise BuildError("TRANSPORT_CENSUS")
    for item in value["edge_transports"]:
        edge, label, target = expected_transports[item["transport_id"]]
        expected_relations = {
            f"{item['transport_id']}^* {item['transport_id']}=id_L_r",
            f"{item['transport_id']} {item['transport_id']}^*=id_{target}",
            f"{item['transport_id']}^* h_{target} {item['transport_id']}=h_L_r",
        }
        if (item["edge_id"], item["label"], item["codomain_line_id"]) != (edge, label, target):
            raise BuildError(f"TRANSPORT_TYPE:{item['transport_id']}")
        if set(item["unitary_relations"]) != expected_relations or item["coordinate_scalar_present"] is not False:
            raise BuildError(f"TRANSPORT_UNITARY:{item['transport_id']}")
    if any(value["licenses"].values()):
        raise BuildError("INSTANCE_LICENSE")


def build() -> None:
    if any((ROOT / name).exists() for name in ["sources", "contracts", "generated", "inventory.generated.json"]):
        raise BuildError("OUTPUT_COLLISION:package outputs")

    for path, expected in EXPECTED.items():
        verify(path, expected)

    decision_copy = mirror_source(DECISION_SOURCE, EXPECTED[DECISION_SOURCE])
    gate3_spec_copy = mirror_source(GATE3_SPEC_SOURCE, EXPECTED[GATE3_SPEC_SOURCE])
    gate3_result_copy = mirror_source(GATE3_RESULT_SOURCE, EXPECTED[GATE3_RESULT_SOURCE])

    contract = schema_document()
    line_contract = line_schema()
    contract_path = ROOT / "contracts/bx_line_pb.schema.json"
    line_contract_path = ROOT / "contracts/gate3_line_subobject.schema.json"
    write_new(contract_path, canonical(contract))
    write_new(line_contract_path, canonical(line_contract))

    gate3_spec_span = line_span(gate3_spec_copy, 11, 43)
    gate3_result_span = line_span(gate3_result_copy, 8, 33)
    decision_span = line_span(decision_copy, 1, len(decision_copy.read_bytes().splitlines()))
    v011_open_span = line_span(V011_SOURCE, 128, 163)
    v011_star_span = line_span(V011_SOURCE, 248, 304)
    u7_pb_span = line_span(U7_SOURCE, 103, 137)

    line_payloads: dict[str, dict[str, Any]] = {}
    line_refs: list[dict[str, Any]] = []
    for line_id, cell_id in [("L_r", "r"), ("L_pM", "p_M"), ("L_pQ", "p_Q"), ("L_pG", "p_G")]:
        value = make_line(line_id, cell_id, gate3_result_span["span_sha256"])
        validate(value, line_contract, line_contract)
        check_line_semantics(value, line_id, cell_id)
        data = canonical(value)
        path = ROOT / "generated/lines" / f"{digest(data)}--{line_id}.json"
        write_new(path, data)
        line_payloads[line_id] = value
        line_refs.append({"line_id": line_id, "payload": content_ref(path)})

    def transport(transport_id: str, edge_id: str, label: str, target: str) -> dict[str, Any]:
        return {
            "transport_id": transport_id,
            "edge_id": edge_id,
            "label": label,
            "domain_line_id": "L_r",
            "codomain_line_id": target,
            "map_kind": "ABSTRACT_UNITARY_HERMITIAN_LINE_MORPHISM",
            "unitary_relations": [
                f"{transport_id}^* {transport_id}=id_L_r",
                f"{transport_id} {transport_id}^*=id_{target}",
                f"{transport_id}^* h_{target} {transport_id}=h_L_r",
            ],
            "coordinate_scalar_present": False,
        }

    instance = {
        "schema": "rd22.step11.v009-01.pb-line-rooted-star.v001",
        "box_id": "BX-LINE-V009-01-PB",
        "row_id": "C-B-V009-01",
        "source_bindings": [
            decision_span,
            gate3_spec_span,
            gate3_result_span,
            v011_open_span,
            v011_star_span,
            u7_pb_span,
        ],
        "ruling": content_ref(decision_copy),
        "gate3_form": {
            "spec": content_ref(gate3_spec_copy),
            "result": content_ref(gate3_result_copy),
            "form_id": "GATE3_M0_IDENTITY_FIBER_FORM",
            "degree": 0,
            "equivalence": "UNIQUE_MODULO_OVERALL_CONGRUENCE",
            "coordinate_basis_licensed": False,
        },
        "topology": {
            "complex_id": "K_open_PB",
            "root_vertex_id": "r",
            "vertices": ["r", "p_M", "p_Q", "p_G"],
            "edges": [
                {"edge_id": "e_M", "label": "M", "source": "r", "target": "p_M"},
                {"edge_id": "e_Q", "label": "Q", "source": "r", "target": "p_Q"},
                {"edge_id": "e_G", "label": "G", "source": "r", "target": "p_G"},
            ],
        },
        "line_subobjects": line_refs,
        "edge_transports": [
            transport("U_eM", "e_M", "M", "L_pM"),
            transport("U_eQ", "e_Q", "Q", "L_pQ"),
            transport("U_eG", "e_G", "G", "L_pG"),
        ],
        "endpoint_carrier": {
            "carrier_id": "E_open_PB",
            "direct_sum_order": ["L_r", "L_pM", "L_pQ", "L_pG"],
            "canonical_summand_inclusions": ["iota_L_r", "iota_L_pM", "iota_L_pQ", "iota_L_pG"],
        },
        "licenses": {"basis": False, "scalar_trivialization": False, "unit_representative": False},
    }

    validate(instance, contract, contract)
    for ref in instance["source_bindings"]:
        verify_ref(ref)
    for ref in [instance["ruling"], instance["gate3_form"]["spec"], instance["gate3_form"]["result"]]:
        verify_ref(ref)
    check_instance_semantics(instance, line_payloads)

    instance_data = canonical(instance)
    instance_sha = digest(instance_data)
    instance_path = ROOT / "generated/instance" / f"{instance_sha}--C-B-V009-01-PB.json"
    component_path = ROOT / "generated/components" / f"{instance_sha}.json"
    write_new(instance_path, instance_data)
    write_new(component_path, instance_data)

    controls = []
    mutations: list[tuple[str, Any, str]] = []
    bad_license = json.loads(instance_data)
    bad_license["licenses"]["basis"] = True
    mutations.append(("basis_license_flip", bad_license, "SCHEMA_CONFORMANCE"))
    duplicate_line = json.loads(instance_data)
    duplicate_line["line_subobjects"][1]["line_id"] = "L_r"
    mutations.append(("duplicate_line_id", duplicate_line, "SCHEMA_CONFORMANCE"))
    bad_transport = json.loads(instance_data)
    bad_transport["edge_transports"][0]["coordinate_scalar_present"] = True
    mutations.append(("coordinate_transport_scalar", bad_transport, "SCHEMA_CONFORMANCE"))
    missing_relation = json.loads(instance_data)
    missing_relation["edge_transports"][0]["unitary_relations"] = missing_relation["edge_transports"][0]["unitary_relations"][:2]
    mutations.append(("unitarity_relation_removed", missing_relation, "SCHEMA_CONFORMANCE"))

    for name, mutated, expected_code in mutations:
        observed = "ACCEPT"
        try:
            validate(mutated, contract, contract)
            check_instance_semantics(mutated, line_payloads)
        except BuildError as exc:
            observed = str(exc).split(":", 1)[0]
        if observed != expected_code:
            raise BuildError(f"NEGATIVE_CONTROL:{name}:{expected_code}:{observed}")
        controls.append({"control": name, "expected": expected_code, "observed": observed, "result": "PASS"})

    compile_result = {
        "schema": "rd22.step11.pb-instance-compilation.v001",
        "row_id": "C-B-V009-01",
        "target_id": "CS:C-B-V009-01:actual-object-fibers-and-inclusion",
        "box_id": "BX-LINE-V009-01-PB",
        "outcome": "PASS_COMPONENT_BUILT",
        "component_sha256": instance_sha,
        "line_payload_sha256s": [item["payload"]["sha256"] for item in line_refs],
        "source_pins_verified": len(EXPECTED),
        "basis_or_trivialization_licensed": False,
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
    }
    status = {
        "schema": "rd22.step11.row-status.v002",
        "row_id": "C-B-V009-01",
        "status": "PARTIAL_CARRIER_READY_ALIAS_CORPUS_ABSENT",
        "produced_components": [instance_sha],
        "remaining_missing": [
            "CD:C-B-V009-01:abstract-line-alias-corpus exact members[]",
            "CD:C-B-V009-01:abstract-line-alias-corpus pre-query member-selection authority",
        ],
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
    }
    self_check = {
        "schema": "rd22.step11.pb-instance-self-check.v001",
        "actual_compile": "PASS_COMPONENT_BUILT",
        "schema_validated": True,
        "content_and_span_refs_verified": True,
        "distinct_line_ids": 4,
        "inclusions_verified": 4,
        "induced_forms_verified": 4,
        "unitary_transports_verified": 3,
        "negative_controls": controls,
        "basis_or_trivialization_licensed": False,
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
    }
    write_new(ROOT / "generated/compile_result.json", canonical(compile_result))
    write_new(ROOT / "generated/row_status.json", canonical(status))
    write_new(ROOT / "generated/self_check.json", canonical(self_check))

    rows = []
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and item.name != "inventory.generated.json"):
        data = path.read_bytes()
        rows.append({"byte_length": len(data), "relative_path": str(path.relative_to(ROOT)), "sha256": digest(data)})
    inventory = {"schema": "rd22.step11.pb-instance-inventory.v001", "files": rows}
    write_new(ROOT / "inventory.generated.json", canonical(inventory))

    print(json.dumps({
        "outcome": "PASS_COMPONENT_BUILT",
        "component_sha256": instance_sha,
        "line_payloads": len(line_refs),
        "unitary_transports": 3,
        "inventory_files": len(rows),
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
    }, sort_keys=True))


def main() -> int:
    try:
        build()
    except (BuildError, OSError, json.JSONDecodeError) as exc:
        print(f"PB_INSTANCE_BUILD_FAIL {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
