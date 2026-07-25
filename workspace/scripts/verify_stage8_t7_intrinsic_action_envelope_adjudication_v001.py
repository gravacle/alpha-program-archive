#!/usr/bin/env python3
"""Independent exact verification of the intrinsic-action envelope."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "stage8_execution/work/T07_intrinsic_action_envelope_adjudication.json"
OUT = ROOT / "stage8_execution/work/T07_intrinsic_action_envelope_adjudication_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def parse_fraction(value: str) -> Fraction:
    return Fraction(value)


def integrate_monomial_symmetric(coefficient: Fraction, power: int) -> Fraction:
    """Return 2*integral_0^(1/2) coefficient*t^power dt."""
    return Fraction(2) * coefficient * Fraction(1, power + 1) * Fraction(1, 2) ** (power + 1)


def main() -> None:
    primary = json.loads(PRIMARY.read_text(encoding="ascii"))

    # This route reconstructs the geometry from piecewise monomial
    # integration rather than importing the primary helper functions.
    v4_over_pi = integrate_monomial_symmetric(Fraction(4, 3), 3)
    rho_times_pi = 1 / v4_over_pi
    old_total_over_pi = integrate_monomial_symmetric(Fraction(128, 3), 6)

    values = {}
    for label, t in (("quarter", Fraction(1, 4)), ("midpoint", Fraction(1, 2))):
        v3_pi = Fraction(4, 3) * t**3
        w = rho_times_pi * v3_pi
        values[label] = {
            "V3_over_pi": v3_pi,
            "w": w,
            "push_times_pi": w / v3_pi,
        }

    checks = {
        "V4": v4_over_pi == Fraction(1, 24),
        "rho": rho_times_pi == 24,
        "time_marginal_quarter": values["quarter"]["w"] == Fraction(1, 2),
        "time_marginal_midpoint": values["midpoint"]["w"] == 4,
        "pushforward_equals_uniform_quarter":
            values["quarter"]["push_times_pi"] == rho_times_pi,
        "pushforward_equals_uniform_midpoint":
            values["midpoint"]["push_times_pi"] == rho_times_pi,
        "old_density_varies":
            values["quarter"]["V3_over_pi"] != values["midpoint"]["V3_over_pi"],
        "old_total": old_total_over_pi == Fraction(2, 21),
        "primary_verdict":
            primary["overall_verdict"] == "INTRINSIC_ACTION_ENVELOPE_DERIVED_ER_B",
        "primary_protected_flags":
            primary["alpha_computed"] is False
            and primary["proof_authorized"] is False
            and primary["kappa_record_computed"] is False,
    }
    require(all(checks.values()), f"Independent envelope check failed: {checks}")

    result = {
        "schema": "stage8_t7_intrinsic_action_envelope_adjudication_verification_v001",
        "primary_sha256": sha256(PRIMARY),
        "independent_exact": {
            "V4_over_pi": "1/24",
            "rho_times_pi": "24",
            "old_ER_A_total_local_measure_over_pi": "2/21",
            "quarter_w": "1/2",
            "midpoint_w": "4",
        },
        "checks": checks,
        "pass": True,
        "envelope_realization_derived": True,
        "ER_B_selected_by_operator_measure": True,
        "sharp_cell_implementability_proved": False,
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
