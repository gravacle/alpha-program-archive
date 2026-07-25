#!/usr/bin/env python3
"""Compare handle-conditioned and full-star BID opening at the frozen tau."""

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
    incidence = np.zeros((4, 3), dtype=complex)
    incidence[0, :] = -1.0
    incidence[1, 0] = 1.0
    incidence[2, 1] = 1.0
    incidence[3, 2] = 1.0
    full_star = np.block(
        [
            [np.zeros((4, 4), dtype=complex), incidence],
            [incidence.conj().T, np.zeros((3, 3), dtype=complex)],
        ]
    )

    root = np.zeros(7, dtype=complex)
    root[0] = 1.0
    tau_record = math.pi / math.sqrt(2.0)
    output = evolve(full_star, tau_record) @ root

    root_magnitude = abs(output[0])
    endpoint_probability = float(np.sum(np.abs(output[1:4]) ** 2))
    edge_probability = float(np.sum(np.abs(output[4:]) ** 2))

    require(abs(root_magnitude - 0.050308493468939536) < 1e-13, "root magnitude changed")
    require(abs(endpoint_probability - 0.3006379858590792) < 1e-13, "endpoint probability changed")
    require(abs(edge_probability - 0.6968310696258078) < 1e-13, "edge probability changed")
    require(abs(root_magnitude**2 + endpoint_probability + edge_probability - 1.0) < 1e-13, "probability not conserved")

    print(f"root_amplitude_magnitude={root_magnitude:.16g}")
    print(f"endpoint_probability={endpoint_probability:.16g}")
    print(f"edge_probability={edge_probability:.16g}")
    print("full_star_completes_at_handle_tau_R=FALSE")
    print("source_access_projectors_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_ACTIVE_HANDLE_CONTROL_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
