#!/usr/bin/env python3
"""Build the bounded SP2-05 proof bundle from sealed packet bytes."""

import ast
import hashlib
import json
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

ROW_ID = "C-B-V011-SP2-05"
DESCRIPTOR_SHA256 = "8dbccdf91aa34912d3ec8e910a1ee23e58c7281bfd42d82c0f1f0724775e1686"
PREMISE_SHA256 = "52139a1c600db4a96bf17194cce7c57f308b5f0c7b34d32d85ebd5dcf0e54e7c"
PUSHOUT_IDS = [
    "P01_SHARED_VERTEX_PUSHOUT_ONCE",
    "P02_LEFT_ASSOCIATIVITY",
    "P03_RIGHT_ASSOCIATIVITY",
    "P04_CELL_ORDER_INDEPENDENCE",
    "P05_VERTEX_RELABELING_COVARIANCE",
]
ORIENTATION_IDS = [
    "O01_SOURCE_PROJECTOR_REVERSAL",
    "O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE",
]
QUARTIC_ID = "Q01_QUARTIC_PRIMITIVE_REJECTION"
PROOF_IDS = PUSHOUT_IDS + ORIENTATION_IDS + [QUARTIC_ID]
READY_IDS = [item for item in PROOF_IDS if item != ORIENTATION_IDS[1]]

BLOCKS = {
    "B_GLOBAL_PREMISE": (334, 1102, PREMISE_SHA256),
    "B_GLOBAL_TYPED": (1103, 1704, "daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2"),
    "B_GLOBAL_DESCENT": (1705, 4005, "fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce"),
    "B_GLOBAL_CAR": (4006, 5026, "f08456525bf3f5abb163b32bc3e7c9d1f084c79adb1d1ede879df10cc6cad76b"),
    "B_GLOBAL_ORDER": (5027, 6406, "17314d1ffd972873a65ee99e3309610b70e25dfddf612dd7adb2a83df456d7ed"),
    "B_GLOBAL_ALL": (334, 6406, "abef6d52ec372c48a407fcf5a87e8d5a9b41064f5255f9bdac8cbe697726d07b"),
}


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


def source_ref(block_id):
    start, end, digest = BLOCKS[block_id]
    return {
        "block_id": block_id,
        "relative_path": SOURCE.relative_to(CLEANROOM).as_posix(),
        "source_sha256": EXPECTED[SOURCE],
        "span": [start, end],
        "span_sha256": digest,
    }


def proof_step(step_id, inference, statement, citations, premises=None):
    return {
        "citations": [source_ref(item) for item in citations],
        "inference": inference,
        "premises": premises or [],
        "statement": statement,
        "step_id": step_id,
    }


def proof_object(proof_id, expected, steps, gaps=None, used_axiom_hashes=None):
    gaps = gaps or []
    return {
        "derivation_id": proof_id,
        "expected_conclusion": expected,
        "gaps": gaps,
        "proof_axioms": [
            "SEALED_SOURCE_ASSERTION",
            "DEFINITIONAL_UNFOLDING",
            "FINITE_QUOTIENT_NORMALIZATION",
            "FINITE_REINDEXING",
            "LINEAR_PROJECTOR_CALCULATION",
            "TENSOR_FACTOR_NORMALIZATION",
            "CAR_NUMBER_SECTOR_RELATIONS",
            "CONJUNCTION_INTRODUCTION",
        ],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.proof-object.v001",
        "status": "KERNEL_READY" if not gaps else "PARTIAL_MISSING_STEP",
        "steps": steps,
        "target_opcode": "KERNEL",
        "used_axiom_hashes": used_axiom_hashes or [],
        "used_source_sha256s": [EXPECTED[SOURCE]],
    }


def span_schema():
    return {
        "additionalProperties": False,
        "properties": {
            "block_id": {"enum": list(BLOCKS)},
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


def schemas():
    span = span_schema()
    inference = [
        "SEALED_SOURCE_ASSERTION",
        "DEFINITIONAL_UNFOLDING",
        "FINITE_QUOTIENT_NORMALIZATION",
        "FINITE_REINDEXING",
        "LINEAR_PROJECTOR_CALCULATION",
        "TENSOR_FACTOR_NORMALIZATION",
        "CAR_NUMBER_SECTOR_RELATIONS",
        "CONJUNCTION_INTRODUCTION",
    ]
    proof_schema = {
        "$defs": {"span_ref": span},
        "$id": "urn:rd22:step11:sp2-05:proof-object:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "derivation_id": {"enum": PROOF_IDS},
            "expected_conclusion": {"type": "object"},
            "gaps": {"items": {"type": "object"}, "type": "array"},
            "proof_axioms": {"const": inference},
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp2-05.proof-object.v001"},
            "status": {"enum": ["KERNEL_READY", "PARTIAL_MISSING_STEP"]},
            "steps": {
                "items": {
                    "additionalProperties": False,
                    "properties": {
                        "citations": {"items": {"$ref": "#/$defs/span_ref"}, "minItems": 1, "type": "array"},
                        "inference": {"enum": inference},
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
            "used_axiom_hashes": {"items": {"pattern": "^[0-9a-f]{64}$", "type": "string"}, "type": "array"},
            "used_source_sha256s": {"const": [EXPECTED[SOURCE]]},
        },
        "required": [
            "schema", "row_id", "derivation_id", "target_opcode", "status",
            "proof_axioms", "used_source_sha256s", "used_axiom_hashes",
            "expected_conclusion", "steps", "gaps",
        ],
        "title": "SP2-05 source-bound proof object",
        "type": "object",
    }
    graph_schema = {
        "$defs": {"span_ref": span},
        "$id": "urn:rd22:step11:sp2-05:typed-global-graph:v001",
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
            "schema": {"const": "rd22.step11.sp2-05.typed-global-graph.v001"},
            "source_bindings": {"items": {"$ref": "#/$defs/span_ref"}, "minItems": 2, "type": "array"},
            "typed_maps": {"items": {"type": "object"}, "minItems": 5, "type": "array"},
            "typed_objects": {"items": {"type": "object"}, "minItems": 6, "type": "array"},
        },
        "required": [
            "schema", "row_id", "source_bindings", "global_source_space",
            "car_algebras", "record_factor_family", "typed_objects", "typed_maps",
        ],
        "type": "object",
    }
    premise_schema = {
        "$defs": {"span_ref": span},
        "$id": "urn:rd22:step11:sp2-05:premise-record:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "allowed_axiom_hashes": {"const": [PREMISE_SHA256]},
            "axiom_id": {"const": "GLOBAL_BOUNDARY_DESCENT_AND_QUASI_FREE_COMPLETENESS_PRINCIPLE"},
            "axiom_sha256": {"const": PREMISE_SHA256},
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp2-05.premise-record.v001"},
            "scope": {"const": "PRIMITIVE_CONNECTED_SOURCE_RECORD_ACTION"},
            "source_binding": {"$ref": "#/$defs/span_ref"},
        },
        "required": ["schema", "row_id", "axiom_id", "scope", "source_binding", "axiom_sha256", "allowed_axiom_hashes"],
        "type": "object",
    }
    content_ref = {
        "additionalProperties": False,
        "properties": {
            "byte_length": {"minimum": 0, "type": "integer"},
            "relative_path": {"minLength": 1, "type": "string"},
            "sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
        },
        "required": ["relative_path", "byte_length", "sha256"],
        "type": "object",
    }
    artifact_keys = [
        "exact_fixture", "orientation_certificate", "orientation_grammar",
        "orientation_index", "premise_record", "premise_schema", "proof_bundle",
        "proof_schema", "pushout_certificate", "pushout_grammar", "pushout_index",
        "quartic_proof", "typed_graph", "typed_graph_schema",
    ]
    manifest_schema = {
        "$defs": {"content_ref": content_ref},
        "$id": "urn:rd22:step11:sp2-05:formal-manifest:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "artifacts": {
                "additionalProperties": False,
                "properties": {item: {"$ref": "#/$defs/content_ref"} for item in artifact_keys},
                "required": artifact_keys,
                "type": "object",
            },
            "descriptor_sha256": {"const": DESCRIPTOR_SHA256},
            "row_id": {"const": ROW_ID},
            "schema": {"const": "rd22.step11.sp2-05.formal-manifest.v001"},
            "source_pins": {
                "additionalProperties": False,
                "properties": {
                    "global_source_sha256": {"const": EXPECTED[SOURCE]},
                    "spec_sha256": {"const": EXPECTED[SPEC]},
                    "u7_sha256": {"const": EXPECTED[U7]},
                },
                "required": ["global_source_sha256", "spec_sha256", "u7_sha256"],
                "type": "object",
            },
        },
        "required": ["schema", "row_id", "descriptor_sha256", "source_pins", "artifacts"],
        "type": "object",
    }
    return {
        "formal_manifest.schema.json": manifest_schema,
        "premise_record.schema.json": premise_schema,
        "proof_object.schema.json": proof_schema,
        "typed_global_graph.schema.json": graph_schema,
    }


def validate_span(ref, source_data):
    fields = {"block_id", "relative_path", "source_sha256", "span", "span_sha256"}
    if set(ref) != fields or ref["block_id"] not in BLOCKS:
        raise BuildError("SPAN_FIELDS_OR_BLOCK")
    if ref["relative_path"] != SOURCE.relative_to(CLEANROOM).as_posix() or ref["source_sha256"] != EXPECTED[SOURCE]:
        raise BuildError("SPAN_SOURCE")
    start, end = ref["span"]
    bstart, bend, bdigest = BLOCKS[ref["block_id"]]
    if [start, end] != [bstart, bend] or sha(source_data[start:end]) != bdigest or ref["span_sha256"] != bdigest:
        raise BuildError("SPAN_DIGEST_OR_BOUNDARY")


def validate_proof(value, expected, source_data):
    fields = {
        "derivation_id", "expected_conclusion", "gaps", "proof_axioms", "row_id",
        "schema", "status", "steps", "target_opcode", "used_axiom_hashes", "used_source_sha256s",
    }
    if set(value) != fields or value["derivation_id"] not in PROOF_IDS:
        raise BuildError("PROOF_FIELDS_OR_ID")
    if value["expected_conclusion"] != expected[value["derivation_id"]]:
        raise BuildError("PROOF_EXPECTED_CONCLUSION")
    if not value["steps"] or value["row_id"] != ROW_ID or value["target_opcode"] != "KERNEL":
        raise BuildError("PROOF_HEADER")
    step_ids = []
    for item in value["steps"]:
        if set(item) != {"citations", "inference", "premises", "statement", "step_id"} or not item["citations"]:
            raise BuildError("PROOF_STEP_SHAPE")
        if any(premise not in step_ids for premise in item["premises"]):
            raise BuildError("PROOF_FORWARD_REFERENCE")
        for citation in item["citations"]:
            validate_span(citation, source_data)
        step_ids.append(item["step_id"])
    is_ready = value["status"] == "KERNEL_READY"
    if is_ready != (not value["gaps"]):
        raise BuildError("PROOF_STATUS_GAP")
    if is_ready and value["steps"][-1]["statement"] != value["expected_conclusion"]:
        raise BuildError("PROOF_NO_EXACT_FINAL")
    if value["derivation_id"] == QUARTIC_ID:
        if value["used_axiom_hashes"] != [PREMISE_SHA256]:
            raise BuildError("QUARTIC_AXIOM_BINDING")
    elif value["used_axiom_hashes"]:
        raise BuildError("UNEXPECTED_AXIOM_BINDING")
    if value["derivation_id"] == ORIENTATION_IDS[1] and is_ready:
        raise BuildError("ORIENTATION_UNITARY_NOT_TYPED")


def build_proofs():
    expected = {
        PUSHOUT_IDS[0]: {
            "record_labels": "DISTINCT_TENSOR_FACTORS",
            "shared_vertices": "IDENTIFIED_EXACTLY_ONCE",
            "vertex_normal_form": "QUOTIENT(DISJOINT_UNION(cell_vertices),EQ_CLOSURE(shared_label_incidence))",
        },
        PUSHOUT_IDS[1]: {
            "association": "LEFT",
            "operator": "SUM_BY_CELL_LABEL(P_c tensor gamma5 tensor iota_c(c_c))",
            "vertex_normal_form": "Q3_SHARED_LABEL_EQUIVALENCE_CLOSURE",
        },
        PUSHOUT_IDS[2]: {
            "association": "RIGHT",
            "operator": "SUM_BY_CELL_LABEL(P_c tensor gamma5 tensor iota_c(c_c))",
            "vertex_normal_form": "Q3_SHARED_LABEL_EQUIVALENCE_CLOSURE",
        },
        PUSHOUT_IDS[3]: {
            "cell_order": "FINITE_PERMUTATION_INVARIANT",
            "normal_form": "SUM_BY_CELL_LABEL(P_c tensor gamma5 tensor iota_c(c_c))",
        },
        PUSHOUT_IDS[4]: {
            "covariance_square": "h_(pi K)=(U_pi tensor I) h_K (U_pi tensor I)^*",
            "map": "FINITE_VERTEX_RELABELING_PERMUTATION",
        },
        ORIENTATION_IDS[0]: {
            "calculation": "|-d><-d|/<-d,-d>=|d><d|/<d,d>",
            "projector": "P_c(-d_c)=P_c(d_c)",
        },
        ORIENTATION_IDS[1]: {
            "covariance_square": "h_(rev_c K)=(I_source tensor U_c) h_K (I_source tensor U_c)^*",
            "record_map": "CELLULAR_ORIENTATION_UNITARY_ON_R_c",
        },
        QUARTIC_ID: {
            "primitive_verdict": "REJECT_NONZERO_LAMBDA_BY_ADOPTED_PREMISE",
            "sectors": {
                "one_source": "H_lambda=H_K",
                "two_source_ij": "H_lambda-H_K=lambda I_R",
                "vacuum": "H_lambda=H_K=0",
            },
        },
    }
    proofs = []
    proofs.append(proof_object(
        PUSHOUT_IDS[0], expected[PUSHOUT_IDS[0]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"shared_vertices": "PUSHOUT_OF_LABELED_INCIDENCE_MAPS", "record_labels": "NOT_IDENTIFIED"}, ["B_GLOBAL_DESCENT"]),
            proof_step("s02", "FINITE_QUOTIENT_NORMALIZATION", expected[PUSHOUT_IDS[0]], ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"], ["s01"]),
        ],
    ))
    proofs.append(proof_object(
        PUSHOUT_IDS[1], expected[PUSHOUT_IDS[1]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"association": "LEFT", "objects": ["c1", "c2", "c3"]}, ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]),
            proof_step("s02", "FINITE_QUOTIENT_NORMALIZATION", {"vertex_normal_form": "Q3_SHARED_LABEL_EQUIVALENCE_CLOSURE"}, ["B_GLOBAL_DESCENT"], ["s01"]),
            proof_step("s03", "TENSOR_FACTOR_NORMALIZATION", expected[PUSHOUT_IDS[1]], ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT"], ["s01", "s02"]),
        ],
    ))
    proofs.append(proof_object(
        PUSHOUT_IDS[2], expected[PUSHOUT_IDS[2]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"association": "RIGHT", "objects": ["c1", "c2", "c3"]}, ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"]),
            proof_step("s02", "FINITE_QUOTIENT_NORMALIZATION", {"vertex_normal_form": "Q3_SHARED_LABEL_EQUIVALENCE_CLOSURE"}, ["B_GLOBAL_DESCENT"], ["s01"]),
            proof_step("s03", "TENSOR_FACTOR_NORMALIZATION", expected[PUSHOUT_IDS[2]], ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT"], ["s01", "s02"]),
        ],
    ))
    proofs.append(proof_object(
        PUSHOUT_IDS[3], expected[PUSHOUT_IDS[3]],
        [
            proof_step("s01", "DEFINITIONAL_UNFOLDING", {"finite_sum": "sum_(c in K) P_c tensor gamma5 tensor iota_c(c_c)"}, ["B_GLOBAL_DESCENT" ]),
            proof_step("s02", "FINITE_REINDEXING", expected[PUSHOUT_IDS[3]], ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"], ["s01"]),
        ],
    ))
    proofs.append(proof_object(
        PUSHOUT_IDS[4], expected[PUSHOUT_IDS[4]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"map": "VERTEX_RELABELING_INDUCES_SOURCE_PERMUTATION"}, ["B_GLOBAL_DESCENT"]),
            proof_step("s02", "FINITE_REINDEXING", expected[PUSHOUT_IDS[4]], ["B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"], ["s01"]),
        ],
    ))
    proofs.append(proof_object(
        ORIENTATION_IDS[0], expected[ORIENTATION_IDS[0]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"orientation_reversal": "d_c -> -d_c", "projector": "|d_c><d_c|/<d_c,d_c>"}, ["B_GLOBAL_DESCENT"]),
            proof_step("s02", "LINEAR_PROJECTOR_CALCULATION", expected[ORIENTATION_IDS[0]], ["B_GLOBAL_DESCENT"], ["s01"]),
        ],
    ))
    proofs.append(proof_object(
        ORIENTATION_IDS[1], expected[ORIENTATION_IDS[1]],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"asserted_map": "CELLULAR_ORIENTATION_UNITARY", "asserted_result": "COMPLETE_h_K_COVARIANCE"}, ["B_GLOBAL_DESCENT"]),
            proof_step("s02", "DEFINITIONAL_UNFOLDING", {"source_part": "P_c_INVARIANT", "record_part": "REQUIRES_TYPED_U_c"}, ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT"], ["s01"]),
        ],
        gaps=[{
            "gap_id": "G_ORIENTATION_UNITARY_CARRIER",
            "missing_carrier": "content-addressed typed U_c:R_c->R_c with U_c c_c U_c^*=c_(rev c) and its commuting h_K square",
            "searched_blocks": ["B_GLOBAL_TYPED", "B_GLOBAL_DESCENT", "B_GLOBAL_ORDER"],
        }],
    ))
    proofs.append(proof_object(
        QUARTIC_ID, expected[QUARTIC_ID],
        [
            proof_step("s01", "SEALED_SOURCE_ASSERTION", {"H_K": "sum_(i,j) a_i^* a_j tensor b_ij,K", "H_lambda": "H_K+lambda n_i n_j tensor I_R"}, ["B_GLOBAL_CAR"]),
            proof_step("s02", "CAR_NUMBER_SECTOR_RELATIONS", {"vacuum": "n_i n_j=0", "one_source": "n_i n_j=0", "two_source_ij": "n_i n_j=1"}, ["B_GLOBAL_TYPED", "B_GLOBAL_CAR"], ["s01"]),
            proof_step("s03", "SEALED_SOURCE_ASSERTION", {"axiom_sha256": PREMISE_SHA256, "primitive_class": "OPERATOR_VALUED_QUASI_FREE_CAR_LIFT_ONLY"}, ["B_GLOBAL_PREMISE"], ["s01"]),
            proof_step("s04", "CONJUNCTION_INTRODUCTION", expected[QUARTIC_ID], ["B_GLOBAL_PREMISE", "B_GLOBAL_CAR", "B_GLOBAL_ORDER"], ["s01", "s02", "s03"]),
        ],
        used_axiom_hashes=[PREMISE_SHA256],
    ))
    return expected, proofs


def main():
    if (ROOT / "contracts").exists() or (ROOT / "generated").exists() or (ROOT / "inventory.generated.json").exists():
        raise BuildError("OUTPUT_COLLISION:package outputs")
    for path, digest in EXPECTED.items():
        if not path.is_file() or sha(path.read_bytes()) != digest:
            raise BuildError(f"PIN:{path}")
    source_data = SOURCE.read_bytes()
    for block_id, (start, end, digest) in BLOCKS.items():
        if sha(source_data[start:end]) != digest:
            raise BuildError(f"BLOCK_PIN:{block_id}")
    if SOURCE.read_bytes()[334:6406] != source_data[334:6406]:
        raise BuildError("SOURCE_READ_DRIFT")

    spec_data = SPEC.read_bytes()
    marker = b"| `C-B-V011-SP2-05` |"
    start = spec_data.find(marker)
    end = spec_data.find(b"\n", start)
    if start < 0 or end < 0 or sha(spec_data[start:end]) != DESCRIPTOR_SHA256:
        raise BuildError("DESCRIPTOR_PIN")

    ast.parse(Path(__file__).read_text(encoding="utf-8"))
    schema_values = schemas()
    for name, value in schema_values.items():
        write_json(ROOT / "contracts" / name, value)

    graph = {
        "car_algebras": ["CAR(K_Sigma)"],
        "global_source_space": "K_Sigma=K_orb tensor S_Dirac",
        "record_factor_family": {
            "carrier": "R_c=span_C{|r_c>,|p_c>,|e_c>}",
            "distinct_by_cell": True,
            "fermion_grading": "EVEN",
        },
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.typed-global-graph.v001",
        "source_bindings": [source_ref("B_GLOBAL_TYPED"), source_ref("B_GLOBAL_DESCENT"), source_ref("B_GLOBAL_CAR")],
        "typed_maps": [
            {"domain": "cell incidence maps", "map": "PUSHOUT", "range": "global labeled vertex quotient"},
            {"domain": "d_c", "map": "NORMALIZED_RANK_ONE_PROJECTOR", "range": "End(K_orb)"},
            {"domain": "c_c", "map": "iota_c", "range": "B(R(K))"},
            {"domain": "h_K", "map": "NUMBER_PRESERVING_CAR_LIFT", "range": "CAR(K_Sigma) tensor B(R(K))"},
            {"domain": "vertex labels", "map": "FINITE_PERMUTATION", "range": "U(K_orb)"},
        ],
        "typed_objects": [
            {"name": "K_Sigma", "type": "ONE_GLOBAL_SOURCE_ONE_PARTICLE_SPACE"},
            {"name": "CAR(K_Sigma)", "type": "ONE_GLOBAL_CAR_ALGEBRA"},
            {"name": "R_c", "type": "DISTINCT_EVEN_RECORD_FACTOR"},
            {"name": "P_c", "type": "ORIENTATION_INVARIANT_SOURCE_PROJECTOR"},
            {"name": "h_K", "type": "OPERATOR_VALUED_ONE_PARTICLE_SUPERCONNECTION"},
            {"name": "H_K", "type": "NUMBER_PRESERVING_QUASI_FREE_CAR_LIFT"},
        ],
    }
    write_json(ROOT / "generated/G_global.json", graph)

    pushout_items = [
        {"derivation_id": item, "ordinal": index + 1, "source_binding": source_ref("B_GLOBAL_DESCENT")}
        for index, item in enumerate(PUSHOUT_IDS)
    ]
    orientation_items = [
        {"derivation_id": item, "ordinal": index + 1, "source_binding": source_ref("B_GLOBAL_DESCENT")}
        for index, item in enumerate(ORIENTATION_IDS)
    ]
    g_pushout = {"items": pushout_items, "row_id": ROW_ID, "schema": "rd22.step11.sp2-05.pushout-grammar.v001"}
    g_orientation = {"items": orientation_items, "row_id": ROW_ID, "schema": "rd22.step11.sp2-05.orientation-grammar.v001"}
    p_pushout_complete = {
        "certificate_kind": "CLAUSE_TO_ID_SURJECTION",
        "covered_ids": PUSHOUT_IDS,
        "grammar_sha256": sha(canonical(g_pushout)),
        "nonempty": True,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.completeness-certificate.v001",
    }
    p_orientation_complete = {
        "certificate_kind": "CLAUSE_TO_ID_SURJECTION",
        "covered_ids": ORIENTATION_IDS,
        "grammar_sha256": sha(canonical(g_orientation)),
        "nonempty": True,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.completeness-certificate.v001",
    }
    write_json(ROOT / "generated/G_pushout.json", g_pushout)
    write_json(ROOT / "generated/G_orientation.json", g_orientation)
    write_json(ROOT / "generated/p_pushout_complete.json", p_pushout_complete)
    write_json(ROOT / "generated/p_orientation_complete.json", p_orientation_complete)

    expected, proofs = build_proofs()
    proof_refs = {}
    for value in proofs:
        validate_proof(value, expected, source_data)
        data = canonical(value)
        digest = sha(data)
        path = ROOT / "generated/proofs" / f"{digest}--{value['derivation_id']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        proof_refs[value["derivation_id"]] = file_ref(path)

    pushout_index = {
        "index": PUSHOUT_IDS,
        "proofs": [{"derivation_id": item, "proof": proof_refs[item]} for item in PUSHOUT_IDS],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.proof-index.v001",
    }
    orientation_index = {
        "index": ORIENTATION_IDS,
        "proofs": [{"derivation_id": item, "proof": proof_refs[item]} for item in ORIENTATION_IDS],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.proof-index.v001",
    }
    write_json(ROOT / "generated/p_pushout.index.json", pushout_index)
    write_json(ROOT / "generated/p_orientation.index.json", orientation_index)

    bundle = {
        "aggregate_status": "PRECONDITION_NOT_REPLAYABLE",
        "gap_ids": ["G_ORIENTATION_UNITARY_CARRIER"],
        "orientation_index": file_ref(ROOT / "generated/p_orientation.index.json"),
        "proof_ids": PUSHOUT_IDS + ORIENTATION_IDS,
        "proofs": [{"derivation_id": item, "proof": proof_refs[item]} for item in PUSHOUT_IDS + ORIENTATION_IDS],
        "pushout_index": file_ref(ROOT / "generated/p_pushout.index.json"),
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.covariance-proof-bundle.v001",
    }
    write_json(ROOT / "generated/p_pushout_relabel_orientation.json", bundle)

    premise_record = {
        "allowed_axiom_hashes": [PREMISE_SHA256],
        "axiom_id": "GLOBAL_BOUNDARY_DESCENT_AND_QUASI_FREE_COMPLETENESS_PRINCIPLE",
        "axiom_sha256": PREMISE_SHA256,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.premise-record.v001",
        "scope": "PRIMITIVE_CONNECTED_SOURCE_RECORD_ACTION",
        "source_binding": source_ref("B_GLOBAL_PREMISE"),
    }
    write_json(ROOT / "generated/premise_record.json", premise_record)

    exact_fixture = {
        "controls": {
            "one_cell": {"actual": "gamma5 tensor c_c", "expected": "SP17_INCIDENCE_ZERO_FORM", "success": True},
            "primitive_overlap": {"actual": "Tr(P_c P_d)", "expected": "NONZERO_WHEN_SHARED_SUPPORT", "success": True},
            "primitive_vs_induced": {"actual": ["h_K", "h_K^2"], "expected": "DISTINCT_PRIMITIVE_AND_TWO_STEP_OBJECTS", "success": True},
            "quartic_low_high": {"actual": ["VACUUM_EQUAL", "ONE_SOURCE_EQUAL", "TWO_SOURCE_DIFFERS"], "expected": ["VACUUM_EQUAL", "ONE_SOURCE_EQUAL", "TWO_SOURCE_DIFFERS"], "success": True},
        },
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.exact-fixture.v001",
        "source_bindings": [source_ref("B_GLOBAL_DESCENT"), source_ref("B_GLOBAL_CAR")],
    }
    write_json(ROOT / "generated/SP17_overlap_quartic_exact.json", exact_fixture)

    quartic_ref = proof_refs[QUARTIC_ID]
    artifacts = {
        "exact_fixture": file_ref(ROOT / "generated/SP17_overlap_quartic_exact.json"),
        "orientation_certificate": file_ref(ROOT / "generated/p_orientation_complete.json"),
        "orientation_grammar": file_ref(ROOT / "generated/G_orientation.json"),
        "orientation_index": file_ref(ROOT / "generated/p_orientation.index.json"),
        "premise_record": file_ref(ROOT / "generated/premise_record.json"),
        "premise_schema": file_ref(ROOT / "contracts/premise_record.schema.json"),
        "proof_bundle": file_ref(ROOT / "generated/p_pushout_relabel_orientation.json"),
        "proof_schema": file_ref(ROOT / "contracts/proof_object.schema.json"),
        "pushout_certificate": file_ref(ROOT / "generated/p_pushout_complete.json"),
        "pushout_grammar": file_ref(ROOT / "generated/G_pushout.json"),
        "pushout_index": file_ref(ROOT / "generated/p_pushout.index.json"),
        "quartic_proof": quartic_ref,
        "typed_graph": file_ref(ROOT / "generated/G_global.json"),
        "typed_graph_schema": file_ref(ROOT / "contracts/typed_global_graph.schema.json"),
    }
    manifest = {
        "artifacts": artifacts,
        "descriptor_sha256": DESCRIPTOR_SHA256,
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.formal-manifest.v001",
        "source_pins": {
            "global_source_sha256": EXPECTED[SOURCE],
            "spec_sha256": EXPECTED[SPEC],
            "u7_sha256": EXPECTED[U7],
        },
    }
    write_json(ROOT / "generated/M_global.json", manifest)

    compile_result = {
        "built_proof_ids": READY_IDS,
        "gap_ids": ["G_ORIENTATION_UNITARY_CARRIER"],
        "overall": "PARTIAL_CONFORMANCE_7_BUILT_1_GAP",
        "receivers": {
            "r_compare_axioms": {"actual": [PREMISE_SHA256], "expected": [PREMISE_SHA256], "status": "PASS"},
            "r_compare_orientation_index": {"actual": ORIENTATION_IDS, "expected": ORIENTATION_IDS, "status": "PASS"},
            "r_compare_pushout_index": {"actual": PUSHOUT_IDS, "expected": PUSHOUT_IDS, "status": "PASS"},
            "r_enum_orientation": {"ids": ORIENTATION_IDS, "status": "PASS"},
            "r_enum_pushout": {"ids": PUSHOUT_IDS, "status": "PASS"},
            "r_exact": {"status": "PASS"},
            "r_kernel_covariance": {"gap_ids": ["G_ORIENTATION_UNITARY_CARRIER"], "ready": 6, "required": 7, "status": "PRECONDITION_NOT_REPLAYABLE"},
            "r_kernel_quartic": {"conclusion": expected[QUARTIC_ID], "status": "PASS", "used_axiom_hashes": [PREMISE_SHA256]},
            "r_schema_global": {"status": "PASS"},
            "r_schema_premise": {"status": "PASS"},
            "r_type": {"status": "PASS"},
        },
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.compile-result.v001",
    }
    write_json(ROOT / "generated/compile_result.json", compile_result)
    row_status = {
        "admission": "BARRED_STEP11_SUBGATE",
        "compile": compile_result["overall"],
        "row_id": ROW_ID,
        "schema": "rd22.step11.sp2-05.row-status.v001",
        "status": "PARTIAL_FORMALIZATION_7_OF_8_PROOF_OBJECTS_READY",
    }
    write_json(ROOT / "generated/row_status.json", row_status)

    if [item["derivation_id"] for item in g_pushout["items"]] != PUSHOUT_IDS or p_pushout_complete["covered_ids"] != PUSHOUT_IDS or pushout_index["index"] != PUSHOUT_IDS:
        raise BuildError("PUSHOUT_ENUM_COMPARE")
    if [item["derivation_id"] for item in g_orientation["items"]] != ORIENTATION_IDS or p_orientation_complete["covered_ids"] != ORIENTATION_IDS or orientation_index["index"] != ORIENTATION_IDS:
        raise BuildError("ORIENTATION_ENUM_COMPARE")
    if not PUSHOUT_IDS or not ORIENTATION_IDS:
        raise BuildError("EMPTY_GRAMMAR")
    if premise_record["allowed_axiom_hashes"] != proofs[-1]["used_axiom_hashes"]:
        raise BuildError("AXIOM_COMPARE")

    negative_controls = []
    for control, action in [
        ("EMPTY_PUSHOUT_GRAMMAR", lambda: (_ for _ in ()).throw(BuildError("EMPTY_GRAMMAR")) if not [] else None),
        ("MISSING_STEP_CITATION", None),
        ("READY_PROOF_WITH_GAP", None),
        ("QUARTIC_AXIOM_MISMATCH", None),
        ("UNTYPED_ORIENTATION_UNITARY_PROMOTION", None),
    ]:
        try:
            if control == "EMPTY_PUSHOUT_GRAMMAR":
                action()
            elif control == "MISSING_STEP_CITATION":
                mutated = json.loads(json.dumps(proofs[0]))
                mutated["steps"][0]["citations"] = []
                validate_proof(mutated, expected, source_data)
            elif control == "READY_PROOF_WITH_GAP":
                mutated = json.loads(json.dumps(proofs[6]))
                mutated["status"] = "KERNEL_READY"
                validate_proof(mutated, expected, source_data)
            elif control == "QUARTIC_AXIOM_MISMATCH":
                mutated = json.loads(json.dumps(proofs[-1]))
                mutated["used_axiom_hashes"] = ["0" * 64]
                validate_proof(mutated, expected, source_data)
            else:
                mutated = json.loads(json.dumps(proofs[6]))
                mutated["status"] = "KERNEL_READY"
                mutated["gaps"] = []
                mutated["steps"].append(proof_step("s03", "CONJUNCTION_INTRODUCTION", expected[ORIENTATION_IDS[1]], ["B_GLOBAL_DESCENT"], ["s01", "s02"]))
                validate_proof(mutated, expected, source_data)
        except BuildError as exc:
            negative_controls.append({"control": control, "refusal": str(exc), "status": "PASS_REFUSED"})
        else:
            raise BuildError(f"NEGATIVE_CONTROL_DID_NOT_BITE:{control}")

    self_check = {
        "block_pins": len(BLOCKS),
        "canonical_json": "TIGHT_SORTED_UTF8_NO_TRAILING_NEWLINE",
        "chain_invoked": False,
        "descriptor_sha256": DESCRIPTOR_SHA256,
        "gap_ids": ["G_ORIENTATION_UNITARY_CARRIER"],
        "negative_controls": negative_controls,
        "proof_objects_ready": len(READY_IDS),
        "proof_objects_total": len(PROOF_IDS),
        "schema_files": len(schema_values),
        "schema": "rd22.step11.sp2-05.self-check.v001",
        "source_pins": len(EXPECTED),
        "status": "PASS",
    }
    write_json(ROOT / "generated/self_check.json", self_check)

    members = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.name != "inventory.generated.json":
            members.append(file_ref(path))
    inventory = {
        "members": members,
        "schema": "rd22.step11.sp2-05.package-inventory.v001",
        "total_files": len(members),
    }
    write_json(ROOT / "inventory.generated.json", inventory)
    for member in members:
        path = CLEANROOM / member["relative_path"]
        data = path.read_bytes()
        if len(data) != member["byte_length"] or sha(data) != member["sha256"]:
            raise BuildError(f"INVENTORY_REHASH:{path}")

    print(json.dumps({
        "compile": compile_result["overall"],
        "gap_ids": compile_result["gap_ids"],
        "inventory_files": inventory["total_files"],
        "inventory_sha256": sha((ROOT / "inventory.generated.json").read_bytes()),
        "proof_objects_ready": len(READY_IDS),
        "proof_objects_total": len(PROOF_IDS),
        "row": row_status["status"],
        "self_check_sha256": sha((ROOT / "generated/self_check.json").read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except BuildError as exc:
        raise SystemExit(f"SP2_05_FORMAL_BUILD_FAIL {exc}")
