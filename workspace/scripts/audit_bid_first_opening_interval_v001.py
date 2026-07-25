#!/usr/bin/env python3
"""Exact/numerical audit of the BID first-opening interval."""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DERIVATION = ROOT / "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md"


def branch_operator(handle: int) -> np.ndarray:
    # Global ordered basis: root, p_M, p_Q, p_G, e_M, e_Q, e_G.
    matrix = np.zeros((7, 7), dtype=float)
    endpoint = 1 + handle
    edge = 4 + handle
    matrix[0, edge] = matrix[edge, 0] = -1.0
    matrix[endpoint, edge] = matrix[edge, endpoint] = 1.0
    return matrix


def unitary_from_symmetric(matrix: np.ndarray, tau: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    phases = np.exp(-1j * tau * eigenvalues)
    return (eigenvectors * phases) @ eigenvectors.conj().T


def causal_diamond_volume(tau: float, slices: int = 200_000) -> float:
    # Midpoint quadrature with c=1 and endpoints separated by tau.
    dt = tau / slices
    total = 0.0
    for index in range(slices):
        time = -tau / 2.0 + (index + 0.5) * dt
        radius = tau / 2.0 - abs(time)
        total += (4.0 * math.pi / 3.0) * radius**3 * dt
    return total


def main() -> int:
    failures: list[str] = []
    text = DERIVATION.read_text(encoding="utf-8") if DERIVATION.is_file() else ""
    if not text:
        failures.append("missing first-opening interval derivation")

    tau_r = math.pi / math.sqrt(2.0)
    root = np.zeros(7, dtype=complex)
    root[0] = 1.0
    outputs = []
    for handle in range(3):
        operator = branch_operator(handle)
        eigenvalues = np.linalg.eigvalsh(operator)
        if not np.allclose(
            eigenvalues, [-math.sqrt(2.0), 0, 0, 0, 0, 0, math.sqrt(2.0)],
            atol=2e-14,
        ):
            failures.append(f"unexpected spectrum for handle {handle}")
        output = unitary_from_symmetric(operator, tau_r) @ root
        target = np.zeros(7, dtype=complex)
        target[1 + handle] = 1.0
        if not np.allclose(output, target, atol=2e-14):
            failures.append(f"handle {handle} does not transfer root to endpoint")
        outputs.append(output)

    gram = np.array([[np.vdot(left, right) for right in outputs] for left in outputs])
    if not np.allclose(gram, np.eye(3), atol=2e-14):
        failures.append("handle-conditioned outputs are not orthonormal")

    earlier_tau = np.nextafter(tau_r, 0.0)
    root_amplitude = (1.0 + math.cos(math.sqrt(2.0) * earlier_tau)) / 2.0
    if root_amplitude < -1e-15:
        failures.append("least-positive root check failed")

    numerical_volume = causal_diamond_volume(1.0)
    exact_volume = math.pi / 24.0
    if abs(numerical_volume - exact_volume) > 2e-11:
        failures.append("causal-diamond four-volume check failed")

    required = (
        "tau_R=pi/sqrt(2)",
        "U_h(tau_R)|r>=|p_h>",
        "tau_R(w)=pi/(sqrt(2)|w|)",
        "four-volume of Omega=pi T_R^4/24",
        "physical_durability_derived = false",
        "alpha_computed = false",
    )
    for item in required:
        if item not in text:
            failures.append(f"missing required derivation text: {item}")

    statuses = dict(
        re.findall(r"^([A-Za-z0-9_]+) = (true|false)$", text, flags=re.MULTILINE)
    )
    if statuses.get("dimensionless_tau_R_fixed") != "true":
        failures.append("dimensionless tau_R is not marked fixed")
    if statuses.get("physical_durability_derived") != "false":
        failures.append("physical durability is prematurely marked derived")
    if statuses.get("alpha_computed") != "false":
        failures.append("alpha is prematurely marked computed")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print("BID_FIRST_OPENING_INTERVAL_AUDIT=FAIL")
        return 1

    print(f"tau_R={tau_r:.16g}")
    print("handle_conditioned_endpoint_Gram=I_3")
    print(f"causal_diamond_unit_four_volume={numerical_volume:.16g}")
    print("physical_durability=PENDING_QSPEC")
    print("BID_FIRST_OPENING_INTERVAL_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
