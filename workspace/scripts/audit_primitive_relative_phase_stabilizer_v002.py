#!/usr/bin/env python3
"""Regression audit for the corrected relative-phase stabilizer result."""

from __future__ import annotations

import cmath
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002.md"
PROVENANCE = ROOT / "provenance_inputs_v003.json"
PRIMITIVE = ROOT / "results" / "primitive_record_carrier_v001.json"
RESULT = ROOT / "results" / "primitive_relative_phase_stabilizer_v002.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_provenance() -> bool:
    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    for item in manifest["inputs"]:
        path = (ROOT / item["path"]).resolve()
        if not path.exists() or sha256(path) != item["sha256"]:
            return False
    return True


def relative_phase(theta_0: float, theta_1: float) -> complex:
    return cmath.exp(1j * (theta_1 - theta_0))


def character(winding: int, theta: float) -> complex:
    return cmath.exp(1j * winding * theta)


def preserves_ordered_projectors(
    matrix: tuple[tuple[complex, complex], tuple[complex, complex]],
    tolerance: float = 1e-14,
) -> bool:
    """A 2x2 unitary preserves both coordinate rays iff it is diagonal."""
    return abs(matrix[0][1]) < tolerance and abs(matrix[1][0]) < tolerance


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    primitive = json.loads(PRIMITIVE.read_text(encoding="utf-8"))

    diagonal_samples = (
        (
            (cmath.exp(0.2j), 0j),
            (0j, cmath.exp(-0.7j)),
        ),
        (
            (cmath.exp(-1.1j), 0j),
            (0j, cmath.exp(2.4j)),
        ),
    )
    mixing_sample = (
        (2**-0.5, 2**-0.5),
        (-2**-0.5, 2**-0.5),
    )

    quotient_errors: list[float] = []
    for theta_0, theta_1 in ((0.1, 0.9), (-0.7, 1.2), (2.3, -1.1)):
        base = relative_phase(theta_0, theta_1)
        for shift in (-4.2, 0.0, 0.37, 3.8):
            shifted = relative_phase(theta_0 + shift, theta_1 + shift)
            quotient_errors.append(abs(base - shifted))

    character_errors: list[float] = []
    for winding in (-3, -1, 0, 1, 4):
        for left, right in ((0.2, 0.7), (-1.1, 0.4), (2.0, -0.3)):
            character_errors.append(
                abs(
                    character(winding, left + right)
                    - character(winding, left)
                    * character(winding, right)
                )
            )

    required_true = (
        "endpoint_projectors_inherited = true",
        "reference_comparison_order_declared = true",
        "endpoint_ray_stabilizer_derived = true",
        "relative_lie_algebra_dimension = 1",
        "relative_character_lattice = Z",
    )
    required_false = (
        "passive_basis_freedom_is_physical_symmetry = false",
        "local_relative_frame_redundancy_derived = false",
        "physical_comparison_connection_derived = false",
        "unique_dynamical_connection_derived = false",
        "identification_with_unique_exterior_EM_connection_derived = false",
        "absolute_Maxwell_stiffness_selected = false",
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
        "all_hash_locked_pre_alpha_sources_match": verify_provenance(),
        "primitive_carrier_is_current": (
            primitive["overall"]
            == "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE"
        ),
        "primitive_unit_winding_is_explicitly_inherited": (
            primitive["primitive_action_character_winding"] == 1
        ),
        "diagonal_unitaries_preserve_ordered_endpoint_rays": all(
            preserves_ordered_projectors(matrix) for matrix in diagonal_samples
        ),
        "mixing_unitary_does_not_preserve_ordered_endpoint_rays": (
            not preserves_ordered_projectors(mixing_sample)
        ),
        "relative_phase_is_invariant_under_common_phase": (
            max(quotient_errors) < 2e-15
        ),
        "integer_characters_compose": max(character_errors) < 2e-15,
        "supported_statuses_present": all(
            phrase in note for phrase in required_true
        ),
        "unsupported_statuses_fail_closed": all(
            phrase in note for phrase in required_false
        ),
        "target_literal_guard_passes": not any(
            pattern.search(note) for pattern in target_patterns
        ),
        "no_invariant_matrix_rank_claim": (
            "primitive_relative_generator_rank" not in note
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY_LOCAL_CONNECTION_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_PRIMITIVE_RELATIVE_PHASE_STABILIZER_V002"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "maximum_common_phase_quotient_error": max(quotient_errors),
        "maximum_character_composition_error": max(character_errors),
        "endpoint_projectors_inherited": True,
        "reference_comparison_order_declared": True,
        "endpoint_ray_stabilizer_derived": True,
        "effective_projective_stabilizer": "U(1)",
        "relative_lie_algebra_dimension": 1,
        "relative_character_lattice": "Z",
        "primitive_unit_winding_inherited_conditionally": True,
        "passive_basis_freedom_is_physical_symmetry": False,
        "local_relative_frame_redundancy_derived": False,
        "physical_comparison_connection_derived": False,
        "unique_dynamical_connection_derived": False,
        "identification_with_unique_exterior_EM_connection_derived": False,
        "absolute_Maxwell_stiffness_selected": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "REGRESSION_GUARD_NOT_PHYSICAL_PREMISE_PROOF",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("physical_comparison_connection_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
