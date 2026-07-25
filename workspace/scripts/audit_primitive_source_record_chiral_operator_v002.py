#!/usr/bin/env python3
"""Exact audit of the supplied scalar/pseudoscalar free chiral block.

The verifier implements Gaussian-integer multivariate polynomial algebra
locally. It checks a declared fixed-time Hermitian kernel. It does not derive
that kernel from record physics, assign its background, prove durability, or
evaluate an EM response.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "primitive_source_record_chiral_operator_v002.json"
VARIABLES = ("p0", "p1", "p2", "p3", "a", "b")
Exponent = tuple[int, ...]
GaussianInteger = tuple[int, int]


def gaussian_add(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    return left[0] + right[0], left[1] + right[1]


def gaussian_multiply(
    left: GaussianInteger, right: GaussianInteger
) -> GaussianInteger:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


class Polynomial:
    """Sparse polynomial over Gaussian integers in the six real variables."""

    def __init__(self, terms: dict[Exponent, GaussianInteger] | None = None):
        self.terms = {
            exponent: coefficient
            for exponent, coefficient in (terms or {}).items()
            if coefficient != (0, 0)
        }

    @classmethod
    def constant(cls, real: int = 0, imaginary: int = 0) -> "Polynomial":
        if real == 0 and imaginary == 0:
            return cls()
        return cls({(0,) * len(VARIABLES): (real, imaginary)})

    @classmethod
    def variable(cls, index: int) -> "Polynomial":
        exponent = [0] * len(VARIABLES)
        exponent[index] = 1
        return cls({tuple(exponent): (1, 0)})

    def __add__(self, other: "Polynomial") -> "Polynomial":
        terms = dict(self.terms)
        for exponent, coefficient in other.terms.items():
            terms[exponent] = gaussian_add(terms.get(exponent, (0, 0)), coefficient)
        return Polynomial(terms)

    def __neg__(self) -> "Polynomial":
        return Polynomial({
            exponent: (-coefficient[0], -coefficient[1])
            for exponent, coefficient in self.terms.items()
        })

    def __sub__(self, other: "Polynomial") -> "Polynomial":
        return self + (-other)

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        terms: dict[Exponent, GaussianInteger] = {}
        for left_exponent, left_coefficient in self.terms.items():
            for right_exponent, right_coefficient in other.terms.items():
                exponent = tuple(
                    left + right
                    for left, right in zip(left_exponent, right_exponent)
                )
                product = gaussian_multiply(left_coefficient, right_coefficient)
                terms[exponent] = gaussian_add(terms.get(exponent, (0, 0)), product)
        return Polynomial(terms)

    def __pow__(self, exponent: int) -> "Polynomial":
        if exponent < 0:
            raise ValueError("Polynomial exponent must be nonnegative")
        result = Polynomial.constant(1)
        for _ in range(exponent):
            result = result * self
        return result

    def conjugate(self) -> "Polynomial":
        return Polynomial({
            exponent: (coefficient[0], -coefficient[1])
            for exponent, coefficient in self.terms.items()
        })

    def evaluate(self, values: Iterable[int]) -> GaussianInteger:
        supplied = tuple(values)
        if len(supplied) != len(VARIABLES):
            raise ValueError("One real integer is required for every variable")
        total = (0, 0)
        for exponent, coefficient in self.terms.items():
            monomial = 1
            for value, power in zip(supplied, exponent):
                monomial *= value**power
            total = gaussian_add(
                total, (coefficient[0] * monomial, coefficient[1] * monomial)
            )
        return total

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Polynomial) and self.terms == other.terms


ZERO = Polynomial.constant()
ONE = Polynomial.constant(1)
I = Polynomial.constant(0, 1)


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def determinant(matrix: list[list[Polynomial]]) -> Polynomial:
    size = len(matrix)
    total = ZERO
    for permutation in itertools.permutations(range(size)):
        term = ONE
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        total = total + term if permutation_sign(permutation) == 1 else total - term
    return total


def matrix_multiply(
    left: list[list[Polynomial]], right: list[list[Polynomial]]
) -> list[list[Polynomial]]:
    rows = len(left)
    columns = len(right[0])
    inner = len(right)
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(inner)),
                ZERO,
            )
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def matrix_add(
    left: list[list[Polynomial]], right: list[list[Polynomial]]
) -> list[list[Polynomial]]:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def conjugate_transpose(
    matrix: list[list[Polynomial]],
) -> list[list[Polynomial]]:
    return [
        [matrix[column][row].conjugate() for column in range(len(matrix))]
        for row in range(len(matrix[0]))
    ]


def identity_matrix(size: int) -> list[list[Polynomial]]:
    return [
        [ONE if row == column else ZERO for column in range(size)]
        for row in range(size)
    ]


def scale_matrix(
    scalar: Polynomial, matrix: list[list[Polynomial]]
) -> list[list[Polynomial]]:
    return [[scalar * entry for entry in row] for row in matrix]


def build_kernel() -> tuple[
    list[list[Polynomial]], list[list[Polynomial]], tuple[Polynomial, ...]
]:
    p0, p1, p2, p3, a, b = tuple(
        Polynomial.variable(index) for index in range(len(VARIABLES))
    )
    phi = a + I * b
    phi_conjugate = a - I * b

    p_sigma = [
        [p0 + p3, p1 - I * p2],
        [p1 + I * p2, p0 - p3],
    ]
    p_bar_sigma = [
        [p0 - p3, -p1 + I * p2],
        [-p1 - I * p2, p0 + p3],
    ]

    kernel = [
        [p_bar_sigma[0][0], p_bar_sigma[0][1], -phi, ZERO],
        [p_bar_sigma[1][0], p_bar_sigma[1][1], ZERO, -phi],
        [-phi_conjugate, ZERO, p_sigma[0][0], p_sigma[0][1]],
        [ZERO, -phi_conjugate, p_sigma[1][0], p_sigma[1][1]],
    ]
    closure = [
        [ZERO, ZERO, phi, ZERO],
        [ZERO, ZERO, ZERO, phi],
        [phi_conjugate, ZERO, ZERO, ZERO],
        [ZERO, phi_conjugate, ZERO, ZERO],
    ]
    return kernel, closure, (p0, p1, p2, p3, a, b)


def main() -> None:
    kernel, closure, variables = build_kernel()
    p0, p1, p2, p3, a, b = variables
    p_squared = p0**2 - p1**2 - p2**2 - p3**2
    phi_squared = a**2 + b**2
    expected_determinant = (p_squared - phi_squared) ** 2

    gamma_ch = [
        [-ONE, ZERO, ZERO, ZERO],
        [ZERO, -ONE, ZERO, ZERO],
        [ZERO, ZERO, ONE, ZERO],
        [ZERO, ZERO, ZERO, ONE],
    ]
    oddness_residual = matrix_add(
        matrix_multiply(gamma_ch, closure),
        matrix_multiply(closure, gamma_ch),
    )
    square_residual = matrix_add(
        matrix_multiply(closure, closure),
        scale_matrix(-phi_squared, identity_matrix(4)),
    )

    assert determinant(kernel) == expected_determinant
    assert oddness_residual == [[ZERO] * 4 for _ in range(4)]
    assert square_residual == [[ZERO] * 4 for _ in range(4)]
    assert kernel == conjugate_transpose(kernel)

    out = {
        "status": "PASS_SUPPLIED_SCALAR_PSEUDOSCALAR_FREE_BLOCK_ALGEBRA_ONLY",
        "arithmetic": "exact_sparse_polynomial_over_gaussian_integers",
        "determinant": "(p^2 - |phi_R|^2)^2",
        "chirality_odd": True,
        "closure_square": "|phi_R|^2 I_4",
        "fixed_time_kernel_hermitian_for_real_momentum": True,
        "free_mass_shell_relation_for_supplied_background": True,
        "operator_tensor_structure_derived_from_record_principles": False,
        "phi_magnitude_assigned": False,
        "complete_source_record_generator_derived": False,
        "durable_closure_saddle_derived": False,
        "record_generated_source_mass_derived": False,
        "interacting_pole_and_residue_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "scope": "exact_free_block_algebra_for_supplied_background_only",
    }
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
