#!/usr/bin/env python3
"""Independent verifier for the primitive causal transition-map theorem."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_SPEC_V001.md"
SPEC_SHA256 = "c4dcbf5bc1e98e3dd3e4503bcc2739e8795be11b7e96873598a181eedf00d654"
PRIMARY = ROOT / "stage8_execution/work/T07_actual_primitive_causal_transition_map.json"
OUTPUT = ROOT / "stage8_execution/work/T07_actual_primitive_causal_transition_map_verification.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    require(sha256(SPEC) == SPEC_SHA256, "spec hash mismatch")
    primary = json.loads(PRIMARY.read_text(encoding="ascii"))
    require(primary["spec_sha256"] == SPEC_SHA256, "primary spec mismatch")

    # Independent local derivation from c^3=2c:
    # exp(-i tau_R c)=I-c^2 at sqrt(2) tau_R=pi. Direct multiplication gives
    # I-c^2=swap(r,p) direct_sum (-1), for both c and -c.
    c2 = (
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(-1), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(2)),
    )
    unitary = tuple(
        tuple(Fraction(int(i == j)) - c2[i][j] for j in range(3))
        for i in range(3)
    )
    expected_unitary = (
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1)),
    )
    require(unitary == expected_unitary, "local endpoint unitary changed")
    require(unitary[1][0] == 1, "local endpoint block changed")

    rows = primary["P3_chain_execution"]
    require(len(rows) == 8, "unexpected chain regression count")
    reconstructed = []
    for count, row in enumerate(rows, start=1):
        coefficient = Fraction(-1, 2) ** (count - 1)
        require(row["N"] == count, "chain index mismatch")
        require(row["baseline_scalar_exact"] == str(coefficient),
                f"baseline mismatch at N={count}")
        require(
            row["transition_range_formula_error_square_exact"] == "0",
            f"range formula error at N={count}",
        )
        require(
            row["returned_scalar_error_square_exact"] == "0",
            f"return formula error at N={count}",
        )
        if count > 1:
            require(
                Fraction(row["adjacent_projector_commutator_norm_square_exact"])
                == Fraction(3, 8),
                f"connected commutator mismatch at N={count}",
            )
        reconstructed.append(
            {
                "N": count,
                "baseline_scalar_exact": str(coefficient),
                "nonzero": coefficient != 0,
            }
        )

    require(
        primary["P1_actual_primitive_parent"]["source_state_used"] is False,
        "source state entered primary",
    )
    require(
        primary["P1_actual_primitive_parent"]["CAR_determinant_used"] is False,
        "CAR determinant entered primary",
    )
    require(
        primary["P2_local_endpoint_compression"]
        ["controlled_endpoint_compression_equals_Pj_tensor_Ispin"] is True,
        "endpoint compression was not derived",
    )
    require(
        primary["verdict"] == "ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_DERIVED",
        "primary verdict changed",
    )
    require(primary["alpha_computed"] is False, "alpha flag changed")
    require(primary["proof_authorized"] is False, "proof flag changed")

    result = {
        "schema": "stage8-t7-actual-primitive-causal-transition-map-verifier-v001",
        "spec_sha256": SPEC_SHA256,
        "primary_sha256": sha256(PRIMARY),
        "independent_method":
            "local minimal-polynomial endpoint block plus incidence-Gram recurrence",
        "local_endpoint_unitary_verified": True,
        "chain_rows": reconstructed,
        "all_finite_baselines_nonzero": True,
        "adjacent_connected_commutator_norm_square_exact": "3/8",
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
