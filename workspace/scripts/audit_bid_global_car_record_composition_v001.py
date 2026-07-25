#!/usr/bin/env python3
"""Finite exact audit of global CAR versus labeled record composition."""

from __future__ import annotations

import numpy as np


def kron(*factors: np.ndarray) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    lowering = np.array([[0, 1], [0, 0]], dtype=complex)
    parity = np.diag([1.0, -1.0]).astype(complex)

    # One particle and one charge-conjugate antiparticle mode in one global
    # CAR source, represented once by Jordan-Wigner.
    a_particle = kron(lowering, i2)
    a_antiparticle = kron(parity, lowering)
    a0 = a_particle
    a1 = a_antiparticle
    source_identity = np.eye(4, dtype=complex)
    for left_index, left in enumerate((a0, a1)):
        for right_index, right in enumerate((a0, a1)):
            expected = source_identity if left_index == right_index else 0.0
            require(
                np.allclose(
                    left @ right + right @ left,
                    z2.repeat(2, 0).repeat(2, 1),
                )
                and np.allclose(
                    left.conj().T @ right.conj().T
                    + right.conj().T @ left.conj().T,
                    z2.repeat(2, 0).repeat(2, 1),
                ),
                "equal-type CAR anticommutator failed",
            )
            require(
                np.allclose(
                    left @ right.conj().T + right.conj().T @ left,
                    expected,
                ),
                "mixed CAR anticommutator failed",
            )

    number0 = a0.conj().T @ a0
    number1 = a1.conj().T @ a1
    require(
        np.allclose(number0 @ number1, number1 @ number0),
        "particle and antiparticle number operators do not commute",
    )
    charge = number0 - number1

    # Two labeled three-state record cells. The source factor remains one C^4.
    i3 = np.eye(3, dtype=complex)
    record_transition = np.zeros((3, 3), dtype=complex)
    record_transition[1, 0] = 1.0
    record_transition[0, 1] = 1.0
    total_identity = kron(source_identity, i3, i3)
    require(total_identity.shape == (36, 36), "total carrier dimension is wrong")

    b0 = kron(number0, record_transition, i3)
    b1 = kron(number1, i3, record_transition)
    require(np.allclose(b0 @ b1, b1 @ b0), "disjoint couplings do not commute")

    total_charge = kron(charge, i3, i3)
    require(
        np.allclose(b0 @ total_charge, total_charge @ b0)
        and np.allclose(b1 @ total_charge, total_charge @ b1),
        "local coupling violates vector charge conservation",
    )

    # Overlapping source bilinears are a mandatory connected competitor.
    hop = a0.conj().T @ a1 + a1.conj().T @ a0
    overlap0 = kron(number0, record_transition, i3)
    overlap1 = kron(hop, i3, record_transition)
    overlap_commutator = overlap0 @ overlap1 - overlap1 @ overlap0
    require(
        np.linalg.norm(overlap_commutator) > 1e-8,
        "overlap connected competitor was incorrectly removed",
    )

    duplicate_same_modes_dimension = 4 * 4 * 3 * 3
    require(
        duplicate_same_modes_dimension == 144,
        "duplicate-source comparison dimension is wrong",
    )
    require(
        total_identity.shape[0] != duplicate_same_modes_dimension,
        "global source was silently duplicated per record cell",
    )

    print("global_CAR_modes=particle_plus_charge_conjugate_antiparticle")
    print("global_source_dimension=4")
    print("labeled_record_dimension=9")
    print("typed_total_dimension=36")
    print("toy_duplicate_same_global_modes_dimension=144")
    print("CAR_relations=PASS")
    print("disjoint_even_couplings_commute=PASS")
    print("vector_U1_charge_conservation=PASS")
    print("overlap_connected_competitor_nonzero=PASS")
    print("complete_connected_source_record_action_derived=FALSE")
    print("physical_source_pole_and_residue_derived=FALSE")
    print("alpha_computed=FALSE")
    print("continuum_local_net_and_quasilocal_completion=OPEN")
    print("complete_even_coupling_family=OPEN")
    print("BID_FINITE_GLOBAL_CAR_RECORD_COMPOSITION_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
