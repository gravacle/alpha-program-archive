#!/usr/bin/env python3
"""Compare sealed Stage-8 T7 independent and primary CAR response bundles.

v002 append-only successor authorized by
STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_V001.md (R1 item 1,
R2, R3).  Repairs relative to v001, each enumerated by the sealed binding:

- Finding 1: single-read buffer hashing (each input read once into memory,
  hashed as a buffer, JSON parsed from the buffer, NPZ loaded from BytesIO;
  the v001 post-hoc re-hash window is removed).
- Finding 5: every Kraus member K_x = sum_lambda <x|P_lambda|ready> u_lambda
  is rebuilt from stored propagators + projectors for BOTH lanes and gated
  against the stored direct Kraus members at 3e-9; the adjoint-exchange
  residual is enforced for both lanes at 3e-9.
- Finding 6: E_conn's fourth term is transported through S, matching the
  sealed spec text exactly.
- Finding 7: pass-output flags renamed comparison_supports_*; no A7-level
  protected-flag name appears as true in comparator output.
- Finding 8: resolved absolute input/output paths and a controller-context
  field are recorded in the sealed output.
- Execution binding B2: every E_conn component is evaluated at the single
  frozen history pair (7/100,-11/100) (labels a1,a2), separately per ell.
- Execution binding B3: same-history identity checks run for ALL five frozen
  history values, both kernels, both ell, at 3e-9.
- Lineage gate (binding R2/R3): each declared one-particle propagator is
  rebuilt from that lane's STORED generator pieces by an independent midpoint
  product integrator (Hermitian-eigendecomposition exponentials) and must
  agree with the stored propagator in operator 2-norm within the frozen
  budgets (primary 5e-3, independent 1e-4).  A bundle not carrying the
  generator pieces blocks.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
SPEC = ROOT / "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md"
SPEC_SHA256 = "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3"
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance"
    / "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")

BUNDLE_SCHEMA = "stage8_t7_actual_parent_regulated_car_operator_response_bundle_v001"
RESULT_SCHEMA = "stage8_t7_actual_parent_regulated_car_operator_response_comparison_v002"
PASS_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED"
BLOCKED_VERDICT = "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_BLOCKED"

# Frozen generator-pieces schema (repair binding R2).  All lanes must store
# the ACTUAL generator pieces used by their own propagation, in the sealed
# tensor convention: total one-particle space = spatial(8) tensor spinor(4)
# with the spinor index FASTEST (lexicographic (a,b,c,s)), so that
# h0 = sum_j kron(p_j, alpha_j) and
# h_lambda(t;a) = h0 + lambda v(t) kron(M(t), S_n) - a kron(B(t), alpha_x).
GENERATOR_PIECES_SCHEMA = "stage8_t7_generator_pieces_v002"
GENERATOR_MIDPOINT_COUNTS = {"primary": 48, "independent": 384}
# Preregistered lineage budgets (repair binding R3; frozen before any code
# ran, outcome-blind; lineage-authenticity gates, not precision claims).
LINEAGE_BUDGETS = {"primary": 5.0e-3, "independent": 1.0e-4}
MIDPOINT_TIME_TOLERANCE = 1.0e-12

SCALAR_TOLERANCE = 2.0e-11
PROJECTOR_TOLERANCE = 2.0e-11
BASIS_UNITARITY_TOLERANCE = 2.0e-11
TRANSPORTED_MATRIX_TOLERANCE = 3.0e-4
INDEPENDENT_TAIL_TOLERANCE = TRANSPORTED_MATRIX_TOLERANCE / 4.0
HERMITICITY_PROJECTOR_TOLERANCE = 2.0e-11
RECORD_SPECTRAL_TOLERANCE = 2.0e-12
INTERNAL_IDENTITY_TOLERANCE = 3.0e-9
PRIMARY_CONVERGENCE_RATIO_MINIMUM = 3.2
CONNECTION_NORM_MINIMUM = 1.0e-6
CONNECTION_SIGNAL_FACTOR = 20.0

SCALAR_CATEGORIES = ("record_eigenvalues", "coefficients")
MATRIX_CATEGORIES = (
    "record_projectors",
    "propagators",
    "cross_operators",
    "direct_kraus_members",
    "direct_responses",
    "aggregate_kernels",
)
TRANSPORTED_CATEGORIES = MATRIX_CATEGORIES[1:]
EXPECTED_DIMENSIONS = {
    "source_dimension": 32,
    "record_dimension": 3,
    "spatial_dimension": 8,
}
EXPECTED_DISCRETE_LABELS = {
    "ell": ["ell0", "ell1"],
    "histories": ["a0", "a1", "a2", "a3", "a4"],
    "history_pairs": [["a0", "a0"], ["a1", "a2"], ["a3", "a4"]],
    "pairs": ["p0", "p1", "p2"],
    "record_labels": ["l0", "l1", "l2"],
    "outcome_labels": ["x0", "x1", "x2"],
    "kernels": ["all", "pointer"],
}


def expected_component_identifiers() -> dict[str, set[str]]:
    result = {
        "record_projectors": {f"l{index}" for index in range(3)},
        "propagators": set(),
        "cross_operators": set(),
        "direct_kraus_members": set(),
        "direct_responses": set(),
        "aggregate_kernels": set(),
    }
    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        for history in EXPECTED_DISCRETE_LABELS["histories"]:
            for record in EXPECTED_DISCRETE_LABELS["record_labels"]:
                result["propagators"].add(f"{ell}.{history}.{record}")
            for outcome in EXPECTED_DISCRETE_LABELS["outcome_labels"]:
                result["direct_kraus_members"].add(f"{ell}.{history}.{outcome}")
        for pair in EXPECTED_DISCRETE_LABELS["pairs"]:
            for left in range(3):
                for right in range(3):
                    result["cross_operators"].add(
                        f"{ell}.{pair}.mu{left}.l{right}"
                    )
            for kernel in EXPECTED_DISCRETE_LABELS["kernels"]:
                result["direct_responses"].add(f"{ell}.{pair}.{kernel}")
                result["aggregate_kernels"].add(f"{ell}.{pair}.{kernel}")
    return result


EXPECTED_COMPONENT_IDENTIFIERS = expected_component_identifiers()
EXPECTED_SCALAR_IDENTIFIERS = {
    "record_eigenvalues": {f"l{index}" for index in range(3)},
    "coefficients": {
        *(f"p.l{index}" for index in range(3)),
        *(f"w.l{index}" for index in range(3)),
        *(f"ell.ell{index}" for index in range(2)),
        *(f"history.a{index}" for index in range(5)),
    },
}
EXECUTOR_PATHS = {
    "primary":
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_primary_v002.py",
    "independent":
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_independent_v002.py",
}
RUNTIME_LAUNCHER_PATH = (
    "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
)


class ComparisonBlocked(RuntimeError):
    """Raised when a sealed comparison obligation is not satisfied."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ComparisonBlocked(message)


def require_runtime_attestation() -> dict[str, Any]:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(
        isinstance(attestation, dict),
        "comparison requires the sealed Stage-8 runtime launcher",
    )
    require(
        attestation.get("schema")
        == "stage8_t7_content_addressed_runtime_attestation_v001",
        "Stage-8 runtime-attestation schema mismatch",
    )
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "Stage-8 runtime-attestation manifest mismatch",
    )
    require(
        attestation.get("python_isolated") is True
        and attestation.get("python_no_site") is True,
        "Stage-8 isolated/no-site runtime flags are absent",
    )
    return dict(attestation)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def atomic_write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(
        payload,
        indent=2,
        sort_keys=True,
        ensure_ascii=True,
        allow_nan=False,
    ) + "\n"
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
        text=True,
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def atomic_write_sealed_json(path: Path, payload: Mapping[str, Any]) -> None:
    seal = Path(f"{path}.seal.sha256")
    require(not path.exists(), f"immutable result already exists: {path}")
    require(not seal.exists(), f"immutable result seal already exists: {seal}")
    atomic_write_json(path, payload)
    try:
        seal.write_text(f"{sha256(path)}  {path.name}\n", encoding="ascii")
        for artifact in (path, seal):
            artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    except Exception:
        path.unlink(missing_ok=True)
        seal.unlink(missing_ok=True)
        raise


def blocked_payload(reason: str, *, details: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return {
        "schema": RESULT_SCHEMA,
        "phase": "A",
        "overall_verdict": BLOCKED_VERDICT,
        "comparison_complete": False,
        "comparison_passed": False,
        "reason": reason,
        "details": dict(details or {}),
        "spec_sha256": SPEC_SHA256,
        "actual_parent_regulated_CAR_operator_response_derived": False,
        "actual_parent_same_carrier_one_source_restriction_derived": False,
        "one_particle_sector_CAR_representation_verified": False,
        "full_Fock_operator_norm_bound_derived": False,
        "continuum_limit_derived": False,
        "regulator_independence_derived": False,
        "physical_connection_normalization_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "ER_fork_closed": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }


def strict_json(path: Path) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise ComparisonBlocked(f"non-finite JSON constant in {path.name}: {value}")

    try:
        payload = json.loads(
            path.read_text(encoding="utf-8"),
            parse_constant=reject_constant,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ComparisonBlocked(f"invalid JSON bundle {path}: {error}") from error
    require(isinstance(payload, dict), f"JSON bundle is not an object: {path}")
    return payload


def strict_json_from_buffer(data: bytes, label: str) -> dict[str, Any]:
    # Finding 1: the JSON is parsed from the exact bytes that were hashed;
    # the file is never re-read after hashing.
    def reject_constant(value: str) -> None:
        raise ComparisonBlocked(f"non-finite JSON constant in {label}: {value}")

    try:
        payload = json.loads(
            data.decode("utf-8"),
            parse_constant=reject_constant,
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ComparisonBlocked(f"invalid JSON bundle {label}: {error}") from error
    require(isinstance(payload, dict), f"JSON bundle is not an object: {label}")
    return payload


def parse_scalar(value: Any, label: str) -> complex:
    if isinstance(value, bool):
        raise ComparisonBlocked(f"{label} is boolean, not scalar")
    if isinstance(value, (int, float)):
        result = complex(float(value), 0.0)
    elif isinstance(value, list) and len(value) == 2:
        require(
            all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in value),
            f"{label} complex pair is malformed",
        )
        result = complex(float(value[0]), float(value[1]))
    elif isinstance(value, dict) and set(value) == {"real", "imag"}:
        real, imag = value["real"], value["imag"]
        require(
            all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in (real, imag)
            ),
            f"{label} complex object is malformed",
        )
        result = complex(float(real), float(imag))
    else:
        raise ComparisonBlocked(f"{label} has unsupported scalar encoding")
    require(np.isfinite(result.real) and np.isfinite(result.imag), f"{label} is non-finite")
    return result


def exact_json_equal(left: Any, right: Any) -> bool:
    return canonical_sha256(left) == canonical_sha256(right)


@dataclass(frozen=True)
class Bundle:
    lane: str
    json_path: Path
    npz_path: Path
    json_sha256: str
    npz_sha256: str
    payload: dict[str, Any]
    manifest: dict[str, Any]
    arrays: dict[str, np.ndarray]


def validate_file(path: Path, expected_sha256: str, label: str) -> tuple[bytes, str]:
    # Finding 1: read each input exactly once into memory and hash the buffer.
    # Every consumer below parses these bytes; the file is never re-read, so
    # there is no window between hashing and consumption.
    require(path.exists(), f"{label} does not exist: {path}")
    require(path.is_file(), f"{label} is not a regular file: {path}")
    require(not path.is_symlink(), f"{label} may not be a symlink: {path}")
    require(
        len(expected_sha256) == 64
        and all(character in "0123456789abcdef" for character in expected_sha256),
        f"{label} expected SHA-256 is malformed",
    )
    try:
        data = path.read_bytes()
    except OSError as error:
        raise ComparisonBlocked(f"unable to read {label}: {error}") from error
    actual = hashlib.sha256(data).hexdigest()
    require(actual == expected_sha256, f"{label} SHA-256 mismatch")
    return data, actual


def verify_implementation_manifest() -> tuple[str, dict[str, str]]:
    require(IMPLEMENTATION_MANIFEST.is_file(), "implementation manifest missing")
    require(IMPLEMENTATION_SEAL.is_file(), "implementation manifest seal missing")
    seal_fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(seal_fields) == 2, "malformed implementation-manifest seal")
    manifest_digest = sha256(IMPLEMENTATION_MANIFEST)
    require(
        seal_fields[0] == manifest_digest,
        "implementation-manifest seal mismatch",
    )
    manifest = strict_json(IMPLEMENTATION_MANIFEST)
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "empty implementation manifest")
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    self_relative = str(SELF.relative_to(ROOT))
    require(
        row_map.get(self_relative) == sha256(SELF),
        "comparator is not the presealed implementation",
    )
    for relative, expected in sorted(row_map.items()):
        require(
            sha256(ROOT / relative) == expected,
            f"presealed implementation drift: {relative}",
        )
    return manifest_digest, row_map


def validate_adjacent_seal(path: Path, expected_digest: str, label: str) -> None:
    seal = Path(f"{path}.seal.sha256")
    require(seal.is_file(), f"{label} adjacent seal is missing")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"{label} adjacent seal is malformed")
    require(fields[0] == expected_digest, f"{label} adjacent-seal hash mismatch")
    require(fields[1] == path.name, f"{label} adjacent-seal filename mismatch")


def validate_component_maps(manifest: Mapping[str, Any], lane: str) -> None:
    scalar_components = manifest.get("scalar_components")
    matrix_components = manifest.get("matrix_components")
    require(isinstance(scalar_components, dict), f"{lane} scalar component map missing")
    require(
        set(scalar_components) == set(SCALAR_CATEGORIES),
        f"{lane} scalar component categories differ from sealed inventory",
    )
    require(isinstance(matrix_components, dict), f"{lane} matrix component map missing")
    require(
        set(matrix_components) == set(MATRIX_CATEGORIES),
        f"{lane} matrix component categories differ from sealed inventory",
    )
    for category, values in scalar_components.items():
        require(isinstance(values, dict) and values, f"{lane} {category} map is empty")
        require(
            set(values) == EXPECTED_SCALAR_IDENTIFIERS[category],
            f"{lane} {category} identifiers differ from sealed inventory",
        )
        for key, value in values.items():
            parse_scalar(value, f"{lane}.{category}.{key}")
    for category, values in matrix_components.items():
        require(isinstance(values, dict) and values, f"{lane} {category} map is empty")
        require(
            set(values) == EXPECTED_COMPONENT_IDENTIFIERS[category],
            f"{lane} {category} identifiers differ from sealed inventory",
        )
        require(
            all(
                isinstance(identifier, str)
                and identifier
                and isinstance(npz_key, str)
                and npz_key
                for identifier, npz_key in values.items()
            ),
            f"{lane} {category} matrix map is malformed",
        )
    all_matrix_keys = [
        npz_key
        for values in matrix_components.values()
        for npz_key in values.values()
    ]
    require(
        len(all_matrix_keys) == len(set(all_matrix_keys)),
        f"{lane} component map aliases distinct components",
    )


def load_bundle(
    lane: str,
    json_path: Path,
    npz_path: Path,
    expected_json_sha256: str,
    expected_npz_sha256: str,
) -> Bundle:
    json_data, json_digest = validate_file(
        json_path, expected_json_sha256, f"{lane} JSON"
    )
    npz_data, npz_digest = validate_file(
        npz_path, expected_npz_sha256, f"{lane} NPZ"
    )
    validate_adjacent_seal(json_path, json_digest, f"{lane} JSON")
    validate_adjacent_seal(npz_path, npz_digest, f"{lane} NPZ")
    payload = strict_json_from_buffer(json_data, f"{lane} JSON")
    require(payload.get("schema") == BUNDLE_SCHEMA, f"{lane} bundle schema mismatch")
    require(payload.get("lane") == lane, f"{lane} lane identity mismatch")
    require(payload.get("spec_sha256") == SPEC_SHA256, f"{lane} spec binding mismatch")
    require(payload.get("npz_sha256") == npz_digest, f"{lane} NPZ binding mismatch")
    require(payload.get("sealed") is True, f"{lane} bundle is not sealed")
    require(payload.get("immutable_bundle") is True, f"{lane} bundle is not immutable")
    require(payload.get("alpha_computed") is False, f"{lane} alpha firewall failed")
    require(
        payload.get("coupling_evaluation_authorized") is False,
        f"{lane} coupling firewall failed",
    )
    require(payload.get("proof_authorized") is False, f"{lane} proof firewall failed")
    runtime_attestation = payload.get("runtime_attestation")
    require(
        isinstance(runtime_attestation, dict),
        f"{lane} runtime attestation is absent",
    )
    require(
        runtime_attestation.get("schema")
        == "stage8_t7_content_addressed_runtime_attestation_v001",
        f"{lane} runtime-attestation schema mismatch",
    )
    require(
        runtime_attestation.get("runtime_manifest_sha256")
        == RUNTIME_MANIFEST_SHA256,
        f"{lane} runtime-manifest binding mismatch",
    )
    require(
        runtime_attestation.get("python_isolated") is True
        and runtime_attestation.get("python_no_site") is True,
        f"{lane} runtime isolation flags are absent",
    )
    require(
        runtime_attestation.get("malicious_interpreter_or_kernel_resistance_claimed")
        is False,
        f"{lane} runtime overstates its threat model",
    )
    require(
        runtime_attestation.get("python_standard_library_trusted_host_boundary")
        is True
        and runtime_attestation.get("accelerate_framework_trusted_host_boundary")
        is True
        and runtime_attestation.get("loaded_native_dependencies_content_addressed")
        is False,
        f"{lane} runtime trusted-host boundary is not disclosed",
    )
    if lane == "independent":
        require(
            payload.get("precomparison_committed") is True,
            "independent precomparison commitment is absent",
        )
        require(
            payload.get("primary_output_paths_readable_during_construction") is False,
            "independent lane did not attest to the primary-path read fence",
        )

    # Repair binding R2: a bundle that does not declare and carry the frozen
    # generator-pieces schema blocks.  Lineage cannot be waived by omission.
    require(
        payload.get("generator_pieces_schema") == GENERATOR_PIECES_SCHEMA,
        f"{lane} bundle does not carry the frozen generator-pieces schema",
    )
    expected_midpoints = GENERATOR_MIDPOINT_COUNTS[lane]
    require(
        payload.get("generator_midpoint_count")
        == {
            ell: expected_midpoints
            for ell in EXPECTED_DISCRETE_LABELS["ell"]
        },
        f"{lane} generator midpoint count differs from the frozen grid",
    )

    manifest = payload.get("manifest")
    require(isinstance(manifest, dict), f"{lane} manifest missing")
    require(
        payload.get("manifest_sha256") == canonical_sha256(manifest),
        f"{lane} manifest self-hash mismatch",
    )
    dimensions = manifest.get("dimensions")
    labels = manifest.get("discrete_labels")
    npz_keys = manifest.get("npz_keys")
    require(isinstance(dimensions, dict) and dimensions, f"{lane} dimensions missing")
    require(
        dimensions == EXPECTED_DIMENSIONS,
        f"{lane} carrier dimensions differ from sealed inventory",
    )
    require(
        labels == EXPECTED_DISCRETE_LABELS,
        f"{lane} discrete labels differ from sealed inventory",
    )
    require(
        isinstance(npz_keys, list)
        and npz_keys
        and npz_keys == sorted(set(npz_keys))
        and all(isinstance(key, str) and key for key in npz_keys),
        f"{lane} NPZ key manifest is malformed",
    )
    validate_component_maps(manifest, lane)

    basis_overlap_key = manifest.get("basis_overlap_key")
    if lane == "independent":
        require(
            isinstance(basis_overlap_key, str) and basis_overlap_key,
            "independent basis-overlap key missing",
        )
    else:
        require(
            basis_overlap_key is None,
            "primary bundle may not supply a fitted basis-overlap matrix",
        )

    try:
        # Finding 1: the NPZ is decoded from the exact hashed buffer.
        with np.load(io.BytesIO(npz_data), allow_pickle=False) as archive:
            require(
                sorted(archive.files) == npz_keys,
                f"{lane} NPZ keys differ from sealed manifest",
            )
            arrays = {key: np.array(archive[key], copy=True) for key in archive.files}
    except (OSError, ValueError, KeyError) as error:
        raise ComparisonBlocked(f"unable to load {lane} NPZ: {error}") from error
    for key, array in arrays.items():
        require(
            np.issubdtype(array.dtype, np.number),
            f"{lane} NPZ component {key} is not numeric",
        )
        require(
            bool(np.all(np.isfinite(array))),
            f"{lane} NPZ component {key} is non-finite",
        )

    referenced = {
        npz_key
        for values in manifest["matrix_components"].values()
        for npz_key in values.values()
    }
    if basis_overlap_key is not None:
        referenced.add(basis_overlap_key)
    require(referenced <= set(arrays), f"{lane} manifest references absent NPZ components")

    return Bundle(
        lane=lane,
        json_path=json_path,
        npz_path=npz_path,
        json_sha256=json_digest,
        npz_sha256=npz_digest,
        payload=payload,
        manifest=manifest,
        arrays=arrays,
    )


def operator_norm(matrix: np.ndarray, label: str) -> float:
    require(matrix.ndim == 2, f"{label} is not a matrix")
    try:
        value = float(np.linalg.norm(matrix, ord=2))
    except np.linalg.LinAlgError as error:
        raise ComparisonBlocked(f"operator norm failed for {label}: {error}") from error
    require(np.isfinite(value), f"operator norm is non-finite for {label}")
    return value


def expected_primary_labels() -> np.ndarray:
    return np.asarray(
        [
            (a, b, c, spin)
            for a in range(2)
            for b in range(2)
            for c in range(2)
            for spin in range(4)
        ],
        dtype=np.int64,
    )


def expected_independent_labels() -> np.ndarray:
    return np.asarray(
        [
            (a, b, c, spin)
            for spin in range(4)
            for c in reversed(range(2))
            for b in range(2)
            for a in reversed(range(2))
        ],
        dtype=np.int64,
    )


def expected_independent_phases(labels: np.ndarray) -> np.ndarray:
    return np.asarray(
        [
            (1j) ** ((int(a) + 2 * int(b) + 3 * int(c) + int(spin)) % 4)
            for a, b, c, spin in labels
        ],
        dtype=complex,
    )


def expected_basis_overlap() -> np.ndarray:
    primary = expected_primary_labels()
    independent = expected_independent_labels()
    phases = expected_independent_phases(independent)
    overlap = np.zeros((32, 32), dtype=complex)
    for row, left in enumerate(primary):
        for column, right in enumerate(independent):
            if bool(np.array_equal(left, right)):
                overlap[row, column] = phases[column]
    return overlap


def expected_diagnostic_keys(lane: str) -> set[str]:
    keys = {
        *(f"diag_h0__{ell}" for ell in EXPECTED_DISCRETE_LABELS["ell"]),
        *(
            f"diag_connection_midpoint__{ell}"
            for ell in EXPECTED_DISCRETE_LABELS["ell"]
        ),
    }
    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        for pair in ("p1", "p2"):
            for kernel in EXPECTED_DISCRETE_LABELS["kernels"]:
                if lane == "primary":
                    for resolution in (12, 24, 48):
                        keys.add(
                            f"diag_primary__{ell}__n{resolution}"
                            f"__{pair}__{kernel}"
                        )
                    keys.add(
                        f"diag_primary_secondary_quadrature__{ell}"
                        f"__n48__{pair}__{kernel}"
                    )
                else:
                    for resolution in (192, 384):
                        keys.add(
                            f"diag_independent__{ell}__n{resolution}"
                            f"__{pair}__{kernel}"
                        )
    if lane == "primary":
        keys.update(
            f"basis_labels__{ell}" for ell in EXPECTED_DISCRETE_LABELS["ell"]
        )
    else:
        keys.update(
            {
                "primary_labels",
                "independent_labels",
                "independent_phases",
                "basis_overlap_primary_from_independent",
            }
        )
    return keys


def validate_basis_and_diagnostic_provenance(bundle: Bundle) -> None:
    expected_keys = expected_diagnostic_keys(bundle.lane)
    require(
        expected_keys <= set(bundle.arrays),
        f"{bundle.lane} diagnostic/provenance arrays are incomplete",
    )
    primary_labels = expected_primary_labels()
    if bundle.lane == "primary":
        for ell in EXPECTED_DISCRETE_LABELS["ell"]:
            require(
                np.array_equal(bundle.arrays[f"basis_labels__{ell}"], primary_labels),
                f"primary basis labels changed for {ell}",
            )
        return
    independent_labels = expected_independent_labels()
    phases = expected_independent_phases(independent_labels)
    require(
        np.array_equal(bundle.arrays["primary_labels"], primary_labels),
        "independent lane primary-label provenance changed",
    )
    require(
        np.array_equal(bundle.arrays["independent_labels"], independent_labels),
        "independent basis labels changed",
    )
    require(
        np.max(np.abs(bundle.arrays["independent_phases"] - phases)) <= 2.0e-15,
        "independent basis phases changed",
    )
    overlap = bundle.arrays["basis_overlap_primary_from_independent"]
    require(
        operator_norm(overlap - expected_basis_overlap(), "basis-overlap provenance")
        <= BASIS_UNITARITY_TOLERANCE,
        "basis overlap is not the predeclared Hermite label/phase overlap",
    )


def generator_piece_keys(ell: str) -> tuple[str, ...]:
    return (
        f"genpiece_midpoint_times__{ell}",
        f"genpiece_M_stack__{ell}",
        f"genpiece_B_stack__{ell}",
        f"genpiece_h0__{ell}",
        f"genpiece_p_stack__{ell}",
    )


def validate_generator_pieces(bundle: Bundle) -> None:
    """Structural + algebraic gates on the stored generator pieces (R2)."""
    steps = GENERATOR_MIDPOINT_COUNTS[bundle.lane]
    lane = bundle.lane
    shared_keys = ("genpiece_alpha_stack", "genpiece_Sn")
    expected_shapes: dict[str, tuple[int, ...]] = {
        "genpiece_alpha_stack": (3, 4, 4),
        "genpiece_Sn": (4, 4),
    }
    expected_dtypes: dict[str, type] = {
        "genpiece_alpha_stack": np.complexfloating,
        "genpiece_Sn": np.complexfloating,
    }
    required = list(shared_keys)
    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        times_key, m_key, b_key, h0_key, p_key = generator_piece_keys(ell)
        required.extend((times_key, m_key, b_key, h0_key, p_key))
        expected_shapes[times_key] = (steps,)
        expected_shapes[m_key] = (steps, 8, 8)
        expected_shapes[b_key] = (steps, 8, 8)
        expected_shapes[h0_key] = (32, 32)
        expected_shapes[p_key] = (3, 8, 8)
        expected_dtypes[times_key] = np.floating
        for key in (m_key, b_key, h0_key, p_key):
            expected_dtypes[key] = np.complexfloating
    for key in required:
        require(key in bundle.arrays, f"{lane} bundle is missing {key}")
        array = bundle.arrays[key]
        require(
            array.shape == expected_shapes[key],
            f"{lane} {key} has shape {array.shape}, expected {expected_shapes[key]}",
        )
        require(
            np.issubdtype(array.dtype, expected_dtypes[key]),
            f"{lane} {key} dtype {array.dtype} violates the frozen schema",
        )
    alpha_stack = bundle.arrays["genpiece_alpha_stack"]
    incidence = bundle.arrays["genpiece_Sn"]
    hermitian_pieces: list[tuple[str, np.ndarray]] = [
        ("genpiece_Sn", incidence),
        *((f"genpiece_alpha_stack[{j}]", alpha_stack[j]) for j in range(3)),
    ]
    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        times_key, m_key, b_key, h0_key, p_key = generator_piece_keys(ell)
        times = bundle.arrays[times_key]
        expected_times = (np.arange(steps, dtype=np.float64) + 0.5) / steps
        require(
            float(np.max(np.abs(times - expected_times))) <= MIDPOINT_TIME_TOLERANCE,
            f"{lane} {times_key} differs from the frozen midpoint grid",
        )
        p_stack = bundle.arrays[p_key]
        h0 = bundle.arrays[h0_key]
        hermitian_pieces.append((h0_key, h0))
        hermitian_pieces.extend(
            (f"{p_key}[{j}]", p_stack[j]) for j in range(3)
        )
        hermitian_pieces.extend(
            (f"{m_key}[{k}]", bundle.arrays[m_key][k]) for k in range(steps)
        )
        hermitian_pieces.extend(
            (f"{b_key}[{k}]", bundle.arrays[b_key][k]) for k in range(steps)
        )
        # The stored h0 is the ACTUAL matrix the lane used in its own basis
        # (R2).  The identity h0 = sum_j kron(p_j, alpha_j) is checked in the
        # sealed tensor convention: directly for the primary lane, and for
        # the independent lane after transport through the predeclared
        # label/phase overlap (comparator-owned; the bundle's own overlap is
        # separately pinned to it at 2e-11).
        assembled_h0 = sum(
            np.kron(p_stack[j], alpha_stack[j]) for j in range(3)
        )
        if lane == "independent":
            transport = expected_basis_overlap()
            stored_h0_canonical = transport @ h0 @ transport.conjugate().T
        else:
            stored_h0_canonical = h0
        require(
            operator_norm(
                stored_h0_canonical - assembled_h0,
                f"{lane}.{h0_key}.assembly",
            )
            <= HERMITICITY_PROJECTOR_TOLERANCE,
            f"{lane} {h0_key} is not the tensor assembly of its stored pieces",
        )
    for label, piece in hermitian_pieces:
        require(
            operator_norm(
                piece - piece.conjugate().T,
                f"{lane}.{label}.hermiticity",
            )
            <= HERMITICITY_PROJECTOR_TOLERANCE,
            f"{lane} generator piece is not Hermitian: {label}",
        )


def typed_envelope(times: np.ndarray) -> np.ndarray:
    # v(t) and r(t) typed from the sealed spec text (R2): r(t)=min(t,1-t),
    # v(t)=(pi/sqrt(2))*32*r(t)^3.
    radius = np.minimum(times, 1.0 - times)
    return (np.pi / np.sqrt(2.0)) * 32.0 * radius**3


def midpoint_product_propagator(h_stack: np.ndarray, dt: float) -> np.ndarray:
    """Chronological product of exp(-i h(t_mid) dt) via Hermitian eigh."""
    hermitian = 0.5 * (h_stack + np.conjugate(np.swapaxes(h_stack, -1, -2)))
    try:
        values, vectors = np.linalg.eigh(hermitian)
    except np.linalg.LinAlgError as error:
        raise ComparisonBlocked(
            f"lineage eigendecomposition failed: {error}"
        ) from error
    phases = np.exp(-1j * dt * values)
    steps = vectors @ (
        phases[..., None] * np.conjugate(np.swapaxes(vectors, -1, -2))
    )
    value = np.eye(h_stack.shape[-1], dtype=complex)
    for step in steps:
        value = step @ value
    return value


def validate_generator_propagator_lineage(
    bundle: Bundle,
    overlap: np.ndarray | None,
) -> dict[str, Any]:
    """Lineage gate (R1 item 1, R2, R3): rebuild every stored one-particle
    propagator from the lane's stored generator pieces with this comparator's
    OWN tensor-assembly code and an independent midpoint product integrator,
    and require operator-2-norm agreement within the preregistered budget.
    Every (ell, lambda, history) combination used by any gated response must
    pass separately.  The independent lane stores its propagators in its own
    basis; they are transported to the sealed tensor convention through the
    predeclared basis overlap (already pinned at 2e-11) before comparison."""
    lane = bundle.lane
    budget = LINEAGE_BUDGETS[lane]
    steps = GENERATOR_MIDPOINT_COUNTS[lane]
    dt = 1.0 / steps
    alpha_stack = bundle.arrays["genpiece_alpha_stack"]
    incidence = bundle.arrays["genpiece_Sn"]
    eigenvalues = [
        manifest_scalar(bundle, "record_eigenvalues", f"l{index}")
        for index in range(3)
    ]
    histories = [
        manifest_scalar(bundle, "coefficients", f"history.a{index}")
        for index in range(5)
    ]
    maximum_residual = 0.0
    cases = 0
    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        times_key, m_key, b_key, h0_key, p_key = generator_piece_keys(ell)
        times = bundle.arrays[times_key]
        envelope = typed_envelope(times)
        # Comparator-owned tensor assembly (no lane import): spinor fastest.
        # h0 is assembled here from the stored momentum and alpha pieces; the
        # stored genpiece_h0 was already gated against this assembly (in the
        # sealed convention) by validate_generator_pieces.
        p_stack = bundle.arrays[p_key]
        h0 = sum(np.kron(p_stack[j], alpha_stack[j]) for j in range(3))
        record_stack = np.stack(
            [
                float(envelope[k]) * np.kron(bundle.arrays[m_key][k], incidence)
                for k in range(steps)
            ]
        )
        connection_stack = np.stack(
            [
                -np.kron(bundle.arrays[b_key][k], alpha_stack[0])
                for k in range(steps)
            ]
        )
        for history_index, history in enumerate(histories):
            for record_index, record_value in enumerate(eigenvalues):
                h_stack = (
                    h0[None, :, :]
                    + record_value.real * record_stack
                    + history.real * connection_stack
                )
                rebuilt = midpoint_product_propagator(h_stack, dt)
                stored = matrix_for(
                    bundle,
                    "propagators",
                    f"{ell}.a{history_index}.l{record_index}",
                )
                if overlap is not None:
                    stored = overlap @ stored @ overlap.conjugate().T
                residual = operator_norm(
                    rebuilt - stored,
                    f"{lane}.lineage.{ell}.a{history_index}.l{record_index}",
                )
                cases += 1
                require(
                    residual <= budget,
                    f"{lane} generator-to-propagator lineage failed for "
                    f"{ell}.a{history_index}.l{record_index}: "
                    f"{residual} > {budget}",
                )
                maximum_residual = max(maximum_residual, residual)
    return {
        "lane": lane,
        "generator_pieces_schema": GENERATOR_PIECES_SCHEMA,
        "midpoint_count": steps,
        "integrator":
            "comparator_owned_midpoint_product_hermitian_eigendecomposition",
        "budget_operator_2_norm": budget,
        "maximum_residual": float(maximum_residual),
        "cases": cases,
        "passed": True,
    }


def comparison_row(
    category: str,
    identifier: str,
    difference: float,
    tolerance: float,
) -> dict[str, Any]:
    return {
        "category": category,
        "identifier": identifier,
        "difference": float(difference),
        "tolerance": float(tolerance),
        "passed": bool(difference <= tolerance),
    }


def compare_scalar_categories(
    primary: Bundle,
    independent: Bundle,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for category in SCALAR_CATEGORIES:
        primary_values = primary.manifest["scalar_components"][category]
        independent_values = independent.manifest["scalar_components"][category]
        require(
            set(primary_values) == set(independent_values),
            f"{category} labels differ",
        )
        for identifier in sorted(primary_values):
            left = parse_scalar(primary_values[identifier], f"primary.{category}.{identifier}")
            right = parse_scalar(
                independent_values[identifier],
                f"independent.{category}.{identifier}",
            )
            rows.append(
                comparison_row(
                    category,
                    identifier,
                    abs(left - right),
                    SCALAR_TOLERANCE,
                )
            )
    return rows


def matrix_for(bundle: Bundle, category: str, identifier: str) -> np.ndarray:
    key = bundle.manifest["matrix_components"][category][identifier]
    return bundle.arrays[key]


def compare_matrix_categories(
    primary: Bundle,
    independent: Bundle,
    overlap: np.ndarray,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    source_dimension = primary.manifest["dimensions"]["source_dimension"]
    record_dimension = primary.manifest["dimensions"]["record_dimension"]
    for category in MATRIX_CATEGORIES:
        primary_values = primary.manifest["matrix_components"][category]
        independent_values = independent.manifest["matrix_components"][category]
        require(set(primary_values) == set(independent_values), f"{category} labels differ")
        for identifier in sorted(primary_values):
            primary_matrix = matrix_for(primary, category, identifier)
            independent_matrix = matrix_for(independent, category, identifier)
            if category == "record_projectors":
                require(
                    primary_matrix.shape == (record_dimension, record_dimension),
                    f"primary {category}.{identifier} shape mismatch",
                )
                require(
                    independent_matrix.shape == (record_dimension, record_dimension),
                    f"independent {category}.{identifier} shape mismatch",
                )
                transported = independent_matrix
                tolerance = PROJECTOR_TOLERANCE
            else:
                require(
                    primary_matrix.shape == (source_dimension, source_dimension),
                    f"primary {category}.{identifier} shape mismatch",
                )
                require(
                    independent_matrix.shape == (source_dimension, source_dimension),
                    f"independent {category}.{identifier} shape mismatch",
                )
                transported = overlap @ independent_matrix @ overlap.conjugate().T
                tolerance = TRANSPORTED_MATRIX_TOLERANCE
            difference = operator_norm(
                primary_matrix - transported,
                f"{category}.{identifier}",
            )
            rows.append(comparison_row(category, identifier, difference, tolerance))
    return rows


def finite_number(value: Any, label: str) -> float:
    require(
        isinstance(value, (int, float)) and not isinstance(value, bool),
        f"{label} is not numeric",
    )
    result = float(value)
    require(np.isfinite(result), f"{label} is non-finite")
    return result


def require_at_most(value: Any, threshold: float, label: str) -> float:
    number = finite_number(value, label)
    require(number <= threshold, f"{label} exceeds {threshold}: {number}")
    return number


def manifest_scalar(bundle: Bundle, category: str, identifier: str) -> complex:
    return parse_scalar(
        bundle.manifest["scalar_components"][category][identifier],
        f"{bundle.lane}.{category}.{identifier}",
    )


def recompute_bundle_internal_gates(bundle: Bundle) -> dict[str, float]:
    identity_source = np.eye(32, dtype=complex)
    identity_record = np.eye(3, dtype=complex)
    ready = np.array([1.0, 0.0, 0.0], dtype=complex)
    pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
    projectors = [
        matrix_for(bundle, "record_projectors", f"l{index}")
        for index in range(3)
    ]
    eigenvalues = [
        manifest_scalar(bundle, "record_eigenvalues", f"l{index}")
        for index in range(3)
    ]
    probabilities = [
        manifest_scalar(bundle, "coefficients", f"p.l{index}")
        for index in range(3)
    ]
    pointer_weights = [
        manifest_scalar(bundle, "coefficients", f"w.l{index}")
        for index in range(3)
    ]
    record = sum(
        eigenvalue * projector
        for eigenvalue, projector in zip(eigenvalues, projectors)
    )
    expected_record = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    maxima = {
        "record_hermiticity": operator_norm(
            record - record.conjugate().T,
            f"{bundle.lane}.record_hermiticity",
        ),
        "record_matrix_reconstruction": operator_norm(
            record - expected_record,
            f"{bundle.lane}.record_matrix_reconstruction",
        ),
        "record_spectral_completeness": operator_norm(
            sum(projectors) - identity_record,
            f"{bundle.lane}.record_spectral_completeness",
        ),
        "record_projector_algebra": 0.0,
        "coefficient_reconstruction": 0.0,
        "sealed_scalar_inputs": 0.0,
        "generator_hermiticity": 0.0,
        "propagator_unitarity": 0.0,
        "cross_operator_reconstruction": 0.0,
        "aggregate_reconstruction": 0.0,
        "direct_kraus_completeness": 0.0,
        "direct_response_reconstruction": 0.0,
        "gaussian_direct_agreement": 0.0,
        "same_history_identity": 0.0,
        "contraction_or_positivity_violation": 0.0,
        "same_history_pointer_spectral_violation": 0.0,
        # Finding 5: spectral-Kraus rebuild and adjoint exchange enforced for
        # BOTH lanes at the sealed 3e-9 internal-identity threshold.
        "spectral_kraus_reconstruction": 0.0,
        "adjoint_exchange": 0.0,
    }
    for left, projector_left in enumerate(projectors):
        maxima["record_projector_algebra"] = max(
            maxima["record_projector_algebra"],
            operator_norm(
                projector_left - projector_left.conjugate().T,
                f"{bundle.lane}.projector_hermiticity.l{left}",
            ),
        )
        for right, projector_right in enumerate(projectors):
            expected = projector_left if left == right else np.zeros((3, 3), complex)
            maxima["record_projector_algebra"] = max(
                maxima["record_projector_algebra"],
                operator_norm(
                    projector_left @ projector_right - expected,
                    f"{bundle.lane}.projector_product.l{left}.l{right}",
                ),
            )
        reconstructed_probability = np.vdot(ready, projector_left @ ready)
        reconstructed_weight = np.vdot(pointer, projector_left @ ready)
        maxima["coefficient_reconstruction"] = max(
            maxima["coefficient_reconstruction"],
            abs(reconstructed_probability - probabilities[left]),
            abs(reconstructed_weight - pointer_weights[left]),
        )
    maxima["coefficient_reconstruction"] = max(
        maxima["coefficient_reconstruction"],
        abs(sum(probabilities) - 1.0),
    )
    for identifier, expected in {
        "ell.ell0": 1.0,
        "ell.ell1": float(np.sqrt(2.0)),
        "history.a0": 0.0,
        "history.a1": 0.07,
        "history.a2": -0.11,
        "history.a3": 0.13,
        "history.a4": 0.04,
    }.items():
        maxima["sealed_scalar_inputs"] = max(
            maxima["sealed_scalar_inputs"],
            abs(manifest_scalar(bundle, "coefficients", identifier) - expected),
        )

    for ell in EXPECTED_DISCRETE_LABELS["ell"]:
        for diagnostic_key in (
            f"diag_h0__{ell}",
            f"diag_connection_midpoint__{ell}",
        ):
            generator = bundle.arrays[diagnostic_key]
            maxima["generator_hermiticity"] = max(
                maxima["generator_hermiticity"],
                operator_norm(
                    generator - generator.conjugate().T,
                    f"{bundle.lane}.{diagnostic_key}.hermiticity",
                ),
            )
        for history in EXPECTED_DISCRETE_LABELS["histories"]:
            propagators = [
                matrix_for(bundle, "propagators", f"{ell}.{history}.l{index}")
                for index in range(3)
            ]
            for record_index, propagator in enumerate(propagators):
                maxima["propagator_unitarity"] = max(
                    maxima["propagator_unitarity"],
                    operator_norm(
                        propagator.conjugate().T @ propagator - identity_source,
                        f"{bundle.lane}.{ell}.{history}.l{record_index}.unitarity",
                    ),
                )
            kraus = [
                matrix_for(bundle, "direct_kraus_members", f"{ell}.{history}.x{index}")
                for index in range(3)
            ]
            kraus_completeness = sum(
                member.conjugate().T @ member for member in kraus
            )
            maxima["direct_kraus_completeness"] = max(
                maxima["direct_kraus_completeness"],
                operator_norm(
                    kraus_completeness - identity_source,
                    f"{bundle.lane}.{ell}.{history}.kraus_completeness",
                ),
            )
            # Finding 5: rebuild K_x = sum_lambda <x|P_lambda|ready> u_lambda
            # from the stored propagators + projectors and gate against the
            # stored direct Kraus members.
            for outcome in range(3):
                rebuilt_member = sum(
                    projectors[record_index][outcome, 0]
                    * propagators[record_index]
                    for record_index in range(3)
                )
                maxima["spectral_kraus_reconstruction"] = max(
                    maxima["spectral_kraus_reconstruction"],
                    operator_norm(
                        rebuilt_member - kraus[outcome],
                        f"{bundle.lane}.{ell}.{history}.x{outcome}"
                        ".spectral_kraus",
                    ),
                )
            # Execution binding B3: same-history identity checks for ALL five
            # frozen history values, both kernels, rebuilt from the stored
            # propagators (nothing removed; the p0 aggregate check below is
            # retained unchanged).
            same_all = sum(
                probabilities[index]
                * (propagators[index].conjugate().T @ propagators[index])
                for index in range(3)
            )
            maxima["same_history_identity"] = max(
                maxima["same_history_identity"],
                operator_norm(
                    same_all - identity_source,
                    f"{bundle.lane}.{ell}.{history}.same_history_identity",
                ),
            )
            same_pointer = sum(
                pointer_weights[left].conjugate()
                * pointer_weights[right]
                * (propagators[left].conjugate().T @ propagators[right])
                for left in range(3)
                for right in range(3)
            )
            pointer_spectrum = np.linalg.eigvalsh(
                0.5 * (same_pointer + same_pointer.conjugate().T)
            )
            maxima["same_history_pointer_spectral_violation"] = max(
                maxima["same_history_pointer_spectral_violation"],
                max(0.0, -float(pointer_spectrum[0])),
                max(0.0, float(pointer_spectrum[-1]) - 1.0),
            )

        for pair_index, (plus_history, minus_history) in enumerate(
            EXPECTED_DISCRETE_LABELS["history_pairs"]
        ):
            cross: dict[tuple[int, int], np.ndarray] = {}
            for left in range(3):
                left_propagator = matrix_for(
                    bundle,
                    "propagators",
                    f"{ell}.{minus_history}.l{left}",
                )
                for right in range(3):
                    right_propagator = matrix_for(
                        bundle,
                        "propagators",
                        f"{ell}.{plus_history}.l{right}",
                    )
                    expected_cross = (
                        left_propagator.conjugate().T @ right_propagator
                    )
                    stored_cross = matrix_for(
                        bundle,
                        "cross_operators",
                        f"{ell}.p{pair_index}.mu{left}.l{right}",
                    )
                    maxima["cross_operator_reconstruction"] = max(
                        maxima["cross_operator_reconstruction"],
                        operator_norm(
                            stored_cross - expected_cross,
                            f"{bundle.lane}.{ell}.p{pair_index}.cross.{left}.{right}",
                        ),
                    )
                    cross[left, right] = stored_cross
            expected_all = sum(
                probabilities[index] * cross[index, index]
                for index in range(3)
            )
            expected_pointer = sum(
                pointer_weights[left].conjugate()
                * pointer_weights[right]
                * cross[left, right]
                for left in range(3)
                for right in range(3)
            )
            plus_kraus = [
                matrix_for(
                    bundle,
                    "direct_kraus_members",
                    f"{ell}.{plus_history}.x{index}",
                )
                for index in range(3)
            ]
            minus_kraus = [
                matrix_for(
                    bundle,
                    "direct_kraus_members",
                    f"{ell}.{minus_history}.x{index}",
                )
                for index in range(3)
            ]
            expected_direct_all = sum(
                left.conjugate().T @ right
                for left, right in zip(minus_kraus, plus_kraus)
            )
            expected_direct_pointer = (
                minus_kraus[1].conjugate().T @ plus_kraus[1]
            )
            for kernel, expected_aggregate, expected_direct in (
                ("all", expected_all, expected_direct_all),
                ("pointer", expected_pointer, expected_direct_pointer),
            ):
                identifier = f"{ell}.p{pair_index}.{kernel}"
                aggregate = matrix_for(bundle, "aggregate_kernels", identifier)
                direct = matrix_for(bundle, "direct_responses", identifier)
                maxima["aggregate_reconstruction"] = max(
                    maxima["aggregate_reconstruction"],
                    operator_norm(
                        aggregate - expected_aggregate,
                        f"{bundle.lane}.{identifier}.aggregate_reconstruction",
                    ),
                )
                maxima["direct_response_reconstruction"] = max(
                    maxima["direct_response_reconstruction"],
                    operator_norm(
                        direct - expected_direct,
                        f"{bundle.lane}.{identifier}.direct_reconstruction",
                    ),
                )
                maxima["gaussian_direct_agreement"] = max(
                    maxima["gaussian_direct_agreement"],
                    operator_norm(
                        aggregate - direct,
                        f"{bundle.lane}.{identifier}.gaussian_direct",
                    ),
                )
                maxima["contraction_or_positivity_violation"] = max(
                    maxima["contraction_or_positivity_violation"],
                    max(0.0, operator_norm(aggregate, identifier) - 1.0),
                )
                if pair_index == 0 and kernel == "all":
                    maxima["same_history_identity"] = max(
                        maxima["same_history_identity"],
                        operator_norm(
                            aggregate - identity_source,
                            f"{bundle.lane}.{ell}.same_history_identity",
                        ),
                    )
                if pair_index == 0 and kernel == "pointer":
                    spectral_values = np.linalg.eigvalsh(
                        0.5 * (aggregate + aggregate.conjugate().T)
                    )
                    maxima["same_history_pointer_spectral_violation"] = max(
                        maxima["same_history_pointer_spectral_violation"],
                        max(0.0, -float(spectral_values[0])),
                        max(0.0, float(spectral_values[-1]) - 1.0),
                    )
            # Finding 5: adjoint-exchange residual R(a+,a-)^dagger = R(a-,a+)
            # enforced for both lanes on both nontrivial pairs and both
            # kernels, with the exchanged response rebuilt from the stored
            # propagators (aggregate route) and stored Kraus members (direct
            # route).
            if pair_index != 0:
                plus_propagators = [
                    matrix_for(
                        bundle,
                        "propagators",
                        f"{ell}.{plus_history}.l{index}",
                    )
                    for index in range(3)
                ]
                minus_propagators = [
                    matrix_for(
                        bundle,
                        "propagators",
                        f"{ell}.{minus_history}.l{index}",
                    )
                    for index in range(3)
                ]
                reverse_all = sum(
                    probabilities[index]
                    * (
                        plus_propagators[index].conjugate().T
                        @ minus_propagators[index]
                    )
                    for index in range(3)
                )
                reverse_pointer = sum(
                    pointer_weights[left].conjugate()
                    * pointer_weights[right]
                    * (
                        plus_propagators[left].conjugate().T
                        @ minus_propagators[right]
                    )
                    for left in range(3)
                    for right in range(3)
                )
                reverse_direct_all = sum(
                    left.conjugate().T @ right
                    for left, right in zip(plus_kraus, minus_kraus)
                )
                reverse_direct_pointer = (
                    plus_kraus[1].conjugate().T @ minus_kraus[1]
                )
                for kernel, reverse_aggregate, reverse_direct in (
                    ("all", reverse_all, reverse_direct_all),
                    ("pointer", reverse_pointer, reverse_direct_pointer),
                ):
                    identifier = f"{ell}.p{pair_index}.{kernel}"
                    aggregate = matrix_for(
                        bundle, "aggregate_kernels", identifier
                    )
                    direct = matrix_for(bundle, "direct_responses", identifier)
                    maxima["adjoint_exchange"] = max(
                        maxima["adjoint_exchange"],
                        operator_norm(
                            aggregate.conjugate().T - reverse_aggregate,
                            f"{bundle.lane}.{identifier}.adjoint_aggregate",
                        ),
                        operator_norm(
                            direct.conjugate().T - reverse_direct,
                            f"{bundle.lane}.{identifier}.adjoint_direct",
                        ),
                    )
    return {key: float(value) for key, value in maxima.items()}


def validate_lane_diagnostics(
    primary: Bundle,
    independent: Bundle,
    component_rows: list[dict[str, Any]],
    overlap: np.ndarray,
) -> dict[str, Any]:
    require(
        isinstance(primary.payload.get("comparison_diagnostics"), dict),
        "primary emitted diagnostics missing",
    )
    require(
        isinstance(independent.payload.get("comparison_diagnostics"), dict),
        "independent emitted diagnostics missing",
    )
    primary_values = recompute_bundle_internal_gates(primary)
    independent_values = recompute_bundle_internal_gates(independent)
    for lane, values in (
        ("primary", primary_values),
        ("independent", independent_values),
    ):
        for key, value in values.items():
            threshold = (
                RECORD_SPECTRAL_TOLERANCE
                if key in {
                    "record_matrix_reconstruction",
                    "record_spectral_completeness",
                    "coefficient_reconstruction",
                    "sealed_scalar_inputs",
                }
                else HERMITICITY_PROJECTOR_TOLERANCE
                if key in {
                    "record_hermiticity",
                    "record_projector_algebra",
                    "generator_hermiticity",
                }
                else INTERNAL_IDENTITY_TOLERANCE
            )
            require_at_most(value, threshold, f"{lane}.recomputed.{key}")

    matrix_difference = {
        (row["category"], row["identifier"]): finite_number(
            row["difference"],
            f"component.{row['category']}.{row['identifier']}",
        )
        for row in component_rows
    }
    convergence_rows: list[dict[str, Any]] = []
    tail_rows: list[dict[str, Any]] = []
    sensitivity_rows: list[dict[str, Any]] = []
    for ell_label in EXPECTED_DISCRETE_LABELS["ell"]:
        for pair_index in (1, 2):
            for kernel in ("all", "pointer"):
                label = f"p{pair_index}.{kernel}"
                primary_12 = primary.arrays[
                    f"diag_primary__{ell_label}__n12__p{pair_index}__{kernel}"
                ]
                primary_24 = primary.arrays[
                    f"diag_primary__{ell_label}__n24__p{pair_index}__{kernel}"
                ]
                primary_48 = primary.arrays[
                    f"diag_primary__{ell_label}__n48__p{pair_index}__{kernel}"
                ]
                require(
                    operator_norm(
                        primary_48
                        - matrix_for(
                            primary,
                            "aggregate_kernels",
                            f"{ell_label}.p{pair_index}.{kernel}",
                        ),
                        f"primary_diagnostic_binding.{ell_label}.{label}",
                    )
                    <= 2.0e-15,
                    f"primary production diagnostic is not bound to aggregate {ell_label}.{label}",
                )
                d_12_24 = operator_norm(
                    primary_24 - primary_12,
                    f"primary_convergence.{ell_label}.{label}.d12_24",
                )
                d_24_48 = operator_norm(
                    primary_48 - primary_24,
                    f"primary_convergence.{ell_label}.{label}.d24_48",
                )
                require(
                    d_24_48 > 1.0e-15,
                    f"unresolved primary convergence tail {ell_label}.{label}",
                )
                ratio = d_12_24 / d_24_48
                require(
                    ratio >= PRIMARY_CONVERGENCE_RATIO_MINIMUM,
                    f"primary convergence ratio failed {ell_label}.{label}: {ratio}",
                )
                convergence_rows.append(
                    {
                        "ell": ell_label,
                        "component": label,
                        "d_12_24": d_12_24,
                        "d_24_48": d_24_48,
                        "ratio": ratio,
                        "minimum": PRIMARY_CONVERGENCE_RATIO_MINIMUM,
                        "passed": True,
                    }
                )
                independent_192 = independent.arrays[
                    f"diag_independent__{ell_label}__n192"
                    f"__p{pair_index}__{kernel}"
                ]
                independent_384 = independent.arrays[
                    f"diag_independent__{ell_label}__n384"
                    f"__p{pair_index}__{kernel}"
                ]
                require(
                    operator_norm(
                        independent_384
                        - matrix_for(
                            independent,
                            "aggregate_kernels",
                            f"{ell_label}.p{pair_index}.{kernel}",
                        ),
                        f"independent_diagnostic_binding.{ell_label}.{label}",
                    )
                    <= 2.0e-15,
                    f"independent production diagnostic is not bound to aggregate "
                    f"{ell_label}.{label}",
                )
                tail = require_at_most(
                    operator_norm(
                        independent_384 - independent_192,
                        f"independent_tail.{ell_label}.{label}",
                    ),
                    INDEPENDENT_TAIL_TOLERANCE,
                    f"independent_tail.{ell_label}.{label}",
                )
                tail_rows.append(
                    {
                        "ell": ell_label,
                        "component": label,
                        "tail": tail,
                        "maximum": INDEPENDENT_TAIL_TOLERANCE,
                        "passed": True,
                    }
                )

        primary_connection_norm = operator_norm(
            primary.arrays[f"diag_connection_midpoint__{ell_label}"],
            f"primary_connection.{ell_label}.maximum_norm",
        )
        independent_connection_norm = operator_norm(
            independent.arrays[f"diag_connection_midpoint__{ell_label}"],
            f"independent_connection.{ell_label}.maximum_norm",
        )
        require(
            primary_connection_norm > CONNECTION_NORM_MINIMUM,
            f"primary connection insertion vanished for {ell_label}",
        )
        require(
            independent_connection_norm > CONNECTION_NORM_MINIMUM,
            f"independent connection insertion vanished for {ell_label}",
        )
        # Execution binding B2: every component of E_conn is evaluated at the
        # single frozen history pair (a_+,a_-)=(7/100,-11/100) — labels
        # (a1,a2), i.e. pair p1 — separately for each ell.  No other pair may
        # be substituted for any component.
        signal = operator_norm(
            matrix_for(
                primary,
                "aggregate_kernels",
                f"{ell_label}.p1.all",
            )
            - np.eye(32, dtype=complex),
            f"primary_connection.{ell_label}.signal",
        )
        primary_tail = operator_norm(
            primary.arrays[f"diag_primary__{ell_label}__n48__p1__all"]
            - primary.arrays[f"diag_primary__{ell_label}__n24__p1__all"],
            f"convergence.{ell_label}.p1.all.d_24_48",
        )
        quadrature_difference = operator_norm(
            primary.arrays[
                f"diag_primary_secondary_quadrature__{ell_label}__n48__p1__all"
            ]
            - primary.arrays[f"diag_primary__{ell_label}__n48__p1__all"],
            f"quadrature.{ell_label}.p1.all",
        )
        lane_difference = matrix_difference.get(
            ("aggregate_kernels", f"{ell_label}.p1.all")
        )
        require(lane_difference is not None, f"aggregate comparison missing {ell_label}.p1.all")
        # Finding 6: the fourth E_conn term is transported through S on both
        # resolutions, ||S R_384 S^dagger - S R_192 S^dagger||_2, matching
        # the sealed spec text exactly.
        independent_tail = operator_norm(
            overlap
            @ independent.arrays[
                f"diag_independent__{ell_label}__n384__p1__all"
            ]
            @ overlap.conjugate().T
            - overlap
            @ independent.arrays[
                f"diag_independent__{ell_label}__n192__p1__all"
            ]
            @ overlap.conjugate().T,
            f"independent_tail.{ell_label}.p1.all",
        )
        error = max(
            primary_tail,
            quadrature_difference,
            lane_difference,
            independent_tail,
        )
        require(
            signal > CONNECTION_SIGNAL_FACTOR * error,
            f"connection sensitivity failed {ell_label}: {signal} <= "
            f"{CONNECTION_SIGNAL_FACTOR}*{error}",
        )
        sensitivity_rows.append(
            {
                "ell": ell_label,
                "signal": signal,
                "error": error,
                "signal_to_error": signal / error if error > 0.0 else None,
                "required_factor": CONNECTION_SIGNAL_FACTOR,
                "pinned_history_pair": ["a1", "a2"],
                "pinned_history_values": [0.07, -0.11],
                "passed": True,
            }
        )
    return {
        "primary_local_gate_maxima": primary_values,
        "independent_local_gate_maxima": independent_values,
        "primary_convergence": convergence_rows,
        "independent_tails": tail_rows,
        "connection_sensitivity": sensitivity_rows,
    }


def validate_current_route2_route1_reduction(
    primary: Bundle,
    independent: Bundle,
) -> dict[str, Any]:
    ready_expected = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
    other_expected = np.array([1.0, -1.0], dtype=complex) / np.sqrt(2.0)
    projectors_expected = {
        "completed": np.outer(ready_expected, ready_expected.conjugate()),
        "other": np.outer(other_expected, other_expected.conjugate()),
    }
    history_values = (0.07, -0.11, 0.13, 0.04)
    pairs = ((0.07, -0.11), (0.13, 0.04))
    rows: list[dict[str, Any]] = []
    for bundle in (primary, independent):
        report = bundle.payload.get(
            "route1_current_route2_architecture_reduction"
        )
        require(isinstance(report, dict), f"{bundle.lane} current Route-1 report absent")
        require(report.get("passed") is True, f"{bundle.lane} current Route-1 report failed")
        require(
            report.get("actual_parent_route1_line_restriction_derived") is False,
            f"{bundle.lane} current Route-1 report overclaims a parent line restriction",
        )
        require(
            bundle.payload.get(
                "route1_current_route2_architecture_reduction_passed"
            )
            is True,
            f"{bundle.lane} current Route-1 pass flag is absent",
        )
        require(
            bundle.payload.get("actual_parent_route1_line_restriction_derived")
            is False,
            f"{bundle.lane} improperly claims an actual-parent Route-1 line",
        )
        ready = bundle.arrays.get("diag_route1_ready")
        require(ready is not None and ready.shape == (2,), f"{bundle.lane} Route-1 ready state")
        ready_error = float(np.linalg.norm(ready - ready_expected))
        require(ready_error <= SCALAR_TOLERANCE, f"{bundle.lane} Route-1 ready changed")
        for label, expected in projectors_expected.items():
            key = f"diag_route1_projector__{label}"
            require(key in bundle.arrays, f"{bundle.lane} missing {key}")
            error = operator_norm(
                bundle.arrays[key] - expected,
                f"{bundle.lane} {key}",
            )
            require(error <= PROJECTOR_TOLERANCE, f"{bundle.lane} {key} changed")
        unitaries: dict[float, np.ndarray] = {}
        for history_index, theta in enumerate(history_values, start=1):
            key = f"diag_route1_unitary__a{history_index}"
            require(key in bundle.arrays, f"{bundle.lane} missing {key}")
            expected = np.diag([1.0, np.exp(1j * theta)]).astype(complex)
            error = operator_norm(
                bundle.arrays[key] - expected,
                f"{bundle.lane} {key}",
            )
            require(error <= SCALAR_TOLERANCE, f"{bundle.lane} {key} changed")
            unitaries[theta] = bundle.arrays[key]

        lane_maximum = 0.0
        for route_index, (plus, minus) in enumerate(pairs):
            plus_amplitudes = np.array(
                [
                    vector.conjugate() @ unitaries[plus] @ ready
                    for vector in (ready_expected, other_expected)
                ],
                dtype=complex,
            )
            minus_amplitudes = np.array(
                [
                    vector.conjugate() @ unitaries[minus] @ ready
                    for vector in (ready_expected, other_expected)
                ],
                dtype=complex,
            )
            recomputed = {
                "completed":
                    np.conjugate(minus_amplitudes[0]) * plus_amplitudes[0],
                "all": np.vdot(minus_amplitudes, plus_amplitudes),
            }
            analytic = {
                "completed":
                    np.conjugate((1.0 + np.exp(1j * minus)) / 2.0)
                    * ((1.0 + np.exp(1j * plus)) / 2.0),
                "all": (1.0 + np.exp(1j * (plus - minus))) / 2.0,
            }
            for component in ("completed", "all"):
                key = f"diag_route1_current__r{route_index}__{component}"
                require(key in bundle.arrays, f"{bundle.lane} missing {key}")
                supplied = bundle.arrays[key]
                require(
                    supplied.shape == (1, 1),
                    f"{bundle.lane} malformed {key}",
                )
                recomputation_error = float(abs(supplied[0, 0] - recomputed[component]))
                analytic_error = float(abs(recomputed[component] - analytic[component]))
                lane_maximum = max(
                    lane_maximum,
                    recomputation_error,
                    analytic_error,
                )
                require(
                    recomputation_error <= SCALAR_TOLERANCE,
                    f"{bundle.lane} current Route-1 {component} is not reproducible",
                )
                require(
                    analytic_error <= 1.0e-10,
                    f"{bundle.lane} current Route-1 {component} failed O6",
                )
                rows.append(
                    {
                        "lane": bundle.lane,
                        "route_pair": route_index,
                        "component": component,
                        "recomputation_error": recomputation_error,
                        "analytic_error": analytic_error,
                        "passed": True,
                    }
                )
        require(
            lane_maximum <= 1.0e-10,
            f"{bundle.lane} current Route-1 architecture reduction failed",
        )

    for route_index in range(2):
        for component in ("completed", "all"):
            key = f"diag_route1_current__r{route_index}__{component}"
            difference = float(
                abs(primary.arrays[key][0, 0] - independent.arrays[key][0, 0])
            )
            require(
                difference <= SCALAR_TOLERANCE,
                f"Route-1 cross-lane mismatch: {key}",
            )
    historical = primary.payload.get("route1_isolated_reexecution")
    require(isinstance(historical, dict), "historical Route-1 rerun report absent")
    require(historical.get("passed") is True, "historical Route-1 rerun failed")
    require(
        float(historical.get("maximum_completed_component_error", 1.0)) <= 1.0e-10,
        "historical Route-1 completed component failed",
    )
    require(
        float(historical.get("maximum_exhaustive_kernel_error", 1.0)) <= 1.0e-10,
        "historical Route-1 exhaustive kernel failed",
    )
    return {
        "current_route2_architecture_reduces_to_O6": True,
        "historical_route1_isolated_reexecution_passed": True,
        "actual_parent_route1_line_restriction_derived": False,
        "rows": rows,
    }


def compare_loaded_bundles(primary: Bundle, independent: Bundle) -> dict[str, Any]:
    validate_basis_and_diagnostic_provenance(primary)
    validate_basis_and_diagnostic_provenance(independent)
    validate_generator_pieces(primary)
    validate_generator_pieces(independent)
    require(
        exact_json_equal(
            primary.manifest["dimensions"],
            independent.manifest["dimensions"],
        ),
        "carrier dimensions differ",
    )
    require(
        exact_json_equal(
            primary.manifest["discrete_labels"],
            independent.manifest["discrete_labels"],
        ),
        "discrete labels differ",
    )
    source_dimension = primary.manifest["dimensions"]["source_dimension"]
    overlap_key = independent.manifest["basis_overlap_key"]
    overlap = independent.arrays[overlap_key]
    require(
        overlap.shape == (source_dimension, source_dimension),
        "basis-overlap shape mismatch",
    )
    basis_residual = operator_norm(
        overlap.conjugate().T @ overlap - np.eye(source_dimension, dtype=complex),
        "basis-overlap unitarity",
    )
    basis_row = comparison_row(
        "basis_overlap",
        "unitarity",
        basis_residual,
        BASIS_UNITARITY_TOLERANCE,
    )

    rows = [basis_row]
    rows.extend(compare_scalar_categories(primary, independent))
    rows.extend(compare_matrix_categories(primary, independent, overlap))
    failures = [row for row in rows if not row["passed"]]
    require(not failures, f"{len(failures)} component comparison(s) failed")
    diagnostic_gates = validate_lane_diagnostics(
        primary, independent, rows, overlap
    )
    # Lineage gate (R2/R3): the primary lane stores its propagators in the
    # sealed tensor convention; the independent lane's are transported through
    # the pinned basis overlap before comparison.
    lineage_gate = {
        "primary": validate_generator_propagator_lineage(primary, None),
        "independent": validate_generator_propagator_lineage(
            independent, overlap
        ),
    }
    route1_gate = validate_current_route2_route1_reduction(primary, independent)
    return {
        "schema": RESULT_SCHEMA,
        "phase": "A",
        "overall_verdict": PASS_VERDICT,
        "comparison_complete": True,
        "comparison_passed": True,
        "spec_sha256": SPEC_SHA256,
        "input_hashes": {
            "independent_json": independent.json_sha256,
            "independent_npz": independent.npz_sha256,
            "primary_json": primary.json_sha256,
            "primary_npz": primary.npz_sha256,
        },
        "thresholds": {
            "scalar_absolute": SCALAR_TOLERANCE,
            "record_projector_operator_2_norm": PROJECTOR_TOLERANCE,
            "basis_overlap_unitarity_operator_2_norm": BASIS_UNITARITY_TOLERANCE,
            "transported_matrix_operator_2_norm": TRANSPORTED_MATRIX_TOLERANCE,
            "primary_lineage_operator_2_norm": LINEAGE_BUDGETS["primary"],
            "independent_lineage_operator_2_norm":
                LINEAGE_BUDGETS["independent"],
        },
        "exact_gates": {
            "dimensions_equal": True,
            "discrete_labels_equal": True,
            "component_identifier_sets_equal": True,
        },
        "component_comparisons": rows,
        "component_count": len(rows),
        "component_failure_count": 0,
        "diagnostic_gates": diagnostic_gates,
        "generator_propagator_lineage": lineage_gate,
        "route1_consistency_falsifier": route1_gate,
        # Finding 7: comparator-level support flags only.  The A7-level
        # protected flag names (actual_parent_regulated_CAR_operator_response_
        # derived, actual_parent_same_carrier_one_source_restriction_derived)
        # never appear as true in comparator output; verdict authority rests
        # with the sealed evaluator.
        "comparison_supports_actual_parent_regulated_CAR_operator_response": True,
        "comparison_supports_actual_parent_same_carrier_one_source_restriction": True,
        "one_particle_sector_CAR_representation_verified": True,
        "numerical_verification_scope":
            "one_particle_sector_CAR_representation_not_full_Fock_operator_norm",
        "full_Fock_operator_norm_bound_derived": False,
        "continuum_limit_derived": False,
        "regulator_independence_derived": False,
        "physical_connection_normalization_derived": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "ER_fork_closed": False,
        "route1_current_route2_architecture_reduction_passed": True,
        "actual_parent_route1_line_restriction_derived": False,
        "actual_finite_parent_state_evaluation_derived": False,
        "actual_finite_parent_operator_to_scalar_bridge_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }


def compare_bundles(
    *,
    independent_json: Path,
    independent_npz: Path,
    primary_json: Path,
    primary_npz: Path,
    independent_json_sha256: str,
    independent_npz_sha256: str,
    primary_json_sha256: str,
    primary_npz_sha256: str,
    output: Path,
    controller_context: str | None = None,
) -> dict[str, Any]:
    inputs = (independent_json, independent_npz, primary_json, primary_npz)
    resolved_output = output.resolve()
    resolved_inputs = tuple(path.resolve() for path in inputs)
    # Finding 8: the sealed result records the resolved absolute input and
    # output paths plus the caller-declared controller context so the
    # controller (and any evaluator) can cross-check them against the
    # canonical workspace paths.
    provenance_paths = {
        "resolved_input_paths": {
            "independent_json": str(resolved_inputs[0]),
            "independent_npz": str(resolved_inputs[1]),
            "primary_json": str(resolved_inputs[2]),
            "primary_npz": str(resolved_inputs[3]),
        },
        "resolved_output_path": str(resolved_output),
        "controller_context": controller_context,
    }
    require(
        all(resolved_output != path for path in resolved_inputs),
        "output path aliases an input bundle",
    )
    require(not output.exists(), f"immutable comparison output already exists: {output}")
    require(
        not Path(f"{output}.seal.sha256").exists(),
        f"immutable comparison-output seal already exists: {output}",
    )
    try:
        runtime_attestation = require_runtime_attestation()
        implementation_manifest_sha256, implementation_rows = (
            verify_implementation_manifest()
        )
        require(
            len(set(resolved_inputs)) == len(resolved_inputs),
            "independent and primary bundle paths must be pairwise distinct",
        )
        require(sha256(SPEC) == SPEC_SHA256, "sealed specification drift")
        require(all(path.exists() for path in inputs), "both complete bundles must exist")

        independent = load_bundle(
            "independent",
            independent_json,
            independent_npz,
            independent_json_sha256,
            independent_npz_sha256,
        )
        primary = load_bundle(
            "primary",
            primary_json,
            primary_npz,
            primary_json_sha256,
            primary_npz_sha256,
        )
        for bundle in (independent, primary):
            executor_path = EXECUTOR_PATHS[bundle.lane]
            # Verification finding (condition 3): the manifest rows for the
            # lane executor and the runtime launcher must exist as non-empty
            # strings BEFORE any equality check, so an absent row can never
            # satisfy a vacuous None == None comparison.
            executor_row = implementation_rows.get(executor_path)
            launcher_row = implementation_rows.get(RUNTIME_LAUNCHER_PATH)
            require(
                isinstance(executor_row, str) and bool(executor_row),
                f"{bundle.lane} executor manifest row is absent",
            )
            require(
                isinstance(launcher_row, str) and bool(launcher_row),
                f"{bundle.lane} runtime-launcher manifest row is absent",
            )
            require(
                bundle.payload.get("implementation_manifest_sha256")
                == implementation_manifest_sha256,
                f"{bundle.lane} implementation-manifest binding mismatch",
            )
            require(
                bundle.payload.get("executor_sha256") == executor_row,
                f"{bundle.lane} executor provenance mismatch",
            )
            require(
                bundle.payload["runtime_attestation"].get("launcher_sha256")
                == launcher_row,
                f"{bundle.lane} runtime-launcher provenance mismatch",
            )
            # Repair binding R1 item 4 (finding 2): the launcher hashes its
            # resolved target and embeds target_sha256 in the attestation;
            # the lane binds it into its bundle; this comparator checks the
            # recorded value against the manifest row for that lane's
            # executor.
            require(
                bundle.payload["runtime_attestation"].get("target_sha256")
                == executor_row,
                f"{bundle.lane} runtime-attestation target-hash binding mismatch",
            )
        result = compare_loaded_bundles(primary, independent)
        result["implementation_manifest_sha256"] = implementation_manifest_sha256
        result["runtime_attestation"] = runtime_attestation
        result.update(provenance_paths)

        # Finding 1: the v001 post-hoc re-hash is removed; every consumed
        # byte was hashed as the single read buffer it was parsed from, so
        # there is no swap-and-restore window to detect.
        atomic_write_sealed_json(output, result)
        return result
    except Exception as error:
        reason = str(error)
        blocked = blocked_payload(
            reason,
            details={"exception_type": type(error).__name__},
        )
        blocked.update(provenance_paths)
        atomic_write_sealed_json(output, blocked)
        return blocked


def parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument("--independent-json", type=Path, required=True)
    argument_parser.add_argument("--independent-npz", type=Path, required=True)
    argument_parser.add_argument("--primary-json", type=Path, required=True)
    argument_parser.add_argument("--primary-npz", type=Path, required=True)
    argument_parser.add_argument("--independent-json-sha256", required=True)
    argument_parser.add_argument("--independent-npz-sha256", required=True)
    argument_parser.add_argument("--primary-json-sha256", required=True)
    argument_parser.add_argument("--primary-npz-sha256", required=True)
    argument_parser.add_argument("--output", type=Path, required=True)
    # Finding 8: the controller declares its context here; a standalone run
    # records null, which the controller cross-check rejects.
    argument_parser.add_argument("--controller-context", default=None)
    return argument_parser


def main() -> int:
    # A launcher failure is outside the comparison lane and must not consume
    # the immutable result path.
    require_runtime_attestation()
    arguments = parser().parse_args()
    result = compare_bundles(
        independent_json=arguments.independent_json,
        independent_npz=arguments.independent_npz,
        primary_json=arguments.primary_json,
        primary_npz=arguments.primary_npz,
        independent_json_sha256=arguments.independent_json_sha256,
        independent_npz_sha256=arguments.independent_npz_sha256,
        primary_json_sha256=arguments.primary_json_sha256,
        primary_npz_sha256=arguments.primary_npz_sha256,
        output=arguments.output,
        controller_context=arguments.controller_context,
    )
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 0 if result["overall_verdict"] == PASS_VERDICT else 1


if __name__ == "__main__":
    raise SystemExit(main())
