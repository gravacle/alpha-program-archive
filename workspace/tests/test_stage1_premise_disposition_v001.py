import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_stage1_premise_disposition() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "audit_stage1_premise_disposition_v001.py")],
        check=True,
        cwd=ROOT,
    )
    result = json.loads(
        (ROOT / "results" / "stage1_premise_disposition_v001.json").read_text(
            encoding="utf-8"
        )
    )
    assert result["overall"] == "PASS_EXPLICIT_PREMISE_CLASSIFICATION_TARGET_AWARE"
    assert result["premise_classification_closed"] is True
    assert result["historical_target_blindness_established"] is False
    assert result["unused_prediction_required"] is True
    assert result["primitive_unit_winding_status"].startswith("DERIVED_")
    assert result["primitive_vectorlike_pair_count_status"] == "DISCLOSED_BRANCH_INPUT"
    assert result["fidelity_action_status"] == "RETIRED_FROM_LOAD_BEARING_ALPHA_PATH"
    assert result["complete_source_spectrum_derived"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False


def test_only_unit_winding_is_faithful_in_regression_window() -> None:
    result = json.loads(
        (ROOT / "results" / "stage1_premise_disposition_v001.json").read_text(
            encoding="utf-8"
        )
    )
    faithful = [row["n"] for row in result["character_regression_witnesses"] if row["faithful"]]
    assert faithful == [-1, 1]
