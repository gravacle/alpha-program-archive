#!/usr/bin/env python3
"""Independent verifier for the parent-to-outgoing compatibility gate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "r3_4_parent_to_outgoing_gns_compatibility_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="ascii"))

    b = np.zeros((3, 3), dtype=complex)
    b[0, 2] = -1.0j
    b[1, 2] = +1.0j
    b[2, 0] = +1.0j
    b[2, 1] = -1.0j
    p = np.eye(3, dtype=complex)[:, 1]
    r = np.eye(3, dtype=complex)[:, 0]
    projector = np.diag([0.0, 1.0, 0.0]).astype(complex)
    commutator_norm = np.linalg.norm(b @ projector - projector @ b)
    require(commutator_norm > 1.0, "Endpoint state unexpectedly invariant")

    tau = math.pi / math.sqrt(2.0)
    b2 = b @ b
    unitary = (
        np.eye(3, dtype=complex)
        - 1.0j * math.sin(math.sqrt(2.0) * tau) * b / math.sqrt(2.0)
        + (math.cos(math.sqrt(2.0) * tau) - 1.0) * b2 / 2.0
    )
    require(np.linalg.norm(unitary @ p - r) < 1e-12, "p-to-r recurrence failed")
    require(
        result["one_cell_static_parent_checks"][
            "endpoint_projector_commutator_frobenius"
        ]
        == commutator_norm,
        "Producer commutator differs",
    )
    require(
        result["product_label_states_algebraically_compatible"] is True,
        "Quasi-local state lift was lost",
    )
    require(
        result["product_label_state_selected_by_complete_parent"] is False,
        "Parent preparation was overclaimed",
    )
    require(
        result["inherited_status"]["response_inequivalent_parent_actions_survive"]
        is True,
        "Parent counterfamily disappeared",
    )
    require(
        result["primary_verdict"] == "PARENT_LIMIT_UNDERDETERMINED",
        "Unexpected primary verdict",
    )
    require(result["parent_to_outgoing_limit_derived"] is False, "False closure")
    require(result["alpha_computed"] is False, "Alpha status changed")
    print("R3.4 parent-to-outgoing independent verification: PASS")


if __name__ == "__main__":
    main()
