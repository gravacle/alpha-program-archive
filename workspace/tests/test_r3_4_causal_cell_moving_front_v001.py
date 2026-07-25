from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_causal_cell_moving_front_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_causal_cell_moving_front_v001.py"
RESULT = ROOT / "results" / "r3_4_causal_cell_moving_front_v001.json"


class CausalCellMovingFrontTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, str(PRODUCER)], check=True, capture_output=True)

    def test_independent_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_profile_and_order_independence(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertLess(max(result["profile_endpoint_errors"].values()), 1e-12)
        self.assertLess(
            max(result["distinct_cell_generator_commutators"].values()),
            1e-13,
        )
        self.assertLess(result["causal_linear_extension_ordering_error"], 1e-12)

    def test_conditional_boundary_retained(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertEqual(
            result["status"],
            "MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_CONDITIONAL",
        )
        self.assertFalse(result["moving_front_bound_by_live_complete_parent"])
        self.assertFalse(result["full_parent_state_covariance_derived"])
        self.assertFalse(result["alpha_computed"])


if __name__ == "__main__":
    unittest.main()
