#!/usr/bin/env python3
"""Fail-closed audit of the corrected cellular zero-form inventory."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def real_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.reshape(-1), matrix.imag.reshape(-1)))


def matrix_unit(size: int, row: int, column: int) -> np.ndarray:
    output = np.zeros((size, size), dtype=complex)
    output[row, column] = 1.0
    return output


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
    rotations = tuple(
        0.25 * (gamma[left] @ gamma[right] - gamma[right] @ gamma[left])
        for left, right in ((1, 2), (2, 3), (3, 1))
    )

    spin_basis = (
        identity4,
        gamma5,
        gamma[0],
        1j * gamma[0] @ gamma5,
    )
    require(
        all(np.allclose(element.conj().T, element) for element in spin_basis),
        "reference spin basis is not Hermitian",
    )
    require(
        all(
            all(
                np.linalg.norm(generator @ element - element @ generator)
                < 1e-12
                for generator in rotations
            )
            for element in spin_basis
        ),
        "reference spin basis leaves the little-group commutant",
    )
    require(
        np.linalg.matrix_rank(
            np.stack(tuple(real_vector(element) for element in spin_basis))
        )
        == 4,
        "spin Hermitian commutant basis is not real-linearly independent",
    )

    diagonal = tuple(matrix_unit(3, index, index) for index in range(3))
    symmetric = tuple(
        matrix_unit(3, left, right) + matrix_unit(3, right, left)
        for left, right in ((0, 1), (0, 2), (1, 2))
    )
    antisymmetric = tuple(
        1j * (matrix_unit(3, left, right) - matrix_unit(3, right, left))
        for left, right in ((0, 1), (0, 2), (1, 2))
    )
    record_basis = diagonal + symmetric + antisymmetric
    require(
        len(record_basis) == 9
        and all(
            np.allclose(element.conj().T, element) for element in record_basis
        )
        and np.linalg.matrix_rank(
            np.stack(tuple(real_vector(element) for element in record_basis))
        )
        == 9,
        "record Hermitian basis is not complete",
    )

    grading_record = np.diag([1.0, 1.0, -1.0]).astype(complex)
    record_even = (
        diagonal[0],
        diagonal[1],
        diagonal[2],
        symmetric[0],
        antisymmetric[0],
    )
    record_odd = (
        symmetric[1],
        antisymmetric[1],
        symmetric[2],
        antisymmetric[2],
    )
    require(
        all(
            np.linalg.norm(grading_record @ element - element @ grading_record)
            < 1e-12
            for element in record_even
        ),
        "record-even basis fails to commute with cellular grading",
    )
    require(
        all(
            np.linalg.norm(grading_record @ element + element @ grading_record)
            < 1e-12
            for element in record_odd
        ),
        "record-odd basis fails to anticommute with cellular grading",
    )

    full_basis = tuple(
        np.kron(spin_element, record_element)
        for spin_element in spin_basis
        for record_element in record_basis
    )
    even_basis = tuple(
        np.kron(spin_element, record_element)
        for spin_element in spin_basis
        for record_element in record_even
    )
    odd_basis = tuple(
        np.kron(spin_element, record_element)
        for spin_element in spin_basis
        for record_element in record_odd
    )
    require(
        np.linalg.matrix_rank(
            np.stack(tuple(real_vector(element) for element in full_basis))
        )
        == 36,
        "full one-normal zero-form basis does not have dimension 36",
    )
    require(
        np.linalg.matrix_rank(
            np.stack(tuple(real_vector(element) for element in even_basis))
        )
        == 20
        and np.linalg.matrix_rank(
            np.stack(tuple(real_vector(element) for element in odd_basis))
        )
        == 16,
        "cellular grading split is not 20+16",
    )

    ambient_constraint = np.stack(
        tuple(
            np.concatenate(
                tuple(
                    real_vector(
                        np.kron(gamma_mu, identity3) @ element
                        + element @ np.kron(gamma_mu, identity3)
                    )
                    for gamma_mu in gamma
                )
            )
            for element in odd_basis
        ),
        axis=1,
    )
    _, ambient_singular_values, ambient_vh = np.linalg.svd(
        ambient_constraint, full_matrices=True
    )
    ambient_rank = int(
        np.count_nonzero(
            ambient_singular_values
            > ambient_singular_values[0] * 1e-12
        )
    )
    ambient_kernel = ambient_vh[ambient_rank:].conj().T
    require(
        ambient_rank == 12 and ambient_kernel.shape == (16, 4),
        "full ambient Clifford constraint does not have rank 12 and nullity 4",
    )

    gamma5_candidate_coefficients = np.zeros((16, 4), dtype=complex)
    gamma5_candidate_coefficients[4:8, :] = np.eye(4, dtype=complex)
    ambient_kernel_projector = ambient_kernel @ ambient_kernel.conj().T
    gamma5_candidate_projector = (
        gamma5_candidate_coefficients
        @ gamma5_candidate_coefficients.conj().T
    )
    require(
        np.linalg.norm(
            ambient_kernel_projector - gamma5_candidate_projector
        )
        < 1e-10,
        "ambient compatible kernel is not exactly gamma5 tensor record-odd",
    )

    tangential_constraint = np.stack(
        tuple(
            np.concatenate(
                tuple(
                    real_vector(
                        np.kron(gamma_mu, identity3) @ element
                        + element @ np.kron(gamma_mu, identity3)
                    )
                    for gamma_mu in gamma[1:]
                )
            )
            for element in odd_basis
        ),
        axis=1,
    )
    tangential_singular_values = np.linalg.svd(
        tangential_constraint, compute_uv=False
    )
    tangential_rank = int(
        np.count_nonzero(
            tangential_singular_values
            > tangential_singular_values[0] * 1e-12
        )
    )
    require(
        16 - tangential_rank == 8,
        "intrinsic tangential competitor did not retain the expected nullity 8",
    )

    laplace_compatible_odd = tuple(
        np.kron(gamma5, record_element) for record_element in record_odd
    )
    require(
        np.linalg.matrix_rank(
            np.stack(
                tuple(real_vector(element) for element in laplace_compatible_odd)
            )
        )
        == 4,
        "Laplace-compatible record-odd subspace does not have dimension four",
    )

    d_boundary = np.array([[-1.0], [1.0]], dtype=complex)
    incidence_record = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_boundary],
            [d_boundary.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    require(
        np.allclose(incidence_record.conj().T, incidence_record)
        and np.linalg.norm(
            grading_record @ incidence_record
            + incidence_record @ grading_record
        )
        < 1e-12,
        "cellular incidence dilation is not Hermitian and record odd",
    )
    cpt_selected_incidence = 1j * grading_record @ incidence_record
    require(
        np.allclose(
            cpt_selected_incidence.conj().T, cpt_selected_incidence
        )
        and np.linalg.norm(
            grading_record @ cpt_selected_incidence
            + cpt_selected_incidence @ grading_record
        )
        < 1e-12,
        "CPT-selected incidence quadrature is not Hermitian and record odd",
    )
    require(
        np.allclose(
            cpt_selected_incidence @ cpt_selected_incidence,
            incidence_record @ incidence_record,
        ),
        "CPT-selected quadrature changes the bare incidence square",
    )
    odd_matrix = np.stack(
        tuple(real_vector(element) for element in record_odd), axis=1
    )
    coefficients, _, _, _ = np.linalg.lstsq(
        odd_matrix, real_vector(incidence_record), rcond=None
    )
    require(
        np.linalg.norm(
            odd_matrix @ coefficients - real_vector(incidence_record)
        )
        < 1e-12,
        "bare incidence dilation is absent from the record-odd basis",
    )
    incidence_cliffordized = np.kron(gamma5, cpt_selected_incidence)
    require(
        incidence_cliffordized.shape == (12, 12),
        "Cliffordized incidence has the wrong carrier dimension",
    )
    require(
        all(
            np.linalg.norm(
                np.kron(gamma_mu, identity3) @ incidence_cliffordized
                + incidence_cliffordized @ np.kron(gamma_mu, identity3)
            )
            < 1e-12
            for gamma_mu in gamma
        ),
        "Cliffordized incidence leaves a first-order square cross term",
    )

    transported_checks = 0
    for axis, rapidity in ((1, 0.7), (2, -0.4), (3, 1.1)):
        transport = (
            np.cosh(rapidity / 2.0) * identity4
            + np.sinh(rapidity / 2.0) * gamma[0] @ gamma[axis]
        )
        inverse = np.linalg.inv(transport)
        normal_slash = transport @ gamma[0] @ inverse
        h_normal = gamma[0] @ normal_slash
        for element in spin_basis:
            transported = transport @ element @ inverse
            sharp = np.linalg.inv(h_normal) @ transported.conj().T @ h_normal
            require(
                np.allclose(sharp, transported),
                "transported spin zero form is not H_n-self-adjoint",
            )
            transported_checks += 1

    print("cellular_record_carrier_complex_dimension=3")
    print("source_cellular_carrier_complex_dimension=12")
    print("one_normal_spin_Hn_self_adjoint_basis_dimension=4")
    print("record_Hermitian_basis_dimension=9")
    print("full_zero_form_real_dimension=36")
    print("record_even_zero_form_real_dimension=20")
    print("record_odd_zero_form_real_dimension=16")
    print("ambient_3plus1_Clifford_constraint_rank=12")
    print("Laplace_compatible_record_odd_real_dimension=4")
    print("ambient_kernel_equals_gamma5_tensor_record_odd=PASS")
    print("intrinsic_tangential_competitor_nullity=8")
    print(f"boosted_Hn_self_adjoint_basis_checks={transported_checks}")
    print("two_normal_common_frame_reduction=SUPPLIED_BY_METRIC_TRANSPORT")
    print("bare_incidence_dilation_in_odd_basis=PASS")
    print("CPT_selected_incidence_quadrature_in_odd_basis=PASS")
    print("CPT_selected_incidence_square_equals_bare_square=PASS")
    print("Cliffordized_incidence_shape=12x12")
    print("Cliffordized_first_order_cross_term=ZERO")
    print("primitive_incidence_selection=CONDITIONAL_ON_TWO_ADOPTED_PRINCIPLES")
    print("local_standard_CPT_incidence_quadrature_applied=TRUE")
    print("complete_CP_axial_reduction_applied=FALSE")
    print("enlarged_geometric_zero_form_branches_exhausted=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
