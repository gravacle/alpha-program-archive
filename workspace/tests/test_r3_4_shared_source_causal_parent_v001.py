from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_shared_source_causal_parent_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_shared_source_causal_parent_v001.py"
RESULT = ROOT / "results" / "r3_4_shared_source_causal_parent_v001.json"


class SharedSourceCausalParentTest(unittest.TestCase):
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

    def test_public_moller_and_pointer_persistence(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(result["shared_source_causal_order_derived"])
        self.assertTrue(result["primitive_pointer_persistence_derived"])
        self.assertTrue(result["outgoing_public_record_Moller_endomorphism_derived"])
        self.assertLess(
            max(result["public_record_restriction_errors"].values()),
            1e-11,
        )

    def test_fail_closed_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertGreater(result["source_inclusive_state_restriction_change"], 1e-3)
        self.assertFalse(result["same_GNS_unitary_Moller_implementer_derived"])
        self.assertFalse(result["parent_selected_physical_in_state_derived"])
        self.assertFalse(result["complete_physical_durability_derived"])
        self.assertFalse(result["physical_spectral_measure_derived"])
        self.assertFalse(result["alpha_computed"])


if __name__ == "__main__":
    unittest.main()
