#!/usr/bin/env python3
"""Fail-closed checks for the redundant-record direct-limit gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_causal_direct_limit_redundant_record_v001.py"
RESULT = ROOT / "results" / "causal_direct_limit_redundant_record_v001.json"


def test_redundant_record_gate_is_scoped() -> None:
    subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
    payload = json.loads(RESULT.read_text(encoding="ascii"))

    assert payload["target_values_used"] is False
    assert payload["coupling_evaluated"] is False
    assert payload["conditional_environment_sectors_orthogonal"] is True
    assert payload["redundancy_grows_without_new_coefficient"] is True
    assert payload["central_sequence_bound_converges_to_zero"] is True
    assert payload[
        "outgoing_record_recoverability_derived_under_adopted_write_rule"
    ] is True
    assert payload["write_rule_itself_derived_here"] is False
    assert payload["ready_state_boundary_condition_derived"] is False
    assert payload["unique_covariant_spectral_measure_derived"] is False
    assert payload["fork_8_closed"] is False
    assert payload["hypothesis_promoted_to_principle"] is False
    assert payload["complete_parent_action_derived"] is False
    assert payload["alpha_computed"] is False
    assert payload["proof_authorized"] is False
