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
    / "audit_r3_4_causal_shared_source_moller_durability_v001.py"
)
VERIFIER = (
    ROOT
    / "scripts"
    / "verify_r3_4_causal_shared_source_moller_durability_v001.py"
)
RESULT = (
    ROOT
    / "results"
    / "r3_4_causal_shared_source_moller_durability_v001.json"
)


class CausalSharedSourceMollerDurabilityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(PRODUCER)], check=True, capture_output=True
        )

    def test_independent_state_vector_verifier(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VERIFIER)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS", completed.stdout)

    def test_primitive_outgoing_result(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertTrue(result["primitive_finite_support_Moller_derived"])
        self.assertTrue(result["primitive_public_pointer_persistence_derived"])
        self.assertTrue(
            result["primitive_public_outgoing_endomorphism_derived"]
        )
        self.assertLess(result["pointer_stability_error"], 2e-10)
        self.assertLess(result["finite_Moller_unitarity_error"], 2e-10)
        self.assertGreater(
            result["shared_source_causal_order_sensitivity"], 1e-3
        )

    def test_no_endpoint_target_and_fail_closed_scope(self) -> None:
        result = json.loads(RESULT.read_text(encoding="ascii"))
        self.assertFalse(result["first_pointer_probability_target_predeclared"])
        self.assertFalse(result["transported_interaction_rule_used"])
        self.assertFalse(result["generated_descendant_action_derived"])
        self.assertFalse(result["complete_physical_durability_derived"])
        self.assertFalse(result["thresholded_source_return_decay_derived"])
        self.assertFalse(result["complete_root_spectral_measure_derived"])
        self.assertFalse(result["coupling_evaluation_authorized"])
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
