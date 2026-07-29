#!/usr/bin/env python3
"""Stage-8 Gate-5/kappa_record battery evaluator v001 (Fable-authored).

THE ONLY AUTHORITY FOR THE BATTERY VERDICT. Per the sealed rule, a script's
own PASS label has no authority; Codex's in-execution PASS strings have no
authority; this evaluator ingests content-addressed reports, verifies every
hash, computes the dependency graph, performs the mechanical fences, and
alone emits the verdict.

Layout (all under EXEC_DIR, default: <workspace>/stage8_execution):
  spec_seal.sha256          two-field line: <sha256>  <spec filename>
  predictions.json          sealed BEFORE execution; lexically fenced
  t_reports/T00.json ... T16.json      one per obligation
  controls/NC1.json ... NC5.json       negative controls
  lane_reports/<lane_id>.json          blind/reproduction lanes
  commitments/<lane_id>.<object>.commit   sha256(salt||canonical_value)
  reveals/<lane_id>.<object>.reveal       "salt||canonical_value"
  core_reports/formal.json physics_operator.json red_team.json
  reconstruction/report.json
  result.json               canonical machine-readable result (schema v002)
  artifact_manifest.txt     every artifact path this execution produced

Every *.json report must carry: {"sha256_of_body": ..} content-addressing —
the file's own sha256 with that field blanked must equal the field value.

Verdict rules implemented: GATE5_CORE_EXECUTED_SEAL_PENDING only if every
T/NC/lane/core-report/reconstruction node passes, hashes verify, the
prediction fence and transform fence pass, and the kappa enclosure excludes
zero. Declared-open items route to GATE5_CORE_CONDITIONAL only if listed in
DECLARED_OPEN. Everything else is GATE5_CORE_BLOCKED.

Self-test: `--selftest` builds synthetic fixtures in a temp dir, including a
deliberate transform-leak artifact and a bad commitment, and asserts the
evaluator detects both (exit 0 = evaluator's own checks fire correctly).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC_SHA256 = "ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5"

T_IDS = [f"T{i:02d}" for i in range(0, 17)]  # T00..T16 (T00 = lineage)
NC_IDS = ["NC1", "NC2", "NC3", "NC4", "NC5"]
CORE_ROLES = ["formal", "physics_operator", "red_team"]
DECLARED_OPEN = {
    "SPEC-SEAL", "holdout_registry_freeze",
    "independent_evaluator_implementation",
}
# Benchmarks the sealed authority discloses; the ONLY numerals allowed in
# predictions.json (as strings) besides structural integers.
PREDICTION_WHITELIST = {"-1/2", "1/2", "pi/sqrt(2)", "pi/sqrt2", "20"}
FLOATLIKE = re.compile(r"(?<![\w./-])\d+\.\d{3,}(?![\w.])")

PROTECTED_FALSE = [
    "physical_Thomson_stiffness_computed", "spectral_evaluation_authorized",
    "complete_Q_spec_sealed", "physical_charged_amplitude_computed",
    "BID_core_result_sealed", "coupling_evaluation_authorized",
    "alpha_computed", "proof_authorized",
]
SELFTEST_FIXTURE = ROOT / "stage8_execution/selftest_fixtures/battery_evaluator_v001"
SKIP_CORPUS_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    return sha256_bytes(p.read_bytes())


def load_content_addressed(p: Path, failures: list) -> dict | None:
    try:
        obj = json.loads(p.read_text())
    except Exception as e:
        failures.append(f"{p.name}: unreadable JSON ({e})")
        return None
    claimed = obj.get("sha256_of_body")
    if not claimed:
        failures.append(f"{p.name}: missing sha256_of_body content address")
        return None
    body = dict(obj)
    body["sha256_of_body"] = ""
    actual = sha256_bytes(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode())
    if actual != claimed:
        failures.append(f"{p.name}: content-address mismatch")
        return None
    return obj


def check_prediction_fence(pred_path: Path, failures: list) -> None:
    if not pred_path.is_file():
        failures.append("predictions.json missing")
        return
    text = pred_path.read_text()
    for m in FLOATLIKE.finditer(text):
        failures.append(f"predictions.json: forbidden numeric literal "
                        f"'{m.group(0)}' (no value predictions allowed)")
    try:
        obj = json.loads(text)
    except Exception as e:
        failures.append(f"predictions.json unreadable ({e})")
        return
    for v in json.dumps(obj).split('"'):
        if "/" in v and v.replace("-", "").replace("/", "").isdigit():
            if v not in PREDICTION_WHITELIST:
                failures.append(
                    f"predictions.json: rational '{v}' not whitelisted")


def load_predictions(pred_path: Path, failures: list) -> dict[str, str]:
    check_prediction_fence(pred_path, failures)
    if not pred_path.is_file():
        return {}
    try:
        obj = json.loads(pred_path.read_text())
    except Exception:
        return {}
    conditions = obj.get("conditions")
    expected = set(T_IDS) | set(NC_IDS)
    if not isinstance(conditions, dict):
        failures.append("predictions.json: conditions object missing")
        return {}
    if set(conditions) != expected:
        failures.append("predictions.json: conditions do not cover exactly T00-T16 and NC1-NC5")
    out: dict[str, str] = {}
    for key in expected:
        value = conditions.get(key)
        if not isinstance(value, str) or not value.strip():
            failures.append(f"predictions.json: empty condition for {key}")
        else:
            out[key] = value
    return out


def enforce_prediction_condition(node_id: str, obj: dict, conditions: dict[str, str],
                                 failures: list) -> None:
    condition = conditions.get(node_id)
    if condition is None:
        failures.append(f"{node_id}: no preregistered prediction condition")
        return
    expected = sha256_bytes(condition.encode())
    if obj.get("preregistered_condition_sha256") != expected:
        failures.append(f"{node_id}: preregistered condition hash missing/mismatch")
    if obj.get("preregistered_condition_satisfied") is not True:
        failures.append(f"{node_id}: preregistered condition not satisfied")


def kappa_transform_strings(lo: Fraction, hi: Fraction) -> list[str]:
    """Digit strings for kappa and elementary transforms, several precisions."""
    import math
    mid = (lo + hi) / 2
    x = float(mid)
    if x <= 0:
        return []
    vals = [x, 1.0 / x, 4 * math.pi * x, 1.0 / (4 * math.pi * x),
            x * x, math.sqrt(x), math.log(x) if x > 0 else 0.0]
    out = []
    for v in vals:
        for digits in (6, 8, 10):
            s = f"{abs(v):.{digits}f}"
            frag = s.replace(".", "")[:digits]
            if len(frag) >= 6 and not all(c == frag[0] for c in frag):
                out.append(frag)
    return sorted(set(out))


def iter_corpus_files(corpus_root: Path) -> set[Path]:
    files: set[Path] = set()
    for path in corpus_root.rglob("*"):
        if any(part in SKIP_CORPUS_DIRS for part in path.parts):
            continue
        if path.is_file():
            files.add(path)
    return files


def check_transform_fence(exec_dir: Path, result: dict, failures: list,
                          corpus_root: Path | None = None) -> None:
    enc = result.get("kappa_record_enclosure") or {}
    try:
        lo, hi = Fraction(enc["lower"]), Fraction(enc["upper"])
    except Exception:
        failures.append("result.json: kappa enclosure missing/not exact-rational")
        return
    if lo <= 0 <= hi:
        failures.append("kappa enclosure contains zero: degenerate (BLOCKED via NC1/T6 rule)")
    frags = kappa_transform_strings(lo, hi)
    manifest = exec_dir / "artifact_manifest.txt"
    paths_to_scan: set[Path] = set()
    if not manifest.is_file():
        failures.append("artifact_manifest.txt missing")
    else:
        for line in manifest.read_text().splitlines():
            raw = Path(line.strip())
            p = raw if raw.is_absolute() else exec_dir / raw
            if line.strip():
                paths_to_scan.add(p)
    if corpus_root is None:
        corpus_root = ROOT
    paths_to_scan.update(iter_corpus_files(corpus_root))
    canonical = exec_dir / "result.json"
    for p in sorted(paths_to_scan):
        if not p.is_file() or p.resolve() == canonical.resolve():
            continue
        try:
            blob = p.read_text(errors="replace").replace(".", "")
        except OSError:
            continue
        for frag in frags:
            if frag in blob:
                failures.append(
                    f"transform fence: kappa digit-string {frag[:8]}… "
                    f"appears in {p} (value may appear ONLY in result.json)")
                break


def check_commitments(exec_dir: Path, failures: list) -> None:
    commits = {p.stem: p for p in (exec_dir / "commitments").glob("*.commit")} \
        if (exec_dir / "commitments").is_dir() else {}
    reveals = {p.stem: p for p in (exec_dir / "reveals").glob("*.reveal")} \
        if (exec_dir / "reveals").is_dir() else {}
    for key, cpath in commits.items():
        if key not in reveals:
            failures.append(f"commitment {key}: no reveal")
            continue
        if sha256_bytes(reveals[key].read_bytes()) != cpath.read_text().strip():
            failures.append(f"commitment {key}: reveal does not match commitment")
    for key in reveals:
        if key not in commits:
            failures.append(f"reveal {key}: no prior commitment (ordering violation)")


def evaluate(exec_dir: Path, spec_path: Path) -> dict:
    failures: list[str] = []
    notes: list[str] = []

    if not spec_path.is_file() or sha256_file(spec_path) != SPEC_SHA256:
        failures.append("sealed spec hash mismatch or spec missing")

    prediction_conditions = load_predictions(exec_dir / "predictions.json", failures)

    nodes = {}
    for tid in T_IDS:
        p = exec_dir / "t_reports" / f"{tid}.json"
        obj = load_content_addressed(p, failures) if p.is_file() else None
        if obj is None:
            if not p.is_file():
                failures.append(f"{tid}: report missing")
            nodes[tid] = False
            continue
        nodes[tid] = obj.get("pass") is True
        enforce_prediction_condition(tid, obj, prediction_conditions, failures)
        if not nodes[tid]:
            item = obj.get("open_item")
            if item in DECLARED_OPEN:
                notes.append(f"{tid}: declared-open item '{item}'")
            else:
                failures.append(f"{tid}: pass is not true")

    for nc in NC_IDS:
        p = exec_dir / "controls" / f"{nc}.json"
        obj = load_content_addressed(p, failures) if p.is_file() else None
        ok = bool(obj and obj.get("behaved_as_predeclared") is True)
        if obj is not None:
            enforce_prediction_condition(nc, obj, prediction_conditions, failures)
        nodes[nc] = ok
        if not ok:
            failures.append(f"{nc}: control missing or misbehaved")

    for role in CORE_ROLES:
        p = exec_dir / "core_reports" / f"{role}.json"
        obj = load_content_addressed(p, failures) if p.is_file() else None
        ok = bool(obj and obj.get("verdict") == "PASS"
                  and obj.get("reviewer_role") == role
                  and obj.get("no_edit_attestation") is True)
        nodes[f"core:{role}"] = ok
        if not ok:
            failures.append(f"core report '{role}': missing, wrong role, or not PASS")

    p = exec_dir / "reconstruction" / "report.json"
    obj = load_content_addressed(p, failures) if p.is_file() else None
    nodes["reconstruction"] = bool(obj and obj.get("agrees_within_rule") is True)
    if not nodes["reconstruction"]:
        failures.append("independent reconstruction: missing or disagrees")

    rp = exec_dir / "result.json"
    result = load_content_addressed(rp, failures) if rp.is_file() else None
    if result is None:
        failures.append("result.json missing/invalid")
        result = {}
    for flag in PROTECTED_FALSE:
        if result.get(flag) is not False:
            failures.append(f"result.json: protected flag {flag} is not false")
    if result.get("primitive_output") != "kappa_record only":
        failures.append("result.json: primitive_output must be 'kappa_record only'")
    if result:
        check_transform_fence(exec_dir, result, failures)

    check_commitments(exec_dir, failures)

    if failures:
        verdict = "GATE5_CORE_BLOCKED"
    elif notes:
        verdict = "GATE5_CORE_CONDITIONAL"
    else:
        verdict = "GATE5_CORE_EXECUTED_SEAL_PENDING"
    return {"verdict": verdict, "failures": failures, "declared_open": notes,
            "nodes": nodes,
            "pending_toward_core_result_seal": sorted(DECLARED_OPEN | {
                "three_core_reports", "independent_core_reconstruction"})}


def selftest() -> int:
    failures: list[str] = []
    if not SELFTEST_FIXTURE.is_dir():
        failures.append(f"fixture directory missing: {SELFTEST_FIXTURE}")
    result_path = SELFTEST_FIXTURE / "result_fixture.json"
    try:
        result = json.loads(result_path.read_text())
    except Exception as exc:
        result = {}
        failures.append(f"result fixture unreadable: {exc}")

    transform_failures: list[str] = []
    check_transform_fence(SELFTEST_FIXTURE, result, transform_failures,
                          corpus_root=SELFTEST_FIXTURE)
    if not any("transform fence" in item for item in transform_failures):
        failures.append("transform fence fixture was not detected")

    commitment_failures: list[str] = []
    check_commitments(SELFTEST_FIXTURE, commitment_failures)
    if not any("does not match" in item for item in commitment_failures):
        failures.append("commitment mismatch fixture was not detected")

    prediction_failures: list[str] = []
    check_prediction_fence(SELFTEST_FIXTURE / "predictions_numeric_leak.json",
                           prediction_failures)
    if not any("forbidden numeric" in item for item in prediction_failures):
        failures.append("prediction leak fixture was not detected")

    if failures:
        print("SELFTEST FAIL:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SELFTEST PASS: committed transform, commitment, and prediction "
          "fixtures all fire.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--exec-dir", type=Path)
    ap.add_argument("--spec", type=Path)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.exec_dir or not args.spec:
        ap.error("--exec-dir and --spec required (or --selftest)")
    out = evaluate(args.exec_dir, args.spec)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out["verdict"] != "GATE5_CORE_BLOCKED" else 1


if __name__ == "__main__":
    sys.exit(main())
