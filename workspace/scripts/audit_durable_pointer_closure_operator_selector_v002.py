#!/usr/bin/env python3
"""Fail-closed exact audit of the conditional two-endpoint pointer commutant."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "durable_pointer_closure_operator_selector_v002.json"
Gaussian = tuple[int, int]
Matrix = tuple[tuple[Gaussian, ...], ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
NEG_ONE: Gaussian = (-1, 0)
I_UNIT: Gaussian = (0, 1)
NEG_I: Gaussian = (0, -1)
ZERO2: Matrix = ((ZERO, ZERO), (ZERO, ZERO))

I2: Matrix = ((ONE, ZERO), (ZERO, ONE))
X: Matrix = ((ZERO, ONE), (ONE, ZERO))
Y: Matrix = ((ZERO, NEG_I), (I_UNIT, ZERO))
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


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(left, matrix_negate(right))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    def entry(row: int, column: int) -> Gaussian:
        total = ZERO
        for index in range(len(right)):
            total = g_add(total, g_multiply(left[row][index], right[index][column]))
        return total

    return tuple(
        tuple(entry(row, column) for column in range(len(right[0])))
        for row in range(len(left))
    )


def conjugate_transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple((matrix[column][row][0], -matrix[column][row][1]) for column in range(len(matrix)))
        for row in range(len(matrix[0]))
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


def exact_rank(columns: list[list[int]]) -> int:
    require(bool(columns), "Rank requires at least one column")
    require(all(len(column) == len(columns[0]) for column in columns), "Ragged columns")
    rows = [
        [Fraction(column[row]) for column in columns]
        for row in range(len(columns[0]))
    ]
    pivot_row = 0
    pivots = 0
    for column in range(len(columns)):
        candidate = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column] != 0),
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
    require(P0 == conjugate_transpose(P0), "P0 is not Hermitian")
    require(P1 == conjugate_transpose(P1), "P1 is not Hermitian")
    require(matrix_multiply(P0, P0) == P0, "P0 is not idempotent")
    require(matrix_multiply(P1, P1) == P1, "P1 is not idempotent")
    require(matrix_multiply(P0, P1) == ZERO2, "P0 and P1 are not orthogonal")
    require(matrix_multiply(P1, P0) == ZERO2, "P1 and P0 are not orthogonal")
    require(matrix_add(P0, P1) == I2, "Endpoint projectors are not complete")
    require(P0 != ZERO2 and P1 != ZERO2 and P0 != P1, "Endpoints are not distinct rank-one sectors")

    contrast = matrix_subtract(P1, P0)
    basis = {"I": I2, "X": X, "Y": Y, "P1-P0": contrast}
    basis_rank = exact_rank([flatten_real(operator) for operator in basis.values()])
    require(basis_rank == 4, "Declared Hermitian domain basis is not independent")

    images = {
        name: flatten_real(commutator(operator, P0))
        + flatten_real(commutator(operator, P1))
        for name, operator in basis.items()
    }
    commutator_rank = exact_rank(list(images.values()))
    commutant_dimension = len(basis) - commutator_rank

    require(commutator_rank == 2, "Unexpected pointer-commutator map rank")
    require(commutant_dimension == 2, "Unexpected Hermitian pointer commutant")
    require(images["I"] == [0] * len(images["I"]), "Identity not in kernel")
    require(images["P1-P0"] == [0] * len(images["P1-P0"]), "Contrast not in kernel")
    require(images["X"] != [0] * len(images["X"]), "X incorrectly in kernel")
    require(images["Y"] != [0] * len(images["Y"]), "Y incorrectly in kernel")
    require(matrix_multiply(contrast, contrast) == I2, "Canonical contrast is not involutive")
    require(contrast[0][0] == NEG_ONE, "Sector P0 contrast eigenvalue is not -1")
    require(contrast[1][1] == ONE, "Sector P1 contrast eigenvalue is not +1")
    require(P0[0][0] == ONE and P1[1][1] == ONE, "Endpoint ordering changed")

    identity_subspace_dimension = exact_rank([flatten_real(I2)])
    require(identity_subspace_dimension == 1, "Identity equivalence subspace is not one-dimensional")
    endpoint_contrast_quotient_dimension = commutant_dimension - identity_subspace_dimension
    require(endpoint_contrast_quotient_dimension == 1, "Unexpected endpoint-contrast quotient")

    out = {
        "status": "PASS_CONDITIONAL_POINTER_COMMUTANT_CLASSIFICATION_ONLY",
        "primitive_record_algebra_input_inherited_from_sealed_authority": True,
        "endpoint_projectors_input_declared": True,
        "endpoint_projector_axioms_verified": True,
        "hermitian_domain_dimension": len(basis),
        "hermitian_domain_basis_rank": basis_rank,
        "pointer_commutator_map_rank": commutator_rank,
        "hermitian_pointer_commutant_dimension": commutant_dimension,
        "commutant_basis": ["I", "P1-P0"],
        "endpoint_contrast_equivalence_adopted": True,
        "endpoint_contrast_quotient_dimension": endpoint_contrast_quotient_dimension,
        "canonical_contrast_representative_defined": True,
        "canonical_contrast_representative": "P1_minus_P0",
        "canonical_contrast_square": "I",
        "identity_quotient_scope": "relative_endpoint_contrast_only",
        "post_closure_invariance_commutator_equivalence_derived": True,
        "physical_post_closure_invariance_realized": False,
        "physical_contrast_normalization_derived": False,
        "physical_pointer_operator_selected": False,
        "common_source_term_excluded": False,
        "source_scalar_embedding_selected": False,
        "complete_closure_operator_selected": False,
        "record_write_dynamics_derived": False,
        "physical_durability_derived": False,
        "kappa_I_derived": False,
        "kappa_Z_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "scope": "conditional_post_closure_commutant_on_primitive_M2_factor_only",
    }
    required_keys = {
        "status",
        "primitive_record_algebra_input_inherited_from_sealed_authority",
        "endpoint_projectors_input_declared",
        "endpoint_projector_axioms_verified",
        "hermitian_domain_dimension",
        "hermitian_domain_basis_rank",
        "pointer_commutator_map_rank",
        "hermitian_pointer_commutant_dimension",
        "commutant_basis",
        "endpoint_contrast_equivalence_adopted",
        "endpoint_contrast_quotient_dimension",
        "canonical_contrast_representative_defined",
        "canonical_contrast_representative",
        "canonical_contrast_square",
        "identity_quotient_scope",
        "post_closure_invariance_commutator_equivalence_derived",
        "physical_post_closure_invariance_realized",
        "physical_contrast_normalization_derived",
        "physical_pointer_operator_selected",
        "common_source_term_excluded",
        "source_scalar_embedding_selected",
        "complete_closure_operator_selected",
        "record_write_dynamics_derived",
        "physical_durability_derived",
        "kappa_I_derived",
        "kappa_Z_derived",
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
