import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_fundamental_boundary_record_action_principle_v001.py"
RESULT = ROOT / "results" / "fundamental_boundary_record_action_principle_v001.json"


def test_record_action_principle_is_sealed_and_fail_closed() -> None:
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    assert (
        payload["overall"]
        == "PASS_LEVEL1_RECORD_ACTION_PRINCIPLE_SEALED_EVALUATION_BLOCKED_ALPHA_FALSE"
    )
    assert payload["fundamental_boundary_record_principle_adopted"] is True
    assert payload["complete_parameter_free_Q_spec_frozen"] is False
    assert payload["finite_c_F2_deformation_excluded"] is False
    assert payload["coupling_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
