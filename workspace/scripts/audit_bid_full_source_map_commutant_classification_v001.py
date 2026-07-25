#!/usr/bin/env python3
"""Fail-closed audit of the full proper-Lorentz source-map commutant."""

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

    lorentz_generators = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            lorentz_generators.append(
                0.25 * (gamma[mu] @ gamma[nu] - gamma[nu] @ gamma[mu])
            )

    constraints = []
    for generator in lorentz_generators:
        constraints.append(
            np.kron(identity4, generator)
            - np.kron(generator.T, identity4)
        )
    commutant_system = np.vstack(constraints)
    require(
        nullity(commutant_system) == 2,
        "proper-Lorentz Dirac commutant does not have complex dimension two",
    )
    for basis in (identity4, gamma5):
        require(
            all(
                np.linalg.norm(generator @ basis - basis @ generator) < 1e-12
                for generator in lorentz_generators
            ),
            "I/gamma5 failed the proper-Lorentz commutant test",
        )

    p_right = 0.5 * (identity4 + gamma5)
    p_left = 0.5 * (identity4 - gamma5)
    require(np.allclose(p_left @ p_right, 0.0), "chiral projectors overlap")
    require(
        np.allclose(p_left + p_right, identity4),
        "chiral projectors incomplete",
    )

    # Admit the omitted nonunitary competitors, then test the isometry rule.
    nonunitary_parameters = ((0.2, 0.0), (0.0, -0.3), (0.2, -0.3))
    for xi, eta in nonunitary_parameters:
        root = np.exp(xi) * p_right + np.exp(-xi) * p_left
        endpoint_factor = np.exp(eta) * p_right + np.exp(-eta) * p_left
        endpoint = gamma[0] @ endpoint_factor
        require(
            not (
                np.allclose(root.conj().T @ root, identity4)
                and np.allclose(endpoint.conj().T @ endpoint, identity4)
            ),
            "nonunitary chiral-rescaling competitor survived isometry",
        )

    phase_cases = ((0.0, 0.0), (0.31, -0.27), (-1.2, 0.9))
    for theta, delta in phase_cases:
        root = np.exp(1j * theta) * p_right + np.exp(-1j * theta) * p_left
        endpoint_factor = (
            np.exp(1j * delta) * p_right
            + np.exp(-1j * delta) * p_left
        )
        endpoint = gamma[0] @ endpoint_factor
        require(
            np.allclose(root.conj().T @ root, identity4),
            "unitary root phase failed isometry",
        )
        require(
            np.allclose(endpoint.conj().T @ endpoint, identity4),
            "unitary endpoint phase failed isometry",
        )
        quotient = endpoint @ root.conj().T
        expected = gamma[0] @ (
            np.exp(1j * (delta - theta)) * p_right
            + np.exp(-1j * (delta - theta)) * p_left
        )
        require(
            np.allclose(quotient, expected),
            "source-frame quotient did not leave one relative axial phase",
        )

    print("proper_Lorentz_commutant_complex_dimension=2")
    print("proper_Lorentz_commutant_basis=I,gamma5")
    print("nonunitary_root_and_endpoint_competitors_admitted=PASS")
    print("record_isometry_rejects_xi_or_eta_nonzero=PASS")
    print("unitary_source_frame_quotient=PASS")
    print("surviving_relative_axial_phases=1")
    print("normal_dependent_source_map_family_exhausted=FALSE")
    print("source_frame_axial_quotient_physically_authorized=FALSE")
    print("physical_record_Hilbertization_derived=FALSE")
    print("charged_boundary_CPT_intertwiner_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_RESTRICTED_SOURCE_MAP_ATTEMPT_AUDIT=SUPERSEDED")


if __name__ == "__main__":
    main()
