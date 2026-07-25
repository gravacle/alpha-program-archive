#!/usr/bin/env python3
"""Fail-closed, target-free mechanical audit of the BID v010 specification."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRINCIPLE = ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V010.md"
MANIFEST = ROOT / "provenance/boundary_incidence_dynamics_preregistration_v010.json"
MATRIX = ROOT / "BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V004.md"
LEDGER = ROOT / "BID_FULL_STACK_REVIEW_LEDGER_V002.md"
BUNDLE = ROOT / "provenance/boundary_incidence_dynamics_spec_bundle_v010.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rational_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                value - scale * basis
                for value, basis in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def fourier_design_audit() -> tuple[int, int, bool]:
    bivectors = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
    momenta = []
    for momentum in product((-1, 0, 1), repeat=4):
        if momentum == (0, 0, 0, 0):
            continue
        if next(value for value in momentum if value) > 0:
            momenta.append(momentum)
    momenta.sort(key=lambda value: (sum(x * x for x in value), value))

    polarizations = []
    for index in range(4):
        vector = [0] * 4
        vector[index] = 1
        polarizations.append(tuple(vector))
    for left, right in combinations(range(4), 2):
        vector = [0] * 4
        vector[left] = vector[right] = 1
        polarizations.append(tuple(vector))

    rows: list[list[Fraction]] = []
    selected: list[list[Fraction]] = []
    topological = [Fraction(0) for _ in range(21)]
    off_diagonal_pairs = list(combinations(range(6), 2))
    for pair in ((0, 3), (1, 4), (2, 5)):
        topological[6 + off_diagonal_pairs.index(pair)] = Fraction(1, 2)

    pluecker_holds = True
    for momentum in momenta:
        for polarization in polarizations:
            bivector = tuple(
                momentum[left] * polarization[right]
                - momentum[right] * polarization[left]
                for left, right in bivectors
            )
            if not any(bivector):
                continue
            row = [Fraction(value * value) for value in bivector]
            row.extend(
                Fraction(2 * bivector[left] * bivector[right])
                for left, right in off_diagonal_pairs
            )
            rows.append(row)
            if sum(value * null for value, null in zip(row, topological)):
                pluecker_holds = False
            if rational_rank(selected + [row]) > len(selected):
                selected.append(row)

    return rational_rank(rows), 21 - rational_rank(rows), pluecker_holds


def levi_civita(indices: tuple[int, int, int, int]) -> int:
    if len(set(indices)) != 4:
        return 0
    inversions = sum(
        indices[left] > indices[right]
        for left in range(4)
        for right in range(left + 1, 4)
    )
    return -1 if inversions % 2 else 1


def hodge_square_audit() -> bool:
    basis = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
    metric = [1, -1, -1, -1]
    hodge = [
        [
            levi_civita((mu, nu, rho, sigma)) * metric[rho] * metric[sigma]
            for rho, sigma in basis
        ]
        for mu, nu in basis
    ]
    square = [
        [sum(hodge[i][k] * hodge[k][j] for k in range(6)) for j in range(6)]
        for i in range(6)
    ]
    return square == [
        [-1 if row == column else 0 for column in range(6)]
        for row in range(6)
    ]


def main() -> int:
    failures: list[str] = []
    for path in (PRINCIPLE, MANIFEST, MATRIX, LEDGER, BUNDLE):
        if not path.is_file():
            failures.append(f"missing required file: {path}")
    if failures:
        print("\n".join(f"FAIL {failure}" for failure in failures))
        return 1

    principle = PRINCIPLE.read_text(encoding="utf-8")
    matrix = MATRIX.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))

    if "PENDING" in manifest["hostile_audit_protocol"]["sha256"]:
        failures.append("matrix hash is still a placeholder")
    if "PENDING" in manifest["hostile_audit_protocol"]["persistent_review_ledger_sha256"]:
        failures.append("ledger hash is still a placeholder")
    if re.search(r"[A-Z0-9_]+_SHA256_PENDING", principle):
        failures.append("principle still contains a hash placeholder")

    protocol = manifest["hostile_audit_protocol"]
    if sha256(ROOT / protocol["path"]) != protocol["sha256"]:
        failures.append("hostile audit matrix hash mismatch")
    if (
        sha256(ROOT / protocol["persistent_review_ledger_path"])
        != protocol["persistent_review_ledger_sha256"]
    ):
        failures.append("persistent review ledger hash mismatch")
    self_audit = manifest["mechanical_specification_audit"]
    if sha256(ROOT / self_audit["path"]) != self_audit["sha256"]:
        failures.append("mechanical specification audit hash mismatch")

    for authority in manifest["pinned_authorities"]:
        if sha256(ROOT / authority["path"]) != authority["sha256"]:
            failures.append(f"authority hash mismatch: {authority['path']}")
    parent = manifest["pinned_postseal_parent"]
    if sha256(ROOT / parent["path"]) != parent["sha256"]:
        failures.append(f"parent hash mismatch: {parent['path']}")

    expected_bundle_paths = {
        PRINCIPLE.relative_to(ROOT).as_posix(),
        MANIFEST.relative_to(ROOT).as_posix(),
        MATRIX.relative_to(ROOT).as_posix(),
        LEDGER.relative_to(ROOT).as_posix(),
        Path(__file__).resolve().relative_to(ROOT).as_posix(),
    }
    bundled_files = {entry["path"]: entry["sha256"] for entry in bundle["files"]}
    if set(bundled_files) != expected_bundle_paths:
        failures.append("specification bundle file set is not the exact frozen set")
    for relative_path, expected_hash in bundled_files.items():
        if sha256(ROOT / relative_path) != expected_hash:
            failures.append(f"specification bundle hash mismatch: {relative_path}")
    if bundle.get("stage") != "SPEC-SEAL-CANDIDATE":
        failures.append("specification bundle has the wrong stage")
    if bundle.get("alpha_computed") is not False:
        failures.append("specification bundle does not keep alpha_computed=false")

    forbidden_targets = {
        "CODATA alpha inverse": r"\b137\.035",
        "decimal alpha": r"\b0\.007297",
        "cosmic endpoint": r"\b17\.543",
    }
    bundle_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (PRINCIPLE, MANIFEST, MATRIX, LEDGER)
    )
    for label, pattern in forbidden_targets.items():
        if re.search(pattern, bundle_text):
            failures.append(f"forbidden target literal present: {label}")

    expected_equivalences = {
        "degree-incidence-root-preserving unitary cell map",
        "orientation reversal",
        "vertex-fiber gauge transformation preserving edge transport",
        "nonzero rescaling of the public-closure constraint covector only, because it leaves the kernel unchanged",
    }
    if set(manifest["allowed_equivalences"]) != expected_equivalences:
        failures.append("allowed equivalences differ from the frozen four-item set")

    markdown_status = {
        key: value == "true"
        for key, value in re.findall(
            r"^([A-Za-z0-9_]+) = (true|false)$", principle, flags=re.MULTILINE
        )
    }
    if markdown_status != manifest["status"]:
        missing = sorted(set(manifest["status"]) - set(markdown_status))
        extra = sorted(set(markdown_status) - set(manifest["status"]))
        changed = sorted(
            key
            for key in set(markdown_status) & set(manifest["status"])
            if markdown_status[key] != manifest["status"][key]
        )
        failures.append(
            f"status parity mismatch: missing={missing}, extra={extra}, changed={changed}"
        )

    result_markers = (
        "_passed",
        "_proved",
        "_computed",
        "_sealed",
        "_authorized",
    )
    for key, value in manifest["status"].items():
        if value and (key.endswith(result_markers) or key == "parent_reproduced_or_corrected"):
            failures.append(f"premature result flag true: {key}")

    matrix_ids = re.findall(r"^\| (A\d\d) \|", matrix, flags=re.MULTILINE)
    expected_ids = [f"A{index:02d}" for index in range(1, 35)]
    if matrix_ids != expected_ids:
        failures.append("audit matrix does not contain exactly A01-A34 in order")

    rank, nullity, pluecker_holds = fourier_design_audit()
    if (rank, nullity, pluecker_holds) != (20, 1, True):
        failures.append(
            "Fourier design audit failed: "
            f"rank={rank}, nullity={nullity}, Pluecker={pluecker_holds}"
        )

    if not hodge_square_audit():
        failures.append("Lorentzian Hodge matrix does not square to -I")

    stages = manifest["review_stage_semantics"]
    required_stage_keys = {
        "specification_seal",
        "core_result_seal",
        "parent_comparison",
        "final_claim_seal",
        "unqualified_SEAL_status_forbidden",
        "required_review_roles_each_stage",
    }
    if set(stages) != required_stage_keys:
        failures.append("review-stage dependency keys are incomplete or expanded")
    if not stages["final_claim_seal"].get("proof_authorized_iff_true"):
        failures.append("proof authorization is not iff FINAL-CLAIM-SEAL")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print("BID_V010_SPECIFICATION_AUDIT=FAIL")
        return 1

    print("Fourier_design_rank=20")
    print("Fourier_design_nullity=1")
    print("Pluecker_topological_null=PASS")
    print("Lorentzian_Hodge_square=PASS")
    print("BID_V010_SPECIFICATION_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
