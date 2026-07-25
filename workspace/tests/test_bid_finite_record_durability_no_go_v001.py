import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_bid_finite_record_durability_no_go_v001.py"
RESULT = ROOT / "results" / "bid_finite_record_durability_no_go_v001.json"


def test_finite_bid_write_is_exactly_recurrent_not_durable():
    subprocess.run(["python3", str(SCRIPT)], check=True, cwd=ROOT)
    data = json.loads(RESULT.read_text(encoding="ascii"))

    assert data["target_values_used"] is False
    assert data["root_to_public_error"] < 1e-12
    assert data["public_to_root_error"] < 1e-12
    assert data["two_interval_recurrence_error"] < 1e-12
    assert data["pointer_commutator_norm"] > 1.0
    assert data["first_orthogonal_write_passed"] is True
    assert data["endpoint_is_nondemolition"] is False
    assert data["finite_closed_parent_establishes_durability"] is False
    assert data["complete_parent_action_derived"] is False
    assert data["alpha_computed"] is False
    assert data["proof_authorized"] is False
    assert data["status"] == "BLOCK_FINITE_BID_PARENT_IS_EXACTLY_RECURRENT"
