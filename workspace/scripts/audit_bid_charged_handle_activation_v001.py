#!/usr/bin/env python3
"""Exact controlled-source audit for the pure charged BID branch."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def evolve(operator: np.ndarray, tau: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    return (
        eigenvectors
        @ np.diag(np.exp(-1j * tau * eigenvalues))
        @ eigenvectors.conj().T
    )


def main() -> None:
    b_q = np.array(
        [
            [0.0, 0.0, -1.0],
            [0.0, 0.0, 1.0],
            [-1.0, 1.0, 0.0],
        ],
        dtype=complex,
    )
    p_0 = np.diag([1.0, 0.0])
    p_q = np.diag([0.0, 1.0])
    controlled = np.kron(p_0, np.zeros((3, 3))) + np.kron(p_q, b_q)
    flux = np.kron(p_q, np.eye(3))

    require(
        np.allclose(controlled, controlled.conj().T),
        "legacy controlled operator is not self-adjoint",
    )
    require(
        np.allclose(controlled @ flux, flux @ controlled),
        "legacy controlled operator violates flux nondemolition",
    )

    source_zero_root = np.zeros(6, dtype=complex)
    source_zero_root[0] = 1.0
    source_one_root = np.zeros(6, dtype=complex)
    source_one_root[3] = 1.0
    source_one_endpoint = np.zeros(6, dtype=complex)
    source_one_endpoint[4] = 1.0

    unitary = evolve(controlled, math.pi / math.sqrt(2.0))
    require(
        np.linalg.norm(unitary @ source_zero_root - source_zero_root)
        < 2e-14,
        "legacy zero-flux state is not fixed",
    )
    require(
        np.linalg.norm(unitary @ source_one_root - source_one_endpoint)
        < 2e-14,
        "legacy unit-flux state does not transfer",
    )

    print("legacy_positive_orientation_restriction=TRUE")
    print("authoritative_full_charge_projector=FALSE")
    print("charged_source_projector=Q_Sigma_ONLY_ON_LEGACY_ZERO_ONE_BRANCH")
    print("source_flux_nondemolition=PASS")
    print("zero_flux_no_charged_write=PASS")
    print("unit_flux_completed_charged_write=PASS")
    print("pure_charged_branch_tau_R_authorized=TRUE")
    print("composite_gravity_charge_branch=PENDING")
    print("alpha_computed=FALSE")
    print("BID_CHARGED_HANDLE_ACTIVATION_AUDIT=SUPERSEDED")


if __name__ == "__main__":
    main()
