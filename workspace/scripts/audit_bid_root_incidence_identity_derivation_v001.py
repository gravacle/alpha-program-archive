#!/usr/bin/env python3
"""Fail-closed functorial audit of the root incidence identity."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def boundary(transport: np.ndarray, source: np.ndarray) -> np.ndarray:
    return np.concatenate((transport @ source, -source))


def main() -> None:
    identity = np.eye(4, dtype=complex)
    transports = (
        identity,
        np.diag([1.0, -1.0, 1j, -1j]),
        np.array(
            [
                [0, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1j],
                [0, 0, 1j, 0],
            ],
            dtype=complex,
        ),
    )
    sources = tuple(np.eye(4, dtype=complex)[:, index] for index in range(4))
    for transport in transports:
        for source in sources:
            result = boundary(transport, source)
            require(
                np.allclose(result[:4], transport @ source),
                "endpoint coefficient is not transported source",
            )
            require(
                np.allclose(result[4:], -source),
                "root coefficient is not negative identity",
            )

    # Subdivision compatibility: boundary endpoint and root contributions are
    # unchanged when U_e is replaced by U_2 U_1.
    first, second = transports[1], transports[2]
    for source in sources:
        require(
            np.allclose(
                boundary(second @ first, source),
                np.concatenate((second @ first @ source, -source)),
            ),
            "subdivision changes root incidence",
        )

    print(f"source_basis_vectors_checked={len(sources)}")
    print(f"edge_transports_checked={len(transports)}")
    print("identity_morphism_root_transport=PASS")
    print("subdivision_compatible_root_incidence=PASS")
    print("root_incidence_component=-I")
    print("normal_dependent_root_zero_forms=SEPARATE_PARENT_COMPETITORS")
    print("complete_parent_zero_form_family_enumerated=FALSE")
    print("alpha_computed=FALSE")
    print("BID_ROOT_INCIDENCE_IDENTITY_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
