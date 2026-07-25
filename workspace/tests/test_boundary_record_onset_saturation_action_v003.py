"""Independent tests for the relative record-orthogonalization budget gate."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_boundary_record_onset_saturation_action_v003.py"


def load_module():
    spec = importlib.util.spec_from_file_location("relative_record_budget", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load relative record-budget audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def matmul(left, right):
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )


def dagger(matrix):
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )


def apply(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(2))
        for row in range(2)
    )


def test_symmetric_relative_product_independently() -> None:
    c = math.sqrt(0.5)
    u0 = ((c, c), (-c, c))
    u1 = ((c, -c), (c, c))
    relative = matmul(dagger(u0), u1)
    expected = ((0j, -1 + 0j), (1 + 0j, 0j))
    for row in range(2):
        for column in range(2):
            if abs(relative[row][column] - expected[row][column]) > 1e-15:
                raise AssertionError("Independent U0^dagger U1 check failed")
    endpoint = apply(relative, (1 + 0j, 0j))
    if abs(endpoint[0]) > 1e-15 or abs(endpoint[1] - 1) > 1e-15:
        raise AssertionError("Independent relative endpoint check failed")


def test_fail_closed_status() -> None:
    module = load_module()
    result = module.build_result()
    if result["relative_FS_budget"] != "pi*hbar/2":
        raise AssertionError("Wrong conditional FS budget")
    if result["symmetric_branch_product_verified"] is not True:
        raise AssertionError("Symmetric branch product not verified")
    if result["relative_onset_saturation_derived"] is not False:
        raise AssertionError("Adopted saturation mislabeled as derived")
    for false_flag in (
        "physical_dynamical_action_fixed",
        "absolute_one_branch_energy_fixed",
        "arbitrary_common_additive_hamiltonian_cancels",
        "orthogonal_reduced_record_supports_derived",
        "physical_durability_derived",
        "unique_causal_record_interval_numerically_derived",
        "relative_generator_identified_with_pointer_coefficient",
        "relative_generator_identified_with_source_mass",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if result[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")


def test_projector_and_generator_mutations_fail_closed() -> None:
    mutations = (
        ("P1", (( (1, 0), (0, 0)), ((0, 0), (0, 0)))),
        ("P1", (( (0, 0), (0, 0)), ((0, 0), (2, 0)))),
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


def test_symmetric_branch_mutation_fails_closed() -> None:
    module = load_module()
    module.SQRT2_U1 = module.SQRT2_U0
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Duplicated symmetric branch passed")
