#!/usr/bin/env python3
"""Connected-kernel locality diagnostic for the period-two Qspec regulator."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import derive_complete_qspec_periodic_connected_amplitude_v001 as periodic
import derive_complete_qspec_sequential_relative_history_transfer_map_v002 as core


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_connected_kernel_locality_v001.json"
)

EXPECTED = {
    SPEC:
        "1073e8d7c4aa590d1f45c0d1376b97ae7895181d22e2479ce2af9493f410a6b7",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
    ROOT / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_RESULT_V001.md":
        "b7f5f0f29c69c14b3cfd6afba285c437ff0c2cb285c2f29f4ce3fb576bdfff48",
    ROOT
    / "scripts/"
    "derive_complete_qspec_sequential_relative_history_transfer_map_v002.py":
        "954f9ca6d6f70cf893748216ceb8b489eba28618e1637afd6c02be3f79be7aa5",
    ROOT / "scripts/derive_complete_qspec_periodic_connected_amplitude_v001.py":
        "d109fc1ad7e7c65292631a1eafafe07d53c946f153521994be8e57315732fdec",
}

STEPS = (32, 64)
EPSILONS = (1.0 / 40.0, 1.0 / 80.0)
ANCHORS = (16, 32)
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


def amplitude(
    prefix: np.ndarray,
    first: tuple[tuple[np.ndarray, ...], ...],
    second: tuple[tuple[np.ndarray, ...], ...] | None,
    zero: tuple[tuple[np.ndarray, ...], ...],
    separation: int,
) -> complex:
    value = apply_supercell(prefix, first, zero)
    if separation > 0:
        for _ in range(separation - 1):
            value = apply_supercell(value, zero, zero)
        if second is None:
            raise RuntimeError("missing second perturbation")
        value = apply_supercell(value, second, zero)
    return complex(np.trace(value))


def gamma(value: complex) -> float:
    absolute = abs(value)
    if absolute <= 0.0:
        return float("inf")
    return -math.log(absolute)


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")

    parent = periodic.build_parent()
    density = parent["density"]
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]

    raw: dict[tuple[int, float, int, int], float] = {}
    raw_amplitudes: dict[str, dict[str, float]] = {}
    minimum_amplitude = 1.0

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
        prefixes: dict[int, np.ndarray] = {}
        value = density.copy()
        for index in range(max(ANCHORS) + 1):
            if index in ANCHORS:
                prefixes[index] = value.copy()
            value = apply_supercell(value, zero, zero)

        for epsilon in EPSILONS:
            branches = {
                sign: tuple(
                    core.cell_kraus(
                        free(sign * epsilon),
                        interaction,
                        record,
                        steps,
                    )
                    for interaction in interactions
                )
                for sign in (-1, 1)
            }
            for anchor in ANCHORS:
                prefix = prefixes[anchor]
                for separation in SEPARATIONS:
                    if separation == 0:
                        plus = amplitude(
                            prefix,
                            branches[1],
                            None,
                            zero,
                            0,
                        )
                        minus = amplitude(
                            prefix,
                            branches[-1],
                            None,
                            zero,
                            0,
                        )
                        minimum_amplitude = min(
                            minimum_amplitude,
                            abs(plus),
                            abs(minus),
                        )
                        kernel = (
                            gamma(plus) + gamma(minus)
                        ) / (epsilon * epsilon)
                        raw_amplitudes[
                            f"steps_{steps}_eps_{epsilon:.8f}_"
                            f"anchor_{anchor}_r_0"
                        ] = {
                            "plus_absolute": abs(plus),
                            "minus_absolute": abs(minus),
                        }
                    else:
                        values: dict[tuple[int, int], complex] = {}
                        for first_sign in (-1, 1):
                            for second_sign in (-1, 1):
                                values[(first_sign, second_sign)] = amplitude(
                                    prefix,
                                    branches[first_sign],
                                    branches[second_sign],
                                    zero,
                                    separation,
                                )
                        minimum_amplitude = min(
                            minimum_amplitude,
                            *(abs(item) for item in values.values()),
                        )
                        kernel = (
                            gamma(values[(1, 1)])
                            - gamma(values[(1, -1)])
                            - gamma(values[(-1, 1)])
                            + gamma(values[(-1, -1)])
                        ) / (4.0 * epsilon * epsilon)
                        raw_amplitudes[
                            f"steps_{steps}_eps_{epsilon:.8f}_"
                            f"anchor_{anchor}_r_{separation}"
                        ] = {
                            f"{first:+d}_{second:+d}_absolute":
                                abs(values[(first, second)])
                            for first in (-1, 1)
                            for second in (-1, 1)
                        }
                    raw[(steps, epsilon, anchor, separation)] = float(kernel)

    time_limits: dict[tuple[float, int, int], float] = {}
    time_corrections: dict[tuple[float, int, int], float] = {}
    for epsilon in EPSILONS:
        for anchor in ANCHORS:
            for separation in SEPARATIONS:
                coarse = raw[(STEPS[0], epsilon, anchor, separation)]
                fine = raw[(STEPS[1], epsilon, anchor, separation)]
                correction = (fine - coarse) / 3.0
                time_limits[(epsilon, anchor, separation)] = (
                    fine + correction
                )
                time_corrections[(epsilon, anchor, separation)] = abs(
                    correction
                )

    kernels: dict[tuple[int, int], float] = {}
    epsilon_corrections: dict[tuple[int, int], float] = {}
    for anchor in ANCHORS:
        for separation in SEPARATIONS:
            coarse = time_limits[
                (EPSILONS[0], anchor, separation)
            ]
            fine = time_limits[
                (EPSILONS[1], anchor, separation)
            ]
            correction = (fine - coarse) / 3.0
            kernels[(anchor, separation)] = fine + correction
            epsilon_corrections[(anchor, separation)] = abs(correction)

    means = {
        separation: float(
            sum(kernels[(anchor, separation)] for anchor in ANCHORS)
            / len(ANCHORS)
        )
        for separation in SEPARATIONS
    }
    anchor_relative_differences = {
        separation: abs(
            kernels[(ANCHORS[0], separation)]
            - kernels[(ANCHORS[1], separation)]
        ) / max(abs(means[separation]), 1e-8)
        for separation in range(9)
    }
    anchor_pass = max(anchor_relative_differences.values()) < 0.05

    fit_rows = [
        separation
        for separation in range(3, 11)
        if abs(means[separation]) > 1e-14
    ]
    if len(fit_rows) >= 2:
        x_values = np.array(fit_rows, dtype=float)
        y_values = np.log(
            np.array([abs(means[row]) for row in fit_rows])
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
        separation * separation * means[separation]
        for separation in range(1, 9)
    )
    c10 = -sum(
        separation * separation * means[separation]
        for separation in range(1, 11)
    )
    c_relative_difference = abs(c10 - c8) / max(abs(c10), 1e-10)
    coefficient_pass = c_relative_difference < 0.05

    fourier: dict[str, dict[str, float]] = {}
    fourier_pass = True
    for cutoff in (8, 10):
        for wave_number in (0.0, math.pi / 16.0, math.pi / 8.0):
            response = means[0] + 2.0 * sum(
                means[separation]
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

    passed = bool(
        minimum_amplitude > 1e-8
        and anchor_pass
        and decay_pass
        and coefficient_pass
        and fourier_pass
    )
    result = {
        "schema": "complete_qspec_connected_kernel_locality_v001",
        "spec_sha256": sha256(SPEC),
        "steps_per_cell": list(STEPS),
        "epsilons": list(EPSILONS),
        "anchors": list(ANCHORS),
        "separations": list(SEPARATIONS),
        "minimum_amplitude_absolute": minimum_amplitude,
        "raw_amplitudes": raw_amplitudes,
        "raw_kernels": {
            f"steps_{steps}_eps_{epsilon:.8f}_anchor_{anchor}_r_{separation}":
                value
            for (steps, epsilon, anchor, separation), value in raw.items()
        },
        "time_corrections": {
            f"eps_{epsilon:.8f}_anchor_{anchor}_r_{separation}":
                value
            for (epsilon, anchor, separation), value
            in time_corrections.items()
        },
        "epsilon_corrections": {
            f"anchor_{anchor}_r_{separation}": value
            for (anchor, separation), value
            in epsilon_corrections.items()
        },
        "extrapolated_kernels": {
            f"anchor_{anchor}_r_{separation}": value
            for (anchor, separation), value in kernels.items()
        },
        "mean_connected_kernel": {
            str(separation): value
            for separation, value in means.items()
        },
        "anchor_relative_differences": {
            str(separation): value
            for separation, value
            in anchor_relative_differences.items()
        },
        "anchor_pass": anchor_pass,
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
            "PERIODIC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_PASS"
            if passed
            else "PERIODIC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_BLOCKED"
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
                "minimum_amplitude_absolute": minimum_amplitude,
                "anchor_pass": anchor_pass,
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
