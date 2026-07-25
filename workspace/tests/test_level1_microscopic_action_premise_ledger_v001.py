from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts" / "audit_level1_microscopic_action_premise_ledger_v001.py"
RESULT = ROOT / "results" / "level1_microscopic_action_premise_ledger_v001.json"


class Level1MicroscopicActionPremiseLedgerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, str(AUDIT)], check=True, capture_output=True)

    def test_premises_are_bound_and_derivations_remain_open(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertEqual(result["premise_count"], 3)
        self.assertTrue(result["explicit_causal_falsifiers_present"])
        self.assertTrue(result["durability_remains_derivation_obligation"])
        self.assertFalse(result["coupling_evaluation_authorized"])
        self.assertFalse(result["alpha_computed"])
        self.assertEqual(
            result["status"],
            "PASS_LEVEL1_PREMISES_BOUND_DERIVATIONS_BLOCKED",
        )


if __name__ == "__main__":
    unittest.main()
