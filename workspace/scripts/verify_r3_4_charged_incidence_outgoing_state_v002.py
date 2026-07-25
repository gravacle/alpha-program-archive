#!/usr/bin/env python3
"""Independent verifier for the charged-incidence outgoing-state gate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_charged_incidence_outgoing_state_v002.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="ascii"))

    c = np.zeros((3, 3), dtype=complex)
    c[0, 2] = -1.0j
    c[1, 2] = +1.0j
    c[2, 0] = +1.0j
    c[2, 1] = -1.0j
    swap = np.eye(3, dtype=complex) - c @ c
    expected = np.array(
        [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0]],
        dtype=complex,
    )
    require(np.array_equal(swap, expected), "Polynomial endpoint map changed")

    t_probe = math.pi / (2.0 * math.sqrt(2.0))
    amplitude = (1.0 + math.cos(math.sqrt(2.0) * t_probe)) / 2.0
    require(abs(amplitude - 0.5) < 1e-15, "Stationary overlap changed")
    require(amplitude**32 < 1e-9, "Infinite-product obstruction disappeared")

    require(
        result["active_endpoint_unitary_swap_error"] < 1e-12,
        "Producer endpoint unitary failed",
    )
    require(
        max(result["finite_state_restriction_errors"].values()) < 1e-12,
        "Producer state restrictions failed",
    )
    require(
        result["charge_superselected_quasilocal_state_lift_derived"] is True,
        "Algebraic state lift was lost",
    )
    require(
        result["stationary_infinite_endpoint_product_GNS_implementation_fails"]
        is True,
        "Stationary GNS obstruction was hidden",
    )
    require(
        result["status"]
        == "CHARGED_INCIDENCE_OUTGOING_STATE_CONDITIONAL_ON_CAUSAL_SUPPORT",
        "Unexpected verdict",
    )
    require(result["complete_parent_action_derived"] is False, "False closure")
    require(result["alpha_computed"] is False, "Alpha status changed")
    print("R3.4 charged-incidence outgoing-state verification: PASS")


if __name__ == "__main__":
    main()
