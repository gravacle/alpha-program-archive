#!/usr/bin/env python3
"""Rigorous Arb certificate for the frozen dyadic zero-transfer matrix."""

from __future__ import annotations

import base64
import csv
from decimal import Decimal, getcontext
from fractions import Fraction
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

NUMPY_SITE = (
    Path.home() / "Library/Python/3.9/lib/python/site-packages"
)
if str(NUMPY_SITE) not in sys.path:
    sys.path.insert(0, str(NUMPY_SITE))

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DEPS = ROOT.parents[1] / ".proof_deps/python_flint"
if str(DEPS) not in sys.path:
    sys.path.insert(0, str(DEPS))

flint = None
acb = None
acb_mat = None
arb = None


SPEC = (
    ROOT
    / "COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md"
)
SPEC_SEAL = Path(f"{SPEC}.seal.sha256")
SCRIPT_SEAL = Path(f"{Path(__file__).resolve()}.seal.sha256")
VERIFIER = (
    ROOT
    / "scripts/verify_complete_qspec_periodic_analytic_continuation_v003.py"
)
THEOREM_JSON = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_periodic_uniform_zero_free_theorem_v001.json"
)
REVIEW_CORRECTION = (
    ROOT
    / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_REVIEW_CORRECTION_V001.md"
)
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_zero_transfer_dyadic_ball_certificate_v001.json"
)

EXPECTED = {
    SPEC:
        "ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95",
    VERIFIER:
        "1cd9528bc6872a3a28df828a452a165f8672cccc455a64323edab9e0905bf69d",
    THEOREM_JSON:
        "048d18a2ac666639a44ec0d52b584a412ece9fdeb90837abffa86e831fc652e0",
    REVIEW_CORRECTION:
        "8d2ab3a0102cb4e8ba7ab925773e1a6fd08b763202859688b14ea4cd12f39650",
    DEPS / "python_flint-0.6.0.dist-info/METADATA":
        "d6b5be0f3a94ff92ad45f8e9d8991ac8face10ab71e362b8b9f25819df4ef06b",
    DEPS / "python_flint-0.6.0.dist-info/RECORD":
        "9b76e8ba99a8555fa73c855c2459614714f25136238c1c96fa6c82dad5b9cf94",
    DEPS / "flint/__init__.py":
        "b959e94c11c23633c0cbfea849a07955b8f252fc3100fd2ed52bd3c35118ba93",
}

EXPECTED_TRANSFER_HEX_SHA256 = (
    "69d6a95de251be3e3aa83d7344c7961b2023f41416399b760d3096fcde83718b"
)
EXPECTED_TRACE_COLUMN_HEX_SHA256 = (
    "07506154f602a1fa17e32c81f4bc377e547868eb4bf540ed11248949afea0876"
)

PRECISION_BITS = 192
FLINT_THREADS = 4
CBAR = Fraction(203, 250)
FINAL_R0_CEILING = Fraction(813, 1000)
ANCHOR_ALLOWANCE = Fraction(1, 10**10)
GRAPH_RADIUS = Fraction(1, 10**8)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_authorities() -> dict[str, str]:
    observed: dict[str, str] = {}
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing frozen authority: {path}")
        actual = sha256(path)
        require(
            actual == expected,
            f"authority mismatch for {path}: {actual} != {expected}",
        )
        observed[str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)] = actual

    fields = SPEC_SEAL.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, "malformed certificate-spec seal")
    require(fields[0] == EXPECTED[SPEC], "certificate-spec seal hash mismatch")
    require(fields[1] == SPEC.name, "certificate-spec seal target mismatch")

    script_fields = SCRIPT_SEAL.read_text(encoding="ascii").strip().split()
    require(len(script_fields) == 2, "malformed certificate-script seal")
    require(
        script_fields[0] == sha256(Path(__file__)),
        "certificate-script seal hash mismatch",
    )
    require(
        script_fields[1] == Path(__file__).name,
        "certificate-script seal target mismatch",
    )
    return observed


def verify_full_wheel_record() -> dict[str, object]:
    record = DEPS / "python_flint-0.6.0.dist-info/RECORD"
    verified: list[dict[str, object]] = []
    deps_root = DEPS.resolve()
    with record.open(newline="", encoding="utf-8") as handle:
        for relative, encoded_hash, encoded_size in csv.reader(handle):
            if not encoded_hash:
                continue
            candidate = (DEPS / relative).resolve()
            if not candidate.is_relative_to(deps_root):
                raise RuntimeError(
                    f"hashed wheel path escapes dependency root: {relative}"
                )
            require(candidate.is_file(), f"wheel payload missing: {relative}")
            algorithm, expected_digest = encoded_hash.split("=", 1)
            require(algorithm == "sha256", "non-SHA256 wheel RECORD entry")
            observed_digest = base64.urlsafe_b64encode(
                hashlib.sha256(candidate.read_bytes()).digest()
            ).decode("ascii").rstrip("=")
            require(
                observed_digest == expected_digest,
                f"wheel payload hash mismatch: {relative}",
            )
            require(
                candidate.stat().st_size == int(encoded_size),
                f"wheel payload size mismatch: {relative}",
            )
            verified.append(
                {
                    "path": relative,
                    "sha256_urlsafe_base64": observed_digest,
                    "size": int(encoded_size),
                }
            )
    require(len(verified) > 100, "implausibly small verified wheel payload")
    native = [
        item
        for item in verified
        if str(item["path"]).endswith((".so", ".dylib"))
    ]
    require(bool(native), "wheel verification found no native payload")
    return {
        "verified_hashed_files": len(verified),
        "verified_native_files": len(native),
        "native_payload": native,
    }


def load_verified_ball_runtime() -> None:
    global flint, acb, acb_mat, arb
    flint = importlib.import_module("flint")
    types_module = importlib.import_module("flint")
    acb = types_module.acb
    acb_mat = types_module.acb_mat
    arb = types_module.arb


def verify_imported_flint_origins() -> list[str]:
    dependency_root = DEPS.resolve()
    origins: list[str] = []
    for name, module in sorted(sys.modules.items()):
        if not (name == "flint" or name.startswith("flint.")):
            continue
        origin = getattr(module, "__file__", None)
        if origin is None:
            continue
        path = Path(origin).resolve()
        require(
            path.is_relative_to(dependency_root),
            f"flint module imported outside pinned wheel: {name}: {path}",
        )
        origins.append(str(path.relative_to(dependency_root)))
    require(bool(origins), "no imported flint module origins recorded")
    return origins


def verify_imported_numpy_origins() -> list[str]:
    site_root = NUMPY_SITE.resolve()
    origins: list[str] = []
    for name, module in sorted(sys.modules.items()):
        if not (name == "numpy" or name.startswith("numpy.")):
            continue
        origin = getattr(module, "__file__", None)
        if origin is None:
            continue
        path = Path(origin).resolve()
        require(
            path.is_relative_to(site_root),
            f"NumPy module imported outside declared site: {name}: {path}",
        )
        origins.append(str(path.relative_to(site_root)))
    require(bool(origins), "no imported NumPy module origins recorded")
    return origins


def load_verifier():
    module_spec = importlib.util.spec_from_file_location(
        "qspec_independent_v003",
        VERIFIER,
    )
    module = importlib.util.module_from_spec(module_spec)
    assert module_spec.loader is not None
    module_spec.loader.exec_module(module)
    return module


def stabilized_zero_transfer(verifier):
    parent = verifier.build_parent()
    raw_cells = tuple(
        verifier.cell_kraus(
            parent["free_zero"],
            interaction,
            parent["record"],
            use_hermitian_spectral_step=True,
        )
        for interaction in parent["interactions"]
    )
    repaired = tuple(
        verifier.retract_stinespring_isometry(kraus)
        for kraus in raw_cells
    )
    require(
        all(bool(item[1]["pass"]) for item in repaired),
        "zero-history Stinespring repair failed",
    )
    zero_cells = tuple(item[0] for item in repaired)
    zero_composites = verifier.composite_kraus(zero_cells)
    support, support_invariance = verifier.reachable_support(
        parent["source_vector"],
        zero_composites,
    )
    require(support.shape[1] == 5, "unexpected zero support dimension")
    require(support_invariance < 1e-11, "zero support is not invariant")
    transfer = verifier.reduced_transfer(
        zero_composites,
        zero_composites,
        support,
    )
    trace_row = support.conjugate().reshape(-1)
    trace_column = trace_row.conjugate()
    return transfer, trace_column, support_invariance


def canonical_hex_sha256(array: np.ndarray) -> str:
    digest = hashlib.sha256()
    for value in np.asarray(array).reshape(-1):
        z = complex(value)
        digest.update(float(z.real).hex().encode("ascii"))
        digest.update(b" ")
        digest.update(float(z.imag).hex().encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def arb_from_binary64(value: float) -> arb:
    numerator, denominator = float(value).as_integer_ratio()
    return arb(numerator) / arb(denominator)


def arb_from_fraction(value: Fraction) -> arb:
    return arb(value.numerator) / arb(value.denominator)


def acb_from_complex128(value: complex) -> acb:
    z = complex(value)
    return acb(
        arb_from_binary64(z.real),
        arb_from_binary64(z.imag),
    )


def acb_matrix_from_numpy(array: np.ndarray) -> acb_mat:
    matrix = np.asarray(array, dtype=np.complex128)
    rows, columns = matrix.shape
    entries = [
        acb_from_complex128(value)
        for value in matrix.reshape(-1)
    ]
    return acb_mat(rows, columns, entries)


def acb_column_from_numpy(array: np.ndarray) -> acb_mat:
    vector = np.asarray(array, dtype=np.complex128).reshape(-1)
    return acb_mat(
        len(vector),
        1,
        [acb_from_complex128(value) for value in vector],
    )


def arb_max(values: list[arb]) -> arb:
    require(bool(values), "arb_max received an empty list")
    winner = values[0]
    for value in values[1:]:
        winner = winner.max(value)
    return winner


def matrix_norm_upper(matrix: acb_mat) -> dict[str, arb]:
    rows = matrix.nrows()
    columns = matrix.ncols()
    row_sums: list[arb] = []
    for row in range(rows):
        total = arb(0)
        for column in range(columns):
            total += abs(matrix[row, column]).upper()
        row_sums.append(total)
    column_sums: list[arb] = []
    for column in range(columns):
        total = arb(0)
        for row in range(rows):
            total += abs(matrix[row, column]).upper()
        column_sums.append(total)
    norm_inf = arb_max(row_sums)
    norm_one = arb_max(column_sums)
    return {
        "one": norm_one,
        "infinity": norm_inf,
        "two": (norm_one * norm_inf).sqrt(),
    }


def hermitian_contains_zero(matrix: acb_mat) -> bool:
    defect = matrix - matrix.conjugate().transpose()
    return bool(defect.contains(acb_mat(matrix.nrows(), matrix.ncols())))


def interval_gershgorin_positive(
    matrix: acb_mat,
) -> dict[str, object]:
    require(matrix.nrows() == matrix.ncols(), "Gershgorin matrix not square")
    size = matrix.nrows()
    margins: list[arb] = []
    diagonal_imaginary_contains_zero = True
    for row in range(size):
        diagonal = matrix[row, row]
        diagonal_imaginary_contains_zero = bool(
            diagonal_imaginary_contains_zero
            and diagonal.imag.contains(0)
        )
        off_diagonal_radius = arb(0)
        for column in range(size):
            if column != row:
                off_diagonal_radius += abs(matrix[row, column]).upper()
        margins.append(
            diagonal.real.lower() - off_diagonal_radius
        )
    minimum = margins[0]
    for margin in margins[1:]:
        minimum = minimum.min(margin)
    passed = bool(
        diagonal_imaginary_contains_zero
        and minimum > 0
        and hermitian_contains_zero(matrix)
    )
    return {
        "dimension": size,
        "minimum_lower_margin": str(minimum),
        "diagonal_imaginary_contains_zero": (
            diagonal_imaginary_contains_zero
        ),
        "Hermitian_defect_contains_zero": (
            hermitian_contains_zero(matrix)
        ),
        "pass": passed,
    }


def exact_ball_complement(
    transfer: np.ndarray,
    trace_column: np.ndarray,
) -> tuple[acb_mat, acb_mat, dict[str, object]]:
    print("ball: converting exact dyadic transfer", flush=True)
    transfer_ball = acb_matrix_from_numpy(transfer)
    trace_ball = acb_column_from_numpy(trace_column)
    trace_dagger = trace_ball.conjugate().transpose()
    tau = (trace_dagger * trace_ball)[0, 0]
    require(tau.imag.contains(0), "trace norm acquired imaginary part")
    require(tau.real > 0, "trace norm is not positive")

    print("ball: constructing exact rational anchor/complement", flush=True)
    projector = (trace_ball * trace_dagger) / tau
    transfer_trace = transfer_ball * trace_ball
    trace_transfer = trace_dagger * transfer_ball
    trace_transfer_trace = (trace_transfer * trace_ball)[0, 0]

    complement = transfer_ball - (
        (trace_ball * trace_transfer) / tau
    )
    complement = complement - (
        (transfer_trace * trace_dagger) / tau
    )
    complement = complement + (
        projector * (trace_transfer_trace / tau)
    )

    anchor_defect = transfer_ball - (projector + complement)
    anchor_norms = matrix_norm_upper(anchor_defect)
    anchor_pass = bool(
        anchor_norms["two"]
        < arb_from_fraction(ANCHOR_ALLOWANCE)
    )
    diagnostics = {
        "trace_norm_squared_ball": str(tau),
        "anchor_defect_norm_one_upper": str(anchor_norms["one"]),
        "anchor_defect_norm_infinity_upper": str(
            anchor_norms["infinity"]
        ),
        "anchor_defect_norm_two_upper": str(anchor_norms["two"]),
        "anchor_defect_below_1e_minus_10": anchor_pass,
    }
    require(anchor_pass, "rigorous anchor-defect allowance failed")

    del transfer_ball
    del transfer_trace
    del trace_transfer
    del trace_transfer_trace
    del trace_ball
    del trace_dagger
    del anchor_defect
    gc.collect()
    return complement, projector, diagnostics


def approximate_preconditioner(
    transfer: np.ndarray,
    trace_column: np.ndarray,
) -> tuple[np.ndarray, dict[str, float]]:
    tau = np.vdot(trace_column, trace_column)
    projector = np.outer(
        trace_column,
        trace_column.conjugate(),
    ) / tau
    identity = np.eye(transfer.shape[0], dtype=np.complex128)
    q = identity - projector
    complement = q @ transfer @ q
    hessian = (
        float(CBAR) ** 2 * identity
        - complement.conjugate().T @ complement
    )
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    return eigenvectors, {
        "diagnostic_complement_norm":
            float(np.linalg.norm(complement, 2)),
        "diagnostic_H_minimum_eigenvalue":
            float(eigenvalues[0]),
        "diagnostic_H_maximum_eigenvalue":
            float(eigenvalues[-1]),
        "diagnostic_preconditioner_unitarity_defect":
            float(
                np.linalg.norm(
                    eigenvectors.conjugate().T @ eigenvectors
                    - identity,
                    np.inf,
                )
            ),
    }


def rigorous_singular_bound(
    complement: acb_mat,
    preconditioner: np.ndarray,
) -> dict[str, object]:
    print("ball: converting congruence preconditioner", flush=True)
    v_ball = acb_matrix_from_numpy(preconditioner)
    v_dagger = v_ball.conjugate().transpose()

    print("ball: computing V^dagger V", flush=True)
    gram = v_dagger * v_ball
    gram_certificate = interval_gershgorin_positive(gram)
    require(gram_certificate["pass"], "V invertibility certificate failed")

    print("ball: computing R V", flush=True)
    rv = complement * v_ball
    del complement
    gc.collect()

    print("ball: computing congruence H certificate", flush=True)
    rv_gram = rv.conjugate().transpose() * rv
    cbar = arb(203) / arb(250)
    congruence = gram * (cbar * cbar) - rv_gram
    h_certificate = interval_gershgorin_positive(congruence)
    require(
        h_certificate["pass"],
        "0.812^2 I - R^dagger R positivity certificate failed",
    )

    del v_ball
    del v_dagger
    del gram
    del rv
    del rv_gram
    del congruence
    gc.collect()
    return {
        "c_bar": "0.812",
        "preconditioner_Gram": gram_certificate,
        "congruence_H": h_certificate,
        "conclusion": "operator_norm_R_strictly_below_0.812",
        "pass": bool(
            gram_certificate["pass"]
            and h_certificate["pass"]
        ),
    }


def graph_enclosure() -> dict[str, object]:
    one = Fraction(1)
    delta = ANCHOR_ALLOWANCE
    radius = GRAPH_RADIUS
    r_bar = CBAR

    graph_gap = (
        one - delta - delta * radius - r_bar
    )
    graph_map_radius = delta / graph_gap
    graph_lipschitz = delta * delta / (graph_gap * graph_gap)
    lambda_min = one - delta - delta * radius
    complement_after_right_graph = r_bar + delta * radius
    sylvester_gap = (
        lambda_min - complement_after_right_graph
    )
    left_graph_radius = delta / sylvester_gap
    similarity_condition = (
        (one + radius) / (one - radius)
    ) ** 2
    lambda_spectral_remainder_upper = (
        similarity_condition
        * complement_after_right_graph
    )
    leading_eigenvalue_unit_shift_upper = (
        delta * (one + radius)
    )
    unit_projector_remainder_upper = (
        lambda_spectral_remainder_upper
        + similarity_condition
        * leading_eigenvalue_unit_shift_upper
    )

    passed = bool(
        graph_gap > 0
        and graph_map_radius < radius
        and graph_lipschitz < 1
        and sylvester_gap > 0
        and left_graph_radius < radius
        and unit_projector_remainder_upper < FINAL_R0_CEILING
    )

    getcontext().prec = 100

    def exact_record(value: Fraction) -> dict[str, object]:
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
            "decimal": str(
                Decimal(value.numerator) / Decimal(value.denominator)
            ),
        }

    return {
        "arithmetic": "exact_rational",
        "anchor_allowance": exact_record(delta),
        "anchor_graph_radius": exact_record(radius),
        "anchor_complement_bound": exact_record(r_bar),
        "right_graph_gap": exact_record(graph_gap),
        "right_graph_map_radius": exact_record(graph_map_radius),
        "right_graph_Lipschitz_bound": exact_record(graph_lipschitz),
        "leading_eigenvalue_modulus_lower": exact_record(lambda_min),
        "right_graph_complement_bound": exact_record(
            complement_after_right_graph
        ),
        "left_Sylvester_gap": exact_record(sylvester_gap),
        "left_graph_radius": exact_record(left_graph_radius),
        "similarity_condition_bound": exact_record(
            similarity_condition
        ),
        "T_minus_lambda_P_spectral_remainder_norm_upper": exact_record(
            lambda_spectral_remainder_upper
        ),
        "leading_eigenvalue_unit_shift_upper": exact_record(
            leading_eigenvalue_unit_shift_upper
        ),
        "spectral_projector_norm_upper": exact_record(
            similarity_condition
        ),
        "T_minus_unit_P_R0_norm_upper": exact_record(
            unit_projector_remainder_upper
        ),
        "final_required_ceiling": exact_record(FINAL_R0_CEILING),
        "pass": passed,
    }


def main() -> None:
    started = time.time()
    require(sys.flags.isolated == 1, "execute with python3 -I")
    require(sys.flags.no_user_site == 1, "user site must be disabled")
    authorities = verify_authorities()
    wheel_record = verify_full_wheel_record()
    load_verified_ball_runtime()
    imported_flint_origins = verify_imported_flint_origins()
    imported_numpy_origins = verify_imported_numpy_origins()
    require(
        flint.__version__ == "0.6.0",
        f"unexpected python-flint version: {flint.__version__}",
    )
    flint.ctx.prec = PRECISION_BITS
    flint.ctx.threads = FLINT_THREADS

    verifier = load_verifier()
    transfer, trace_column, support_invariance = (
        stabilized_zero_transfer(verifier)
    )
    require(
        transfer.shape == (350, 350),
        f"unexpected transfer shape: {transfer.shape}",
    )
    transfer_hash = canonical_hex_sha256(transfer)
    trace_hash = canonical_hex_sha256(trace_column)
    require(
        transfer_hash == EXPECTED_TRANSFER_HEX_SHA256,
        "frozen transfer canonical hash mismatch",
    )
    require(
        trace_hash == EXPECTED_TRACE_COLUMN_HEX_SHA256,
        "frozen trace-column canonical hash mismatch",
    )

    preconditioner, midpoint_diagnostics = (
        approximate_preconditioner(transfer, trace_column)
    )
    complement_ball, projector_ball, anchor_diagnostics = (
        exact_ball_complement(transfer, trace_column)
    )
    del projector_ball
    gc.collect()

    singular_certificate = rigorous_singular_bound(
        complement_ball,
        preconditioner,
    )
    graph_certificate = graph_enclosure()
    require(graph_certificate["pass"], "anchor graph enclosure failed")

    passed = bool(
        anchor_diagnostics[
            "anchor_defect_below_1e_minus_10"
        ]
        and singular_certificate["pass"]
        and graph_certificate["pass"]
    )
    result = {
        "schema":
            "complete_qspec_zero_transfer_dyadic_ball_certificate_v001",
        "exact_object":
            "frozen_96_slice_binary64_dyadic_zero_transfer",
        "scope": {
            "frozen_dyadic_numerical_regulator_only": True,
            "continuous_time_parent_R0_certified": False,
            "periodic_volume_uniform_zero_free_neighborhood_proved":
                False,
            "periodic_thermodynamic_log_density_proved": False,
            "periodic_connected_linked_cluster_density_proved": False,
            "all_stage8_regulators_zero_free_proved": False,
        },
        "authorities": authorities,
        "wheel_record_verification": wheel_record,
        "imported_flint_module_origins": imported_flint_origins,
        "numpy_version": np.__version__,
        "imported_numpy_module_origins_non_authoritative":
            imported_numpy_origins,
        "numpy_role": (
            "reconstructs a canonically hash-pinned dyadic object and "
            "supplies a non-authoritative congruence preconditioner"
        ),
        "python_isolated_mode": bool(sys.flags.isolated),
        "script_sha256": sha256(Path(__file__)),
        "python_flint_version": flint.__version__,
        "arb_precision_bits": PRECISION_BITS,
        "flint_threads": FLINT_THREADS,
        "transfer_dimension": transfer.shape[0],
        "transfer_canonical_hex_sha256": transfer_hash,
        "trace_column_canonical_hex_sha256": trace_hash,
        "zero_support_invariance_residual_binary64":
            support_invariance,
        "midpoint_diagnostics_not_used_as_proof":
            midpoint_diagnostics,
        "anchor_certificate": anchor_diagnostics,
        "singular_value_certificate": singular_certificate,
        "graph_enclosure_certificate": graph_certificate,
        "verdict": (
            "FROZEN_DYADIC_ZERO_TRANSFER_R0_CERTIFIED"
            if passed
            else "FROZEN_DYADIC_ZERO_TRANSFER_R0_BLOCKED"
        ),
        "pass": passed,
        "validated_frozen_dyadic_R0_enclosure_proved": passed,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "elapsed_seconds": time.time() - started,
        "target_access_statement": (
            "The rational 0.812 enclosure was selected after the "
            "midpoint diagnostic; no alpha or coupling target enters "
            "the certificate."
        ),
        "no_alpha_or_coupling_target_access_attestation": True,
        "generic_target_blindness_claimed": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "anchor_norm_upper": anchor_diagnostics[
                    "anchor_defect_norm_two_upper"
                ],
                "gram_margin": singular_certificate[
                    "preconditioner_Gram"
                ]["minimum_lower_margin"],
                "H_margin": singular_certificate[
                    "congruence_H"
                ]["minimum_lower_margin"],
                "r0_upper": graph_certificate[
                    "T_minus_unit_P_R0_norm_upper"
                ]["decimal"],
                "elapsed_seconds": result["elapsed_seconds"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        ),
        flush=True,
    )
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
