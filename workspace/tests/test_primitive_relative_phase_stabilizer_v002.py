import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_relative_phase_stabilizer_v002.py"
RESULT = ROOT / "results" / "primitive_relative_phase_stabilizer_v002.json"


def test_corrected_relative_phase_stabilizer_gate() -> None:
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
        == "PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY_LOCAL_CONNECTION_OPEN_ALPHA_FALSE"
    )
    assert payload["endpoint_ray_stabilizer_derived"] is True
    assert payload["relative_lie_algebra_dimension"] == 1
    assert payload["physical_comparison_connection_derived"] is False
    assert payload["absolute_Maxwell_stiffness_selected"] is False
    assert payload["coupling_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
