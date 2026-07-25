"""Independent checks for the closure-magnitude non-derivation audit."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_record_closure_magnitude_nonderivation_v002.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("closure_magnitude_audit", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_both_declared_nonzero_stationarity_conditions() -> None:
    module = load_audit_module()
    assert module.nonzero_stationarity_factor(1, 1) == 0
    assert module.nonzero_stationarity_factor(2, 2) == 0


def test_both_minima_and_radial_curvatures() -> None:
    module = load_audit_module()
    for n in (1, 2):
        assert module.potential(n, n) == 0
        assert module.radial_curvature(n, n) == 8 * n
        assert module.radial_curvature(n, n) > 0


def test_result_builder_retains_all_failure_booleans() -> None:
    module = load_audit_module()
    result = module.build_result()
    assert result["status"] == "PASS_DECLARED_TRIAL_POTENTIAL_ALGEBRA_ONLY"
    assert result["declared_trial_minima_differ"] is True
    assert result["historical_target_blindness_established"] is False
    assert result["complete_record_dynamics_supplied"] is False
    assert result["two_complete_admissible_closure_actions_exhibited"] is False
    assert result["full_Q_spec_nonuniqueness_proved"] is False
    assert result["closure_magnitude_presently_derived"] is False
    assert result["record_generated_source_mass_derived"] is False
    assert result["spectral_evaluation_authorized"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False
