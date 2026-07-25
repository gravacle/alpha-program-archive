from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_regulator_scheme_and_ray_sufficiency_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_regulator_scheme_and_ray_sufficiency_v001.py"
RESULT = ROOT / "results" / "r3_4_regulator_scheme_and_ray_sufficiency_v001.json"


class RegulatorSchemeAndRaySufficiencyTest(unittest.TestCase):
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

    def test_negative_statuses_are_explicit(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertFalse(
            result["all_three_full_measures_equivalent_up_to_energy_scale"]
        )
        self.assertFalse(
            result["covector_ray_and_quasilocal_state_fix_spectral_measure"]
        )
        self.assertFalse(result["unique_covariant_spectral_measure_derived"])
        self.assertFalse(result["alpha_computed"])

    def test_common_decay_is_retained_at_correct_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(result["all_three_share_t_minus_3_probability_class"])
        self.assertEqual(result["regulator_scheme_verdict"], "COMMON_DECAY_CLASS_ONLY")


if __name__ == "__main__":
    unittest.main()
