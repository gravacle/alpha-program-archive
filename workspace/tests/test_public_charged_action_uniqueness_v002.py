#!/usr/bin/env python3
"""Regression test for the corrected public-action gate."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_public_charged_action_uniqueness_v002.py"
RESULT = ROOT / "results" / "public_charged_action_uniqueness_v002.json"


class PublicChargedActionUniquenessV002Test(unittest.TestCase):
    def test_nonselection_status_is_fail_closed(self) -> None:
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
            "PASS_PUBLIC_ACTION_PREMISES_DO_NOT_SELECT_K_SCOPE_ONLY_ALPHA_FALSE",
        )
        self.assertEqual(
            payload["executable_role"],
            "REGRESSION_GUARD_NOT_PROOF_EVIDENCE",
        )
        self.assertFalse(payload["absolute_Maxwell_stiffness_selected"])
        self.assertFalse(payload["coupling_evaluation_authorized"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
