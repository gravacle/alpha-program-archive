import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "scripts" / "audit_r3_4_outgoing_record_gns_completion_v001.py"
VERIFY = ROOT / "scripts" / "verify_r3_4_outgoing_record_gns_completion_v001.py"
RESULT = ROOT / "results" / "r3_4_outgoing_record_gns_completion_v001.json"
VERIFY_RESULT = (
    ROOT
    / "results"
    / "r3_4_outgoing_record_gns_completion_verification_v001.json"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_outgoing_record_gns_primary():
    module = load_module("outgoing_record_gns_audit", AUDIT)
    module.main()
    result = json.loads(RESULT.read_text())
    assert result["specification_seal_matches"] is True
    assert result["authority_hashes_match"] is True
    assert result["all_record_restrictions_pass"] is True
    assert result["all_matrix_units_pass"] is True
    assert result["all_homomorphism_pass"] is True
    assert result["dressed_net_stabilizes"] is True
    assert result["source_negative_control_pass"] is True
    assert result["central_sequence"]["bound_pass"] is True
    assert result["central_sequence"]["label_separation_pass"] is True
    assert result["outgoing_record_GNS_derived"] is True
    assert result["global_source_inclusive_state_limit_derived"] is False
    assert result["global_infinite_future_source_Moller_unitary_derived"] is False
    assert result["verdict"] == "OUTGOING_RECORD_GNS_AND_DRESSED_NET_DERIVED"
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False


def test_outgoing_record_gns_independent_verifier():
    module = load_module("outgoing_record_gns_verifier", VERIFY)
    module.main()
    result = json.loads(VERIFY_RESULT.read_text())
    assert result["independent_verification_pass"] is True
    assert result["alpha_computed"] is False
    assert result["proof_authorized"] is False
