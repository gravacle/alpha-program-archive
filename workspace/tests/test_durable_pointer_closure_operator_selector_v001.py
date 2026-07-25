"""Independent checks for the primitive durable-pointer selector."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_durable_pointer_closure_operator_selector_v001.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("pointer_selector", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load pointer-selector audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_general_hermitian_commutator_directly() -> None:
    # H=[[a,c-id],[c+id,b]]. Commuting with P0 forces c=d=0.
    samples = (
        (2, -3, 0, 0, True),
        (2, -3, 1, 0, False),
        (2, -3, 0, 1, False),
        (2, -3, 4, 5, False),
    )
    for a, b, c, d, should_commute in samples:
        h = ((complex(a), complex(c, -d)), (complex(c, d), complex(b)))
        p0 = ((1 + 0j, 0j), (0j, 0j))
        hp = (
            (
                h[0][0] * p0[0][0] + h[0][1] * p0[1][0],
                h[0][0] * p0[0][1] + h[0][1] * p0[1][1],
            ),
            (
                h[1][0] * p0[0][0] + h[1][1] * p0[1][0],
                h[1][0] * p0[0][1] + h[1][1] * p0[1][1],
            ),
        )
        ph = (
            (
                p0[0][0] * h[0][0] + p0[0][1] * h[1][0],
                p0[0][0] * h[0][1] + p0[0][1] * h[1][1],
            ),
            (
                p0[1][0] * h[0][0] + p0[1][1] * h[1][0],
                p0[1][0] * h[0][1] + p0[1][1] * h[1][1],
            ),
        )
        commutes = hp == ph
        if commutes is not should_commute:
            raise AssertionError("Direct Hermitian commutator classification failed")


def test_fail_closed_scope() -> None:
    module = load_audit_module()
    result = module.build_result()
    if result["hermitian_pointer_commutant_dimension"] != 2:
        raise AssertionError("Wrong pointer commutant dimension")
    if result["response_null_identity_quotient_dimension"] != 1:
        raise AssertionError("Wrong public quotient dimension")
    for false_flag in (
        "nondemolition_pointer_condition_derived",
        "complete_closure_operator_selected",
        "record_write_dynamics_derived",
        "physical_durability_derived",
        "kappa_R_derived",
        "record_generated_source_mass_derived",
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
