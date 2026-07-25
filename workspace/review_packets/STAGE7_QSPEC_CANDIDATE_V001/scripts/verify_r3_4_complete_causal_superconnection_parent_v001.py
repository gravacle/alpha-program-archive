#!/usr/bin/env python3
"""Independent state-level verifier for the complete causal parent."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_RESULT = (
    ROOT
    / "results"
    / "r3_4_complete_causal_superconnection_parent_v001.json"
)
VERIFY_RESULT = (
    ROOT
    / "results"
    / "r3_4_complete_causal_superconnection_parent_verification_v001.json"
)


def pauli_matrices():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def matrices():
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    gamma_spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = (
        1j
        * gamma0
        @ gamma_spatial[0]
        @ gamma_spatial[1]
        @ gamma_spatial[2]
    )
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    return gamma0, gamma_spatial, gamma5, c_partial


def embed(operator, site, count):
    result = np.array([[1.0]], dtype=complex)
    for index in range(count):
        result = np.kron(
            result,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return result


def derivative(site_count):
    result = np.zeros((site_count, site_count), dtype=complex)
    for site in range(site_count):
        result[site, (site + 1) % site_count] += 0.5
        result[site, (site - 1) % site_count] -= 0.5
    return result


def envelope(time):
    if time < 0.0 or time > 1.0:
        return 0.0
    return 32.0 * min(time, 1.0 - time) ** 3


def rk4_state(initial, hamiltonian, start, stop, steps):
    dt = (stop - start) / steps
    value = initial.astype(complex)

    def rhs(time, state):
        return -1j * hamiltonian(time) @ state

    for index in range(steps):
        time = start + index * dt
        k1 = rhs(time, value)
        k2 = rhs(time + dt / 2.0, value + dt * k1 / 2.0)
        k3 = rhs(time + dt / 2.0, value + dt * k2 / 2.0)
        k4 = rhs(time + dt, value + dt * k3)
        value = value + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return value


def reduce_first(state, source_dimension):
    tensor = state.reshape(source_dimension, 3, 3)
    return np.einsum("sab,sdb->ad", tensor, tensor.conjugate())


def main() -> None:
    primary = json.loads(PRIMARY_RESULT.read_text())
    gamma0, gamma_spatial, gamma5, c_partial = matrices()
    alpha_x = gamma0 @ gamma_spatial[0]
    incidence_spin = -1j * gamma0 @ gamma5

    site_count = 3
    record_count = 2
    record_dimension = 9
    source_dimension = site_count * 4
    momentum = -1j * derivative(site_count)
    h_source = np.kron(momentum, alpha_x)
    h_free = np.kron(h_source, np.eye(record_dimension, dtype=complex))
    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    writes = [
        np.kron(
            np.kron(mask, incidence_spin),
            embed(c_partial, index, record_count),
        )
        for index, mask in enumerate(masks)
    ]

    source_site = np.array([1.0, 0.0, 0.0], dtype=complex)
    source_spin = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(np.kron(source_site, source_spin), np.kron(ready, ready))
    action = math.pi / math.sqrt(2.0)

    first_hamiltonian = lambda time: h_free + action * envelope(time) * writes[0]
    second_hamiltonian = lambda time: h_free + action * envelope(time) * writes[1]
    after_first = rk4_state(initial, first_hamiltonian, 0.0, 1.0, 2400)
    after_second = rk4_state(
        after_first,
        second_hamiltonian,
        0.0,
        1.0,
        2400,
    )
    first_reduced = reduce_first(after_first, source_dimension)
    second_reduced = reduce_first(after_second, source_dimension)
    restriction_error = float(np.linalg.norm(first_reduced - second_reduced))

    pointer = np.diag([0.0, 1.0, 0.0]).astype(complex)
    pointer_operator = np.kron(
        np.eye(source_dimension, dtype=complex),
        embed(pointer, 0, record_count),
    )
    pointer_after_first = float(
        np.real(np.vdot(after_first, pointer_operator @ after_first))
    )
    pointer_after_second = float(
        np.real(np.vdot(after_second, pointer_operator @ after_second))
    )
    primary_finite = primary["finite_parent_regression"]
    comparisons = {
        "first_pointer_probability": abs(
            pointer_after_first
            - primary_finite["first_pointer_probability_after_first"]
        )
        < 2e-5,
        "second_pointer_probability": abs(
            pointer_after_second
            - primary_finite["first_pointer_probability_after_second"]
        )
        < 2e-5,
        "record_restriction": restriction_error < 2e-7,
        "primary_verdict": (
            primary["verdict"]
            == "FINITE_CAUSAL_PARENT_DERIVED_CONTINUUM_COMPLETION_OPEN"
        ),
        "alpha_false": primary["alpha_computed"] is False,
        "proof_false": primary["proof_authorized"] is False,
    }
    independent_verification_pass = all(comparisons.values())
    result = {
        "method": "independent RK4 state propagation",
        "rk4_steps_per_cell": 2400,
        "first_pointer_probability": pointer_after_first,
        "second_pointer_probability": pointer_after_second,
        "record_restriction_error": restriction_error,
        "comparisons": comparisons,
        "independent_verification_pass": independent_verification_pass,
        "construction_uses_alpha": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    VERIFY_RESULT.parent.mkdir(parents=True, exist_ok=True)
    VERIFY_RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
