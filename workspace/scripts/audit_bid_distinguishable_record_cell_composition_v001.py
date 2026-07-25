#!/usr/bin/env python3
"""Audit the labeled-cell Hilbert composition used by the BID record sector."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    local_dimension = 3
    product_dimension = local_dimension**2

    # The canonical Cartesian-product-to-tensor map in lexicographic bases.
    canonical_map = np.eye(product_dimension)
    require(
        np.allclose(canonical_map.conj().T @ canonical_map, np.eye(9)),
        "Cartesian-product tensor map is not unitary",
    )

    # Swap labeled cells. It is a nontrivial unitary, not an identification.
    swap = np.zeros((9, 9))
    for left in range(3):
        for right in range(3):
            source = 3 * left + right
            target = 3 * right + left
            swap[target, source] = 1.0
    require(np.allclose(swap.T @ swap, np.eye(9)), "cell swap is not unitary")
    require(
        np.linalg.matrix_rank(swap - np.eye(9)) > 0,
        "cell swap was incorrectly reduced to identity",
    )

    symmetric_dimension = local_dimension * (local_dimension + 1) // 2
    antisymmetric_dimension = local_dimension * (local_dimension - 1) // 2
    require(symmetric_dimension == 6, "symmetric quotient dimension is wrong")
    require(
        antisymmetric_dimension == 3,
        "antisymmetric quotient dimension is wrong",
    )
    require(product_dimension == 9, "labeled product dimension is wrong")

    # Exact disjoint Kronecker-sum generator.
    b = np.array(
        [[0.0, 0.0, -1.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 0.0]]
    )
    disjoint = np.kron(b, np.eye(3)) + np.kron(np.eye(3), b)
    require(np.allclose(disjoint, disjoint.T), "disjoint generator is not symmetric")

    print(f"local_record_dimension={local_dimension}")
    print(f"labeled_two_cell_dimension={product_dimension}")
    print(f"bosonic_symmetric_dimension={symmetric_dimension}")
    print(f"fermionic_antisymmetric_dimension={antisymmetric_dimension}")
    print("canonical_l2_product_tensor_map=PASS")
    print("cell_swap_is_unitary_not_identification=PASS")
    print("disjoint_kronecker_sum_generator=PASS")
    print("connected_cross_cell_terms=PENDING_QSPEC")
    print("alpha_computed=FALSE")
    print("BID_DISTINGUISHABLE_RECORD_CELL_COMPOSITION_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
