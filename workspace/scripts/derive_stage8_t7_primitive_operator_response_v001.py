#!/usr/bin/env python3
"""Execute the sealed finite primitive operator-response gate."""

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
RUNTIME_BUILDER = (
    ROOT / "scripts/build_stage8_t7_numpy_runtime_manifest_v001.py"
)
OUT = ROOT / "stage8_execution/work/T07_primitive_operator_response_v001.json"

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
RUNTIME_BUILDER_SHA256 = (
    "293f16de83384b4f42c6ccb1c1c9b4ac44564d1c579edc68548a9d22e767b05c"
)

DIRECT_AUTHORITIES = {
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md":
        "345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md":
        "949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md":
        "e30f2e631204df2416b9aa38e55c2710db1d676749fcd2fbdb6604388f3ea391",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md":
        "e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6",
    "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_RESULT_V001.md":
        "94d035231df7908f9fdde62b1a6aae7d791fa74c8f32c1a95b2511d346fd54c2",
}

BUNDLE_AUTHORITIES = {
    "stage8_execution/t7_actual_parent_record_amplitude/"
    "T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256":
        "322510075e1f8f6616eb47b1325f47963d90e8adaf20e83f7209c8be5f048b40",
    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.seal.sha256":
        "199987876a3c7a6b9ed6bfda123256daddf0f5dd96cfdf929e3e155ddb32fc35",
}

STRUCTURAL_TOLERANCE = 1.0e-10
DUHAMEL_FINE_TOLERANCE = 2.0e-5
SITE_COUNT = 3
SPIN_DIMENSION = 4
RECORD_COUNT = 2
RECORD_DIMENSION = 3
SOURCE_DIMENSION = SITE_COUNT * SPIN_DIMENSION
FINAL_RECORD_DIMENSION = RECORD_DIMENSION**RECORD_COUNT
MIDPOINT_STEPS = 96
WRITE_ACTION = math.pi / math.sqrt(2.0)
HISTORY_PAIRS = ((0.0, 0.0), (0.07, -0.11), (0.13, 0.04))
DUHAMEL_EPSILONS = (2.0**-8, 2.0**-9, 2.0**-10)
COMPLETED_OUTCOME = (1, 1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(payload: dict[str, object]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUT.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(OUT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_single_seal(path: Path, seal: Path, expected: str | None = None) -> str:
    require(path.is_file(), f"missing sealed file: {path}")
    require(seal.is_file(), f"missing seal: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {seal}")
    recorded, recorded_path = fields
    require(recorded_path == path.name or recorded_path == str(path.relative_to(ROOT)),
            f"seal path mismatch: {seal}")
    actual = sha256(path)
    require(recorded == actual, f"seal hash mismatch: {path}")
    if expected is not None:
        require(actual == expected, f"expected hash mismatch: {path}")
    return actual


def verify_bundle(relative: str, expected_bundle_hash: str) -> list[dict[str, str]]:
    bundle = ROOT / relative
    require(sha256(bundle) == expected_bundle_hash, f"bundle drift: {relative}")
    rows: list[dict[str, str]] = []
    for line in bundle.read_text(encoding="ascii").splitlines():
        if not line.strip():
            continue
        fields = line.split(maxsplit=1)
        require(len(fields) == 2, f"malformed bundle row: {relative}")
        expected, child_relative = fields
        child = (ROOT / child_relative).resolve()
        require(ROOT.resolve() in child.parents or child == ROOT.resolve(),
                f"bundle path escapes root: {child_relative}")
        require(child.is_file(), f"missing bundled artifact: {child_relative}")
        actual = sha256(child)
        require(actual == expected, f"bundled artifact drift: {child_relative}")
        rows.append({"path": child_relative, "sha256": actual})
    require(rows, f"empty authority bundle: {relative}")
    return rows


def verify_runtime_manifest() -> dict[str, object]:
    verify_single_seal(
        RUNTIME_MANIFEST,
        RUNTIME_MANIFEST_SEAL,
        RUNTIME_MANIFEST_SHA256,
    )
    manifest = json.loads(RUNTIME_MANIFEST.read_text(encoding="utf-8"))
    require(
        manifest.get("schema") == "stage8_t7_numpy_runtime_manifest_v001",
        "runtime manifest schema mismatch",
    )
    python = Path(str(manifest.get("python_executable"))).resolve()
    require(
        python == Path(sys.executable).resolve(),
        "runtime Python executable mismatch",
    )
    require(
        sha256(python) == manifest.get("python_executable_sha256"),
        "runtime Python executable hash mismatch",
    )
    require(
        manifest.get("python_isolated") is True
        and manifest.get("python_no_site") is True,
        "runtime manifest was not built in -I -S mode",
    )
    site_packages = Path(str(manifest.get("site_packages"))).resolve()
    rows = manifest.get("files")
    require(isinstance(rows, list) and bool(rows), "empty runtime manifest")
    require(
        manifest.get("file_count") == len(rows),
        "runtime manifest file-count mismatch",
    )
    seen = set()
    for row in rows:
        require(isinstance(row, dict), "malformed runtime manifest row")
        relative = str(row.get("path"))
        require(relative not in seen, f"duplicate runtime path: {relative}")
        seen.add(relative)
        path = (site_packages / relative).resolve()
        require(
            site_packages in path.parents,
            f"runtime path escapes site-packages: {relative}",
        )
        require(path.is_file(), f"missing runtime file: {relative}")
        require(
            sha256(path) == row.get("sha256"),
            f"runtime file hash mismatch: {relative}",
        )
    return manifest


def load_pinned_numpy(manifest: dict[str, object]):
    site_packages = Path(str(manifest["site_packages"])).resolve()
    sys.path.append(str(site_packages))
    import numpy as np

    audit_loaded_runtime_modules(manifest)
    return np


def audit_loaded_runtime_modules(
    manifest: dict[str, object],
) -> dict[str, object]:
    site_packages = Path(str(manifest["site_packages"])).resolve()
    allowed = {
        str(row["path"]): str(row["sha256"])
        for row in manifest["files"]
    }
    loaded = {}
    for name, module in sorted(sys.modules.items()):
        origin_value = getattr(module, "__file__", None)
        if origin_value is None:
            continue
        origin = Path(origin_value).resolve()
        if site_packages not in origin.parents:
            continue
        relative = str(origin.relative_to(site_packages))
        require(
            relative in allowed,
            f"unmanifested site-package module loaded: {name} -> {relative}",
        )
        actual = sha256(origin)
        require(
            actual == allowed[relative],
            f"loaded module hash mismatch: {name} -> {relative}",
        )
        loaded[name] = {"path": relative, "sha256": actual}
    require("numpy" in loaded, "NumPy was not audited as a loaded module")
    return {
        "loaded_site_package_module_count": len(loaded),
        "loaded_site_package_modules": loaded,
    }


def verify_authorities() -> dict[str, object]:
    require(sys.flags.isolated == 1, "executor requires isolated Python (-I)")
    require(sys.flags.no_site == 1, "executor requires no-site Python (-S)")
    require("sitecustomize" not in sys.modules, "sitecustomize was loaded")
    require("usercustomize" not in sys.modules, "usercustomize was loaded")
    verify_single_seal(SPEC, SPEC_SEAL, SPEC_SHA256)
    verify_single_seal(
        EXACT_DERIVATION,
        EXACT_DERIVATION_SEAL,
        EXACT_DERIVATION_SHA256,
    )
    verify_single_seal(
        AUTHORITY_AMENDMENT,
        AUTHORITY_AMENDMENT_SEAL,
        AUTHORITY_AMENDMENT_SHA256,
    )
    require(
        sha256(RUNTIME_BUILDER) == RUNTIME_BUILDER_SHA256,
        "runtime-manifest builder provenance drift",
    )
    runtime_manifest = verify_runtime_manifest()
    verify_single_seal(SELF, SELF_SEAL)
    direct_rows = []
    for relative, expected in DIRECT_AUTHORITIES.items():
        path = ROOT / relative
        actual = sha256(path)
        require(actual == expected, f"authority drift: {relative}")
        direct_rows.append({"path": relative, "sha256": actual})
    bundle_rows = {}
    for relative, expected in BUNDLE_AUTHORITIES.items():
        bundle_rows[relative] = verify_bundle(relative, expected)
    return {
        "spec_sha256": SPEC_SHA256,
        "exact_derivation_sha256": EXACT_DERIVATION_SHA256,
        "authority_amendment_sha256": AUTHORITY_AMENDMENT_SHA256,
        "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
        "runtime_builder_sha256": RUNTIME_BUILDER_SHA256,
        "self_sha256": sha256(SELF),
        "direct": direct_rows,
        "bundles": bundle_rows,
        "runtime_manifest_file_count": runtime_manifest["file_count"],
        "_runtime_manifest": runtime_manifest,
    }


def pauli_matrices():
    import numpy as np

    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return sx, sy, sz


def dirac_data():
    import numpy as np

    sx, sy, sz = pauli_matrices()
    identity = np.eye(2, dtype=complex)
    zero = np.zeros((2, 2), dtype=complex)
    gamma0 = np.block([[identity, zero], [zero, -identity]])
    spatial = tuple(
        np.block([[zero, sigma], [-sigma, zero]])
        for sigma in (sx, sy, sz)
    )
    gamma5 = 1j * gamma0 @ spatial[0] @ spatial[1] @ spatial[2]
    return gamma0 @ spatial[0], -1j * gamma0 @ gamma5


def covariant_derivative(theta: float):
    import numpy as np

    derivative = np.zeros((SITE_COUNT, SITE_COUNT), dtype=complex)
    phase = np.exp(1j * theta / SITE_COUNT)
    for site in range(SITE_COUNT):
        derivative[site, (site + 1) % SITE_COUNT] += 0.5 * phase
        derivative[site, (site - 1) % SITE_COUNT] -= 0.5 * phase.conjugate()
    return derivative


def covariant_derivative_tangent():
    import numpy as np

    tangent = np.zeros((SITE_COUNT, SITE_COUNT), dtype=complex)
    for site in range(SITE_COUNT):
        tangent[site, (site + 1) % SITE_COUNT] += 1j / 6.0
        tangent[site, (site - 1) % SITE_COUNT] += 1j / 6.0
    return tangent


def c_partial_matrix():
    import numpy as np

    return np.array(
        [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
        dtype=complex,
    )


def embed_record(operator, site: int):
    import numpy as np

    value = np.array([[1.0]], dtype=complex)
    for index in range(RECORD_COUNT):
        value = np.kron(
            value,
            operator if index == site else np.eye(RECORD_DIMENSION, dtype=complex),
        )
    return value


def diamond_time_marginal(local_time: float) -> float:
    if not 0.0 <= local_time <= 1.0:
        return 0.0
    return 32.0 * min(local_time, 1.0 - local_time) ** 3


def exp_hermitian(operator, interval: float):
    import numpy as np

    values, vectors = np.linalg.eigh(operator)
    return (
        vectors
        @ np.diag(np.exp(-1j * interval * values))
        @ vectors.conjugate().T
    )


def exp_hermitian_frechet(operator, tangent, interval: float):
    import numpy as np

    values, vectors = np.linalg.eigh(operator)
    transformed = vectors.conjugate().T @ tangent @ vectors
    phases = np.exp(-1j * interval * values)
    divided = np.empty((len(values), len(values)), dtype=complex)
    for row, left in enumerate(values):
        for column, right in enumerate(values):
            difference = left - right
            if abs(difference) <= 1e-11:
                divided[row, column] = -1j * interval * phases[row]
            else:
                divided[row, column] = (
                    phases[row] - phases[column]
                ) / difference
    exponential = vectors @ np.diag(phases) @ vectors.conjugate().T
    derivative = vectors @ (divided * transformed) @ vectors.conjugate().T
    return exponential, derivative


def ready_injection():
    import numpy as np

    injection = np.zeros(
        (SOURCE_DIMENSION * FINAL_RECORD_DIMENSION, SOURCE_DIMENSION),
        dtype=complex,
    )
    for source in range(SOURCE_DIMENSION):
        injection[source * FINAL_RECORD_DIMENSION, source] = 1.0
    return injection


def parent_data(theta: float):
    import numpy as np

    alpha_x, source_incidence_spin = dirac_data()
    h_source = np.kron(-1j * covariant_derivative(theta), alpha_x)
    h_free = np.kron(
        h_source,
        np.eye(FINAL_RECORD_DIMENSION, dtype=complex),
    )
    tangent_source = np.kron(
        -1j * covariant_derivative_tangent(),
        alpha_x,
    )
    tangent_free = np.kron(
        tangent_source,
        np.eye(FINAL_RECORD_DIMENSION, dtype=complex),
    )
    masks = (
        np.diag([1.0, 1.0, 0.0]).astype(complex),
        np.diag([0.0, 1.0, 1.0]).astype(complex),
    )
    c_partial = c_partial_matrix()
    writes = tuple(
        np.kron(
            np.kron(masks[site], source_incidence_spin),
            embed_record(c_partial, site),
        )
        for site in range(RECORD_COUNT)
    )
    return h_free, tangent_free, writes


def pulse_apply(state, h_free, write):
    dt = 1.0 / MIDPOINT_STEPS
    value = state.copy()
    for index in range(MIDPOINT_STEPS):
        midpoint = (index + 0.5) * dt
        hamiltonian = (
            h_free
            + WRITE_ACTION * diamond_time_marginal(midpoint) * write
        )
        value = exp_hermitian(hamiltonian, dt) @ value
    return value


def pulse_apply_with_tangent(state, tangent_state, h_free, tangent_free, write):
    dt = 1.0 / MIDPOINT_STEPS
    value = state.copy()
    tangent_value = tangent_state.copy()
    for index in range(MIDPOINT_STEPS):
        midpoint = (index + 0.5) * dt
        hamiltonian = (
            h_free
            + WRITE_ACTION * diamond_time_marginal(midpoint) * write
        )
        exponential, derivative = exp_hermitian_frechet(
            hamiltonian,
            tangent_free,
            dt,
        )
        tangent_value = derivative @ value + exponential @ tangent_value
        value = exponential @ value
    return value, tangent_value


def evolve_from_parent(h_free, writes, injection):
    value = injection.copy()
    for write in writes:
        value = pulse_apply(value, h_free, write)
    return value


def evolve_stinespring(theta: float):
    h_free, _, writes = parent_data(theta)
    return evolve_from_parent(h_free, writes, ready_injection())


def evolve_stinespring_with_tangent(theta: float):
    import numpy as np

    h_free, tangent_free, writes = parent_data(theta)
    value = ready_injection()
    tangent = np.zeros_like(value)
    for write in writes:
        value, tangent = pulse_apply_with_tangent(
            value,
            tangent,
            h_free,
            tangent_free,
            write,
        )
    return value, tangent


def outcome_index(outcome: tuple[int, int]) -> int:
    return outcome[0] * RECORD_DIMENSION + outcome[1]


def kraus_family(stinespring):
    tensor = stinespring.reshape(
        SOURCE_DIMENSION,
        FINAL_RECORD_DIMENSION,
        SOURCE_DIMENSION,
    )
    family = {}
    for first in range(RECORD_DIMENSION):
        for second in range(RECORD_DIMENSION):
            outcome = (first, second)
            family[outcome] = tensor[:, outcome_index(outcome), :]
    return family


def scalar_residual(operator) -> float:
    import numpy as np

    scalar = np.trace(operator) / operator.shape[0]
    return float(
        np.linalg.norm(
            operator - scalar * np.eye(operator.shape[0], dtype=complex)
        )
    )


def op_norm(operator) -> float:
    import numpy as np

    return float(np.linalg.norm(operator, ord=2))


def serialize_complex_matrix(operator) -> list[list[list[float]]]:
    return [
        [[float(value.real), float(value.imag)] for value in row]
        for row in operator
    ]


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


def response_from_stinespring(left, right, completed: bool):
    import numpy as np

    record_projection = np.eye(FINAL_RECORD_DIMENSION, dtype=complex)
    if completed:
        record_projection = np.zeros(
            (FINAL_RECORD_DIMENSION, FINAL_RECORD_DIMENSION),
            dtype=complex,
        )
        completed_index = outcome_index(COMPLETED_OUTCOME)
        record_projection[completed_index, completed_index] = 1.0
    return compressed_response(
        left,
        right,
        SOURCE_DIMENSION,
        record_projection,
    )


def response_from_kraus(left, right, completed: bool):
    import numpy as np

    left_family = kraus_family(left)
    right_family = kraus_family(right)
    outcomes = (
        (COMPLETED_OUTCOME,)
        if completed
        else tuple(sorted(left_family))
    )
    value = np.zeros((SOURCE_DIMENSION, SOURCE_DIMENSION), dtype=complex)
    for outcome in outcomes:
        value += (
            left_family[outcome].conjugate().T
            @ right_family[outcome]
        )
    return value


def structural_checks(cache: dict[float, object]) -> dict[str, object]:
    import numpy as np

    identity = np.eye(SOURCE_DIMENSION, dtype=complex)
    pair_rows = []
    maximum_kraus_error = 0.0
    maximum_adjoint_error = 0.0
    maximum_diagonal_error = 0.0
    maximum_comp_lower_violation = 0.0
    maximum_comp_upper_violation = 0.0
    maximum_all_norm = 0.0
    maximum_comp_norm = 0.0

    for theta_plus, theta_minus in HISTORY_PAIRS:
        plus = cache[theta_plus]
        minus = cache[theta_minus]
        all_direct = response_from_stinespring(minus, plus, False)
        all_kraus = response_from_kraus(minus, plus, False)
        comp_direct = response_from_stinespring(minus, plus, True)
        comp_kraus = response_from_kraus(minus, plus, True)
        reverse_all = response_from_stinespring(plus, minus, False)
        reverse_comp = response_from_stinespring(plus, minus, True)

        all_kraus_error = op_norm(all_direct - all_kraus)
        comp_kraus_error = op_norm(comp_direct - comp_kraus)
        all_adjoint_error = op_norm(all_direct.conjugate().T - reverse_all)
        comp_adjoint_error = op_norm(comp_direct.conjugate().T - reverse_comp)
        maximum_kraus_error = max(
            maximum_kraus_error, all_kraus_error, comp_kraus_error
        )
        maximum_adjoint_error = max(
            maximum_adjoint_error, all_adjoint_error, comp_adjoint_error
        )
        maximum_all_norm = max(maximum_all_norm, op_norm(all_direct))
        maximum_comp_norm = max(maximum_comp_norm, op_norm(comp_direct))

        pair_rows.append(
            {
                "theta_plus": theta_plus,
                "theta_minus": theta_minus,
                "all_kraus_direct_error": all_kraus_error,
                "completed_kraus_direct_error": comp_kraus_error,
                "all_adjoint_exchange_error": all_adjoint_error,
                "completed_adjoint_exchange_error": comp_adjoint_error,
                "all_operator_norm": op_norm(all_direct),
                "completed_operator_norm": op_norm(comp_direct),
            }
        )

    for theta in sorted(cache):
        same_all = response_from_stinespring(cache[theta], cache[theta], False)
        same_comp = response_from_stinespring(cache[theta], cache[theta], True)
        diagonal_error = op_norm(same_all - identity)
        eigenvalues = np.linalg.eigvalsh(
            0.5 * (same_comp + same_comp.conjugate().T)
        )
        maximum_diagonal_error = max(maximum_diagonal_error, diagonal_error)
        maximum_comp_lower_violation = max(
            maximum_comp_lower_violation,
            max(0.0, float(-eigenvalues.min())),
        )
        maximum_comp_upper_violation = max(
            maximum_comp_upper_violation,
            max(0.0, float(eigenvalues.max() - 1.0)),
        )

    return {
        "pairs": pair_rows,
        "maximum_kraus_direct_error": maximum_kraus_error,
        "maximum_adjoint_exchange_error": maximum_adjoint_error,
        "maximum_all_diagonal_identity_error": maximum_diagonal_error,
        "maximum_completed_positivity_violation": maximum_comp_lower_violation,
        "maximum_completed_upper_bound_violation": maximum_comp_upper_violation,
        "maximum_all_operator_norm": maximum_all_norm,
        "maximum_completed_operator_norm": maximum_comp_norm,
        "pass": bool(
            maximum_kraus_error <= STRUCTURAL_TOLERANCE
            and maximum_adjoint_error <= STRUCTURAL_TOLERANCE
            and maximum_diagonal_error <= STRUCTURAL_TOLERANCE
            and maximum_comp_lower_violation <= STRUCTURAL_TOLERANCE
            and maximum_comp_upper_violation <= STRUCTURAL_TOLERANCE
            and maximum_all_norm <= 1.0 + STRUCTURAL_TOLERANCE
            and maximum_comp_norm <= 1.0 + STRUCTURAL_TOLERANCE
        ),
    }


def construction_checks(required_thetas: set[float]) -> dict[str, object]:
    import numpy as np

    injection = ready_injection()
    identity_source = np.eye(SOURCE_DIMENSION, dtype=complex)
    injection_isometry_error = op_norm(
        injection.conjugate().T @ injection - identity_source
    )

    pvm_sum = np.zeros(
        (FINAL_RECORD_DIMENSION, FINAL_RECORD_DIMENSION),
        dtype=complex,
    )
    pvm_idempotence_errors = []
    pvm_pair_errors = []
    projectors = []
    for index in range(FINAL_RECORD_DIMENSION):
        projector = np.zeros_like(pvm_sum)
        projector[index, index] = 1.0
        projectors.append(projector)
        pvm_sum += projector
        pvm_idempotence_errors.append(op_norm(projector @ projector - projector))
    for left in range(FINAL_RECORD_DIMENSION):
        for right in range(left + 1, FINAL_RECORD_DIMENSION):
            pvm_pair_errors.append(op_norm(projectors[left] @ projectors[right]))
    pvm_exhaustiveness_error = op_norm(
        pvm_sum - np.eye(FINAL_RECORD_DIMENSION, dtype=complex)
    )

    hamiltonian_hermiticity_errors = []
    tangent_hermiticity_errors = []
    for theta in sorted(required_thetas):
        h_free, tangent_free, writes = parent_data(theta)
        hamiltonian_hermiticity_errors.append(
            op_norm(h_free - h_free.conjugate().T)
        )
        tangent_hermiticity_errors.append(
            op_norm(tangent_free - tangent_free.conjugate().T)
        )
        hamiltonian_hermiticity_errors.extend(
            op_norm(write - write.conjugate().T)
            for write in writes
        )

    maximum_pvm_idempotence_error = max(pvm_idempotence_errors)
    maximum_pvm_orthogonality_error = max(pvm_pair_errors)
    maximum_hamiltonian_hermiticity_error = max(
        hamiltonian_hermiticity_errors
    )
    maximum_tangent_hermiticity_error = max(tangent_hermiticity_errors)
    passed = bool(
        injection_isometry_error <= STRUCTURAL_TOLERANCE
        and pvm_exhaustiveness_error <= STRUCTURAL_TOLERANCE
        and maximum_pvm_idempotence_error <= STRUCTURAL_TOLERANCE
        and maximum_pvm_orthogonality_error <= STRUCTURAL_TOLERANCE
        and maximum_hamiltonian_hermiticity_error <= STRUCTURAL_TOLERANCE
        and maximum_tangent_hermiticity_error <= STRUCTURAL_TOLERANCE
    )
    return {
        "ready_injection_isometry_error": injection_isometry_error,
        "PVM_exhaustiveness_error": pvm_exhaustiveness_error,
        "maximum_PVM_idempotence_error": maximum_pvm_idempotence_error,
        "maximum_PVM_orthogonality_error": maximum_pvm_orthogonality_error,
        "maximum_parent_generator_hermiticity_error":
            maximum_hamiltonian_hermiticity_error,
        "maximum_parent_tangent_hermiticity_error":
            maximum_tangent_hermiticity_error,
        "pass": passed,
    }


def passive_covariance_check(cache: dict[float, object]) -> dict[str, object]:
    import numpy as np

    site_change = np.diag(
        [1.0, np.exp(1j * math.pi / 7.0), np.exp(-1j * math.pi / 5.0)]
    )
    source_change = np.kron(site_change, np.eye(SPIN_DIMENSION, dtype=complex))
    full_change = np.kron(
        source_change,
        np.eye(FINAL_RECORD_DIMENSION, dtype=complex),
    )
    transformed_injection = (
        full_change
        @ ready_injection()
        @ source_change.conjugate().T
    )

    transformed = {}
    stinespring_errors = {}
    for theta in (0.07, -0.11):
        h_free, _, writes = parent_data(theta)
        transformed_h_free = (
            full_change @ h_free @ full_change.conjugate().T
        )
        transformed_writes = tuple(
            full_change @ write @ full_change.conjugate().T
            for write in writes
        )
        transformed[theta] = evolve_from_parent(
            transformed_h_free,
            transformed_writes,
            transformed_injection,
        )
        expected = (
            full_change
            @ cache[theta]
            @ source_change.conjugate().T
        )
        stinespring_errors[str(theta)] = op_norm(
            transformed[theta] - expected
        )

    plus = cache[0.07]
    minus = cache[-0.11]
    plus_changed = transformed[0.07]
    minus_changed = transformed[-0.11]
    rows = {}
    for label, completed in (("all", False), ("completed", True)):
        original = response_from_stinespring(minus, plus, completed)
        changed = response_from_stinespring(
            minus_changed, plus_changed, completed
        )
        expected = source_change @ original @ source_change.conjugate().T
        rows[label] = op_norm(changed - expected)
    return {
        "stinespring_reconstruction_errors": stinespring_errors,
        "all_error": rows["all"],
        "completed_error": rows["completed"],
        "pass": max(
            (*rows.values(), *stinespring_errors.values())
        ) <= STRUCTURAL_TOLERANCE,
    }


def derivative_errors(cache: dict[float, object]) -> dict[str, object]:
    import numpy as np

    base, tangent = evolve_stinespring_with_tangent(0.0)
    base_family = kraus_family(base)
    tangent_family = kraus_family(tangent)
    plus_derivatives = {
        "all": base.conjugate().T @ tangent,
        "completed": (
            base_family[COMPLETED_OUTCOME].conjugate().T
            @ tangent_family[COMPLETED_OUTCOME]
        ),
    }
    minus_derivatives = {
        "all": tangent.conjugate().T @ base,
        "completed": (
            tangent_family[COMPLETED_OUTCOME].conjugate().T
            @ base_family[COMPLETED_OUTCOME]
        ),
    }
    adjoint_errors = {
        label: op_norm(
            minus_derivatives[label]
            - plus_derivatives[label].conjugate().T
        )
        for label in plus_derivatives
    }

    rows: dict[str, dict[str, object]] = {}
    overall_pass = max(adjoint_errors.values()) <= STRUCTURAL_TOLERANCE
    for branch in ("plus", "minus"):
        for label, completed in (("all", False), ("completed", True)):
            analytic = (
                plus_derivatives[label]
                if branch == "plus"
                else minus_derivatives[label]
            )
            denominator = op_norm(analytic)
            require(denominator > 0.0, f"zero Duhamel norm: {branch}/{label}")
            errors = []
            for epsilon in DUHAMEL_EPSILONS:
                if branch == "plus":
                    positive = response_from_stinespring(
                        cache[0.0], cache[epsilon], completed
                    )
                    negative = response_from_stinespring(
                        cache[0.0], cache[-epsilon], completed
                    )
                else:
                    positive = response_from_stinespring(
                        cache[epsilon], cache[0.0], completed
                    )
                    negative = response_from_stinespring(
                        cache[-epsilon], cache[0.0], completed
                    )
                central = (positive - negative) / (2.0 * epsilon)
                errors.append(op_norm(central - analytic) / denominator)
            decreasing = all(
                errors[index + 1] < errors[index]
                for index in range(len(errors) - 1)
            )
            factors = [
                errors[index] / errors[index + 1]
                for index in range(len(errors) - 1)
            ]
            row_pass = bool(
                errors[-1] <= DUHAMEL_FINE_TOLERANCE
                and decreasing
                and all(factor >= 2.0 for factor in factors)
            )
            rows[f"{branch}_{label}"] = {
                "duhamel_operator_norm": denominator,
                "epsilons": list(DUHAMEL_EPSILONS),
                "relative_errors": errors,
                "reduction_factors": factors,
                "strictly_decreasing": decreasing,
                "pass": row_pass,
            }
            overall_pass = overall_pass and row_pass

    return {
        "rows": rows,
        "adjoint_exchange_errors": adjoint_errors,
        "analytic_derivatives": {
            "plus_all": serialize_complex_matrix(plus_derivatives["all"]),
            "plus_completed": serialize_complex_matrix(
                plus_derivatives["completed"]
            ),
            "minus_all": serialize_complex_matrix(minus_derivatives["all"]),
            "minus_completed": serialize_complex_matrix(
                minus_derivatives["completed"]
            ),
        },
        "pass": bool(overall_pass),
    }


def route1_special_case_control() -> dict[str, object]:
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
    rows = []
    maximum_component_error = 0.0
    maximum_all_error = 0.0
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
        expected_full = 0.5 * (
            1.0 + np.exp(1j * (theta_plus - theta_minus))
        )
        component_error = abs(completed - expected_completed)
        full_error = abs(full - expected_full)
        maximum_component_error = max(maximum_component_error, component_error)
        maximum_all_error = max(maximum_all_error, full_error)
        rows.append(
            {
                "theta_plus": theta_plus,
                "theta_minus": theta_minus,
                "route1_completed_component_real": completed.real,
                "route1_completed_component_imag": completed.imag,
                "completed_component_error": component_error,
                "route2_generic_all_kernel_real": full.real,
                "route2_generic_all_kernel_imag": full.imag,
                "all_kernel_error": full_error,
            }
        )
    passed = bool(
        maximum_component_error <= STRUCTURAL_TOLERANCE
        and maximum_all_error <= STRUCTURAL_TOLERANCE
    )
    return {
        "rows": rows,
        "maximum_completed_component_error": maximum_component_error,
        "maximum_all_kernel_error": maximum_all_error,
        "overall_verdict": (
            "ROUTE1_SPECIAL_CASE_CONSISTENCY_FALSIFIER_PASSED"
            if passed
            else "ROUTE1_SPECIAL_CASE_CONSISTENCY_FALSIFIER_FAILED"
        ),
        "actual_parent_route1_line_restriction_derived": False,
        "pass": passed,
    }


def run() -> dict[str, object]:
    authority = verify_authorities()
    runtime_manifest = authority.pop("_runtime_manifest")
    np = load_pinned_numpy(runtime_manifest)

    numpy_origin = Path(np.__file__).resolve()
    approved_runtime = Path(
        "/Users/bgm/.cache/codex-runtimes/"
        "codex-primary-runtime/dependencies/python"
    ).resolve()
    require(
        approved_runtime in numpy_origin.parents,
        f"NumPy loaded outside approved runtime: {numpy_origin}",
    )
    required_thetas = {
        value
        for pair in HISTORY_PAIRS
        for value in pair
    }
    required_thetas.update(DUHAMEL_EPSILONS)
    required_thetas.update(-value for value in DUHAMEL_EPSILONS)
    cache = {
        theta: evolve_stinespring(theta)
        for theta in sorted(required_thetas)
    }

    zero_family = kraus_family(cache[0.0])
    completed = zero_family[COMPLETED_OUTCOME]
    completed_frobenius = float(np.linalg.norm(completed))
    completed_scalar_distance = scalar_residual(completed)
    witness = {
        "completed_11_frobenius_norm": completed_frobenius,
        "completed_11_scalar_distance": completed_scalar_distance,
        "expected_frobenius_norm": 2.158029616704532,
        "expected_scalar_distance": 2.151758052952419,
        "frobenius_reproduction_error":
            abs(completed_frobenius - 2.158029616704532),
        "scalar_distance_reproduction_error":
            abs(completed_scalar_distance - 2.151758052952419),
        "completed_11_is_non_scalar":
            completed_scalar_distance > STRUCTURAL_TOLERANCE,
    }
    witness["pass"] = bool(
        witness["frobenius_reproduction_error"] <= STRUCTURAL_TOLERANCE
        and witness["scalar_distance_reproduction_error"] <= STRUCTURAL_TOLERANCE
        and witness["completed_11_is_non_scalar"]
    )

    construction = construction_checks(required_thetas)
    structural = structural_checks(cache)
    covariance = passive_covariance_check(cache)
    duhamel = derivative_errors(cache)
    route1 = route1_special_case_control()
    terminal_runtime_audit = audit_loaded_runtime_modules(runtime_manifest)

    exact_derivation_binding = {
        "authority_path": str(EXACT_DERIVATION.relative_to(ROOT)),
        "authority_sha256": EXACT_DERIVATION_SHA256,
        "D1_isometric_Stinespring_map":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "D2_PVM_Kraus_resolution":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "D3_structural_operator_identities":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "D4_passive_source_basis_covariance":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "D5_finite_Duhamel_derivative":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "D6_Route1_architecture_control":
            "PROVED_IN_SEALED_EXACT_DERIVATION",
        "numerical_execution_is_proof_of_exact_identity": False,
    }

    passed = bool(
        construction["pass"]
        and witness["pass"]
        and structural["pass"]
        and covariance["pass"]
        and duhamel["pass"]
        and route1["pass"]
    )

    return {
        "schema": "stage8_t7_primitive_operator_response_v001",
        "authority_verification": authority,
        "runtime": {
            "python_executable": sys.executable,
            "python_isolated": bool(sys.flags.isolated),
            "numpy_version": np.__version__,
            "numpy_origin": str(numpy_origin),
            "terminal_module_audit": terminal_runtime_audit,
        },
        "frozen_regression": {
            "site_count": SITE_COUNT,
            "spin_dimension": SPIN_DIMENSION,
            "record_count": RECORD_COUNT,
            "record_dimension": RECORD_DIMENSION,
            "midpoint_steps_per_pulse": MIDPOINT_STEPS,
            "write_action": "pi/sqrt(2)",
            "history_pairs": [list(pair) for pair in HISTORY_PAIRS],
            "duhamel_epsilons": list(DUHAMEL_EPSILONS),
            "completed_outcome": list(COMPLETED_OUTCOME),
            "arithmetic": "IEEE-754 binary64 / numpy complex128",
            "structural_tolerance": STRUCTURAL_TOLERANCE,
            "duhamel_finest_tolerance": DUHAMEL_FINE_TOLERANCE,
        },
        "exact_derivation_binding": exact_derivation_binding,
        "finite_construction_checks": construction,
        "actual_parent_non_scalar_witness": witness,
        "structural_regression": structural,
        "passive_source_basis_covariance": covariance,
        "finite_operator_Duhamel_regression": duhamel,
        "route1_special_case_consistency_falsifier": route1,
        "overall_verdict": (
            "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED"
            if passed
            else "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_BLOCKED"
        ),
        "finite_primitive_operator_response_bundle_derived": passed,
        "finite_primitive_operator_Duhamel_tangent_derived": passed,
        "primitive_source_scalarization_derived": False,
        "complete_Qspec_state_hash_pinned_for_route2": False,
        "route1_special_case_consistency_falsifier_frozen": True,
        "route1_special_case_consistency_falsifier_passed":
            bool(route1["pass"]),
        "actual_parent_route1_line_restriction_derived": False,
        "finite_primitive_operator_gauge_covariance_derived": False,
        "finite_primitive_operator_graded_monoidality_derived": False,
        "stage8_route2_architecture_amended": False,
        "volume_uniform_zero_free_neighborhood_proved": False,
        "connected_linked_cluster_density_proved": False,
        "Duhamel_intensive_Hessian_equality_proved": False,
        "kappa_record_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_target_access_attestation": True,
    }


def main() -> None:
    atomic_write(
        {
            "schema": "stage8_t7_primitive_operator_response_v001",
            "overall_verdict":
                "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BLOCKED_PENDING_RUN",
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
            "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_DERIVED"
        ):
            raise SystemExit(1)
    except SystemExit:
        raise
    except Exception as error:
        blocked = {
            "schema": "stage8_t7_primitive_operator_response_v001",
            "overall_verdict":
                "FINITE_PRIMITIVE_OPERATOR_RESPONSE_BUNDLE_BLOCKED",
            "failure_type": type(error).__name__,
            "failure_message": str(error),
            "finite_primitive_operator_response_bundle_derived": False,
            "finite_primitive_operator_Duhamel_tangent_derived": False,
            "primitive_source_scalarization_derived": False,
            "complete_Qspec_state_hash_pinned_for_route2": False,
            "route1_special_case_consistency_falsifier_passed": False,
            "actual_parent_route1_line_restriction_derived": False,
            "finite_primitive_operator_gauge_covariance_derived": False,
            "finite_primitive_operator_graded_monoidality_derived": False,
            "stage8_route2_architecture_amended": False,
            "volume_uniform_zero_free_neighborhood_proved": False,
            "connected_linked_cluster_density_proved": False,
            "Duhamel_intensive_Hessian_equality_proved": False,
            "kappa_record_computed": False,
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
