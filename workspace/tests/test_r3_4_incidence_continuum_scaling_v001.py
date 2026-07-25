import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_r3_4_incidence_continuum_scaling_v001.py"
RESULT = ROOT / "results" / "r3_4_incidence_continuum_scaling_v001.json"

module_spec = importlib.util.spec_from_file_location("continuum_v1", SCRIPT)
continuum_v1 = importlib.util.module_from_spec(module_spec)
if module_spec.loader is None:
    raise RuntimeError("unable to load continuum audit")
module_spec.loader.exec_module(continuum_v1)


class IncidenceContinuumTest(unittest.TestCase):
    def test_free_tail_closes_without_promoting_complete_operator(self):
        before = RESULT.read_bytes() if RESULT.exists() else None
        data = continuum_v1.build_result()
        after = RESULT.read_bytes() if RESULT.exists() else None
        self.assertEqual(before, after)
        self.assertEqual(
            data["status"]["verdict"],
            "FREE_FLAT_TAIL_OPERATOR_AND_ROOT_MEASURE_DERIVED_"
            "WRITE_DEFECT_OPEN",
        )
        self.assertTrue(data["status"]["free_flat_continuum_scaling_derived"])
        self.assertTrue(
            data["status"]["operator_derived_positive_branch_root_measure_computed"]
        )
        self.assertFalse(
            data["status"]["physical_positive_energy_record_branch_selected"]
        )
        self.assertFalse(
            data["status"]["complete_outgoing_root_spectral_measure_derived"]
        )
        self.assertFalse(data["status"]["alpha_computed"])

    def test_projectors_and_root_warnings(self):
        data = continuum_v1.build_result()
        weights = data["operator"]["checks"]["root_projector_weights"]
        self.assertAlmostEqual(weights["positive"], 0.5)
        self.assertAlmostEqual(weights["negative"], 0.5)
        self.assertAlmostEqual(weights["transverse_zero"], 0.0)
        self.assertTrue(
            data["root_measure"]["full_truncated_operator_has_transverse_zero_eigenspace"]
        )
        self.assertFalse(data["root_measure"]["sharp_root_in_generator_domain"])
        self.assertFalse(data["root_measure"]["sharp_root_mean_energy_finite"])


if __name__ == "__main__":
    unittest.main()
