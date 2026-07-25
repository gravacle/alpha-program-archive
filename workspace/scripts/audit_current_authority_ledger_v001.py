#!/usr/bin/env python3
"""Verify that current alpha-clean-room authority excludes retired results."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V001.json"
RESULT = ROOT / "results" / "current_authority_ledger_v001.json"


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    current_paths = list(ledger["current_results"].values())
    superseded_paths = list(ledger["superseded_results"])

    current_payloads = {
        path: json.loads((ROOT / path).read_text(encoding="utf-8"))
        for path in current_paths
    }
    checks = {
        "all_current_results_exist": all(
            (ROOT / path).exists() for path in current_paths
        ),
        "all_superseded_results_exist_for_audit_trail": all(
            (ROOT / path).exists() for path in superseded_paths
        ),
        "no_superseded_result_is_current": not (
            set(current_paths) & set(superseded_paths)
        ),
        "microscopic_scope_uses_corrected_v002": (
            current_payloads[
                "results/microscopic_exhaustion_v002.json"
            ]["overall"]
            == "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE"
        ),
        "public_action_uses_qualified_v002": (
            current_payloads[
                "results/public_charged_action_uniqueness_v002.json"
            ]["overall"]
            == "PASS_PUBLIC_ACTION_PREMISES_DO_NOT_SELECT_K_SCOPE_ONLY_ALPHA_FALSE"
        ),
        "all_current_results_keep_alpha_false": all(
            payload.get("alpha_computed") is False
            for payload in current_payloads.values()
        ),
        "ledger_keeps_proof_authorization_false": (
            ledger["execution_state"]["proof_authorized"] is False
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_CURRENT_AUTHORITY_EXCLUDES_RETIRED_RESULTS_ALPHA_FALSE"
        if not failed
        else "FAIL_CURRENT_AUTHORITY_LEDGER"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "current_results": current_paths,
        "superseded_results": superseded_paths,
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
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
