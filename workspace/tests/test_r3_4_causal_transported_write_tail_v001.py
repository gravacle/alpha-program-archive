from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_causal_transported_write_tail_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_causal_transported_write_tail_v001.py"
RESULT = ROOT / "results" / "r3_4_causal_transported_write_tail_v001.json"


class CausalTransportedWriteTailTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True
        )

    def test_fail_closed_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_candidate_math_is_reproducible(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertLess(result["transport_covariance_error"], 1e-11)
        self.assertLess(result["finite_support_Moller_error"], 1e-11)
        self.assertAlmostEqual(
            result["transported_parent_first_pointer_probability"],
            1.0,
            places=12,
        )
        self.assertLess(result["static_sum_first_pointer_probability"], 0.99)

    def test_candidate_is_not_physical_derivation(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertFalse(
            result["causal_transport_rule_derived_from_pinned_principles"]
        )
        self.assertFalse(result["static_sum_rejected_by_adopted_principles"])
        self.assertFalse(result["physical_write_tail_join_derived"])
        self.assertFalse(
            result["free_outgoing_tail_generator_inherited_from_same_parent"]
        )
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
