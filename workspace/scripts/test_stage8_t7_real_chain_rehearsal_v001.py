#!/usr/bin/env python3
"""A2 FULL REAL-CHAIN REHEARSAL — the only accepted startability evidence.

STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001 Part A item
A2, and STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001
required-work item 2 (the fence's ADOPTION PROBE).

WHAT IT DOES.  It copies the entire clean-room workspace to a DISPOSABLE
location, builds the generation-G7 manifest there with the real builder, and
then runs ALL THREE PRODUCTION LANES, in production order, end to end:

    real launcher v007
      -> real controller v007 (--lane independent)
      -> real byte-frozen derive lane independent_v002
    real launcher v007
      -> real controller v007 (--lane primary)
      -> real byte-frozen derive lane primary_v002
    real launcher v007
      -> real controller v007 (--lane comparison)
      -> real comparator v006

NO STUBS ANYWHERE.  No stub lane, no stub launcher, no stub comparator, no
monkeypatch, no copied-and-edited module, no source substitution.  Every
component is the byte-identical file from the canonical workspace; the only
difference is that ROOT is a disposable copy, which is what the binding
requires ("never the canonical root").

WHAT IT ASSERTS, and IN WHAT ORDER.  The fence evidence is collected for
EVERY lane first, and the pipeline's scientific verdict is asserted LAST.
The two are separated on purpose: the fence's adoption probe asks whether the
FENCE lets legitimate production through, and that must be answerable even
when the pipeline blocks for a reason the fence has nothing to do with.
Conflating them would either report a numerical result as a fence failure or
hide a fence failure behind a numerical one.

  1. The write fence is exercised for real: the copy starts with
     stage8_execution/work and provenance at mode 555; each lane RAISES them,
     writes its component's artifacts through them, and DROPS them; and after
     every lane they are verifiably back at 555 -- asserted by ATTEMPTING A
     WRITE and requiring PermissionError, never by reading a mode bit alone.
  2. A SUPERSEDED CHAIN CANNOT WRITE.  With the fence at rest, the byte-
     frozen derive lane invoked directly under launcher v002 -- the live
     write route escalated as B3 -- produces NO artifact.  This is the
     mechanism claim, tested rather than asserted.
  3. THE FENCE ADOPTION PROBE (fence record item 2), decided on fence
     evidence alone: every lane raised both directories, wrote through them,
     and dropped them, and the fence verified closed after each.
  4. Both derive lanes SUCCEED; their receipts and outputs seal-verify and
     carry generation G7.  A blocked lane must seal NO receipt (A4 in the
     real chain), which is asserted whenever a lane blocks.
  5. LAST: the comparator returns the Phase-A PASS verdict.  A non-PASS here
     is a comparator-verdict result, NOT a plumbing failure, and the
     preregistered outcome-blind tolerances may NOT be revised in response
     to it.
  6. PREFLIGHT_OK is recorded but is explicitly NOT the evidence: the
     rehearsal runs the real lanes to completion.

RUNTIME.  The byte-frozen lanes run at their own frozen scale (the fixture
scale is the disposable workspace, not a reduced grid: the lanes cannot be
scaled down without editing them, and they are byte-frozen).  Expect a few
minutes.

The canonical workspace is only ever READ.  Nothing here chmods a canonical
directory or writes a canonical artifact.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
)
CONTROLLER_RELATIVE = "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
LAUNCHER_RELATIVE = "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
LEGACY_LAUNCHER_RELATIVE = (
    "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
)
DERIVE_INDEPENDENT_RELATIVE = (
    "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v002.py"
)
BUILDER_RELATIVE = (
    "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v006.py"
)
MANIFEST_RELATIVE = (
    "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_"
    "v006.json"
)
FENCED_RELATIVES = ("stage8_execution/work", "provenance")
AT_REST_MODE = 0o555
LANES = ("independent", "primary", "comparison")
LANE_RECEIPT_RELATIVES = {
    "independent": (
        "provenance/"
        "stage8_t7_actual_parent_car_independent_execution_receipt_v001.json"
    ),
    "primary": (
        "provenance/"
        "stage8_t7_actual_parent_car_primary_execution_receipt_v001.json"
    ),
    "comparison": (
        "provenance/"
        "stage8_t7_actual_parent_car_comparison_execution_receipt_v001.json"
    ),
}
LANE_OUTPUT_RELATIVES = {
    "independent": (
        "stage8_execution/work/T07_actual_parent_regulated_car_operator_"
        "response_independent_precomparison_v001.json",
        "stage8_execution/work/T07_actual_parent_regulated_car_operator_"
        "response_independent_precomparison_v001.npz",
    ),
    "primary": (
        "stage8_execution/work/T07_actual_parent_regulated_car_operator_"
        "response_primary_v001.json",
        "stage8_execution/work/T07_actual_parent_regulated_car_operator_"
        "response_primary_v001.npz",
    ),
    "comparison": (
        "stage8_execution/work/T07_actual_parent_regulated_car_operator_"
        "response_comparison_v001.json",
    ),
}
PASS_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED"
COPY_EXCLUDES = (".proof_deps", ".pytest_cache", ".git", ".git_disabled")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def directory_mode(directory: Path) -> int:
    return stat.S_IMODE(directory.stat().st_mode)


def scratch_directory() -> Path:
    base = os.environ.get("STAGE8_T7_TEST_SCRATCH")
    if base:
        Path(base).mkdir(parents=True, exist_ok=True)
    return Path(
        tempfile.mkdtemp(prefix="stage8_t7_real_chain_rehearsal_", dir=base)
    ).resolve()


def copy_workspace(destination_root: Path) -> Path:
    workspace = destination_root / "workspace"
    shutil.copytree(
        ROOT,
        workspace,
        symlinks=True,
        ignore=shutil.ignore_patterns(*COPY_EXCLUDES),
    )
    # The copy starts in the canonical AT-REST state: the fence is live.
    for relative in FENCED_RELATIVES:
        directory = workspace / relative
        require(directory.is_dir(), f"copy is missing {relative}")
        directory.chmod(AT_REST_MODE)
    return workspace


def assert_fence_at_rest(workspace: Path, stage: str) -> None:
    """Verify the closed state by ATTEMPTING A WRITE, not by reading a bit."""
    for relative in FENCED_RELATIVES:
        directory = workspace / relative
        mode = directory_mode(directory)
        require(
            mode == AT_REST_MODE,
            f"{stage}: {relative} is mode {mode:04o}, expected "
            f"{AT_REST_MODE:04o}",
        )
        probe = directory / ".rehearsal_write_probe"
        try:
            probe.write_text("probe\n", encoding="ascii")
        except PermissionError:
            continue
        probe.unlink(missing_ok=True)
        raise RuntimeError(
            f"{stage}: the fence is NOT closed -- a write to {relative} "
            "succeeded"
        )


def launch(workspace: Path, target: str, *arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(workspace / LAUNCHER_RELATIVE),
            target,
            *arguments,
        ],
        cwd=workspace,
        check=False,
        capture_output=True,
        text=True,
    )


def verify_adjacent_seal(workspace: Path, relative: str) -> str:
    path = workspace / relative
    seal = Path(f"{path}.seal.sha256")
    require(path.is_file(), f"expected artifact is absent: {relative}")
    require(seal.is_file(), f"expected artifact seal is absent: {relative}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {relative}")
    digest = sha256(path)
    require(fields[0] == digest, f"seal digest mismatch: {relative}")
    require(fields[1] == path.name, f"seal filename mismatch: {relative}")
    return digest


def run_rehearsal() -> dict[str, Any]:
    started = time.monotonic()
    destination_root = scratch_directory()
    workspace = copy_workspace(destination_root)
    record: dict[str, Any] = {
        "schema": "stage8_t7_real_chain_rehearsal_record_v001",
        "workspace": str(workspace),
        "canonical_root_touched": False,
        "stubs_used": False,
        "monkeypatches_used": False,
        "lanes": {},
    }

    # ---- the fence is live in the copy, before anything runs -------------
    assert_fence_at_rest(workspace, "at rest, before the manifest build")

    # ---- L4: the construction lane builds the G7 manifest deliberately ---
    build = launch(workspace, BUILDER_RELATIVE, "--l4-raise-and-record")
    require(
        build.returncode == 0,
        f"the G7 manifest build failed: {build.stderr[-3000:]}",
    )
    build_summary = json.loads(build.stdout)
    require(
        build_summary["row_count"] == 12,
        f"the G7 manifest has {build_summary['row_count']} rows, expected 12",
    )
    record["manifest_sha256"] = build_summary["manifest_sha256"]
    record["l4_raise_record"] = build_summary.get("l4_raise_record")
    assert_fence_at_rest(workspace, "after the L4 manifest build")

    # ---- probe: a superseded write route cannot write (B3's route set) ---
    # The byte-frozen derive lane, invoked DIRECTLY under launcher v002 --
    # the route escalated as B3 -- with the fence at rest.
    legacy = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(workspace / LEGACY_LAUNCHER_RELATIVE),
            DERIVE_INDEPENDENT_RELATIVE,
        ],
        cwd=workspace,
        check=False,
        capture_output=True,
        text=True,
    )
    for relative in LANE_OUTPUT_RELATIVES["independent"]:
        require(
            not (workspace / relative).exists(),
            "FENCE FAILURE: the superseded launcher-v002 route created "
            f"{relative}",
        )
    record["superseded_route_probe"] = {
        "route": f"{LEGACY_LAUNCHER_RELATIVE} -> {DERIVE_INDEPENDENT_RELATIVE}",
        "returncode": legacy.returncode,
        "blocked": legacy.returncode != 0,
        "artifacts_created": 0,
        "stderr_tail": legacy.stderr[-400:],
    }
    require(
        legacy.returncode != 0,
        "FENCE FAILURE: the superseded launcher-v002 route exited 0",
    )
    assert_fence_at_rest(workspace, "after the superseded-route probe")

    # ---- pre-flight, recorded but NOT offered as startability evidence ---
    preflight = launch(
        workspace, CONTROLLER_RELATIVE, "--lane", "independent", "--preflight-only"
    )
    require(
        preflight.returncode == 0,
        f"pre-flight blocked in the disposable copy: {preflight.stdout}\n"
        f"{preflight.stderr[-3000:]}",
    )
    preflight_summary = json.loads(preflight.stdout)
    require(
        preflight_summary["status"] == "PREFLIGHT_OK",
        f"unexpected pre-flight status: {preflight_summary['status']}",
    )
    require(
        preflight_summary["preflight_ok_is_not_startability_evidence"] is True,
        "the controller no longer discloses that PREFLIGHT_OK is not evidence",
    )
    record["preflight"] = {
        "status": preflight_summary["status"],
        "preconditions": preflight_summary["preconditions"],
        "is_startability_evidence": False,
    }
    assert_fence_at_rest(workspace, "after --preflight-only")

    # ---- THE REHEARSAL: all three lanes, real components, in order -------
    #
    # ORDER OF ASSERTIONS.  The FENCE evidence for every lane is collected
    # FIRST, including for a lane whose own verdict blocks, and the pipeline
    # verdict is asserted LAST.  That separation is deliberate: the fence's
    # adoption probe asks whether the FENCE lets legitimate production
    # through, and that question must be answerable even when the pipeline
    # blocks for a reason the fence has nothing to do with.  Conflating the
    # two would report a numerical failure as a fence failure, or worse,
    # hide a fence failure behind a numerical one.
    for lane in LANES:
        lane_started = time.monotonic()
        completed = launch(workspace, CONTROLLER_RELATIVE, "--lane", lane)
        lane_blocked = completed.returncode != 0
        if lane != "comparison":
            require(
                not lane_blocked,
                f"REHEARSAL FAILED at the {lane} derive lane (returncode "
                f"{completed.returncode}).\nstdout: {completed.stdout[-3000:]}\n"
                f"stderr: {completed.stderr[-6000:]}",
            )
        summary = json.loads(completed.stdout) if completed.stdout.strip() else {}
        if not lane_blocked:
            require(
                summary.get("generation_tag") == "stage8_t7_generation_g7",
                f"{lane} summary does not record generation G7: {summary}",
            )
        # The fence record is emitted on stderr on every exit path.
        fence_records = [
            json.loads(line)
            for line in completed.stderr.splitlines()
            if line.startswith('{"fence_anomalies"')
            or '"stage8_t7_directory_permission_fence_record_v001"' in line
        ]
        require(
            len(fence_records) == 1,
            f"{lane}: expected exactly one fence record on stderr, found "
            f"{len(fence_records)}",
        )
        fence_record = fence_records[0]
        require(
            sorted(fence_record["raised"]) == sorted(FENCED_RELATIVES),
            f"{lane}: the fence was not raised over both directories: "
            f"{fence_record['raised']}",
        )
        require(
            sorted(fence_record["dropped"]) == sorted(FENCED_RELATIVES),
            f"{lane}: the fence was not dropped over both directories: "
            f"{fence_record['dropped']}",
        )
        require(
            all(
                mode == f"{AT_REST_MODE:04o}"
                for mode in fence_record["fence_state_after_drop"].values()
            ),
            f"{lane}: the fence record does not show the at-rest mode after "
            f"the drop: {fence_record['fence_state_after_drop']}",
        )
        assert_fence_at_rest(workspace, f"after the {lane} lane")

        receipt_relative = LANE_RECEIPT_RELATIVES[lane]
        lane_record: dict[str, Any] = {
            "returncode": completed.returncode,
            "blocked": lane_blocked,
            "fence_raised": fence_record["raised"],
            "fence_dropped": fence_record["dropped"],
            "fence_state_after_drop": fence_record["fence_state_after_drop"],
            "wrote_through_the_raised_fence": [],
            "seconds": round(time.monotonic() - lane_started, 1),
        }
        if lane_blocked:
            # A4 IN THE REAL CHAIN: a blocked lane seals NO receipt, so the
            # canonical receipt path stays free and the run is retryable.
            require(
                not (workspace / receipt_relative).exists(),
                "A4 VIOLATION IN THE REAL CHAIN: the blocked "
                f"{lane} lane sealed a receipt at {receipt_relative}",
            )
            require(
                not Path(f"{workspace / receipt_relative}.seal.sha256").exists(),
                f"A4 VIOLATION IN THE REAL CHAIN: the blocked {lane} lane "
                "sealed a receipt seal",
            )
            lane_record["a4_no_receipt_sealed_on_block"] = True
            lane_record["block_reason_tail"] = completed.stderr[-1200:]
            # Whatever the lane's own component DID write through the raised
            # fence is recorded, because that is the fence evidence.
            for relative in LANE_OUTPUT_RELATIVES[lane]:
                if (workspace / relative).exists():
                    lane_record["wrote_through_the_raised_fence"].append(relative)
            record["lanes"][lane] = lane_record
            print(
                f"BLOCKED rehearsal lane {lane} "
                f"({lane_record['seconds']}s) -- fence raise/drop verified, "
                "no receipt sealed (A4)",
                flush=True,
            )
            continue

        receipt_digest = verify_adjacent_seal(workspace, receipt_relative)
        receipt = json.loads(
            (workspace / receipt_relative).read_text(encoding="utf-8")
        )
        require(
            receipt["status"] == "SUCCEEDED",
            f"{lane} receipt does not record SUCCEEDED: {receipt['status']}",
        )
        require(
            receipt["returncode"] == 0,
            f"{lane} receipt records a nonzero returncode",
        )
        require(
            receipt["runtime_launcher"] == LAUNCHER_RELATIVE,
            f"{lane} receipt records the wrong launcher: "
            f"{receipt['runtime_launcher']}",
        )
        require(
            receipt["generation_tag"] == "stage8_t7_generation_g7",
            f"{lane} receipt does not carry the generation tag",
        )
        require(
            receipt["alpha_computed"] is False
            and receipt["proof_authorized"] is False,
            f"{lane} receipt violated the alpha/proof firewall",
        )
        outputs = {}
        for relative in LANE_OUTPUT_RELATIVES[lane]:
            outputs[relative] = verify_adjacent_seal(workspace, relative)
        lane_record["receipt"] = receipt_relative
        lane_record["receipt_sha256"] = receipt_digest
        lane_record["outputs"] = outputs
        lane_record["wrote_through_the_raised_fence"] = sorted(outputs) + [
            receipt_relative
        ]
        record["lanes"][lane] = lane_record
        print(
            f"PASS rehearsal lane {lane} ({lane_record['seconds']}s)",
            flush=True,
        )

    # ---- THE FENCE ADOPTION PROBE, decided on fence evidence alone -------
    # Fence record item 2 asks whether LEGITIMATE PRODUCTION completes
    # THROUGH the fence.  The answer is decided by whether every lane
    # raised, wrote its component's artifacts, and dropped -- NOT by the
    # pipeline's scientific verdict, which the fence does not influence.
    wrote_through = {
        lane: bool(entry["wrote_through_the_raised_fence"])
        for lane, entry in record["lanes"].items()
    }
    fence_mechanics_clean = all(
        sorted(entry["fence_raised"]) == sorted(FENCED_RELATIVES)
        and sorted(entry["fence_dropped"]) == sorted(FENCED_RELATIVES)
        for entry in record["lanes"].values()
    )
    record["fence_adoption_probe"] = {
        "question": (
            "does legitimate production complete THROUGH the write fence?"
        ),
        "answer": "YES" if (fence_mechanics_clean and all(wrote_through.values()))
        else "NO",
        "evidence": {
            "every_lane_raised_and_dropped_both_directories": (
                fence_mechanics_clean
            ),
            "every_lane_wrote_its_artifacts_through_the_raised_fence": (
                wrote_through
            ),
            "fence_verified_closed_after_every_lane": True,
            "superseded_route_wrote_nothing": True,
        },
        "scope_note": (
            "This probe is about the FENCE. It is NOT a claim that the "
            "pipeline PASSED; the pipeline verdict is asserted separately "
            "below and is independent of the fence."
        ),
    }
    require(
        record["fence_adoption_probe"]["answer"] == "YES",
        "FENCE ADOPTION PROBE FAILED: the fence did not let legitimate "
        f"production through: {json.dumps(record['fence_adoption_probe'])}",
    )

    # ---- THE PIPELINE VERDICT, asserted last and separately --------------
    comparison_output = workspace / LANE_OUTPUT_RELATIVES["comparison"][0]
    require(
        comparison_output.exists(),
        "the comparator produced no output at all; that is neither a PASS "
        "nor a verdict",
    )
    comparison = json.loads(comparison_output.read_text(encoding="utf-8"))
    require(
        comparison["alpha_computed"] is False
        and comparison["proof_authorized"] is False,
        "the comparison output violated the alpha/proof firewall",
    )
    record["comparison_verdict"] = comparison["overall_verdict"]
    record["comparison_reason"] = comparison.get("reason")
    record["alpha_computed"] = False
    record["proof_authorized"] = False
    record["seconds"] = round(time.monotonic() - started, 1)

    # Final state: the copy is left with the fence CLOSED.
    assert_fence_at_rest(workspace, "final state")
    require(
        comparison["overall_verdict"] == PASS_VERDICT,
        "REHEARSAL: the real chain ran end to end and the FENCE PASSED its "
        "adoption probe, but the PIPELINE VERDICT IS NOT A PASS: the "
        f"comparator returned {comparison['overall_verdict']} "
        f"({comparison.get('reason')}). This is a comparator-verdict result, "
        "not a plumbing failure: the fence, the generation coherence, the "
        "launcher, the manifests and the receipt ordering all behaved as "
        "designed. Read the recorded rehearsal JSON above before touching "
        "any tolerance -- the transported-matrix budgets are preregistered "
        "and outcome-blind, and are NOT revisable in response to this "
        f"result.\nFULL RECORD: {json.dumps(record, indent=2, sort_keys=True)}",
    )
    return record


def main() -> int:
    if sys.flags.isolated != 1 or sys.flags.no_site != 1:
        completed = subprocess.run(
            [sys.executable, "-I", "-S", str(SELF), *sys.argv[1:]],
            cwd=ROOT,
            check=False,
        )
        return completed.returncode
    require(PINNED_PYTHON.is_file(), "the pinned runtime python is absent")
    record = run_rehearsal()
    print(json.dumps(record, indent=2, sort_keys=True))
    print("real_chain_rehearsal_passed 1/1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
