"""Independent checks of the conditional source-record exchange structure."""

from __future__ import annotations

import cmath
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_record_generator_structure_v001.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("source_record_generator", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_fail_closed_result_flags() -> None:
    module = load_audit_module()
    result = module.build_result()
    assert result["unconstrained_real_dimension"] == 4
    assert result["conditional_conserved_real_dimension"] == 2
    assert result["combined_grading_conservation_derived"] is False
    assert result["exchange_magnitude_derived"] is False
    assert result["physical_record_interval_derived"] is False
    assert result["durable_record_dynamics_derived"] is False
    assert result["source_mass_derived"] is False
    assert result["coupling_evaluation_authorized"] is False
    assert result["alpha_computed"] is False


def test_exact_exchange_transfer_at_first_swap_angle() -> None:
    angle = cmath.pi / 2
    retained_amplitude = cmath.cos(angle)
    transferred_amplitude = -1j * cmath.sin(angle)
    assert abs(retained_amplitude) < 1e-15
    assert abs(abs(transferred_amplitude) - 1.0) < 1e-15


def test_no_target_literals() -> None:
    text = SCRIPT.read_text(encoding="utf-8").lower()
    forbidden = ("137.035", "137.036", "0.007297", "0.510998", "17.543")
    assert all(value not in text for value in forbidden)
