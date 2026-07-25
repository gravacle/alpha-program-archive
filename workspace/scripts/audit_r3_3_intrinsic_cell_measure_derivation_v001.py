#!/usr/bin/env python3
"""Exact nested-diamond and sealed-text audit for R3.3."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BID = ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
MONOIDAL = ROOT / "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md"
RESULT = ROOT / "results" / "r3_3_intrinsic_cell_measure_derivation_v001.json"


def poly_add(left: dict[int, Fraction], right: dict[int, Fraction]):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, Fraction()) + value
    return {degree: value for degree, value in result.items() if value}


def poly_mul(left: dict[int, Fraction], right: dict[int, Fraction]):
    result: dict[int, Fraction] = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, Fraction()) + left_value * right_value
    return result


def poly_scale(poly: dict[int, Fraction], scale: Fraction):
    return {degree: value * scale for degree, value in poly.items()}


def poly_power(poly: dict[int, Fraction], exponent: int):
    result = {0: Fraction(1)}
    for _ in range(exponent):
        result = poly_mul(result, poly)
    return result


def poly_integral(poly: dict[int, Fraction], lower: Fraction, upper: Fraction):
    return sum(
        value * (upper ** (degree + 1) - lower ** (degree + 1))
        / Fraction(degree + 1)
        for degree, value in poly.items()
    )


def bipoly_add(
    left: dict[int, dict[int, Fraction]],
    right: dict[int, dict[int, Fraction]],
):
    result = dict(left)
    for radial_degree, time_poly in right.items():
        result[radial_degree] = poly_add(
            result.get(radial_degree, {}), time_poly
        )
    return {
        radial_degree: time_poly
        for radial_degree, time_poly in result.items()
        if time_poly
    }


def bipoly_mul(
    left: dict[int, dict[int, Fraction]],
    right: dict[int, dict[int, Fraction]],
):
    result: dict[int, dict[int, Fraction]] = {}
    for left_radial, left_time in left.items():
        for right_radial, right_time in right.items():
            radial_degree = left_radial + right_radial
            result[radial_degree] = poly_add(
                result.get(radial_degree, {}),
                poly_mul(left_time, right_time),
            )
    return result


def bipoly_scale(poly: dict[int, dict[int, Fraction]], scale: Fraction):
    return {
        radial_degree: poly_scale(time_poly, scale)
        for radial_degree, time_poly in poly.items()
    }


def integrate_unit_diamond(poly: dict[int, dict[int, Fraction]]) -> Fraction:
    """Return (1/pi) times the 3+1-dimensional unit-diamond integral."""
    time = {1: Fraction(1)}
    half = {0: Fraction(1, 2)}
    total = Fraction()
    regions = (
        (Fraction(-1, 2), Fraction(0), poly_add(half, time)),
        (
            Fraction(0),
            Fraction(1, 2),
            poly_add(half, poly_scale(time, Fraction(-1))),
        ),
    )
    for lower, upper, radial_limit in regions:
        radial_integral: dict[int, Fraction] = {}
        for radial_degree, time_poly in poly.items():
            radial_integral = poly_add(
                radial_integral,
                poly_scale(
                    poly_mul(
                        time_poly,
                        poly_power(radial_limit, radial_degree + 3),
                    ),
                    Fraction(1, radial_degree + 3),
                ),
            )
        # Angular integration contributes 4*pi.
        total += Fraction(4) * poly_integral(radial_integral, lower, upper)
    return total


def nested_diamond_moments():
    """Compute all raw moments after mapping the child to a unit diamond."""
    time = {1: Fraction(1)}
    half = {0: Fraction(1, 2)}

    child_plus = poly_power(poly_add(time, half), 2)
    child_minus = poly_power(
        poly_add(half, poly_scale(time, Fraction(-1))), 2
    )
    parent_far_minus = poly_power(
        poly_add({0: Fraction(3, 2)}, poly_scale(time, Fraction(-1))), 2
    )

    one = {0: {0: Fraction(1)}}
    child_u = {
        0: poly_mul(child_plus, child_minus),
        2: poly_scale(poly_add(child_plus, child_minus), Fraction(-1)),
        4: {0: Fraction(1)},
    }
    parent_u = bipoly_scale(
        {
            0: poly_mul(child_plus, parent_far_minus),
            2: poly_scale(
                poly_add(child_plus, parent_far_minus), Fraction(-1)
            ),
            4: {0: Fraction(1)},
        },
        Fraction(1, 16),
    )
    physical_time = {0: {0: Fraction(-1, 4), 1: Fraction(1, 2)}}

    return {
        "volume": integrate_unit_diamond(one),
        "child_u": integrate_unit_diamond(child_u),
        "parent_u": integrate_unit_diamond(parent_u),
        "physical_time": integrate_unit_diamond(physical_time),
        "time_child_u": integrate_unit_diamond(
            bipoly_mul(physical_time, child_u)
        ),
        "time_parent_u": integrate_unit_diamond(
            bipoly_mul(physical_time, parent_u)
        ),
        "child_u_squared": integrate_unit_diamond(
            bipoly_mul(child_u, child_u)
        ),
        "child_u_parent_u": integrate_unit_diamond(
            bipoly_mul(child_u, parent_u)
        ),
    }


def rational_mean(base_num, weighted_num, base_den, weighted_den, a):
    return (base_num + a * weighted_num) / (base_den + a * weighted_den)


def as_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    bid_text = BID.read_text()
    monoidal_text = MONOIDAL.read_text()
    inherited_text_checks = {
        "per_cell_H_r_U": all(
            phrase in bid_text
            for phrase in (
                "H_(disjoint c)=tensor_c H_c",
                "r_(disjoint c)=tensor_c r_c",
                "U_(disjoint c)=tensor_c U_c",
            )
        ),
        "per_cell_amplitude": "A_(disjoint c)=product_c A_c" in bid_text,
        "each_cell_volume_response": all(
            phrase in bid_text
            for phrase in (
                "Therefore each cell contributes",
                "V_cell sum_(mu<nu) F_(mu nu)^2",
            )
        ),
        "shape_scalar_forbidden": (
            "any residual\nshape-dependent scalar fails A27" in bid_text
        ),
        "common_refinement_pullback_required": (
            "The response map must commute with pullback to a common refinement"
            in bid_text
        ),
        "elementary_refinement_invariance_required": (
            "invariant under each elementary\nrefinement" in bid_text
        ),
        "cellulation_dependence_is_failure": (
            "limit depends on cellulation, the connected response gate fails"
            in monoidal_text
        ),
    }
    intrinsic_binding_pass = all(inherited_text_checks.values())

    moments = nested_diamond_moments()
    expected_moments = {
        "volume": Fraction(1, 24),
        "child_u": Fraction(1, 1440),
        "parent_u": Fraction(19, 23040),
        "physical_time": Fraction(-1, 96),
        "time_child_u": Fraction(-1, 5760),
        "time_parent_u": Fraction(-1, 5760),
        "child_u_squared": Fraction(1, 50400),
        "child_u_parent_u": Fraction(1, 57600),
    }
    exact_moments_pass = moments == expected_moments

    samples = {}
    for integer_a in (0, 1, 2, 4, 8):
        a = Fraction(integer_a)
        parent_time = rational_mean(
            moments["physical_time"],
            moments["time_parent_u"],
            moments["volume"],
            moments["parent_u"],
            a,
        )
        child_time = rational_mean(
            moments["physical_time"],
            moments["time_child_u"],
            moments["volume"],
            moments["child_u"],
            a,
        )
        parent_child_u = rational_mean(
            moments["child_u"],
            moments["child_u_parent_u"],
            moments["volume"],
            moments["parent_u"],
            a,
        )
        child_child_u = rational_mean(
            moments["child_u"],
            moments["child_u_squared"],
            moments["volume"],
            moments["child_u"],
            a,
        )
        samples[str(integer_a)] = {
            "delta_mean_t_parent_minus_intrinsic": as_text(
                parent_time - child_time
            ),
            "delta_mean_u_child_parent_minus_intrinsic": as_text(
                parent_child_u - child_child_u
            ),
        }

    # Exact symbolic differences:
    # delta_t = 3a/[4(960+19a)]
    # delta_u = -a(a+45)/[7(a+60)(19a+960)]
    symbolic_factor_check = True
    for integer_a in range(0, 33):
        a = Fraction(integer_a)
        expected_delta_time = (
            Fraction(3) * a / (Fraction(4) * (Fraction(960) + 19 * a))
        )
        expected_delta_u = (
            -a
            * (a + 45)
            / (Fraction(7) * (a + 60) * (19 * a + 960))
        )
        if Fraction(samples.get(str(integer_a), {}).get(
            "delta_mean_t_parent_minus_intrinsic", "0/1"
        )) != expected_delta_time and integer_a in (0, 1, 2, 4, 8):
            symbolic_factor_check = False

        parent_time = rational_mean(
            moments["physical_time"],
            moments["time_parent_u"],
            moments["volume"],
            moments["parent_u"],
            a,
        )
        child_time = rational_mean(
            moments["physical_time"],
            moments["time_child_u"],
            moments["volume"],
            moments["child_u"],
            a,
        )
        parent_child_u = rational_mean(
            moments["child_u"],
            moments["child_u_parent_u"],
            moments["volume"],
            moments["parent_u"],
            a,
        )
        child_child_u = rational_mean(
            moments["child_u"],
            moments["child_u_squared"],
            moments["volume"],
            moments["child_u"],
            a,
        )
        symbolic_factor_check &= parent_time - child_time == expected_delta_time
        symbolic_factor_check &= parent_child_u - child_child_u == expected_delta_u

    only_a_zero_survives_nonnegative_family = symbolic_factor_check

    if (
        intrinsic_binding_pass
        and exact_moments_pass
        and only_a_zero_survives_nonnegative_family
    ):
        verdict = "INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE"
    elif not intrinsic_binding_pass:
        verdict = "STRICT_LOCALITY_ADOPTION_REQUIRED"
    else:
        verdict = "R3_3_REMAINS_OPEN"

    result = {
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "inherited_text_checks": inherited_text_checks,
        "intrinsic_per_cell_response_binding": intrinsic_binding_pass,
        "moments_over_pi_in_child_unit_coordinates": {
            key: as_text(value) for key, value in moments.items()
        },
        "exact_moments_pass": exact_moments_pass,
        "symbolic_differences": {
            "delta_mean_t_parent_minus_intrinsic": (
                "3*a/[4*(960+19*a)]"
            ),
            "delta_mean_u_child_parent_minus_intrinsic": (
                "-a*(a+45)/[7*(a+60)*(19*a+960)]"
            ),
        },
        "sample_differences": samples,
        "symbolic_factor_check": symbolic_factor_check,
        "only_a_zero_survives_for_a_ge_zero": (
            only_a_zero_survives_nonnegative_family
        ),
        "new_strict_locality_principle_adopted": False,
        "verdict": verdict,
        "spectral_density_derived": False,
        "hypothesis_promoted_to_principle": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
