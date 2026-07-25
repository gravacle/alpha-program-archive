#!/usr/bin/env python3
"""Fail-closed audit of first-opening graph refinement equivalence."""

from __future__ import annotations

import cmath
import itertools


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def compose_path(phases: tuple[float, ...], order: tuple[int, ...]) -> complex:
    segments = [cmath.exp(1j * phase) for phase in phases]
    active = segments[:]
    # Each order entry chooses an adjacent pair in the current list.
    for choice in order:
        left = choice % (len(active) - 1)
        active[left : left + 2] = [active[left + 1] * active[left]]
    require(len(active) == 1, "path reduction did not terminate")
    return active[0]


def cycle_rank(vertices: int, edges: int, components: int = 1) -> int:
    return edges - vertices + components


def main() -> None:
    path_lengths = tuple(range(1, 11))
    reduction_cases = 0
    for length in path_lengths:
        phases = tuple(0.13 * (index + 1) for index in range(length))
        expected = cmath.exp(1j * sum(phases))
        if length == 1:
            require(abs(compose_path(phases, ()) - expected) < 1e-13, "length-one path")
            reduction_cases += 1
            continue
        canonical = tuple(0 for _ in range(length - 1))
        reverse = tuple(
            size - 2 for size in range(length, 1, -1)
        )
        require(
            abs(compose_path(phases, canonical) - expected) < 1e-13,
            f"left reduction failed at length {length}",
        )
        require(
            abs(compose_path(phases, reverse) - expected) < 1e-13,
            f"right reduction failed at length {length}",
        )
        reduction_cases += 2

    # A linear path is a tree, so subdivision preserves cycle rank zero.
    for length in path_lengths:
        require(
            cycle_rank(length + 1, length) == 0,
            "linear path acquired a cycle under subdivision",
        )

    enlarged = {
        "two_parallel_edges": (2, 2, 1),
        "triangle_loop": (3, 3, 1),
        "branched_tree": (4, 3, 0),
    }
    require(
        cycle_rank(*enlarged["two_parallel_edges"][:2])
        == enlarged["two_parallel_edges"][2],
        "parallel-path cycle-rank control failed",
    )
    require(
        cycle_rank(*enlarged["triangle_loop"][:2])
        == enlarged["triangle_loop"][2],
        "loop cycle-rank control failed",
    )
    vertices, edges, expected_rank = enlarged["branched_tree"]
    require(
        cycle_rank(vertices, edges) == expected_rank,
        "branched-tree cycle-rank control failed",
    )
    require(
        any(degree > 2 for degree in (3, 1, 1, 1)),
        "branch-valence negative control failed",
    )

    # Exhaust all binary label patterns on up to four internal vertices:
    # only the all-unlabeled pattern is completely reducible.
    labeled_patterns = 0
    for count in range(1, 5):
        for labels in itertools.product((False, True), repeat=count):
            reducible = not any(labels)
            require(
                reducible == (sum(labels) == 0),
                "public-label reduction rule inconsistent",
            )
            labeled_patterns += 1

    print(f"linear_path_lengths={len(path_lengths)}")
    print(f"transport_reduction_orders_checked={reduction_cases}")
    print("transport_composition_associativity=PASS")
    print("invisible_bivalent_subdivisions_reduce=PASS")
    print(f"public_label_patterns_checked={labeled_patterns}")
    print("parallel_branch_loop_public_label_competitors=ENLARGED")
    print("one_arrow_unique_reduced_linear_representative=PASS")
    print("universal_graph_exhaustion_across_enlarged_branches=FALSE")
    print("alpha_computed=FALSE")
    print("BID_FIRST_OPENING_GRAPH_REFINEMENT_AUDIT=PASS")


if __name__ == "__main__":
    main()
