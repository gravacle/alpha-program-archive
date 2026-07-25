import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_local_covariant_cell_measure_selector_v001.py"
RESULT = ROOT / "results" / "local_covariant_cell_measure_selector_v001.json"


def load_audit():
    spec = importlib.util.spec_from_file_location("cell_measure_audit", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_exact_unit_diamond_moments():
    audit = load_audit()
    assert audit.diamond_moment_of_u(0) == Fraction(1, 24)
    assert audit.diamond_moment_of_u(1) == Fraction(1, 1440)
    assert audit.diamond_moment_of_u(2) == Fraction(1, 50400)


def test_profile_scalar_is_boost_invariant():
    audit = load_audit()
    p = (-0.5, 0.0, 0.0, 0.0)
    q = (0.5, 0.0, 0.0, 0.0)
    x = (0.1, 0.1, 0.04, -0.02)
    before = audit.profile_scalar(p, q, x)
    after = audit.profile_scalar(
        audit.boost_x(p, 0.63),
        audit.boost_x(q, 0.63),
        audit.boost_x(x, 0.63),
    )
    assert abs(before - after) < 1e-14


def test_selector_blocks_uniqueness_without_strict_locality():
    audit = load_audit()
    audit.main()
    result = json.loads(RESULT.read_text())
    assert result["construction_uses_alpha"] is False
    assert result["alpha_computed"] is False
    assert result["checks"]["at_least_two_distinct_normalized_measures"] is True
    assert (
        result["verdict"]
        == "MEASURE_NOT_UNIQUE_STRICT_LOCALITY_DECISION_REQUIRED"
    )
    assert result["hypothesis_promoted_to_principle"] is False
