#!/usr/bin/env python3
"""Audit the exact competing Stage-3 energy normalizations."""

from fractions import Fraction
import json
import math
from pathlib import Path


def main() -> None:
    # At marginal compactness C=1 and R=cT/2:
    # E_MS T / hbar = (T/t_P)^2 / 4
    # E_BY T / hbar = (T/t_P)^2 / 2
    ms_quadratic_coefficient = Fraction(1, 4)
    by_quadratic_coefficient = Fraction(1, 2)
    interval_ratio_ms_over_by = math.sqrt(
        float(by_quadratic_coefficient / ms_quadratic_coefficient)
    )

    result = {
        "schema": "bid-ctp-hamilton-jacobi-scale-bridge-v001",
        "target_values_used": False,
        "marginal_compactness": 1,
        "causal_radius_over_cT": "1/2",
        "misner_sharp_action_coefficient": str(ms_quadratic_coefficient),
        "brown_york_action_coefficient": str(by_quadratic_coefficient),
        "T_over_tP_for_s_equals_pi_misner_sharp": 2.0 * math.sqrt(math.pi),
        "T_over_tP_for_s_equals_pi_brown_york": math.sqrt(2.0 * math.pi),
        "interval_ratio_misner_sharp_over_brown_york": interval_ratio_ms_over_by,
        "energy_choice_changes_interval": not math.isclose(
            interval_ratio_ms_over_by, 1.0
        ),
        "bare_null_diamond_action_normalization_unique": False,
        "reparametrized_null_diamond_action_scale_unique": False,
        "causal_diamond_action_selects_absolute_radius": False,
        "absolute_record_interval_derived": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "BLOCK_STAGE3_HAMILTON_JACOBI_ENERGY_NOT_SELECTED",
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "bid_ctp_hamilton_jacobi_scale_bridge_v001.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
