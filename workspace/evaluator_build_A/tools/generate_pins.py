#!/usr/bin/env python3
"""Generate Builder A's one closed pin manifest from the supplied sealed bytes."""

import hashlib
import json
from pathlib import Path


def canonical(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    package = Path(__file__).resolve().parents[1]
    cleanroom = package.parent
    program = cleanroom.parent
    archive = Path("/Users/bgm/MB Work/alpha-program-archive")
    packet = cleanroom / "review_packets/STAGE7_QSPEC_CANDIDATE_V001"
    sources = {
        "authorization": (archive / "supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md", "supervision/DECISION_RD22_BUILD_AUTHORIZED_2026-08-07.md"),
        "blocker_ledger": (cleanroom / "BID_FULL_STACK_REVIEW_LEDGER_V003.md", "alpha_fundamental_record_action_cleanroom_v003/BID_FULL_STACK_REVIEW_LEDGER_V003.md"),
        "evidence_a21": (cleanroom / "STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A21_OPEN_LEG_DISPOSITION_LANE2_V001.md"),
        "evidence_assembly": (cleanroom / "STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_LP_QSPEC_ASSEMBLY_DARIO_V005.md"),
        "evidence_cpt": (packet / "BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md", "alpha_fundamental_record_action_cleanroom_v003/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md"),
        "evidence_matrix": (cleanroom / "STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_LP_MATRIX_LEDGER_LANE3_V001.md"),
        "evidence_matrix_review": (cleanroom / "STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_LP_MATRIX_LEDGER_REVIEW_DARIO_V001.md"),
        "grounding_precedence": (archive / "supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md", "supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md"),
        "grounding_relocation": (cleanroom / "STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_GROUNDING_RELOCATION_DARIO_V001.md"),
        "grounding_source": (cleanroom / "provenance/boundary_incidence_dynamics_preregistration_v011.json", "alpha_fundamental_record_action_cleanroom_v003/provenance/boundary_incidence_dynamics_preregistration_v011.json"),
        "integration_addendum": (cleanroom / "STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_SPEC_V005_INTEGRATION_ADDENDUM_DARIO_V001.md"),
        "packet_manifest": (packet / "STAGE7_PACKET_MANIFEST_V001.sha256", "alpha_fundamental_record_action_cleanroom_v003/review_packets/STAGE7_QSPEC_CANDIDATE_V001/STAGE7_PACKET_MANIFEST_V001.sha256"),
        "packet_v011": (packet / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md", "alpha_fundamental_record_action_cleanroom_v003/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md"),
        "root_membership_source": (cleanroom / "STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_SCHEMA_IN_ROOT_DARIO_V001.md"),
        "runtime_gate": (program / "primitive_step6_content_addressed_runtime_gate_v010.md", "primitive_step6_content_addressed_runtime_gate_v010.md"),
        "runtime_snapshot": (program / "provenance/primitive_step6_runtime_snapshot_v012.json", "provenance/primitive_step6_runtime_snapshot_v012.json"),
        "source_parent_gate": (packet / "BID_SOURCE_PARENT_CLOSURE_GATE_V003.md", "alpha_fundamental_record_action_cleanroom_v003/review_packets/STAGE7_QSPEC_CANDIDATE_V001/BID_SOURCE_PARENT_CLOSURE_GATE_V003.md"),
        "specification": (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V009.md"),
        "specification_base_v008": (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V008.md"),
        "specification_base_v007": (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V007.md"),
        "specification_v005": (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V005.md"),
        "specification_v006": (cleanroom / "STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_A35_EVALUATOR_SPEC_LANE2_V006.md"),
        "verifier_manifest_v008": (cleanroom / "evaluator_build_B/rd22.verifier-manifest.v001.json", "alpha_fundamental_record_action_cleanroom_v003/evaluator_build_B/rd22.verifier-manifest.v001.json"),
        "verifier_v008_integration_report": (cleanroom / "STAGE8_TASK6_V008_INTEGRATION_DARIO_V001.md", "alpha_fundamental_record_action_cleanroom_v003/STAGE8_TASK6_V008_INTEGRATION_DARIO_V001.md"),
        "verifier_verdict_schema": (cleanroom / "evaluator_build_B/contracts/verifier_verdict.schema.json", "alpha_fundamental_record_action_cleanroom_v003/evaluator_build_B/contracts/verifier_verdict.schema.json"),
    }
    rows = []
    for kind, (path, relative_path) in sorted(sources.items()):
        if not path.is_file():
            raise SystemExit(f"PIN_GENERATION_FAIL missing:{kind}:{path}")
        data = path.read_bytes()
        rows.append({"byte_length": len(data), "kind": kind, "relative_path": relative_path, "sha256": digest(data)})
    value = {"pins": rows, "schema": "rd22.builder-a-pin-manifest.v001"}
    output = package / "manifests/pins.json"
    output.write_bytes(canonical(value))
    print(json.dumps({"pins": len(rows), "sha256": digest(output.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
