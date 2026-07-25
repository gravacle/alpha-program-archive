#!/usr/bin/env python3
"""Fail-closed matrix audit of boundary hypersurface-metric transport."""

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
    identity4 = np.eye(4, dtype=complex)

    transforms = []
    for axis, rapidity in ((1, 0.7), (2, -0.4), (3, 1.1)):
        generator = gamma[0] @ gamma[axis]
        transforms.append(
            np.cosh(rapidity / 2.0) * identity4
            + np.sinh(rapidity / 2.0) * generator
        )
    for left, right, angle in ((1, 2, 0.8), (2, 3, -0.6), (3, 1, 0.3)):
        generator = gamma[left] @ gamma[right]
        transforms.append(
            np.cos(angle / 2.0) * identity4
            + np.sin(angle / 2.0) * generator
        )

    normal_root_slash = gamma[0]
    h_root = gamma[0] @ normal_root_slash
    phase_cases = (0.0, 0.41, -1.3)
    checked = 0
    for spin_transport in transforms:
        inverse = np.linalg.inv(spin_transport)
        require(
            np.allclose(
                spin_transport.conj().T @ gamma[0],
                gamma[0] @ inverse,
            ),
            "spin transport is not Dirac-pseudounitary",
        )
        normal_endpoint_slash = (
            spin_transport @ normal_root_slash @ inverse
        )
        require(
            np.allclose(
                normal_endpoint_slash @ normal_endpoint_slash,
                identity4,
            ),
            "transported normal is not unit timelike",
        )
        h_endpoint = gamma[0] @ normal_endpoint_slash
        require(
            np.all(np.linalg.eigvalsh(h_endpoint) > 0),
            "transported hypersurface metric is not positive",
        )
        for phase in phase_cases:
            full_transport = np.exp(1j * phase) * spin_transport
            require(
                np.allclose(
                    full_transport.conj().T
                    @ h_endpoint
                    @ full_transport,
                    h_root,
                ),
                "spin/U1 transport does not preserve h_n",
            )
            checked += 1

    print(f"proper_Lorentz_spin_transports={len(transforms)}")
    print(f"spin_U1_metric_compatibility_cases={checked}")
    print("endpoint_normal_transport=PASS")
    print("Dirac_pseudounitarity=PASS")
    print("positive_hypersurface_metric=PASS")
    print("boundary_metric_edge_transport_isometry=PASS")
    print("proper_orthochronous_scope_only=TRUE")
    print("charged_boundary_CPT_intertwiner_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_BOUNDARY_METRIC_TRANSPORT_AUDIT=PASS")


if __name__ == "__main__":
    main()
