#!/usr/bin/env python3
"""Fail-closed audit of the conditional BID superconnection inventory."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    # Keep differential order and BID incidence degree as separate fields.
    competitors = {
        "scalar_pseudoscalar_endomorphism": (0, 0),
        "covariant_transport": (1, 1),
        "Pauli_curvature_endomorphism": (0, 2),
        "F_squared_endomorphism": (0, 4),
    }
    require(
        competitors["Pauli_curvature_endomorphism"] == (0, 2),
        "Pauli competitor gradings were conflated",
    )

    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, s], [-s, z2]]) for s in pauli)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]

    delta = 0.37
    phi = np.cos(delta) * np.eye(4) + 1j * np.sin(delta) * gamma5
    phi_chiral_commutator = gamma5 @ phi - phi @ gamma5
    require(
        np.linalg.norm(phi_chiral_commutator) < 1e-12,
        "declared phi unexpectedly odd under spin chirality",
    )
    first_order_cross = gamma[0] @ phi + phi @ gamma[0]
    require(
        np.linalg.norm(first_order_cross) > 1e-8,
        "negative control failed: displayed square accidentally lost its cross term",
    )

    field_strength = np.array(
        [
            [0, 1, -2, 3],
            [-1, 0, 4, -1],
            [2, -4, 0, 2],
            [-3, 1, -2, 0],
        ],
        dtype=float,
    )
    direct = np.zeros((4, 4), dtype=complex)
    commutator_form = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        for nu in range(4):
            direct += gamma[mu] @ gamma[nu] * field_strength[mu, nu]
            commutator_form += (
                0.5
                * (gamma[mu] @ gamma[nu] - gamma[nu] @ gamma[mu])
                * field_strength[mu, nu]
            )
    require(
        np.allclose(direct, commutator_form),
        "Clifford curvature identity failed",
    )

    print("differential_order_and_BID_incidence_degree=SEPARATED")
    print("Pauli_competitor=differential_order_0,incidence_degree_2")
    print("degree_one_primitive_filter=ADOPTED_NOT_DERIVED")
    print("spin_chirality_phi_oddness=FALSE")
    print("displayed_operator_square_has_omitted_first_order_cross_term=TRUE")
    print("Clifford_curvature_identity=PASS")
    print("complete_zero_order_endomorphism_class=OPEN")
    print("internal_superconnection_grading=OPEN")
    print("primitive_Pauli_exclusion_theorem=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_PRIMITIVE_SUPERCONNECTION_CONDITIONAL_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
