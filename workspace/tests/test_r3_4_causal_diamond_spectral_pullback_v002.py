import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_r3_4_causal_diamond_spectral_pullback_v002.py"
RESULT = ROOT / "results" / "r3_4_causal_diamond_spectral_pullback_v002.json"

module_spec = importlib.util.spec_from_file_location("r34v2", SCRIPT)
r34v2 = importlib.util.module_from_spec(module_spec)
if module_spec.loader is None:
    raise RuntimeError("unable to load R3.4 v002 audit")
module_spec.loader.exec_module(r34v2)


class R34V002Test(unittest.TestCase):
    def test_build_is_side_effect_free_and_fail_closed(self):
        before = RESULT.read_bytes() if RESULT.exists() else None
        data = r34v2.build_result()
        after = RESULT.read_bytes() if RESULT.exists() else None
        self.assertEqual(before, after)
        self.assertEqual(
            data["status"]["verdict"],
            "CONDITIONAL_SCALAR_DIAMOND_DENSITY_ONLY",
        )
        self.assertTrue(data["status"]["layer_m_scalar_calculation_passed"])
        self.assertFalse(data["status"]["layer_p_physical_provenance_passed"])
        self.assertFalse(data["status"]["alpha_computed"])

    def test_mathematical_checks_are_executed(self):
        data = r34v2.build_result()
        self.assertLess(
            data["independent_numerical_checks"]["maximum_transform_error"],
            2.0e-10,
        )
        self.assertLess(
            data["independent_numerical_checks"]["normalization_error"],
            2.0e-8,
        )
        self.assertTrue(all(data["layer_m_checks"].values()))
        self.assertFalse(data["regulator_comparison"]["same_class"])


if __name__ == "__main__":
    unittest.main()
