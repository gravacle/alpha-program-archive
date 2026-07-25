from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "scripts" / "audit_r3_4_lorentzian_threshold_return_v001.py"
VERIFIER = ROOT / "scripts" / "verify_r3_4_lorentzian_threshold_return_v001.py"
RESULT = ROOT / "results" / "r3_4_lorentzian_threshold_return_v001.json"


class LorentzianThresholdReturnTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True
        )

    def test_independent_quadrature_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_operator_theorem(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(result["nonflat_band_spectrum_derived"])
        self.assertTrue(
            result["L2_root_spectral_measure_absolutely_continuous"]
        )
        self.assertTrue(result["L2_root_spectral_density_integrable"])
        self.assertTrue(
            result["Riemann_Lebesgue_threshold_return_derived_for_this_H"]
        )
        self.assertTrue(result["point_momentum_root_excluded_from_L2_theorem"])

    def test_fail_closed_physical_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertFalse(result["complete_outgoing_generator_identified"])
        self.assertFalse(result["parent_selected_physical_root_derived"])
        self.assertFalse(result["finite_energy_physical_root_derived"])
        self.assertFalse(result["positive_frequency_state_derived_from_parent"])
        self.assertFalse(result["generated_descendant_spectrum_exhausted"])
        self.assertFalse(result["complete_write_defect_bound_states_excluded"])
        self.assertFalse(result["complete_physical_durability_derived"])
        self.assertFalse(result["coupling_evaluation_authorized"])
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
