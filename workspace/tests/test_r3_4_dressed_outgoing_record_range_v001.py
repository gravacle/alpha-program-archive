from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_dressed_outgoing_record_range_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_dressed_outgoing_record_range_v001.py"
RESULT = ROOT / "results" / "r3_4_dressed_outgoing_record_range_v001.json"


class DressedOutgoingRecordRangeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True
        )

    def test_closed_form_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_range_correction(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertGreater(result["maximum_record_only_range_distance"], 1e-3)
        self.assertGreater(
            result["pointer_image_source_commutator_norm"], 1e-3
        )
        self.assertFalse(result["bare_record_endomorphism_derived"])
        self.assertTrue(result["stable_dressed_record_monomorphism_derived"])
        self.assertTrue(
            result["dressed_output_record_algebra_embedded_in_full_parent"]
        )

    def test_algebra_and_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertLess(result["maximum_image_stabilization_error"], 1e-11)
        self.assertLess(result["maximum_star_preservation_error"], 1e-11)
        self.assertLess(result["maximum_multiplication_error"], 1e-11)
        self.assertLess(result["unitality_error"], 1e-11)
        self.assertLess(result["maximum_norm_preservation_error"], 1e-11)
        self.assertFalse(result["complete_parent_to_outgoing_GNS_map_derived"])
        self.assertFalse(result["generated_descendant_action_derived"])
        self.assertFalse(result["complete_physical_durability_derived"])
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
