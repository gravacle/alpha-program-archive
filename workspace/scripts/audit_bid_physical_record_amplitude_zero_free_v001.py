#!/usr/bin/env python3
"""Exact one-handle obstruction for the BID response amplitude."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    root = np.array([1.0, 0.0, 0.0], dtype=complex)
    endpoint = np.array([0.0, 1.0, 0.0], dtype=complex)
    operator = np.array(
        [
            [0.0, 0.0, -1.0],
            [0.0, 0.0, 1.0],
            [-1.0, 1.0, 0.0],
        ],
        dtype=complex,
    )

    tau_record = math.pi / math.sqrt(2.0)
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    unitary = (
        eigenvectors
        @ np.diag(np.exp(-1j * tau_record * eigenvalues))
        @ eigenvectors.conj().T
    )

    survival = np.vdot(root, unitary @ root)
    transition = np.vdot(endpoint, unitary @ root)

    require(abs(survival) < 1e-14, "root survival is not zero")
    require(abs(transition - 1.0) < 1e-14, "record transition is not complete")

    print(f"tau_R={tau_record:.17g}")
    print(f"root_survival_abs={abs(survival):.3e}")
    print(f"completed_record_transition={transition.real:.17g}")
    print("root_survival_log_response=REJECTED")
    print("physical_response_amplitude_selected=FALSE")
    print("alpha_computed=FALSE")
    print("BID_PHYSICAL_RECORD_AMPLITUDE_ZERO_FREE_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
