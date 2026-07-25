#!/usr/bin/env python3
"""Fail-closed exact rank audit of the reduced source-record operator space."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_record_generator_structure_v002.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)

IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
Z: Matrix = ((ONE, ZERO), (ZERO, NEG_ONE))
PAULI = {"I": IDENTITY, "X": X, "Y": Y, "Z": Z}


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
        tuple(entry(row, column) for column in range(len(right[0])))
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


def flatten_real(matrix: Matrix) -> list[int]:
    return [
        component
        for row in matrix
        for entry in row
        for component in entry
    ]


def columns_to_rows(columns: list[list[int]]) -> list[list[Fraction]]:
    require(bool(columns), "At least one column is required")
    height = len(columns[0])
    require(
        all(len(column) == height for column in columns),
        "Linear-map columns have inconsistent dimensions",
    )
    return [
        [Fraction(column[row]) for column in columns]
        for row in range(height)
    ]


def rref(
    rows: list[list[Fraction]],
) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [list(row) for row in rows]
    if not matrix:
        return matrix, []
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_columns: list[int] = []
    pivot_row = 0

    for column in range(column_count):
        candidate = next(
            (
                row
                for row in range(pivot_row, row_count)
                if matrix[row][column] != 0
            ),
            None,
        )
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor != 0:
                matrix[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(
                        matrix[row], matrix[pivot_row]
                    )
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return matrix, pivot_columns


def matrix_rank(rows: list[list[Fraction]]) -> int:
    return len(rref(rows)[1])


def nullspace(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(rows)
    column_count = len(rows[0]) if rows else 0
    free_columns = [column for column in range(column_count) if column not in pivots]
    vectors: list[list[Fraction]] = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free] = Fraction(1)
        for pivot_row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[pivot_row][free]
        vectors.append(vector)
    return vectors


def linear_combination(columns: list[list[int]], coefficients: list[int]) -> list[int]:
    require(len(columns) == len(coefficients), "Coefficient count mismatch")
    return [
        sum(
            coefficient * column[row]
            for coefficient, column in zip(coefficients, columns)
        )
        for row in range(len(columns[0]))
    ]


def build_result() -> dict[str, object]:
    labels = [left + right for left in PAULI for right in PAULI]
    operators = [
        kronecker(PAULI[label[0]], PAULI[label[1]])
        for label in labels
    ]
    z_source = kronecker(Z, IDENTITY)
    z_record = kronecker(IDENTITY, Z)
    z_total = matrix_add(z_source, z_record)

    odd_map_columns = [
        flatten_real(anticommutator(operator, z_source))
        + flatten_real(anticommutator(operator, z_record))
        for operator in operators
    ]
    odd_map_rows = columns_to_rows(odd_map_columns)
    odd_rank = matrix_rank(odd_map_rows)
    odd_nullspace = nullspace(odd_map_rows)
    require(odd_rank == 12, f"Unexpected odd-map rank: {odd_rank}")
    require(len(odd_nullspace) == 4, "Unexpected odd-map nullity")

    expected_odd_labels = ("XX", "XY", "YX", "YY")
    expected_indices = [labels.index(label) for label in expected_odd_labels]
    expected_odd_vectors = [
        [Fraction(int(index == selected)) for index in range(len(labels))]
        for selected in expected_indices
    ]
    combined_odd_span = columns_to_rows(odd_nullspace + expected_odd_vectors)
    require(
        matrix_rank(combined_odd_span) == 4,
        "Computed odd kernel differs from the expected Pauli span",
    )

    odd_operators = [operators[index] for index in expected_indices]
    conserved_columns = [
        flatten_real(commutator(operator, z_total))
        for operator in odd_operators
    ]
    conserved_rows = columns_to_rows(conserved_columns)
    conserved_rank = matrix_rank(conserved_rows)
    conserved_nullspace = nullspace(conserved_rows)
    require(conserved_rank == 2, f"Unexpected restricted rank: {conserved_rank}")
    require(len(conserved_nullspace) == 2, "Unexpected exchange nullity")

    exchange_real = [1, 0, 0, 1]
    exchange_imag = [0, 1, -1, 0]
    require(
        all(value == 0 for value in linear_combination(conserved_columns, exchange_real)),
        "XX+YY is not in the computed exchange kernel",
    )
    require(
        all(value == 0 for value in linear_combination(conserved_columns, exchange_imag)),
        "XY-YX is not in the computed exchange kernel",
    )
    exchange_span = columns_to_rows(
        conserved_nullspace
        + [
            [Fraction(value) for value in exchange_real],
            [Fraction(value) for value in exchange_imag],
        ]
    )
    require(
        matrix_rank(exchange_span) == 2,
        "Computed conserved kernel differs from the exchange span",
    )

    return {
        "status": "PASS_REDUCED_SOURCE_RECORD_GENERATOR_RANKS_ONLY",
        "full_pauli_product_domain_dimension": len(labels),
        "reduced_odd_odd_linear_map_rank": odd_rank,
        "reduced_odd_odd_kernel_dimension": len(odd_nullspace),
        "reduced_odd_odd_kernel_basis": list(expected_odd_labels),
        "conditional_restricted_commutator_rank": conserved_rank,
        "conditional_exchange_kernel_dimension": len(conserved_nullspace),
        "conditional_exchange_basis": ["XX+YY", "XY-YX"],
        "reduced_source_record_product_factor_declared": True,
        "minimal_product_carrier_derived": False,
        "complete_closure_operator_space_dimension_derived": False,
        "combined_grading_conservation_derived": False,
        "nonzero_exchange_derived": False,
        "exchange_magnitude_derived": False,
        "physical_record_interval_derived": False,
        "durable_record_dynamics_derived": False,
        "source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "exact_linear_algebra_on_declared_reduced_factor_only",
    }


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
