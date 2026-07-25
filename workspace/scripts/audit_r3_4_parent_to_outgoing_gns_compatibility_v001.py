#!/usr/bin/env python3
"""Audit the parent-to-outgoing state/dynamics compatibility gate."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_PARENT_TO_OUTGOING_GNS_COMPATIBILITY_SPEC_V001.md"
PROVENANCE = ROOT / "R3_4_PARENT_TO_OUTGOING_GNS_COMPATIBILITY_PROVENANCE_V001.json"
OUTPUT = ROOT / "results" / "r3_4_parent_to_outgoing_gns_compatibility_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_provenance() -> dict:
    provenance = json.loads(PROVENANCE.read_text(encoding="ascii"))
    for authority in provenance["authorities"]:
        path = ROOT / authority["path"]
        require(path.is_file(), f"Missing authority: {authority['path']}")
        require(
            sha256(path) == authority["sha256"],
            f"Authority hash mismatch: {authority['path']}",
        )
    return provenance


def exact_status(path: Path, key: str) -> bool:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(true|false)\s*$", re.MULTILINE)
    matches = pattern.findall(path.read_text(encoding="utf-8"))
    require(len(matches) == 1, f"Expected one {key} status in {path.name}")
    return matches[0] == "true"


def one_cell_checks() -> dict:
    b = np.array(
        [
            [0.0, 0.0, -1.0j],
            [0.0, 0.0, +1.0j],
            [+1.0j, -1.0j, 0.0],
        ],
        dtype=complex,
    )
    r = np.array([1.0, 0.0, 0.0], dtype=complex)
    p = np.array([0.0, 1.0, 0.0], dtype=complex)
    p_projector = np.outer(p, p.conjugate())
    commutator = b @ p_projector - p_projector @ b
    eigenvalues, eigenvectors = np.linalg.eigh(b)
    tau = math.pi / math.sqrt(2.0)
    unitary = (
        eigenvectors
        @ np.diag(np.exp(-1.0j * tau * eigenvalues))
        @ eigenvectors.conjugate().T
    )
    evolved_p = unitary @ p
    evolved_r = unitary @ r

    test_observable = np.array(
        [
            [0.2, 0.3 + 0.1j, -0.2j],
            [0.3 - 0.1j, -0.4, 0.5],
            [0.2j, 0.5, 0.7],
        ],
        dtype=complex,
    )
    identity = np.eye(3, dtype=complex)
    b_disjoint = np.kron(b, identity) + np.kron(identity, b)
    a_embedded = np.kron(test_observable, identity)
    lhs = b_disjoint @ a_embedded - a_embedded @ b_disjoint
    rhs = np.kron(
        b @ test_observable - test_observable @ b,
        identity,
    )

    return {
        "c_partial_hermitian": bool(np.allclose(b, b.conjugate().T, atol=1e-14)),
        "endpoint_projector_commutator_frobenius": float(
            np.linalg.norm(commutator)
        ),
        "completed_label_stationary_under_static_parent": bool(
            np.linalg.norm(commutator) < 1e-13
        ),
        "tau_R": tau,
        "evolved_p_to_root_error": float(np.linalg.norm(evolved_p - r)),
        "evolved_root_to_p_error": float(np.linalg.norm(evolved_r - p)),
        "disjoint_derivation_embedding_error": float(np.linalg.norm(lhs - rhs)),
        "disjoint_static_derivation_compatible": bool(
            np.linalg.norm(lhs - rhs) < 1e-13
        ),
    }


def main() -> None:
    verify_provenance()

    fundamental = ROOT / "FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md"
    global_parent = ROOT / "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md"
    ray = ROOT / "CAUSAL_DIRECT_LIMIT_COVECTOR_RAY_LIFT_RESULT_V001.md"
    underdetermination = ROOT / "COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md"
    source_gate = ROOT / "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md"

    inherited = {
        "complete_Q_spec_frozen": exact_status(
            fundamental, "complete_parameter_free_Q_spec_frozen"
        ),
        "finite_global_one_particle_parent_constructed": exact_status(
            global_parent, "global_operator_valued_one_particle_superconnection_constructed"
        ),
        "time_dependent_continuum_ordering_derived": exact_status(
            global_parent, "time_dependent_continuum_ordering_derived"
        ),
        "connected_preparation_derived": exact_status(
            global_parent, "connected_preparation_derived"
        ),
        "quasilocal_state_limit_derived": exact_status(
            ray, "quasilocal_state_limit_derived"
        ),
        "outgoing_record_algebra_subobligation_closed": exact_status(
            ray, "outgoing_record_algebra_subobligation_closed"
        ),
        "unique_covariant_spectral_measure_derived": exact_status(
            ray, "unique_covariant_spectral_measure_derived"
        ),
        "response_inequivalent_parent_actions_survive": exact_status(
            underdetermination,
            "current_premises_admit_two_response_inequivalent_parent_actions",
        ),
        "complete_parent_action_uniquely_derived": exact_status(
            underdetermination, "complete_parent_action_uniquely_derived"
        ),
        "complete_relativistic_source_parent_derived": exact_status(
            source_gate, "complete_relativistic_source_parent_derived"
        ),
    }

    one_cell = one_cell_checks()
    require(one_cell["c_partial_hermitian"], "One-cell generator lost Hermiticity")
    require(
        one_cell["evolved_p_to_root_error"] < 1e-12,
        "Finite recurrence negative control changed",
    )
    require(
        one_cell["evolved_root_to_p_error"] < 1e-12,
        "Finite write negative control changed",
    )
    require(
        one_cell["disjoint_static_derivation_compatible"],
        "Disjoint derivation compatibility failed",
    )

    product_label_states_algebraically_compatible = inherited[
        "quasilocal_state_limit_derived"
    ]
    product_label_state_parent_selected = inherited["connected_preparation_derived"]
    static_parent_preserves_completed_label = one_cell[
        "completed_label_stationary_under_static_parent"
    ]

    all_closure_requirements = (
        inherited["complete_Q_spec_frozen"]
        and inherited["complete_parent_action_uniquely_derived"]
        and inherited["complete_relativistic_source_parent_derived"]
        and inherited["time_dependent_continuum_ordering_derived"]
        and inherited["connected_preparation_derived"]
        and inherited["unique_covariant_spectral_measure_derived"]
        and static_parent_preserves_completed_label
    )

    primary_verdict = (
        "PARENT_TO_OUTGOING_LIMIT_DERIVED"
        if all_closure_requirements
        else (
            "PARENT_LIMIT_UNDERDETERMINED"
            if inherited["response_inequivalent_parent_actions_survive"]
            else "STATIC_PARENT_STATE_DYNAMICS_MISMATCH"
        )
    )

    result = {
        "schema": "r3.4-parent-to-outgoing-gns-compatibility-v001",
        "spec_sha256": sha256(SPEC),
        "provenance_sha256": sha256(PROVENANCE),
        "authorities_verified": True,
        "target_values_used": False,
        "inherited_status": inherited,
        "one_cell_static_parent_checks": one_cell,
        "product_label_states_algebraically_compatible": (
            product_label_states_algebraically_compatible
        ),
        "product_label_state_selected_by_complete_parent": (
            product_label_state_parent_selected
        ),
        "static_parent_preserves_completed_public_label": (
            static_parent_preserves_completed_label
        ),
        "disjoint_static_parent_embeddings_compatible": one_cell[
            "disjoint_static_derivation_compatible"
        ],
        "connected_parent_state_and_dynamics_compatible": False,
        "inductive_limit_parent_selected_state_derived": False,
        "strongly_continuous_parent_selected_GNS_dynamics_derived": False,
        "nonzero_parent_selected_root_in_generator_form_domain_derived": False,
        "compact_write_defect_or_causal_switch_off_derived": False,
        "bound_and_point_spectrum_inventory_closed": False,
        "parent_derived_root_spectral_measure_computed": False,
        "static_parent_verdict": (
            "STATIC_PARENT_LABEL_NOT_INVARIANT"
            if not static_parent_preserves_completed_label
            else "STATIC_PARENT_LABEL_INVARIANT"
        ),
        "primary_verdict": primary_verdict,
        "parent_to_outgoing_limit_derived": all_closure_requirements,
        "requires_parent_derived_resolution": [
            "causal post-write decoupling",
            "invariant pointer or superselection algebra",
            "parent-derived scattering or outgoing state",
        ],
        "hypothesis_promoted_to_principle": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "PARENT_LIMIT_UNDERDETERMINED_STATIC_LABEL_MISMATCH",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
