#!/usr/bin/env python3
"""Fail-closed verifier for the conditional transported write/tail candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md"
RESULT = ROOT / "results" / "r3_4_causal_transported_write_tail_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )
    require(
        stored["causal_transport_functional_equation_unique_given_rule"] is True,
        "Candidate transport equation was not solved",
    )
    require(
        stored["causal_transport_rule_derived_from_pinned_principles"] is False,
        "Underived transport rule was silently promoted",
    )
    require(
        stored["static_sum_fails_comoving_covariance"] is True,
        "Static negative control did not fail",
    )
    require(
        stored["static_sum_rejected_by_adopted_principles"] is False,
        "Static competitor was rejected without an adopted selector",
    )
    require(
        stored["candidate_first_opening_survives_free_tail_attachment"] is True,
        "Candidate did not reproduce its stated endpoint",
    )
    require(
        stored["physical_write_tail_join_derived"] is False,
        "Successful candidate was promoted to a physical derivation",
    )
    require(
        stored["free_outgoing_tail_generator_inherited_from_same_parent"] is False,
        "Tail inheritance was overclaimed",
    )
    require(
        stored["status"] == "CAUSAL_TRANSPORT_CONDITIONAL",
        "Conditional verdict was not retained",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(stored["proof_authorized"] is False, "Proof was authorized")
    print("PASS transported write/tail candidate remains fail-closed")


if __name__ == "__main__":
    main()
