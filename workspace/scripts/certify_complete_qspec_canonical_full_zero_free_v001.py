#!/usr/bin/env python3
"""Outward-rounded all-volume gate for the canonical physical transfer."""

from __future__ import annotations

import base64
import csv
import hashlib
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
SPEC = ROOT / "COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_SPEC_V001.md"
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_canonical_full_zero_free_promotion_v001.json"
)
EXACT_JSON = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_exact_spin2_support_bridge_v001.json"
)
CANONICAL_JSON = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_canonical_spin2_transfer_ball_certificate_v001.json"
)
EXTERNAL_REVIEW = Path(
    "/Users/bgm/MB Work/alpha_supervision/"
    "OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md"
)
FLINT_ROOT = ROOT.parents[1] / ".proof_deps/python_flint"
FLINT_RECORD = (
    FLINT_ROOT / "python_flint-0.6.0.dist-info/RECORD"
)

EXPECTED = {
    SPEC:
        "61d3822f78b1b48c690951e4ffb710ca798ee2b8cbc7986d5c1b6164c7e52e83",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md":
        "b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0",
    EXACT_JSON:
        "093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md":
        "6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676",
    ROOT / "COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md":
        "e0b477ac3fa2a8cdb48523465739d695e46076c141356229eed249789e26fdf2",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_SPEC_V001.md":
        "80c21c579518bb28878b0468615e3d03a02654356964074a50e3684820f43f06",
    ROOT / "scripts/certify_complete_qspec_canonical_spin2_transfer_v001.py":
        "00da930b54722791552434252a9cbe6b26a43494d4f7d78eae365bb7938481ce",
    CANONICAL_JSON:
        "46dd8f18dc7e9bfcdda7b90278f8cc71bd1e80aa157c29ba39433057d74be807",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md":
        "12dc40274aa431e08245573963cf2f47de6f7ed4aa9803ae38b71539f538d261",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md":
        "54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690",
    ROOT / "COMPLETE_QSPEC_PERIODIC_REDUCED_TO_FULL_BRIDGE_CORRECTION_V001.md":
        "40e5fdac17bd61616b34fcd401a0019b8889e0df38aa0d0b06bd4aec2b1e9e59",
    EXTERNAL_REVIEW:
        "83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2",
    FLINT_ROOT / "python_flint-0.6.0.dist-info/METADATA":
        "d6b5be0f3a94ff92ad45f8e9d8991ac8face10ab71e362b8b9f25819df4ef06b",
    FLINT_RECORD:
        "9b76e8ba99a8555fa73c855c2459614714f25136238c1c96fa6c82dad5b9cf94",
    FLINT_ROOT / "flint/__init__.py":
        "b959e94c11c23633c0cbfea849a07955b8f252fc3100fd2ed52bd3c35118ba93",
}

SEALED_LOCAL = (
    SPEC,
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_SPEC_V001.md",
    ROOT / "scripts/certify_complete_qspec_canonical_spin2_transfer_v001.py",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md",
    ROOT / "COMPLETE_QSPEC_PERIODIC_REDUCED_TO_FULL_BRIDGE_CORRECTION_V001.md",
)

PRECISION_BITS = 192
FINITE_CUTOFF = 6
DOMINANCE_START = 7


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def atomic_write_result(payload: dict[str, object]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUT.with_suffix(f"{OUT.suffix}.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(OUT)


def blocked_payload(reason: str) -> dict[str, object]:
    return {
        "schema": "complete_qspec_canonical_full_zero_free_promotion_v001",
        "script_sha256": sha256(SCRIPT),
        "verdict":
            "CANONICAL_FULL_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_BLOCKED",
        "pass": False,
        "block_reason": reason,
        "canonical_full_periodic_zero_free_neighborhood_proved": False,
        "full_completed_record_amplitude_zero_free_for_all_volumes":
            False,
        "canonical_full_periodic_thermodynamic_log_density_proved":
            False,
        "full_completed_record_amplitude_thermodynamic_log_density_proved":
            False,
        "frozen_periodic_local_source_polydisc_proved": False,
        "physical_continuum_local_source_addressability_derived": False,
        "periodic_connected_linked_cluster_density_proved": False,
        "connected_cumulant_absolute_majorant_proved": False,
        "all_stage8_regulators_zero_free_proved": False,
        "all_connected_cellulations_linked_cluster_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_coupling_or_alpha_target_access_attestation": True,
    }


def verify_seal(path: Path) -> None:
    seal = Path(f"{path}.seal.sha256")
    require(seal.is_file(), f"missing seal: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {seal}")
    require(fields[0] == sha256(path), f"seal hash mismatch: {path}")
    require(fields[1] == path.name, f"seal name mismatch: {path}")


def verify_authorities() -> dict[str, str]:
    observed = {}
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing authority: {path}")
        actual = sha256(path)
        require(actual == expected, f"authority mismatch: {path}")
        observed[str(path)] = actual
    for path in SEALED_LOCAL:
        verify_seal(path)
    verify_seal(SCRIPT)
    return observed


def verify_wheel_record() -> dict[str, int]:
    verified = 0
    native = 0
    root_resolved = FLINT_ROOT.resolve()
    with FLINT_RECORD.open(newline="", encoding="utf-8") as handle:
        for relative, encoded_hash, encoded_size in csv.reader(handle):
            if not encoded_hash:
                continue
            candidate = (FLINT_ROOT / relative).resolve()
            require(
                candidate.is_relative_to(root_resolved),
                f"wheel path escapes root: {relative}",
            )
            require(candidate.is_file(), f"wheel file missing: {relative}")
            algorithm, digest = encoded_hash.split("=", 1)
            require(algorithm == "sha256", "non-SHA256 wheel entry")
            observed = base64.urlsafe_b64encode(
                hashlib.sha256(candidate.read_bytes()).digest()
            ).decode("ascii").rstrip("=")
            require(observed == digest, f"wheel hash mismatch: {relative}")
            require(
                candidate.stat().st_size == int(encoded_size),
                f"wheel size mismatch: {relative}",
            )
            verified += 1
            if candidate.suffix in (".so", ".dylib"):
                native += 1
    require(verified > 100, "implausibly small python-flint record")
    return {
        "verified_hashed_files": verified,
        "verified_native_files": native,
    }


def load_flint():
    sys.path.insert(0, str(FLINT_ROOT))
    import flint

    flint.ctx.prec = PRECISION_BITS
    flint.ctx.threads = 4
    return flint


def audit_flint_origins() -> list[str]:
    origins = []
    root = FLINT_ROOT.resolve()
    for name, module in sorted(sys.modules.items()):
        if not (name == "flint" or name.startswith("flint.")):
            continue
        origin = getattr(module, "__file__", None)
        if origin is None:
            continue
        path = Path(origin).resolve()
        require(
            path.is_relative_to(root),
            f"flint module imported outside pinned root: {name}: {path}",
        )
        origins.append(str(path.relative_to(root)))
    require(origins, "no loaded flint origins recorded")
    return origins


def verify_prerequisites() -> dict[str, object]:
    exact = json.loads(EXACT_JSON.read_text(encoding="utf-8"))
    canonical = json.loads(CANONICAL_JSON.read_text(encoding="utf-8"))

    require(exact["pass"] is True, "exact support bridge did not pass")
    require(
        exact["verdict"] == "EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_DERIVED",
        "exact support bridge verdict mismatch",
    )
    require(
        exact["exact_zero_history_spin2_support_derived"] is True,
        "exact support sector is not derived",
    )
    require(
        exact["exact_reduced_to_full_finite_amplitude_identity_derived"]
        is True,
        "exact full-amplitude bridge is absent",
    )
    require(
        exact["right_history_support_induction_derived"] is True,
        "right-history induction is absent",
    )

    require(canonical["pass"] is True, "canonical transfer did not pass")
    require(
        canonical["verdict"]
        == "CANONICAL_EXACT_SPIN2_TRANSFER_AND_R0_BALL_CERTIFIED",
        "canonical transfer verdict mismatch",
    )
    for key in (
        "canonical_spin2_transfer_ball_certified",
        "exact_physical_R0_norm_below_0_812",
        "exact_trace_identity_algebraically_derived",
        "trace_start_ball_contains_one",
        "gaussian_cell_reduction_lemma_verified",
    ):
        require(canonical[key] is True, f"canonical prerequisite false: {key}")
    require(
        canonical["isometry_accounting"]["canonical_exact_cell_factor"]
        == "1",
        "canonical isometry factor is not one",
    )
    require(
        canonical["isometry_accounting"]["generic_polar_retraction_used"]
        is False,
        "generic polar retraction was used",
    )
    require(
        canonical["isometry_accounting"]["inherited_polar_correction"]
        == "none",
        "a polar correction was inherited",
    )
    require(
        canonical["anchor_certificate"]["below_1e_minus_10"] is True,
        "anchor ceiling prerequisite failed",
    )
    require(
        canonical["R0_norm_certificate"]["pass"] is True,
        "R0 certificate prerequisite failed",
    )

    for payload, label in ((exact, "exact"), (canonical, "canonical")):
        require(payload["alpha_computed"] is False, f"{label} alpha flag true")
        require(
            payload["proof_authorized"] is False,
            f"{label} proof flag true",
        )
        require(
            payload["no_coupling_or_alpha_target_access_attestation"] is True,
            f"{label} no-target attestation absent",
        )

    return {
        "exact_bridge_verdict": exact["verdict"],
        "canonical_transfer_verdict": canonical["verdict"],
        "canonical_anchor_defect_norm_two_upper":
            canonical["anchor_certificate"]["defect_norm_two_upper"],
        "canonical_R0_positive_congruence_margin":
            canonical["R0_norm_certificate"]["positive_congruence"][
                "minimum_lower_margin"
            ],
        "canonical_isometry_accounting":
            canonical["isometry_accounting"],
    }


def compute_certificate(flint) -> dict[str, object]:
    arb = flint.arb
    one = arb(1)
    rho = one / arb(500)
    r = arb(203) / arb(250)
    x_radius = one / arb(20)
    delta0 = one / arb(10**10)
    sqrt5 = arb(5).sqrt()

    free_lipschitz = (
        arb(2)
        / arb(3)
        * (
            one
            + arb(2)
            * rho
            / arb(3)
            * (rho / arb(3)).exp()
        )
    )
    delta_free = free_lipschitz * rho
    epsilon = arb(3) * ((arb(2) * delta_free).exp() - one)
    eta_upper = epsilon.upper() + delta0

    d_lower = (
        one - eta_upper * (one + x_radius)
    ).lower()
    n_upper = (
        eta_upper + (r + eta_upper) * x_radius
    ).upper()
    graph_map_upper = (n_upper / d_lower).upper()
    graph_lipschitz_upper = (
        (r + eta_upper) / d_lower
        + eta_upper * n_upper / (d_lower * d_lower)
    ).upper()

    projector_delta_upper = (
        (
            arb(2) * x_radius
            + arb(2) * x_radius * x_radius
        )
        / (one - x_radius * x_radius)
    ).upper()
    coefficient_lower = (
        one - sqrt5 * projector_delta_upper
    ).lower()
    stable_bound_upper = (
        r + eta_upper + eta_upper * x_radius
    ).upper()
    similarity_upper = (
        (one + x_radius) / (one - x_radius)
    ).upper()

    finite_bounds = {}
    for volume in range(1, FINITE_CUTOFF + 1):
        finite_bounds[str(volume)] = (
            sqrt5
            * arb(volume)
            * eta_upper
            * (one + eta_upper) ** (volume - 1)
        ).upper()

    ratio_upper = (stable_bound_upper / d_lower).upper()
    prefactor_upper = (
        sqrt5 * similarity_upper / coefficient_lower
    ).upper()
    dominance_upper = (
        prefactor_upper * ratio_upper ** DOMINANCE_START
    ).upper()

    graph_denominator_positive_pass = bool(d_lower > 0)
    graph_self_map_pass = bool(graph_map_upper < x_radius)
    graph_contraction_pass = bool(graph_lipschitz_upper < 1)
    graph_pass = bool(
        graph_denominator_positive_pass
        and graph_self_map_pass
        and graph_contraction_pass
    )
    coefficient_pass = bool(coefficient_lower > 0)
    finite_passes = {
        key: bool(bound < 1)
        for key, bound in finite_bounds.items()
    }
    finite_pass = bool(all(finite_passes.values()))
    large_volume_ratio_pass = bool(ratio_upper < 1)
    large_volume_dominance_at_N7_pass = bool(dominance_upper < 1)
    dominance_pass = bool(
        large_volume_ratio_pass
        and large_volume_dominance_at_N7_pass
    )
    thermodynamic_log_consequence_pass = bool(
        graph_pass
        and coefficient_pass
        and finite_pass
        and dominance_pass
    )

    return {
        "disk_radius": str(rho),
        "R0_norm_ceiling": str(r),
        "graph_radius": str(x_radius),
        "anchor_allowance": str(delta0),
        "free_Lipschitz": str(free_lipschitz),
        "free_delta": str(delta_free),
        "transfer_perturbation_epsilon": str(epsilon),
        "total_perturbation_eta_upper": str(eta_upper),
        "graph_denominator_d_lower": str(d_lower),
        "graph_numerator_n_upper": str(n_upper),
        "graph_map_upper": str(graph_map_upper),
        "graph_Lipschitz_upper": str(graph_lipschitz_upper),
        "projector_delta_upper": str(projector_delta_upper),
        "leading_coefficient_lower": str(coefficient_lower),
        "stable_block_bound_upper": str(stable_bound_upper),
        "similarity_condition_upper": str(similarity_upper),
        "finite_volume_nonzero_bounds": {
            key: str(value)
            for key, value in finite_bounds.items()
        },
        "large_volume_ratio_upper": str(ratio_upper),
        "large_volume_prefactor_upper": str(prefactor_upper),
        "dominance_bound_at_N7_upper": str(dominance_upper),
        "graph_denominator_positive_pass":
            graph_denominator_positive_pass,
        "graph_self_map_pass": graph_self_map_pass,
        "graph_contraction_pass": graph_contraction_pass,
        "graph_pass": graph_pass,
        "coefficient_pass": coefficient_pass,
        "finite_volume_nonzero_passes": finite_passes,
        "finite_volume_pass": finite_pass,
        "large_volume_ratio_pass": large_volume_ratio_pass,
        "large_volume_dominance_at_N7_pass":
            large_volume_dominance_at_N7_pass,
        "large_volume_dominance_pass": dominance_pass,
        "thermodynamic_log_consequence_pass":
            thermodynamic_log_consequence_pass,
        "pass": thermodynamic_log_consequence_pass,
    }


def main() -> None:
    started = time.time()
    require(sys.flags.isolated == 1, "execute with python3 -I")
    require(sys.flags.no_site == 1, "execute with python3 -S")
    require(sys.flags.no_user_site == 1, "user site must be disabled")
    require(
        sys.flags.ignore_environment == 1,
        "environment variables must be ignored",
    )

    authorities = verify_authorities()
    wheel_record = verify_wheel_record()
    prerequisites = verify_prerequisites()
    flint = load_flint()
    certificate = compute_certificate(flint)
    runtime_origins = audit_flint_origins()
    passed = bool(certificate["pass"])

    result = {
        "schema": "complete_qspec_canonical_full_zero_free_promotion_v001",
        "authorities": authorities,
        "script_sha256": sha256(SCRIPT),
        "python_isolated_mode": bool(sys.flags.isolated),
        "python_no_site_mode": bool(sys.flags.no_site),
        "python_ignore_environment": bool(sys.flags.ignore_environment),
        "python_flint_version": flint.__version__,
        "arb_precision_bits": PRECISION_BITS,
        "verified_wheel_hashed_files":
            wheel_record["verified_hashed_files"],
        "verified_wheel_native_files":
            wheel_record["verified_native_files"],
        "final_flint_runtime_origins": runtime_origins,
        "prerequisites": prerequisites,
        "analytic_certificate": certificate,
        "verdict": (
            "CANONICAL_FULL_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED"
            if passed
            else "CANONICAL_FULL_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_BLOCKED"
        ),
        "pass": passed,
        "canonical_full_periodic_zero_free_neighborhood_proved":
            passed,
        "full_completed_record_amplitude_zero_free_for_all_volumes":
            passed,
        "canonical_full_periodic_thermodynamic_log_density_proved":
            passed,
        "full_completed_record_amplitude_thermodynamic_log_density_proved":
            passed,
        "frozen_periodic_local_source_polydisc_proved": False,
        "physical_continuum_local_source_addressability_derived": False,
        "periodic_connected_linked_cluster_density_proved": False,
        "connected_cumulant_absolute_majorant_proved": False,
        "all_stage8_regulators_zero_free_proved": False,
        "all_connected_cellulations_linked_cluster_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_coupling_or_alpha_target_access_attestation": True,
        "elapsed_seconds": time.time() - started,
    }

    atomic_write_result(result)
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "graph_map_upper": certificate["graph_map_upper"],
                "graph_Lipschitz_upper":
                    certificate["graph_Lipschitz_upper"],
                "finite_N6":
                    certificate["finite_volume_nonzero_bounds"]["6"],
                "dominance_N7":
                    certificate["dominance_bound_at_N7_upper"],
                "full_completed_record_amplitude_zero_free_for_all_volumes":
                    result[
                        "full_completed_record_amplitude_zero_free_for_all_volumes"
                    ],
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
    atomic_write_result(blocked_payload("execution_started_no_pass"))
    try:
        main()
    except Exception as error:
        atomic_write_result(
            blocked_payload(
                f"{type(error).__name__}: {error}"
            )
        )
        raise
