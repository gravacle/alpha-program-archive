#!/usr/bin/env python3
"""Run one sealed Stage-8 T7 production lane and issue a local execution receipt.

v004 (STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_V001; re-audit FIX 1 +
RE-SCOPE; base v003, sole changes enumerated in amendment A2 item 2):
  a. Targets comparator v004 and binds to the v003 implementation manifest
     (provenance/..._implementation_v003.json); the required manifest row
     set is the amendment A2 item-5 inventory.
  b. BRIDGE PRE-FLIGHT (FIX 1): before any lane runs and before any
     canonical path is consumed, the ENTIRE manifest-binding bridge
     condition is verified from disk: the sealed manifest at the canonical
     v001 path (the object the byte-frozen derive lanes verify and stamp)
     and this controller's own v003 manifest are both present with
     verifying adjacent seals; both digests are recomputed from disk; the
     derive-lane executor rows are hash-equal row-by-row across the two
     manifests; the own-manifest launcher row equals the launcher on disk
     (the hash the runtime attestation will record); and every v001-path
     manifest row matches its on-disk file, so the frozen lanes' own
     manifest verification cannot fail after this pre-flight passes. Any
     bridge failure blocks with zero artifacts.
  c. PUSH-CAPABILITY PRE-FLIGHT (RE-SCOPE item): anchoring requires push
     capability to the archive repository; a push failure discovered after
     sealing would reproduce the GPG wedge. Before any canonical path is
     consumed the controller runs
     git -C /Users/bgm/MB Work/alpha-program-archive
     push --dry-run origin main and requires returncode 0, fail-closed.
     The dry run pushes nothing; it only proves the capability.
  d. RE-SCOPE of enforcement language: this controller enforces
     RECEIPT-EXISTENCE lane ordering only — primary refuses without the
     sealed+verified independent receipt; comparison refuses without both
     lane receipts. External anchoring of each receipt (commit+push per
     the S3 procedure) is a COOPERATIVE procedure executed by the operator
     between invocations; no code here enforces anchor-before-next-lane,
     and the summary field anchor_receipt_before_next_lane is a
     cooperative reminder, not an enforced guarantee.

Retained from v003: GPG fully removed; per-lane invocation (--lane) with
receipt-existence lane ordering; every fail-closed precondition verified
BEFORE any canonical output path is consumed; receipts record
paths_verified_absent (the exact absence list checked); the comparison lane
passes both lane-receipt digests to the comparator and cross-checks the
recorded values. These recorded fields are RECORDINGS for the externally
anchored receipt chain, not self-authentication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
).resolve()
RUNTIME_LAUNCHER = (
    ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v004.py"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v003.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")
BRIDGE_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
BRIDGE_SEAL = Path(f"{BRIDGE_MANIFEST}.seal.sha256")
ARCHIVE_REPOSITORY = Path("/Users/bgm/MB Work/alpha-program-archive")
CONTROLLER_CONTEXT_ENVIRONMENT_KEY = "STAGE8_T7_CONTROLLER_CONTEXT"
RECEIPT_SCHEMA = "stage8_t7_local_sealed_execution_receipt_v003"

WORK = ROOT / "stage8_execution/work"
INDEPENDENT_JSON = (
    WORK
    / "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001.json"
)
INDEPENDENT_NPZ = INDEPENDENT_JSON.with_suffix(".npz")
PRIMARY_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
PRIMARY_NPZ = PRIMARY_JSON.with_suffix(".npz")
COMPARISON_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_comparison_v001.json"
)
INDEPENDENT_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_independent_execution_receipt_v001.json"
)
PRIMARY_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_primary_execution_receipt_v001.json"
)
COMPARISON_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_comparison_execution_receipt_v001.json"
)

LANE_SEQUENCE = ("independent", "primary", "comparison")

TARGETS = {
    "independent": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py"
    ),
    "primary": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    ),
    "comparison": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v004.py"
    ),
}

LANE_OUTPUTS = {
    "independent": (INDEPENDENT_JSON, INDEPENDENT_NPZ),
    "primary": (PRIMARY_JSON, PRIMARY_NPZ),
    "comparison": (COMPARISON_JSON,),
}

LANE_RECEIPTS = {
    "independent": INDEPENDENT_RECEIPT,
    "primary": PRIMARY_RECEIPT,
    "comparison": COMPARISON_RECEIPT,
}

# Amendment A2 item-5 inventory: controller v004, launcher v003, comparator
# v004, derive v002 x2, the v004 test files, launcher/controller tests,
# derive-lane v002 tests.
REQUIRED_MANIFEST_ROWS = frozenset(
    {
        "scripts/run_stage8_t7_actual_parent_car_pipeline_v004.py",
        "scripts/launch_stage8_t7_content_addressed_runtime_v004.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v004.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v004.py",
        "scripts/test_stage8_t7_launcher_v004.py",
        "scripts/test_stage8_t7_controller_v004.py",
    }
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def strict_json(path: Path) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=object_pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(
            RuntimeError(f"non-finite JSON constant in {path}: {value}")
        ),
    )
    require(isinstance(value, dict), f"JSON document is not an object: {path}")
    return value


def atomic_sealed_json(path: Path, payload: dict[str, Any]) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(not path.exists(), f"immutable receipt already exists: {path}")
    require(not seal.exists(), f"immutable receipt seal already exists: {seal}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)
    digest = sha256(path)
    seal_temporary = seal.with_suffix(seal.suffix + ".tmp")
    seal_temporary.write_text(f"{digest}  {path.name}\n", encoding="ascii")
    os.replace(seal_temporary, seal)
    for artifact in (path, seal):
        artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return digest


def verify_adjacent_seal(path: Path) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(path.is_file(), f"expected output is absent: {path}")
    require(seal.is_file(), f"expected output seal is absent: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed output seal: {seal}")
    digest = sha256(path)
    require(fields[0] == digest, f"output seal digest mismatch: {path}")
    require(fields[1] == path.name, f"output seal filename mismatch: {path}")
    return digest


def verify_implementation() -> tuple[str, dict[str, str]]:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(isinstance(attestation, dict), "pipeline requires the sealed runtime launcher")
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "pipeline runtime manifest mismatch",
    )
    require(IMPLEMENTATION_MANIFEST.is_file(), "implementation manifest is absent")
    require(IMPLEMENTATION_SEAL.is_file(), "implementation seal is absent")
    manifest_digest = sha256(IMPLEMENTATION_MANIFEST)
    fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, "malformed implementation seal")
    require(fields[0] == manifest_digest, "implementation seal digest mismatch")
    manifest = strict_json(IMPLEMENTATION_MANIFEST)
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "implementation file inventory is empty")
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    missing_rows = sorted(REQUIRED_MANIFEST_ROWS - set(row_map))
    require(
        not missing_rows,
        f"implementation manifest is missing required rows: {missing_rows}",
    )
    require(
        row_map.get(str(SELF.relative_to(ROOT))) == sha256(SELF),
        "pipeline is not implementation-bound",
    )
    for relative, expected in row_map.items():
        path = ROOT / relative
        require(path.is_file(), f"implementation input is absent: {relative}")
        require(sha256(path) == expected, f"implementation drift: {relative}")
    require(
        (ROOT / TARGETS["comparison"]).is_file(),
        "v004 comparator is not reachable",
    )
    return manifest_digest, row_map


def verify_bridge_binding(implementation_rows: dict[str, str]) -> str:
    """FIX 1 bridge pre-flight (amendment A1): verify the ENTIRE
    manifest-binding bridge condition from disk BEFORE any lane runs.

    The byte-frozen derive lanes verify and stamp the sealed manifest at the
    canonical v001 path; comparator v004 accepts exactly bundles whose
    stamped digest equals that manifest's recomputed digest AND whose
    executing code's authority rows agree with the comparator's own
    manifest. This pre-flight proves, before any canonical path is
    consumed: the v001-path manifest is sealed on disk with a verifying
    adjacent seal (digest recomputed, not copied); the derive-lane executor
    rows are hash-equal row-by-row across the v001-path manifest and this
    controller's own manifest; the own-manifest launcher row equals the
    launcher on disk (the hash the runtime attestation will record); and
    every v001-path manifest row matches its on-disk file, so the frozen
    lanes' own manifest verification cannot fail later. Failure blocks with
    zero artifacts.
    """
    require(
        BRIDGE_MANIFEST.is_file(),
        "bridge pre-flight: v001-path implementation manifest is absent",
    )
    require(
        BRIDGE_SEAL.is_file(),
        "bridge pre-flight: v001-path implementation seal is absent",
    )
    bridge_digest = sha256(BRIDGE_MANIFEST)
    fields = BRIDGE_SEAL.read_text(encoding="ascii").strip().split()
    require(
        len(fields) == 2,
        "bridge pre-flight: malformed v001-path implementation seal",
    )
    require(
        fields[0] == bridge_digest,
        "bridge pre-flight: v001-path implementation seal digest mismatch",
    )
    require(
        fields[1] == BRIDGE_MANIFEST.name,
        "bridge pre-flight: v001-path implementation seal filename mismatch",
    )
    bridge = strict_json(BRIDGE_MANIFEST)
    rows = bridge.get("files")
    require(
        isinstance(rows, list) and bool(rows),
        "bridge pre-flight: v001-path implementation file inventory is empty",
    )
    bridge_rows = {str(row["path"]): str(row["sha256"]) for row in rows}
    for relative in (TARGETS["independent"], TARGETS["primary"]):
        require(
            relative in bridge_rows,
            f"bridge pre-flight: v001-path manifest lacks the executor row: {relative}",
        )
        require(
            relative in implementation_rows,
            f"bridge pre-flight: own manifest lacks the executor row: {relative}",
        )
        require(
            bridge_rows[relative] == implementation_rows[relative],
            f"bridge pre-flight: manifest row mismatch for {relative}",
        )
    launcher_relative = str(RUNTIME_LAUNCHER.relative_to(ROOT))
    require(
        implementation_rows.get(launcher_relative) == sha256(RUNTIME_LAUNCHER),
        "bridge pre-flight: launcher row inconsistent with the launcher on disk: "
        f"{launcher_relative}",
    )
    for relative, expected in sorted(bridge_rows.items()):
        path = ROOT / relative
        require(
            path.is_file(),
            f"bridge pre-flight: v001-path implementation input is absent: {relative}",
        )
        require(
            sha256(path) == expected,
            f"bridge pre-flight: v001-path implementation drift: {relative}",
        )
    return bridge_digest


def preflight_push_capability() -> None:
    """RE-SCOPE item: prove push capability to the archive repository BEFORE
    any canonical path is consumed, fail-closed. A push failure discovered
    only after sealing would reproduce the GPG wedge (sealed artifacts that
    cannot be anchored). The dry run pushes nothing."""
    require(
        ARCHIVE_REPOSITORY.is_dir(),
        f"push-capability pre-flight: archive repository is absent: "
        f"{ARCHIVE_REPOSITORY}",
    )
    completed = subprocess.run(
        [
            "git",
            "-C",
            str(ARCHIVE_REPOSITORY),
            "push",
            "--dry-run",
            "origin",
            "main",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        completed.returncode == 0,
        "push-capability pre-flight failed "
        f"(returncode {completed.returncode}); anchoring would wedge after "
        f"sealing: {completed.stderr[-2000:]}",
    )


def verify_prior_receipt(lane: str) -> tuple[str, dict[str, Any]]:
    receipt = LANE_RECEIPTS[lane]
    require(
        receipt.is_file(),
        f"lane-order violation: the {lane} receipt is absent; "
        f"run --lane {lane} (and anchor it) first",
    )
    digest = verify_adjacent_seal(receipt)
    payload = strict_json(receipt)
    require(
        payload.get("schema") == RECEIPT_SCHEMA,
        f"{lane} receipt schema mismatch",
    )
    require(payload.get("lane") == lane, f"{lane} receipt lane mismatch")
    require(
        payload.get("status") == "SUCCEEDED",
        f"{lane} receipt does not record a SUCCEEDED lane",
    )
    require(
        payload.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        f"{lane} receipt runtime manifest mismatch",
    )
    return digest, payload


def receipt_output_digests(lane: str, payload: dict[str, Any]) -> dict[str, str]:
    rows = payload.get("outputs")
    require(isinstance(rows, list) and bool(rows), f"{lane} receipt has no output rows")
    digests: dict[str, str] = {}
    for row in rows:
        relative = str(row["path"])
        expected = str(row["sha256"])
        require(
            verify_adjacent_seal(ROOT / relative) == expected,
            f"{lane} output drifted from its sealed receipt: {relative}",
        )
        digests[relative] = expected
    for output in LANE_OUTPUTS[lane]:
        require(
            str(output.relative_to(ROOT)) in digests,
            f"{lane} receipt does not cover the canonical output: {output}",
        )
    return digests


def preflight_absences(lane: str) -> list[str]:
    """Verify absence of every canonical output and receipt that must not yet
    exist before this lane runs, and return the exact list verified (recorded
    in the receipt as paths_verified_absent)."""
    lane_index = LANE_SEQUENCE.index(lane)
    pending = LANE_SEQUENCE[lane_index:]
    checked: list[Path] = []
    for pending_lane in pending:
        checked.extend(LANE_OUTPUTS[pending_lane])
    for pending_lane in pending:
        checked.append(LANE_RECEIPTS[pending_lane])
    for path in checked:
        require(
            not path.exists(),
            f"pre-flight: canonical path already exists before the {lane} lane: {path}",
        )
        require(
            not Path(f"{path}.seal.sha256").exists(),
            f"pre-flight: canonical seal already exists before the {lane} lane: {path}",
        )
    return [str(path.relative_to(ROOT)) for path in checked]


def lane_command(target: str, arguments: list[str]) -> list[str]:
    return [
        str(PINNED_PYTHON),
        "-I",
        "-S",
        str(RUNTIME_LAUNCHER),
        target,
        *arguments,
    ]


def run_lane(
    *,
    lane: str,
    target: str,
    arguments: list[str],
    outputs: tuple[Path, ...],
    receipt: Path,
    implementation_digest: str,
    implementation_rows: dict[str, str],
    paths_verified_absent: list[str],
) -> dict[str, str]:
    require(target == TARGETS[lane], f"unexpected {lane} target")
    for output in outputs:
        require(not output.exists(), f"immutable output already exists: {output}")
        require(
            not Path(f"{output}.seal.sha256").exists(),
            f"immutable output seal already exists: {output}",
        )
    require(not receipt.exists(), f"immutable receipt already exists: {receipt}")
    require(
        not Path(f"{receipt}.seal.sha256").exists(),
        f"immutable receipt seal already exists: {receipt}",
    )

    expected_target_sha256 = implementation_rows[target]
    target_sha256_pre_execution = sha256(ROOT / target)
    require(
        target_sha256_pre_execution == expected_target_sha256,
        f"{lane} target drift before execution: {target}",
    )
    command = lane_command(target, arguments)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    target_sha256_post_execution = sha256(ROOT / target)
    target_intact = target_sha256_post_execution == expected_target_sha256
    output_rows: list[dict[str, str]] = []
    if completed.returncode == 0:
        for output in outputs:
            digest = verify_adjacent_seal(output)
            output_rows.append(
                {
                    "path": str(output.relative_to(ROOT)),
                    "sha256": digest,
                    "seal_sha256": sha256(Path(f"{output}.seal.sha256")),
                }
            )
    else:
        for output in outputs:
            if output.is_file() and Path(f"{output}.seal.sha256").is_file():
                output_rows.append(
                    {
                        "path": str(output.relative_to(ROOT)),
                        "sha256": verify_adjacent_seal(output),
                        "seal_sha256": sha256(Path(f"{output}.seal.sha256")),
                    }
                )

    payload = {
        "schema": RECEIPT_SCHEMA,
        "lane": lane,
        "status": (
            "SUCCEEDED" if completed.returncode == 0 and target_intact else "BLOCKED"
        ),
        "returncode": completed.returncode,
        "target": target,
        "target_sha256": implementation_rows[target],
        "target_sha256_pre_execution": target_sha256_pre_execution,
        "target_sha256_post_execution": target_sha256_post_execution,
        "controller": str(SELF.relative_to(ROOT)),
        "controller_sha256": implementation_rows[str(SELF.relative_to(ROOT))],
        "runtime_launcher": str(RUNTIME_LAUNCHER.relative_to(ROOT)),
        "runtime_launcher_sha256": implementation_rows[
            str(RUNTIME_LAUNCHER.relative_to(ROOT))
        ],
        "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
        "implementation_manifest_sha256": implementation_digest,
        "paths_verified_absent": paths_verified_absent,
        "outputs": output_rows,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
        "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
        "local_execution_receipt_not_remote_attestation": True,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    atomic_sealed_json(receipt, payload)
    require(
        target_intact,
        f"{lane} target drifted across execution: {target}",
    )
    require(
        completed.returncode == 0,
        f"{lane} lane blocked: {completed.stderr[-2000:]}",
    )
    return {row["path"]: row["sha256"] for row in output_rows}


def run_comparison_lane(
    *,
    controller_context: str,
    implementation_digest: str,
    implementation_rows: dict[str, str],
    paths_verified_absent: list[str],
) -> dict[str, Any]:
    independent_receipt_sha256, independent_payload = verify_prior_receipt(
        "independent"
    )
    primary_receipt_sha256, primary_payload = verify_prior_receipt("primary")
    independent_hashes = receipt_output_digests("independent", independent_payload)
    primary_hashes = receipt_output_digests("primary", primary_payload)
    comparison_arguments = [
        "--independent-json",
        str(INDEPENDENT_JSON),
        "--independent-npz",
        str(INDEPENDENT_NPZ),
        "--primary-json",
        str(PRIMARY_JSON),
        "--primary-npz",
        str(PRIMARY_NPZ),
        "--independent-json-sha256",
        independent_hashes[str(INDEPENDENT_JSON.relative_to(ROOT))],
        "--independent-npz-sha256",
        independent_hashes[str(INDEPENDENT_NPZ.relative_to(ROOT))],
        "--primary-json-sha256",
        primary_hashes[str(PRIMARY_JSON.relative_to(ROOT))],
        "--primary-npz-sha256",
        primary_hashes[str(PRIMARY_NPZ.relative_to(ROOT))],
        "--output",
        str(COMPARISON_JSON),
        "--controller-context",
        controller_context,
        "--independent-receipt-sha256",
        independent_receipt_sha256,
        "--primary-receipt-sha256",
        primary_receipt_sha256,
    ]
    comparison_hashes = run_lane(
        lane="comparison",
        target=TARGETS["comparison"],
        arguments=comparison_arguments,
        outputs=LANE_OUTPUTS["comparison"],
        receipt=COMPARISON_RECEIPT,
        implementation_digest=implementation_digest,
        implementation_rows=implementation_rows,
        paths_verified_absent=paths_verified_absent,
    )
    comparison = strict_json(COMPARISON_JSON)
    require(
        comparison.get("overall_verdict")
        == "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED",
        "sealed comparator did not return the Phase-A PASS verdict",
    )
    require(
        comparison.get("comparison_supports_actual_parent_regulated_CAR_operator_response")
        is True,
        "comparator did not set comparison_supports_actual_parent_regulated_CAR_operator_response",
    )
    require(
        comparison.get(
            "comparison_supports_actual_parent_same_carrier_one_source_restriction"
        )
        is True,
        "comparator did not set comparison_supports_actual_parent_same_carrier_one_source_restriction",
    )
    canonical_input_paths = {
        "independent_json": str(INDEPENDENT_JSON.resolve()),
        "independent_npz": str(INDEPENDENT_NPZ.resolve()),
        "primary_json": str(PRIMARY_JSON.resolve()),
        "primary_npz": str(PRIMARY_NPZ.resolve()),
    }
    require(
        comparison.get("resolved_input_paths") == canonical_input_paths,
        "comparator resolved input paths do not match the canonical pinned paths",
    )
    require(
        comparison.get("resolved_output_path") == str(COMPARISON_JSON.resolve()),
        "comparator resolved output path does not match the canonical pinned path",
    )
    require(
        comparison.get("controller_context") == controller_context,
        "comparator did not record the controller context",
    )
    require(
        comparison.get("independent_receipt_sha256") == independent_receipt_sha256,
        "comparator did not record the independent receipt digest verbatim",
    )
    require(
        comparison.get("primary_receipt_sha256") == primary_receipt_sha256,
        "comparator did not record the primary receipt digest verbatim",
    )
    return {
        "schema": "stage8_t7_actual_parent_car_pipeline_summary_v003",
        "lane": "comparison",
        "overall_verdict": comparison["overall_verdict"],
        "implementation_manifest_sha256": implementation_digest,
        "independent_receipt_sha256": independent_receipt_sha256,
        "primary_receipt_sha256": primary_receipt_sha256,
        "comparison_receipt_sha256": sha256(COMPARISON_RECEIPT),
        "comparison_output_sha256":
            comparison_hashes[str(COMPARISON_JSON.relative_to(ROOT))],
        "phase": "A",
        "alpha_computed": False,
        "proof_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run exactly one Stage-8 T7 production lane (v004)."
    )
    parser.add_argument("--lane", required=True, choices=LANE_SEQUENCE)
    lane = parser.parse_args().lane
    controller_context = str(SELF.relative_to(ROOT))
    os.environ[CONTROLLER_CONTEXT_ENVIRONMENT_KEY] = controller_context

    # PRE-FLIGHT (all fail-closed preconditions BEFORE any canonical output
    # path is consumed): runtime attestation, complete manifest row set +
    # adjacent seal, launcher/target/comparator hashes, the FIX 1
    # manifest-binding bridge condition, push capability to the archive
    # repository, prior-lane receipts, and the lane-appropriate canonical
    # absences.
    implementation_digest, implementation_rows = verify_implementation()
    verify_bridge_binding(implementation_rows)
    preflight_push_capability()
    lane_index = LANE_SEQUENCE.index(lane)
    for prior_lane in LANE_SEQUENCE[:lane_index]:
        verify_prior_receipt(prior_lane)
    paths_verified_absent = preflight_absences(lane)

    if lane == "comparison":
        summary = run_comparison_lane(
            controller_context=controller_context,
            implementation_digest=implementation_digest,
            implementation_rows=implementation_rows,
            paths_verified_absent=paths_verified_absent,
        )
    else:
        hashes = run_lane(
            lane=lane,
            target=TARGETS[lane],
            arguments=[],
            outputs=LANE_OUTPUTS[lane],
            receipt=LANE_RECEIPTS[lane],
            implementation_digest=implementation_digest,
            implementation_rows=implementation_rows,
            paths_verified_absent=paths_verified_absent,
        )
        summary = {
            "schema": "stage8_t7_actual_parent_car_lane_summary_v003",
            "lane": lane,
            "implementation_manifest_sha256": implementation_digest,
            "receipt": str(LANE_RECEIPTS[lane].relative_to(ROOT)),
            "receipt_sha256": sha256(LANE_RECEIPTS[lane]),
            "outputs": hashes,
            "anchor_receipt_before_next_lane": True,
            "phase": "A",
            "alpha_computed": False,
            "proof_authorized": False,
        }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
