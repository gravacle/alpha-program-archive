from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_selected_record_write_matrix_only() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_primitive_reversible_record_write_v002.py"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    assert (
        "PASS_SELECTED_CONTROLLED_X_MATRIX_IDENTITIES_ONLY_PHYSICAL_CLAIMS_BLOCKED"
        in completed.stdout
    )

    result = json.loads(
        (
            ROOT / "results" / "primitive_reversible_record_write_v002.json"
        ).read_text(encoding="utf-8")
    )
    assert result["standard_principal_matrix_log_exists"] is False
    assert result["controlled_x_extension_unique"] is False
    assert result["durable_record_established"] is False
    assert result["candidate_is_active_Level_1_postulate"] is False
    assert result["alpha_computed"] is False
