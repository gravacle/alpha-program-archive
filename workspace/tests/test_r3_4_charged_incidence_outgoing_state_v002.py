from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = (
    ROOT / "scripts" / "audit_r3_4_charged_incidence_outgoing_state_v002.py"
)
VERIFIER = (
    ROOT / "scripts" / "verify_r3_4_charged_incidence_outgoing_state_v002.py"
)
RESULT = ROOT / "results" / "r3_4_charged_incidence_outgoing_state_v002.json"


class ChargedIncidenceOutgoingStateTest(unittest.TestCase):
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

    def test_endpoint_and_state_lift(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertLess(result["active_endpoint_unitary_swap_error"], 1e-12)
        self.assertLess(
            max(result["finite_state_restriction_errors"].values()),
            1e-12,
        )
        self.assertTrue(
            result["charge_superselected_quasilocal_state_lift_derived"]
        )

    def test_no_durability_or_alpha_promotion(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(
            result["stationary_infinite_endpoint_product_GNS_implementation_fails"]
        )
        self.assertFalse(result["complete_continuous_parent_covariance_derived"])
        self.assertFalse(result["complete_parent_action_derived"])
        self.assertFalse(result["alpha_computed"])


if __name__ == "__main__":
    unittest.main()
