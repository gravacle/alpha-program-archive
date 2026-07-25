"""Independent tests for the relative record-onset action gate."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_boundary_record_onset_saturation_action_v002.py"


def load_module():
    spec = importlib.util.spec_from_file_location("relative_record_onset", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load relative record-onset audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def matrix_vector(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(2))
        for row in range(2)
    )


def inner(left, right):
    return sum(left[index].conjugate() * right[index] for index in range(2))


def test_relative_and_symmetric_constructions_independently() -> None:
    ready = (1 + 0j, 0j)
    relative = ((0j, -1 + 0j), (1 + 0j, 0j))
    if matrix_vector(relative, ready) != (0j, 1 + 0j):
        raise AssertionError("Independent relative endpoint check failed")

    # U0=exp(+i*pi*Y/4), U1=exp(-i*pi*Y/4).
    c = math.sqrt(0.5)
    u0 = ((c, c), (-c, c))
    u1 = ((c, -c), (c, c))
    r0 = matrix_vector(u0, ready)
    r1 = matrix_vector(u1, ready)
    if abs(inner(r0, r1)) > 1e-15:
        raise AssertionError("Symmetric branches are not orthogonal")
    if abs(abs(inner(ready, r0)) - c) > 1e-15:
        raise AssertionError("First branch did not move pi/4")
    if abs(abs(inner(ready, r1)) - c) > 1e-15:
        raise AssertionError("Second branch did not move pi/4")


def test_fail_closed_status() -> None:
    module = load_module()
    result = module.build_result()
    if result["integrated_relative_write_action"] != "pi*hbar/2":
        raise AssertionError("Wrong integrated relative action")
    if result["conditional_record_overlap_object"] != "U0_dagger_U1":
        raise AssertionError("Wrong comparison object")
    for false_flag in (
        "historical_target_blindness_established",
        "absolute_one_branch_write_action_fixed",
        "common_branch_hamiltonian_fixed",
        "unique_causal_record_interval_numerically_derived",
        "complete_source_record_environment_action_derived",
        "physical_durability_derived",
        "relative_write_energy_identified_with_pointer_coefficient",
        "relative_write_energy_identified_with_source_mass",
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


def test_mutated_relative_generator_is_detected() -> None:
    module = load_module()
    module.Y = module.I2
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Identity mutation passed as a relative generator")
