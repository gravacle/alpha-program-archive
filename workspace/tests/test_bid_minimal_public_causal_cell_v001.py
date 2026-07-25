import importlib.util
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "derive_bid_minimal_public_causal_cell_v001.py"
SPEC = importlib.util.spec_from_file_location("causal_cell_v001", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_baseline_scale_and_compactness() -> None:
    row = MODULE.scale_ratios(math.pi, 0.5, 1.0)
    assert math.isclose(row["T_R_over_t_P"], 2.0 * math.sqrt(math.pi))
    assert math.isclose(row["R_R_over_l_P"], math.sqrt(math.pi))
    assert math.isclose(row["E_R_over_E_P"], math.sqrt(math.pi) / 2.0)
    assert math.isclose(row["reconstructed_compactness"], 1.0)


def test_each_load_bearing_input_changes_the_scale() -> None:
    baseline = MODULE.scale_ratios(math.pi, 0.5, 1.0)["T_R_over_t_P"]
    variants = (
        MODULE.scale_ratios(math.pi / 2.0, 0.5, 1.0)["T_R_over_t_P"],
        MODULE.scale_ratios(math.pi, 1.0, 1.0)["T_R_over_t_P"],
        MODULE.scale_ratios(math.pi, 0.5, 0.5)["T_R_over_t_P"],
    )
    assert all(not math.isclose(value, baseline) for value in variants)


def test_invalid_inputs_fail_closed() -> None:
    for args in ((0.0, 0.5, 1.0), (math.pi, 0.0, 1.0), (math.pi, 0.5, 0.0)):
        try:
            MODULE.scale_ratios(*args)
        except ValueError:
            continue
        raise AssertionError(f"invalid input did not fail closed: {args}")
