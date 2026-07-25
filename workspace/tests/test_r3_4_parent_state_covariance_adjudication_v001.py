from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = (
    ROOT / "scripts" / "audit_r3_4_parent_state_covariance_adjudication_v001.py"
)
VERIFIER = (
    ROOT / "scripts" / "verify_r3_4_parent_state_covariance_adjudication_v001.py"
)
RESULT = ROOT / "results" / "r3_4_parent_state_covariance_adjudication_v001.json"


class ParentStateCovarianceAdjudicationTest(unittest.TestCase):
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

    def test_current_parent_is_blocked(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertEqual(
            result["status"],
            "PARENT_STATE_COVARIANCE_CURRENT_PARENT_BLOCKED",
        )
        self.assertFalse(result["live_parent_complete_under_principle"])
        self.assertFalse(result["alpha_computed"])

    def test_covariance_does_not_select_action(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        control = result["covariance_nonuniqueness_negative_control"]
        self.assertLess(control["minimal_net_interior_derivation_error"], 1e-13)
        self.assertLess(control["interacting_net_interior_derivation_error"], 1e-13)
        self.assertTrue(control["two_covariant_parent_responses_differ"])
        self.assertFalse(
            result["parent_state_covariance_alone_selects_unique_parent"]
        )


if __name__ == "__main__":
    unittest.main()
