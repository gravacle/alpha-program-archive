#!/usr/bin/env python3
"""Independent transfer-derivative verifier for connected-kernel locality."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import derive_complete_qspec_periodic_connected_amplitude_v001 as periodic
import derive_complete_qspec_sequential_relative_history_transfer_map_v002 as core


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    ROOT
    / "COMPLETE_QSPEC_CONNECTED_KERNEL_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
PRIMARY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_connected_kernel_locality_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_connected_kernel_locality_verification_v001.json"
)

EXPECTED = {
    PROTOCOL:
        "349d56e6b884664a8d99aa84c9a2fa2f2d833fa58018bda824bc623932ba09bf",
    ROOT / "COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_SPEC_V001.md":
        "1073e8d7c4aa590d1f45c0d1376b97ae7895181d22e2479ce2af9493f410a6b7",
    ROOT / "scripts/derive_complete_qspec_connected_kernel_locality_v001.py":
        "2795e2b6c9e3176911508445bf13e1145e4cb258361432413939b9c86cbebfcf",
    PRIMARY:
        "f22706d4d2a72c764a35b6e5874a52f25e4bd56ee88dabd9405541cce5b5ea4b",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
}

STEPS = (48, 96)
H_VALUES = (1.0 / 160.0, 1.0 / 320.0)
SEPARATIONS = tuple(range(11))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def apply_supercell(
    value: np.ndarray,
    branch: tuple[tuple[np.ndarray, ...], ...],
    zero: tuple[tuple[np.ndarray, ...], ...],
) -> np.ndarray:
    result = value
    for cell in range(2):
        result = sum(
            left @ result @ right.conjugate().T
            for left, right in zip(branch[cell], zero[cell])
        )
    return result


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")
    primary = json.loads(PRIMARY.read_text())
    parent = periodic.build_parent()
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]

    raw: dict[tuple[int, float, int], float] = {}
    stationarity: dict[int, dict[str, float]] = {}
    for steps in STEPS:
        zero = tuple(
            core.cell_kraus(
                parent["free_zero"],
                interaction,
                record,
                steps,
            )
            for interaction in interactions
        )
        bulk = parent["density"].copy()
        for _ in range(64):
            bulk = apply_supercell(bulk, zero, zero)
        next_bulk = apply_supercell(bulk, zero, zero)
        stationarity[steps] = {
            "trace_error": abs(complex(np.trace(bulk)) - 1.0),
            "one_step_frobenius_change":
                float(np.linalg.norm(next_bulk - bulk)),
        }

        for h_value in H_VALUES:
            branch = {
                multiple: tuple(
                    core.cell_kraus(
                        free(multiple * h_value),
                        interaction,
                        record,
                        steps,
                    )
                    for interaction in interactions
                )
                for multiple in (-2, -1, 1, 2)
            }

            def map_at(multiple: int, value: np.ndarray) -> np.ndarray:
                if multiple == 0:
                    return apply_supercell(value, zero, zero)
                return apply_supercell(value, branch[multiple], zero)

            def first_derivative(value: np.ndarray) -> np.ndarray:
                return (
                    map_at(-2, value)
                    - 8.0 * map_at(-1, value)
                    + 8.0 * map_at(1, value)
                    - map_at(2, value)
                ) / (12.0 * h_value)

            def second_derivative(value: np.ndarray) -> np.ndarray:
                return (
                    -map_at(2, value)
                    + 16.0 * map_at(1, value)
                    - 30.0 * map_at(0, value)
                    + 16.0 * map_at(-1, value)
                    - map_at(-2, value)
                ) / (12.0 * h_value * h_value)

            tangent = first_derivative(bulk)
            z_one = complex(np.trace(tangent))
            raw[(steps, h_value, 0)] = float(
                -np.real(
                    complex(np.trace(second_derivative(bulk)))
                    - z_one * z_one
                )
            )
            for separation in range(1, 11):
                propagated = tangent.copy()
                for _ in range(separation - 1):
                    propagated = apply_supercell(propagated, zero, zero)
                mixed = first_derivative(propagated)
                raw[(steps, h_value, separation)] = float(
                    -np.real(complex(np.trace(mixed)) - z_one * z_one)
                )

    h_limits: dict[tuple[int, int], float] = {}
    h_corrections: dict[tuple[int, int], float] = {}
    for steps in STEPS:
        for separation in SEPARATIONS:
            coarse = raw[(steps, H_VALUES[0], separation)]
            fine = raw[(steps, H_VALUES[1], separation)]
            correction = (fine - coarse) / 15.0
            h_limits[(steps, separation)] = fine + correction
            h_corrections[(steps, separation)] = abs(correction)

    kernels: dict[int, float] = {}
    time_corrections: dict[int, float] = {}
    for separation in SEPARATIONS:
        coarse = h_limits[(STEPS[0], separation)]
        fine = h_limits[(STEPS[1], separation)]
        correction = (fine - coarse) / 3.0
        kernels[separation] = fine + correction
        time_corrections[separation] = abs(correction)

    primary_kernel = {
        int(key): float(value)
        for key, value in primary["mean_connected_kernel"].items()
    }
    primary_relative_differences = {
        separation: abs(
            kernels[separation] - primary_kernel[separation]
        ) / max(abs(primary_kernel[separation]), 1e-7)
        for separation in range(9)
    }
    primary_agreement_pass = (
        max(primary_relative_differences.values()) < 0.02
    )

    fit_rows = [
        separation
        for separation in range(3, 11)
        if abs(kernels[separation]) > 1e-14
    ]
    if len(fit_rows) >= 2:
        x_values = np.array(fit_rows, dtype=float)
        y_values = np.log(
            np.array([abs(kernels[row]) for row in fit_rows])
        )
        slope, intercept = np.polyfit(x_values, y_values, 1)
        predicted = intercept + slope * x_values
        residual_sum = float(np.sum((y_values - predicted) ** 2))
        total_sum = float(np.sum((y_values - np.mean(y_values)) ** 2))
        r_squared = (
            1.0 - residual_sum / total_sum
            if total_sum > 0.0
            else 1.0
        )
        decay_q = float(math.exp(slope))
    else:
        slope = float("nan")
        intercept = float("nan")
        r_squared = float("nan")
        decay_q = float("inf")
    decay_pass = bool(
        len(fit_rows) >= 6
        and decay_q < 0.8
        and r_squared > 0.90
    )

    c8 = -sum(
        separation * separation * kernels[separation]
        for separation in range(1, 9)
    )
    c10 = -sum(
        separation * separation * kernels[separation]
        for separation in range(1, 11)
    )
    c_relative_difference = abs(c10 - c8) / max(abs(c10), 1e-10)
    coefficient_pass = c_relative_difference < 0.05

    fourier: dict[str, dict[str, float]] = {}
    fourier_pass = True
    for cutoff in (8, 10):
        for wave_number in (0.0, math.pi / 16.0, math.pi / 8.0):
            response = kernels[0] + 2.0 * sum(
                kernels[separation]
                * math.cos(wave_number * separation)
                for separation in range(1, cutoff + 1)
            )
            fourier[
                f"R_{cutoff}_k_{wave_number:.12f}"
            ] = {
                "response": float(response),
                "positive": response > 0.0,
            }
            fourier_pass = fourier_pass and response > 0.0

    stationarity_pass = all(
        row["trace_error"] < 1e-10
        and row["one_step_frobenius_change"] < 1e-10
        for row in stationarity.values()
    )
    passed = bool(
        stationarity_pass
        and primary_agreement_pass
        and decay_pass
        and coefficient_pass
        and fourier_pass
    )
    result = {
        "schema":
            "complete_qspec_connected_kernel_locality_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "method":
            "five_point_transfer_derivatives_on_iterated_bulk_state",
        "steps_per_cell": list(STEPS),
        "h_values": list(H_VALUES),
        "stationarity": {
            str(steps): row
            for steps, row in stationarity.items()
        },
        "stationarity_pass": stationarity_pass,
        "raw_kernels": {
            f"steps_{steps}_h_{h_value:.8f}_r_{separation}": value
            for (steps, h_value, separation), value in raw.items()
        },
        "h_corrections": {
            f"steps_{steps}_r_{separation}": value
            for (steps, separation), value in h_corrections.items()
        },
        "time_corrections": {
            str(separation): value
            for separation, value in time_corrections.items()
        },
        "independent_connected_kernel": {
            str(separation): value
            for separation, value in kernels.items()
        },
        "primary_relative_differences": {
            str(separation): value
            for separation, value
            in primary_relative_differences.items()
        },
        "primary_agreement_pass": primary_agreement_pass,
        "decay_fit": {
            "rows": fit_rows,
            "slope": float(slope),
            "intercept": float(intercept),
            "q": decay_q,
            "r_squared": r_squared,
            "pass": decay_pass,
        },
        "low_frequency_quadratic_coefficient": {
            "C8": float(c8),
            "C10": float(c10),
            "relative_difference": float(c_relative_difference),
            "pass": coefficient_pass,
        },
        "truncated_fourier_responses": fourier,
        "fourier_positivity_pass": fourier_pass,
        "verdict": (
            "INDEPENDENT_PERIODIC_CONNECTED_KERNEL_LOCALITY_CONFIRMED"
            if passed
            else "INDEPENDENT_PERIODIC_CONNECTED_KERNEL_LOCALITY_BLOCKED"
        ),
        "pass": passed,
        "periodic_connected_kernel_locality_diagnostic_passed": passed,
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
                "stationarity_pass": stationarity_pass,
                "maximum_primary_relative_difference":
                    max(primary_relative_differences.values()),
                "decay_fit": result["decay_fit"],
                "low_frequency_quadratic_coefficient":
                    result["low_frequency_quadratic_coefficient"],
                "fourier_positivity_pass": fourier_pass,
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
