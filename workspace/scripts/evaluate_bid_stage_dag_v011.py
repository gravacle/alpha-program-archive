#!/usr/bin/env python3
"""Compute BID stage status from immutable subjects and independent reports."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = (
    ROOT / "provenance/boundary_incidence_dynamics_preregistration_v011.json"
)

REQUIRED_ROLES = {
    "SPEC-SEAL": {
        "formal type/category",
        "physics/operator",
        "independent full-stack red team",
    },
    "CORE-RESULT-SEAL": {
        "gate executor",
        "formal type/category",
        "physics/operator",
        "independent full-stack red team",
        "independent core reconstruction",
    },
    "PARENT-COMPARISON": {"independent parent comparator"},
    "HOLDOUT-UNIVERSE-SEAL": {
        "independent outcome custodian",
        "registry completeness auditor",
    },
    "QSPEC-SPEC-SEAL": {
        "formal type/category",
        "physics/operator",
        "independent full-stack red team",
    },
    "PREDICTION-MAP-SEAL": {"independent prediction-map auditor"},
    "THOMSON-RESULT-SEAL": {
        "qspec executor",
        "formal type/category",
        "physics/operator",
        "independent full-stack red team",
        "independent Thomson reconstruction",
    },
    "ALPHA-RESULT-SEAL": {"independent alpha evaluator"},
    "HOLDOUT-RESULT-SEAL": {
        "independent outcome custodian",
        "independent contamination auditor",
    },
    "END-TO-END-RECONSTRUCTION-SEAL": {"independent end-to-end reconstruction"},
    "FINAL-CLAIM-SEAL": {
        "formal type/category",
        "physics/operator",
        "independent full-stack red team",
    },
}

REPORT_KEYS = {
    "schema_version",
    "subject_sha256",
    "stage",
    "reviewer_role",
    "process_id",
    "verdict",
    "blockers",
    "full_matrix_attestation",
    "no_edit_attestation",
    "artifact_hashes",
    "created_utc",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_sha256(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_report(
    report: dict[str, object],
    path: Path,
    subjects: dict[str, str],
) -> list[str]:
    failures: list[str] = []
    if set(report) != REPORT_KEYS:
        failures.append(f"{path.name}: report schema keys differ")
        return failures
    stage = report["stage"]
    if stage not in REQUIRED_ROLES:
        failures.append(f"{path.name}: unknown stage {stage}")
        return failures
    if report["reviewer_role"] not in REQUIRED_ROLES[stage]:
        failures.append(f"{path.name}: unrecognized role for {stage}")
    if report["subject_sha256"] != subjects.get(stage):
        failures.append(f"{path.name}: subject hash mismatch")
    if report["verdict"] not in {"PASS", "FAIL"}:
        failures.append(f"{path.name}: invalid verdict")
    if not isinstance(report["blockers"], list):
        failures.append(f"{path.name}: blockers is not a list")
    if report["verdict"] == "PASS" and report["blockers"]:
        failures.append(f"{path.name}: PASS report contains blockers")
    if report["full_matrix_attestation"] is not True:
        failures.append(f"{path.name}: no full-matrix attestation")
    if report["no_edit_attestation"] is not True:
        failures.append(f"{path.name}: no no-edit attestation")
    if not isinstance(report["process_id"], str) or not report["process_id"]:
        failures.append(f"{path.name}: empty process_id")
    if not isinstance(report["created_utc"], str) or not report["created_utc"]:
        failures.append(f"{path.name}: empty created_utc")
    if not isinstance(report["artifact_hashes"], dict):
        failures.append(f"{path.name}: artifact_hashes is not an object")
    else:
        for relative, expected in report["artifact_hashes"].items():
            artifact = ROOT / relative
            if not is_sha256(expected):
                failures.append(f"{path.name}: bad artifact hash for {relative}")
            elif not artifact.is_file() or sha256(artifact) != expected:
                failures.append(f"{path.name}: artifact mismatch for {relative}")
    return failures


def acyclic(graph: dict[str, list[str]]) -> bool:
    if set(graph) != set(REQUIRED_ROLES):
        return False
    if any(dependency not in graph for deps in graph.values() for dependency in deps):
        return False
    state: dict[str, int] = {}

    def visit(node: str) -> bool:
        if state.get(node) == 1:
            return False
        if state.get(node) == 2:
            return True
        state[node] = 1
        if not all(visit(dependency) for dependency in graph[node]):
            return False
        state[node] = 2
        return True

    return all(visit(node) for node in graph)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--subjects", type=Path, required=True)
    parser.add_argument("--reports", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    subjects = load_json(args.subjects)
    graph = manifest["review_stage_semantics"]["stage_dependencies"]
    failures: list[str] = []

    if not acyclic(graph):
        failures.append("manifest stage graph is missing nodes or cyclic")
    if set(subjects) != set(graph):
        failures.append("subjects file does not contain exactly every stage")
    for stage, subject in subjects.items():
        if not is_sha256(subject):
            failures.append(f"subject hash is invalid for {stage}")

    reports_by_stage: dict[str, list[dict[str, object]]] = {
        stage: [] for stage in graph
    }
    if not args.reports.is_dir():
        failures.append("reports path is not a directory")
    else:
        for path in sorted(args.reports.glob("*.json")):
            report = load_json(path)
            failures.extend(validate_report(report, path, subjects))
            if isinstance(report, dict) and report.get("stage") in reports_by_stage:
                reports_by_stage[report["stage"]].append(report)

    status: dict[str, bool] = {}
    blockers: dict[str, list[str]] = {}
    for stage in graph:
        stage_reports = reports_by_stage[stage]
        roles = {report["reviewer_role"] for report in stage_reports}
        process_ids = {report["process_id"] for report in stage_reports}
        report_blockers = [
            blocker
            for report in stage_reports
            if report["verdict"] == "FAIL"
            for blocker in report["blockers"]
        ]
        dependencies_pass = all(status.get(dependency, False) for dependency in graph[stage])
        roles_complete = REQUIRED_ROLES[stage].issubset(roles)
        processes_independent = len(process_ids) >= len(REQUIRED_ROLES[stage])
        unanimous = all(report["verdict"] == "PASS" for report in stage_reports)
        no_extra_fail = not any(report["verdict"] == "FAIL" for report in stage_reports)
        status[stage] = (
            not failures
            and dependencies_pass
            and roles_complete
            and processes_independent
            and unanimous
            and no_extra_fail
        )
        blockers[stage] = report_blockers

    output = {
        "schema_version": 1,
        "manifest_sha256": sha256(args.manifest),
        "subjects_sha256": sha256(args.subjects),
        "stage_status": status,
        "stage_blockers": blockers,
        "proof_authorized": status.get("FINAL-CLAIM-SEAL", False),
        "evaluator_failures": failures,
    }
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
