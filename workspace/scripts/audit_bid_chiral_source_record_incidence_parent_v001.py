#!/usr/bin/env python3
"""Exact audit of the BID chiral source-record incidence parent."""

from __future__ import annotations

import cmath
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
    identity = np.eye(2, dtype=complex)
    z_chi = np.diag([1.0, -1.0])

    phase_pairs = ((0.0, 0.0), (0.2, 1.1), (math.pi / 3, -0.7))
    reduced_maps = []
    for alpha, beta in phase_pairs:
        endpoint_map = np.array(
            [
                [0.0, cmath.exp(1j * alpha)],
                [cmath.exp(1j * beta), 0.0],
            ]
        )
        common_phase = (alpha + beta) / 2.0
        endpoint_rephasing = cmath.exp(-1j * common_phase) * identity
        reduced_map = endpoint_rephasing @ endpoint_map
        delta = (alpha - beta) / 2.0
        expected_reduced = np.array(
            [
                [0.0, cmath.exp(1j * delta)],
                [cmath.exp(-1j * delta), 0.0],
            ]
        )
        require(np.allclose(endpoint_map.conj().T @ endpoint_map, identity), "endpoint map not unitary")
        require(np.allclose(endpoint_map @ z_chi + z_chi @ endpoint_map, 0.0), "endpoint map not chiral odd")
        require(np.allclose(reduced_map, expected_reduced), "phase reduction failed")
        require(np.allclose(reduced_map, reduced_map.conj().T), "reduced map not Hermitian")
        reduced_maps.append(reduced_map)

    # Exhaust the continuous relative-magnitude family analytically on a
    # dense grid. The exact inequality is the arithmetic-geometric mean bound.
    weights = np.linspace(0.001, 1.999, 1999)
    endpoint_probabilities = 4.0 * weights * (2.0 - weights) / 4.0
    maximum_index = int(np.argmax(endpoint_probabilities))
    require(abs(weights[maximum_index] - 1.0) < 1e-15, "weight maximum shifted")
    require(abs(endpoint_probabilities[maximum_index] - 1.0) < 1e-15, "completion maximum not one")
    require(bool(np.all(endpoint_probabilities <= 1.0 + 1e-15)), "probability exceeds one")
    require(bool(np.all(endpoint_probabilities[weights != 1.0] < 1.0)), "completion maximum not unique")

    expected = np.array(
        [-math.sqrt(2), -math.sqrt(2), 0.0, 0.0, math.sqrt(2), math.sqrt(2)]
    )
    for reduced_map in reduced_maps:
        incidence = np.vstack((-identity, reduced_map))
        require(np.allclose(incidence.conj().T @ incidence, 2.0 * identity), "incidence Gram mismatch")
        joint = np.block(
            [
                [np.zeros((4, 4), dtype=complex), incidence],
                [incidence.conj().T, np.zeros((2, 2), dtype=complex)],
            ]
        )
        require(np.allclose(joint, joint.conj().T), "joint operator not self-adjoint")
        require(np.allclose(np.linalg.eigvalsh(joint), expected, atol=2e-14), "joint spectrum mismatch")

        # Basis: Lr,Rr,Lp,Rp,Le,Re.
        left_root = np.eye(6, dtype=complex)[:, 0]
        right_root = np.eye(6, dtype=complex)[:, 1]
        expected_left = np.zeros(6, dtype=complex)
        expected_right = np.zeros(6, dtype=complex)
        expected_left[2:4] = reduced_map @ np.array([1.0, 0.0])
        expected_right[2:4] = reduced_map @ np.array([0.0, 1.0])
        unitary = evolve(joint, math.pi / math.sqrt(2.0))
        require(np.linalg.norm(unitary @ left_root - expected_left) < 2e-14, "left transfer failed")
        require(np.linalg.norm(unitary @ right_root - expected_right) < 2e-14, "right transfer failed")

    print(f"endpoint_phase_competitors={len(phase_pairs)}")
    print("common_endpoint_phase_removal=PASS")
    print("relative_axial_phase_unresolved=TRUE")
    print("complete_relative_magnitude_family=ADMITTED")
    print("conditional_pure_offdiagonal_perfect_transfer_unique_at_|a|=|b|=1=PASS")
    print("source_independent_scaled_normalization_derived=FALSE")
    print("parent_zero_form_detuning_derived_absent=FALSE")
    print("incidence_Gram=2I")
    print("joint_spectrum=-sqrt2,-sqrt2,0,0,+sqrt2,+sqrt2")
    print("chiral_odd_completed_endpoint_transfer=PASS")
    print("physical_source_mass_computed=FALSE")
    print("alpha_computed=FALSE")
    print("full_normal_dependent_source_map_family_exhausted=FALSE")
    print("BID_CHIRAL_SOURCE_RECORD_INCIDENCE_PARENT_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
