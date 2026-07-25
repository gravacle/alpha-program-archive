import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_r3_3_intrinsic_cell_measure_derivation_v001.py"
RESULT = ROOT / "results" / "r3_3_intrinsic_cell_measure_derivation_v001.json"


def load_audit():
    spec = importlib.util.spec_from_file_location("r3_3_measure_audit", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_nested_diamond_exact_moments():
    audit = load_audit()
    moments = audit.nested_diamond_moments()
    assert moments["volume"] == Fraction(1, 24)
    assert moments["child_u"] == Fraction(1, 1440)
    assert moments["parent_u"] == Fraction(19, 23040)
    assert moments["physical_time"] == Fraction(-1, 96)
    assert moments["time_child_u"] == Fraction(-1, 5760)
    assert moments["time_parent_u"] == Fraction(-1, 5760)
    assert moments["child_u_squared"] == Fraction(1, 50400)
    assert moments["child_u_parent_u"] == Fraction(1, 57600)


def test_intrinsic_binding_and_uniform_measure_verdict():
    audit = load_audit()
    audit.main()
    result = json.loads(RESULT.read_text())
    assert result["construction_uses_alpha"] is False
    assert result["alpha_computed"] is False
    assert result["intrinsic_per_cell_response_binding"] is True
    assert result["exact_moments_pass"] is True
    assert result["symbolic_factor_check"] is True
    assert result["only_a_zero_survives_for_a_ge_zero"] is True
    assert result["new_strict_locality_principle_adopted"] is False
    assert (
        result["verdict"]
        == "INHERITED_REFINEMENT_NATURALITY_FORCES_UNIFORM_MEASURE"
    )
    assert result["spectral_density_derived"] is False
    assert result["hypothesis_promoted_to_principle"] is False
