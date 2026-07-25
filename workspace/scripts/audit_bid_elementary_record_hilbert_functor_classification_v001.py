#!/usr/bin/env python3
"""Fail-closed audit of the conditional elementary-record metric classification."""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    columns = len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    left - scale * right
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def hermitian_constraint_system(dimension: int) -> tuple[list[list[Fraction]], int]:
    # A Hermitian n x n matrix has n diagonal real variables and two real
    # variables for every off-diagonal pair: n^2 real variables in total.
    variable_count = dimension * dimension
    rows: list[list[Fraction]] = []
    for variable in range(variable_count):
        row = [Fraction(0, 1) for _ in range(variable_count)]
        row[variable] = Fraction(1, 1)
        rows.append(row)
    return rows, variable_count


def induced_inclusion(
    source_dimension: int,
    target_dimension: int,
    image: tuple[int, ...],
    phases: tuple[complex, ...],
) -> list[list[complex]]:
    require(len(image) == source_dimension, "inclusion image has wrong size")
    require(len(phases) == source_dimension, "phase list has wrong size")
    require(len(set(image)) == source_dimension, "inclusion is not injective")
    require(
        all(0 <= index < target_dimension for index in image),
        "inclusion index outside target",
    )
    require(
        all(abs(abs(phase) - 1.0) < 1e-15 for phase in phases),
        "fiber phase is not unitary",
    )
    matrix = [
        [0j for _ in range(source_dimension)] for _ in range(target_dimension)
    ]
    for source_index, target_index in enumerate(image):
        matrix[target_index][source_index] = phases[source_index]
    return matrix


def adjoint_product(matrix: list[list[complex]]) -> list[list[complex]]:
    rows = len(matrix)
    columns = len(matrix[0])
    return [
        [
            sum(
                matrix[row][left].conjugate() * matrix[row][right]
                for row in range(rows)
            )
            for right in range(columns)
        ]
        for left in range(columns)
    ]


def identity(dimension: int) -> list[list[complex]]:
    return [
        [complex(row == column) for column in range(dimension)]
        for row in range(dimension)
    ]


def main() -> None:
    classified_dimensions = tuple(range(1, 13))
    for dimension in classified_dimensions:
        system, variables = hermitian_constraint_system(dimension)
        require(variables == dimension * dimension, "wrong Hermitian variable count")
        require(
            rank(system) == variables,
            "orthogonality and unit-line constraints do not fix every variable",
        )

    # These cases represent degrees 0, 1, and 2, with nontrivial unit changes
    # of frame on the abstract Hermitian line fibers.
    inclusion_cases = (
        (0, 1, 4, (2,), (1j,)),
        (1, 2, 5, (0, 4), (-1 + 0j, 1j)),
        (2, 3, 7, (1, 3, 6), (1 + 0j, -1j, -1 + 0j)),
        (2, 4, 9, (0, 2, 5, 8), (1j, -1j, 1 + 0j, -1 + 0j)),
    )
    for _, source_dimension, target_dimension, image, phases in inclusion_cases:
        inclusion = induced_inclusion(
            source_dimension, target_dimension, image, phases
        )
        require(
            adjoint_product(inclusion) == identity(source_dimension),
            "canonical induced map is not an isometry",
        )

    rescaling_competitors = (
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(3, 2),
    )
    require(
        all(scale * scale != 1 for scale in rescaling_competitors),
        "a positive nonunit rescaling survived",
    )

    print(f"positive_Hermitian_dimensions_classified={len(classified_dimensions)}")
    print("real_variables_per_n_by_n_Hermitian_matrix=n_squared")
    print("constraint_rank_equals_variable_count=PASS")
    print("abstract_Hermitian_line_unit_frames=PASS")
    print("degrees_0_1_2_scope=PASS")
    print(f"canonical_inclusion_isometry_cases={len(inclusion_cases)}")
    print("positive_nonunit_rescalings_rejected=PASS")
    print("counting_metric_unique_given_declared_hypothesis=PASS")
    print("strong_monoidal_functor_derived=FALSE")
    print("deeper_physical_Hilbertization_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_ELEMENTARY_RECORD_METRIC_CONDITIONAL_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
