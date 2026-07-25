from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_parent_to_outgoing_gns_compatibility_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_parent_to_outgoing_gns_compatibility_v001.py"
RESULT = ROOT / "results" / "r3_4_parent_to_outgoing_gns_compatibility_v001.json"


class ParentToOutgoingGNSCompatibilityTest(unittest.TestCase):
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

    def test_static_parent_negative_control(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertFalse(result["static_parent_preserves_completed_public_label"])
        self.assertEqual(
            result["static_parent_verdict"],
            "STATIC_PARENT_LABEL_NOT_INVARIANT",
        )

    def test_no_parent_or_alpha_promotion(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertEqual(result["primary_verdict"], "PARENT_LIMIT_UNDERDETERMINED")
        self.assertFalse(result["parent_to_outgoing_limit_derived"])
        self.assertFalse(result["hypothesis_promoted_to_principle"])
        self.assertFalse(result["alpha_computed"])


if __name__ == "__main__":
    unittest.main()
