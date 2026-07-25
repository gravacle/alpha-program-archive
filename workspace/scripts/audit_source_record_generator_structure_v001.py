#!/usr/bin/env python3
"""Exact Gaussian-integer audit of the minimal source-record operator space."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_record_generator_structure_v001.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(len(left)))
        for row in range(len(left))
    )


def matrix_negate(matrix: Matrix) -> Matrix:
    return tuple(
        tuple((-entry[0], -entry[1]) for entry in row)
        for row in matrix
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(left, matrix_negate(right))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    def entry(row: int, column: int) -> Gaussian:
        total = ZERO
        for index in range(len(right)):
            total = g_add(
                total,
                g_multiply(left[row][index], right[index][column]),
            )
        return total

    return tuple(
        tuple(
            entry(row, column)
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            g_multiply(
                left[left_row][left_column],
                right[right_row][right_column],
            )
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_subtract(matrix_multiply(left, right), matrix_multiply(right, left))


def anticommutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matrix_multiply(left, right), matrix_multiply(right, left))


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(size)) for _ in range(size))


IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
Z: Matrix = ((ONE, ZERO), (ZERO, NEG_ONE))


def build_result() -> dict[str, object]:
    z_source = kronecker(Z, IDENTITY)
    z_record = kronecker(IDENTITY, Z)
    z_total = matrix_add(z_source, z_record)

    basis = {
        "XX": kronecker(X, X),
        "XY": kronecker(X, Y),
        "YX": kronecker(Y, X),
        "YY": kronecker(Y, Y),
    }
    zero = zero_matrix(4)
    assert all(anticommutator(operator, z_source) == zero for operator in basis.values())
    assert all(anticommutator(operator, z_record) == zero for operator in basis.values())

    exchange_real = matrix_add(basis["XX"], basis["YY"])
    exchange_imag = matrix_subtract(basis["XY"], basis["YX"])
    pair_real = matrix_subtract(basis["XX"], basis["YY"])
    pair_imag = matrix_add(basis["XY"], basis["YX"])

    assert commutator(exchange_real, z_total) == zero
    assert commutator(exchange_imag, z_total) == zero
    assert commutator(pair_real, z_total) != zero
    assert commutator(pair_imag, z_total) != zero

    return {
        "status": "PASS_SOURCE_RECORD_GENERATOR_STRUCTURE_ALGEBRA_ONLY",
        "source_odd_record_changing_basis": list(basis),
        "unconstrained_real_dimension": 4,
        "conditional_conserved_exchange_basis": [
            "XX+YY",
            "XY-YX",
        ],
        "conditional_conserved_real_dimension": 2,
        "combined_grading_conservation_derived": False,
        "exchange_magnitude_derived": False,
        "physical_record_interval_derived": False,
        "durable_record_dynamics_derived": False,
        "source_mass_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "scope": "finite_operator_structure_only",
    }


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
