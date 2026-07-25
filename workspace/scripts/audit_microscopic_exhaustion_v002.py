#!/usr/bin/env python3
"""Audit the hostile-review correction to the v001 exhaustion gate."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "MICROSCOPIC_EXHAUSTION_IDENTIFIABILITY_GATE_V002.md"
V001_RESULT = ROOT / "results" / "microscopic_exhaustion_v001.json"
SEAL = ROOT / "PREREGISTRATION_V003.seal.sha256"
RESULT = ROOT / "results" / "microscopic_exhaustion_v002.json"


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
    v001 = json.loads(V001_RESULT.read_text(encoding="utf-8"))

    required_findings = (
        "its Gaussian reduced response was not periodic",
        "reversibility was established for the enlarged unitary evolution",
        "separately recoverable microscopic modes required an enlarged",
        "arbitrary finite mode counts did not by themselves establish",
        "the script verified the Gaussian identity but did not construct",
    )
    missing_findings = [
        phrase for phrase in required_findings if phrase not in note
    ]
    required_status = (
        "v001_Gaussian_countermodel_proof_valid = false",
        "microscopic_nonentailment_theorem_proved = false",
        "microscopic_record_exhaustion_derived = false",
        "complete_g_A_psi_record_specification_derived = false",
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
        "sealed_v003_authority_unchanged": verify_seal(),
        "v001_attempt_is_preserved": (
            v001["overall"]
            == "PASS_CURRENT_PRE_ALPHA_PRINCIPLES_DO_NOT_DERIVE_MICROSCOPIC_EXHAUSTION_ALPHA_FALSE"
        ),
        "all_hostile_findings_are_recorded": not missing_findings,
        "v001_proof_claim_is_explicitly_retired": (
            "v001_Gaussian_family_is_proof_grade_countermodel = false"
            in note
        ),
        "corrected_scope_flags_fail_closed": not missing_status,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE"
        if not failed
        else "FAIL_MICROSCOPIC_EXHAUSTION_V002_CORRECTION_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "v001_Gaussian_countermodel_proof_valid": False,
        "microscopic_nonentailment_theorem_proved": False,
        "primitive_result_scope_stops_before_microscopic_exhaustion": True,
        "microscopic_record_exhaustion_derived": False,
        "complete_g_A_psi_record_specification_derived": False,
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
    print("v001_Gaussian_countermodel_proof_valid=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
