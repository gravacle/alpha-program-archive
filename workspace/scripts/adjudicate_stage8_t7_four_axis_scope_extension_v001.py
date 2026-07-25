#!/usr/bin/env python3
"""Adjudicate the sealed Stage-8 T7 four-axis scope extension.

This is an authority-state audit, not a response calculation. Every
obligation is classified from hash-pinned evidence as ESTABLISHED, REFUTED,
or NOT_ESTABLISHED. An axis is DERIVED only when every positive obligation
is ESTABLISHED.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
SPEC = ROOT / "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_SPEC_V001.md"
SPEC_SHA256 = "dcc0878f6af6bdfe1498b0bff7db81336ea7f1f9b34ed0891f5edd21ea01c339"
OUTPUT = (
    ROOT
    / "stage8_execution/work/T07_four_axis_scope_extension_adjudication_v001.json"
)

EXPECTED_AUTHORITIES = {
    "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md":
        "85d24996987278b285d63b8fe15a8732e55664e7c1b09063617b66cb4bc926b4",
    "STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md":
        "9410ee80ff89beed4e133f75fcdb952d059f3386df12069793b5d60895d15486",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_RESULT_V001.md":
        "0df721a170f4f4a1ec630775a3ae47b0d793c82e100b326e681030389eaf0694",
    "STAGE8_T7_RELAY_DEPENDENCY_ORDER_AMENDMENT_V001.md":
        "29c32f90e6a4f88a26e22c91504b6d92a1fc4083ad6368984a1e94858caa4365",
    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md":
        "52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d",
    "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md":
        "7aafba8667ac01f1c4326b0d714e838bf068eec7c8f4ce28ef03c8bef9d62098",
    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md":
        "6447eb80c9347e614a1ecfbfef6234e4acec5caadf829a8649fdb5282439aa09",
    "STAGE8_T7_THREE_SITE_BASELINE_SCOPE_ERRATUM_V001.md":
        "f1dc38f8a08b9e21675dc35fc91ffbd5e0b94d3feb5113f850c09a19b89bbd38",
    "STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md":
        "6e24ceb6b18e6e6da5a6d21e872f90f6d79a324df9f305d226ab6edec863831b",
    "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md":
        "a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510",
    "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md":
        "6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676",
    "COMPLETE_QSPEC_CANONICAL_FULL_LOCAL_SOURCE_POLYDISC_RESULT_V001.md":
        "ecca90cdb3ca81605da84b1a341d361127446df56cb9139e5a9efbc663919f5c",
}

SEMANTIC_READS: set[Path] = set()
HASH_ONLY_READS: set[Path] = set()
ALLOWED_SEMANTIC_READS: set[Path] = set()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def resolved(path: Path) -> Path:
    return path.resolve()


def raw_sha256(path: Path) -> str:
    target = resolved(path)
    require(target.exists(), f"missing hash target: {target}")
    HASH_ONLY_READS.add(target)
    return hashlib.sha256(target.read_bytes()).hexdigest()


def semantic_text(path: Path) -> str:
    target = resolved(path)
    require(target in ALLOWED_SEMANTIC_READS,
            f"semantic read outside sealed allowlist: {target}")
    SEMANTIC_READS.add(target)
    return target.read_text()


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def blocked_artifact(reason: str) -> dict[str, Any]:
    return {
        "schema": "stage8-t7-four-axis-scope-extension-adjudication-v001",
        "verdict": "VALIDATION_INCOMPLETE_BLOCKED",
        "validation_error": reason,
        "axis1_primitive_layer_derived": False,
        "axis2_continuum_carrier_member_derived": False,
        "axis3_connected_exhaustion_uniformity_derived": False,
        "axis4_one_handle_reduction_derived": False,
        "primitive_source_scalarization_derived": False,
        "connected_primitive_amplitude_derived": False,
        "primitive_continuum_exhaustion_member_derived": False,
        "primitive_connected_cellulation_uniformity_proved": False,
        "primitive_ZN_one_handle_reduction_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }


def parse_pinned_authorities(spec_text: str) -> dict[str, str]:
    match = re.search(
        r"## Pinned authorities\s+```text\s+(.*?)\s+```",
        spec_text,
        flags=re.DOTALL,
    )
    require(match is not None, "sealed pinned-authority block missing")
    parsed: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = re.fullmatch(r"([0-9a-f]{64})\s{2}(.+)", line.strip())
        require(item is not None, f"malformed pinned-authority line: {line}")
        digest, name = item.groups()
        require(name not in parsed, f"duplicate pinned authority: {name}")
        parsed[name] = digest
    require(parsed == EXPECTED_AUTHORITIES,
            "executor authority dictionary differs from sealed spec")
    return parsed


def sidecar_candidates(path: Path) -> tuple[Path, ...]:
    return (
        Path(str(path) + ".seal.sha256"),
        path.with_suffix("").with_suffix(".seal.sha256"),
    )


def verify_sidecar(authority: Path, pinned_hash: str,
                   sidecar: Path) -> dict[str, Any]:
    sidecar_hash = raw_sha256(sidecar)
    entries: list[dict[str, Any]] = []
    seen_targets: dict[Path, str] = {}
    authority_seen = False
    for raw_line in sidecar.read_text().splitlines():
        line = raw_line.strip()
        if not line:
            continue
        match = re.fullmatch(r"([0-9a-f]{64})\s{2}(.+)", line)
        require(match is not None, f"malformed sidecar line: {sidecar.name}")
        expected, relative = match.groups()
        target = Path(relative)
        if not target.is_absolute():
            target = ROOT / target
        target = resolved(target)
        require(target == ROOT or ROOT in target.parents,
                f"sidecar target escapes workspace: {target}")
        require(target not in seen_targets or seen_targets[target] == expected,
                f"conflicting sidecar entries: {target}")
        seen_targets[target] = expected
        actual = raw_sha256(target)
        require(actual == expected, f"sidecar hash mismatch: {target}")
        if target == resolved(authority):
            require(expected == pinned_hash,
                    f"sidecar disagrees with pinned authority: {authority.name}")
            authority_seen = True
        entries.append(
            {
                "path": str(target.relative_to(ROOT)),
                "sha256": actual,
                "verified": True,
            }
        )
    require(entries, f"empty sidecar: {sidecar.name}")
    require(authority_seen,
            f"sidecar does not seal its authority: {sidecar.name}")
    return {
        "sidecar": str(sidecar.relative_to(ROOT)),
        "sidecar_sha256": sidecar_hash,
        "authority": authority.name,
        "entries": entries,
        "verified": True,
    }


def canonical_assignments(text: str, key: str) -> set[bool]:
    values = {
        value == "true"
        for value in re.findall(
            rf"(?m)^\s*{re.escape(key)}\s*=\s*(true|false)\s*$",
            text,
        )
    }
    require(len(values) <= 1, f"conflicting canonical bindings for {key}")
    return values


def canonical_claim(texts: dict[str, str], authority: str, key: str,
                    expected: bool, section: str) -> dict[str, Any]:
    values = canonical_assignments(texts[authority], key)
    require(values == {expected},
            f"missing or wrong canonical binding: {authority}:{key}")
    return {
        "state": "ESTABLISHED" if expected else "NOT_ESTABLISHED",
        "authority": authority,
        "authority_sha256": EXPECTED_AUTHORITIES[authority],
        "claim_key": key,
        "claim_value": expected,
        "section": section,
    }


def exact_section_claim(texts: dict[str, str], authority: str, section: str,
                        required_fragments: tuple[str, ...],
                        state: str, claim_key: str) -> dict[str, Any]:
    require(state in {"ESTABLISHED", "REFUTED", "NOT_ESTABLISHED"},
            f"invalid evidence state: {state}")
    text = texts[authority]
    heading = re.search(
        rf"(?ms)^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)",
        text,
    )
    require(heading is not None,
            f"missing canonical section {section}: {authority}")
    body = heading.group(1)
    for fragment in required_fragments:
        require(fragment in body,
                f"missing canonical evidence in {authority}:{section}: {fragment}")
    return {
        "state": state,
        "authority": authority,
        "authority_sha256": EXPECTED_AUTHORITIES[authority],
        "claim_key": claim_key,
        "claim_value": state,
        "section": section,
    }


def inventory_claim(texts: dict[str, str], claim_key: str) -> dict[str, Any]:
    positive = []
    negative = []
    for authority, text in texts.items():
        values = canonical_assignments(text, claim_key)
        if values == {True}:
            positive.append(authority)
        elif values == {False}:
            negative.append(authority)
    require(not positive,
            f"positive pinned derivation exists for {claim_key}: {positive}")
    return {
        "state": "NOT_ESTABLISHED",
        "authority": "sealed pinned-authority inventory",
        "authority_sha256": SPEC_SHA256,
        "claim_key": claim_key,
        "claim_value": False,
        "section": "exact authority inventory",
        "negative_bindings": negative,
    }


def obligation(evidence: dict[str, Any]) -> dict[str, Any]:
    require(evidence["state"] in {"ESTABLISHED", "REFUTED", "NOT_ESTABLISHED"},
            "invalid obligation state")
    return evidence


def adjudicate_axis(reason: str,
                    obligations: dict[str, dict[str, Any]]) -> dict[str, Any]:
    status = (
        "DERIVED"
        if all(item["state"] == "ESTABLISHED" for item in obligations.values())
        else "SCOPE_RESTRICTED_BLOCKING"
    )
    return {
        "status": status,
        "reason": reason if status == "SCOPE_RESTRICTED_BLOCKING" else "DERIVED",
        "obligations": obligations,
    }


def main() -> None:
    require(sys.flags.isolated == 1, "executor requires python3 -I")
    require(sys.flags.no_site == 1, "executor requires python3 -S")
    atomic_json(OUTPUT, blocked_artifact("validation started; no verdict yet"))

    global ALLOWED_SEMANTIC_READS
    ALLOWED_SEMANTIC_READS = {resolved(SPEC)}
    require(raw_sha256(SPEC) == SPEC_SHA256, "sealed spec hash mismatch")
    spec_text = semantic_text(SPEC)
    authorities = parse_pinned_authorities(spec_text)
    ALLOWED_SEMANTIC_READS = {
        resolved(SPEC),
        *(resolved(ROOT / name) for name in authorities),
    }

    verified: dict[str, str] = {}
    sidecars: list[dict[str, Any]] = []
    seen_sidecars: set[Path] = set()
    for relative, expected in authorities.items():
        path = ROOT / relative
        actual = raw_sha256(path)
        require(actual == expected, f"authority hash mismatch: {relative}")
        verified[relative] = actual
        for candidate in sidecar_candidates(path):
            candidate = resolved(candidate)
            if candidate.exists() and candidate not in seen_sidecars:
                sidecars.append(verify_sidecar(path, expected, candidate))
                seen_sidecars.add(candidate)

    texts = {
        name: semantic_text(ROOT / name)
        for name in authorities
    }

    critical = "STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md"
    three_site = "STAGE8_T7_THREE_SITE_BASELINE_SCOPE_ERRATUM_V001.md"
    galerkin = "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md"
    battery = "STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_V001.md"

    precedence = {
        "critical_path_scope_correction": exact_section_claim(
            texts,
            critical,
            "2. CAR/Fock/Hermite calculations",
            (
                "They belong to the downstream complete-Q_spec "
                "continuum-provenance program.",
                "They may not be supplied as primitive T7 closure",
            ),
            "ESTABLISHED",
            "critical_path_scope_correction_controls",
        ),
        "three_site_scope_erratum": exact_section_claim(
            texts,
            three_site,
            "Withdrawn inference",
            (
                "a member of the physical continuum exhaustion;",
                "the primitive T7 amplitude;",
            ),
            "ESTABLISHED",
            "three_site_scope_erratum_controls",
        ),
        "continuum_galerkin_correction": exact_section_claim(
            texts,
            galerkin,
            "Authority correction",
            (
                "Its stronger label, `PARENT_STATE_REGULATOR_RESTRICTION_DERIVED`,\n"
                "is withdrawn.",
                "That family does not exist for the free massless Dirac multiplier.",
            ),
            "ESTABLISHED",
            "continuum_galerkin_correction_controls",
        ),
    }

    car_fences = {
        "battery_no_CAR_determinant": exact_section_claim(
            texts,
            battery,
            "A. Authority and scope",
            ("No CAR determinant",),
            "ESTABLISHED",
            "battery_no_CAR_determinant",
        ),
        "primitive_parent_CAR_UHF_allowance": {
            "state": "ESTABLISHED",
            "authority": SPEC.name,
            "authority_sha256": SPEC_SHA256,
            "claim_key": "primitive_parent_CAR_UHF_allowance",
            "claim_value": (
                "A CAR/UHF or quasifree scalarization remains admissible "
                "if it is derived from the primitive parent itself"
                in spec_text
            ),
            "section": "Axis 1 - Layer",
        },
        "downstream_Qspec_import_forbidden": {
            "state": "ESTABLISHED",
            "authority": SPEC.name,
            "authority_sha256": SPEC_SHA256,
            "claim_key": "downstream_Qspec_import_forbidden",
            "claim_value": (
                "It may not be imported from a\n"
                "downstream complete-`Q_spec` result."
                in spec_text
            ),
            "section": "Axis 1 - Layer",
        },
    }
    require(all(item["claim_value"] for item in car_fences.values()),
            "CAR/UHF scoping fence missing")

    axis1 = adjudicate_axis(
        "AXIS1_PRIMITIVE_SCALAR_AMPLITUDE_SCOPE_RESTRICTED",
        {
            "actual_parent_supplies_normalized_scalar": obligation(
                exact_section_claim(
                    texts,
                    "STAGE8_T7_ACTUAL_PARENT_RECORD_AMPLITUDE_ADJUDICATION_RESULT_V001.md",
                    "Verdict",
                    ("ACTUAL_PARENT_RECORD_AMPLITUDE_BLOCKED",),
                    "REFUTED",
                    "actual_parent_supplies_normalized_scalar",
                )
            ),
            "canonical_primitive_scalar_functional": obligation(
                canonical_claim(
                    texts,
                    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.md",
                    "primitive_source_scalarization_derived",
                    False,
                    "Fixed status",
                )
            ),
            "all_finite_flat_baselines_nonzero": obligation(
                canonical_claim(
                    texts,
                    galerkin,
                    "physical_regulator_completed_record_baseline_derived",
                    False,
                    "Current verdict",
                )
            ),
            "exact_one_handle_reduction": obligation(
                inventory_claim(texts, "primitive_ZN_one_handle_reduction_proved")
            ),
        },
    )

    axis2 = adjudicate_axis(
        "AXIS2_CARRIER_SCOPE_RESTRICTED",
        {
            "beyond_three_site_physical_member": obligation(
                canonical_claim(
                    texts,
                    galerkin,
                    "genuine_finite_rank_continuum_restriction_constructed",
                    False,
                    "Authority correction",
                )
            ),
            "continuum_response_provenance": obligation(
                canonical_claim(
                    texts,
                    "STAGE8_T7_COMPLETED_CONTINUUM_RESPONSE_PROVENANCE_SPEC_V001.md",
                    "completed_continuum_response_provenance_derived",
                    False,
                    "Fixed status",
                )
            ),
            "regulator_compatible_parent_state": obligation(
                canonical_claim(
                    texts,
                    galerkin,
                    "parent_state_regulator_restriction_derived",
                    False,
                    "Authority correction",
                )
            ),
        },
    )

    axis3 = adjudicate_axis(
        "AXIS3_QUANTIFIER_SCOPE_RESTRICTED",
        {
            "relayed_causal_exhaustion_uniformity": obligation(
                canonical_claim(
                    texts,
                    "STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md",
                    "volume_uniform_zero_free_neighborhood_proved",
                    False,
                    "Fixed status",
                )
            ),
            "all_declared_connected_cellulations": obligation(
                canonical_claim(
                    texts,
                    "COMPLETE_QSPEC_CANONICAL_FULL_LOCAL_SOURCE_POLYDISC_RESULT_V001.md",
                    "all_connected_cellulations_linked_cluster_proved",
                    False,
                    "Fixed status",
                )
            ),
            "common_refinement_compatibility": obligation(
                inventory_claim(texts, "common_refinement_compatibility_proved")
            ),
        },
    )

    axis4 = adjudicate_axis(
        "AXIS4_ONE_HANDLE_REDUCTION_SCOPE_RESTRICTED",
        {
            "pinned_one_handle_ratio": obligation(
                canonical_claim(
                    texts,
                    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
                    "primitive_complex_transition_amplitude_unique",
                    True,
                    "Status",
                )
            ),
            "actual_parent_connected_amplitude": obligation(
                canonical_claim(
                    texts,
                    critical,
                    "connected_primitive_amplitude_derived",
                    False,
                    "Fixed status",
                )
            ),
            "exact_actual_parent_Z1_reduction": obligation(
                inventory_claim(texts, "primitive_ZN_one_handle_reduction_proved")
            ),
        },
    )

    axes = {
        "axis1_layer": axis1,
        "axis2_carrier": axis2,
        "axis3_quantifier": axis3,
        "axis4_object": axis4,
    }
    all_derived = all(item["status"] == "DERIVED" for item in axes.values())
    verdict = (
        "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_DERIVED"
        if all_derived
        else "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_BLOCKED"
    )

    expected_semantic = {resolved(SPEC), *(resolved(ROOT / name) for name in authorities)}
    require(SEMANTIC_READS == expected_semantic,
            "semantic read set differs from sealed allowlist")
    no_target_access = {
        "isolated_python": sys.flags.isolated == 1,
        "site_disabled": sys.flags.no_site == 1,
        "semantic_read_set_exact": SEMANTIC_READS == expected_semantic,
        "unpinned_semantic_reads": [],
        "semantic_reads": sorted(
            str(path.relative_to(ROOT)) for path in SEMANTIC_READS
        ),
        "hash_only_reads": sorted(
            str(path.relative_to(ROOT))
            for path in HASH_ONLY_READS
            if path == ROOT or ROOT in path.parents
        ),
        "coupling_value_accessed": False,
        "kappa_record_value_accessed": False,
        "alpha_value_accessed": False,
        "downstream_match_artifact_accessed": False,
    }

    result = {
        "schema": "stage8-t7-four-axis-scope-extension-adjudication-v001",
        "spec_sha256": SPEC_SHA256,
        "executor_sha256": raw_sha256(SCRIPT),
        "authority_sha256": verified,
        "verified_sidecars": sidecars,
        "precedence": precedence,
        "CAR_UHF_scope_fences": car_fences,
        "no_target_access_attestation": no_target_access,
        "axes": axes,
        "verdict": verdict,
        "axis1_primitive_layer_derived": axis1["status"] == "DERIVED",
        "axis2_continuum_carrier_member_derived": axis2["status"] == "DERIVED",
        "axis3_connected_exhaustion_uniformity_derived":
            axis3["status"] == "DERIVED",
        "axis4_one_handle_reduction_derived": axis4["status"] == "DERIVED",
        "primitive_source_scalarization_derived": False,
        "connected_primitive_amplitude_derived": False,
        "primitive_continuum_exhaustion_member_derived": False,
        "primitive_connected_cellulation_uniformity_proved": False,
        "primitive_ZN_one_handle_reduction_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    atomic_json(OUTPUT, result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        atomic_json(OUTPUT, blocked_artifact(f"{type(exc).__name__}: {exc}"))
        raise
