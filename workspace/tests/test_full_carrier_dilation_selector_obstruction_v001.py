"""Independent tests for the reduced full-carrier selector obstruction."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_full_carrier_dilation_selector_obstruction_v001.py"
RESULT = ROOT / "results" / "full_carrier_dilation_selector_obstruction_v001.json"


def load_module():
    spec = importlib.util.spec_from_file_location("dilation_selector", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load dilation-selector audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_reduced_dimensions_and_obstruction() -> None:
    module = load_module()
    out = module.build_result()
    expected = {
        "full_reduced_Pauli_product_dimension": 64,
        "odd_odd_reduced_operator_dimension": 16,
        "source_record_only_kernel_dimension": 8,
        "unit_weight_candidate_kernel_dimension": 4,
        "source_doubled_candidate_kernel_dimension": 2,
        "neighbor_weight_assignments_with_same_nullity": 8,
    }
    for key, value in expected.items():
        if out[key] != value:
            raise AssertionError(f"Unexpected {key}: {out[key]}")
    if out["unit_weight_candidate_writes_edge"] is not False:
        raise AssertionError("Unit-weight candidate unexpectedly writes edge")
    if out["source_doubled_candidate_writes_edge"] is not True:
        raise AssertionError("Source-doubled candidate lacks edge write")
    if out["schur_self_energy_deforms_with_unfixed_gap"] is not True:
        raise AssertionError("Schur gap deformation was not exhibited")


def test_nullspace_vectors_and_edge_blocks_independently() -> None:
    module = load_module()
    labels, operators, z_source, z_record, z_edge = module.build_odd_basis()
    unit_kernel = module.kernel_for_weights(
        module.UNIT_EDGE_WEIGHTS,
        operators,
        z_source,
        z_record,
        z_edge,
    )
    doubled_kernel = module.kernel_for_weights(
        module.SOURCE_DOUBLED_WEIGHTS,
        operators,
        z_source,
        z_record,
        z_edge,
    )

    def has_edge_block(kernel) -> bool:
        for vector in kernel:
            operator = module.linear_operator(vector, operators)
            # The edge bit is the fastest tensor-product index. A nonzero
            # matrix element between opposite edge bits is an edge flip.
            for row in range(8):
                for column in range(8):
                    if row % 2 != column % 2 and operator[row][column] != module.ZERO:
                        return True
        return False

    if has_edge_block(unit_kernel):
        raise AssertionError("Unit-weight kernel has an edge off-diagonal block")
    if not has_edge_block(doubled_kernel):
        raise AssertionError("Source-doubled kernel lacks an edge off-diagonal block")

    for weights in module.primitive_weight_triples(module.WEIGHT_SEARCH_BOUND):
        kernel = module.kernel_for_weights(
            weights,
            operators,
            z_source,
            z_record,
            z_edge,
        )
        if module.kernel_has_edge_flip(kernel, operators) != has_edge_block(kernel):
            raise AssertionError(
                f"Production edge classifier disagrees at weights {weights}"
            )


def test_edge_classifier_depends_on_operator_blocks_not_kernel_dimension() -> None:
    module = load_module()
    labels, operators, _, _, _ = module.build_odd_basis()

    edge_diagonal_indices = [
        index for index, label in enumerate(labels) if label[-1] in ("I", "Z")
    ]
    edge_flipping_indices = [
        index for index, label in enumerate(labels) if label[-1] in ("X", "Y")
    ]

    def basis_vector(index: int) -> list[Fraction]:
        return [
            Fraction(int(position == index))
            for position in range(len(operators))
        ]

    two_dimensional_diagonal = [
        basis_vector(index)
        for index in edge_diagonal_indices[:2]
    ]
    if module.kernel_has_edge_flip(two_dimensional_diagonal, operators):
        raise AssertionError(
            "Two-dimensional edge-diagonal kernel was mislabeled as a flip"
        )

    four_dimensional_with_flip = [
        basis_vector(edge_diagonal_indices[0]),
        basis_vector(edge_diagonal_indices[1]),
        basis_vector(edge_diagonal_indices[2]),
        basis_vector(edge_flipping_indices[0]),
    ]
    if not module.kernel_has_edge_flip(four_dimensional_with_flip, operators):
        raise AssertionError(
            "Four-dimensional kernel with an edge flip was mislabeled diagonal"
        )


def test_neighbor_distribution_independently_sums_to_primitive_inventory() -> None:
    module = load_module()
    triples = module.primitive_weight_triples(2)
    if len(triples) != 49:
        raise AssertionError("Unexpected primitive weight inventory")
    out = module.build_result()
    distribution = {
        int(key): value
        for key, value in out["neighbor_weight_nullity_distribution"].items()
    }
    if distribution != {0: 22, 2: 8, 4: 12, 6: 4, 8: 3}:
        raise AssertionError("Unexpected nullity distribution")
    if sum(distribution.values()) != len(triples):
        raise AssertionError("Distribution does not exhaust neighbor inventory")


def test_fail_closed_scope() -> None:
    out = load_module().build_result()
    for false_flag in (
        "complete_physical_carrier_derived",
        "source_doubled_grading_weights_derived",
        "unique_full_carrier_coupling_ray_derived",
        "axial_Ward_identity_with_inflow_derived",
        "closure_sector_spectrum_derived",
        "record_onset_to_source_self_energy_ratio_derived",
        "complete_source_record_environment_operator_derived",
        "physical_durability_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if out[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")


def test_weight_and_search_mutations_fail_closed() -> None:
    mutations = (
        ("WEIGHT_SEARCH_BOUND", 3),
        ("UNIT_EDGE_WEIGHTS", (2, 1, -1)),
        ("SOURCE_DOUBLED_WEIGHTS", (1, 1, 1)),
    )
    for name, value in mutations:
        module = load_module()
        setattr(module, name, value)
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Mutation passed: {name}")


def test_schur_block_elimination_and_singular_case() -> None:
    module = load_module()
    block = (
        (Fraction(0), Fraction(3)),
        (Fraction(3), Fraction(2)),
    )
    if module.schur_public_scalar(block, Fraction(0)) != Fraction(-9, 2):
        raise AssertionError("Schur complement lost the squared coupling")
    try:
        module.schur_public_scalar(block, Fraction(2))
    except RuntimeError:
        pass
    else:
        raise AssertionError("Singular Schur complement passed")
    try:
        module.schur_public_scalar(
            ((Fraction(0), Fraction(3)), (Fraction(-3), Fraction(2))),
            Fraction(0),
        )
    except RuntimeError:
        pass
    else:
        raise AssertionError("Non-Hermitian Schur block passed")


def test_stored_result_parity_without_rewrite() -> None:
    module = load_module()
    stored = module.load_result(RESULT)
    direct = load_module().build_result()
    if not module.strict_equal(stored, direct):
        raise AssertionError("Stored result differs from direct result")
    mutated = json.loads(json.dumps(stored))
    mutated["alpha_computed"] = True
    if module.strict_equal(mutated, direct):
        raise AssertionError("Stored-result alpha mutation was accepted")
