#!/usr/bin/env python3
"""Fail-closed audit of the cellular graded superconnection repair."""

from __future__ import annotations

import numpy as np


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
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, s], [-s, z2]]) for s in sigma)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    identity4 = np.eye(4, dtype=complex)
    identity3 = np.eye(3, dtype=complex)

    d_boundary = np.array([[-1.0], [1.0]], dtype=complex)
    b_partial = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_boundary],
            [d_boundary.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    grading = np.diag([1.0, 1.0, -1.0]).astype(complex)
    require(b_partial.shape == (3, 3), "cellular incidence dilation is not 3x3")
    require(
        np.allclose(b_partial.conj().T, b_partial),
        "cellular incidence dilation is not self-adjoint",
    )
    require(
        np.linalg.norm(grading @ b_partial + b_partial @ grading) < 1e-12,
        "cellular incidence dilation is not record odd",
    )
    c_partial = 1j * grading @ b_partial
    require(
        np.allclose(c_partial.conj().T, c_partial),
        "CPT-selected cellular quadrature is not self-adjoint",
    )
    require(
        np.linalg.norm(grading @ c_partial + c_partial @ grading) < 1e-12,
        "CPT-selected cellular quadrature is not record odd",
    )
    require(
        np.allclose(c_partial @ c_partial, b_partial @ b_partial),
        "CPT-selected cellular quadrature changes the incidence square",
    )

    cliffordized_incidence = np.kron(gamma5, c_partial)
    require(
        cliffordized_incidence.shape == (12, 12),
        "Cliffordized incidence is not 12x12",
    )
    for gamma_mu in gamma:
        kinetic_symbol = np.kron(gamma_mu, identity3)
        require(
            np.linalg.norm(
                kinetic_symbol @ cliffordized_incidence
                + cliffordized_incidence @ kinetic_symbol
            )
            < 1e-12,
            "Cliffordized incidence leaves a first-order derivative cross term",
        )
    require(
        np.allclose(
            cliffordized_incidence @ cliffordized_incidence,
            np.kron(identity4, b_partial @ b_partial),
        ),
        "Cliffordized incidence square has the wrong zero-order term",
    )

    # Verify that gamma5 is the unique direction in the declared Hermitian
    # one-normal spin basis that cancels every kinetic-symbol cross term.
    spin_basis = (
        identity4,
        gamma5,
        gamma[0],
        1j * gamma[0] @ gamma5,
    )
    compatible = tuple(
        index
        for index, element in enumerate(spin_basis)
        if all(
            np.linalg.norm(gamma_mu @ element + element @ gamma_mu) < 1e-12
            for gamma_mu in gamma
        )
    )
    require(
        compatible == (1,),
        "Laplace-compatible one-normal spin direction is not uniquely gamma5",
    )
    tangential_compatible = tuple(
        index
        for index, element in enumerate(spin_basis)
        if all(
            np.linalg.norm(gamma_mu @ element + element @ gamma_mu) < 1e-12
            for gamma_mu in gamma[1:]
        )
    )
    require(
        len(tangential_compatible) == 2,
        "intrinsic tangential symbol did not retain two spin directions",
    )

    # A generic spin-dependent odd zero form is a real competitor but does
    # not belong to the Laplace-compatible branch.
    noncompatible = np.kron(gamma[0], c_partial)
    require(
        any(
            np.linalg.norm(
                np.kron(gamma_mu, identity3) @ noncompatible
                + noncompatible @ np.kron(gamma_mu, identity3)
            )
            > 1e-8
            for gamma_mu in gamma
        ),
        "non-Laplace odd competitor was accidentally accepted",
    )

    print("cellular_record_carrier_complex_dimension=3")
    print("source_cellular_carrier_complex_dimension=12")
    print("cellular_b_partial_shape=3x3")
    print("spin_lifted_B_hat_partial_shape=12x12")
    print("bare_rectangular_incidence_square_dilation=PASS")
    print("cellular_incidence_record_oddness=PASS")
    print("CPT_selected_cellular_quadrature=I_GAMMA_CELL_B_PARTIAL")
    print("CPT_selected_cellular_quadrature_square=BARE_INCIDENCE_SQUARE")
    print("ambient_3plus1_Laplace_compatible_spin_direction=gamma5")
    print("intrinsic_tangential_compatible_spin_dimension=2")
    print("Cliffordized_incidence_shape=12x12")
    print("Cliffordized_first_order_cross_term=ZERO")
    print("non_Laplace_odd_competitor=ADMITTED_OUTSIDE_DECLARED_BRANCH")
    print("differential_and_incidence_orders=SEPARATED")
    print("primitive_BID_filtration_derived_independently=FALSE")
    print("primitive_Pauli_exclusion=CONDITIONAL_ON_ADOPTED_SINGLE_OPERATOR")
    print("local_standard_CPT_incidence_quadrature_applied=TRUE")
    print("complete_CP_axial_reduction_applied=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
