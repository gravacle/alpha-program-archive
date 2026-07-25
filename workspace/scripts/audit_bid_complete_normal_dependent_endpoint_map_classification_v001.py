#!/usr/bin/env python3
"""Fail-closed audit of the full normal-dependent endpoint-map family."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def nullity(matrix: np.ndarray, tolerance: float = 1e-10) -> int:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    return matrix.shape[1] - int(np.sum(singular_values > tolerance))


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

    rotation_generators = []
    for left, right in ((1, 2), (2, 3), (3, 1)):
        rotation_generators.append(
            0.25 * (gamma[left] @ gamma[right] - gamma[right] @ gamma[left])
        )
    constraints = np.vstack(
        [
            np.kron(identity4, generator)
            - np.kron(generator.T, identity4)
            for generator in rotation_generators
        ]
    )
    require(
        nullity(constraints) == 4,
        "Spin(3) little-group commutant does not have complex dimension four",
    )
    basis = (identity4, gamma5, gamma[0], gamma[0] @ gamma5)
    for element in basis:
        require(
            all(
                np.linalg.norm(generator @ element - element @ generator) < 1e-12
                for generator in rotation_generators
            ),
            "declared little-group basis element fails to commute",
        )

    # Conditional source-independent all-spinor normalization requires
    # E^sharp E to be scalar. At the reference normal, sharp is the ordinary
    # adjoint. Every surviving endpoint can then be normalized to U(2) on the
    # equivalent spin-1/2 multiplicity sectors.
    unitary2_cases = (
        np.eye(2, dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array(
            [
                [np.cos(0.4), 1j * np.sin(0.4)],
                [1j * np.sin(0.4), np.cos(0.4)],
            ],
            dtype=complex,
        ),
    )
    scaled_unitary_cases = []
    for scale in (0.2, 1.0, 3.7):
        for unitary2 in unitary2_cases:
            scaled_unitary_cases.append((scale, np.kron(unitary2, i2)))

    for scale, unitary_endpoint in scaled_unitary_cases:
        endpoint = scale * unitary_endpoint
        endpoint_gram = endpoint.conj().T @ endpoint
        require(
            np.allclose(endpoint_gram, scale * scale * identity4),
            "scaled U2 endpoint fails source-independent normalization",
        )
        normalized_endpoint = endpoint / np.sqrt(
            np.trace(endpoint_gram).real / identity4.shape[0]
        )
        require(
            all(
                np.linalg.norm(
                    generator @ normalized_endpoint
                    - normalized_endpoint @ generator
                )
                < 1e-12
                for generator in rotation_generators
            ),
            "normalized U2 endpoint leaves the little-group commutant",
        )
        require(
            np.allclose(
                normalized_endpoint.conj().T @ normalized_endpoint, identity4
            ),
            "positive endpoint scale did not absorb into incidence weight",
        )
        for a_abs, b_abs in ((1.0, 1.0), (0.8, 1.2), (1.3, 0.4)):
            incidence = np.vstack(
                (-a_abs * identity4, b_abs * normalized_endpoint)
            )
            expected = (a_abs * a_abs + b_abs * b_abs) * identity4
            require(
                np.allclose(incidence.conj().T @ incidence, expected),
                "incidence Gram depends on endpoint U2 element",
            )

    zero_endpoint = np.kron(np.zeros((2, 2), dtype=complex), i2)
    nonzero_rank_deficient = np.kron(
        np.diag([1.0, 0.0]).astype(complex), i2
    )
    anisotropic_full_rank = np.kron(
        np.diag([2.0, 0.5]).astype(complex), i2
    )
    require(
        tuple(
            np.linalg.matrix_rank(endpoint)
            for endpoint in (
                zero_endpoint,
                nonzero_rank_deficient,
                anisotropic_full_rank,
            )
        )
        == (0, 2, 4),
        "endpoint rank strata are not 0,2,4",
    )
    for competitor in (
        zero_endpoint,
        nonzero_rank_deficient,
        anisotropic_full_rank,
    ):
        require(
            all(
                np.linalg.norm(generator @ competitor - competitor @ generator)
                < 1e-12
                for generator in rotation_generators
            ),
            "endpoint rank/anisotropy competitor left the classified commutant",
        )
    require(
        np.allclose(zero_endpoint.conj().T @ zero_endpoint, np.zeros((4, 4)))
        and np.linalg.matrix_rank(zero_endpoint) == 0,
        "zero endpoint stratum was not retained before completion",
    )
    for competitor in (nonzero_rank_deficient, anisotropic_full_rank):
        gram = competitor.conj().T @ competitor
        scalar_gram = (
            np.trace(gram).real / identity4.shape[0]
        ) * identity4
        require(
            not np.allclose(gram, scalar_gram),
            "rank-deficient/anisotropic competitor survived all-spinor normalization",
        )

    # Away from the reference normal, use the positive hypersurface adjoint,
    # not the ordinary Euclidean adjoint.
    boosted_checks = 0
    for axis, rapidity in ((1, 0.7), (2, -0.4), (3, 1.1)):
        spin_transport = (
            np.cosh(rapidity / 2.0) * identity4
            + np.sinh(rapidity / 2.0) * gamma[0] @ gamma[axis]
        )
        inverse_transport = np.linalg.inv(spin_transport)
        normal_slash = spin_transport @ gamma[0] @ inverse_transport
        h_normal = gamma[0] @ normal_slash
        require(
            np.all(np.linalg.eigvalsh(h_normal) > 0),
            "boosted hypersurface metric is not positive",
        )
        for unitary2 in unitary2_cases:
            endpoint_reference = np.kron(unitary2, i2)
            endpoint_normal = (
                spin_transport @ endpoint_reference @ inverse_transport
            )
            endpoint_sharp = (
                np.linalg.inv(h_normal)
                @ endpoint_normal.conj().T
                @ h_normal
            )
            require(
                np.allclose(endpoint_sharp @ endpoint_normal, identity4),
                "transported endpoint is not unitary in the h_n adjoint",
            )
            boosted_checks += 1

    a_squared = np.linspace(0.0005, 1.9995, 3999)
    b_squared = 2.0 - a_squared
    transfer = 4.0 * a_squared * b_squared / (a_squared + b_squared) ** 2
    maximum_index = int(np.argmax(transfer))
    require(
        abs(a_squared[maximum_index] - 1.0) < 1e-14
        and abs(transfer[maximum_index] - 1.0) < 1e-14,
        "conditional pure off-diagonal transfer maximum is not equal weight",
    )

    print("normal_little_group_commutant_complex_dimension=4")
    print("normal_dependent_basis=I,gamma5,slashn,slashn_gamma5")
    print("chiral_even_and_chiral_odd_competitors=ADMITTED")
    print("endpoint_zero_form_role=PARENT_NOT_INCIDENCE")
    print("endpoint_rank_strata=0,2,4")
    print("all_endpoint_rank_strata_before_normalization=ADMITTED")
    print("all_spinor_scaled_normalization_derived_from_QR1_QR7=FALSE")
    print("conditional_all_spinor_normalization_forces_E_sharp_E_scalar=PASS")
    print("conditional_rank_deficient_nonzero_endpoint=REJECTED")
    print("conditional_anisotropic_endpoint_rescaling=REJECTED")
    print("conditional_scaled_unitary_absorption=PASS")
    print(f"scaled_endpoint_U2_cases={len(scaled_unitary_cases)}")
    print(f"h_n_adjoint_boosted_endpoint_cases={boosted_checks}")
    print("bare_covariant_incidence_column=-I,+U_e")
    print("conditional_pure_offdiagonal_equal_transfer=PASS")
    print("parent_zero_form_detuning_excluded=FALSE")
    print("root_axial_source_frame_quotient_used=FALSE")
    print("endpoint_U2_element_selected=FALSE")
    print("complete_parent_zero_form_family_enumerated=FALSE")
    print("alpha_computed=FALSE")
    print("BID_COMPLETE_NORMAL_ENDPOINT_MAP_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
