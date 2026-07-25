import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_stage7_condition_implementation_v001.py"
RESULT = ROOT / "results" / "stage7_condition_implementation_v001.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_stage7_conditions_are_implemented_without_alpha_authorization():
    module = load_module("stage7_condition_implementation", SCRIPT)
    module.main()
    result = json.loads(RESULT.read_text())
    assert result["construction_lane_gate_not_independent_review"] is True
    assert result["all_checks_pass"] is True
    assert all(result["checks"].values())
    assert result["stage8_theorem_battery_authored"] is False
    assert result["stage8_cross_execution_completed"] is False
    assert result["complete_parameter_free_Q_spec_frozen"] is False
    assert result["physical_Thomson_stiffness_computed"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
    assert result["verdict"] == (
        "STAGE7_CONDITIONS_C1_C7_IMPLEMENTED_STAGE8_HANDOFF_READY"
    )
