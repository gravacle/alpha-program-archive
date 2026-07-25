#!/usr/bin/env python3
"""Fail-closed audit of restricted charged-handle projector algebra."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def evolve(operator: np.ndarray, tau: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1j * tau * values)) @ vectors.conj().T


def main() -> None:
    charge = np.diag([0.0, 1.0, -1.0])
    p_ch = charge @ charge
    p_plus = (p_ch + charge) / 2.0
    p_minus = (p_ch - charge) / 2.0
    p_zero = np.eye(3) - p_ch

    for name, projector in (
        ("charged", p_ch),
        ("positive", p_plus),
        ("negative", p_minus),
        ("zero", p_zero),
    ):
        require(np.allclose(projector @ projector, projector), f"{name} not projector")
    require(np.allclose(p_plus @ p_minus, 0.0), "orientation sectors overlap")
    require(
        np.allclose(p_plus + p_minus + p_zero, np.eye(3)),
        "restricted projectors are incomplete",
    )

    full_test_charge = np.diag([-2.0, -1.0, 0.0, 1.0, 2.0])
    full_test_square = full_test_charge @ full_test_charge
    require(
        not np.allclose(full_test_square @ full_test_square, full_test_square),
        "Q squared was incorrectly accepted as a full-spectrum projector",
    )

    # Restricted antiunitary CPT quotient: theta(v)=S conjugate(v).
    cpt_swap = np.array(
        [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
        dtype=complex,
    )
    require(
        np.allclose(cpt_swap @ charge.conjugate() @ cpt_swap.T, -charge),
        "restricted CPT swap does not reverse charge",
    )
    require(
        np.allclose(cpt_swap @ p_plus.conjugate() @ cpt_swap.T, p_minus),
        "restricted CPT swap does not exchange orientations",
    )

    incidence = np.array([[-1.0], [1.0]])
    b_q = np.block(
        [
            [np.zeros((2, 2)), incidence],
            [incidence.T, np.zeros((1, 1))],
        ]
    )
    controlled = np.kron(p_ch, b_q)
    charge_total = np.kron(charge, np.eye(3))
    require(
        np.allclose(
            controlled @ charge_total - charge_total @ controlled,
            0.0,
        ),
        "selected controlled operator fails charge conservation",
    )

    unitary = evolve(controlled, math.pi / math.sqrt(2.0))
    basis = np.eye(9, dtype=complex)
    require(
        np.linalg.norm(unitary @ basis[:, 0] - basis[:, 0]) < 2e-14,
        "selected neutral state is not fixed",
    )
    require(
        np.linalg.norm(unitary @ basis[:, 3] - basis[:, 4]) < 2e-14,
        "selected positive sector does not transfer",
    )
    require(
        np.linalg.norm(unitary @ basis[:, 6] - basis[:, 7]) < 2e-14,
        "selected negative sector does not transfer",
    )

    print("primitive_flux_spectrum=DECLARED_-1,0,+1_QUOTIENT")
    print("integer_spectrum_status=INHERITED_GIVEN_COMPACT_U1_REPRESENTATION")
    print("restricted_access_projector=Q_prim_squared")
    print("full_integer_spectrum_Q_squared_projector=FALSE")
    print("restricted_projector_algebra=PASS")
    print("restricted_CPT_swap_algebra=PASS")
    print("physical_current_and_charge_operator_constructed=FALSE")
    print("physical_CPT_operator_constructed=FALSE")
    print("sign_insensitive_activation=ADOPTED_PREMISE")
    print("unique_charge_controlled_coupling_derived=FALSE")
    print("pure_charged_branch_tau_R_authorized=FALSE")
    print("alpha_computed=FALSE")
    print("BID_CHARGED_HANDLE_RESTRICTED_ALGEBRA_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
