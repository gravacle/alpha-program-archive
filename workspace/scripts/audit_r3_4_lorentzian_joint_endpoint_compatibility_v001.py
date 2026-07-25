#!/usr/bin/env python3
"""Audit exact endpoint compatibility in the local Lorentzian joint parent."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_SPEC_V001.md"
SEAL = ROOT / "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_lorentzian_joint_endpoint_compatibility_v001.json"

PINNED = {
    "BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md":
        "dc0498615a94218c56ed91a3e679a2aa55e32d4fcb96220a50a7a88669a8fc34",
    "scripts/audit_bid_lorentzian_source_schur_pole_v001.py":
        "4de9e7528b86682670373ac6f1e215706013300c94c5b9febb880096216c832b",
    "BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md":
        "6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546",
    "scripts/audit_bid_free_quasifree_ctp_propagator_v001.py":
        "922260b10d026be0e8f9f13d48cc880fc2db56e9ba0f1e5ea6fd861a869adb0b",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "scripts/audit_bid_first_opening_interval_v001.py":
        "c5de96772a85f128df0a51a68d364a61c73b8c94c7e8e13e26b95964048651d5",
    "CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md":
        "60c82b021a7f5ffcb514ae8c20f083a7b2c9b42872586922b1c0464c4822d73f",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


def main() -> None:
    require(
        SEAL.read_text(encoding="ascii").strip().split()
        == [sha256(SPEC), SPEC.name],
        "Specification seal failed",
    )
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Upstream drift: {name}")

    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in pauli)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    dirac_alpha = tuple(gamma[0] @ gamma[index] for index in range(1, 4))
    internal_sign = -1.0j * gamma[0] @ gamma5
    sign_values, sign_vectors = np.linalg.eigh(internal_sign)
    spin = sign_vectors[:, int(np.argmax(sign_values))]

    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    initial = np.kron(spin, ready)
    pointer_projector = np.kron(
        np.eye(4, dtype=complex), np.outer(pointer, pointer)
    )

    duration = 1.0
    tau = math.pi / math.sqrt(2.0)
    mu = tau / duration
    momenta = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0)
    probabilities = {}
    frequency_data = {}
    for momentum in momenta:
        kinetic = dirac_alpha[0] * momentum
        hamiltonian = np.kron(kinetic, np.eye(3)) + (
            mu * np.kron(internal_sign, c_partial)
        )
        output = exp_hermitian(hamiltonian, duration) @ initial
        probabilities[str(momentum)] = float(
            np.real(np.vdot(output, pointer_projector @ output))
        )
        frequency_data[str(momentum)] = {
            "massless_frequency": momentum,
            "massive_frequency": math.sqrt(momentum**2 + 2.0 * mu**2),
        }

    grid = np.linspace(-3.0, 3.0, 1201)
    sigma = 0.7
    weights = np.exp(-(grid / sigma) ** 2)
    weights /= np.sum(weights)
    wavepacket_probability = 0.0
    for momentum, weight in zip(grid, weights):
        kinetic = dirac_alpha[0] * momentum
        hamiltonian = np.kron(kinetic, np.eye(3)) + (
            mu * np.kron(internal_sign, c_partial)
        )
        output = exp_hermitian(hamiltonian, duration) @ initial
        wavepacket_probability += weight * float(
            np.real(np.vdot(output, pointer_projector @ output))
        )

    z_record = (ready + pointer) / math.sqrt(2.0)
    m_record = (ready - pointer) / math.sqrt(2.0)
    zero_mode_error = float(np.linalg.norm(c_partial @ z_record))
    massive_square_error = float(
        np.linalg.norm(c_partial @ c_partial @ m_record - 2.0 * m_record)
    )

    require(zero_mode_error < 1e-13, "Record zero mode failed")
    require(massive_square_error < 1e-13, "Record massive mode failed")
    require(abs(probabilities["0.0"] - 1.0) < 1e-12,
            "Rest-normal endpoint failed")
    require(
        max(abs(probabilities[str(p)] - probabilities["0.0"]) for p in momenta[1:])
        > 0.1,
        "Momentum dependence was not resolved",
    )
    require(wavepacket_probability < 0.999, "Wavepacket remained an exact endpoint")

    result = {
        "schema": "r3.4-lorentzian-joint-endpoint-compatibility-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "preseal_exploratory_diagnostic_performed": True,
        "dimensionless_record_duration": duration,
        "dimensionless_incidence_rate": mu,
        "record_zero_mode_error": zero_mode_error,
        "record_massive_square_error": massive_square_error,
        "pointer_probabilities_at_T_R": probabilities,
        "frequency_data": frequency_data,
        "gaussian_wavepacket_sigma": sigma,
        "gaussian_wavepacket_pointer_probability_at_T_R":
            wavepacket_probability,
        "exact_transfer_conditions": {
            "massive_phase": "E(p) t = n pi",
            "kinetic_phase": "|p| t = k pi",
            "parity": "n+k odd",
        },
        "rest_normal_exact_endpoint_derived": True,
        "universal_exact_finite_wavepacket_write_derived": False,
        "primitive_internal_interval_distinguished_from_physical_durability": True,
        "transported_interaction_promoted_as_repair": False,
        "thresholded_direct_limit_route_required": True,
        "physical_thresholded_durability_derived": False,
        "physical_in_state_selected": False,
        "complete_root_spectral_measure_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
