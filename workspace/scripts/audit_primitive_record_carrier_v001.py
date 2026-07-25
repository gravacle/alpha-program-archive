#!/usr/bin/env python3
"""Audit the primitive record carrier and additive-action kinematics."""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PRIMITIVE_RECORD_CARRIER_AND_KINEMATICS_V001.md"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
AUTHORITY = ROOT / "results" / "preregistration_v003_audit.json"
RESULT = ROOT / "results" / "primitive_record_carrier_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matmul(
    left: tuple[tuple[complex, ...], ...],
    right: tuple[tuple[complex, ...], ...],
) -> tuple[tuple[complex, ...], ...]:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))

    # Real orientation generator written as a complex-valued exact matrix.
    j = ((0j, -1 + 0j), (1 + 0j, 0j))
    j_squared = matmul(j, j)
    minus_identity = ((-1 + 0j, 0j), (0j, -1 + 0j))

    phases = (0.17, 0.63, 1.41)
    composition_errors = []
    for left in phases:
        for right in phases:
            direct = cmath.exp(1j * (left + right))
            composed = cmath.exp(1j * left) * cmath.exp(1j * right)
            composition_errors.append(abs(direct - composed))

    overlap_zero = abs((1 + cmath.exp(0j)) / 2)
    overlap_half_turn = abs((1 + cmath.exp(1j * math.pi)) / 2)

    source_rows = []
    for item in provenance["inputs"]:
        path = (ROOT / item["path"]).resolve()
        actual = sha256(path)
        source_rows.append(actual == item["sha256"])

    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [pattern.pattern for pattern in forbidden if pattern.search(note)]

    required = (
        "complete_multi_handle_record_carrier_derived = false",
        "complete_g_A_psi_record_action_derived = false",
        "unique_UV_completion_selected = false",
        "candidate_action_evaluation_authorized = false",
        "alpha_computed = false",
    )
    missing = [phrase for phrase in required if phrase not in note]
    checks = {
        "v003_resolved_provenance_authority_passes": (
            authority["overall"]
            == "PASS_V003_RESOLVED_PROVENANCE_SYMBOLIC_ONLY_ALPHA_FALSE"
        ),
        "all_pre_alpha_source_hashes_still_match": all(source_rows),
        "orientation_generator_squares_to_minus_identity": (
            j_squared == minus_identity
        ),
        "additive_action_representation_composes": (
            max(composition_errors) < 1e-15
        ),
        "comparison_overlap_has_expected_endpoints": (
            abs(overlap_zero - 1) < 1e-15 and overlap_half_turn < 1e-15
        ),
        "scope_remains_primitive_not_complete": not missing,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE"
        if not failed
        else "FAIL_PRIMITIVE_RECORD_CARRIER_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "target_literal_hits": target_hits,
        "primitive_single_handle_real_carrier_dimension": 2,
        "primitive_single_handle_order_unit_dimension": 4,
        "primitive_action_character_winding": 1,
        "primitive_comparator_kinematics_derived": True,
        "complete_multi_handle_record_carrier_derived": False,
        "complete_g_A_psi_record_action_derived": False,
        "unique_UV_completion_selected": False,
        "complete_quantum_specification_frozen": False,
        "candidate_action_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "coupling_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(overall)
    print("complete_g_A_psi_record_action_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

