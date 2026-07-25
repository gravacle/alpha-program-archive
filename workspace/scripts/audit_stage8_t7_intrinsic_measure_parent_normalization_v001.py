#!/usr/bin/env python3
"""Exact audit of the causal-cell measure-to-Hamiltonian normalization."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_INTRINSIC_MEASURE_PARENT_NORMALIZATION_AUDIT_SPEC_V001.md"
OUT = ROOT / "stage8_execution/work/T07_intrinsic_measure_parent_normalization.json"

AUTHORITIES = {
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md":
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md":
        "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md":
        "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def integrate_monomial(coefficient: Fraction, power: int, upper: Fraction) -> Fraction:
    return coefficient * upper ** (power + 1) / (power + 1)


def main() -> None:
    for relative, expected in AUTHORITIES.items():
        require(sha256(ROOT / relative) == expected, f"Authority drift: {relative}")

    half = Fraction(1, 2)
    spatial_volume_pi_coefficient = Fraction(4, 3)
    four_volume_pi_coefficient = 2 * integrate_monomial(
        spatial_volume_pi_coefficient, 3, half
    )
    marginal_coefficient = (
        spatial_volume_pi_coefficient / four_volume_pi_coefficient
    )
    marginal_integral = 2 * integrate_monomial(
        marginal_coefficient, 3, half
    )
    uniform_measure_of_cell = Fraction(1)
    parent_uniform_test_pi_coefficient = 2 * integrate_monomial(
        marginal_coefficient * spatial_volume_pi_coefficient,
        6,
        half,
    )

    require(
        four_volume_pi_coefficient == Fraction(1, 24),
        "Unexpected causal-diamond four-volume",
    )
    require(marginal_coefficient == 32, "Unexpected time marginal")
    require(marginal_integral == 1, "Time marginal is not normalized")
    require(uniform_measure_of_cell == 1, "Uniform cell measure is not normalized")
    require(
        parent_uniform_test_pi_coefficient == Fraction(2, 21),
        "Unexpected double-counted full-cell integral",
    )

    result = {
        "schema": "stage8_t7_intrinsic_measure_parent_normalization_v001",
        "spec_sha256": sha256(SPEC),
        "authority_hashes_verified": True,
        "exact": {
            "V3_left_half": "(4*pi/3)*t^3",
            "V4": "pi/24",
            "time_marginal_left_half": "32*t^3",
            "time_marginal_integral": "1",
            "uniform_measure_full_cell_integral": "1",
            "old_parent_full_cell_uniform_test": "2*pi/21",
            "old_to_uniform_pointwise_ratio_left_half": "(4*pi/3)*t^3",
        },
        "old_parent_equals_uniform_intrinsic_action": False,
        "old_parent_counts_slice_volume_twice": True,
        "equivalent_correct_forms": [
            "tau_R/V4 * M(t)",
            "tau_R*w(t) * M(t)/V3(t)",
        ],
        "overall_verdict": "PARENT_NORMALIZATION_DOUBLE_COUNTS_SLICE_VOLUME",
        "old_hermite_amplitudes_physical_baseline": False,
        "corrected_parent_normalization_frozen": False,
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
