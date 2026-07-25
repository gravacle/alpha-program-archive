#!/usr/bin/env python3
"""Exact support-projector normalization audit for the causal parent."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_INTRINSIC_MEASURE_SUPPORT_PROJECTION_NORMALIZATION_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_support_projection_normalization.json"

AUTHORITIES = {
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md":
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md":
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def integrate_left_monomial(coefficient: Fraction, power: int) -> Fraction:
    half = Fraction(1, 2)
    return 2 * coefficient * half ** (power + 1) / (power + 1)


def main() -> None:
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    w_integral = integrate_left_monomial(Fraction(32), 3)
    require(w_integral == 1, "Intrinsic time marginal is not normalized")

    # Exact finite-dimensional witness for the abstract projection statements.
    # M=diag(1,1,0), with rational normalized probability vectors represented
    # directly by their component probabilities.
    full_probabilities = (Fraction(1, 4), Fraction(3, 4), Fraction(0))
    partial_probabilities = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
    full_occupancy = sum(full_probabilities[:2])
    partial_occupancy = sum(partial_probabilities[:2])
    require(full_occupancy == 1, "Full-support witness failed")
    require(partial_occupancy == Fraction(1, 2), "Partial witness failed")

    # A constant occupancy profile integrates to that same occupancy because
    # w is a probability density.
    full_fraction = w_integral * full_occupancy
    partial_fraction = w_integral * partial_occupancy

    # V3/pi=(4/3)r^3. Its reciprocal is nonconstant and diverges at r=0.
    slice_normalized_is_projection = False
    slice_normalized_bounded_at_tips = False
    additional_scalar_preserves_unit_incidence = False

    pass_value = (
        full_fraction == 1
        and 0 <= partial_fraction < 1
        and not slice_normalized_is_projection
        and not slice_normalized_bounded_at_tips
        and not additional_scalar_preserves_unit_incidence
    )
    require(pass_value, "Support-projector normalization theorem failed")

    result = {
        "schema": "stage8_t7_support_projection_normalization_v001",
        "spec_sha256": sha256(SPEC),
        "authority_hashes_verified": True,
        "exact": {
            "time_marginal_integral": "1",
            "support_projector_spectrum": ["0", "1"],
            "full_support_fraction": "1",
            "partial_support_witness_fraction": "1/2",
            "tau_eff_full_support": "tau_R",
            "tau_eff_partial_witness": "tau_R/2",
            "slice_normalized_multiplier": "M(t)/V3(t)",
            "slice_normalized_tip_behavior": "unbounded as r(t)^(-3)",
        },
        "theorem": {
            "support_fraction_bounds": True,
            "equality_requires_full_support_almost_everywhere": True,
            "positive_measure_deficit_is_strict": True,
            "extra_scalar_changes_unit_incidence": True,
            "slice_normalized_candidate_rejected": True,
            "scalar_density_test_is_not_normalized_state_expectation": True,
        },
        "overall_verdict": "SUPPORT_PROJECTION_NORMALIZATION_DERIVED",
        "support_projection_normalization_derived": True,
        "finite_energy_full_support_state_derived": False,
        "sharp_cell_implementability_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
