from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_current_authority_v008_fails_closed() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "audit_current_authority_v008.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert (
        "PASS_AUTHORITY_V008_TRANSPORT_ONLY_ADOPTED_EVALUATION_BLOCKED"
        in completed.stdout
    )

    result = json.loads(
        (ROOT / "results" / "current_authority_v008.json").read_text(encoding="utf-8")
    )
    assert result["transport_only_principle_is_theorem"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
