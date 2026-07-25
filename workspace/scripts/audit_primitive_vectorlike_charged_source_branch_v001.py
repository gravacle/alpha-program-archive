#!/usr/bin/env python3
"""Seal and anomaly audit for the primitive vectorlike source branch."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V001.md"
SEAL = ROOT / "PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V001.seal.sha256"
BUNDLE = ROOT / "results" / "local_projective_record_bundle_v001.json"
RESULT = ROOT / "results" / "primitive_vectorlike_charged_source_branch_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    sealed_hash, sealed_name = SEAL.read_text(encoding="utf-8").split()
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))

    charges = (1, -1)
    cubic_anomaly = sum(charge**3 for charge in charges)
    mixed_gravity_anomaly = sum(charges)
    single_charge_cubic_anomaly = 1**3
    single_charge_mixed_anomaly = 1

    required_false = (
        "spinor_source_derived_from_pre_alpha_record_principles = false",
        "universal_matter_spectrum_derived = false",
        "composite_spectrum_derived = false",
        "record_generated_mass_derived = false",
        "complete_Q_spec_frozen = false",
        "charged_determinant_evaluation_authorized = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    target_patterns = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )

    checks = {
        "source_branch_seal_matches": (
            sealed_name == NOTE.name and sealed_hash == sha256(NOTE)
        ),
        "level1_local_bundle_is_current": (
            bundle["overall"]
            == "PASS_LEVEL1_LOCAL_RECORD_BUNDLE_AUXILIARY_CONNECTION_ONLY_ALPHA_FALSE"
        ),
        "single_unit_weyl_source_is_anomalous": (
            single_charge_cubic_anomaly != 0
            and single_charge_mixed_anomaly != 0
        ),
        "minimal_vectorlike_pair_cancels_cubic_anomaly": cubic_anomaly == 0,
        "minimal_vectorlike_pair_cancels_mixed_gravity_anomaly": (
            mixed_gravity_anomaly == 0
        ),
        "branch_inputs_and_limits_are_disclosed": (
            "The existence of a spinor source is a branch input." in note
            and "Additional vectorlike pairs are consistent" in note
            and "are not proved impossible" in note
        ),
        "response_evaluation_remains_blocked": all(
            phrase in note for phrase in required_false
        ),
        "target_literal_guard_passes": not any(
            pattern.search(note) for pattern in target_patterns
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_PRIMITIVE_VECTORLIKE_SOURCE_BRANCH_SEALED_QSPEC_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_PRIMITIVE_VECTORLIKE_SOURCE_BRANCH_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "branch_sha256": sha256(NOTE),
        "primitive_charge_magnitude": 1,
        "primitive_vectorlike_pair_count": 1,
        "primitive_source_representation": "four_component_Dirac",
        "primitive_source_statistics": "fermionic",
        "primitive_bare_mass": 0,
        "cubic_U1_anomaly": cubic_anomaly,
        "mixed_gravity_U1_anomaly": mixed_gravity_anomaly,
        "spinor_source_derived_from_pre_alpha_record_principles": False,
        "universal_matter_spectrum_derived": False,
        "complete_Q_spec_frozen": False,
        "charged_determinant_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "SEAL_AND_ANOMALY_REGRESSION_GUARD_NOT_BRANCH_UNIQUENESS_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("charged_determinant_evaluation_authorized=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
