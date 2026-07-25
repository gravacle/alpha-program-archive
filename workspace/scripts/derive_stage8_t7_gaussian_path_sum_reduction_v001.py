#!/usr/bin/env python3
"""Derive and test the exact finite Gaussian path-sum representation."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_SPEC_V001.md"
SPEC_SHA256 = "49ee64dc171c4fd76003a60dcb5a4527b9d8b11f3b1b6caab7634e4d29f23513"
FINITE = ROOT / "stage8_execution/work/T07_finite_fock_completed_record_amplitude.json"
OUT = ROOT / "stage8_execution/work/T07_gaussian_path_sum_reduction.json"

AUTHORITIES = {
    "STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md":
        "907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6",
    "stage8_execution/t7_finite_fock_completed_record_amplitude/"
    "T07_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_V001.seal.sha256":
        "5dcdd0a74370d27703d2ece580738fd2070d50e1b8ffc6a268ce313553e83fdd",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md":
        "3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parent_matrices() -> tuple[np.ndarray, tuple[np.ndarray, np.ndarray], np.ndarray]:
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    eye_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    gamma_0 = np.block([[eye_2, zero_2], [zero_2, -eye_2]])
    gamma_space = tuple(
        np.block([[zero_2, sigma], [-sigma, zero_2]])
        for sigma in (sigma_1, sigma_2, sigma_3)
    )
    gamma_5 = (
        1j
        * gamma_0
        @ gamma_space[0]
        @ gamma_space[1]
        @ gamma_space[2]
    )
    alpha_x = gamma_0 @ gamma_space[0]
    incidence_spin = -1j * gamma_0 @ gamma_5

    derivative = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        derivative[site, (site + 1) % 3] = 0.5
        derivative[site, (site - 1) % 3] = -0.5
    parent_free = np.kron(-1j * derivative, alpha_x)
    values, vectors = np.linalg.eigh(parent_free)
    active = np.abs(values) > 1e-12
    active_values = values[active]
    active_vectors = vectors[:, active]
    free = np.diag(active_values)

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions = tuple(
        active_vectors.conjugate().T
        @ np.kron(mask, incidence_spin)
        @ active_vectors
        for mask in masks
    )
    occupied = np.eye(8, dtype=complex)[:, active_values < 0.0]
    return free, interactions, occupied


def record_spectral_data() -> tuple[np.ndarray, np.ndarray]:
    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    values, vectors = np.linalg.eigh(record)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    weights = np.array(
        [
            np.vdot(pointer, vectors[:, index])
            * np.vdot(vectors[:, index], ready)
            for index in range(3)
        ],
        dtype=complex,
    )
    require(np.linalg.norm(record - vectors @ np.diag(values) @ vectors.conjugate().T) < 1e-14,
            "Record spectral resolution failed")
    require(abs(np.sum(weights)) < 1e-14,
            "Completed transition lost ready/pointer orthogonality")
    return values, weights


def diamond_weight(time: float) -> float:
    return 32.0 * min(time, 1.0 - time) ** 3


def one_particle_pulse(
    free: np.ndarray,
    interaction: np.ndarray,
    record_eigenvalue: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    action = math.pi / math.sqrt(2.0)
    free_values, free_vectors = np.linalg.eigh(free)
    interaction_values, interaction_vectors = np.linalg.eigh(interaction)
    half_free = (
        free_vectors
        @ np.diag(np.exp(-0.5j * dt * free_values))
        @ free_vectors.conjugate().T
    )
    propagator = np.eye(free.shape[0], dtype=complex)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        interaction_step = (
            interaction_vectors
            @ np.diag(
                np.exp(
                    -1j
                    * action
                    * diamond_weight(midpoint)
                    * dt
                    * record_eigenvalue
                    * interaction_values
                )
            )
            @ interaction_vectors.conjugate().T
        )
        propagator = half_free @ interaction_step @ half_free @ propagator
    return propagator


def path_sum(
    cell_propagators: tuple[tuple[np.ndarray, ...], ...],
    weights: np.ndarray,
    occupied: np.ndarray,
) -> complex:
    total = 0.0j
    for labels in itertools.product(range(3), repeat=len(cell_propagators)):
        one_particle = np.eye(occupied.shape[0], dtype=complex)
        path_weight = 1.0 + 0.0j
        for cell, label in enumerate(labels):
            one_particle = cell_propagators[cell][label] @ one_particle
            path_weight *= weights[label]
        total += path_weight * np.linalg.det(
            occupied.conjugate().T @ one_particle @ occupied
        )
    return complex(total)


def complex_from_stored(data: dict[str, float]) -> complex:
    return complex(data["real"], data["imag"])


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    stored = json.loads(FINITE.read_text(encoding="utf-8"))
    free, interactions, occupied = parent_matrices()
    record_values, weights = record_spectral_data()

    amplitudes: dict[int, dict[str, object]] = {}
    path_counts: dict[int, int] = {}
    propagators_by_resolution: dict[int, tuple[tuple[np.ndarray, ...], ...]] = {}
    for steps in (100, 200, 400):
        propagators = tuple(
            tuple(
                one_particle_pulse(free, interaction, float(value), steps)
                for value in record_values
            )
            for interaction in interactions
        )
        propagators_by_resolution[steps] = propagators
        one = path_sum((propagators[0],), weights, occupied)
        two = path_sum(propagators, weights, occupied)
        amplitudes[steps] = {
            "one": {"real": one.real, "imag": one.imag},
            "two": {"real": two.real, "imag": two.imag},
        }
        path_counts[steps] = 3 + 9

    one_100 = complex_from_stored(amplitudes[100]["one"])
    one_200 = complex_from_stored(amplitudes[200]["one"])
    one_400 = complex_from_stored(amplitudes[400]["one"])
    two_100 = complex_from_stored(amplitudes[100]["two"])
    two_200 = complex_from_stored(amplitudes[200]["two"])
    two_400 = complex_from_stored(amplitudes[400]["two"])
    one_ratio = abs(one_100 - one_200) / abs(one_200 - one_400)
    two_ratio = abs(two_100 - two_200) / abs(two_200 - two_400)

    primary_one = complex_from_stored(stored["one_cell_completed_amplitude"])
    primary_two = complex_from_stored(stored["two_cell_completed_amplitude"])
    one_difference = abs(one_400 - primary_one)
    two_difference = abs(two_400 - primary_two)
    unitarity_error = max(
        np.linalg.norm(unitary.conjugate().T @ unitary - np.eye(8))
        for cell in propagators_by_resolution[400]
        for unitary in cell
    )

    require(one_ratio > 3.5, "One-cell path sum lost second-order convergence")
    require(two_ratio > 3.5, "Two-cell path sum lost second-order convergence")
    require(unitarity_error < 2e-12, "One-particle path lost unitarity")
    require(one_difference < 1e-4, "One-cell path sum disagrees with finite Fock")
    require(two_difference < 1e-4, "Two-cell path sum disagrees with finite Fock")

    result = {
        "schema": "stage8_t7_gaussian_path_sum_reduction_v001",
        "spec_sha256": SPEC_SHA256,
        "record_eigenvalues": [float(value) for value in record_values],
        "record_transition_weights": [
            {"real": float(value.real), "imag": float(value.imag)}
            for value in weights
        ],
        "record_weight_sum_absolute": float(abs(np.sum(weights))),
        "valid_termwise_determinants_used": True,
        "single_determinant_shortcut_used": False,
        "postselected_source_ray_used": False,
        "path_count_one_cell": 3,
        "path_count_two_cells": 9,
        "amplitudes_by_steps": amplitudes,
        "one_cell_convergence_ratio": float(one_ratio),
        "two_cell_convergence_ratio": float(two_ratio),
        "maximum_one_particle_unitarity_error": float(unitarity_error),
        "finite_fock_one_cell_difference": float(one_difference),
        "finite_fock_two_cell_difference": float(two_difference),
        "gaussian_path_sum_reduction_derived": True,
        "overall_verdict": "GAUSSIAN_PATH_SUM_REDUCTION_DERIVED",
        "all_finite_connected_baselines_nonzero_proved": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
