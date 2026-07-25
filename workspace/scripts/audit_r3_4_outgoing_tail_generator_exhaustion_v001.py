#!/usr/bin/env python3
"""Fail-closed reduced public-tail zero-form exhaustion audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_SPEC_V001.md"
PROVENANCE = ROOT / "R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_PROVENANCE_V001.json"
SPEC_SEAL = ROOT / "R3_4_OUTGOING_TAIL_GENERATOR_EXHAUSTION_SPEC_V001.seal.sha256"
DEFAULT_RESULT = ROOT / "results" / "r3_4_outgoing_tail_generator_exhaustion_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_status(path: Path, key: str) -> bool:
    matches = re.findall(
        rf"(?m)^{re.escape(key)} = (true|false)$",
        path.read_text(encoding="utf-8"),
    )
    require(len(matches) == 1, f"{path.name}: expected exactly one {key}")
    return matches[0] == "true"


def verify_provenance() -> dict:
    seal_entries = {}
    for line in SPEC_SEAL.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        digest, path = line.split(maxsplit=1)
        require(path not in seal_entries, f"duplicate seal path {path}")
        seal_entries[path] = digest
    expected = {SPEC.name: sha256(SPEC), PROVENANCE.name: sha256(PROVENANCE)}
    require(seal_entries == expected, "spec/provenance seal mismatch")

    manifest = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    rows = []
    for authority in manifest["authorities"]:
        path = ROOT / authority["path"]
        require(path.is_file(), f"missing authority {authority['path']}")
        actual_hash = sha256(path)
        require(actual_hash == authority["sha256"], f"hash mismatch {path.name}")
        statuses = {}
        for key, expected_value in authority["status"].items():
            actual_value = exact_status(path, key)
            require(actual_value is expected_value, f"status mismatch {path.name}:{key}")
            statuses[key] = actual_value
        rows.append(
            {
                "path": authority["path"],
                "sha256": actual_hash,
                "status": statuses,
            }
        )
    return {
        "spec_sha256": expected[SPEC.name],
        "provenance_sha256": expected[PROVENANCE.name],
        "authorities": rows,
        "continuum_obligations": manifest["continuum_obligations"],
    }


def matrix_rank(matrices: list[np.ndarray], tolerance: float = 1.0e-12) -> int:
    columns = [matrix.reshape(-1) for matrix in matrices]
    return int(np.linalg.matrix_rank(np.column_stack(columns), tol=tolerance))


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def build_result() -> dict:
    provenance = verify_provenance()

    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    basis = {"I": identity, "X": x, "Y": y, "Z": z}

    pointer_commutators = {
        name: commutator(matrix, z) for name, matrix in basis.items()
    }
    nondemolition_kernel = [
        name
        for name, value in pointer_commutators.items()
        if np.linalg.norm(value) < 1.0e-12
    ]
    nondemolition_rank = matrix_rank(list(pointer_commutators.values()))

    public_basis = {"I": identity, "Z": z}
    public_actions = {
        phi_name: {
            observable_name: float(np.linalg.norm(commutator(phi, observable)))
            for observable_name, observable in public_basis.items()
        }
        for phi_name, phi in {"I": identity, "Z": z}.items()
    }
    full_actions = {
        observable_name: float(np.linalg.norm(commutator(z, observable)))
        for observable_name, observable in basis.items()
    }

    reduced_public_zero_form_exhausted = (
        nondemolition_kernel == ["I", "Z"]
        and all(
            norm == 0.0
            for row in public_actions.values()
            for norm in row.values()
        )
    )
    z_nontrivial_on_full_hilbert_algebra = any(
        norm > 0.0 for norm in full_actions.values()
    )

    continuum = provenance["continuum_obligations"]
    continuum_closed = all(continuum.values())
    if not reduced_public_zero_form_exhausted:
        verdict = "NONTRIVIAL_PUBLIC_TAIL_ZERO_FORM_SURVIVES"
    elif continuum_closed:
        verdict = "UNIQUE_INCIDENCE_ONLY_OUTGOING_GENERATOR_DERIVED"
    else:
        verdict = "PUBLIC_TAIL_ZERO_FORM_EXHAUSTED_CONTINUUM_SCALING_OPEN"

    return {
        "sealed_inputs": provenance,
        "target_firewall": {
            "alpha_used": False,
            "measured_constants_used": False,
            "candidate_density_used_as_selector": False,
        },
        "reduced_register_exhaustion": {
            "hermitian_basis": list(basis),
            "nondemolition_commutator_rank": nondemolition_rank,
            "nondemolition_kernel": nondemolition_kernel,
            "pointer_rotating_directions": ["X", "Y"],
            "identity_direction_projectively_null": True,
            "Z_direction_action_on_public_algebra": public_actions["Z"],
            "Z_direction_action_on_full_M2": full_actions,
            "Z_nontrivial_on_full_hilbert_algebra": (
                z_nontrivial_on_full_hilbert_algebra
            ),
            "reduced_public_zero_form_exhausted": (
                reduced_public_zero_form_exhausted
            ),
        },
        "scope": {
            "source_supported_terms_vanish_if_compactly_supported": True,
            "all_source_terms_proved_compactly_supported": False,
            "spin_edge_enlarged_tail_factors_exhausted": False,
            "public_tail_equivalence_proves_full_generator_equivalence": False,
        },
        "status": {
            "verdict": verdict,
            "reduced_public_tail_zero_form_exhausted": (
                reduced_public_zero_form_exhausted
            ),
            "complete_asymptotic_tail_zero_form_exhausted": False,
            "continuum_scaling_closed": continuum_closed,
            "operator_derived_root_spectral_measure_computed": False,
            "hypothesis_promoted_to_principle": False,
            "spectral_evaluation_authorized": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    result = build_result()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["status"], indent=2))


if __name__ == "__main__":
    main()
