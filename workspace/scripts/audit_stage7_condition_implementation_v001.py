#!/usr/bin/env python3
"""Audit the Stage-7 review-condition successors without doing physics."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.json"
CANDIDATE = ROOT / "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md"
RESULT = ROOT / "results" / "stage7_condition_implementation_v001.json"

SEALS = (
    "STAGE7_INDEPENDENT_REVIEW_VERDICTS_V001.seal.sha256",
    "STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.seal.sha256",
    "R3_4_CONCURRENT_CELL_SCOPE_ERRATUM_V001.seal.sha256",
    "CAUSAL_DIRECT_LIMIT_RECORD_PRINCIPLE_V002.seal.sha256",
    "FINITE_PARENT_ANALYTIC_AUTHORITY_V001.seal.sha256",
    "EM_DEPENDENCY_ORDER_FREEZE_V001.seal.sha256",
    "STAGE6_PARENT_ACTION_LEDGER_SPEC_V002.seal.sha256",
    "STAGE6_PARENT_ACTION_LEDGER_V002.seal.sha256",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.seal.sha256",
    "STAGE7_CONDITION_IMPLEMENTATION_GATE_SPEC_V001.seal.sha256",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seal_matches(path: Path) -> bool:
    fields = path.read_text().split()
    if len(fields) < 2:
        return False
    target = ROOT / fields[1]
    return target.is_file() and sha256(target) == fields[0]


def has_all(text: str, values: tuple[str, ...]) -> bool:
    return all(value in text for value in values)


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    candidate = CANDIDATE.read_text()
    qstatus = ledger["qspec_component_status"]
    not_derived = ledger["explicitly_not_derived"]

    checks = {
        "successor_authority_seals_match": all(
            seal_matches(ROOT / name) for name in SEALS
        ),
        "C1_source_inclusive_slots_open": all(
            qstatus[name] == "OPEN"
            for name in (
                "source_inclusive_state_projective_limit",
                "infinite_future_source_Moller_limit",
                "source_limit_continuum_regulator_independence",
            )
        ),
        "C1_envelope_ER_A_disclosed": (
            "DISCLOSED_BRANCH_PREMISE"
            in ledger["disclosed_branch_inputs"]["envelope_realization"]
            and "ER-A" in candidate
        ),
        "C1_finite_energy_per_state": (
            qstatus["admitted_finite_energy_excitation_class"]
            == "DEFINED_PER_STATE_THRESHOLD_QUANTIFIERS"
            and "T(psi,delta)" in candidate
            and "No state-uniform threshold time is claimed." in candidate
        ),
        "C1_cell_and_packing_scope": (
            qstatus["admissible_cell_complex_and_packing_class"]
            == "CAUSALLY_SEQUENTIAL_PACKING_NORMALIZATION_FORBIDDEN"
            and "packing-dependent response normalization is forbidden"
            in candidate.lower()
        ),
        "C2_concurrent_scope_withdrawn": (
            not_derived["spacetime_concurrent_exact_record_compatibility"]
            is False
            and has_all(
                candidate,
                (
                    "Spacetime-overlapping concurrent-cell compatibility is not derived.",
                    "causally sequential",
                    "counterexample",
                ),
            )
        ),
        "C3_in_state_disclosed_contour_derived": (
            qstatus["in_state"]
            == "DISCLOSED_STATIONARY_QUASIFREE_BRANCH_STATE"
            and qstatus["CTP_contour"]
            == "FREE_CONTOUR_DERIVED_FROM_DISCLOSED_STATE_INTERACTING_OPEN"
        ),
        "C4_six_premise_classes_visible": (
            len(ledger["adopted_microscopic_principles"]) == 6
            and has_all(
                candidate,
                (
                    "Fundamental Boundary Record Action",
                    "Parent-State Covariance",
                    "Causal Incidence Support",
                    "Boundary Superconnection / Single-Operator Completeness",
                    "Global Boundary Descent / Quasi-Free Completeness",
                    "zero independent bare F^2 compositeness",
                ),
            )
        ),
        "C4_standard_inputs_visible": (
            len(ledger["standard_theory_and_kinematic_inputs"]) == 4
            and has_all(candidate, ("Dirac spinors", "CAR", "CPT", "record axioms"))
        ),
        "C5_analytic_authority_corrected": (
            ledger["derived_parent_and_durability"][
                "common_self_adjoint_domain_and_finite_propagator"
            ]
            is True
            and ledger["derived_parent_and_durability"][
                "smooth_to_sharp_under_L1_operator_norm_hypothesis"
            ]
            is True
            and not_derived["spacelike_disjoint_write_commutation"] is False
            and not_derived["spacelike_swap_independence"] is False
        ),
        "C6_no_intermediate_implementability_claim": (
            qstatus["intermediate_asymptotic_unitary_implementability"]
            == "NOT_CLAIMED_OFF_DIAGONAL_NOT_HILBERT_SCHMIDT"
            and "No unitary implementability of" in candidate
        ),
        "C7_nine_step_order_frozen": (
            len(ledger["EM_dependency_order"]) == 9
            and ledger["stage7_review_conditions"][
                "C7_EM_dependency_order_frozen"
            ]
            is True
        ),
        "all_review_conditions_true": all(
            ledger["stage7_review_conditions"].values()
        ),
        "stage8_not_executed": (
            ledger["stage8_theorem_battery_authored"] is False
            and ledger["stage8_cross_execution_completed"] is False
        ),
        "downstream_authorizations_false": all(
            ledger[name] is False
            for name in (
                "complete_source_inclusive_parent_limit_derived",
                "complete_parameter_free_Q_spec_frozen",
                "physical_Thomson_stiffness_computed",
                "coupling_evaluation_authorized",
                "alpha_computed",
                "proof_authorized",
            )
        ),
        "candidate_contains_no_true_alpha_or_proof": not any(
            value in candidate
            for value in ("alpha_computed = true", "proof_authorized = true")
        ),
    }

    passed = all(checks.values())
    result = {
        "schema": "stage7-condition-implementation-v001",
        "date": "2026-07-24",
        "construction_lane_gate_not_independent_review": True,
        "checks": checks,
        "all_checks_pass": passed,
        "stage8_theorem_battery_authored": False,
        "stage8_cross_execution_completed": False,
        "complete_parameter_free_Q_spec_frozen": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "verdict": (
            "STAGE7_CONDITIONS_C1_C7_IMPLEMENTED_STAGE8_HANDOFF_READY"
            if passed
            else "STAGE7_CONDITION_IMPLEMENTATION_BLOCKED"
        ),
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
