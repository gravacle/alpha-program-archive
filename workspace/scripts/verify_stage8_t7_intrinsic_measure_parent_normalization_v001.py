#!/usr/bin/env python3
"""Independent exact verifier for the cell-normalization audit."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "stage8_execution/work/T07_intrinsic_measure_parent_normalization.json"
OUT = ROOT / "stage8_execution/work/T07_intrinsic_measure_parent_normalization_verification.json"


def main() -> None:
    primary = json.loads(PRIMARY.read_text())

    # Radius variable r: each radius occurs on two equal time branches.
    # Values are exact coefficients of pi.
    half = Fraction(1, 2)
    slice_volume_pi = Fraction(4, 3)
    cell_volume_pi = (
        2 * slice_volume_pi * half**4 / 4
    )
    old_integral_pi = (
        2
        * slice_volume_pi**2
        * half**7
        / 7
        / cell_volume_pi
    )

    pass_value = (
        cell_volume_pi == Fraction(1, 24)
        and old_integral_pi == Fraction(2, 21)
        and primary["overall_verdict"]
        == "PARENT_NORMALIZATION_DOUBLE_COUNTS_SLICE_VOLUME"
    )

    result = {
        "schema": (
            "stage8_t7_intrinsic_measure_parent_normalization_verification_v001"
        ),
        "independent_coordinate": "slice radius r, with two equal time branches",
        "V4": "pi/24",
        "old_parent_full_cell_uniform_test": "2*pi/21",
        "expected_uniform_intrinsic_measure_test": "1",
        "pass": bool(pass_value),
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not pass_value:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
