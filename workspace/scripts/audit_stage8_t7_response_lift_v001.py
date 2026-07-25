#!/usr/bin/env python3
"""Audit whether the sealed Stage-8 lineage fixes a connected scalar amplitude."""

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
AUDIT_DIR = EXEC / "t7_response_lift"

AUTHORITIES = {
    "primitive_amplitude": ROOT
    / "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
    "monoidal_extensivity": ROOT / "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md",
    "composition": ROOT / "BID_GLOBAL_CAR_RECORD_COMPOSITION_DERIVATION_V001.md",
    "finite_parent": ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
    "outgoing_gns": ROOT / "R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md",
    "stage7_candidate": ROOT / "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md",
    "stage8_spec": ROOT
    / "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md",
}

REQUIRED_DISCLOSURES = {
    "primitive_amplitude": (
        "volume_uniform_zero_free_neighborhood_proved = false",
        "connected_many_record_amplitude_derived = false",
        "complete_Q_spec_amplitude_derived = false",
    ),
    "monoidal_extensivity": (
        "connected_linked_cluster_density_proved = false",
        "primitive_record_stiffness_computed = false",
    ),
    "composition": (
        "complete_connected_source_record_action_derived = false",
        "connected_preparation_derived = false",
    ),
    "finite_parent": (
        "complete_parent_to_outgoing_GNS_map_derived = false",
        "complete_parameter_free_Q_spec_frozen = false",
    ),
    "outgoing_gns": (
        "complete_source_inclusive_GNS_derived = false",
        "coupling_evaluation_authorized = false",
    ),
    "stage7_candidate": (
        "A normalized interacting CTP amplitude and its gauge/ghost/edge functional",
        "normalized interacting CTP amplitude;",
        "complete_parameter_free_Q_spec_frozen = false",
    ),
    "stage8_spec": (
        "prove a volume-uniform",
        "linked-cluster thermodynamic density on connected cellulations",
        "verify the Duhamel covariance computed",
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


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


def authority_audit() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for label, path in AUTHORITIES.items():
        text = path.read_text()
        disclosures = REQUIRED_DISCLOSURES[label]
        rows.append(
            {
                "label": label,
                "path": str(path),
                "sha256": sha256_file(path),
                "required_disclosures": list(disclosures),
                "all_required_disclosures_present": all(
                    disclosure in text for disclosure in disclosures
                ),
            }
        )
    return {
        "all_authorities_present": all(path.is_file() for path in AUTHORITIES.values()),
        "all_disclosures_verified": all(
            row["all_required_disclosures_present"] for row in rows
        ),
        "rows": rows,
    }


def scalar_closure_counterexample() -> dict[str, object]:
    # A completed-record compression of a shared-source parent is still a
    # source operator. Use a two-level source and a one-parameter unitary
    # T(theta)=diag(exp(i theta),exp(-i theta)). Fix rho=I/2.
    #
    # In-out/Loschmidt scalarization:
    #   Z_L(theta)=Tr(rho T(theta))=cos(theta),
    #   [-log |Z_L|]''_(theta=0)=1.
    #
    # Inclusive equal-branch CTP scalarization:
    #   Z_CTP(theta)=Tr(T(theta) rho T(theta)^dagger)=1,
    #   [-log |Z_CTP|]''_(theta=0)=0.
    #
    # Both are normalized at zero and zero-free near zero. They differ only
    # in the undeclared source/final-boundary closure.
    hessian_loschmidt = Fraction(1)
    hessian_equal_branch_ctp = Fraction(0)
    return {
        "shared_source_dimension": 2,
        "fixed_initial_source_state": "rho=I_2/2",
        "completed_record_compression_type": "End(H_source), not C",
        "source_operator_family": "T(theta)=diag(exp(i*theta),exp(-i*theta))",
        "closures": [
            {
                "name": "in_out_loschmidt",
                "definition": "Z_L(theta)=Tr(rho*T(theta))=cos(theta)",
                "normalized_at_zero": True,
                "locally_zero_free": True,
                "gamma_hessian_at_zero": str(hessian_loschmidt),
            },
            {
                "name": "inclusive_equal_branch_ctp",
                "definition": (
                    "Z_CTP(theta)=Tr(T(theta)*rho*T(theta)^dagger)=1"
                ),
                "normalized_at_zero": True,
                "locally_zero_free": True,
                "gamma_hessian_at_zero": str(hessian_equal_branch_ctp),
            },
        ],
        "hessians_differ": hessian_loschmidt != hessian_equal_branch_ctp,
        "target_value_used": False,
    }


def render_markdown(result: dict[str, object]) -> str:
    authority = result["authority_audit"]
    example = result["scalar_closure_counterexample"]
    rows = "\n".join(
        f"- `{row['label']}`: `{row['sha256']}`; disclosures verified = "
        f"`{str(row['all_required_disclosures_present']).lower()}`"
        for row in authority["rows"]
    )
    return f"""# Stage-8 T7 Parent-to-Primitive Response-Lift Audit v001

## Verdict

```text
{result['verdict']}
```

T7 cannot currently pass. The finite connected parent and outgoing record
GNS are derived, but the sealed lineage does not derive the scalar,
normalized connected amplitude required for the response Hessian.

## Type obstruction

Projecting a connected source-record evolution onto completed record
alternatives leaves an element of `End(H_source)`. It does not produce a
complex scalar. A further source/final-boundary closure is required.

The existing authority explicitly leaves the normalized interacting CTP
amplitude, connected many-record amplitude, volume-uniform zero-free
neighborhood, connected linked-cluster density, and complete
parent-to-outgoing map open.

## Constructive non-uniqueness witness

For one fixed two-level source state `rho=I_2/2` and
`T(theta)=diag(exp(i theta),exp(-i theta))`, two standard normalized closures
of the same source operator are:

```text
Z_L(theta)   = Tr(rho T(theta))                   = cos(theta)
Z_CTP(theta) = Tr(T(theta) rho T(theta)^dagger)  = 1
```

Both equal one at `theta=0` and are zero-free in a neighborhood of zero, but

```text
[-log|Z_L|]''(0)   = {example['closures'][0]['gamma_hessian_at_zero']}
[-log|Z_CTP|]''(0) = {example['closures'][1]['gamma_hessian_at_zero']}.
```

Thus completed-record semantics and the finite parent alone do not select
the response Hessian. Choosing one closure during Stage-8 execution would
be a new theory choice, not a computation from the sealed battery.

## Closure condition

Before T7 can be rerun, derive and forward-seal a parent-to-primitive
response lift that fixes, without a coupling target:

1. the source/final-boundary functional or CTP branch prescription;
2. the completed-record effect and its normalization;
3. the map from the F1 connection tangent into the connected parent;
4. a volume-uniform zero-free neighborhood;
5. a local linked-cluster density; and
6. equality of its intensive Hessian with the declared Duhamel covariance.

The lift must reduce to the pinned one-handle completed-record amplitude.

## Authority custody

{rows}

## Protected status

```text
kappa_record_computed = false
physical_charged_amplitude_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
"""


def update_artifact_manifest(paths: list[Path]) -> None:
    manifest = EXEC / "artifact_manifest.txt"
    existing = {
        line.strip() for line in manifest.read_text().splitlines() if line.strip()
    }
    existing.update(str(path) for path in paths)
    manifest.write_text("\n".join(sorted(existing)) + "\n")


def run() -> dict[str, object]:
    WORK.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)

    authority = authority_audit()
    example = scalar_closure_counterexample()
    blocked = bool(
        authority["all_authorities_present"]
        and authority["all_disclosures_verified"]
        and example["hessians_differ"]
    )
    result = {
        "schema": "stage8-t7-response-lift-audit-v001",
        "verdict": (
            "T7_BLOCKED_PARENT_TO_PRIMITIVE_RESPONSE_LIFT_UNDERIVED"
            if blocked
            else "AUDIT_MALFORMED"
        ),
        "t7_pass": False,
        "authority_audit": authority,
        "scalar_closure_counterexample": example,
        "missing_derived_map": (
            "connected completed-record/source operator -> unique normalized "
            "complex scalar amplitude"
        ),
        "new_principle_adopted": False,
        "target_value_used": False,
        "protected_flags": {
            "kappa_record_computed": False,
            "physical_charged_amplitude_computed": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }

    json_path = WORK / "T07_response_lift_underdetermination.json"
    md_path = ROOT / "STAGE8_T7_PARENT_TO_PRIMITIVE_RESPONSE_LIFT_AUDIT_V001.md"
    write_content_addressed(json_path, result)
    md_path.write_text(render_markdown(result))

    seal_path = AUDIT_DIR / "T07_RESPONSE_LIFT_AUDIT_V001.seal.sha256"
    seal_entries = [
        ROOT / "scripts/audit_stage8_t7_response_lift_v001.py",
        json_path,
        md_path,
    ]
    seal_path.write_text(
        "".join(
            f"{sha256_file(path)}  {path.relative_to(ROOT)}\n"
            for path in seal_entries
        )
    )
    update_artifact_manifest([*seal_entries, seal_path])
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()
