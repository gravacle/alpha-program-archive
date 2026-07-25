#!/usr/bin/env python3
"""Independent algebra/status verifier for the Gaussian path-sum gate."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution/work/T07_gaussian_path_sum_reduction.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="utf-8"))

    c = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    eye = np.eye(3, dtype=complex)
    root_two = np.sqrt(2.0)
    projectors = (
        (c @ c - root_two * c) / 4.0,
        eye - (c @ c) / 2.0,
        (c @ c + root_two * c) / 4.0,
    )
    require(
        np.linalg.norm(sum(projectors) - eye) < 1e-14,
        "Record projectors do not resolve identity",
    )
    for index, projector in enumerate(projectors):
        require(
            np.linalg.norm(projector @ projector - projector) < 1e-14,
            f"Record projector {index} is not idempotent",
        )
        for other_index, other in enumerate(projectors):
            if index != other_index:
                require(
                    np.linalg.norm(projector @ other) < 1e-14,
                    "Record projectors are not orthogonal",
                )

    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    weights = np.array(
        [np.vdot(pointer, projector @ ready) for projector in projectors]
    )
    expected = np.array([-0.25, 0.5, -0.25], dtype=complex)
    require(np.linalg.norm(weights - expected) < 1e-14, "Record weights changed")
    require(abs(np.sum(weights)) < 1e-14, "Vacuum cancellation changed")

    require(stored["valid_termwise_determinants_used"] is True,
            "Termwise determinant representation was not used")
    require(stored["single_determinant_shortcut_used"] is False,
            "Forbidden single determinant reappeared")
    require(stored["path_count_one_cell"] == 3, "One-cell path count changed")
    require(stored["path_count_two_cells"] == 9, "Two-cell path count changed")
    require(stored["finite_fock_one_cell_difference"] < 1e-12,
            "One-cell finite-Fock regression failed")
    require(stored["finite_fock_two_cell_difference"] < 1e-12,
            "Two-cell finite-Fock regression failed")
    require(stored["gaussian_path_sum_reduction_derived"] is True,
            "Path-sum verdict changed")
    require(stored["all_finite_connected_baselines_nonzero_proved"] is False,
            "All-volume nonzero baselines were overclaimed")
    require(stored["volume_uniform_zero_free_neighborhood_proved"] is False,
            "Uniform zero-free theorem was overclaimed")
    require(stored["connected_linked_cluster_density_proved"] is False,
            "Cluster density was overclaimed")
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(stored["proof_authorized"] is False, "Proof was authorized")

    print(
        "PASS Gaussian path-sum algebra/status verification "
        f"(weights={weights.real.tolist()})"
    )


if __name__ == "__main__":
    main()
