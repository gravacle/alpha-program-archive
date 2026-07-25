#!/usr/bin/env python3
"""Exact algebraic audit of the record-onset action gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "boundary_record_onset_saturation_action_v001.json"
Gaussian = tuple[int, int]
Vector = tuple[Gaussian, Gaussian]
Matrix = tuple[tuple[Gaussian, Gaussian], tuple[Gaussian, Gaussian]]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)
ZERO2: Matrix = ((ZERO, ZERO), (ZERO, ZERO))
I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
P0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
P1: Matrix = ((ZERO, ZERO), (ZERO, ONE))
R0: Vector = (ONE, ZERO)
R1: Vector = (ZERO, ONE)


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


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(2))
        for row in range(2)
    )


def matrix_neg(matrix: Matrix) -> Matrix:
    return tuple(tuple((-entry[0], -entry[1]) for entry in row) for row in matrix)


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


def matrix_vector_mul(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum_gaussian(g_mul(matrix[row][index], vector[index]) for index in range(2))
        for row in range(2)
    )


def sum_gaussian(values) -> Gaussian:
    total = ZERO
    for value in values:
        total = g_add(total, value)
    return total


def inner(left: Vector, right: Vector) -> Gaussian:
    return sum_gaussian(g_mul(g_conj(left[index]), right[index]) for index in range(2))


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matrix_mul(left, right), matrix_neg(matrix_mul(right, left)))


def trace(matrix: Matrix) -> Gaussian:
    return g_add(matrix[0][0], matrix[1][1])


def build_result() -> dict[str, object]:
    contrast = matrix_add(P1, matrix_neg(P0))
    geodesic_endpoint_unitary = (
        (ZERO, NEG_ONE),
        (ONE, ZERO),
    )

    require(inner(R0, R1) == ZERO, "Declared record endpoints are not orthogonal")
    require(matrix_mul(Y, Y) == I2, "Write generator is not unit normalized")
    require(inner(R0, matrix_vector_mul(Y, R0)) == ZERO, "Write mean is not zero")
    require(
        inner(R0, matrix_vector_mul(matrix_mul(Y, Y), R0)) == ONE,
        "Write second moment is not one",
    )
    require(
        matrix_vector_mul(geodesic_endpoint_unitary, R0) == R1,
        "Geodesic endpoint unitary does not write the record",
    )
    require(commutator(Y, P0) != ZERO2, "Write direction incorrectly preserves P0")
    require(commutator(Y, P1) != ZERO2, "Write direction incorrectly preserves P1")
    require(commutator(contrast, P0) == ZERO2, "Contrast does not preserve P0")
    require(commutator(contrast, P1) == ZERO2, "Contrast does not preserve P1")
    require(trace(matrix_mul(Y, contrast)) == ZERO, "Write and contrast are not orthogonal")

    out = {
        "status": "PASS_RECORD_ONSET_ACTION_FIXED_SOURCE_SCALE_OPEN",
        "record_endpoint_overlap": 0,
        "fubini_study_orthogonal_distance": "pi/2",
        "integrated_energy_uncertainty_lower_bound": "pi*hbar/2",
        "allow_require_onset_saturation_adopted_Level_1": True,
        "integrated_write_action": "pi*hbar/2",
        "constant_geodesic_write_energy": "pi*hbar/(2*tau_star)",
        "write_generator_second_moment_in_ready_state": 1,
        "write_generator_preserves_endpoint_sectors": False,
        "post_closure_contrast_preserves_endpoint_sectors": True,
        "write_contrast_hilbert_schmidt_inner_product": 0,
        "historical_target_blindness_established": False,
        "unique_causal_record_interval_numerically_derived": False,
        "complete_source_record_environment_action_derived": False,
        "physical_durability_derived": False,
        "write_energy_identified_with_pointer_coefficient": False,
        "write_energy_identified_with_source_mass": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "orthogonalization_bound_plus_adopted_onset_saturation_only",
    }
    return out


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
