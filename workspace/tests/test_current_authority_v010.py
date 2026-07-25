"""Hostile-mode tests for the V010 fail-closed authority audit."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_v010.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("authority_v010", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load V010 authority audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_runtime_error(callback) -> None:
    try:
        callback()
    except RuntimeError:
        return
    raise AssertionError("Fail-closed audit accepted a corrupted state")


def test_require_survives_optimized_python() -> None:
    module = load_audit_module()
    expect_runtime_error(lambda: module.require(False, "sentinel"))


def test_every_execution_state_key_is_exhaustively_frozen() -> None:
    module = load_audit_module()
    module.validate_execution_state(dict(module.EXPECTED_EXECUTION_STATE))

    promoted = copy.deepcopy(module.EXPECTED_EXECUTION_STATE)
    promoted["alpha_computed"] = True
    expect_runtime_error(lambda: module.validate_execution_state(promoted))

    missing = copy.deepcopy(module.EXPECTED_EXECUTION_STATE)
    del missing["proof_authorized"]
    expect_runtime_error(lambda: module.validate_execution_state(missing))

    enlarged = copy.deepcopy(module.EXPECTED_EXECUTION_STATE)
    enlarged["unreviewed_success_flag"] = True
    expect_runtime_error(lambda: module.validate_execution_state(enlarged))


def test_high_risk_promotions_are_rejected_individually() -> None:
    module = load_audit_module()
    risky_false_flags = (
        "physical_public_EM_connection_derived",
        "complete_parent_action_uniquely_derived",
        "complete_parameter_free_Q_spec_frozen",
        "finite_c_F2_deformation_excluded_as_universal_theorem",
        "closure_magnitude_presently_derived",
        "record_generated_source_mass_derived",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    )
    for key in risky_false_flags:
        promoted = copy.deepcopy(module.EXPECTED_EXECUTION_STATE)
        promoted[key] = True
        expect_runtime_error(lambda promoted=promoted: module.validate_execution_state(promoted))
