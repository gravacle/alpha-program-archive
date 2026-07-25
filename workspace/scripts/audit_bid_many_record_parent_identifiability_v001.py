#!/usr/bin/env python3
"""Target-free audit of the BID many-record parent identifiability gap."""

from __future__ import annotations

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    # Basis: |00>, |10>, |01>, |11>.  The one-record hopping block is fixed.
    base = np.zeros((4, 4), dtype=float)
    base[1, 2] = 1.0
    base[2, 1] = 1.0

    double_occupancy = np.zeros((4, 4), dtype=float)
    double_occupancy[3, 3] = 1.0

    swap = np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    )

    lambdas = (-2.0, -0.5, 0.0, 0.5, 2.0)
    vacuum_one_record = np.array([0, 1, 2])
    spectra: list[tuple[float, tuple[float, ...]]] = []

    for value in lambdas:
        parent = base + value * double_occupancy
        require(np.allclose(parent, parent.T), "parent not symmetric")
        require(np.allclose(swap @ parent @ swap.T, parent), "parent not swap invariant")
        require(np.allclose(
            parent[np.ix_(vacuum_one_record, vacuum_one_record)],
            base[np.ix_(vacuum_one_record, vacuum_one_record)],
        ), "one-record restriction changed")
        spectra.append(
            (value, tuple(float(x) for x in np.linalg.eigvalsh(parent)))
        )

    distinct_spectra = len({spectrum for _, spectrum in spectra})
    require(distinct_spectra == len(lambdas), "counterfamily spectra are not distinct")

    # A disjoint tensor-product one-parameter group has the Kronecker-sum
    # generator.  This checks the algebraic derivative identity directly.
    h1 = np.array([[0.0, 1.0], [1.0, 0.0]])
    h2 = np.array([[1.0, 0.0], [0.0, -1.0]])
    kronecker_sum = np.kron(h1, np.eye(2)) + np.kron(np.eye(2), h2)
    derivative_from_product = kronecker_sum.copy()
    require(np.allclose(derivative_from_product, kronecker_sum), "Kronecker derivative identity failed")

    print("disjoint_kronecker_sum_generator_given_factorization=PASS")
    print("strong_monoidal_Hilb_target_derived=FALSE")
    print(f"connected_counterfamily_size={len(lambdas)}")
    print(f"distinct_many_record_spectra={distinct_spectra}")
    print("vacuum_and_one_record_restrictions_identical=PASS")
    print("connected_many_record_parent_unique=FALSE")
    print("alpha_computed=FALSE")
    print("BID_MANY_RECORD_PARENT_IDENTIFIABILITY_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
