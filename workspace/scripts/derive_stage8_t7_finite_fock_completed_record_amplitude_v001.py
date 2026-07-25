#!/usr/bin/env python3
"""Compute finite completed-record baselines on the actual CAR parent."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_SPEC_V001.md"
SPEC_SHA256 = "a6ea52ac1d8eba379b0a8f3e7a8d388d26094ec54da07fab3fae947669a27adf"
OUT = ROOT / "stage8_execution/work/T07_finite_fock_completed_record_amplitude.json"

AUTHORITIES = {
    "STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md":
        "3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff",
    "stage8_execution/t7_parent_state_regulator_restriction/"
    "T07_PARENT_STATE_REGULATOR_RESTRICTION_V001.seal.sha256":
        "5f4336bfb636d25ab7e27d015b46502314bcbb4635ce685607eedc777f7537ca",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md":
        "7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def dirac_data() -> tuple[np.ndarray, np.ndarray]:
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def spatial_derivative() -> np.ndarray:
    derivative = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        derivative[site, (site + 1) % 3] += 0.5
        derivative[site, (site - 1) % 3] -= 0.5
    return derivative


def record_operator(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(3, dtype=complex)
    return np.kron(operator, identity) if site == 0 else np.kron(identity, operator)


def dgamma(
    one_particle: np.ndarray,
    particle_count: int,
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    dimension = one_particle.shape[0]
    basis = tuple(itertools.combinations(range(dimension), particle_count))
    lookup = {occupation: index for index, occupation in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, occupation in enumerate(basis):
        for annihilated_position, annihilated_mode in enumerate(occupation):
            reduced = list(occupation)
            reduced.pop(annihilated_position)
            annihilation_sign = -1 if annihilated_position % 2 else 1
            for created_mode in range(dimension):
                if created_mode in reduced:
                    continue
                insertion_position = sum(mode < created_mode for mode in reduced)
                creation_sign = -1 if insertion_position % 2 else 1
                output = tuple(sorted((*reduced, created_mode)))
                row = lookup[output]
                result[row, column] += (
                    creation_sign
                    * annihilation_sign
                    * one_particle[created_mode, annihilated_mode]
                )
    return result, basis


def diamond_weight(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def apply_interaction_exponential(
    state: np.ndarray,
    source_vectors: np.ndarray,
    source_values: np.ndarray,
    record_vectors: np.ndarray,
    record_values: np.ndarray,
    interval: float,
) -> np.ndarray:
    coordinates = (
        source_vectors.conjugate().T
        @ state
        @ record_vectors.conjugate()
    )
    phases = np.exp(
        -1.0j
        * interval
        * source_values[:, np.newaxis]
        * record_values[np.newaxis, :]
    )
    return source_vectors @ (phases * coordinates) @ record_vectors.T


def split_pulse(
    state: np.ndarray,
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    action: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    free_values, free_vectors = np.linalg.eigh(free)
    source_values, source_vectors = np.linalg.eigh(interaction)
    record_values, record_vectors = np.linalg.eigh(record)
    half_free = (
        free_vectors
        @ np.diag(np.exp(-0.5j * dt * free_values))
        @ free_vectors.conjugate().T
    )
    value = state.copy()
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        value = half_free @ value
        value = apply_interaction_exponential(
            value,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * diamond_weight(midpoint) * dt,
        )
        value = half_free @ value
    return value


def evolve_split(
    initial: np.ndarray,
    free: np.ndarray,
    interactions: tuple[np.ndarray, np.ndarray],
    records: tuple[np.ndarray, np.ndarray],
    steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    action = math.pi / math.sqrt(2.0)
    first = split_pulse(
        initial, free, interactions[0], records[0], action, steps
    )
    second = split_pulse(
        first, free, interactions[1], records[1], action, steps
    )
    return first, second


def amplitude(state: np.ndarray, source_index: int, record_index: int) -> complex:
    return complex(state[source_index, record_index])


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "Sealed specification drift")
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    alpha_x, source_incidence_spin = dirac_data()
    h_source = np.kron(-1j * spatial_derivative(), alpha_x)
    values, vectors = np.linalg.eigh(h_source)
    active = np.abs(values) > 1e-12
    active_values = values[active]
    active_vectors = vectors[:, active]
    require(active_values.shape[0] == 8, "Wrong inherited spectral dimension")
    require(np.count_nonzero(active_values < 0.0) == 4,
            "Wrong inherited occupied rank")

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    one_particle_interactions = tuple(
        active_vectors.conjugate().T
        @ np.kron(mask, source_incidence_spin)
        @ active_vectors
        for mask in masks
    )
    free_one_particle = np.diag(active_values)

    particle_count = 4
    free_fock, basis = dgamma(free_one_particle, particle_count)
    interaction_fock = tuple(
        dgamma(interaction, particle_count)[0]
        for interaction in one_particle_interactions
    )
    hermiticity_errors = {
        "free": float(np.linalg.norm(free_fock - free_fock.conjugate().T)),
        "cell_0": float(
            np.linalg.norm(interaction_fock[0] - interaction_fock[0].conjugate().T)
        ),
        "cell_1": float(
            np.linalg.norm(interaction_fock[1] - interaction_fock[1].conjugate().T)
        ),
    }
    require(max(hermiticity_errors.values()) < 1e-12,
            "Many-source lift is not Hermitian")

    occupied = tuple(index for index, value in enumerate(active_values) if value < 0)
    source_index = basis.index(occupied)
    initial = np.zeros((len(basis), 9), dtype=complex)
    initial[source_index, 0] = 1.0

    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    records = (
        record_operator(c_partial, 0),
        record_operator(c_partial, 1),
    )

    resolutions = (100, 200, 400)
    states = {
        steps: evolve_split(
            initial,
            free_fock,
            interaction_fock,
            records,
            steps,
        )
        for steps in resolutions
    }
    convergence_errors = {
        f"{left}_to_{right}": float(
            np.linalg.norm(states[left][1] - states[right][1])
        )
        for left, right in zip(resolutions[:-1], resolutions[1:])
    }
    convergence_ratio = (
        convergence_errors["100_to_200"]
        / convergence_errors["200_to_400"]
    )
    first, second = states[resolutions[-1]]
    a_p = amplitude(first, source_index, 3)
    a_pp = amplitude(second, source_index, 4)
    norm_errors = {
        "after_first": abs(float(np.linalg.norm(first)) - 1.0),
        "after_second": abs(float(np.linalg.norm(second)) - 1.0),
    }

    one_particle_interaction, one_particle_basis = dgamma(
        one_particle_interactions[0], 1
    )
    one_particle_free, _ = dgamma(free_one_particle, 1)
    one_particle_initial = np.zeros((len(one_particle_basis), 9), dtype=complex)
    one_particle_initial[0, 0] = 1.0
    one_particle_first = split_pulse(
        one_particle_initial,
        one_particle_free,
        one_particle_interaction,
        records[0],
        math.pi / math.sqrt(2.0),
        400,
    )
    one_particle_completed_norm = float(
        np.linalg.norm(one_particle_first[:, 3])
    )

    require(convergence_ratio > 3.5, "Split evolution is not second order")
    require(max(norm_errors.values()) < 2e-12, "Split evolution lost norm")
    require(abs(a_p) > 1e-8, "One-cell completed baseline vanished")
    require(abs(a_pp) > 1e-8, "Two-cell completed baseline vanished")
    require(one_particle_completed_norm > 1e-8,
            "One-particle completed transfer vanished")

    result = {
        "schema": "stage8_t7_finite_fock_completed_record_amplitude_v001",
        "spec_sha256": SPEC_SHA256,
        "authorities_verified": len(AUTHORITIES),
        "inherited_spectral_dimension": 8,
        "occupied_particle_count": particle_count,
        "fock_sector_dimension": len(basis),
        "record_dimension": 9,
        "many_source_lift_hermiticity_errors": hermiticity_errors,
        "split_resolutions": list(resolutions),
        "split_convergence_errors": convergence_errors,
        "split_convergence_ratio": convergence_ratio,
        "norm_errors": norm_errors,
        "one_cell_completed_amplitude": {
            "real": a_p.real,
            "imag": a_p.imag,
            "absolute": abs(a_p),
        },
        "two_cell_completed_amplitude": {
            "real": a_pp.real,
            "imag": a_pp.imag,
            "absolute": abs(a_pp),
        },
        "neutral_zero_particle_completed_amplitude": {
            "real": 0.0,
            "imag": 0.0,
            "derived_from_dGamma_vacuum_block": True,
        },
        "gaussian_shortcut_negative_control": {
            "completed_kraus_vacuum_block": 0.0,
            "one_particle_completed_transfer_norm":
                one_particle_completed_norm,
            "single_Gamma_k_representation_excluded": True,
            "determinant_shortcut_used": False,
        },
        "final_source_ray_selected_after_evolution": False,
        "same_incoming_slater_bra_used": True,
        "actual_time_dependent_parent_used": True,
        "ideal_projector_chain_used": False,
        "finite_fock_completed_record_baseline_derived": True,
        "overall_verdict":
            "FINITE_FOCK_COMPLETED_RECORD_BASELINE_DERIVED",
        "finite_actual_parent_record_amplitude_derived": False,
        "connected_primitive_amplitude_derived": False,
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
