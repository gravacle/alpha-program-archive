#!/usr/bin/env python3
"""Execute the sealed completed-effect extension of the primitive T7 block."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_COMPLETED_EFFECT_ZERO_BASELINE_SPEC_V001.md"
SPEC_SHA256 = "5039541c716d9c30f07ef613060d6c31a15439bb9fbfb53868d6786cdaf30976"
OUT = ROOT / "stage8_execution/work/T07_completed_effect_zero_baseline.json"

AUTHORITIES = {
    "stage8_execution/t0_lineage/core_scripts/43_gate4_covector_ray_v001.py":
        "b8235b89ac2f7fed5ba913df5cc67f828da1c8b374ae35cd1b29a7c7040bf8d6",
    "STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_SPEC_V001.md":
        "63116a5d2b6f1e557db421e9bbd9e8363f85c84ac04c5d54cb7e7dd314aab544",
    "stage8_execution/work/T07_primitive_connected_lift.json":
        "1a6c92719410e49c4abb7770abe86e403384a2b479c9e5b528ce80d26dfce0ab",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum((value * vector[j] for j, value in enumerate(row)), Fraction(0))
        for row in matrix
    ]


def norm_square(vector: list[Fraction]) -> Fraction:
    return sum((value * value for value in vector), Fraction(0))


def main() -> None:
    if sha256(SPEC) != SPEC_SHA256:
        raise RuntimeError("sealed spec hash mismatch")
    for relative, expected in AUTHORITIES.items():
        if sha256(ROOT / relative) != expected:
            raise RuntimeError(f"authority hash mismatch: {relative}")

    root = [Fraction(1), Fraction(0), Fraction(0)]
    effect = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(1, 4)],
        [Fraction(0), Fraction(1, 4), Fraction(1, 2)],
    ]
    effect_root = matvec(effect, root)
    no_output_value = sum(
        (root[i] * effect_root[i] for i in range(3)), Fraction(0)
    )

    # One exact subordinate Kraus representative supported only on the
    # completed sector. The theorem in the result covers every K^*K <= E.
    kraus = [
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 2)],
    ]
    kraus_root = matvec(kraus, root)

    # Negative control: violating no-output permits a nonzero baseline.
    bad_effect = [
        [Fraction(1, 4), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 2)],
    ]
    bad_root = matvec(bad_effect, root)
    bad_value = sum(
        (root[i] * bad_root[i] for i in range(3)), Fraction(0)
    )

    checks = {
        "effect_root_exactly_zero": all(value == 0 for value in effect_root),
        "no_output_expectation_exactly_zero": no_output_value == 0,
        "subordinate_kraus_root_exactly_zero":
            norm_square(kraus_root) == 0,
        "negative_control_has_output": bad_value == Fraction(1, 4),
    }
    if not all(checks.values()):
        raise RuntimeError("completed-effect regression failed")

    result = {
        "schema": "stage8_t7_completed_effect_zero_baseline_v001",
        "spec_sha256": SPEC_SHA256,
        "checks": checks,
        "verdict": "COMPLETED_EFFECT_ESCAPE_EXCLUDED",
        "theorem": (
            "For E>=0, <r|E|r>=||E^(1/2)r||^2=0 implies E r=0. "
            "If K^*K<=E, then ||K r||^2<=<r|E|r>=0."
        ),
        "connected_primitive_completed_endpoint_derived": False,
        "connected_primitive_amplitude_derived": False,
        "kappa_record_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
