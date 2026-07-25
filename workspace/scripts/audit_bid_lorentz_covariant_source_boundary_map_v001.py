#!/usr/bin/env python3
"""Audit the local Lorentz-covariant source-boundary map."""

from __future__ import annotations

import math

import numpy as np


def matrix_rank(matrix: np.ndarray, tolerance: float = 1e-11) -> int:
    return int(np.sum(np.linalg.svd(matrix, compute_uv=False) > tolerance))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sigma = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma0 = np.block([[z2, i2], [i2, z2]])
    gamma = [gamma0]
    for pauli in sigma:
        gamma.append(np.block([[z2, pauli], [-pauli, z2]]))
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    i4 = np.eye(4, dtype=complex)
    metric = np.diag([1.0, -1.0, -1.0, -1.0])

    for mu in range(4):
        for nu in range(4):
            anticommutator = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            require(
                np.allclose(anticommutator, 2.0 * metric[mu, nu] * i4),
                "Clifford relation failed",
            )
    require(np.allclose(gamma5 @ gamma5, i4), "gamma5 does not square to I")
    for gamma_mu in gamma:
        require(
            np.allclose(gamma5 @ gamma_mu + gamma_mu @ gamma5, 0.0),
            "gamma5 does not anticommute with a gamma matrix",
        )

    # At a rest boundary, rotational covariance and chiral oddness leave one
    # complex scalar in each off-diagonal Weyl block: two complex dimensions.
    rotation_generators = [
        np.block([[pauli, z2], [z2, pauli]]) / 2.0 for pauli in sigma
    ]
    basis = []
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1.0
            basis.append(unit)
    rotation_blocks = []
    for generator in rotation_generators:
        rotation_blocks.append(
            np.stack(
                [
                    (unit @ generator - generator @ unit).reshape(-1)
                    for unit in basis
                ],
                axis=1,
            )
        )
    rotation_matrix = np.vstack(rotation_blocks)
    odd_matrix = np.stack(
        [(unit @ gamma5 + gamma5 @ unit).reshape(-1) for unit in basis], axis=1
    )
    combined = np.vstack((rotation_matrix, odd_matrix))
    complex_nullity = 16 - matrix_rank(combined)
    require(complex_nullity == 2, "local chiral-odd commutant nullity is not two")

    upper_to_lower = np.block([[z2, i2], [z2, z2]])
    lower_to_upper = np.block([[z2, z2], [i2, z2]])
    for candidate in (upper_to_lower, lower_to_upper):
        for generator in rotation_generators:
            require(
                np.allclose(
                    candidate @ generator - generator @ candidate, 0.0
                ),
                "explicit chiral map is not rotationally invariant",
            )
        require(
            np.allclose(candidate @ gamma5 + gamma5 @ candidate, 0.0),
            "explicit chiral map is not chiral odd",
        )
    require(
        matrix_rank(
            np.stack(
                (upper_to_lower.reshape(-1), lower_to_upper.reshape(-1)),
                axis=1,
            )
        )
        == 2,
        "explicit chiral maps do not span a two-dimensional family",
    )

    deltas = (0.0, 0.37, 1.11)
    rapidities = (0.0, 0.2, -0.7)
    covariance_cases = 0
    for delta in deltas:
        chiral_phase = np.diag(np.exp(1j * delta * np.diag(gamma5)))
        rest_map = gamma0 @ chiral_phase
        expected_rest = np.block(
            [
                [z2, np.exp(1j * delta) * i2],
                [np.exp(-1j * delta) * i2, z2],
            ]
        )
        require(np.allclose(rest_map, expected_rest), "rest map is not C_delta")
        require(
            np.allclose(rest_map.conj().T @ rest_map, i4),
            "rest map is not unitary",
        )
        require(
            np.allclose(rest_map.conj().T, rest_map),
            "rest map is not self-adjoint",
        )
        require(
            np.allclose(rest_map @ gamma5 + gamma5 @ rest_map, 0.0),
            "rest map is not chiral odd",
        )

        for axis in range(1, 4):
            boost_generator = gamma0 @ gamma[axis]
            require(
                np.allclose(boost_generator @ boost_generator, i4),
                "boost generator has wrong square",
            )
            for rapidity in rapidities:
                spin_boost = (
                    math.cosh(rapidity / 2.0) * i4
                    - math.sinh(rapidity / 2.0) * boost_generator
                )
                spin_boost_inverse = (
                    math.cosh(rapidity / 2.0) * i4
                    + math.sinh(rapidity / 2.0) * boost_generator
                )
                slash_n = spin_boost @ gamma0 @ spin_boost_inverse
                boundary_metric = gamma0 @ slash_n
                map_n = spin_boost @ rest_map @ spin_boost_inverse
                riesz_map = slash_n @ chiral_phase

                require(
                    np.allclose(slash_n @ slash_n, i4),
                    "boosted normal slash does not square to I",
                )
                require(
                    np.allclose(map_n, riesz_map),
                    "boosted map differs from boundary Riesz map",
                )
                require(
                    np.allclose(
                        boundary_metric, boundary_metric.conj().T
                    ),
                    "boosted boundary metric is not Hermitian",
                )
                require(
                    np.min(np.linalg.eigvalsh(boundary_metric)) > 0.0,
                    "boosted boundary metric is not positive",
                )
                require(
                    np.allclose(
                        map_n.conj().T @ boundary_metric @ map_n,
                        boundary_metric,
                    ),
                    "boosted map is not h_n-unitary",
                )
                require(
                    np.allclose(
                        map_n.conj().T @ boundary_metric,
                        boundary_metric @ map_n,
                    ),
                    "boosted map is not h_n-self-adjoint",
                )
                covariance_cases += 1

    print("Clifford_3_plus_1=PASS")
    print(f"rotationally_isotropic_chiral_odd_complex_dimension={complex_nullity}")
    print("explicit_nullspace_basis_spans_complete_family=PASS")
    print("h_n_Hermitian_unitary_constraints=v=conjugate(u),|u|=1")
    print("boundary_normal_Riesz_map=PASS")
    print(f"proper_orthochronous_Lorentz_covariance_cases={covariance_cases}")
    print("positive_hypersurface_metric=PASS")
    print("h_n_unitarity_and_self_adjointness=PASS")
    print("rest_frame_C_delta_with_spin_multiplicity=PASS")
    print("neutral_bilinear_CPT_delta_family=DISCLOSED_ANALYTIC_RESULT")
    print("charged_boundary_CPT_intertwiner_derived=FALSE")
    print("relative_axial_phase_unresolved=TRUE")
    print("unit_magnitude_rho_derived_here=FALSE")
    print("global_particle_antiparticle_CAR_carrier_derived=FALSE")
    print("physical_source_mass_computed=FALSE")
    print("alpha_computed=FALSE")
    print("BID_LOCAL_PROPER_LORENTZ_RIESZ_KINEMATICS_AUDIT=PASS")


if __name__ == "__main__":
    main()
