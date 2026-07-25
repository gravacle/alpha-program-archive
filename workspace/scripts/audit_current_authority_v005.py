#!/usr/bin/env python3
"""Fail-closed authority audit after the complete one-cell CTP gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V005.json"
SEAL = ROOT / "CURRENT_AUTHORITY_LEDGER_V005.seal.sha256"
CTP_RESULT = ROOT / "results" / "complete_one_cell_ctp_kernel_v001.json"
RESULT = ROOT / "results" / "current_authority_v005.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    ctp = json.loads(CTP_RESULT.read_text(encoding="utf-8"))
    sealed_hash, sealed_name = SEAL.read_text(encoding="utf-8").split()
    state = ledger["execution_state"]

    checks = {
        "ledger_seal_matches": (
            sealed_name == LEDGER.name and sealed_hash == sha256(LEDGER)
        ),
        "ctp_kernel_audit_passed": (
            ctp["overall"]
            == "PASS_COMPLETE_CTP_KERNEL_FIDELITY_PARENT_ACTION_BLOCKED_ALPHA_FALSE"
        ),
        "fidelity_action_is_not_parent": (
            ledger["conditional_or_diagnostic_only"][
                "PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md"
            ]
            == "POSTSELECTED_DIAGONAL_WEIGHT_NOT_PARENT_CTP_ACTION"
            and ctp["fidelity_weight_is_parent_ctp_action"] is False
        ),
        "complete_parent_kernel_remains_open": (
            state["complete_dynamical_parent_kernel_frozen"] is False
        ),
        "all_coupling_gates_remain_closed": (
            state["complete_parameter_free_Q_spec_frozen"] is False
            and state["finite_c_F2_deformation_excluded"] is False
            and state["coupling_evaluation_authorized"] is False
            and state["alpha_computed"] is False
            and state["proof_authorized"] is False
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_CURRENT_AUTHORITY_V005_PARENT_KERNEL_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_CURRENT_AUTHORITY_V005"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "ledger_sha256": sha256(LEDGER),
        "complete_dynamical_parent_kernel_frozen": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "AUTHORITY_AND_FAIL_CLOSED_STATUS_GUARD",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("complete_dynamical_parent_kernel_frozen=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
