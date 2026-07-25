#!/usr/bin/env python3
"""Build the v002 content-addressed source-parent regression manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v008.json"
RUNTIME_BUILDER = (
    PROJECT_ROOT / "scripts" / "build_primitive_step6_runtime_snapshot_v008.py"
)
RUNTIME_GATE = PROJECT_ROOT / "primitive_step6_content_addressed_runtime_gate_v006.md"
RUNTIME_WITNESS_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_runtime_witness_verification_v001_execution_manifest.json"
)
RUNTIME_WITNESS_OUTPUT = (
    PROJECT_ROOT
    / "results"
    / "bid_source_parent_runtime_witness_verification_v001.json"
)
RUNTIME_WITNESS_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_runtime_witness_verification_v001_execution_receipt.json"
)
MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_closure_v002_execution_manifest.json"
)
OUTPUT = PROJECT_ROOT / "results" / "bid_source_parent_closure_v002_sealed.json"
RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_closure_v002_execution_receipt.json"
)
TARGET = ROOT / "scripts" / "audit_bid_source_parent_closure_gate_v002.py"
OBLIGATION_ROW = re.compile(
    r"^\| (SP\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$"
)

DOCUMENTS = (
    "BID_SOURCE_PARENT_CLOSURE_GATE_V002.md",
    "BID_CHIRAL_SOURCE_RECORD_INCIDENCE_PARENT_V001.md",
    "BID_CHARGED_HANDLE_ACTIVATION_DERIVATION_V002.md",
    "BID_DISTINGUISHABLE_RECORD_CELL_COMPOSITION_DERIVATION_V001.md",
    "BID_LORENTZ_COVARIANT_SOURCE_BOUNDARY_MAP_DERIVATION_V001.md",
    "BID_GLOBAL_CAR_RECORD_COMPOSITION_DERIVATION_V001.md",
    "BID_SOURCE_DECORATED_FIRST_OPENING_CLASSIFICATION_V001.md",
    "BID_ELEMENTARY_RECORD_HILBERT_FUNCTOR_CLASSIFICATION_V001.md",
    "BID_PRIMITIVE_BOUNDARY_SUPERCONNECTION_CLASSIFICATION_V001.md",
    "BID_FULL_SOURCE_MAP_COMMUTANT_CLASSIFICATION_V001.md",
    "BID_GLOBAL_CAR_CHARGE_AND_ACTIVATION_DERIVATION_V001.md",
    "BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md",
    "BID_GRADED_BOUNDARY_SUPERCONNECTION_REPAIR_V001.md",
    "BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md",
    "BID_FIRST_OPENING_GRAPH_REFINEMENT_QUOTIENT_V001.md",
    "BID_ROOT_INCIDENCE_IDENTITY_DERIVATION_V001.md",
    "BID_COMPLETE_NORMAL_DEPENDENT_ENDPOINT_MAP_CLASSIFICATION_V001.md",
    "BID_COMPLETE_ONE_NORMAL_ZERO_FORM_ENUMERATION_V001.md",
    "BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md",
    "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md",
    "BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md",
    "BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
    "BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md",
    "BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json",
)

AUDITS = (
    "audit_bid_elementary_record_hilbert_functor_classification_v001.py",
    "audit_bid_source_decorated_first_opening_classification_v001.py",
    "audit_bid_charged_handle_activation_v002.py",
    "audit_bid_primitive_boundary_superconnection_classification_v001.py",
    "audit_bid_full_source_map_commutant_classification_v001.py",
    "audit_bid_global_car_charge_and_activation_v001.py",
    "audit_bid_public_record_hilbertization_derivation_v001.py",
    "audit_bid_graded_boundary_superconnection_repair_v001.py",
    "audit_bid_boundary_metric_transport_derivation_v001.py",
    "audit_bid_first_opening_graph_refinement_quotient_v001.py",
    "audit_bid_chiral_source_record_incidence_parent_v001.py",
    "audit_bid_active_handle_control_v001.py",
    "audit_bid_physical_record_amplitude_zero_free_v001.py",
    "audit_bid_many_record_parent_identifiability_v001.py",
    "audit_bid_root_incidence_identity_derivation_v001.py",
    "audit_bid_complete_normal_dependent_endpoint_map_classification_v001.py",
    "audit_bid_complete_one_normal_zero_form_enumeration_v001.py",
    "audit_bid_full_dirac_car_source_typing_v001.py",
    "audit_bid_charged_cellular_cpt_intertwiner_v001.py",
    "audit_bid_axial_phase_cp_reduction_v001.py",
    "audit_bid_unique_charged_controlled_coupling_v001.py",
    "audit_bid_global_boundary_descent_quasi_free_v001.py",
    "audit_bid_lorentzian_source_schur_pole_v001.py",
    "audit_bid_lorentz_covariant_source_boundary_map_v001.py",
    "audit_bid_distinguishable_record_cell_composition_v001.py",
    "audit_bid_global_car_record_composition_v001.py",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cleanroom_content_root(paths: tuple[str, ...]) -> str:
    digest = hashlib.sha256()
    for relative in sorted(paths):
        payload = (ROOT / relative).read_bytes()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(payload).digest())
    return digest.hexdigest()


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def main() -> None:
    for path in (
        RUNTIME,
        RUNTIME_BUILDER,
        RUNTIME_GATE,
        RUNTIME_WITNESS_MANIFEST,
        RUNTIME_WITNESS_OUTPUT,
        RUNTIME_WITNESS_RECEIPT,
        TARGET,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)
    for path in (MANIFEST, OUTPUT, RECEIPT):
        if path.exists():
            raise FileExistsError(f"refusing to overwrite {path}")

    dependency_relatives = (
        DOCUMENTS
        + tuple(f"scripts/{name}" for name in AUDITS)
        + ("scripts/audit_bid_source_parent_closure_gate_v002.py",)
    )
    dependency_paths = tuple(ROOT / relative for relative in dependency_relatives)
    if not all(path.is_file() for path in dependency_paths):
        missing = [str(path) for path in dependency_paths if not path.is_file()]
        raise FileNotFoundError(f"missing sealed dependency: {missing}")

    obligations = {}
    gate_text = (ROOT / DOCUMENTS[0]).read_text(encoding="utf-8")
    for line in gate_text.splitlines():
        match = OBLIGATION_ROW.fullmatch(line.strip())
        if match:
            identifier, _, state, _ = match.groups()
            obligations[identifier] = state.strip()
    if set(obligations) != {f"SP{index:02d}" for index in range(1, 19)}:
        raise RuntimeError("SP01-SP18 inventory is not exact")
    blocking = sorted(
        identifier
        for identifier, state in obligations.items()
        if not state.startswith("PASS")
    )
    if not blocking:
        raise RuntimeError("refusing to seal an unexpectedly closed source parent")

    files = {
        project_relative(path): sha256(path)
        for path in dependency_paths
        + (
            RUNTIME_BUILDER,
            RUNTIME_GATE,
            RUNTIME_WITNESS_MANIFEST,
            RUNTIME_WITNESS_OUTPUT,
            RUNTIME_WITNESS_RECEIPT,
        )
    }
    checks = [
        "structured_status_contradiction_rejection",
        "subordinate_output_contradiction_rejection",
        "subordinate_specific_verdict_enforcement",
        "normal_optimized_source_equivalence",
        "startup_custom_modules_absent",
        "all_known_obligations_retained",
        "two_layer_runtime_witness_verified",
    ]
    exact = {
        "schema": "gravacle.bid-source-parent-regression.v002",
        "known_source_parent_obligations": 18,
        "currently_blocking_obligations": len(blocking),
        "content_root_sha256": cleanroom_content_root(dependency_relatives),
        "content_addressed_runtime_sealed": True,
        "source_parent_closure": False,
        "proof_authorized": False,
        "alpha_computed": False,
    }
    payload = {
        "schema": "gravacle.sealed-target-execution.v002",
        "stage": "bid-source-parent-regression-gate-v002",
        "alpha_computed": False,
        "runtime_snapshot": project_relative(RUNTIME),
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "target_script": project_relative(TARGET),
        "expected_output": project_relative(OUTPUT),
        "execution_receipt": project_relative(RECEIPT),
        "files": files,
        "output_contract": {
            "required_fields": list(exact) + ["checks"],
            "exact_values": exact,
            "required_check_keys": checks,
        },
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(MANIFEST)
    print(f"sealed_dependency_files={len(files)}")
    print(f"currently_blocking_obligations={len(blocking)}")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
