"""Independent tests for the typed charge/chiral/record invariant-form gate."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_typed_charge_chiral_record_invariant_form_v001.py"
RESULT = ROOT / "results" / "typed_charge_chiral_record_invariant_form_v001.json"


def load_module():
    spec = importlib.util.spec_from_file_location("typed_forms", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load typed invariant-form audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_invariant_form_dimensions() -> None:
    out = load_module().build_result()
    if out["symmetric_form_domain_dimension"] != 10:
        raise AssertionError("Wrong symmetric-form domain")
    if out["independent_rephase_constraint_rank"] != 8:
        raise AssertionError("Wrong independent-rephase rank")
    if out["independent_rephase_invariant_form_dimension"] != 2:
        raise AssertionError("Independent rephasings did not leave two weights")
    if out["swap_extended_constraint_rank"] != 9:
        raise AssertionError("Wrong swap-extended rank")
    if out["chirality_record_swap_reduces_form_dimension_to_one"] is not True:
        raise AssertionError("Swap did not reduce form space to one dimension")


def test_typed_operators_are_independent_and_charge_neutral() -> None:
    module = load_module()
    charge, mass_x, mass_y, write_x, write_y = module.typed_operator_basis()
    zero8 = module.g_zero_matrix(8)
    for operator in (mass_x, mass_y, write_x, write_y):
        if module.g_commutator(charge, operator) != zero8:
            raise AssertionError("Typed operator is not charge neutral")
    rows = module.columns_to_rows(
        [
            module.g_flatten_real(operator)
            for operator in (mass_x, mass_y, write_x, write_y)
        ]
    )
    _, pivots = module.rref(rows)
    if len(pivots) != 4:
        raise AssertionError("Typed operator basis is not independent")


def test_independent_plane_norms_are_invariant() -> None:
    module = load_module()
    chiral = module.block_diagonal(module.CANONICAL_J2, module.ZERO2)
    record = module.block_diagonal(module.ZERO2, module.CANONICAL_J2)
    mass_norm = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
    )
    record_norm = (
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    )
    for form in (mass_norm, record_norm):
        if module.invariant_map(chiral, form) != module.block_diagonal(
            module.ZERO2, module.ZERO2
        ):
            raise AssertionError("Plane norm is not chiral-rephase invariant")
        if module.invariant_map(record, form) != module.block_diagonal(
            module.ZERO2, module.ZERO2
        ):
            raise AssertionError("Plane norm is not record-rephase invariant")


def test_fail_closed_scope() -> None:
    out = load_module().build_result()
    for false_flag in (
        "complete_physical_carrier_derived",
        "chirality_record_swap_derived",
        "single_superconnection_forces_common_normalization",
        "unique_full_carrier_coupling_ray_derived",
        "complete_source_record_environment_operator_derived",
        "record_onset_to_source_self_energy_ratio_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if out[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")


def test_generator_and_swap_mutations_fail_closed() -> None:
    zero = (Fraction(0), Fraction(0))
    one = (Fraction(1), Fraction(0))
    mutations = (
        ("CHIRAL_REPHASE_SCALE", Fraction(1)),
        ("G_Q", ((zero, one), (one, zero))),
        ("FACTOR_ORDER", ("chirality", "flux", "record")),
        ("SWAP_PLANES", tuple(tuple(int(r == c) for c in range(4)) for r in range(4))),
    )
    for name, value in mutations:
        module = load_module()
        setattr(module, name, value)
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Mutation passed: {name}")


def test_pauli_hermiticity_and_normalization_mutations_fail_closed() -> None:
    for multiplier in (
        (Fraction(0), Fraction(1)),
        (Fraction(2), Fraction(0)),
    ):
        module = load_module()
        module.G_X = module.g_matrix_scale(multiplier, module.G_X)
        module.G_Y = module.g_matrix_scale(multiplier, module.G_Y)
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Mutated Pauli pair passed: multiplier={multiplier}")


def test_scaled_projector_mutation_fails_closed() -> None:
    module = load_module()
    module.G_Q = module.g_matrix_scale(
        (Fraction(2), Fraction(0)),
        module.G_Q,
    )
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Scaled flux projector passed")


def test_stored_result_parity_without_rewrite() -> None:
    module = load_module()
    stored = module.load_result()
    direct = module.build_result()
    if not module.strict_equal(stored, direct):
        raise AssertionError("Stored result differs from direct result")
    mutated = json.loads(json.dumps(stored))
    mutated["alpha_computed"] = True
    if module.strict_equal(mutated, direct):
        raise AssertionError("Stored alpha mutation was accepted")
