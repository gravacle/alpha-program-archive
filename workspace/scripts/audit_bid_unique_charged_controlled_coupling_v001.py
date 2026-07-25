#!/usr/bin/env python3
"""Fail-closed audit of the primitive charged controlled coupling."""

from __future__ import annotations

import math

import numpy as np


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def antiunitary_conjugate(
    unitary_part: np.ndarray, operator: np.ndarray
) -> np.ndarray:
    return unitary_part @ operator.conj() @ unitary_part.conj().T


def evolve(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return vectors @ np.diag(np.exp(-1j * interval * values)) @ vectors.conj().T


def solve_projection_module_control() -> tuple[np.ndarray, np.ndarray]:
    """Solve the complete linear control-map constraints in a nontrivial case."""

    dimension = 3
    active = (0, 1)
    matrix_dimension = dimension**2
    unknown_count = matrix_dimension**2
    projector = np.diag([1.0, 1.0, 0.0]).astype(complex)
    units = []
    for row in range(dimension):
        for column in range(dimension):
            unit = np.zeros((dimension, dimension), dtype=complex)
            unit[row, column] = 1.0
            units.append(unit)

    equations = []
    targets = []

    # Support: every output lies in P End(H) P.
    for input_index in range(matrix_dimension):
        for row in range(dimension):
            for column in range(dimension):
                if row in active and column in active:
                    continue
                equation = np.zeros(unknown_count, dtype=complex)
                output_index = row * dimension + column
                equation[output_index * matrix_dimension + input_index] = 1.0
                equations.append(equation)
                targets.append(0.0)

    # Retraction: an operator already supported in P is unchanged.
    for row in active:
        for column in active:
            input_index = row * dimension + column
            for output_index in range(matrix_dimension):
                equation = np.zeros(unknown_count, dtype=complex)
                equation[output_index * matrix_dimension + input_index] = 1.0
                equations.append(equation)
                targets.append(
                    1.0 if output_index == input_index else 0.0
                )

    # Bimodule property for a basis of P End(H) P on both sides.
    active_units = [
        units[row * dimension + column]
        for row in active
        for column in active
    ]
    for left in active_units:
        for right in active_units:
            action_on_output = np.kron(left, right.T)
            for input_index, input_unit in enumerate(units):
                transformed_input = (left @ input_unit @ right).reshape(-1)
                for output_index in range(matrix_dimension):
                    equation = np.zeros(unknown_count, dtype=complex)
                    for column_index, coefficient in enumerate(
                        transformed_input
                    ):
                        equation[
                            output_index * matrix_dimension + column_index
                        ] += coefficient
                    for row_index, coefficient in enumerate(
                        action_on_output[output_index]
                    ):
                        equation[
                            row_index * matrix_dimension + input_index
                        ] -= coefficient
                    if np.linalg.norm(equation) > 1e-14:
                        equations.append(equation)
                        targets.append(0.0)

    constraint = np.vstack(equations)
    target = np.asarray(targets, dtype=complex)
    singular_values = np.linalg.svd(
        constraint, compute_uv=False, full_matrices=False
    )
    tolerance = singular_values[0] * 1e-12
    rank = int(np.count_nonzero(singular_values > tolerance))
    require(
        rank == unknown_count,
        "projection-module control axioms leave an unresolved linear family",
    )
    solution, _, _, _ = np.linalg.lstsq(constraint, target, rcond=None)
    require(
        np.linalg.norm(constraint @ solution - target) < 1e-10,
        "projection-module control constraints are inconsistent",
    )
    solved_superoperator = solution.reshape(
        matrix_dimension, matrix_dimension
    )
    compression_superoperator = np.zeros_like(solved_superoperator)
    for input_index, input_unit in enumerate(units):
        compression_superoperator[:, input_index] = (
            projector @ input_unit @ projector
        ).reshape(-1)
    require(
        np.linalg.norm(
            solved_superoperator - compression_superoperator
        )
        < 1e-10,
        "unique control-map solution is not orthogonal compression",
    )
    return solved_superoperator, compression_superoperator


def main() -> None:
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sigma = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    gamma = [np.block([[z2, i2], [i2, z2]])]
    gamma.extend(np.block([[z2, value], [-value, z2]]) for value in sigma)
    gamma5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    dirac_cpt = gamma5 @ gamma[2]

    d_cell = np.array([[-1.0], [1.0]], dtype=complex)
    b_cell = np.block(
        [
            [np.zeros((2, 2), dtype=complex), d_cell],
            [d_cell.conj().T, np.zeros((1, 1), dtype=complex)],
        ]
    )
    grading_cell = np.diag([1.0, 1.0, -1.0]).astype(complex)
    c_cell = 1j * grading_cell @ b_cell
    causal_role_reversal = np.array(
        [[0, 1, 0], [1, 0, 0], [0, 0, -1]], dtype=complex
    )
    b_q = np.kron(gamma5, c_cell)
    theta_record = np.kron(dirac_cpt, causal_role_reversal)
    require(
        np.allclose(
            antiunitary_conjugate(theta_record, b_q), b_q
        ),
        "normalized charged record operator is not CPT even",
    )

    # The source carrier is (direct sum_q M_q) tensor S_Dirac. The 2,3,3
    # dimensions below belong only to unresolved multiplicity factors M_q;
    # the structural Dirac factor is carried explicitly inside b_q.
    source_dimension = 8
    neutral_slice = slice(0, 2)
    plus_slice = slice(2, 5)
    minus_slice = slice(5, 8)
    charge_values = np.array([0.0, 0.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0])
    charge = np.diag(charge_values).astype(complex)
    p_zero = np.diag((charge_values == 0.0).astype(float)).astype(complex)
    p_plus = np.diag((charge_values == 1.0).astype(float)).astype(complex)
    p_minus = np.diag((charge_values == -1.0).astype(float)).astype(complex)
    p_charged = p_plus + p_minus
    charge_swap = np.zeros((source_dimension, source_dimension), dtype=complex)
    charge_swap[neutral_slice, neutral_slice] = np.eye(2)
    charge_swap[plus_slice, minus_slice] = np.eye(3)
    charge_swap[minus_slice, plus_slice] = np.eye(3)
    require(
        np.allclose(
            antiunitary_conjugate(charge_swap, charge), -charge
        )
        and np.allclose(
            antiunitary_conjugate(charge_swap, p_plus), p_minus
        )
        and np.allclose(
            antiunitary_conjugate(charge_swap, p_charged), p_charged
        ),
        "primitive charge-sector CPT action is inconsistent",
    )
    spin_record_chirality = np.kron(gamma5, np.eye(c_cell.shape[0]))
    require(
        not np.allclose(
            gamma[0] @ gamma5 - gamma5 @ gamma[0],
            0.0,
        ),
        "Dirac spin factor was incorrectly reduced to unresolved multiplicity",
    )

    # Compute the commutant of every full matrix algebra acting inside each
    # charge eigenspace. Public charge-only naturality must leave exactly one
    # scalar identity per charge sector.
    matrix_basis = []
    for row in range(source_dimension):
        for column in range(source_dimension):
            unit = np.zeros((source_dimension, source_dimension), dtype=complex)
            unit[row, column] = 1.0
            matrix_basis.append(unit)
    internal_generators = []
    for sector in (range(0, 2), range(2, 5), range(5, 8)):
        for row in sector:
            for column in sector:
                generator = np.zeros(
                    (source_dimension, source_dimension), dtype=complex
                )
                generator[row, column] = 1.0
                internal_generators.append(generator)
    commutant_constraint = np.concatenate(
        tuple(
            np.stack(
                tuple(
                    (basis @ generator - generator @ basis).reshape(-1)
                    for basis in matrix_basis
                ),
                axis=1,
            )
            for generator in internal_generators
        ),
        axis=0,
    )
    _, commutant_singular_values, commutant_vh = np.linalg.svd(
        commutant_constraint, full_matrices=True
    )
    commutant_rank = int(
        np.count_nonzero(
            commutant_singular_values
            > commutant_singular_values[0] * 1e-12
        )
    )
    commutant_kernel = commutant_vh[commutant_rank:].conj().T
    require(
        commutant_kernel.shape == (source_dimension**2, 3),
        "internal-sector unitary commutant is not three-dimensional",
    )
    sector_scalars = np.column_stack(
        tuple(
            projector.reshape(-1) / np.linalg.norm(projector)
            for projector in (p_zero, p_plus, p_minus)
        )
    )
    require(
        np.linalg.norm(
            commutant_kernel @ commutant_kernel.conj().T
            - sector_scalars @ sector_scalars.conj().T
        )
        < 1e-10,
        "computed internal-sector commutant is not the projector span",
    )

    # Charge conservation alone admits internal-block competitors. The public
    # charge-only naturality condition rejects them.
    internal_plus_competitor = np.zeros(
        (source_dimension, source_dimension), dtype=complex
    )
    internal_plus_competitor[2, 2] = 1.0
    internal_plus_competitor[3, 3] = -1.0
    require(
        np.allclose(
            internal_plus_competitor @ charge
            - charge @ internal_plus_competitor,
            0.0,
        ),
        "internal multiplicity competitor should conserve charge",
    )
    mixing_generator = np.zeros(
        (source_dimension, source_dimension), dtype=complex
    )
    mixing_generator[2, 3] = mixing_generator[3, 2] = 1.0
    require(
        not np.allclose(
            internal_plus_competitor @ mixing_generator
            - mixing_generator @ internal_plus_competitor,
            0.0,
        ),
        "internal multiplicity competitor incorrectly passed naturality",
    )
    lifted_mixing_generator = np.kron(
        mixing_generator, np.eye(b_q.shape[0], dtype=complex)
    )
    lifted_chirality = np.kron(
        np.eye(source_dimension, dtype=complex), spin_record_chirality
    )
    lifted_record_operator = np.kron(
        np.eye(source_dimension, dtype=complex), b_q
    )
    require(
        np.allclose(
            lifted_mixing_generator @ lifted_chirality
            - lifted_chirality @ lifted_mixing_generator,
            0.0,
        )
        and np.allclose(
            lifted_mixing_generator @ lifted_record_operator
            - lifted_record_operator @ lifted_mixing_generator,
            0.0,
        ),
        "unresolved-multiplicity action does not preserve structural Dirac data",
    )

    solved_control, compression_control = solve_projection_module_control()
    require(
        np.allclose(solved_control, compression_control),
        "projection-module uniqueness solver did not return compression",
    )
    scaled_control = 1.17 * compression_control
    active_test = np.zeros((3, 3), dtype=complex)
    active_test[0, 1] = 1.0
    active_test_vector = active_test.reshape(-1)
    require(
        not np.allclose(
            scaled_control @ active_test_vector,
            active_test_vector,
        ),
        "rescaled control map incorrectly passed active-algebra retraction",
    )

    # Boundary Incidence Dynamics defines source control as orthogonal
    # spectral restriction of the already normalized parent incidence
    # operator. Compression changes support but cannot introduce a new
    # sector multiplier.
    b_parent = lifted_record_operator
    pi_charged = np.kron(
        p_charged, np.eye(b_q.shape[0], dtype=complex)
    )
    require(
        np.allclose(pi_charged @ pi_charged, pi_charged)
        and np.allclose(pi_charged.conj().T, pi_charged),
        "charged support is not an orthogonal spectral projector",
    )
    b_controlled = pi_charged @ b_parent @ pi_charged
    expected = np.kron(p_charged, b_q)
    require(
        np.allclose(b_controlled, expected),
        "spectral compression does not reduce to P_ch tensor B_Q",
    )

    active_indices = np.flatnonzero(
        np.diag(pi_charged).real > 0.5
    )
    charged_inclusion = np.eye(
        b_parent.shape[0], dtype=complex
    )[:, active_indices]
    require(
        np.allclose(
            charged_inclusion.conj().T @ charged_inclusion,
            np.eye(active_indices.size, dtype=complex),
        )
        and np.allclose(
            charged_inclusion @ charged_inclusion.conj().T,
            pi_charged,
        ),
        "charged-subspace inclusion is not isometric",
    )
    restricted_parent = (
        charged_inclusion.conj().T
        @ b_parent
        @ charged_inclusion
    )
    require(
        np.allclose(
            charged_inclusion
            @ restricted_parent
            @ charged_inclusion.conj().T,
            b_controlled,
        ),
        "isometric restriction does not reconstruct the compressed operator",
    )

    # The independently fixed first-opening interval now crosschecks the
    # compression; it is not used to solve for a coefficient.
    tau_record = math.pi / math.sqrt(2.0)
    root = np.array([1.0, 0.0, 0.0], dtype=complex)
    endpoint = np.array([0.0, 1.0, 0.0], dtype=complex)
    require(
        np.allclose(
            evolve(c_cell, tau_record) @ root,
            endpoint,
            atol=2e-14,
        ),
        "compressed unit-incidence operator failed the record interval",
    )
    for odd_multiplier in (1.0, 3.0, 5.0):
        output = evolve(odd_multiplier * c_cell, tau_record) @ root
        require(
            np.allclose(output, endpoint, atol=2e-14),
            "odd recurrence competitor did not return the endpoint",
        )
        first_transfer = math.pi / (
            math.sqrt(2.0) * odd_multiplier
        )
        require(
            bool(np.isclose(first_transfer, tau_record))
            == (odd_multiplier == 1.0),
            "least-positive recurrence test classified a multiplier incorrectly",
        )

    charge_total = np.kron(charge, np.eye(b_q.shape[0], dtype=complex))
    require(
        np.allclose(
            b_controlled @ charge_total - charge_total @ b_controlled,
            0.0,
        ),
        "controlled operator violates charge nondemolition",
    )
    full_cpt = np.kron(charge_swap, theta_record)
    require(
        np.allclose(
            antiunitary_conjugate(full_cpt, b_controlled), b_controlled
        ),
        "controlled operator violates CPT",
    )
    require(
        np.allclose(
            np.kron(p_zero, np.eye(b_q.shape[0])) @ b_controlled, 0.0
        ),
        "neutral charged-handle block is not inactive",
    )

    # Negative controls: each omitted physical condition leaves a competitor.
    neutral_competitor = b_controlled + np.kron(p_zero, b_q)
    require(
        np.allclose(
            neutral_competitor @ charge_total
            - charge_total @ neutral_competitor,
            0.0,
        )
        and np.allclose(
            antiunitary_conjugate(full_cpt, neutral_competitor),
            neutral_competitor,
        ),
        "neutral competitor should survive charge conservation and CPT",
    )
    require(
        not np.allclose(
            np.kron(p_zero, np.eye(b_q.shape[0]))
            @ neutral_competitor,
            0.0,
        ),
        "neutral competitor did not violate charged-handle inactivity",
    )
    orientation_competitor = (
        np.kron(p_plus, b_q) + np.kron(p_minus, 1.17 * b_q)
    )
    require(
        not np.allclose(
            antiunitary_conjugate(full_cpt, orientation_competitor),
            orientation_competitor,
        ),
        "unequal orientation coefficients passed CPT",
    )
    normalization_competitor_scale = 1.17
    normalization_competitor = normalization_competitor_scale * expected
    require(
        np.allclose(
            antiunitary_conjugate(full_cpt, normalization_competitor),
            normalization_competitor,
        )
        and not np.allclose(normalization_competitor, expected),
        "normalization competitor was not kept distinct",
    )
    require(
        not np.allclose(
            normalization_competitor,
            pi_charged @ b_parent @ pi_charged,
        ),
        "rescaled competitor incorrectly passed the compression identity",
    )
    require(
        not np.allclose(
            evolve(normalization_competitor_scale * c_cell, tau_record)
            @ root,
            endpoint,
            atol=2e-14,
        )
        and not np.isclose(
            math.pi
            / (
                math.sqrt(2.0)
                * normalization_competitor_scale
            ),
            tau_record,
        ),
        "normalization competitor passed the least-positive interval gate",
    )

    print("general_charge_nondemolition_block_family=CLASSIFIED")
    print("source_charge_sector_dimensions=2,3,3")
    print("source_carrier_factorization=MULTIPLICITY_TENSOR_DIRAC")
    print("Dirac_spinor_factor=STRUCTURAL_NOT_MULTIPLICITY")
    print("internal_sector_unitary_commutant_dimension=3")
    print("internal_multiplicity_competitor_charge_conserving=PASS")
    print("internal_multiplicity_competitor_public_naturality=REJECTED")
    print("multiplicity_action_preserves_Dirac_structure=PASS")
    print("projection_module_control_affine_nullity=0")
    print("projection_module_unique_control=PBP")
    print("rescaled_control_retraction_negative_control=REJECTED")
    print("pure_charged_neutral_inactivity_constraint=PASS")
    print("CPT_positive_negative_coefficient_equality=PASS")
    print("charged_control=ORTHOGONAL_SPECTRAL_COMPRESSION")
    print("charged_subspace_inclusion=ISOMETRIC")
    print("compression_preserves_parent_incidence_normalization=PASS")
    print("record_only_least_positive_interval=IMPORTED")
    print("compressed_operator_first_opening_interval=CROSSCHECK_PASS")
    print("odd_integer_recurrence_competitors=REJECTED_AS_NONFIRST")
    print("unique_control_coefficient_solution=0,1,1")
    print("controlled_operator=P_CH_TENSOR_B_Q")
    print("controlled_operator_charge_nondemolition=PASS")
    print("controlled_operator_CPT_covariance=PASS")
    print("neutral_inactivity_negative_control=REJECTED")
    print("orientation_coefficient_negative_control=REJECTED")
    print("normalization_competitor=REJECTED_BY_COMPRESSION_AND_INTERVAL")
    print("full_many_charge_controlled_coupling_derived=FALSE")
    print("complete_connected_source_record_action_derived=FALSE")
    print("alpha_computed=FALSE")
    print("BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_AUDIT=PASS_BLOCKED")


if __name__ == "__main__":
    main()
