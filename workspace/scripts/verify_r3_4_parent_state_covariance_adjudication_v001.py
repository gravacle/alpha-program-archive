#!/usr/bin/env python3
"""Independent checks for the parent-state covariance adjudication."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_parent_state_covariance_adjudication_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="ascii"))

    c_partial = np.zeros((3, 3), dtype=complex)
    c_partial[0, 2] = -1.0j
    c_partial[1, 2] = +1.0j
    c_partial[2, 0] = +1.0j
    c_partial[2, 1] = -1.0j
    endpoint = np.outer(np.eye(3)[:, 1], np.eye(3)[:, 1])
    norm = np.linalg.norm(c_partial @ endpoint - endpoint @ c_partial)

    require(abs(norm - math.sqrt(2.0)) < 1e-13, "Static norm mismatch")
    require(
        abs(
            norm
            - result["one_cell_static_parent"][
                "endpoint_commutator_frobenius"
            ]
        )
        < 1e-13,
        "Producer and verifier disagree",
    )
    require(
        result["superseded_write_rule_used_by_redundancy_lane"] is True,
        "Superseded write dependency was not retained",
    )
    require(
        result["parent_state_covariance_alone_selects_unique_parent"] is False,
        "Covariance was promoted into a parent selector",
    )
    require(
        result["pauli_exclusion_derived_from_parent_state_covariance"] is False,
        "Pauli exclusion was misattributed",
    )
    require(
        result["live_parent_complete_under_principle"] is False,
        "Incomplete parent was promoted",
    )
    require(
        result["status"] == "PARENT_STATE_COVARIANCE_CURRENT_PARENT_BLOCKED",
        "Unexpected verdict",
    )
    require(result["alpha_computed"] is False, "Alpha status changed")
    print("R3.4 parent-state covariance adjudication: PASS")


if __name__ == "__main__":
    main()
