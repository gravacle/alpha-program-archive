from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_current_authority_v009_rejects_premature_promotions() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "audit_current_authority_v009.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert (
        "PASS_AUTHORITY_V009_PREMATURE_GENERATOR_PROMOTIONS_REJECTED"
        in completed.stdout
    )

    result = json.loads(
        (ROOT / "results" / "current_authority_v009.json").read_text(encoding="utf-8")
    )
    assert result["durable_record_generator_derived"] is False
    assert result["record_generated_source_mass_derived"] is False
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
