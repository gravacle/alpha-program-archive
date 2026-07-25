#!/usr/bin/env python3
"""Regression test for the v002 microscopic-exhaustion correction."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_microscopic_exhaustion_v002.py"
RESULT = ROOT / "results" / "microscopic_exhaustion_v002.json"


class MicroscopicExhaustionCorrectionTest(unittest.TestCase):
    def test_failed_v001_proof_is_retired(self) -> None:
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
            "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE",
        )
        self.assertFalse(payload["v001_Gaussian_countermodel_proof_valid"])
        self.assertFalse(payload["microscopic_nonentailment_theorem_proved"])
        self.assertFalse(payload["coupling_evaluation_authorized"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
