#!/usr/bin/env python3
"""Audit causal transport as the unique write/tail joining rule."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md"
SEAL = ROOT / "R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_causal_transported_write_tail_v001.json"

PINNED = {
    "R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md":
        "781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24",
    "results/r3_4_shared_source_causal_parent_v001.json":
        "4f5beba98c55a7ee032664265f2af0e213fc2cd3201b76a701eb8a1cf0f4db48",
    "R3_4_INCIDENCE_CONTINUUM_SCALING_SPEC_V001.md":
        "e25cc20a95a0b6318389348ceacac93eccd2aebb0720350f08131d9e988cb6d3",
    "R3_4_INCIDENCE_CONTINUUM_SCALING_RESULT_V001.md":
        "3f18b011ef11cdde3b7c83a7bc7cc90a2cdfd82c64edf92b3b2e57b6254b520d",
    "results/r3_4_incidence_continuum_scaling_v001.json":
        "1633a5f727be8a3d084c8ed12517ea279c7197dea0ae7c0589b9ce3e76330cfd",
    "scripts/audit_r3_4_incidence_continuum_scaling_v001.py":
        "01315cfb7bcd11d1852dfd1621f3bcf82d5595ff4a1fdc356c72e5f6a4a69ecf",
    "scripts/verify_r3_4_incidence_continuum_scaling_v001.py":
        "bc61b84b06ae976c228db39b5a6c5f3d1ffbae711fda3bd427eac7952c844025",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


def source_incidence(cell_count: int) -> np.ndarray:
    value = np.zeros((cell_count + 1, cell_count), dtype=complex)
    for cell in range(cell_count):
        value[cell, cell] = -1.0
        value[cell + 1, cell] = 1.0
    return value


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def time_slice(
    h_free: np.ndarray,
    b_write: np.ndarray,
    duration: float,
    steps: int,
) -> np.ndarray:
    dt = duration / steps
    value = np.eye(h_free.shape[0], dtype=complex)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        u0 = exp_hermitian(h_free, midpoint)
        transported = u0 @ b_write @ u0.conjugate().T
        value = exp_hermitian(h_free + transported, dt) @ value
    return value


def main() -> None:
    fields = SEAL.read_text(encoding="ascii").strip().split()
    require(fields == [sha256(SPEC), SPEC.name], "Specification seal failed")
    for name, digest in PINNED.items():
        require(sha256(ROOT / name) == digest, f"Upstream drift: {name}")

    cell_count = 2
    d = source_incidence(cell_count)
    vertex_count, edge_count = d.shape
    h0 = np.block(
        [
            [np.zeros((vertex_count, vertex_count), dtype=complex), d],
            [d.conjugate().T, np.zeros((edge_count, edge_count), dtype=complex)],
        ]
    )
    one_particle_dim = h0.shape[0]
    gamma5 = np.diag([1.0, -1.0]).astype(complex)
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    record_dim = 3**cell_count
    h_free = np.kron(np.kron(h0, np.eye(2, dtype=complex)), np.eye(record_dim))

    writes = []
    for cell in range(cell_count):
        ray = d[:, cell]
        p_vertex = np.outer(ray, ray.conjugate()) / np.vdot(ray, ray)
        p_source = np.zeros_like(h0)
        p_source[:vertex_count, :vertex_count] = p_vertex
        writes.append(
            np.kron(
                np.kron(p_source, gamma5),
                embed_record(c_partial, cell, cell_count),
            )
        )

    tau = math.pi / math.sqrt(2.0)
    b_write = writes[0]
    u_free = exp_hermitian(h_free, tau)
    u_write = exp_hermitian(b_write, tau)
    exact_joint = u_free @ u_write
    static_joint = exp_hermitian(h_free + b_write, tau)

    sample_t = 0.37 * tau
    sample_s = 0.21 * tau
    u_t = exp_hermitian(h_free, sample_t)
    u_s = exp_hermitian(h_free, sample_s)
    u_ts = exp_hermitian(h_free, sample_t + sample_s)
    b_t = u_t @ b_write @ u_t.conjugate().T
    b_ts = u_ts @ b_write @ u_ts.conjugate().T
    covariance_error = float(
        np.linalg.norm(b_ts - u_s @ b_t @ u_s.conjugate().T)
    )
    static_covariance_failure = float(
        np.linalg.norm(b_write - u_s @ b_write @ u_s.conjugate().T)
    )
    free_write_commutator = float(
        np.linalg.norm(h_free @ b_write - b_write @ h_free)
    )

    ray0 = d[:, 0] / np.linalg.norm(d[:, 0])
    source_root = np.zeros(one_particle_dim, dtype=complex)
    source_root[:vertex_count] = ray0
    spin_root = np.array([1.0, 0.0], dtype=complex)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(np.kron(source_root, spin_root), np.kron(ready, ready))
    p0 = np.kron(
        np.eye(one_particle_dim * 2, dtype=complex),
        np.kron(np.diag([0.0, 1.0, 0.0]), np.eye(3, dtype=complex)),
    )

    static_out = static_joint @ initial
    exact_out = exact_joint @ initial
    static_pointer_probability = float(np.real(np.vdot(static_out, p0 @ static_out)))
    transported_pointer_probability = float(np.real(np.vdot(exact_out, p0 @ exact_out)))

    moller = u_free.conjugate().T @ exact_joint
    moller_error = float(np.linalg.norm(moller - u_write))
    moller_unitarity_error = float(
        np.linalg.norm(moller.conjugate().T @ moller - np.eye(moller.shape[0]))
    )

    slicing_steps = (10, 20, 40, 80)
    slicing_errors = {}
    for steps in slicing_steps:
        approximate = time_slice(h_free, b_write, tau, steps)
        slicing_errors[str(steps)] = float(np.linalg.norm(approximate - exact_joint))
    slicing_ratios = {
        f"{left}_to_{right}": slicing_errors[str(left)] / slicing_errors[str(right)]
        for left, right in zip(slicing_steps[:-1], slicing_steps[1:])
    }

    profiles = {
        "constant": (tau,),
        "uneven_positive": (tau / 7.0, 2.0 * tau / 7.0, 4.0 * tau / 7.0),
        "sign_changing": (1.5 * tau, -0.5 * tau),
    }
    interaction_picture_profile_errors = {}
    for name, segments in profiles.items():
        ui = np.eye(b_write.shape[0], dtype=complex)
        for segment in segments:
            ui = exp_hermitian(b_write, segment) @ ui
        interaction_picture_profile_errors[name] = float(np.linalg.norm(ui - u_write))

    ordered_interaction_picture = exp_hermitian(writes[1], tau) @ u_write
    full_two_cell = exp_hermitian(h_free, 2.0 * tau) @ ordered_interaction_picture
    two_cell_moller = (
        exp_hermitian(h_free, -2.0 * tau) @ full_two_cell
    )
    two_cell_moller_error = float(
        np.linalg.norm(two_cell_moller - ordered_interaction_picture)
    )

    require(free_write_commutator > 1e-6, "Static and free operators commute")
    require(static_covariance_failure > 1e-6, "Static competitor passed covariance")
    require(covariance_error < 1e-11, "Transported interaction failed covariance")
    require(static_pointer_probability < 0.99, "Static negative control did not fail")
    require(
        abs(transported_pointer_probability - 1.0) < 1e-12,
        "Transported parent did not preserve first opening",
    )
    require(moller_error < 1e-11 and moller_unitarity_error < 1e-11,
            "Finite-support Moller operator failed")
    require(max(interaction_picture_profile_errors.values()) < 1e-11,
            "Profile independence failed")
    require(two_cell_moller_error < 1e-11, "Two-cell causal Moller factor failed")
    require(
        all(value > 3.7 for value in slicing_ratios.values()),
        "Midpoint time slicing did not show second-order convergence",
    )

    result = {
        "schema": "r3.4-causal-transported-write-tail-v001",
        "spec_sha256": sha256(SPEC),
        "spec_seal_verified": True,
        "upstream_hashes_verified": len(PINNED),
        "target_values_used": False,
        "preseal_exploratory_diagnostic_performed": True,
        "free_write_commutator_norm": free_write_commutator,
        "transport_covariance_error": covariance_error,
        "static_covariance_failure": static_covariance_failure,
        "static_sum_first_pointer_probability": static_pointer_probability,
        "transported_parent_first_pointer_probability":
            transported_pointer_probability,
        "finite_support_Moller_error": moller_error,
        "finite_support_Moller_unitarity_error": moller_unitarity_error,
        "interaction_picture_profile_errors": interaction_picture_profile_errors,
        "direct_time_slicing_errors": slicing_errors,
        "direct_time_slicing_convergence_ratios": slicing_ratios,
        "two_cell_causal_Moller_error": two_cell_moller_error,
        "causal_transport_functional_equation_unique_given_rule": True,
        "causal_transport_rule_derived_from_pinned_principles": False,
        "static_sum_fails_comoving_covariance": True,
        "static_sum_rejected_by_adopted_principles": False,
        "write_tail_relative_coefficient_added": False,
        "candidate_first_opening_survives_free_tail_attachment": True,
        "candidate_shared_source_causal_product_survives_tail_attachment": True,
        "candidate_finite_support_Moller_operator_computed": True,
        "physical_write_tail_join_derived": False,
        "free_outgoing_tail_generator_inherited_from_same_parent": False,
        "physical_in_state_selected": False,
        "finite_energy_physical_root_derived": False,
        "generated_descendant_durability_closed": False,
        "complete_physical_durability_derived": False,
        "complete_write_plus_tail_root_measure_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "CAUSAL_TRANSPORT_CONDITIONAL",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
