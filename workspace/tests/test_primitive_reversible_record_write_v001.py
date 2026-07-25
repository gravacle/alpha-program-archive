from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_primitive_reversible_record_write_matrix() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_primitive_reversible_record_write_v001.py"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_ADOPTED_CONTROLLED_RECORD_WRITE_MATRIX_ALPHA_FALSE" in completed.stdout

    result = json.loads(
        (
            ROOT / "results" / "primitive_reversible_record_write_v001.json"
        ).read_text(encoding="utf-8")
    )
    assert result["extension_derived_from_unitarity_alone"] is False
    assert result["field_history_control_projectors_derived"] is False
    assert result["alpha_computed"] is False
