#!/usr/bin/env python3
"""Audit the Stage-1 premise dispositions without evaluating alpha."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUT = ROOT / "results" / "stage1_premise_disposition_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_text(path: Path, needles: tuple[str, ...]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise AssertionError(f"{path.name}: missing required text {needle!r}")


def main() -> None:
    provenance_path = ROOT / "provenance_inputs_v003.json"
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    provenance_checks = []
    for item in provenance["inputs"]:
        source = (ROOT / item["path"]).resolve()
        actual = sha256(source)
        if actual != item["sha256"]:
            raise AssertionError(f"provenance drift: {source}")
        provenance_checks.append(
            {"path": str(source), "sha256": actual, "status": "PASS"}
        )

    required_files = (
        ROOT / "SOURCE_RECORD_MASS_TRANSFER_GATE_V001.md",
        ROOT / "COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md",
        ROOT / "scripts" / "audit_primitive_source_record_chiral_operator_v002.py",
    )
    for path in required_files:
        if not path.is_file():
            raise AssertionError(f"missing premise dependency: {path}")

    require_text(
        ROOT / "PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md",
        ("effective_projective_stabilizer = U(1)", "chi_n(theta) = exp(i n theta)"),
    )
    require_text(
        ROOT / "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md",
        (
            "primitive_fundamental_vectorlike_pairs = 1",
            "Additional vectorlike pairs are consistent and are not proved impossible.",
        ),
    )
    require_text(
        ROOT / "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md",
        (
            "It cannot be the complete parent action of a closed unitary record theory.",
            "fidelity_weight_is_complete_parent_CTP_action = false",
        ),
    )
    require_text(
        ROOT / "STAGE1_PREMISE_DISPOSITION_V001.md",
        (
            "stage1_hidden_premise_ledger_closed = true",
            "historical_target_blindness_established = false",
            "alpha_computed = false",
        ),
    )

    # Continuous characters of U(1) are indexed by n in Z. The finite checks
    # below are regression witnesses for the analytic kernel classification
    # stated in the disposition; they are not offered as its proof.
    character_witnesses = []
    for n in range(-8, 9):
        faithful = abs(n) == 1
        kernel_order = None if n == 0 else abs(n)
        character_witnesses.append(
            {
                "n": n,
                "faithful": faithful,
                "kernel_order": kernel_order,
            }
        )

    result = {
        "schema_version": 1,
        "overall": "PASS_EXPLICIT_PREMISE_CLASSIFICATION_TARGET_AWARE",
        "premise_classification_closed": True,
        "historical_target_blindness_established": False,
        "unused_prediction_required": True,
        "primitive_unit_winding_status": "DERIVED_GIVEN_FAITHFUL_U1_CHARACTER",
        "primitive_vectorlike_pair_count_status": "DISCLOSED_BRANCH_INPUT",
        "fidelity_action_status": "RETIRED_FROM_LOAD_BEARING_ALPHA_PATH",
        "complete_source_spectrum_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "unique_causal_record_cell_derived": False,
        "physical_Thomson_stiffness_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "provenance_checks": provenance_checks,
        "required_files": [str(path) for path in required_files],
        "character_regression_witnesses": character_witnesses,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    print(result["overall"])


if __name__ == "__main__":
    main()
