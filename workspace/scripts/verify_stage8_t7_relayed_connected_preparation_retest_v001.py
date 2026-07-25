#!/usr/bin/env python3
"""Independent verifier for the relayed preparation no-go."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_SPEC_V001.md"
REPORT = ROOT / "stage8_execution/work/T07_relayed_connected_preparation_retest.json"
OUT = (
    ROOT
    / "stage8_execution/work/"
    "T07_relayed_connected_preparation_retest_verification.json"
)
SPEC_SHA256 = "47fe0d5f6b97899ae17a5ea682222fd0ca48f81c16d4e581219af64f6135f111"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    report = json.loads(REPORT.read_text())
    # Exact Gram matrix of normalized incidence directions.
    gram = [
        [Fraction(1), Fraction(-1, 2), Fraction(0)],
        [Fraction(-1, 2), Fraction(1), Fraction(-1, 2)],
        [Fraction(0), Fraction(-1, 2), Fraction(1)],
    ]
    expected: dict[str, dict[str, str]] = {}
    in_out: dict[str, str] = {}
    for count in (1, 2, 3):
        coefficient = Fraction(1)
        for index in range(1, count):
            coefficient *= gram[index][index - 1]
        final = count - 1
        expected[f"N{count}"] = {}
        for state in range(3):
            value = coefficient * gram[state][final] * gram[0][state]
            expected[f"N{count}"][f"P{state}"] = str(value)
        trace_value = (
            coefficient * gram[0][final] / 4
        )
        expected[f"N{count}"]["I_over_4"] = str(trace_value)
        in_out[f"N{count}"] = str(coefficient)

    observed = report["P1_P2_exact_baseline_table"]
    checks = {
        "sealed_spec_verified": sha256(SPEC) == SPEC_SHA256,
        "reported_spec_verified": report["spec_sha256"] == SPEC_SHA256,
        "baseline_table_recomputed_from_gram":
            observed["state_expectation_amplitudes"] == expected,
        "in_out_table_recomputed_from_gram":
            observed["off_diagonal_in_out_amplitudes"] == in_out,
        "zero_and_state_dependence_real":
            observed["at_least_one_zero_baseline"] is True
            and observed["state_expectations_not_unique"] is True,
        "in_out_not_substituted":
            observed["in_out_functional_is_not_a_state_expectation"] is True,
        "authority_status_preserved":
            report["P3_state_selection_audit"][
                "ordinary_branch_quasifree_state_status"
            ]
            == "DISCLOSED_BRANCH_STATE"
            and report["P3_state_selection_audit"][
                "unique_physical_charged_in_state_derived"
            ]
            is False,
        "blocked_verdict_matches":
            report["overall_verdict"]
            == "T7_CONNECTED_PREPARATION_BLOCKED_AFTER_RELAY",
        "protected_flags_false":
            report["kappa_record_computed"] is False
            and report["coupling_evaluation_authorized"] is False
            and report["alpha_computed"] is False
            and report["proof_authorized"] is False,
        "no_target_access": report["no_target_access_attestation"] is True,
    }
    output = {
        "schema":
            "stage8_t7_relayed_connected_preparation_retest_verification_v001",
        "pass": all(checks.values()),
        "checks": checks,
        "independent_gram_matrix": [
            [str(value) for value in row] for row in gram
        ],
        "construction_script_imported": False,
    }
    OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
