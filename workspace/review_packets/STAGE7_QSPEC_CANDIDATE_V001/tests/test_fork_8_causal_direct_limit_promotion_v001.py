import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts" / "audit_fork_8_causal_direct_limit_promotion_v001.py"
CROSSCHECK = (
    ROOT / "scripts" / "crosscheck_fork_8_causal_direct_limit_promotion_v001.py"
)
PRIMARY_RESULT = (
    ROOT / "results" / "fork_8_causal_direct_limit_promotion_v001.json"
)
CROSSCHECK_RESULT = (
    ROOT
    / "results"
    / "fork_8_causal_direct_limit_promotion_crosscheck_v001.json"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_fork_8_primary_gate():
    module = load_module("fork_8_promotion_audit", AUDIT)
    module.main()
    result = json.loads(PRIMARY_RESULT.read_text())
    assert result["specification_seal_matches"] is True
    assert result["authority_hashes_match"] is True
    assert result["all_promotion_tests_pass"] is True
    assert all(result["promotion_tests"].values())
    assert result["fork_8_closed"] is True
    assert result["hypothesis_promoted_to_principle"] is True
    assert result["global_source_inclusive_state_limit_derived"] is False
    assert result["complete_parameter_free_Q_spec_frozen"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False


def test_fork_8_construction_lane_crosscheck():
    module = load_module("fork_8_promotion_crosscheck", CROSSCHECK)
    module.main()
    result = json.loads(CROSSCHECK_RESULT.read_text())
    assert result["review_independence"] == (
        "CONSTRUCTION_LANE_CROSSCHECK_NOT_INDEPENDENT_REVIEW"
    )
    assert result["crosscheck_pass"] is True
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
