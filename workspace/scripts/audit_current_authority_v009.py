#!/usr/bin/env python3
"""Fail-closed bookkeeping audit for CURRENT_AUTHORITY_LEDGER_V009."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V009.json"


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    state = data["execution_state"]

    required_files = [
        *data["sealed_pre_alpha_authority"].values(),
        *data["current_derived_results"].values(),
        *data["current_level_1_postulates"].values(),
        *data["external_target_independent_route_audits"].keys(),
        *data["conditional_or_diagnostic_only"].keys(),
    ]
    missing = [name for name in required_files if not (ROOT / name).resolve().exists()]
    assert not missing, f"Missing authority inputs: {missing}"

    assert data["schema_version"] == 9
    assert state["binary_gap_interval_relation_is_conditional"] is True
    assert state["physical_binary_record_generator_derived"] is False
    assert state["controlled_x_write_candidate_unique"] is False
    assert state["durable_record_generator_derived"] is False
    assert state["record_generated_source_mass_derived"] is False
    assert state["complete_parent_action_uniquely_derived"] is False
    assert state["finite_flux_response_evaluated"] is False
    assert state["coupling_evaluation_authorized"] is False
    assert state["alpha_computed"] is False
    assert state["proof_authorized"] is False

    out = {
        "status": "PASS_AUTHORITY_V009_PREMATURE_GENERATOR_PROMOTIONS_REJECTED",
        "missing_files": missing,
        "durable_record_generator_derived": state["durable_record_generator_derived"],
        "record_generated_source_mass_derived": state[
            "record_generated_source_mass_derived"
        ],
        "alpha_computed": state["alpha_computed"],
        "proof_authorized": state["proof_authorized"],
        "scope": "bookkeeping_consistency_only",
    }
    result_path = ROOT / "results" / "current_authority_v009.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
