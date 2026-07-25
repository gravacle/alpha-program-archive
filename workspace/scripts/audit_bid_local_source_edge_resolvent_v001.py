#!/usr/bin/env python3
"""Audit the exact source-edge resolvent of the BID joint parent."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    identity = np.eye(2, dtype=complex)
    x_chi = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    incidence = np.vstack((-identity, x_chi))
    parent = np.block(
        [
            [np.zeros((4, 4), dtype=complex), incidence],
            [incidence.conj().T, np.zeros((2, 2), dtype=complex)],
        ]
    )

    test_points = (0.3j, 0.7 + 0.2j, -1.1 + 0.4j, 2.0j)
    for z_value in test_points:
        resolvent = np.linalg.inv(z_value * np.eye(6) - parent)
        source_block = resolvent[4:6, 4:6]
        exact = (z_value / (z_value**2 - 2.0)) * identity
        require(
            np.allclose(source_block, exact, atol=2e-14),
            "source resolvent block disagrees with the exact expression",
        )

    zero_modes = []
    values, vectors = np.linalg.eigh(parent)
    for index, value in enumerate(values):
        if abs(value) < 1e-13:
            zero_modes.append(vectors[:, index])
    require(len(zero_modes) == 2, "parent does not have two zero modes")
    require(
        max(np.linalg.norm(vector[4:6]) for vector in zero_modes) < 2e-14,
        "a zero mode has nonzero source residue",
    )

    tau_record = math.pi / math.sqrt(2.0)
    phase = math.sqrt(2.0) * tau_record
    require(
        abs(phase - math.pi) < 1e-15,
        "dimensionless source-record phase is not pi",
    )

    print(f"resolvent_test_points={len(test_points)}")
    print("source_resolvent=z/(z^2-2) I_2")
    print("source_zero_pole=ABSENT")
    print("record_zero_mode_source_residue=ZERO")
    print(f"dimensionless_source_record_phase={phase:.17g}")
    print("physical_source_mass_computed=FALSE")
    print("alpha_computed=FALSE")
    print("BID_LOCAL_SOURCE_EDGE_RESOLVENT_AUDIT=PASS")


if __name__ == "__main__":
    main()
