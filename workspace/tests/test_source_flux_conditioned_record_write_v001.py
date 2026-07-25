"""Independent checks of the source-flux-conditioned write gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_flux_conditioned_record_write_v001.py"


def load_module():
    spec = importlib.util.spec_from_file_location("source_flux_write", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load source-flux write audit")
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


def test_controlled_write_and_phase_ambiguity_independently() -> None:
    write = (
        (1 + 0j, 0j, 0j, 0j),
        (0j, 1 + 0j, 0j, 0j),
        (0j, 0j, 0j, -1 + 0j),
        (0j, 0j, 1 + 0j, 0j),
    )
    state_00 = (1 + 0j, 0j, 0j, 0j)
    state_10 = (0j, 0j, 1 + 0j, 0j)
    if apply(write, state_00) != state_00:
        raise AssertionError("Independent zero-flux check failed")
    written = apply(write, state_10)
    if written != (0j, 0j, 0j, 1 + 0j):
        raise AssertionError("Independent active write check failed")
    phase_written = tuple(-entry for entry in written)
    if outer(written) != outer(phase_written):
        raise AssertionError("Branch phase changed the density matrix")
    if written == phase_written:
        raise AssertionError("Branch phase mutation was not distinct")


def test_fail_closed_scope() -> None:
    module = load_module()
    result = module.build_result()
    if result["integrated_record_changing_generator"] != (
        "(pi/2)*Q_Sigma_tensor_Y_up_to_rephasing"
    ):
        raise AssertionError("Wrong integrated write generator")
    for false_flag in (
        "active_branch_identity_phase_changes_record_density",
        "source_conditioned_identity_phase_fixed",
        "complete_source_record_operator_derived",
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
    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")


def test_source_flux_mutation_fails() -> None:
    module = load_module()
    module.Q1 = module.Q0
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Duplicated source-flux projector passed")
