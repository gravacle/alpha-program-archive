#!/usr/bin/env python3
"""Matrix-free spectral diagnostic for the period-two Qspec transfer map."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import derive_complete_qspec_periodic_connected_amplitude_v001 as periodic
import derive_complete_qspec_relative_history_transfer_map_v001 as core


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_SPEC_V001.md"
)
FINITE = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_connected_amplitude_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_transfer_spectrum_v001.json"
)

EXPECTED = {
    SPEC:
        "881a342376e8c8a4e92930db9bd77969508572b96737f490fab35c1068eaf125",
    ROOT / "COMPLETE_QSPEC_PERIODIC_CONNECTED_AMPLITUDE_NUMERICAL_BLOCK_V001.md":
        "b3800c690cf7376a13375f1fb747e94ccc1a000383f0ea48ab1a3341fcd45549",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_SPEC_V001.md":
        "7e79583981dd97b2fb5e0ebb6a3498b7bdc03a29cb46f8e2c654f62bc52315ef",
    ROOT / "scripts/derive_complete_qspec_relative_history_transfer_map_v001.py":
        "3800b661ea0dacb052aeb0a843f331a13eddc9c838949e5e224c2a5c288271d1",
    ROOT / "stage8_execution/work/QSPEC_relative_history_transfer_map_v001.json":
        "b202278190c5e440713abbea247fcfcb92c1dc4fba1a1b08d8db648f3579caaf",
    ROOT / "scripts/derive_complete_qspec_periodic_connected_amplitude_v001.py":
        "d109fc1ad7e7c65292631a1eafafe07d53c946f153521994be8e57315732fdec",
    FINITE:
        "d8491a0a8008ac407ba3afe074fb253398f079689232d7ef399b048725eb0274",
}

STEPS = (32, 64)
THETAS = (1.0 / 20.0, 1.0 / 40.0)
KRYLOV_DIMENSION = 48
POWER_ITERATIONS = 128


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supercell_action(
    vector: np.ndarray,
    source_dimension: int,
    plus: tuple[tuple[np.ndarray, ...], ...],
    minus: tuple[tuple[np.ndarray, ...], ...],
) -> np.ndarray:
    value = vector.reshape(source_dimension, source_dimension)
    for cell in range(2):
        value = core.compose_cross_map(
            value,
            plus[cell],
            minus[cell],
        )
    return value.reshape(-1)


def arnoldi_modes(
    start: np.ndarray,
    action,
    source_dimension: int,
) -> dict[str, object]:
    vector_dimension = start.size
    q_values = np.zeros(
        (vector_dimension, KRYLOV_DIMENSION + 1),
        dtype=complex,
    )
    hessenberg = np.zeros(
        (KRYLOV_DIMENSION + 1, KRYLOV_DIMENSION),
        dtype=complex,
    )
    q_values[:, 0] = start / np.linalg.norm(start)
    completed = KRYLOV_DIMENSION
    for column in range(KRYLOV_DIMENSION):
        work = action(q_values[:, column])
        for _ in range(2):
            for row in range(column + 1):
                coefficient = np.vdot(q_values[:, row], work)
                hessenberg[row, column] += coefficient
                work -= coefficient * q_values[:, row]
        beta = np.linalg.norm(work)
        hessenberg[column + 1, column] = beta
        if beta < 1e-14:
            completed = column + 1
            break
        q_values[:, column + 1] = work / beta

    reduced = hessenberg[:completed, :completed]
    eigenvalues, eigenvectors = np.linalg.eig(reduced)
    modes = []
    for index, eigenvalue in enumerate(eigenvalues):
        vector = q_values[:, :completed] @ eigenvectors[:, index]
        norm = np.linalg.norm(vector)
        if norm == 0.0:
            continue
        vector /= norm
        residual = np.linalg.norm(action(vector) - eigenvalue * vector)
        trace_overlap = abs(
            np.trace(vector.reshape(source_dimension, source_dimension))
        )
        modes.append(
            {
                "eigenvalue": complex(eigenvalue),
                "residual": float(residual),
                "trace_overlap": float(trace_overlap),
                "modulus": float(abs(eigenvalue)),
            }
        )
    eligible = [
        mode for mode in modes
        if mode["residual"] < 1e-8
        and mode["trace_overlap"] > 1e-8
    ]
    eligible.sort(key=lambda mode: mode["modulus"], reverse=True)
    selected = eligible[0] if eligible else None
    next_mode = eligible[1] if len(eligible) > 1 else None
    relative_gap = (
        (selected["modulus"] - next_mode["modulus"])
        / selected["modulus"]
        if selected is not None and next_mode is not None
        else 1.0 if selected is not None else 0.0
    )
    return {
        "completed_dimension": completed,
        "eligible_count": len(eligible),
        "selected": selected,
        "next": next_mode,
        "relative_modulus_gap": float(relative_gap),
        "all_modes": modes,
    }


def power_check(start: np.ndarray, action) -> dict[str, object]:
    vector = start / np.linalg.norm(start)
    quotient = 0.0 + 0.0j
    for _ in range(POWER_ITERATIONS):
        image = action(vector)
        quotient = complex(np.vdot(vector, image))
        norm = np.linalg.norm(image)
        if norm == 0.0:
            return {
                "rayleigh_quotient": 0.0 + 0.0j,
                "residual": float("inf"),
            }
        vector = image / norm
    image = action(vector)
    quotient = complex(np.vdot(vector, image))
    residual = float(np.linalg.norm(image - quotient * vector))
    return {
        "rayleigh_quotient": quotient,
        "residual": residual,
    }


def complex_row(value: complex) -> dict[str, float]:
    return {
        "real": value.real,
        "imag": value.imag,
        "absolute": abs(value),
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")
    finite = json.loads(FINITE.read_text())
    parent = periodic.build_parent()
    source_dimension = int(parent["source_dimension"])
    start = parent["density"].reshape(-1)
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]

    spectral: dict[tuple[int, float], dict[str, object]] = {}
    all_spectral_pass = True
    for steps in STEPS:
        zero_kraus = tuple(
            core.cell_kraus(
                parent["free_zero"],
                interaction,
                record,
                steps,
            )
            for interaction in interactions
        )
        for signed_theta in (
            THETAS[0],
            -THETAS[0],
            THETAS[1],
            -THETAS[1],
        ):
            branch_kraus = tuple(
                core.cell_kraus(
                    free(signed_theta),
                    interaction,
                    record,
                    steps,
                )
                for interaction in interactions
            )

            def action(vector):
                return supercell_action(
                    vector,
                    source_dimension,
                    branch_kraus,
                    zero_kraus,
                )

            arnoldi = arnoldi_modes(start, action, source_dimension)
            power = power_check(start, action)
            selected = arnoldi["selected"]
            if selected is None:
                comparison = float("inf")
                row_pass = False
            else:
                selected_value = selected["eigenvalue"]
                power_value = power["rayleigh_quotient"]
                comparison = abs(power_value - selected_value) / max(
                    abs(selected_value),
                    1e-30,
                )
                row_pass = bool(
                    selected["residual"] < 1e-8
                    and selected["trace_overlap"] > 1e-8
                    and arnoldi["relative_modulus_gap"] > 1e-5
                    and power["residual"] < 1e-6
                    and comparison < 1e-6
                )
            all_spectral_pass = all_spectral_pass and row_pass
            spectral[(steps, signed_theta)] = {
                "arnoldi": arnoldi,
                "power": power,
                "power_arnoldi_relative_difference": float(comparison),
                "pass": row_pass,
            }

    raw_intensive: dict[tuple[int, float], float] = {}
    if all_spectral_pass:
        for steps in STEPS:
            for theta in THETAS:
                plus = spectral[(steps, theta)]["arnoldi"]["selected"][
                    "eigenvalue"
                ]
                minus = spectral[(steps, -theta)]["arnoldi"]["selected"][
                    "eigenvalue"
                ]
                raw_intensive[(steps, theta)] = float(
                    (
                        -math.log(abs(plus))
                        - math.log(abs(minus))
                    )
                    / (2.0 * theta * theta)
                )

        time_limits: dict[float, float] = {}
        time_corrections: dict[float, float] = {}
        for theta in THETAS:
            coarse = raw_intensive[(STEPS[0], theta)]
            fine = raw_intensive[(STEPS[1], theta)]
            correction = (fine - coarse) / 3.0
            time_limits[theta] = fine + correction
            time_corrections[theta] = abs(correction)
        theta_correction = (
            time_limits[THETAS[1]] - time_limits[THETAS[0]]
        ) / 3.0
        infinite_limit = time_limits[THETAS[1]] + theta_correction
        radius = (
            max(time_corrections.values())
            + abs(theta_correction)
            + 1e-8
        )
        interval = [
            infinite_limit - radius,
            infinite_limit + radius,
        ]
    else:
        time_limits = {}
        time_corrections = {}
        theta_correction = float("nan")
        infinite_limit = float("nan")
        radius = float("nan")
        interval = [float("nan"), float("nan")]

    h8 = float(
        finite["extrapolated_intensive_responses"]["8"]["limit"]
    )
    h16 = float(
        finite["extrapolated_intensive_responses"]["16"]["limit"]
    )
    h32 = float(
        finite["extrapolated_intensive_responses"]["32"]["limit"]
    )
    d16 = h16 - infinite_limit
    d32 = h32 - infinite_limit
    boundary_ratio = abs(d32 / d16) if d16 != 0.0 else float("inf")
    boundary_pass = bool(
        np.sign(d16) == np.sign(d32)
        and 0.35 < boundary_ratio < 0.65
    )
    passed = bool(
        all_spectral_pass
        and interval[0] > 0.0
        and boundary_pass
    )

    formatted_spectral = {}
    for (steps, theta), row in spectral.items():
        arnoldi = row["arnoldi"]
        power = row["power"]
        formatted_spectral[
            f"steps_{steps}_theta_{theta:+.8f}"
        ] = {
            "completed_dimension": arnoldi["completed_dimension"],
            "eligible_count": arnoldi["eligible_count"],
            "selected": (
                {
                    "eigenvalue": complex_row(
                        arnoldi["selected"]["eigenvalue"]
                    ),
                    "residual": arnoldi["selected"]["residual"],
                    "trace_overlap":
                        arnoldi["selected"]["trace_overlap"],
                    "modulus": arnoldi["selected"]["modulus"],
                }
                if arnoldi["selected"] is not None
                else None
            ),
            "next": (
                {
                    "eigenvalue": complex_row(
                        arnoldi["next"]["eigenvalue"]
                    ),
                    "residual": arnoldi["next"]["residual"],
                    "trace_overlap": arnoldi["next"]["trace_overlap"],
                    "modulus": arnoldi["next"]["modulus"],
                }
                if arnoldi["next"] is not None
                else None
            ),
            "relative_modulus_gap": arnoldi["relative_modulus_gap"],
            "power": {
                "rayleigh_quotient": complex_row(
                    power["rayleigh_quotient"]
                ),
                "residual": power["residual"],
            },
            "power_arnoldi_relative_difference":
                row["power_arnoldi_relative_difference"],
            "pass": row["pass"],
        }

    result = {
        "schema": "complete_qspec_periodic_transfer_spectrum_v001",
        "spec_sha256": sha256(SPEC),
        "matrix_free_supercell_operator": True,
        "dense_4900_operator_built": False,
        "full_record_Hilbert_space_built": False,
        "krylov_dimension": KRYLOV_DIMENSION,
        "power_iterations": POWER_ITERATIONS,
        "spectral_rows": formatted_spectral,
        "all_spectral_rows_pass": all_spectral_pass,
        "raw_spectral_intensive_responses": {
            f"steps_{steps}_theta_{theta:.8f}": value
            for (steps, theta), value in raw_intensive.items()
        },
        "time_extrapolated_by_theta": {
            f"{theta:.8f}": value
            for theta, value in time_limits.items()
        },
        "time_corrections": {
            f"{theta:.8f}": value
            for theta, value in time_corrections.items()
        },
        "theta_correction": theta_correction,
        "infinite_chain_intensive_limit": infinite_limit,
        "infinite_chain_interval": interval,
        "boundary_correction": {
            "h8": h8,
            "h16": h16,
            "h32": h32,
            "d16": d16,
            "d32": d32,
            "absolute_ratio_d32_over_d16": boundary_ratio,
            "O_1_over_N_window_pass": boundary_pass,
        },
        "verdict": (
            "PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_PASS"
            if passed
            else "PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_BLOCKED"
        ),
        "pass": passed,
        "relative_history_transfer_map_derived": True,
        "periodic_connected_amplitude_constructed": True,
        "periodic_transfer_spectral_limit_computed": passed,
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
                "all_spectral_rows_pass": all_spectral_pass,
                "infinite_chain_intensive_limit": infinite_limit,
                "infinite_chain_interval": interval,
                "boundary_correction":
                    result["boundary_correction"],
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
