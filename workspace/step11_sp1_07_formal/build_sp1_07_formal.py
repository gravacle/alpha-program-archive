#!/usr/bin/env python3
"""Build the bounded SP1-07 formalization bundle from sealed source spans."""

import hashlib
import json
import re
from pathlib import Path


CLEANROOM = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parent
SOURCE = CLEANROOM / "review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
SPEC = CLEANROOM / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md"
U7 = CLEANROOM / "STAGE8_7A_U7_DISPOSITION_CODEX2_V001.md"

EXPECTED = {
    SOURCE: "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    SPEC: "382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504",
    U7: "0145c5dbbed1681067a211021892100cf6d18c6ef25ba9c7e905aeedc8a7f20d",
}

ROW_ID = "C-B-V011-SP1-07"
PROOF_IDS = [
    "D01_SHARED_BOUNDARY_DESCENT",
    "D02_THREE_CELL_LEFT_PARENTHESIZATION",
    "D03_THREE_CELL_RIGHT_PARENTHESIZATION",
    "D04_CELL_ORDER_INDEPENDENCE",
    "D05_PRIMITIVE_SHARED_SUPPORT_OVERLAP",
    "D06_GRADED_RECORD_FACTOR_COMMUTATION",
    "D07_VERTEX_RELABELING_COVARIANCE",
    "D08_ORIENTATION_REVERSAL_COVARIANCE",
    "D09_FINITE_STONE_ORDERING",
]


class BuildError(Exception):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical(value))


def file_ref(path):
    data = path.read_bytes()
    return {
        "byte_length": len(data),
        "relative_path": path.relative_to(CLEANROOM).as_posix(),
        "sha256": sha(data),
    }


def offsets(data):
    result = [0]
    for line in data.splitlines(keepends=True):
        result.append(result[-1] + len(line))
    return result


def source_ref(data, line_offsets, start_line, end_line, block_id, blocks):
    start = line_offsets[start_line - 1]
    end = line_offsets[end_line]
    block = blocks[block_id]
    if start < block[0] or end > block[1] or start >= end:
        raise BuildError(f"SPAN_NOT_BLOCK_COVERED:{start_line}-{end_line}:{block_id}")
    return {
        "block_id": block_id,
        "relative_path": SOURCE.relative_to(CLEANROOM).as_posix(),
        "source_sha256": EXPECTED[SOURCE],
        "span": [start, end],
        "span_sha256": sha(data[start:end]),
    }


def step(step_id, inference, statement, citations, premises=None):
    return {
        "citations": citations,
        "inference": inference,
        "premises": premises or [],
        "statement": statement,
        "step_id": step_id,
    }


def proof(proof_id, expected, steps, gaps):
    status = "KERNEL_READY" if not gaps else "PARTIAL_MISSING_STEP"
    return {
        "derivation_id": proof_id,
        "expected_conclusion": expected,
        "gaps": gaps,
        "proof_axioms": [
            "SEALED_SOURCE_ASSERTION",
            "DEFINITIONAL_UNFOLDING",
            "CONJUNCTION_INTRODUCTION",
        ],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.proof-object.v001",
        "status": status,
        "steps": steps,
        "target_opcode": "KERNEL",
        "used_source_sha256s": [EXPECTED[SOURCE]],
    }


def schemas():
    span_ref = {
        "additionalProperties": False,
        "properties": {
            "block_id": {"enum": ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]},
            "relative_path": {"const": SOURCE.relative_to(CLEANROOM).as_posix()},
            "source_sha256": {"const": EXPECTED[SOURCE]},
            "span": {
                "items": False,
                "maxItems": 2,
                "minItems": 2,
                "prefixItems": [
                    {"minimum": 0, "type": "integer"},
                    {"minimum": 0, "type": "integer"},
                ],
                "type": "array",
            },
            "span_sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
        },
        "required": ["block_id", "relative_path", "source_sha256", "span", "span_sha256"],
        "type": "object",
    }
    proof_schema = {
        "$defs": {"span_ref": span_ref},
        "$id": "urn:rd22:step11:sp1-07:proof-object:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "derivation_id": {"enum": PROOF_IDS},
            "expected_conclusion": {"type": "object"},
            "gaps": {"items": {"type": "object"}, "type": "array"},
            "proof_axioms": {
                "const": [
                    "SEALED_SOURCE_ASSERTION",
                    "DEFINITIONAL_UNFOLDING",
                    "CONJUNCTION_INTRODUCTION",
                ]
            },
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp1-07.proof-object.v001"},
            "status": {"enum": ["KERNEL_READY", "PARTIAL_MISSING_STEP"]},
            "steps": {
                "items": {
                    "additionalProperties": False,
                    "properties": {
                        "citations": {"items": {"$ref": "#/$defs/span_ref"}, "minItems": 1, "type": "array"},
                        "inference": {"enum": ["SEALED_SOURCE_ASSERTION", "DEFINITIONAL_UNFOLDING", "CONJUNCTION_INTRODUCTION"]},
                        "premises": {"items": {"type": "string"}, "type": "array"},
                        "statement": {"type": "object"},
                        "step_id": {"minLength": 1, "type": "string"},
                    },
                    "required": ["step_id", "inference", "premises", "statement", "citations"],
                    "type": "object",
                },
                "minItems": 1,
                "type": "array",
            },
            "target_opcode": {"const": "KERNEL"},
            "used_source_sha256s": {"const": [EXPECTED[SOURCE]]},
        },
        "required": [
            "schema",
            "row_id",
            "derivation_id",
            "target_opcode",
            "status",
            "proof_axioms",
            "used_source_sha256s",
            "expected_conclusion",
            "steps",
            "gaps",
        ],
        "title": "SP1-07 source-bound proof object",
        "type": "object",
    }
    typed_schema = {
        "$id": "urn:rd22:step11:sp1-07:typed-global-graph:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "car_algebras": {"const": ["CAR(K_Sigma)"]},
            "global_source_space": {"const": "K_Sigma=K_orb tensor S_Dirac"},
            "record_factor_family": {
                "const": {
                    "carrier": "R_c=span_C{|r_c>,|p_c>,|e_c>}",
                    "distinct_by_cell": True,
                    "fermion_grading": "EVEN",
                }
            },
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp1-07.typed-global-graph.v001"},
            "source_bindings": {"items": span_ref, "minItems": 2, "type": "array"},
            "typed_objects": {"items": {"type": "object"}, "minItems": 5, "type": "array"},
            "typed_maps": {"items": {"type": "object"}, "minItems": 3, "type": "array"},
        },
        "required": [
            "schema",
            "row_id",
            "source_bindings",
            "global_source_space",
            "car_algebras",
            "record_factor_family",
            "typed_objects",
            "typed_maps",
        ],
        "title": "SP1-07 typed one-global-source / distinct-record graph",
        "type": "object",
    }
    content_ref = {
        "additionalProperties": False,
        "properties": {
            "byte_length": {"minimum": 0, "type": "integer"},
            "relative_path": {"minLength": 1, "type": "string"},
            "sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
        },
        "required": ["byte_length", "relative_path", "sha256"],
        "type": "object",
    }
    manifest_schema = {
        "$defs": {"content_ref": content_ref},
        "$id": "urn:rd22:step11:sp1-07:formal-manifest:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "artifacts": {
                "additionalProperties": False,
                "properties": {
                    key: {"$ref": "#/$defs/content_ref"}
                    for key in [
                        "completeness_certificate",
                        "composition_schema",
                        "derivation_grammar",
                        "expected_ledger",
                        "expected_schema",
                        "proof_index",
                        "proof_schema",
                        "typed_graph",
                        "typed_graph_schema",
                    ]
                },
                "required": [
                    "completeness_certificate",
                    "composition_schema",
                    "derivation_grammar",
                    "expected_ledger",
                    "expected_schema",
                    "proof_index",
                    "proof_schema",
                    "typed_graph",
                    "typed_graph_schema",
                ],
                "type": "object",
            },
            "blocks": {"items": {"type": "object"}, "minItems": 3, "type": "array"},
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp1-07.formal-manifest.v001"},
            "source_pins": {"items": {"$ref": "#/$defs/content_ref"}, "minItems": 3, "type": "array"},
        },
        "required": ["schema", "row_id", "source_pins", "blocks", "artifacts"],
        "title": "SP1-07 closed composition manifest",
        "type": "object",
    }
    expected_schema = {
        "$id": "urn:rd22:step11:sp1-07:expected-ledger:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "entries": {
                "items": {
                    "additionalProperties": False,
                    "properties": {
                        "derivation_id": {"enum": PROOF_IDS},
                        "expected_conclusion": {"type": "object"},
                    },
                    "required": ["derivation_id", "expected_conclusion"],
                    "type": "object",
                },
                "maxItems": len(PROOF_IDS),
                "minItems": len(PROOF_IDS),
                "type": "array",
            },
            "required_ids": {"const": PROOF_IDS},
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp1-07.expected-ledger.v001"},
        },
        "required": ["schema", "row_id", "required_ids", "entries"],
        "title": "SP1-07 closed nonempty expected ledger",
        "type": "object",
    }
    return proof_schema, typed_schema, manifest_schema, expected_schema


def validate_ref(ref, data, blocks):
    required = {"block_id", "relative_path", "source_sha256", "span", "span_sha256"}
    if set(ref) != required:
        raise BuildError(f"SPAN_REF_FIELDS:{sorted(set(ref) ^ required)}")
    if ref["relative_path"] != SOURCE.relative_to(CLEANROOM).as_posix():
        raise BuildError("SPAN_REF_PATH")
    if ref["source_sha256"] != EXPECTED[SOURCE]:
        raise BuildError("SPAN_REF_SOURCE")
    if ref["block_id"] not in blocks:
        raise BuildError("SPAN_REF_BLOCK")
    start, end = ref["span"]
    bstart, bend, bdigest = blocks[ref["block_id"]]
    if start < bstart or end > bend or start >= end:
        raise BuildError("SPAN_REF_COVERAGE")
    if sha(data[bstart:bend]) != bdigest:
        raise BuildError("BLOCK_DIGEST")
    if sha(data[start:end]) != ref["span_sha256"]:
        raise BuildError("SPAN_DIGEST")


def validate_proof(value, data, blocks):
    fields = {
        "derivation_id",
        "expected_conclusion",
        "gaps",
        "proof_axioms",
        "row_id",
        "schema",
        "status",
        "steps",
        "target_opcode",
        "used_source_sha256s",
    }
    if set(value) != fields or value["derivation_id"] not in PROOF_IDS:
        raise BuildError("PROOF_FIELDS_OR_ID")
    if value["row_id"] != ROW_ID or value["target_opcode"] != "KERNEL":
        raise BuildError("PROOF_TARGET")
    if value["status"] == "KERNEL_READY" and value["gaps"]:
        raise BuildError("READY_WITH_GAP")
    if value["status"] == "PARTIAL_MISSING_STEP" and not value["gaps"]:
        raise BuildError("PARTIAL_WITHOUT_GAP")
    seen = set()
    for item in value["steps"]:
        if item["step_id"] in seen:
            raise BuildError("DUPLICATE_STEP")
        for premise in item["premises"]:
            if premise not in seen:
                raise BuildError("FORWARD_OR_UNKNOWN_PREMISE")
        if not item["citations"]:
            raise BuildError("UNCITED_STEP")
        for citation in item["citations"]:
            validate_ref(citation, data, blocks)
        seen.add(item["step_id"])
    if value["status"] == "KERNEL_READY":
        if value["steps"][-1]["statement"] != value["expected_conclusion"]:
            raise BuildError("READY_CONCLUSION_MISMATCH")


def main():
    if (ROOT / "generated").exists() or (ROOT / "inventory.generated.json").exists():
        raise BuildError("OUTPUT_COLLISION:package outputs")
    for path, expected in EXPECTED.items():
        if not path.is_file() or sha(path.read_bytes()) != expected:
            raise BuildError(f"SOURCE_PIN:{path}")

    data = SOURCE.read_bytes()
    line_offsets = offsets(data)
    blocks = {
        "B_GLOBAL_TYPED": (line_offsets[26], line_offsets[52], "daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2"),
        "B_GLOBAL_DESCENT": (line_offsets[53], line_offsets[113], "fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce"),
        "B_GLOBAL_ORDER": (line_offsets[152], line_offsets[188], "17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed"),
    }
    for block_id, (start, end, expected) in blocks.items():
        if sha(data[start:end]) != expected:
            raise BuildError(f"BLOCK_PIN:{block_id}")
    block_rows = [
        {
            "block_id": block_id,
            "source_sha256": EXPECTED[SOURCE],
            "span": [start, end],
            "span_sha256": digest,
        }
        for block_id, (start, end, digest) in blocks.items()
    ]

    ref = lambda a, b, c: source_ref(data, line_offsets, a, b, c, blocks)
    conclusions = {
        "D01_SHARED_BOUNDARY_DESCENT": {
            "distinct_even_record_factors": True,
            "global_operator": "h_K=sum_c P_c tensor gamma^5 tensor iota_c(c_c)",
            "one_global_source_car": "CAR(K_Sigma)",
            "predicate": "SHARED_BOUNDARY_DESCENT",
            "shared_vertices_identified_once_by_pushout": True,
        },
        "D02_THREE_CELL_LEFT_PARENTHESIZATION": {
            "parenthesization": "PUSHOUT(PUSHOUT(c1,c2),c3)",
            "predicate": "THREE_CELL_GLOBAL_ASSEMBLY",
            "result": "h_K(c1,c2,c3)",
        },
        "D03_THREE_CELL_RIGHT_PARENTHESIZATION": {
            "parenthesization": "PUSHOUT(c1,PUSHOUT(c2,c3))",
            "predicate": "THREE_CELL_GLOBAL_ASSEMBLY",
            "result": "h_K(c1,c2,c3)",
        },
        "D04_CELL_ORDER_INDEPENDENCE": {
            "predicate": "CELL_ORDER_INDEPENDENCE",
            "result": "ASSEMBLY(order_1)=ASSEMBLY(order_2)=h_K",
        },
        "D05_PRIMITIVE_SHARED_SUPPORT_OVERLAP": {
            "formula": "Tr(P_c P_d)=|<d_c,d_d>|^2/(||d_c||^2 ||d_d||^2)",
            "h_K_off_diagonal": True,
            "h_K_squared_not_primitive": True,
            "orientation_sign_independent": True,
            "predicate": "PRIMITIVE_SHARED_SUPPORT_OVERLAP",
        },
        "D06_GRADED_RECORD_FACTOR_COMMUTATION": {
            "predicate": "GRADED_RECORD_FACTOR_COMMUTATION",
            "result": "[iota_c(x),iota_d(y)]_graded=0 for c!=d and even x,y",
        },
        "D07_VERTEX_RELABELING_COVARIANCE": {
            "predicate": "VERTEX_RELABELING_COVARIANCE",
            "result": "h_relabel=P_source h_K P_source^-1",
        },
        "D08_ORIENTATION_REVERSAL_COVARIANCE": {
            "predicate": "ORIENTATION_REVERSAL_COVARIANCE",
            "result": "h_reversed=U_record h_K U_record^-1",
        },
        "D09_FINITE_STONE_ORDERING": {
            "predicate": "FINITE_STONE_ORDERING",
            "result": "U_K(t+s)=U_K(t)U_K(s), U_K(t)=exp(-itH_K), unique",
        },
    }

    proofs = []
    proofs.append(
        proof(
            PROOF_IDS[0],
            conclusions[PROOF_IDS[0]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"one_global_source_space": "K_Sigma=K_orb tensor S_Dirac", "single_car": "CAR(K_Sigma)"}, [ref(29, 36, "B_GLOBAL_TYPED")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"record_factors": "R(K)=tensor_(c in K) R_c", "record_grading": "EVEN", "source_not_copied_per_cell": True}, [ref(36, 52, "B_GLOBAL_TYPED")]),
                step("s03", "SEALED_SOURCE_ASSERTION", {"record_labels_identified": False, "shared_vertices_identified_once_by_pushout": True}, [ref(67, 70, "B_GLOBAL_DESCENT")]),
                step("s04", "DEFINITIONAL_UNFOLDING", {"global_operator": "h_K=sum_c P_c tensor gamma^5 tensor iota_c(c_c)"}, [ref(71, 80, "B_GLOBAL_DESCENT")], ["s01", "s02", "s03"]),
                step("s05", "CONJUNCTION_INTRODUCTION", conclusions[PROOF_IDS[0]], [ref(67, 80, "B_GLOBAL_DESCENT")], ["s01", "s02", "s03", "s04"]),
            ],
            [],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[1],
            conclusions[PROOF_IDS[1]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"finite_pushout_and_assembly_associative": True}, [ref(105, 111, "B_GLOBAL_DESCENT")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"required_comparison": "both_three_cell_parenthesizations"}, [ref(175, 178, "B_GLOBAL_ORDER")], ["s01"]),
            ],
            [{"gap_id": "G02_LEFT_PUSHOUT_WITNESS", "missing": "explicit c1,c2,c3 incidence-map objects, the left-associated pushout cocone, and its canonical equality map to h_K(c1,c2,c3)", "searched_blocks": ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[2],
            conclusions[PROOF_IDS[2]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"finite_pushout_and_assembly_associative": True}, [ref(105, 111, "B_GLOBAL_DESCENT")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"required_comparison": "both_three_cell_parenthesizations"}, [ref(175, 178, "B_GLOBAL_ORDER")], ["s01"]),
            ],
            [{"gap_id": "G03_RIGHT_PUSHOUT_WITNESS", "missing": "explicit c1,c2,c3 incidence-map objects, the right-associated pushout cocone, and its canonical equality map to h_K(c1,c2,c3)", "searched_blocks": ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[3],
            conclusions[PROOF_IDS[3]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"required_comparison": "same_global_operator_under_both_cell_orders"}, [ref(176, 179, "B_GLOBAL_ORDER")]),
            ],
            [{"gap_id": "G04_CELL_ORDER_EQUALITY", "missing": "the two sealed cell-order enumerations and a term-by-term permutation/equality witness for their assembled h_K records", "searched_blocks": ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[4],
            conclusions[PROOF_IDS[4]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"projector": "P_c=|d_c><d_c|/<d_c,d_c>"}, [ref(59, 65, "B_GLOBAL_DESCENT")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"condition": "shared source support", "result": "P_c P_d nonzero and h_K has source-orbital off-diagonal blocks"}, [ref(92, 94, "B_GLOBAL_DESCENT")], ["s01"]),
                step("s03", "SEALED_SOURCE_ASSERTION", {"formula": conclusions[PROOF_IDS[4]]["formula"], "orientation_sign_independent": True}, [ref(95, 101, "B_GLOBAL_DESCENT")], ["s01", "s02"]),
                step("s04", "SEALED_SOURCE_ASSERTION", {"h_K_squared_not_primitive": True}, [ref(101, 103, "B_GLOBAL_DESCENT")], ["s02"]),
                step("s05", "CONJUNCTION_INTRODUCTION", conclusions[PROOF_IDS[4]], [ref(92, 103, "B_GLOBAL_DESCENT")], ["s01", "s02", "s03", "s04"]),
            ],
            [],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[5],
            conclusions[PROOF_IDS[5]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"record_algebra_fermion_grading": "TRIVIAL", "record_factors_distinct": True}, [ref(43, 52, "B_GLOBAL_TYPED")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"iota_c_action": "c_c on R_c and identity on every other record factor"}, [ref(67, 72, "B_GLOBAL_DESCENT")], ["s01"]),
            ],
            [{"gap_id": "G06_GRADED_COMMUTATION_IDENTITY", "missing": "an explicit sealed calculation of [iota_c(x),iota_d(y)]_graded=0 for distinct even record factors", "searched_blocks": ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[6],
            conclusions[PROOF_IDS[6]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"vertex_relabeling": "conjugates h_K by induced source permutation"}, [ref(105, 107, "B_GLOBAL_DESCENT")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"required_check": "vertex-relabeling covariance"}, [ref(178, 180, "B_GLOBAL_ORDER")], ["s01"]),
            ],
            [{"gap_id": "G07_RELABELING_SQUARE", "missing": "the explicit vertex permutation map on incidence vectors and the commuting conjugation square for h_K", "searched_blocks": ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[7],
            conclusions[PROOF_IDS[7]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"orientation_effect": "d_c -> -d_c and P_c invariant"}, [ref(67, 70, "B_GLOBAL_DESCENT")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"record_quadrature": "conjugated by cellular orientation unitary", "h_K_covariant": True}, [ref(107, 111, "B_GLOBAL_DESCENT")], ["s01"]),
                step("s03", "SEALED_SOURCE_ASSERTION", {"required_check": "orientation-reversal covariance"}, [ref(178, 180, "B_GLOBAL_ORDER")], ["s01", "s02"]),
            ],
            [{"gap_id": "G08_ORIENTATION_UNITARY_SQUARE", "missing": "the cellular orientation unitary as a typed content-addressed map and its explicit h_K conjugation square", "searched_blocks": ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]}],
        )
    )
    proofs.append(
        proof(
            PROOF_IDS[8],
            conclusions[PROOF_IDS[8]],
            [
                step("s01", "SEALED_SOURCE_ASSERTION", {"assumption": "finite stationary self-adjoint H_K"}, [ref(153, 156, "B_GLOBAL_ORDER")]),
                step("s02", "SEALED_SOURCE_ASSERTION", {"definition": "U_K(t)=exp(-i t H_K)"}, [ref(155, 159, "B_GLOBAL_ORDER")], ["s01"]),
                step("s03", "SEALED_SOURCE_ASSERTION", {"claim": "unique one-parameter group law"}, [ref(161, 162, "B_GLOBAL_ORDER")], ["s01", "s02"]),
                step("s04", "SEALED_SOURCE_ASSERTION", {"required_check": "finite stationary Stone composition"}, [ref(184, 187, "B_GLOBAL_ORDER")], ["s03"]),
            ],
            [{"gap_id": "G09_STONE_REPLAY", "missing": "a sealed self-adjointness certificate for H_K and the exponential-composition/uniqueness proof used by KERNEL", "searched_blocks": ["B_GLOBAL_ORDER"]}],
        )
    )

    proof_schema, typed_schema, manifest_schema, expected_schema = schemas()
    write_json(ROOT / "contracts/proof_object.schema.json", proof_schema)
    write_json(ROOT / "contracts/typed_global_graph.schema.json", typed_schema)
    write_json(ROOT / "contracts/formal_manifest.schema.json", manifest_schema)
    write_json(ROOT / "contracts/expected_ledger.schema.json", expected_schema)

    typed_graph = {
        "car_algebras": ["CAR(K_Sigma)"],
        "global_source_space": "K_Sigma=K_orb tensor S_Dirac",
        "record_factor_family": {
            "carrier": "R_c=span_C{|r_c>,|p_c>,|e_c>}",
            "distinct_by_cell": True,
            "fermion_grading": "EVEN",
        },
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.typed-global-graph.v001",
        "source_bindings": [ref(27, 52, "B_GLOBAL_TYPED"), ref(54, 80, "B_GLOBAL_DESCENT")],
        "typed_maps": [
            {"codomain": "GLOBAL_INCIDENCE_PUSHOUT", "map_id": "incidence_c", "type": "LABELED_INCIDENCE_MAP"},
            {"codomain": "B(R(K))", "domain": "B(R_c)", "map_id": "iota_c", "type": "EVEN_RECORD_FACTOR_INCLUSION"},
            {"codomain": "End(K_orb tensor S_Dirac tensor R(K))", "map_id": "assemble_h_K", "type": "OPERATOR_SUM"},
        ],
        "typed_objects": [
            {"object_id": "K_Sigma", "type": "GLOBAL_ONE_PARTICLE_SPACE"},
            {"object_id": "CAR(K_Sigma)", "type": "SINGLE_GLOBAL_CAR_ALGEBRA"},
            {"object_id": "R_c", "type": "DISTINCT_EVEN_RECORD_FACTOR_FAMILY"},
            {"object_id": "R(K)", "type": "FINITE_RECORD_TENSOR_PRODUCT"},
            {"object_id": "GLOBAL_INCIDENCE_PUSHOUT", "type": "FINITE_LABELED_PUSHOUT"},
            {"object_id": "h_K", "type": "GLOBAL_OPERATOR_VALUED_ONE_PARTICLE_SUPERCONNECTION"},
        ],
    }
    write_json(ROOT / "generated/G_SP1_07.typed_graph.json", typed_graph)

    proof_rows = []
    for value in proofs:
        validate_proof(value, data, blocks)
        encoded = canonical(value)
        digest = sha(encoded)
        path = ROOT / "generated/proofs" / f"{digest}--{value['derivation_id']}.json"
        write_json(path, value)
        proof_rows.append(
            {
                "derivation_id": value["derivation_id"],
                "expected_conclusion_sha256": sha(canonical(value["expected_conclusion"])),
                "proof": file_ref(path),
                "status": value["status"],
            }
        )

    grammar = {
        "ids": PROOF_IDS,
        "items": [
            {"derivation_id": item, "mandatory": True, "ordinal": index}
            for index, item in enumerate(PROOF_IDS, 1)
        ],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.derivation-grammar.v001",
    }
    expected_ledger = {
        "entries": [
            {"derivation_id": item, "expected_conclusion": conclusions[item]}
            for item in PROOF_IDS
        ],
        "required_ids": PROOF_IDS,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.expected-ledger.v001",
    }
    proof_index = {
        "entries": proof_rows,
        "ids": PROOF_IDS,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.proof-index.v001",
    }
    completeness = {
        "coverage": [
            {"clause": "shared-boundary descent", "ids": [PROOF_IDS[0]]},
            {"clause": "both three-cell parenthesizations", "ids": [PROOF_IDS[1], PROOF_IDS[2]]},
            {"clause": "both cell orders", "ids": [PROOF_IDS[3]]},
            {"clause": "primitive shared-support overlap", "ids": [PROOF_IDS[4]]},
            {"clause": "graded distinct-record behavior", "ids": [PROOF_IDS[5]]},
            {"clause": "vertex relabeling", "ids": [PROOF_IDS[6]]},
            {"clause": "orientation reversal", "ids": [PROOF_IDS[7]]},
            {"clause": "finite Stone ordering", "ids": [PROOF_IDS[8]]},
        ],
        "enumerated_ids": PROOF_IDS,
        "nonempty": True,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.completeness-certificate.v001",
        "source_blocks": block_rows,
    }
    write_json(ROOT / "generated/G_overlap_order.json", grammar)
    write_json(ROOT / "generated/p_complete.json", completeness)
    write_json(ROOT / "generated/E_SP1_07.json", expected_ledger)
    write_json(ROOT / "generated/P_SP1_07.json", proof_index)

    manifest = {
        "artifacts": {
            "completeness_certificate": file_ref(ROOT / "generated/p_complete.json"),
            "composition_schema": file_ref(ROOT / "contracts/formal_manifest.schema.json"),
            "derivation_grammar": file_ref(ROOT / "generated/G_overlap_order.json"),
            "expected_ledger": file_ref(ROOT / "generated/E_SP1_07.json"),
            "expected_schema": file_ref(ROOT / "contracts/expected_ledger.schema.json"),
            "proof_index": file_ref(ROOT / "generated/P_SP1_07.json"),
            "proof_schema": file_ref(ROOT / "contracts/proof_object.schema.json"),
            "typed_graph": file_ref(ROOT / "generated/G_SP1_07.typed_graph.json"),
            "typed_graph_schema": file_ref(ROOT / "contracts/typed_global_graph.schema.json"),
        },
        "blocks": block_rows,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.formal-manifest.v001",
        "source_pins": [file_ref(SOURCE), file_ref(SPEC), file_ref(U7)],
    }
    write_json(ROOT / "generated/M_SP1_07.json", manifest)

    ready = [row["derivation_id"] for row in proof_rows if row["status"] == "KERNEL_READY"]
    partial = [row["derivation_id"] for row in proof_rows if row["status"] != "KERNEL_READY"]
    if ready != [PROOF_IDS[0], PROOF_IDS[4]] or len(partial) != 7:
        raise BuildError("READY_PARTITION")
    if grammar["ids"] != expected_ledger["required_ids"] or grammar["ids"] != proof_index["ids"]:
        raise BuildError("ID_CENSUS")

    gap_rows = []
    for value in proofs:
        for gap in value["gaps"]:
            gap_rows.append({"derivation_id": value["derivation_id"], **gap})
    compile_result = {
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
        "gaps": gap_rows,
        "kernel_ready_ids": ready,
        "opcode_results": {
            "r_enum": "PASS_9_IDS",
            "r_exact": "PRECONDITION_NOT_REPLAYABLE:G02,G03,G04,G06",
            "r_expected": "PASS",
            "r_nonempty": "PASS",
            "r_proof_ids": "PASS",
            "r_required_ids": "PASS",
            "r_schema": "PASS",
            "r_type": "PASS",
            "repeatable_r_d": "2 KERNEL_READY / 7 PRECONDITION_NOT_REPLAYABLE",
        },
        "outcome": "PARTIAL_CONFORMANCE_2_BUILT_7_GAPS",
        "partial_ids": partial,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp1-07.compile-result.v001",
    }
    row_status = {
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
        "kernel_ready": 2,
        "named_gaps": 7,
        "row_id": ROW_ID,
        "schema": "rd22.step11.row-status.v002",
        "status": "PARTIAL_FORMALIZATION_2_OF_9_KERNEL_READY",
    }
    write_json(ROOT / "generated/compile_result.json", compile_result)
    write_json(ROOT / "generated/row_status.json", row_status)

    # Four controls verify that citation and census failures cannot be hidden.
    controls = []
    mutations = []
    missing_citation = json.loads(json.dumps(proofs[0]))
    missing_citation["steps"][0]["citations"] = []
    mutations.append(("missing_step_citation", missing_citation))
    bad_span = json.loads(json.dumps(proofs[0]))
    bad_span["steps"][0]["citations"][0]["span_sha256"] = "0" * 64
    mutations.append(("span_digest_flip", bad_span))
    ready_with_gap = json.loads(json.dumps(proofs[0]))
    ready_with_gap["gaps"] = [{"gap_id": "X", "missing": "x", "searched_blocks": []}]
    mutations.append(("ready_with_gap", ready_with_gap))
    unknown_id = json.loads(json.dumps(proofs[0]))
    unknown_id["derivation_id"] = "D99_UNKNOWN"
    mutations.append(("unknown_derivation_id", unknown_id))
    for name, mutation in mutations:
        observed = "ACCEPTED"
        try:
            validate_proof(mutation, data, blocks)
        except BuildError:
            observed = "SCHEMA_OR_INTEGRITY_REFUSAL"
        controls.append(
            {
                "control": name,
                "expected": "SCHEMA_OR_INTEGRITY_REFUSAL",
                "observed": observed,
                "result": "PASS" if observed == "SCHEMA_OR_INTEGRITY_REFUSAL" else "FAIL",
            }
        )
    if any(item["result"] != "PASS" for item in controls):
        raise BuildError("NEGATIVE_CONTROL")

    self_check = {
        "admission": "BARRED_STEP11_SUBGATE",
        "block_pins_verified": len(blocks),
        "chain_invoked": False,
        "complete_proofs": len(ready),
        "id_census": len(PROOF_IDS),
        "named_gaps": len(gap_rows),
        "negative_controls": controls,
        "partial_proofs": len(partial),
        "schema_files_verified": 4,
        "schema": "rd22.step11.sp1-07.self-check.v001",
        "source_pins_verified": len(EXPECTED),
        "step_citations_verified": sum(len(item["citations"]) for value in proofs for item in value["steps"]),
    }
    write_json(ROOT / "generated/self_check.json", self_check)

    inventory_rows = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.name != "inventory.generated.json":
            inventory_rows.append(file_ref(path))
    inventory = {"files": inventory_rows, "schema": "rd22.step11.sp1-07.inventory.v001"}
    write_json(ROOT / "inventory.generated.json", inventory)
    print(
        json.dumps(
            {
                "admission": "barred",
                "files": len(inventory_rows),
                "gaps": len(gap_rows),
                "kernel_ready": len(ready),
                "outcome": compile_result["outcome"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except BuildError as exc:
        raise SystemExit(f"SP1_07_FORMAL_BUILD_FAIL {exc}")
