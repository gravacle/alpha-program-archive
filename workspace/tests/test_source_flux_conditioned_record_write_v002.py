"""Independent checks of the conditional source-flux record holonomy."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_flux_conditioned_record_write_v002.py"


def load_module():
    spec = importlib.util.spec_from_file_location("source_flux_holonomy", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load source-flux holonomy audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def apply(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(4))
        for row in range(4)
    )


def outer(vector):
    return tuple(
        tuple(vector[row] * vector[column].conjugate() for column in range(4))
        for row in range(4)
    )


def partial_trace_source(joint):
    return tuple(
        tuple(
            sum(joint[2 * source + row][2 * source + column] for source in range(2))
            for column in range(2)
        )
        for row in range(2)
    )


def test_coherent_source_phase_ambiguity_independently() -> None:
    write = (
        (1 + 0j, 0j, 0j, 0j),
        (0j, 1 + 0j, 0j, 0j),
        (0j, 0j, 0j, -1 + 0j),
        (0j, 0j, 1 + 0j, 0j),
    )
    phase_pi = (
        (1 + 0j, 0j, 0j, 0j),
        (0j, 1 + 0j, 0j, 0j),
        (0j, 0j, 0j, 1 + 0j),
        (0j, 0j, -1 + 0j, 0j),
    )
    ready = (1 + 0j, 0j, 1 + 0j, 0j)
    written = apply(write, ready)
    phase_written = apply(phase_pi, ready)
    joint = outer(written)
    phase_joint = outer(phase_written)
    if joint == phase_joint:
        raise AssertionError("Source-relative phase did not change joint coherence")
    if partial_trace_source(joint) != partial_trace_source(phase_joint):
        raise AssertionError("Source-relative phase changed reduced record density")


def test_fail_closed_scope() -> None:
    module = load_module()
    result = module.build_result()
    if result["integrated_record_changing_holonomy"] != (
        "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing"
    ):
        raise AssertionError("Wrong conditional holonomy")
    for false_flag in (
        "active_identity_phase_changes_reduced_record_density",
        "complete_physical_write_operator_derived",
        "physical_dynamical_action_fixed",
        "source_conditioned_identity_phase_fixed",
        "complete_source_record_environment_operator_derived",
        "post_closure_pointer_coefficient_derived",
        "source_odd_scalar_pseudoscalar_coefficient_derived",
        "physical_durability_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if result[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")


def test_projector_and_generator_mutations_fail() -> None:
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
