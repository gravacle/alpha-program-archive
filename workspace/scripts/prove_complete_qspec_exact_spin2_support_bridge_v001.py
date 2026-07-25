#!/usr/bin/env python3
"""Exact symbolic proof gate for the zero-history spin-2 support bridge."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SYMPY_ROOT = ROOT / ".proof_deps/sympy"
sys.path.insert(0, str(SYMPY_ROOT))

import sympy as sp  # noqa: E402


SPEC = ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md"
SPEC_SEAL = Path(f"{SPEC}.seal.sha256")
SCRIPT_SEAL = Path(f"{Path(__file__).resolve()}.seal.sha256")
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_exact_spin2_support_bridge_v001.json"
)

EXPECTED_SPEC_SHA256 = (
    "b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0"
)
EXPECTED = {
    ROOT / "scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py":
        "1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md":
        "273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md":
        "5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3",
    ROOT / "COMPLETE_QSPEC_PERIODIC_REDUCED_TO_FULL_BRIDGE_CORRECTION_V001.md":
        "40e5fdac17bd61616b34fcd401a0019b8889e0df38aa0d0b06bd4aec2b1e9e59",
    ROOT / "COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md":
        "ad3286ee2961fc7569db7ed6572e1cb4bdc5ff5415226cd2b5b5e56625b2ab1e",
    Path(
        "/Users/bgm/MB Work/alpha_supervision/"
        "OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md"
    ):
        "83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2",
}
SEALED_AUTHORITIES = (
    ROOT / "COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_seal(target: Path, seal: Path) -> None:
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {seal}")
    require(fields[0] == sha256(target), f"seal hash mismatch: {target}")
    require(fields[1] == target.name, f"seal name mismatch: {target}")


def verify_authorities() -> dict[str, str]:
    require(sha256(SPEC) == EXPECTED_SPEC_SHA256, "spec hash mismatch")
    observed = {str(SPEC.relative_to(ROOT)): sha256(SPEC)}
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing authority: {path}")
        actual = sha256(path)
        require(actual == expected, f"authority mismatch: {path}")
        observed[str(path)] = actual
    for path in SEALED_AUTHORITIES:
        verify_seal(path, Path(f"{path}.seal.sha256"))
    verify_seal(SPEC, SPEC_SEAL)
    verify_seal(Path(__file__).resolve(), SCRIPT_SEAL)
    return observed


def exact_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def exact_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and exact_zero(left - right)


def dgamma(
    one_body: sp.MatrixBase,
    particles: int,
) -> tuple[sp.SparseMatrix, tuple[tuple[int, ...], ...]]:
    dimension = one_body.rows
    basis = tuple(itertools.combinations(range(dimension), particles))
    lookup = {occupation: row for row, occupation in enumerate(basis)}
    output = sp.MutableSparseMatrix(len(basis), len(basis), {})
    for column, occupation in enumerate(basis):
        for q_position, q_mode in enumerate(occupation):
            reduced = list(occupation)
            reduced.pop(q_position)
            q_sign = -1 if q_position % 2 else 1
            for p_mode in range(dimension):
                if p_mode in reduced:
                    continue
                p_position = sum(mode < p_mode for mode in reduced)
                p_sign = -1 if p_position % 2 else 1
                target = tuple(sorted((*reduced, p_mode)))
                output[lookup[target], column] += (
                    q_sign * p_sign * one_body[p_mode, q_mode]
                )
    return sp.SparseMatrix(output), basis


def matrix_strings(matrix: sp.MatrixBase) -> list[list[str]]:
    return [
        [str(sp.simplify(matrix[row, column]))
         for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def exterior_power_matrix(
    one_body_unitary: sp.MatrixBase,
    particles: int,
    basis: tuple[tuple[int, ...], ...],
) -> sp.SparseMatrix:
    output = sp.MutableSparseMatrix(len(basis), len(basis), {})
    for row, target in enumerate(basis):
        for column, source in enumerate(basis):
            value = sp.simplify(
                one_body_unitary.extract(target, source).det()
            )
            if value != 0:
                output[row, column] = value
    return sp.SparseMatrix(output)


def build_exact_parent():
    I = sp.I
    sqrt2 = sp.sqrt(2)
    sqrt3 = sp.sqrt(3)

    directed = sp.zeros(3)
    for site in range(3):
        directed[site, (site + 1) % 3] += sp.Rational(1, 2)
        directed[site, (site - 1) % 3] -= sp.Rational(1, 2)

    alpha_x = sp.Matrix(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ]
    )
    incidence = sp.Matrix(
        [
            [0, 0, -I, 0],
            [0, 0, 0, -I],
            [I, 0, 0, 0],
            [0, I, 0, 0],
        ]
    )
    record = sp.Matrix(
        [
            [0, 0, -I],
            [0, 0, I],
            [I, -I, 0],
        ]
    )
    one_body_full = -I * sp.kronecker_product(directed, alpha_x)
    active_projector = sp.simplify(
        sp.Rational(4, 3) * one_body_full**2
    )
    spectral_scale = sqrt3 / 2
    negative_projector = sp.simplify(
        (active_projector - one_body_full / spectral_scale) / 2
    )
    positive_projector = sp.simplify(
        (active_projector + one_body_full / spectral_scale) / 2
    )

    omega = (-1 + I * sqrt3) / 2
    omega_bar = (-1 - I * sqrt3) / 2
    f_plus = sp.Matrix([1, omega, omega**2]) / sqrt3
    f_minus = sp.Matrix([1, omega_bar, omega_bar**2]) / sqrt3

    e = sp.eye(4)
    u_minus_1 = (e[:, 0] - e[:, 3]) / sqrt2
    u_minus_2 = (e[:, 1] - e[:, 2]) / sqrt2
    u_plus_1 = (e[:, 0] + e[:, 3]) / sqrt2
    u_plus_2 = (e[:, 1] + e[:, 2]) / sqrt2

    active_basis = sp.Matrix.hstack(
        sp.kronecker_product(f_plus, u_minus_1),
        sp.kronecker_product(f_plus, u_minus_2),
        sp.kronecker_product(f_minus, u_plus_1),
        sp.kronecker_product(f_minus, u_plus_2),
        sp.kronecker_product(f_plus, u_plus_1),
        sp.kronecker_product(f_plus, u_plus_2),
        sp.kronecker_product(f_minus, u_minus_1),
        sp.kronecker_product(f_minus, u_minus_2),
    )

    active_orthonormal = exact_equal(
        sp.simplify(active_basis.conjugate().T * active_basis),
        sp.eye(8),
    )
    active_projector_pass = bool(
        exact_equal(active_projector**2, active_projector)
        and active_projector.rank() == 8
        and exact_equal(
            active_basis * active_basis.conjugate().T,
            active_projector,
        )
    )
    negative_basis = active_basis[:, :4]
    positive_basis = active_basis[:, 4:]
    spectral_projector_pass = bool(
        exact_equal(negative_projector**2, negative_projector)
        and exact_equal(positive_projector**2, positive_projector)
        and negative_projector.rank() == 4
        and positive_projector.rank() == 4
        and exact_equal(
            negative_basis * negative_basis.conjugate().T,
            negative_projector,
        )
        and exact_equal(
            positive_basis * positive_basis.conjugate().T,
            positive_projector,
        )
    )
    active_free = sp.simplify(
        active_basis.conjugate().T * one_body_full * active_basis
    )
    expected_active_free = sp.diag(
        *([-sqrt3 / 2] * 4 + [sqrt3 / 2] * 4)
    )

    masks = (
        sp.diag(1, 1, 0),
        sp.diag(0, 1, 1),
    )
    active_interactions = tuple(
        sp.simplify(
            active_basis.conjugate().T
            * sp.kronecker_product(mask, incidence)
            * active_basis
        )
        for mask in masks
    )

    h0, fock_basis = dgamma(active_free, 4)
    h1, _ = dgamma(active_interactions[0], 4)
    h2, _ = dgamma(active_interactions[1], 4)
    psi0 = sp.zeros(len(fock_basis), 1)
    psi0[fock_basis.index((0, 1, 2, 3)), 0] = 1

    hadamard_2 = sp.Matrix([[1, 1], [1, -1]]) / sqrt2
    u_minus = sp.diag(hadamard_2, sp.eye(2))
    u_plus = sp.diag(sp.eye(2), hadamard_2)
    frame_unitary = sp.diag(u_minus, u_plus)
    alternate_active_basis = sp.simplify(active_basis * frame_unitary)
    gamma_4 = exterior_power_matrix(frame_unitary, 4, fock_basis)
    alternate_h0_one = sp.simplify(
        frame_unitary.conjugate().T
        * active_free
        * frame_unitary
    )
    alternate_h1_one = sp.simplify(
        frame_unitary.conjugate().T
        * active_interactions[0]
        * frame_unitary
    )
    alternate_h2_one = sp.simplify(
        frame_unitary.conjugate().T
        * active_interactions[1]
        * frame_unitary
    )
    alternate_h0, _ = dgamma(alternate_h0_one, 4)
    alternate_h1, _ = dgamma(alternate_h1_one, 4)
    alternate_h2, _ = dgamma(alternate_h2_one, 4)
    exterior_covariance_pass = bool(
        exact_equal(
            alternate_active_basis,
            active_basis * frame_unitary,
        )
        and exact_equal(
            alternate_h0,
            gamma_4.conjugate().T * h0 * gamma_4,
        )
        and exact_equal(
            alternate_h1,
            gamma_4.conjugate().T * h1 * gamma_4,
        )
        and exact_equal(
            alternate_h2,
            gamma_4.conjugate().T * h2 * gamma_4,
        )
    )
    sea_frame_image = sp.simplify(gamma_4 * psi0)
    sea_phase = sp.simplify(u_minus.det())
    sea_phase_pass = exact_equal(sea_frame_image, sea_phase * psi0)

    return {
        "active_orthonormal": active_orthonormal,
        "active_projector_pass": active_projector_pass,
        "spectral_projector_pass": spectral_projector_pass,
        "active_free": active_free,
        "expected_active_free": expected_active_free,
        "active_interactions": active_interactions,
        "h0": h0,
        "h1": h1,
        "h2": h2,
        "record": record,
        "psi0": psi0,
        "fock_dimension": len(fock_basis),
        "exterior_covariance_pass": exterior_covariance_pass,
        "sea_phase": sea_phase,
        "sea_phase_pass": sea_phase_pass,
    }


def prove_spin2(parent):
    sqrt3 = sp.sqrt(3)
    sqrt6 = sp.sqrt(6)
    h0 = parent["h0"]
    h1 = parent["h1"]
    h2 = parent["h2"]
    current = parent["psi0"]
    previous = sp.zeros(current.rows, 1)
    beta_previous = sp.Integer(0)
    lanczos_basis = []
    lanczos_alpha = []
    lanczos_beta = []
    terminal_residual = None
    for index in range(5):
        lanczos_basis.append(current)
        work = sp.simplify(h1 * current - beta_previous * previous)
        alpha = sp.simplify((current.conjugate().T * work)[0, 0])
        lanczos_alpha.append(alpha)
        work = sp.simplify(work - alpha * current)
        for basis_vector in lanczos_basis:
            overlap = sp.simplify(
                (basis_vector.conjugate().T * work)[0, 0]
            )
            work = sp.simplify(work - overlap * basis_vector)
        beta_squared = sp.simplify(
            (work.conjugate().T * work)[0, 0]
        )
        beta = sp.simplify(sp.sqrt(beta_squared))
        if index < 4:
            require(beta != 0, f"Lanczos breakdown at index {index}")
            lanczos_beta.append(beta)
            previous, current = current, sp.simplify(work / beta)
            beta_previous = beta
        else:
            terminal_residual = work
    q = sp.Matrix.hstack(*lanczos_basis)

    outer = sp.Rational(4, 3)
    inner = 2 * sqrt6 / 3
    expected_h0 = sqrt3 * sp.diag(-2, -1, 0, 1, 2)
    expected_hx = sp.zeros(5)
    for index, value in enumerate((outer, inner, inner, outer)):
        expected_hx[index, index + 1] = value
        expected_hx[index + 1, index] = value

    cyclic = sp.Matrix.hstack(
        parent["psi0"],
        h1 * parent["psi0"],
        h1**2 * parent["psi0"],
        h1**3 * parent["psi0"],
        h1**4 * parent["psi0"],
    )
    gram = sp.simplify(cyclic.conjugate().T * cyclic)
    gram_determinant = sp.factor(gram.det())

    restricted_h0 = sp.simplify(q.conjugate().T * h0 * q)
    restricted_h1 = sp.simplify(q.conjugate().T * h1 * q)
    restricted_h2 = sp.simplify(q.conjugate().T * h2 * q)
    residual_h0 = sp.simplify(h0 * q - q * expected_h0)
    residual_h1 = sp.simplify(h1 * q - q * expected_hx)
    residual_h2 = sp.simplify(h2 * q - q * expected_hx)

    return {
        "basis": q,
        "gram_determinant": gram_determinant,
        "orthonormal": exact_equal(q.conjugate().T * q, sp.eye(5)),
        "lanczos_alpha": lanczos_alpha,
        "lanczos_beta": lanczos_beta,
        "lanczos_terminal_residual_zero":
            exact_zero(terminal_residual),
        "restricted_h0": restricted_h0,
        "restricted_h1": restricted_h1,
        "restricted_h2": restricted_h2,
        "expected_h0": expected_h0,
        "expected_hx": expected_hx,
        "h0_residual_zero": exact_zero(residual_h0),
        "h1_residual_zero": exact_zero(residual_h1),
        "h2_residual_zero": exact_zero(residual_h2),
        "h0_residual": residual_h0,
        "h1_residual": residual_h1,
        "h2_residual": residual_h2,
    }


def derive_cell_and_induction_certificate(parent, spin2):
    q = spin2["basis"]
    source_identity = sp.eye(parent["h0"].rows)
    source_projector = sp.simplify(q * q.conjugate().T)
    source_complement = source_identity - source_projector
    source_projector_orthogonal = bool(
        exact_equal(source_projector**2, source_projector)
        and exact_equal(
            source_projector.conjugate().T,
            source_projector,
        )
    )
    source_generators_Hermitian = bool(
        exact_equal(parent["h0"], parent["h0"].conjugate().T)
        and exact_equal(parent["h1"], parent["h1"].conjugate().T)
        and exact_equal(parent["h2"], parent["h2"].conjugate().T)
    )
    record_generator_Hermitian = exact_equal(
        parent["record"],
        parent["record"].conjugate().T,
    )
    identity_record = sp.eye(parent["record"].rows)
    joint_free = sp.kronecker_product(
        spin2["restricted_h0"],
        identity_record,
    )
    joint_interaction_1 = sp.kronecker_product(
        spin2["restricted_h1"],
        parent["record"],
    )
    joint_interaction_2 = sp.kronecker_product(
        spin2["restricted_h2"],
        parent["record"],
    )
    joint_generators_Hermitian = bool(
        exact_equal(joint_free, joint_free.conjugate().T)
        and exact_equal(
            joint_interaction_1,
            joint_interaction_1.conjugate().T,
        )
        and exact_equal(
            joint_interaction_2,
            joint_interaction_2.conjugate().T,
        )
    )
    full_joint_generators_Hermitian_derived = bool(
        source_generators_Hermitian
        and record_generator_Hermitian
    )
    record_basis = sp.eye(parent["record"].rows)
    ready_state = record_basis[:, 0]
    ready_state_norm = sp.simplify(
        (ready_state.conjugate().T * ready_state)[0, 0]
    )
    ready_state_normalized = ready_state_norm == 1
    ready_embedding = sp.kronecker_product(
        sp.eye(q.cols),
        ready_state,
    )
    ready_embedding_isometry = exact_equal(
        ready_embedding.conjugate().T * ready_embedding,
        sp.eye(q.cols),
    )
    record_completeness = sp.zeros(parent["record"].rows)
    for column in range(record_basis.cols):
        vector = record_basis[:, column]
        record_completeness += vector * vector.conjugate().T
    record_completeness_pass = exact_equal(
        record_completeness,
        sp.eye(parent["record"].rows),
    )

    incoming_support_pass = exact_equal(
        parent["psi0"].conjugate().T,
        parent["psi0"].conjugate().T * source_projector,
    )
    source_generator_reduction_pass = bool(
        all(
            exact_zero(source_complement * generator * source_projector)
            and exact_zero(source_projector * generator * source_complement)
            for generator in (parent["h0"], parent["h1"], parent["h2"])
        )
    )
    joint_reducing_projector_derived = bool(
        source_projector_orthogonal
        and source_generator_reduction_pass
    )

    return {
        "source_projector_orthogonal_pass":
            source_projector_orthogonal,
        "source_generators_Hermitian":
            source_generators_Hermitian,
        "record_generator_Hermitian":
            record_generator_Hermitian,
        "joint_generators_Hermitian": joint_generators_Hermitian,
        "full_joint_generators_Hermitian_derived":
            full_joint_generators_Hermitian_derived,
        "record_completeness_pass": record_completeness_pass,
        "ready_state": matrix_strings(ready_state),
        "ready_state_norm": str(ready_state_norm),
        "ready_state_normalized": ready_state_normalized,
        "ready_embedding_isometry_pass":
            ready_embedding_isometry,
        "source_generator_reduction_pass":
            source_generator_reduction_pass,
        "joint_reducing_projector_derived":
            joint_reducing_projector_derived,
        "incoming_right_support_pass": incoming_support_pass,
        "factor_unitarity_derived":
            full_joint_generators_Hermitian_derived,
        "time_ordered_product_unitarity_derived":
            full_joint_generators_Hermitian_derived,
        "Kraus_Gram_identity_derived":
            bool(
                full_joint_generators_Hermitian_derived
                and record_completeness_pass
                and ready_state_normalized
                and ready_embedding_isometry
            ),
        "one_step_right_support_identity_derived":
            bool(
                joint_reducing_projector_derived
                and incoming_support_pass
            ),
        "finite_N_induction_derived":
            bool(
                joint_reducing_projector_derived
                and incoming_support_pass
                and full_joint_generators_Hermitian_derived
                and record_completeness_pass
                and ready_state_normalized
                and ready_embedding_isometry
            ),
        "proof_chain": [
            "Hermitian exact joint generators imply unitary factors.",
            "Products of unitary factors give the exact cell unitary.",
            "Record-basis completeness gives sum_q K_q^dagger K_q=I.",
            "Two-sided generator reduction implies exact cell reduction.",
            "(I-P)K_q^-P=0 follows from exact cell reduction.",
            "For X=XP, X K_q^(-dagger)=[X K_q^(-dagger)]P.",
            "Left multiplication by arbitrary admissible K_q^+ preserves "
            "the right-support identity.",
            "Induction from rho_in=rho_in P proves the finite-N identity.",
        ],
    }


def main() -> None:
    require(sys.flags.isolated == 1, "execute with python3 -I")
    require(sys.flags.no_user_site == 1, "user site must be disabled")
    authorities = verify_authorities()
    lemma_path = (
        ROOT
        / "COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md"
    )
    general_lemmas_verified = bool(
        authorities[str(lemma_path)] == EXPECTED[lemma_path]
    )
    parent = build_exact_parent()
    spin2 = prove_spin2(parent)
    cell_induction = derive_cell_and_induction_certificate(parent, spin2)

    active_free_pass = exact_equal(
        parent["active_free"],
        parent["expected_active_free"],
    )
    Hermitian_generators_pass = bool(
        exact_equal(parent["h0"], parent["h0"].conjugate().T)
        and exact_equal(parent["h1"], parent["h1"].conjugate().T)
        and exact_equal(parent["h2"], parent["h2"].conjugate().T)
    )
    record_Hermitian_pass = exact_equal(
        parent["record"],
        parent["record"].conjugate().T,
    )
    exact_rank_pass = spin2["gram_determinant"] != 0
    computed_lanczos_pass = bool(
        all(value == 0 for value in spin2["lanczos_alpha"])
        and spin2["lanczos_beta"]
        == [
            sp.Rational(4, 3),
            2 * sp.sqrt(6) / 3,
            2 * sp.sqrt(6) / 3,
            sp.Rational(4, 3),
        ]
        and spin2["lanczos_terminal_residual_zero"]
    )
    generator_invariance_pass = bool(
        spin2["h0_residual_zero"]
        and spin2["h1_residual_zero"]
        and spin2["h2_residual_zero"]
    )
    spin2_identification_pass = bool(
        spin2["orthonormal"]
        and computed_lanczos_pass
        and exact_equal(spin2["restricted_h0"], spin2["expected_h0"])
        and exact_equal(spin2["restricted_h1"], spin2["expected_hx"])
        and exact_equal(spin2["restricted_h2"], spin2["expected_hx"])
    )
    exact_cell_invariance_pass = bool(
        generator_invariance_pass
        and Hermitian_generators_pass
        and record_Hermitian_pass
        and cell_induction["joint_generators_Hermitian"]
        and cell_induction["full_joint_generators_Hermitian_derived"]
        and cell_induction["source_projector_orthogonal_pass"]
        and cell_induction["source_generator_reduction_pass"]
        and cell_induction["joint_reducing_projector_derived"]
    )
    exact_stinespring_gram_identity_derived = bool(
        exact_cell_invariance_pass
        and cell_induction["Kraus_Gram_identity_derived"]
    )
    finite_amplitude_identity_pass = bool(
        exact_cell_invariance_pass
        and exact_stinespring_gram_identity_derived
        and cell_induction["one_step_right_support_identity_derived"]
        and cell_induction["finite_N_induction_derived"]
    )
    passed = bool(
        general_lemmas_verified
        and
        parent["active_orthonormal"]
        and parent["active_projector_pass"]
        and parent["spectral_projector_pass"]
        and parent["exterior_covariance_pass"]
        and parent["sea_phase_pass"]
        and active_free_pass
        and Hermitian_generators_pass
        and record_Hermitian_pass
        and exact_rank_pass
        and generator_invariance_pass
        and spin2_identification_pass
        and exact_cell_invariance_pass
        and finite_amplitude_identity_pass
    )

    result = {
        "schema": "complete_qspec_exact_spin2_support_bridge_v001",
        "authorities": authorities,
        "script_sha256": sha256(Path(__file__).resolve()),
        "python_isolated_mode": bool(sys.flags.isolated),
        "sympy_version": sp.__version__,
        "exact_field": "Q(i,sqrt(3),sqrt(2),sqrt(6))",
        "active_one_body_dimension": parent["active_free"].rows,
        "four_fermion_dimension": parent["fock_dimension"],
        "active_basis_orthonormal": parent["active_orthonormal"],
        "basis_independent_active_projector_pass":
            parent["active_projector_pass"],
        "negative_positive_spectral_projectors_pass":
            parent["spectral_projector_pass"],
        "active_free_exact_pass": active_free_pass,
        "four_fermion_generators_Hermitian":
            Hermitian_generators_pass,
        "record_generator_Hermitian": record_Hermitian_pass,
        "basis_independent_parent_projectors_established":
            bool(
                parent["active_projector_pass"]
                and parent["spectral_projector_pass"]
            ),
        "generic_same_projector_frame_intertwiner_derived":
            general_lemmas_verified,
        "universal_exterior_power_frame_covariance_lemma_verified":
            general_lemmas_verified,
        "exact_stinespring_completeness_lemma_verified":
            general_lemmas_verified,
        "exterior_power_frame_covariance_witness_pass":
            parent["exterior_covariance_pass"],
        "filled_negative_sea_frame_phase": str(parent["sea_phase"]),
        "filled_negative_sea_frame_phase_pass":
            parent["sea_phase_pass"],
        "cyclic_gram_determinant": str(spin2["gram_determinant"]),
        "cyclic_support_exact_rank": 5 if exact_rank_pass else None,
        "spin2_basis_orthonormal": spin2["orthonormal"],
        "computed_Lanczos_alpha": [
            str(value) for value in spin2["lanczos_alpha"]
        ],
        "computed_Lanczos_beta": [
            str(value) for value in spin2["lanczos_beta"]
        ],
        "computed_Lanczos_coefficients_pass":
            computed_lanczos_pass,
        "Lanczos_terminal_residual_exact_zero":
            spin2["lanczos_terminal_residual_zero"],
        "restricted_H0": matrix_strings(spin2["restricted_h0"]),
        "restricted_H1": matrix_strings(spin2["restricted_h1"]),
        "restricted_H2": matrix_strings(spin2["restricted_h2"]),
        "expected_H0": matrix_strings(spin2["expected_h0"]),
        "expected_H1_H2": matrix_strings(spin2["expected_hx"]),
        "H0_invariance_residual_exact_zero":
            spin2["h0_residual_zero"],
        "H1_invariance_residual_exact_zero":
            spin2["h1_residual_zero"],
        "H2_invariance_residual_exact_zero":
            spin2["h2_residual_zero"],
        "H0_invariance_residual_matrix":
            matrix_strings(spin2["h0_residual"]),
        "H1_invariance_residual_matrix":
            matrix_strings(spin2["h1_residual"]),
        "H2_invariance_residual_matrix":
            matrix_strings(spin2["h2_residual"]),
        "exact_generator_invariance_pass": generator_invariance_pass,
        "cell_and_induction_certificate": cell_induction,
        "exact_cell_and_Kraus_invariance_pass":
            exact_cell_invariance_pass,
        "exact_stinespring_Gram_identity_derived":
            exact_stinespring_gram_identity_derived,
        "right_history_support_induction_derived":
            finite_amplitude_identity_pass,
        "exact_reduced_to_full_finite_amplitude_identity_pass":
            finite_amplitude_identity_pass,
        "verdict": (
            "EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_DERIVED"
            if passed
            else "EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_BLOCKED"
        ),
        "pass": passed,
        "exact_zero_history_spin2_support_derived": passed,
        "exact_reduced_to_full_finite_amplitude_identity_derived":
            passed,
        "canonical_spin2_transfer_ball_certified": False,
        "full_completed_record_amplitude_zero_free_for_all_volumes":
            False,
        "physical_continuum_local_source_addressability_derived":
            False,
        "periodic_connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_coupling_or_alpha_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "gram_determinant": result["cyclic_gram_determinant"],
                "generator_invariance":
                    result["exact_generator_invariance_pass"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
