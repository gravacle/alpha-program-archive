import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_stage6_parent_action_ledger_v002.py"
RESULT = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_stage7_conditions_land_without_downstream_authorization():
    module = load_module("stage6_parent_action_ledger_v002", SCRIPT)
    module.main()
    result = json.loads(RESULT.read_text())

    assert result["specification_seal_matches"] is True
    assert result["authority_hashes_match"] is True
    assert result["successor_seals_match"] is True
    assert all(result["derived_parent_and_durability"].values())
    assert all(result["stage7_review_conditions"].values())
    assert result["stage7_independent_reviews_completed"] is True
    assert result["stage7_review_conditions_landed"] is True
    assert result["stage8_cross_execution_ready"] is True
    assert result["stage8_cross_execution_completed"] is False

    assert result["explicitly_not_derived"][
        "spacetime_concurrent_exact_record_compatibility"
    ] is False
    assert result["explicitly_not_derived"][
        "source_inclusive_state_projective_limit"
    ] is False
    assert result["qspec_component_status"]["in_state"] == (
        "DISCLOSED_STATIONARY_QUASIFREE_BRANCH_STATE"
    )
    assert result["qspec_component_status"]["CTP_contour"] == (
        "FREE_CONTOUR_DERIVED_FROM_DISCLOSED_STATE_INTERACTING_OPEN"
    )
    assert len(result["adopted_microscopic_principles"]) == 6
    assert len(result["EM_dependency_order"]) == 9

    assert result["complete_source_inclusive_parent_limit_derived"] is False
    assert result["complete_parameter_free_Q_spec_frozen"] is False
    assert result["physical_Thomson_stiffness_computed"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
    assert result["verdict"] == (
        "STAGE7_CONDITIONS_LANDED_STAGE8_CROSS_EXECUTION_READY"
    )
