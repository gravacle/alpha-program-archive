#!/usr/bin/env python3
"""Run one sealed Stage-8 T7 production lane and issue a local execution receipt.

v005 (STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001 + the v004
re-audit return, EXTERNAL_REAUDIT_2026-07-26_fable_v004_return.md; base
v004, sole changes enumerated here):

  a. REPOINTS (B1/Blocking-2 cycle): the runtime launcher is
     launch_stage8_t7_content_addressed_runtime_v005.py (whose rebuilt
     allowlist carries a row for THIS controller, closing the B1
     launcher-vs-controller deadlock); the comparison target is comparator
     v005; the controller's own implementation authority is the sealed v004
     manifest (provenance/..._implementation_v004.json); the required
     manifest row set is the ten-row v005 inventory below.
  b. M1 BUNDLE-STAMP MEMBER: the comparison-lane pre-flight verifies the
     FULL manifest-binding bridge condition INCLUDING the bundle-stamp
     member — the v001-path manifest digest is recomputed from disk and
     compared against the implementation_manifest_sha256 stamped in BOTH
     lane bundle JSONs on disk — BEFORE the canonical comparison path is
     consumed (closes the inter-invocation regeneration hazard).
  c. M2 AUTHORITY-DIGEST PRE-FLIGHT: pre-flight recomputes and verifies,
     from disk, the sealed Phase-A spec digest and EVERY authority digest
     the byte-frozen derive lanes and the comparator verify at runtime
     (the frozen AUTHORITY_DIGESTS inventory below), BEFORE any canonical
     consumption in any lane. Previously these were verified only after
     canonical path commitment, inside the lanes.
  d. --preflight-only (per the sealed discipline's mandated instrument):
     runs EVERY enumerated precondition for the given --lane and exits 0
     with a one-line PREFLIGHT_OK json (or exits nonzero with the precise
     block reason) BEFORE any canonical write. The enumerated precondition
     list is the module-level frozen tuple PRECONDITIONS; the verification
     order is documented at that tuple, pre-flight executes the tuple in
     order, and every canonical write in this module occurs only after
     run_preflight() has returned (provable by the real-component
     end-to-end startability test in test_stage8_t7_controller_v005.py).

Retained from v004: the FIX 1 manifest-binding bridge pre-flight (now one
member richer, M1); the push-capability pre-flight (git push --dry-run,
fail-closed, pushes nothing); RECEIPT-EXISTENCE lane ordering only (external
anchoring between invocations is a cooperative operator procedure, not
enforced here; anchor_receipt_before_next_lane is a cooperative reminder);
GPG fully removed; per-lane invocation (--lane); every fail-closed
precondition verified BEFORE any canonical output path is consumed; receipts
record paths_verified_absent; the comparison lane passes both lane-receipt
digests to the comparator and cross-checks the recorded values. Recorded
fields are RECORDINGS for the externally anchored receipt chain, not
self-authentication.
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
from typing import Any, Callable


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
    ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v005.py"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v004.json"
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

# M2: the sealed Phase-A specification digest, recomputed in pre-flight.
SPEC_RELATIVE = (
    "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md"
)
SPEC_SHA256 = "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3"

# M2: EVERY authority digest the byte-frozen v002 derive lanes and the
# comparator verify at runtime (the union of both lanes' AUTHORITIES
# inventories plus the comparator's spec and runtime-manifest pins; the
# sealed Phase-A spec row and the sealed NumPy runtime-manifest row are
# members). Pre-flight recomputes each from disk BEFORE any canonical
# consumption in any lane, so a lane's own authority verification cannot
# fail after this pre-flight passes.
AUTHORITY_DIGESTS = {
    SPEC_RELATIVE: SPEC_SHA256,
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md":
        "460e87522884e703968025081cceccc0153af3cda27410c397fc2a09a0b367e3",
    "STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md":
        "4e1282bc800c47441d255e9d9d576958608d955dce15f02969261cd6e601e268",
    "STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md":
        "5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7",
    "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md":
        "a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510",
    "STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_RESULT_V001.md":
        "235246abd1c4df69c80bda8f79494c342e30178504dadec411612c18d6f8685b",
    "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md":
        "1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md":
        "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md":
        "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd",
    "STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_"
    "AMENDMENT_V001.md":
        "8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md":
        "76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md":
        "2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde",
    "STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md":
        "a79939adf1d7185fdf4d6ec5ccb929de2e4f5997bee2ed085c0d63164dc8e370",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json":
        "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py":
        "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c",
    "stage8_execution/work/T07_hermite_galerkin_baseline.json":
        "87593740c5f35f68ea1c484c7ab304fbd12ee7b54f62f48f38417c80a2e33f7c",
    "stage8_execution/work/T07_hermite_galerkin_baseline_verification.json":
        "fc55cdedb059d31843b2490a9af2a74902c20acaed08793d64ff5c1e2a7f32f8",
}

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
        "v005.py"
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

# The ten-row v005 inventory: controller v005, launcher v005, comparator
# v005, the byte-frozen v002 derive lanes, and the five test files (the
# three v005 suites plus the byte-frozen v002 derive-lane suites).
REQUIRED_MANIFEST_ROWS = frozenset(
    {
        "scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py",
        "scripts/launch_stage8_t7_content_addressed_runtime_v005.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v005.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py",
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py",
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v005.py",
        "scripts/test_stage8_t7_launcher_v005.py",
        "scripts/test_stage8_t7_controller_v005.py",
    }
)

# THE ENUMERATED PRECONDITIONS (sealed discipline rule 2; frozen tuple).
# run_preflight() executes exactly this tuple, in exactly this order, for
# every invocation mode (--preflight-only and production alike); every
# canonical write in this module occurs only in run_lane()/run_comparison_
# lane(), which main() reaches only after run_preflight() has returned.
# Verification order and rationale:
#   1. runtime_attestation      — the launcher's cooperative marker and the
#                                 sealed runtime-manifest digest must be
#                                 present first: nothing else is trusted
#                                 outside the sealed runtime.
#   2. implementation_manifest  — the controller's own sealed v004 manifest:
#                                 adjacent seal, complete ten-row set,
#                                 self-binding, and row-by-row disk
#                                 equality (includes launcher, targets, and
#                                 the v005 comparator row).
#   3. authority_digests        — M2: the sealed Phase-A spec digest and
#                                 every runtime authority digest of the
#                                 derive lanes and comparator, recomputed
#                                 from disk.
#   4. bridge_binding           — FIX 1: the sealed v001-path manifest the
#                                 frozen lanes verify and stamp: adjacent
#                                 seal, derive-executor row equality with
#                                 the own manifest, launcher-on-disk row,
#                                 row-by-row disk equality.
#   5. push_capability          — git push --dry-run to the archive
#                                 repository (pushes nothing, fail-closed).
#   6. prior_receipts           — receipt-existence lane ordering for every
#                                 lane before --lane.
#   7. comparison_bundle_stamps — M1 (comparison lane; no-op earlier lanes
#                                 have no bundles): the implementation_
#                                 manifest_sha256 stamped in BOTH lane
#                                 bundle JSONs on disk equals the bridge
#                                 digest recomputed in step 4.
#   8. canonical_absences       — the lane-appropriate canonical outputs,
#                                 receipts, and seals are absent.
# Steps 1-8 all precede the first canonical write; steps 6-7 additionally
# precede any consumption of the canonical comparison path.
PRECONDITIONS = (
    "runtime_attestation",
    "implementation_manifest",
    "authority_digests",
    "bridge_binding",
    "push_capability",
    "prior_receipts",
    "comparison_bundle_stamps",
    "canonical_absences",
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


# --------------------------------------------------------------------------
# Precondition steps (each takes the lane and the shared pre-flight context;
# dispatched by run_preflight() in PRECONDITIONS order).
# --------------------------------------------------------------------------


def preflight_runtime_attestation(lane: str, context: dict[str, Any]) -> None:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(
        isinstance(attestation, dict),
        "pipeline requires the sealed runtime launcher",
    )
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "pipeline runtime manifest mismatch",
    )


def preflight_implementation_manifest(lane: str, context: dict[str, Any]) -> None:
    require(
        IMPLEMENTATION_MANIFEST.is_file(),
        "implementation manifest is absent: "
        f"{IMPLEMENTATION_MANIFEST.relative_to(ROOT)}",
    )
    require(
        IMPLEMENTATION_SEAL.is_file(),
        f"implementation seal is absent: {IMPLEMENTATION_SEAL.relative_to(ROOT)}",
    )
    manifest_digest = sha256(IMPLEMENTATION_MANIFEST)
    fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, "malformed implementation seal")
    require(fields[0] == manifest_digest, "implementation seal digest mismatch")
    manifest = strict_json(IMPLEMENTATION_MANIFEST)
    rows = manifest.get("files")
    require(
        isinstance(rows, list) and bool(rows),
        "implementation file inventory is empty",
    )
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
        "v005 comparator is not reachable",
    )
    context["implementation_digest"] = manifest_digest
    context["implementation_rows"] = row_map


def preflight_authority_digests(lane: str, context: dict[str, Any]) -> None:
    """M2: recompute, from disk, the sealed Phase-A spec digest and every
    authority digest the byte-frozen derive lanes and the comparator verify
    at runtime, BEFORE any canonical consumption in any lane."""
    spec = ROOT / SPEC_RELATIVE
    require(
        spec.is_file(),
        f"authority pre-flight: sealed Phase-A spec is absent: {SPEC_RELATIVE}",
    )
    require(
        sha256(spec) == SPEC_SHA256,
        f"authority pre-flight: sealed Phase-A spec digest mismatch: {SPEC_RELATIVE}",
    )
    for relative, expected in sorted(AUTHORITY_DIGESTS.items()):
        path = ROOT / relative
        require(
            path.is_file(),
            f"authority pre-flight: authority is absent: {relative}",
        )
        require(
            sha256(path) == expected,
            f"authority pre-flight: authority digest mismatch: {relative}",
        )


def preflight_bridge_binding(lane: str, context: dict[str, Any]) -> None:
    """FIX 1 bridge pre-flight (retained from v004): verify the manifest-
    binding bridge condition from disk BEFORE any lane runs.

    The byte-frozen derive lanes verify and stamp the sealed manifest at the
    canonical v001 path; the comparator accepts exactly bundles whose
    stamped digest equals that manifest's recomputed digest AND whose
    executing code's authority rows agree with the comparator's own
    manifest. This pre-flight proves, before any canonical path is
    consumed: the v001-path manifest is sealed on disk with a verifying
    adjacent seal (digest recomputed, not copied); the derive-lane executor
    rows are hash-equal row-by-row across the v001-path manifest and this
    controller's own manifest; the own-manifest launcher row equals the
    launcher on disk (the hash the runtime attestation will record); and
    every v001-path manifest row matches its on-disk file, so the frozen
    lanes' own manifest verification cannot fail later. The bundle-stamp
    member of the bridge condition is verified by the comparison_bundle_
    stamps step against the digest recorded here. Failure blocks with zero
    artifacts.
    """
    implementation_rows = context["implementation_rows"]
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
    context["bridge_digest"] = bridge_digest


def preflight_push_capability(lane: str, context: dict[str, Any]) -> None:
    """Retained from v004: prove push capability to the archive repository
    BEFORE any canonical path is consumed, fail-closed. A push failure
    discovered only after sealing would reproduce the GPG wedge (sealed
    artifacts that cannot be anchored). The dry run pushes nothing."""
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


def preflight_prior_receipts(lane: str, context: dict[str, Any]) -> None:
    lane_index = LANE_SEQUENCE.index(lane)
    for prior_lane in LANE_SEQUENCE[:lane_index]:
        verify_prior_receipt(prior_lane)


def preflight_comparison_bundle_stamps(lane: str, context: dict[str, Any]) -> None:
    """M1: the bundle-stamp member of the bridge condition. For the
    comparison lane, the implementation_manifest_sha256 stamped in BOTH
    lane bundle JSONs on disk must equal the v001-path manifest digest
    recomputed by the bridge_binding step in THIS invocation, so a bundle
    regenerated against a different manifest between invocations cannot
    reach the comparator. Earlier lanes have no bundles yet; the step is a
    documented no-op for them."""
    if lane != "comparison":
        return
    bridge_digest = context["bridge_digest"]
    for bundle_lane, bundle_json in (
        ("independent", INDEPENDENT_JSON),
        ("primary", PRIMARY_JSON),
    ):
        require(
            bundle_json.is_file(),
            f"bundle-stamp pre-flight: {bundle_lane} bundle JSON is absent: "
            f"{bundle_json.relative_to(ROOT)}",
        )
        payload = strict_json(bundle_json)
        stamped = payload.get("implementation_manifest_sha256")
        require(
            stamped == bridge_digest,
            f"bundle-stamp pre-flight: {bundle_lane} bundle stamp does not "
            "equal the recomputed v001-path manifest digest",
        )


def preflight_canonical_absences(lane: str, context: dict[str, Any]) -> None:
    """Verify absence of every canonical output and receipt that must not yet
    exist before this lane runs, and record the exact list verified (written
    into the receipt as paths_verified_absent)."""
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
    context["paths_verified_absent"] = [
        str(path.relative_to(ROOT)) for path in checked
    ]


PRECONDITION_STEPS: dict[str, Callable[[str, dict[str, Any]], None]] = {
    "runtime_attestation": preflight_runtime_attestation,
    "implementation_manifest": preflight_implementation_manifest,
    "authority_digests": preflight_authority_digests,
    "bridge_binding": preflight_bridge_binding,
    "push_capability": preflight_push_capability,
    "prior_receipts": preflight_prior_receipts,
    "comparison_bundle_stamps": preflight_comparison_bundle_stamps,
    "canonical_absences": preflight_canonical_absences,
}


def run_preflight(lane: str) -> dict[str, Any]:
    """Execute EVERY enumerated precondition, in PRECONDITIONS order, for
    the given lane. Performs no write anywhere. Every canonical write in
    this module happens only after this function has returned."""
    context: dict[str, Any] = {}
    for name in PRECONDITIONS:
        PRECONDITION_STEPS[name](lane, context)
    return context


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
        description="Run exactly one Stage-8 T7 production lane (v005)."
    )
    parser.add_argument("--lane", required=True, choices=LANE_SEQUENCE)
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help=(
            "Run EVERY enumerated precondition (the frozen PRECONDITIONS "
            "tuple, in order) for the given lane and exit before any "
            "canonical write: exit 0 with a one-line PREFLIGHT_OK json, or "
            "exit 1 with the precise block reason."
        ),
    )
    arguments = parser.parse_args()
    lane = arguments.lane
    controller_context = str(SELF.relative_to(ROOT))
    os.environ[CONTROLLER_CONTEXT_ENVIRONMENT_KEY] = controller_context

    if arguments.preflight_only:
        # Sealed-discipline instrument: every enumerated precondition, in
        # the documented order, with NO write anywhere and NO canonical
        # consumption; the outcome is a single line of JSON.
        try:
            context = run_preflight(lane)
        except RuntimeError as error:
            print(
                json.dumps(
                    {
                        "schema": "stage8_t7_preflight_only_summary_v001",
                        "status": "PREFLIGHT_BLOCKED",
                        "lane": lane,
                        "preconditions": list(PRECONDITIONS),
                        "reason": str(error),
                        "alpha_computed": False,
                        "proof_authorized": False,
                    },
                    sort_keys=True,
                )
            )
            print(f"preflight blocked: {error}", file=sys.stderr)
            return 1
        print(
            json.dumps(
                {
                    "schema": "stage8_t7_preflight_only_summary_v001",
                    "status": "PREFLIGHT_OK",
                    "lane": lane,
                    "preconditions": list(PRECONDITIONS),
                    "implementation_manifest_sha256":
                        context["implementation_digest"],
                    "bridge_manifest_sha256": context["bridge_digest"],
                    "paths_verified_absent": context["paths_verified_absent"],
                    "alpha_computed": False,
                    "proof_authorized": False,
                },
                sort_keys=True,
            )
        )
        return 0

    # PRE-FLIGHT (the frozen PRECONDITIONS tuple, in order; all fail-closed
    # preconditions BEFORE any canonical output path is consumed).
    context = run_preflight(lane)
    implementation_digest = context["implementation_digest"]
    implementation_rows = context["implementation_rows"]
    paths_verified_absent = context["paths_verified_absent"]

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
