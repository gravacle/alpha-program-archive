#!/usr/bin/env python3
"""Execute the sealed causal-line connection-return lift."""

from __future__ import annotations

from fractions import Fraction
import cmath
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_CAUSAL_LINE_CONNECTION_RETURN_LIFT_SPEC_V001.md"
SPEC_SHA256 = "e1b09d4bb5eb42ac05f959f7558f72dc1442b1631bec971cd285725cde86748f"
OUT = ROOT / "stage8_execution/work/T07_causal_line_connection_return_lift.json"

AUTHORITIES = {
    "STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_RESULT_V001.md":
        "21b782b50e9b0ddf1785727ff625a2b933d370aaf539c9fea74982025279b729",
    "stage8_execution/t7_relayed_connected_preparation_retest/"
    "T07_RELAYED_CONNECTED_PREPARATION_RETEST_V001.seal.sha256":
        "b2e8cd624bb7ee5c946762d423e8dcee5a4527dcc92d9724064d8ffb3e5beaf1",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md":
        "52187f8174b203d3cf2acb641d800f45ae733331cc0f3d56658898ed7daec244",
    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md":
        "52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d",
    "R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md":
        "2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21",
    "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md":
        "1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305",
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
                (
                    left[row][pivot] * right[pivot][column]
                    for pivot in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def frobenius_square(matrix: Matrix) -> Fraction:
    return sum(
        (entry * entry for row in matrix for entry in row),
        Fraction(0),
    )


def identity(size: int) -> Matrix:
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def apply(matrix: Matrix, vector: tuple[int, ...]) -> list[Fraction]:
    return [
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(len(vector))
            ),
            Fraction(0),
        )
        for row in range(len(matrix))
    ]


def outer(left: tuple[int, ...], right: tuple[int, ...]) -> Matrix:
    return [
        [
            Fraction(left[row] * right[column], 2)
            for column in range(len(right))
        ]
        for row in range(len(left))
    ]


def incidence_vectors(count: int) -> list[tuple[int, ...]]:
    vectors = []
    for cell in range(count):
        vector = [0] * (count + 1)
        vector[cell] = -1
        vector[cell + 1] = 1
        vectors.append(tuple(vector))
    return vectors


def chain_row(count: int) -> dict[str, object]:
    vectors = incidence_vectors(count)
    projectors = [outer(vector, vector) for vector in vectors]
    transition = projectors[0]
    for index in range(1, count):
        transition = matmul(projectors[index], transition)

    connection = outer(vectors[-1], vectors[0])
    local_connections = [
        outer(vectors[index], vectors[index - 1])
        for index in range(1, count)
    ]
    composed_connection = projectors[0]
    for local_connection in local_connections:
        composed_connection = matmul(local_connection, composed_connection)
    if count == 1:
        composed_connection = projectors[0]

    shift = [[Fraction(0) for _ in range(count + 1)] for _ in range(count + 1)]
    for vertex in range(count):
        shift[vertex + 1][vertex] = Fraction(1)
    shift_errors = []
    local_isometry_errors = []
    for index, local_connection in enumerate(local_connections, start=1):
        shifted = apply(shift, vectors[index - 1])
        shift_errors.append(
            sum(
                (
                    (shifted[row] - vectors[index][row]) ** 2
                    for row in range(count + 1)
                ),
                Fraction(0),
            )
        )
        local_isometry_errors.append(
            max(
                frobenius_square(
                    subtract(
                        matmul(transpose(local_connection), local_connection),
                        projectors[index - 1],
                    )
                ),
                frobenius_square(
                    subtract(
                        matmul(local_connection, transpose(local_connection)),
                        projectors[index],
                    )
                ),
            )
        )

    connection_composition_error = frobenius_square(
        subtract(composed_connection, connection)
    )
    returned = matmul(transpose(connection), transition)
    expected_scalar = Fraction(-1, 2) ** (count - 1)
    expected_returned = [
        [expected_scalar * value for value in row]
        for row in projectors[0]
    ]
    error_square = frobenius_square(subtract(returned, expected_returned))
    require(error_square == 0, f"return identity failed for N={count}")
    require(expected_scalar != 0, f"zero baseline for N={count}")
    require(
        all(error == 0 for error in shift_errors),
        f"oriented shift failed for N={count}",
    )
    require(
        all(error == 0 for error in local_isometry_errors),
        f"line isometry failed for N={count}",
    )
    require(
        connection_composition_error == 0,
        f"connection composition failed for N={count}",
    )
    return {
        "N": count,
        "source_dimension": count + 1,
        "baseline_scalar_exact": str(expected_scalar),
        "returned_endomorphism_error_square_exact": str(error_square),
        "oriented_shift_error_squares_exact": [
            str(error) for error in shift_errors
        ],
        "local_partial_isometry_error_squares_exact": [
            str(error) for error in local_isometry_errors
        ],
        "connection_composition_error_square_exact": str(
            connection_composition_error
        ),
        "normalized_baseline": "1",
    }


def phase_covariance_check() -> dict[str, object]:
    scalar = complex(-0.5)
    phi_initial = 0.37
    phi_final = -0.81
    transition_rephased = (
        cmath.exp(1j * phi_final)
        * scalar
        * cmath.exp(-1j * phi_initial)
    )
    connection_rephased = (
        cmath.exp(1j * phi_final)
        * 1.0
        * cmath.exp(-1j * phi_initial)
    )
    returned = connection_rephased.conjugate() * transition_rephased
    return {
        "test_scalar_real": scalar.real,
        "returned_scalar_real": returned.real,
        "returned_scalar_imag": returned.imag,
        "absolute_error": abs(returned - scalar),
        "symbolic_identity": (
            "(e^{i phi_f} V e^{-i phi_i})^dagger "
            "(e^{i phi_f} T e^{-i phi_i})=e^{i phi_i} V^dagger T "
            "e^{-i phi_i}"
        ),
    }


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"authority drift: {relative}")

    rows = [chain_row(count) for count in range(1, 9)]
    phase = phase_covariance_check()
    require(phase["absolute_error"] < 2e-16, "phase covariance failed")
    connection_derived = all(
        all(value == "0" for value in row["oriented_shift_error_squares_exact"])
        and all(
            value == "0"
            for value in row["local_partial_isometry_error_squares_exact"]
        )
        and row["connection_composition_error_square_exact"] == "0"
        for row in rows
    )
    require(connection_derived, "oriented connection return not derived")
    result = {
        "schema": "stage8_t7_causal_line_connection_return_lift_v001",
        "spec_sha256": SPEC_SHA256,
        "Q1_source_lines": {
            "rank_one_for_every_executed_history": True,
            "enlarged_rank_or_multiendpoint_branch_used": False,
        },
        "Q2_connection_return": {
            "incidence_chain_partial_isometry_algebra_derived":
                connection_derived,
            "physical_source_line_transport_derived": False,
            "boundary_metric_isometry_imported": True,
            "phase_covariance": phase,
            "response_dependent_return_used": False,
        },
        "Q3_Q4_chain_execution": rows,
        "arbitrary_finite_N_formula": "a_N(0)=(-1/2)^(N-1)",
        "arbitrary_finite_N_baseline_nonzero": True,
        "one_handle_reduction_exact": rows[0]["baseline_scalar_exact"] == "1",
        "Q5_uniqueness": {
            "complex_linear_closure_imported": True,
            "fixed_initial_source_line_imported": True,
            "fixed_final_source_line_derived": False,
            "endomorphism_of_one_dimensional_line": True,
            "full_source_state_expectation_used": False,
            "inclusive_probability_used": False,
            "response_dependent_final_line_used": False,
            "polar_return_from_perturbed_transition_used": False,
            "branch_sum_used": False,
            "normalized_amplitude_independent_of_constant_return_phase": True,
        },
        "physical_parent_audit": {
            "finite_lorentzian_parent_used": False,
            "ideal_incidence_projector_chain_used": True,
            "completed_record_endpoint_replaced_by_source_line": True,
            "conditional_projector_chain_identity_derived": True,
        },
        "overall_verdict": "CAUSAL_LINE_CONNECTION_RETURN_LIFT_BLOCKED",
        "finite_relayed_connection_return_amplitude_derived": False,
        "state_expectation_C1_superseded_for_primitive_line_amplitude": False,
        "complete_source_CTP_amplitude_derived": False,
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
