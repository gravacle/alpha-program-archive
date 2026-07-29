#!/usr/bin/env python3
"""Corpus process gate for the alpha-program archive.

This checker renders process invariants in code. It reports and blocks; it never
rules, adopts, retires, repairs, or seals anything. A checker that could rule
would be a checker that could fit.

The checker does not compute or read physical values. It refuses to open
``a32_holdout/custodian_private`` under any circumstance. All load-bearing checks
use unconditional control flow; no Python ``assert`` statements are used because
assertions disappear under ``python -O``.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

CHECKS = (
    "seal_integrity",
    "deploy_state",
    "substring_certification",
    "hardcoded_claim_flags",
    "voided_pass",
    "marker_prefix_collision",
    "superseded_path_hardwire",
    "fingerprint_currency",
    "scope_declaration",
    "relay_sequence_head",
    "authority_currency",
)
RED_CHECKS = {
    "seal_integrity",
    "deploy_state",
    "voided_pass",
    "marker_prefix_collision",
    "fingerprint_currency",
    "authority_currency",
}
YELLOW_CHECKS = {
    "substring_certification",
    "hardcoded_claim_flags",
    "superseded_path_hardwire",
    "scope_declaration",
    "relay_sequence_head",
}
DEFAULT_BASELINE = "corpus_check_baseline_v001.json"
CUSTODIAN_PARTS = ("a32_holdout", "custodian_private")
SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".DS_Store",
}
TEXT_EXTS = {".md", ".txt", ".json", ".jsonl", ".csv", ".py", ".sha256"}
ARTIFACT_EXTS = {".md", ".py", ".json", ".jsonl", ".csv", ".txt"}
NEGATIVE_RE = re.compile(r"\b(zero hits|does not exist|do not exist|nowhere|no such|zero occurrences|0 occurrences|not found)\b", re.I)
SCOPE_RE = re.compile(r"\b(search root|root:|searched|grep|rg |ripgrep|bounded|scope|scoped|within|under /|in /|corpus-wide|cleanroom|workspace|supervision)\b", re.I)
PASS_RE = re.compile(r"\bPASS_[A-Z0-9_]+\b")
FAIL_RE = re.compile(r"\b(FAIL|FAILED|NO_GO|BLOCKED|REFUTED|VOID|VOIDED|INVALID|MISMATCH)\b", re.I)
VERSION_RE = re.compile(r"(?P<stem>[A-Za-z0-9_./-]*?_v)(?P<num>\d{3})(?P<suffix>\.[A-Za-z0-9_.-]+)")
PASTE_RE = re.compile(r"\bPASTE\s*#?\s*(\d+)\b", re.I)
CLAIM_KEY_RE = re.compile(
    r"(pass|fail|closed|derived|computed|verified|authorized|available|current|complete|valid|blocked|proved|exists|sealed|accepted|executed|certified|established|matched|clean|success|ok|status|result)",
    re.I,
)
TEXTY_NAMES = {"text", "body", "content", "contents", "markdown", "report", "report_text", "file_text", "payload_text"}


@dataclass
class Finding:
    path: str
    line: int | None = None
    detail: str = ""

    def as_dict(self) -> dict[str, Any]:
        item: dict[str, Any] = {"path": self.path, "detail": self.detail}
        if self.line is not None:
            item["line"] = self.line
        return item


@dataclass
class CheckResult:
    name: str
    severity: str
    status: str = "GREEN"
    issue_count: int = 0
    metric: int | None = None
    summary: str = ""
    findings: list[Finding] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def as_dict(self, sample_limit: int = 50) -> dict[str, Any]:
        return {
            "name": self.name,
            "severity": self.severity,
            "status": self.status,
            "issue_count": self.issue_count,
            "metric": self.metric,
            "summary": self.summary,
            "details": self.details,
            "findings": [f.as_dict() for f in self.findings[:sample_limit]],
            "truncated_findings": max(0, len(self.findings) - sample_limit),
        }


def safe_rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def is_custodian_path(path: Path) -> bool:
    parts = path.parts
    for idx in range(0, max(0, len(parts) - 1)):
        if parts[idx : idx + 2] == CUSTODIAN_PARTS:
            return True
    return False


def refuse_custodian_root(path: Path) -> None:
    resolved = path.resolve()
    if is_custodian_path(resolved):
        raise SystemExit(f"REFUSING custodian_private root: {resolved}")


def walk_files(roots: Iterable[Path], suffixes: set[str] | None = None) -> Iterable[Path]:
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        refuse_custodian_root(root)
        for dirpath, dirnames, filenames in os.walk(root):
            d = Path(dirpath)
            if is_custodian_path(d):
                dirnames[:] = []
                continue
            dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS and not is_custodian_path(d / name)]
            for filename in filenames:
                p = d / filename
                if is_custodian_path(p):
                    continue
                if suffixes is not None and p.suffix not in suffixes:
                    continue
                resolved = p.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                yield p


def read_text(path: Path) -> str | None:
    if is_custodian_path(path):
        raise RuntimeError(f"refused custodian_private read: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None
    except OSError:
        return None


def sha256_file(path: Path) -> str:
    if is_custodian_path(path):
        raise RuntimeError(f"refused custodian_private hash: {path}")
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_git(root: Path, args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True, check=False)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def roots_from_args(args: argparse.Namespace) -> dict[str, Any]:
    archive = Path(args.archive_root).resolve()
    refuse_custodian_root(archive)
    scan_roots = [archive / "workspace", archive / "supervision", archive / "cleanroom_output", archive / "a32_holdout"]
    scan_roots = [p for p in scan_roots if p.exists()]
    external_supervision = Path(args.supervision_root).resolve() if args.supervision_root else Path("/Users/bgm/MB Work/alpha_supervision")
    supervision_for_authority = external_supervision if external_supervision.exists() else archive / "supervision"
    refuse_custodian_root(supervision_for_authority)
    governing = Path(args.governing_root).resolve() if args.governing_root else archive / "workspace"
    refuse_custodian_root(governing)
    program_root = Path(args.program_root).resolve() if args.program_root else Path("/Users/bgm/Documents/New project/gravity_emergence_evidence_program")
    if program_root.exists():
        refuse_custodian_root(program_root)
    return {
        "archive": archive,
        "scan_roots": scan_roots,
        "governing": governing,
        "supervision": supervision_for_authority,
        "program_root": program_root if program_root.exists() else None,
    }


def check_seal_integrity(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    sidecars = list(walk_files(ctx["scan_roots"], None))
    sidecars = [p for p in sidecars if p.name.endswith(".seal.sha256")]
    for sidecar in sidecars:
        target = sidecar.with_name(sidecar.name[: -len(".seal.sha256")])
        text = read_text(sidecar)
        if text is None:
            findings.append(Finding(safe_rel(sidecar, root), None, "seal sidecar unreadable"))
            continue
        parts = text.split()
        expected = parts[0] if parts else ""
        if len(parts) >= 2:
            named_target = sidecar.parent / Path(parts[1]).name
            if named_target.exists():
                target = named_target
        if not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
            findings.append(Finding(safe_rel(sidecar, root), None, "sidecar does not begin with SHA-256"))
            continue
        if not target.exists():
            findings.append(Finding(safe_rel(sidecar, root), None, f"target missing: {target.name}"))
            continue
        actual = sha256_file(target)
        if actual.lower() != expected.lower():
            findings.append(Finding(safe_rel(sidecar, root), None, f"seal mismatch expected={expected.lower()} actual={actual}"))
    unsealed_by_class: dict[str, int] = {}
    unsealed_samples: dict[str, list[str]] = {}
    for p in walk_files(ctx["scan_roots"], ARTIFACT_EXTS):
        if p.name.endswith(".seal.sha256"):
            continue
        if (p.with_name(p.name + ".seal.sha256")).exists():
            continue
        cls = p.suffix.lstrip(".") or "no_ext"
        unsealed_by_class[cls] = unsealed_by_class.get(cls, 0) + 1
        unsealed_samples.setdefault(cls, [])
        if len(unsealed_samples[cls]) < 20:
            unsealed_samples[cls].append(safe_rel(p, root))
    status = "RED" if findings else "GREEN"
    return CheckResult(
        "seal_integrity",
        "RED",
        status=status,
        issue_count=len(findings),
        summary=f"{len(sidecars)} sidecars checked; {sum(unsealed_by_class.values())} unsealed artifacts listed by class",
        findings=findings,
        details={"unsealed_by_class": unsealed_by_class, "unsealed_samples": unsealed_samples},
    )


def check_deploy_state(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    rc, status, err = run_git(root, ["status", "--porcelain"])
    if rc != 0:
        findings.append(Finding(".", None, f"git status failed: {err}"))
        status_text = ""
    else:
        status_text = status
        if status_text:
            findings.append(Finding(".", None, "working tree not clean"))
    rc2, upstream, _ = run_git(root, ["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"])
    ahead = None
    if rc2 == 0 and upstream:
        rc3, counts, err3 = run_git(root, ["rev-list", "--left-right", "--count", f"{upstream}...HEAD"])
        if rc3 == 0 and counts:
            parts = counts.split()
            if len(parts) == 2:
                ahead = int(parts[1])
                if ahead != 0:
                    findings.append(Finding(".", None, f"archive ahead-count is {ahead}"))
        else:
            findings.append(Finding(".", None, f"ahead-count unavailable: {err3}"))
    else:
        findings.append(Finding(".", None, "no upstream configured"))
    return CheckResult(
        "deploy_state",
        "RED",
        status="RED" if findings else "GREEN",
        issue_count=len(findings),
        summary="archive ahead-count 0 and working tree clean" if not findings else "archive deploy state not clean/current",
        findings=findings,
        details={"ahead_count": ahead, "porcelain": status_text.splitlines()[:50]},
    )


def is_text_read_expr(node: ast.AST) -> bool:
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "read_text":
        return True
    if isinstance(node, ast.Name) and node.id in TEXTY_NAMES:
        return True
    if isinstance(node, ast.Attribute) and node.attr in TEXTY_NAMES:
        return True
    if isinstance(node, ast.Call):
        return any(is_text_read_expr(child) for child in ast.iter_child_nodes(node))
    return False


def script_is_checker(path: Path) -> bool:
    name = path.name.lower()
    return any(word in name for word in ("audit", "check", "verify", "evaluator", "gate"))


def check_substring_certification(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    scripts = [p for p in walk_files(ctx["scan_roots"], {".py"}) if script_is_checker(p)]
    for p in scripts:
        text = read_text(p)
        if text is None:
            continue
        try:
            tree = ast.parse(text, filename=str(p))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare):
                for op, comp in zip(node.ops, node.comparators):
                    if isinstance(op, ast.In) and (is_text_read_expr(comp) or is_text_read_expr(node.left)):
                        findings.append(Finding(safe_rel(p, root), getattr(node, "lineno", None), "substring certification over file text"))
                        break
    return CheckResult(
        "substring_certification",
        "YELLOW",
        status="YELLOW" if findings else "GREEN",
        issue_count=len(findings),
        metric=len(findings),
        summary=f"{len(findings)} substring-certification comparisons over checker-shaped scripts",
        findings=findings,
        details={"scripts_scanned": len(scripts)},
    )


def key_from_node(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def check_hardcoded_claim_flags(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    for p in walk_files(ctx["scan_roots"], {".py"}):
        text = read_text(p)
        if text is None:
            continue
        try:
            tree = ast.parse(text, filename=str(p))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Dict):
                for key_node, value_node in zip(node.keys, node.values):
                    key = key_from_node(key_node) if key_node is not None else None
                    if key and CLAIM_KEY_RE.search(key) and isinstance(value_node, ast.Constant) and isinstance(value_node.value, bool):
                        findings.append(Finding(safe_rel(p, root), getattr(value_node, "lineno", getattr(node, "lineno", None)), f"literal {value_node.value} for claim key {key}"))
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                value = node.value
                if isinstance(value, ast.Constant) and isinstance(value.value, bool):
                    targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                    for target in targets:
                        key = key_from_node(target)
                        if key and CLAIM_KEY_RE.search(key):
                            findings.append(Finding(safe_rel(p, root), getattr(node, "lineno", None), f"literal {value.value} assigned to claim key {key}"))
    return CheckResult(
        "hardcoded_claim_flags",
        "YELLOW",
        status="YELLOW" if findings else "GREEN",
        issue_count=len(findings),
        metric=len(findings),
        summary=f"{len(findings)} literal boolean claim-shaped payload entries or assignments",
        findings=findings,
    )


def check_voided_pass(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    pass_hashes: dict[str, str] = {}
    for p in walk_files(ctx["scan_roots"], TEXT_EXTS):
        if "/results/" not in str(p).replace("\\", "/"):
            continue
        text = read_text(p)
        if text and "PASS" in text:
            pass_hashes[sha256_file(p)] = safe_rel(p, root)
    failure_texts: list[tuple[Path, str]] = []
    for p in walk_files(ctx["scan_roots"], TEXT_EXTS):
        if "/provenance/" not in str(p).replace("\\", "/"):
            continue
        text = read_text(p)
        if text and FAIL_RE.search(text):
            failure_texts.append((p, text))
    findings: list[Finding] = []
    for h, result_path in pass_hashes.items():
        for p, text in failure_texts:
            if h in text:
                findings.append(Finding(result_path, None, f"PASS result hash named in later/provenance failure text: {safe_rel(p, root)}"))
    return CheckResult(
        "voided_pass",
        "RED",
        status="RED" if findings else "GREEN",
        issue_count=len(findings),
        summary=f"{len(pass_hashes)} PASS result hashes checked against {len(failure_texts)} failure-shaped provenance files",
        findings=findings,
    )


def marker_string_contexts(ctx: dict[str, Any]) -> dict[str, list[Finding]]:
    root = ctx["archive"]
    contexts: dict[str, list[Finding]] = {}
    for p in walk_files(ctx["scan_roots"], {".py"}):
        text = read_text(p)
        if text is None:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            if " in " not in line and "report_has" not in line and "marker" not in line:
                continue
            for marker in PASS_RE.findall(line):
                contexts.setdefault(marker, []).append(Finding(safe_rel(p, root), idx, line.strip()[:180]))
    return contexts


def check_marker_prefix_collision(ctx: dict[str, Any]) -> CheckResult:
    contexts = marker_string_contexts(ctx)
    markers = sorted(contexts)
    findings: list[Finding] = []
    for i, a in enumerate(markers):
        for b in markers[i + 1 :]:
            if b.startswith(a) and b != a:
                for ctx_find in contexts.get(a, [])[:5]:
                    findings.append(Finding(ctx_find.path, ctx_find.line, f"acceptance marker {a} is strict prefix of {b} under substring matching"))
                break
    return CheckResult(
        "marker_prefix_collision",
        "RED",
        status="RED" if findings else "GREEN",
        issue_count=len(findings),
        summary=f"{len(markers)} substring-matched PASS markers checked for strict-prefix collisions",
        findings=findings,
    )


def build_existing_paths(ctx: dict[str, Any]) -> set[str]:
    rels: set[str] = set()
    for p in walk_files(ctx["scan_roots"], None):
        for root in ctx["scan_roots"]:
            try:
                rels.add(str(p.relative_to(root)))
            except ValueError:
                continue
        rels.add(p.name)
    return rels


def check_superseded_path_hardwire(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    existing = build_existing_paths(ctx)
    findings: list[Finding] = []
    for p in walk_files(ctx["scan_roots"], {".py", ".md", ".json"}):
        text = read_text(p)
        if text is None:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            for m in VERSION_RE.finditer(line):
                num = int(m.group("num"))
                successor = f"{m.group('stem')}{num + 1:03d}{m.group('suffix')}"
                successor_name = Path(successor).name
                if successor in existing or successor_name in existing:
                    findings.append(Finding(safe_rel(p, root), idx, f"references {m.group(0)} while successor {successor_name} exists"))
    return CheckResult(
        "superseded_path_hardwire",
        "YELLOW",
        status="YELLOW" if findings else "GREEN",
        issue_count=len(findings),
        metric=len(findings),
        summary=f"{len(findings)} vNNN hardwires with vNNN+1 present",
        findings=findings,
    )


def manifest_files(payload: Any) -> dict[str, str] | None:
    if isinstance(payload, dict):
        if isinstance(payload.get("files"), dict):
            files = payload["files"]
            if files and all(isinstance(k, str) and isinstance(v, str) and re.fullmatch(r"[0-9a-fA-F]{64}", v) for k, v in files.items()):
                return dict(files)
        # Common manifest style: direct map path -> hash.
        if payload and all(isinstance(k, str) and isinstance(v, str) and re.fullmatch(r"[0-9a-fA-F]{64}", v) for k, v in payload.items()):
            return dict(payload)
    return None


def check_fingerprint_currency(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    manifests_checked = 0
    for p in walk_files(ctx["scan_roots"], {".json"}):
        text = read_text(p)
        if text is None:
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        files = manifest_files(payload)
        if not files:
            continue
        manifests_checked += 1
        base = p.parent
        if p.parent.name == "results" and p.parent.parent.exists():
            base = p.parent.parent
        for rel, expected in files.items():
            target = base / rel
            if not target.exists():
                target = ctx["archive"] / rel
            if not target.exists() and ctx.get("program_root") is not None:
                target = ctx["program_root"] / rel
            if not target.exists():
                findings.append(Finding(safe_rel(p, root), None, f"tracked file missing: {rel}"))
                continue
            actual = sha256_file(target)
            if actual.lower() != expected.lower():
                findings.append(Finding(safe_rel(p, root), None, f"tracked hash mismatch for {rel}: expected {expected.lower()} actual {actual}"))
    return CheckResult(
        "fingerprint_currency",
        "RED",
        status="RED" if findings else "GREEN",
        issue_count=len(findings),
        summary=f"{manifests_checked} tracked-hash manifests recomputed",
        findings=findings,
    )


def check_scope_declaration(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    findings: list[Finding] = []
    for p in walk_files(ctx["scan_roots"], {".md", ".txt"}):
        text = read_text(p)
        if text is None:
            continue
        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            if not NEGATIVE_RE.search(line):
                continue
            lo = max(0, idx - 6)
            hi = min(len(lines), idx + 5)
            window = "\n".join(lines[lo:hi])
            if not SCOPE_RE.search(window):
                findings.append(Finding(safe_rel(p, root), idx, "negative assertion lacks nearby search-root/scope declaration"))
    return CheckResult(
        "scope_declaration",
        "YELLOW",
        status="YELLOW" if findings else "GREEN",
        issue_count=len(findings),
        metric=len(findings),
        summary=f"{len(findings)} negative assertions without nearby scope declaration",
        findings=findings,
    )


def check_relay_sequence_head(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    max_paste = 0
    occurrences: list[Finding] = []
    by_number: dict[int, int] = {}
    for p in walk_files([ctx["archive"], ctx["supervision"]], {".md", ".txt"}):
        if p.name.startswith("CORPUS_CHECK_REPORT_"):
            continue
        text = read_text(p)
        if text is None:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            for m in PASTE_RE.finditer(line):
                num = int(m.group(1))
                max_paste = max(max_paste, num)
                by_number[num] = by_number.get(num, 0) + 1
                if len(occurrences) < 50:
                    occurrences.append(Finding(safe_rel(p, root), idx, f"PASTE {num}"))
    duplicate_numbers = sorted([num for num, count in by_number.items() if count > 1])
    return CheckResult(
        "relay_sequence_head",
        "YELLOW",
        status="YELLOW" if duplicate_numbers else "GREEN",
        issue_count=len(duplicate_numbers),
        metric=len(duplicate_numbers),
        summary=f"max paste number {max_paste}; {len(duplicate_numbers)} duplicate-number classes",
        findings=occurrences,
        details={"max_paste_number": max_paste, "duplicate_numbers_sample": duplicate_numbers[:50]},
    )


def principal_ruling_files(supervision: Path) -> list[Path]:
    candidates: list[Path] = []
    if not supervision.exists():
        return candidates
    for p in walk_files([supervision], {".md"}):
        name = p.name.upper()
        text = read_text(p) or ""
        head = text[:2500].upper()
        is_decision_name = "PRINCIPAL_DECISION" in name or name.startswith("A32_FREEZE_V")
        is_principal_act = "PROVENANCE: A PRINCIPAL ACT" in head or "PRINCIPAL ACT," in head
        if is_decision_name or is_principal_act:
            if "DRAFT" not in name and "QUEUE" not in name:
                candidates.append(p)
    return sorted(set(candidates))


def check_authority_currency(ctx: dict[str, Any]) -> CheckResult:
    root = ctx["archive"]
    governing_text_parts: list[str] = []
    for p in walk_files([ctx["governing"]], TEXT_EXTS):
        text = read_text(p)
        if text:
            governing_text_parts.append(text)
    governing_text = "\n".join(governing_text_parts)
    findings: list[Finding] = []
    rulings = principal_ruling_files(ctx["supervision"])
    for ruling in rulings:
        h = sha256_file(ruling)
        name = ruling.name
        cited = name in governing_text or h in governing_text or str(ruling) in governing_text
        if not cited:
            findings.append(Finding(safe_rel(ruling, root), None, f"principal ruling not cited by governing chain; sha256={h}"))
    return CheckResult(
        "authority_currency",
        "RED",
        status="RED" if findings else "GREEN",
        issue_count=len(findings),
        summary=f"{len(rulings)} principal ruling files checked against governing chain citations",
        findings=findings,
        details={"supervision_root": str(ctx["supervision"]), "governing_root": str(ctx["governing"])},
    )


CHECK_FUNCS = {
    "seal_integrity": check_seal_integrity,
    "deploy_state": check_deploy_state,
    "substring_certification": check_substring_certification,
    "hardcoded_claim_flags": check_hardcoded_claim_flags,
    "voided_pass": check_voided_pass,
    "marker_prefix_collision": check_marker_prefix_collision,
    "superseded_path_hardwire": check_superseded_path_hardwire,
    "fingerprint_currency": check_fingerprint_currency,
    "scope_declaration": check_scope_declaration,
    "relay_sequence_head": check_relay_sequence_head,
    "authority_currency": check_authority_currency,
}


def selected_checks(args: argparse.Namespace) -> list[str]:
    if args.check:
        requested = []
        for item in args.check:
            requested.extend([part.strip() for part in item.split(",") if part.strip()])
    else:
        requested = list(CHECKS)
    skips: set[str] = set()
    for item in args.skip_check or []:
        skips.update(part.strip() for part in item.split(",") if part.strip())
    unknown = sorted((set(requested) | skips) - set(CHECKS))
    if unknown:
        raise SystemExit(f"unknown check(s): {', '.join(unknown)}")
    return [name for name in requested if name not in skips]


def run_checks(args: argparse.Namespace) -> list[CheckResult]:
    ctx = roots_from_args(args)
    results: list[CheckResult] = []
    for name in selected_checks(args):
        results.append(CHECK_FUNCS[name](ctx))
    return results


def load_baseline(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"baseline JSON is invalid: {path}: {exc}") from exc


def baseline_metrics(results: list[CheckResult]) -> dict[str, int]:
    metrics: dict[str, int] = {}
    for result in results:
        if result.name in YELLOW_CHECKS:
            metrics[result.name] = result.metric if result.metric is not None else result.issue_count
    return metrics


def gate_failures(results: list[CheckResult], baseline: dict[str, Any] | None) -> list[str]:
    failures: list[str] = []
    for result in results:
        if result.name in RED_CHECKS and result.status == "RED":
            failures.append(f"RED {result.name}: {result.issue_count} issue(s)")
    if baseline:
        base_counts = baseline.get("yellow_counts", {})
        for result in results:
            if result.name not in YELLOW_CHECKS:
                continue
            current = result.metric if result.metric is not None else result.issue_count
            if result.name in base_counts and current > int(base_counts[result.name]):
                failures.append(f"YELLOW growth {result.name}: {current} > baseline {base_counts[result.name]}")
    return failures


def report_text(results: list[CheckResult], baseline: dict[str, Any] | None, sample_limit: int) -> str:
    failures = gate_failures(results, baseline)
    lines = [
        "# Corpus Check Report",
        "",
        f"Overall gate verdict: `{'RED' if failures else 'GREEN'}`",
        f"Baseline loaded: `{baseline is not None}`",
        "",
        "This checker reports and blocks process defects only. It never rules, adopts, retires, repairs, seals, or computes physical values.",
        "",
    ]
    if failures:
        lines.append("## Gate Failures")
        lines.append("")
        for failure in failures:
            lines.append(f"- {failure}")
        lines.append("")
    lines.append("## Checks")
    lines.append("")
    for result in results:
        metric = result.metric if result.metric is not None else result.issue_count
        lines.append(f"### {result.name}")
        lines.append("")
        lines.append(f"- severity: `{result.severity}`")
        lines.append(f"- status: `{result.status}`")
        lines.append(f"- issue_count: `{result.issue_count}`")
        lines.append(f"- metric: `{metric}`")
        lines.append(f"- summary: {result.summary}")
        if result.details:
            lines.append(f"- details: `{json.dumps(result.details, sort_keys=True)[:1000]}`")
        if result.findings:
            lines.append("")
            lines.append("Sample findings:")
            for finding in result.findings[:sample_limit]:
                line = f":{finding.line}" if finding.line is not None else ""
                lines.append(f"- `{finding.path}{line}` — {finding.detail}")
            if len(result.findings) > sample_limit:
                lines.append(f"- ... {len(result.findings) - sample_limit} more not shown")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def report_json(results: list[CheckResult], baseline: dict[str, Any] | None, sample_limit: int) -> dict[str, Any]:
    failures = gate_failures(results, baseline)
    return {
        "overall": "RED" if failures else "GREEN",
        "failures": failures,
        "baseline_loaded": baseline is not None,
        "checks": [r.as_dict(sample_limit=sample_limit) for r in results],
        "alpha_computed": False,
        "proof_authorized": False,
    }


def write_baseline(path: Path, results: list[CheckResult]) -> None:
    payload = {
        "baseline": "corpus_check_yellow_counts_v001",
        "date": "2026-07-29",
        "yellow_counts": baseline_metrics(results),
        "red_checks": sorted(RED_CHECKS),
        "yellow_checks": sorted(YELLOW_CHECKS),
        "discipline": "YELLOW classes may not increase; RED classes block in --gate.",
        "alpha_computed": False,
        "proof_authorized": False,
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def selftest(args: argparse.Namespace) -> int:
    script = Path(__file__).resolve()
    base_cmd = [sys.executable, "-B", str(script), "--report", "--format", "json", "--sample-limit", "10"]
    if args.baseline:
        base_cmd.extend(["--baseline", args.baseline])
    base_cmd.extend(["--archive-root", args.archive_root])
    if args.supervision_root:
        base_cmd.extend(["--supervision-root", args.supervision_root])
    if args.governing_root:
        base_cmd.extend(["--governing-root", args.governing_root])
    if args.program_root:
        base_cmd.extend(["--program-root", args.program_root])
    normal = subprocess.run(base_cmd, text=True, capture_output=True, check=False)
    opt_cmd = [sys.executable, "-O", "-B", str(script), *base_cmd[3:]]
    optimized = subprocess.run(opt_cmd, text=True, capture_output=True, check=False)
    if normal.returncode != 0 or optimized.returncode != 0:
        print("SELFTEST FAIL: report command failed under normal or optimized interpreter")
        print(normal.stderr)
        print(optimized.stderr)
        return 1
    try:
        normal_json = json.loads(normal.stdout)
        optimized_json = json.loads(optimized.stdout)
    except json.JSONDecodeError as exc:
        print(f"SELFTEST FAIL: invalid JSON report: {exc}")
        return 1
    normal_verdict = {"overall": normal_json.get("overall"), "failures": normal_json.get("failures"), "checks": [(c.get("name"), c.get("status"), c.get("issue_count"), c.get("metric")) for c in normal_json.get("checks", [])]}
    optimized_verdict = {"overall": optimized_json.get("overall"), "failures": optimized_json.get("failures"), "checks": [(c.get("name"), c.get("status"), c.get("issue_count"), c.get("metric")) for c in optimized_json.get("checks", [])]}
    if normal_verdict != optimized_verdict:
        print("SELFTEST FAIL: verdict changed under python -O")
        print(json.dumps({"normal": normal_verdict, "optimized": optimized_verdict}, indent=2, sort_keys=True))
        return 1
    print("SELFTEST PASS: verdict unchanged under python -O")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run corpus-wide process checks.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--report", action="store_true", help="human-readable report mode; exits 0")
    mode.add_argument("--gate", action="store_true", help="gate mode; exits non-zero on RED or yellow growth")
    mode.add_argument("--selftest", action="store_true", help="prove verdict is unchanged under python -O")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--check", action="append", help="only run named check(s), comma-separated allowed")
    parser.add_argument("--skip-check", action="append", help="skip named check(s), comma-separated allowed")
    parser.add_argument("--archive-root", default=str(Path(__file__).resolve().parent))
    parser.add_argument("--supervision-root", default="/Users/bgm/MB Work/alpha_supervision")
    parser.add_argument("--governing-root", default=None)
    parser.add_argument("--program-root", default="/Users/bgm/Documents/New project/gravity_emergence_evidence_program")
    parser.add_argument("--baseline", default=DEFAULT_BASELINE)
    parser.add_argument("--write-baseline", default=None, help="write frozen yellow baseline from this run")
    parser.add_argument("--sample-limit", type=int, default=20)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if not args.report and not args.gate and not args.selftest:
        args.report = True
    if args.selftest:
        return selftest(args)
    results = run_checks(args)
    baseline_path = Path(args.baseline)
    if not baseline_path.is_absolute():
        baseline_path = Path(args.archive_root) / baseline_path
    baseline = load_baseline(baseline_path)
    if args.write_baseline:
        out = Path(args.write_baseline)
        if not out.is_absolute():
            out = Path(args.archive_root) / out
        write_baseline(out, results)
    if args.format == "json":
        print(json.dumps(report_json(results, baseline, args.sample_limit), indent=2, sort_keys=True))
    else:
        print(report_text(results, baseline, args.sample_limit), end="")
    if args.gate:
        failures = gate_failures(results, baseline)
        if failures:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
