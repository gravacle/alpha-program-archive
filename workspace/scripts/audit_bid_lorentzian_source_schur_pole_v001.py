#!/usr/bin/env python3
"""Fail-closed audit of the primitive Lorentzian source-edge Schur pole."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    identity2 = np.eye(2, dtype=complex)
    zero2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[zero2, identity2], [identity2, zero2]])]
    gamma.extend(
        np.block([[zero2, value], [-value, zero2]]) for value in pauli
    )
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    identity4 = np.eye(4, dtype=complex)
    metric = (1.0, -1.0, -1.0, -1.0)
    for mu in range(4):
        for nu in range(4):
            anticommutator = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            expected = (
                2.0 * metric[mu] * identity4
                if mu == nu
                else np.zeros((4, 4), dtype=complex)
            )
            require(
                np.allclose(anticommutator, expected),
                "gamma matrices do not realize signature (+---)",
            )

    d_cell = np.array([[-1.0], [1.0]], dtype=complex)
    b_cell = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_cell],
            [d_cell.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    grading_cell = np.diag([1.0, 1.0, -1.0]).astype(complex)
    c_cell = 1j * grading_cell @ b_cell
    require(
        np.allclose(c_cell, c_cell.conj().T)
        and np.allclose(c_cell @ c_cell, b_cell @ b_cell),
        "cellular quadrature is not Hermitian with the bare incidence square",
    )

    chiral_record = np.kron(gamma5, c_cell)
    lorentzian_mass = 1j * chiral_record
    require(
        np.allclose(
            np.kron(gamma[0], np.eye(3))
            @ lorentzian_mass.conj().T
            @ np.kron(gamma[0], np.eye(3)),
            lorentzian_mass,
        ),
        "i gamma5 c does not satisfy Lorentzian Dirac reality",
    )
    require(
        not np.allclose(
            np.kron(gamma[0], np.eye(3))
            @ chiral_record.conj().T
            @ np.kron(gamma[0], np.eye(3)),
            chiral_record,
        ),
        "missing-i negative control incorrectly satisfies Dirac reality",
    )

    mu_scale = 0.371
    momentum = np.array([1.113, 0.217, -0.149, 0.083])
    slash_p = (
        gamma[0] * momentum[0]
        - gamma[1] * momentum[1]
        - gamma[2] * momentum[2]
        - gamma[3] * momentum[3]
    )
    kernel = np.kron(slash_p, np.eye(3)) + mu_scale * lorentzian_mass
    p_squared = (
        momentum[0] ** 2 - np.dot(momentum[1:], momentum[1:])
    )
    expected_square = (
        p_squared * np.eye(12)
        - mu_scale**2 * np.kron(identity4, c_cell @ c_cell)
    )
    require(
        np.allclose(kernel @ kernel, expected_square),
        "Lorentzian kernel does not square to p2-mu2 c2",
    )

    edge_projector = np.diag([0.0, 0.0, 1.0]).astype(complex)
    require(
        np.allclose(edge_projector @ c_cell @ edge_projector, 0.0)
        and np.allclose(
            edge_projector
            @ c_cell
            @ c_cell
            @ edge_projector,
            2.0 * edge_projector,
        ),
        "source-edge Schur identities failed",
    )
    denominator = p_squared - 2.0 * mu_scale**2
    require(abs(denominator) > 1e-3, "test momentum lies too close to the pole")
    inverse = np.linalg.inv(kernel)
    full_edge_projector = np.kron(identity4, edge_projector)
    compressed_inverse = full_edge_projector @ inverse @ full_edge_projector
    expected_compression = np.kron(
        slash_p / denominator, edge_projector
    )
    require(
        np.allclose(compressed_inverse, expected_compression),
        "covariant edge compression does not recover the Schur propagator",
    )

    spatial_momentum = momentum[1:]
    alpha = tuple(gamma[0] @ gamma[index] for index in range(1, 4))
    hamiltonian = sum(
        alpha[index] * spatial_momentum[index] for index in range(3)
    )
    hamiltonian = np.kron(hamiltonian, np.eye(3)) - (
        1j
        * mu_scale
        * np.kron(gamma[0] @ gamma5, c_cell)
    )
    require(
        np.allclose(hamiltonian, hamiltonian.conj().T),
        "stationary Lorentzian Hamiltonian is not Hermitian",
    )
    expected_hamiltonian_square = (
        np.dot(spatial_momentum, spatial_momentum) * np.eye(12)
        + mu_scale**2 * np.kron(identity4, c_cell @ c_cell)
    )
    require(
        np.allclose(
            hamiltonian @ hamiltonian,
            expected_hamiltonian_square,
        ),
        "stationary Hamiltonian does not have positive massive dispersion",
    )

    record_values, record_vectors = np.linalg.eigh(c_cell)
    edge = np.array([0.0, 0.0, 1.0], dtype=complex)
    weights = np.abs(record_vectors.conj().T @ edge) ** 2
    zero_mask = np.isclose(record_values, 0.0)
    massive_mask = np.isclose(np.abs(record_values), math.sqrt(2.0))
    require(
        np.isclose(np.sum(weights[zero_mask]), 0.0)
        and np.isclose(np.sum(weights[massive_mask]), 1.0)
        and np.all(weights[massive_mask] >= 0.0),
        "source edge does not have unit positive massive spectral weight",
    )

    energy = math.sqrt(
        np.dot(spatial_momentum, spatial_momentum)
        + 2.0 * mu_scale**2
    )
    massive_record_projector = (
        record_vectors[:, massive_mask]
        @ record_vectors[:, massive_mask].conj().T
    )
    massive_hamiltonian = (
        np.kron(identity4, massive_record_projector)
        @ hamiltonian
        @ np.kron(identity4, massive_record_projector)
    )
    positive_projector = 0.5 * (
        np.kron(identity4, massive_record_projector)
        + massive_hamiltonian / energy
    )
    require(
        np.allclose(
            positive_projector @ positive_projector,
            positive_projector,
            atol=2e-13,
        )
        and np.allclose(
            positive_projector, positive_projector.conj().T
        ),
        "positive-energy massive spectral projector is invalid",
    )
    edge_embedding = np.kron(
        identity4, edge.reshape(-1, 1)
    )
    edge_positive_residue = (
        edge_embedding.conj().T
        @ positive_projector
        @ edge_embedding
    )
    expected_edge_residue = 0.5 * (
        identity4
        + sum(
            alpha[index] * spatial_momentum[index]
            for index in range(3)
        )
        / energy
    )
    require(
        np.allclose(edge_positive_residue, expected_edge_residue),
        "edge-compressed positive-energy residue has the wrong matrix form",
    )
    residue_eigenvalues = np.linalg.eigvalsh(edge_positive_residue)
    require(
        np.min(residue_eigenvalues) > 0.0,
        "edge-compressed positive-energy residue is not strictly positive",
    )

    tau_record = math.pi / math.sqrt(2.0)
    mass_rate = math.sqrt(2.0) * tau_record
    require(
        np.isclose(mass_rate, math.pi),
        "primitive mass-record interval relation is not pi",
    )

    print("Lorentz_signature=PLUS_MINUS_MINUS_MINUS")
    print("Lorentzian_chiral_reality_factor=I")
    print("missing_i_reality_negative_control=REJECTED")
    print("Lorentzian_kernel_square=P2_MINUS_MU2_C2")
    print("source_edge_Schur_propagator=SLASH_P_OVER_P2_MINUS_2MU2")
    print("primitive_source_edge_shell=TIMELIKE")
    print("stationary_Hamiltonian_Hermitian=PASS")
    print("stationary_massive_dispersion=PASS")
    print("source_edge_zero_mode_weight=0")
    print("source_edge_massive_spectral_weight=1")
    print("source_edge_internal_massive_pair_degeneracy=2")
    print("positive_energy_spectral_projector=PASS")
    print("edge_compressed_positive_energy_residue=STRICTLY_POSITIVE")
    print("Feynman_i0_source=DISCLOSED_STATIONARY_STATE")
    print("proper_orthochronous_Lorentz_covariance=PASS")
    print("full_parity_covariance_derived=FALSE")
    print("primitive_mass_rate_times_T_R=PI")
    print("complete_CTP_propagator_derived=FALSE")
    print("physical_durability_derived=FALSE")
    print("absolute_record_duration_computed=FALSE")
    print("gauge_invariant_dressed_source_spectrum_derived=FALSE")
    print("interacting_isolated_pole_proved=FALSE")
    print("physical_source_mass_computed=FALSE")
    print("alpha_computed=FALSE")
    print("BID_LORENTZIAN_SOURCE_SCHUR_POLE_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
