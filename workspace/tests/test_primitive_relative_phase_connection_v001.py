#!/usr/bin/env python3
"""Regression test for the primitive relative-phase connection."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_primitive_relative_phase_connection_v001.py"
RESULT = ROOT / "results" / "primitive_relative_phase_connection_v001.json"


class PrimitiveRelativePhaseConnectionTest(unittest.TestCase):
    def test_group_derivation_keeps_dynamics_open(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(RESULT.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["overall"],
            "PASS_PRIMITIVE_RELATIVE_PHASE_CONNECTION_EM_IDENTIFICATION_OPEN_ALPHA_FALSE",
        )
        self.assertTrue(payload["primitive_relative_phase_group_derived"])
        self.assertTrue(payload["local_record_comparison_connection_derived"])
        self.assertFalse(
            payload["identification_with_unique_exterior_EM_connection_derived"]
        )
        self.assertFalse(payload["absolute_Maxwell_stiffness_selected"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
