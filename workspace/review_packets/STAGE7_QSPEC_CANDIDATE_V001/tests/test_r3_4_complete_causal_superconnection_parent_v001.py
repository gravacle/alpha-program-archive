import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = (
    ROOT
    / "scripts"
    / "audit_r3_4_complete_causal_superconnection_parent_v001.py"
)
VERIFY = (
    ROOT
    / "scripts"
    / "verify_r3_4_complete_causal_superconnection_parent_v001.py"
)
RESULT = (
    ROOT
    / "results"
    / "r3_4_complete_causal_superconnection_parent_v001.json"
)
VERIFY_RESULT = (
    ROOT
    / "results"
    / "r3_4_complete_causal_superconnection_parent_verification_v001.json"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_complete_parent_primary_audit():
    module = load_module("complete_parent_audit", AUDIT)
    module.main()
    result = json.loads(RESULT.read_text())
    assert result["specification_seal_matches"] is True
    assert result["authority_hashes_match"] is True
    assert result["intrinsic_envelope"]["normalized"] is True
    assert result["generated_descendants"]["full_square_identity_error"] < 1e-10
    assert result["generated_descendants"]["overlap_descendant_norm"] > 0
    assert (
        result["generated_descendants"]["derivative_support_descendant_norm"]
        > 0
    )
    finite = result["finite_parent_regression"]
    assert finite["convergence_ratio"] > 3.5
    assert finite["later_record_restriction_error"] < 1e-10
    assert finite["free_tail_record_restriction_error"] < 1e-10
    assert finite["finite_Moller_unitarity_error"] < 1e-9
    assert finite["dressed_pointer_bare_algebra_distance"] > 0
    assert result["free_tail"]["source_point_spectrum_absent"] is True
    assert result["numerical_regression_pass"] is True
    assert result["finite_causal_source_record_parent_derived"] is True
    assert result["complete_causal_source_record_parent_flat_branch"] is False
    assert result["complete_parent_to_outgoing_GNS_map_derived"] is False
    assert (
        result["verdict"]
        == "FINITE_CAUSAL_PARENT_DERIVED_CONTINUUM_COMPLETION_OPEN"
    )
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False


def test_complete_parent_independent_verifier():
    module = load_module("complete_parent_verifier", VERIFY)
    module.main()
    result = json.loads(VERIFY_RESULT.read_text())
    assert result["independent_verification_pass"] is True
    assert result["record_restriction_error"] < 2e-7
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
