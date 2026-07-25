#!/usr/bin/env python3
"""Independent, side-effect-free verifier for the R3.4 v002 result."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_causal_diamond_spectral_pullback_v002.json"
VOLUME = math.pi / 24.0


def fail(message: str) -> None:
    raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closed_form(energy: float) -> float:
    if abs(energy) < 1.0e-3:
        return 1.0 - energy**2 / 40.0 + energy**4 / 4480.0
    z = energy / 2.0
    return 24.0 * (math.sin(z) - z * math.cos(z)) / energy**3


def midpoint_diamond_integral(energy: float, intervals_per_half: int = 200000) -> float:
    total = 0.0
    for lower, upper in ((-0.5, 0.0), (0.0, 0.5)):
        step = (upper - lower) / intervals_per_half
        t = lower + (np.arange(intervals_per_half) + 0.5) * step
        radius = 0.5 - np.abs(t)
        if energy == 0.0:
            spatial = 4.0 * math.pi * radius**3 / 3.0
        else:
            z = energy * radius
            spatial = np.empty_like(z)
            small = np.abs(z) < 1.0e-3
            r = radius[small]
            spatial[small] = 4.0 * math.pi * (
                r**3 / 3.0
                - energy**2 * r**5 / 30.0
                + energy**4 * r**7 / 840.0
            )
            spatial[~small] = (
                4.0
                * math.pi
                * (np.sin(z[~small]) - z[~small] * np.cos(z[~small]))
                / energy**3
            )
        total += step * float(np.sum(np.cos(energy * t) * spatial))
    return total / VOLUME


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    status = data["status"]
    if status["verdict"] != "CONDITIONAL_SCALAR_DIAMOND_DENSITY_ONLY":
        fail("unexpected physical verdict")
    if status["alpha_computed"] is not False:
        fail("alpha firewall failed")

    sealed = data["sealed_inputs"]
    for row in sealed["authorities"]:
        if sha256(ROOT / row["path"]) != row["sha256"]:
            fail(f"authority changed: {row['path']}")

    for energy in (0.0, 0.2, 1.0, 3.0, 7.0):
        direct = midpoint_diamond_integral(energy)
        if abs(direct - closed_form(energy)) > 2.0e-9:
            fail(f"independent diamond integral failed at E={energy}")

    if data["regulator_comparison"]["same_class"] is not False:
        fail("discrete/covariant decay classes were conflated")
    if data["conditional_scalar_result"]["normalization"] != "12*pi":
        fail("normalization changed")
    print("R3_4_V002_INDEPENDENT_VERIFICATION_PASS")


if __name__ == "__main__":
    main()
