#!/usr/bin/env python3
"""Audit the response carried by the primitive causal transition map."""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ACTUAL_PRIMITIVE_TRANSITION_RESPONSE_AUDIT_SPEC_V001.md"
SPEC_SHA256 = "8b53704d5ba0f49bec6c385984ea8d68d00a04f218c0db47092e5890bdbe127d"
OUTPUT = ROOT / "stage8_execution/work/T07_actual_primitive_transition_response_audit.json"

PINNED = {
    "STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_SPEC_V001.md":
        "c4dcbf5bc1e98e3dd3e4503bcc2739e8795be11b7e96873598a181eedf00d654",
    "scripts/derive_stage8_t7_actual_primitive_causal_transition_map_v001.py":
        "f04a54f4b52489e5e67eba3445b54a2028a947828204674ad1fbcb17d19be091",
    "stage8_execution/work/T07_actual_primitive_causal_transition_map.json":
        "3f7191c817435104f16c9e48fc43b4cd6f734417d0dcdc99add5acffc46b829d",
    "scripts/verify_stage8_t7_actual_primitive_causal_transition_map_v001.py":
        "0ece7cdb1b2a947dc50a0f9a961a568dd708ff60cf828767ba1bf3cd81964e8f",
    "stage8_execution/work/T07_actual_primitive_causal_transition_map_verification.json":
        "3a722c3867d90b664ba32420b75f2ff213f7f7bbce53e247e4fc94297a59c776",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def adjacent_overlap(previous_phase: float) -> complex:
    return -0.5 * cmath.exp(1j * previous_phase)


def normalized_amplitude(phases: tuple[float, ...]) -> complex:
    if len(phases) <= 1:
        return 1.0 + 0.0j
    amplitude = 1.0 + 0.0j
    baseline = 1.0
    for previous_phase in phases[:-1]:
        amplitude *= adjacent_overlap(previous_phase)
        baseline *= -0.5
    return amplitude / baseline


def gamma_modulus(phases: tuple[float, ...]) -> float:
    return -math.log(abs(normalized_amplitude(phases)))


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    verified = {}
    for relative, expected in PINNED.items():
        actual = sha256(ROOT / relative)
        require(actual == expected, f"candidate drift: {relative}")
        verified[relative] = actual

    rows = []
    maximum_modulus_error = 0.0
    maximum_gamma = 0.0
    maximum_hessian = 0.0
    step = 1e-4
    for count in range(1, 65):
        phases = tuple(
            0.37 * math.sin((index + 1) * 0.61)
            for index in range(count)
        )
        value = normalized_amplitude(phases)
        modulus_error = abs(abs(value) - 1.0)
        gamma = abs(gamma_modulus(phases))

        plus = list(phases)
        minus = list(phases)
        if phases:
            plus[0] += step
            minus[0] -= step
        hessian = abs(
            (
                gamma_modulus(tuple(plus))
                - 2.0 * gamma_modulus(phases)
                + gamma_modulus(tuple(minus))
            )
            / (step * step)
        )
        maximum_modulus_error = max(maximum_modulus_error, modulus_error)
        maximum_gamma = max(maximum_gamma, gamma)
        maximum_hessian = max(maximum_hessian, hessian)
        rows.append(
            {
                "N": count,
                "normalized_amplitude_real": value.real,
                "normalized_amplitude_imag": value.imag,
                "modulus_error": modulus_error,
                "gamma_abs": gamma,
                "finite_difference_hessian_abs": hessian,
            }
        )

    # The exact conclusion follows algebraically from
    # |<u_j(A),u_(j-1)(A)>|=1/2, not from these floating checks.
    require(maximum_modulus_error < 2e-15, "unit modulus regression failed")
    require(maximum_gamma < 2e-15, "nonzero Gamma regression")
    require(maximum_hessian < 1e-6, "nonzero Hessian regression")

    result = {
        "schema": "stage8-t7-actual-primitive-transition-response-audit-v001",
        "spec_sha256": SPEC_SHA256,
        "candidate_hashes_verified": verified,
        "target_value_used": False,
        "A1_exact_adjacent_overlap":
            "<u_j(A_j),u_(j-1)(A_(j-1))>=-(1/2)exp(i A_(j-1))",
        "A1_exact_overlap_modulus": "1/2",
        "A2_exact_normalized_amplitude":
            "Z_N(A)=exp(i sum_(j=0)^(N-2) A_j), up to the fixed return convention",
        "A2_exact_normalized_modulus": "1",
        "A2_exact_Gamma": "0",
        "A2_exact_first_derivative_of_Gamma": "0",
        "A2_exact_Hessian_of_Gamma": "0",
        "A2_exact_intensive_Hessian": "0",
        "numerical_regression": {
            "N_range": [1, 64],
            "maximum_modulus_error": maximum_modulus_error,
            "maximum_Gamma_abs": maximum_gamma,
            "maximum_finite_difference_Hessian_abs": maximum_hessian,
            "rows": rows,
        },
        "verdict": "OPEN_LINE_HOLONOMY_ZERO_STIFFNESS",
        "finite_connected_transition_map_retained": True,
        "nonzero_primitive_response_survives": False,
        "volume_uniform_zero_free_neighborhood_proved_for_this_map": True,
        "connected_linked_cluster_density": "zero density",
        "Duhamel_intensive_Hessian_for_this_map": "zero",
        "kappa_record_computed": False,
        "gate_routes_to_blocked_exact_zero": True,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
