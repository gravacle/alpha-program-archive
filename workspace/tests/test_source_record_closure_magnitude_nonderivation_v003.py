"""Independent fail-closed checks for closure-magnitude trial algebra."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_record_closure_magnitude_nonderivation_v003.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("closure_magnitude_v003", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load closure-magnitude audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_declared_stationary_points_and_curvatures() -> None:
    module = load_audit_module()
    for n in (1, 2):
        if module.nonzero_stationarity_factor(n, n) != 0:
            raise AssertionError("Nonzero stationarity factor failed")
        if module.potential(n, n) != 0:
            raise AssertionError("Trial function is nonzero at stationary point")
        if module.radial_second_derivative(n, n) != 8 * n:
            raise AssertionError("Incorrect radial second derivative")


def test_result_builder_uses_algebraic_not_physical_stability() -> None:
    module = load_audit_module()
    result = module.build_result()
    if result["status"] != "PASS_DECLARED_TRIAL_FUNCTION_ALGEBRA_ONLY":
        raise AssertionError("Unexpected audit status")
    if result["declared_trial_stationary_points_differ"] is not True:
        raise AssertionError("Distinct trial stationary points not computed")
    if result["physical_closure_stability_derived"] is not False:
        raise AssertionError("Toy curvature promoted to physical stability")
    if result["two_complete_admissible_closure_actions_exhibited"] is not False:
        raise AssertionError("Trial functions promoted to complete actions")
    if result["full_Q_spec_nonuniqueness_proved"] is not False:
        raise AssertionError("Trial functions promoted to Q_spec countermodels")
    if result["closure_magnitude_presently_derived"] is not False:
        raise AssertionError("Closure magnitude promoted prematurely")
    if result["record_generated_source_mass_derived"] is not False:
        raise AssertionError("Source mass promoted prematurely")
    if result["alpha_computed"] is not False:
        raise AssertionError("Alpha promoted prematurely")


def test_require_survives_optimized_python() -> None:
    module = load_audit_module()
    try:
        module.require(False, "sentinel")
    except RuntimeError as error:
        if str(error) != "sentinel":
            raise
    else:
        raise AssertionError("Fail-closed require did not raise")
