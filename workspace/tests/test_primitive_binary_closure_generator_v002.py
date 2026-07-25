from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_conditional_binary_orthogonalization_only() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_primitive_binary_closure_generator_v002.py"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_CONDITIONAL_BALANCED_ORTHOGONALIZATION_ALGEBRA" in completed.stdout

    result = json.loads(
        (
            ROOT / "results" / "primitive_binary_closure_generator_v002.json"
        ).read_text(encoding="utf-8")
    )
    assert result["balanced_calibration_derived"] is False
    assert result["durable_record_condition_established"] is False
    assert result["physical_record_generator_derived"] is False
    assert result["alpha_computed"] is False
