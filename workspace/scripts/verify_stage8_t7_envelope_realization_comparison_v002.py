#!/usr/bin/env python3
"""Independent midpoint verification of the higher-resolution envelope comparison."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import verify_stage8_t7_hermite_galerkin_baseline_v001 as independent


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_NUMERICS_SUCCESSOR_SPEC_V001.md"
PRIMARY = ROOT / "stage8_execution/work/T07_envelope_realization_comparison_v002.json"
OUT = ROOT / "stage8_execution/work/T07_envelope_realization_comparison_verification_v002.json"

TOLERANCE = 5e-5


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def envelope(mode: str, midpoint: float) -> float:
    tau = math.pi / math.sqrt(2.0)
    if mode == "ER-A":
        radius = min(midpoint, 1.0 - midpoint)
        return tau * 32.0 * radius**3
    if mode == "ER-B":
        return tau * 24.0 / math.pi
    raise ValueError(mode)


def histories(
    mode: str,
    steps: int,
    alpha: tuple[np.ndarray, ...],
    incidence: np.ndarray,
) -> tuple[np.ndarray, ...]:
    n = 2
    ell = 1.0
    h0 = independent.h0_matrix(n, ell, alpha)
    dt = 1.0 / steps
    output = []
    for lam in (-math.sqrt(2.0), 0.0, math.sqrt(2.0)):
        value = np.eye(h0.shape[0], dtype=complex)
        for index in range(steps):
            midpoint = (index + 0.5) / steps
            radius = min(midpoint, 1.0 - midpoint)
            multiplication = independent.ball_matrix(
                radius, n, ell, 14, 14, 28
            )
            h = h0 + lam * envelope(mode, midpoint) * np.kron(
                multiplication, incidence
            )
            value = independent.exp_h(h, dt) @ value
        output.append(value)
    return tuple(output)


def read_complex(value: dict[str, float]) -> complex:
    return complex(value["real"], value["imag"])


def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    alpha, incidence = independent.gamma_data()
    covariance = independent.mixed_c(2, alpha)
    h0 = independent.h0_matrix(2, 1.0, alpha)
    values, vectors = np.linalg.eigh(h0)
    occupied = vectors[:, values < 0.0]
    primary_case = next(
        case
        for case in primary["cases"]
        if case["n"] == 2 and abs(case["ell"] - 1.0) < 1e-15
    )

    checks = {}
    passed = True
    for mode in ("ER-A", "ER-B"):
        midpoint_96 = independent.amplitude(
            histories(mode, 96, alpha, incidence), covariance, occupied
        )
        midpoint_192 = independent.amplitude(
            histories(mode, 192, alpha, incidence), covariance, occupied
        )
        strang = tuple(
            read_complex(
                primary_case["branches"][mode]["amplitudes"]["96"][scheme]
            )
            for scheme in ("mixed", "pure")
        )
        mode_checks = {}
        for index, scheme in enumerate(("mixed", "pure")):
            tail = abs(midpoint_96[index] - midpoint_192[index])
            cross = abs(midpoint_192[index] - strang[index])
            mode_checks[scheme] = {
                "midpoint_96_to_192": float(tail),
                "midpoint_192_to_primary_strang_96": float(cross),
            }
            passed = passed and tail < TOLERANCE and cross < TOLERANCE
        checks[mode] = mode_checks

    result = {
        "schema": "stage8_t7_envelope_realization_comparison_verification_v002",
        "spec_sha256": sha256(SPEC),
        "checks": checks,
        "independent_integrator": "full-Hamiltonian midpoint exponential",
        "independent_ball_quadrature": "14x14x28 direct Hermite evaluation",
        "independent_covariance_quadrature_order": 24,
        "tolerance": TOLERANCE,
        "pass": bool(passed),
        "ER_A_selected": False,
        "ER_B_selected": False,
        "envelope_realization_derived": False,
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
