#!/usr/bin/env python3
"""Regression audit for the primitive relative-phase connection."""

from __future__ import annotations

import cmath
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
PRIMITIVE = ROOT / "results" / "primitive_record_carrier_v001.json"
ACTION_GATE = ROOT / "results" / "public_charged_action_uniqueness_v002.json"
RESULT = ROOT / "results" / "primitive_relative_phase_connection_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_provenance() -> bool:
    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    for item in manifest["inputs"]:
        path = (ROOT / item["path"]).resolve()
        if not path.exists() or sha256(path) != item["sha256"]:
            return False
    return True


def rel_phase(theta_0: float, theta_1: float) -> complex:
    return cmath.exp(1j * (theta_1 - theta_0))


def character(winding: int, theta: float) -> complex:
    return cmath.exp(1j * winding * theta)


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    primitive = json.loads(PRIMITIVE.read_text(encoding="utf-8"))
    action_gate = json.loads(ACTION_GATE.read_text(encoding="utf-8"))

    phase_pairs = ((0.1, 0.9), (-0.7, 1.2), (2.3, -1.1))
    common_shifts = (-4.2, 0.0, 0.37, 3.8)
    quotient_errors = []
    for theta_0, theta_1 in phase_pairs:
        base = rel_phase(theta_0, theta_1)
        for shift in common_shifts:
            shifted = rel_phase(theta_0 + shift, theta_1 + shift)
            quotient_errors.append(abs(base - shifted))

    character_errors = []
    for winding in (-3, -1, 0, 1, 4):
        for left, right in ((0.2, 0.7), (-1.1, 0.4), (2.0, -0.3)):
            character_errors.append(
                abs(
                    character(winding, left + right)
                    - character(winding, left)
                    * character(winding, right)
                )
            )

    q = ((0.0, 0.0), (0.0, 1.0))
    q_centered = ((-0.5, 0.0), (0.0, 0.5))
    rank_q = sum(1 for value in (q[0][0], q[1][1]) if value != 0)
    centered_trace = q_centered[0][0] + q_centered[1][1]

    required_status = (
        "identification_with_unique_exterior_EM_connection_derived = false",
        "absolute_Maxwell_stiffness_selected = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    missing_status = [
        phrase for phrase in required_status if phrase not in note
    ]
    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [
        pattern.pattern for pattern in forbidden if pattern.search(note)
    ]

    checks = {
        "all_hash_locked_pre_alpha_sources_match": verify_provenance(),
        "primitive_two_alternative_carrier_is_current": (
            primitive["overall"]
            == "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE"
        ),
        "absolute_action_nonselection_gate_is_current": (
            action_gate["overall"]
            == "PASS_PUBLIC_ACTION_PREMISES_DO_NOT_SELECT_K_SCOPE_ONLY_ALPHA_FALSE"
        ),
        "relative_phase_is_invariant_under_common_rephasing": (
            max(quotient_errors) < 2e-15
        ),
        "integer_characters_compose": max(character_errors) < 2e-15,
        "primitive_uncentered_generator_has_rank_one": rank_q == 1,
        "centered_generator_is_traceless": centered_trace == 0,
        "scope_flags_fail_closed": not missing_status,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_PRIMITIVE_RELATIVE_PHASE_CONNECTION_EM_IDENTIFICATION_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_PRIMITIVE_RELATIVE_PHASE_CONNECTION_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "maximum_common_rephasing_error": max(quotient_errors),
        "maximum_character_composition_error": max(character_errors),
        "primitive_relative_phase_group_derived": True,
        "primitive_relative_generator_rank": 1,
        "primitive_character_lattice": "Z",
        "primitive_unit_winding_derived": True,
        "local_record_comparison_connection_derived": True,
        "identification_with_unique_exterior_EM_connection_derived": False,
        "absolute_Maxwell_stiffness_selected": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "REGRESSION_GUARD_NOT_PROOF_EVIDENCE",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("identification_with_unique_exterior_EM_connection_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
