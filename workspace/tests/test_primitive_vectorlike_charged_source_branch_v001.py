import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_vectorlike_charged_source_branch_v001.py"
RESULT = ROOT / "results" / "primitive_vectorlike_charged_source_branch_v001.json"


def test_primitive_vectorlike_source_branch_is_sealed() -> None:
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
        == "PASS_PRIMITIVE_VECTORLIKE_SOURCE_BRANCH_SEALED_QSPEC_OPEN_ALPHA_FALSE"
    )
    assert payload["primitive_charge_magnitude"] == 1
    assert payload["primitive_vectorlike_pair_count"] == 1
    assert payload["cubic_U1_anomaly"] == 0
    assert payload["mixed_gravity_U1_anomaly"] == 0
    assert payload["universal_matter_spectrum_derived"] is False
    assert payload["charged_determinant_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
