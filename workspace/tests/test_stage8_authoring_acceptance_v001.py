import contextlib
import importlib.util
import io
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify_stage8_authoring_acceptance_v001.py"
RESULT = ROOT / "results" / "stage8_authoring_acceptance_v001.json"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_stage8_authoring_is_accepted_without_cross_execution():
    module = load_module("stage8_authoring_acceptance", SCRIPT)
    with contextlib.redirect_stdout(io.StringIO()):
        module.main()
    result = json.loads(RESULT.read_text())

    assert all(result["checks"].values())
    assert result["embedded_authority_hashes_verified"] == 43
    assert result["stage8_theorem_battery_authored"] is True
    assert result["stage8_spec_sealed"] is True
    assert result["stage8_independent_evaluator_received"] is False
    assert result["stage8_test_harness_received"] is False
    assert result["stage8_cross_execution_authorized"] is False
    assert result["stage8_cross_execution_completed"] is False
    assert result["T0_first_cross_execution_obligation"] is True
    assert result["primitive_output_contract"] == "kappa_record only"
    assert result["primitive_output_not_physical_alpha"] is True
    assert result["BID_core_result_sealed"] is False
    assert result["spectral_evaluation_authorized"] is False
    assert result["complete_Q_spec_sealed"] is False
    assert result["physical_charged_amplitude_computed"] is False
    assert result["complete_parameter_free_Q_spec_frozen"] is False
    assert result["physical_Thomson_stiffness_computed"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
    assert result["verdict"] == (
        "STAGE8_SPEC_AUTHORED_SEALED_EVALUATOR_RELAY_PENDING"
    )
