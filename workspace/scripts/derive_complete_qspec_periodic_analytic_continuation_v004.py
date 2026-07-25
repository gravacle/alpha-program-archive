#!/usr/bin/env python3
"""Holomorphic continuation repair and periodic zero-free diagnostic."""

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
    / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_DERIVATIVE_REPAIR_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_analytic_continuation_v004.json"
)

EXPECTED = {
    SPEC:
        "5065836ae6162cdcc609b3a0058777a54322c90fb551ab7d037855646a53cdd0",
    ROOT / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_REPAIR_SPEC_V001.md":
        "1f7e78a8a71dffb6ccf80614a78344ab170381d633fa91ce7483187673512c57",
    ROOT / "scripts/derive_complete_qspec_periodic_analytic_continuation_v003.py":
        "776651fd0c7732e6eb0d91a6efa16d53290a1d4bdbbb632d2d09e32069491a40",
    ROOT / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_PREFLIGHT_FAILURE_V001.md":
        "02fb0d29cfb7e48422924a833379050c0a49ad57cc4182b270d963774554dc87",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
    ROOT / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_RESULT_V001.md":
        "b7f5f0f29c69c14b3cfd6afba285c437ff0c2cb285c2f29f4ce3fb576bdfff48",
    ROOT / "COMPLETE_QSPEC_CONNECTED_KERNEL_LOCALITY_DIAGNOSTIC_RESULT_V001.md":
        "880ce005c7672857b927b12c24b3f07a16da9aeb1c89ed6430b4992fddfec47e",
    ROOT / "COMPLETE_QSPEC_COMPLEX_ZERO_FREE_RUNTIME_PORTABILITY_ADDENDUM_V001.md":
        "01501e04a9935c6714599076c0503353350245ce094e6ad18e3e146d7ff9d53b",
    ROOT / "COMPLETE_QSPEC_COMPLEX_CONTINUATION_CONJUGATION_ERRATUM_V001.md":
        "f706a4ab85f5863b87f6f5591a6907b25164cc6bebc6484e87b67a04bfc107b4",
}

STEPS = (48, 96)
RADIUS = 1.0 / 100.0
BOUNDARY_ANGLES = 64
INTERIOR_RADII = (1.0 / 400.0, 1.0 / 200.0, 3.0 / 400.0)
INTERIOR_ANGLES = 16
MAX_VOLUME = 64
REAL_AXIS_POINTS = (
    -1.0 / 100.0,
    -1.0 / 200.0,
    0.0,
    1.0 / 200.0,
    1.0 / 100.0,
)
CR_POINTS = (
    0.0 + 1j / 200.0,
    (1.0 + 1.0j) / (200.0 * math.sqrt(2.0)),
    (-1.0 + 2.0j) / 1000.0,
)
CR_STEPS = (1e-5, 5e-6)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expm_pade13(matrix: np.ndarray) -> np.ndarray:
    """Order-13 Pade scaling-and-squaring matrix exponential."""
    coefficients = (
        64764752532480000.0,
        32382376266240000.0,
        7771770303897600.0,
        1187353796428800.0,
        129060195264000.0,
        10559470521600.0,
        670442572800.0,
        33522128640.0,
        1323241920.0,
        40840800.0,
        960960.0,
        16380.0,
        182.0,
        1.0,
    )
    theta_13 = 5.371920351148152
    norm_one = float(np.linalg.norm(matrix, 1))
    scaling = (
        max(0, int(math.ceil(math.log2(norm_one / theta_13))))
        if norm_one > theta_13
        else 0
    )
    value = matrix / (2 ** scaling)
    identity = np.eye(value.shape[0], dtype=complex)
    value_2 = value @ value
    value_4 = value_2 @ value_2
    value_6 = value_4 @ value_2
    b = coefficients
    odd = value @ (
        value_6 @ (
            b[13] * value_6
            + b[11] * value_4
            + b[9] * value_2
        )
        + b[7] * value_6
        + b[5] * value_4
        + b[3] * value_2
        + b[1] * identity
    )
    even = (
        value_6 @ (
            b[12] * value_6
            + b[10] * value_4
            + b[8] * value_2
        )
        + b[6] * value_6
        + b[4] * value_4
        + b[2] * value_2
        + b[0] * identity
    )
    result = np.linalg.solve(even - odd, even + odd)
    for _ in range(scaling):
        result = result @ result
    return result


def analytic_covariant_difference(theta: complex) -> np.ndarray:
    """Entire directed-edge continuation of the three-site connection."""
    matrix = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = np.exp(-1j * theta / 3.0)
    for site in range(3):
        matrix[site, (site + 1) % 3] += forward / 2.0
        matrix[site, (site - 1) % 3] -= backward / 2.0
    return matrix


def analytic_covariant_difference_derivative(
    theta: complex,
) -> np.ndarray:
    """Exact theta derivative of the entire directed-edge continuation."""
    matrix = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = np.exp(-1j * theta / 3.0)
    derivative_forward = (1j / 3.0) * forward
    derivative_backward = (-1j / 3.0) * backward
    for site in range(3):
        matrix[site, (site + 1) % 3] += derivative_forward / 2.0
        matrix[site, (site - 1) % 3] -= derivative_backward / 2.0
    return matrix


def analytic_free_factory():
    """Return the entire free generator and its exact theta derivative."""
    alpha_x, _ = core.dirac_operators()
    full_zero = np.kron(
        -1j * core.covariant_difference(0.0),
        alpha_x,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(full_zero)
    active_vectors = eigenvectors[:, np.abs(eigenvalues) > 1e-12]

    def analytic_free(theta: complex) -> np.ndarray:
        full = np.kron(
            -1j * analytic_covariant_difference(theta),
            alpha_x,
        )
        one_body = active_vectors.conjugate().T @ full @ active_vectors
        return core.dgamma(one_body, 4)[0]

    def analytic_free_derivative(theta: complex) -> np.ndarray:
        full = np.kron(
            -1j * analytic_covariant_difference_derivative(theta),
            alpha_x,
        )
        one_body = active_vectors.conjugate().T @ full @ active_vectors
        return core.dgamma(one_body, 4)[0]

    return analytic_free, analytic_free_derivative


def cauchy_riemann_residual(function, point: complex, step: float) -> float:
    derivative_x = (
        function(point + step) - function(point - step)
    ) / (2.0 * step)
    derivative_y = (
        function(point + 1j * step) - function(point - 1j * step)
    ) / (2.0 * step)
    return float(
        np.linalg.norm(derivative_y - 1j * derivative_x)
        / max(
            np.linalg.norm(derivative_x),
            np.linalg.norm(derivative_y),
            1e-30,
        )
    )


def derivative_residuals(
    function,
    exact_derivative,
    point: complex,
    step: float,
) -> dict[str, float]:
    derivative_x = (
        function(point + step) - function(point - step)
    ) / (2.0 * step)
    derivative_y = (
        function(point + 1j * step) - function(point - 1j * step)
    ) / (2.0 * step)
    target = exact_derivative(point)
    target_norm = max(np.linalg.norm(target), 1e-30)
    return {
        "x_vs_exact": float(
            np.linalg.norm(derivative_x - target) / target_norm
        ),
        "y_vs_i_exact": float(
            np.linalg.norm(derivative_y - 1j * target) / target_norm
        ),
        "cauchy_riemann": float(
            np.linalg.norm(derivative_y - 1j * derivative_x)
            / max(
                np.linalg.norm(derivative_x),
                np.linalg.norm(derivative_y),
                1e-30,
            )
        ),
    }


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
    half_free = expm_pade13(-0.5j * dt * free)
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
    analytic_free, analytic_free_derivative = analytic_free_factory()
    identity_error = float(
        np.linalg.norm(
            expm_pade13(np.zeros((4, 4), dtype=complex))
            - np.eye(4, dtype=complex)
        )
    )
    real_axis_rows = {}
    maximum_real_axis_generator_difference = 0.0
    maximum_real_axis_difference = 0.0
    maximum_real_axis_unitarity_error = 0.0
    for theta in REAL_AXIS_POINTS:
        real_free = free(theta)
        repaired_free = analytic_free(theta)
        generator_difference = float(
            np.linalg.norm(repaired_free - real_free)
            / max(np.linalg.norm(real_free), 1e-30)
        )
        maximum_real_axis_generator_difference = max(
            maximum_real_axis_generator_difference,
            generator_difference,
        )
        eigenvalues, eigenvectors = np.linalg.eigh(real_free)
        dt_check = 1.0 / STEPS[-1]
        reference = (
            eigenvectors
            @ np.diag(np.exp(-0.5j * dt_check * eigenvalues))
            @ eigenvectors.conjugate().T
        )
        candidate = expm_pade13(-0.5j * dt_check * repaired_free)
        difference = float(np.linalg.norm(candidate - reference))
        unitarity_error = float(
            np.linalg.norm(
                candidate.conjugate().T @ candidate
                - np.eye(candidate.shape[0], dtype=complex)
            )
        )
        maximum_real_axis_difference = max(
            maximum_real_axis_difference,
            difference,
        )
        maximum_real_axis_unitarity_error = max(
            maximum_real_axis_unitarity_error,
            unitarity_error,
        )
        real_axis_rows[f"{theta:+.8f}"] = {
            "generator_relative_difference": generator_difference,
            "pade_eigh_difference": difference,
            "unitarity_error": unitarity_error,
        }
    portability_pass = bool(
        identity_error < 1e-14
        and maximum_real_axis_generator_difference < 1e-12
        and maximum_real_axis_difference < 1e-11
        and maximum_real_axis_unitarity_error < 1e-11
    )
    if not portability_pass:
        raise RuntimeError("self-contained matrix exponential preflight failed")

    cr_rows: dict[str, dict[str, object]] = {}
    maximum_repaired_derivative_residual = 0.0
    maximum_superseded_cr_residual = 0.0
    for point in CR_POINTS:
        repaired = tuple(
            derivative_residuals(
                analytic_free,
                analytic_free_derivative,
                point,
                step,
            )
            for step in CR_STEPS
        )
        superseded = tuple(
            cauchy_riemann_residual(free, point, step)
            for step in CR_STEPS
        )
        maximum_repaired_derivative_residual = max(
            maximum_repaired_derivative_residual,
            *(
                value
                for row in repaired
                for value in row.values()
            ),
        )
        maximum_superseded_cr_residual = max(
            maximum_superseded_cr_residual,
            superseded[-1],
        )
        cr_rows[point_key(point)] = {
            "steps": list(CR_STEPS),
            "repaired_derivative_residuals": list(repaired),
            "superseded_residuals": list(superseded),
        }
    cr_pass = bool(
        maximum_repaired_derivative_residual < 1e-8
        and maximum_superseded_cr_residual > 1e-3
    )
    if not cr_pass:
        raise RuntimeError("analytic-continuation preflight failed")

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
                        analytic_free(point),
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
        portability_pass
        and cr_pass
        and minimum_amplitude > 0.95
        and maximum_step_disagreement < 1e-4
        and winding_pass
        and ratio_pass
    )
    result = {
        "schema": "complete_qspec_periodic_analytic_continuation_v004",
        "spec_sha256": sha256(SPEC),
        "analytic_continuation": {
            "forward_factor": "exp(+i theta/3)",
            "backward_factor": "exp(-i theta/3)",
            "uses_complex_conjugation": False,
            "entrywise_entire": True,
        },
        "runtime_portability_preflight": {
            "method": "order_13_Pade_scaling_and_squaring",
            "identity_error": identity_error,
            "real_axis_rows": real_axis_rows,
            "maximum_real_axis_generator_relative_difference":
                maximum_real_axis_generator_difference,
            "maximum_real_axis_difference":
                maximum_real_axis_difference,
            "maximum_real_axis_unitarity_error":
                maximum_real_axis_unitarity_error,
            "pass": portability_pass,
        },
        "cauchy_riemann_preflight": {
            "points": cr_rows,
            "maximum_repaired_derivative_residual":
                maximum_repaired_derivative_residual,
            "maximum_superseded_residual":
                maximum_superseded_cr_residual,
            "pass": cr_pass,
        },
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
            "PERIODIC_ANALYTIC_CONTINUATION_DIAGNOSTIC_PASS"
            if passed
            else "PERIODIC_ANALYTIC_CONTINUATION_DIAGNOSTIC_BLOCKED"
        ),
        "pass": passed,
        "analytic_complex_continuation_repaired": passed,
        "periodic_analytic_continuation_diagnostic_passed": passed,
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
