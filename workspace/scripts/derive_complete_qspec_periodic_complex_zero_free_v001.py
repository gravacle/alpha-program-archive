#!/usr/bin/env python3
"""Complex-disk zero-free diagnostic for the periodic Qspec amplitude."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm

import derive_complete_qspec_periodic_connected_amplitude_v001 as periodic
import derive_complete_qspec_sequential_relative_history_transfer_map_v002 as core


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_complex_zero_free_v001.json"
)

EXPECTED = {
    SPEC:
        "fc2ca9ff890f3833a495107ae4619b3b341e009a1357ae2943836fd5ecf5456d",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
    ROOT / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_RESULT_V001.md":
        "b7f5f0f29c69c14b3cfd6afba285c437ff0c2cb285c2f29f4ce3fb576bdfff48",
    ROOT / "COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_RESULT_V001.md":
        "880ce005c7672857b927b12c24b3f07a16da9aeb1c89ed6430b4992fddfec47e",
}

STEPS = (48, 96)
RADIUS = 1.0 / 100.0
BOUNDARY_ANGLES = 64
INTERIOR_RADII = (1.0 / 400.0, 1.0 / 200.0, 3.0 / 400.0)
INTERIOR_ANGLES = 16
MAX_VOLUME = 64


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cell_kraus_complex(
    free: np.ndarray,
    interaction: np.ndarray,
    record: np.ndarray,
    steps: int,
) -> tuple[np.ndarray, ...]:
    source_dimension = free.shape[0]
    record_dimension = record.shape[0]
    source_values, source_vectors = np.linalg.eigh(interaction)
    record_values, record_vectors = np.linalg.eigh(record)
    dt = 1.0 / steps
    half_free = expm(-0.5j * dt * free)
    state = np.zeros(
        (source_dimension, record_dimension, source_dimension),
        dtype=complex,
    )
    state[:, 0, :] = np.eye(source_dimension, dtype=complex)
    action = math.pi / math.sqrt(2.0)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        state = core.apply_free_tensor(state, half_free)
        state = core.apply_interaction_tensor(
            state,
            source_vectors,
            source_values,
            record_vectors,
            record_values,
            action * core.diamond_weight(midpoint) * dt,
        )
        state = core.apply_free_tensor(state, half_free)
    return tuple(
        state[:, outcome, :]
        for outcome in range(record_dimension)
    )


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


def point_key(point: complex) -> str:
    return f"{point.real:+.12f}_{point.imag:+.12f}i"


def complex_row(value: complex) -> dict[str, float]:
    return {
        "real": float(value.real),
        "imag": float(value.imag),
        "absolute": float(abs(value)),
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")

    boundary = tuple(
        RADIUS * np.exp(2j * math.pi * index / BOUNDARY_ANGLES)
        for index in range(BOUNDARY_ANGLES)
    )
    interior = tuple(
        radius * np.exp(2j * math.pi * index / INTERIOR_ANGLES)
        for radius in INTERIOR_RADII
        for index in range(INTERIOR_ANGLES)
    )
    points = (0.0 + 0.0j,) + boundary + interior

    parent = periodic.build_parent()
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]
    amplitudes: dict[tuple[int, complex, int], complex] = {}

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
        for point in points:
            branch = (
                zero
                if point == 0.0
                else tuple(
                    cell_kraus_complex(
                        free(point),
                        interaction,
                        record,
                        steps,
                    )
                    for interaction in interactions
                )
            )
            value = parent["density"].copy()
            for volume in range(1, MAX_VOLUME + 1):
                value = apply_supercell(value, branch, zero)
                amplitudes[(steps, point, volume)] = complex(
                    np.trace(value)
                )

    minimum_amplitude = min(
        abs(value) for value in amplitudes.values()
    )
    minimum_location = min(
        amplitudes,
        key=lambda key: abs(amplitudes[key]),
    )
    maximum_step_disagreement = 0.0
    for point in points:
        for volume in range(1, MAX_VOLUME + 1):
            coarse = amplitudes[(STEPS[0], point, volume)]
            fine = amplitudes[(STEPS[1], point, volume)]
            disagreement = abs(fine - coarse) / max(abs(fine), 1e-30)
            maximum_step_disagreement = max(
                maximum_step_disagreement,
                disagreement,
            )

    winding: dict[int, dict[str, float | int | bool]] = {}
    winding_pass = True
    for volume in range(1, MAX_VOLUME + 1):
        values = [
            amplitudes[(STEPS[1], point, volume)]
            for point in boundary
        ]
        increments = [
            float(np.angle(values[(index + 1) % len(values)] / values[index]))
            for index in range(len(values))
        ]
        total = sum(increments)
        winding_number = int(round(total / (2.0 * math.pi)))
        maximum_increment = max(abs(item) for item in increments)
        row_pass = bool(
            winding_number == 0
            and maximum_increment < math.pi / 2.0
        )
        winding_pass = winding_pass and row_pass
        winding[volume] = {
            "winding_number": winding_number,
            "total_phase": float(total),
            "maximum_adjacent_phase_increment": maximum_increment,
            "pass": row_pass,
        }

    ratio_rows: dict[str, dict[str, object]] = {}
    ratio_pass = True
    for point in boundary:
        z47 = amplitudes[(STEPS[1], point, 47)]
        z48 = amplitudes[(STEPS[1], point, 48)]
        z63 = amplitudes[(STEPS[1], point, 63)]
        z64 = amplitudes[(STEPS[1], point, 64)]
        lambda48 = z48 / z47
        lambda64 = z64 / z63
        convergence = abs(lambda64 - lambda48) / max(
            abs(lambda64),
            1e-30,
        )
        row_pass = convergence < 1e-6
        ratio_pass = ratio_pass and row_pass
        ratio_rows[point_key(point)] = {
            "lambda48": complex_row(lambda48),
            "lambda64": complex_row(lambda64),
            "relative_difference": float(convergence),
            "pass": row_pass,
        }

    sample_summaries = {}
    for point in points:
        point_values = [
            amplitudes[(STEPS[1], point, volume)]
            for volume in range(1, MAX_VOLUME + 1)
        ]
        sample_summaries[point_key(point)] = {
            "minimum_amplitude_absolute":
                min(abs(value) for value in point_values),
            "z64": complex_row(point_values[-1]),
        }

    passed = bool(
        minimum_amplitude > 0.95
        and maximum_step_disagreement < 1e-4
        and winding_pass
        and ratio_pass
    )
    result = {
        "schema": "complete_qspec_periodic_complex_zero_free_v001",
        "spec_sha256": sha256(SPEC),
        "disk_radius": RADIUS,
        "boundary_angles": BOUNDARY_ANGLES,
        "interior_radii": list(INTERIOR_RADII),
        "interior_angles": INTERIOR_ANGLES,
        "steps_per_cell": list(STEPS),
        "maximum_volume": MAX_VOLUME,
        "sample_count": len(points),
        "minimum_amplitude_absolute": minimum_amplitude,
        "minimum_location": {
            "steps": minimum_location[0],
            "theta": complex_row(minimum_location[1]),
            "volume": minimum_location[2],
        },
        "maximum_time_step_relative_disagreement":
            maximum_step_disagreement,
        "winding_by_volume": {
            str(volume): row
            for volume, row in winding.items()
        },
        "winding_pass": winding_pass,
        "boundary_ratio_convergence": ratio_rows,
        "boundary_ratio_convergence_pass": ratio_pass,
        "sample_summaries_fine_steps": sample_summaries,
        "verdict": (
            "PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_PASS"
            if passed
            else "PERIODIC_COMPLEX_ZERO_FREE_DIAGNOSTIC_BLOCKED"
        ),
        "pass": passed,
        "periodic_complex_zero_free_diagnostic_passed": passed,
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
                "sample_count": len(points),
                "minimum_amplitude_absolute": minimum_amplitude,
                "maximum_time_step_relative_disagreement":
                    maximum_step_disagreement,
                "winding_pass": winding_pass,
                "boundary_ratio_convergence_pass": ratio_pass,
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
