#!/usr/bin/env python3
"""Gauge/naturality audit of the primitive BID record-transition amplitude."""

from __future__ import annotations

import cmath
import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def handle_operator(transport: complex) -> np.ndarray:
    return np.array(
        [
            [0.0, 0.0, -1.0],
            [0.0, 0.0, transport],
            [-1.0, transport.conjugate(), 0.0],
        ],
        dtype=complex,
    )


def evolve(operator: np.ndarray, tau: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    return (
        eigenvectors
        @ np.diag(np.exp(-1j * tau * eigenvalues))
        @ eigenvectors.conj().T
    )


def main() -> None:
    root = np.array([1.0, 0.0, 0.0], dtype=complex)
    endpoint = np.array([0.0, 1.0, 0.0], dtype=complex)
    tau_record = math.pi / math.sqrt(2.0)

    phases = (
        0.0,
        math.pi / 11.0,
        math.pi / 3.0,
        math.pi,
        1.731,
    )
    returned_scalars = []

    for phase in phases:
        transport = cmath.exp(1j * phase)
        unitary = evolve(handle_operator(transport), tau_record)
        transition = np.vdot(endpoint, unitary @ root)
        returned = transport.conjugate() * transition
        returned_scalars.append(returned)
        require(
            abs(returned - 1.0) < 2e-14,
            "connection-returned transition scalar is not one",
        )

    require(
        max(abs(value - returned_scalars[0]) for value in returned_scalars)
        < 2e-14,
        "returned transition scalar depends on endpoint phase",
    )

    print(f"phase_samples={len(phases)}")
    print("connection_returned_transition_scalar=1")
    print("endpoint_rephasing_invariance=PASS")
    print("primitive_transition_baseline_nonzero=PASS")
    print("volume_uniform_zero_free_neighborhood=PENDING")
    print("alpha_computed=FALSE")
    print("BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_AUDIT=PASS")


if __name__ == "__main__":
    main()
