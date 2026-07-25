#!/usr/bin/env python3
"""Fail-closed bookkeeping audit for CURRENT_AUTHORITY_LEDGER_V008.

This checks that the new Level-1 adoption is not mislabeled as a theorem and
that coupling evaluation remains blocked.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "CURRENT_AUTHORITY_LEDGER_V008.json"


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    state = data["execution_state"]

    required_files = [
        *data["sealed_pre_alpha_authority"].values(),
        *data["current_derived_results"].values(),
        *data["current_level_1_postulates"].values(),
        *data["external_target_independent_route_audits"].keys(),
    ]
    missing = [name for name in required_files if not (ROOT / name).resolve().exists()]
    assert not missing, f"Missing authority inputs: {missing}"

    assert data["schema_version"] == 8
    assert state["transport_only_phase_complete_principle_adopted"] is True
    assert state["transport_only_phase_complete_principle_is_derived_theorem"] is False
    assert state["primitive_F_dependent_identity_phase_allowed"] is False
    assert state["primitive_Pauli_vertex_allowed"] is False
    assert state["primitive_dissipative_rate_allowed"] is False
    assert state["complete_parent_action_uniquely_derived"] is False
    assert state["unique_causal_record_cell_derived"] is False
    assert state["record_generated_mass_derived"] is False
    assert state["finite_c_F2_deformation_excluded_inside_adopted_primitive_branch"] is True
    assert state["finite_c_F2_deformation_excluded_as_universal_theorem"] is False
    assert state["coupling_evaluation_authorized"] is False
    assert state["alpha_computed"] is False
    assert state["proof_authorized"] is False

    out = {
        "status": "PASS_AUTHORITY_V008_TRANSPORT_ONLY_ADOPTED_EVALUATION_BLOCKED",
        "missing_files": missing,
        "transport_only_principle_is_theorem": state[
            "transport_only_phase_complete_principle_is_derived_theorem"
        ],
        "alpha_computed": state["alpha_computed"],
        "proof_authorized": state["proof_authorized"],
        "scope": "bookkeeping_consistency_only",
    }
    result_path = ROOT / "results" / "current_authority_v008.json"
    result_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(out["status"])


if __name__ == "__main__":
    main()
