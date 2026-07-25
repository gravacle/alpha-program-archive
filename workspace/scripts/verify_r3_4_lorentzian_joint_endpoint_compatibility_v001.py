#!/usr/bin/env python3
"""Independent functional-calculus verifier for the Lorentzian endpoint gate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_SPEC_V001.md"
RESULT = ROOT / "results" / "r3_4_lorentzian_joint_endpoint_compatibility_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def closed_form_evolution(
    hamiltonian: np.ndarray,
    momentum: float,
    mu: float,
    c_squared: np.ndarray,
    duration: float,
) -> np.ndarray:
    """Evaluate exp(-iHt) from H^2, without diagonalizing H."""
    identity_spin = np.eye(4, dtype=complex)
    identity_record = np.eye(3, dtype=complex)
    massive_record = c_squared / 2.0
    zero_record = identity_record - massive_record
    omega_zero = abs(momentum)
    omega_massive = math.sqrt(momentum**2 + 2.0 * mu**2)

    cosine = (
        math.cos(omega_zero * duration) * np.kron(identity_spin, zero_record)
        + math.cos(omega_massive * duration)
        * np.kron(identity_spin, massive_record)
    )
    zero_sinc = (
        duration
        if omega_zero == 0.0
        else math.sin(omega_zero * duration) / omega_zero
    )
    sine_over_frequency = (
        zero_sinc * np.kron(identity_spin, zero_record)
        + math.sin(omega_massive * duration)
        / omega_massive
        * np.kron(identity_spin, massive_record)
    )
    return cosine - 1.0j * hamiltonian @ sine_over_frequency


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )

    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in pauli)
    gamma5 = 1.0j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    alpha_one = gamma[0] @ gamma[1]
    internal_sign = -1.0j * gamma[0] @ gamma5
    sign_values, sign_vectors = np.linalg.eigh(internal_sign)
    spin = sign_vectors[:, int(np.argmax(sign_values))]

    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    c_squared = c_partial @ c_partial
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    initial = np.kron(spin, ready)
    pointer_projector = np.kron(
        np.eye(4, dtype=complex), np.outer(pointer, pointer)
    )

    duration = 1.0
    mu = math.pi / math.sqrt(2.0)

    def probability(momentum: float) -> float:
        hamiltonian = (
            np.kron(momentum * alpha_one, np.eye(3, dtype=complex))
            + mu * np.kron(internal_sign, c_partial)
        )
        require(
            np.linalg.norm(
                hamiltonian @ hamiltonian
                - (
                    momentum**2 * np.eye(12, dtype=complex)
                    + mu**2 * np.kron(np.eye(4, dtype=complex), c_squared)
                )
            )
            < 1e-12,
            "H-squared decomposition failed",
        )
        output = closed_form_evolution(
            hamiltonian, momentum, mu, c_squared, duration
        ) @ initial
        return float(np.real(np.vdot(output, pointer_projector @ output)))

    for momentum_text, expected in stored["pointer_probabilities_at_T_R"].items():
        actual = probability(float(momentum_text))
        require(
            abs(actual - expected) < 2e-12,
            f"Closed-form probability mismatch at p={momentum_text}",
        )

    grid = np.linspace(-3.0, 3.0, 1201)
    weights = np.exp(-(grid / stored["gaussian_wavepacket_sigma"]) ** 2)
    weights /= np.sum(weights)
    packet_probability = sum(
        float(weight) * probability(float(momentum))
        for momentum, weight in zip(grid, weights)
    )
    require(
        abs(
            packet_probability
            - stored["gaussian_wavepacket_pointer_probability_at_T_R"]
        )
        < 2e-12,
        "Independent wavepacket probability mismatch",
    )
    require(
        abs(stored["pointer_probabilities_at_T_R"]["0.0"] - 1.0) < 1e-12,
        "Rest-normal endpoint is not exact",
    )
    require(packet_probability < 0.999, "Finite packet was incorrectly exact")
    require(
        stored["universal_exact_finite_wavepacket_write_derived"] is False,
        "Universal finite-packet endpoint was overclaimed",
    )
    require(
        stored["physical_thresholded_durability_derived"] is False,
        "Thresholded durability was overclaimed",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(
        stored["status"]
        == "EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED",
        "Wrong verdict",
    )
    print("PASS independent Lorentzian endpoint compatibility verification")


if __name__ == "__main__":
    main()
