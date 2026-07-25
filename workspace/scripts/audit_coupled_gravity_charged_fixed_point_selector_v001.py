#!/usr/bin/env python3
"""Algebra and fail-closed audit for the coupled fixed-point selector."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "COUPLED_GRAVITY_CHARGED_FIXED_POINT_SELECTOR_GATE_V001.md"
AUTHORITY = ROOT / "results" / "current_authority_ledger_v002.json"
RESULT = ROOT / "results" / "coupled_gravity_charged_fixed_point_selector_v001.json"


def beta(alpha: float, f_grav: float, b_ch: float) -> float:
    return -f_grav * alpha + b_ch * alpha * alpha


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))

    algebra_errors: list[float] = []
    for f_grav, b_ch in ((0.2, 3.0), (1.25, 8.5), (0.031, 0.77)):
        alpha_star = f_grav / b_ch
        k_star = b_ch / (4.0 * math.pi * f_grav)
        alpha_from_k = 1.0 / (4.0 * math.pi * k_star)
        algebra_errors.append(abs(beta(alpha_star, f_grav, b_ch)))
        algebra_errors.append(abs(alpha_from_k - alpha_star))

    required_false = (
        "local_physical_charged_connection_derived = false",
        "f_grav_derived = false",
        "b_ch_derived = false",
        "unique_coupled_fixed_point_derived = false",
        "Thomson_matching_map_derived = false",
        "fixed_point_evaluation_authorized = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    target_patterns = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )

    checks = {
        "corrected_authority_is_current": (
            authority["overall"]
            == "PASS_CURRENT_AUTHORITY_V002_STABILIZER_ONLY_LOCALIZATION_OPEN_ALPHA_FALSE"
        ),
        "fixed_point_algebra_is_consistent": max(algebra_errors) < 2e-16,
        "all_unresolved_physics_flags_fail_closed": all(
            phrase in note for phrase in required_false
        ),
        "target_literal_guard_passes": not any(
            pattern.search(note) for pattern in target_patterns
        ),
        "endpoint_is_not_used_as_uv_anomalous_dimension": (
            "Equating them without a" in note
            and "derived flow map would be a new numerical identification"
            in note
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_FIXED_POINT_SELECTOR_FORM_INPUTS_UNDERIVED_ALPHA_FALSE"
        if not failed
        else "FAIL_COUPLED_FIXED_POINT_SELECTOR_GATE_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "maximum_selector_identity_error": max(algebra_errors),
        "coupled_fixed_point_is_valid_selector_form": True,
        "local_physical_charged_connection_derived": False,
        "f_grav_derived": False,
        "b_ch_derived": False,
        "unique_coupled_fixed_point_derived": False,
        "Thomson_matching_map_derived": False,
        "fixed_point_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "SELECTOR_ALGEBRA_REGRESSION_GUARD_NOT_DYNAMICS_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("fixed_point_evaluation_authorized=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
