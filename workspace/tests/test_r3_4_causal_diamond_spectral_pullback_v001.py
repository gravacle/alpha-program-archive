import importlib.util
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_r3_4_causal_diamond_spectral_pullback_v001.py"
RESULT = ROOT / "results" / "r3_4_causal_diamond_spectral_pullback_v001.json"

spec = importlib.util.spec_from_file_location("r34", SCRIPT)
r34 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(r34)


def test_form_factor_is_normalized_and_matches_full_diamond_quadrature():
    assert r34.diamond_form_factor(0.0) == 1.0
    for energy in (0.01, 0.2, 1.0, 3.0, 7.0, 12.0):
        assert math.isclose(
            r34.diamond_form_factor(energy),
            r34.independent_diamond_quadrature(energy),
            rel_tol=0.0,
            abs_tol=2.0e-10,
        )


def test_density_is_positive_and_normalized():
    energies = np.linspace(0.0, 500.0, 50001)
    assert np.all(r34.density(energies) >= 0.0)
    assert abs(r34.independent_normalization_check() - 1.0) < 2.0e-8


def test_provenance_blocks_premature_promotion():
    r34.main()
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    assert data["status"]["conditional_density_computed"] is True
    assert data["status"]["unique_covariant_spectral_measure_derived"] is False
    assert data["status"]["hypothesis_promoted_to_principle"] is False
    assert data["status"]["alpha_computed"] is False
    assert (
        data["status"]["verdict"]
        == "CONDITIONAL_DIAMOND_PULLBACK_OPERATOR_OR_ROOT_OPEN"
    )
