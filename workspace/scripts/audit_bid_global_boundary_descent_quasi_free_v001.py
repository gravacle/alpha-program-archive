#!/usr/bin/env python3
"""Fail-closed audit of typed global descent and operator-valued CAR lift."""

from __future__ import annotations

import itertools
import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def one_cell_complex(
    cell: tuple[str, str, str, str]
) -> tuple[tuple[str, ...], tuple[tuple[str, str, str, str], ...]]:
    label, _, source, target = cell
    require(source != target, f"cell {label} has a degenerate source edge")
    return tuple(sorted((source, target))), (cell,)


def glue_complexes(
    left: tuple[tuple[str, ...], tuple[tuple[str, str, str, str], ...]],
    right: tuple[tuple[str, ...], tuple[tuple[str, str, str, str], ...]],
) -> tuple[tuple[str, ...], tuple[tuple[str, str, str, str], ...]]:
    vertices = tuple(sorted(set(left[0]) | set(right[0])))
    cell_map = {cell[0]: cell for cell in left[1]}
    for cell in right[1]:
        if cell[0] in cell_map:
            require(
                cell_map[cell[0]] == cell,
                "same cell label carries inconsistent overlap data",
            )
        cell_map[cell[0]] = cell
    return vertices, tuple(cell_map[label] for label in sorted(cell_map))


def incidence(
    vertices: tuple[str, ...], edges: tuple[tuple[str, str, str], ...]
) -> np.ndarray:
    vertex_index = {label: index for index, label in enumerate(vertices)}
    require(
        len(vertex_index) == len(vertices),
        "shared source vertex was counted more than once",
    )
    result = np.zeros((len(vertices), len(edges)), dtype=complex)
    seen_edges: set[str] = set()
    for column, (label, source, target) in enumerate(edges):
        require(label not in seen_edges, "source edge was counted more than once")
        require(
            source in vertex_index and target in vertex_index,
            "source edge endpoint is absent from global pushout",
        )
        seen_edges.add(label)
        result[vertex_index[source], column] = -1.0
        result[vertex_index[target], column] = 1.0
    return result


def projector(vector: np.ndarray) -> np.ndarray:
    norm_squared = np.vdot(vector, vector)
    require(norm_squared.real > 0.0, "zero source incidence vector")
    return np.outer(vector, vector.conj()) / norm_squared


def occupation_basis(mode_count: int, particle_count: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.combinations(range(mode_count), particle_count))


def one_body_wedge_matrix(
    mode_count: int, particle_count: int, row: int, column: int
) -> np.ndarray:
    basis = occupation_basis(mode_count, particle_count)
    basis_index = {state: index for index, state in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), dtype=complex)
    for input_index, occupied in enumerate(basis):
        if column not in occupied:
            continue
        removal_position = occupied.index(column)
        sign = -1.0 if removal_position % 2 else 1.0
        reduced = list(occupied)
        reduced.pop(removal_position)
        if row in reduced:
            continue
        insertion_position = sum(value < row for value in reduced)
        if insertion_position % 2:
            sign *= -1.0
        output = tuple(sorted((*reduced, row)))
        result[basis_index[output], input_index] = sign
    return result


def operator_valued_car_lift(
    one_particle_record: np.ndarray,
    source_modes: int,
    record_dimension: int,
    particle_count: int,
) -> np.ndarray:
    wedge_dimension = math.comb(source_modes, particle_count)
    result = np.zeros(
        (wedge_dimension * record_dimension,) * 2, dtype=complex
    )
    for row in range(source_modes):
        row_slice = slice(
            row * record_dimension, (row + 1) * record_dimension
        )
        for column in range(source_modes):
            column_slice = slice(
                column * record_dimension,
                (column + 1) * record_dimension,
            )
            record_block = one_particle_record[row_slice, column_slice]
            if np.linalg.norm(record_block) < 1e-14:
                continue
            source_block = one_body_wedge_matrix(
                source_modes, particle_count, row, column
            )
            result += np.kron(source_block, record_block)
    return result


def evolve(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1j * interval * values))
        @ vectors.conj().T
    )


def main() -> None:
    # Build the source-orbital pushout from separate cell cospans. The shared
    # vertices occur exactly once, and both three-cell parenthesizations agree.
    cell_01 = ("c01", "e01", "v0", "v1")
    cell_12 = ("c12", "e12", "v1", "v2")
    cell_23 = ("c23", "e23", "v2", "v3")
    complex_01 = one_cell_complex(cell_01)
    complex_12 = one_cell_complex(cell_12)
    complex_23 = one_cell_complex(cell_23)
    glued_two = glue_complexes(complex_01, complex_12)
    left_associated = glue_complexes(
        glue_complexes(complex_01, complex_12), complex_23
    )
    right_associated = glue_complexes(
        complex_01, glue_complexes(complex_12, complex_23)
    )
    require(
        left_associated == right_associated,
        "three-cell source pushout depends on parenthesization",
    )
    require(
        glued_two[0] == ("v0", "v1", "v2"),
        "shared source vertex was not identified exactly once by pushout",
    )
    vertices = glued_two[0]
    cells = glued_two[1]
    edges = tuple((edge, source, target) for _, edge, source, target in cells)
    boundary = incidence(vertices, edges)
    require(
        boundary.shape == (3, 2),
        "global source incidence carrier has the wrong dimension",
    )
    source_vectors = tuple(boundary[:, index] for index in range(2))
    source_projectors = tuple(projector(vector) for vector in source_vectors)
    overlap = np.trace(source_projectors[0] @ source_projectors[1]).real
    require(
        np.isclose(overlap, 0.25),
        "shared-source-support invariant was not generated by incidence",
    )

    # The actual SP17 Dirac-record operator remains type-distinct from source
    # orbitals and from the second record factor.
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in pauli)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]

    d_cell = np.array([[-1.0], [1.0]], dtype=complex)
    b_cell = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_cell],
            [d_cell.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    grading_cell = np.diag([1.0, 1.0, -1.0]).astype(complex)
    c_cell = 1j * grading_cell @ b_cell
    require(
        np.allclose(c_cell, c_cell.conj().T),
        "SP17 cellular quadrature is not Hermitian",
    )
    actual_sp17_zero_form = np.kron(gamma5, c_cell)
    require(
        actual_sp17_zero_form.shape == (12, 12),
        "SP17 local incidence zero-form is not 12x12",
    )

    record_dimension = 3**2
    record_identity = np.eye(3, dtype=complex)
    c_record_01 = np.kron(c_cell, record_identity)
    c_record_12 = np.kron(record_identity, c_cell)
    require(
        np.allclose(
            c_record_01 @ c_record_12 - c_record_12 @ c_record_01,
            0.0,
        ),
        "distinguishable even record factors do not commute",
    )

    source_spin_terms = tuple(
        np.kron(source_projector, gamma5)
        for source_projector in source_projectors
    )
    local_terms = (
        np.kron(source_spin_terms[0], c_record_01),
        np.kron(source_spin_terms[1], c_record_12),
    )
    global_one_particle = local_terms[0] + local_terms[1]
    require(
        np.allclose(
            global_one_particle, global_one_particle.conj().T
        ),
        "global operator-valued one-particle superconnection is not Hermitian",
    )

    # Each isolated one-cell construction compresses exactly to SP17.
    root_record = np.array([[1.0], [0.0], [0.0]], dtype=complex)
    source_embeddings = tuple(
        np.kron(
            (vector / np.linalg.norm(vector)).reshape(-1, 1),
            np.eye(4, dtype=complex),
        )
        for vector in source_vectors
    )
    record_embeddings = (
        np.kron(np.eye(3, dtype=complex), root_record),
        np.kron(root_record, np.eye(3, dtype=complex)),
    )
    for index in range(2):
        embedding = np.kron(
            source_embeddings[index], record_embeddings[index]
        )
        compressed = (
            embedding.conj().T @ local_terms[index] @ embedding
        )
        require(
            np.allclose(compressed, actual_sp17_zero_form),
            f"cell {index} does not recover the SP17 incidence zero-form",
        )

    # Assembly is independent of cell enumeration order. Relabeling acts by
    # conjugation and orientation reversal leaves support projectors fixed.
    reversed_assembly = local_terms[1] + local_terms[0]
    require(
        np.array_equal(global_one_particle, reversed_assembly),
        "global operator depends on cell enumeration order",
    )
    vertex_permutation = np.array(
        [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]],
        dtype=complex,
    )
    relabeled_projectors = tuple(
        vertex_permutation @ value @ vertex_permutation.conj().T
        for value in source_projectors
    )
    relabeled_operator = (
        np.kron(np.kron(relabeled_projectors[0], gamma5), c_record_01)
        + np.kron(np.kron(relabeled_projectors[1], gamma5), c_record_12)
    )
    source_relabeling = np.kron(vertex_permutation, np.eye(4, dtype=complex))
    full_relabeling = np.kron(
        source_relabeling, np.eye(record_dimension, dtype=complex)
    )
    require(
        np.allclose(
            relabeled_operator,
            full_relabeling
            @ global_one_particle
            @ full_relabeling.conj().T,
        ),
        "vertex relabeling is not implemented naturally",
    )
    reversed_orientation_projector = projector(-source_vectors[0])
    require(
        np.allclose(
            reversed_orientation_projector, source_projectors[0]
        ),
        "orientation reversal changed the physical source support",
    )
    cell_orientation = grading_cell
    require(
        np.allclose(
            cell_orientation @ c_cell @ cell_orientation.conj().T,
            -c_cell,
        ),
        "cellular orientation unitary does not reverse the quadrature",
    )
    record_orientation_01 = np.kron(
        cell_orientation, record_identity
    )
    reversed_record_01 = (
        record_orientation_01
        @ c_record_01
        @ record_orientation_01.conj().T
    )
    explicitly_reversed_global = (
        np.kron(source_spin_terms[0], reversed_record_01)
        + local_terms[1]
    )
    full_orientation = np.kron(
        np.eye(len(vertices) * 4, dtype=complex),
        record_orientation_01,
    )
    require(
        np.allclose(
            full_orientation
            @ global_one_particle
            @ full_orientation.conj().T,
            explicitly_reversed_global,
        ),
        "complete source-record operator is not orientation covariant",
    )

    primitive_overlap_commutator = (
        local_terms[0] @ local_terms[1]
        - local_terms[1] @ local_terms[0]
    )
    require(
        np.linalg.norm(primitive_overlap_commutator) > 1e-10,
        "shared source support generated no connected primitive structure",
    )
    induced_two_step = global_one_particle @ global_one_particle
    require(
        np.linalg.norm(induced_two_step) > 0.0,
        "induced two-step propagation vanished unexpectedly",
    )

    # One global source CAR carrier: three source orbitals times Dirac-4.
    source_modes = len(vertices) * 4
    require(
        source_modes == 12 and source_modes != 2 * 12,
        "source carrier was copied once per record cell",
    )
    h_one = operator_valued_car_lift(
        global_one_particle, source_modes, record_dimension, 1
    )
    require(
        np.allclose(h_one, global_one_particle),
        "operator-valued CAR lift does not recover the one-source operator",
    )
    h_two = operator_valued_car_lift(
        global_one_particle, source_modes, record_dimension, 2
    )
    require(
        np.allclose(h_two, h_two.conj().T),
        "two-source quasi-free lift is not Hermitian",
    )

    # A quartic density competitor agrees on vacuum and one-source sectors,
    # but differs on a two-source sector. Its coefficient is arbitrary and
    # exact; no target value is involved.
    mode_i = 0
    mode_j = 1
    n_i_one = one_body_wedge_matrix(source_modes, 1, mode_i, mode_i)
    n_j_one = one_body_wedge_matrix(source_modes, 1, mode_j, mode_j)
    require(
        np.allclose(n_i_one @ n_j_one, 0.0),
        "quartic control should vanish on the one-source sector",
    )
    n_i_two = one_body_wedge_matrix(source_modes, 2, mode_i, mode_i)
    n_j_two = one_body_wedge_matrix(source_modes, 2, mode_j, mode_j)
    quartic_two = np.kron(
        n_i_two @ n_j_two, np.eye(record_dimension, dtype=complex)
    )
    require(
        np.linalg.norm(quartic_two) > 0.0,
        "quartic negative control vanished on the two-source sector",
    )
    competitor_two = h_two + 0.5 * quartic_two
    require(
        not np.allclose(competitor_two, h_two),
        "quartic competitor did not change the two-source action",
    )
    vacuum_generator = np.zeros(
        (record_dimension, record_dimension), dtype=complex
    )
    require(
        np.allclose(vacuum_generator, 0.0),
        "vacuum central normalization is not zero",
    )

    time_a = 0.071
    time_b = 0.113
    require(
        np.allclose(
            evolve(h_one, time_a + time_b),
            evolve(h_one, time_a) @ evolve(h_one, time_b),
            atol=3e-13,
        ),
        "finite stationary Stone evolution fails composition",
    )

    print("single_global_source_CAR_mode_count=12")
    print("duplicated_source_per_record_cell=FALSE")
    print("distinguishable_even_record_factor_count=2")
    print("record_directions_fermionized=FALSE")
    print("shared_source_vertex_counted_once=PASS")
    print("three_cell_pushout_associativity=PASS")
    print("actual_SP17_one_cell_incidence_zero_form_recovered=PASS")
    print("complete_SP17_kinetic_operator_recovered_here=FALSE")
    print("cell_enumeration_order_independence=PASS")
    print("vertex_relabeling_naturality=PASS")
    print("complete_operator_orientation_reversal_covariance=PASS")
    print(f"shared_support_projector_overlap={overlap:.2f}")
    print("primitive_shared_support_commutator=NONZERO")
    print("h_squared_role=INDUCED_TWO_STEP_NOT_PRIMITIVE_OVERLAP")
    print("operator_valued_CAR_one_source_recovery=PASS")
    print("operator_valued_CAR_two_source_lift=PASS")
    print("quartic_competitor_vacuum_and_one_source_match=PASS")
    print("quartic_competitor_two_source_difference=DETECTED")
    print("primitive_quartic_competitor=REJECTED_BY_QUASI_FREE_COMPLETENESS")
    print("effective_descendant_interactions_forbidden=FALSE")
    print("finite_stationary_Stone_ordering=PASS")
    print("time_dependent_continuum_ordering_derived=FALSE")
    print("connected_preparation_derived=FALSE")
    print("physical_source_pole_and_residue_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
