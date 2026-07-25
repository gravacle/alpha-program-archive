from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = (
    ROOT
    / "scripts"
    / "audit_r3_4_lorentzian_joint_endpoint_compatibility_v001.py"
)
VERIFIER = (
    ROOT
    / "scripts"
    / "verify_r3_4_lorentzian_joint_endpoint_compatibility_v001.py"
)
RESULT = (
    ROOT
    / "results"
    / "r3_4_lorentzian_joint_endpoint_compatibility_v001.json"
)


class LorentzianJointEndpointCompatibilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True
        )

    def test_independent_functional_calculus_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_exact_rest_normal_but_not_finite_packet(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertAlmostEqual(
            result["pointer_probabilities_at_T_R"]["0.0"], 1.0, places=12
        )
        self.assertLess(
            result["gaussian_wavepacket_pointer_probability_at_T_R"], 0.999
        )
        self.assertFalse(
            result["universal_exact_finite_wavepacket_write_derived"]
        )

    def test_fail_closed_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(result["thresholded_direct_limit_route_required"])
        self.assertFalse(result["physical_thresholded_durability_derived"])
        self.assertFalse(result["physical_in_state_selected"])
        self.assertFalse(result["complete_root_spectral_measure_derived"])
        self.assertFalse(result["coupling_evaluation_authorized"])
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
