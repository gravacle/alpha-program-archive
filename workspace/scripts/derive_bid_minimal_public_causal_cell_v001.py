#!/usr/bin/env python3
"""Audit the Stage-3 minimal public causal-cell algebra.

This program verifies algebra and deformation sensitivity. It does not prove
the physical marginal-publicity premise and it does not evaluate alpha.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "bid_minimal_public_causal_cell_v001.json"


def scale_ratios(
    action_marker: float,
    causal_radius_fraction: float,
    compactness_threshold: float,
) -> dict[str, float]:
    if action_marker <= 0:
        raise ValueError("action_marker must be positive")
    if causal_radius_fraction <= 0:
        raise ValueError("causal_radius_fraction must be positive")
    if compactness_threshold <= 0:
        raise ValueError("compactness_threshold must be positive")

    t_over_tp = math.sqrt(
        2.0
        * action_marker
        / (causal_radius_fraction * compactness_threshold)
    )
    r_over_lp = causal_radius_fraction * t_over_tp
    e_over_ep = action_marker / t_over_tp
    compactness = (
        2.0
        * e_over_ep
        / r_over_lp
    )
    return {
        "T_R_over_t_P": t_over_tp,
        "R_R_over_l_P": r_over_lp,
        "E_R_over_E_P": e_over_ep,
        "M_R_over_m_P": e_over_ep,
        "reconstructed_compactness": compactness,
    }


def main() -> None:
    baseline = scale_ratios(math.pi, 0.5, 1.0)
    expected = {
        "T_R_over_t_P": 2.0 * math.sqrt(math.pi),
        "R_R_over_l_P": math.sqrt(math.pi),
        "E_R_over_E_P": math.sqrt(math.pi) / 2.0,
        "M_R_over_m_P": math.sqrt(math.pi) / 2.0,
        "reconstructed_compactness": 1.0,
    }

    tolerance = 2.0e-15
    baseline_checks = {
        key: math.isclose(baseline[key], value, rel_tol=tolerance, abs_tol=tolerance)
        for key, value in expected.items()
    }

    deformations = {
        "half_action_marker": scale_ratios(math.pi / 2.0, 0.5, 1.0),
        "full_duration_radius": scale_ratios(math.pi, 1.0, 1.0),
        "half_compactness_threshold": scale_ratios(math.pi, 0.5, 0.5),
    }
    deformation_changes_scale = {
        name: not math.isclose(
            row["T_R_over_t_P"],
            baseline["T_R_over_t_P"],
            rel_tol=1.0e-12,
            abs_tol=1.0e-12,
        )
        for name, row in deformations.items()
    }

    all_checks_pass = all(baseline_checks.values()) and all(
        deformation_changes_scale.values()
    )
    result = {
        "schema_version": 1,
        "scope": "STAGE_3_4_CAUSAL_CELL_CONDITIONAL_ALGEBRA_ONLY",
        "inputs": {
            "action_marker_s": "pi",
            "causal_radius_fraction_xi": "1/2",
            "compactness_threshold_chi_star": "1",
            "marginal_public_closure_rule_status": "ADOPTED_LEVEL_1",
            "stationary_Hamiltonian_action_identification_status": "OPEN",
        },
        "baseline": baseline,
        "expected": expected,
        "baseline_checks": baseline_checks,
        "deformations": deformations,
        "deformation_changes_scale": deformation_changes_scale,
        "strict_inequality_without_saturation_selects_unique_scale": False,
        "physical_premise_proved_by_script": False,
        "conditional_absolute_record_interval_formula_derived": all_checks_pass,
        "relative_marker_equals_complete_stationary_Hamiltonian_action_derived": False,
        "absolute_record_interval_derived_in_declared_branch": False,
        "physical_durability_derived": False,
        "complete_Q_spec_sealed": False,
        "physical_Thomson_stiffness_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "verdict": (
            "PASS_CONDITIONAL_CELL_ALGEBRA_PHYSICAL_ACTION_MAP_OPEN"
            if all_checks_pass
            else "BLOCK_STAGE3_ALGEBRA"
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(f"T_R/t_P={baseline['T_R_over_t_P']:.16g}")
    print(f"R_R/l_P={baseline['R_R_over_l_P']:.16g}")
    print(f"E_R/E_P={baseline['E_R_over_E_P']:.16g}")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
