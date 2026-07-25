#!/usr/bin/env python3
"""Freeze separate normal and optimized source-parent producer manifests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
RUNTIME = PROJECT_ROOT / "provenance" / "primitive_step6_runtime_snapshot_v014.json"
RUNTIME_BUILDER = (
    PROJECT_ROOT / "scripts" / "build_primitive_step6_runtime_snapshot_v014.py"
)
RUNTIME_GATE = PROJECT_ROOT / "primitive_step6_content_addressed_runtime_gate_v012.md"
LAUNCHER = PROJECT_ROOT / "scripts" / "launch_content_addressed_runtime_script_v014.py"
GENERIC_VALIDATION = (
    PROJECT_ROOT
    / "scripts"
    / "validate_content_addressed_runtime_evidence_v014.py"
)
ALIAS_TEST = (
    PROJECT_ROOT / "tests" / "test_content_addressed_runtime_source_namespace_alias_v003.py"
)
MANIFEST_CONTRACT_TEST = (
    PROJECT_ROOT / "tests" / "test_bid_source_parent_terminal_v006_manifest_contract.py"
)
TARGET = ROOT / "scripts" / "audit_bid_source_parent_closure_gate_v003.py"
BUILDER = Path(__file__).resolve()
VERIFIER = ROOT / "scripts" / "verify_bid_source_parent_terminal_children_v006.py"
VERIFIER_BUILDER = (
    ROOT / "scripts" / "build_bid_source_parent_terminal_verifier_manifest_v006.py"
)
SUPERVISOR = ROOT / "scripts" / "run_bid_source_parent_terminal_supervisor_v006.py"
V003_FAILURE_RECORD = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.json"
)
V003_FAILURE_SEAL = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v003_failure_record.seal.sha256"
)
V003_FAILURE_RECORD_SHA256 = (
    "4195917299558acd17b5c94c64d8e1b33a440d7c32db578a143b9319c07407c6"
)
V003_FAILURE_SEAL_SHA256 = (
    "1465596364b659f6bfaf86f1501441669cdf03ab1de2c78e628d961a8557f627"
)
V005_FAILURE_RECORD = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v005_failure_record.json"
)
V005_FAILURE_SEAL = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_sp14_terminal_v005_failure_record.seal.sha256"
)
V005_FAILURE_RECORD_SHA256 = (
    "16b92ed10af821a5a740cbaf9b8280a97066fe93e59ec4b54166e989e5dcda42"
)
V005_FAILURE_SEAL_SHA256 = (
    "262b208893c07caaa6d65a383364b3b1b435c962c78420024dfda50654b79008"
)
NORMAL_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v006_execution_manifest.json"
)
OPTIMIZED_MANIFEST = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v006_execution_manifest.json"
)
NORMAL_OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_normal_v006.json"
)
OPTIMIZED_OUTPUT = (
    PROJECT_ROOT / "results" / "bid_source_parent_terminal_producer_optimized_v006.json"
)
NORMAL_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_normal_v006_execution_receipt.json"
)
OPTIMIZED_RECEIPT = (
    PROJECT_ROOT
    / "provenance"
    / "bid_source_parent_terminal_producer_optimized_v006_execution_receipt.json"
)
OBLIGATION_ROW = re.compile(
    r"^\| (SP\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$"
)

DOCUMENTS = (
    "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md",
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
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def content_root(paths: tuple[str, ...]) -> str:
    digest = hashlib.sha256()
    for relative in sorted(paths):
        payload = (ROOT / relative).read_bytes()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(payload).digest())
    return digest.hexdigest()


def project_relative(path: Path) -> str:
    return str(path.resolve().relative_to(PROJECT_ROOT.resolve()))


def preserved_failure_lineage() -> dict[str, dict[str, str]]:
    return {
        "v003": {
            "record": project_relative(V003_FAILURE_RECORD),
            "record_sha256": V003_FAILURE_RECORD_SHA256,
            "seal": project_relative(V003_FAILURE_SEAL),
            "seal_sha256": V003_FAILURE_SEAL_SHA256,
        },
        "v005": {
            "record": project_relative(V005_FAILURE_RECORD),
            "record_sha256": V005_FAILURE_RECORD_SHA256,
            "seal": project_relative(V005_FAILURE_SEAL),
            "seal_sha256": V005_FAILURE_SEAL_SHA256,
        },
    }


def build_manifest_payload(
    output: Path,
    receipt: Path,
    optimize: int,
    files: dict[str, str],
    exact_common: dict[str, object],
    checks: list[str],
) -> dict[str, object]:
    return {
        "schema": "gravacle.sealed-target-execution.v002",
        "stage": (
            "bid-source-parent-terminal-producer-"
            f"{'optimized' if optimize else 'normal'}-v006"
        ),
        "python_optimize": optimize,
        "alpha_computed": False,
        "runtime_snapshot": project_relative(RUNTIME),
        "runtime_snapshot_sha256": sha256(RUNTIME),
        "target_script": project_relative(TARGET),
        "expected_output": project_relative(output),
        "execution_receipt": project_relative(receipt),
        "files": files,
        "preserved_failure_lineage": preserved_failure_lineage(),
        "terminal_supervisor_pre_frozen": True,
        "independent_verifier_pre_frozen": True,
        "output_contract": {
            "required_fields": list(exact_common) + ["python_optimize", "checks"],
            "exact_values": {**exact_common, "python_optimize": optimize},
            "required_check_keys": checks,
        },
    }


def write_manifest(
    path: Path,
    output: Path,
    receipt: Path,
    optimize: int,
    files: dict[str, str],
    exact_common: dict[str, object],
    checks: list[str],
) -> None:
    payload = build_manifest_payload(
        output,
        receipt,
        optimize,
        files,
        exact_common,
        checks,
    )
    with path.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")


def main() -> None:
    fixed = (
        RUNTIME,
        RUNTIME_BUILDER,
        RUNTIME_GATE,
        LAUNCHER,
        GENERIC_VALIDATION,
        ALIAS_TEST,
        MANIFEST_CONTRACT_TEST,
        TARGET,
        BUILDER,
        VERIFIER,
        VERIFIER_BUILDER,
        SUPERVISOR,
        V003_FAILURE_RECORD,
        V003_FAILURE_SEAL,
        V005_FAILURE_RECORD,
        V005_FAILURE_SEAL,
    )
    for path in fixed:
        if not path.is_file():
            raise FileNotFoundError(path)
    for record, record_hash, seal, seal_hash in (
        (
            V003_FAILURE_RECORD,
            V003_FAILURE_RECORD_SHA256,
            V003_FAILURE_SEAL,
            V003_FAILURE_SEAL_SHA256,
        ),
        (
            V005_FAILURE_RECORD,
            V005_FAILURE_RECORD_SHA256,
            V005_FAILURE_SEAL,
            V005_FAILURE_SEAL_SHA256,
        ),
    ):
        if (
            sha256(record) != record_hash
            or sha256(seal) != seal_hash
            or seal.read_text(encoding="utf-8").strip()
            != f"{record_hash}  {record.name}"
        ):
            raise RuntimeError(
                f"preserved failure lineage does not match its trust anchor: {record.name}"
            )
    for path in (
        NORMAL_MANIFEST,
        OPTIMIZED_MANIFEST,
        NORMAL_OUTPUT,
        OPTIMIZED_OUTPUT,
        NORMAL_RECEIPT,
        OPTIMIZED_RECEIPT,
    ):
        if path.exists():
            raise FileExistsError(f"refusing to overwrite {path}")

    dependency_relatives = (
        DOCUMENTS
        + tuple(f"scripts/{name}" for name in AUDITS)
        + ("scripts/audit_bid_source_parent_closure_gate_v003.py",)
    )
    dependency_paths = tuple(ROOT / relative for relative in dependency_relatives)
    if not all(path.is_file() for path in dependency_paths):
        missing = [str(path) for path in dependency_paths if not path.is_file()]
        raise FileNotFoundError(f"missing producer dependency: {missing}")

    obligations: dict[str, str] = {}
    for line in (ROOT / DOCUMENTS[0]).read_text(encoding="utf-8").splitlines():
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
    if blocking != ["SP08", "SP09", "SP14"]:
        raise RuntimeError(f"unexpected producer blocker set: {blocking}")

    files = {
        project_relative(path): sha256(path)
        for path in dependency_paths + fixed[1:]
    }
    checks = [
        "structured_status_contradiction_rejection",
        "subordinate_output_contradiction_rejection",
        "subordinate_specific_verdict_enforcement",
        "subordinate_process_optimize_exact",
        "startup_custom_modules_absent",
        "all_known_obligations_retained",
    ]
    exact_common: dict[str, object] = {
        "schema": "gravacle.bid-source-parent-regression.v003",
        "known_source_parent_obligations": 18,
        "currently_blocking_obligations": 3,
        "content_root_sha256": content_root(dependency_relatives),
        "content_addressed_runtime_sealed": True,
        "source_parent_closure": False,
        "proof_authorized": False,
        "alpha_computed": False,
    }
    write_manifest(
        NORMAL_MANIFEST,
        NORMAL_OUTPUT,
        NORMAL_RECEIPT,
        0,
        files,
        exact_common,
        checks,
    )
    write_manifest(
        OPTIMIZED_MANIFEST,
        OPTIMIZED_OUTPUT,
        OPTIMIZED_RECEIPT,
        1,
        files,
        exact_common,
        checks,
    )
    print(NORMAL_MANIFEST)
    print(OPTIMIZED_MANIFEST)
    print(f"sealed_dependency_files={len(files)}")
    print("producer_blockers=SP08,SP09,SP14")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
