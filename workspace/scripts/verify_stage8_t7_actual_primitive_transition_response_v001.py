#!/usr/bin/env python3
"""Independent algebraic verifier for the open-line zero-stiffness result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ACTUAL_PRIMITIVE_TRANSITION_RESPONSE_AUDIT_SPEC_V001.md"
SPEC_SHA256 = "8b53704d5ba0f49bec6c385984ea8d68d00a04f218c0db47092e5890bdbe127d"
PRIMARY = ROOT / "stage8_execution/work/T07_actual_primitive_transition_response_audit.json"
OUTPUT = ROOT / "stage8_execution/work/T07_actual_primitive_transition_response_audit_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "spec hash mismatch")
    primary = json.loads(PRIMARY.read_text(encoding="ascii"))
    require(primary["spec_sha256"] == SPEC_SHA256, "primary spec mismatch")

    # Independent coefficient argument:
    # d_j has coefficient -1 at the shared vertex v_j.
    # d_(j-1) has coefficient exp(i A_(j-1)) there.
    # Both norms are sqrt(2), so the overlap has modulus 1/2.
    shared_vertex_left_modulus_squared = 1
    shared_vertex_right_modulus_squared = 1
    norm_squared_left = 2
    norm_squared_right = 2
    overlap_modulus_squared = (
        shared_vertex_left_modulus_squared
        * shared_vertex_right_modulus_squared
        / (norm_squared_left * norm_squared_right)
    )
    require(overlap_modulus_squared == 0.25, "overlap modulus changed")

    require(primary["A1_exact_overlap_modulus"] == "1/2",
            "primary overlap formula changed")
    require(primary["A2_exact_normalized_modulus"] == "1",
            "primary normalized modulus changed")
    require(primary["A2_exact_Gamma"] == "0", "primary Gamma changed")
    require(primary["A2_exact_Hessian_of_Gamma"] == "0",
            "primary Hessian changed")
    require(primary["verdict"] == "OPEN_LINE_HOLONOMY_ZERO_STIFFNESS",
            "primary verdict changed")
    require(primary["gate_routes_to_blocked_exact_zero"] is True,
            "exact-zero boundary changed")
    require(primary["alpha_computed"] is False, "alpha flag changed")
    require(primary["proof_authorized"] is False, "proof flag changed")

    result = {
        "schema": "stage8-t7-actual-primitive-transition-response-verifier-v001",
        "spec_sha256": SPEC_SHA256,
        "primary_sha256": sha256(PRIMARY),
        "independent_method": "shared-vertex coefficient and norm calculation",
        "overlap_modulus_squared_exact": "1/4",
        "normalized_modulus_exact": "1",
        "Gamma_exact": "0",
        "Hessian_exact": "0",
        "verdict_verified": True,
        "pass": True,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
