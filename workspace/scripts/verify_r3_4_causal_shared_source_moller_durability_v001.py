#!/usr/bin/env python3
"""Independent state-vector verifier for the causal shared-source parent."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_SPEC_V001.md"
RESULT = (
    ROOT
    / "results"
    / "r3_4_causal_shared_source_moller_durability_v001.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def weight(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * (0.5 - abs(local_time - 0.5)) ** 3


def rk4_pulse(
    state: np.ndarray,
    h_free: np.ndarray,
    write: np.ndarray,
    integrated_action: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps

    def derivative(local_time: float, vector: np.ndarray) -> np.ndarray:
        hamiltonian = h_free + integrated_action * weight(local_time) * write
        return -1.0j * hamiltonian @ vector

    value = state.copy()
    for index in range(steps):
        time = index * dt
        k1 = derivative(time, value)
        k2 = derivative(time + dt / 2.0, value + dt * k1 / 2.0)
        k3 = derivative(time + dt / 2.0, value + dt * k2 / 2.0)
        k4 = derivative(time + dt, value + dt * k3)
        value = value + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    return value


def probability(state: np.ndarray, projector: np.ndarray) -> float:
    return float(np.real(np.vdot(state, projector @ state)))


def main() -> None:
    stored = json.loads(RESULT.read_text(encoding="ascii"))
    require(
        stored["spec_sha256"] == hashlib.sha256(SPEC.read_bytes()).hexdigest(),
        "Specification digest mismatch",
    )

    incidence = np.zeros((3, 2), dtype=complex)
    incidence[0, 0] = -1.0
    incidence[1, 0] = 1.0
    incidence[1, 1] = -1.0
    incidence[2, 1] = 1.0
    h_source = incidence @ incidence.conjugate().T
    projectors = tuple(
        np.outer(incidence[:, j], incidence[:, j].conjugate()) / 2.0
        for j in range(2)
    )
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    h_free = np.kron(h_source, np.eye(9, dtype=complex))
    writes = tuple(
        np.kron(projectors[j], embed_record(c_partial, j, 2))
        for j in range(2)
    )
    pointer = np.diag([0.0, 1.0, 0.0]).astype(complex)
    pointer_zero = np.kron(
        np.eye(3, dtype=complex), embed_record(pointer, 0, 2)
    )

    source_root = incidence[:, 0] / np.linalg.norm(incidence[:, 0])
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(source_root, np.kron(ready, ready))
    action = math.pi / math.sqrt(2.0)
    after_first = rk4_pulse(initial, h_free, writes[0], action, 4000)
    after_second = rk4_pulse(after_first, h_free, writes[1], action, 4000)
    first_probability = probability(after_first, pointer_zero)
    second_probability = probability(after_second, pointer_zero)

    expected = stored["first_pointer_probabilities"]
    require(
        abs(first_probability - expected["after_first_closure"]) < 5e-5,
        "Independent first-pulse probability mismatch",
    )
    require(
        abs(second_probability - expected["after_second_closure"]) < 5e-5,
        "Independent second-pulse probability mismatch",
    )
    require(
        abs(second_probability - first_probability) < 2e-10,
        "Independent evolution rewrote the completed pointer",
    )
    require(
        np.linalg.norm(h_free @ pointer_zero - pointer_zero @ h_free) < 1e-13,
        "Free generator changes completed pointer",
    )
    require(
        np.linalg.norm(writes[1] @ pointer_zero - pointer_zero @ writes[1])
        < 1e-13,
        "Later primitive interaction changes completed pointer",
    )
    require(
        stored["primitive_finite_support_Moller_derived"] is True,
        "Finite-support Moller result missing",
    )
    require(
        stored["generated_descendant_action_derived"] is False,
        "Generated descendants were overclaimed",
    )
    require(
        stored["complete_physical_durability_derived"] is False,
        "Complete durability was overclaimed",
    )
    require(stored["alpha_computed"] is False, "Alpha was promoted")
    require(
        stored["status"]
        == "PRIMITIVE_CAUSAL_MOLLER_AND_PUBLIC_DURABILITY_DERIVED",
        "Wrong verdict",
    )
    print("PASS independent causal shared-source Moller/durability verification")


if __name__ == "__main__":
    main()
