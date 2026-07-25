#!/usr/bin/env python3
"""Independent Gauss-Legendre verifier for Lorentzian threshold return."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_LORENTZIAN_THRESHOLD_RETURN_SPEC_V001.md"
RESULT = ROOT / "results" / "r3_4_lorentzian_threshold_return_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )

    nodes, weights = np.polynomial.legendre.leggauss(768)
    momentum = 4.5 * (nodes + 1.0)
    quadrature_weights = 4.5 * weights
    density = (
        4.0
        / math.sqrt(math.pi)
        * momentum**2
        * np.exp(-momentum**2)
    )
    normalization = float(np.sum(quadrature_weights * density))
    require(abs(normalization - 1.0) < 2e-13, "Gaussian normalization failed")

    mass = math.pi
    for time_text, expected in stored["gaussian_return_amplitudes"].items():
        time = float(time_text)
        massless_exact = (
            math.exp(-(time**2) / 4.0) * (1.0 - time**2 / 2.0)
        )
        massive = float(
            np.sum(
                quadrature_weights
                * density
                * np.cos(np.sqrt(momentum**2 + mass**2) * time)
            )
        )
        actual = 0.5 * (massless_exact + massive)
        require(
            abs(actual - expected) < 2e-12,
            f"Independent quadrature mismatch at t={time_text}",
        )

    eigenvalues = np.asarray(stored["record_eigenvalues"])
    require(
        np.max(
            np.abs(
                eigenvalues
                - np.array([-math.sqrt(2.0), 0.0, math.sqrt(2.0)])
            )
        )
        < 1e-12,
        "Record spectrum mismatch",
    )
    require(stored["nonflat_band_spectrum_derived"] is True,
            "Non-flat band result missing")
    require(
        stored["L2_root_spectral_measure_absolutely_continuous"] is True,
        "Absolute-continuity result missing",
    )
    require(
        stored["Riemann_Lebesgue_threshold_return_derived_for_this_H"] is True,
        "Threshold-return theorem missing",
    )
    require(
        stored["point_momentum_root_excluded_from_L2_theorem"] is True,
        "Point-root negative control was not scoped out",
    )
    require(
        stored["complete_outgoing_generator_identified"] is False,
        "Complete outgoing generator was overclaimed",
    )
    require(
        stored["complete_physical_durability_derived"] is False,
        "Complete durability was overclaimed",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(
        stored["status"]
        == "LORENTZIAN_L2_THRESHOLD_RETURN_THEOREM_DERIVED",
        "Wrong verdict",
    )
    print("PASS independent Lorentzian threshold-return verification")


if __name__ == "__main__":
    main()
