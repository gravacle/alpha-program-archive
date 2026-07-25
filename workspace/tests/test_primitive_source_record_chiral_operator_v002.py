"""Independent checks for the supplied free chiral-block audit."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_source_record_chiral_operator_v002.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("source_record_audit", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def numeric_determinant(matrix: list[list[complex]]) -> complex:
    total = 0j
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(permutation))
            for right in range(left + 1, len(permutation))
        )
        product = 1 + 0j
        for row, column in enumerate(permutation):
            product *= matrix[row][column]
        total += (-1 if inversions % 2 else 1) * product
    return total


def numeric_kernel(
    p0: int, p1: int, p2: int, p3: int, a: int, b: int
) -> list[list[complex]]:
    phi = complex(a, b)
    return [
        [p0 - p3, -p1 + 1j * p2, -phi, 0],
        [-p1 - 1j * p2, p0 + p3, 0, -phi],
        [-phi.conjugate(), 0, p0 + p3, p1 - 1j * p2],
        [0, -phi.conjugate(), p1 + 1j * p2, p0 - p3],
    ]


def test_determinant_on_independent_non_target_points() -> None:
    points = (
        (2, 1, -3, 4, 5, -2),
        (7, -2, 1, 3, -4, 6),
        (-3, 5, 2, -1, 1, 8),
    )
    for point in points:
        p0, p1, p2, p3, a, b = point
        expected = (
            p0**2 - p1**2 - p2**2 - p3**2 - a**2 - b**2
        ) ** 2
        assert numeric_determinant(numeric_kernel(*point)) == complex(expected)


def test_closure_square_at_three_four_five_slice() -> None:
    phi = complex(3, 4)
    closure = [
        [0, 0, phi, 0],
        [0, 0, 0, phi],
        [phi.conjugate(), 0, 0, 0],
        [0, phi.conjugate(), 0, 0],
    ]
    square = [
        [
            sum(closure[row][index] * closure[index][column] for index in range(4))
            for column in range(4)
        ]
        for row in range(4)
    ]
    assert square == [
        [25, 0, 0, 0],
        [0, 25, 0, 0],
        [0, 0, 25, 0],
        [0, 0, 0, 25],
    ]


def test_no_alpha_or_mass_target_literal_in_audit() -> None:
    text = SCRIPT.read_text(encoding="utf-8").lower()
    forbidden = ("137.035", "137.036", "0.007297", "0.510998", "17.543")
    assert all(value not in text for value in forbidden)
