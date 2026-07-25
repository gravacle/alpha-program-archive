#!/usr/bin/env python3
"""Exact audit of the source-flux-conditioned record-write operator."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_flux_conditioned_record_write_v001.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]
Vector = tuple[Gaussian, ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)

I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
Q0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
Q1: Matrix = ((ZERO, ZERO), (ZERO, ONE))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
MINUS_I_Y: Matrix = ((ZERO, NEG_ONE), (ONE, ZERO))


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


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matrix_mul(left, right), matrix_scale(NEG_ONE, matrix_mul(right, left)))


def build_result() -> dict[str, object]:
    zero4: Matrix = tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
    i4 = kron(I2, I2)
    source_flux = kron(Q1, I2)
    inactive = kron(Q0, I2)
    active_write = kron(Q1, MINUS_I_Y)
    write_unitary = matrix_add(inactive, active_write)
    active_phase_flipped = matrix_add(inactive, matrix_scale(NEG_ONE, active_write))

    state_00: Vector = (ONE, ZERO, ZERO, ZERO)
    state_10: Vector = (ZERO, ZERO, ONE, ZERO)
    state_11: Vector = (ZERO, ZERO, ZERO, ONE)

    require(matrix_add(Q0, Q1) == I2, "Source-flux projectors are incomplete")
    require(matrix_mul(Q1, Q1) == Q1, "Unit-flux projector is not idempotent")
    require(matrix_mul(write_unitary, conjugate_transpose(write_unitary)) == i4, "Write is not unitary")
    require(commutator(write_unitary, source_flux) == zero4, "Write changes source flux")
    require(matrix_vector_mul(write_unitary, state_00) == state_00, "Zero-flux branch moved")
    require(matrix_vector_mul(write_unitary, state_10) == state_11, "Unit-flux branch did not write")

    written = matrix_vector_mul(write_unitary, state_10)
    phase_written = matrix_vector_mul(active_phase_flipped, state_10)
    require(density(written) == density(phase_written), "Identity-phase mutation changed record density")
    require(written != phase_written, "Identity-phase mutation did not change branch phase")

    out = {
        "status": "PASS_SOURCE_FLUX_WRITE_FIXED_ACTIVE_PHASE_OPEN",
        "source_flux_spectrum": [0, 1],
        "zero_flux_branch_identity": True,
        "unit_flux_branch_record_write": True,
        "source_flux_nondemolition": True,
        "integrated_record_changing_generator": "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing",
        "source_flux_conditioned_write_operator_derived": True,
        "active_branch_identity_phase_changes_record_density": False,
        "active_branch_identity_phase_changes_branch_vector": True,
        "source_conditioned_identity_phase_fixed": False,
        "complete_source_record_operator_derived": False,
        "post_closure_pointer_coefficient_derived": False,
        "source_odd_scalar_pseudoscalar_coefficient_derived": False,
        "physical_durability_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "primitive_zero_or_one_flux_record_changing_operator_only",
    }
    return out


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
