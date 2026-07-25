#!/usr/bin/env python3
"""Exact audit of the conditional source-flux record holonomy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_flux_conditioned_record_write_v002.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]
Vector = tuple[Gaussian, ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)
ZERO2: Matrix = ((ZERO, ZERO), (ZERO, ZERO))

I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
Q0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
Q1: Matrix = ((ZERO, ZERO), (ZERO, ONE))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))


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
        tuple(g_add(left[row][column], right[row][column]) for column in range(len(left[0])))
        for row in range(len(left))
    )


def matrix_scale(value: Gaussian, matrix: Matrix) -> Matrix:
    return tuple(tuple(g_mul(value, entry) for entry in row) for row in matrix)


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum_gaussian(
                g_mul(left[row][index], right[index][column])
                for index in range(len(right))
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def conjugate_transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(g_conj(matrix[column][row]) for column in range(len(matrix)))
        for row in range(len(matrix[0]))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            g_mul(
                left[row_left][column_left],
                right[row_right][column_right],
            )
            for column_left in range(len(left[0]))
            for column_right in range(len(right[0]))
        )
        for row_left in range(len(left))
        for row_right in range(len(right))
    )


def matrix_vector_mul(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum_gaussian(g_mul(matrix[row][column], vector[column]) for column in range(len(vector)))
        for row in range(len(matrix))
    )


def density(vector: Vector) -> Matrix:
    return tuple(
        tuple(g_mul(vector[row], g_conj(vector[column])) for column in range(len(vector)))
        for row in range(len(vector))
    )


def partial_trace_source(joint_density: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum_gaussian(
                joint_density[2 * source + record_row][2 * source + record_column]
                for source in range(2)
            )
            for record_column in range(2)
        )
        for record_row in range(2)
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matrix_mul(left, right), matrix_scale(NEG_ONE, matrix_mul(right, left)))


def build_result() -> dict[str, object]:
    require(Q0 == conjugate_transpose(Q0), "Q0 is not Hermitian")
    require(Q1 == conjugate_transpose(Q1), "Q1 is not Hermitian")
    require(matrix_mul(Q0, Q0) == Q0, "Q0 is not idempotent")
    require(matrix_mul(Q1, Q1) == Q1, "Q1 is not idempotent")
    require(matrix_mul(Q0, Q1) == ZERO2, "Source-flux projectors are not orthogonal")
    require(matrix_add(Q0, Q1) == I2, "Source-flux projectors are incomplete")
    require(Y == conjugate_transpose(Y), "Record generator is not Hermitian")
    require(matrix_mul(Y, Y) == I2, "Record generator is not unit normalized")

    minus_i_y = matrix_scale(NEG_I, Y)
    zero4: Matrix = tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
    i4 = kron(I2, I2)
    source_flux = kron(Q1, I2)
    inactive = kron(Q0, I2)
    active_write = kron(Q1, minus_i_y)
    write_unitary = matrix_add(inactive, active_write)
    phase_pi_unitary = matrix_add(inactive, matrix_scale(NEG_ONE, active_write))

    state_00: Vector = (ONE, ZERO, ZERO, ZERO)
    state_10: Vector = (ZERO, ZERO, ONE, ZERO)
    state_11: Vector = (ZERO, ZERO, ZERO, ONE)
    source_superposition_ready: Vector = (ONE, ZERO, ONE, ZERO)

    require(matrix_mul(write_unitary, conjugate_transpose(write_unitary)) == i4, "Write is not unitary")
    require(matrix_mul(phase_pi_unitary, conjugate_transpose(phase_pi_unitary)) == i4, "Phase mutation is not unitary")
    require(commutator(write_unitary, source_flux) == zero4, "Write changes source flux")
    require(matrix_vector_mul(write_unitary, state_00) == state_00, "Zero-flux branch moved")
    require(matrix_vector_mul(write_unitary, state_10) == state_11, "Unit-flux branch did not write")

    coherent_written = matrix_vector_mul(write_unitary, source_superposition_ready)
    coherent_phase_written = matrix_vector_mul(phase_pi_unitary, source_superposition_ready)
    joint_density = density(coherent_written)
    phase_joint_density = density(coherent_phase_written)
    require(joint_density != phase_joint_density, "Active identity phase did not change joint coherence")
    require(
        partial_trace_source(joint_density) == partial_trace_source(phase_joint_density),
        "Active identity phase changed the reduced record density",
    )

    out = {
        "status": "PASS_CONDITIONAL_SOURCE_FLUX_HOLONOMY_ACTIVE_PHASE_OPEN",
        "unit_source_flux_sector_inherited": True,
        "zero_flux_no_charged_write_adopted": True,
        "relative_onset_saturation_inherited_as_adopted": True,
        "source_flux_spectrum": [0, 1],
        "source_flux_nondemolition": True,
        "equatorial_first_onset_holonomy_class_derived_conditionally": True,
        "integrated_record_changing_holonomy_fixed_conditionally": True,
        "integrated_record_changing_holonomy": "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing",
        "active_identity_phase_changes_joint_density": True,
        "active_identity_phase_changes_reduced_record_density": False,
        "complete_physical_write_operator_derived": False,
        "physical_dynamical_action_fixed": False,
        "source_conditioned_identity_phase_fixed": False,
        "complete_source_record_environment_operator_derived": False,
        "post_closure_pointer_coefficient_derived": False,
        "source_odd_scalar_pseudoscalar_coefficient_derived": False,
        "physical_durability_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "conditional_zero_or_one_flux_ready_subspace_holonomy_only",
    }
    return out


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
