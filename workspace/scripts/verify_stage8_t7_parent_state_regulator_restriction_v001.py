#!/usr/bin/env python3
"""Independent closed-form verifier for finite quasifree restrictions."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution/work/T07_parent_state_regulator_restriction.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def alpha_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    return tuple(
        gamma0 @ np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )


def closed_covariance(momentum: tuple[float, float, float]) -> np.ndarray:
    alphas = alpha_matrices()
    hamiltonian = sum(
        (
            momentum[index] * alphas[index]
            for index in range(3)
        ),
        np.zeros((4, 4), dtype=complex),
    )
    radius = math.sqrt(sum(value * value for value in momentum))
    require(radius > 0.0, "Zero momentum is outside this spectral cohort")
    return (np.eye(4, dtype=complex) - hamiltonian / radius) / 2.0


def block_covariance(
    momenta: tuple[tuple[float, float, float], ...],
) -> np.ndarray:
    dimension = 4 * len(momenta)
    result = np.zeros((dimension, dimension), dtype=complex)
    for index, momentum in enumerate(momenta):
        block = slice(4 * index, 4 * index + 4)
        result[block, block] = closed_covariance(momentum)
    return result


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="utf-8"))
    small_momenta = tuple(
        tuple(momentum) for momentum in stored["small_cohort"]["momenta"]
    )
    large_momenta = tuple(
        tuple(momentum) for momentum in stored["large_cohort"]["momenta"]
    )
    small = block_covariance(small_momenta)
    large = block_covariance(large_momenta)

    require(
        np.linalg.norm(small @ small - small) < 1e-12,
        "Closed-form small covariance is not a projection",
    )
    require(
        np.linalg.norm(large @ large - large) < 1e-12,
        "Closed-form large covariance is not a projection",
    )
    require(
        np.linalg.norm(large[:8, :8] - small) < 1e-12,
        "Closed-form nested restriction failed",
    )
    require(
        np.linalg.matrix_rank(small, tol=1e-10)
        == stored["small_cohort"]["covariance_rank"],
        "Small rank mismatch",
    )
    require(
        np.linalg.matrix_rank(large, tol=1e-10)
        == stored["large_cohort"]["covariance_rank"],
        "Large rank mismatch",
    )
    require(
        stored["parent_state_regulator_restriction_derived"] is True,
        "State restriction was not promoted",
    )
    require(
        stored["new_zero_mode_filling_adopted"] is False,
        "A zero-mode filling was silently added",
    )
    require(
        stored["thermal_parameter_introduced"] is False,
        "A thermal selector was silently added",
    )
    for flag in (
        "finite_actual_parent_record_amplitude_derived",
        "connected_primitive_amplitude_derived",
        "volume_uniform_zero_free_neighborhood_proved",
        "connected_linked_cluster_density_proved",
        "kappa_record_computed",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        require(stored[flag] is False, f"Protected flag promoted: {flag}")

    print("PASS independent parent-state regulator restriction verification")


if __name__ == "__main__":
    main()
