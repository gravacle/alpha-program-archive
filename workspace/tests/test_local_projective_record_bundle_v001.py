import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_local_projective_record_bundle_v001.py"
RESULT = ROOT / "results" / "local_projective_record_bundle_v001.json"


def test_level1_local_projective_record_bundle() -> None:
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
        == "PASS_LEVEL1_LOCAL_RECORD_BUNDLE_AUXILIARY_CONNECTION_ONLY_ALPHA_FALSE"
    )
    assert payload["local_projective_record_bundle_derived"] is True
    assert payload["auxiliary_covariant_comparison_connection_derived"] is True
    assert payload["dynamical_public_connection_derived"] is False
    assert payload["unique_induced_Maxwell_stiffness_derived"] is False
    assert payload["coupling_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
