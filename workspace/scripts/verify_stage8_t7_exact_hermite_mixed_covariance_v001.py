#!/usr/bin/env python3
"""Independent factorial-form verification of the exact Hermite covariance."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.json"
MATRICES = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.npz"
OUT = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hermite_closed_form(order: int) -> tuple[int, ...]:
    coefficients = [0] * (order + 1)
    for m in range(order // 2 + 1):
        power = order - 2 * m
        coefficients[power] = (
            (-1) ** m
            * math.factorial(order)
            * 2**power
            // (math.factorial(m) * math.factorial(power))
        )
    return tuple(coefficients)


def polynomial_product(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return tuple(output)


def integral_pi_coefficient(exponents: tuple[int, int, int]) -> Fraction:
    if any(exponent % 2 for exponent in exponents):
        return Fraction(0)
    a, b, c = (exponent // 2 for exponent in exponents)
    total = a + b + c
    numerator = (
        4
        * math.factorial(total)
        * math.factorial(total + 1)
        * math.factorial(2 * a)
        * math.factorial(2 * b)
        * math.factorial(2 * c)
    )
    denominator = (
        math.factorial(2 * total + 2)
        * math.factorial(a)
        * math.factorial(b)
        * math.factorial(c)
    )
    return Fraction(numerator, denominator)


def element(
    bra: tuple[int, int, int],
    ket: tuple[int, int, int],
    direction: int,
) -> complex:
    products = tuple(
        polynomial_product(hermite_closed_form(a), hermite_closed_form(b))
        for a, b in zip(bra, ket)
    )
    pi_coefficient = Fraction(0)
    for ex, cx in enumerate(products[0]):
        for ey, cy in enumerate(products[1]):
            for ez, cz in enumerate(products[2]):
                powers = [ex, ey, ez]
                powers[direction] += 1
                pi_coefficient += (
                    cx * cy * cz * integral_pi_coefficient(tuple(powers))
                )
    degree = sum(bra) + sum(ket)
    factorial_product = (
        math.prod(math.factorial(value) for value in bra)
        * math.prod(math.factorial(value) for value in ket)
    )
    normalization = 1.0 / math.sqrt(
        math.pi * 2**degree * factorial_product
    )
    phase = (1j) ** sum(bra) * (-1j) ** sum(ket)
    return complex(phase * float(pi_coefficient) * normalization)


def direction_matrix(n: int, direction: int) -> np.ndarray:
    indices = tuple(
        (a, b, c)
        for a in range(n)
        for b in range(n)
        for c in range(n)
    )
    output = np.empty((n**3, n**3), dtype=complex)
    for row, bra in enumerate(indices):
        for column, ket in enumerate(indices):
            output[row, column] = element(bra, ket, direction)
    return output


def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    stored = np.load(MATRICES)
    checks = {}
    passed = True
    for n in (2, 4):
        errors = []
        for direction, label in enumerate(("x", "y", "z")):
            rebuilt = direction_matrix(n, direction)
            expected = stored[f"direction_n{n}_{label}"]
            error = float(np.linalg.norm(rebuilt - expected, ord=2))
            errors.append(error)
            passed = passed and error < 2e-14
        checks[str(n)] = {
            "independent_direction_operator_norm_errors": errors,
        }
    passed = (
        passed
        and primary["overall_verdict"]
        == "EXACT_HERMITE_MIXED_COVARIANCE_DERIVED"
        and primary["matrix_artifact_sha256"] == sha256(MATRICES)
    )
    result = {
        "schema": "stage8_t7_exact_hermite_mixed_covariance_verification_v001",
        "independent_formula": (
            "closed Hermite sum plus exact factorial form for I/pi"
        ),
        "checks": checks,
        "matrix_artifact_sha256": sha256(MATRICES),
        "pass": bool(passed),
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
