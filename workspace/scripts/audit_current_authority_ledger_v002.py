#!/usr/bin/env python3
"""Fail-closed audit of the corrected v003 authority ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V002.json"
RESULT = ROOT / "results" / "current_authority_ledger_v002.json"

EXPECTED = {
    "primitive_record_carrier": (
        "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE"
    ),
    "ordered_endpoint_projective_stabilizer": (
        "PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY_LOCAL_CONNECTION_OPEN_ALPHA_FALSE"
    ),
    "microscopic_exhaustion_scope": (
        "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE"
    ),
    "public_charged_action_nonselection": (
        "PASS_PUBLIC_ACTION_PREMISES_DO_NOT_SELECT_K_SCOPE_ONLY_ALPHA_FALSE"
    ),
}


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    loaded: dict[str, dict] = {}
    checks: dict[str, bool] = {}

    for name, relative_path in ledger["current_results"].items():
        path = ROOT / relative_path
        checks[f"{name}_result_exists"] = path.exists()
        if path.exists():
            loaded[name] = json.loads(path.read_text(encoding="utf-8"))
            checks[f"{name}_status_is_current"] = (
                loaded[name]["overall"] == EXPECTED[name]
            )

    stabilizer = loaded.get("ordered_endpoint_projective_stabilizer", {})
    state = ledger["execution_state"]
    checks.update(
        {
            "retired_local_connection_result_is_not_current": (
                "results/primitive_relative_phase_connection_v001.json"
                not in ledger["current_results"].values()
            ),
            "pointwise_stabilizer_is_the_only_promoted_phase_result": (
                stabilizer.get("endpoint_ray_stabilizer_derived") is True
                and stabilizer.get("physical_comparison_connection_derived")
                is False
            ),
            "ledger_localization_stays_open": (
                state["local_relative_frame_redundancy_derived"] is False
                and state["physical_comparison_connection_derived"] is False
            ),
            "ledger_coupling_gate_stays_closed": (
                state["complete_public_charged_action_unique"] is False
                and state["unique_finite_coincident_extension_derived"] is False
                and state["coupling_evaluation_authorized"] is False
                and state["alpha_computed"] is False
                and state["proof_authorized"] is False
            ),
        }
    )

    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_CURRENT_AUTHORITY_V002_STABILIZER_ONLY_LOCALIZATION_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_CURRENT_AUTHORITY_LEDGER_V002"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        **state,
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("physical_comparison_connection_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
