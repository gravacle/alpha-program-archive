#!/usr/bin/env python3
"""Audit absolute charged-action uniqueness under the sealed pre-alpha rules."""

from __future__ import annotations

import hashlib
import json
import re
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PUBLIC_CHARGED_ACTION_UNIQUENESS_GATE_V001.md"
EXHAUSTION = ROOT / "results" / "microscopic_exhaustion_v002.json"
SEAL = ROOT / "PREREGISTRATION_V003.seal.sha256"
RESULT = ROOT / "results" / "public_charged_action_uniqueness_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal() -> bool:
    rows = SEAL.read_text(encoding="utf-8").splitlines()
    if not rows:
        return False
    for row in rows:
        expected, relative = row.split(maxsplit=1)
        sealed_path = (ROOT / relative.strip()).resolve()
        if not sealed_path.exists() or sha256(sealed_path) != expected:
            return False
    return True


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    exhaustion = json.loads(EXHAUSTION.read_text(encoding="utf-8"))

    stiffnesses = tuple(
        Decimal(value) for value in ("0.25", "0.5", "1", "2", "8", "32")
    )
    mutations = tuple(
        Decimal(value) for value in ("-0.125", "0", "0.125", "0.75")
    )
    with localcontext() as context:
        context.prec = 80
        pi = Decimal(
            "3.14159265358979323846264338327950288419716939937510"
        )
        response_values = [Decimal(1) / k for k in stiffnesses]
        coupling_values = [Decimal(1) / (4 * pi * k) for k in stiffnesses]
        shifted = [
            stiffness + mutation
            for stiffness in stiffnesses
            for mutation in mutations
            if stiffness + mutation > 0
        ]

    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [
        pattern.pattern for pattern in forbidden if pattern.search(note)
    ]
    required_status = (
        "absolute_Maxwell_stiffness_selected = false",
        "zero_bare_condition_removes_finite_local_mutation = false",
        "complete_public_charged_action_unique = false",
        "unique_finite_coincident_extension_derived = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    missing_status = [
        phrase for phrase in required_status if phrase not in note
    ]

    checks = {
        "sealed_v003_authority_unchanged": verify_seal(),
        "upstream_microscopic_exhaustion_correction_passes_fail_closed": (
            exhaustion["overall"]
            == "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE"
        ),
        "multiple_positive_stiffnesses_are_admissible": (
            len(stiffnesses) > 1 and all(k > 0 for k in stiffnesses)
        ),
        "admissible_stiffnesses_give_distinct_absolute_responses": (
            len(set(response_values)) == len(response_values)
        ),
        "admissible_stiffnesses_give_distinct_couplings": (
            len(set(coupling_values)) == len(coupling_values)
        ),
        "finite_local_mutations_leave_positive_survivors": (
            len(set(shifted)) > len(stiffnesses)
        ),
        "scope_flags_fail_closed": not missing_status,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_PRE_ALPHA_PRINCIPLES_DO_NOT_SELECT_ABSOLUTE_CHARGED_ACTION_ALPHA_FALSE"
        if not failed
        else "FAIL_PUBLIC_CHARGED_ACTION_UNIQUENESS_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "stiffnesses_tested": [str(value) for value in stiffnesses],
        "inverse_response_values": [
            str(value) for value in response_values
        ],
        "unit_character_coupling_values": [
            str(value) for value in coupling_values
        ],
        "finite_mutations_tested": [str(value) for value in mutations],
        "primitive_unit_character_holonomy_derived": True,
        "absolute_Maxwell_stiffness_selected": False,
        "zero_bare_condition_removes_finite_local_mutation": False,
        "complete_public_charged_action_unique": False,
        "unique_finite_coincident_extension_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("complete_public_charged_action_unique=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
