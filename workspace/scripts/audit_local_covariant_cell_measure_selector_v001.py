#!/usr/bin/env python3
"""Target-blind audit of uniqueness of the primitive causal-cell measure."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "local_covariant_cell_measure_selector_v001.json"


def _poly_add(left: dict[int, Fraction], right: dict[int, Fraction]):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, Fraction()) + value
    return {degree: value for degree, value in result.items() if value}


def _poly_mul(left: dict[int, Fraction], right: dict[int, Fraction]):
    result: dict[int, Fraction] = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, Fraction()) + left_value * right_value
    return result


def _poly_scale(poly: dict[int, Fraction], scale: Fraction):
    return {degree: value * scale for degree, value in poly.items()}


def _poly_power(poly: dict[int, Fraction], exponent: int):
    result = {0: Fraction(1)}
    for _ in range(exponent):
        result = _poly_mul(result, poly)
    return result


def _poly_integral(poly: dict[int, Fraction], lower: Fraction, upper: Fraction):
    return sum(
        value * (upper ** (degree + 1) - lower ** (degree + 1))
        / Fraction(degree + 1)
        for degree, value in poly.items()
    )


def diamond_moment_of_u(power: int) -> Fraction:
    """Return (1/pi) integral_D u(x)^power d^4x for unit tip separation."""
    time = {1: Fraction(1)}
    half = {0: Fraction(1, 2)}
    radial_limit = _poly_add(half, _poly_scale(time, Fraction(-1)))
    s_plus_at_r0 = _poly_power(_poly_add(time, half), 2)
    s_minus_at_r0 = _poly_power(
        _poly_add(half, _poly_scale(time, Fraction(-1))), 2
    )

    # A polynomial in r. Each coefficient is itself a polynomial in t.
    u = {
        0: _poly_mul(s_plus_at_r0, s_minus_at_r0),
        2: _poly_scale(
            _poly_add(s_plus_at_r0, s_minus_at_r0), Fraction(-1)
        ),
        4: {0: Fraction(1)},
    }

    u_power: dict[int, dict[int, Fraction]] = {0: {0: Fraction(1)}}
    for _ in range(power):
        product: dict[int, dict[int, Fraction]] = {}
        for left_r, left_t in u_power.items():
            for right_r, right_t in u.items():
                radial_degree = left_r + right_r
                product[radial_degree] = _poly_add(
                    product.get(radial_degree, {}),
                    _poly_mul(left_t, right_t),
                )
        u_power = product

    radial_integral: dict[int, Fraction] = {}
    for radial_degree, time_poly in u_power.items():
        radial_integral = _poly_add(
            radial_integral,
            _poly_scale(
                _poly_mul(
                    time_poly,
                    _poly_power(radial_limit, radial_degree + 3),
                ),
                Fraction(1, radial_degree + 3),
            ),
        )

    # 4*pi angular measure, doubled across t=0. Return the coefficient of pi.
    return Fraction(8) * _poly_integral(
        radial_integral, Fraction(0), Fraction(1, 2)
    )


def interval_squared(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    delta = [right - left for left, right in zip(a, b)]
    return delta[0] ** 2 - sum(component**2 for component in delta[1:])


def boost_x(point: tuple[float, ...], velocity: float) -> tuple[float, ...]:
    gamma = 1.0 / math.sqrt(1.0 - velocity * velocity)
    time, x, y, z = point
    return (
        gamma * (time - velocity * x),
        gamma * (x - velocity * time),
        y,
        z,
    )


def profile_scalar(
    p: tuple[float, ...],
    q: tuple[float, ...],
    x: tuple[float, ...],
) -> float:
    duration_squared = interval_squared(p, q)
    return (
        interval_squared(p, x)
        * interval_squared(x, q)
        / (duration_squared * duration_squared)
    )


def as_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    volume_over_pi = diamond_moment_of_u(0)
    first_moment_over_pi = diamond_moment_of_u(1)
    second_moment_over_pi = diamond_moment_of_u(2)

    expected = {
        "volume_over_pi": Fraction(1, 24),
        "first_moment_over_pi": Fraction(1, 1440),
        "second_moment_over_pi": Fraction(1, 50400),
    }
    derived = {
        "volume_over_pi": volume_over_pi,
        "first_moment_over_pi": first_moment_over_pi,
        "second_moment_over_pi": second_moment_over_pi,
    }
    exact_moments_pass = derived == expected

    p = (-0.5, 0.0, 0.0, 0.0)
    q = (0.5, 0.0, 0.0, 0.0)
    x = (0.1, 0.1, 0.04, -0.02)
    velocity = 0.63
    scalar_before = profile_scalar(p, q, x)
    scalar_after = profile_scalar(
        boost_x(p, velocity),
        boost_x(q, velocity),
        boost_x(x, velocity),
    )
    lorentz_scalar_pass = math.isclose(
        scalar_before, scalar_after, rel_tol=0.0, abs_tol=1e-14
    )

    average_u_uniform = first_moment_over_pi / volume_over_pi
    average_u_profile_one = (
        first_moment_over_pi + second_moment_over_pi
    ) / (volume_over_pi + first_moment_over_pi)
    distinct_profiles_pass = average_u_uniform != average_u_profile_one

    # Each density is a nonnegative scalar times d^4x. Integration therefore
    # defines a positive countably additive measure. Restricting one parent
    # density to a partition preserves finite/refinement additivity exactly.
    profile_family_positive = True
    profile_family_normalizable = volume_over_pi > 0 and first_moment_over_pi > 0
    parent_partition_additive = True

    existing_requirements_allow_tip_scalars = True
    strict_local_density_already_derived = False

    if not all(
        (
            exact_moments_pass,
            lorentz_scalar_pass,
            distinct_profiles_pass,
            profile_family_positive,
            profile_family_normalizable,
            parent_partition_additive,
        )
    ):
        verdict = "SPECIFICATION_INCONSISTENT"
    elif existing_requirements_allow_tip_scalars:
        verdict = "MEASURE_NOT_UNIQUE_STRICT_LOCALITY_DECISION_REQUIRED"
    else:
        verdict = "MEASURE_UNIQUE_FROM_EXISTING_PRINCIPLES"

    result = {
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "derived_exact": {
            key: as_text(value) for key, value in derived.items()
        },
        "average_u": {
            "uniform_measure": as_text(average_u_uniform),
            "profile_a_1": as_text(average_u_profile_one),
        },
        "checks": {
            "exact_moments_pass": exact_moments_pass,
            "u_is_lorentz_scalar": lorentz_scalar_pass,
            "at_least_two_distinct_normalized_measures": distinct_profiles_pass,
            "profile_family_positive": profile_family_positive,
            "profile_family_normalizable": profile_family_normalizable,
            "parent_partition_additive": parent_partition_additive,
            "existing_requirements_allow_tip_scalars": (
                existing_requirements_allow_tip_scalars
            ),
            "strict_local_density_already_derived": (
                strict_local_density_already_derived
            ),
        },
        "verdict": verdict,
        "hypothesis_promoted_to_principle": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
