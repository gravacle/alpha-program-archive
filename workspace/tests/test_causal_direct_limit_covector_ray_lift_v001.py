import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_causal_direct_limit_covector_ray_lift_v001.py"
RESULT = ROOT / "results" / "causal_direct_limit_covector_ray_lift_v001.json"


def load_audit():
    spec = importlib.util.spec_from_file_location("ray_lift_audit", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_product_state_compatibility_under_identity_embedding():
    audit = load_audit()
    observable = [
        [1.3 + 0j, 0.1j, 0.2 + 0j, -0.1j],
        [-0.1j, -0.7 + 0j, 0.05j, 0.3 + 0j],
        [0.2 + 0j, -0.05j, 0.4 + 0j, 0.2j],
        [0.1j, 0.3 + 0j, -0.2j, 2.1 + 0j],
    ]
    identity = [[1 + 0j, 0j], [0j, 1 + 0j]]
    embedded = audit.kron(observable, identity)
    for label in (0, 1):
        assert audit.product_state_expectation(observable, label, 2) == (
            audit.product_state_expectation(embedded, label, 3)
        )


def test_selector_finds_quasilocal_lift_only():
    audit = load_audit()
    audit.main()
    result = json.loads(RESULT.read_text())
    assert result["construction_uses_alpha"] is False
    assert result["alpha_computed"] is False
    assert result["verdict"] == "QUASILOCAL_STATE_LIFT_ONLY"
    assert result["outgoing_record_algebra_subobligation_closed"] is True
    assert result["fork_8_closed"] is False
