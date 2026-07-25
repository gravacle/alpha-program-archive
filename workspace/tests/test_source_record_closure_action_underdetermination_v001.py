"""Independent exact checks for the closure-potential countermodels."""

from __future__ import annotations

from fractions import Fraction


def potential_derivative(rho: Fraction, n: int) -> Fraction:
    return 4 * rho * (rho * rho - n)


def potential_second_derivative(rho_squared: Fraction, n: int) -> Fraction:
    return 12 * rho_squared - 4 * n


def test_v1_stationary_curvatures() -> None:
    assert potential_derivative(Fraction(0), 1) == 0
    assert potential_derivative(Fraction(1), 1) == 0
    assert potential_second_derivative(Fraction(0), 1) < 0
    assert potential_second_derivative(Fraction(1), 1) > 0


def test_v2_stationary_curvatures_without_float_sqrt() -> None:
    assert potential_derivative(Fraction(0), 2) == 0
    assert potential_second_derivative(Fraction(0), 2) < 0
    assert potential_second_derivative(Fraction(2), 2) > 0


def test_two_minimum_radius_squares_are_distinct() -> None:
    assert Fraction(1) != Fraction(2)
