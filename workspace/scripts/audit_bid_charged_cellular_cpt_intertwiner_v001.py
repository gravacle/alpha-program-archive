#!/usr/bin/env python3
"""Fail-closed audit of the charged cellular CPT intertwiner."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def antiunitary_conjugate(
    unitary_part: np.ndarray, operator: np.ndarray
) -> np.ndarray:
    return unitary_part @ operator.conj() @ unitary_part.conj().T


def antiunitary_similarity(
    linear_part: np.ndarray, operator: np.ndarray
) -> np.ndarray:
    return linear_part @ operator.conj() @ np.linalg.inv(linear_part)


def incidence_dilation(boundary: np.ndarray) -> np.ndarray:
    vertex_dimension, edge_dimension = boundary.shape
    return np.block(
        [
            [
                np.zeros(
                    (vertex_dimension, vertex_dimension), dtype=complex
                ),
                boundary,
            ],
            [
                boundary.conj().T,
                np.zeros((edge_dimension, edge_dimension), dtype=complex),
            ],
        ]
    )


def slash(vector: np.ndarray, gamma: list[np.ndarray]) -> np.ndarray:
    return (
        vector[0] * gamma[0]
        - vector[1] * gamma[1]
        - vector[2] * gamma[2]
        - vector[3] * gamma[3]
    )


def weighted_incidence_dilation(
    boundary: np.ndarray,
    vertex_metric: np.ndarray,
    edge_metric: np.ndarray,
) -> np.ndarray:
    vertex_dimension, edge_dimension = boundary.shape
    weighted_adjoint = np.linalg.solve(
        edge_metric, boundary.conj().T @ vertex_metric
    )
    return np.block(
        [
            [
                np.zeros(
                    (vertex_dimension, vertex_dimension), dtype=complex
                ),
                boundary,
            ],
            [
                weighted_adjoint,
                np.zeros((edge_dimension, edge_dimension), dtype=complex),
            ],
        ]
    )


def phase_lift(phase: complex, boundary: np.ndarray) -> np.ndarray:
    vertex_dimension, edge_dimension = boundary.shape
    return np.block(
        [
            [
                np.zeros(
                    (vertex_dimension, vertex_dimension), dtype=complex
                ),
                phase * boundary,
            ],
            [
                np.conjugate(phase) * boundary.conj().T,
                np.zeros((edge_dimension, edge_dimension), dtype=complex),
            ],
        ]
    )


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
    dirac_cpt_unitary = gamma5 @ gamma[2]

    require(
        np.allclose(
            dirac_cpt_unitary.conj().T @ dirac_cpt_unitary, identity4
        ),
        "Dirac CPT matrix is not unitary",
    )
    require(
        np.allclose(
            dirac_cpt_unitary @ dirac_cpt_unitary.conj(), -identity4
        ),
        "Dirac CPT antiunitary has the wrong square",
    )
    require(
        all(
            np.allclose(
                antiunitary_conjugate(dirac_cpt_unitary, gamma_mu),
                gamma_mu,
            )
            for gamma_mu in gamma
        ),
        "Dirac CPT does not intertwine all four gamma matrices",
    )
    legacy_incomplete_unitary = 1j * gamma5.conj()
    require(
        not all(
            np.allclose(
                antiunitary_conjugate(legacy_incomplete_unitary, gamma_mu),
                gamma_mu,
            )
            for gamma_mu in gamma
        ),
        "the legacy gamma5-only CPT matrix passed the full Clifford gate",
    )
    require(
        np.allclose(
            antiunitary_conjugate(dirac_cpt_unitary, gamma5), -gamma5
        ),
        "gamma5 does not have the derived CPT-odd sign",
    )

    momentum = np.array([0.31, -0.22, 0.47, 0.83])
    mass = 0.71
    dirac_symbol = (
        momentum[0] * gamma[0]
        - momentum[1] * gamma[1]
        - momentum[2] * gamma[2]
        - momentum[3] * gamma[3]
        - mass * identity4
    )
    require(
        np.allclose(
            antiunitary_conjugate(dirac_cpt_unitary, dirac_symbol),
            (
                momentum[0] * gamma[0]
                - momentum[1] * gamma[1]
                - momentum[2] * gamma[2]
                - momentum[3] * gamma[3]
                - mass * identity4
            ),
        ),
        "CPT-conjugated Dirac kinetic/mass symbol is inconsistent",
    )

    basis_change = np.linalg.qr(
        np.array(
            [
                [1, 1j, 0, 2],
                [0, 1, 1j, 1],
                [2j, 0, 1, -1],
                [1, -2j, 1, 0],
            ],
            dtype=complex,
        )
    )[0]
    transformed_gamma = tuple(
        basis_change @ value @ basis_change.conj().T for value in gamma
    )
    transformed_cpt = (
        basis_change @ dirac_cpt_unitary @ basis_change.T
    )
    require(
        all(
            np.allclose(
                antiunitary_conjugate(transformed_cpt, transformed),
                transformed,
            )
            for transformed in transformed_gamma
        ),
        "CPT intertwining failed after a spin-basis change",
    )

    minkowski = np.diag([1.0, -1.0, -1.0, -1.0])
    spacetime_inversion = -np.eye(4)
    normal_checks = 0
    for axis in (
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([2.0, -1.0, 3.0]) / np.sqrt(14.0),
    ):
        for rapidity in (0.0, 0.3, 1.2):
            normal = np.concatenate(
                (
                    np.array([np.cosh(rapidity)]),
                    np.sinh(rapidity) * axis,
                )
            )
            tetrad_rapidity = 0.19
            source_tetrad = np.eye(4)
            source_tetrad[0, 0] = np.cosh(tetrad_rapidity)
            source_tetrad[0, 1:] = (
                np.sinh(tetrad_rapidity) * axis
            )
            source_tetrad[1:, 0] = (
                np.sinh(tetrad_rapidity) * axis
            )
            source_tetrad[1:, 1:] = (
                np.eye(3)
                + (np.cosh(tetrad_rapidity) - 1.0)
                * np.outer(axis, axis)
            )
            require(
                np.allclose(
                    source_tetrad.T @ minkowski @ source_tetrad, minkowski
                )
                and np.isclose(np.linalg.det(source_tetrad), 1.0),
                "source tetrad is not proper Lorentz",
            )
            source_normal = source_tetrad @ normal
            geometric_pushforward_normal = (
                spacetime_inversion @ source_normal
            )
            target_tetrad = -spacetime_inversion @ source_tetrad
            target_normal = -geometric_pushforward_normal
            target_components = np.linalg.solve(
                target_tetrad, target_normal
            )
            require(
                geometric_pushforward_normal[0] < 0.0
                and target_normal[0] > 0.0,
                "geometric inversion and future reorientation were conflated",
            )
            require(
                np.allclose(target_components, normal),
                "reoriented target-normal components changed",
            )
            require(
                np.allclose(
                    target_tetrad.T @ minkowski @ target_tetrad, minkowski
                )
                and np.isclose(np.linalg.det(target_tetrad), 1.0),
                "reoriented target tetrad is not proper Lorentz",
            )
            slash_normal = slash(normal, gamma)
            h_normal = gamma[0] @ slash_normal
            require(
                np.allclose(
                    dirac_cpt_unitary.conj().T
                    @ h_normal
                    @ dirac_cpt_unitary,
                    h_normal.conj(),
                ),
                "CPT is not an isometry of the future-normal Hilbert form",
            )
            normal_checks += 1

    charge = np.diag([1.0, -1.0, 0.0]).astype(complex)
    charge_swap = np.array(
        [[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex
    )
    p_plus = np.diag([1.0, 0.0, 0.0]).astype(complex)
    p_minus = np.diag([0.0, 1.0, 0.0]).astype(complex)
    p_zero = np.diag([0.0, 0.0, 1.0]).astype(complex)
    require(
        np.allclose(
            antiunitary_conjugate(charge_swap, charge), -charge
        ),
        "charge does not reverse under CPT",
    )
    require(
        np.allclose(
            antiunitary_conjugate(charge_swap, p_plus), p_minus
        )
        and np.allclose(
            antiunitary_conjugate(charge_swap, p_minus), p_plus
        )
        and np.allclose(
            antiunitary_conjugate(charge_swap, p_zero), p_zero
        ),
        "charge spectral projectors have the wrong CPT action",
    )

    transport_checks = 0
    for axis in (
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([2.0, -1.0, 3.0]) / np.sqrt(14.0),
    ):
        spatial_gamma = (
            axis[0] * gamma[1]
            + axis[1] * gamma[2]
            + axis[2] * gamma[3]
        )
        boost_generator = gamma[0] @ spatial_gamma
        for rapidity, phase in ((0.21, 0.17), (0.73, -0.41)):
            target_normal_components = np.concatenate(
                (
                    np.array([np.cosh(rapidity)]),
                    np.sinh(rapidity) * axis,
                )
            )
            spin_transport = (
                np.cosh(rapidity / 2.0) * identity4
                + np.sinh(rapidity / 2.0) * boost_generator
            )
            transport = np.exp(phase * 1j) * spin_transport
            h_root = identity4
            h_public = gamma[0] @ slash(target_normal_components, gamma)
            require(
                np.allclose(
                    transport.conj().T @ h_public @ transport, h_root
                ),
                "different-normal transport is not an h_n isometry",
            )
            source_boundary = np.vstack((-identity4, transport))
            reverse_transport = (
                dirac_cpt_unitary
                @ np.linalg.inv(transport).conj()
                @ dirac_cpt_unitary.conj().T
            )
            target_boundary = np.vstack((-identity4, reverse_transport))
            theta_zero = np.block(
                [
                    [
                        np.zeros((4, 4), dtype=complex),
                        dirac_cpt_unitary,
                    ],
                    [
                        dirac_cpt_unitary,
                        np.zeros((4, 4), dtype=complex),
                    ],
                ]
            )
            theta_one = -dirac_cpt_unitary @ transport.conj()
            require(
                np.allclose(
                    theta_zero @ source_boundary.conj(),
                    target_boundary @ theta_one,
                ),
                "transported charged edge fails the CPT chain equation",
            )
            source_vertex_metric = np.block(
                [
                    [h_root, np.zeros((4, 4), dtype=complex)],
                    [np.zeros((4, 4), dtype=complex), h_public],
                ]
            )
            target_vertex_metric = np.block(
                [
                    [h_public, np.zeros((4, 4), dtype=complex)],
                    [np.zeros((4, 4), dtype=complex), h_root],
                ]
            )
            source_dilation = weighted_incidence_dilation(
                source_boundary, source_vertex_metric, h_root
            )
            target_dilation = weighted_incidence_dilation(
                target_boundary, target_vertex_metric, h_public
            )
            theta_transport_cell = np.block(
                [
                    [
                        theta_zero,
                        np.zeros((8, 4), dtype=complex),
                    ],
                    [
                        np.zeros((4, 8), dtype=complex),
                        theta_one,
                    ],
                ]
            )
            require(
                np.allclose(
                    antiunitary_similarity(
                        theta_transport_cell, source_dilation
                    ),
                    target_dilation,
                ),
                "weighted-adjoint incidence dilation is not CPT covariant",
            )
            transport_checks += 1

    d_cell = np.array([[-1.0], [1.0]], dtype=complex)
    b_cell = incidence_dilation(d_cell)
    grading_cell = np.diag([1.0, 1.0, -1.0]).astype(complex)
    causal_role_reversal = np.array(
        [[0, 1, 0], [1, 0, 0], [0, 0, -1]], dtype=complex
    )
    require(
        np.allclose(
            antiunitary_conjugate(causal_role_reversal, b_cell), b_cell
        ),
        "real cellular incidence does not have CPT-even parity",
    )
    c_cell = 1j * grading_cell @ b_cell
    require(
        np.allclose(c_cell.conj().T, c_cell)
        and np.allclose(c_cell @ c_cell, b_cell @ b_cell),
        "CPT-compatible cellular quadrature has wrong adjoint or square",
    )
    require(
        np.allclose(
            antiunitary_conjugate(causal_role_reversal, c_cell), -c_cell
        ),
        "cellular conjugate quadrature is not CPT odd",
    )
    phase_basis_lifts = (
        phase_lift(1.0 + 0.0j, d_cell),
        phase_lift(0.0 + 1.0j, d_cell),
    )
    phase_constraint_columns = []
    for lift in phase_basis_lifts:
        odd_residual = (
            antiunitary_conjugate(causal_role_reversal, lift) + lift
        )
        phase_constraint_columns.append(
            np.concatenate(
                (odd_residual.real.ravel(), odd_residual.imag.ravel())
            )
        )
    phase_constraint = np.column_stack(phase_constraint_columns)
    phase_rank = int(np.linalg.matrix_rank(phase_constraint))
    require(
        phase_rank == 1 and phase_constraint.shape[1] - phase_rank == 1,
        "CPT phase constraint does not leave one imaginary direction",
    )
    _, _, phase_vh = np.linalg.svd(phase_constraint)
    phase_null_vector = phase_vh[-1]
    phase_null_vector /= np.linalg.norm(phase_null_vector)
    require(
        np.isclose(abs(phase_null_vector[0]), 0.0)
        and np.isclose(abs(phase_null_vector[1]), 1.0),
        "computed CPT phase kernel is not the imaginary quadrature",
    )
    for phase, expected_parity in (
        (1.0 + 0.0j, 1.0),
        (0.0 + 1.0j, -1.0),
        (0.0 - 1.0j, -1.0),
    ):
        lifted_phase = phase_lift(phase, d_cell)
        require(
            np.allclose(
                antiunitary_conjugate(causal_role_reversal, lifted_phase),
                expected_parity * lifted_phase,
            ),
            "fixed-incidence phase has the wrong cellular CPT parity",
        )
    full_cpt_unitary = np.kron(
        np.kron(dirac_cpt_unitary, charge_swap),
        causal_role_reversal,
    )
    real_incidence_primitive = np.kron(
        np.kron(gamma5, np.eye(3, dtype=complex)), b_cell
    )
    cpt_incidence_primitive = np.kron(
        np.kron(gamma5, np.eye(3, dtype=complex)), c_cell
    )
    require(
        np.allclose(
            antiunitary_conjugate(
                full_cpt_unitary, real_incidence_primitive
            ),
            -real_incidence_primitive,
        ),
        "real gamma5-incidence primitive was incorrectly accepted as CPT even",
    )
    require(
        np.allclose(
            antiunitary_conjugate(
                full_cpt_unitary, cpt_incidence_primitive
            ),
            cpt_incidence_primitive,
        ),
        "CPT-selected gamma5-cellular quadrature is not invariant",
    )

    b_zero = 0.37 * np.eye(3, dtype=complex)
    require(
        np.allclose(
            antiunitary_conjugate(causal_role_reversal, b_zero), b_zero
        ),
        "nonzero neutral control block is not CPT even",
    )
    b_plus = np.array(
        [[0, 1j, 0], [-1j, 0, 2], [0, 2, 0]], dtype=complex
    )
    b_minus = antiunitary_conjugate(causal_role_reversal, b_plus)
    controlled = (
        np.kron(p_zero, b_zero)
        + np.kron(p_plus, b_plus)
        + np.kron(p_minus, b_minus)
    )
    controlled_cpt = np.kron(charge_swap, causal_role_reversal)
    require(
        np.allclose(
            antiunitary_conjugate(controlled_cpt, controlled), controlled
        ),
        "full projector-controlled coupling is not CPT covariant",
    )
    wrong_b_minus = b_minus + np.diag([0.0, 0.0, 0.25])
    wrong_controlled = (
        np.kron(p_zero, b_zero)
        + np.kron(p_plus, b_plus)
        + np.kron(p_minus, wrong_b_minus)
    )
    require(
        not np.allclose(
            antiunitary_conjugate(controlled_cpt, wrong_controlled),
            wrong_controlled,
        ),
        "incorrect negative-charge coupling passed the CPT negative control",
    )
    wrong_b_zero = b_zero + np.diag([0.13, 0.0, 0.0])
    wrong_neutral_controlled = (
        np.kron(p_zero, wrong_b_zero)
        + np.kron(p_plus, b_plus)
        + np.kron(p_minus, b_minus)
    )
    require(
        not np.allclose(
            antiunitary_conjugate(
                controlled_cpt, wrong_neutral_controlled
            ),
            wrong_neutral_controlled,
        ),
        "incorrect neutral coupling passed the CPT negative control",
    )

    print("explicit_Dirac_CPT_antiunitary=PASS")
    print("all_four_gamma_CPT_intertwiners=PASS")
    print("legacy_gamma5_only_CPT_matrix=REJECTED")
    print("Dirac_CPT_square=MINUS_IDENTITY")
    print("Dirac_kinetic_mass_CPT_covariance=PASS")
    print("spin_basis_change_covariance=PASS")
    print(f"future_normal_pushforward_reorientation_checks={normal_checks}")
    print(f"future_normal_Hilbert_isometry_checks={normal_checks}")
    print("charge_line_conjugation=PASS")
    print("charge_projector_CPT_action=PASS")
    print(
        f"different_normal_transport_CPT_chain_checks={transport_checks}"
    )
    print("different_normal_transport_CPT_chain_equation=PASS")
    print("weighted_adjoint_incidence_dilation_CPT_covariance=PASS")
    print("real_incidence_quadrature_CPT_parity=EVEN")
    print("gamma5_real_incidence_product_CPT_parity=ODD")
    print("Hermitian_conjugate_cellular_quadrature_CPT_parity=ODD")
    print(
        "CPT_even_Cliffordized_incidence_phase="
        "PURE_IMAGINARY_UNIQUE_UP_TO_SIGN"
    )
    print("computed_phase_constraint_rank=1")
    print("computed_phase_kernel_dimension=1")
    print("gamma5_conjugate_quadrature_product_CPT_parity=EVEN")
    print("controlled_coupling_CPT_classification=PASS")
    print("controlled_coupling_negative_control=REJECTED")
    print("nonzero_neutral_CPT_even_block=PASS")
    print("neutral_block_negative_control=REJECTED")
    print("orientation_blind_B_plus_equals_B_minus=FALSE")
    print("CPT_selects_axial_phase_delta_zero=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_CHARGED_CELLULAR_CPT_INTERTWINER_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
