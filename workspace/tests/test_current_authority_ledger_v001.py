#!/usr/bin/env python3
"""Regression test for the clean-room authority ledger."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_current_authority_ledger_v001.py"
RESULT = ROOT / "results" / "current_authority_ledger_v001.json"


class CurrentAuthorityLedgerTest(unittest.TestCase):
    def test_retired_results_are_not_current_authority(self) -> None:
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
            "PASS_CURRENT_AUTHORITY_EXCLUDES_RETIRED_RESULTS_ALPHA_FALSE",
        )
        self.assertFalse(payload["coupling_evaluation_authorized"])
        self.assertFalse(payload["alpha_computed"])
        self.assertFalse(payload["proof_authorized"])


if __name__ == "__main__":
    unittest.main()
