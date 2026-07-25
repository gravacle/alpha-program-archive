#!/usr/bin/env python3
"""Certificate for the frozen periodic uniform zero-free theorem."""

from __future__ import annotations

from decimal import Decimal, getcontext
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md"
VERIFIER = (
    ROOT
    / "scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_uniform_zero_free_theorem_v001.json"
)

EXPECTED = {
    SPEC:
        "54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690",
    ROOT / "COMPLETE_QSPEC_ANALYTIC_CONTINUATION_INDEPENDENT_ISOMETRY_STABILIZATION_ADDENDUM_V001.md":
        "85d5a138a1c11dbcfcd85428536afd65bad1f9f6603c7a79c9ad489cd3070e37",
    VERIFIER:
        "1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d",
    ROOT / "stage8_execution/work/QSPEC_periodic_analytic_continuation_verification_v003.json":
        "f39103452e214c8e0ef29ebeddd884074140a35316c486fadabb12c4b160bf65",
    ROOT / "COMPLETE_QSPEC_PERIODIC_ANALYTIC_CONTINUATION_INDEPENDENT_RESULT_V001.md":
        "fbe852adafe1d83e506a8f302622ed3a8234354223df029c7183a0dd4b2ea83a",
}

RADIUS = Decimal(1) / Decimal(500)
R0_BOUND = Decimal(813) / Decimal(1000)
GRAPH_RADIUS = Decimal(1) / Decimal(20)
FINITE_CUTOFF = 6
DOMINANCE_START = 7
DIAGNOSTIC_ANGLES = 16
DERIVATIVE_DIAGNOSTIC_ANGLES = 256


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_verifier():
    spec = importlib.util.spec_from_file_location(
        "qspec_independent_v003",
        VERIFIER,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def active_fourier_lift_derivative_norm(
    verifier,
    point: complex,
) -> float:
    derivative = -1j * verifier.directed_difference_derivative(point)
    omega = np.exp(2j * np.pi / 3.0)
    fourier = tuple(
        np.array([omega ** (k * site) for site in range(3)])
        / math.sqrt(3.0)
        for k in (1, 2)
    )
    spatial_values = tuple(
        complex(vector.conjugate() @ derivative @ vector)
        for vector in fourier
    )
    one_body_values = []
    for value in spatial_values:
        for spin_value in (-1.0, 1.0):
            one_body_values.extend((spin_value * value,) * 2)
    lifted_values = tuple(
        sum(one_body_values[index] for index in occupation)
        for occupation in itertools.combinations(range(8), 4)
    )
    return float(max(abs(value) for value in lifted_values))


def stabilized_zero_objects(verifier):
    parent = verifier.build_parent()
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
    if not all(bool(item[1]["pass"]) for item in repaired):
        raise RuntimeError("zero-history isometry stabilization failed")
    zero_cells = tuple(item[0] for item in repaired)
    zero_composites = verifier.composite_kraus(zero_cells)
    support, invariance = verifier.reachable_support(
        parent["source_vector"],
        zero_composites,
    )
    transfer = verifier.reduced_transfer(
        zero_composites,
        zero_composites,
        support,
    )
    start = (parent["density"] @ support).reshape(-1)
    trace_functional = support.conjugate().reshape(-1)
    return (
        parent,
        zero_composites,
        support,
        invariance,
        transfer,
        start,
        trace_functional,
    )


def zero_transfer_certificate(
    transfer: np.ndarray,
    start: np.ndarray,
    trace_functional: np.ndarray,
) -> tuple[dict[str, object], np.ndarray]:
    eigenvalues, right_vectors = np.linalg.eig(transfer)
    leading_index = int(np.argmax(np.abs(eigenvalues)))
    leading = complex(eigenvalues[leading_index])
    right = right_vectors[:, leading_index]

    left_values, left_vectors = np.linalg.eig(transfer.conjugate().T)
    left_index = int(
        np.argmin(np.abs(left_values - np.conjugate(leading)))
    )
    left = left_vectors[:, left_index]
    left /= np.conjugate(np.vdot(left, right))
    projector = np.outer(right, left.conjugate())
    remainder = transfer - projector

    left_singular, singular_values, right_singular_h = np.linalg.svd(
        remainder,
        full_matrices=False,
    )
    singular_max = float(singular_values[0])
    singular_left = left_singular[:, 0]
    singular_right = right_singular_h.conjugate().T[:, 0]
    right_residual = float(
        np.linalg.norm(
            remainder @ singular_right
            - singular_max * singular_left
        )
    )
    left_residual = float(
        np.linalg.norm(
            remainder.conjugate().T @ singular_left
            - singular_max * singular_right
        )
    )

    gram = remainder.conjugate().T @ remainder
    independent_squared = float(np.max(np.linalg.eigvalsh(gram)))
    independent_singular = math.sqrt(max(independent_squared, 0.0))

    rows = {
        "leading_eigenvalue": {
            "real": leading.real,
            "imag": leading.imag,
            "absolute": abs(leading),
        },
        "leading_unit_error": abs(leading - 1.0),
        "projector_idempotence_error":
            float(np.linalg.norm(projector @ projector - projector)),
        "projector_Hermiticity_error":
            float(np.linalg.norm(projector - projector.conjugate().T)),
        "left_invariance_error":
            float(np.linalg.norm(projector @ transfer - projector)),
        "right_invariance_error":
            float(np.linalg.norm(transfer @ projector - projector)),
        "transfer_spectral_norm": float(np.linalg.norm(transfer, 2)),
        "remainder_spectral_norm_SVD": singular_max,
        "remainder_spectral_norm_Gram": independent_singular,
        "singular_method_disagreement":
            abs(singular_max - independent_singular),
        "right_singular_residual": right_residual,
        "left_singular_residual": left_residual,
        "amplitude_coefficient_at_zero": {
            "real": complex(
                trace_functional @ projector @ start
            ).real,
            "imag": complex(
                trace_functional @ projector @ start
            ).imag,
        },
        "amplitude_coefficient_unit_error":
            abs(trace_functional @ projector @ start - 1.0),
        "start_norm": float(np.linalg.norm(start)),
        "trace_functional_norm":
            float(np.linalg.norm(trace_functional)),
    }
    rows["pass"] = bool(
        rows["leading_unit_error"] < 1e-12
        and rows["projector_idempotence_error"] < 1e-11
        and rows["projector_Hermiticity_error"] < 1e-11
        and rows["left_invariance_error"] < 1e-11
        and rows["right_invariance_error"] < 1e-11
        and rows["transfer_spectral_norm"] < 1.0 + 1e-11
        and singular_max < float(R0_BOUND)
        and independent_singular < float(R0_BOUND)
        and rows["singular_method_disagreement"] < 1e-12
        and right_residual < 1e-11
        and left_residual < 1e-11
        and rows["amplitude_coefficient_unit_error"] < 1e-11
        and rows["start_norm"] < 1.0 + 1e-11
        and rows["trace_functional_norm"] < math.sqrt(5.0) + 1e-11
    )
    return rows, projector


def decimal_bounds() -> dict[str, Decimal]:
    getcontext().prec = 80
    one = Decimal(1)
    two = Decimal(2)
    three = Decimal(3)
    five = Decimal(5)
    free_lipschitz = (
        two
        / three
        * (
            one
            + two
            * RADIUS
            / three
            * (RADIUS / three).exp()
        )
    )
    delta = free_lipschitz * RADIUS
    epsilon = three * ((two * delta).exp() - one)
    complement = R0_BOUND + epsilon
    separation = (
        one
        - epsilon
        - epsilon * GRAPH_RADIUS
        - complement
    )
    graph_map = epsilon / separation
    graph_contraction = graph_map * graph_map
    lambda_min = one - epsilon * (one + GRAPH_RADIUS)
    complement_tilde = (
        complement + epsilon * GRAPH_RADIUS
    )
    projector_delta = (
        two * GRAPH_RADIUS
        + two * GRAPH_RADIUS * GRAPH_RADIUS
    ) / (one - GRAPH_RADIUS * GRAPH_RADIUS)
    sqrt_five = five.sqrt()
    coefficient_min = one - sqrt_five * projector_delta
    similarity_condition = (
        one + GRAPH_RADIUS
    ) / (
        one - GRAPH_RADIUS
    )
    ratio = complement_tilde / lambda_min
    prefactor = (
        sqrt_five
        * similarity_condition
        / coefficient_min
    )
    return {
        "free_Lipschitz": free_lipschitz,
        "delta": delta,
        "epsilon": epsilon,
        "complement_bound": complement,
        "separation": separation,
        "graph_map_radius": graph_map,
        "graph_contraction": graph_contraction,
        "lambda_min": lambda_min,
        "complement_tilde_max": complement_tilde,
        "projector_delta": projector_delta,
        "coefficient_min": coefficient_min,
        "similarity_condition": similarity_condition,
        "q": ratio,
        "prefactor": prefactor,
    }


def diagnostic_checks(
    verifier,
    parent,
    zero_composites,
    support,
    transfer_zero,
    bounds: dict[str, Decimal],
) -> dict[str, object]:
    free_lipschitz = float(bounds["free_Lipschitz"])
    derivative_rows = []
    maximum_enumerated = 0.0
    maximum_matrix = 0.0
    for index in range(DERIVATIVE_DIAGNOSTIC_ANGLES):
        point = float(RADIUS) * np.exp(
            2j * np.pi * index / DERIVATIVE_DIAGNOSTIC_ANGLES
        )
        enumerated = active_fourier_lift_derivative_norm(
            verifier,
            point,
        )
        matrix_norm = float(
            np.linalg.norm(parent["free_derivative"](point), 2)
        )
        maximum_enumerated = max(maximum_enumerated, enumerated)
        maximum_matrix = max(maximum_matrix, matrix_norm)
        derivative_rows.append(abs(enumerated - matrix_norm))

    transfer_rows = {}
    maximum_transfer_difference = 0.0
    for index in range(DIAGNOSTIC_ANGLES):
        point = float(RADIUS) * np.exp(
            2j * np.pi * index / DIAGNOSTIC_ANGLES
        )
        branch_cells = tuple(
            verifier.cell_kraus(
                parent["free"](point),
                interaction,
                parent["record"],
            )
            for interaction in parent["interactions"]
        )
        branch_composites = verifier.composite_kraus(branch_cells)
        transfer = verifier.reduced_transfer(
            branch_composites,
            zero_composites,
            support,
        )
        difference = float(
            np.linalg.norm(transfer - transfer_zero, 2)
        )
        maximum_transfer_difference = max(
            maximum_transfer_difference,
            difference,
        )
        transfer_rows[f"{index:02d}"] = difference

    return {
        "derivative_mesh_points": DERIVATIVE_DIAGNOSTIC_ANGLES,
        "maximum_enumerated_active_lift_derivative_norm":
            maximum_enumerated,
        "maximum_direct_matrix_derivative_norm": maximum_matrix,
        "maximum_enumeration_matrix_disagreement":
            max(derivative_rows),
        "analytic_free_Lipschitz_bound": free_lipschitz,
        "derivative_diagnostic_pass": bool(
            maximum_enumerated <= free_lipschitz
            and maximum_matrix <= free_lipschitz
            and max(derivative_rows) < 1e-11
        ),
        "transfer_boundary_samples": transfer_rows,
        "maximum_sampled_transfer_difference":
            maximum_transfer_difference,
        "analytic_transfer_difference_bound":
            float(bounds["epsilon"]),
        "transfer_negative_control_pass": bool(
            maximum_transfer_difference
            <= float(bounds["epsilon"])
        ),
    }


def main() -> None:
    for path, expected in EXPECTED.items():
        if sha256(path) != expected:
            raise RuntimeError(f"authority drift: {path.name}")

    verifier = load_verifier()
    (
        parent,
        zero_composites,
        support,
        support_invariance,
        transfer_zero,
        start,
        trace_functional,
    ) = stabilized_zero_objects(verifier)
    zero_certificate, _ = zero_transfer_certificate(
        transfer_zero,
        start,
        trace_functional,
    )
    bounds = decimal_bounds()
    diagnostics = diagnostic_checks(
        verifier,
        parent,
        zero_composites,
        support,
        transfer_zero,
        bounds,
    )

    finite_bounds = {
        str(volume): (
            Decimal(5).sqrt()
            * Decimal(volume)
            * bounds["epsilon"]
            * (Decimal(1) + bounds["epsilon"])
            ** Decimal(volume - 1)
        )
        for volume in range(1, FINITE_CUTOFF + 1)
    }
    dominance_at_start = (
        bounds["prefactor"]
        * bounds["q"] ** Decimal(DOMINANCE_START)
    )

    graph_pass = bool(
        bounds["separation"] > 0
        and bounds["graph_map_radius"] < GRAPH_RADIUS
        and bounds["graph_contraction"] < 1
    )
    amplitude_pass = bool(
        bounds["lambda_min"] > 0
        and bounds["coefficient_min"] > 0
        and bounds["q"] < 1
        and max(finite_bounds.values()) < 1
        and dominance_at_start < 1
    )
    theorem_pass = bool(
        zero_certificate["pass"]
        and support.shape[1] == 5
        and support_invariance < 1e-11
        and diagnostics["derivative_diagnostic_pass"]
        and diagnostics["transfer_negative_control_pass"]
        and graph_pass
        and amplitude_pass
    )

    result = {
        "schema": "complete_qspec_periodic_uniform_zero_free_theorem_v001",
        "spec_sha256": sha256(SPEC),
        "zero_transfer_certificate": zero_certificate,
        "zero_support_dimension": int(support.shape[1]),
        "zero_support_invariance_residual": support_invariance,
        "theorem_constants": {
            "disk_radius": str(RADIUS),
            "zero_complement_bound": str(R0_BOUND),
            "graph_ball_radius": str(GRAPH_RADIUS),
            "finite_volume_cutoff": FINITE_CUTOFF,
            "dominance_start": DOMINANCE_START,
        },
        "analytic_bounds": {
            key: str(value)
            for key, value in bounds.items()
        },
        "finite_volume_difference_bounds": {
            key: str(value)
            for key, value in finite_bounds.items()
        },
        "dominance_bound_at_N7": str(dominance_at_start),
        "diagnostic_checks": diagnostics,
        "invariant_graph_pass": graph_pass,
        "uniform_nonzero_amplitude_pass": amplitude_pass,
        "uniform_analytic_log_density_pass": theorem_pass,
        "verdict": (
            "PERIODIC_UNIFORM_ZERO_FREE_AND_DENSITY_PROVED"
            if theorem_pass
            else "PERIODIC_UNIFORM_ZERO_FREE_AND_DENSITY_BLOCKED"
        ),
        "pass": theorem_pass,
        "periodic_volume_uniform_zero_free_neighborhood_proved":
            theorem_pass,
        "periodic_connected_linked_cluster_density_proved":
            theorem_pass,
        "all_stage8_regulators_zero_free_proved": False,
        "all_connected_cellulations_linked_cluster_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "r0": zero_certificate[
                    "remainder_spectral_norm_SVD"
                ],
                "epsilon": result["analytic_bounds"]["epsilon"],
                "finite_N6": result[
                    "finite_volume_difference_bounds"
                ]["6"],
                "dominance_N7": result["dominance_bound_at_N7"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not theorem_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
