#!/usr/bin/env python3
"""Seal and fail-closed audit for the new Level-1 record-action principle."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V001.md"
SEAL = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V001.seal.sha256"
AUTHORITY = ROOT / "results" / "current_authority_ledger_v002.json"
RESULT = ROOT / "results" / "fundamental_boundary_record_action_principle_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))
    sealed_hash, sealed_name = SEAL.read_text(encoding="utf-8").split()

    required_true = (
        "fundamental_boundary_record_principle_adopted = true",
        "new_axiom_limits_claim_to_Level_1 = true",
    )
    required_false = (
        "unique_causal_record_cell_derived = false",
        "local_physical_comparison_connection_derived = false",
        "complete_charged_carrier_derived = false",
        "complete_parameter_free_Q_spec_frozen = false",
        "finite_c_F2_deformation_excluded = false",
        "unique_finite_response_derived = false",
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
        "corrected_pre_action_authority_is_current": (
            authority["overall"]
            == "PASS_CURRENT_AUTHORITY_V002_STABILIZER_ONLY_LOCALIZATION_OPEN_ALPHA_FALSE"
        ),
        "seal_names_the_principle": sealed_name == NOTE.name,
        "sealed_hash_matches": sealed_hash == sha256(NOTE),
        "new_axiom_is_disclosed": all(
            phrase in note for phrase in required_true
        ),
        "all_downstream_authorizations_fail_closed": all(
            phrase in note for phrase in required_false
        ),
        "zero_bare_clause_is_explicit": (
            "K_bare = 0." in note
            and "arbitrary finite `c`" in note
            and "this route fails to compute the coupling" in note
        ),
        "historical_blindness_is_not_claimed": (
            "Forward sealing cannot" in note
            and "create historical blindness" in note
        ),
        "target_literal_guard_passes": not any(
            pattern.search(note) for pattern in target_patterns
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_LEVEL1_RECORD_ACTION_PRINCIPLE_SEALED_EVALUATION_BLOCKED_ALPHA_FALSE"
        if not failed
        else "FAIL_FUNDAMENTAL_RECORD_ACTION_PRINCIPLE_SEAL_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "principle_sha256": sha256(NOTE),
        "fundamental_boundary_record_principle_adopted": True,
        "new_axiom_limits_claim_to_Level_1": True,
        "unique_causal_record_cell_derived": False,
        "local_physical_comparison_connection_derived": False,
        "complete_charged_carrier_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "finite_c_F2_deformation_excluded": False,
        "unique_finite_response_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "SEAL_AND_STATUS_GUARD_NOT_DYNAMICAL_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print(f"principle_sha256={sha256(NOTE)}")
    print("coupling_evaluation_authorized=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
