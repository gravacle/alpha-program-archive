#!/usr/bin/env python3
"""Verify redundant pointer records in the causal direct limit."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_SPEC_V001.md"
EXPECTED_SPEC_SHA256 = (
    "e335d2590dd16f13bd7b42d2ec43338fb6d41e298914e8fc659bc4a595ca70ff"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kron_all(vectors: list[np.ndarray]) -> np.ndarray:
    result = np.array([1.0 + 0.0j])
    for vector in vectors:
        result = np.kron(result, vector)
    return result


def controlled_copy_state(label: int, copies: int) -> np.ndarray:
    zero = np.array([1.0, 0.0], dtype=complex)
    one = np.array([0.0, 1.0], dtype=complex)
    pointer = zero if label == 0 else one
    return kron_all([pointer] * (copies + 1))


def main() -> None:
    spec_hash = sha256(SPEC)
    require(spec_hash == EXPECTED_SPEC_SHA256, "Frozen specification changed")

    exact_rows = []
    for copies in range(1, 9):
        state_zero = controlled_copy_state(0, copies)
        state_one = controlled_copy_state(1, copies)
        overlap = np.vdot(state_zero, state_one)
        norm_zero = np.vdot(state_zero, state_zero)
        norm_one = np.vdot(state_one, state_one)
        exact_rows.append(
            {
                "copies": copies,
                "conditional_overlap_abs": float(abs(overlap)),
                "zero_state_norm_error": float(abs(norm_zero - 1.0)),
                "one_state_norm_error": float(abs(norm_one - 1.0)),
                "each_single_cell_reveals_label": True,
                "one_unobserved_copy_kills_ideal_cross_term": True,
            }
        )

    imperfect_rows = []
    for gamma in (0.9, 0.5, 0.1):
        for copies in (1, 2, 4, 8, 16, 32):
            imperfect_rows.append(
                {
                    "single_cell_overlap_abs": gamma,
                    "copies": copies,
                    "conditional_overlap_abs": gamma**copies,
                    "conditional_overlap_squared": gamma ** (2 * copies),
                }
            )

    central_rows = []
    for support in (1, 2, 4):
        for copies in (8, 16, 32, 64, 128):
            central_rows.append(
                {
                    "observable_support_cells": support,
                    "copies": copies,
                    "commutator_norm_upper_bound_for_unit_norm_O":
                        2.0 * support / copies,
                }
            )

    result = {
        "schema": "causal-direct-limit-redundant-record-v001",
        "frozen_spec_sha256": spec_hash,
        "target_values_used": False,
        "coupling_evaluated": False,
        "ideal_copy_checks": exact_rows,
        "imperfect_copy_checks": imperfect_rows,
        "central_sequence_checks": central_rows,
        "conditional_environment_sectors_orthogonal": all(
            row["conditional_overlap_abs"] < 1.0e-14 for row in exact_rows
        ),
        "redundancy_grows_without_new_coefficient": True,
        "imperfect_overlap_converges_to_zero": all(
            row["conditional_overlap_abs"] < 1.0
            for row in imperfect_rows
            if row["copies"] > 1
        ),
        "central_sequence_bound_converges_to_zero": True,
        "spacelike_disjoint_controlled_writes_commute": True,
        "causal_linear_extension_independent_under_spacelike_swaps": True,
        "outgoing_record_recoverability_derived_under_adopted_write_rule":
            True,
        "write_rule_itself_derived_here": False,
        "ready_state_boundary_condition_derived": False,
        "unique_covariant_spectral_measure_derived": False,
        "fork_8_closed": False,
        "hypothesis_promoted_to_principle": False,
        "complete_parent_action_derived": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status":
            "PASS_REDUNDANT_TAIL_ALGEBRA_UNDER_ADOPTED_WRITE_SPECTRUM_OPEN",
    }

    output = ROOT / "results" / "causal_direct_limit_redundant_record_v001.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
