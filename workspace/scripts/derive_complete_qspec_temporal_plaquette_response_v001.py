#!/usr/bin/env python3
"""Evaluate the sealed endpoint-trivial temporal-plaquette diagnostic."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_DIAGNOSTIC_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_temporal_plaquette_response_v001.json"
)

EXPECTED = {
    SPEC:
        "632aa96ab2b3e5c77d329e4a2f1bbef4eda50e7d6e7b2211a06a0ae372c27909",
    ROOT / "COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_RESULT_V001.md":
        "69fa91955337a0b9c74aa4d4bbb78e42bc9d1e825eef4b5c47585742885db106",
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

PROFILE_COEFFICIENTS = {
    "f1": (1.0, 0.0, 0.0),
    "f2": (0.0, 1.0, 0.0),
    "f3": (0.0, 0.0, 1.0),
    "f1_plus_f2": (1.0, 1.0, 0.0),
    "f1_plus_f3": (1.0, 0.0, 1.0),
    "f2_plus_f3": (0.0, 1.0, 1.0),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def dirac_operators() -> tuple[np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma_zero = np.block([[identity, zero], [zero, -identity]])
    gamma_space = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma_five = (
        1j
        * gamma_zero
        @ gamma_space[0]
        @ gamma_space[1]
        @ gamma_space[2]
    )
    return gamma_zero @ gamma_space[0], -1j * gamma_zero @ gamma_five


def covariant_difference(theta: float) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    phase = np.exp(1j * theta / 3.0)
    for site in range(3):
        matrix[site, (site + 1) % 3] += phase / 2.0
        matrix[site, (site - 1) % 3] -= phase.conjugate() / 2.0
    return matrix


def particle_lift(
    one_body: np.ndarray,
    particle_count: int,
) -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    dimension = one_body.shape[0]
    basis = tuple(
        itertools.combinations(range(dimension), particle_count)
    )
    lookup = {occupation: row for row, occupation in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, occupation in enumerate(basis):
        for q_position, q_mode in enumerate(occupation):
            reduced = list(occupation)
            reduced.pop(q_position)
            q_sign = -1 if q_position % 2 else 1
            for p_mode in range(dimension):
                if p_mode in reduced:
                    continue
                p_position = sum(mode < p_mode for mode in reduced)
                p_sign = -1 if p_position % 2 else 1
                output = tuple(sorted((*reduced, p_mode)))
                result[lookup[output], column] += (
                    q_sign
                    * p_sign
                    * one_body[p_mode, q_mode]
                )
    return result, basis


def record_on_site(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(operator.shape[0], dtype=complex)
    return (
        np.kron(operator, identity)
        if site == 0
        else np.kron(identity, operator)
    )


def profile_value(coefficients: tuple[float, float, float], time: float) -> float:
    value = 0.0
    for n, coefficient in enumerate(coefficients, start=1):
        frequency = n * math.pi / 2.0
        value += coefficient * math.sin(frequency * time) / frequency
    return value


def causal_weight(local_time: float) -> float:
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def integrate_cell(
    state: np.ndarray,
    cell_index: int,
    amplitude: float,
    coefficients: tuple[float, float, float],
    free_cos: np.ndarray,
    free_sin: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    action = math.pi / math.sqrt(2.0)

    def rhs(
        value: np.ndarray,
        local_time: float,
    ) -> np.ndarray:
        global_time = cell_index + local_time
        theta = amplitude * profile_value(coefficients, global_time)
        free = (
            math.cos(theta / 3.0) * free_cos
            + math.sin(theta / 3.0) * free_sin
        )
        strength = action * causal_weight(local_time)
        return -1j * (
            free @ value
            + strength * interaction @ value @ record.T
        )

    value = state.copy()
    for index in range(steps):
        time = index * dt
        k1 = rhs(value, time)
        k2 = rhs(value + 0.5 * dt * k1, time + 0.5 * dt)
        k3 = rhs(value + 0.5 * dt * k2, time + 0.5 * dt)
        k4 = rhs(value + dt * k3, time + dt)
        value += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return value


def response_hessian(
    zero_state: np.ndarray,
    plus_state: np.ndarray,
    minus_state: np.ndarray,
    amplitude: float,
) -> dict[str, float]:
    z_plus = complex(np.vdot(zero_state, plus_state))
    z_minus = complex(np.vdot(zero_state, minus_state))
    hessian = (
        -math.log(abs(z_plus))
        - math.log(abs(z_minus))
    ) / (amplitude * amplitude)
    return {
        "Z_plus_real": z_plus.real,
        "Z_plus_imag": z_plus.imag,
        "Z_plus_absolute": abs(z_plus),
        "Z_minus_real": z_minus.real,
        "Z_minus_imag": z_minus.imag,
        "Z_minus_absolute": abs(z_minus),
        "H_response": hessian,
    }


def extrapolate(
    rows: dict[tuple[int, float], dict[str, float]],
    coarse_amplitude: float,
    fine_amplitude: float,
) -> dict[str, object]:
    time_limits: dict[float, float] = {}
    time_corrections: dict[float, float] = {}
    for amplitude in (coarse_amplitude, fine_amplitude):
        coarse = rows[(800, amplitude)]["H_response"]
        fine = rows[(1600, amplitude)]["H_response"]
        correction = (fine - coarse) / 15.0
        time_limits[amplitude] = fine + correction
        time_corrections[amplitude] = abs(correction)
    amplitude_correction = (
        time_limits[fine_amplitude]
        - time_limits[coarse_amplitude]
    ) / 3.0
    limit = time_limits[fine_amplitude] + amplitude_correction
    radius = (
        max(time_corrections.values())
        + abs(amplitude_correction)
        + 1e-8
    )
    return {
        "limit": limit,
        "radius": radius,
        "interval": [limit - radius, limit + radius],
        "time_limits": {
            f"{amplitude:.8f}": value
            for amplitude, value in time_limits.items()
        },
        "time_corrections": {
            f"{amplitude:.8f}": value
            for amplitude, value in time_corrections.items()
        },
        "amplitude_correction": amplitude_correction,
    }


def contains_zero(interval: list[float]) -> bool:
    return interval[0] <= 0.0 <= interval[1]


def main() -> None:
    for path, expected in EXPECTED.items():
        require(sha256(path) == expected, f"authority drift: {path.name}")

    alpha_x, incidence_spin = dirac_operators()
    forward = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        forward[site, (site + 1) % 3] = 1.0
    backward = forward.conjugate().T
    difference_cos = (forward - backward) / 2.0
    difference_sin = 1j * (forward + backward) / 2.0
    full_free_cos = np.kron(-1j * difference_cos, alpha_x)
    full_free_sin = np.kron(-1j * difference_sin, alpha_x)

    eigenvalues, eigenvectors = np.linalg.eigh(full_free_cos)
    active = np.abs(eigenvalues) > 1e-12
    active_values = eigenvalues[active]
    active_vectors = eigenvectors[:, active]
    require(active_values.shape[0] == 8, "wrong active dimension")
    require(np.count_nonzero(active_values < 0.0) == 4, "wrong occupied rank")

    free_cos_one = (
        active_vectors.conjugate().T
        @ full_free_cos
        @ active_vectors
    )
    free_sin_one = (
        active_vectors.conjugate().T
        @ full_free_sin
        @ active_vectors
    )
    free_cos, basis = particle_lift(free_cos_one, 4)
    free_sin = particle_lift(free_sin_one, 4)[0]

    source_masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions = tuple(
        particle_lift(
            active_vectors.conjugate().T
            @ np.kron(mask, incidence_spin)
            @ active_vectors,
            4,
        )[0]
        for mask in source_masks
    )
    record_seed = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    records = (
        record_on_site(record_seed, 0),
        record_on_site(record_seed, 1),
    )

    occupied = tuple(
        index for index, value in enumerate(active_values)
        if value < 0.0
    )
    initial_source = basis.index(occupied)
    initial = np.zeros((len(basis), 9), dtype=complex)
    initial[initial_source, 0] = 1.0

    def evolve(
        amplitude: float,
        coefficients: tuple[float, float, float],
        steps: int,
    ) -> np.ndarray:
        state = initial.copy()
        for cell, (interaction, record) in enumerate(
            zip(interactions, records)
        ):
            state = integrate_cell(
                state,
                cell,
                amplitude,
                coefficients,
                free_cos,
                free_sin,
                interaction,
                record,
                steps,
            )
        return state

    step_values = (800, 1600)
    amplitude_values = (1.0 / 80.0, 1.0 / 160.0)
    zero_states = {
        steps: evolve(0.0, PROFILE_COEFFICIENTS["f1"], steps)
        for steps in step_values
    }
    states: dict[tuple[str, int, float], np.ndarray] = {}
    norm_errors: dict[str, float] = {}
    for steps in step_values:
        norm_errors[f"zero_N_{steps}"] = abs(
            float(np.linalg.norm(zero_states[steps])) - 1.0
        )
        for name, coefficients in PROFILE_COEFFICIENTS.items():
            for amplitude in amplitude_values:
                for sign in (1.0, -1.0):
                    signed = sign * amplitude
                    state = evolve(signed, coefficients, steps)
                    states[(name, steps, signed)] = state
                    norm_errors[
                        f"{name}_N_{steps}_a_{signed:+.8f}"
                    ] = abs(float(np.linalg.norm(state)) - 1.0)

    raw: dict[str, dict[tuple[int, float], dict[str, float]]] = {}
    extrapolated: dict[str, dict[str, object]] = {}
    for name in PROFILE_COEFFICIENTS:
        rows: dict[tuple[int, float], dict[str, float]] = {}
        for steps in step_values:
            for amplitude in amplitude_values:
                rows[(steps, amplitude)] = response_hessian(
                    zero_states[steps],
                    states[(name, steps, amplitude)],
                    states[(name, steps, -amplitude)],
                    amplitude,
                )
        raw[name] = rows
        extrapolated[name] = extrapolate(
            rows,
            amplitude_values[0],
            amplitude_values[1],
        )

    diagonal_names = ("f1", "f2", "f3")
    pair_names = {
        (0, 1): "f1_plus_f2",
        (0, 2): "f1_plus_f3",
        (1, 2): "f2_plus_f3",
    }
    center = np.zeros((3, 3), dtype=float)
    radii = np.zeros((3, 3), dtype=float)
    for index, name in enumerate(diagonal_names):
        center[index, index] = float(extrapolated[name]["limit"])
        radii[index, index] = float(extrapolated[name]["radius"])
    for (left, right), pair_name in pair_names.items():
        value = (
            float(extrapolated[pair_name]["limit"])
            - center[left, left]
            - center[right, right]
        ) / 2.0
        radius = (
            float(extrapolated[pair_name]["radius"])
            + radii[left, left]
            + radii[right, right]
        ) / 2.0
        center[left, right] = center[right, left] = value
        radii[left, right] = radii[right, left] = radius

    eigenvalues_center = np.linalg.eigvalsh(center)
    radius_operator_norm = float(np.linalg.norm(radii, 2))
    certified_minimum = float(eigenvalues_center[0] - radius_operator_norm)

    diagonal_intervals = [
        extrapolated[name]["interval"] for name in diagonal_names
    ]
    off_diagonal_intervals: dict[str, list[float]] = {}
    for (left, right), _ in pair_names.items():
        key = f"f{left + 1}_f{right + 1}"
        off_diagonal_intervals[key] = [
            center[left, right] - radii[left, right],
            center[left, right] + radii[left, right],
        ]
    diagonal_common_intersection = [
        max(interval[0] for interval in diagonal_intervals),
        min(interval[1] for interval in diagonal_intervals),
    ]
    local_form_supported = bool(
        diagonal_common_intersection[0]
        <= diagonal_common_intersection[1]
        and all(
            contains_zero(interval)
            for interval in off_diagonal_intervals.values()
        )
    )

    endpoint_errors: dict[str, float] = {}
    for name, coefficients in PROFILE_COEFFICIENTS.items():
        for endpoint in (0.0, 2.0):
            endpoint_errors[f"{name}_t_{endpoint:.0f}"] = abs(
                profile_value(coefficients, endpoint)
            )
    zero_overlap_errors = {
        str(steps): abs(
            complex(np.vdot(zero_states[steps], zero_states[steps])) - 1.0
        )
        for steps in step_values
    }

    theta_probe = (
        amplitude_values[0]
        * max(
            abs(profile_value(coefficients, time))
            for coefficients in PROFILE_COEFFICIENTS.values()
            for time in np.linspace(0.0, 2.0, 401)
        )
    )
    derivative_probe = covariant_difference(theta_probe)
    antihermiticity_error = float(
        np.linalg.norm(
            derivative_probe + derivative_probe.conjugate().T
        )
    )
    endpoint_loop_errors = {
        name: max(
            abs(
                np.exp(
                    1j
                    * amplitude_values[0]
                    * profile_value(coefficients, endpoint)
                )
                - 1.0
            )
            for endpoint in (0.0, 2.0)
        )
        for name, coefficients in PROFILE_COEFFICIENTS.items()
    }
    hermiticity_errors = {
        "free_cos": float(
            np.linalg.norm(free_cos - free_cos.conjugate().T)
        ),
        "free_sin": float(
            np.linalg.norm(free_sin - free_sin.conjugate().T)
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
    temporal_response_present = bool(
        max(endpoint_errors.values()) < 1e-14
        and max(endpoint_loop_errors.values()) < 1e-14
        and antihermiticity_error < 1e-12
        and max(hermiticity_errors.values()) < 1e-12
        and max(norm_errors.values()) < 2e-9
        and max(zero_overlap_errors.values()) < 2e-9
        and all(interval[0] > 0.0 for interval in diagonal_intervals)
        and certified_minimum > 0.0
    )

    formatted_raw = {
        name: {
            f"N_{steps}_a_{amplitude:.8f}": values
            for (steps, amplitude), values in rows.items()
        }
        for name, rows in raw.items()
    }
    result = {
        "schema": "complete_qspec_temporal_plaquette_response_v001",
        "spec_sha256": sha256(SPEC),
        "profile_definition":
            "f_n(t)=sin(n*pi*t/2)/(n*pi/2), n=1,2,3",
        "profile_derivative_gram": [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ],
        "profile_endpoint_errors": endpoint_errors,
        "endpoint_loop_holonomy_errors": endpoint_loop_errors,
        "connection_antihermiticity_error": antihermiticity_error,
        "hermiticity_errors": hermiticity_errors,
        "dimensions": {
            "active": int(active_values.shape[0]),
            "occupied": len(occupied),
            "fock": len(basis),
            "record": initial.shape[1],
        },
        "norm_errors": norm_errors,
        "zero_overlap_errors": zero_overlap_errors,
        "raw_profile_responses": formatted_raw,
        "extrapolated_profile_responses": extrapolated,
        "temporal_response_matrix_center": center.tolist(),
        "temporal_response_matrix_radii": radii.tolist(),
        "temporal_response_matrix_center_eigenvalues":
            eigenvalues_center.tolist(),
        "radius_matrix_operator_norm": radius_operator_norm,
        "certified_minimum_response_eigenvalue": certified_minimum,
        "diagonal_common_intersection": diagonal_common_intersection,
        "off_diagonal_intervals": off_diagonal_intervals,
        "curvature_response_verdict": (
            "FINITE_TEMPORAL_PLAQUETTE_RESPONSE_PRESENT"
            if temporal_response_present
            else "FINITE_TEMPORAL_PLAQUETTE_RESPONSE_BLOCKED"
        ),
        "local_Maxwell_form_verdict": (
            "FINITE_TEMPORAL_LOCAL_MAXWELL_FORM_SUPPORTED"
            if local_form_supported
            else "FINITE_TEMPORAL_RESPONSE_NONLOCAL_OR_INHOMOGENEOUS"
        ),
        "finite_temporal_plaquette_response_computed":
            temporal_response_present,
        "finite_temporal_local_Maxwell_form_supported":
            local_form_supported,
        "complete_final_identity_used": True,
        "record_outcome_postselected": False,
        "final_source_state_postselected": False,
        "determinant_used": False,
        "open_tree_zero_stiffness_retained": True,
        "no_target_access_attestation": True,
        "complete_Qspec_CTP_scalar_closure_derived": True,
        "finite_Qspec_holonomy_response_diagnostic_passed": True,
        "local_Maxwell_response_derived": False,
        "interacting_continuum_CTP_amplitude_derived": False,
        "connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "curvature_response_verdict":
                    result["curvature_response_verdict"],
                "local_Maxwell_form_verdict":
                    result["local_Maxwell_form_verdict"],
                "response_matrix_center": center.tolist(),
                "response_matrix_radii": radii.tolist(),
                "certified_minimum_response_eigenvalue":
                    certified_minimum,
                "alpha_computed": False,
                "proof_authorized": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not temporal_response_present:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
