#!/usr/bin/env python3
"""Independently verify the fail-closed causal-line lift result."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution/work/T07_causal_line_connection_return_lift.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = result["Q3_Q4_chain_execution"]

    require(len(rows) == 8, "Expected N=1,...,8")
    for row in rows:
        count = row["N"]
        expected = Fraction(-1, 2) ** (count - 1)
        require(
            Fraction(row["baseline_scalar_exact"]) == expected,
            f"Conditional chain identity failed at N={count}",
        )
        require(
            row["returned_endomorphism_error_square_exact"] == "0",
            f"Returned endomorphism mismatch at N={count}",
        )
        require(
            row["connection_composition_error_square_exact"] == "0",
            f"Connection composition mismatch at N={count}",
        )

    q2 = result["Q2_connection_return"]
    physical = result["physical_parent_audit"]
    require(
        q2["incidence_chain_partial_isometry_algebra_derived"] is True,
        "Conditional incidence algebra was not retained",
    )
    require(
        q2["physical_source_line_transport_derived"] is False,
        "Physical source-line transport was overclaimed",
    )
    require(
        physical["finite_lorentzian_parent_used"] is False,
        "Ideal chain was mislabeled as the finite Lorentzian parent",
    )
    require(
        physical["conditional_projector_chain_identity_derived"] is True,
        "Useful conditional identity was lost",
    )
    require(
        result["overall_verdict"]
        == "CAUSAL_LINE_CONNECTION_RETURN_LIFT_BLOCKED",
        "Result did not fail closed",
    )
    require(
        result["finite_relayed_connection_return_amplitude_derived"] is False,
        "Physical amplitude was overclaimed",
    )
    require(
        result["state_expectation_C1_superseded_for_primitive_line_amplitude"]
        is False,
        "Failed state-expectation result was improperly superseded",
    )
    for flag in (
        "connected_primitive_amplitude_derived",
        "volume_uniform_zero_free_neighborhood_proved",
        "connected_linked_cluster_density_proved",
        "kappa_record_computed",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        require(result[flag] is False, f"Protected flag promoted: {flag}")

    print("PASS fail-closed causal-line connection-return verification")


if __name__ == "__main__":
    main()
