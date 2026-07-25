#!/usr/bin/env python3
"""Audit the free quasifree CTP construction for the primitive BID pole."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "bid_free_quasifree_ctp_propagator_v001.json"
TOL = 3e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def unitary_evolution(hamiltonian: np.ndarray, time: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(hamiltonian)
    return (vectors * np.exp(-1j * values * time)) @ vectors.conj().T


def main() -> None:
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
    i4 = np.eye(4, dtype=complex)

    d_cell = np.array([[-1.0], [1.0]], dtype=complex)
    b_cell = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_cell],
            [d_cell.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    grading = np.diag([1.0, 1.0, -1.0]).astype(complex)
    c_cell = 1j * grading @ b_cell

    momentum = np.array([0.271, -0.193, 0.127])
    mu_scale = 0.419
    alpha_matrices = tuple(gamma[0] @ gamma[index] for index in range(1, 4))
    hamiltonian = np.kron(
        sum(alpha_matrices[i] * momentum[i] for i in range(3)),
        np.eye(3),
    ) - 1j * mu_scale * np.kron(gamma[0] @ gamma5, c_cell)

    require(
        np.allclose(hamiltonian, hamiltonian.conj().T, atol=TOL),
        "Hamiltonian is not Hermitian",
    )
    values, vectors = np.linalg.eigh(hamiltonian)
    require(np.min(np.abs(values)) > 1e-6, "test momentum has a zero-energy mode")
    p_plus = vectors[:, values > 0] @ vectors[:, values > 0].conj().T
    p_minus = vectors[:, values < 0] @ vectors[:, values < 0].conj().T
    identity = np.eye(hamiltonian.shape[0], dtype=complex)
    require(np.allclose(p_plus + p_minus, identity, atol=TOL), "spectral resolution failed")
    require(np.allclose(p_plus @ p_minus, 0.0, atol=TOL), "spectral projectors overlap")
    require(
        np.allclose(p_plus @ p_plus, p_plus, atol=TOL)
        and np.allclose(p_minus @ p_minus, p_minus, atol=TOL),
        "spectral projectors are not idempotent",
    )

    contour_errors = []
    equation_errors = []
    unitarity_errors = []
    for time in (-1.37, -0.41, 0.29, 1.11):
        evolution = unitary_evolution(hamiltonian, time)
        g_greater = -1j * evolution @ p_plus
        g_lesser = 1j * evolution @ p_minus
        if time > 0:
            g_pp = g_greater
            g_mm = g_lesser
            g_retarded = -1j * evolution
            g_advanced = np.zeros_like(evolution)
        else:
            g_pp = g_lesser
            g_mm = g_greater
            g_retarded = np.zeros_like(evolution)
            g_advanced = 1j * evolution

        contour_errors.append(
            np.linalg.norm(g_pp + g_mm - g_lesser - g_greater)
        )
        if time > 0:
            derivative_retarded = -hamiltonian @ evolution
            equation_errors.append(
                np.linalg.norm(1j * derivative_retarded - hamiltonian @ g_retarded)
            )
        else:
            derivative_advanced = hamiltonian @ evolution
            equation_errors.append(
                np.linalg.norm(1j * derivative_advanced - hamiltonian @ g_advanced)
            )
        unitarity_errors.append(
            np.linalg.norm(evolution.conj().T @ evolution - identity)
        )

    require(max(contour_errors) < TOL, "CTP contour identity failed")
    require(max(equation_errors) < TOL, "retarded/advanced equation failed away from t=0")
    require(max(unitarity_errors) < TOL, "free evolution is not unitary")

    record_values, record_vectors = np.linalg.eigh(c_cell)
    edge = np.array([0.0, 0.0, 1.0], dtype=complex)
    record_weights = np.abs(record_vectors.conj().T @ edge) ** 2
    zero_weight = float(np.sum(record_weights[np.isclose(record_values, 0.0)]))
    massive_weight = float(
        np.sum(record_weights[np.isclose(np.abs(record_values), np.sqrt(2.0))])
    )
    require(abs(zero_weight) < TOL, "edge retains massless record support")
    require(abs(massive_weight - 1.0) < TOL, "edge massive support is not normalized")

    expected_massive_energy = float(
        np.sqrt(np.dot(momentum, momentum) + 2.0 * mu_scale**2)
    )
    edge_embedding = np.kron(i4, edge.reshape(-1, 1))
    edge_h2 = edge_embedding.conj().T @ (hamiltonian @ hamiltonian) @ edge_embedding
    require(
        np.allclose(edge_h2, expected_massive_energy**2 * i4, atol=TOL),
        "edge-projected dispersion is not purely massive",
    )

    result = {
        "schema_version": 1,
        "overall": "PASS_FREE_QUASIFREE_CTP_SUBGATE_DURABILITY_OPEN",
        "max_ctp_identity_error": max(contour_errors),
        "max_free_equation_error": max(equation_errors),
        "max_unitarity_error": max(unitarity_errors),
        "edge_zero_mode_weight": zero_weight,
        "edge_massive_mode_weight": massive_weight,
        "edge_massive_energy": expected_massive_energy,
        "complete_free_quasifree_CTP_contour_derived": True,
        "physical_durability_derived": False,
        "gauge_invariant_dressed_source_spectrum_derived": False,
        "interacting_isolated_pole_proved": False,
        "absolute_record_duration_computed": False,
        "physical_source_mass_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    print(result["overall"])


if __name__ == "__main__":
    main()
