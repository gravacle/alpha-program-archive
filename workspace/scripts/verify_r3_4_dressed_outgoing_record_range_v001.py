#!/usr/bin/env python3
"""Closed-form verifier for the dressed outgoing-record range correction."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_DRESSED_OUTGOING_RECORD_RANGE_SPEC_V001.md"
RESULT = ROOT / "results" / "r3_4_dressed_outgoing_record_range_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def embed(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(3, dtype=complex)
    return np.kron(operator, identity) if site == 0 else np.kron(identity, operator)


def conditional_expectation(operator: np.ndarray) -> np.ndarray:
    tensor = operator.reshape(3, 9, 3, 9)
    record_operator = np.einsum("aiaj->ij", tensor) / 3.0
    return np.kron(np.eye(3, dtype=complex), record_operator)


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )

    incidence = np.zeros((3, 2), dtype=complex)
    incidence[0, 0] = -1.0
    incidence[1, 0] = 1.0
    incidence[1, 1] = -1.0
    incidence[2, 1] = 1.0
    projectors = tuple(
        np.outer(incidence[:, j], incidence[:, j].conjugate()) / 2.0
        for j in range(2)
    )
    endpoint = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]],
        dtype=complex,
    )
    identity_source = np.eye(3, dtype=complex)
    identity_records = np.eye(9, dtype=complex)
    unitaries = tuple(
        np.kron(identity_source - projectors[j], identity_records)
        + np.kron(projectors[j], embed(endpoint, j))
        for j in range(2)
    )
    first_history = unitaries[0]
    second_history = unitaries[1] @ unitaries[0]

    pointer = np.diag([0.0, 1.0, 0.0]).astype(complex)
    bare = np.kron(identity_source, embed(pointer, 0))
    first_image = first_history.conjugate().T @ bare @ first_history
    second_image = second_history.conjugate().T @ bare @ second_history
    stabilization = float(np.linalg.norm(second_image - first_image))
    range_distance = float(
        np.linalg.norm(first_image - conditional_expectation(first_image))
    )
    source_probe = np.kron(
        np.diag([1.0, 0.0, 0.0]), identity_records
    )
    source_commutator = float(
        np.linalg.norm(
            first_image @ source_probe - source_probe @ first_image
        )
    )

    require(stabilization < 1e-12, "Closed-form image did not stabilize")
    require(
        abs(range_distance - stored["record_only_range_distances"]["(1, 1)"])
        < 1e-12,
        "Closed-form range distance mismatch",
    )
    require(
        abs(source_commutator - stored["pointer_image_source_commutator_norm"])
        < 1e-12,
        "Closed-form source commutator mismatch",
    )
    require(stored["bare_record_endomorphism_derived"] is False,
            "Bare endomorphism overclaim survived")
    require(stored["stable_dressed_record_monomorphism_derived"] is True,
            "Dressed monomorphism result missing")
    require(
        stored["prior_bare_record_endomorphism_claim_superseded"] is True,
        "Prior claim was not superseded",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    print("PASS closed-form dressed outgoing-record range verification")


if __name__ == "__main__":
    main()
