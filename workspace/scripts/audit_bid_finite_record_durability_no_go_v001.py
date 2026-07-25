#!/usr/bin/env python3
"""Verify the exact recurrence of the finite one-cell BID write."""

import json
import math
from pathlib import Path

import numpy as np


def main() -> None:
    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    values, vectors = np.linalg.eigh(c_partial)

    def evolve(tau: float) -> np.ndarray:
        return vectors @ np.diag(np.exp(-1.0j * tau * values)) @ vectors.conj().T

    tau_r = math.pi / math.sqrt(2.0)
    u_r = evolve(tau_r)
    u_2r = evolve(2.0 * tau_r)
    root = np.array([1.0, 0.0, 0.0], dtype=complex)
    public = np.array([0.0, 1.0, 0.0], dtype=complex)
    p_public = np.outer(public, public.conj())
    commutator = c_partial @ p_public - p_public @ c_partial

    root_to_public_error = float(np.linalg.norm(u_r @ root - public))
    public_to_root_error = float(np.linalg.norm(u_r @ public - root))
    recurrence_error = float(np.linalg.norm(u_2r - np.eye(3)))
    pointer_commutator_norm = float(np.linalg.norm(commutator))

    result = {
        "schema": "bid-finite-record-durability-no-go-v001",
        "target_values_used": False,
        "spectrum": [float(value) for value in values],
        "tau_R": tau_r,
        "root_to_public_error": root_to_public_error,
        "public_to_root_error": public_to_root_error,
        "two_interval_recurrence_error": recurrence_error,
        "pointer_commutator_norm": pointer_commutator_norm,
        "first_orthogonal_write_passed": root_to_public_error < 1e-12,
        "endpoint_is_nondemolition": pointer_commutator_norm < 1e-12,
        "finite_closed_parent_establishes_durability": False,
        "complete_parent_action_derived": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "BLOCK_FINITE_BID_PARENT_IS_EXACTLY_RECURRENT",
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "bid_finite_record_durability_no_go_v001.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
