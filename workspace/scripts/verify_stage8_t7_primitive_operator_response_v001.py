#!/usr/bin/env python3
"""Independently verify the sealed primitive operator-response execution."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
SELF_SEAL = Path(f"{SELF}.seal.sha256")
SPEC = ROOT / "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md"
SPEC_SEAL = Path(f"{SPEC}.seal.sha256")
EXACT_DERIVATION = (
    ROOT / "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md"
)
EXACT_DERIVATION_SEAL = Path(f"{EXACT_DERIVATION}.seal.sha256")
AUTHORITY_AMENDMENT = (
    ROOT
    / "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md"
)
AUTHORITY_AMENDMENT_SEAL = Path(f"{AUTHORITY_AMENDMENT}.seal.sha256")
RUNTIME_MANIFEST = (
    ROOT / "provenance/stage8_t7_numpy_runtime_manifest_v001.json"
)
RUNTIME_MANIFEST_SEAL = Path(f"{RUNTIME_MANIFEST}.seal.sha256")
PRIMARY = ROOT / "scripts/derive_stage8_t7_primitive_operator_response_v001.py"
PRIMARY_SEAL = Path(f"{PRIMARY}.seal.sha256")
PRIMARY_RESULT = (
    ROOT / "stage8_execution/work/T07_primitive_operator_response_v001.json"
)
PRIMARY_RESULT_SEAL = Path(f"{PRIMARY_RESULT}.seal.sha256")
OUT = (
    ROOT
    / "stage8_execution/work/"
    "T07_primitive_operator_response_verification_v001.json"
)

SPEC_SHA256 = "2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde"
EXACT_DERIVATION_SHA256 = (
    "a9875788301d8434113f77e3b5726b49d70d8609fbcfcc72c9fede76a1249e4a"
)
AUTHORITY_AMENDMENT_SHA256 = (
    "1d26607ad490c2ee02ee42171cedd9e3f24cecf7e37d49fb8c91fac20b6aca39"
)
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PRIMARY_SHA256 = (
    "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c"
)
TOLERANCE = 1.0e-10
DERIVATIVE_TOLERANCE = 2.0e-5
SITE_COUNT = 3
SPIN_DIMENSION = 4
SOURCE_DIMENSION = 12
RECORD_COUNT = 2
RECORD_DIMENSION = 3
FINAL_RECORD_DIMENSION = 9
STEPS = 96
ACTION = math.pi / math.sqrt(2.0)
EPSILONS = (2.0**-8, 2.0**-9, 2.0**-10)
HISTORY_PAIRS = ((0.0, 0.0), (0.07, -0.11), (0.13, 0.04))
COMPLETED_INDEX = 4


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def atomic_write(payload: dict[str, object]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(OUT)


def verify_seal(path: Path, seal: Path, expected: str | None = None) -> str:
    require(path.is_file(), f"missing artifact: {path}")
    require(seal.is_file(), f"missing seal: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {seal}")
    recorded, recorded_path = fields
    allowed_paths = {path.name, str(path.relative_to(ROOT))}
    require(recorded_path in allowed_paths, f"seal path mismatch: {seal}")
    actual = sha256(path)
    require(actual == recorded, f"seal hash mismatch: {path}")
    if expected is not None:
        require(actual == expected, f"expected hash mismatch: {path}")
    return actual


def validate_runtime_manifest() -> dict[str, object]:
    verify_seal(
        RUNTIME_MANIFEST,
        RUNTIME_MANIFEST_SEAL,
        RUNTIME_MANIFEST_SHA256,
    )
    payload = json.loads(RUNTIME_MANIFEST.read_text(encoding="utf-8"))
    require(
        payload.get("schema") == "stage8_t7_numpy_runtime_manifest_v001",
        "runtime-manifest schema mismatch",
    )
    executable = Path(str(payload.get("python_executable"))).resolve()
    require(
        executable == Path(sys.executable).resolve(),
        "runtime-manifest executable mismatch",
    )
    require(
        sha256(executable) == payload.get("python_executable_sha256"),
        "runtime-manifest executable hash mismatch",
    )
    root = Path(str(payload.get("site_packages"))).resolve()
    rows = payload.get("files")
    require(isinstance(rows, list) and bool(rows), "empty runtime manifest")
    require(payload.get("file_count") == len(rows), "runtime file-count mismatch")
    table = {}
    for row in rows:
        require(isinstance(row, dict), "malformed runtime row")
        relative = str(row.get("path"))
        require(relative not in table, f"duplicate runtime path: {relative}")
        candidate = (root / relative).resolve()
        require(root in candidate.parents, f"runtime path escape: {relative}")
        require(candidate.is_file(), f"missing runtime file: {relative}")
        actual = sha256(candidate)
        require(actual == row.get("sha256"), f"runtime drift: {relative}")
        table[relative] = actual
    payload["_verified_table"] = table
    return payload


def import_verified_numpy(manifest: dict[str, object]):
    root = Path(str(manifest["site_packages"])).resolve()
    sys.path.append(str(root))
    import numpy as np

    audit_runtime_modules(manifest)
    return np


def audit_runtime_modules(manifest: dict[str, object]) -> dict[str, object]:
    root = Path(str(manifest["site_packages"])).resolve()
    table = manifest["_verified_table"]
    observed = {}
    for name, module in sorted(sys.modules.items()):
        raw_origin = getattr(module, "__file__", None)
        if raw_origin is None:
            continue
        origin = Path(raw_origin).resolve()
        if root not in origin.parents:
            continue
        relative = str(origin.relative_to(root))
        require(relative in table, f"unlisted runtime module: {name}")
        actual = sha256(origin)
        require(actual == table[relative], f"runtime module drift: {name}")
        observed[name] = {"path": relative, "sha256": actual}
    require("numpy" in observed, "NumPy missing from runtime audit")
    return {
        "loaded_site_package_module_count": len(observed),
        "loaded_site_package_modules": observed,
    }


def pauli_and_dirac():
    import numpy as np

    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[eye, zero], [zero, -eye]])
    gamma = [
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    ]
    gamma5 = 1j * gamma0 @ gamma[0] @ gamma[1] @ gamma[2]
    return gamma0 @ gamma[0], -1j * gamma0 @ gamma5


def derivative_matrix(theta: float):
    import numpy as np

    value = np.zeros((3, 3), dtype=complex)
    forward = np.exp(1j * theta / 3.0)
    backward = forward.conjugate()
    for row in range(3):
        value[row, (row + 1) % 3] = 0.5 * forward
        value[row, (row - 1) % 3] = -0.5 * backward
    return value


def record_embedding(local, position: int):
    import numpy as np

    factors = [
        local if index == position else np.eye(3, dtype=complex)
        for index in range(2)
    ]
    return np.kron(factors[0], factors[1])


def cell_weight(time: float) -> float:
    return 32.0 * min(time, 1.0 - time) ** 3


def spectral_step(hamiltonian, interval: float):
    import numpy as np

    values, vectors = np.linalg.eigh(hamiltonian)
    return (
        vectors * np.exp(-1j * interval * values)
    ) @ vectors.conjugate().T


def build_generators(theta: float):
    import numpy as np

    alpha_x, incidence_spin = pauli_and_dirac()
    source = np.kron(-1j * derivative_matrix(theta), alpha_x)
    free = np.kron(source, np.eye(9, dtype=complex))
    c_partial = np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )
    masks = (
        np.diag([1.0, 1.0, 0.0]),
        np.diag([0.0, 1.0, 1.0]),
    )
    interactions = []
    for index, mask in enumerate(masks):
        interactions.append(
            np.kron(
                np.kron(mask.astype(complex), incidence_spin),
                record_embedding(c_partial, index),
            )
        )
    return free, tuple(interactions)


def initial_isometry():
    import numpy as np

    value = np.zeros((108, 12), dtype=complex)
    value[::9, :] = np.eye(12, dtype=complex)
    return value


def evolve_from_generators(free, interactions, injection):
    dt = 1.0 / STEPS
    state = injection.copy()
    for interaction in interactions:
        for step in range(STEPS):
            time = (step + 0.5) * dt
            hamiltonian = free + ACTION * cell_weight(time) * interaction
            state = spectral_step(hamiltonian, dt) @ state
    return state


def evolve(theta: float):
    free, interactions = build_generators(theta)
    return evolve_from_generators(
        free,
        interactions,
        initial_isometry(),
    )


def components(stinespring):
    import numpy as np

    values = []
    for record_index in range(FINAL_RECORD_DIMENSION):
        block = np.zeros(
            (SOURCE_DIMENSION, SOURCE_DIMENSION),
            dtype=complex,
        )
        for source_out in range(SOURCE_DIMENSION):
            flat_row = (
                source_out * FINAL_RECORD_DIMENSION + record_index
            )
            for source_in in range(SOURCE_DIMENSION):
                block[source_out, source_in] = stinespring[
                    flat_row,
                    source_in,
                ]
        values.append(block)
    return tuple(values)


def compressed_response(left, right, source_dimension: int, record_projection):
    import numpy as np

    return (
        left.conjugate().T
        @ np.kron(
            np.eye(source_dimension, dtype=complex),
            record_projection,
        )
        @ right
    )


def response(left, right, completed: bool):
    import numpy as np

    projection = np.eye(FINAL_RECORD_DIMENSION, dtype=complex)
    if completed:
        projection = np.zeros(
            (FINAL_RECORD_DIMENSION, FINAL_RECORD_DIMENSION),
            dtype=complex,
        )
        projection[COMPLETED_INDEX, COMPLETED_INDEX] = 1.0
    return compressed_response(
        left,
        right,
        SOURCE_DIMENSION,
        projection,
    )


def kraus_response(left, right, completed: bool):
    import numpy as np

    left_components = components(left)
    right_components = components(right)
    indices = (COMPLETED_INDEX,) if completed else range(9)
    total = np.zeros((12, 12), dtype=complex)
    for index in indices:
        total += (
            left_components[index].conjugate().T
            @ right_components[index]
        )
    return total


def norm(operator) -> float:
    import numpy as np

    return float(np.linalg.norm(operator, ord=2))


def matrix_from_json(rows):
    import numpy as np

    return np.array(
        [
            [complex(value[0], value[1]) for value in row]
            for row in rows
        ],
        dtype=complex,
    )


def structural_reconstruction(cache: dict[float, object]) -> dict[str, object]:
    import numpy as np

    identity = np.eye(12, dtype=complex)
    direct_kraus_errors = []
    adjoint_errors = []
    diagonal_errors = []
    hermiticity_errors = []
    bound_violations = []
    for plus_theta, minus_theta in HISTORY_PAIRS:
        plus = cache[plus_theta]
        minus = cache[minus_theta]
        for completed in (False, True):
            direct = response(minus, plus, completed)
            via_kraus = kraus_response(minus, plus, completed)
            reverse = response(plus, minus, completed)
            direct_kraus_errors.append(norm(direct - via_kraus))
            adjoint_errors.append(norm(direct.conjugate().T - reverse))
            bound_violations.append(max(0.0, norm(direct) - 1.0))
    for theta, value in cache.items():
        full = response(value, value, False)
        completed = response(value, value, True)
        diagonal_errors.append(norm(full - identity))
        hermiticity_errors.append(
            norm(completed - completed.conjugate().T)
        )
        eigenvalues = np.linalg.eigvalsh(
            0.5 * (completed + completed.conjugate().T)
        )
        bound_violations.extend(
            (
                max(0.0, float(-eigenvalues.min())),
                max(0.0, float(eigenvalues.max() - 1.0)),
            )
        )
    maximum = {
        "direct_kraus": max(direct_kraus_errors),
        "adjoint": max(adjoint_errors),
        "diagonal": max(diagonal_errors),
        "completed_hermiticity": max(hermiticity_errors),
        "bounds": max(bound_violations),
    }
    return {
        "maximum_errors": maximum,
        "pass": all(value <= TOLERANCE for value in maximum.values()),
    }


def central_derivatives(
    cache: dict[float, object],
    branch: str,
    completed: bool,
):
    derivatives = []
    for epsilon in EPSILONS:
        if branch == "plus":
            positive = response(cache[0.0], cache[epsilon], completed)
            negative = response(cache[0.0], cache[-epsilon], completed)
        else:
            positive = response(cache[epsilon], cache[0.0], completed)
            negative = response(cache[-epsilon], cache[0.0], completed)
        derivatives.append((positive - negative) / (2.0 * epsilon))
    return derivatives


def derivative_crosscheck(cache, primary):
    rows = {}
    passed = True
    stored = primary["finite_operator_Duhamel_regression"][
        "analytic_derivatives"
    ]
    for branch in ("plus", "minus"):
        for label, completed in (("all", False), ("completed", True)):
            key = f"{branch}_{label}"
            independent = central_derivatives(
                cache, branch, completed
            )
            primary_matrix = matrix_from_json(stored[key])
            denominator = norm(primary_matrix)
            require(denominator > 0.0, f"zero primary derivative: {key}")
            relative_errors = [
                norm(derivative - primary_matrix) / denominator
                for derivative in independent
            ]
            decreasing = all(
                relative_errors[index + 1] < relative_errors[index]
                for index in range(len(relative_errors) - 1)
            )
            reduction_factors = [
                relative_errors[index] / relative_errors[index + 1]
                for index in range(len(relative_errors) - 1)
            ]
            row_pass = bool(
                relative_errors[-1] <= DERIVATIVE_TOLERANCE
                and decreasing
                and all(factor >= 2.0 for factor in reduction_factors)
            )
            rows[key] = {
                "epsilons": list(EPSILONS),
                "relative_errors_against_primary_Duhamel": relative_errors,
                "reduction_factors": reduction_factors,
                "strictly_decreasing": decreasing,
                "pass": row_pass,
            }
            passed = passed and row_pass
    return {"rows": rows, "pass": passed}


def passive_covariance(cache):
    import numpy as np

    site = np.diag(
        [1.0, np.exp(1j * math.pi / 7.0), np.exp(-1j * math.pi / 5.0)]
    )
    source = np.kron(site, np.eye(4, dtype=complex))
    full = np.kron(source, np.eye(9, dtype=complex))
    left = cache[-0.11]
    right = cache[0.07]
    changed_injection = (
        full @ initial_isometry() @ source.conjugate().T
    )
    changed = {}
    stinespring_errors = []
    for theta in (-0.11, 0.07):
        free, interactions = build_generators(theta)
        changed_free = full @ free @ full.conjugate().T
        changed_interactions = tuple(
            full @ interaction @ full.conjugate().T
            for interaction in interactions
        )
        changed[theta] = evolve_from_generators(
            changed_free,
            changed_interactions,
            changed_injection,
        )
        expected = full @ cache[theta] @ source.conjugate().T
        stinespring_errors.append(norm(changed[theta] - expected))
    left_changed = changed[-0.11]
    right_changed = changed[0.07]
    errors = []
    for completed in (False, True):
        original = response(left, right, completed)
        changed = response(left_changed, right_changed, completed)
        errors.append(norm(changed - source @ original @ source.conjugate().T))
    maximum = max((*errors, *stinespring_errors))
    return {
        "kernel_errors": errors,
        "stinespring_reconstruction_errors": stinespring_errors,
        "maximum_error": maximum,
        "pass": maximum <= TOLERANCE,
    }


def route1_control():
    import numpy as np

    plus_state = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    minus_state = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2.0)
    completed_projection = np.outer(
        plus_state,
        plus_state.conjugate(),
    )
    all_projection = (
        completed_projection
        + np.outer(minus_state, minus_state.conjugate())
    )
    completed_errors = []
    all_errors = []
    for theta_plus, theta_minus in ((0.07, -0.11), (0.13, 0.04)):
        def stinespring(theta: float):
            unitary = np.diag([1.0, np.exp(1j * theta)])
            return (unitary @ plus_state).reshape(2, 1)

        right = stinespring(theta_plus)
        left = stinespring(theta_minus)
        completed = complex(
            compressed_response(
                left,
                right,
                1,
                completed_projection,
            )[0, 0]
        )
        full = complex(
            compressed_response(
                left,
                right,
                1,
                all_projection,
            )[0, 0]
        )
        expected_completed = (
            0.5 * (1.0 + np.exp(-1j * theta_minus))
            * 0.5 * (1.0 + np.exp(1j * theta_plus))
        )
        expected_all = 0.5 * (
            1.0 + np.exp(1j * (theta_plus - theta_minus))
        )
        completed_errors.append(abs(completed - expected_completed))
        all_errors.append(abs(full - expected_all))
    maximum_completed = max(completed_errors)
    maximum_all = max(all_errors)
    return {
        "maximum_completed_component_error": maximum_completed,
        "maximum_all_kernel_error": maximum_all,
        "pass": max(maximum_completed, maximum_all) <= TOLERANCE,
    }


def run() -> dict[str, object]:
    require(sys.flags.isolated == 1, "verifier requires isolated Python (-I)")
    require(sys.flags.no_site == 1, "verifier requires no-site Python (-S)")
    require("sitecustomize" not in sys.modules, "sitecustomize was loaded")
    require("usercustomize" not in sys.modules, "usercustomize was loaded")
    spec_hash = verify_seal(SPEC, SPEC_SEAL, SPEC_SHA256)
    exact_derivation_hash = verify_seal(
        EXACT_DERIVATION,
        EXACT_DERIVATION_SEAL,
        EXACT_DERIVATION_SHA256,
    )
    authority_amendment_hash = verify_seal(
        AUTHORITY_AMENDMENT,
        AUTHORITY_AMENDMENT_SEAL,
        AUTHORITY_AMENDMENT_SHA256,
    )
    runtime_manifest = validate_runtime_manifest()
    self_hash = verify_seal(SELF, SELF_SEAL)
    primary_hash = verify_seal(PRIMARY, PRIMARY_SEAL, PRIMARY_SHA256)
    primary_result_hash = verify_seal(
        PRIMARY_RESULT,
        PRIMARY_RESULT_SEAL,
    )
    primary_bytes = PRIMARY_RESULT.read_bytes()
    require(
        hashlib.sha256(primary_bytes).hexdigest() == primary_result_hash,
        "primary result changed after seal verification",
    )
    primary = json.loads(primary_bytes.decode("utf-8"))
    require(
        primary.get("schema")
        == "stage8_t7_primitive_operator_response_v001",
        "primary schema mismatch",
    )
    require(
        primary.get("overall_verdict")
        == "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED",
        "primary gate did not derive the finite response bundle",
    )
    require(
        primary.get("alpha_computed") is False
        and primary.get("coupling_evaluation_authorized") is False,
        "protected primary status changed",
    )
    require(
        primary.get("proof_authorized") is False
        and primary.get("primitive_source_scalarization_derived") is False
        and primary.get("stage8_route2_architecture_amended") is False,
        "protected primary derivation status changed",
    )
    primary_authority = primary.get("authority_verification", {})
    require(
        primary_authority.get("spec_sha256") == SPEC_SHA256,
        "primary spec binding mismatch",
    )
    require(
        primary_authority.get("exact_derivation_sha256")
        == EXACT_DERIVATION_SHA256,
        "primary exact-derivation binding mismatch",
    )
    require(
        primary_authority.get("authority_amendment_sha256")
        == AUTHORITY_AMENDMENT_SHA256,
        "primary authority-amendment binding mismatch",
    )
    require(
        primary_authority.get("runtime_manifest_sha256")
        == RUNTIME_MANIFEST_SHA256,
        "primary runtime-manifest binding mismatch",
    )
    require(
        primary_authority.get("self_sha256") == primary_hash,
        "primary self binding mismatch",
    )
    frozen = primary.get("frozen_regression", {})
    expected_frozen = {
        "site_count": SITE_COUNT,
        "spin_dimension": SPIN_DIMENSION,
        "record_count": RECORD_COUNT,
        "record_dimension": RECORD_DIMENSION,
        "midpoint_steps_per_pulse": STEPS,
        "write_action": "pi/sqrt(2)",
        "history_pairs": [list(pair) for pair in HISTORY_PAIRS],
        "duhamel_epsilons": list(EPSILONS),
        "completed_outcome": [1, 1],
        "arithmetic": "IEEE-754 binary64 / numpy complex128",
        "structural_tolerance": TOLERANCE,
        "duhamel_finest_tolerance": DERIVATIVE_TOLERANCE,
    }
    require(frozen == expected_frozen, "primary frozen-regression mismatch")

    np = import_verified_numpy(runtime_manifest)

    numpy_origin = Path(np.__file__).resolve()
    approved_runtime = Path(
        "/Users/bgm/.cache/codex-runtimes/"
        "codex-primary-runtime/dependencies/python"
    ).resolve()
    require(
        approved_runtime in numpy_origin.parents,
        f"NumPy loaded outside approved runtime: {numpy_origin}",
    )

    required = {value for pair in HISTORY_PAIRS for value in pair}
    required.update(EPSILONS)
    required.update(-value for value in EPSILONS)
    cache = {theta: evolve(theta) for theta in sorted(required)}

    structural = structural_reconstruction(cache)
    derivative = derivative_crosscheck(cache, primary)
    covariance = passive_covariance(cache)
    route1 = route1_control()

    completed = components(cache[0.0])[COMPLETED_INDEX]
    trace_scalar = np.trace(completed) / 12.0
    scalar_distance = float(
        np.linalg.norm(completed - trace_scalar * np.eye(12, dtype=complex))
    )
    witness = {
        "completed_11_frobenius_norm": float(np.linalg.norm(completed)),
        "completed_11_scalar_distance": scalar_distance,
        "non_scalar": scalar_distance > TOLERANCE,
        "matches_sealed_frobenius": abs(
            float(np.linalg.norm(completed)) - 2.158029616704532
        ) <= TOLERANCE,
        "matches_sealed_scalar_distance": abs(
            scalar_distance - 2.151758052952419
        ) <= TOLERANCE,
    }
    witness["pass"] = all(witness.values())
    terminal_runtime_audit = audit_runtime_modules(runtime_manifest)

    passed = bool(
        structural["pass"]
        and derivative["pass"]
        and covariance["pass"]
        and route1["pass"]
        and witness["pass"]
    )
    return {
        "schema": "stage8_t7_primitive_operator_response_verification_v001",
        "spec_sha256": spec_hash,
        "exact_derivation_sha256": exact_derivation_hash,
        "authority_amendment_sha256": authority_amendment_hash,
        "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
        "verifier_sha256": self_hash,
        "primary_script_sha256": primary_hash,
        "primary_result_sha256": primary_result_hash,
        "runtime": {
            "python_executable": sys.executable,
            "python_isolated": bool(sys.flags.isolated),
            "numpy_version": np.__version__,
            "numpy_origin": str(numpy_origin),
            "terminal_module_audit": terminal_runtime_audit,
        },
        "independent_structural_reconstruction": structural,
        "independent_derivative_crosscheck": derivative,
        "independent_passive_covariance": covariance,
        "independent_route1_special_case_control": route1,
        "independent_non_scalar_witness": witness,
        "overall_verdict": (
            "INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_CONFIRMED"
            if passed
            else "INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_BLOCKED"
        ),
        "finite_primitive_operator_response_bundle_derived": passed,
        "finite_primitive_operator_Duhamel_tangent_derived": passed,
        "primitive_source_scalarization_derived": False,
        "actual_parent_route1_line_restriction_derived": False,
        "finite_primitive_operator_gauge_covariance_derived": False,
        "finite_primitive_operator_graded_monoidality_derived": False,
        "stage8_route2_architecture_amended": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }


def main() -> None:
    atomic_write(
        {
            "schema":
                "stage8_t7_primitive_operator_response_verification_v001",
            "overall_verdict":
                "INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_BLOCKED_PENDING_RUN",
            "finite_primitive_operator_response_bundle_derived": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        }
    )
    try:
        result = run()
        atomic_write(result)
        print(json.dumps(result, indent=2, sort_keys=True))
        if result["overall_verdict"] != (
            "INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_CONFIRMED"
        ):
            raise SystemExit(1)
    except SystemExit:
        raise
    except Exception as error:
        blocked = {
            "schema": "stage8_t7_primitive_operator_response_verification_v001",
            "overall_verdict":
                "INDEPENDENT_PRIMITIVE_OPERATOR_RESPONSE_BLOCKED",
            "failure_type": type(error).__name__,
            "failure_message": str(error),
            "finite_primitive_operator_response_bundle_derived": False,
            "finite_primitive_operator_Duhamel_tangent_derived": False,
            "primitive_source_scalarization_derived": False,
            "actual_parent_route1_line_restriction_derived": False,
            "finite_primitive_operator_gauge_covariance_derived": False,
            "finite_primitive_operator_graded_monoidality_derived": False,
            "stage8_route2_architecture_amended": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
            "no_target_access_attestation": True,
        }
        atomic_write(blocked)
        print(json.dumps(blocked, indent=2, sort_keys=True))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
