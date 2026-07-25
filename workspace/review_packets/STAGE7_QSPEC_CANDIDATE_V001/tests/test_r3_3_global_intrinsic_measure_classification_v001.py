import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = (
    ROOT
    / "scripts"
    / "audit_r3_3_global_intrinsic_measure_classification_v001.py"
)
VERIFY = (
    ROOT
    / "scripts"
    / "verify_r3_3_global_intrinsic_measure_classification_v001.py"
)
RESULT = (
    ROOT
    / "results"
    / "r3_3_global_intrinsic_measure_classification_v001.json"
)
VERIFY_RESULT = (
    ROOT
    / "results"
    / "r3_3_global_intrinsic_measure_classification_verification_v001.json"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_primary_global_classification():
    audit = load_module("r3_3_global_measure_audit", AUDIT)
    audit.main()
    result = json.loads(RESULT.read_text())
    assert result["authority_hashes_match"] is True
    assert result["specification_seal_matches"] is True
    assert result["assumptions_textually_pinned"] is True
    assert result["fixed_covector_constraint_rank"] == 4
    assert result["fixed_covector_nullity"] == 0
    assert result["lorentz_generator_span_rank"] == 6
    assert result["lorentz_commutator_span_rank"] == 6
    assert result["lorentz_lie_algebra_perfect"] is True
    assert result["translations_alone_permit_nonuniform_character"] is True
    assert result["sample_nonzero_character_violates_lorentz"] is True
    assert (
        result["mu_a_negative_control"]["only_uniform_member_survives"]
        is True
    )
    assert result["uniform_flat_cell_measure_derived"] is True
    assert (
        result["verdict"]
        == "GLOBAL_INTRINSIC_FLAT_CELL_MEASURE_CLASSIFIED"
    )
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False


def test_independent_global_classification_verifier():
    verifier = load_module("r3_3_global_measure_verifier", VERIFY)
    verifier.main()
    result = json.loads(VERIFY_RESULT.read_text())
    assert result["fixed_space_witness_determinant"] != "0/1"
    assert result["zero_fixed_covector_space"] is True
    assert result["lorentz_lie_algebra_perfect"] is True
    assert result["mu_a_negative_control_pass"] is True
    assert result["independent_verification_pass"] is True
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
