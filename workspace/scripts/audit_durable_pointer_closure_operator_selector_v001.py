#!/usr/bin/env python3
"""Fail-closed exact audit of the two-endpoint pointer commutant."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "durable_pointer_closure_operator_selector_v001.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)

I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
Z: Matrix = ((ONE, ZERO), (ZERO, NEG_ONE))
P0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
P1: Matrix = ((ZERO, ZERO), (ZERO, ONE))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


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
        tuple(entry(row, column) for column in range(len(right[0])))
        for row in range(len(left))
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(
        matrix_multiply(left, right),
        matrix_negate(matrix_multiply(right, left)),
    )


def flatten_real(matrix: Matrix) -> list[int]:
    return [
        component
        for row in matrix
        for entry in row
        for component in entry
    ]


def rank(columns: list[list[int]]) -> int:
    rows = [
        [Fraction(column[row]) for column in columns]
        for row in range(len(columns[0]))
    ]
    pivot_row = 0
    pivots = 0
    for column in range(len(columns)):
        candidate = next(
            (
                row
                for row in range(pivot_row, len(rows))
                if rows[row][column] != 0
            ),
            None,
        )
        if candidate is None:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        pivots += 1
    return pivots


def build_result() -> dict[str, object]:
    basis = {"I": I2, "X": X, "Y": Y, "Z": Z}
    commutator_columns = [
        flatten_real(commutator(operator, P0))
        + flatten_real(commutator(operator, P1))
        for operator in basis.values()
    ]
    commutator_rank = rank(commutator_columns)
    commutant_dimension = len(basis) - commutator_rank
    require(commutator_rank == 2, "Unexpected pointer-commutator map rank")
    require(commutant_dimension == 2, "Unexpected Hermitian pointer commutant")

    require(commutator(I2, P0) == ((ZERO, ZERO), (ZERO, ZERO)), "I fails P0")
    require(commutator(I2, P1) == ((ZERO, ZERO), (ZERO, ZERO)), "I fails P1")
    require(commutator(Z, P0) == ((ZERO, ZERO), (ZERO, ZERO)), "Z fails P0")
    require(commutator(Z, P1) == ((ZERO, ZERO), (ZERO, ZERO)), "Z fails P1")
    require(commutator(X, P0) != ((ZERO, ZERO), (ZERO, ZERO)), "X survived")
    require(commutator(Y, P0) != ((ZERO, ZERO), (ZERO, ZERO)), "Y survived")
    require(matrix_multiply(Z, Z) == I2, "Pointer contrast is not involutive")

    return {
        "status": "PASS_DURABLE_POINTER_DIRECTION_ALGEBRA_ONLY",
        "hermitian_domain_dimension": len(basis),
        "pointer_commutator_map_rank": commutator_rank,
        "hermitian_pointer_commutant_dimension": commutant_dimension,
        "commutant_basis": ["I", "Z"],
        "response_null_identity_quotient_dimension": 1,
        "public_pointer_direction": "Z_up_to_endpoint_relabeling",
        "dimensionless_pointer_contrast_square": "I",
        "nondemolition_pointer_condition_derived": False,
        "complete_closure_operator_selected": False,
        "record_write_dynamics_derived": False,
        "physical_durability_derived": False,
        "kappa_R_derived": False,
        "record_generated_source_mass_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "post_closure_pointer_direction_on_primitive_M2_factor_only",
    }


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
