"""PASS-REACHABILITY CONTROL.

ONE QUESTION: CAN THE COMPARATOR PASS?

The comparator's accepting branch has never executed in this program's history.
A detector that has only ever refused is not distinguishable from a broken one.
This control constructs a bundle pair that SHOULD pass on every gate and runs
the REAL comparator, UNMODIFIED, to see whether the PASS verdict is emitted and
sealed and whether the accepting branch runs end to end.

CONSTRUCTION, and why it is honest rather than fabricated:
  the comparator transports the independent lane's matrices into the primary
  basis as  transported = O @ M_ind @ O^H  and compares to M_prim, where O is
  the pinned basis overlap and is UNITARY (the comparator itself gates its
  unitarity residual at 2e-11).  So we build a synthetic INDEPENDENT bundle by
  BACK-TRANSPORTING the real primary bundle:  M_ind := O^H @ M_prim @ O.
  Then transported == M_prim identically, to machine epsilon.
  Unitary conjugation preserves hermiticity, projector identities, spectra,
  traces, operator norms and reconstruction-from-pieces, so the independent
  bundle's own internal gates should still hold.  Nothing is invented: every
  number descends from a real lane's real output by an exact unitary map.

RULE 8: authorized by the principal as a CONTROL, not a mechanism.  It adds no
fence, no generation, no provenance apparatus.  It runs in a disposable copy.
"""

from __future__ import annotations

import hashlib
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
SCRATCH = Path(
    "/private/tmp/claude-501/-Users-bgm-MB-Work"
    "/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad"
)
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
AT_REST = 0o555
WORK = "stage8_execution/work"
IND_JSON = (f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
            "independent_precomparison_v001.json")
IND_NPZ = IND_JSON[:-5] + ".npz"
PRI_JSON = (f"{WORK}/T07_actual_parent_regulated_car_operator_response_"
            "primary_v001.json")
PRI_NPZ = PRI_JSON[:-5] + ".npz"
COPY_EXCLUDES = (".proof_deps", ".pytest_cache", ".git", ".git_disabled")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build_copy() -> Path:
    root = Path(tempfile.mkdtemp(prefix="stage8_t7_passctl_", dir=SCRATCH)).resolve()
    ws = root / "workspace"
    shutil.copytree(CANONICAL, ws, symlinks=True,
                    ignore=shutil.ignore_patterns(*COPY_EXCLUDES))
    for rel in FENCED:
        (ws / rel).chmod(AT_REST)
    return ws


def run_lane(ws: Path, lane: str) -> dict[str, Any]:
    c = subprocess.run(
        [str(PINNED_PYTHON), "-I", "-S", str(ws / LAUNCHER), CONTROLLER,
         "--lane", lane],
        cwd=ws, check=False, capture_output=True, text=True)
    return {"lane": lane, "rc": c.returncode,
            "err_tail": c.stderr.strip().splitlines()[-2:]}


def load_comparator(ws: Path):
    spec = importlib.util.spec_from_file_location("passctl_cmp", ws / COMPARATOR)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["passctl_cmp"] = mod
    spec.loader.exec_module(mod)
    return mod


def synthesise(ws: Path, cmp_mod) -> dict[str, Any]:
    """Back-transport the real primary into a synthetic independent bundle,
    walking each bundle's MANIFEST COMPONENT STRUCTURE (category, identifier)
    rather than matching raw NPZ names -- the two lanes do not share array
    names, which is why the name-matched first attempt converted only 6."""
    O = cmp_mod.expected_basis_overlap()
    Oh = O.conjugate().T
    for rel in FENCED:
        (ws / rel).chmod(0o755)
    for rel in (IND_NPZ, IND_JSON):
        (ws / rel).chmod(0o644)

    ij = json.loads((ws / IND_JSON).read_text())
    pj = json.loads((ws / PRI_JSON).read_text())
    pri = dict(np.load(ws / PRI_NPZ))
    indz = np.load(ws / IND_NPZ)
    out = {k: np.array(v) for k, v in indz.items()}
    indz.close()

    transported, copied, missing = [], [], []
    for cat in cmp_mod.MATRIX_CATEGORIES:
        pmap = pj["manifest"]["matrix_components"][cat]
        imap = ij["manifest"]["matrix_components"][cat]
        for ident in sorted(pmap):
            if ident not in imap:
                missing.append(f"{cat}.{ident}")
                continue
            M = np.array(pri[pmap[ident]])
            if cat == "record_projectors":
                out[imap[ident]] = M            # not transported by the comparator
                copied.append(f"{cat}.{ident}")
            else:
                out[imap[ident]] = Oh @ M @ O   # exact back-transport
                transported.append(f"{cat}.{ident}")
    out[cmp_mod.PINNED_BASIS_OVERLAP_KEY] = O
    np.savez(ws / IND_NPZ, **out)

    for cat in cmp_mod.SCALAR_CATEGORIES:
        if cat in pj["manifest"].get("scalar_components", {}) and cat in ij["manifest"].get("scalar_components", {}):
            for k, v in pj["manifest"]["scalar_components"][cat].items():
                if k in ij["manifest"]["scalar_components"][cat]:
                    ij["manifest"]["scalar_components"][cat][k] = v
    # The comparator gates payload["manifest_sha256"] == canonical_sha256(manifest)
    # (line 901), so the recomputation uses the comparator's OWN function.
    # The bundle self-binds: payload["npz_sha256"] must equal its own NPZ
    # digest (comparator line 829).  A synthetic bundle must describe itself.
    ij["npz_sha256"] = sha256(ws / IND_NPZ)
    ij["manifest_sha256"] = cmp_mod.canonical_sha256(ij["manifest"])
    (ws / IND_JSON).write_text(json.dumps(ij, indent=1, sort_keys=True))

    # The synthetic bundle's ADJACENT SEALS must match its own content; the
    # derive lane's seals describe the bundle we replaced.  A seal that does
    # not match its file is simply a wrong seal.  Rewritten in the disposable
    # copy only.
    for rel in (IND_JSON, IND_NPZ):
        f = ws / rel
        seal = Path(f"{f}.seal.sha256")
        if seal.exists():
            seal.chmod(0o644)
        seal.write_text(f"{sha256(f)}  {f.name}\n", encoding="ascii")
    return {"back_transported": len(transported), "copied_untransported": len(copied),
            "identifiers_missing_in_independent": missing,
            "overlap_unitarity_residual": float(np.linalg.norm(Oh @ O - np.eye(32), 2))}


def main() -> int:
    report: dict[str, Any] = {"schema": "stage8_t7_pass_reachability_control_v001"}
    ws = build_copy()
    report["workspace"] = str(ws)

    report["lanes"] = [run_lane(ws, l) for l in ("independent", "primary")]
    if any(r["rc"] != 0 for r in report["lanes"]):
        report["outcome"] = "LANES_FAILED"
        print(json.dumps(report, indent=1)); return 1

    cmp_mod = load_comparator(ws)
    report["synthesis"] = synthesise(ws, cmp_mod)

    out = ws / f"{WORK}/T07_PASS_REACHABILITY_CONTROL_v001.json"
    for rel in FENCED:
        (ws / rel).chmod(0o755)
    cmd = [str(PINNED_PYTHON), "-I", "-S", str(ws / LAUNCHER), COMPARATOR,
           "--independent-json", str(ws / IND_JSON),
           "--independent-npz", str(ws / IND_NPZ),
           "--primary-json", str(ws / PRI_JSON),
           "--primary-npz", str(ws / PRI_NPZ),
           "--independent-json-sha256", sha256(ws / IND_JSON),
           "--independent-npz-sha256", sha256(ws / IND_NPZ),
           "--primary-json-sha256", sha256(ws / PRI_JSON),
           "--primary-npz-sha256", sha256(ws / PRI_NPZ),
           "--output", str(out),
           "--independent-receipt-sha256", "0" * 64,
           "--primary-receipt-sha256", "0" * 64,
           "--controller-context", "pass_reachability_control"]
    c = subprocess.run(cmd, cwd=ws, check=False, capture_output=True, text=True)
    report["comparator_returncode"] = c.returncode
    report["stderr_tail"] = c.stderr.strip().splitlines()[-3:]
    try:
        result = json.loads(c.stdout)
        report["outcome"] = "COMPARATOR_RETURNED"
        report["overall_verdict"] = result.get("overall_verdict")
        report["comparison_passed"] = result.get("comparison_passed")
        report["component_count"] = result.get("component_count")
        report["component_failure_count"] = result.get("component_failure_count")
        report["accepting_branch_gates_present"] = {
            k: (k in result) for k in
            ("diagnostic_gates", "piece_authenticity", "tied_diagnostics",
             "generator_propagator_lineage", "route1_consistency_falsifier")}
        rows = result.get("component_comparisons") or []
        d = sorted((float(r["difference"]) for r in rows), reverse=True)
        report["worst_component_difference"] = d[0] if d else None
    except Exception:
        report["outcome"] = "COMPARATOR_BLOCKED_OR_UNPARSEABLE"
        report["stdout_tail"] = c.stdout.strip().splitlines()[-4:]
    report["output_written"] = out.is_file()
    report["output_seal_written"] = Path(f"{out}.seal.sha256").is_file()
    for rel in FENCED:
        (ws / rel).chmod(AT_REST)

    print(json.dumps(report, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
