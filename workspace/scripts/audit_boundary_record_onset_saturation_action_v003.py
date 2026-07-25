#!/usr/bin/env python3
"""Exact realization audit for the relative record-orthogonalization budget."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "boundary_record_onset_saturation_action_v003.json"
Gaussian = tuple[int, int]
Vector = tuple[Gaussian, Gaussian]
Matrix = tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
TWO: Gaussian = (2, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)
ZERO2: Matrix = ((ZERO, ZERO), (ZERO, ZERO))
I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
P0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
P1: Matrix = ((ZERO, ZERO), (ZERO, ONE))
READY: Vector = (ONE, ZERO)
ORTHOGONAL: Vector = (ZERO, ONE)

# sqrt(2) times the two symmetric branch unitaries.
SQRT2_U0: Matrix = ((ONE, ONE), (NEG_ONE, ONE))
SQRT2_U1: Matrix = ((ONE, NEG_ONE), (ONE, ONE))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def g_conj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def sum_gaussian(values) -> Gaussian:
    total = ZERO
    for value in values:
        total = g_add(total, value)
    return total


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )


def matrix_neg(matrix: Matrix) -> Matrix:
    return tuple(tuple((-entry[0], -entry[1]) for entry in row) for row in matrix)


def matrix_scale(value: Gaussian, matrix: Matrix) -> Matrix:
    return tuple(tuple(g_mul(value, entry) for entry in row) for row in matrix)


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum_gaussian(
                g_mul(left[row][index], right[index][column])
                for index in range(2)
            )
            for column in range(2)
        )
        for row in range(2)
    )


def conjugate_transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(g_conj(matrix[column][row]) for column in range(2))
        for row in range(2)
    )


def matrix_vector_mul(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum_gaussian(g_mul(matrix[row][index], vector[index]) for index in range(2))
        for row in range(2)
    )


def inner(left: Vector, right: Vector) -> Gaussian:
    return sum_gaussian(g_mul(g_conj(left[index]), right[index]) for index in range(2))


def density(vector: Vector) -> Matrix:
    return tuple(
        tuple(g_mul(vector[row], g_conj(vector[column])) for column in range(2))
        for row in range(2)
    )


def trace(matrix: Matrix) -> Gaussian:
    return g_add(matrix[0][0], matrix[1][1])


def build_result() -> dict[str, object]:
    require(P0 == conjugate_transpose(P0), "P0 is not Hermitian")
    require(P1 == conjugate_transpose(P1), "P1 is not Hermitian")
    require(matrix_mul(P0, P0) == P0, "P0 is not idempotent")
    require(matrix_mul(P1, P1) == P1, "P1 is not idempotent")
    require(matrix_mul(P0, P1) == ZERO2, "Endpoint projectors are not orthogonal")
    require(matrix_add(P0, P1) == I2, "Endpoint projectors are not complete")
    require(P0 == density(READY), "P0 is not the ready-state projector")
    require(P1 == density(ORTHOGONAL), "P1 is not the orthogonal-state projector")

    require(Y == conjugate_transpose(Y), "Relative generator is not Hermitian")
    require(matrix_mul(Y, Y) == I2, "Relative generator is not unit normalized")

    require(
        matrix_mul(conjugate_transpose(SQRT2_U0), SQRT2_U0)
        == matrix_scale(TWO, I2),
        "U0 numerator is not sqrt(2)-unitary",
    )
    require(
        matrix_mul(conjugate_transpose(SQRT2_U1), SQRT2_U1)
        == matrix_scale(TWO, I2),
        "U1 numerator is not sqrt(2)-unitary",
    )

    relative_numerator = matrix_mul(conjugate_transpose(SQRT2_U0), SQRT2_U1)
    relative_unitary = matrix_scale(NEG_I, Y)
    require(
        relative_numerator == matrix_scale(TWO, relative_unitary),
        "Symmetric branches do not produce U0^dagger U1=-iY",
    )
    require(
        matrix_mul(relative_unitary, conjugate_transpose(relative_unitary)) == I2,
        "Relative endpoint operator is not unitary",
    )
    relative_endpoint = matrix_vector_mul(relative_unitary, READY)
    require(relative_endpoint == ORTHOGONAL, "Relative endpoint is not orthogonal")
    require(inner(READY, relative_endpoint) == ZERO, "Relative overlap is nonzero")

    contrast = matrix_add(P1, matrix_neg(P0))
    hs_write_contrast = trace(matrix_mul(conjugate_transpose(Y), contrast))
    require(hs_write_contrast == ZERO, "Relative generator and pointer contrast overlap")

    out = {
        "status": "PASS_RELATIVE_FS_BUDGET_CONDITIONAL_PHYSICAL_ACTION_OPEN",
        "common_closed_dilation_declared": True,
        "conditional_overlap_object": "U0_dagger_U1",
        "conditional_overlap_relative_unitary_identity_derived": True,
        "relative_orthogonalization_bound_imported": True,
        "relative_endpoint_overlap_computed": 0,
        "orthogonality_budget_pi_over_two_derived": True,
        "relative_onset_saturation_derived": False,
        "relative_onset_saturation_adopted_Level_1": True,
        "relative_FS_budget_fixed_conditional_on_adopted_rule": True,
        "relative_FS_budget": "pi*hbar/2",
        "relative_generator_coefficient": "pi*hbar/(2*tau_star)",
        "symmetric_branch_product_verified": True,
        "physical_dynamical_action_fixed": False,
        "absolute_one_branch_energy_fixed": False,
        "arbitrary_common_additive_hamiltonian_cancels": False,
        "factored_common_left_unitary_cancels": True,
        "orthogonal_reduced_record_supports_derived": False,
        "physical_durability_derived": False,
        "unique_causal_record_interval_numerically_derived": False,
        "relative_generator_identified_with_pointer_coefficient": False,
        "relative_generator_identified_with_source_mass": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "closed_dilation_relative_FS_bound_and_adopted_saturation_only",
    }
    required_keys = {
        "status",
        "common_closed_dilation_declared",
        "conditional_overlap_object",
        "conditional_overlap_relative_unitary_identity_derived",
        "relative_orthogonalization_bound_imported",
        "relative_endpoint_overlap_computed",
        "orthogonality_budget_pi_over_two_derived",
        "relative_onset_saturation_derived",
        "relative_onset_saturation_adopted_Level_1",
        "relative_FS_budget_fixed_conditional_on_adopted_rule",
        "relative_FS_budget",
        "relative_generator_coefficient",
        "symmetric_branch_product_verified",
        "physical_dynamical_action_fixed",
        "absolute_one_branch_energy_fixed",
        "arbitrary_common_additive_hamiltonian_cancels",
        "factored_common_left_unitary_cancels",
        "orthogonal_reduced_record_supports_derived",
        "physical_durability_derived",
        "unique_causal_record_interval_numerically_derived",
        "relative_generator_identified_with_pointer_coefficient",
        "relative_generator_identified_with_source_mass",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
        "scope",
    }
    require(set(out) == required_keys, "Result schema drift")
    return out


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
