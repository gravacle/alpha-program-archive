#!/usr/bin/env python3
"""Independent direct-ODE verifier for the finite-Qspec holonomy response."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    ROOT
    / "COMPLETE_QSPEC_FINITE_HOLONOMY_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
PRIMARY_SCRIPT = (
    ROOT / "scripts/derive_complete_qspec_finite_holonomy_response_v003.py"
)
PRIMARY = (
    ROOT / "stage8_execution/work/QSPEC_finite_holonomy_response_v003.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_finite_holonomy_response_verification_v001.json"
)

EXPECTED_HASHES = {
    PROTOCOL:
        "f5302ee851bc8c76e4abf91ca7fdbddaca9569202b556db4ef59f0235c592ebe",
    PRIMARY_SCRIPT:
        "ec91dd9c2a283aa2306bebd92b275e4a6e680c0dd05164fb9d305fd6451bec43",
    PRIMARY:
        "49deb24656a3655f59b429c8590566da296d7d4d18fca7e6f15cf1937abf28db",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_DIAGNOSTIC_SPEC_V001.md":
        "d1b5ab24ebf8c1bc9b7598449596a6431c2152cab7edcf4d0cefcfd64e3815a5",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_PROTOCOL_V001.md":
        "057a892611f21b3cb6dfb8d547610762445261583840320a3a1b970078c30921",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_DUHAMEL_CROSSCHECK_PROTOCOL_V001.md":
        "3d86dc4f15cc51bd3a3848b71c295734c6cee565cffc5817b7ddcfcedd30126f",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_SUCCESSOR_V001.md":
        "88df55332902fa3ca103939eb53bf08fc7affddf0243c1c9c7847b98fa2ddeaa",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_NUMERICS_SUCCESSOR_V002.md":
        "e0f3ebfde6fff3ef6d12245d48f782b261e93c2f86cf7692b4830fdee6dc98c1",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pauli_data() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )


def dirac_operators() -> tuple[np.ndarray, np.ndarray]:
    sx, sy, sz = pauli_data()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma_zero = np.block([[identity, zero], [zero, -identity]])
    gamma_space = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma_five = (
        1j
        * gamma_zero
        @ gamma_space[0]
        @ gamma_space[1]
        @ gamma_space[2]
    )
    alpha_x = gamma_zero @ gamma_space[0]
    incidence_spin = -1j * gamma_zero @ gamma_five
    return alpha_x, incidence_spin


def covariant_difference(theta: float) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = forward.conjugate()
    for position in range(3):
        matrix[position, (position + 1) % 3] += forward / 2.0
        matrix[position, (position - 1) % 3] -= backward / 2.0
    return matrix


def fixed_particle_lift(
    one_body: np.ndarray,
    particles: int,
) -> tuple[np.ndarray, tuple[int, ...]]:
    """Lift with integer occupations, independently of tuple deletion."""
    def population(mask: int) -> int:
        return bin(mask).count("1")

    modes = one_body.shape[0]
    occupations = tuple(
        sum(1 << mode for mode in occupied)
        for occupied in itertools.combinations(range(modes), particles)
    )
    row_of = {mask: row for row, mask in enumerate(occupations)}
    lifted = np.zeros((len(occupations), len(occupations)), dtype=complex)
    for column, mask in enumerate(occupations):
        for removed in range(modes):
            if not mask & (1 << removed):
                continue
            below_removed = population(mask & ((1 << removed) - 1))
            annihilation_sign = -1 if below_removed % 2 else 1
            reduced = mask ^ (1 << removed)
            for added in range(modes):
                if reduced & (1 << added):
                    continue
                below_added = population(reduced & ((1 << added) - 1))
                creation_sign = -1 if below_added % 2 else 1
                output = reduced | (1 << added)
                lifted[row_of[output], column] += (
                    annihilation_sign
                    * creation_sign
                    * one_body[added, removed]
                )
    return lifted, occupations


def record_on_site(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(operator.shape[0], dtype=complex)
    if site == 0:
        return np.kron(operator, identity)
    return np.kron(identity, operator)


def causal_weight(time: float) -> float:
    return 32.0 * min(time, 1.0 - time) ** 3


def direct_rhs(
    state: np.ndarray,
    time: float,
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
) -> np.ndarray:
    strength = (math.pi / math.sqrt(2.0)) * causal_weight(time)
    h_state = (
        free @ state
        + strength * interaction @ state @ record.T
    )
    return -1j * h_state


def direct_rk4_pulse(
    state: np.ndarray,
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    steps: int,
) -> np.ndarray:
    """Integrate the unsplit full equation; no primary routine is reused."""
    dt = 1.0 / steps
    value = state.copy()
    for index in range(steps):
        time = index * dt
        k1 = direct_rhs(value, time, free, interaction, record)
        k2 = direct_rhs(
            value + 0.5 * dt * k1,
            time + 0.5 * dt,
            free,
            interaction,
            record,
        )
        k3 = direct_rhs(
            value + 0.5 * dt * k2,
            time + 0.5 * dt,
            free,
            interaction,
            record,
        )
        k4 = direct_rhs(
            value + dt * k3,
            time + dt,
            free,
            interaction,
            record,
        )
        value += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return value


def response(
    zero_state: np.ndarray,
    plus_state: np.ndarray,
    minus_state: np.ndarray,
    theta: float,
) -> dict[str, float]:
    z_plus = complex(np.vdot(zero_state, plus_state))
    z_minus = complex(np.vdot(zero_state, minus_state))
    h_ctp = (
        -math.log(abs(z_plus))
        - math.log(abs(z_minus))
    ) / (theta * theta)
    tangent = (plus_state - minus_state) / (2.0 * theta)
    projection = complex(np.vdot(zero_state, tangent))
    g_fs = float(
        np.vdot(tangent, tangent).real - abs(projection) ** 2
    )
    return {
        "Z_plus_absolute": abs(z_plus),
        "Z_minus_absolute": abs(z_minus),
        "H_CTP": h_ctp,
        "g_FS": g_fs,
    }


def extrapolate(
    rows: dict[tuple[int, float], dict[str, float]],
    key: str,
    coarse_h: float,
    fine_h: float,
) -> dict[str, object]:
    time_limits: dict[float, float] = {}
    time_corrections: dict[float, float] = {}
    for theta in (coarse_h, fine_h):
        coarse = rows[(800, theta)][key]
        fine = rows[(1600, theta)][key]
        correction = (fine - coarse) / 15.0
        time_limits[theta] = fine + correction
        time_corrections[theta] = abs(correction)
    theta_correction = (
        time_limits[fine_h] - time_limits[coarse_h]
    ) / 3.0
    limit = time_limits[fine_h] + theta_correction
    radius = (
        max(time_corrections.values())
        + abs(theta_correction)
        + 1e-8
    )
    return {
        "limit": limit,
        "radius": radius,
        "interval": [limit - radius, limit + radius],
        "time_limits": {
            f"{theta:.8f}": value
            for theta, value in time_limits.items()
        },
        "time_corrections": {
            f"{theta:.8f}": value
            for theta, value in time_corrections.items()
        },
        "theta_correction": theta_correction,
    }


def intervals_overlap(left: list[float], right: list[float]) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def strictly_positive(interval: list[float]) -> bool:
    return interval[0] > 0.0


def main() -> None:
    hash_checks = {
        str(path.relative_to(ROOT)): sha256(path) == expected
        for path, expected in EXPECTED_HASHES.items()
    }
    if not all(hash_checks.values()):
        raise RuntimeError("frozen authority hash mismatch")

    primary = json.loads(PRIMARY.read_text())
    alpha_x, incidence_spin = dirac_operators()
    full_free_zero = np.kron(
        -1j * covariant_difference(0.0),
        alpha_x,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(full_free_zero)
    active_mask = np.abs(eigenvalues) > 1e-12
    active_values = eigenvalues[active_mask]
    active_vectors = eigenvectors[:, active_mask]

    source_masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions_one_body = tuple(
        active_vectors.conjugate().T
        @ np.kron(mask, incidence_spin)
        @ active_vectors
        for mask in source_masks
    )
    interactions = tuple(
        fixed_particle_lift(value, 4)[0]
        for value in interactions_one_body
    )

    record_seed = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    records = (
        record_on_site(record_seed, 0),
        record_on_site(record_seed, 1),
    )

    free_zero, fock_basis = fixed_particle_lift(
        np.diag(active_values),
        4,
    )
    occupied_modes = [
        index for index, value in enumerate(active_values)
        if value < 0.0
    ]
    occupied_mask = sum(1 << mode for mode in occupied_modes)
    initial_source = fock_basis.index(occupied_mask)
    initial = np.zeros((len(fock_basis), 9), dtype=complex)
    initial[initial_source, 0] = 1.0

    identity_full = np.eye(12, dtype=complex)

    def free_at(theta: float) -> tuple[np.ndarray, float]:
        full = np.kron(-1j * covariant_difference(theta), alpha_x)
        projected = active_vectors.conjugate().T @ full @ active_vectors
        leakage = np.linalg.norm(
            (identity_full - active_vectors @ active_vectors.conjugate().T)
            @ full
            @ active_vectors
        )
        return fixed_particle_lift(projected, 4)[0], float(leakage)

    def evolve(theta: float, steps: int) -> tuple[np.ndarray, float]:
        free, leakage = free_at(theta)
        state = initial.copy()
        for interaction, record in zip(interactions, records):
            state = direct_rk4_pulse(
                state,
                free,
                interaction,
                record,
                steps,
            )
        return state, leakage

    time_steps = (800, 1600)
    theta_steps = (1.0 / 80.0, 1.0 / 160.0)
    states: dict[tuple[int, float], np.ndarray] = {}
    norm_errors: dict[str, float] = {}
    leakages: dict[str, float] = {}
    for steps in time_steps:
        theta_values = (
            0.0,
            theta_steps[0],
            -theta_steps[0],
            theta_steps[1],
            -theta_steps[1],
        )
        for theta in theta_values:
            state, leakage = evolve(theta, steps)
            states[(steps, theta)] = state
            label = f"N_{steps}_theta_{theta:+.8f}"
            norm_errors[label] = abs(float(np.linalg.norm(state)) - 1.0)
            leakages[label] = leakage

    rows: dict[tuple[int, float], dict[str, float]] = {}
    for steps in time_steps:
        for theta in theta_steps:
            rows[(steps, theta)] = response(
                states[(steps, 0.0)],
                states[(steps, theta)],
                states[(steps, -theta)],
                theta,
            )

    h_result = extrapolate(
        rows,
        "H_CTP",
        theta_steps[0],
        theta_steps[1],
    )
    g_result = extrapolate(
        rows,
        "g_FS",
        theta_steps[0],
        theta_steps[1],
    )
    h_interval = h_result["interval"]
    g_interval = g_result["interval"]
    primary_d = primary["g_Duhamel_interval"]

    derivative = covariant_difference(theta_steps[1])
    antihermiticity_error = float(
        np.linalg.norm(derivative + derivative.conjugate().T)
    )
    loop_error = float(
        abs(
            np.exp(1j * theta_steps[1] / 3.0) ** 3
            - np.exp(1j * theta_steps[1])
        )
    )
    hermiticity_errors = {
        "free_zero": float(
            np.linalg.norm(free_zero - free_zero.conjugate().T)
        ),
        "interaction_0": float(
            np.linalg.norm(
                interactions[0] - interactions[0].conjugate().T
            )
        ),
        "interaction_1": float(
            np.linalg.norm(
                interactions[1] - interactions[1].conjugate().T
            )
        ),
        "record_0": float(
            np.linalg.norm(records[0] - records[0].conjugate().T)
        ),
        "record_1": float(
            np.linalg.norm(records[1] - records[1].conjugate().T)
        ),
    }

    protected_names = (
        "interacting_continuum_CTP_amplitude_derived",
        "local_Maxwell_response_derived",
        "volume_uniform_zero_free_neighborhood_proved",
        "connected_linked_cluster_density_proved",
        "Duhamel_intensive_Hessian_equality_proved",
        "kappa_record_computed",
        "physical_Thomson_stiffness_computed",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    )
    protected = all(not primary[name] for name in protected_names)

    primary_intervals = (
        primary["H_CTP_interval"],
        primary["g_FS_interval"],
        primary["g_Duhamel_interval"],
    )
    primary_intervals_valid = bool(
        all(strictly_positive(value) for value in primary_intervals)
        and all(
            intervals_overlap(primary_intervals[left], primary_intervals[right])
            for left, right in ((0, 1), (0, 2), (1, 2))
        )
    )
    independent_intervals_valid = bool(
        strictly_positive(h_interval)
        and strictly_positive(g_interval)
        and intervals_overlap(h_interval, g_interval)
        and intervals_overlap(h_interval, primary_d)
        and intervals_overlap(g_interval, primary_d)
    )
    dimensions_valid = bool(
        active_values.shape[0] == 8
        and len(occupied_modes) == 4
        and len(fock_basis) == 70
        and initial.shape[1] == 9
    )
    no_postselection = bool(
        primary["complete_final_identity_used"]
        and not primary["record_outcome_postselected"]
        and not primary["final_source_state_postselected"]
        and not primary["determinant_used"]
    )
    pass_value = bool(
        all(hash_checks.values())
        and primary["overall_verdict"]
        == "FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_PASS"
        and primary["finite_Qspec_holonomy_response_diagnostic_passed"]
        and dimensions_valid
        and antihermiticity_error < 1e-12
        and loop_error < 1e-12
        and max(hermiticity_errors.values()) < 1e-12
        and max(norm_errors.values()) < 2e-9
        and independent_intervals_valid
        and primary_intervals_valid
        and no_postselection
        and protected
        and primary["no_target_access_attestation"]
    )

    formatted_rows = {
        f"N_{steps}_theta_{theta:.8f}": values
        for (steps, theta), values in rows.items()
    }
    result = {
        "schema":
            "complete_qspec_finite_holonomy_response_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "primary_script_sha256": sha256(PRIMARY_SCRIPT),
        "primary_result_sha256": sha256(PRIMARY),
        "verification_method": {
            "CAR_lift": "integer_bitmask_creation_annihilation_parity",
            "time_evolution": "direct_unsplit_RK4",
            "tangent_method": "centered_state_difference_with_Richardson",
            "primary_script_imported": False,
            "verification_is_target_blind": False,
        },
        "hash_checks": hash_checks,
        "dimensions": {
            "active": int(active_values.shape[0]),
            "occupied": len(occupied_modes),
            "fock": len(fock_basis),
            "record": initial.shape[1],
            "pass": dimensions_valid,
        },
        "antihermiticity_error": antihermiticity_error,
        "loop_holonomy_error": loop_error,
        "hermiticity_errors": hermiticity_errors,
        "norm_errors": norm_errors,
        "regulator_subspace_leakage": leakages,
        "raw_responses": formatted_rows,
        "H_CTP_extrapolation": h_result,
        "g_FS_extrapolation": g_result,
        "independent_intervals_valid": independent_intervals_valid,
        "primary_intervals_valid": primary_intervals_valid,
        "primary_Duhamel_interval": primary_d,
        "complete_final_identity_verified": no_postselection,
        "protected_statuses_verified": protected,
        "verdict": (
            "INDEPENDENT_FINITE_QSPEC_HOLONOMY_RESPONSE_CONFIRMED"
            if pass_value
            else "INDEPENDENT_FINITE_QSPEC_HOLONOMY_RESPONSE_BLOCKED"
        ),
        "pass": pass_value,
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
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not pass_value:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
