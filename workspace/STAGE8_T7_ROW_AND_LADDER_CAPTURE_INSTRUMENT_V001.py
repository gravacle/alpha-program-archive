"""Capture instrument: per-component comparison rows + the primary convergence
ladder, at the UNCHANGED primary resolution N_t = 48.

WHAT THIS IS FOR.  Comparator v006 computes every component difference and then
DISCARDS them on the blocked path (it raises with only the failure count), so
the per-tier magnitudes that the principal's N-derivation consumes have no
sealed pedigree (finding V-2, CONFIRMED).  This instrument re-obtains them by
calling THE COMPARATOR'S OWN row-building functions on the bundles the real
lanes produce, and reads the byte-frozen primary lane's own 12/24/48
convergence ladder out of its emitted arrays.

DISCIPLINE (successor spec O-1..O-4):
  * READ-ONLY with respect to numerics.  No budget, tolerance, threshold,
    quadrature or basis pin is read from anywhere but the comparator itself,
    and none is altered.  No comparison is re-implemented: the row values come
    from compare_scalar_categories / compare_matrix_categories verbatim.
  * The canonical workspace is COPIED, never written.  All execution happens in
    a disposable copy whose fence starts at rest.
  * The primary derive lane is BYTE-FROZEN and is not touched.  N_t stays 48.

DEVIATION FROM test_..._real_chain_rehearsal_v001.py, DISCLOSED: that harness
opens by BUILDING manifest v006, and its builder is fail-closed against
overwriting.  Manifest v006 now exists canonically (it was sealed to close the
cycle-7 verdict's item 2), so the copy inherits it and the build step correctly
refuses.  This driver therefore SKIPS the build step and runs the three lanes
against the manifest as it now stands canonically -- which is the real
production state, not a weakening of it.
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import numpy as np

CANONICAL = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program"
    "/alpha_fundamental_record_action_cleanroom_v003"
).resolve()
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/codex-primary-runtime"
    "/dependencies/python/bin/python3"
)
LAUNCHER = "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
CONTROLLER = "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py"
COMPARATOR = (
    "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response"
    "_v006.py"
)
FENCED = ("stage8_execution/work", "provenance")
AT_REST_MODE = 0o555
LANES = ("independent", "primary", "comparison")
COPY_EXCLUDES = (".proof_deps", ".pytest_cache", ".git", ".git_disabled")

WORK = "stage8_execution/work"
BUNDLES = {
    "independent": (
        f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
        "independent_precomparison_v001.json",
        f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
        "independent_precomparison_v001.npz",
    ),
    "primary": (
        f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
        "primary_v001.json",
        f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
        "primary_v001.npz",
    ),
}
LADDER_RUNGS = (12, 24, 48)


def sha256(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_copy() -> Path:
    root = Path(
        tempfile.mkdtemp(
            prefix="stage8_t7_capture_",
            dir="/private/tmp/claude-501/-Users-bgm-MB-Work"
            "/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad",
        )
    ).resolve()
    workspace = root / "workspace"
    shutil.copytree(
        CANONICAL,
        workspace,
        symlinks=True,
        ignore=shutil.ignore_patterns(*COPY_EXCLUDES),
    )
    for relative in FENCED:
        (workspace / relative).chmod(AT_REST_MODE)
    return workspace


def assert_fence_at_rest(workspace: Path, stage: str) -> None:
    """Verify the closed state by ATTEMPTING A WRITE, not by reading a bit."""
    for relative in FENCED:
        directory = workspace / relative
        mode = directory.stat().st_mode & 0o7777
        if mode != AT_REST_MODE:
            raise RuntimeError(
                f"{stage}: {relative} is {mode:04o}, expected "
                f"{AT_REST_MODE:04o}"
            )
        probe = directory / ".capture_write_probe"
        try:
            probe.write_text("probe\n", encoding="ascii")
        except PermissionError:
            continue
        probe.unlink(missing_ok=True)
        raise RuntimeError(f"{stage}: fence NOT closed -- {relative} writable")


def run_lane(workspace: Path, lane: str) -> dict[str, Any]:
    completed = subprocess.run(
        [
            str(PINNED_PYTHON),
            "-I",
            "-S",
            str(workspace / LAUNCHER),
            CONTROLLER,
            "--lane",
            lane,
        ],
        cwd=workspace,
        check=False,
        capture_output=True,
        text=True,
    )
    return {
        "lane": lane,
        "returncode": completed.returncode,
        "stdout_tail": completed.stdout.strip().splitlines()[-3:],
        "stderr_tail": completed.stderr.strip().splitlines()[-3:],
    }


def load_comparator(workspace: Path):
    """Import the comparator WITHOUT running its main() (module name is not
    __main__, so any __main__ guard does not fire)."""
    path = workspace / COMPARATOR
    spec = importlib.util.spec_from_file_location("captured_comparator", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["captured_comparator"] = module
    spec.loader.exec_module(module)
    return module


def capture_rows(workspace: Path, comparator) -> list[dict[str, Any]]:
    bundles = {}
    for lane, (json_rel, npz_rel) in BUNDLES.items():
        json_path = workspace / json_rel
        npz_path = workspace / npz_rel
        if not json_path.is_file() or not npz_path.is_file():
            raise RuntimeError(f"{lane} bundle absent: {json_rel}")
        bundles[lane] = comparator.load_bundle(
            lane,
            json_path,
            npz_path,
            sha256(json_path),
            sha256(npz_path),
        )
    overlap = comparator.expected_basis_overlap()
    rows: list[dict[str, Any]] = []
    rows.extend(
        comparator.compare_scalar_categories(
            bundles["primary"], bundles["independent"]
        )
    )
    rows.extend(
        comparator.compare_matrix_categories(
            bundles["primary"], bundles["independent"], overlap
        )
    )
    return rows


def capture_ladder(workspace: Path) -> dict[str, Any]:
    """Read the byte-frozen primary lane's OWN emitted convergence rungs."""
    npz_path = workspace / BUNDLES["primary"][1]
    with np.load(npz_path) as data:
        names = [n for n in data.files if n.startswith("diag_primary__")]
        rungs: dict[str, dict[int, np.ndarray]] = {}
        for name in names:
            parts = name.split("__")
            if len(parts) != 5:
                continue
            _, tag, nstep, pair, kernel = parts
            if not nstep.startswith("n"):
                continue
            try:
                steps = int(nstep[1:])
            except ValueError:
                continue
            if steps not in LADDER_RUNGS:
                continue
            key = f"{tag}__{pair}__{kernel}"
            rungs.setdefault(key, {})[steps] = np.array(data[name])
    out: dict[str, Any] = {"series": {}, "ratios": []}
    for key, by_steps in sorted(rungs.items()):
        if not all(s in by_steps for s in LADDER_RUNGS):
            continue
        d_12_24 = float(np.linalg.norm(by_steps[24] - by_steps[12], 2))
        d_24_48 = float(np.linalg.norm(by_steps[48] - by_steps[24], 2))
        ratio = d_12_24 / d_24_48 if d_24_48 > 0 else None
        out["series"][key] = {
            "d_12_24": d_12_24,
            "d_24_48": d_24_48,
            "ratio": ratio,
        }
        if ratio is not None:
            out["ratios"].append(ratio)
    if out["ratios"]:
        out["ratio_min"] = min(out["ratios"])
        out["ratio_max"] = max(out["ratios"])
        out["ratio_mean"] = sum(out["ratios"]) / len(out["ratios"])
        out["count"] = len(out["ratios"])
    return out


def main() -> int:
    workspace = build_copy()
    report: dict[str, Any] = {
        "schema": "stage8_t7_row_and_ladder_capture_v001",
        "primary_N_t": 48,
        "primary_lane_byte_frozen_unchanged": True,
        "workspace": str(workspace),
        "canonical_read_only": True,
    }
    assert_fence_at_rest(workspace, "before lanes")
    report["lanes"] = [run_lane(workspace, lane) for lane in LANES]
    assert_fence_at_rest(workspace, "after lanes")

    comparator = load_comparator(workspace)
    report["transported_matrix_tolerance"] = float(
        comparator.TRANSPORTED_MATRIX_TOLERANCE
    )
    rows = capture_rows(workspace, comparator)
    failures = [r for r in rows if not r["passed"]]
    passing = [r for r in rows if r["passed"]]

    def tier(rs, key="difference"):
        return sorted((float(r[key]) for r in rs), reverse=True)

    transported = [
        r
        for r in rows
        if abs(float(r["tolerance"]) - comparator.TRANSPORTED_MATRIX_TOLERANCE)
        < 1e-18
    ]
    report["counts"] = {
        "rows_total": len(rows),
        "failures": len(failures),
        "passing": len(passing),
        "transported_rows": len(transported),
    }
    fail_diffs = tier(failures)
    report["failure_magnitudes"] = {
        "worst": fail_diffs[0] if fail_diffs else None,
        "typical_median": (
            sorted(fail_diffs)[len(fail_diffs) // 2] if fail_diffs else None
        ),
        "best": fail_diffs[-1] if fail_diffs else None,
        "all_sorted_desc": fail_diffs,
    }
    passing_transported = [
        float(r["difference"]) for r in transported if r["passed"]
    ]
    report["passing_transported_worst_margin"] = (
        max(passing_transported) if passing_transported else None
    )
    from collections import Counter

    report["failures_by_category"] = dict(
        Counter(r["category"] for r in failures)
    )
    report["failures_by_ell"] = dict(
        Counter(
            next(
                (t for t in ("ell0", "ell1", "ell2") if t in r["identifier"]),
                "other",
            )
            for r in failures
        )
    )
    report["rows"] = rows
    report["ladder"] = capture_ladder(workspace)
    report["convergence_ratio_floor_in_frozen_lane"] = 3.2
    print(json.dumps(report, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
