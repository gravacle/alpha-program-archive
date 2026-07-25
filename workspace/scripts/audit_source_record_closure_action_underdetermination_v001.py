#!/usr/bin/env python3
"""Exact countermodel audit for the source-record closure magnitude."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_record_closure_action_underdetermination_v001.json"


def potential(radius_squared: int, minimum_radius_squared: int) -> int:
    return (radius_squared - minimum_radius_squared) ** 2


def radial_stationary_radius_squares(
    minimum_radius_squared: int,
) -> tuple[int, int]:
    """Return squared nonnegative stationary radii of (rho^2-n)^2."""
    return 0, minimum_radius_squared


def radial_second_derivative_from_square(
    radius_squared: int, minimum_radius_squared: int
) -> int:
    """Second derivative of (rho^2-n)^2 with respect to rho."""
    return 12 * radius_squared - 4 * minimum_radius_squared


def main() -> None:
    radius_squares = {}
    for label, minimum_radius_squared in (("V1", 1), ("V2", 2)):
        origin_squared, stable_radius_squared = radial_stationary_radius_squares(
            minimum_radius_squared
        )
        assert origin_squared == 0
        assert potential(stable_radius_squared, minimum_radius_squared) == 0
        assert (
            radial_second_derivative_from_square(
                origin_squared, minimum_radius_squared
            )
            < 0
        )
        assert (
            radial_second_derivative_from_square(
                stable_radius_squared, minimum_radius_squared
            )
            > 0
        )
        radius_squares[label] = stable_radius_squared

    assert radius_squares["V1"] != radius_squares["V2"]

    out = {
        "status": "PASS_CURRENT_PREMISES_DO_NOT_SELECT_CLOSURE_MAGNITUDE",
        "target_values_used": False,
        "V1_stable_radius_in_cell_units": "1",
        "V2_stable_radius_in_cell_units": "sqrt(2)",
        "V1_stable_radius_squared_in_cell_units": radius_squares["V1"],
        "V2_stable_radius_squared_in_cell_units": radius_squares["V2"],
        "stable_radii_differ": True,
        "trial_terms_are_complete_Q_spec_models": False,
        "response_inequivalence_evaluated": False,
        "complete_record_dynamics_supplied": False,
        "closure_background_uniquely_derived": False,
        "record_generated_source_mass_derived": False,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "scope": "local_symmetry_level_nonselection_witness_not_complete_Q_spec_pair",
    }
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
