#!/usr/bin/env python3
"""Independent status checks for the Fork-8 architecture audit."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_causal_direct_limit_architectures_v001.py"
RESULT = ROOT / "results" / "causal_direct_limit_architecture_audit_v001.json"


def test_architecture_audit_remains_fail_closed() -> None:
    subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
    payload = json.loads(RESULT.read_text(encoding="ascii"))

    assert payload["target_values_used"] is False
    assert payload["coupling_evaluated"] is False
    assert payload["winner_or_ranking_emitted"] is False
    assert len(payload["decay_laws"]) == 5
    assert payload["covariance_selector"]["status"] == (
        "CLASS_LEVEL_SELECTOR_ONLY"
    )
    assert payload["covariance_selector"][
        "unique_microscopic_complex_selected"
    ] is False
    assert payload["covariance_selector"][
        "unique_spectral_measure_selected"
    ] is False

    exponents = {
        row["architecture"]: row["late_time_probability_exponent_fit"]
        for row in payload["decay_laws"]
    }
    assert 2.6 < exponents["A1_causal_half_line"] < 3.4
    assert 2.6 < exponents["A2_three_branch_causal_tree"] < 3.4
    assert 2.5 < exponents["A3_three_dimensional_spatial_lattice"] < 3.5
    assert 5.7 < exponents[
        "A4_Lorentz_covariant_causal_complex_continuum"
    ] < 6.3
    assert 1.9 < exponents["A5_effective_environment_continuum"] < 2.1

    proof = payload["direct_limit_existence_attempt"]
    assert proof[
        "bounded_degree_exhaustion_suffices_for_bounded_self_adjoint_limit"
    ] is True
    assert proof[
        "Lorentz_covariance_forces_unique_root_spectral_density"
    ] is False
    assert proof[
        "record_principles_derive_label_preserving_outgoing_tail_algebra"
    ] is False
    assert payload["fork_8_closed"] is False
    assert payload["hypothesis_promoted_to_principle"] is False
    assert payload["complete_parent_action_derived"] is False
    assert payload["alpha_computed"] is False
    assert payload["proof_authorized"] is False
