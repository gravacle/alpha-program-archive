#!/usr/bin/env python3
"""Evaluate the sealed finite-Qspec holonomy response diagnostic, successor v003."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_DIAGNOSTIC_SPEC_V001.md"
NUMERICS = ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_PROTOCOL_V001.md"
DUHAMEL = ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_DUHAMEL_CROSSCHECK_PROTOCOL_V001.md"
SUCCESSOR = ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_SUCCESSOR_V001.md"
SUCCESSOR2 = ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_SUCCESSOR_V002.md"
OUT = ROOT / "stage8_execution/work/QSPEC_finite_holonomy_response_v003.json"

EXPECTED = {
    SPEC: "d1b5ab24ebf8c1bc9b7598449596a6431c2152cab7edcf4d0cefcfd64e3815a5",
    NUMERICS: "057a892611f21b3cb6dfb8d547610762445261583840320a3a1b970078c30921",
    DUHAMEL: "3d86dc4f15cc51bd3a3848b71c295734c6cee565cffc5817b7ddcfcedd30126f",
    SUCCESSOR: "88df55332902fa3ca103939eb53bf08fc7affddf0243c1c9c7847b98fa2ddeaa",
    SUCCESSOR2: "e0f3ebfde6fff3ef6d12245d48f782b261e93c2f86cf7692b4830fdee6dc98c1",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md":
        "273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb",
    ROOT / "STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md":
        "907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6",
    ROOT / "STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md":
        "3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff",
    ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    ROOT / "BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md":
        "0fe3905aa14ed744bda883dd68aa799dc9bb90f4f5647b477be3f6de65330f57",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


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
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def covariant_derivative(theta: float) -> np.ndarray:
    derivative = np.zeros((3, 3), dtype=complex)
    phase = np.exp(1j * theta / 3.0)
    for site in range(3):
        derivative[site, (site + 1) % 3] += 0.5 * phase
        derivative[site, (site - 1) % 3] -= 0.5 * phase.conjugate()
    return derivative


def covariant_derivative_tangent() -> np.ndarray:
    tangent = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        tangent[site, (site + 1) % 3] += 1j / 6.0
        tangent[site, (site - 1) % 3] += 1j / 6.0
    return tangent


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
                result[lookup[output], column] += (
                    creation_sign
                    * annihilation_sign
                    * one_particle[created_mode, annihilated_mode]
                )
    return result, basis


def diamond_weight(local_time: float) -> float:
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
        -1j
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
    action = math.pi / math.sqrt(2.0)
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


def rk4_tangent_pulse(
    state: np.ndarray,
    tangent_state: np.ndarray,
    free: np.ndarray,
    current: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    dt = 1.0 / steps
    action = math.pi / math.sqrt(2.0)

    def rhs(
        psi: np.ndarray,
        eta: np.ndarray,
        local_time: float,
    ) -> tuple[np.ndarray, np.ndarray]:
        strength = action * diamond_weight(local_time)
        h_psi = (
            free @ psi
            + strength * interaction @ psi @ record.T
        )
        h_eta = (
            free @ eta
            + strength * interaction @ eta @ record.T
        )
        return -1j * h_psi, -1j * (h_eta + current @ psi)

    psi = state.copy()
    eta = tangent_state.copy()
    for index in range(steps):
        t = index * dt
        k1_psi, k1_eta = rhs(psi, eta, t)
        k2_psi, k2_eta = rhs(
            psi + 0.5 * dt * k1_psi,
            eta + 0.5 * dt * k1_eta,
            t + 0.5 * dt,
        )
        k3_psi, k3_eta = rhs(
            psi + 0.5 * dt * k2_psi,
            eta + 0.5 * dt * k2_eta,
            t + 0.5 * dt,
        )
        k4_psi, k4_eta = rhs(
            psi + dt * k3_psi,
            eta + dt * k3_eta,
            t + dt,
        )
        psi += dt * (k1_psi + 2 * k2_psi + 2 * k3_psi + k4_psi) / 6
        eta += dt * (k1_eta + 2 * k2_eta + 2 * k3_eta + k4_eta) / 6
    return psi, eta


def interval(center: float, radius: float) -> tuple[float, float]:
    return center - radius, center + radius


def overlap(a: tuple[float, float], b: tuple[float, float]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


def main() -> None:
    for path, expected in EXPECTED.items():
        require(sha256(path) == expected, f"authority drift: {path.name}")

    alpha_x, source_incidence_spin = dirac_data()
    full_h0 = np.kron(-1j * covariant_derivative(0.0), alpha_x)
    values, vectors = np.linalg.eigh(full_h0)
    active = np.abs(values) > 1e-12
    active_values = values[active]
    active_vectors = vectors[:, active]
    require(active_values.shape[0] == 8, "wrong fixed active dimension")
    require(np.count_nonzero(active_values < 0.0) == 4, "wrong occupied rank")

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
    particle_count = 4
    interaction_fock = tuple(
        dgamma(value, particle_count)[0]
        for value in one_particle_interactions
    )

    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    records = (
        record_operator(c_partial, 0),
        record_operator(c_partial, 1),
    )

    free_zero_one = np.diag(active_values)
    free_zero, basis = dgamma(free_zero_one, particle_count)
    occupied = tuple(index for index, value in enumerate(active_values) if value < 0)
    source_index = basis.index(occupied)
    initial = np.zeros((len(basis), 9), dtype=complex)
    initial[source_index, 0] = 1.0

    tangent_full = np.kron(-1j * covariant_derivative_tangent(), alpha_x)
    tangent_active = (
        active_vectors.conjugate().T @ tangent_full @ active_vectors
    )
    current_fock = dgamma(tangent_active, particle_count)[0]

    def free_fock(theta: float) -> tuple[np.ndarray, float]:
        full = np.kron(-1j * covariant_derivative(theta), alpha_x)
        projected = active_vectors.conjugate().T @ full @ active_vectors
        leakage = np.linalg.norm(
            (np.eye(12, dtype=complex) - active_vectors @ active_vectors.conjugate().T)
            @ full
            @ active_vectors
        )
        return dgamma(projected, particle_count)[0], float(leakage)

    def evolve(theta: float, steps: int) -> tuple[np.ndarray, float]:
        free, leakage = free_fock(theta)
        state = initial.copy()
        for interaction, record in zip(interaction_fock, records):
            state = split_pulse(state, free, interaction, record, steps)
        return state, leakage

    theta_values = (1.0 / 20.0, 1.0 / 40.0)
    time_values = (200, 400)
    states: dict[tuple[int, float], np.ndarray] = {}
    leakages: dict[str, float] = {}
    norm_errors: dict[str, float] = {}
    for steps in time_values:
        for theta in (0.0, *theta_values, *(-value for value in theta_values)):
            state, leakage = evolve(theta, steps)
            states[(steps, theta)] = state
            key = f"steps_{steps}_theta_{theta:+.8f}"
            leakages[key] = leakage
            norm_errors[key] = abs(float(np.linalg.norm(state)) - 1.0)

    estimates: dict[tuple[int, float], dict[str, float]] = {}
    for steps in time_values:
        psi0 = states[(steps, 0.0)]
        for theta in theta_values:
            psi_plus = states[(steps, theta)]
            psi_minus = states[(steps, -theta)]
            z_plus = complex(np.vdot(psi0, psi_plus))
            z_minus = complex(np.vdot(psi0, psi_minus))
            gamma_plus = -math.log(abs(z_plus))
            gamma_minus = -math.log(abs(z_minus))
            hessian = (gamma_plus + gamma_minus) / (theta * theta)
            dot_state = (psi_plus - psi_minus) / (2.0 * theta)
            projection = complex(np.vdot(psi0, dot_state))
            g_fs = float(
                np.vdot(dot_state, dot_state).real - abs(projection) ** 2
            )
            estimates[(steps, theta)] = {
                "Z_plus_real": z_plus.real,
                "Z_plus_imag": z_plus.imag,
                "Z_plus_absolute": abs(z_plus),
                "Z_minus_real": z_minus.real,
                "Z_minus_imag": z_minus.imag,
                "Z_minus_absolute": abs(z_minus),
                "H_CTP": hessian,
                "g_FS_finite_difference": g_fs,
            }

    coarse_steps, fine_steps = time_values
    theta_coarse, theta_fine = theta_values
    h_fine = estimates[(fine_steps, theta_fine)]["H_CTP"]
    g_fine = estimates[(fine_steps, theta_fine)]["g_FS_finite_difference"]
    h_param_tail = abs(
        h_fine - estimates[(fine_steps, theta_coarse)]["H_CTP"]
    ) / 3.0
    h_time_tail = abs(
        h_fine - estimates[(coarse_steps, theta_fine)]["H_CTP"]
    ) / 3.0
    g_param_tail = abs(
        g_fine
        - estimates[(fine_steps, theta_coarse)]["g_FS_finite_difference"]
    ) / 3.0
    g_time_tail = abs(
        g_fine
        - estimates[(coarse_steps, theta_fine)]["g_FS_finite_difference"]
    ) / 3.0
    h_radius = h_param_tail + h_time_tail + 1e-8
    g_radius = g_param_tail + g_time_tail + 1e-8
    h_interval = interval(h_fine, h_radius)
    g_interval = interval(g_fine, g_radius)

    duhamel_time_values = (1600, 3200)
    duhamel_estimates: dict[int, dict[str, float]] = {}
    for steps in duhamel_time_values:
        psi = initial.copy()
        eta = np.zeros_like(initial)
        for interaction, record in zip(interaction_fock, records):
            psi, eta = rk4_tangent_pulse(
                psi,
                eta,
                free_zero,
                current_fock,
                interaction,
                record,
                steps,
            )
        projection = complex(np.vdot(psi, eta))
        g_duhamel = float(np.vdot(eta, eta).real - abs(projection) ** 2)
        duhamel_estimates[steps] = {
            "g_Duhamel": g_duhamel,
            "state_norm_error": abs(float(np.linalg.norm(psi)) - 1.0),
        }
    d_coarse_steps, d_fine_steps = duhamel_time_values
    d_fine = duhamel_estimates[d_fine_steps]["g_Duhamel"]
    d_radius = (
        abs(d_fine - duhamel_estimates[d_coarse_steps]["g_Duhamel"]) / 3.0
        + 1e-8
    )
    d_interval = interval(d_fine, d_radius)

    derivative = covariant_derivative(theta_fine)
    antihermiticity_error = float(np.linalg.norm(derivative + derivative.conjugate().T))
    loop_error = abs(np.exp(1j * theta_fine / 3.0) ** 3 - np.exp(1j * theta_fine))
    hermiticity_errors = {
        "free_zero": float(np.linalg.norm(free_zero - free_zero.conjugate().T)),
        "current": float(np.linalg.norm(current_fock - current_fock.conjugate().T)),
        "interaction_0": float(
            np.linalg.norm(interaction_fock[0] - interaction_fock[0].conjugate().T)
        ),
        "interaction_1": float(
            np.linalg.norm(interaction_fock[1] - interaction_fock[1].conjugate().T)
        ),
    }

    pass_value = bool(
        antihermiticity_error < 1e-12
        and loop_error < 1e-12
        and max(hermiticity_errors.values()) < 1e-12
        and max(norm_errors.values()) < 2e-10
        and max(
            row["state_norm_error"] for row in duhamel_estimates.values()
        ) < 2e-10
        and abs(complex(np.vdot(states[(fine_steps, 0.0)], states[(fine_steps, 0.0)])) - 1.0)
        < 1e-12
        and h_interval[0] > 0.0
        and g_interval[0] > 0.0
        and d_interval[0] > 0.0
        and overlap(h_interval, g_interval)
        and overlap(h_interval, d_interval)
        and overlap(g_interval, d_interval)
    )

    formatted_estimates = {
        f"steps_{steps}_theta_{theta:.8f}": value
        for (steps, theta), value in estimates.items()
    }
    result = {
        "schema": "complete_qspec_finite_holonomy_response_v003",
        "spec_sha256": sha256(SPEC),
        "numerics_protocol_sha256": sha256(NUMERICS),
        "duhamel_protocol_sha256": sha256(DUHAMEL),
        "numerics_successor_sha256": sha256(SUCCESSOR),
        "numerics_successor_v002_sha256": sha256(SUCCESSOR2),
        "connection": {
            "carrier": "three_site_periodic_regulator",
            "coordinate": "total_Wilson_loop_angle_theta",
            "uniform_link_phase": "theta/3",
            "antihermiticity_error": antihermiticity_error,
            "loop_holonomy_error": float(loop_error),
            "local_Maxwell_field_strength_claimed": False,
        },
        "fixed_active_dimension": int(active_values.shape[0]),
        "occupied_particle_count": particle_count,
        "fock_dimension": len(basis),
        "record_dimension": 9,
        "regulator_subspace_leakage": leakages,
        "hermiticity_errors": hermiticity_errors,
        "norm_errors": norm_errors,
        "estimates": formatted_estimates,
        "H_CTP_interval": list(h_interval),
        "g_FS_interval": list(g_interval),
        "Duhamel_estimates": {
            str(key): value for key, value in duhamel_estimates.items()
        },
        "g_Duhamel_interval": list(d_interval),
        "interval_intersections": {
            "H_with_gFS": overlap(h_interval, g_interval),
            "H_with_Duhamel": overlap(h_interval, d_interval),
            "gFS_with_Duhamel": overlap(g_interval, d_interval),
        },
        "complete_final_identity_used": True,
        "record_outcome_postselected": False,
        "final_source_state_postselected": False,
        "determinant_used": False,
        "open_tree_zero_stiffness_retained": True,
        "overall_verdict": (
            "FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_PASS"
            if pass_value
            else "FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_BLOCKED"
        ),
        "complete_Qspec_CTP_scalar_closure_derived": True,
        "finite_Qspec_holonomy_response_diagnostic_passed": pass_value,
        "interacting_continuum_CTP_amplitude_derived": False,
        "local_Maxwell_response_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not pass_value:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
