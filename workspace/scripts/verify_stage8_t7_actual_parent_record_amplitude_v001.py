#!/usr/bin/env python3
"""Independent RK4 verifier for the actual-parent amplitude obstruction."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution/work/T07_actual_parent_record_amplitude.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def dirac_data() -> tuple[np.ndarray, np.ndarray]:
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def embed_record(operator: np.ndarray, site: int) -> np.ndarray:
    identity = np.eye(3, dtype=complex)
    return np.kron(operator, identity) if site == 0 else np.kron(identity, operator)


def weight(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def rk4_pulse(
    states: np.ndarray,
    h_free: np.ndarray,
    write: np.ndarray,
    action: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps

    def derivative(time: float, values: np.ndarray) -> np.ndarray:
        hamiltonian = h_free + action * weight(time) * write
        return -1.0j * hamiltonian @ values

    values = states.copy()
    for index in range(steps):
        time = index * dt
        k1 = derivative(time, values)
        k2 = derivative(time + dt / 2.0, values + dt * k1 / 2.0)
        k3 = derivative(time + dt / 2.0, values + dt * k2 / 2.0)
        k4 = derivative(time + dt, values + dt * k3)
        values = values + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return values


def project_record(
    states: np.ndarray,
    first_label: int,
    second_label: int,
) -> np.ndarray:
    columns = []
    for column in range(states.shape[1]):
        tensor = states[:, column].reshape(12, 3, 3)
        columns.append(tensor[:, first_label, second_label])
    return np.column_stack(columns)


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="utf-8"))

    alpha_x, source_incidence_spin = dirac_data()
    derivative = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        derivative[site, (site + 1) % 3] += 0.5
        derivative[site, (site - 1) % 3] -= 0.5
    h_source = np.kron(-1j * derivative, alpha_x)
    eigenvalues = np.linalg.eigvalsh(h_source)
    zero_count = int(np.count_nonzero(np.abs(eigenvalues) <= 1e-12))
    require(zero_count == 4, "Independent source zero-mode count changed")

    h_free = np.kron(h_source, np.eye(9, dtype=complex))
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    writes = tuple(
        np.kron(
            np.kron(masks[site], source_incidence_spin),
            embed_record(c_partial, site),
        )
        for site in range(2)
    )

    uniform_site = np.ones(3, dtype=complex) / math.sqrt(3.0)
    site_zero = np.array([1.0, 0.0, 0.0], dtype=complex)
    site_one = np.array([0.0, 1.0, 0.0], dtype=complex)
    spin_zero = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    source_vectors = np.column_stack(
        (
            np.kron(uniform_site, spin_zero),
            np.kron(site_zero, spin_zero),
            np.kron(site_one, spin_zero),
        )
    )
    ready = np.zeros(9, dtype=complex)
    ready[0] = 1.0
    initial = np.column_stack(
        [np.kron(source_vectors[:, index], ready) for index in range(3)]
    )

    action = math.pi / math.sqrt(2.0)
    after_first = rk4_pulse(initial, h_free, writes[0], action, 2400)
    after_second = rk4_pulse(after_first, h_free, writes[1], action, 2400)

    completed_pp = project_record(after_second, 1, 1)
    zero_mode_completed_norm = float(np.linalg.norm(completed_pp[:, 0]))
    require(
        zero_mode_completed_norm > 1e-3,
        "Completed record unexpectedly decoupled from an exact zero mode",
    )

    second_source = source_vectors[:, 1]
    second_output = completed_pp[:, 1]
    parallel = np.vdot(second_source, second_output) * second_source
    non_scalar_witness = float(np.linalg.norm(second_output - parallel))
    require(
        non_scalar_witness > 1e-3,
        "Completed record Kraus action unexpectedly scalar",
    )

    first_p_ready = project_record(after_first, 1, 0)
    one_handle_amplitude = np.vdot(
        second_source,
        first_p_ready[:, 1],
    )
    stored_amplitude = complex(
        stored["one_handle_regression"][
            "disclosed_finite_parent_vector_amplitude_real"
        ],
        stored["one_handle_regression"][
            "disclosed_finite_parent_vector_amplitude_imag"
        ],
    )
    require(
        abs(one_handle_amplitude - stored_amplitude) < 5e-5,
        "Independent one-handle amplitude mismatch: "
        f"{one_handle_amplitude!r} versus {stored_amplitude!r}",
    )
    require(
        abs(one_handle_amplitude - 1.0) > 1e-2,
        "Generic finite packet was mistaken for the exact root line",
    )

    require(
        stored["overall_verdict"] == "ACTUAL_PARENT_RECORD_AMPLITUDE_BLOCKED",
        "Stored result did not fail closed",
    )
    require(
        stored["finite_actual_parent_record_amplitude_derived"] is False,
        "Finite scalar amplitude was overclaimed",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(stored["proof_authorized"] is False, "Proof was authorized")

    print(
        "PASS independent actual-parent obstruction verification "
        f"(zero branch norm={zero_mode_completed_norm:.12g}, "
        f"non-scalar witness={non_scalar_witness:.12g})"
    )


if __name__ == "__main__":
    main()
