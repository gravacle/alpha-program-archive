#!/usr/bin/env python3
"""Regression audit for public charged-action non-selection v002."""

from __future__ import annotations

import hashlib
import json
import re
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PUBLIC_CHARGED_ACTION_UNIQUENESS_GATE_V002.md"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
EXHAUSTION = ROOT / "results" / "microscopic_exhaustion_v002.json"
SEAL = ROOT / "PREREGISTRATION_V003.seal.sha256"
RESULT = ROOT / "results" / "public_charged_action_uniqueness_v002.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal() -> bool:
    rows = SEAL.read_text(encoding="utf-8").splitlines()
    if not rows:
        return False
    for row in rows:
        expected, relative = row.split(maxsplit=1)
        sealed_path = (ROOT / relative.strip()).resolve()
        if not sealed_path.exists() or sha256(sealed_path) != expected:
            return False
    return True


def verify_provenance() -> bool:
    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    for item in manifest["inputs"]:
        path = (ROOT / item["path"]).resolve()
        if not path.exists() or sha256(path) != item["sha256"]:
            return False
    return True


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    exhaustion = json.loads(EXHAUSTION.read_text(encoding="utf-8"))

    stiffnesses = tuple(
        Decimal(value) for value in ("0.25", "0.5", "1", "2", "8", "32")
    )
    with localcontext() as context:
        context.prec = 80
        pi = Decimal(
            "3.14159265358979323846264338327950288419716939937510"
        )
        coupling_values = [Decimal(1) / (4 * pi * k) for k in stiffnesses]

    required_text = (
        "At a declared response scale `mu`",
        "The measured low-energy constant requires Thomson-limit matching",
        "no-go against a future Gravacle dynamical selector",
        "This does **not** assert that arbitrary `c` values are all generated",
        "It is a regression guard.",
    )
    missing_text = [phrase for phrase in required_text if phrase not in note]
    required_status = (
        "absolute_Maxwell_stiffness_selected = false",
        "zero_bare_alone_selects_finite_induced_coefficient = false",
        "complete_public_charged_action_unique = false",
        "unique_finite_coincident_extension_derived = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    missing_status = [
        phrase for phrase in required_status if phrase not in note
    ]
    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [
        pattern.pattern for pattern in forbidden if pattern.search(note)
    ]

    checks = {
        "sealed_v003_authority_unchanged": verify_seal(),
        "all_hash_locked_pre_alpha_sources_match": verify_provenance(),
        "microscopic_v001_countermodel_is_retired": (
            exhaustion["overall"]
            == "PASS_V001_COUNTERMODEL_PROOF_RETIRED_SCOPE_DIAGNOSTIC_ONLY_ALPHA_FALSE"
        ),
        "hostile_review_qualifications_are_present": not missing_text,
        "positive_stiffness_family_has_distinct_conventional_couplings": (
            all(k > 0 for k in stiffnesses)
            and len(set(coupling_values)) == len(coupling_values)
        ),
        "scope_flags_fail_closed": not missing_status,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_PUBLIC_ACTION_PREMISES_DO_NOT_SELECT_K_SCOPE_ONLY_ALPHA_FALSE"
        if not failed
        else "FAIL_PUBLIC_CHARGED_ACTION_UNIQUENESS_V002_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "executable_role": "REGRESSION_GUARD_NOT_PROOF_EVIDENCE",
        "absolute_Maxwell_stiffness_selected": False,
        "zero_bare_alone_selects_finite_induced_coefficient": False,
        "complete_public_charged_action_unique": False,
        "unique_finite_coincident_extension_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("executable_role=REGRESSION_GUARD_NOT_PROOF_EVIDENCE")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
