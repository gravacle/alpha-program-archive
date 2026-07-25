import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_r3_4_outgoing_tail_generator_exhaustion_v001.py"
RESULT = ROOT / "results" / "r3_4_outgoing_tail_generator_exhaustion_v001.json"

module_spec = importlib.util.spec_from_file_location("tail_v1", SCRIPT)
tail_v1 = importlib.util.module_from_spec(module_spec)
if module_spec.loader is None:
    raise RuntimeError("unable to load outgoing-tail audit")
module_spec.loader.exec_module(tail_v1)


class OutgoingTailTest(unittest.TestCase):
    def test_reduced_public_exhaustion_does_not_promote_full_operator(self):
        before = RESULT.read_bytes() if RESULT.exists() else None
        data = tail_v1.build_result()
        after = RESULT.read_bytes() if RESULT.exists() else None
        self.assertEqual(before, after)
        self.assertEqual(
            data["status"]["verdict"],
            "PUBLIC_TAIL_ZERO_FORM_EXHAUSTED_CONTINUUM_SCALING_OPEN",
        )
        self.assertTrue(data["status"]["reduced_public_tail_zero_form_exhausted"])
        self.assertFalse(
            data["status"]["complete_asymptotic_tail_zero_form_exhausted"]
        )
        self.assertFalse(data["status"]["alpha_computed"])

    def test_full_algebra_warning_survives(self):
        data = tail_v1.build_result()
        reduced = data["reduced_register_exhaustion"]
        self.assertEqual(reduced["nondemolition_kernel"], ["I", "Z"])
        self.assertTrue(reduced["Z_nontrivial_on_full_hilbert_algebra"])
        self.assertFalse(
            data["scope"]["public_tail_equivalence_proves_full_generator_equivalence"]
        )


if __name__ == "__main__":
    unittest.main()
