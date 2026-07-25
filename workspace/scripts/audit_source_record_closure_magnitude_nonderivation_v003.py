#!/usr/bin/env python3
"""Fail-closed algebra audit of two declared radial trial functions."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_record_closure_magnitude_nonderivation_v003.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def potential(radius_squared: int, n: int) -> int:
    return (radius_squared - n) ** 2


def nonzero_stationarity_factor(radius_squared: int, n: int) -> int:
    """The nonzero factor of d[(rho^2-n)^2]/d rho = 4 rho(rho^2-n)."""
    return radius_squared - n


def radial_second_derivative(radius_squared: int, n: int) -> int:
    return 12 * radius_squared - 4 * n


def analyze_declared_trial(n: int) -> dict[str, int | bool]:
    stationary_radius_squared = n
    stationarity_residual = nonzero_stationarity_factor(
        stationary_radius_squared, n
    )
    minimum_value = potential(stationary_radius_squared, n)
    second_derivative = radial_second_derivative(stationary_radius_squared, n)
    return {
        "declared_n": n,
        "stationary_radius_squared": stationary_radius_squared,
        "nonzero_stationarity_residual": stationarity_residual,
        "trial_function_value": minimum_value,
        "radial_second_derivative": second_derivative,
        "stationarity_condition_verified": stationarity_residual == 0,
        "positive_radial_second_derivative_verified": second_derivative > 0,
        "physical_stability_derived": False,
    }


def build_result() -> dict[str, object]:
    trials = [analyze_declared_trial(n) for n in (1, 2)]
    require(
        all(trial["stationarity_condition_verified"] for trial in trials),
        "A declared nonzero stationarity condition failed",
    )
    require(
        all(trial["trial_function_value"] == 0 for trial in trials),
        "A declared trial function does not vanish at its stationary point",
    )
    require(
        all(
            trial["positive_radial_second_derivative_verified"]
            for trial in trials
        ),
        "A declared radial second derivative is not positive",
    )
    stationary_points_differ = (
        trials[0]["stationary_radius_squared"]
        != trials[1]["stationary_radius_squared"]
    )
    require(stationary_points_differ, "Declared stationary points do not differ")

    return {
        "status": "PASS_DECLARED_TRIAL_FUNCTION_ALGEBRA_ONLY",
        "trials": trials,
        "declared_trial_stationary_points_differ": stationary_points_differ,
        "measured_target_values_embedded_in_formulas": False,
        "historical_target_blindness_established": False,
        "complete_record_dynamics_supplied": False,
        "physical_closure_stability_derived": False,
        "two_complete_admissible_closure_actions_exhibited": False,
        "full_Q_spec_nonuniqueness_proved": False,
        "closure_magnitude_presently_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "scope": "declared_trial_polynomial_algebra_and_missing_derivation_only",
    }


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
