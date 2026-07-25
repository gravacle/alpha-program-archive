#!/usr/bin/env python3
"""Target-free diagnostics for the reduced-to-full Qspec transfer bridge."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = (
    ROOT
    / "scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py"
)


def generated_algebra_dimension(
    generators: tuple[np.ndarray, ...],
    tolerance: float = 1e-11,
) -> tuple[int, list[float]]:
    dimension = generators[0].shape[0]
    basis: list[np.ndarray] = []

    def add(candidate: np.ndarray) -> bool:
        vector = candidate.reshape(-1).astype(complex)
        for item in basis:
            vector -= np.vdot(item.reshape(-1), vector) * item.reshape(-1)
        norm = np.linalg.norm(vector)
        if norm <= tolerance:
            return False
        basis.append((vector / norm).reshape(dimension, dimension))
        return True

    add(np.eye(dimension, dtype=complex))
    for generator in generators:
        add(generator)
    changed = True
    while changed:
        changed = False
        snapshot = tuple(basis)
        for left in snapshot:
            for right in generators:
                changed = add(left @ right) or changed
    gram = np.column_stack([item.reshape(-1) for item in basis])
    singular = np.linalg.svd(gram, compute_uv=False)
    return len(basis), [float(value) for value in singular]


def commutant_nullity(
    generators: tuple[np.ndarray, ...],
    tolerance: float = 1e-10,
) -> tuple[int, list[float]]:
    dimension = generators[0].shape[0]
    identity = np.eye(dimension, dtype=complex)
    equations = np.row_stack(
        tuple(
            np.kron(identity, generator)
            - np.kron(generator.T, identity)
            for generator in generators
        )
    )
    singular = np.linalg.svd(equations, compute_uv=False)
    return (
        int(np.sum(singular < tolerance)),
        [float(value) for value in singular],
    )


def reachable_generator_support(
    initial: np.ndarray,
    generators: tuple[np.ndarray, ...],
    tolerance: float = 1e-11,
) -> tuple[np.ndarray, list[dict[str, object]]]:
    basis = initial[:, np.newaxis]
    rows = []
    for iteration in range(initial.size):
        candidates = np.column_stack(
            (basis, *(generator @ basis for generator in generators))
        )
        left, singular, _ = np.linalg.svd(candidates, full_matrices=False)
        next_basis = left[:, singular > tolerance]
        rows.append(
            {
                "iteration": iteration,
                "rank": int(next_basis.shape[1]),
                "singular_values": [float(value) for value in singular],
            }
        )
        if next_basis.shape[1] == basis.shape[1]:
            return next_basis, rows
        basis = next_basis
    return basis, rows


def load_verifier():
    spec = importlib.util.spec_from_file_location("qspec_v003", VERIFIER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def complement_operator(
    left_kraus: tuple[np.ndarray, ...],
    right_kraus: tuple[np.ndarray, ...],
) -> tuple:
    left_dimension = left_kraus[0].shape[0]
    right_dimension = right_kraus[0].shape[0]
    dimension = left_dimension * right_dimension

    def matvec(vector: np.ndarray) -> np.ndarray:
        matrix = vector.reshape(left_dimension, right_dimension)
        result = sum(
            left @ matrix @ right.conjugate().T
            for left, right in zip(left_kraus, right_kraus)
        )
        return result.reshape(-1)

    def rmatvec(vector: np.ndarray) -> np.ndarray:
        matrix = vector.reshape(left_dimension, right_dimension)
        result = sum(
            left.conjugate().T @ matrix @ right
            for left, right in zip(left_kraus, right_kraus)
        )
        return result.reshape(-1)

    return dimension, matvec, rmatvec


def largest_singular_value_power(
    dimension: int,
    matvec,
    rmatvec,
    iterations: int = 300,
) -> tuple[float, float]:
    rng = np.random.default_rng(20260725)
    vector = (
        rng.standard_normal(dimension)
        + 1j * rng.standard_normal(dimension)
    )
    vector /= np.linalg.norm(vector)
    previous = 0.0
    for _ in range(iterations):
        image = matvec(vector)
        adjoint_image = rmatvec(image)
        norm = np.linalg.norm(adjoint_image)
        if norm == 0:
            return 0.0, 0.0
        vector = adjoint_image / norm
        estimate = float(np.linalg.norm(image))
        if abs(estimate - previous) < 1e-13:
            break
        previous = estimate
    residual = float(
        np.linalg.norm(
            rmatvec(matvec(vector)) - estimate * estimate * vector
        )
    )
    return estimate, residual


def main() -> None:
    verifier = load_verifier()
    alpha_x, incidence_spin = verifier.dirac_operators()
    full_zero = np.kron(
        -1j * verifier.directed_difference(0.0),
        alpha_x,
    )
    one_body_values, one_body_vectors = np.linalg.eigh(full_zero)
    active = np.abs(one_body_values) > 1e-12
    active_values = one_body_values[active]
    active_vectors = one_body_vectors[:, active]
    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    one_body_interactions = tuple(
        active_vectors.conjugate().T
        @ np.kron(mask, incidence_spin)
        @ active_vectors
        for mask in masks
    )
    one_body_generators = (
        np.diag(active_values),
        *one_body_interactions,
    )
    algebra_dimension, algebra_singular = generated_algebra_dimension(
        one_body_generators
    )
    commutant_dimension, commutant_singular = commutant_nullity(
        one_body_generators
    )

    parent = verifier.build_parent()
    generator_support, generator_support_rows = (
        reachable_generator_support(
            parent["source_vector"],
            (
                parent["free_zero"],
                *parent["interactions"],
            ),
        )
    )
    raw_cells = tuple(
        verifier.cell_kraus(
            parent["free_zero"],
            interaction,
            parent["record"],
            use_hermitian_spectral_step=True,
        )
        for interaction in parent["interactions"]
    )
    repaired = tuple(
        verifier.retract_stinespring_isometry(kraus)
        for kraus in raw_cells
    )
    zero_cells = tuple(item[0] for item in repaired)
    zero_composites = verifier.composite_kraus(zero_cells)
    support, support_residual = verifier.reachable_support(
        parent["source_vector"],
        zero_composites,
    )

    source_dimension = support.shape[0]
    projector = support @ support.conjugate().T
    projector_diagonal = np.real(np.diag(projector))
    q_values, q_vectors = np.linalg.eigh(
        (np.eye(source_dimension) - projector
         + (np.eye(source_dimension) - projector).conjugate().T)
        / 2
    )
    complement = q_vectors[:, q_values > 0.5]

    leakage_blocks = tuple(
        complement.conjugate().T @ operator @ support
        for operator in zero_composites
    )
    return_blocks = tuple(
        support.conjugate().T @ operator @ complement
        for operator in zero_composites
    )
    complement_blocks = tuple(
        complement.conjugate().T @ operator @ complement
        for operator in zero_composites
    )

    red_to_leak = sum(
        np.kron(left, leak.conjugate())
        for left, leak in zip(zero_composites, leakage_blocks)
    )
    leak_to_red = sum(
        np.kron(left, ret.conjugate())
        for left, ret in zip(zero_composites, return_blocks)
    )

    complement_dimension_total, complement_matvec, complement_rmatvec = (
        complement_operator(
        zero_composites,
        complement_blocks,
        )
    )
    largest_complement_sv, complement_power_residual = (
        largest_singular_value_power(
            complement_dimension_total,
            complement_matvec,
            complement_rmatvec,
        )
    )

    krylov_rows = []
    basis = parent["source_vector"][:, np.newaxis]
    for iteration in range(8):
        candidates = np.column_stack(
            (basis, *(operator @ basis for operator in zero_composites))
        )
        _, singular, _ = np.linalg.svd(candidates, full_matrices=False)
        krylov_rows.append(
            {
                "iteration": iteration,
                "candidate_columns": candidates.shape[1],
                "singular_values": [float(value) for value in singular],
            }
        )
        basis = np.linalg.svd(candidates, full_matrices=False)[0][
            :, singular > 1e-11
        ]

    report = {
        "schema": "complete_qspec_reduced_full_bridge_diagnostic_v001",
        "source_dimension": source_dimension,
        "active_one_body_dimension": len(active_values),
        "active_one_body_eigenvalues": [
            float(value) for value in active_values
        ],
        "one_body_generated_algebra_dimension": algebra_dimension,
        "one_body_generated_algebra_basis_singular_values":
            algebra_singular,
        "one_body_commutant_dimension": commutant_dimension,
        "one_body_commutant_smallest_singular_values":
            sorted(commutant_singular)[:20],
        "support_dimension": support.shape[1],
        "generator_reachable_support_dimension":
            generator_support.shape[1],
        "generator_reachable_support_iterations":
            generator_support_rows,
        "complement_dimension": complement.shape[1],
        "composite_kraus_count": len(zero_composites),
        "reported_support_residual": support_residual,
        "support_projector_diagonal": [
            {
                "row": int(index),
                "weight": float(weight),
            }
            for index, weight in sorted(
                enumerate(projector_diagonal),
                key=lambda item: item[1],
                reverse=True,
            )
            if weight > 1e-12
        ],
        "individual_leakage_norms": [
            float(np.linalg.norm(block, 2))
            for block in leakage_blocks
        ],
        "individual_return_norms": [
            float(np.linalg.norm(block, 2))
            for block in return_blocks
        ],
        "individual_complement_norms": [
            float(np.linalg.norm(block, 2))
            for block in complement_blocks
        ],
        "red_to_leak_superoperator_norm": float(
            np.linalg.norm(red_to_leak, 2)
        ),
        "leak_to_red_superoperator_norm": float(
            np.linalg.norm(leak_to_red, 2)
        ),
        "complement_superoperator_norm_approx":
            largest_complement_sv,
        "complement_power_normal_equation_residual":
            complement_power_residual,
        "krylov_singular_spectra": krylov_rows,
        "proof_status_changed": False,
        "kappa_record_computed": False,
        "alpha_computed": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
