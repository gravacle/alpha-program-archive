#!/usr/bin/env python3
"""Independent unitary-splitting verifier for temporal-plaquette response."""

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
    / "COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_DIAGNOSTIC_SPEC_V001.md"
)
PRIMARY_SCRIPT = (
    ROOT / "scripts/derive_complete_qspec_temporal_plaquette_response_v001.py"
)
PRIMARY = (
    ROOT / "stage8_execution/work/QSPEC_temporal_plaquette_response_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_temporal_plaquette_response_verification_v001.json"
)

EXPECTED = {
    PROTOCOL:
        "d5ca397a4ced62840a0934d0c9641c7c5f66e9701d35c75a8400a44f20b9a95a",
    SPEC:
        "632aa96ab2b3e5c77d329e4a2f1bbef4eda50e7d6e7b2211a06a0ae372c27909",
    PRIMARY_SCRIPT:
        "c29a7456a6cfb965662678ddee1ee82360d790bab444d38a96c8952496f31e94",
    PRIMARY:
        "0db640eeb1fd5274b89c004791e0f7b9f9c437a70b4ee831316aaea5071b5c6e",
}

PROFILES = {
    "f1": (1.0, 0.0, 0.0),
    "f2": (0.0, 1.0, 0.0),
    "f3": (0.0, 0.0, 1.0),
    "f1_plus_f2": (1.0, 1.0, 0.0),
    "f1_plus_f3": (1.0, 0.0, 1.0),
    "f2_plus_f3": (0.0, 1.0, 1.0),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dirac_data() -> tuple[np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def bitmask_lift(
    one_body: np.ndarray,
    particles: int,
) -> tuple[np.ndarray, tuple[int, ...]]:
    modes = one_body.shape[0]
    basis = tuple(
        sum(1 << mode for mode in occupied)
        for occupied in itertools.combinations(range(modes), particles)
    )
    row_of = {mask: row for row, mask in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), dtype=complex)

    def count(mask: int) -> int:
        return bin(mask).count("1")

    for column, mask in enumerate(basis):
        for removed in range(modes):
            if not mask & (1 << removed):
                continue
            sign_remove = -1 if count(mask & ((1 << removed) - 1)) % 2 else 1
            reduced = mask ^ (1 << removed)
            for added in range(modes):
                if reduced & (1 << added):
                    continue
                sign_add = (
                    -1
                    if count(reduced & ((1 << added) - 1)) % 2
                    else 1
                )
                output = reduced | (1 << added)
                result[row_of[output], column] += (
                    sign_remove
                    * sign_add
                    * one_body[added, removed]
                )
    return result, basis


def record_at_site(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(operator.shape[0], dtype=complex)
    if site == 0:
        return np.kron(operator, identity)
    return np.kron(identity, operator)


def profile(coefficients: tuple[float, float, float], time: float) -> float:
    return sum(
        coefficient
        * math.sin(n * math.pi * time / 2.0)
        / (n * math.pi / 2.0)
        for n, coefficient in enumerate(coefficients, start=1)
    )


def envelope(local_time: float) -> float:
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def apply_free(
    state: np.ndarray,
    vectors: np.ndarray,
    free_cos_values: np.ndarray,
    free_sin_values: np.ndarray,
    theta: float,
    interval: float,
) -> np.ndarray:
    values = (
        math.cos(theta / 3.0) * free_cos_values
        + math.sin(theta / 3.0) * free_sin_values
    )
    coordinates = vectors.conjugate().T @ state
    coordinates *= np.exp(-1j * interval * values)[:, np.newaxis]
    return vectors @ coordinates


def apply_interaction(
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


def strang_cell(
    state: np.ndarray,
    cell: int,
    amplitude: float,
    coefficients: tuple[float, float, float],
    free_vectors: np.ndarray,
    free_cos_values: np.ndarray,
    free_sin_values: np.ndarray,
    source_vectors: np.ndarray,
    source_values: np.ndarray,
    record_vectors: np.ndarray,
    record_values: np.ndarray,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    action = math.pi / math.sqrt(2.0)
    value = state.copy()
    for index in range(steps):
        local_midpoint = (index + 0.5) * dt
        global_midpoint = cell + local_midpoint
        theta = amplitude * profile(coefficients, global_midpoint)
        value = apply_free(
            value,
            free_vectors,
            free_cos_values,
            free_sin_values,
            theta,
            dt / 2.0,
        )
        value = apply_interaction(
            value,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * envelope(local_midpoint) * dt,
        )
        value = apply_free(
            value,
            free_vectors,
            free_cos_values,
            free_sin_values,
            theta,
            dt / 2.0,
        )
    return value


def response(
    zero: np.ndarray,
    plus: np.ndarray,
    minus: np.ndarray,
    amplitude: float,
) -> float:
    z_plus = complex(np.vdot(zero, plus))
    z_minus = complex(np.vdot(zero, minus))
    return (
        -math.log(abs(z_plus))
        - math.log(abs(z_minus))
    ) / (amplitude * amplitude)


def extrapolate(
    rows: dict[tuple[int, float], float],
    coarse_amplitude: float,
    fine_amplitude: float,
) -> dict[str, object]:
    time_limits: dict[float, float] = {}
    time_corrections: dict[float, float] = {}
    for amplitude in (coarse_amplitude, fine_amplitude):
        coarse = rows[(400, amplitude)]
        fine = rows[(800, amplitude)]
        correction = (fine - coarse) / 3.0
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
        "time_corrections": {
            f"{key:.8f}": value
            for key, value in time_corrections.items()
        },
        "amplitude_correction": amplitude_correction,
    }


def overlap(left: list[float], right: list[float]) -> bool:
    return bool(max(left[0], right[0]) <= min(left[1], right[1]))


def contains_zero(interval: list[float]) -> bool:
    return bool(interval[0] <= 0.0 <= interval[1])


def main() -> None:
    hash_checks = {
        str(path.relative_to(ROOT)): sha256(path) == expected
        for path, expected in EXPECTED.items()
    }
    if not all(hash_checks.values()):
        raise RuntimeError("authority hash mismatch")
    primary = json.loads(PRIMARY.read_text())

    alpha_x, incidence_spin = dirac_data()
    shift = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        shift[site, (site + 1) % 3] = 1.0
    difference_cos = (shift - shift.conjugate().T) / 2.0
    difference_sin = 1j * (shift + shift.conjugate().T) / 2.0
    full_cos = np.kron(-1j * difference_cos, alpha_x)
    full_sin = np.kron(-1j * difference_sin, alpha_x)
    source_values, source_vectors = np.linalg.eigh(full_cos)
    active = np.abs(source_values) > 1e-12
    active_values = source_values[active]
    active_vectors = source_vectors[:, active]
    cos_one = active_vectors.conjugate().T @ full_cos @ active_vectors
    sin_one = active_vectors.conjugate().T @ full_sin @ active_vectors
    free_cos, fock_basis = bitmask_lift(cos_one, 4)
    free_sin = bitmask_lift(sin_one, 4)[0]

    free_combo = free_cos + math.sqrt(2.0) * free_sin
    _, free_vectors = np.linalg.eigh(free_combo)
    free_cos_basis = (
        free_vectors.conjugate().T @ free_cos @ free_vectors
    )
    free_sin_basis = (
        free_vectors.conjugate().T @ free_sin @ free_vectors
    )
    simultaneous_diagonalization_errors = {
        "free_cos_offdiagonal": float(
            np.linalg.norm(
                free_cos_basis - np.diag(np.diag(free_cos_basis))
            )
        ),
        "free_sin_offdiagonal": float(
            np.linalg.norm(
                free_sin_basis - np.diag(np.diag(free_sin_basis))
            )
        ),
        "commutator": float(
            np.linalg.norm(free_cos @ free_sin - free_sin @ free_cos)
        ),
    }
    free_cos_values = np.diag(free_cos_basis).real
    free_sin_values = np.diag(free_sin_basis).real

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions = tuple(
        bitmask_lift(
            active_vectors.conjugate().T
            @ np.kron(mask, incidence_spin)
            @ active_vectors,
            4,
        )[0]
        for mask in masks
    )
    source_spectra = tuple(np.linalg.eigh(value) for value in interactions)

    record_seed = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    records = (
        record_at_site(record_seed, 0),
        record_at_site(record_seed, 1),
    )
    record_spectra = tuple(np.linalg.eigh(value) for value in records)

    occupied_modes = [
        index for index, value in enumerate(active_values)
        if value < 0.0
    ]
    occupied_mask = sum(1 << mode for mode in occupied_modes)
    initial_row = fock_basis.index(occupied_mask)
    initial = np.zeros((len(fock_basis), 9), dtype=complex)
    initial[initial_row, 0] = 1.0

    def evolve(
        amplitude: float,
        coefficients: tuple[float, float, float],
        steps: int,
    ) -> np.ndarray:
        state = initial.copy()
        for cell in range(2):
            source_eigenvalues, source_eigenvectors = source_spectra[cell]
            record_eigenvalues, record_eigenvectors = record_spectra[cell]
            state = strang_cell(
                state,
                cell,
                amplitude,
                coefficients,
                free_vectors,
                free_cos_values,
                free_sin_values,
                source_eigenvectors,
                source_eigenvalues,
                record_eigenvectors,
                record_eigenvalues,
                steps,
            )
        return state

    step_values = (400, 800)
    amplitudes = (1.0 / 80.0, 1.0 / 160.0)
    zero_states = {
        steps: evolve(0.0, PROFILES["f1"], steps)
        for steps in step_values
    }
    norm_errors: dict[str, float] = {}
    states: dict[tuple[str, int, float], np.ndarray] = {}
    for steps in step_values:
        norm_errors[f"zero_N_{steps}"] = abs(
            float(np.linalg.norm(zero_states[steps])) - 1.0
        )
        for name, coefficients in PROFILES.items():
            for amplitude in amplitudes:
                for sign in (1.0, -1.0):
                    signed = sign * amplitude
                    state = evolve(signed, coefficients, steps)
                    states[(name, steps, signed)] = state
                    norm_errors[
                        f"{name}_N_{steps}_a_{signed:+.8f}"
                    ] = abs(float(np.linalg.norm(state)) - 1.0)

    extrapolated: dict[str, dict[str, object]] = {}
    raw: dict[str, dict[str, float]] = {}
    for name in PROFILES:
        rows: dict[tuple[int, float], float] = {}
        for steps in step_values:
            for amplitude in amplitudes:
                rows[(steps, amplitude)] = response(
                    zero_states[steps],
                    states[(name, steps, amplitude)],
                    states[(name, steps, -amplitude)],
                    amplitude,
                )
        extrapolated[name] = extrapolate(
            rows,
            amplitudes[0],
            amplitudes[1],
        )
        raw[name] = {
            f"N_{steps}_a_{amplitude:.8f}": value
            for (steps, amplitude), value in rows.items()
        }

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
    for (left, right), name in pair_names.items():
        center[left, right] = center[right, left] = (
            float(extrapolated[name]["limit"])
            - center[left, left]
            - center[right, right]
        ) / 2.0
        radii[left, right] = radii[right, left] = (
            float(extrapolated[name]["radius"])
            + radii[left, left]
            + radii[right, right]
        ) / 2.0

    off_diagonal_intervals = {
        f"f{left + 1}_f{right + 1}": [
            float(center[left, right] - radii[left, right]),
            float(center[left, right] + radii[left, right]),
        ]
        for left, right in pair_names
    }
    diagonal_intervals = [
        extrapolated[name]["interval"] for name in diagonal_names
    ]
    diagonal_common = [
        max(value[0] for value in diagonal_intervals),
        min(value[1] for value in diagonal_intervals),
    ]
    local_form = bool(
        diagonal_common[0] <= diagonal_common[1]
        and all(
            contains_zero(value)
            for value in off_diagonal_intervals.values()
        )
    )

    eigenvalues = np.linalg.eigvalsh(center)
    radius_norm = float(np.linalg.norm(radii, 2))
    certified_minimum = float(eigenvalues[0] - radius_norm)

    profile_endpoint_errors = {
        f"{name}_t_{endpoint:.0f}": abs(profile(coefficients, endpoint))
        for name, coefficients in PROFILES.items()
        for endpoint in (0.0, 2.0)
    }
    endpoint_loop_errors = {
        name: max(
            abs(
                np.exp(
                    1j
                    * amplitudes[0]
                    * profile(coefficients, endpoint)
                )
                - 1.0
            )
            for endpoint in (0.0, 2.0)
        )
        for name, coefficients in PROFILES.items()
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

    primary_profile_intervals = {
        name: primary["extrapolated_profile_responses"][name]["interval"]
        for name in PROFILES
    }
    primary_offdiagonal = primary["off_diagonal_intervals"]
    profile_interval_agreement = {
        name: overlap(
            extrapolated[name]["interval"],
            primary_profile_intervals[name],
        )
        for name in PROFILES
    }
    offdiagonal_interval_agreement = {
        name: overlap(
            interval,
            primary_offdiagonal[name],
        )
        for name, interval in off_diagonal_intervals.items()
    }

    protected = all(
        not primary[name]
        for name in (
            "local_Maxwell_response_derived",
            "interacting_continuum_CTP_amplitude_derived",
            "connected_linked_cluster_density_proved",
            "kappa_record_computed",
            "physical_Thomson_stiffness_computed",
            "coupling_evaluation_authorized",
            "alpha_computed",
            "proof_authorized",
        )
    )
    no_postselection = bool(
        primary["complete_final_identity_used"]
        and not primary["record_outcome_postselected"]
        and not primary["final_source_state_postselected"]
        and not primary["determinant_used"]
    )
    classification_matches = bool(
        local_form
        == primary["finite_temporal_local_Maxwell_form_supported"]
    )
    dimensions_pass = bool(
        active_values.shape[0] == 8
        and len(occupied_modes) == 4
        and len(fock_basis) == 70
        and initial.shape[1] == 9
    )
    pass_value = bool(
        all(hash_checks.values())
        and dimensions_pass
        and max(simultaneous_diagonalization_errors.values()) < 1e-11
        and max(profile_endpoint_errors.values()) < 1e-14
        and max(endpoint_loop_errors.values()) < 1e-14
        and max(hermiticity_errors.values()) < 1e-12
        and max(norm_errors.values()) < 2e-9
        and all(value[0] > 0.0 for value in diagonal_intervals)
        and certified_minimum > 0.0
        and all(profile_interval_agreement.values())
        and all(offdiagonal_interval_agreement.values())
        and classification_matches
        and no_postselection
        and protected
        and primary["no_target_access_attestation"]
    )

    result = {
        "schema":
            "complete_qspec_temporal_plaquette_response_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "primary_script_sha256": sha256(PRIMARY_SCRIPT),
        "primary_result_sha256": sha256(PRIMARY),
        "hash_checks": hash_checks,
        "method": {
            "CAR_lift": "integer_bitmask_creation_annihilation_parity",
            "evolution": "midpoint_unitary_Strang_splitting",
            "free_step": "simultaneously_diagonalized_cos_sin_generators",
            "interaction_step": "exact_source_record_spectral_exponential",
            "primary_script_imported": False,
            "verification_is_target_blind": False,
        },
        "dimensions_pass": dimensions_pass,
        "simultaneous_diagonalization_errors":
            simultaneous_diagonalization_errors,
        "profile_endpoint_errors": profile_endpoint_errors,
        "endpoint_loop_holonomy_errors": endpoint_loop_errors,
        "hermiticity_errors": hermiticity_errors,
        "norm_errors": norm_errors,
        "raw_profile_responses": raw,
        "extrapolated_profile_responses": extrapolated,
        "response_matrix_center": center.tolist(),
        "response_matrix_radii": radii.tolist(),
        "response_matrix_eigenvalues": eigenvalues.tolist(),
        "radius_matrix_operator_norm": radius_norm,
        "certified_minimum_response_eigenvalue": certified_minimum,
        "off_diagonal_intervals": off_diagonal_intervals,
        "diagonal_common_intersection": diagonal_common,
        "profile_interval_agreement": profile_interval_agreement,
        "offdiagonal_interval_agreement": offdiagonal_interval_agreement,
        "local_form_supported": local_form,
        "classification_matches_primary": classification_matches,
        "complete_final_identity_verified": no_postselection,
        "protected_statuses_verified": protected,
        "verdict": (
            "INDEPENDENT_TEMPORAL_PLAQUETTE_RESPONSE_CONFIRMED"
            if pass_value
            else "INDEPENDENT_TEMPORAL_PLAQUETTE_RESPONSE_BLOCKED"
        ),
        "pass": pass_value,
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
                "verdict": result["verdict"],
                "response_matrix_center": center.tolist(),
                "response_matrix_radii": radii.tolist(),
                "certified_minimum_response_eigenvalue":
                    certified_minimum,
                "local_form_supported": local_form,
                "classification_matches_primary": classification_matches,
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not pass_value:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
