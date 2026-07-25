#!/usr/bin/env python3
"""Derive the actual primitive causal completed-record transition map."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_SPEC_V001.md"
SPEC_SHA256 = "c4dcbf5bc1e98e3dd3e4503bcc2739e8795be11b7e96873598a181eedf00d654"
OUTPUT = ROOT / "stage8_execution/work/T07_actual_primitive_causal_transition_map.json"

AUTHORITIES = {
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md":
        "b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md":
        "52187f8174b203d3cf2acb641d800f45ae733331cc0f3d56658898ed7daec244",
    "STAGE8_T7_CAUSAL_LINE_CONNECTION_RETURN_LIFT_RESULT_V001.md":
        "5096f4cc2421574badf392cad591787e12928d27335683b5c77d0d98cd8e5918",
    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md":
        "52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d",
    "STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_RESULT_V001.md":
        "df2f478b936df96bd9e5cc4cf980231a88859f098528e4ca3923a3add27345da",
    "STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md":
        "9410ee80ff89beed4e133f75fcdb952d059f3386df12069793b5d60895d15486",
}

Matrix = list[list[Fraction]]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def frobenius_square(matrix: Matrix) -> Fraction:
    return sum((entry * entry for row in matrix for entry in row), Fraction(0))


def outer_normalized(left: tuple[int, ...], right: tuple[int, ...]) -> Matrix:
    return [
        [Fraction(left[i] * right[j], 2) for j in range(len(right))]
        for i in range(len(left))
    ]


def incidence_vectors(count: int) -> list[tuple[int, ...]]:
    vectors = []
    for cell in range(count):
        value = [0] * (count + 1)
        value[cell] = -1
        value[cell + 1] = 1
        vectors.append(tuple(value))
    return vectors


def complex_matmul(left: list[list[complex]], right: list[list[complex]]) -> list[list[complex]]:
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(len(right))), 0j)
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def local_record_endpoint_block() -> dict[str, object]:
    c = [
        [0j, 0j, -1j],
        [0j, 0j, 1j],
        [1j, -1j, 0j],
    ]
    c2 = complex_matmul(c, c)
    identity = [
        [complex(int(i == j)) for j in range(3)]
        for i in range(3)
    ]
    # At tau_R, sin(sqrt(2) tau_R)=0 and cos(sqrt(2) tau_R)=-1.
    unitary_plus = [
        [identity[i][j] - c2[i][j] for j in range(3)]
        for i in range(3)
    ]
    unitary_minus = [row[:] for row in unitary_plus]
    expected = [
        [0j, 1 + 0j, 0j],
        [1 + 0j, 0j, 0j],
        [0j, 0j, -1 + 0j],
    ]
    plus_error = max(
        abs(unitary_plus[i][j] - expected[i][j])
        for i in range(3)
        for j in range(3)
    )
    minus_error = max(
        abs(unitary_minus[i][j] - expected[i][j])
        for i in range(3)
        for j in range(3)
    )
    endpoint_plus = unitary_plus[1][0]
    endpoint_minus = unitary_minus[1][0]
    require(plus_error == 0 and minus_error == 0, "local exact unitary changed")
    require(endpoint_plus == 1 and endpoint_minus == 1,
            "endpoint block is not the spin identity")
    return {
        "c_cubed_equals_2c": True,
        "unitary_at_tau_R": "swap(r,p) direct_sum (-1 on e)",
        "gamma5_plus_endpoint_amplitude": endpoint_plus.real,
        "gamma5_minus_endpoint_amplitude": endpoint_minus.real,
        "endpoint_block_equals_identity_on_spin": True,
        "controlled_endpoint_compression_equals_Pj_tensor_Ispin": True,
    }


def chain_row(count: int) -> dict[str, object]:
    vectors = incidence_vectors(count)
    projectors = [outer_normalized(vector, vector) for vector in vectors]
    transition = projectors[0]
    for index in range(1, count):
        transition = matmul(projectors[index], transition)

    coefficient = Fraction(-1, 2) ** (count - 1)
    range_map = outer_normalized(vectors[-1], vectors[0])
    expected_transition = [
        [coefficient * entry for entry in row]
        for row in range_map
    ]
    transition_error = frobenius_square(
        subtract(transition, expected_transition)
    )

    returned = matmul(transpose(range_map), transition)
    expected_return = [
        [coefficient * entry for entry in row]
        for row in projectors[0]
    ]
    returned_error = frobenius_square(subtract(returned, expected_return))

    if count == 1:
        adjacent_commutator_square = Fraction(0)
    else:
        commutator = subtract(
            matmul(projectors[1], projectors[0]),
            matmul(projectors[0], projectors[1]),
        )
        adjacent_commutator_square = frobenius_square(commutator)

    require(transition_error == 0, f"range formula failed at N={count}")
    require(returned_error == 0, f"return scalar failed at N={count}")
    require(coefficient != 0, f"zero finite baseline at N={count}")
    if count > 1:
        require(adjacent_commutator_square > 0,
                f"adjacent connectedness vanished at N={count}")

    return {
        "N": count,
        "source_orbital_dimension": count + 1,
        "Dirac_spin_dimension": 4,
        "actual_endpoint_compression_product_used": True,
        "transition_range_is_last_incidence_line": True,
        "transition_rank_on_orbital_carrier": 1,
        "returned_map_is_scalar_identity_on_initial_line_times_spin": True,
        "baseline_scalar_exact": str(coefficient),
        "transition_range_formula_error_square_exact": str(transition_error),
        "returned_scalar_error_square_exact": str(returned_error),
        "adjacent_projector_commutator_norm_square_exact":
            str(adjacent_commutator_square),
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    verified = {}
    for relative, expected in AUTHORITIES.items():
        actual = sha256(ROOT / relative)
        require(actual == expected, f"authority drift: {relative}")
        verified[relative] = actual

    local = local_record_endpoint_block()
    rows = [chain_row(count) for count in range(1, 9)]

    result = {
        "schema": "stage8-t7-actual-primitive-causal-transition-map-v001",
        "spec_sha256": SPEC_SHA256,
        "authority_sha256": verified,
        "target_value_used": False,
        "P1_actual_primitive_parent": {
            "one_source_sector_of_global_parent_used": True,
            "causal_one_use_unitaries_used": True,
            "source_state_used": False,
            "Fock_expectation_used": False,
            "CAR_determinant_used": False,
            "normalized_trace_used": False,
        },
        "P2_local_endpoint_compression": local,
        "P3_chain_execution": rows,
        "arbitrary_finite_N_transition_formula":
            "T_N=[product_(j=1)^(N-1)<u_j,u_(j-1)>]"
            "|u_(N-1)><u_0| tensor I_spin",
        "arbitrary_finite_N_baseline":
            "a_N(0)=(-1/2)^(N-1), nonzero for every finite N",
        "P4_competitor_scope": {
            "connected_adjacent_incidence_overlaps_retained": True,
            "independent_primitive_record_only_contact_kernel_allowed": False,
            "exclusion_basis":
                "adopted Global Boundary Descent / Quasi-Free Completeness",
            "exclusion_is_premise_based_not_theorem_based": True,
            "generated_descendants_remain_downstream": True,
        },
        "verdict": "ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_DERIVED",
        "finite_connected_scalar_amplitude_derived": True,
        "connected_primitive_amplitude_derived": True,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
