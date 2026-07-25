#!/usr/bin/env python3
"""Rigorous composition gate for the frozen periodic zero-free theorem."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import gc
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "COMPLETE_QSPEC_PERIODIC_ZERO_FREE_PROMOTION_SPEC_V001.md"
SPEC_SEAL = Path(f"{SPEC}.seal.sha256")
SCRIPT_SEAL = Path(f"{Path(__file__).resolve()}.seal.sha256")
CERT_SCRIPT = (
    ROOT / "scripts/certify_complete_qspec_zero_transfer_dyadic_v001.py"
)
CERT_OUTPUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_zero_transfer_dyadic_ball_certificate_v001.json"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_zero_free_promotion_v001.json"
)

EXPECTED = {
    SPEC:
        "8b47ff6af29537289675dd40d8095a2dc606147a93fb524a3ff659e0aabb6bb7",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md":
        "54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690",
    ROOT / "stage8_execution/work/QSPEC_periodic_uniform_zero_free_theorem_v001.json":
        "048d18a2ac666639a44ec0d52b584a412ece9fdeb90837abffa86e831fc652e0",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_REVIEW_CORRECTION_V001.md":
        "8d2ab3a0102cb4e8ba7ab925773e1a6fd08b763202859688b14ea4cd12f39650",
    ROOT / "COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md":
        "ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95",
    CERT_SCRIPT:
        "26e76a3f3625bdcddf3324bde28b94dd58f75454a8edbcacc5872c43356db015",
    CERT_OUTPUT:
        "93a37fb83fe9b7264808a80b2f7bffb487af642180affb6918c5b98b65dbb74b",
    ROOT / "COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_RESULT_V001.md":
        "2c193f34786c2eeff57a6ea611116448926076d676fd177b5f9c73980ec6496a",
    ROOT / "scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py":
        "1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d",
    ROOT / "COMPLETE_QSPEC_PERIODIC_ZERO_FREE_ZERO_ALIGNMENT_ADDENDUM_V001.md":
        "3a5c7a7d6b3ed2ae4d9c69feab78bdb34c2222149415e9fa0e8eb5b38f4670f1",
}

EXPECTED_TRANSFER_HASH = (
    "69d6a95de251be3e3aa83d7344c7961b2023f41416399b760d3096fcde83718b"
)
EXPECTED_TRACE_COLUMN_HASH = (
    "07506154f602a1fa17e32c81f4bc377e547868eb4bf540ed11248949afea0876"
)
EXPECTED_START_HASH = (
    "510205f86d4b068828d0a2ca0bfa4d6e43c62f44c555b7a627d25b20e0d4e4c7"
)
EXPECTED_ANALYTIC_ZERO_TRANSFER_HASH = (
    "5e59e660c1b0859e915f86258944972b0ecf5e939c4ca264158edc3eb95aec39"
)

PRECISION_BITS = 192
FINITE_CUTOFF = 6
DOMINANCE_START = 7


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_authorities() -> dict[str, str]:
    observed: dict[str, str] = {}
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing authority: {path}")
        actual = sha256(path)
        require(
            actual == expected,
            f"authority mismatch: {path}: {actual} != {expected}",
        )
        observed[str(path.relative_to(ROOT))] = actual

    for target, seal in (
        (SPEC, SPEC_SEAL),
        (Path(__file__).resolve(), SCRIPT_SEAL),
    ):
        fields = seal.read_text(encoding="ascii").strip().split()
        require(len(fields) == 2, f"malformed seal: {seal}")
        require(fields[0] == sha256(target), f"seal hash mismatch: {target}")
        require(fields[1] == target.name, f"seal name mismatch: {target}")
    return observed


def load_certificate_module():
    module_spec = importlib.util.spec_from_file_location(
        "dyadic_r0_certificate_v001",
        CERT_SCRIPT,
    )
    module = importlib.util.module_from_spec(module_spec)
    assert module_spec.loader is not None
    module_spec.loader.exec_module(module)
    return module


def stabilized_objects(certificate):
    verifier = certificate.load_verifier()
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
    require(
        all(bool(item[1]["pass"]) for item in repaired),
        "zero-history Stinespring repair failed",
    )
    zero_cells = tuple(item[0] for item in repaired)
    zero_composites = verifier.composite_kraus(zero_cells)
    support, support_invariance = verifier.reachable_support(
        parent["source_vector"],
        zero_composites,
    )
    require(support.shape[1] == 5, "unexpected support dimension")
    require(support_invariance < 1e-11, "support invariance failed")
    transfer = verifier.reduced_transfer(
        zero_composites,
        zero_composites,
        support,
    )
    analytic_zero_cells = tuple(
        verifier.cell_kraus(
            parent["free"](0.0),
            interaction,
            parent["record"],
        )
        for interaction in parent["interactions"]
    )
    analytic_zero_composites = verifier.composite_kraus(
        analytic_zero_cells
    )
    analytic_zero_transfer = verifier.reduced_transfer(
        analytic_zero_composites,
        zero_composites,
        support,
    )
    start = (parent["density"] @ support).reshape(-1)
    trace_column = support.reshape(-1)
    return (
        transfer,
        analytic_zero_transfer,
        trace_column,
        start,
        support_invariance,
    )


def upper(value):
    return value.upper()


def lower(value):
    return value.lower()


def exact_anchor_scalars(certificate, trace_column, start):
    trace = certificate.acb_column_from_numpy(trace_column)
    start_ball = certificate.acb_column_from_numpy(start)
    trace_dagger = trace.conjugate().transpose()
    start_dagger = start_ball.conjugate().transpose()
    trace_norm_squared = (trace_dagger * trace)[0, 0]
    start_norm_squared = (start_dagger * start_ball)[0, 0]
    overlap = (trace_dagger * start_ball)[0, 0]
    for name, value in (
        ("trace norm", trace_norm_squared),
        ("start norm", start_norm_squared),
    ):
        require(value.imag.contains(0), f"{name} acquired imaginary part")
        require(value.real > 0, f"{name} is not positive")
    return {
        "trace_norm_squared": trace_norm_squared,
        "start_norm_squared": start_norm_squared,
        "trace_norm_upper": trace_norm_squared.real.upper().sqrt().upper(),
        "start_norm_upper": start_norm_squared.real.upper().sqrt().upper(),
        "overlap": overlap,
        "overlap_absolute_lower": abs(overlap).lower(),
        "overlap_unit_error_upper": abs(overlap - 1).upper(),
    }


def exact_zero_alignment(
    certificate,
    transfer,
    analytic_zero_transfer,
    trace_column,
):
    complement, projector, anchor = certificate.exact_ball_complement(
        transfer,
        trace_column,
    )
    analytic_zero_ball = certificate.acb_matrix_from_numpy(
        analytic_zero_transfer
    )
    defect = analytic_zero_ball - (projector + complement)
    norms = certificate.matrix_norm_upper(defect)
    allowance = certificate.arb(1) / certificate.arb(10**10)
    passed = bool(norms["two"] < allowance)
    result = {
        "analytic_zero_to_anchor_norm_one_upper":
            str(norms["one"]),
        "analytic_zero_to_anchor_norm_infinity_upper":
            str(norms["infinity"]),
        "analytic_zero_to_anchor_norm_two_upper":
            str(norms["two"]),
        "required_ceiling": str(allowance),
        "repaired_T0_anchor_certificate": anchor,
        "pass": passed,
    }
    del complement
    del projector
    del analytic_zero_ball
    del defect
    gc.collect()
    require(passed, "analytic-zero to certified-anchor alignment failed")
    return result


def analytic_bounds(certificate, scalars):
    arb = certificate.arb
    one = arb(1)
    radius = arb(1) / arb(500)
    r_bar = arb(203) / arb(250)
    graph_radius = arb(1) / arb(20)
    anchor_allowance = arb(1) / arb(10**10)

    free_lipschitz = (
        arb(2)
        / arb(3)
        * (
            one
            + arb(2)
            * radius
            / arb(3)
            * (radius / arb(3)).exp()
        )
    )
    free_delta = free_lipschitz * radius
    epsilon = arb(3) * ((arb(2) * free_delta).exp() - one)
    eta = epsilon.upper() + anchor_allowance

    separation = (
        one
        - eta
        - eta * graph_radius
        - (r_bar + eta)
    ).lower()
    graph_map = (eta / separation).upper()
    graph_lipschitz = (graph_map * graph_map).upper()
    lambda_min = (
        one - eta * (one + graph_radius)
    ).lower()
    complement_max = (
        r_bar + eta + eta * graph_radius
    ).upper()
    projector_delta = (
        (
            arb(2) * graph_radius
            + arb(2) * graph_radius * graph_radius
        )
        / (one - graph_radius * graph_radius)
    ).upper()
    similarity_condition = (
        (one + graph_radius)
        / (one - graph_radius)
    ).upper()

    trace_start_product = (
        scalars["trace_norm_upper"]
        * scalars["start_norm_upper"]
    ).upper()
    coefficient_min = (
        scalars["overlap_absolute_lower"]
        - trace_start_product * projector_delta
    ).lower()

    finite_bounds = {}
    for volume in range(1, FINITE_CUTOFF + 1):
        bound = (
            scalars["overlap_unit_error_upper"]
            + trace_start_product
            * volume
            * eta
            * (one + eta) ** (volume - 1)
        ).upper()
        finite_bounds[str(volume)] = bound

    ratio = (complement_max / lambda_min).upper()
    prefactor = (
        trace_start_product
        * similarity_condition
        / coefficient_min
    ).upper()
    dominance = (
        prefactor * ratio ** DOMINANCE_START
    ).upper()

    graph_pass = bool(
        separation > 0
        and graph_map < graph_radius
        and graph_lipschitz < 1
    )
    coefficient_pass = bool(coefficient_min > 0)
    finite_pass = bool(
        all(bound < 1 for bound in finite_bounds.values())
    )
    dominance_pass = bool(
        lambda_min > 0
        and ratio < 1
        and dominance < 1
    )
    return {
        "disk_radius": str(radius),
        "free_Lipschitz": str(free_lipschitz),
        "free_delta": str(free_delta),
        "transfer_perturbation_epsilon": str(epsilon),
        "anchor_allowance": str(anchor_allowance),
        "total_perturbation_eta_upper": str(eta),
        "separation_lower": str(separation),
        "graph_map_upper": str(graph_map),
        "graph_Lipschitz_upper": str(graph_lipschitz),
        "lambda_modulus_lower": str(lambda_min),
        "complement_norm_upper": str(complement_max),
        "projector_delta_upper": str(projector_delta),
        "similarity_condition_upper": str(similarity_condition),
        "trace_start_norm_product_upper": str(trace_start_product),
        "coefficient_modulus_lower": str(coefficient_min),
        "finite_volume_nonzero_bounds": {
            key: str(value)
            for key, value in finite_bounds.items()
        },
        "large_volume_ratio_upper": str(ratio),
        "large_volume_prefactor_upper": str(prefactor),
        "dominance_bound_at_N7_upper": str(dominance),
        "graph_pass": graph_pass,
        "coefficient_pass": coefficient_pass,
        "finite_volume_pass": finite_pass,
        "large_volume_dominance_pass": dominance_pass,
        "pass": bool(
            graph_pass
            and coefficient_pass
            and finite_pass
            and dominance_pass
        ),
    }


def main() -> None:
    started = time.time()
    require(sys.flags.isolated == 1, "execute with python3 -I")
    require(sys.flags.no_user_site == 1, "user site must be disabled")
    authorities = verify_authorities()
    certificate = load_certificate_module()
    wheel_record = certificate.verify_full_wheel_record()
    certificate.load_verified_ball_runtime()
    certificate.flint.ctx.prec = PRECISION_BITS
    certificate.flint.ctx.threads = 4

    cert_data = json.loads(CERT_OUTPUT.read_text(encoding="utf-8"))
    require(
        cert_data["verdict"]
        == "FROZEN_DYADIC_ZERO_TRANSFER_R0_CERTIFIED",
        "R0 certificate verdict mismatch",
    )
    require(cert_data["pass"] is True, "R0 certificate did not pass")
    require(
        cert_data["validated_frozen_dyadic_R0_enclosure_proved"]
        is True,
        "R0 enclosure flag is false",
    )
    require(
        cert_data["singular_value_certificate"]["pass"] is True,
        "anchor-complement certificate did not pass",
    )

    (
        transfer,
        analytic_zero_transfer,
        trace_column,
        start,
        support_invariance,
    ) = stabilized_objects(certificate)
    require(
        certificate.canonical_hex_sha256(transfer)
        == EXPECTED_TRANSFER_HASH,
        "transfer hash mismatch",
    )
    require(
        certificate.canonical_hex_sha256(trace_column)
        == EXPECTED_TRACE_COLUMN_HASH,
        "trace-column hash mismatch",
    )
    require(
        certificate.canonical_hex_sha256(start)
        == EXPECTED_START_HASH,
        "start-vector hash mismatch",
    )
    require(
        certificate.canonical_hex_sha256(analytic_zero_transfer)
        == EXPECTED_ANALYTIC_ZERO_TRANSFER_HASH,
        "analytic-zero transfer hash mismatch",
    )

    scalars = exact_anchor_scalars(
        certificate,
        trace_column,
        start,
    )
    zero_alignment = exact_zero_alignment(
        certificate,
        transfer,
        analytic_zero_transfer,
        trace_column,
    )
    bounds = analytic_bounds(certificate, scalars)
    passed = bool(zero_alignment["pass"] and bounds["pass"])

    result = {
        "schema":
            "complete_qspec_periodic_zero_free_promotion_v001",
        "authorities": authorities,
        "script_sha256": sha256(Path(__file__)),
        "python_isolated_mode": bool(sys.flags.isolated),
        "python_flint_version": certificate.flint.__version__,
        "arb_precision_bits": PRECISION_BITS,
        "verified_wheel_hashed_files":
            wheel_record["verified_hashed_files"],
        "verified_wheel_native_files":
            wheel_record["verified_native_files"],
        "transfer_canonical_hex_sha256": EXPECTED_TRANSFER_HASH,
        "trace_column_canonical_hex_sha256":
            EXPECTED_TRACE_COLUMN_HASH,
        "start_vector_canonical_hex_sha256": EXPECTED_START_HASH,
        "analytic_zero_transfer_canonical_hex_sha256":
            EXPECTED_ANALYTIC_ZERO_TRANSFER_HASH,
        "zero_support_invariance_residual_binary64":
            support_invariance,
        "anchor_scalars": {
            key: str(value)
            for key, value in scalars.items()
        },
        "zero_alignment_certificate": zero_alignment,
        "analytic_certificate": bounds,
        "verdict": (
            "FROZEN_DYADIC_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED"
            if passed
            else "FROZEN_DYADIC_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_BLOCKED"
        ),
        "pass": passed,
        "frozen_dyadic_periodic_zero_free_neighborhood_proved":
            passed,
        "frozen_dyadic_periodic_thermodynamic_log_density_proved":
            passed,
        "continuous_time_parent_zero_free_proved": False,
        "periodic_connected_linked_cluster_density_proved": False,
        "all_stage8_regulators_zero_free_proved": False,
        "all_connected_cellulations_linked_cluster_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "elapsed_seconds": time.time() - started,
        "no_alpha_or_coupling_target_access_attestation": True,
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
                "epsilon": bounds["transfer_perturbation_epsilon"],
                "eta": bounds["total_perturbation_eta_upper"],
                "coefficient_min":
                    bounds["coefficient_modulus_lower"],
                "finite_N6":
                    bounds["finite_volume_nonzero_bounds"]["6"],
                "dominance_N7":
                    bounds["dominance_bound_at_N7_upper"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        ),
        flush=True,
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
