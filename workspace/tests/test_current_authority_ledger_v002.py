import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_ledger_v002.py"
RESULT = ROOT / "results" / "current_authority_ledger_v002.json"


def test_corrected_current_authority_ledger() -> None:
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
        == "PASS_CURRENT_AUTHORITY_V002_STABILIZER_ONLY_LOCALIZATION_OPEN_ALPHA_FALSE"
    )
    assert payload["pointwise_projective_stabilizer_derived"] is True
    assert payload["physical_comparison_connection_derived"] is False
    assert payload["coupling_evaluation_authorized"] is False
    assert payload["alpha_computed"] is False
    assert "alpha_computed=false" in completed.stdout
