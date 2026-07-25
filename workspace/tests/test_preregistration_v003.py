from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_preregistration_v003.py"
RESULT = ROOT / "results" / "preregistration_v003_audit.json"


class PreregistrationV003Test(unittest.TestCase):
    def test_all_external_provenance_sources_resolve_and_match(self) -> None:
        subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, check=True)
        payload = json.loads(RESULT.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["overall"],
            "PASS_V003_RESOLVED_PROVENANCE_SYMBOLIC_ONLY_ALPHA_FALSE",
        )
        self.assertEqual(payload["failed_checks"], [])
        self.assertIs(
            payload["all_pre_alpha_source_paths_resolved_and_hash_checked"], True
        )
        self.assertIs(payload["candidate_action_evaluation_authorized"], False)
        self.assertEqual(payload["current_claim_ceiling"], "LEVEL_1")
        self.assertIs(payload["coupling_evaluation_authorized"], False)
        self.assertIs(payload["alpha_computed"], False)


if __name__ == "__main__":
    unittest.main()
