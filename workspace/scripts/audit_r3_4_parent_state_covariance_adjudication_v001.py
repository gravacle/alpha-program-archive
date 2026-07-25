#!/usr/bin/env python3
"""Audit the adopted Parent-State Covariance Principle against live authority."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_SPEC_V001.md"
SPEC_SEAL = ROOT / "R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_SPEC_V001.seal.sha256"
PRINCIPLE = ROOT / "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md"
PRINCIPLE_SEAL = ROOT / "PARENT_STATE_COVARIANCE_PRINCIPLE_V001.seal.sha256"
OUTPUT = ROOT / "results" / "r3_4_parent_state_covariance_adjudication_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_single_seal(path: Path, seal: Path) -> None:
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"Malformed seal: {seal.name}")
    require(fields[1] == path.name, f"Seal path mismatch: {seal.name}")
    require(fields[0] == sha256(path), f"Seal hash mismatch: {path.name}")


def exact_status(path: Path, key: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(true|false)\s*$", re.MULTILINE)
    matches = pattern.findall(path.read_text(encoding="utf-8"))
    require(len(matches) == 1, f"Expected one {key} in {path.name}")
    return matches[0] == "true"


def kron_site(operator: np.ndarray, site: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    for index in range(count):
        result = np.kron(result, operator if index == site else identity)
    return result


def local_parent_negative_control() -> dict:
    """Construct two response-inequivalent local nets satisfying covariance."""
    identity = np.eye(2, dtype=complex)
    x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)

    def parents(count: int) -> tuple[np.ndarray, np.ndarray]:
        h0 = sum(kron_site(x, site, count) for site in range(count))
        h1 = h0.copy()
        for site in range(count - 1):
            left = kron_site(z, site, count)
            right = kron_site(z, site + 1, count)
            h1 += left @ right
        return h0, h1

    h0_4, h1_4 = parents(4)
    h0_5, h1_5 = parents(5)
    observable_4 = kron_site(y, 1, 4)
    observable_5 = np.kron(observable_4, identity)

    def derivation(hamiltonian: np.ndarray, observable: np.ndarray) -> np.ndarray:
        return 1.0j * (hamiltonian @ observable - observable @ hamiltonian)

    d0_4 = derivation(h0_4, observable_4)
    d0_5 = derivation(h0_5, observable_5)
    d1_4 = derivation(h1_4, observable_4)
    d1_5 = derivation(h1_5, observable_5)

    d0_embedding_error = np.linalg.norm(d0_5 - np.kron(d0_4, identity))
    d1_embedding_error = np.linalg.norm(d1_5 - np.kron(d1_4, identity))
    response_difference = np.linalg.norm(d1_4 - d0_4)

    trace_state_4 = np.eye(2**4, dtype=complex) / (2**4)
    trace_state_5 = np.eye(2**5, dtype=complex) / (2**5)
    restriction_probe = np.diag(np.arange(1, 2**4 + 1)).astype(complex)
    restricted_4 = np.trace(trace_state_4 @ restriction_probe)
    restricted_5 = np.trace(
        trace_state_5 @ np.kron(restriction_probe, identity)
    )

    return {
        "minimal_net_interior_derivation_error": float(d0_embedding_error),
        "interacting_net_interior_derivation_error": float(d1_embedding_error),
        "compatible_trace_state_restriction_error": float(
            abs(restricted_5 - restricted_4)
        ),
        "two_covariant_parent_responses_differ": bool(response_difference > 1.0),
        "response_difference_frobenius": float(response_difference),
    }


def one_cell_static_check() -> dict:
    c_partial = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    endpoint = np.diag([0.0, 1.0, 0.0]).astype(complex)
    commutator = c_partial @ endpoint - endpoint @ c_partial
    return {
        "endpoint_commutator_frobenius": float(np.linalg.norm(commutator)),
        "expected_sqrt_two_error": float(
            abs(np.linalg.norm(commutator) - math.sqrt(2.0))
        ),
        "completed_label_invariant": bool(np.linalg.norm(commutator) < 1e-13),
    }


def main() -> None:
    verify_single_seal(SPEC, SPEC_SEAL)
    verify_single_seal(PRINCIPLE, PRINCIPLE_SEAL)

    write_v1 = ROOT / "PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V001.md"
    write_v2 = ROOT / "PRIMITIVE_REVERSIBLE_RECORD_WRITE_PRINCIPLE_V002.md"
    flux_v3 = ROOT / "SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md"
    global_parent = ROOT / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
    redundancy = ROOT / "CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md"
    authority = json.loads(
        (ROOT / "CURRENT_AUTHORITY_LEDGER_V013.json").read_text(encoding="ascii")
    )

    redundancy_text = redundancy.read_text(encoding="utf-8")
    current = {
        "write_v1_claimed_adopted": (
            "already adopted Primitive Reversible Record-Write Principle"
            in redundancy_text
        ),
        "write_v2_active_level_1": exact_status(
            write_v2, "candidate_is_active_Level_1_postulate"
        ),
        "complete_physical_write_operator_derived": exact_status(
            flux_v3, "complete_physical_write_operator_derived"
        ),
        "complete_source_record_environment_operator_derived": exact_status(
            flux_v3, "complete_source_record_environment_operator_derived"
        ),
        "connected_preparation_derived": exact_status(
            global_parent, "connected_preparation_derived"
        ),
        "time_dependent_continuum_ordering_derived": exact_status(
            global_parent, "time_dependent_continuum_ordering_derived"
        ),
        "authority_complete_environment_operator": authority[
            "execution_state_additions"
        ]["complete_source_record_environment_operator_derived"],
        "authority_complete_Q_spec": authority["protected_parent_flags"][
            "complete_parameter_free_Q_spec_frozen"
        ],
    }

    static = one_cell_static_check()
    negative = local_parent_negative_control()
    require(static["expected_sqrt_two_error"] < 1e-13, "Static check drifted")
    require(
        negative["minimal_net_interior_derivation_error"] < 1e-13,
        "Minimal local net lost covariance",
    )
    require(
        negative["interacting_net_interior_derivation_error"] < 1e-13,
        "Interacting local net lost covariance",
    )
    require(
        negative["compatible_trace_state_restriction_error"] < 1e-13,
        "Compatible state restriction failed",
    )
    require(
        negative["two_covariant_parent_responses_differ"],
        "Negative-control parents became response equivalent",
    )

    live_parent_complete = (
        current["write_v2_active_level_1"]
        and current["complete_physical_write_operator_derived"]
        and current["complete_source_record_environment_operator_derived"]
        and current["connected_preparation_derived"]
        and current["time_dependent_continuum_ordering_derived"]
        and current["authority_complete_Q_spec"]
        and static["completed_label_invariant"]
    )

    result = {
        "schema": "r3.4-parent-state-covariance-adjudication-v001",
        "spec_sha256": sha256(SPEC),
        "principle_sha256": sha256(PRINCIPLE),
        "seals_verified": True,
        "target_values_used": False,
        "live_authority": current,
        "one_cell_static_parent": static,
        "covariance_nonuniqueness_negative_control": negative,
        "superseded_write_rule_used_by_redundancy_lane": (
            current["write_v1_claimed_adopted"]
            and not current["write_v2_active_level_1"]
        ),
        "parent_state_covariance_alone_selects_unique_parent": False,
        "transport_only_branch_excludes_primitive_pauli_by_adoption": True,
        "pauli_exclusion_derived_from_parent_state_covariance": False,
        "live_parent_supplies_complete_scattering_construction": False,
        "live_parent_complete_under_principle": live_parent_complete,
        "outgoing_recoverability_result_authoritative_unconditionally": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "PARENT_STATE_COVARIANCE_CURRENT_PARENT_BLOCKED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
