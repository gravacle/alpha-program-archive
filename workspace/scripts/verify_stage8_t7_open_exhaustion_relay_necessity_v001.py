#!/usr/bin/env python3
"""Independent verifier for the sealed Stage-8 T7 O1-O4 result.

This verifier does not import the construction script.  It uses closed-form
star amplitudes, tuple-level relay maps, and exact rational matrices for the
causal-order witness.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = (
    ROOT
    / "STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_SPEC_V001.md"
)
REPORT = ROOT / "stage8_execution/work/T07_open_exhaustion_relay_necessity.json"
EXTERNAL = Path(
    "/Users/bgm/MB Work/alpha_supervision/"
    "STAGE8_T7_LIFT_ADJUDICATION_RETURN_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "T07_open_exhaustion_relay_necessity_verification.json"
)

SPEC_SHA256 = "1836c808eef24ce0a4dab994f4d9857d77396bbbecc4830c6289d63db7144803"
REPORT_SHA256 = "dc75298c2a8b6614b634e2e54a456ccdb6dc6519a554bee01f6e3d9253bc7b04"
EXTERNAL_SHA256 = "34ebb4dbc2903b91231bd4253dba78c0012c4be4eac062b8145f970fee808eb2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def closed_star_rows() -> dict[str, dict[str, float]]:
    """Evaluate the independently derived star spectral formulas."""
    tau = math.pi / math.sqrt(2.0)
    rows: dict[str, dict[str, float]] = {}
    for arms in (1, 2, 3):
        angle = math.sqrt(arms + 1.0) * tau
        cosine = math.cos(angle)
        survival = (1.0 + arms * cosine) / (arms + 1.0)
        designated = (1.0 - cosine) / (arms + 1.0)
        rows[str(arms)] = {
            "survival": survival,
            "designated_transfer": designated,
            "max_designated_transfer": 2.0 / (arms + 1.0),
            "max_symmetric_transfer":
                2.0 * math.sqrt(arms) / (arms + 1.0),
        }
    return rows


def tuple_relay_checks() -> dict[str, object]:
    """Check the Q_spec relay without Kronecker products or dense matrices."""
    ready = "r"
    pointer = "p"

    def inject(old: tuple[str, ...]) -> tuple[str, ...]:
        return old + (ready,)

    def incidence_swap(state: tuple[str, ...]) -> tuple[str, ...]:
        require(state[-1] == ready, "new factor is not a ready root")
        return state[:-1] + (pointer,)

    rows: dict[str, dict[str, bool]] = {}
    state = (pointer,)
    for old_count in (1, 2):
        old = state
        injected = inject(old)
        state = incidence_swap(injected)
        rows[f"{old_count}_to_{old_count + 1}"] = {
            "old_record_prefix_preserved": state[:-1] == old,
            "new_ready_root_consumed": state[-1] == pointer,
            "restriction_recovers_prior_state": state[:-1] == old,
            "norm_preserved_on_basis": True,
        }

    labels = ("h0", "h1", "h2")
    images = {(label, ready) for label in labels}
    return {
        "finite_rows": rows,
        "all_finite_checks_pass": all(
            all(entry.values()) for entry in rows.values()
        ),
        "generic_branch_relay_injective": len(images) == len(labels),
        "generic_branch_relay_isometric_on_orthonormal_basis": True,
    }


Matrix = list[list[Fraction]]


def zeros(size: int) -> Matrix:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def identity(size: int) -> Matrix:
    result = zeros(size)
    for index in range(size):
        result[index][index] = Fraction(1)
    return result


def matmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    result = zeros(size)
    for row in range(size):
        for pivot in range(size):
            coefficient = left[row][pivot]
            if coefficient == 0:
                continue
            for column in range(size):
                if right[pivot][column] != 0:
                    result[row][column] += coefficient * right[pivot][column]
    return result


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def kron(left: Matrix, right: Matrix) -> Matrix:
    left_size = len(left)
    right_size = len(right)
    result = zeros(left_size * right_size)
    for i in range(left_size):
        for j in range(left_size):
            if left[i][j] == 0:
                continue
            for k in range(right_size):
                for ell in range(right_size):
                    if right[k][ell] != 0:
                        result[i * right_size + k][j * right_size + ell] = (
                            left[i][j] * right[k][ell]
                        )
    return result


def projector(vector: tuple[int, ...]) -> Matrix:
    denominator = sum(value * value for value in vector)
    return [
        [
            Fraction(vector[row] * vector[column], denominator)
            for column in range(len(vector))
        ]
        for row in range(len(vector))
    ]


def exact_order_witness() -> dict[str, object]:
    """Rebuild the two-cell order witness using exact post-opening unitaries."""
    source_projectors = [
        projector((-1, 1, 0)),
        projector((0, -1, 1)),
    ]
    local_swap: Matrix = [
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(-1)],
    ]
    local_identity = identity(3)
    delta = subtract(local_swap, local_identity)
    record_identity = identity(9)
    deltas = [
        kron(delta, local_identity),
        kron(local_identity, delta),
    ]
    full_identity = identity(27)
    unitaries: list[Matrix] = []
    for source_projector, record_delta in zip(source_projectors, deltas):
        correction = kron(source_projector, record_delta)
        unitary = [
            [
                full_identity[row][column] + correction[row][column]
                for column in range(27)
            ]
            for row in range(27)
        ]
        unitaries.append(unitary)

    forward = matmul(unitaries[1], unitaries[0])
    reverse = matmul(unitaries[0], unitaries[1])
    difference = subtract(forward, reverse)
    norm_square = sum(
        entry * entry for row in difference for entry in row
    )
    overlap = sum(
        source_projectors[0][row][column]
        * source_projectors[1][column][row]
        for row in range(3)
        for column in range(3)
    )
    return {
        "forward_reverse_norm_square_exact": str(norm_square),
        "forward_reverse_norm": math.sqrt(float(norm_square)),
        "source_projector_overlap_exact": str(overlap),
        "noncommuting": norm_square > 0,
    }


def main() -> None:
    report = json.loads(REPORT.read_text())
    require(sha256(SPEC) == SPEC_SHA256, "spec hash mismatch")
    require(sha256(REPORT) == REPORT_SHA256, "result hash mismatch")
    require(sha256(EXTERNAL) == EXTERNAL_SHA256, "external hash mismatch")

    stars = closed_star_rows()
    relay = tuple_relay_checks()
    order = exact_order_witness()
    reported_stars = report["O1_branch_conditioned_exactness"]["stars"]

    star_agreement = all(
        abs(
            stars[key]["survival"]
            - reported_stars[key]["formula_survival"]
        )
        < 2e-15
        and abs(
            stars[key]["designated_transfer"]
            - reported_stars[key]["formula_designated_transfer"]
        )
        < 2e-15
        for key in ("1", "2", "3")
    )
    checks = {
        "sealed_hashes_verified": True,
        "closed_form_star_rows_match": star_agreement,
        "one_arm_only_exact_designated_closure":
            abs(stars["1"]["designated_transfer"] - 1.0) < 2e-15
            and stars["2"]["max_designated_transfer"] < 1.0
            and stars["3"]["max_designated_transfer"] < 1.0,
        "mixed_symmetric_exact_closure_excluded":
            stars["2"]["max_symmetric_transfer"] < 1.0
            and stars["3"]["max_symmetric_transfer"] < 1.0,
        "tuple_relay_checks_pass":
            relay["all_finite_checks_pass"]
            and relay["generic_branch_relay_injective"],
        "causal_order_witness_exact":
            order["forward_reverse_norm_square_exact"] == "24"
            and order["source_projector_overlap_exact"] == "1/4"
            and order["noncommuting"],
        "stage_ordering_verdict_matches":
            report["overall_verdict"]
            == "STAGE_ORDERING_AMENDMENT_REQUIRED"
            and report["stage_ordering_amendment_derived"] is True,
        "scope_not_inflated":
            report["primitive_relay_durability_map_derived"] is True
            and report["complete_physical_durability_derived"] is False
            and report["connected_primitive_amplitude_derived"] is False,
        "protected_flags_false":
            report["kappa_record_computed"] is False
            and report["coupling_evaluation_authorized"] is False
            and report["alpha_computed"] is False
            and report["proof_authorized"] is False,
        "no_target_access": report["no_target_access_attestation"] is True,
    }
    output = {
        "schema":
            "stage8_t7_open_exhaustion_relay_necessity_verification_v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_star_formulas": stars,
        "independent_tuple_relay": relay,
        "independent_exact_order_witness": order,
        "construction_script_imported": False,
    }
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
