#!/usr/bin/env python3
"""Independent self-review of the Stage-8 structural execution tranche.

This verifier deliberately does not import run_stage8_structural_core_v001.
It uses incidence vectors, concrete matrix power series, modular rank, and
floating-point diagonalization as separate implementations of the decisive
checks. It is a labeled self-review, not one of the required fresh-context
Stage-8 reviewer lanes.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
EXEC = ROOT / "stage8_execution"
REPORTS = EXEC / "t_reports"
CONTROLS = EXEC / "controls"
WORK = EXEC / "work"
OUTPUT = WORK / "structural_core_independent_verification.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def content_address_valid(path: Path) -> bool:
    body = json.loads(path.read_text())
    claimed = body.get("sha256_of_body")
    if not claimed:
        return False
    body["sha256_of_body"] = ""
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    return claimed == sha256_bytes(canonical)


def verify_manifest(path: Path) -> bool:
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        artifact = path.parent / relative
        if not artifact.is_file() or sha256_file(artifact) != expected:
            return False
    return True


def series_product(
    left: list[np.ndarray], right: list[np.ndarray], degree: int
) -> list[np.ndarray]:
    size = left[0].shape[0]
    result = [np.zeros((size, size), dtype=object) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                result[i + j] = result[i + j] + a @ b
    return result


def modular_rank(rows: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], prime - 2, prime)
        matrix[pivot_row] = [
            (value * inverse) % prime for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    (matrix[row][j] - factor * matrix[pivot_row][j]) % prime
                    for j in range(len(matrix[0]))
                ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def bivector(n: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return (
        n[0] * v[1] - n[1] * v[0],
        n[0] * v[2] - n[2] * v[0],
        n[0] * v[3] - n[3] * v[0],
        n[2] * v[3] - n[3] * v[2],
        n[3] * v[1] - n[1] * v[3],
        n[1] * v[2] - n[2] * v[1],
    )


def quadratic_design_row(values: tuple[int, ...]) -> list[int]:
    row = [value * value for value in values]
    row.extend(
        2 * values[i] * values[j]
        for i in range(6)
        for j in range(i + 1, 6)
    )
    return row


def main() -> int:
    checks: dict[str, bool] = {}

    report_names = ("T01", "T02", "T03", "T04", "T06", "T08", "T10", "T11", "T16")
    control_names = ("NC1", "NC2", "NC3", "NC4", "NC5")
    checks["all_report_content_addresses_valid"] = all(
        content_address_valid(REPORTS / f"{name}.json") for name in report_names
    )
    checks["all_control_content_addresses_valid"] = all(
        content_address_valid(CONTROLS / f"{name}.json") for name in control_names
    )

    # T1: compare the two path boundaries in an independently built incidence basis.
    vertex_index = {
        "x": 0,
        "x_plus_mu": 1,
        "x_plus_nu": 2,
        "x_plus_mu_plus_nu": 3,
    }

    def incidence(source: str, target: str) -> np.ndarray:
        vector = np.zeros(4, dtype=int)
        vector[vertex_index[source]] = -1
        vector[vertex_index[target]] = 1
        return vector

    plus_boundary = incidence("x", "x_plus_mu") + incidence(
        "x_plus_mu", "x_plus_mu_plus_nu"
    )
    minus_boundary = incidence("x", "x_plus_nu") + incidence(
        "x_plus_nu", "x_plus_mu_plus_nu"
    )
    t1 = json.loads((REPORTS / "T01.json").read_text())
    reported_loop = np.array(
        [
            t1["evidence"]["closed_loop_gauge_exponents"][name]
            for name in vertex_index
        ],
        dtype=int,
    )
    checks["T1_incidence_cancellation"] = bool(
        np.array_equal(plus_boundary, minus_boundary)
        and np.array_equal(plus_boundary - minus_boundary, reported_loop)
        and np.all(reported_loop == 0)
    )

    # T2: concrete truncated matrix series, independent of the free-word algebra.
    identity = np.eye(2, dtype=object)
    zero = np.zeros((2, 2), dtype=object)
    n = np.array([[0, 1], [0, 0]], dtype=object)
    m = np.array([[0, 0], [1, 0]], dtype=object)
    n_series = [identity, n, zero]
    m_series = [identity, m, zero]
    n_inverse = [identity, -n, n @ n]
    m_inverse = [identity, -m, m @ m]
    product = n_series
    for factor in (m_series, n_inverse, m_inverse):
        product = series_product(product, factor, 2)
    expected_commutator = n @ m - m @ n
    checks["T2_concrete_degree_two_commutator"] = bool(
        np.array_equal(product[0], identity)
        and np.array_equal(product[1], zero)
        and np.array_equal(product[2], expected_commutator)
        and np.any(expected_commutator != 0)
    )

    # T3: evaluate the two explicit i-bearing conversion factors directly.
    t3_coefficient = 0.25 * (-2j) * (-1j)
    t3 = json.loads((REPORTS / "T03.json").read_text())
    checks["T3_clifford_coefficient"] = bool(
        abs(t3_coefficient.real + 0.5) < 1e-15
        and abs(t3_coefficient.imag) < 1e-15
        and t3["evidence"]["signed_leading_coefficient"] == "-1/2"
    )

    # T4: verify its authority seal and independently diagonalize B_h.
    parent_seal = ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256"
    b_h = np.array([[0.0, 0.0, -1.0], [0.0, 0.0, 1.0], [-1.0, 1.0, 0.0]])
    b_h_eigenvalues = np.linalg.eigvalsh(b_h)
    checks["T4_parent_seal_and_spectrum"] = bool(
        verify_manifest(parent_seal)
        and np.allclose(b_h @ b_h @ b_h, 2.0 * b_h, atol=1e-14)
        and np.allclose(
            b_h_eigenvalues,
            np.array([-math.sqrt(2.0), 0.0, math.sqrt(2.0)]),
            atol=1e-14,
        )
    )

    # T12 precheck: modular arithmetic gives an independent exact rank certificate.
    momenta = [
        n_value
        for n_value in __import__("itertools").product((-1, 0, 1), repeat=4)
        if any(n_value) and next(value for value in n_value if value) > 0
    ]
    polarizations = [
        tuple(int(i == j) for i in range(4)) for j in range(4)
    ] + [
        tuple(int(i in (j, k)) for i in range(4))
        for j in range(4)
        for k in range(j + 1, 4)
    ]
    design = [
        quadratic_design_row(bivector(n_value, polarization))
        for n_value in momenta
        for polarization in polarizations
    ]
    ranks = [modular_rank(design, prime) for prime in (1_000_003, 1_000_033)]
    pair_order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    top_pair_indices = [pair_order.index(pair) for pair in ((0, 3), (1, 4), (2, 5))]
    plucker = [
        sum(row[6 + pair_index] // 2 for pair_index in top_pair_indices)
        for row in design
    ]
    t12 = json.loads((WORK / "T12_design_precheck.json").read_text())
    checks["T12_modular_rank_and_topological_null"] = bool(
        ranks == [20, 20]
        and all(value == 0 for value in plucker)
        and t12["exact_rank"] == 20
        and t12["T_top_in_nullspace"]
    )

    # T16: numerical eigensystem and trace moments, separate from exact charpoly.
    d = np.array(
        [[-1, -1, 0, 0], [1, 0, -1, 0], [0, 1, 0, -1], [0, 0, 1, -1]],
        dtype=float,
    )
    zero4 = np.zeros((4, 4))
    b_square = np.block([[zero4, d], [d.T, zero4]])
    eigenvalues = np.linalg.eigvalsh(b_square)
    expected = np.sort(
        np.array(
            [
                -math.sqrt(2 + math.sqrt(2)),
                -math.sqrt(2 + math.sqrt(2)),
                -math.sqrt(2 - math.sqrt(2)),
                -math.sqrt(2 - math.sqrt(2)),
                math.sqrt(2 - math.sqrt(2)),
                math.sqrt(2 - math.sqrt(2)),
                math.sqrt(2 + math.sqrt(2)),
                math.sqrt(2 + math.sqrt(2)),
            ]
        )
    )
    trace_b2 = float(np.trace(b_square @ b_square))
    trace_b4 = float(np.trace(b_square @ b_square @ b_square @ b_square))
    checks["T16_numerical_spectrum_and_moments"] = bool(
        np.allclose(eigenvalues, expected, atol=1e-13)
        and abs(trace_b2 - 16.0) < 1e-13
        and abs(trace_b4 - 48.0) < 1e-12
        and np.min(np.abs(eigenvalues)) > 0.7
    )

    passed = all(checks.values())
    result = {
        "schema": "stage8-structural-core-independent-self-review-v001",
        "role": "self-review; not a mandated fresh-context independent lane",
        "pass": passed,
        "checks": checks,
        "protected_flags": {
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
