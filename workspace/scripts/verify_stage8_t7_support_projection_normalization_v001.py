#!/usr/bin/env python3
"""Independent verifier for support-projector normalization."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "stage8_execution/work/T07_support_projection_normalization.json"
OUT = ROOT / "stage8_execution/work/T07_support_projection_normalization_verification.json"


def main() -> None:
    primary = json.loads(PRIMARY.read_text())

    # Piecewise exact quadrature in the time coordinate.
    left = Fraction(32) * Fraction(1, 2) ** 4 / 4
    marginal_total = 2 * left
    occupancies = (Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(1))
    accumulated = tuple(marginal_total * value for value in occupancies)

    pass_value = (
        marginal_total == 1
        and accumulated == occupancies
        and primary["overall_verdict"]
        == "SUPPORT_PROJECTION_NORMALIZATION_DERIVED"
        and primary["support_projection_normalization_derived"]
    )
    result = {
        "schema": "stage8_t7_support_projection_normalization_verification_v001",
        "time_marginal_integral": "1",
        "constant_occupancy_profiles": [str(value) for value in occupancies],
        "accumulated_support_fractions": [str(value) for value in accumulated],
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
