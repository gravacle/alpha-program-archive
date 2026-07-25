#!/usr/bin/env python3
"""Independent verifier for the Stage-8 T7 connected analytic audit."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution" / "work" / "T07_connected_analytic_closure.json"
SPEC = ROOT / "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.md"
SPEC_SEAL = ROOT / "STAGE8_T7_CONNECTED_ANALYTIC_CLOSURE_SPEC_V001.seal.sha256"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    data = json.loads(RESULT.read_text())
    expected_spec = SPEC_SEAL.read_text().split()[0]
    require(sha256(SPEC) == expected_spec, "Spec seal mismatch")
    require(data["custody"]["spec_sha256"] == expected_spec, "Result/spec mismatch")
    require(
        all(row["verified"] for row in data["custody"]["authority_rows"]),
        "Unverified authority",
    )
    require(
        all(row["present"] for row in data["open_status_rows"]),
        "Missing inherited open statement",
    )

    witness = data["C3_uniform_zero_free"]["necessity_witness"]
    tau = math.pi / math.sqrt(2.0)
    recomputed = [
        math.pi / (2.0 * tau * int(n)) for n in witness["volumes"]
    ]
    require(
        max(abs(a - b) for a, b in zip(recomputed, witness["first_zeros"]))
        < 1e-15,
        "GHZ first-zero recomputation failed",
    )
    require(
        all(
            recomputed[index + 1] < recomputed[index]
            for index in range(len(recomputed) - 1)
        ),
        "First zeros do not approach the origin",
    )

    require(data["C1_connected_preparation"]["pass"] is False, "C1 overpromoted")
    require(data["C2_finite_Duhamel"]["pass"] is False, "C2 overpromoted")
    require(data["C3_uniform_zero_free"]["pass"] is False, "C3 overpromoted")
    require(data["C4_linked_cluster_density"]["pass"] is False, "C4 overpromoted")
    require(data["C5_thermodynamic_Duhamel"]["pass"] is False, "C5 overpromoted")
    require(data["verdict"] == "T7_CONNECTED_PREPARATION_BLOCKED", "Bad verdict")

    protected = (
        "volume_uniform_zero_free_neighborhood_proved",
        "connected_linked_cluster_density_proved",
        "Duhamel_intensive_Hessian_equality_proved",
        "kappa_record_computed",
        "physical_charged_amplitude_computed",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    )
    require(all(data[key] is False for key in protected), "Protected flag changed")
    require(data["target_value_used"] is False, "Target access detected")
    require(data["new_principle_adopted"] is False, "Unexpected principle adoption")

    print(json.dumps({
        "schema": "stage8-t7-connected-analytic-verification-v001",
        "result_sha256": sha256(RESULT),
        "spec_sha256": sha256(SPEC),
        "independent_zero_sequence_recomputed": True,
        "inherited_open_statuses_verified": True,
        "protected_flags_verified_false": True,
        "verdict_verified": True,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
