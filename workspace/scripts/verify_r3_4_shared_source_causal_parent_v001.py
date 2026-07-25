#!/usr/bin/env python3
"""Independent closed-form verifier for the shared-source causal parent."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_SHARED_SOURCE_CAUSAL_PARENT_SPEC_V001.md"
RESULT = ROOT / "results" / "r3_4_shared_source_causal_parent_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def embed(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )

    count = 3
    incidence = np.zeros((4, 3), dtype=complex)
    for index in range(3):
        incidence[index, index] = -1.0
        incidence[index + 1, index] = 1.0
    projectors = tuple(
        np.outer(incidence[:, j], incidence[:, j].conjugate()) / 2.0
        for j in range(3)
    )
    require(
        all(
            abs(np.trace(projectors[j] @ projectors[j + 1]).real - 0.25)
            < 1e-14
            for j in range(2)
        ),
        "Independent overlap check failed",
    )

    gamma5 = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    generators = tuple(
        np.kron(np.kron(projectors[j], gamma5), embed(c_partial, j, count))
        for j in range(3)
    )

    # Every generator has spectrum in {0,+/-sqrt(2)}. At tau=pi/sqrt(2),
    # functional calculus therefore gives U=I-B^2 without diagonalization.
    identity = np.eye(generators[0].shape[0], dtype=complex)
    unitaries = tuple(identity - value @ value for value in generators)
    require(
        max(np.linalg.norm(value @ value - identity) for value in unitaries)
        < 1e-12,
        "Closed-form endpoint unitary is not involutive",
    )

    adjacent_order = np.linalg.norm(
        unitaries[1] @ unitaries[0] - unitaries[0] @ unitaries[1]
    )
    disjoint_order = np.linalg.norm(
        unitaries[2] @ unitaries[0] - unitaries[0] @ unitaries[2]
    )
    require(adjacent_order > 1.0, "Adjacent causal order lost")
    require(disjoint_order < 1e-12, "Disjoint cells failed to commute")

    p = np.diag([0.0, 1.0, 0.0]).astype(complex)
    old_pointer = np.kron(np.eye(16, dtype=complex), embed(p, 0, count))
    require(
        max(
            np.linalg.norm(generators[j] @ old_pointer - old_pointer @ generators[j])
            for j in (1, 2)
        )
        < 1e-12,
        "Later cell changes earlier pointer",
    )

    require(
        abs(stored["adjacent_order_error"] - adjacent_order) < 1e-10,
        "Producer/verifier adjacent-order mismatch",
    )
    require(
        abs(stored["disjoint_order_error"] - disjoint_order) < 1e-12,
        "Producer/verifier disjoint-order mismatch",
    )
    require(stored["primitive_pointer_persistence_derived"] is True,
            "Pointer-persistence result missing")
    require(stored["outgoing_public_record_Moller_endomorphism_derived"] is True,
            "Outgoing endomorphism result missing")
    require(stored["same_GNS_unitary_Moller_implementer_derived"] is False,
            "Same-GNS unitary was overclaimed")
    require(stored["complete_physical_durability_derived"] is False,
            "Complete durability was overclaimed")
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(
        stored["status"] == "SHARED_SOURCE_CAUSAL_PARENT_PUBLIC_MOLLER_DERIVED",
        "Wrong verdict",
    )
    print("PASS independent closed-form shared-source verification")


if __name__ == "__main__":
    main()
