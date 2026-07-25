#!/usr/bin/env python3
"""Fail-closed audit of the ordinary CP-even axial-phase reduction."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def real_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


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
    charge_conjugation = 1j * gamma[2] @ gamma[0]
    charge_conjugation_inverse = np.linalg.inv(charge_conjugation)

    scalar = identity4
    pseudoscalar = 1j * gamma5
    parity = gamma[0]

    for mu, gamma_mu in enumerate(gamma):
        require(
            np.allclose(
                charge_conjugation
                @ gamma_mu.T
                @ charge_conjugation_inverse,
                -gamma_mu,
            ),
            f"charge-conjugation matrix identity failed for gamma[{mu}]",
        )

    def c_transform(bilinear: np.ndarray) -> np.ndarray:
        return (
            charge_conjugation
            @ bilinear.T
            @ charge_conjugation_inverse
        )

    def cp_transform(bilinear: np.ndarray) -> np.ndarray:
        return parity @ c_transform(bilinear) @ parity

    require(
        np.allclose(c_transform(scalar), scalar),
        "scalar bilinear is not charge-conjugation even",
    )
    require(
        np.allclose(c_transform(pseudoscalar), pseudoscalar),
        "pseudoscalar bilinear is not charge-conjugation even",
    )
    require(
        np.allclose(parity @ scalar @ parity, scalar),
        "scalar bilinear is not parity even",
    )
    require(
        np.allclose(parity @ pseudoscalar @ parity, -pseudoscalar),
        "pseudoscalar bilinear is not parity odd",
    )

    cp_basis = (scalar, pseudoscalar)
    cp_constraint_columns = []
    for element in cp_basis:
        cp_odd_residual = cp_transform(element) - element
        cp_constraint_columns.append(real_vector(cp_odd_residual))
    cp_constraint = np.column_stack(cp_constraint_columns)
    cp_rank = int(np.linalg.matrix_rank(cp_constraint))
    require(
        cp_rank == 1 and cp_constraint.shape[1] - cp_rank == 1,
        "CP constraint does not leave exactly one coefficient direction",
    )
    _, _, cp_vh = np.linalg.svd(cp_constraint)
    cp_kernel = cp_vh[-1]
    cp_kernel /= np.linalg.norm(cp_kernel)
    require(
        np.isclose(abs(cp_kernel[0]), 1.0)
        and np.isclose(abs(cp_kernel[1]), 0.0),
        "computed CP-even kernel is not the scalar axis",
    )

    for delta, expected_invariant in (
        (0.0, True),
        (np.pi, True),
        (0.37, False),
        (-0.91, False),
    ):
        coupling = (
            np.cos(delta) * scalar + np.sin(delta) * pseudoscalar
        )
        transformed = cp_transform(coupling)
        require(
            np.allclose(transformed, coupling) is expected_invariant,
            f"CP classification failed at delta={delta}",
        )

    c_zero = gamma[0]
    c_pi = gamma[0] @ (
        np.cos(np.pi) * identity4 + 1j * np.sin(np.pi) * gamma5
    )
    require(
        np.allclose(c_pi, -c_zero),
        "delta=pi endpoint map is not minus the delta=0 map",
    )
    d_zero = np.vstack((-identity4, c_zero))
    d_pi = np.vstack((-identity4, c_pi))
    endpoint_orientation = np.block(
        [
            [identity4, np.zeros((4, 4), dtype=complex)],
            [np.zeros((4, 4), dtype=complex), -identity4],
        ]
    )
    require(
        np.allclose(endpoint_orientation @ d_zero, d_pi),
        "delta=0 and delta=pi incidence columns are not orientation equivalent",
    )
    require(
        np.allclose(
            endpoint_orientation.conj().T @ endpoint_orientation,
            np.eye(8, dtype=complex),
        ),
        "endpoint orientation equivalence is not unitary",
    )

    # The ordinary determinant branch uses a closed doubled Euclidean cell.
    # Its finite Galerkin cohort has a gamma5-invariant full domain and an
    # explicitly chiral Dirac operator; pairing is derived, not inserted.
    left_dimension = 2
    right_dimension = 2
    chiral_block = np.array(
        [[1.0, 0.2j], [0.3, 1.4]], dtype=complex
    )
    closed_dirac = np.block(
        [
            [
                np.zeros((left_dimension, left_dimension), dtype=complex),
                chiral_block,
            ],
            [
                chiral_block.conj().T,
                np.zeros((right_dimension, right_dimension), dtype=complex),
            ],
        ]
    )
    closed_gamma5 = np.diag(
        [1.0] * left_dimension + [-1.0] * right_dimension
    ).astype(complex)
    closed_domain_projector = np.eye(
        left_dimension + right_dimension, dtype=complex
    )
    require(
        np.allclose(
            closed_gamma5
            @ closed_domain_projector
            @ closed_gamma5,
            closed_domain_projector,
        ),
        "closed regulated Dirac domain is not gamma5 invariant",
    )
    require(
        np.allclose(
            closed_dirac @ closed_gamma5
            + closed_gamma5 @ closed_dirac,
            0.0,
        ),
        "closed regulated massless Dirac operator is not chiral",
    )
    closed_values = np.linalg.eigvalsh(closed_dirac)
    require(
        np.allclose(closed_values, -closed_values[::-1]),
        "closed regulated Dirac spectrum is not paired",
    )
    closed_index = (
        (left_dimension - np.linalg.matrix_rank(chiral_block))
        - (right_dimension - np.linalg.matrix_rank(chiral_block))
    )
    require(closed_index == 0, "closed regulator index is not zero")

    axial_angle = np.pi / 2

    def fujikawa_jacobian(index: int) -> complex:
        return np.exp(2j * axial_angle * index)

    require(
        np.allclose(fujikawa_jacobian(0), 1.0),
        "discrete scalar-sign flip is anomalous in the zero-index branch",
    )

    # The determinant ratio is evaluated on the actual regulated operator.
    mass = 0.73
    paired_positive = np.linalg.det(
        closed_dirac + mass * np.eye(closed_dirac.shape[0])
    )
    paired_negative = np.linalg.det(
        closed_dirac - mass * np.eye(closed_dirac.shape[0])
    )
    require(
        np.allclose(paired_positive, paired_negative),
        "zero-index regulated determinant is not invariant under mass sign",
    )

    # A rectangular chiral block gives one unpaired left zero mode. It keeps
    # the domain gamma5 invariant but carries nonzero index and must fail.
    negative_left_dimension = 3
    negative_right_dimension = 2
    rectangular_block = np.array(
        [[1.0, 0.0], [0.2, 1.1], [0.3j, 0.4]], dtype=complex
    )
    negative_dirac = np.block(
        [
            [
                np.zeros(
                    (negative_left_dimension, negative_left_dimension),
                    dtype=complex,
                ),
                rectangular_block,
            ],
            [
                rectangular_block.conj().T,
                np.zeros(
                    (negative_right_dimension, negative_right_dimension),
                    dtype=complex,
                ),
            ],
        ]
    )
    negative_gamma5 = np.diag(
        [1.0] * negative_left_dimension
        + [-1.0] * negative_right_dimension
    ).astype(complex)
    require(
        np.allclose(
            negative_dirac @ negative_gamma5
            + negative_gamma5 @ negative_dirac,
            0.0,
        ),
        "nonzero-index control is not a chiral Dirac operator",
    )
    block_rank = int(np.linalg.matrix_rank(rectangular_block))
    negative_index = (
        (negative_left_dimension - block_rank)
        - (negative_right_dimension - block_rank)
    )
    require(negative_index == 1, "negative control index is not one")
    require(
        not np.allclose(fujikawa_jacobian(negative_index), 1.0),
        "nonzero-index negative control was silently identified",
    )
    negative_positive = np.linalg.det(
        negative_dirac + mass * np.eye(negative_dirac.shape[0])
    )
    negative_negative = np.linalg.det(
        negative_dirac - mass * np.eye(negative_dirac.shape[0])
    )
    require(
        np.allclose(
            negative_positive,
            -negative_negative,
        ),
        "nonzero-index determinant control did not distinguish mass signs",
    )

    print("complete_scalar_pseudoscalar_coefficient_dimension=2")
    print("charge_conjugation_matrix_identity=PASS")
    print("scalar_and_pseudoscalar_C_even=PASS")
    print("combined_CP_action_constructed=PASS")
    print("computed_CP_constraint_rank=1")
    print("computed_CP_even_kernel_dimension=1")
    print("computed_CP_even_kernel=SCALAR_AXIS")
    print("delta_zero_and_pi_CP_even=PASS")
    print("generic_nonzero_pseudoscalar_phase=REJECTED")
    print("delta_zero_pi_orientation_equivalence=PASS")
    print("axial_field_redefinition_used=FALSE")
    print("source_determinant_regulator=CLOSED_DOUBLED_CELL")
    print("regulated_Dirac_domain_gamma5_invariant=PASS")
    print("massless_regulated_Dirac_chiral_anticommutation=PASS")
    print("zero_index_spectral_pairing=DERIVED")
    print("boundary_eta_phase=ABSENT_CLOSED_REGULATOR")
    print("ordinary_zero_index_sector_disclosed=TRUE")
    print("zero_index_fujikawa_jacobian=ONE")
    print("nonzero_index_negative_control=REJECTED")
    print("zero_index_regulated_determinant_mass_sign_equivalence=PASS")
    print("nonzero_index_regulated_determinant_mass_sign_equivalence=REJECTED")
    print("fermion_measure_anomaly_silently_ignored=FALSE")
    print("ordinary_CP_even_axial_phase_class=UNIQUE")
    print("CP_violating_enlarged_branches_excluded_universally=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_AXIAL_PHASE_CP_REDUCTION_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
