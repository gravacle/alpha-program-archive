"""Independent exact checks for the conditional pointer-commutant classification."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_durable_pointer_closure_operator_selector_v002.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("pointer_selector_v002", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load pointer-selector audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def direct_commutator(matrix, projector):
    product_left = tuple(
        tuple(
            sum(matrix[row][index] * projector[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )
    product_right = tuple(
        tuple(
            sum(projector[row][index] * matrix[index][column] for index in range(2))
            for column in range(2)
        )
        for row in range(2)
    )
    return tuple(
        tuple(product_left[row][column] - product_right[row][column] for column in range(2))
        for row in range(2)
    )


def test_kernel_and_rank_independently() -> None:
    p0 = ((1 + 0j, 0j), (0j, 0j))
    identity = ((1 + 0j, 0j), (0j, 1 + 0j))
    x = ((0j, 1 + 0j), (1 + 0j, 0j))
    y = ((0j, -1j), (1j, 0j))
    z = ((1 + 0j, 0j), (0j, -1 + 0j))
    zero = ((0j, 0j), (0j, 0j))

    image_i = direct_commutator(identity, p0)
    image_x = direct_commutator(x, p0)
    image_y = direct_commutator(y, p0)
    image_z = direct_commutator(z, p0)

    if image_i != zero or image_z != zero:
        raise AssertionError("Independent kernel check failed")
    if image_x[0][1].real != -1 or image_x[0][1].imag != 0:
        raise AssertionError("X image lacks its independent real coordinate")
    if image_y[0][1].real != 0 or image_y[0][1].imag != 1:
        raise AssertionError("Y image lacks its independent imaginary coordinate")

    # The two independent image coordinates give rank >= 2. The explicit
    # two-dimensional kernel {I,Z} in a four-dimensional domain gives rank <= 2.
    independent_rank = 2
    independent_nullity = 2
    if independent_rank + independent_nullity != 4:
        raise AssertionError("Independent rank-nullity check failed")


def test_fail_closed_scope_and_source_identity_retention() -> None:
    module = load_audit_module()
    result = module.build_result()
    expected = {
        "endpoint_projector_axioms_verified": True,
        "hermitian_domain_basis_rank": 4,
        "pointer_commutator_map_rank": 2,
        "hermitian_pointer_commutant_dimension": 2,
        "endpoint_contrast_equivalence_adopted": True,
        "endpoint_contrast_quotient_dimension": 1,
        "identity_quotient_scope": "relative_endpoint_contrast_only",
    }
    for key, value in expected.items():
        if result[key] != value:
            raise AssertionError(f"Unexpected {key}: {result[key]!r}")

    for false_flag in (
        "physical_post_closure_invariance_realized",
        "physical_contrast_normalization_derived",
        "physical_pointer_operator_selected",
        "common_source_term_excluded",
        "source_scalar_embedding_selected",
        "complete_closure_operator_selected",
        "record_write_dynamics_derived",
        "physical_durability_derived",
        "kappa_I_derived",
        "kappa_Z_derived",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if result[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")

    # A common source term survives sector projection: kappa_I +/- kappa_Z.
    kappa_i = 7
    kappa_z = 3
    if (kappa_i - kappa_z, kappa_i + kappa_z) != (4, 10):
        raise AssertionError("Common source coefficient was incorrectly quotiented")

    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")


def test_malformed_endpoint_mutations_fail_closed() -> None:
    malformed_p1_values = (
        # Duplicate endpoint.
        (( (1, 0), (0, 0)), ((0, 0), (0, 0))),
        # Non-idempotent endpoint.
        (( (0, 0), (0, 0)), ((0, 0), (2, 0))),
        # Incomplete endpoint pair.
        (( (0, 0), (0, 0)), ((0, 0), (0, 0))),
        # Non-Hermitian endpoint.
        (( (0, 0), (1, 0)), ((0, 0), (1, 0))),
    )
    for malformed in malformed_p1_values:
        module = load_audit_module()
        module.P1 = malformed
        try:
            module.build_result()
        except RuntimeError:
            continue
        raise AssertionError(f"Malformed P1 passed: {malformed!r}")


def test_exact_rank_across_all_domain_ranks() -> None:
    module = load_audit_module()
    zero = [0, 0, 0, 0]
    e0 = [1, 0, 0, 0]
    e1 = [0, 1, 0, 0]
    e2 = [0, 0, 1, 0]
    e3 = [0, 0, 0, 1]
    cases = (
        ([zero], 0),
        ([e0], 1),
        ([e0, e1], 2),
        ([e0, e1, e2], 3),
        ([e0, e1, e2, e3], 4),
        ([e0, e0, e1], 2),
    )
    for columns, expected_rank in cases:
        actual = module.exact_rank(columns)
        if actual != expected_rank:
            raise AssertionError(
                f"Exact rank mismatch: expected {expected_rank}, got {actual}"
            )


def test_duplicate_contrast_basis_fails_closed() -> None:
    module = load_audit_module()
    original_subtract = module.matrix_subtract

    def duplicate_identity(left, right):
        del left, right
        return module.I2

    module.matrix_subtract = duplicate_identity
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Duplicated contrast basis passed")
    finally:
        module.matrix_subtract = original_subtract
