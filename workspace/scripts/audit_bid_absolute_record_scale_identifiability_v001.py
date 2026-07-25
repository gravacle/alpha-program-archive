#!/usr/bin/env python3
"""Audit the exact positive scale orbit of first-opening dynamics."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def evolve(operator: np.ndarray, duration: float, hbar: float = 1.0) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1j * duration * values / hbar))
        @ vectors.conj().T
    )


def main() -> None:
    incidence = np.array([[-1.0], [1.0]])
    b_record = np.block(
        [
            [np.zeros((2, 2)), incidence],
            [incidence.T, np.zeros((1, 1))],
        ]
    )
    tau_r = math.pi / math.sqrt(2.0)
    base_duration = 3.7
    base_generator = tau_r * b_record / base_duration
    base_unitary = evolve(base_generator, base_duration)

    scale_factors = (0.125, 0.5, 1.0, 3.0, 17.0, 1000.0)
    for scale in scale_factors:
        duration = scale * base_duration
        generator = base_generator / scale
        require(
            np.allclose(
                evolve(generator, duration), base_unitary, atol=2e-14
            ),
            "positive scale competitor changed the first-opening unitary",
        )

    print(f"positive_scale_competitors={len(scale_factors)}")
    print("dimensionless_first_opening_evolution_invariant=PASS")
    print("scale_orbit_broken_by_current_kinematics=FALSE")
    print("absolute_SI_record_duration_derived=FALSE")
    print("Planck_time_selected=FALSE")
    print("coupled_gravity_record_stationarity_equation_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
