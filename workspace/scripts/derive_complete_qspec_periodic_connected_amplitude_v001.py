#!/usr/bin/env python3
"""Connected period-two transfer regression for the complete-Qspec parent."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import derive_complete_qspec_relative_history_transfer_map_v001 as core


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_connected_amplitude_v001.json"
)

EXPECTED = {
    SPEC:
        "ab5f44b8dfcab84ee25964f4184d8b5ca4599b85de2e4af603ab54dd3d353a81",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md":
        "7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef",
    ROOT / "scripts/derive_complete_qspec_relative_history_transfer_map_v001.py":
        "3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1",
    ROOT / "stage8_execution/work/QSPEC_relative_history_transfer_map_v001.json":
        "b202278190c5e440713abbea247fcfcb92c1dc4fba1a1b08d8db648f3579caaf",
    ROOT / "scripts/verify_complete_qspec_relative_history_transfer_map_v001.py":
        "0a928509699a6d2a827c95bce7311e438e49424c22fc88142b1578d67a2368f6",
    ROOT
    / "stage8_execution/work/"
    "QSPEC_relative_history_transfer_map_verification_v001.json":
        "868e14f16e75e17cfd7b50112354ec911286789fd4e482cec1931e956fd6b5e0",
}

SCHEDULE = (1, 2, 4, 8, 16, 32)
STEP_VALUES = (32, 64)
THETA_VALUES = (1.0 / 20.0, 1.0 / 40.0)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_parent() -> dict[str, object]:
    alpha_x, incidence_spin = core.dirac_operators()
    full_zero = np.kron(
        -1j * core.covariant_difference(0.0),
        alpha_x,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(full_zero)
    active = np.abs(eigenvalues) > 1e-12
    active_values = eigenvalues[active]
    active_vectors = eigenvectors[:, active]

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    interactions = tuple(
        core.dgamma(
            active_vectors.conjugate().T
            @ np.kron(mask, incidence_spin)
            @ active_vectors,
            4,
        )[0]
        for mask in masks
    )
    free_zero, basis = core.dgamma(np.diag(active_values), 4)
    occupied = tuple(
        index for index, value in enumerate(active_values)
        if value < 0.0
    )
    source_row = basis.index(occupied)
    source_vector = np.zeros(len(basis), dtype=complex)
    source_vector[source_row] = 1.0
    density = np.outer(source_vector, source_vector.conjugate())
    record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )

    def free(theta: float) -> np.ndarray:
        full = np.kron(
            -1j * core.covariant_difference(theta),
            alpha_x,
        )
        one_body = active_vectors.conjugate().T @ full @ active_vectors
        return core.dgamma(one_body, 4)[0]

    return {
        "active_dimension": int(active_values.shape[0]),
        "source_dimension": len(basis),
        "record_dimension": 3,
        "density": density,
        "interactions": interactions,
        "record": record,
        "free": free,
        "free_zero": free_zero,
    }


def iterate_supercells(
    initial: np.ndarray,
    plus: tuple[tuple[np.ndarray, ...], ...],
    minus: tuple[tuple[np.ndarray, ...], ...],
) -> dict[int, complex]:
    value = initial.copy()
    rows: dict[int, complex] = {}
    for supercell in range(1, max(SCHEDULE) + 1):
        for cell in range(2):
            value = core.compose_cross_map(
                value,
                plus[cell],
                minus[cell],
            )
        if supercell in SCHEDULE:
            rows[supercell] = complex(np.trace(value))
    return rows


def extrapolate(
    raw: dict[tuple[int, float, int], float],
    supercells: int,
) -> dict[str, object]:
    time_limits: dict[float, float] = {}
    time_corrections: dict[float, float] = {}
    for theta in THETA_VALUES:
        coarse = raw[(STEP_VALUES[0], theta, supercells)]
        fine = raw[(STEP_VALUES[1], theta, supercells)]
        correction = (fine - coarse) / 3.0
        time_limits[theta] = fine + correction
        time_corrections[theta] = abs(correction)
    theta_correction = (
        time_limits[THETA_VALUES[1]]
        - time_limits[THETA_VALUES[0]]
    ) / 3.0
    limit = time_limits[THETA_VALUES[1]] + theta_correction
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
            f"{key:.8f}": value
            for key, value in time_limits.items()
        },
        "time_corrections": {
            f"{key:.8f}": value
            for key, value in time_corrections.items()
        },
        "theta_correction": theta_correction,
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")

    parent = build_parent()
    density = parent["density"]
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]

    amplitudes: dict[
        tuple[int, float, int],
        dict[str, complex],
    ] = {}
    diagonal_errors: dict[str, float] = {}
    minimum_amplitude = 1.0

    for steps in STEP_VALUES:
        zero_kraus = tuple(
            core.cell_kraus(
                parent["free_zero"],
                interaction,
                record,
                steps,
            )
            for interaction in interactions
        )
        diagonal = iterate_supercells(density, zero_kraus, zero_kraus)
        for count, value in diagonal.items():
            diagonal_errors[f"N_{count}_steps_{steps}"] = abs(value - 1.0)

        for theta in THETA_VALUES:
            plus_kraus = tuple(
                core.cell_kraus(
                    free(theta),
                    interaction,
                    record,
                    steps,
                )
                for interaction in interactions
            )
            minus_kraus = tuple(
                core.cell_kraus(
                    free(-theta),
                    interaction,
                    record,
                    steps,
                )
                for interaction in interactions
            )
            positive = iterate_supercells(
                density,
                plus_kraus,
                zero_kraus,
            )
            negative = iterate_supercells(
                density,
                minus_kraus,
                zero_kraus,
            )
            for count in SCHEDULE:
                amplitudes[(steps, theta, count)] = {
                    "plus": positive[count],
                    "minus": negative[count],
                }
                minimum_amplitude = min(
                    minimum_amplitude,
                    abs(positive[count]),
                    abs(negative[count]),
                )

    raw_response: dict[tuple[int, float, int], float] = {}
    for (steps, theta, count), branches in amplitudes.items():
        extensive = (
            -np.log(abs(branches["plus"]))
            - np.log(abs(branches["minus"]))
        ) / (theta * theta)
        raw_response[(steps, theta, count)] = float(
            extensive / (2 * count)
        )

    extrapolated = {
        count: extrapolate(raw_response, count)
        for count in SCHEDULE
    }
    tail_8_16 = abs(
        float(extrapolated[16]["limit"])
        - float(extrapolated[8]["limit"])
    )
    tail_16_32 = abs(
        float(extrapolated[32]["limit"])
        - float(extrapolated[16]["limit"])
    )
    passed = bool(
        minimum_amplitude > 1e-14
        and max(diagonal_errors.values()) < 1e-9
        and all(
            value["interval"][0] > 0.0
            for value in extrapolated.values()
        )
        and tail_16_32 < tail_8_16
        and tail_16_32 < 1e-6
    )

    formatted_amplitudes = {
        f"steps_{steps}_theta_{theta:.8f}_N_{count}": {
            "plus_real": branches["plus"].real,
            "plus_imag": branches["plus"].imag,
            "plus_absolute": abs(branches["plus"]),
            "minus_real": branches["minus"].real,
            "minus_imag": branches["minus"].imag,
            "minus_absolute": abs(branches["minus"]),
        }
        for (steps, theta, count), branches in amplitudes.items()
    }
    formatted_raw = {
        f"steps_{steps}_theta_{theta:.8f}_N_{count}": value
        for (steps, theta, count), value in raw_response.items()
    }
    result = {
        "schema": "complete_qspec_periodic_connected_amplitude_v001",
        "spec_sha256": sha256(SPEC),
        "regression_scope": {
            "supercell": "two_frozen_source_masks_repeated_causally",
            "physical_continuum_exhaustion_claimed": False,
            "fresh_record_per_cell": True,
            "closed_record_return_interaction": False,
            "full_record_Hilbert_space_built": False,
        },
        "dimensions": {
            "active": parent["active_dimension"],
            "source": parent["source_dimension"],
            "single_record": parent["record_dimension"],
            "maximum_implicit_record_dimension": f"3^{2 * max(SCHEDULE)}",
            "propagated_cross_density_shape": [
                parent["source_dimension"],
                parent["source_dimension"],
            ],
        },
        "schedule": list(SCHEDULE),
        "steps_per_cell": list(STEP_VALUES),
        "theta_values": list(THETA_VALUES),
        "minimum_tested_amplitude_absolute": minimum_amplitude,
        "diagonal_normalization_errors": diagonal_errors,
        "amplitudes": formatted_amplitudes,
        "raw_intensive_responses": formatted_raw,
        "extrapolated_intensive_responses": {
            str(key): value for key, value in extrapolated.items()
        },
        "tail_differences": {
            "N8_to_N16": tail_8_16,
            "N16_to_N32": tail_16_32,
            "decreasing": tail_16_32 < tail_8_16,
            "final_below_1e-6": tail_16_32 < 1e-6,
        },
        "verdict": (
            "PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_PASS"
            if passed
            else "PERIODIC_CONNECTED_AMPLITUDE_DIAGNOSTIC_BLOCKED"
        ),
        "pass": passed,
        "relative_history_transfer_map_derived": True,
        "periodic_connected_amplitude_constructed": True,
        "periodic_intensive_limit_diagnostic_passed": passed,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "local_Maxwell_response_derived": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "minimum_tested_amplitude_absolute": minimum_amplitude,
                "intensive_limits": {
                    str(count): extrapolated[count]["limit"]
                    for count in SCHEDULE
                },
                "tail_differences": result["tail_differences"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
