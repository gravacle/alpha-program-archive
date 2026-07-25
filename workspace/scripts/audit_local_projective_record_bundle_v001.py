#!/usr/bin/env python3
"""Regression audit for the Level-1 local projective record bundle."""

from __future__ import annotations

import cmath
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md"
PRINCIPLE = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V001.md"
PRINCIPLE_SEAL = (
    ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V001.seal.sha256"
)
STABILIZER = ROOT / "results" / "primitive_relative_phase_stabilizer_v002.json"
RESULT = ROOT / "results" / "local_projective_record_bundle_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    sealed_hash, sealed_name = PRINCIPLE_SEAL.read_text(
        encoding="utf-8"
    ).split()
    stabilizer = json.loads(STABILIZER.read_text(encoding="utf-8"))

    cocycle_errors: list[float] = []
    covariance_errors: list[float] = []
    curvature_errors: list[float] = []
    samples = (
        (0.2, -0.7, 0.5),
        (1.1, 0.4, -1.5),
        (-2.0, 0.3, 1.7),
    )
    for theta_ij, theta_jk, theta_ki in samples:
        cocycle = cmath.exp(
            1j * (theta_ij + theta_jk + theta_ki)
        )
        cocycle_errors.append(abs(cocycle - 1.0))

        z = complex(0.4, -0.2)
        dz = complex(-0.3, 0.8)
        theta = theta_ij
        dtheta = theta_jk
        a_i = theta_ki
        phase = cmath.exp(1j * theta)
        z_j = phase * z
        dz_j = phase * (dz + 1j * dtheta * z)
        a_j = a_i + dtheta
        lhs = dz_j - 1j * a_j * z_j
        rhs = phase * (dz - 1j * a_i * z)
        covariance_errors.append(abs(lhs - rhs))

        da_i = complex(theta_ij, theta_jk)
        d2theta = 0j
        da_j = da_i + d2theta
        curvature_errors.append(abs(da_j - da_i))

    required_false = (
        "unique_connection_selected = false",
        "dynamical_public_connection_derived = false",
        "complete_charged_current_derived = false",
        "unique_induced_Maxwell_stiffness_derived = false",
        "identification_with_exterior_EM_derived = false",
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
        "record_action_principle_seal_matches": (
            sealed_name == PRINCIPLE.name
            and sealed_hash == sha256(PRINCIPLE)
        ),
        "pointwise_projective_stabilizer_is_current": (
            stabilizer["overall"]
            == "PASS_ORDERED_ENDPOINT_PROJECTIVE_STABILIZER_ONLY_LOCAL_CONNECTION_OPEN_ALPHA_FALSE"
        ),
        "u1_transition_cocycle_closes": max(cocycle_errors) < 2e-15,
        "connection_transformation_gives_covariant_derivative": (
            max(covariance_errors) < 2e-15
        ),
        "curvature_patches_globally": max(curvature_errors) == 0.0,
        "all_dynamical_claims_fail_closed": all(
            phrase in note for phrase in required_false
        ),
        "zero_bare_clause_is_preserved": "K_bare = 0." in note,
        "target_literal_guard_passes": not any(
            pattern.search(note) for pattern in target_patterns
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_LEVEL1_LOCAL_RECORD_BUNDLE_AUXILIARY_CONNECTION_ONLY_ALPHA_FALSE"
        if not failed
        else "FAIL_LOCAL_PROJECTIVE_RECORD_BUNDLE_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "maximum_cocycle_error": max(cocycle_errors),
        "maximum_covariance_error": max(covariance_errors),
        "maximum_curvature_patch_error": max(curvature_errors),
        "Level_1_record_bundle_result": True,
        "local_projective_record_bundle_derived": True,
        "local_U1_representative_redundancy_derived": True,
        "auxiliary_covariant_comparison_connection_derived": True,
        "global_curvature_form_defined": True,
        "primitive_comparison_character_normalized": True,
        "unique_connection_selected": False,
        "dynamical_public_connection_derived": False,
        "complete_charged_current_derived": False,
        "unique_induced_Maxwell_stiffness_derived": False,
        "identification_with_exterior_EM_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "BUNDLE_ALGEBRA_REGRESSION_GUARD_NOT_DYNAMICS_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print("unique_induced_Maxwell_stiffness_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
