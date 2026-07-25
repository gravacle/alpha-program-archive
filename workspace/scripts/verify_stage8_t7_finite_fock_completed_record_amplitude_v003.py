#!/usr/bin/env python3
"""Portable independent CAR/RK4 verification of finite-Fock amplitudes.

v003 retains v002's Python 3.9 compatibility repair and doubles both RK4
resolutions after sealed v002 failed its unchanged 2e-9 tail gate.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "stage8_execution/work/T07_finite_fock_completed_record_amplitude.json"

# Frozen before the independent amplitudes were evaluated. The primary
# second-order tail estimate is 1.8934e-4 / 3 = 6.311e-5.
COMPLEX_AMPLITUDE_TOLERANCE = 1.0e-4


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def population_count(bits: int) -> int:
    return bin(bits).count("1")


def dirac_operators() -> tuple[np.ndarray, np.ndarray]:
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    eye_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    gamma_0 = np.block([[eye_2, zero_2], [zero_2, -eye_2]])
    gamma_space = tuple(
        np.block([[zero_2, sigma], [-sigma, zero_2]])
        for sigma in (sigma_1, sigma_2, sigma_3)
    )
    gamma_5 = (
        1j
        * gamma_0
        @ gamma_space[0]
        @ gamma_space[1]
        @ gamma_space[2]
    )
    return gamma_0 @ gamma_space[0], -1j * gamma_0 @ gamma_5


def canonical_range_basis(projector: np.ndarray, rank: int) -> np.ndarray:
    """Build a range basis by canonical-column Gram-Schmidt, not eigencolumns."""
    accepted: list[np.ndarray] = []
    for column in range(projector.shape[1]):
        candidate = projector[:, column].copy()
        for vector in accepted:
            candidate -= vector * np.vdot(vector, candidate)
        norm = np.linalg.norm(candidate)
        if norm > 1e-10:
            accepted.append(candidate / norm)
        if len(accepted) == rank:
            break
    require(len(accepted) == rank, "Canonical range construction lost rank")
    basis = np.column_stack(accepted)
    require(
        np.linalg.norm(basis.conjugate().T @ basis - np.eye(rank)) < 1e-12,
        "Canonical range basis is not orthonormal",
    )
    return basis


def fixed_number_lift(
    one_body: np.ndarray,
    particle_count: int,
) -> tuple[np.ndarray, tuple[int, ...]]:
    """Lift with raw occupation-bit CAR signs, independent of the primary path."""
    dimension = one_body.shape[0]
    states = tuple(
        bits
        for bits in range(1 << dimension)
        if population_count(bits) == particle_count
    )
    state_to_row = {bits: row for row, bits in enumerate(states)}
    lifted = np.zeros((len(states), len(states)), dtype=complex)

    for column, bits in enumerate(states):
        for annihilated in range(dimension):
            if not bits & (1 << annihilated):
                continue
            sign_a = (
                -1
                if population_count(bits & ((1 << annihilated) - 1)) % 2
                else 1
            )
            reduced = bits ^ (1 << annihilated)
            for created in range(dimension):
                if reduced & (1 << created):
                    continue
                sign_c = (
                    -1
                    if population_count(reduced & ((1 << created) - 1)) % 2
                    else 1
                )
                output = reduced | (1 << created)
                lifted[state_to_row[output], column] += (
                    sign_a * sign_c * one_body[created, annihilated]
                )
    return lifted, states


def slater_coordinates(
    occupied_orbitals: np.ndarray,
    bit_states: tuple[int, ...],
) -> np.ndarray:
    vector = np.zeros(len(bit_states), dtype=complex)
    for row, bits in enumerate(bit_states):
        occupied_rows = [
            index
            for index in range(occupied_orbitals.shape[0])
            if bits & (1 << index)
        ]
        vector[row] = np.linalg.det(occupied_orbitals[occupied_rows, :])
    require(abs(np.linalg.norm(vector) - 1.0) < 1e-12, "Slater norm changed")
    return vector


def record_embedding(operator: np.ndarray, cell: int) -> np.ndarray:
    eye_3 = np.eye(3, dtype=complex)
    if cell == 0:
        return np.kron(operator, eye_3)
    return np.kron(eye_3, operator)


def diamond_envelope(local_time: float) -> float:
    if local_time < 0.0 or local_time > 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def rk4_cell(
    initial: np.ndarray,
    free: np.ndarray,
    source_write: np.ndarray,
    record_write: np.ndarray,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    action = math.pi / math.sqrt(2.0)

    def flow(time: float, state: np.ndarray) -> np.ndarray:
        interaction = (
            source_write
            @ state
            @ record_write.T
        )
        return -1j * (
            free @ state
            + action * diamond_envelope(time) * interaction
        )

    state = initial.copy()
    for index in range(steps):
        time = index * dt
        k1 = flow(time, state)
        k2 = flow(time + dt / 2.0, state + dt * k1 / 2.0)
        k3 = flow(time + dt / 2.0, state + dt * k2 / 2.0)
        k4 = flow(time + dt, state + dt * k3)
        state += dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    return state


def evolve(
    initial: np.ndarray,
    free: np.ndarray,
    writes: tuple[np.ndarray, np.ndarray],
    record_writes: tuple[np.ndarray, np.ndarray],
    steps: int,
) -> tuple[np.ndarray, np.ndarray]:
    first = rk4_cell(initial, free, writes[0], record_writes[0], steps)
    second = rk4_cell(first, free, writes[1], record_writes[1], steps)
    return first, second


def complex_from_record(data: dict[str, float]) -> complex:
    return complex(data["real"], data["imag"])


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="utf-8"))
    require(
        stored["overall_verdict"]
        == "FINITE_FOCK_COMPLETED_RECORD_BASELINE_DERIVED",
        "Primary result did not retain its finite-baseline verdict",
    )

    alpha_x, incidence_spin = dirac_operators()
    derivative = np.zeros((3, 3), dtype=complex)
    for site in range(3):
        derivative[site, (site + 1) % 3] = 0.5
        derivative[site, (site - 1) % 3] = -0.5
    parent_free = np.kron(-1j * derivative, alpha_x)

    parent_values, parent_vectors = np.linalg.eigh(parent_free)
    nonzero = np.abs(parent_values) > 1e-12
    active_projector = (
        parent_vectors[:, nonzero]
        @ parent_vectors[:, nonzero].conjugate().T
    )
    active_basis = canonical_range_basis(active_projector, 8)
    free_one_body = active_basis.conjugate().T @ parent_free @ active_basis

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    writes_one_body = tuple(
        active_basis.conjugate().T
        @ np.kron(mask, incidence_spin)
        @ active_basis
        for mask in masks
    )

    free_fock, bit_states = fixed_number_lift(free_one_body, 4)
    writes_fock = tuple(
        fixed_number_lift(write, 4)[0]
        for write in writes_one_body
    )
    free_values, free_vectors = np.linalg.eigh(free_one_body)
    negative_orbitals = free_vectors[:, free_values < -1e-12]
    require(negative_orbitals.shape == (8, 4), "Occupied rank changed")
    source_state = slater_coordinates(negative_orbitals, bit_states)

    partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    record_writes = (
        record_embedding(partial, 0),
        record_embedding(partial, 1),
    )
    initial = np.zeros((len(bit_states), 9), dtype=complex)
    initial[:, 0] = source_state

    coarse = evolve(initial, free_fock, writes_fock, record_writes, 1600)
    fine = evolve(initial, free_fock, writes_fock, record_writes, 3200)
    rk4_tail = float(np.linalg.norm(coarse[1] - fine[1]))
    require(rk4_tail < 2e-9, f"RK4 tail too large: {rk4_tail}")

    source_bra = source_state.conjugate()
    independent_one = complex(source_bra @ fine[0][:, 3])
    independent_two = complex(source_bra @ fine[1][:, 4])
    primary_one = complex_from_record(stored["one_cell_completed_amplitude"])
    primary_two = complex_from_record(stored["two_cell_completed_amplitude"])
    one_difference = abs(independent_one - primary_one)
    two_difference = abs(independent_two - primary_two)

    require(
        one_difference < COMPLEX_AMPLITUDE_TOLERANCE,
        "Independent one-cell amplitude mismatch: "
        f"{independent_one!r} versus {primary_one!r}",
    )
    require(
        two_difference < COMPLEX_AMPLITUDE_TOLERANCE,
        "Independent two-cell amplitude mismatch: "
        f"{independent_two!r} versus {primary_two!r}",
    )
    require(abs(independent_one) > 1e-8, "Independent one-cell amplitude vanished")
    require(abs(independent_two) > 1e-8, "Independent two-cell amplitude vanished")
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(stored["proof_authorized"] is False, "Proof was authorized")

    print(
        "PASS independent finite-Fock completed-record verification "
        f"(RK4 tail={rk4_tail:.3e}, "
        f"|delta a_p|={one_difference:.3e}, "
        f"|delta a_pp|={two_difference:.3e})"
    )


if __name__ == "__main__":
    main()
