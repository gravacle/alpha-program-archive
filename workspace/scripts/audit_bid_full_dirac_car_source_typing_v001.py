#!/usr/bin/env python3
"""Fail-closed finite type audit for the integrated Dirac/CAR source."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def annihilation_mode(mode: int, mode_count: int) -> np.ndarray:
    dimension = 1 << mode_count
    operator = np.zeros((dimension, dimension), dtype=complex)
    for state in range(dimension):
        if not ((state >> mode) & 1):
            continue
        lower_bits = state & ((1 << mode) - 1)
        sign = -1.0 if bin(lower_bits).count("1") % 2 else 1.0
        operator[state ^ (1 << mode), state] = sign
    return operator


def main() -> None:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sigma = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in sigma)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    identity4 = np.eye(4, dtype=complex)
    p_left = (identity4 - gamma5) / 2
    p_right = (identity4 + gamma5) / 2
    require(np.allclose(p_left @ p_left, p_left), "P_L is not a projector")
    require(np.allclose(p_right @ p_right, p_right), "P_R is not a projector")
    require(np.allclose(p_left @ p_right, 0), "chiral projectors overlap")
    require(
        np.allclose(p_left + p_right, identity4),
        "chiral projectors are incomplete",
    )
    require(
        round(float(np.trace(p_left).real)) == 2
        and round(float(np.trace(p_right).real)) == 2,
        "Dirac chirality multiplicities are not two plus two",
    )

    vector_charge_local = np.eye(4, dtype=complex)
    require(
        np.allclose(vector_charge_local @ gamma5, gamma5 @ vector_charge_local),
        "vector charge does not commute with chirality",
    )

    normal_checks = 0
    for axis in (
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 2.0, -3.0]) / np.sqrt(14.0),
    ):
        for rapidity in (0.0, 0.2, 1.0, 2.5):
            normal = np.concatenate(
                (
                    np.array([np.cosh(rapidity)]),
                    np.sinh(rapidity) * axis,
                )
            )
            slash_normal = (
                normal[0] * gamma[0]
                - normal[1] * gamma[1]
                - normal[2] * gamma[2]
                - normal[3] * gamma[3]
            )
            h_normal = gamma[0] @ slash_normal
            expected_eigenvalues = np.sort(
                np.array(
                    [
                        np.exp(-rapidity),
                        np.exp(-rapidity),
                        np.exp(rapidity),
                        np.exp(rapidity),
                    ]
                )
            )
            require(
                np.allclose(h_normal, h_normal.conj().T),
                "hypersurface form is not Hermitian",
            )
            require(
                np.allclose(
                    np.sort(np.linalg.eigvalsh(h_normal)),
                    expected_eigenvalues,
                ),
                "hypersurface metric eigenvalues are not exp(plus/minus eta)",
            )
            normal_checks += 1

    alpha_dirac = tuple(gamma[0] @ gamma[index] for index in (1, 2, 3))
    beta_dirac = gamma[0]
    momentum = np.array([0.31, -0.27, 0.43])
    mass = 0.79
    energy = float(np.sqrt(mass**2 + np.dot(momentum, momentum)))
    h_plus_momentum = (
        mass * beta_dirac
        + momentum[0] * alpha_dirac[0]
        + momentum[1] * alpha_dirac[1]
        + momentum[2] * alpha_dirac[2]
    )
    h_minus_momentum = (
        mass * beta_dirac
        - momentum[0] * alpha_dirac[0]
        - momentum[1] * alpha_dirac[1]
        - momentum[2] * alpha_dirac[2]
    )
    pi_plus = (identity4 + h_plus_momentum / energy) / 2
    pi_minus = (identity4 - h_plus_momentum / energy) / 2
    require(
        np.allclose(h_plus_momentum, h_plus_momentum.conj().T)
        and np.allclose(pi_plus @ pi_plus, pi_plus)
        and np.allclose(pi_minus @ pi_minus, pi_minus)
        and np.allclose(pi_plus @ pi_minus, 0)
        and np.allclose(pi_plus + pi_minus, identity4),
        "stationary Dirac spectral projectors are not orthogonal and complete",
    )
    require(
        round(float(np.trace(pi_plus).real)) == 2
        and round(float(np.trace(pi_minus).real)) == 2,
        "stationary spectral polarization does not have rank two plus two",
    )

    charge_conjugation_unitary = 1j * gamma[2]
    require(
        np.allclose(
            charge_conjugation_unitary
            @ h_plus_momentum.conj()
            @ charge_conjugation_unitary.conj().T,
            -h_minus_momentum,
        ),
        "charge conjugation does not send H(p) to -H(-p)",
    )
    pi_minus_at_minus_momentum = (
        identity4 - h_minus_momentum / energy
    ) / 2
    require(
        np.allclose(
            charge_conjugation_unitary
            @ pi_plus.conj()
            @ charge_conjugation_unitary.conj().T,
            pi_minus_at_minus_momentum,
        ),
        "charge conjugation does not exchange spectral subspaces",
    )
    require(
        np.allclose(
            charge_conjugation_unitary
            @ gamma5.conj()
            @ charge_conjugation_unitary.conj().T,
            -gamma5,
        ),
        "charge conjugation does not exchange chirality",
    )

    mode_count = 4
    annihilators = [
        annihilation_mode(mode, mode_count) for mode in range(mode_count)
    ]
    identity_fock = np.eye(1 << mode_count, dtype=complex)
    for left in range(mode_count):
        for right in range(mode_count):
            anticommutator = (
                annihilators[left] @ annihilators[right].conj().T
                + annihilators[right].conj().T @ annihilators[left]
            )
            expected = identity_fock if left == right else 0
            require(
                np.allclose(anticommutator, expected),
                "finite CAR relation failed",
            )
            require(
                np.allclose(
                    annihilators[left] @ annihilators[right]
                    + annihilators[right] @ annihilators[left],
                    0,
                )
                and np.allclose(
                    annihilators[left].conj().T
                    @ annihilators[right].conj().T
                    + annihilators[right].conj().T
                    @ annihilators[left].conj().T,
                    0,
                ),
                "equal-type finite CAR anticommutator failed",
            )
    number_particle = sum(
        (
            annihilators[index].conj().T @ annihilators[index]
            for index in (0, 1)
        ),
        start=np.zeros_like(identity_fock),
    )
    number_antiparticle = sum(
        (
            annihilators[index].conj().T @ annihilators[index]
            for index in (2, 3)
        ),
        start=np.zeros_like(identity_fock),
    )
    charge = number_particle - number_antiparticle
    require(
        set(np.rint(np.linalg.eigvalsh(charge)).astype(int))
        == {-2, -1, 0, 1, 2},
        "finite particle/antiparticle charge spectrum is wrong",
    )

    delta = 0.37
    exponential_gamma5 = (
        np.cos(delta) * identity4 + 1j * np.sin(delta) * gamma5
    )
    four_dimensional_boundary_map = gamma[0] @ exponential_gamma5
    c_delta = np.array(
        [[0, np.exp(1j * delta)], [np.exp(-1j * delta), 0]],
        dtype=complex,
    )
    require(
        np.allclose(c_delta.conj().T, c_delta)
        and np.allclose(c_delta @ c_delta, np.eye(2)),
        "multiplicity-free chirality map has the wrong type",
    )
    require(
        np.allclose(
            four_dimensional_boundary_map,
            np.kron(c_delta, i2),
        ),
        "four-dimensional boundary map does not factor as C_delta tensor I2",
    )

    print("Dirac_chiral_projectors=PASS")
    print("Dirac_chirality_multiplicity=2_PLUS_2")
    print("vector_charge_chirality_commutation=PASS")
    print(f"future_hypersurface_metric_eigenvalue_checks={normal_checks}")
    print("stationary_Dirac_spectral_projectors=PASS")
    print("stationary_Dirac_polarization_rank=2_PLUS_2")
    print("charge_conjugation_spectral_exchange=PASS")
    print("charge_conjugation_chirality_exchange=PASS")
    print("finite_particle_antiparticle_complete_CAR=PASS")
    print("finite_vector_charge_spectrum=MINUS2_THROUGH_PLUS2")
    print("four_to_two_dimensional_chirality_factorization=PASS")
    print("vacuum_polarization_status=DISCLOSED_STANDARD_BRANCH_INPUT")
    print("continuum_CAR_status=DISCLOSED_STANDARD_RESULT")
    print("existence_of_charged_Dirac_matter_derived_by_BID=FALSE")
    print("physical_source_mass_computed=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_FULL_DIRAC_CAR_SOURCE_TYPING_AUDIT=PASS_CONDITIONAL")


if __name__ == "__main__":
    main()
