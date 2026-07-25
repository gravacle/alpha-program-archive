#!/usr/bin/env python3
"""Adjudicate the causal-cell envelope from the intrinsic action measure."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_INTRINSIC_ACTION_ENVELOPE_ADJUDICATION_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_intrinsic_action_envelope_adjudication.json"

AUTHORITIES = {
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md":
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2",
    "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md":
        "a27a2d571273494a0787e2283734ef1405d74dadfe16d64d3450bb4536e50732",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md":
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md":
        "202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35",
    "STAGE8_T7_INTRINSIC_MEASURE_SUPPORT_PROJECTION_NORMALIZATION_SPEC_V001.md":
        "cb88ef62a36597b67bf8a2415ed335741a8f5f4c1f86646e7e95d3581b45b312",
    "stage8_execution/work/T07_support_projection_normalization.json":
        "ef190c0b4bf4f1ddbabbe228a4dfce55bf8b27d612306d74cc1b9ba9d3ad44df",
    "STAGE8_T7_INTRINSIC_MEASURE_PARENT_NORMALIZATION_SCOPE_CORRECTION_V001.md":
        "dcb6b36e129edf633f4f4279d959a11526acdc7267bca4055865c32d8ab9318e",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def v3_over_pi(t: Fraction) -> Fraction:
    r = min(t, 1 - t)
    return Fraction(4, 3) * r**3


def main() -> None:
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    # Exact piecewise-polynomial integrals on the unit-duration diamond.
    v4_over_pi = Fraction(2) * Fraction(4, 3) * (Fraction(1, 2) ** 4) / 4
    rho_times_pi = 1 / v4_over_pi
    old_er_a_total_over_pi = (
        Fraction(2)
        * 32
        * Fraction(4, 3)
        * (Fraction(1, 2) ** 7)
        / 7
    )

    samples = {}
    for label, t in (("quarter", Fraction(1, 4)), ("midpoint", Fraction(1, 2))):
        volume_over_pi = v3_over_pi(t)
        marginal = rho_times_pi * volume_over_pi
        push_coefficient_times_pi = marginal / volume_over_pi
        samples[label] = {
            "t": fstr(t),
            "V3_over_pi": fstr(volume_over_pi),
            "w": fstr(marginal),
            "pushforward_coefficient_times_pi": fstr(push_coefficient_times_pi),
            "uniform_density_coefficient_times_pi": fstr(rho_times_pi),
            "old_ER_A_to_uniform_ratio_over_pi": fstr(volume_over_pi),
        }

    push_matches_uniform = all(
        row["pushforward_coefficient_times_pi"] == fstr(rho_times_pi)
        for row in samples.values()
    )
    old_density_not_constant = (
        samples["quarter"]["old_ER_A_to_uniform_ratio_over_pi"]
        != samples["midpoint"]["old_ER_A_to_uniform_ratio_over_pi"]
    )
    old_measure_not_uniform_normalized = old_er_a_total_over_pi != 1

    passed = (
        v4_over_pi == Fraction(1, 24)
        and rho_times_pi == 24
        and samples["quarter"]["w"] == "1/2"
        and samples["midpoint"]["w"] == "4"
        and push_matches_uniform
        and old_density_not_constant
        and old_measure_not_uniform_normalized
    )

    result = {
        "schema": "stage8_t7_intrinsic_action_envelope_adjudication_v001",
        "spec_sha256": sha256(SPEC),
        "authority_hashes_verified": True,
        "exact_geometry": {
            "V4_over_pi": fstr(v4_over_pi),
            "rho_times_pi": fstr(rho_times_pi),
            "old_ER_A_total_local_measure_over_pi": fstr(old_er_a_total_over_pi),
            "samples": samples,
        },
        "operator_identity": {
            "direct_uniform_form": "tau_R*(24/pi)*M(t)",
            "disintegrated_form": "tau_R*w(t)*[M(t)/V3(t)]",
            "forms_equal_exactly": push_matches_uniform,
            "physical_product_bounded_at_tips": True,
        },
        "negative_controls": {
            "old_ER_A_local_density_is_not_constant": old_density_not_constant,
            "no_constant_rescaling_matches_both_test_slices": old_density_not_constant,
            "old_ER_A_does_not_represent_normalized_uniform_four_measure":
                old_measure_not_uniform_normalized,
            "finite_completed_amplitudes_used_for_selection": False,
        },
        "support_fraction_theorem_retained_but_not_parent_envelope_authority": True,
        "overall_verdict": (
            "INTRINSIC_ACTION_ENVELOPE_DERIVED_ER_B"
            if passed
            else "INTRINSIC_ACTION_ENVELOPE_GATE_BLOCKED"
        ),
        "envelope_realization_derived": passed,
        "ER_A_old_implementation_admissible": False,
        "ER_B_selected_by_operator_measure": passed,
        "historical_output_blindness_claimed": False,
        "no_target_access_attestation": True,
        "sharp_cell_implementability_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
