from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_record_carrier_v001.py"
RESULT = ROOT / "results" / "primitive_record_carrier_v001.json"


class PrimitiveRecordCarrierTest(unittest.TestCase):
    def test_primitive_carrier_is_derived_without_promoting_complete_action(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        payload = json.loads(RESULT.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["overall"],
            "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE",
        )
        self.assertEqual(payload["failed_checks"], [])
        self.assertEqual(payload["primitive_single_handle_real_carrier_dimension"], 2)
        self.assertEqual(payload["primitive_single_handle_order_unit_dimension"], 4)
        self.assertEqual(payload["primitive_action_character_winding"], 1)
        self.assertIs(payload["primitive_comparator_kinematics_derived"], True)
        self.assertIs(payload["complete_g_A_psi_record_action_derived"], False)
        self.assertIs(payload["unique_UV_completion_selected"], False)
        self.assertIs(payload["candidate_action_evaluation_authorized"], False)
        self.assertIs(payload["alpha_computed"], False)


if __name__ == "__main__":
    unittest.main()
