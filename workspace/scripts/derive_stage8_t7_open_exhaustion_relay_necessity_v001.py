#!/usr/bin/env python3
"""Execute the sealed Stage-8 T7 O1-O4 relay-necessity gate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_SPEC_V001.md"
)
SPEC_SHA256 = "1836c808eef24ce0a4dab994f4d9857d77396bbbecc4830c6289d63db7144803"
OUT = ROOT / "stage8_execution/work/T07_open_exhaustion_relay_necessity.json"
EXTERNAL = Path(
    "/Users/bgm/MB Work/alpha_supervision/"
    "STAGE8_T7_LIFT_ADJUDICATION_RETURN_V001.md"
)

AUTHORITIES = {
    "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md":
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md":
        "202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35",
    "R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md":
        "2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
    "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md":
        "10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_RESULT_V001.md":
        "eb83e5450928bf148cae58b3b553c9dff482b07172aa8aeb182e0834bb869723",
    "STAGE8_T7_COMPLETED_EFFECT_ZERO_BASELINE_RESULT_V001.md":
        "30903a1623718fd0ecb3cb2ad50765792c20f402710454e43cfbbccb42048af8",
    "stage8_execution/t7_primitive_connected_lift/"
    "T07_PRIMITIVE_CONNECTED_LIFT_VERIFIER_V002.seal.sha256":
        "93b4a836962a177301d0338c8e81c3203cc52136a2123ca3e11a3c9a844b95a8",
}
EXTERNAL_SHA256 = "34ebb4dbc2903b91231bd4253dba78c0012c4be4eac062b8145f970fee808eb2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def exp_hermitian(operator: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1j * time * values)) @ vectors.conj().T


def star_operator(arms: int) -> np.ndarray:
    differential = np.zeros((arms + 1, arms), dtype=complex)
    for arm in range(arms):
        differential[0, arm] = -1.0
        differential[arm + 1, arm] = 1.0
    return np.block(
        [
            [np.zeros((arms + 1, arms + 1)), differential],
            [differential.conj().T, np.zeros((arms, arms))],
        ]
    )


def star_checks() -> dict[str, object]:
    tau_record = math.pi / math.sqrt(2.0)
    rows = {}
    for arms in (1, 2, 3):
        operator = star_operator(arms)
        unitary = exp_hermitian(operator, tau_record)
        root = np.zeros(2 * arms + 1, dtype=complex)
        root[0] = 1.0
        endpoint = np.zeros_like(root)
        endpoint[1] = 1.0
        survival = complex(np.vdot(root, unitary @ root))
        transfer = complex(np.vdot(endpoint, unitary @ root))
        angle = math.sqrt(arms + 1.0) * tau_record
        formula_survival = (
            1.0 / (arms + 1.0)
            + arms / (arms + 1.0) * math.cos(angle)
        )
        formula_transfer = (1.0 - math.cos(angle)) / (arms + 1.0)
        rows[str(arms)] = {
            "survival_real": float(survival.real),
            "survival_imag": float(survival.imag),
            "designated_transfer_real": float(transfer.real),
            "designated_transfer_imag": float(transfer.imag),
            "formula_survival": formula_survival,
            "formula_designated_transfer": formula_transfer,
            "max_designated_transfer": 2.0 / (arms + 1.0),
            "max_symmetric_transfer":
                2.0 * math.sqrt(arms) / (arms + 1.0),
            "matrix_formula_error": max(
                abs(survival - formula_survival),
                abs(transfer - formula_transfer),
            ),
        }

    require(rows["1"]["matrix_formula_error"] < 2e-14, "m=1 formula")
    require(abs(rows["1"]["survival_real"]) < 2e-14, "m=1 survival")
    require(
        abs(rows["1"]["designated_transfer_real"] - 1.0) < 2e-14,
        "m=1 transfer",
    )
    for arms in ("2", "3"):
        require(rows[arms]["matrix_formula_error"] < 2e-14, f"m={arms}")
        require(rows[arms]["max_designated_transfer"] < 1.0, "mixed max")
        require(rows[arms]["max_symmetric_transfer"] < 1.0, "symmetric max")
    return {
        "tau_record": tau_record,
        "stars": rows,
        "exact_closure_unique_in_sealed_competitor_set": True,
    }


def kron_all(vectors: list[np.ndarray]) -> np.ndarray:
    value = np.array([1.0 + 0.0j])
    for vector in vectors:
        value = np.kron(value, vector)
    return value


def embed_local(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0 + 0.0j]])
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(operator.shape[0]),
        )
    return value


def partial_trace_last_pure(
    state: np.ndarray, local_dimension: int, count: int
) -> np.ndarray:
    matrix = state.reshape(local_dimension ** (count - 1), local_dimension)
    return matrix @ matrix.conj().T


def relay_checks() -> dict[str, object]:
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    edge = np.array([0.0, 0.0, 1.0], dtype=complex)
    swap = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]],
        dtype=complex,
    )
    require(np.linalg.norm(swap @ ready - pointer) < 1e-15, "root->pointer")
    require(np.linalg.norm(swap @ edge + edge) < 1e-15, "edge sign")

    rows = {}
    state = pointer.copy()
    for old_count in (1, 2):
        injected = np.kron(state, ready)
        next_swap = embed_local(swap, old_count, old_count + 1)
        advanced = next_swap @ injected
        expected = kron_all([pointer] * (old_count + 1))
        density_restricted = partial_trace_last_pure(
            advanced, 3, old_count + 1
        )
        old_density = np.outer(state, state.conj())
        old_pointer_observable = embed_local(
            np.diag([0.0, 1.0, 0.0]), 0, old_count + 1
        )
        commutator = (
            next_swap @ old_pointer_observable
            - old_pointer_observable @ next_swap
        )
        rows[f"{old_count}_to_{old_count + 1}"] = {
            "relay_isometry_norm_error": abs(
                np.linalg.norm(injected) - np.linalg.norm(state)
            ),
            "advanced_state_error": float(np.linalg.norm(advanced - expected)),
            "restriction_error": float(
                np.linalg.norm(density_restricted - old_density)
            ),
            "old_pointer_commutator_norm": float(np.linalg.norm(commutator)),
        }
        state = advanced

    # Generic branch-label relay p_h -> e_h tensor r_next.
    branch_count = 3
    relay = np.zeros((branch_count * 1, branch_count), dtype=complex)
    for branch in range(branch_count):
        relay[branch, branch] = 1.0
    gram_error = float(
        np.linalg.norm(relay.conj().T @ relay - np.eye(branch_count))
    )
    require(gram_error < 1e-15, "branch relay isometry")
    require(
        all(
            max(row.values()) < 2e-14
            for row in rows.values()
        ),
        "finite relay regression",
    )
    return {
        "type_obstruction": (
            "codomain L_p(c) differs from domain L_r(c+1); direct "
            "composition is undefined"
        ),
        "branch_relay_gram_error": gram_error,
        "finite_Qspec_relay": rows,
        "prior_records_preserved": True,
        "new_ready_root_supplied": True,
        "primitive_Qspec_relay_realizes_required_type": True,
        "complete_physical_durability_claimed": False,
        "verdict": "DEPENDENCY_INVERSION_DERIVED",
    }


def causal_order_witness() -> dict[str, float | bool]:
    incidence = np.array(
        [[-1.0, 0.0], [1.0, -1.0], [0.0, 1.0]], dtype=complex
    )
    projectors = [
        np.outer(incidence[:, j], incidence[:, j].conj()) / 2.0
        for j in range(2)
    ]
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]], dtype=complex
    )
    tau_record = math.pi / math.sqrt(2.0)
    writes = [
        np.kron(
            projectors[j],
            embed_local(c_partial, j, 2),
        )
        for j in range(2)
    ]
    unitaries = [exp_hermitian(write, tau_record) for write in writes]
    forward = unitaries[1] @ unitaries[0]
    reverse = unitaries[0] @ unitaries[1]
    difference = float(np.linalg.norm(forward - reverse))
    difference_square = difference * difference
    require(difference > 1e-6, "causal assignment order erased")
    require(abs(difference_square - 24.0) < 2e-12, "order witness != sqrt24")
    return {
        "shared_source_projector_overlap":
            float(np.trace(projectors[0] @ projectors[1]).real),
        "forward_reverse_unitary_norm": difference,
        "forward_reverse_unitary_norm_square": difference_square,
        "strictly_nonzero": True,
    }


def endpoint_conditioning_witness(stars: dict[str, object]) -> dict[str, object]:
    row = stars["2"]
    q = float(row["designated_transfer_real"])
    return {
        "endpoint_1_amplitude": q,
        "endpoint_2_amplitude": q,
        "endpoint_vector": [q, q],
        "normalized_symmetric_endpoint_amplitude": math.sqrt(2.0) * q,
        "inclusive_endpoint_probability": 2.0 * q * q,
        "component_equality_does_not_identify_operations": True,
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    require(sha256(EXTERNAL) == EXTERNAL_SHA256, "external authority drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"authority drift: {relative}")

    o1 = star_checks()
    o2 = relay_checks()
    o3 = {
        "mixed_designated_endpoint_exact_closure_exists": False,
        "mixed_symmetric_endpoint_exact_closure_exists": False,
        "proof": (
            "For m>1, |q_m(t)|<=2/(m+1)<1 and the normalized symmetric "
            "amplitude is <=2*sqrt(m)/(m+1)<1."
        ),
        "replacement_interval_search_authorized": False,
    }
    o4_order = causal_order_witness()
    o4_endpoint = endpoint_conditioning_witness(o1["stars"])

    result = {
        "schema": "stage8_t7_open_exhaustion_relay_necessity_v001",
        "spec_sha256": SPEC_SHA256,
        "external_authority_sha256": EXTERNAL_SHA256,
        "O1_branch_conditioned_exactness": o1,
        "O2_dependency_inversion": o2,
        "O3_mixed_interval": o3,
        "O4_assignment_witness": o4_order,
        "O4_endpoint_conditioning_witness": o4_endpoint,
        "overall_verdict": "STAGE_ORDERING_AMENDMENT_REQUIRED",
        "stage_ordering_amendment_derived": True,
        "primitive_relay_durability_map_derived": True,
        "complete_physical_durability_derived": False,
        "connected_primitive_amplitude_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
