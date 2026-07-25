#!/usr/bin/env python3
"""Independent exact verifier for the R3.4 regulator/ray audit."""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_regulator_scheme_and_ray_sufficiency_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def catalan(n: int) -> int:
    numerator = 1
    denominator = 1
    for k in range(2, n + 1):
        numerator *= n + k
        denominator *= k
    return numerator // denominator


def cubic_closed_walks(order: int) -> int:
    directions = (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    total = 0
    for path in itertools.product(directions, repeat=order):
        endpoint = tuple(sum(step[j] for step in path) for j in range(3))
        total += endpoint == (0, 0, 0)
    return total


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="ascii"))
    half = {2 * n: catalan(n) for n in (1, 2, 3)}
    tree = {order: value * 3 ** (order // 2) for order, value in half.items()}
    cubic = {order: cubic_closed_walks(order) for order in (2, 4, 6)}

    expected = {
        "half_line": {str(k): str(v) for k, v in half.items()},
        "radial_tree": {str(k): str(v) for k, v in tree.items()},
        "cubic_lattice": {str(k): str(v) for k, v in cubic.items()},
    }
    require(result["root_even_moments"] == expected, "Moment reconstruction failed")

    half_m4 = Fraction(half[4], half[2] ** 2)
    half_m6 = Fraction(half[6], half[2] ** 3)
    cubic_m4 = Fraction(cubic[4], cubic[2] ** 2)
    cubic_m6 = Fraction(cubic[6], cubic[2] ** 3)
    require((half_m4, half_m6) == (Fraction(2), Fraction(5)), "Half invariants")
    require(
        (cubic_m4, cubic_m6) == (Fraction(5, 2), Fraction(155, 18)),
        "Cubic invariants",
    )
    require(result["all_three_share_t_minus_3_probability_class"] is True, "Decay")
    require(
        result["all_three_full_measures_equivalent_up_to_energy_scale"] is False,
        "Measure inequivalence was lost",
    )
    require(
        result["covector_ray_and_quasilocal_state_fix_spectral_measure"] is False,
        "Ray sufficiency overclaimed",
    )
    require(result["alpha_computed"] is False, "Alpha status changed")
    print("R3.4 regulator/ray independent verification: PASS")


if __name__ == "__main__":
    main()
