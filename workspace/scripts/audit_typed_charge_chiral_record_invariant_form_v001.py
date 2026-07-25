#!/usr/bin/env python3
"""Exact typed-carrier invariant-form audit."""

from __future__ import annotations

from fractions import Fraction
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "TYPED_CHARGE_CHIRAL_RECORD_INVARIANT_FORM_GATE_V001.md"
RESULT = ROOT / "results" / "typed_charge_chiral_record_invariant_form_v001.json"

Matrix = tuple[tuple[Fraction, ...], ...]
Gaussian = tuple[Fraction, Fraction]
GMatrix = tuple[tuple[Gaussian, ...], ...]

CANONICAL_J2: Matrix = (
    (Fraction(0), Fraction(-1)),
    (Fraction(1), Fraction(0)),
)
ZERO2: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
SWAP_PLANES: Matrix = (
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
)

G_ZERO: Gaussian = (Fraction(0), Fraction(0))
G_ONE: Gaussian = (Fraction(1), Fraction(0))
G_NEG_ONE: Gaussian = (Fraction(-1), Fraction(0))
G_I: Gaussian = (Fraction(0), Fraction(1))
G_NEG_I: Gaussian = (Fraction(0), Fraction(-1))
G_I2: GMatrix = ((G_ONE, G_ZERO), (G_ZERO, G_ONE))
G_X: GMatrix = ((G_ZERO, G_ONE), (G_ONE, G_ZERO))
G_Y: GMatrix = ((G_ZERO, G_NEG_I), (G_I, G_ZERO))
G_Z: GMatrix = ((G_ONE, G_ZERO), (G_ZERO, G_NEG_ONE))
G_Q: GMatrix = ((G_ZERO, G_ZERO), (G_ZERO, G_ONE))
FACTOR_ORDER = ("flux", "chirality", "record")
CHIRAL_REPHASE_SCALE = Fraction(1, 2)
RECORD_REPHASE_SCALE = Fraction(1, 2)

RESULT_SCHEMA = {
    "status": str,
    "typed_flux_chirality_record_factor_declared": bool,
    "complete_physical_carrier_derived": bool,
    "typed_candidate_operator_dimension": int,
    "vector_U1_neutrality_verified": bool,
    "symmetric_form_domain_dimension": int,
    "independent_rephase_constraint_rank": int,
    "independent_rephase_invariant_form_dimension": int,
    "invariant_form_has_independent_mass_and_record_weights": bool,
    "swap_extended_constraint_rank": int,
    "chirality_record_swap_reduces_form_dimension_to_one": bool,
    "chirality_record_swap_derived": bool,
    "single_superconnection_forces_common_normalization": bool,
    "unique_full_carrier_coupling_ray_derived": bool,
    "complete_source_record_environment_operator_derived": bool,
    "record_onset_to_source_self_energy_ratio_derived": bool,
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


def load_result() -> dict[str, Any]:
    try:
        value = json.loads(
            RESULT.read_text(encoding="utf-8"),
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


def g_conj(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def g_dagger(matrix: GMatrix) -> GMatrix:
    return tuple(
        tuple(g_conj(matrix[column][row]) for column in range(len(matrix)))
        for row in range(len(matrix[0]))
    )


def g_matrix_add(left: GMatrix, right: GMatrix) -> GMatrix:
    return tuple(
        tuple(g_add(left[row][column], right[row][column]) for column in range(len(left)))
        for row in range(len(left))
    )


def g_matrix_neg(matrix: GMatrix) -> GMatrix:
    return tuple(
        tuple((-entry[0], -entry[1]) for entry in row)
        for row in matrix
    )


def g_matrix_sub(left: GMatrix, right: GMatrix) -> GMatrix:
    return g_matrix_add(left, g_matrix_neg(right))


def g_matrix_scale(value: Gaussian, matrix: GMatrix) -> GMatrix:
    return tuple(
        tuple(g_mul(value, entry) for entry in row)
        for row in matrix
    )


def g_matrix_mul(left: GMatrix, right: GMatrix) -> GMatrix:
    def entry(row: int, column: int) -> Gaussian:
        total = G_ZERO
        for index in range(len(right)):
            total = g_add(total, g_mul(left[row][index], right[index][column]))
        return total

    return tuple(
        tuple(entry(row, column) for column in range(len(right[0])))
        for row in range(len(left))
    )


def g_kronecker(left: GMatrix, right: GMatrix) -> GMatrix:
    return tuple(
        tuple(
            g_mul(left[lr][lc], right[rr][rc])
            for lc in range(len(left[0]))
            for rc in range(len(right[0]))
        )
        for lr in range(len(left))
        for rr in range(len(right))
    )


def g_commutator(left: GMatrix, right: GMatrix) -> GMatrix:
    return g_matrix_sub(g_matrix_mul(left, right), g_matrix_mul(right, left))


def g_flatten_real(matrix: GMatrix) -> list[Fraction]:
    return [
        component
        for row in matrix
        for entry in row
        for component in entry
    ]


def g_zero_matrix(size: int) -> GMatrix:
    return tuple(tuple(G_ZERO for _ in range(size)) for _ in range(size))


def g_trace(matrix: GMatrix) -> Gaussian:
    total = G_ZERO
    for index in range(len(matrix)):
        total = g_add(total, matrix[index][index])
    return total


def validate_pauli_triple() -> None:
    for label, matrix in (("X", G_X), ("Y", G_Y), ("Z", G_Z)):
        require(g_dagger(matrix) == matrix, f"{label} is not Hermitian")
        require(
            g_matrix_mul(matrix, matrix) == G_I2,
            f"{label} is not unit-normalized",
        )
        require(g_trace(matrix) == G_ZERO, f"{label} is not traceless")
    require(
        g_matrix_mul(G_X, G_Y) == g_matrix_scale(G_I, G_Z),
        "XY is not iZ",
    )
    require(
        g_matrix_mul(G_Y, G_Z) == g_matrix_scale(G_I, G_X),
        "YZ is not iX",
    )
    require(
        g_matrix_mul(G_Z, G_X) == g_matrix_scale(G_I, G_Y),
        "ZX is not iY",
    )


def block_diagonal(left: Matrix, right: Matrix) -> Matrix:
    left_size = len(left)
    right_size = len(right)
    return tuple(
        tuple(
            (
                left[row][column]
                if row < left_size and column < left_size
                else right[row - left_size][column - left_size]
                if row >= left_size and column >= left_size
                else Fraction(0)
            )
            for column in range(left_size + right_size)
        )
        for row in range(left_size + right_size)
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[column][row] for column in range(len(matrix)))
        for row in range(len(matrix[0]))
    )


def identity(size: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left)))
        for row in range(len(left))
    )


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(len(left)))
        for row in range(len(left))
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (
                    left[row][index] * right[index][column]
                    for index in range(len(right))
                ),
                Fraction(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def symmetric_basis(size: int) -> list[Matrix]:
    basis: list[Matrix] = []
    for row in range(size):
        for column in range(row, size):
            basis.append(
                tuple(
                    tuple(
                        Fraction(
                            int((r, c) == (row, column))
                            + int(row != column and (r, c) == (column, row))
                        )
                        for c in range(size)
                    )
                    for r in range(size)
                )
            )
    return basis


def flatten(matrix: Matrix) -> list[Fraction]:
    return [entry for row in matrix for entry in row]


def columns_to_rows(columns: list[list[Fraction]]) -> list[list[Fraction]]:
    require(bool(columns), "At least one column is required")
    return [
        [column[row] for column in columns]
        for row in range(len(columns[0]))
    ]


def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [list(row) for row in rows]
    pivots: list[int] = []
    pivot_row = 0
    if not matrix:
        return matrix, pivots
    for column in range(len(matrix[0])):
        candidate = next(
            (
                row
                for row in range(pivot_row, len(matrix))
                if matrix[row][column] != 0
            ),
            None,
        )
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
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
        if pivot_row == len(matrix):
            break
    return matrix, pivots


def nullspace(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(rows)
    column_count = len(rows[0]) if rows else 0
    free_columns = [column for column in range(column_count) if column not in pivots]
    out: list[list[Fraction]] = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        out.append(vector)
    return out


def invariant_map(generator: Matrix, form: Matrix) -> Matrix:
    return add(multiply(transpose(generator), form), multiply(form, generator))


def swap_map(swap: Matrix, form: Matrix) -> Matrix:
    return subtract(multiply(multiply(transpose(swap), form), swap), form)


def invariant_form_kernel(
    generators: tuple[Matrix, ...],
    include_swap: bool,
) -> tuple[int, list[list[Fraction]]]:
    forms = symmetric_basis(4)
    columns: list[list[Fraction]] = []
    for form in forms:
        constraints: list[Fraction] = []
        for generator in generators:
            constraints.extend(flatten(invariant_map(generator, form)))
        if include_swap:
            constraints.extend(flatten(swap_map(SWAP_PLANES, form)))
        columns.append(constraints)
    rows = columns_to_rows(columns)
    _, pivots = rref(rows)
    return len(pivots), nullspace(rows)


def linear_combination(
    coefficients: list[Fraction],
    basis: list[Matrix],
) -> Matrix:
    require(len(coefficients) == len(basis), "Coefficient count mismatch")
    size = len(basis[0])
    return tuple(
        tuple(
            sum(
                (
                    coefficient * form[row][column]
                    for coefficient, form in zip(coefficients, basis)
                ),
                Fraction(0),
            )
            for column in range(size)
        )
        for row in range(size)
    )


def coordinates_in_operator_basis(
    target: GMatrix,
    basis: list[GMatrix],
) -> list[Fraction]:
    columns = [g_flatten_real(operator) for operator in basis]
    target_column = g_flatten_real(target)
    rows = [
        [column[row] for column in columns] + [target_column[row]]
        for row in range(len(target_column))
    ]
    reduced, pivots = rref(rows)
    require(pivots[: len(basis)] == list(range(len(basis))), "Operator basis lost rank")
    require(
        not any(
            all(entry == 0 for entry in row[:-1]) and row[-1] != 0
            for row in reduced
        ),
        "Operator is outside the typed basis",
    )
    solution = [Fraction(0) for _ in basis]
    for row_index, pivot in enumerate(pivots):
        if pivot < len(basis):
            solution[pivot] = reduced[row_index][-1]
    reconstructed = g_zero_matrix(len(target))
    for coefficient, operator in zip(solution, basis):
        require(coefficient.denominator == 1, "Nonintegral operator coordinate")
        reconstructed = g_matrix_add(
            reconstructed,
            g_matrix_scale((coefficient, Fraction(0)), operator),
        )
    require(reconstructed == target, "Operator-coordinate reconstruction failed")
    return solution


def coefficient_action(
    actions: list[GMatrix],
    basis: list[GMatrix],
) -> Matrix:
    columns = [coordinates_in_operator_basis(action, basis) for action in actions]
    return tuple(
        tuple(columns[column][row] for column in range(len(columns)))
        for row in range(len(columns[0]))
    )


def typed_operator_basis() -> tuple[GMatrix, GMatrix, GMatrix, GMatrix, GMatrix]:
    require(
        FACTOR_ORDER == ("flux", "chirality", "record"),
        "Typed factor-order declaration drift",
    )
    charge = g_kronecker(g_kronecker(G_Q, G_I2), G_I2)
    mass_x = g_kronecker(g_kronecker(G_Q, G_X), G_I2)
    mass_y = g_kronecker(g_kronecker(G_Q, G_Y), G_I2)
    write_x = g_kronecker(g_kronecker(G_Q, G_I2), G_X)
    write_y = g_kronecker(g_kronecker(G_Q, G_I2), G_Y)
    return charge, mass_x, mass_y, write_x, write_y


def build_result() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8")
    required_note_lines = (
        "typed_flux_chirality_record_factor_declared = true",
        "complete_physical_carrier_derived = false",
        "independent_rephase_invariant_form_dimension = 2",
        "chirality_record_swap_derived = false",
        "single_superconnection_forces_common_normalization = false",
        "unique_full_carrier_coupling_ray_derived = false",
        "complete_source_record_environment_operator_derived = false",
        "record_generated_source_mass_derived = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    require(
        all(line in note for line in required_note_lines),
        "Gate note is missing required scope/status lines",
    )
    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    require(
        not any(pattern.search(note) for pattern in forbidden),
        "Target-number literal found in typed gate",
    )

    validate_pauli_triple()
    expected_q = g_matrix_scale(
        (Fraction(1, 2), Fraction(0)),
        g_matrix_sub(G_I2, G_Z),
    )
    require(G_Q == expected_q, "Flux projector is not (I-Z)/2")
    require(g_dagger(G_Q) == G_Q, "Flux projector is not Hermitian")
    require(g_matrix_mul(G_Q, G_Q) == G_Q, "Flux projector is not idempotent")
    require(g_trace(G_Q) == G_ONE, "Flux projector is not rank one")

    charge, mass_x, mass_y, write_x, write_y = typed_operator_basis()
    typed_operators = [mass_x, mass_y, write_x, write_y]
    require(
        all(g_dagger(operator) == operator for operator in typed_operators),
        "Typed mass/write operator is not Hermitian",
    )
    zero8 = g_zero_matrix(8)
    require(
        all(g_commutator(charge, operator) == zero8 for operator in typed_operators),
        "Typed candidate operator is not vector-U(1) neutral",
    )
    typed_rows = columns_to_rows(
        [g_flatten_real(operator) for operator in typed_operators]
    )
    _, typed_pivots = rref(typed_rows)
    require(len(typed_pivots) == 4, "Typed operator planes are not independent")

    chiral_generator = g_matrix_scale(
        (CHIRAL_REPHASE_SCALE, Fraction(0)),
        g_kronecker(g_kronecker(G_I2, G_Z), G_I2),
    )
    record_generator = g_matrix_scale(
        (RECORD_REPHASE_SCALE, Fraction(0)),
        g_kronecker(g_kronecker(G_I2, G_I2), G_Z),
    )
    minus_i = (Fraction(0), Fraction(-1))
    chiral_actions = [
        g_matrix_scale(minus_i, g_commutator(chiral_generator, operator))
        for operator in typed_operators
    ]
    record_actions = [
        g_matrix_scale(minus_i, g_commutator(record_generator, operator))
        for operator in typed_operators
    ]
    require(
        chiral_actions == [mass_y, g_matrix_neg(mass_x), zero8, zero8],
        "Typed chiral rephase action is wrong",
    )
    require(
        record_actions == [zero8, zero8, write_y, g_matrix_neg(write_x)],
        "Typed record rephase action is wrong",
    )

    a_chiral = coefficient_action(chiral_actions, typed_operators)
    a_record = coefficient_action(record_actions, typed_operators)
    require(
        a_chiral == block_diagonal(CANONICAL_J2, ZERO2),
        "Derived chiral coefficient action is not J2 direct-sum zero",
    )
    require(
        a_record == block_diagonal(ZERO2, CANONICAL_J2),
        "Derived record coefficient action is not zero direct-sum J2",
    )

    identity4 = identity(4)
    require(
        multiply(SWAP_PLANES, SWAP_PLANES) == identity4,
        "Plane swap is not an involution",
    )
    require(
        multiply(transpose(SWAP_PLANES), SWAP_PLANES) == identity4,
        "Plane swap is not orthogonal",
    )
    require(
        multiply(multiply(transpose(SWAP_PLANES), a_chiral), SWAP_PLANES)
        == a_record,
        "Plane swap does not send chiral action to record action",
    )
    require(
        multiply(multiply(transpose(SWAP_PLANES), a_record), SWAP_PLANES)
        == a_chiral,
        "Plane swap does not send record action to chiral action",
    )
    forms = symmetric_basis(4)
    require(len(forms) == 10, "Wrong symmetric-form domain dimension")

    rank, kernel = invariant_form_kernel((a_chiral, a_record), include_swap=False)
    require(rank == 8, "Wrong independent-rephase constraint rank")
    require(len(kernel) == 2, "Wrong independent-rephase invariant nullity")
    kernel_forms = [linear_combination(vector, forms) for vector in kernel]
    expected_mass = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    )
    expected_record = (
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )
    combined = columns_to_rows(
        [flatten(form) for form in kernel_forms + [expected_mass, expected_record]]
    )
    _, combined_pivots = rref(combined)
    require(len(combined_pivots) == 2, "Invariant kernel differs from two plane norms")

    swap_rank, swap_kernel = invariant_form_kernel(
        (a_chiral, a_record), include_swap=True
    )
    require(swap_rank == 9, "Wrong swap-extended constraint rank")
    require(len(swap_kernel) == 1, "Swap does not reduce invariant nullity to one")

    out: dict[str, object] = {
        "status": "PASS_TYPED_INVARIANT_FORMS_TWO_WEIGHTS_COMMON_NORM_OPEN",
        "typed_flux_chirality_record_factor_declared": True,
        "complete_physical_carrier_derived": False,
        "typed_candidate_operator_dimension": len(typed_pivots),
        "vector_U1_neutrality_verified": True,
        "symmetric_form_domain_dimension": len(forms),
        "independent_rephase_constraint_rank": rank,
        "independent_rephase_invariant_form_dimension": len(kernel),
        "invariant_form_has_independent_mass_and_record_weights": True,
        "swap_extended_constraint_rank": swap_rank,
        "chirality_record_swap_reduces_form_dimension_to_one": len(swap_kernel) == 1,
        "chirality_record_swap_derived": False,
        "single_superconnection_forces_common_normalization": False,
        "unique_full_carrier_coupling_ray_derived": False,
        "complete_source_record_environment_operator_derived": False,
        "record_onset_to_source_self_energy_ratio_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "exact_invariant_forms_on_declared_typed_reduced_carrier_only",
    }
    required_keys = {
        "status",
        "typed_flux_chirality_record_factor_declared",
        "complete_physical_carrier_derived",
        "typed_candidate_operator_dimension",
        "vector_U1_neutrality_verified",
        "symmetric_form_domain_dimension",
        "independent_rephase_constraint_rank",
        "independent_rephase_invariant_form_dimension",
        "invariant_form_has_independent_mass_and_record_weights",
        "swap_extended_constraint_rank",
        "chirality_record_swap_reduces_form_dimension_to_one",
        "chirality_record_swap_derived",
        "single_superconnection_forces_common_normalization",
        "unique_full_carrier_coupling_ray_derived",
        "complete_source_record_environment_operator_derived",
        "record_onset_to_source_self_energy_ratio_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
        "scope",
    }
    require(set(out) == required_keys == set(RESULT_SCHEMA), "Result schema drift")
    require(
        all(type(out[key]) is RESULT_SCHEMA[key] for key in RESULT_SCHEMA),
        "Result type drift",
    )
    return out


def main() -> None:
    out = build_result()
    stored = load_result()
    require(strict_equal(stored, out), "Stored result parity failure")
    print(out["status"])


if __name__ == "__main__":
    main()
