#!/usr/bin/env python3
"""Independent verifier for the causal-cell moving-front gate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_causal_cell_moving_front_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="ascii"))

    c = np.array(
        [[0.0, 0.0, -1.0j], [0.0, 0.0, 1.0j], [1.0j, -1.0j, 0.0]],
        dtype=complex,
    )
    require(np.allclose(c @ c @ c, 2.0 * c), "Incidence polynomial changed")
    tau = math.pi / math.sqrt(2.0)
    endpoint = np.eye(3, dtype=complex) - c @ c
    require(
        np.allclose(
            endpoint,
            np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]], dtype=complex),
        ),
        "Endpoint polynomial is not the full swap",
    )
    require(
        max(result["profile_endpoint_errors"].values()) < 1e-12,
        "Profile independence failed",
    )
    require(
        max(result["distinct_cell_generator_commutators"].values()) < 1e-13,
        "Cell commutation failed",
    )
    require(
        result["fixed_local_public_observables_eventually_stabilize"] is True,
        "Local stabilization was lost",
    )
    require(
        result["moving_front_bound_by_live_complete_parent"] is False,
        "Conditional moving front was promoted",
    )
    require(
        result["status"] == "MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_CONDITIONAL",
        "Unexpected verdict",
    )
    require(result["alpha_computed"] is False, "Alpha status changed")
    print("R3.4 causal-cell moving-front verification: PASS")


if __name__ == "__main__":
    main()
