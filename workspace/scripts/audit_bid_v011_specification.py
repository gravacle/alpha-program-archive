#!/usr/bin/env python3
"""Fail-closed, target-free mechanical audit of the BID V011 specification."""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRINCIPLE = ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"
MANIFEST = ROOT / "provenance/boundary_incidence_dynamics_preregistration_v011.json"
MATRIX = ROOT / "BID_CONSOLIDATED_HOSTILE_AUDIT_MATRIX_V005.md"
LEDGER = ROOT / "BID_FULL_STACK_REVIEW_LEDGER_V003.md"
BUNDLE = ROOT / "provenance/boundary_incidence_dynamics_spec_bundle_v011.json"
EVALUATOR = ROOT / "scripts/evaluate_bid_stage_dag_v011.py"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_sha256(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


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


def fourier_design_audit() -> tuple[int, int, bool, Fraction]:
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
    off_diagonal_pairs = list(combinations(range(6), 2))
    topological = [Fraction(0) for _ in range(21)]
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

    topological_frobenius_norm_squared = 6 * Fraction(1, 4)
    rank = rational_rank(rows)
    return rank, 21 - rank, pluecker_holds, topological_frobenius_norm_squared


def real_mode_normalization_audit() -> bool:
    for length in (3, 5, 7):
        count = length**4
        for momentum in ((1, 0, 0, 0), (1, 1, 0, 0), (1, -1, 1, 0)):
            cosine_norm = 0.0
            sine_norm = 0.0
            cross = 0.0
            scale = math.sqrt(2.0 / count)
            for point in product(range(length), repeat=4):
                phase = 2.0 * math.pi * sum(
                    n * x for n, x in zip(momentum, point)
                ) / length
                cosine = scale * math.cos(phase)
                sine = scale * math.sin(phase)
                cosine_norm += cosine * cosine
                sine_norm += sine * sine
                cross += cosine * sine
            if not (
                abs(cosine_norm - 1.0) < 2e-12
                and abs(sine_norm - 1.0) < 2e-12
                and abs(cross) < 2e-12
            ):
                return False
    return True


def direct_sum_negative_control() -> bool:
    lengths = (9, 17, 33, 65, 129)
    kappas = [
        1.0 / (4.0 * length**4 * math.sin(math.pi / length) ** 2)
        for length in lengths
    ]
    scaled = [length**2 * value for length, value in zip(lengths, kappas)]
    target = 1.0 / (4.0 * math.pi**2)
    return (
        all(right < left for left, right in zip(kappas, kappas[1:]))
        and abs(scaled[-1] - target) / target < 2e-4
        and kappas[-1] < 2e-6
    )


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


def acyclic(graph: dict[str, list[str]]) -> bool:
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


def require_substrings(
    failures: list[str], text: str, label: str, required: tuple[str, ...]
) -> None:
    for item in required:
        if item not in text:
            failures.append(f"{label} missing required text: {item}")


def main() -> int:
    failures: list[str] = []
    required_files = (PRINCIPLE, MANIFEST, MATRIX, LEDGER, EVALUATOR, BUNDLE)
    for path in required_files:
        if not path.is_file():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print("BID_V011_SPECIFICATION_AUDIT=FAIL")
        return 1

    principle = PRINCIPLE.read_text(encoding="utf-8")
    matrix = MATRIX.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))

    if manifest.get("schema_version") != 11:
        failures.append("manifest schema_version is not 11")
    if manifest.get("principle") != PRINCIPLE.name:
        failures.append("manifest points to the wrong principle")

    protocol = manifest.get("hostile_audit_protocol", {})
    for key in ("sha256", "persistent_review_ledger_sha256"):
        if not is_sha256(protocol.get(key)):
            failures.append(f"hostile audit protocol {key} is not frozen")
    if is_sha256(protocol.get("sha256")) and (
        sha256(ROOT / protocol["path"]) != protocol["sha256"]
    ):
        failures.append("hostile audit matrix hash mismatch")
    if is_sha256(protocol.get("persistent_review_ledger_sha256")) and (
        sha256(ROOT / protocol["persistent_review_ledger_path"])
        != protocol["persistent_review_ledger_sha256"]
    ):
        failures.append("persistent review ledger hash mismatch")

    self_audit = manifest.get("mechanical_specification_audit", {})
    if not is_sha256(self_audit.get("sha256")):
        failures.append("mechanical audit hash is not frozen")
    elif sha256(ROOT / self_audit["path"]) != self_audit["sha256"]:
        failures.append("mechanical audit hash mismatch")

    for authority in manifest.get("pinned_authorities", []):
        authority_path = ROOT / authority["path"]
        if not authority_path.is_file() or sha256(authority_path) != authority["sha256"]:
            failures.append(f"authority hash mismatch: {authority['path']}")
    parent = manifest.get("pinned_postseal_parent", {})
    parent_path = ROOT / parent.get("path", "")
    if not parent_path.is_file() or sha256(parent_path) != parent.get("sha256"):
        failures.append(f"parent hash mismatch: {parent.get('path')}")

    expected_bundle_paths = {
        path.relative_to(ROOT).as_posix()
        for path in (PRINCIPLE, MANIFEST, MATRIX, LEDGER, Path(__file__), EVALUATOR)
    }
    bundled_files = {entry["path"]: entry["sha256"] for entry in bundle.get("files", [])}
    if set(bundled_files) != expected_bundle_paths:
        failures.append("specification bundle is not the exact V011 six-file set")
    for relative_path, expected_hash in bundled_files.items():
        path = ROOT / relative_path
        if not path.is_file() or sha256(path) != expected_hash:
            failures.append(f"specification bundle hash mismatch: {relative_path}")
    if bundle.get("stage") != "SPEC-SEAL-CANDIDATE":
        failures.append("specification bundle has the wrong stage")
    for marker in (
        "primitive_record_stiffness_computed",
        "physical_Thomson_stiffness_computed",
        "alpha_computed",
        "proof_authorized",
    ):
        if bundle.get(marker) is not False:
            failures.append(f"specification bundle does not keep {marker}=false")

    forbidden_targets = {
        "CODATA alpha inverse": r"\b137\.035",
        "decimal alpha": r"\b0\.007297",
        "cosmic endpoint": r"\b17\.543",
    }
    bundle_text = "\n".join((principle, MANIFEST.read_text(), matrix, ledger))
    for label, pattern in forbidden_targets.items():
        if re.search(pattern, bundle_text):
            failures.append(f"forbidden target literal present: {label}")

    markdown_status = {
        key: value == "true"
        for key, value in re.findall(
            r"^([A-Za-z0-9_]+) = (true|false)$", principle, flags=re.MULTILINE
        )
    }
    if markdown_status != manifest.get("status"):
        failures.append("manifest/markdown authorization-state parity failed")
    result_markers = ("_passed", "_proved", "_computed", "_sealed", "_authorized")
    for key, value in manifest.get("status", {}).items():
        if value and (
            key.endswith(result_markers) or key == "parent_reproduced_or_corrected"
        ):
            failures.append(f"premature result flag true: {key}")

    matrix_ids = re.findall(r"^\| (A\d\d) \|", matrix, flags=re.MULTILINE)
    if matrix_ids != [f"A{index:02d}" for index in range(1, 36)]:
        failures.append("audit matrix does not contain exactly A01-A35 in order")

    rank, nullity, pluecker, top_norm = fourier_design_audit()
    if (rank, nullity, pluecker, top_norm) != (20, 1, True, Fraction(3, 2)):
        failures.append(
            "Fourier/topology audit failed: "
            f"rank={rank}, nullity={nullity}, Pluecker={pluecker}, "
            f"||T_top||^2={top_norm}"
        )
    if not real_mode_normalization_audit():
        failures.append("normalized real sine/cosine mode audit failed")
    if not direct_sum_negative_control():
        failures.append("V010 direct-sum zero-stiffness regression failed")
    if not hodge_square_audit():
        failures.append("Lorentzian Hodge matrix does not square to -I")

    regression = set(manifest.get("v010_regression_firewall", []))
    if len(regression) != 13:
        failures.append("V010 regression firewall does not contain 13 blockers")

    response = manifest.get("record_response_and_normalization_gate", {})
    if "tau>0" not in response.get("admitted_competitors", {}).get("interval", ""):
        failures.append("complete tau>0 competitor family is absent")
    if "c>0" not in response.get("admitted_competitors", {}).get(
        "action_multiplier", ""
    ):
        failures.append("complete c>0 competitor family is absent")
    if response.get("primitive_output") != "kappa_record only":
        failures.append("primitive gate is not restricted to kappa_record")
    if not response.get("extensivity", {}).get("posthoc_volume_factor_forbidden"):
        failures.append("post-hoc extensive factor is not forbidden")
    if response.get("finite_pure_state_kinematics", {}).get(
        "fixes_physical_action_multiplier"
    ):
        failures.append("Fubini-Study still claims to fix physical normalization")

    qspec = manifest.get("complete_Q_spec_gate", {})
    if qspec.get("primitive_equals_Thomson_assumed"):
        failures.append("manifest assumes kappa_record=kappa_Thomson")
    if len(qspec.get("required_contents", [])) < 10:
        failures.append("complete Q_spec inventory is incomplete")
    if qspec.get("alpha_value_evaluated"):
        failures.append("Q_spec gate prematurely evaluates alpha")

    category = manifest.get("record_category", {})
    for required_key in (
        "open_name",
        "open_objects",
        "decorated_objects",
        "open_morphism_rule",
        "decorated_morphism_rule",
        "forgetful_functors",
    ):
        if required_key not in category:
            failures.append(f"record category missing {required_key}")

    semantics = manifest.get("review_stage_semantics", {})
    graph = semantics.get("stage_dependencies", {})
    if not graph or not acyclic(graph):
        failures.append("stage dependency graph is missing or cyclic")
    if "ALPHA-RESULT-SEAL" in graph.get("CORE-RESULT-SEAL", []):
        failures.append("core seal depends on alpha and recreates the V010 cycle")
    if not semantics.get("independent_evaluator_required"):
        failures.append("independent stage evaluator is not required")
    if semantics.get("self_declared_status_has_authority") is not False:
        failures.append("self-declared statuses still have authority")

    holdout = manifest.get("external_holdout_protocol", {})
    if holdout.get("manual_candidate_curation_forbidden") is not True:
        failures.append("manual holdout curation is not forbidden")
    if holdout.get("registry_source_query_cutoff_currently_set") is not True:
        failures.append("holdout registry source/query/cutoff remains unset")
    if holdout.get("future_external_randomness_beacon_required") is not True:
        failures.append("future external randomness beacon is not required")
    if holdout.get("prediction_code_sealed_before_alpha") is not True:
        failures.append("prediction code is not sealed before alpha")

    require_substrings(
        failures,
        principle,
        "principle",
        (
            "V010 direct-sum global ray is a mandatory negative control",
            "Multiplying it afterward by `L^2`, `L^4`, a cell",
            "P_root(L)=P(im J_r,L)",
            "Gamma_(disjoint c)=-log|A_(disjoint c)|=sum_c Gamma_c",
            "kappa_record=kappa_Thomson",
            "V_cell/(ell_mu^2 ell_nu^2)",
            "<M_L,T_top>_F=0",
            "||Rem(p)|| <= C |p|^(2+delta)",
            "It does not output",
            "A hand-curated",
        ),
    )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print("BID_V011_SPECIFICATION_AUDIT=FAIL")
        return 1

    print("V010_direct_sum_zero_stiffness=REPRODUCED_AND_REJECTED")
    print("Fourier_design_rank=20")
    print("Fourier_design_nullity=1")
    print("Pluecker_topological_null=PASS")
    print("T_top_Frobenius_norm_squared=3/2")
    print("Real_mode_normalization=PASS")
    print("Lorentzian_Hodge_square=PASS")
    print("Stage_dependency_graph=ACYCLIC")
    print("BID_V011_SPECIFICATION_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
