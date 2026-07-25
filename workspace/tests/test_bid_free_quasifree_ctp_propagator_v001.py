import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_free_quasifree_ctp_subgate() -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_bid_free_quasifree_ctp_propagator_v001.py"),
        ],
        cwd=ROOT,
        check=True,
    )
    result = json.loads(
        (ROOT / "results" / "bid_free_quasifree_ctp_propagator_v001.json").read_text(
            encoding="utf-8"
        )
    )
    assert result["overall"] == "PASS_FREE_QUASIFREE_CTP_SUBGATE_DURABILITY_OPEN"
    assert result["max_ctp_identity_error"] < 3e-12
    assert result["max_free_equation_error"] < 3e-12
    assert result["max_unitarity_error"] < 3e-12
    assert result["edge_zero_mode_weight"] < 3e-12
    assert abs(result["edge_massive_mode_weight"] - 1.0) < 3e-12
    assert result["complete_free_quasifree_CTP_contour_derived"] is True
    assert result["physical_durability_derived"] is False
    assert result["alpha_computed"] is False
