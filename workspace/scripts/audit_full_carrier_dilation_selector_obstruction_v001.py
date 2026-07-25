#!/usr/bin/env python3
"""Exact reduced-carrier selector obstruction audit."""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "full_carrier_dilation_selector_obstruction_v001.json"

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
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}

WEIGHT_SEARCH_BOUND = 2
UNIT_EDGE_WEIGHTS = (1, 1, 1)
SOURCE_DOUBLED_WEIGHTS = (2, 1, -1)

RESULT_SCHEMA = {
    "status": str,
    "reduced_three_factor_carrier_declared": bool,
    "complete_physical_carrier_derived": bool,
    "full_reduced_Pauli_product_dimension": int,
    "odd_odd_reduced_operator_dimension": int,
    "source_record_only_kernel_dimension": int,
    "unit_weight_candidate_weights": list,
    "unit_weight_candidate_kernel_dimension": int,
    "unit_weight_candidate_writes_edge": bool,
    "source_doubled_candidate_weights": list,
    "source_doubled_candidate_kernel_dimension": int,
    "source_doubled_candidate_writes_edge": bool,
    "source_doubled_grading_weights_derived": bool,
    "neighbor_weight_search_bound": int,
    "neighbor_weight_nullity_distribution": dict,
    "neighbor_weight_assignments_with_same_nullity": int,
    "nullity_two_weight_assignments": list,
    "schur_witness_gap_1_at_zero": str,
    "schur_witness_gap_2_at_zero": str,
    "schur_self_energy_deforms_with_unfixed_gap": bool,
    "unique_full_carrier_coupling_ray_derived": bool,
    "axial_Ward_identity_with_inflow_derived": bool,
    "closure_sector_spectrum_derived": bool,
    "record_onset_to_source_self_energy_ratio_derived": bool,
    "complete_source_record_environment_operator_derived": bool,
    "physical_durability_derived": bool,
    "record_generated_source_mass_derived": bool,
    "spectral_evaluation_authorized": bool,
    "coupling_evaluation_authorized": bool,
    "alpha_computed": bool,
    "proof_authorized": bool,
    "scope": str,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return (
            set(left) == set(right)
            and all(strict_equal(left[key], right[key]) for key in left)
        )
    if isinstance(left, list):
        return (
            len(left) == len(right)
            and all(strict_equal(a, b) for a, b in zip(left, right))
        )
    return left == right


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in out, f"Duplicate JSON key: {key}")
        out[key] = value
    return out


def load_result(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Unable to load stored result: {error}") from error
    require(type(value) is dict, "Stored result is not an object")
    require(set(value) == set(RESULT_SCHEMA), "Stored result schema drift")
    require(
        all(type(value[key]) is RESULT_SCHEMA[key] for key in RESULT_SCHEMA),
        "Stored result type drift",
    )
    return value


def g_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def g_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(len(left)))
        for row in range(len(left))
    )


def matrix_neg(matrix: Matrix) -> Matrix:
    return tuple(tuple((-entry[0], -entry[1]) for entry in row) for row in matrix)


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(left, matrix_neg(right))


def matrix_scale(value: int, matrix: Matrix) -> Matrix:
    return tuple(
        tuple((value * entry[0], value * entry[1]) for entry in row)
        for row in matrix
    )


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    def entry(row: int, column: int) -> Gaussian:
        total = ZERO
        for index in range(len(right)):
            total = g_add(total, g_mul(left[row][index], right[index][column]))
        return total

    return tuple(
        tuple(entry(row, column) for column in range(len(right[0])))
        for row in range(len(left))
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            g_mul(left[lr][lc], right[rr][rc])
            for lc in range(len(left[0]))
            for rc in range(len(right[0]))
        )
        for lr in range(len(left))
        for rr in range(len(right))
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_sub(matrix_mul(left, right), matrix_mul(right, left))


def anticommutator(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(matrix_mul(left, right), matrix_mul(right, left))


def flatten_real(matrix: Matrix) -> list[int]:
    return [
        component
        for row in matrix
        for entry in row
        for component in entry
    ]


def zero_matrix(size: int) -> Matrix:
    return tuple(tuple(ZERO for _ in range(size)) for _ in range(size))


def columns_to_rows(columns: list[list[int]]) -> list[list[Fraction]]:
    require(bool(columns), "At least one column is required")
    require(
        all(len(column) == len(columns[0]) for column in columns),
        "Column height mismatch",
    )
    return [
        [Fraction(column[row]) for column in columns]
        for row in range(len(columns[0]))
    ]


def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [list(row) for row in rows]
    if not matrix:
        return matrix, []
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivots: list[int] = []
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
                    for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return matrix, pivots


def nullspace(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(rows)
    column_count = len(rows[0]) if rows else 0
    free = [column for column in range(column_count) if column not in pivots]
    vectors: list[list[Fraction]] = []
    for free_column in free:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        vectors.append(vector)
    require(
        len(pivots) + len(vectors) == column_count,
        "Rank-nullity failure",
    )
    for vector in vectors:
        require(
            all(
                sum(
                    (row[column] * vector[column] for column in range(column_count)),
                    Fraction(0),
                )
                == 0
                for row in rows
            ),
            "Returned vector is not in the nullspace",
        )
    if vectors:
        vector_rows = columns_to_rows(vectors)
        _, vector_pivots = rref(vector_rows)
        require(
            len(vector_pivots) == len(vectors),
            "Nullspace basis is linearly dependent",
        )
    return vectors


def build_odd_basis() -> tuple[list[str], list[Matrix], Matrix, Matrix, Matrix]:
    z_source = kronecker(kronecker(Z, I2), I2)
    z_record = kronecker(kronecker(I2, Z), I2)
    z_edge = kronecker(kronecker(I2, I2), Z)
    zero8 = zero_matrix(8)
    labels: list[str] = []
    operators: list[Matrix] = []
    for source, record, edge in itertools.product(PAULI, repeat=3):
        operator = kronecker(kronecker(PAULI[source], PAULI[record]), PAULI[edge])
        if (
            anticommutator(operator, z_source) == zero8
            and anticommutator(operator, z_record) == zero8
        ):
            labels.append(source + record + edge)
            operators.append(operator)
    return labels, operators, z_source, z_record, z_edge


def kernel_for_weights(
    weights: tuple[int, int, int],
    operators: list[Matrix],
    z_source: Matrix,
    z_record: Matrix,
    z_edge: Matrix,
) -> list[list[Fraction]]:
    grading = matrix_add(
        matrix_add(
            matrix_scale(weights[0], z_source),
            matrix_scale(weights[1], z_record),
        ),
        matrix_scale(weights[2], z_edge),
    )
    rows = columns_to_rows(
        [flatten_real(commutator(operator, grading)) for operator in operators]
    )
    return nullspace(rows)


def linear_operator(
    coefficients: list[Fraction],
    operators: list[Matrix],
) -> Matrix:
    require(len(coefficients) == len(operators), "Operator coefficient mismatch")
    size = len(operators[0])
    out = zero_matrix(size)
    for coefficient, operator in zip(coefficients, operators):
        require(coefficient.denominator == 1, "Nonintegral diagnostic coefficient")
        out = matrix_add(out, matrix_scale(coefficient.numerator, operator))
    return out


def edge_projectors() -> tuple[Matrix, Matrix]:
    p0: Matrix = ((ONE, ZERO), (ZERO, ZERO))
    p1: Matrix = ((ZERO, ZERO), (ZERO, ONE))
    return (
        kronecker(kronecker(I2, I2), p0),
        kronecker(kronecker(I2, I2), p1),
    )


def edge_offdiagonal_part(operator: Matrix) -> Matrix:
    p0, p1 = edge_projectors()
    return matrix_add(
        matrix_mul(matrix_mul(p0, operator), p1),
        matrix_mul(matrix_mul(p1, operator), p0),
    )


def kernel_has_edge_flip(
    kernel: list[list[Fraction]],
    operators: list[Matrix],
) -> bool:
    zero8 = zero_matrix(8)
    return any(
        edge_offdiagonal_part(linear_operator(vector, operators)) != zero8
        for vector in kernel
    )


def primitive_weight_triples(bound: int) -> list[tuple[int, int, int]]:
    triples: list[tuple[int, int, int]] = []
    for triple in itertools.product(range(-bound, bound + 1), repeat=3):
        if triple == (0, 0, 0):
            continue
        gcd = math.gcd(math.gcd(abs(triple[0]), abs(triple[1])), abs(triple[2]))
        if gcd != 1:
            continue
        first_nonzero = next(value for value in triple if value != 0)
        if first_nonzero < 0:
            continue
        triples.append(triple)
    return triples


def schur_public_scalar(
    block: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    z_value: Fraction,
) -> Fraction:
    require(block[0][1] == block[1][0], "Schur block is not Hermitian")
    denominator = z_value - block[1][1]
    require(denominator != 0, "Schur complement is singular")
    return block[0][0] + block[0][1] * block[1][0] / denominator


def build_result() -> dict[str, object]:
    require(WEIGHT_SEARCH_BOUND == 2, "Neighbor search bound drift")
    labels, operators, z_source, z_record, z_edge = build_odd_basis()
    require(len(labels) == 16, "Unexpected odd/odd basis dimension")
    require(
        labels
        == [
            source + record + edge
            for source in ("X", "Y")
            for record in ("X", "Y")
            for edge in ("I", "X", "Y", "Z")
        ],
        "Odd/odd basis ordering drift",
    )

    source_record_kernel = kernel_for_weights(
        (1, 1, 0), operators, z_source, z_record, z_edge
    )
    unit_edge_kernel = kernel_for_weights(
        UNIT_EDGE_WEIGHTS, operators, z_source, z_record, z_edge
    )
    source_doubled_kernel = kernel_for_weights(
        SOURCE_DOUBLED_WEIGHTS, operators, z_source, z_record, z_edge
    )
    require(len(source_record_kernel) == 8, "Wrong source-record kernel dimension")
    require(len(unit_edge_kernel) == 4, "Wrong unit-edge kernel dimension")
    require(
        not kernel_has_edge_flip(unit_edge_kernel, operators),
        "Unit-edge kernel unexpectedly writes the edge",
    )
    require(len(source_doubled_kernel) == 2, "Wrong source-doubled kernel dimension")
    require(
        kernel_has_edge_flip(source_doubled_kernel, operators),
        "Source-doubled kernel does not write the edge",
    )

    distribution: dict[int, int] = {}
    nullity_two_weights: list[list[int]] = []
    for weights in primitive_weight_triples(WEIGHT_SEARCH_BOUND):
        dimension = len(
            kernel_for_weights(weights, operators, z_source, z_record, z_edge)
        )
        distribution[dimension] = distribution.get(dimension, 0) + 1
        if dimension == 2:
            nullity_two_weights.append(list(weights))
    expected_distribution = {0: 22, 2: 8, 4: 12, 6: 4, 8: 3}
    require(distribution == expected_distribution, "Weight-nullity distribution drift")
    require(
        list(SOURCE_DOUBLED_WEIGHTS) in nullity_two_weights,
        "Selected diagnostic weights absent from nullity-two neighbors",
    )

    g = Fraction(1)
    z_value = Fraction(0)
    sigma_gap_1 = schur_public_scalar(
        ((Fraction(0), g), (g, Fraction(1))),
        z_value,
    )
    sigma_gap_2 = schur_public_scalar(
        ((Fraction(0), g), (g, Fraction(2))),
        z_value,
    )
    require(sigma_gap_1 == -1, "Wrong first Schur witness")
    require(sigma_gap_2 == Fraction(-1, 2), "Wrong second Schur witness")
    require(sigma_gap_1 != sigma_gap_2, "Schur witnesses do not differ")

    out: dict[str, object] = {
        "status": "PASS_REDUCED_DILATION_SELECTOR_OBSTRUCTION_FULL_OPERATOR_OPEN",
        "reduced_three_factor_carrier_declared": True,
        "complete_physical_carrier_derived": False,
        "full_reduced_Pauli_product_dimension": 64,
        "odd_odd_reduced_operator_dimension": len(labels),
        "source_record_only_kernel_dimension": len(source_record_kernel),
        "unit_weight_candidate_weights": list(UNIT_EDGE_WEIGHTS),
        "unit_weight_candidate_kernel_dimension": len(unit_edge_kernel),
        "unit_weight_candidate_writes_edge": kernel_has_edge_flip(
            unit_edge_kernel, operators
        ),
        "source_doubled_candidate_weights": list(SOURCE_DOUBLED_WEIGHTS),
        "source_doubled_candidate_kernel_dimension": len(source_doubled_kernel),
        "source_doubled_candidate_writes_edge": kernel_has_edge_flip(
            source_doubled_kernel, operators
        ),
        "source_doubled_grading_weights_derived": False,
        "neighbor_weight_search_bound": WEIGHT_SEARCH_BOUND,
        "neighbor_weight_nullity_distribution": {
            str(key): value for key, value in sorted(distribution.items())
        },
        "neighbor_weight_assignments_with_same_nullity": len(nullity_two_weights),
        "nullity_two_weight_assignments": nullity_two_weights,
        "schur_witness_gap_1_at_zero": str(sigma_gap_1),
        "schur_witness_gap_2_at_zero": str(sigma_gap_2),
        "schur_self_energy_deforms_with_unfixed_gap": sigma_gap_1 != sigma_gap_2,
        "unique_full_carrier_coupling_ray_derived": False,
        "axial_Ward_identity_with_inflow_derived": False,
        "closure_sector_spectrum_derived": False,
        "record_onset_to_source_self_energy_ratio_derived": False,
        "complete_source_record_environment_operator_derived": False,
        "physical_durability_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "exact_reduced_three_factor_identifiability_obstruction_only",
    }
    require(set(out) == set(RESULT_SCHEMA), "Result schema drift")
    require(
        all(type(out[key]) is RESULT_SCHEMA[key] for key in RESULT_SCHEMA),
        "Result type drift",
    )
    return out


def main() -> None:
    out = build_result()
    stored = load_result(RESULT)
    require(strict_equal(stored, out), "Stored result parity failure")
    print(out["status"])


if __name__ == "__main__":
    main()
