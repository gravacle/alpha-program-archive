#!/usr/bin/env python3
"""Pre-execution unit tests for the primary regulated CAR response lane."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "scripts/"
    "derive_stage8_t7_actual_parent_regulated_car_operator_response_primary_v001.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("primary_lane", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load primary lane")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    lane = load_module()
    alphas, source_incidence = lane.dirac_matrices()
    require(
        max(
            np.linalg.norm(
                alphas[left] @ alphas[right]
                + alphas[right] @ alphas[left]
                - (
                    2.0 * np.eye(4, dtype=complex)
                    if left == right
                    else np.zeros((4, 4), dtype=complex)
                )
            )
            for left in range(3)
            for right in range(3)
        )
        < 1.0e-12,
        "Clifford control failed",
    )

    endpoint_cell, endpoint_bump = lane.multiplication_matrices(
        0.0, 2, 1.0, (4, 4, 8)
    )
    require(np.linalg.norm(endpoint_cell) == 0.0, "Endpoint cell did not vanish")
    require(np.linalg.norm(endpoint_bump) == 0.0, "Endpoint bump did not vanish")
    midpoint_cell, midpoint_bump = lane.multiplication_matrices(
        0.5, 2, 1.0, (6, 6, 12)
    )
    require(np.linalg.norm(midpoint_cell) > 0.0, "Midpoint cell vanished")
    require(np.linalg.norm(midpoint_bump) > 0.0, "Smooth midpoint bump vanished")
    require(
        np.linalg.eigvalsh(midpoint_bump)[0] > -1.0e-12,
        "Smooth bump compression is not positive",
    )

    record, values, projectors, probabilities, pointer_weights = lane.record_data()
    require(
        np.max(np.abs(values - np.array(lane.RECORD_VALUES))) < 1.0e-12,
        "Record eigenvalues changed",
    )
    require(
        np.linalg.norm(np.sum(projectors, axis=0) - np.eye(3)) < 1.0e-12,
        "Record spectral resolution failed",
    )
    require(abs(np.sum(probabilities) - 1.0) < 1.0e-12, "Probabilities changed")
    require(
        np.max(
            np.abs(
                pointer_weights
                - np.array([-0.25, 0.5, -0.25], dtype=complex)
            )
        )
        < 1.0e-12,
        "Pointer weights changed",
    )

    hermitian = np.array([[1.0, 0.2j], [-0.2j, -0.3]], dtype=complex)
    unitary = lane.exp_hermitian(hermitian, 0.37)
    require(
        np.linalg.norm(unitary.conjugate().T @ unitary - np.eye(2)) < 1.0e-12,
        "Hermitian exponential lost unitarity",
    )

    ready = lane.ready_injection(2)
    require(
        np.linalg.norm(ready.conjugate().T @ ready - np.eye(2)) == 0.0,
        "Ready injection is not isometric",
    )
    blocks = lane.kraus_blocks(ready)
    require(np.linalg.norm(blocks[0] - np.eye(2)) == 0.0, "Ready block changed")
    require(np.linalg.norm(blocks[1]) == 0.0, "Pointer block not empty")
    require(np.linalg.norm(blocks[2]) == 0.0, "Else block not empty")

    zero = np.zeros((2, 2), dtype=complex)
    identity = np.eye(2, dtype=complex)
    direct_all, direct_pointer = lane.direct_responses(
        (identity, zero, zero),
        (identity, zero, zero),
    )
    require(np.linalg.norm(direct_all - identity) == 0.0, "Identity response failed")
    require(np.linalg.norm(direct_pointer) == 0.0, "Pointer control failed")

    require(
        lane.SPEC_SHA256
        == "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3",
        "Spec pin changed",
    )
    require(
        abs(math.pi / math.sqrt(2.0) - 2.221441469079183) < 1.0e-15,
        "Opening action control changed",
    )
    route1_arrays: dict[str, np.ndarray] = {}
    route1 = lane.current_route2_route1_architecture_reduction(route1_arrays)
    require(route1["passed"] is True, "Current Route-2/O6 reduction failed")
    require(
        route1["actual_parent_route1_line_restriction_derived"] is False,
        "Route-2/O6 reduction overclaimed an actual-parent line",
    )
    require(
        route1["maximum_completed_component_error"] <= 1.0e-10
        and route1["maximum_exhaustive_kernel_error"] <= 1.0e-10,
        "Current Route-2/O6 formula mismatch",
    )
    require(
        "diag_route1_current__r0__completed" in route1_arrays
        and "diag_route1_current__r1__all" in route1_arrays,
        "Current Route-2/O6 raw diagnostics are incomplete",
    )
    dummy_arrays: dict[str, np.ndarray] = {
        f"record_projector__l{record_index}": np.eye(3, dtype=complex)
        for record_index in range(3)
    }
    for ell_index in range(len(lane.ELLS)):
        ell_tag = lane.tag_ell(ell_index)
        for history_index in range(len(lane.HISTORIES)):
            for record_index in range(3):
                dummy_arrays[
                    f"u__{ell_tag}__a{history_index}__l{record_index}"
                ] = np.eye(32, dtype=complex)
            for outcome in range(3):
                dummy_arrays[
                    f"direct_kraus__{ell_tag}__a{history_index}__x{outcome}"
                ] = np.eye(32, dtype=complex)
        for pair_index in range(len(lane.PAIRS)):
            for cross_index in range(9):
                dummy_arrays[
                    f"cross__{ell_tag}__p{pair_index}__c{cross_index}"
                ] = np.eye(32, dtype=complex)
            for kernel in ("all", "pointer"):
                dummy_arrays[
                    f"direct_{kernel}__{ell_tag}__p{pair_index}"
                ] = np.eye(32, dtype=complex)
                dummy_arrays[
                    f"gaussian_{kernel}__{ell_tag}__p{pair_index}"
                ] = np.eye(32, dtype=complex)
    manifest = lane.common_component_manifest(
        dummy_arrays,
        values,
        probabilities,
        pointer_weights,
    )
    counts = {
        category: len(entries)
        for category, entries in manifest["matrix_components"].items()
    }
    require(
        counts
        == {
            "record_projectors": 3,
            "propagators": 30,
            "cross_operators": 54,
            "direct_kraus_members": 30,
            "direct_responses": 12,
            "aggregate_kernels": 12,
        },
        f"Common component inventory changed: {counts}",
    )
    expected_propagators = {
        f"ell{ell}.a{history}.l{record_index}"
        for ell in range(2)
        for history in range(5)
        for record_index in range(3)
    }
    expected_cross = {
        f"ell{ell}.p{pair}.mu{left}.l{right}"
        for ell in range(2)
        for pair in range(3)
        for left in range(3)
        for right in range(3)
    }
    expected_kraus = {
        f"ell{ell}.a{history}.x{outcome}"
        for ell in range(2)
        for history in range(5)
        for outcome in range(3)
    }
    expected_responses = {
        f"ell{ell}.p{pair}.{kernel}"
        for ell in range(2)
        for pair in range(3)
        for kernel in ("all", "pointer")
    }
    require(
        set(manifest["matrix_components"]["propagators"])
        == expected_propagators,
        "Propagator logical inventory changed",
    )
    require(
        set(manifest["matrix_components"]["cross_operators"]) == expected_cross,
        "Cross-operator logical inventory changed",
    )
    require(
        set(manifest["matrix_components"]["direct_kraus_members"])
        == expected_kraus,
        "Direct-Kraus logical inventory changed",
    )
    require(
        set(manifest["matrix_components"]["direct_responses"])
        == expected_responses
        == set(manifest["matrix_components"]["aggregate_kernels"]),
        "Response logical inventory changed",
    )
    print("PASS primary pre-execution unit tests")


if __name__ == "__main__":
    main()
