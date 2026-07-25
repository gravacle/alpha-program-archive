import json
import math
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_bid_ctp_hamilton_jacobi_scale_bridge_v001.py"
RESULT = ROOT / "results" / "bid_ctp_hamilton_jacobi_scale_bridge_v001.json"


def test_hamilton_jacobi_energy_ambiguity_blocks_stage3():
    subprocess.run(["python3", str(SCRIPT)], check=True, cwd=ROOT)
    data = json.loads(RESULT.read_text(encoding="ascii"))

    assert data["target_values_used"] is False
    assert data["misner_sharp_action_coefficient"] == "1/4"
    assert data["brown_york_action_coefficient"] == "1/2"
    assert math.isclose(
        data["interval_ratio_misner_sharp_over_brown_york"],
        math.sqrt(2.0),
        rel_tol=0.0,
        abs_tol=1e-15,
    )
    assert data["energy_choice_changes_interval"] is True
    assert data["bare_null_diamond_action_normalization_unique"] is False
    assert data["reparametrized_null_diamond_action_scale_unique"] is False
    assert data["causal_diamond_action_selects_absolute_radius"] is False
    assert data["absolute_record_interval_derived"] is False
    assert data["alpha_computed"] is False
    assert data["proof_authorized"] is False
    assert data["status"] == "BLOCK_STAGE3_HAMILTON_JACOBI_ENERGY_NOT_SELECTED"
