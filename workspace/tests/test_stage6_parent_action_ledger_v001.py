import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_stage6_parent_action_ledger_v001.py"
RESULT = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V001.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_stage6_ledger_is_least_favorable_and_review_ready():
    module = load_module("stage6_parent_action_ledger", SCRIPT)
    module.main()
    result = json.loads(RESULT.read_text())
    assert result["specification_seal_matches"] is True
    assert result["authority_hashes_match"] is True
    assert all(result["derived_parent_and_durability"].values())
    assert result["historical_target_blindness_established"] is False
    assert result["stage6_ledger_frozen"] is True
    assert result["stage7_qspec_review_candidate_assembly_authorized"] is True
    assert result["complete_source_inclusive_parent_limit_derived"] is False
    assert result["complete_parameter_free_Q_spec_frozen"] is False
    assert result["physical_Thomson_stiffness_computed"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
    assert result["verdict"] == (
        "STAGE6_LEDGER_FROZEN_STAGE7_REVIEW_CANDIDATE_AUTHORIZED"
    )
