#!/usr/bin/env python3
"""Regression test for the public charged-action uniqueness gate."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_public_charged_action_uniqueness_v001.py"
RESULT = ROOT / "results" / "public_charged_action_uniqueness_v001.json"


class PublicChargedActionUniquenessGateTest(unittest.TestCase):
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
            "PASS_PRE_ALPHA_PRINCIPLES_DO_NOT_SELECT_ABSOLUTE_CHARGED_ACTION_ALPHA_FALSE",
        )
        self.assertFalse(payload["absolute_Maxwell_stiffness_selected"])
        self.assertFalse(payload["complete_public_charged_action_unique"])
        self.assertFalse(payload["coupling_evaluation_authorized"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
