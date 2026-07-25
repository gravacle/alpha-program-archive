#!/usr/bin/env python3
"""Analytic Hermite-basis compression of the massless Dirac vacuum projector."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import derive_stage8_t7_hermite_galerkin_baseline_v001 as baseline


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.json"
MATRICES = ROOT / "stage8_execution/work/T07_exact_hermite_mixed_covariance.npz"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def physicists_hermite_coefficients(order: int) -> tuple[int, ...]:
    if order == 0:
        return (1,)
    if order == 1:
        return (0, 2)
    previous = [1]
    current = [0, 2]
    for n in range(1, order):
        shifted = [0] + [2 * value for value in current]
        correction = [-2 * n * value for value in previous]
        correction += [0] * (len(shifted) - len(correction))
        following = [left + right for left, right in zip(shifted, correction)]
        previous, current = current, following
    return tuple(current)


def convolve(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return tuple(output)


def monomial_over_radius(exponents: tuple[int, int, int]) -> float:
    if any(exponent % 2 for exponent in exponents):
        return 0.0
    a, b, c = (exponent // 2 for exponent in exponents)
    total = a + b + c
    return (
        math.gamma(total + 1)
        * math.gamma(a + 0.5)
        * math.gamma(b + 0.5)
        * math.gamma(c + 0.5)
        / math.gamma(total + 1.5)
    )


def direction_element(
    bra: tuple[int, int, int],
    ket: tuple[int, int, int],
    direction: int,
) -> complex:
    products = tuple(
        convolve(
            physicists_hermite_coefficients(bra_axis),
            physicists_hermite_coefficients(ket_axis),
        )
        for bra_axis, ket_axis in zip(bra, ket)
    )
    integral = 0.0
    for ex, cx in enumerate(products[0]):
        for ey, cy in enumerate(products[1]):
            for ez, cz in enumerate(products[2]):
                exponents = [ex, ey, ez]
                exponents[direction] += 1
                integral += (
                    cx
                    * cy
                    * cz
                    * monomial_over_radius(tuple(exponents))
                )
    degree_bra = sum(bra)
    degree_ket = sum(ket)
    normalization = (
        math.pi ** (-1.5)
        / math.sqrt(
            2 ** (degree_bra + degree_ket)
            * math.prod(math.factorial(value) for value in bra)
            * math.prod(math.factorial(value) for value in ket)
        )
    )
    phase = (1j) ** degree_bra * (-1j) ** degree_ket
    return complex(phase * normalization * integral)


def exact_direction_matrices(n: int) -> tuple[np.ndarray, ...]:
    indices = tuple(
        (a, b, c)
        for a in range(n)
        for b in range(n)
        for c in range(n)
    )
    output = []
    for direction in range(3):
        matrix = np.empty((n**3, n**3), dtype=complex)
        for row, bra in enumerate(indices):
            for column, ket in enumerate(indices):
                matrix[row, column] = direction_element(
                    bra, ket, direction
                )
        output.append(matrix)
    return tuple(output)


def exact_covariance(
    n: int,
    alphas: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    directions = exact_direction_matrices(n)
    covariance = 0.5 * np.eye(4 * n**3, dtype=complex)
    for direction, alpha in zip(directions, alphas):
        covariance -= 0.5 * np.kron(direction, alpha)
    return covariance, directions


def main() -> None:
    alphas, _, clifford_error = baseline.dirac_matrices()
    reports = []
    covariances = {}
    directions_by_n = {}
    for n in (2, 4):
        covariance, directions = exact_covariance(n, alphas)
        covariances[n] = covariance
        directions_by_n[n] = directions
        eigenvalues = np.linalg.eigvalsh(covariance)
        gh = {}
        previous = None
        for order in (16, 20, 24, 28, 32):
            approximation = baseline.mixed_covariance(
                n, alphas, quadrature_order=order
            )
            gh[str(order)] = {
                "operator_norm_to_exact": float(
                    np.linalg.norm(approximation - covariance, ord=2)
                ),
                "operator_norm_from_previous": (
                    None
                    if previous is None
                    else float(np.linalg.norm(approximation - previous, ord=2))
                ),
            }
            previous = approximation
        reports.append(
            {
                "n": n,
                "dimension": int(covariance.shape[0]),
                "covariance_hermiticity_error": float(
                    np.linalg.norm(
                        covariance - covariance.conjugate().T, ord=2
                    )
                ),
                "direction_hermiticity_errors": [
                    float(np.linalg.norm(value - value.conjugate().T, ord=2))
                    for value in directions
                ],
                "minimum_eigenvalue": float(eigenvalues[0]),
                "maximum_eigenvalue": float(eigenvalues[-1]),
                "gh_convergence": gh,
            }
        )

    spatial_indices = [
        (a * 4 + b) * 4 + c
        for a in range(2)
        for b in range(2)
        for c in range(2)
    ]
    spin_indices = [
        4 * spatial + spin
        for spatial in spatial_indices
        for spin in range(4)
    ]
    nesting_error = float(
        np.linalg.norm(
            covariances[4][np.ix_(spin_indices, spin_indices)]
            - covariances[2],
            ord=2,
        )
    )
    converges = all(
        report["gh_convergence"]["32"]["operator_norm_to_exact"]
        < report["gh_convergence"]["28"]["operator_norm_to_exact"]
        < report["gh_convergence"]["24"]["operator_norm_to_exact"]
        for report in reports
    )
    passed = (
        clifford_error < 1e-12
        and nesting_error < 2e-12
        and converges
        and all(report["covariance_hermiticity_error"] < 2e-12 for report in reports)
        and all(report["minimum_eigenvalue"] >= -2e-12 for report in reports)
        and all(report["maximum_eigenvalue"] <= 1 + 2e-12 for report in reports)
    )

    np.savez(
        MATRICES,
        covariance_n2=covariances[2],
        covariance_n4=covariances[4],
        direction_n2_x=directions_by_n[2][0],
        direction_n2_y=directions_by_n[2][1],
        direction_n2_z=directions_by_n[2][2],
        direction_n4_x=directions_by_n[4][0],
        direction_n4_y=directions_by_n[4][1],
        direction_n4_z=directions_by_n[4][2],
    )
    result = {
        "schema": "stage8_t7_exact_hermite_mixed_covariance_v001",
        "spec_sha256": sha256(SPEC),
        "clifford_error": clifford_error,
        "reports": reports,
        "n2_inside_n4_operator_norm_error": nesting_error,
        "gh_sequence_converges_toward_exact": converges,
        "overall_verdict": (
            "EXACT_HERMITE_MIXED_COVARIANCE_DERIVED"
            if passed
            else "EXACT_HERMITE_MIXED_COVARIANCE_BLOCKED"
        ),
        "matrix_artifact": str(MATRICES.relative_to(ROOT)),
        "matrix_artifact_sha256": sha256(MATRICES),
        "exact_mixed_covariance_derived": passed,
        "physical_regulator_completed_record_baseline_derived": False,
        "sharp_cell_implementability_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
