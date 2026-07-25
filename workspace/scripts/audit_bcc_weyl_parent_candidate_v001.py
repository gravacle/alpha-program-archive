#!/usr/bin/env python3
"""Target-free audit of the minimal isotropic BCC Weyl-walk candidate."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "bcc_weyl_parent_candidate_v001.json"

Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def dagger(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[0][0].conjugate(), matrix[1][0].conjugate()),
        (matrix[0][1].conjugate(), matrix[1][1].conjugate()),
    )


def subtract(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def max_abs(matrix: Matrix2) -> float:
    return max(abs(entry) for row in matrix for entry in row)


IDENTITY: Matrix2 = ((1.0 + 0.0j, 0.0j), (0.0j, 1.0 + 0.0j))


def exp_pauli_x(angle: float) -> Matrix2:
    c = math.cos(angle)
    s = math.sin(angle)
    return ((c, -1j * s), (-1j * s, c))


def exp_pauli_y(angle: float) -> Matrix2:
    c = math.cos(angle)
    s = math.sin(angle)
    return ((c, -s), (s, c))


def exp_pauli_z(angle: float) -> Matrix2:
    return (
        (cmath.exp(-1j * angle), 0.0j),
        (0.0j, cmath.exp(1j * angle)),
    )


def walk(kx: float, ky: float, kz: float) -> Matrix2:
    return matmul(
        matmul(exp_pauli_x(kx), exp_pauli_y(ky)),
        exp_pauli_z(kz),
    )


def lambda_and_standard_pauli_vector(
    kx: float, ky: float, kz: float
) -> tuple[float, tuple[float, float, float]]:
    cx, cy, cz = math.cos(kx), math.cos(ky), math.cos(kz)
    sx, sy, sz = math.sin(kx), math.sin(ky), math.sin(kz)
    lam = cx * cy * cz - sx * sy * sz
    nx = sx * cy * cz + cx * sy * sz
    ny = cx * sy * cz - sx * cy * sz
    nz = cx * cy * sz + sx * sy * cz
    return lam, (nx, ny, nz)


def determinant3(matrix: tuple[tuple[float, float, float], ...]) -> float:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def chirality_at(node: tuple[float, float, float]) -> tuple[int, float]:
    lam, _ = lambda_and_standard_pauli_vector(*node)
    baseline = 1.0 if lam >= 0.0 else -1.0
    step = 1.0e-6
    columns: list[tuple[float, float, float]] = []
    for axis in range(3):
        plus = list(node)
        minus = list(node)
        plus[axis] += step
        minus[axis] -= step
        _, n_plus = lambda_and_standard_pauli_vector(*plus)
        _, n_minus = lambda_and_standard_pauli_vector(*minus)
        columns.append(
            tuple(
                baseline * (n_plus[index] - n_minus[index]) / (2.0 * step)
                for index in range(3)
            )
        )
    jacobian = tuple(
        tuple(columns[column][row] for column in range(3))
        for row in range(3)
    )
    determinant = determinant3(jacobian)
    return (1 if determinant > 0.0 else -1), determinant


def main() -> None:
    sample = tuple(-2.4 + 0.2 * index for index in range(25))
    unitarity_error = 0.0
    for kx in sample:
        for ky in sample[::4]:
            for kz in sample[::5]:
                product = matmul(dagger(walk(kx, ky, kz)), walk(kx, ky, kz))
                unitarity_error = max(
                    unitarity_error,
                    max_abs(subtract(product, IDENTITY)),
                )

    nodes = {
        "k0": (0.0, 0.0, 0.0),
        "k1": (math.pi / 2.0, math.pi / 2.0, math.pi / 2.0),
        "k2": (-math.pi / 2.0, -math.pi / 2.0, -math.pi / 2.0),
        "k3": (math.pi, 0.0, 0.0),
    }
    node_payload: dict[str, dict[str, float | int]] = {}
    node_error = 0.0
    chiralities: list[int] = []
    for name, node in nodes.items():
        lam, vector = lambda_and_standard_pauli_vector(*node)
        node_error = max(node_error, *(abs(value) for value in vector))
        chirality, determinant = chirality_at(node)
        chiralities.append(chirality)
        node_payload[name] = {
            "quasienergy_baseline_sign": 1 if lam >= 0.0 else -1,
            "linearized_chirality_sign": chirality,
            "linearized_jacobian_determinant": determinant,
        }

    positive = sum(value > 0 for value in chiralities)
    negative = sum(value < 0 for value in chiralities)
    tolerance = 2.0e-13
    checks = {
        "free_walk_is_unitary": unitarity_error < tolerance,
        "four_declared_weyl_nodes_are_exact": node_error < tolerance,
        "net_chirality_cancels": positive == 2 and negative == 2,
        "one_two_component_walk_has_four_weyl_cones": (
            len(nodes) == 4 and positive + negative == 4
        ),
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_BCC_FREE_PARENT_FOUR_CONES_GAUGED_KERNEL_OPEN_ALPHA_FALSE"
        if not failed
        else "FAIL_BCC_WEYL_PARENT_CANDIDATE_V001"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "max_unitarity_error": unitarity_error,
        "max_node_vector_error": node_error,
        "nodes": node_payload,
        "positive_chirality_cones": positive,
        "negative_chirality_cones": negative,
        "total_weyl_cones": len(nodes),
        "one_Dirac_source_inventory_survives": False,
        "gauged_unitary_parent_kernel_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "executable_role": "FREE_WALK_AND_SPECIES_GATE_NOT_COUPLING_PROOF",
    }
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print(f"max_unitarity_error={unitarity_error:.3e}")
    print(f"max_node_vector_error={node_error:.3e}")
    print(f"chirality_counts=positive:{positive},negative:{negative}")
    print("one_Dirac_source_inventory_survives=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

