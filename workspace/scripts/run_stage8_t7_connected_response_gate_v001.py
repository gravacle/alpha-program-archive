#!/usr/bin/env python3
"""Execute the sealed Stage-8 T7 connected primitive-response gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
EXEC = ROOT / "stage8_execution"
REPORTS = EXEC / "t_reports"
WORK = EXEC / "work"
GATE_DIR = EXEC / "t7_connected_response"

AUTHORITIES = {
    "primitive_amplitude": ROOT
    / "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
    "zero_free_gate": ROOT / "BID_PHYSICAL_RECORD_AMPLITUDE_ZERO_FREE_GATE_V001.md",
    "cell_composition": ROOT
    / "BID_DISTINGUISHABLE_RECORD_CELL_COMPOSITION_DERIVATION_V001.md",
    "monoidal_extensivity": ROOT / "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md",
    "parent_identifiability": ROOT / "BID_MANY_RECORD_PARENT_IDENTIFIABILITY_GATE_V001.md",
    "global_descent": ROOT
    / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
    "finite_parent_successor": ROOT
    / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
    "stage7_successor": ROOT / "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md",
    "stage8_spec": ROOT
    / "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md",
}

REQUIRED_STATEMENTS = {
    "primitive_amplitude": (
        "primitive_complex_transition_amplitude_unique = true",
        "primitive_transition_amplitude_gauge_invariant = true",
        "connected_many_record_amplitude_derived = false",
    ),
    "zero_free_gate": (
        "volume_uniform_zero_free_neighborhood_proved = false",
        "thermodynamic_log_hessian_authorized = false",
    ),
    "cell_composition": (
        "strong_monoidal_Hilb_carrier_for_disjoint_cells_derived = true",
        "connected_cross_cell_terms_derived = false",
        "connected_linked_cluster_density_proved = false",
    ),
    "monoidal_extensivity": (
        "exact_disjoint_monoidal_additivity_proved = true",
        "connected_linked_cluster_density_proved = false",
    ),
    "parent_identifiability": (
        "connected_parent_counterfamily_constructed = true",
        "connected_preparation_derived = false",
        "record_interval_inside_controlled_thermodynamic_domain = false",
    ),
    "global_descent": (
        "global_operator_valued_one_particle_superconnection_constructed = true",
        "connected_preparation_derived = false",
        "time_dependent_continuum_ordering_derived = false",
    ),
    "finite_parent_successor": (
        "finite_causal_source_record_parent_derived = true",
        "complete_parent_to_outgoing_GNS_map_derived = false",
        "complete_parameter_free_Q_spec_frozen = false",
    ),
    "stage7_successor": (
        "stationary quasifree in-state",
        "A normalized interacting CTP amplitude and its gauge/ghost/edge functional measure remain open.",
        "stage8_cross_execution_completed = false",
    ),
    "stage8_spec": (
        "failure is BLOCKED",
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


def matrix_counterfamily() -> dict[str, object]:
    # Basis: |00>, |10>, |01>, |11>. The lambda term is invisible on the
    # vacuum-plus-one-record subspace but changes connected two-record
    # dynamics.
    b0 = (
        (0, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 0),
    )
    b1 = (
        (0, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
    )
    restricted0 = tuple(tuple(row[j] for j in range(3)) for row in b0[:3])
    restricted1 = tuple(tuple(row[j] for j in range(3)) for row in b1[:3])
    return {
        "basis": ["|00>", "|10>", "|01>", "|11>"],
        "B_lambda_definition": (
            "|10><01|+|01><10|+lambda*|11><11|"
        ),
        "lambda_values_tested": [0, 1],
        "vacuum_and_one_record_restrictions_equal": restricted0 == restricted1,
        "two_record_matrix_element_lambda0": b0[3][3],
        "two_record_matrix_element_lambda1": b1[3][3],
        "connected_two_record_dynamics_differ": b0[3][3] != b1[3][3],
        "characteristic_polynomial_lambda0": "x^2*(x-1)*(x+1)",
        "characteristic_polynomial_lambda1": "x*(x-1)^2*(x+1)",
        "target_value_used": False,
    }


def authority_audit() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for label, path in AUTHORITIES.items():
        text = path.read_text()
        normalized_text = " ".join(text.split())
        statements = REQUIRED_STATEMENTS[label]
        rows.append(
            {
                "label": label,
                "path": str(path),
                "sha256": sha256_file(path),
                "required_statements": list(statements),
                "all_required_statements_present": all(
                    " ".join(statement.split()) in normalized_text
                    for statement in statements
                ),
            }
        )
    return {
        "all_files_present": all(path.is_file() for path in AUTHORITIES.values()),
        "all_required_statements_verified": all(
            row["all_required_statements_present"] for row in rows
        ),
        "rows": rows,
    }


def corpus_closure_scan() -> dict[str, object]:
    keys = (
        "connected_linked_cluster_density_proved",
        "volume_uniform_zero_free_neighborhood_proved",
        "thermodynamic_log_hessian_authorized",
    )
    true_hits: list[str] = []
    false_hits: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".json"}:
            continue
        text = path.read_text(errors="replace")
        relative = str(path.relative_to(ROOT))
        for key in keys:
            if f"{key} = true" in text:
                true_hits.append(f"{relative}: {key} = true")
            if f"{key} = false" in text:
                false_hits.append(f"{relative}: {key} = false")
    return {
        "keys": list(keys),
        "true_hit_count": len(true_hits),
        "true_hits": true_hits,
        "false_hit_count": len(false_hits),
        "false_hits": false_hits,
        "no_successor_closure_found": not true_hits and bool(false_hits),
    }


def render_markdown(report: dict[str, object]) -> str:
    counter = report["evidence"]["connected_counterfamily"]
    return f"""# Stage-8 T7 Connected Primitive Response Gate v001

## Verdict

```text
T7_BLOCKED_CONNECTED_PRIMITIVE_RESPONSE_NOT_DERIVED
```

The pinned one-cell completed-record amplitude is derived, gauge invariant,
and nonzero at its baseline. Exact disjoint tensor composition and additive
`-log|A|` are also derived.

The mandatory connected step is not derived. The authority explicitly
retains:

```text
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
connected_preparation_derived = false
record_interval_inside_controlled_thermodynamic_domain = false
```

Consequently no intensive connected Hessian exists yet against which the
local Duhamel covariance can be checked.

## Exact underdetermination witness

On the basis `|00>,|10>,|01>,|11>`, the target-free family

```text
B_lambda=|10><01|+|01><10|+lambda |11><11|
```

has the same vacuum and one-record restriction for `lambda=0` and
`lambda=1`, but its two-record matrix element changes from
`{counter['two_record_matrix_element_lambda0']}` to
`{counter['two_record_matrix_element_lambda1']}`. The respective
characteristic polynomials are:

```text
{counter['characteristic_polynomial_lambda0']}
{counter['characteristic_polynomial_lambda1']}
```

Thus the one-cell amplitude, locality, target independence, and disjoint
composition do not select connected many-record dynamics. The later adopted
global-boundary-descent principle fixes a finite stationary primitive
operator, but its own status still leaves connected preparation,
time-dependent continuum ordering, and the thermodynamic domain open.

## T7 sub-obligations

```text
T7(i)  primitive completed-record amplitude       PASS
T7(ii) volume-uniform zero-free neighborhood      BLOCKED
T7(iii) disjoint monoidality                       PASS
T7(iii) connected linked-cluster density          BLOCKED
T7(iv) Duhamel/intensive-Hessian equality          NOT EXECUTABLE
```

The Stage-8 boundary rule makes this `BLOCKED`, not `CONDITIONAL`.

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
    entries = {
        line.strip() for line in manifest.read_text().splitlines() if line.strip()
    }
    entries.update(str(path) for path in paths)
    manifest.write_text("\n".join(sorted(entries)) + "\n")


def run() -> dict[str, object]:
    REPORTS.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    GATE_DIR.mkdir(parents=True, exist_ok=True)

    authority = authority_audit()
    counterfamily = matrix_counterfamily()
    closure_scan = corpus_closure_scan()
    evidence_complete = bool(
        authority["all_files_present"]
        and authority["all_required_statements_verified"]
        and counterfamily["vacuum_and_one_record_restrictions_equal"]
        and counterfamily["connected_two_record_dynamics_differ"]
        and closure_scan["no_successor_closure_found"]
    )
    report = {
        "schema": "stage8-obligation-report-v001",
        "obligation": "T07",
        "pass": False,
        "failure_class": (
            "MANDATORY_ZERO_FREE_AND_CONNECTED_DENSITY_NOT_DERIVED"
            if evidence_complete
            else "AUDIT_MALFORMED"
        ),
        "open_item": None,
        "evidence": {
            "T7_i_primitive_completed_record_amplitude": "PASS",
            "T7_ii_volume_uniform_zero_free_neighborhood": "BLOCKED",
            "T7_iii_disjoint_monoidality": "PASS",
            "T7_iii_connected_linked_cluster_density": "BLOCKED",
            "T7_iv_Duhamel_equals_intensive_Hessian": "NOT_EXECUTABLE",
            "authority_audit": authority,
            "corpus_closure_scan": closure_scan,
            "connected_counterfamily": counterfamily,
            "downstream_Qspec_CTP_issue_used_as_T7_blocker": False,
            "new_principle_adopted": False,
            "target_value_used": False,
        },
        "protected_flags": {
            "kappa_record_computed": False,
            "physical_charged_amplitude_computed": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }

    report_path = REPORTS / "T07.json"
    markdown_path = ROOT / "STAGE8_T7_CONNECTED_PRIMITIVE_RESPONSE_GATE_V001.md"
    write_content_addressed(report_path, report)
    markdown_path.write_text(render_markdown(report))

    seal_entries = [
        ROOT / "scripts/run_stage8_t7_connected_response_gate_v001.py",
        report_path,
        markdown_path,
        ROOT / "STAGE8_T7_PARENT_TO_PRIMITIVE_RESPONSE_LIFT_AUDIT_SCOPE_ERRATUM_V001.md",
    ]
    seal_path = GATE_DIR / "T07_CONNECTED_RESPONSE_GATE_V001.seal.sha256"
    seal_path.write_text(
        "".join(
            f"{sha256_file(path)}  {path.relative_to(ROOT)}\n"
            for path in seal_entries
        )
    )
    update_artifact_manifest([*seal_entries, seal_path])
    print(json.dumps(report, indent=2, sort_keys=True))
    return report


if __name__ == "__main__":
    run()
