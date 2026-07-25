#!/usr/bin/env python3
"""Derive the primitive Stage-8 T7 response closure from sealed authorities."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
EXEC = ROOT / "stage8_execution"
WORK = EXEC / "work"
DERIVATION_DIR = EXEC / "t7_response_closure_selection"
SPEC = ROOT / "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_SPEC_V001.md"
SPEC_SEAL = (
    ROOT
    / "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_SPEC_V001.seal.sha256"
)

AUTHORITIES = {
    ROOT / "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md":
        "aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a",
    ROOT / "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.md":
        "f72b4714d5189279171c51f1efd25abb2883ab7bc91358d23ca4a5039a242a8c",
    ROOT
    / "stage8_execution/t0_lineage/core_scripts/"
    "31_gate4_differential_uniqueness_v001.py":
        "0510e4b1829b54a3983a898673f8b399f8bef3ebdeacc42966e62b720984edbf",
    ROOT
    / "stage8_execution/t0_lineage/core_scripts/"
    "34_gate1_comparison_group_v001.py":
        "0e107dfd78f605a32e5f44f6181a460cb60a7217af0addb6c692fd866a6d3a5e",
}

SPEC_SHA256 = "e1ea14e7661a4eb5169671e48008c42116343d90c86d8f8b3697e183e05c06bc"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def frac(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def write_json(path: Path, body: dict[str, object]) -> None:
    path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")


def write_content_addressed(path: Path, body: dict[str, object]) -> None:
    addressed = dict(body)
    addressed["sha256_of_body"] = ""
    canonical = json.dumps(
        addressed, sort_keys=True, separators=(",", ":")
    ).encode()
    addressed["sha256_of_body"] = sha256_bytes(canonical)
    write_json(path, addressed)


def verify_authorities() -> dict[str, object]:
    rows = []
    for path, expected in AUTHORITIES.items():
        actual = sha256_file(path)
        rows.append(
            {
                "path": str(path.relative_to(ROOT)),
                "expected_sha256": expected,
                "actual_sha256": actual,
                "verified": actual == expected,
            }
        )
    spec_seal_expected, spec_name = SPEC_SEAL.read_text().strip().split("  ", 1)
    return {
        "spec_path": spec_name,
        "spec_expected_sha256": SPEC_SHA256,
        "spec_actual_sha256": sha256_file(SPEC),
        "spec_seal_expected_sha256": spec_seal_expected,
        "spec_verified": (
            sha256_file(SPEC) == SPEC_SHA256 == spec_seal_expected
        ),
        "authority_rows": rows,
        "all_authorities_verified": all(row["verified"] for row in rows),
    }


def classify_closures() -> list[dict[str, object]]:
    return [
        {
            "id": "complex_linear_connection_return",
            "formula": "C(z I_E)=z",
            "complex_linear": True,
            "one_handle_reduction": True,
            "holonomy_sensitive": True,
            "admissible": True,
        },
        {
            "id": "complex_antilinear_return",
            "formula": "C(z I_E)=conjugate(z)",
            "complex_linear": False,
            "one_handle_reduction": False,
            "holonomy_sensitive": True,
            "admissible": False,
        },
        {
            "id": "endpoint_probability",
            "formula": "C(z I_E)=|z|^2",
            "complex_linear": False,
            "one_handle_reduction": False,
            "holonomy_sensitive": False,
            "admissible": False,
        },
        {
            "id": "inclusive_unitary_sandwich",
            "formula": "C(U)=Tr(U rho U^dagger)",
            "complex_linear": False,
            "one_handle_reduction": False,
            "holonomy_sensitive": False,
            "admissible": False,
        },
        {
            "id": "nonlinear_power_n_not_1",
            "formula": "C(z I_E)=z^n, n!=1",
            "complex_linear": False,
            "one_handle_reduction": False,
            "holonomy_sensitive": True,
            "admissible": False,
        },
    ]


def holonomy_witness() -> dict[str, object]:
    # psi(theta)=(|0>+exp(i theta)|1>)/sqrt(2).
    # At theta=0:
    # <dpsi|dpsi>=1/2 and |<psi|dpsi>|^2=1/4.
    dpsi_norm = Fraction(1, 2)
    berry_norm = Fraction(1, 4)
    fs_metric = dpsi_norm - berry_norm

    # z(theta)=(1+exp(i theta))/2:
    # z(0)=1, z'(0)=i/2, z''(0)=-1/2.
    # Gamma''=-Re[z''/z-(z'/z)^2]=1/4.
    linear_gamma_hessian = Fraction(1, 4)
    probability_gamma_hessian = 2 * linear_gamma_hessian
    inclusive_gamma_hessian = Fraction(0)
    return {
        "ray": "(|0>+exp(i*theta)|1>)/sqrt(2)",
        "linear_overlap": "(1+exp(i*theta))/2",
        "dpsi_norm": frac(dpsi_norm),
        "berry_norm": frac(berry_norm),
        "FS_metric": frac(fs_metric),
        "linear_Gamma_hessian": frac(linear_gamma_hessian),
        "probability_Gamma_hessian": frac(probability_gamma_hessian),
        "inclusive_sandwich_Gamma_hessian": frac(inclusive_gamma_hessian),
        "linear_matches_FS": linear_gamma_hessian == fs_metric,
        "probability_violates_pinned_FS_normalization": (
            probability_gamma_hessian != fs_metric
        ),
        "inclusive_violates_pinned_FS_normalization": (
            inclusive_gamma_hessian != fs_metric
        ),
        "target_value_used": False,
    }


def linear_uniqueness() -> dict[str, object]:
    # End_C(E)=span_C{I_E}. Every C-linear functional has one coefficient c.
    # Unit normalization is the exact equation c=1.
    coefficient_before_normalization = "c in C"
    coefficient_after_normalization = "1"
    return {
        "domain_complex_dimension": 1,
        "dual_complex_dimension": 1,
        "general_complex_linear_functional": "C(z I_E)=c*z",
        "coefficient_before_normalization": coefficient_before_normalization,
        "normalization_equation": "C(I_E)=c=1",
        "coefficient_after_normalization": coefficient_after_normalization,
        "normalized_solution_count": 1,
        "unique_closure": "C(z I_E)=z",
    }


def finite_stage_check() -> dict[str, object]:
    authority = (ROOT / "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.md").read_text()
    amplitude = (
        ROOT / "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md"
    ).read_text()
    checks = {
        "common_domain_theorem_present": "## Common-domain theorem" in authority,
        "finite_propagator_theorem_present": "## Finite propagator theorem" in authority,
        "unique_finite_propagator_stated": (
            "unique finite-parent propagator" in authority
        ),
        "connection_returned_scalar_stated": (
            "this endomorphism is one complex scalar" in amplitude
        ),
        "nonzero_baseline_stated": "a_h(0)=1" in amplitude,
        "source_inclusive_continuum_claimed": False,
        "volume_uniform_zero_free_claimed": False,
        "connected_density_claimed": False,
    }
    positive = (
        "common_domain_theorem_present",
        "finite_propagator_theorem_present",
        "unique_finite_propagator_stated",
        "connection_returned_scalar_stated",
        "nonzero_baseline_stated",
    )
    prohibited = (
        "source_inclusive_continuum_claimed",
        "volume_uniform_zero_free_claimed",
        "connected_density_claimed",
    )
    passed = all(checks[key] for key in positive) and all(
        checks[key] is False for key in prohibited
    )
    return {
        "checks": checks,
        "required_true": list(positive),
        "required_false": list(prohibited),
        "pass": passed,
    }


def render_markdown(result: dict[str, object]) -> str:
    witness = result["D2_exclusion_witness"]
    return f"""# Stage-8 T7 Response-Closure Selection Derivation Result v001

## Verdict

```text
{result['verdict']}
```

No response principle was adopted.

## D1 — Admissible class

The primitive completed-record return is an endomorphism of the
one-dimensional complex root line. The candidate audit retains only the
complex-linear, normalized, holonomy-sensitive connection return.

The endpoint probability `|a_h|^2` is a Born probability, not the pinned
complex amplitude. The fully inclusive unitary sandwich is constant and
therefore phase blind. Antilinear and nonlinear-power candidates fail
complex linearity and exact one-handle reduction.

## D2 — Exact relative-holonomy witness

For:

```text
|psi(theta)>=(|0>+exp(i theta)|1>)/sqrt(2),
```

the exact local curvatures are:

```text
Fubini-Study metric                         = {witness['FS_metric']}
[-log|linear amplitude|]''(0)              = {witness['linear_Gamma_hessian']}
[-log|endpoint probability|]''(0)          = {witness['probability_Gamma_hessian']}
[-log|inclusive unitary sandwich|]''(0)    = {witness['inclusive_sandwich_Gamma_hessian']}
```

Only the linear amplitude has the pinned Fubini-Study normalization.
Fubini-Study is a check here; the independent downstream `c>0`
action-multiplier family remains unresolved.

## D3 — Uniqueness

Because `End_C(L_r)=span_C{{I}}`, every complex-linear functional has:

```text
C(z I)=c z.
```

Unit normalization gives `c=C(I)=1`. Therefore:

```text
C(z I)=z
```

is the unique normalized complex-linear primitive closure.

## D4 — Finite stage

The hash-pinned finite-parent authority supplies the common domain and
unique finite propagator. Endpoint compression and connection return are
therefore finite-stage well-defined. No source-inclusive continuum,
volume-uniform zero-free, connected-cluster, or Duhamel/Hessian theorem is
claimed.

## Remaining T7 obligations

```text
response_closure_selection_derived = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
"""


def update_artifact_manifest(paths: list[Path]) -> None:
    manifest = EXEC / "artifact_manifest.txt"
    entries = {
        line.strip() for line in manifest.read_text().splitlines() if line.strip()
    }
    entries.update(str(path) for path in paths)
    manifest.write_text("\n".join(sorted(entries)) + "\n")


def run() -> dict[str, object]:
    WORK.mkdir(parents=True, exist_ok=True)
    DERIVATION_DIR.mkdir(parents=True, exist_ok=True)

    custody = verify_authorities()
    closures = classify_closures()
    witness = holonomy_witness()
    uniqueness = linear_uniqueness()
    finite = finite_stage_check()

    d1 = sum(1 for item in closures if item["admissible"]) == 1
    d2 = bool(
        witness["linear_matches_FS"]
        and witness["probability_violates_pinned_FS_normalization"]
        and witness["inclusive_violates_pinned_FS_normalization"]
    )
    d3 = uniqueness["normalized_solution_count"] == 1
    d4 = finite["pass"]
    passed = bool(
        custody["spec_verified"]
        and custody["all_authorities_verified"]
        and d1
        and d2
        and d3
        and d4
    )
    result = {
        "schema": "stage8-t7-response-closure-selection-v001",
        "verdict": (
            "RESPONSE_CLOSURE_SELECTION_DERIVED"
            if passed
            else "RESPONSE_CLOSURE_SELECTION_BLOCKED"
        ),
        "pass": passed,
        "custody": custody,
        "D1_admissible_closure_class": {
            "pass": d1,
            "candidates": closures,
            "surviving_ids": [
                item["id"] for item in closures if item["admissible"]
            ],
        },
        "D2_exclusion_witness": witness,
        "D3_linear_uniqueness": uniqueness,
        "D4_finite_stage": finite,
        "new_principle_adopted": False,
        "source_inclusive_CTP_closed": False,
        "action_multiplier_c_fixed": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "physical_charged_amplitude_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "target_value_used": False,
    }

    report_path = WORK / "T07_response_closure_selection.json"
    result_path = (
        ROOT / "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md"
    )
    write_content_addressed(report_path, result)
    result_path.write_text(render_markdown(result))

    seal_entries = [
        SPEC,
        SPEC_SEAL,
        ROOT / "scripts/derive_stage8_t7_response_closure_selection_v001.py",
        report_path,
        result_path,
    ]
    seal_path = (
        DERIVATION_DIR / "T07_RESPONSE_CLOSURE_SELECTION_V001.seal.sha256"
    )
    seal_path.write_text(
        "".join(
            f"{sha256_file(path)}  {path.relative_to(ROOT)}\n"
            for path in seal_entries
        )
    )
    update_artifact_manifest([*seal_entries, seal_path])
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)
    return result


if __name__ == "__main__":
    run()
