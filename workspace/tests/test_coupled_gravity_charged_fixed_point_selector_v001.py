import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_coupled_gravity_charged_fixed_point_selector_v001.py"
RESULT = ROOT / "results" / "coupled_gravity_charged_fixed_point_selector_v001.json"


def test_coupled_fixed_point_selector_stays_fail_closed() -> None:
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
        == "PASS_FIXED_POINT_SELECTOR_FORM_INPUTS_UNDERIVED_ALPHA_FALSE"
    )
    assert payload["coupled_fixed_point_is_valid_selector_form"] is True
    assert payload["f_grav_derived"] is False
    assert payload["b_ch_derived"] is False
    assert payload["fixed_point_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
