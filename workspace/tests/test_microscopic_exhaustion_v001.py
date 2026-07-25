#!/usr/bin/env python3
"""Regression test for the microscopic-exhaustion identifiability gate."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_microscopic_exhaustion_v001.py"
RESULT = ROOT / "results" / "microscopic_exhaustion_v001.json"


class MicroscopicExhaustionGateTest(unittest.TestCase):
    def test_gate_passes_fail_closed(self) -> None:
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
            "PASS_CURRENT_PRE_ALPHA_PRINCIPLES_DO_NOT_DERIVE_MICROSCOPIC_EXHAUSTION_ALPHA_FALSE",
        )
        self.assertFalse(payload["microscopic_record_exhaustion_derived"])
        self.assertFalse(
            payload["complete_g_A_psi_record_specification_derived"]
        )
        self.assertFalse(payload["coupling_evaluation_authorized"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
