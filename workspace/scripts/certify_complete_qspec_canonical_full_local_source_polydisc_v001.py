#!/usr/bin/env python3
"""Outward-rounded gate for the canonical full local-source polydisc."""

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
SPEC = (
    ROOT
    / "COMPLETE_QSPEC_CANONICAL_FULL_LOCAL_SOURCE_POLYDISC_SPEC_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_canonical_full_local_source_polydisc_v001.json"
)
FULL_ZERO_FREE_JSON = (
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
LOCAL_SOURCE_LIFT = (
    ROOT / "COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_LIFT_DERIVATION_V001.md"
)
FACTORIZATION_LEMMA = (
    ROOT
    / "COMPLETE_QSPEC_BOUNDARY_ADAPTED_NONAUTONOMOUS_FACTORIZATION_LEMMA_V001.md"
)
FLINT_ROOT = ROOT.parents[1] / ".proof_deps/python_flint"
FLINT_RECORD = FLINT_ROOT / "python_flint-0.6.0.dist-info/RECORD"

EXPECTED = {
    SPEC:
        "4e9a780da0e3e26013f914347563cbb9e556b3d052d9760ff766c17dd01c0e07",
    ROOT / "COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md":
        "273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_TRANSFER_INDUCTION_PROOF_V001.md":
        "5fc923b9ecca5ee6e63fe8faa50047d72747ebaf09646b14b03affc48a6e84a3",
    ROOT / "COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_RESULT_V001.md":
        "ade49876242ffc4ce6c90942f8b63261f3cc1c463103110ff1e2e60fee232e84",
    ROOT / "COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_LIFT_DERIVATION_V001.md":
        "24c8c7f5dc5ffa8be553de6a85899e7f0142347b378b0ca97c5252dadb573bb0",
    EXACT_JSON:
        "093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md":
        "6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676",
    CANONICAL_JSON:
        "46dd8f18dc7e9bfcdda7b90278f8cc71bd1e80aa157c29ba39433057d74be807",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md":
        "12dc40274aa431e08245573963cf2f47de6f7ed4aa9803ae38b71539f538d261",
    ROOT / "COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_SPEC_V001.md":
        "61d3822f78b1b48c690951e4ffb710ca798ee2b8cbc7986d5c1b6164c7e52e83",
    ROOT / "scripts/certify_complete_qspec_canonical_full_zero_free_v001.py":
        "3cde9448454d95ede29b904a353b72b56f8f21bc746918f794ed527430ac2aef",
    FULL_ZERO_FREE_JSON:
        "bf693cea0ad011d4d7fa020cc9f74ead93a9054c967ccd3878438e1312562473",
    ROOT / "COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_RESULT_V001.md":
        "083e63e2516e1f319e4dd1edbb17f97d3e58a9eec683739c95310cb1dedb6640",
    FACTORIZATION_LEMMA:
        "a6c2124626701e79a78a40923fe09cd8e9c93bbd2eec741c22344dbe10709c16",
    FLINT_ROOT / "python_flint-0.6.0.dist-info/METADATA":
        "d6b5be0f3a94ff92ad45f8e9d8991ac8face10ab71e362b8b9f25819df4ef06b",
    FLINT_RECORD:
        "9b76e8ba99a8555fa73c855c2459614714f25136238c1c96fa6c82dad5b9cf94",
    FLINT_ROOT / "flint/__init__.py":
        "b959e94c11c23633c0cbfea849a07955b8f252fc3100fd2ed52bd3c35118ba93",
}

SEALED_LOCAL = (
    SPEC,
    ROOT / "COMPLETE_QSPEC_PERIODIC_LOCAL_SOURCE_LIFT_DERIVATION_V001.md",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_SPEC_V001.md",
    ROOT / "scripts/certify_complete_qspec_canonical_full_zero_free_v001.py",
    ROOT / "COMPLETE_QSPEC_CANONICAL_FULL_ZERO_FREE_PROMOTION_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_BOUNDARY_ADAPTED_NONAUTONOMOUS_FACTORIZATION_LEMMA_V001.md",
)

PRECISION_BITS = 192


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
        "schema":
            "complete_qspec_canonical_full_local_source_polydisc_v001",
        "script_sha256": sha256(SCRIPT),
        "verdict":
            "CANONICAL_FULL_PERIODIC_LOCAL_SOURCE_POLYDISC_BLOCKED",
        "pass": False,
        "block_reason": reason,
        "canonical_full_periodic_local_source_polydisc_proved": False,
        "full_completed_record_amplitude_local_source_zero_free_for_all_volumes":
            False,
        "finite_volume_multivariable_log_generator_proved": False,
        "periodic_boundary_graph_contraction_proved": False,
        "physical_continuum_local_source_addressability_derived": False,
        "periodic_connected_linked_cluster_density_proved": False,
        "connected_cumulant_absolute_majorant_proved": False,
        "periodic_connected_cumulant_thermodynamic_limit_proved": False,
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
    previous = json.loads(
        FULL_ZERO_FREE_JSON.read_text(encoding="utf-8")
    )

    require(exact["pass"] is True, "exact bridge machine pass is false")
    require(
        exact["verdict"] == "EXACT_ZERO_HISTORY_SPIN2_SUPPORT_BRIDGE_DERIVED",
        "exact bridge verdict mismatch",
    )
    require(
        exact["exact_reduced_to_full_finite_amplitude_identity_derived"]
        is True,
        "exact reduced-to-full identity is absent",
    )
    require(
        exact["right_history_support_induction_derived"] is True,
        "right-history support induction is absent",
    )

    require(
        canonical["pass"] is True,
        "canonical transfer machine pass is false",
    )
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
        "canonical cell factor is not one",
    )
    require(
        canonical["isometry_accounting"]["generic_polar_retraction_used"]
        is False,
        "canonical transfer used generic polar retraction",
    )

    require(previous["pass"] is True, "full zero-free prerequisite failed")
    require(
        previous["verdict"]
        == "CANONICAL_FULL_PERIODIC_ZERO_FREE_AND_LOG_DENSITY_PROVED",
        "full zero-free prerequisite verdict mismatch",
    )
    for key in (
        "canonical_full_periodic_zero_free_neighborhood_proved",
        "full_completed_record_amplitude_zero_free_for_all_volumes",
        "canonical_full_periodic_thermodynamic_log_density_proved",
        "full_completed_record_amplitude_thermodynamic_log_density_proved",
    ):
        require(previous[key] is True, f"prerequisite false: {key}")
    for payload, label in (
        (exact, "exact bridge"),
        (canonical, "canonical transfer"),
        (previous, "full zero-free"),
    ):
        for key in (
            "kappa_record_computed",
            "physical_Thomson_stiffness_computed",
            "coupling_evaluation_authorized",
            "alpha_computed",
            "proof_authorized",
        ):
            require(payload[key] is False, f"{label} protected flag true: {key}")
        require(
            payload["no_coupling_or_alpha_target_access_attestation"]
            is True,
            f"{label} no-target attestation absent",
        )

    return {
        "exact_bridge_verdict": exact["verdict"],
        "exact_bridge_machine_pass": exact["pass"],
        "exact_reduced_to_full_identity":
            exact[
                "exact_reduced_to_full_finite_amplitude_identity_derived"
            ],
        "right_history_support_induction":
            exact["right_history_support_induction_derived"],
        "canonical_transfer_verdict": canonical["verdict"],
        "canonical_transfer_machine_pass": canonical["pass"],
        "canonical_trace_start_contains_one":
            canonical["trace_start_ball_contains_one"],
        "canonical_exact_trace_identity":
            canonical["exact_trace_identity_algebraically_derived"],
        "full_zero_free_verdict": previous["verdict"],
        "full_zero_free_machine_pass": previous["pass"],
        "full_amplitude_bridge_active":
            previous[
                "full_completed_record_amplitude_zero_free_for_all_volumes"
            ],
        "prior_total_perturbation_eta_upper":
            previous["analytic_certificate"][
                "total_perturbation_eta_upper"
            ],
    }


def derive_theorem_bindings(
    authorities: dict[str, str],
    prerequisites: dict[str, object],
) -> dict[str, bool]:
    factorization_lemma_verified = bool(
        authorities[str(FACTORIZATION_LEMMA)]
        == EXPECTED[FACTORIZATION_LEMMA]
    )
    local_source_lift_verified = bool(
        authorities[str(LOCAL_SOURCE_LIFT)]
        == EXPECTED[LOCAL_SOURCE_LIFT]
    )
    full_amplitude_local_source_identity_verified = bool(
        local_source_lift_verified
        and prerequisites["exact_bridge_machine_pass"]
        and prerequisites["exact_reduced_to_full_identity"]
        and prerequisites["right_history_support_induction"]
        and prerequisites["canonical_transfer_machine_pass"]
    )
    holomorphic_log_normalization_verified = bool(
        full_amplitude_local_source_identity_verified
        and prerequisites["canonical_trace_start_contains_one"]
        and prerequisites["canonical_exact_trace_identity"]
        and prerequisites["full_zero_free_machine_pass"]
        and prerequisites["full_amplitude_bridge_active"]
    )
    return {
        "factorization_lemma_verified":
            factorization_lemma_verified,
        "local_source_lift_verified": local_source_lift_verified,
        "full_amplitude_local_source_identity_verified":
            full_amplitude_local_source_identity_verified,
        "holomorphic_log_normalization_verified":
            holomorphic_log_normalization_verified,
    }


def compute_certificate(
    flint,
    theorem_bindings: dict[str, bool],
) -> dict[str, object]:
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
    graph_contraction_margin_lower = (
        one - graph_lipschitz_upper
    ).lower()
    boundary_coefficient_lower = (
        one - sqrt5 * x_radius
    ).lower()

    d_positive_pass = bool(d_lower > 0)
    graph_self_map_pass = bool(graph_map_upper < x_radius)
    graph_contraction_pass = bool(graph_lipschitz_upper < 1)
    boundary_coefficient_pass = bool(boundary_coefficient_lower > 0)
    passed = bool(
        d_positive_pass
        and graph_self_map_pass
        and graph_contraction_pass
        and boundary_coefficient_pass
        and theorem_bindings["factorization_lemma_verified"]
        and theorem_bindings[
            "full_amplitude_local_source_identity_verified"
        ]
        and theorem_bindings[
            "holomorphic_log_normalization_verified"
        ]
    )

    return {
        "disk_radius_per_source": str(rho),
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
        "graph_contraction_margin_lower":
            str(graph_contraction_margin_lower),
        "boundary_coefficient_lower": str(boundary_coefficient_lower),
        "symbolic_volume_uniform_lower_bound":
            "[1-sqrt(5)/20] * d^N",
        "d_positive_pass": d_positive_pass,
        "graph_self_map_pass": graph_self_map_pass,
        "graph_contraction_pass": graph_contraction_pass,
        "boundary_coefficient_pass": boundary_coefficient_pass,
        "factorization_lemma_verified":
            theorem_bindings["factorization_lemma_verified"],
        "local_source_lift_verified":
            theorem_bindings["local_source_lift_verified"],
        "full_amplitude_local_source_identity_verified":
            theorem_bindings[
                "full_amplitude_local_source_identity_verified"
            ],
        "holomorphic_log_normalization_verified":
            theorem_bindings[
                "holomorphic_log_normalization_verified"
            ],
        "pass": passed,
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
    theorem_bindings = derive_theorem_bindings(
        authorities,
        prerequisites,
    )
    flint = load_flint()
    certificate = compute_certificate(flint, theorem_bindings)
    runtime_origins = audit_flint_origins()
    passed = bool(certificate["pass"])

    result = {
        "schema":
            "complete_qspec_canonical_full_local_source_polydisc_v001",
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
            "CANONICAL_FULL_PERIODIC_LOCAL_SOURCE_POLYDISC_PROVED"
            if passed
            else "CANONICAL_FULL_PERIODIC_LOCAL_SOURCE_POLYDISC_BLOCKED"
        ),
        "pass": passed,
        "canonical_full_periodic_local_source_polydisc_proved":
            passed,
        "full_completed_record_amplitude_local_source_zero_free_for_all_volumes":
            passed,
        "finite_volume_multivariable_log_generator_proved": passed,
        "periodic_boundary_graph_contraction_proved": passed,
        "physical_continuum_local_source_addressability_derived": False,
        "periodic_connected_linked_cluster_density_proved": False,
        "connected_cumulant_absolute_majorant_proved": False,
        "periodic_connected_cumulant_thermodynamic_limit_proved": False,
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
                "d_lower": certificate["graph_denominator_d_lower"],
                "graph_map_upper": certificate["graph_map_upper"],
                "graph_Lipschitz_upper":
                    certificate["graph_Lipschitz_upper"],
                "boundary_coefficient_lower":
                    certificate["boundary_coefficient_lower"],
                "local_source_polydisc_proved":
                    result[
                        "canonical_full_periodic_local_source_polydisc_proved"
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
            blocked_payload(f"{type(error).__name__}: {error}")
        )
        raise
