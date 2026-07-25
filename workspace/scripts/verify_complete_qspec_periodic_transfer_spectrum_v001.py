#!/usr/bin/env python3
"""Direct-ratio verifier for the periodic transfer spectral diagnostic."""

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
    / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_INDEPENDENT_VERIFIER_PROTOCOL_V001.md"
)
PRIMARY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_transfer_spectrum_v001.json"
)
TRANSFER = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_sequential_relative_history_transfer_map_v002.json"
)
TRANSFER_VERIFY = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_sequential_relative_history_transfer_map_verification_v002.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_transfer_spectrum_verification_v001.json"
)

EXPECTED = {
    PROTOCOL:
        "fe5397b5cd36ca61f8d6e8b18ea6389340d7508f011e8f3b77d7593a78ad99d9",
    ROOT / "COMPLETE_QSPEC_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_SPEC_V001.md":
        "881a342376e8c8a4e92930db9bd77969508572b96737f490fab35c1068eaf125",
    ROOT / "scripts/derive_complete_qspec_periodic_transfer_spectrum_v001.py":
        "2238fddb429452955022b7118d020f892f9a221e73e7bc401d8f64c8d3ffd32a",
    PRIMARY:
        "6814adf091ee24b8ab0793088cf034eb0745e93507fc80ff0cc4edfe012072db",
    ROOT
    / "scripts/"
    "derive_complete_qspec_sequential_relative_history_transfer_map_v002.py":
        "954f9ca6d6f70cf893748216ceb8b489eba28618e1637afd6c02be3f79be7aa5",
    TRANSFER:
        "ce84fb8244751d8f2cc8495a64ee219bd2dd4d9ffc5d3593a34b7265da589cca",
    ROOT
    / "scripts/"
    "verify_complete_qspec_sequential_relative_history_transfer_map_v002.py":
        "665aeb862c02e7d7fa0c57d12047a8cc67f7d0831b894ca709f2ff29ba30039b",
    TRANSFER_VERIFY:
        "a620a6bfd86e9e1799173befa31bbd0c0e5d7cfeec83a9d7680d68460defde57",
}

STEPS = (32, 64)
THETAS = (1.0 / 20.0, 1.0 / 40.0)
CHECKPOINTS = (63, 64, 95, 96)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def direct_ratios(
    initial: np.ndarray,
    plus: tuple[tuple[np.ndarray, ...], ...],
    minus: tuple[tuple[np.ndarray, ...], ...],
) -> dict[str, complex]:
    value = initial.copy()
    traces: dict[int, complex] = {}
    for count in range(1, max(CHECKPOINTS) + 1):
        for cell in range(2):
            value = sum(
                left @ value @ right.conjugate().T
                for left, right in zip(plus[cell], minus[cell])
            )
        if count in CHECKPOINTS:
            traces[count] = complex(np.trace(value))
    if abs(traces[63]) <= 1e-12 or abs(traces[95]) <= 1e-12:
        raise RuntimeError("direct-ratio denominator below frozen floor")
    return {
        "z63": traces[63],
        "z64": traces[64],
        "z95": traces[95],
        "z96": traces[96],
        "lambda64": traces[64] / traces[63],
        "lambda96": traces[96] / traces[95],
    }


def complex_row(value: complex) -> dict[str, float]:
    return {
        "real": float(value.real),
        "imag": float(value.imag),
        "absolute": float(abs(value)),
    }


def main() -> None:
    hash_checks = {
        str(path.relative_to(ROOT)): sha256(path) == expected
        for path, expected in EXPECTED.items()
    }
    if not all(hash_checks.values()):
        raise RuntimeError("authority hash mismatch")
    transfer_verify_hash = sha256(TRANSFER_VERIFY)
    transfer_verify = json.loads(TRANSFER_VERIFY.read_text())
    if not (
        transfer_verify["pass"]
        and transfer_verify["verdict"]
        == "INDEPENDENT_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_CONFIRMED"
    ):
        raise RuntimeError("sequential transfer repair is not independently confirmed")

    primary = json.loads(PRIMARY.read_text())
    parent = periodic.build_parent()
    density = parent["density"]
    interactions = parent["interactions"]
    record = parent["record"]
    free = parent["free"]

    rows: dict[tuple[int, float], dict[str, object]] = {}
    all_rows_pass = True
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
        for theta in (THETAS[0], -THETAS[0], THETAS[1], -THETAS[1]):
            branch_kraus = tuple(
                core.cell_kraus(
                    free(theta),
                    interaction,
                    record,
                    steps,
                )
                for interaction in interactions
            )
            direct = direct_ratios(
                density,
                branch_kraus,
                zero_kraus,
            )
            convergence = abs(
                direct["lambda96"] - direct["lambda64"]
            ) / max(abs(direct["lambda96"]), 1e-30)
            primary_key = f"steps_{steps}_theta_{theta:+.8f}"
            primary_modulus = primary["spectral_rows"][primary_key][
                "selected"
            ]["modulus"]
            primary_difference = abs(
                abs(direct["lambda96"]) - primary_modulus
            ) / primary_modulus
            row_pass = bool(
                min(abs(direct["z63"]), abs(direct["z95"])) > 1e-12
                and convergence < 1e-10
                and primary_difference < 1e-10
            )
            all_rows_pass = all_rows_pass and row_pass
            rows[(steps, theta)] = {
                **direct,
                "lambda_ratio_convergence": float(convergence),
                "primary_modulus": float(primary_modulus),
                "primary_modulus_relative_difference":
                    float(primary_difference),
                "pass": row_pass,
            }

    raw: dict[tuple[int, float], float] = {}
    for steps in STEPS:
        for theta in THETAS:
            plus = rows[(steps, theta)]["lambda96"]
            minus = rows[(steps, -theta)]["lambda96"]
            raw[(steps, theta)] = float(
                (
                    -math.log(abs(plus))
                    - math.log(abs(minus))
                )
                / (2.0 * theta * theta)
            )

    time_limits: dict[float, float] = {}
    time_corrections: dict[float, float] = {}
    for theta in THETAS:
        correction = (
            raw[(STEPS[1], theta)]
            - raw[(STEPS[0], theta)]
        ) / 3.0
        time_limits[theta] = raw[(STEPS[1], theta)] + correction
        time_corrections[theta] = abs(correction)
    theta_correction = (
        time_limits[THETAS[1]] - time_limits[THETAS[0]]
    ) / 3.0
    independent_limit = time_limits[THETAS[1]] + theta_correction
    primary_limit = float(primary["infinite_chain_intensive_limit"])
    primary_interval = primary["infinite_chain_interval"]
    limit_difference = abs(independent_limit - primary_limit)

    h16 = float(primary["boundary_correction"]["h16"])
    h32 = float(primary["boundary_correction"]["h32"])
    d16 = h16 - independent_limit
    d32 = h32 - independent_limit
    boundary_ratio = abs(d32 / d16) if d16 != 0.0 else float("inf")
    boundary_pass = bool(
        np.sign(d16) == np.sign(d32)
        and 0.35 < boundary_ratio < 0.65
    )
    passed = bool(
        all_rows_pass
        and limit_difference < 5e-7
        and primary_interval[0] < independent_limit < primary_interval[1]
        and boundary_pass
    )

    formatted_rows = {}
    for (steps, theta), row in rows.items():
        formatted_rows[f"steps_{steps}_theta_{theta:+.8f}"] = {
            "z63": complex_row(row["z63"]),
            "z64": complex_row(row["z64"]),
            "z95": complex_row(row["z95"]),
            "z96": complex_row(row["z96"]),
            "lambda64": complex_row(row["lambda64"]),
            "lambda96": complex_row(row["lambda96"]),
            "lambda_ratio_convergence":
                row["lambda_ratio_convergence"],
            "primary_modulus": row["primary_modulus"],
            "primary_modulus_relative_difference":
                row["primary_modulus_relative_difference"],
            "pass": row["pass"],
        }

    result = {
        "schema":
            "complete_qspec_periodic_transfer_spectrum_verification_v001",
        "protocol_sha256": sha256(PROTOCOL),
        "hash_checks": hash_checks,
        "transfer_verification_sha256": transfer_verify_hash,
        "method":
            "direct_long_chain_successive_amplitude_ratios_no_arnoldi",
        "rows": formatted_rows,
        "all_rows_pass": all_rows_pass,
        "raw_intensive_responses": {
            f"steps_{steps}_theta_{theta:.8f}": value
            for (steps, theta), value in raw.items()
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
        "independent_infinite_chain_intensive_limit":
            independent_limit,
        "primary_infinite_chain_intensive_limit": primary_limit,
        "limit_absolute_difference": limit_difference,
        "primary_interval": primary_interval,
        "independent_limit_inside_primary_interval":
            primary_interval[0] < independent_limit < primary_interval[1],
        "boundary_correction": {
            "h16": h16,
            "h32": h32,
            "d16": d16,
            "d32": d32,
            "absolute_ratio_d32_over_d16": boundary_ratio,
            "O_1_over_N_window_pass": boundary_pass,
        },
        "verdict": (
            "INDEPENDENT_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_CONFIRMED"
            if passed
            else "INDEPENDENT_PERIODIC_TRANSFER_SPECTRAL_DIAGNOSTIC_BLOCKED"
        ),
        "pass": passed,
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
                "all_rows_pass": all_rows_pass,
                "independent_limit": independent_limit,
                "primary_limit": primary_limit,
                "limit_absolute_difference": limit_difference,
                "boundary_correction": result["boundary_correction"],
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
