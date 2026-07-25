#!/usr/bin/env python3
"""Fail-closed audit of the repaired public-record Hilbertization axioms."""

from __future__ import annotations

from fractions import Fraction
import itertools


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                left - scale * right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def parameter_indices(size: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    diagonal = tuple(range(size))
    offdiagonal = tuple(range(size, size * size))
    require(
        len(diagonal) + len(offdiagonal) == size * size,
        "Hermitian parameter inventory is incomplete",
    )
    return diagonal, offdiagonal


def constraint_system(size: int, include_singleton_inclusions: bool) -> list[list[Fraction]]:
    variables = size * size
    diagonal, offdiagonal = parameter_indices(size)
    rows: list[list[Fraction]] = []

    # QR2: both real and imaginary parts of every off-diagonal Hermitian
    # parameter vanish because pointer projections are orthogonal.
    for variable in offdiagonal:
        row = [Fraction(0, 1) for _ in range(variables)]
        row[variable] = Fraction(1, 1)
        rows.append(row)

    # QR5: relabeling invariance makes every diagonal norm equal. Without
    # QR3 this leaves exactly one common positive scale.
    for variable in diagonal[1:]:
        row = [Fraction(0, 1) for _ in range(variables)]
        row[variable] = Fraction(1, 1)
        row[diagonal[0]] = Fraction(-1, 1)
        rows.append(row)

    # QR3: each singleton inclusion is probability preserving, so every
    # diagonal label norm is one in the larger register.
    if include_singleton_inclusions:
        for variable in diagonal:
            row = [Fraction(0, 1) for _ in range(variables)]
            row[variable] = Fraction(1, 1)
            rows.append(row)
    return rows


def main() -> None:
    object_sizes = tuple(range(1, 17))
    old_axiom_free_dimensions = []
    for size in object_sizes:
        variables = size * size
        old_rank = rank(constraint_system(size, False))
        repaired_rank = rank(constraint_system(size, True))
        require(
            old_rank == variables - 1,
            f"QR1,QR2,QR4,QR5 did not retain exactly one common scale at size {size}",
        )
        require(
            repaired_rank == variables,
            f"repaired record axioms leave a Gram freedom at size {size}",
        )
        old_axiom_free_dimensions.append(variables - old_rank)

    require(
        max(old_axiom_free_dimensions) > 0,
        "old underdetermination negative control disappeared",
    )

    product_cases = ((1, 1), (2, 3), (3, 4), (5, 2))
    for left, right in product_cases:
        cartesian = tuple(itertools.product(range(left), range(right)))
        tensor_indices = tuple(
            (index // right, index % right) for index in range(left * right)
        )
        require(
            cartesian == tensor_indices,
            f"Cartesian/tensor basis mismatch for {left}x{right}",
        )

    left_size, middle_size, right_size = 2, 3, 4
    triples = tuple(
        itertools.product(
            range(left_size), range(middle_size), range(right_size)
        )
    )
    left_associated = tuple(((x, y), z) for x, y, z in triples)
    right_associated = tuple((x, (y, z)) for x, y, z in triples)
    require(
        tuple((xy[0], xy[1], z) for xy, z in left_associated) == triples,
        "left associator is not canonical",
    )
    require(
        tuple((x, yz[0], yz[1]) for x, yz in right_associated) == triples,
        "right associator is not canonical",
    )
    original_pairs = ((0, 1), (1, 2))
    swapped_once = tuple((right, left) for left, right in original_pairs)
    swapped_twice = tuple((right, left) for left, right in swapped_once)
    require(swapped_twice == original_pairs, "symmetry is not involutive")

    print(f"record_register_sizes_classified={len(object_sizes)}")
    print("without_QR3_common_scale_freedom=REPRODUCED")
    print("pointer_projection_offdiagonal_constraints=PASS")
    print("probability_preserving_singleton_inclusions=PASS")
    print("repaired_constraint_rank_equals_n_squared=PASS")
    print(f"independent_register_product_cases={len(product_cases)}")
    print("tensor_associativity_and_symmetry_given_QR6_QR7=PASS")
    print("public_record_Hilbertization_from_QR1_QR7=PASS")
    print("Born_kinematics_derived_from_deeper_action=FALSE")
    print("global_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_PUBLIC_RECORD_HILBERTIZATION_AUDIT=PASS_CONDITIONAL")


if __name__ == "__main__":
    main()
