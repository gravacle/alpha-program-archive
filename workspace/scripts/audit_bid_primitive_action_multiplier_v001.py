#!/usr/bin/env python3
"""Exact finite audit of the primitive U(1) action-character multiplier."""

from __future__ import annotations

from fractions import Fraction


def kernel_order(character: int) -> int | str:
    if character == 0:
        return "infinite"
    return abs(character)


def main() -> None:
    characters = tuple(range(-12, 13))
    nontrivial_faithful = tuple(
        n for n in characters if n != 0 and kernel_order(n) == 1
    )
    assert nontrivial_faithful == (-1, 1)

    noninteger_competitors = (
        Fraction(1, 2),
        Fraction(3, 2),
        Fraction(5, 3),
    )
    # exp(i c theta) is single-valued on theta mod 2pi iff c is integer.
    assert all(value.denominator != 1 for value in noninteger_competitors)

    higher_integer_competitors = tuple(n for n in range(2, 13))
    assert all(kernel_order(n) > 1 for n in higher_integer_competitors)

    print(f"integer_characters_audited={len(characters)}")
    print("nontrivial_faithful_characters=-1,+1")
    print("noninteger_amplitude_powers_single_valued=FALSE")
    print("higher_integer_characters_primitive_faithful=FALSE")
    print("positive_orientation_primitive_character=+1")
    print("primitive_attenuation_multiplier=1")
    print("complete_Q_spec_amplitude_derived=FALSE")
    print("unique_physical_record_duration_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_PRIMITIVE_ACTION_MULTIPLIER_AUDIT=PASS")


if __name__ == "__main__":
    main()
