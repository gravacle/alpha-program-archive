#!/usr/bin/env python3
"""Resolve and hash every v003 provenance input under the sealed v002 policy."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
NOTE = ROOT / "PREREGISTRATION_V003.md"
CONTRACT = ROOT / "contract_v003.json"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
V002_NOTE = ROOT.parent / "alpha_fundamental_record_action_cleanroom_v002" / "PREREGISTRATION_V002.md"
V002_CONTRACT = ROOT.parent / "alpha_fundamental_record_action_cleanroom_v002" / "contract_v002.json"
RESULT = ROOT / "results" / "preregistration_v003_audit.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    state = contract["execution_state"]

    source_rows = []
    for item in provenance["inputs"]:
        path = (ROOT / item["path"]).resolve()
        exists = path.is_file()
        actual = sha256(path) if exists else None
        source_rows.append(
            {
                "declared_path": item["path"],
                "resolved_path": str(path),
                "exists": exists,
                "declared_sha256": item["sha256"],
                "actual_sha256": actual,
                "matches": exists and actual == item["sha256"],
            }
        )

    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    scanned = note + CONTRACT.read_text(encoding="utf-8") + PROVENANCE.read_text(
        encoding="utf-8"
    )
    target_hits = [pattern.pattern for pattern in forbidden if pattern.search(scanned)]

    blocked_flags = (
        "candidate_action_evaluation_authorized",
        "complete_quantum_specification_frozen",
        "unique_action_or_specification_derived",
        "unique_finite_coincident_extension_derived",
        "full_operator_closure_derived",
        "numerical_root_finding_authorized",
        "coupling_evaluation_authorized",
        "coupling_computed",
        "alpha_computed",
        "proof_authorized",
    )
    bad_flags = [key for key in blocked_flags if state.get(key) is not False]
    checks = {
        "sealed_v002_preregistration_hash_matches": (
            sha256(V002_NOTE) == contract["imported_v002_preregistration_sha256"]
        ),
        "sealed_v002_contract_hash_matches": (
            sha256(V002_CONTRACT) == contract["imported_v002_contract_sha256"]
        ),
        "every_pre_alpha_source_resolves_and_matches_hash": all(
            row["matches"] for row in source_rows
        ),
        "only_symbolic_work_is_authorized": (
            state["symbolic_model_space_derivation_authorized"] is True
            and not bad_flags
        ),
        "claim_ceiling_remains_level_1": (
            provenance["current_claim_ceiling"] == "LEVEL_1"
            and contract["new_axiom_currently_limits_claim_to_level_1"] is True
        ),
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_V003_RESOLVED_PROVENANCE_SYMBOLIC_ONLY_ALPHA_FALSE"
        if not failed
        else "FAIL_V003_PROVENANCE_AUTHORITY"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "source_resolution": source_rows,
        "bad_execution_flags": bad_flags,
        "target_literal_hits": target_hits,
        "all_pre_alpha_source_paths_resolved_and_hash_checked": (
            all(row["matches"] for row in source_rows)
        ),
        "symbolic_model_space_derivation_authorized": True,
        "candidate_action_evaluation_authorized": False,
        "current_claim_ceiling": "LEVEL_1",
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(overall)
    print(
        "all_pre_alpha_source_paths_resolved_and_hash_checked="
        + str(payload["all_pre_alpha_source_paths_resolved_and_hash_checked"]).lower()
    )
    print("candidate_action_evaluation_authorized=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

