from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_primitive_binary_closure_generator_algebra() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_primitive_binary_closure_generator_v001.py"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_BINARY_CLOSURE_GENERATOR_ALGEBRA_ALPHA_FALSE" in completed.stdout

    result = json.loads(
        (
            ROOT / "results" / "primitive_binary_closure_generator_v001.json"
        ).read_text(encoding="utf-8")
    )
    assert result["source_mass_identified_with_record_gap"] is False
    assert result["alpha_computed"] is False
    assert result["scope"] == "two_state_algebra_only"
