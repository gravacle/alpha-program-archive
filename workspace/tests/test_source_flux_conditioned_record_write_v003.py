"""Independent checks of the conditional source-flux holonomy."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_flux_conditioned_record_write_v003.py"


def load_module():
    spec = importlib.util.spec_from_file_location("source_flux_holonomy_v003", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load source-flux holonomy audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_nominal_partial_trace_against_expected() -> None:
    module = load_module()
    result = module.build_result()
    if result["joint_density_changes_in_fixed_source_basis"] is not True:
        raise AssertionError("Joint fixed-basis change not detected")
    if result["reduced_record_density_invariant"] is not True:
        raise AssertionError("Reduced record invariance not detected")


def test_fail_closed_scope() -> None:
    module = load_module()
    result = module.build_result()
    if result["integrated_record_changing_holonomy"] != (
        "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing"
    ):
        raise AssertionError("Wrong conditional holonomy")
    for false_flag in (
        "physical_source_flux_nondemolition_derived",
        "coherent_flux_superposition_physically_admissible_derived",
        "source_phase_reference_supplied",
        "source_relative_phase_observability_derived",
        "gauge_invariant_phase_effect_derived",
        "complete_physical_write_operator_derived",
        "physical_dynamical_action_fixed",
        "complete_source_record_environment_operator_derived",
        "physical_durability_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if result[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")


def test_projector_generator_and_partial_trace_mutations_fail() -> None:
    mutations = (
        ("Q1", (( (1, 0), (0, 0)), ((0, 0), (0, 0)))),
        ("Q1", (( (0, 0), (0, 0)), ((0, 0), (2, 0)))),
        ("Y", (( (0, 0), (2, 0)), ((0, 0), (0, 0)))),
    )
    for name, value in mutations:
        module = load_module()
        setattr(module, name, value)
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Malformed {name} mutation passed")

    module = load_module()
    module.partial_trace_source = lambda joint: module.ZERO2
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Zero partial-trace mutation passed")
