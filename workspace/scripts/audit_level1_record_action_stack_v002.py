#!/usr/bin/env python3
"""Seal/status guard for the corrected Level-1 record-action stack.

This audit checks provenance, forbidden target literals, and fail-closed
authorization. It does not certify the adopted physical premises.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRINCIPLE = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md"
PRINCIPLE_SEAL = ROOT / (
    "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.seal.sha256"
)
ACTION = ROOT / "PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md"
ACTION_SEAL = ROOT / (
    "PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.seal.sha256"
)
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V003.json"
LEDGER_SEAL = ROOT / "CURRENT_AUTHORITY_LEDGER_V003.seal.sha256"
RESULT = ROOT / "results" / "level1_record_action_stack_v002.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_seal(path: Path) -> tuple[str, str]:
    digest, name = path.read_text(encoding="utf-8").split()
    return digest, name


def main() -> None:
    principle = PRINCIPLE.read_text(encoding="utf-8")
    action = ACTION.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

    principle_digest, principle_name = read_seal(PRINCIPLE_SEAL)
    action_digest, action_name = read_seal(ACTION_SEAL)
    ledger_digest, ledger_name = read_seal(LEDGER_SEAL)

    target_patterns = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    combined = principle + "\n" + action

    checks = {
        "principle_seal_matches": (
            principle_name == PRINCIPLE.name
            and principle_digest == sha256(PRINCIPLE)
        ),
        "action_seal_matches": (
            action_name == ACTION.name and action_digest == sha256(ACTION)
        ),
        "ledger_seal_matches": (
            ledger_name == LEDGER.name and ledger_digest == sha256(LEDGER)
        ),
        "lift_U1_is_not_charged_U1": (
            "common_ray_lift_U1_identified_with_charged_U1 = false"
            in principle
        ),
        "connection_is_disclosed_as_adopted": (
            "auxiliary_compact_connection_adopted = true" in principle
            and "charged_connection_status = adopted_Level_1_field_content"
            in action
        ),
        "physical_EM_connection_is_not_claimed": (
            "physical_public_EM_connection_derived = false" in principle
            and ledger["execution_state"][
                "physical_public_EM_connection_derived"
            ]
            is False
        ),
        "record_weight_is_disclosed_as_postulate": (
            "This is a new action postulate." in action
            and "one_cell_weight_postulate = Born_reference_fidelity"
            in action
        ),
        "no_expansion_was_evaluated": (
            "No numerical expansion coefficient is evaluated in this file."
            in action
        ),
        "finite_counterterm_gate_is_open": (
            ledger["execution_state"]["finite_c_F2_deformation_excluded"]
            is False
            and "finite_c_F2_deformation_excluded = false" in action
        ),
        "all_evaluation_gates_are_closed": (
            ledger["execution_state"]["coupling_evaluation_authorized"]
            is False
            and ledger["execution_state"]["alpha_computed"] is False
            and ledger["execution_state"]["proof_authorized"] is False
            and "coupling_evaluation_authorized = false" in action
            and "alpha_computed = false" in action
            and "proof_authorized = false" in action
        ),
        "target_literal_guard_passes": not any(
            pattern.search(combined) for pattern in target_patterns
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_LEVEL1_ACTION_STACK_SEALED_EVALUATION_BLOCKED_ALPHA_FALSE"
        if not failed
        else "FAIL_LEVEL1_ACTION_STACK_V002"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "principle_sha256": sha256(PRINCIPLE),
        "action_sha256": sha256(ACTION),
        "ledger_sha256": sha256(LEDGER),
        "connection_status": "ADOPTED_LEVEL_1_NOT_DERIVED",
        "one_cell_action_status": "FROZEN_CANDIDATE_NOT_EVALUATED",
        "finite_c_F2_deformation_excluded": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "SEAL_AND_STATUS_GUARD_NOT_PHYSICAL_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("connection_status=ADOPTED_LEVEL_1_NOT_DERIVED")
    print("coupling_evaluation_authorized=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
