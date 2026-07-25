#!/usr/bin/env python3
"""Algebra-only audit of two declared radial trial functions."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_record_closure_magnitude_nonderivation_v002.json"


def potential(radius_squared: int, n: int) -> int:
    return (radius_squared - n) ** 2


def nonzero_stationarity_factor(radius_squared: int, n: int) -> int:
    """The nonzero factor of d[(rho^2-n)^2]/d rho = 4 rho(rho^2-n)."""
    return radius_squared - n


def radial_curvature(radius_squared: int, n: int) -> int:
    """d^2[(rho^2-n)^2]/d rho^2 = 12 rho^2 - 4 n."""
    return 12 * radius_squared - 4 * n


def analyze_declared_trial(n: int) -> dict[str, int | bool]:
    stable_radius_squared = n
    stationarity_residual = nonzero_stationarity_factor(
        stable_radius_squared, n
    )
    minimum_value = potential(stable_radius_squared, n)
    curvature = radial_curvature(stable_radius_squared, n)
    return {
        "declared_n": n,
        "stable_radius_squared": stable_radius_squared,
        "nonzero_stationarity_residual": stationarity_residual,
        "minimum_value": minimum_value,
        "radial_curvature": curvature,
        "stationary": stationarity_residual == 0,
        "radially_stable": curvature > 0,
    }


def build_result() -> dict[str, object]:
    trials = [analyze_declared_trial(n) for n in (1, 2)]
    assert all(trial["stationary"] for trial in trials)
    assert all(trial["minimum_value"] == 0 for trial in trials)
    assert all(trial["radially_stable"] for trial in trials)
    minima_differ = (
        trials[0]["stable_radius_squared"]
        != trials[1]["stable_radius_squared"]
    )
    assert minima_differ

    return {
        "status": "PASS_DECLARED_TRIAL_POTENTIAL_ALGEBRA_ONLY",
        "trials": trials,
        "declared_trial_minima_differ": minima_differ,
        "measured_target_values_embedded_in_formulas": False,
        "historical_target_blindness_established": False,
        "complete_record_dynamics_supplied": False,
        "two_complete_admissible_closure_actions_exhibited": False,
        "full_Q_spec_nonuniqueness_proved": False,
        "closure_magnitude_presently_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "scope": "declared_trial_function_algebra_and_missing_derivation_only",
    }


def main() -> None:
    out = build_result()
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
