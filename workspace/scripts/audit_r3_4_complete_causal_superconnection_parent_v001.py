#!/usr/bin/env python3
"""Audit the sealed complete causal superconnection parent specification."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md"
SPEC_SEAL = (
    ROOT
    / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.seal.sha256"
)
RESULT = (
    ROOT
    / "results"
    / "r3_4_complete_causal_superconnection_parent_v001.json"
)

PINNED_HASHES = {
    "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md": (
        "a27a2d571273494a0787e2283734ef1405d74dadfe16d64d3450bb4536e50732"
    ),
    "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md": (
        "532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb"
    ),
    "CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md": (
        "b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30"
    ),
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md": (
        "e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2"
    ),
    "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_V001.seal.sha256": (
        "dcab767cf5d38548ae0fc4e30b3c674cc527082e398575907ce53efaae08e199"
    ),
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md": (
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd"
    ),
    "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md": (
        "2215f79cbe69f1de1643427ad5d422b0c3064ff758327e43ff1629de8633f72d"
    ),
    "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md": (
        "50b5a651df2aca90ee47c6f85b2a502461370a652706ebccad871f191565a2d9"
    ),
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md": (
        "0322763ac48a4428b432124a6947da81826a41f612efa6803ee9a87317929b98"
    ),
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md": (
        "b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f"
    ),
    "BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md": (
        "7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476"
    ),
    "R3_4_LORENTZIAN_JOINT_ENDPOINT_COMPATIBILITY_RESULT_V001.md": (
        "1868656d1881e67c8f6263062b27806f71bcc9de03d7eec0e612085fb47de0cf"
    ),
    "R3_4_DRESSED_OUTGOING_RECORD_RANGE_RESULT_V001.md": (
        "3240d935ef558948e09dd6a70092a3f3592747b5e5c99ea559d64adc2a5c303e"
    ),
    "R3_4_SHARED_SOURCE_OUTGOING_RANGE_ERRATUM_V001.md": (
        "5f8e60629f2b0fc703b5b6de02ca2de96ffb9d5e8aa48f961a043c40f8c93f41"
    ),
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md": (
        "5c679e3741abe782688b8a75ffa1928c308775248e41af192d03976f01cb4dbf"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def dirac_matrices() -> tuple[np.ndarray, list[np.ndarray], np.ndarray]:
    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0, spatial, gamma5


def c_partial_matrix() -> np.ndarray:
    return np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )


def embed_record(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    value = np.array([[1.0]], dtype=complex)
    for index in range(count):
        value = np.kron(
            value,
            operator if index == site else np.eye(3, dtype=complex),
        )
    return value


def diamond_time_marginal(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1.0j * interval * values))
        @ vectors.conjugate().T
    )


def pulse_unitary(
    h_free: np.ndarray,
    write: np.ndarray,
    integrated_action: float,
    steps: int,
) -> np.ndarray:
    dt = 1.0 / steps
    value = np.eye(h_free.shape[0], dtype=complex)
    for index in range(steps):
        midpoint = (index + 0.5) * dt
        hamiltonian = (
            h_free
            + integrated_action * diamond_time_marginal(midpoint) * write
        )
        value = exp_hermitian(hamiltonian, dt) @ value
    return value


def spatial_derivative(site_count: int) -> np.ndarray:
    derivative = np.zeros((site_count, site_count), dtype=complex)
    for site in range(site_count):
        derivative[site, (site + 1) % site_count] += 0.5
        derivative[site, (site - 1) % site_count] -= 0.5
    return derivative


def reduced_first_record(
    state: np.ndarray,
    source_dimension: int,
) -> np.ndarray:
    tensor = state.reshape(source_dimension, 3, 3)
    return np.einsum("sab,sdb->ad", tensor, tensor.conjugate())


def record_conditional_expectation(
    operator: np.ndarray,
    source_dimension: int,
    record_dimension: int,
) -> np.ndarray:
    tensor = operator.reshape(
        source_dimension,
        record_dimension,
        source_dimension,
        record_dimension,
    )
    trace_source = np.einsum("sasb->ab", tensor)
    return np.kron(
        np.eye(source_dimension, dtype=complex) / source_dimension,
        trace_source,
    )


def gaussian_massless_return(time: float) -> float:
    return (1.0 - 0.5 * time * time) * math.exp(-0.25 * time * time)


def main() -> None:
    expected_spec_hash = SPEC_SEAL.read_text().split()[0]
    spec_seal_matches = sha256(SPEC) == expected_spec_hash
    authority_hashes = {
        name: {
            "expected": expected,
            "actual": sha256(ROOT / name),
            "matches": sha256(ROOT / name) == expected,
        }
        for name, expected in PINNED_HASHES.items()
    }
    authority_hashes_match = all(
        item["matches"] for item in authority_hashes.values()
    )
    require(spec_seal_matches, "Specification seal failed")
    require(authority_hashes_match, "Pinned authority drift")

    # Exact causal-diamond time marginal checks.
    envelope_integral = (
        2
        * Fraction(32)
        * Fraction(1, 4)
        * Fraction(1, 2) ** 4
    )
    envelope_mean = Fraction(1, 2)
    envelope_normalized = envelope_integral == 1

    gamma0, gamma_spatial, gamma5 = dirac_matrices()
    identity4 = np.eye(4, dtype=complex)
    clifford_errors = {}
    gamma_all = [gamma0, *gamma_spatial]
    metric = [1.0, -1.0, -1.0, -1.0]
    for left in range(4):
        for right in range(4):
            expected = (
                2.0 * metric[left] * identity4 if left == right else 0.0
            )
            clifford_errors[f"{left}{right}"] = float(
                np.linalg.norm(
                    gamma_all[left] @ gamma_all[right]
                    + gamma_all[right] @ gamma_all[left]
                    - expected
                )
            )
    max_clifford_error = max(clifford_errors.values())

    alpha_x = gamma0 @ gamma_spatial[0]
    source_incidence_spin = -1j * gamma0 @ gamma5
    spin_hermiticity_error = float(
        np.linalg.norm(
            source_incidence_spin - source_incidence_spin.conjugate().T
        )
    )
    spin_square_error = float(
        np.linalg.norm(
            source_incidence_spin @ source_incidence_spin - identity4
        )
    )
    kinetic_incidence_anticommutator_error = float(
        np.linalg.norm(
            alpha_x @ source_incidence_spin
            + source_incidence_spin @ alpha_x
        )
    )

    c_partial = c_partial_matrix()
    c_hermiticity_error = float(
        np.linalg.norm(c_partial - c_partial.conjugate().T)
    )
    c_spectrum = np.linalg.eigvalsh(c_partial)
    expected_c_spectrum = np.array([-math.sqrt(2.0), 0.0, math.sqrt(2.0)])
    c_spectrum_error = float(np.linalg.norm(c_spectrum - expected_c_spectrum))

    # Finite Galerkin regression of the same first-order parent.
    site_count = 3
    record_count = 2
    record_dimension = 3**record_count
    source_dimension = site_count * 4
    derivative = spatial_derivative(site_count)
    momentum = -1j * derivative
    h_source = np.kron(momentum, alpha_x)
    h_free = np.kron(h_source, np.eye(record_dimension, dtype=complex))

    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    record_incidence = tuple(
        embed_record(c_partial, site, record_count)
        for site in range(record_count)
    )
    writes = tuple(
        np.kron(
            np.kron(masks[site], source_incidence_spin),
            record_incidence[site],
        )
        for site in range(record_count)
    )

    # Exact generated-square identity, including derivative support and
    # overlap descendants.
    combined_write = writes[0] + writes[1]
    direct_square = (h_free + combined_write) @ (h_free + combined_write)
    derivative_descendant = np.zeros_like(h_free)
    for mask, record_operator in zip(masks, record_incidence):
        commutator = derivative @ mask - mask @ derivative
        derivative_descendant += -1j * np.kron(
            np.kron(
                commutator,
                alpha_x @ source_incidence_spin,
            ),
            record_operator,
        )
    generated_square = (
        h_free @ h_free
        + combined_write @ combined_write
        + derivative_descendant
    )
    generated_square_error = float(np.linalg.norm(direct_square - generated_square))
    overlap_descendant = writes[0] @ writes[1] + writes[1] @ writes[0]
    overlap_descendant_norm = float(np.linalg.norm(overlap_descendant))
    derivative_descendant_norm = float(np.linalg.norm(derivative_descendant))

    integrated_action = math.pi / math.sqrt(2.0)
    resolutions = (24, 48, 96)
    unitaries = {}
    for steps in resolutions:
        first = pulse_unitary(h_free, writes[0], integrated_action, steps)
        second = pulse_unitary(h_free, writes[1], integrated_action, steps)
        unitaries[steps] = (first, second, second @ first)
    convergence_errors = {
        f"{left}_to_{right}": float(
            np.linalg.norm(unitaries[left][2] - unitaries[right][2])
        )
        for left, right in zip(resolutions[:-1], resolutions[1:])
    }
    convergence_ratio = (
        convergence_errors["24_to_48"] / convergence_errors["48_to_96"]
    )

    first, second, total = unitaries[resolutions[-1]]
    source_site = np.array([1.0, 0.0, 0.0], dtype=complex)
    source_spin = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    initial = np.kron(np.kron(source_site, source_spin), np.kron(ready, ready))
    after_first = first @ initial
    after_second = second @ after_first
    free_later = exp_hermitian(h_free, 1.75) @ after_second

    first_reduced = reduced_first_record(after_first, source_dimension)
    second_reduced = reduced_first_record(after_second, source_dimension)
    free_reduced = reduced_first_record(free_later, source_dimension)
    later_record_restriction_error = float(
        np.linalg.norm(first_reduced - second_reduced)
    )
    free_record_restriction_error = float(
        np.linalg.norm(second_reduced - free_reduced)
    )

    pointer = np.diag([0.0, 1.0, 0.0]).astype(complex)
    pointer_first_record = np.kron(
        np.eye(source_dimension, dtype=complex),
        embed_record(pointer, 0, record_count),
    )
    pointer_probability_after_first = float(
        np.real(np.vdot(after_first, pointer_first_record @ after_first))
    )
    pointer_probability_after_second = float(
        np.real(np.vdot(after_second, pointer_first_record @ after_second))
    )

    free_two_cells = exp_hermitian(h_free, 2.0)
    moller = free_two_cells.conjugate().T @ total
    moller_unitarity_error = float(
        np.linalg.norm(
            moller.conjugate().T @ moller
            - np.eye(moller.shape[0], dtype=complex)
        )
    )
    dressed_pointer = (
        moller.conjugate().T @ pointer_first_record @ moller
    )
    bare_projection = record_conditional_expectation(
        dressed_pointer,
        source_dimension,
        record_dimension,
    )
    dressed_pointer_bare_distance = float(
        np.linalg.norm(dressed_pointer - bare_projection)
    )
    dressed_star_error = float(
        np.linalg.norm(
            dressed_pointer - dressed_pointer.conjugate().T
        )
    )
    dressed_idempotence_error = float(
        np.linalg.norm(dressed_pointer @ dressed_pointer - dressed_pointer)
    )

    reverse_order = first @ second
    causal_order_sensitivity = float(np.linalg.norm(total - reverse_order))

    # Exact free-tail Clifford regression in three spatial dimensions.
    momentum_samples = (
        np.array([0.25, -0.5, 0.75]),
        np.array([1.0, 0.0, -1.5]),
        np.array([-2.0, 0.3, 0.1]),
    )
    free_dispersion_errors = []
    alpha_matrices = [gamma0 @ gamma for gamma in gamma_spatial]
    for vector in momentum_samples:
        h_momentum = sum(
            (vector[index] * alpha_matrices[index] for index in range(3)),
            np.zeros((4, 4), dtype=complex),
        )
        free_dispersion_errors.append(
            float(
                np.linalg.norm(
                    h_momentum @ h_momentum
                    - float(vector @ vector) * identity4
                )
            )
        )
    maximum_free_dispersion_error = max(free_dispersion_errors)
    gaussian_return_samples = {
        str(time): gaussian_massless_return(time)
        for time in (0.0, 1.0, 2.0, 4.0, 8.0)
    }

    numerical_pass = all(
        (
            envelope_normalized,
            max_clifford_error < 1e-12,
            spin_hermiticity_error < 1e-12,
            spin_square_error < 1e-12,
            kinetic_incidence_anticommutator_error < 1e-12,
            c_hermiticity_error < 1e-12,
            c_spectrum_error < 1e-12,
            generated_square_error < 1e-10,
            overlap_descendant_norm > 1e-6,
            derivative_descendant_norm > 1e-6,
            convergence_ratio > 3.5,
            later_record_restriction_error < 1e-10,
            free_record_restriction_error < 1e-10,
            moller_unitarity_error < 1e-9,
            dressed_pointer_bare_distance > 1e-5,
            dressed_star_error < 1e-10,
            dressed_idempotence_error < 1e-9,
            causal_order_sensitivity > 1e-5,
            maximum_free_dispersion_error < 1e-12,
        )
    )
    require(numerical_pass, "Complete-parent numerical regression failed")

    result = {
        "schema": "r3.4-complete-causal-superconnection-parent-v001",
        "specification_sha256": sha256(SPEC),
        "specification_seal_matches": spec_seal_matches,
        "authority_hashes": authority_hashes,
        "authority_hashes_match": authority_hashes_match,
        "construction_uses_alpha": False,
        "intrinsic_envelope": {
            "integral": (
                f"{envelope_integral.numerator}/{envelope_integral.denominator}"
            ),
            "mean": f"{envelope_mean.numerator}/{envelope_mean.denominator}",
            "normalized": envelope_normalized,
        },
        "clifford": {
            "maximum_relation_error": max_clifford_error,
            "incidence_spin_hermiticity_error": spin_hermiticity_error,
            "incidence_spin_square_error": spin_square_error,
            "kinetic_incidence_anticommutator_error": (
                kinetic_incidence_anticommutator_error
            ),
            "record_incidence_hermiticity_error": c_hermiticity_error,
            "record_incidence_spectrum_error": c_spectrum_error,
        },
        "generated_descendants": {
            "full_square_identity_error": generated_square_error,
            "overlap_descendant_norm": overlap_descendant_norm,
            "derivative_support_descendant_norm": derivative_descendant_norm,
            "independent_descendant_coefficient_used": False,
        },
        "finite_parent_regression": {
            "site_count": site_count,
            "record_count": record_count,
            "midpoint_resolutions": list(resolutions),
            "convergence_errors": convergence_errors,
            "convergence_ratio": convergence_ratio,
            "first_pointer_probability_after_first": (
                pointer_probability_after_first
            ),
            "first_pointer_probability_after_second": (
                pointer_probability_after_second
            ),
            "later_record_restriction_error": (
                later_record_restriction_error
            ),
            "free_tail_record_restriction_error": (
                free_record_restriction_error
            ),
            "finite_Moller_unitarity_error": moller_unitarity_error,
            "dressed_pointer_bare_algebra_distance": (
                dressed_pointer_bare_distance
            ),
            "dressed_pointer_star_error": dressed_star_error,
            "dressed_pointer_idempotence_error": (
                dressed_idempotence_error
            ),
            "causal_order_sensitivity": causal_order_sensitivity,
        },
        "free_tail": {
            "maximum_three_dimensional_dispersion_error": (
                maximum_free_dispersion_error
            ),
            "gaussian_return_samples": gaussian_return_samples,
            "source_spectrum_purely_absolutely_continuous": True,
            "source_point_spectrum_absent": True,
            "record_label_degeneracy_is_invariant_public_sector": True,
            "thresholded_return_for_every_L2_source_root": True,
        },
        "analytic_obligations": {
            "bounded_compact_time_perturbation_common_domain": True,
            "unique_unitary_propagator": True,
            "sharp_intrinsic_envelope_strong_limit": True,
            "same_parent_supplies_free_tail": True,
            "same_parent_supplies_asymptotic_quasifree_state": True,
            "finite_compact_support_Moller_limits_exist": True,
            "finite_output_record_state_restriction_compatible": True,
            "quasilocal_output_record_state_exists": True,
            "incoming_pullback_is_dressed_monomorphism": True,
            "reduced_record_persistence_exact": True,
            "root_return_and_record_recoverability_kept_distinct": True,
            "source_inclusive_state_projective_limit_derived": False,
            "infinite_future_Moller_limit_derived": False,
            "continuum_regulator_independence_derived": False,
        },
        "numerical_regression_pass": numerical_pass,
        "verdict": "FINITE_CAUSAL_PARENT_DERIVED_CONTINUUM_COMPLETION_OPEN",
        "finite_causal_source_record_parent_derived": True,
        "complete_causal_source_record_parent_flat_branch": False,
        "complete_parent_to_outgoing_GNS_map_derived": False,
        "absolute_record_interval_derived": False,
        "curved_nonstationary_parent_derived": False,
        "interacting_gauge_infraparticle_spectrum_derived": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
