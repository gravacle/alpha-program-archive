#!/usr/bin/env python3
"""Independent state-restriction verifier for the outgoing record GNS."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_RESULT = ROOT / "results" / "r3_4_outgoing_record_gns_completion_v001.json"
VERIFY_RESULT = (
    ROOT
    / "results"
    / "r3_4_outgoing_record_gns_completion_verification_v001.json"
)


def exp_from_spectral_polynomial(operator, interval):
    values, vectors = np.linalg.eigh(operator)
    phases = np.cos(interval * values) - 1j * np.sin(interval * values)
    return vectors @ np.diag(phases) @ vectors.conjugate().T


def embed(operator, site, total):
    result = np.array([[1.0]], dtype=complex)
    for index in range(total):
        result = np.kron(
            result,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return result


def reduce_records(state, source_dimension, kept, total):
    tensor = state.reshape(source_dimension, 3**kept, 3 ** (total - kept))
    return np.einsum("sak,sbk->ab", tensor, tensor.conjugate())


def reduce_source(state, source_dimension, record_dimension):
    tensor = state.reshape(source_dimension, record_dimension)
    return tensor @ tensor.conjugate().T


def main() -> None:
    source_dimension = 4
    total_records = 3
    incidence = np.zeros((source_dimension, total_records), dtype=complex)
    for cell in range(total_records):
        incidence[cell, cell] = -1.0
        incidence[cell + 1, cell] = 1.0
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    unitary_cells = []
    for cell in range(total_records):
        vector = incidence[:, cell]
        projector = np.outer(vector, vector.conjugate()) / np.vdot(vector, vector)
        generator = np.kron(projector, embed(c_partial, cell, total_records))
        unitary_cells.append(
            exp_from_spectral_polynomial(generator, math.pi / math.sqrt(2.0))
        )

    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    source = incidence[:, 0] / np.linalg.norm(incidence[:, 0])
    state = np.kron(source, np.kron(np.kron(ready, ready), ready))
    states = []
    for unitary in unitary_cells:
        state = unitary @ state
        states.append(state)

    restriction_errors = {}
    for kept in (1, 2):
        before = reduce_records(
            states[kept - 1],
            source_dimension,
            kept,
            total_records,
        )
        after = reduce_records(
            states[kept],
            source_dimension,
            kept,
            total_records,
        )
        restriction_errors[f"{kept}_to_{kept + 1}"] = float(
            np.max(np.abs(before - after))
        )

    record_dimension = 3**total_records
    source_states = [
        reduce_source(state_item, source_dimension, record_dimension)
        for state_item in states
    ]
    source_changes = {
        "1_to_2": float(np.linalg.norm(source_states[0] - source_states[1])),
        "2_to_3": float(np.linalg.norm(source_states[1] - source_states[2])),
    }

    primary = json.loads(PRIMARY_RESULT.read_text())
    comparisons = {
        "one_to_two_record_restriction": restriction_errors["1_to_2"] < 1e-12,
        "two_to_three_record_restriction": restriction_errors["2_to_3"] < 1e-12,
        "source_negative_control": min(source_changes.values()) > 1e-3,
        "primary_record_restrictions": primary["all_record_restrictions_pass"]
        is True,
        "primary_source_limit_false": (
            primary["global_source_inclusive_state_limit_derived"] is False
        ),
        "primary_verdict": (
            primary["verdict"]
            == "OUTGOING_RECORD_GNS_AND_DRESSED_NET_DERIVED"
        ),
        "alpha_false": primary["alpha_computed"] is False,
        "proof_false": primary["proof_authorized"] is False,
    }
    result = {
        "method": "independent spectral-polynomial cell evolution",
        "record_restriction_max_entry_errors": restriction_errors,
        "source_state_changes": source_changes,
        "comparisons": comparisons,
        "independent_verification_pass": all(comparisons.values()),
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    VERIFY_RESULT.parent.mkdir(parents=True, exist_ok=True)
    VERIFY_RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
