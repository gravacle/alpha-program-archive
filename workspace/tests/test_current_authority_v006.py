from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_current_authority_v006_fails_closed() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "audit_current_authority_v006.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_AUTHORITY_V006_FINITE_CELL_PROTOCOL_FROZEN_ALPHA_FALSE" in completed.stdout

    result = json.loads(
        (ROOT / "results" / "current_authority_v006.json").read_text(encoding="utf-8")
    )
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
    assert result["scope"] == "bookkeeping_consistency_only"
