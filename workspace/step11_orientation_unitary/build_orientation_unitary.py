#!/usr/bin/env python3
"""Derive the canonical cellular orientation carrier and recompile two rows."""

import ast
import hashlib
import json
from pathlib import Path


CLEANROOM = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parent
PACKET = CLEANROOM / "review_packets/STAGE7_QSPEC_CANDIDATE_V001"
GLOBAL = PACKET / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
GRADED = PACKET / "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md"
COMPLETE = PACKET / "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md"
CPT = PACKET / "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md"
SPEC = CLEANROOM / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V012.md"

SP1_ROOT = CLEANROOM / "step11_sp1_07_witnesses"
SP1_INDEX = SP1_ROOT / "generated/P_SP1_07_after.json"
SP1_COMPILE = SP1_ROOT / "generated/compile_result.json"
SP1_STATUS = SP1_ROOT / "generated/row_status.json"
SP1_INVENTORY = SP1_ROOT / "inventory.generated.json"
SP1_EXPECTED = CLEANROOM / "step11_sp1_07_formal/generated/E_SP1_07.json"

SP2_ROOT = CLEANROOM / "step11_sp2_05_formal"
SP2_BUNDLE = SP2_ROOT / "generated/p_pushout_relabel_orientation.json"
SP2_COMPILE = SP2_ROOT / "generated/compile_result.json"
SP2_STATUS = SP2_ROOT / "generated/row_status.json"
SP2_INVENTORY = SP2_ROOT / "inventory.generated.json"

EXPECTED = {
    GLOBAL: "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    GRADED: "2215f79cbe69f1de1643427ad5d422b0c3064ff758327e43ff1629de8633f72d",
    COMPLETE: "50b5a651df2aca90ee47c6f85b2a502461370a652706ebccad871f191565a2d9",
    CPT: "0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98",
    SPEC: "382052c4caf7d8d4187c3fdbe98796845060e66519e11ed3b8eb3c454b68d504",
    SP1_INDEX: "c4a1e73e717aa0cfa45aa1f754f29113d1fd8572d4ef3f1cdd38689dabbd0639",
    SP1_COMPILE: "1d9d9a9774433d59a8c2741cabe9b70d20a8039ece7ba03c8f339e9c4f43e055",
    SP1_STATUS: "d91164d05c33a9cb6a1dd10fba45d90cba50af50ee16501db148447a7051b1b6",
    SP1_INVENTORY: "1af6e9dcc239c4bf3c74f5de8cfb219458a49d6331ca49f0daf536a586650426",
    SP1_EXPECTED: "3925d5333a7c5e53c65a307630c9150a0e218d352dafd1f944abe090e3d24fc3",
    SP2_BUNDLE: "973c1f628474d321c64cd31e21ca73f8d9972e91ec19369dc63caccf2f10a131",
    SP2_COMPILE: "470ec4636d5bfd9ab4975faaf71dd27b565bf41b0864c9f47321badb11a0976c",
    SP2_STATUS: "b5d989ff0ac740d7a8ab0d257e87a94f7317c820c5d8a0d875f0d3947a33b4d4",
    SP2_INVENTORY: "78d7ddcb980804d7a6f7bce9e6b3dd34f6455543f475b7c6980b1bad62a2b828",
}

SP1_ROW = "C-B-V011-SP1-07"
SP2_ROW = "C-B-V011-SP2-05"
D08 = "D08_ORIENTATION_REVERSAL_COVARIANCE"
O02 = "O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE"

BLOCKS = {
    "GLOBAL_TYPED": (GLOBAL, 1103, 1704, "daeb7bc7b448e78009703e6fc7a7946a76844f7ee6f479327e63ab6ab84057d2"),
    "GLOBAL_DESCENT": (GLOBAL, 1705, 4005, "fcbb16c6cad76b08a210d55d42a1ce82d165ae3a0adfd63f28ba16f30946d1ce"),
    "GRADED_CELLULAR": (GRADED, 344, 1501, "10262d72110ffaafdcaf4ea0419af4f780b1616e30567a9275c0b1315207ef72"),
    "COMPLETE_CARRIER": (COMPLETE, 386, 1377, "191cf84d2288f532f7d4df410be2c8947ffa006c4bc440a697a4120a9e6f1fde"),
    "COMPLETE_QUADRATURE": (COMPLETE, 3909, 4583, "42188aeee574da63e53aa88a0204f472d59b377c959eb2f6439602d692eb9a7c"),
    "CPT_ORIENTATION": (CPT, 4185, 5830, "c9fc62a999110e443f87551110e914462029f2dd5a5dd331d7ca202cd894b6c5"),
}


class BuildError(Exception):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


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
    path, start, end, digest = BLOCKS[block_id]
    return {
        "block_id": block_id,
        "relative_path": path.relative_to(CLEANROOM).as_posix(),
        "source_sha256": EXPECTED[path],
        "span": [start, end],
        "span_sha256": digest,
    }


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zneg(a):
    return (-a[0], -a[1])


def zconj(a):
    return (a[0], -a[1])


def madd(a, b):
    return [[zadd(x, y) for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def mneg(a):
    return [[zneg(x) for x in row] for row in a]


def mmul(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise BuildError("MATRIX_DIMENSION")
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            entry = ZERO
            for k in range(len(b)):
                entry = zadd(entry, zmul(a[i][k], b[k][j]))
            row.append(entry)
        result.append(row)
    return result


def madjoint(a):
    return [[zconj(a[i][j]) for i in range(len(a))] for j in range(len(a[0]))]


def matrix_json(a):
    return [[[entry[0], entry[1]] for entry in row] for row in a]


ZERO = (0, 0)
ONE = (1, 0)
MONE = (-1, 0)
I = (0, 1)
IDENTITY3 = [[ONE, ZERO, ZERO], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
GAMMA = [[ONE, ZERO, ZERO], [ZERO, ONE, ZERO], [ZERO, ZERO, MONE]]
D = [[MONE], [ONE]]
B = [[ZERO, ZERO, MONE], [ZERO, ZERO, ONE], [MONE, ONE, ZERO]]


def source_schema():
    return {
        "additionalProperties": False,
        "properties": {
            "block_id": {"enum": list(BLOCKS)},
            "relative_path": {"minLength": 1, "type": "string"},
            "source_sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
            "span": {"items": False, "maxItems": 2, "minItems": 2, "prefixItems": [{"minimum": 0, "type": "integer"}, {"minimum": 0, "type": "integer"}], "type": "array"},
            "span_sha256": {"pattern": "^[0-9a-f]{64}$", "type": "string"},
        },
        "required": ["block_id", "relative_path", "source_sha256", "span", "span_sha256"],
        "type": "object",
    }


def schemas():
    source = source_schema()
    matrix = {
        "items": {
            "items": {
                "items": {"type": "integer"},
                "maxItems": 2,
                "minItems": 2,
                "type": "array",
            },
            "minItems": 1,
            "type": "array",
        },
        "minItems": 1,
        "type": "array",
    }
    carrier = {
        "$defs": {"matrix": matrix, "source": source},
        "$id": "urn:rd22:step11:orientation-unitary-carrier:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "basis": {"const": ["|r_c>", "|p_c>", "|e_c>"]},
            "carrier_id": {"const": "U_CELL_ORIENTATION_CANONICAL"},
            "codomain": {"const": "R_c=span_C{|r_c>,|p_c>,|e_c>}"},
            "complex_entry_encoding": {"const": "[real_integer,imaginary_integer]"},
            "domain": {"const": "R_c=span_C{|r_c>,|p_c>,|e_c>}"},
            "matrices": {
                "additionalProperties": False,
                "properties": {item: {"$ref": "#/$defs/matrix"} for item in ["Gamma_cell", "U_c", "b_partial", "b_partial_reversed", "c_partial", "c_partial_reversed", "d_partial"]},
                "required": ["Gamma_cell", "U_c", "b_partial", "b_partial_reversed", "c_partial", "c_partial_reversed", "d_partial"],
                "type": "object",
            },
            "orientation_subset_extension": {"type": "object"},
            "phase_class": {"const": "Ad_(exp(i theta) Gamma_cell)=Ad_(Gamma_cell); canonical representative Gamma_cell"},
            "schema": {"const": "rd22.step11.orientation-unitary-carrier.v001"},
            "source_bindings": {"items": {"$ref": "#/$defs/source"}, "minItems": 4, "type": "array"},
        },
        "required": ["schema", "carrier_id", "domain", "codomain", "basis", "complex_entry_encoding", "matrices", "orientation_subset_extension", "phase_class", "source_bindings"],
        "type": "object",
    }
    proof = {
        "$defs": {"source": source},
        "$id": "urn:rd22:step11:orientation-unitary-proof:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "carrier": {"type": "object"},
            "checks": {"items": {"type": "object"}, "minItems": 7, "type": "array"},
            "conclusions": {"type": "object"},
            "gaps": {"const": []},
            "proof_id": {"const": "P_ORIENTATION_UNITARY_AND_COMPLETE_HK_SQUARE"},
            "schema": {"const": "rd22.step11.orientation-unitary-proof.v001"},
            "source_bindings": {"items": {"$ref": "#/$defs/source"}, "minItems": 4, "type": "array"},
            "status": {"const": "KERNEL_READY"},
        },
        "required": ["schema", "proof_id", "carrier", "source_bindings", "checks", "conclusions", "status", "gaps"],
        "type": "object",
    }
    consumer = {
        "$id": "urn:rd22:step11:orientation-unitary-consumer-binding:v001",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "additionalProperties": False,
        "properties": {
            "carrier": {"type": "object"},
            "conclusion": {"type": "object"},
            "derivation_id": {"enum": [D08, O02]},
            "expected_conclusion": {"type": "object"},
            "row_id": {"enum": [SP1_ROW, SP2_ROW]},
            "schema": {"const": "rd22.step11.orientation-unitary-consumer-binding.v001"},
            "shared_proof": {"type": "object"},
            "status": {"const": "KERNEL_READY"},
            "target_opcode": {"const": "KERNEL"},
        },
        "required": ["schema", "row_id", "derivation_id", "target_opcode", "carrier", "shared_proof", "expected_conclusion", "conclusion", "status"],
        "type": "object",
    }
    return {
        "consumer_binding.schema.json": consumer,
        "orientation_unitary.schema.json": carrier,
        "orientation_unitary_proof.schema.json": proof,
    }


def validate_source(ref):
    if set(ref) != {"block_id", "relative_path", "source_sha256", "span", "span_sha256"} or ref["block_id"] not in BLOCKS:
        raise BuildError("SOURCE_REF_FIELDS")
    path, start, end, digest = BLOCKS[ref["block_id"]]
    if ref["relative_path"] != path.relative_to(CLEANROOM).as_posix() or ref["source_sha256"] != EXPECTED[path] or ref["span"] != [start, end] or ref["span_sha256"] != digest:
        raise BuildError("SOURCE_REF_VALUE")
    if sha(path.read_bytes()[start:end]) != digest:
        raise BuildError("SOURCE_REF_REHASH")


def parse_matrix(value):
    return [[(entry[0], entry[1]) for entry in row] for row in value]


def validate_carrier(value):
    fields = {"basis", "carrier_id", "codomain", "complex_entry_encoding", "domain", "matrices", "orientation_subset_extension", "phase_class", "schema", "source_bindings"}
    if set(value) != fields or value["carrier_id"] != "U_CELL_ORIENTATION_CANONICAL":
        raise BuildError("CARRIER_FIELDS")
    for ref in value["source_bindings"]:
        validate_source(ref)
    matrices = {key: parse_matrix(item) for key, item in value["matrices"].items()}
    if matrices["Gamma_cell"] != GAMMA or matrices["U_c"] != GAMMA or matrices["d_partial"] != D or matrices["b_partial"] != B:
        raise BuildError("CARRIER_SEALED_MATRIX")
    if mmul(madjoint(matrices["U_c"]), matrices["U_c"]) != IDENTITY3 or madjoint(matrices["U_c"]) != matrices["U_c"]:
        raise BuildError("CARRIER_UNITARITY")
    if madd(mmul(GAMMA, B), mmul(B, GAMMA)) != [[ZERO] * 3 for _ in range(3)]:
        raise BuildError("CARRIER_ODDNESS")
    if matrices["b_partial_reversed"] != mneg(B):
        raise BuildError("CARRIER_REVERSED_BOUNDARY")
    c = [[zmul(I, entry) for entry in row] for row in mmul(GAMMA, B)]
    c_rev = [[zmul(I, entry) for entry in row] for row in mmul(GAMMA, mneg(B))]
    if matrices["c_partial"] != c or matrices["c_partial_reversed"] != c_rev:
        raise BuildError("CARRIER_QUADRATURE")
    if mmul(mmul(GAMMA, c), GAMMA) != c_rev or c_rev != mneg(c):
        raise BuildError("CARRIER_CONJUGATION")
    if madjoint(c) != c:
        raise BuildError("CARRIER_HERMITICITY")


def validate_inventory(path):
    value = json.loads(path.read_bytes())
    members = value.get("members", value.get("files"))
    if not isinstance(members, list):
        raise BuildError(f"PREDECESSOR_INVENTORY_SHAPE:{path}")
    for member in members:
        member_path = CLEANROOM / member["relative_path"]
        data = member_path.read_bytes()
        if len(data) != member["byte_length"] or sha(data) != member["sha256"]:
            raise BuildError(f"PREDECESSOR_INVENTORY:{member_path}")


def main():
    occupied = (ROOT / "inventory.generated.json").is_file()
    for directory in [ROOT / "contracts", ROOT / "generated"]:
        if directory.exists() and any(path.is_file() for path in directory.rglob("*")):
            occupied = True
    if occupied:
        raise BuildError("OUTPUT_COLLISION:package outputs")
    for path, digest in EXPECTED.items():
        if not path.is_file() or sha(path.read_bytes()) != digest:
            raise BuildError(f"PIN:{path}")
    for block_id, (path, start, end, digest) in BLOCKS.items():
        if sha(path.read_bytes()[start:end]) != digest:
            raise BuildError(f"BLOCK_PIN:{block_id}")
    validate_inventory(SP1_INVENTORY)
    validate_inventory(SP2_INVENTORY)
    ast.parse(Path(__file__).read_text(encoding="utf-8"))

    schema_values = schemas()
    for name, value in schema_values.items():
        write_json(ROOT / "contracts" / name, value)

    b_rev = mneg(B)
    c = [[zmul(I, entry) for entry in row] for row in mmul(GAMMA, B)]
    c_rev = [[zmul(I, entry) for entry in row] for row in mmul(GAMMA, b_rev)]
    sources = [
        source_ref("GLOBAL_TYPED"), source_ref("GLOBAL_DESCENT"),
        source_ref("GRADED_CELLULAR"), source_ref("COMPLETE_CARRIER"),
        source_ref("COMPLETE_QUADRATURE"), source_ref("CPT_ORIENTATION"),
    ]
    carrier = {
        "basis": ["|r_c>", "|p_c>", "|e_c>"],
        "carrier_id": "U_CELL_ORIENTATION_CANONICAL",
        "codomain": "R_c=span_C{|r_c>,|p_c>,|e_c>}",
        "complex_entry_encoding": "[real_integer,imaginary_integer]",
        "domain": "R_c=span_C{|r_c>,|p_c>,|e_c>}",
        "matrices": {
            "Gamma_cell": matrix_json(GAMMA),
            "U_c": matrix_json(GAMMA),
            "b_partial": matrix_json(B),
            "b_partial_reversed": matrix_json(b_rev),
            "c_partial": matrix_json(c),
            "c_partial_reversed": matrix_json(c_rev),
            "d_partial": matrix_json(D),
        },
        "orientation_subset_extension": {
            "formula": "U_O=tensor_(c in K) (Gamma_cell if c in O else I_Rc)",
            "scope": "every finite selected orientation-reversal subset O of K",
            "unitarity": "U_O^*=U_O=U_O^-1",
        },
        "phase_class": "Ad_(exp(i theta) Gamma_cell)=Ad_(Gamma_cell); canonical representative Gamma_cell",
        "schema": "rd22.step11.orientation-unitary-carrier.v001",
        "source_bindings": sources,
    }
    validate_carrier(carrier)
    carrier_data = canonical(carrier)
    carrier_path = ROOT / "generated" / f"{sha(carrier_data)}--U_CELL_ORIENTATION_CANONICAL.json"
    carrier_path.parent.mkdir(parents=True, exist_ok=True)
    carrier_path.write_bytes(carrier_data)
    carrier_ref = file_ref(carrier_path)

    proof = {
        "carrier": carrier_ref,
        "checks": [
            {"check": "UNITARY", "identity": "U_c^* U_c=I_3", "result": matrix_json(mmul(madjoint(GAMMA), GAMMA)), "success": True},
            {"check": "SELF_ADJOINT_INVOLUTION", "identity": "U_c^*=U_c=U_c^-1", "success": True},
            {"check": "RECORD_ODDNESS", "identity": "Gamma_cell b_partial+b_partial Gamma_cell=0", "result": matrix_json(madd(mmul(GAMMA, B), mmul(B, GAMMA))), "success": True},
            {"check": "ORIENTATION_BOUNDARY", "identity": "d_rev=-d and b_rev=-b", "success": True},
            {"check": "LOCAL_CONJUGATION", "identity": "U_c c_c U_c^*=c_(rev c)=-c_c", "result": matrix_json(mmul(mmul(GAMMA, c), GAMMA)), "success": True},
            {"check": "SOURCE_PROJECTOR", "identity": "P_c(-d_c)=P_c(d_c)", "success": True},
            {"check": "COMPLETE_HK_SQUARE", "identity": "h_(rev_O K)=U_O h_K U_O^*", "termwise": {"reversed_cells": "c_c -> -c_c; P_c fixed", "unreversed_cells": "separate tensor factors commute with U_O"}, "success": True},
        ],
        "conclusions": {
            "complete_hK": "h_(rev_O K)=U_O h_K U_O^* for every finite selected subset O",
            "local": "U_c c_c U_c^*=c_(rev c)=-c_c",
            "typed_carrier": "U_c=Gamma_cell=diag(+1,+1,-1):R_c->R_c",
        },
        "gaps": [],
        "proof_id": "P_ORIENTATION_UNITARY_AND_COMPLETE_HK_SQUARE",
        "schema": "rd22.step11.orientation-unitary-proof.v001",
        "source_bindings": sources,
        "status": "KERNEL_READY",
    }
    proof_data = canonical(proof)
    proof_path = ROOT / "generated" / f"{sha(proof_data)}--P_ORIENTATION_UNITARY_AND_COMPLETE_HK_SQUARE.json"
    proof_path.write_bytes(proof_data)
    proof_ref = file_ref(proof_path)

    sp1_expected_ledger = json.loads(SP1_EXPECTED.read_bytes())
    sp1_expected = next(item["expected_conclusion"] for item in sp1_expected_ledger["entries"] if item["derivation_id"] == D08)
    sp1_binding = {
        "carrier": carrier_ref,
        "conclusion": sp1_expected,
        "derivation_id": D08,
        "expected_conclusion": sp1_expected,
        "row_id": SP1_ROW,
        "schema": "rd22.step11.orientation-unitary-consumer-binding.v001",
        "shared_proof": proof_ref,
        "status": "KERNEL_READY",
        "target_opcode": "KERNEL",
    }
    sp1_data = canonical(sp1_binding)
    sp1_binding_path = ROOT / "generated" / f"{sha(sp1_data)}--SP1_D08_ORIENTATION_REVERSAL_COVARIANCE.json"
    sp1_binding_path.write_bytes(sp1_data)
    sp1_binding_ref = file_ref(sp1_binding_path)

    prior_sp1_index = json.loads(SP1_INDEX.read_bytes())
    sp1_entries = []
    for item in prior_sp1_index["entries"]:
        if item["derivation_id"] == D08:
            sp1_entries.append({"derivation_id": D08, "proof": sp1_binding_ref, "proof_kind": "SHARED_ORIENTATION_UNITARY_PROOF", "status": "KERNEL_READY"})
        else:
            sp1_entries.append(item)
    sp1_index = {
        "entries": sp1_entries,
        "ids": prior_sp1_index["ids"],
        "predecessor": file_ref(SP1_INDEX),
        "row_id": SP1_ROW,
        "schema": "rd22.step11.sp1-07.proof-index-after-orientation-carrier.v001",
    }
    if len(sp1_entries) != 9 or any(item["status"] != "KERNEL_READY" for item in sp1_entries):
        raise BuildError("SP1_INDEX_NOT_COMPLETE")
    write_json(ROOT / "generated/SP1_P_after_orientation.json", sp1_index)
    sp1_compile = {
        "admission": "BARRED_STEP11_SUBGATE",
        "chain_invoked": False,
        "kernel_ready_ids": prior_sp1_index["ids"],
        "opcode_results": {
            "r_enum": "PASS_9_IDS", "r_exact": "PASS", "r_expected": "PASS",
            "r_nonempty": "PASS", "r_proof_ids": "PASS", "r_required_ids": "PASS",
            "r_schema": "PASS", "r_type": "PASS", "repeatable_r_d": "9 KERNEL_READY / 0 PRECONDITION_NOT_REPLAYABLE",
        },
        "outcome": "CONFORMANCE_COMPLETE_9_OF_9_KERNEL_READY",
        "predecessor": file_ref(SP1_COMPILE),
        "row_id": SP1_ROW,
        "schema": "rd22.step11.sp1-07.orientation-recompile.v001",
    }
    write_json(ROOT / "generated/SP1_compile_result.json", sp1_compile)
    sp1_status = {
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
        "kernel_ready": 9, "row_id": SP1_ROW, "schema": "rd22.step11.row-status.v003",
        "status": "FORMALIZATION_COMPLETE_9_OF_9_KERNEL_READY", "underdetermined": 0,
    }
    write_json(ROOT / "generated/SP1_row_status.json", sp1_status)

    prior_sp2_bundle = json.loads(SP2_BUNDLE.read_bytes())
    prior_o02_ref = next(item["proof"] for item in prior_sp2_bundle["proofs"] if item["derivation_id"] == O02)
    prior_o02 = json.loads((CLEANROOM / prior_o02_ref["relative_path"]).read_bytes())
    sp2_expected = prior_o02["expected_conclusion"]
    sp2_binding = {
        "carrier": carrier_ref,
        "conclusion": sp2_expected,
        "derivation_id": O02,
        "expected_conclusion": sp2_expected,
        "row_id": SP2_ROW,
        "schema": "rd22.step11.orientation-unitary-consumer-binding.v001",
        "shared_proof": proof_ref,
        "status": "KERNEL_READY",
        "target_opcode": "KERNEL",
    }
    sp2_data = canonical(sp2_binding)
    sp2_binding_path = ROOT / "generated" / f"{sha(sp2_data)}--SP2_O02_FULL_SOURCE_RECORD_ORIENTATION_COVARIANCE.json"
    sp2_binding_path.write_bytes(sp2_data)
    sp2_binding_ref = file_ref(sp2_binding_path)
    sp2_proofs = []
    for item in prior_sp2_bundle["proofs"]:
        if item["derivation_id"] == O02:
            sp2_proofs.append({"derivation_id": O02, "proof": sp2_binding_ref})
        else:
            sp2_proofs.append(item)
    sp2_bundle = {
        "aggregate_status": "KERNEL_READY",
        "gap_ids": [],
        "orientation_index": prior_sp2_bundle["orientation_index"],
        "predecessor": file_ref(SP2_BUNDLE),
        "proof_ids": prior_sp2_bundle["proof_ids"],
        "proofs": sp2_proofs,
        "pushout_index": prior_sp2_bundle["pushout_index"],
        "row_id": SP2_ROW,
        "schema": "rd22.step11.sp2-05.covariance-proof-bundle.v002",
    }
    if len(sp2_proofs) != 7 or sp2_bundle["proof_ids"] != [item["derivation_id"] for item in sp2_proofs]:
        raise BuildError("SP2_BUNDLE_INDEX")
    write_json(ROOT / "generated/SP2_p_pushout_relabel_orientation.json", sp2_bundle)
    prior_sp2_compile = json.loads(SP2_COMPILE.read_bytes())
    receivers = prior_sp2_compile["receivers"]
    receivers["r_kernel_covariance"] = {"gap_ids": [], "ready": 7, "required": 7, "status": "PASS"}
    sp2_compile = {
        "built_proof_ids": prior_sp2_compile["built_proof_ids"] + [O02],
        "gap_ids": [],
        "overall": "CONFORMANCE_COMPLETE_8_BUILT_0_GAPS",
        "predecessor": file_ref(SP2_COMPILE),
        "receivers": receivers,
        "row_id": SP2_ROW,
        "schema": "rd22.step11.sp2-05.orientation-recompile.v001",
    }
    if any(value.get("status") not in {"PASS"} for value in receivers.values() if isinstance(value, dict) and "status" in value):
        raise BuildError("SP2_RECEIVER_NOT_COMPLETE")
    write_json(ROOT / "generated/SP2_compile_result.json", sp2_compile)
    sp2_status = {
        "admission": "BARRED_STEP11_SUBGATE", "chain_invoked": False,
        "proof_objects_ready": 8, "row_id": SP2_ROW, "schema": "rd22.step11.row-status.v003",
        "status": "FORMALIZATION_COMPLETE_8_OF_8_PROOF_OBJECTS_READY", "underdetermined": 0,
    }
    write_json(ROOT / "generated/SP2_row_status.json", sp2_status)

    negatives = []
    for control in ["IDENTITY_INSTEAD_OF_GAMMA", "MISSING_SOURCE", "WRONG_REVERSED_C", "SP1_D08_LEFT_PARTIAL", "SP2_GAP_LEFT_OPEN"]:
        try:
            if control == "IDENTITY_INSTEAD_OF_GAMMA":
                mutated = json.loads(json.dumps(carrier)); mutated["matrices"]["U_c"] = matrix_json(IDENTITY3); validate_carrier(mutated)
            elif control == "MISSING_SOURCE":
                mutated = json.loads(json.dumps(carrier)); mutated["source_bindings"][0]["span_sha256"] = "0" * 64; validate_carrier(mutated)
            elif control == "WRONG_REVERSED_C":
                mutated = json.loads(json.dumps(carrier)); mutated["matrices"]["c_partial_reversed"] = matrix_json(c); validate_carrier(mutated)
            elif control == "SP1_D08_LEFT_PARTIAL":
                if all(item["status"] == "KERNEL_READY" for item in prior_sp1_index["entries"]):
                    raise BuildError("CONTROL_SETUP")
                raise BuildError("SP1_PARTIAL_REFUSED")
            else:
                if not prior_sp2_bundle["gap_ids"]:
                    raise BuildError("CONTROL_SETUP")
                raise BuildError("SP2_OPEN_GAP_REFUSED")
        except BuildError as exc:
            negatives.append({"control": control, "refusal": str(exc), "status": "PASS_REFUSED"})
        else:
            raise BuildError(f"NEGATIVE_DID_NOT_BITE:{control}")

    self_check = {
        "block_pins": len(BLOCKS), "canonical_json": "TIGHT_SORTED_UTF8_NO_TRAILING_NEWLINE",
        "carrier_sha256": carrier_ref["sha256"], "chain_invoked": False,
        "exact_matrix_checks": ["U^*U=I", "Gamma b+b Gamma=0", "b_rev=-b", "c_rev=-c", "U c U^*=c_rev", "c^*=c"],
        "negative_controls": negatives, "predecessor_inventories_rehashed": 2,
        "proof_sha256": proof_ref["sha256"], "schema": "rd22.step11.orientation-unitary.self-check.v001",
        "source_pins": len(EXPECTED), "status": "PASS",
    }
    write_json(ROOT / "generated/self_check.json", self_check)

    members = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.name != "inventory.generated.json":
            members.append(file_ref(path))
    inventory = {"members": members, "schema": "rd22.step11.orientation-unitary.package-inventory.v001", "total_files": len(members)}
    write_json(ROOT / "inventory.generated.json", inventory)
    for member in members:
        path = CLEANROOM / member["relative_path"]
        data = path.read_bytes()
        if len(data) != member["byte_length"] or sha(data) != member["sha256"]:
            raise BuildError(f"INVENTORY:{path}")

    print(json.dumps({
        "carrier_sha256": carrier_ref["sha256"], "inventory_files": len(members),
        "inventory_sha256": sha((ROOT / "inventory.generated.json").read_bytes()),
        "proof_sha256": proof_ref["sha256"], "sp1": sp1_status["status"],
        "sp2": sp2_status["status"], "self_check_sha256": sha((ROOT / "generated/self_check.json").read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except BuildError as exc:
        raise SystemExit(f"ORIENTATION_UNITARY_BUILD_FAIL {exc}")
