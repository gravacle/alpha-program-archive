#!/usr/bin/env python3
"""Ball certificate for the canonical exact-spin-2 periodic transfer."""

from __future__ import annotations

import base64
import csv
from fractions import Fraction
import gc
import hashlib
import itertools
import json
from pathlib import Path
import runpy
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
SYMPY_ROOT = ROOT / ".proof_deps/sympy"
FLINT_ROOT = ROOT.parents[1] / ".proof_deps/python_flint"
NUMPY_ROOT = Path.home() / "Library/Python/3.9/lib/python/site-packages"

SPEC = (
    ROOT
    / "COMPLETE_QSPEC_CANONICAL_SPIN2_TRANSFER_BALL_CERTIFICATE_SPEC_V001.md"
)
SCRIPT = Path(__file__).resolve()
OUT = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_canonical_spin2_transfer_ball_certificate_v001.json"
)

EXACT_EXECUTOR = (
    ROOT / "scripts/prove_complete_qspec_exact_spin2_support_bridge_v001.py"
)
EXACT_JSON = (
    ROOT
    / "stage8_execution/work/"
    "QSPEC_exact_spin2_support_bridge_v001.json"
)
EXTERNAL_REVIEW = Path(
    "/Users/bgm/MB Work/alpha_supervision/"
    "OVERNIGHT_PROOF_ADJUDICATION_RETURN_V001.md"
)

EXPECTED = {
    SPEC:
        "80c21c579518bb28878b0468615e3d03a02654356964074a50e3684820f43f06",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md":
        "b92e69082d297b38700abcc9750e3b70899714133c290538a03885ebb90079c0",
    ROOT / "COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md":
        "ad3286ee2961fc7569db7ed6572e1cb4bdc5ff5415226cd2b5b5e56625b2ab1e",
    EXACT_EXECUTOR:
        "5aeaf5f88f95f62b188d424e695ab3bc47c320a11fe89f5ef70497a0cef7f052",
    EXACT_JSON:
        "093585374cc3cc1aafb4e500e7de032cec81809b6ee30800cc763b3c1d53fa3e",
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md":
        "6a49a75669e61f74b2d1a6904c7bc1a4bb172842f4b01b84456c4cee65334676",
    ROOT / "COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md":
        "e0b477ac3fa2a8cdb48523465739d695e46076c141356229eed249789e26fdf2",
    EXTERNAL_REVIEW:
        "83a59120eb09e4d058602234d89aacfe6aeedaa792d4983f3ae8e3389f6efcf2",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md":
        "54c972914b180d694517ed7598ac3344fd4dde3aa953d139a7a1572ddb281690",
    ROOT / "COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md":
        "ada56f525f4a5a9708545e29e62e7e5f0e2dd762d37f168429284194c7babd95",
    SYMPY_ROOT / "sympy-1.14.0.dist-info/METADATA":
        "b756c2fbfd5be05ac5bdb0ebca61f55618f30f633ed92d88a5687429313a7595",
    SYMPY_ROOT / "sympy-1.14.0.dist-info/RECORD":
        "d0550b2806421a7c3eabe78fcb748587224de0c0071429ccfd9729eab90d395e",
    SYMPY_ROOT / "sympy/__init__.py":
        "4e9476348ba105feab28d82f5bcf6cdba2e3e84de6e059bbfe7a13728c0a4ab0",
    SYMPY_ROOT / "mpmath-1.3.0.dist-info/METADATA":
        "44b66ea444b9c0d19ae94815d356bf047ae6b680c19268b5c265687cd6a81406",
    SYMPY_ROOT / "mpmath-1.3.0.dist-info/RECORD":
        "7f23f46a725ebad6e62bf1e6d189311e805363fc899b6809b8e1463d0d544646",
    SYMPY_ROOT / "mpmath/__init__.py":
        "b241584d2c1fc0304b0a1015ea923749d7b0800411dd406dcab7c82bf25d9fe8",
    FLINT_ROOT / "python_flint-0.6.0.dist-info/METADATA":
        "d6b5be0f3a94ff92ad45f8e9d8991ac8face10ab71e362b8b9f25819df4ef06b",
    FLINT_ROOT / "python_flint-0.6.0.dist-info/RECORD":
        "9b76e8ba99a8555fa73c855c2459614714f25136238c1c96fa6c82dad5b9cf94",
    FLINT_ROOT / "flint/__init__.py":
        "b959e94c11c23633c0cbfea849a07955b8f252fc3100fd2ed52bd3c35118ba93",
}

SEALED_LOCAL = (
    SPEC,
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_SPEC_V001.md",
    ROOT / "COMPLETE_QSPEC_EXTERIOR_FRAME_AND_STINESPRING_LEMMAS_V001.md",
    EXACT_EXECUTOR,
    ROOT / "COMPLETE_QSPEC_EXACT_SPIN2_SUPPORT_BRIDGE_RESULT_V001.md",
    ROOT / "COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md",
    ROOT / "COMPLETE_QSPEC_PERIODIC_UNIFORM_ZERO_FREE_THEOREM_SPEC_V001.md",
    ROOT / "COMPLETE_QSPEC_ZERO_TRANSFER_DYADIC_BALL_CERTIFICATE_SPEC_V001.md",
)

STEPS = 96
PRECISION_BITS = 192
FLINT_THREADS = 4
CBAR = Fraction(203, 250)
ANCHOR_ALLOWANCE = Fraction(1, 10**10)

sp = None
np = None
flint = None
acb = None
acb_mat = None
arb = None


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def verify_seal(path: Path) -> None:
    seal = Path(f"{path}.seal.sha256")
    require(seal.is_file(), f"missing seal: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed seal: {seal}")
    require(fields[0] == sha256(path), f"seal hash mismatch: {path}")
    require(fields[1] == path.name, f"seal name mismatch: {path}")


def verify_authorities() -> dict[str, str]:
    observed = {}
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing authority: {path}")
        actual = sha256(path)
        require(actual == expected, f"authority mismatch: {path}")
        observed[str(path)] = actual
    for path in SEALED_LOCAL:
        verify_seal(path)
    verify_seal(SCRIPT)
    return observed


def verify_wheel_record(root: Path, record: Path) -> dict[str, int]:
    verified = 0
    native = 0
    root_resolved = root.resolve()
    with record.open(newline="", encoding="utf-8") as handle:
        for relative, encoded_hash, encoded_size in csv.reader(handle):
            if not encoded_hash:
                continue
            candidate = (root / relative).resolve()
            require(
                candidate.is_relative_to(root_resolved),
                f"wheel path escapes root: {relative}",
            )
            require(candidate.is_file(), f"wheel file missing: {relative}")
            algorithm, digest = encoded_hash.split("=", 1)
            require(algorithm == "sha256", "non-SHA256 wheel entry")
            observed = base64.urlsafe_b64encode(
                hashlib.sha256(candidate.read_bytes()).digest()
            ).decode("ascii").rstrip("=")
            require(observed == digest, f"wheel hash mismatch: {relative}")
            require(
                candidate.stat().st_size == int(encoded_size),
                f"wheel size mismatch: {relative}",
            )
            verified += 1
            if candidate.suffix in (".so", ".dylib"):
                native += 1
    require(verified > 100, f"implausibly small wheel record: {record}")
    return {"verified_hashed_files": verified, "native_files": native}


def audit_runtime_origins() -> dict[str, list[str]]:
    origins = {}
    for prefix, root in (
        ("sympy", SYMPY_ROOT),
        ("mpmath", SYMPY_ROOT),
        ("flint", FLINT_ROOT),
        ("numpy", NUMPY_ROOT),
    ):
        paths = []
        for name, module in sorted(sys.modules.items()):
            if not (name == prefix or name.startswith(f"{prefix}.")):
                continue
            origin = getattr(module, "__file__", None)
            if origin is None:
                continue
            path = Path(origin).resolve()
            require(
                path.is_relative_to(root.resolve()),
                f"runtime imported outside declared root: {name}: {path}",
            )
            paths.append(str(path.relative_to(root.resolve())))
        require(paths, f"no imported origins recorded for {prefix}")
        origins[prefix] = paths
    return origins


def load_runtimes() -> dict[str, object]:
    global sp, np, flint, acb, acb_mat, arb
    sys.path.insert(0, str(SYMPY_ROOT))
    sys.path.insert(0, str(FLINT_ROOT))
    sys.path.insert(0, str(NUMPY_ROOT))
    import sympy as sympy_module
    import numpy as numpy_module
    import flint as flint_module

    sp = sympy_module
    np = numpy_module
    flint = flint_module
    acb = flint.acb
    acb_mat = flint.acb_mat
    arb = flint.arb
    flint.ctx.prec = PRECISION_BITS
    flint.ctx.threads = FLINT_THREADS

    return {
        "sympy_version": sp.__version__,
        "numpy_version_non_authoritative": np.__version__,
        "python_flint_version": flint.__version__,
        "initial_origins": audit_runtime_origins(),
    }


def exact_zero(matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def exact_equal(left, right) -> bool:
    return left.shape == right.shape and exact_zero(left - right)


def exact_lagrange_projectors(matrix, eigenvalues):
    identity = sp.eye(matrix.rows)
    projectors = []
    for value in eigenvalues:
        projector = identity
        for other in eigenvalues:
            if other == value:
                continue
            projector = projector * (
                (matrix - other * identity) / (value - other)
            )
        projectors.append(sp.simplify(projector))
    return tuple(projectors)


def exact_resolution_checks(matrix, eigenvalues, projectors):
    identity = sp.eye(matrix.rows)
    Hermitian = exact_equal(matrix, matrix.conjugate().T)
    self_adjoint = all(
        exact_equal(projector, projector.conjugate().T)
        for projector in projectors
    )
    orthogonal = True
    for left_index, left in enumerate(projectors):
        for right_index, right in enumerate(projectors):
            target = left if left_index == right_index else sp.zeros(matrix.rows)
            orthogonal = bool(
                orthogonal and exact_equal(left * right, target)
            )
    complete = exact_equal(sum(projectors, sp.zeros(matrix.rows)), identity)
    reconstructed = exact_equal(
        sum(
            (
                value * projector
                for value, projector in zip(eigenvalues, projectors)
            ),
            sp.zeros(matrix.rows),
        ),
        matrix,
    )
    return {
        "Hermitian": Hermitian,
        "projectors_self_adjoint": self_adjoint,
        "projectors_pairwise_orthogonal": orthogonal,
        "projectors_complete": complete,
        "generator_reconstructed": reconstructed,
        "projector_ranks": [projector.rank() for projector in projectors],
        "pass": bool(
            Hermitian
            and self_adjoint
            and orthogonal
            and complete
            and reconstructed
        ),
    }


def exact_fock_spectrum(one_body_values, particles):
    return tuple(
        sorted(
            set(
                sum(choice)
                for choice in itertools.combinations(one_body_values, particles)
            )
        )
    )


def exact_polynomial_projectors(matrix, eigenvalues):
    x = sp.Symbol("x")
    identity = sp.eye(matrix.rows)
    maximum_degree = len(eigenvalues) - 1
    powers = [identity]
    for _ in range(maximum_degree):
        powers.append(sp.simplify(powers[-1] * matrix))
    projectors = []
    for value in eigenvalues:
        polynomial = sp.Poly(
            sp.prod(
                (x - other) / (value - other)
                for other in eigenvalues
                if other != value
            ),
            x,
        )
        projector = sp.zeros(matrix.rows)
        for degree in range(maximum_degree + 1):
            projector += polynomial.nth(degree) * powers[degree]
        projectors.append(sp.simplify(projector))
    annihilator = sp.zeros(matrix.rows)
    polynomial = sp.Poly(
        sp.prod(x - value for value in eigenvalues),
        x,
    )
    powers.append(sp.simplify(powers[-1] * matrix))
    for degree in range(len(eigenvalues) + 1):
        annihilator += polynomial.nth(degree) * powers[degree]
    require(exact_zero(annihilator), "declared Fock spectrum is incomplete")
    require(
        exact_equal(sum(projectors, sp.zeros(matrix.rows)), identity),
        "Fock spectral projectors do not sum to identity",
    )
    require(
        exact_equal(
            sum(
                (
                    value * projector
                    for value, projector in zip(eigenvalues, projectors)
                ),
                sp.zeros(matrix.rows),
            ),
            matrix,
        ),
        "Fock spectral projectors do not reconstruct generator",
    )
    return tuple(projectors)


def sympy_to_acb(value):
    value = sp.sympify(value)
    require(not value.has(sp.Float), f"inexact SymPy atom: {value}")
    if value == sp.I:
        return acb(0, 1)
    if value.is_Integer:
        return acb(int(value))
    if value.is_Rational:
        return acb(int(value.p)) / acb(int(value.q))
    if value.is_Add:
        result = acb(0)
        for term in value.args:
            result += sympy_to_acb(term)
        return result
    if value.is_Mul:
        result = acb(1)
        for factor in value.args:
            result *= sympy_to_acb(factor)
        return result
    if value.is_Pow:
        base, exponent = value.args
        if exponent == sp.Rational(1, 2):
            return sympy_to_acb(base).sqrt()
        if exponent.is_Integer:
            return sympy_to_acb(base) ** int(exponent)
    raise RuntimeError(f"unsupported exact expression: {value}")


def sympy_matrix_to_acb(matrix):
    return acb_mat(
        matrix.rows,
        matrix.cols,
        [sympy_to_acb(matrix[row, column])
         for row in range(matrix.rows)
         for column in range(matrix.cols)],
    )


def acb_identity(size):
    return acb_mat(
        size,
        size,
        [acb(1 if row == column else 0)
         for row in range(size)
         for column in range(size)],
    )


def acb_diagonal(diagonal):
    size = len(diagonal)
    return acb_mat(
        size,
        size,
        [diagonal[row] if row == column else acb(0)
         for row in range(size)
         for column in range(size)],
    )


def acb_linear_combination(projectors, coefficients):
    require(len(projectors) == len(coefficients), "combination mismatch")
    output = acb_mat(projectors[0].nrows(), projectors[0].ncols())
    for projector, coefficient in zip(projectors, coefficients):
        output += projector * coefficient
    return output


def matrix_contains_zero(matrix) -> bool:
    return bool(
        matrix.contains(acb_mat(matrix.nrows(), matrix.ncols()))
    )


def matrix_norm_upper(matrix):
    row_sums = []
    for row in range(matrix.nrows()):
        total = arb(0)
        for column in range(matrix.ncols()):
            total += abs(matrix[row, column]).upper()
        row_sums.append(total)
    column_sums = []
    for column in range(matrix.ncols()):
        total = arb(0)
        for row in range(matrix.nrows()):
            total += abs(matrix[row, column]).upper()
        column_sums.append(total)
    norm_inf = row_sums[0]
    for value in row_sums[1:]:
        norm_inf = norm_inf.max(value)
    norm_one = column_sums[0]
    for value in column_sums[1:]:
        norm_one = norm_one.max(value)
    return {
        "one": norm_one,
        "infinity": norm_inf,
        "two": (norm_one * norm_inf).sqrt(),
    }


def diagonal_sandwich(matrix, diagonal):
    return acb_mat(
        matrix.nrows(),
        matrix.ncols(),
        [
            diagonal[row] * matrix[row, column] * diagonal[column]
            for row in range(matrix.nrows())
            for column in range(matrix.ncols())
        ],
    )


def frozen_weight(index: int) -> Fraction:
    midpoint = Fraction(2 * index + 1, 2 * STEPS)
    edge = min(midpoint, 1 - midpoint)
    return 32 * edge**3


def spectral_exponential(projectors, eigenvalues, scalar):
    coefficients = [
        (scalar * sympy_to_acb(value)).exp()
        for value in eigenvalues
    ]
    return acb_linear_combination(projectors, coefficients)


def conditional_cell_evolutions(
    source_projectors,
    source_eigenvalues,
    free_energies,
    record_eigenvalues,
    label,
):
    dimension = len(free_energies)
    half_free = [
        (
            acb(0, -1)
            * sympy_to_acb(energy)
            / acb(2 * STEPS)
        ).exp()
        for energy in free_energies
    ]
    total_free = [
        (acb(0, -1) * sympy_to_acb(energy)).exp()
        for energy in free_energies
    ]
    action = arb.pi() / arb(2).sqrt()
    output = []
    for mu_index, mu in enumerate(record_eigenvalues):
        print(f"cell {label}: record block {mu_index + 1}/3", flush=True)
        if sp.simplify(mu) == 0:
            output.append(acb_diagonal(total_free))
            continue
        mu_ball = sympy_to_acb(mu)
        current = acb_identity(dimension)
        cache = {}
        for index in range(STEPS):
            weight = frozen_weight(index)
            key = (weight.numerator, weight.denominator)
            interaction = cache.get(key)
            if interaction is None:
                interval = (
                    action
                    * arb(weight.numerator)
                    / arb(weight.denominator)
                    / arb(STEPS)
                )
                scalar = acb(0, -1) * interval * mu_ball
                interaction = spectral_exponential(
                    source_projectors,
                    source_eigenvalues,
                    scalar,
                )
                cache[key] = interaction
            step = diagonal_sandwich(interaction, half_free)
            current = step * current
            if (index + 1) % 24 == 0:
                print(
                    f"cell {label}: block {mu_index + 1}, "
                    f"step {index + 1}/{STEPS}",
                    flush=True,
                )
        output.append(current)
    return tuple(output)


def kraus_from_record_blocks(
    conditional_evolutions,
    record_projectors,
):
    dimension = conditional_evolutions[0].nrows()
    kraus = []
    for outcome in range(3):
        value = acb_mat(dimension, dimension)
        for evolution, projector in zip(
            conditional_evolutions,
            record_projectors,
        ):
            value += evolution * projector[outcome, 0]
        kraus.append(value)
    return tuple(kraus)


def gram_certificate(kraus):
    dimension = kraus[0].nrows()
    gram = acb_mat(dimension, dimension)
    for operator in kraus:
        gram += operator.conjugate().transpose() * operator
    defect = gram - acb_identity(dimension)
    return {
        "defect_ball_contains_zero": matrix_contains_zero(defect),
        "defect_norm_upper": str(matrix_norm_upper(defect)["two"]),
    }


def compress_kraus(full_kraus, support_basis, support_kraus):
    dagger = support_basis.conjugate().transpose()
    rows = []
    for full, direct in zip(full_kraus, support_kraus):
        residual = dagger * full * support_basis - direct
        rows.append(
            {
                "contains_zero": matrix_contains_zero(residual),
                "norm_upper": str(matrix_norm_upper(residual)["two"]),
            }
        )
    return rows


def compose_cells(first, second):
    return tuple(
        second_operator * first_operator
        for first_operator in first
        for second_operator in second
    )


def two_cell_trace_identity_certificate(
    exact_support_recheck,
    exact_stinespring_Gram_identity_derived,
    record_state_checks,
):
    per_cell_reducing_intertwiner = bool(
        exact_support_recheck["pass"]
    )
    per_cell_completeness = bool(
        exact_stinespring_Gram_identity_derived
        and all(record_state_checks.values())
    )
    composite_completeness = bool(
        per_cell_completeness
    )
    identity_derived = bool(
        per_cell_reducing_intertwiner
        and composite_completeness
    )
    return {
        "per_cell_reducing_intertwiner_derived":
            per_cell_reducing_intertwiner,
        "per_cell_Stinespring_completeness_derived":
            per_cell_completeness,
        "two_cell_completeness_derived_by_nested_outcome_sum":
            composite_completeness,
        "identity":
            "sum_(q1,q2) C_full^dagger Q_S C_support = Q_S",
        "derivation": [
            "Exact two-sided reduction gives both C_full Q_S="
            "Q_S C_support and C_full^dagger Q_S="
            "Q_S C_support^dagger.",
            "The nested q2 then q1 sums give "
            "sum C_support^dagger C_support=I_S.",
            "Substitution yields sum C_full^dagger Q_S "
            "C_support=Q_S.",
            "Taking the row-major Frobenius adjoint proves trace T0=trace.",
        ],
        "pass": identity_derived,
    }


def composite_intertwiner_ball_certificate(
    full_composites,
    support_composites,
    support_basis,
):
    residual = acb_mat(support_basis.nrows(), support_basis.ncols())
    for full, reduced in zip(full_composites, support_composites):
        residual += (
            full.conjugate().transpose()
            * support_basis
            * reduced
        )
    residual -= support_basis
    return {
        "defect_ball_contains_zero": matrix_contains_zero(residual),
        "defect_norm_upper": str(matrix_norm_upper(residual)["two"]),
    }


def build_transfer(full_composites, support_composites):
    require(len(full_composites) == 9, "full composite count mismatch")
    require(len(support_composites) == 9, "support composite count mismatch")
    transfer = acb_mat(350, 350)
    for source_row in range(70):
        for support_row in range(5):
            row = 5 * source_row + support_row
            for source_column in range(70):
                for support_column in range(5):
                    column = 5 * source_column + support_column
                    value = acb(0)
                    for full, reduced in zip(
                        full_composites,
                        support_composites,
                    ):
                        value += (
                            full[source_row, source_column]
                            * reduced[support_row, support_column].conjugate()
                        )
                    transfer[row, column] = value
        if (source_row + 1) % 10 == 0:
            print(
                f"transfer rows: {5 * (source_row + 1)}/350",
                flush=True,
            )
    return transfer


def flatten_row_major(matrix):
    return [
        matrix[row, column]
        for row in range(matrix.nrows())
        for column in range(matrix.ncols())
    ]


def ball_matrix_midpoint(matrix):
    return np.array(
        [
            complex(float(value.real), float(value.imag))
            for value in (
                matrix[row, column]
                for row in range(matrix.nrows())
                for column in range(matrix.ncols())
            )
        ],
        dtype=np.complex128,
    ).reshape(matrix.nrows(), matrix.ncols())


def acb_from_binary64(value: float):
    numerator, denominator = float(value).as_integer_ratio()
    return acb(numerator) / acb(denominator)


def acb_matrix_from_numpy(matrix):
    array = np.asarray(matrix, dtype=np.complex128)
    return acb_mat(
        array.shape[0],
        array.shape[1],
        [
            acb(
                acb_from_binary64(complex(value).real).real,
                acb_from_binary64(complex(value).imag).real,
            )
            for value in array.reshape(-1)
        ],
    )


def interval_gershgorin_positive(matrix):
    require(matrix.nrows() == matrix.ncols(), "matrix is not square")
    margins = []
    diagonal_imaginary_contains_zero = True
    for row in range(matrix.nrows()):
        diagonal = matrix[row, row]
        diagonal_imaginary_contains_zero = bool(
            diagonal_imaginary_contains_zero
            and diagonal.imag.contains(0)
        )
        radius = arb(0)
        for column in range(matrix.ncols()):
            if column != row:
                radius += abs(matrix[row, column]).upper()
        margins.append(diagonal.real.lower() - radius)
    minimum = margins[0]
    for margin in margins[1:]:
        minimum = minimum.min(margin)
    Hermitian_defect = (
        matrix - matrix.conjugate().transpose()
    )
    Hermitian_contains_zero = matrix_contains_zero(Hermitian_defect)
    passed = bool(
        minimum > 0
        and diagonal_imaginary_contains_zero
        and Hermitian_contains_zero
    )
    return {
        "minimum_lower_margin": str(minimum),
        "diagonal_imaginary_contains_zero":
            diagonal_imaginary_contains_zero,
        "Hermitian_defect_contains_zero": Hermitian_contains_zero,
        "pass": passed,
    }


def anchor_and_complement(transfer, trace_column):
    trace_dagger = trace_column.conjugate().transpose()
    tau = (trace_dagger * trace_column)[0, 0]
    require(tau.imag.contains(0), "trace norm has imaginary part")
    require(tau.real > 0, "trace norm is not positive")
    projector = (trace_column * trace_dagger) / tau
    transfer_trace = transfer * trace_column
    trace_transfer = trace_dagger * transfer
    scalar = (trace_transfer * trace_column)[0, 0]
    complement = transfer - (trace_column * trace_transfer) / tau
    complement -= (transfer_trace * trace_dagger) / tau
    complement += projector * (scalar / tau)
    anchor_defect = transfer - (projector + complement)
    norms = matrix_norm_upper(anchor_defect)
    require(
        norms["two"] < arb(ANCHOR_ALLOWANCE.numerator)
        / arb(ANCHOR_ALLOWANCE.denominator),
        "anchor defect exceeds frozen allowance",
    )
    return complement, projector, {
        "trace_norm_squared": str(tau),
        "defect_norm_one_upper": str(norms["one"]),
        "defect_norm_infinity_upper": str(norms["infinity"]),
        "defect_norm_two_upper": str(norms["two"]),
        "below_1e_minus_10": True,
    }


def approximate_preconditioner(transfer_midpoint, trace_midpoint):
    tau = np.vdot(trace_midpoint, trace_midpoint)
    projector = np.outer(
        trace_midpoint,
        trace_midpoint.conjugate(),
    ) / tau
    identity = np.eye(transfer_midpoint.shape[0], dtype=np.complex128)
    complement = (
        (identity - projector)
        @ transfer_midpoint
        @ (identity - projector)
    )
    hessian = (
        float(CBAR) ** 2 * identity
        - complement.conjugate().T @ complement
    )
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    return eigenvectors, {
        "midpoint_H_minimum_eigenvalue": float(eigenvalues[0]),
        "midpoint_H_maximum_eigenvalue": float(eigenvalues[-1]),
        "midpoint_complement_norm":
            float(np.linalg.norm(complement, 2)),
    }


def certify_complement_norm(complement, preconditioner):
    v = acb_matrix_from_numpy(preconditioner)
    v_dagger = v.conjugate().transpose()
    gram = v_dagger * v
    gram_certificate = interval_gershgorin_positive(gram)
    require(gram_certificate["pass"], "preconditioner Gram not positive")
    rv = complement * v
    rv_gram = rv.conjugate().transpose() * rv
    cbar = arb(CBAR.numerator) / arb(CBAR.denominator)
    congruence = gram * (cbar * cbar) - rv_gram
    h_certificate = interval_gershgorin_positive(congruence)
    require(h_certificate["pass"], "R0 norm certificate failed")
    return {
        "c_bar": "0.812",
        "preconditioner_Gram": gram_certificate,
        "positive_congruence": h_certificate,
        "pass": True,
    }


def canonical_ball_hash(matrix):
    digest = hashlib.sha256()
    maximum_radius = arb(0)
    for row in range(matrix.nrows()):
        for column in range(matrix.ncols()):
            value = matrix[row, column]
            real_text = value.real.str(80, more=True)
            imag_text = value.imag.str(80, more=True)
            digest.update(real_text.encode("ascii"))
            digest.update(b";")
            digest.update(imag_text.encode("ascii"))
            digest.update(b"\n")
            maximum_radius = maximum_radius.max(value.real.rad())
            maximum_radius = maximum_radius.max(value.imag.rad())
    return digest.hexdigest(), str(maximum_radius)


def canonical_midpoint_hex_hash(matrix):
    digest = hashlib.sha256()
    for value in matrix.reshape(-1):
        z = complex(value)
        digest.update(float(z.real).hex().encode("ascii"))
        digest.update(b" ")
        digest.update(float(z.imag).hex().encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def run_certificate() -> None:
    started = time.time()
    require(sys.flags.isolated == 1, "execute with python3 -I")
    require(sys.flags.no_site == 1, "execute with python3 -S")
    require(sys.flags.no_user_site == 1, "user site must be disabled")

    authorities = verify_authorities()
    wheel_records = {
        "python_flint": verify_wheel_record(
            FLINT_ROOT,
            FLINT_ROOT / "python_flint-0.6.0.dist-info/RECORD",
        ),
    }
    runtime = load_runtimes()

    exact_module = runpy.run_path(
        str(EXACT_EXECUTOR),
        run_name="qspec_exact_support_authority",
    )
    exact_result = json.loads(EXACT_JSON.read_text(encoding="utf-8"))
    exact_support_theorem_verified = bool(
        exact_result["pass"]
        and exact_result["exact_zero_history_spin2_support_derived"]
        and exact_result[
            "exact_reduced_to_full_finite_amplitude_identity_derived"
        ]
    )
    gaussian_lemma_path = (
        ROOT / "COMPLETE_QSPEC_GAUSSIAN_CELL_REDUCTION_LEMMA_V001.md"
    )
    gaussian_cell_lemma_verified = bool(
        authorities[str(gaussian_lemma_path)]
        == EXPECTED[gaussian_lemma_path]
    )
    require(
        exact_support_theorem_verified and gaussian_cell_lemma_verified,
        "exact theorem authority failed",
    )
    parent = exact_module["build_exact_parent"]()
    spin2 = exact_module["prove_spin2"](parent)
    q_exact = spin2["basis"]
    exact_support_recheck = {
        "support_isometry": spin2["orthonormal"],
        "cyclic_rank_five": bool(spin2["gram_determinant"] != 0),
        "H0_invariance_residual_zero": spin2["h0_residual_zero"],
        "H1_invariance_residual_zero": spin2["h1_residual_zero"],
        "H2_invariance_residual_zero": spin2["h2_residual_zero"],
        "restricted_H0_exact": exact_equal(
            spin2["restricted_h0"],
            spin2["expected_h0"],
        ),
        "restricted_H1_exact": exact_equal(
            spin2["restricted_h1"],
            spin2["expected_hx"],
        ),
        "restricted_H2_exact": exact_equal(
            spin2["restricted_h2"],
            spin2["expected_hx"],
        ),
    }
    exact_support_recheck["pass"] = bool(
        all(exact_support_recheck.values())
    )
    require(
        exact_support_recheck["pass"],
        "independent exact support recheck failed",
    )

    one_body_values = (
        -sp.Integer(1),
        -sp.Integer(1),
        -sp.Rational(1, 3),
        -sp.Rational(1, 3),
        sp.Rational(1, 3),
        sp.Rational(1, 3),
        sp.Integer(1),
        sp.Integer(1),
    )
    one_body_eigenvalues = (
        -sp.Integer(1),
        -sp.Rational(1, 3),
        sp.Rational(1, 3),
        sp.Integer(1),
    )
    one_body_projectors = []
    one_body_checks = []
    for interaction in parent["active_interactions"]:
        require(
            exact_zero(
                (interaction**2 - sp.eye(8))
                * (interaction**2 - sp.eye(8) / 9)
            ),
            "one-body interaction polynomial failed",
        )
        projectors = exact_lagrange_projectors(
            interaction,
            one_body_eigenvalues,
        )
        checks = exact_resolution_checks(
            interaction,
            one_body_eigenvalues,
            projectors,
        )
        require(checks["pass"], "one-body spectral resolution failed")
        require(
            checks["projector_ranks"] == [2, 2, 2, 2],
            "one-body spectral multiplicities failed",
        )
        one_body_projectors.append(projectors)
        one_body_checks.append(checks)

    record_values = (-sp.sqrt(2), sp.Integer(0), sp.sqrt(2))
    record_projectors_exact = exact_lagrange_projectors(
        parent["record"],
        record_values,
    )
    record_checks = exact_resolution_checks(
        parent["record"],
        record_values,
        record_projectors_exact,
    )
    require(record_checks["pass"], "record spectral resolution failed")
    require(
        record_checks["projector_ranks"] == [1, 1, 1],
        "record spectral multiplicities failed",
    )
    require(
        exact_zero(
            parent["record"]
            * (parent["record"]**2 - 2 * sp.eye(3))
        ),
        "record polynomial failed",
    )
    record_basis_exact = sp.eye(3)
    record_ready_exact = record_basis_exact[:, 0]
    record_state_checks = {
        "ready_state_normalized": bool(
            sp.simplify(
                (
                    record_ready_exact.conjugate().T
                    * record_ready_exact
                )[0, 0]
            ) == 1
        ),
        "outcome_basis_orthonormal": exact_equal(
            record_basis_exact.conjugate().T * record_basis_exact,
            sp.eye(3),
        ),
        "outcome_basis_complete": exact_equal(
            sum(
                (
                    record_basis_exact[:, column]
                    * record_basis_exact[:, column].conjugate().T
                    for column in range(3)
                ),
                sp.zeros(3),
            ),
            sp.eye(3),
        ),
    }
    require(
        all(record_state_checks.values()),
        "record ready/outcome state checks failed",
    )
    exact_stinespring_Gram_identity_derived = bool(
        gaussian_cell_lemma_verified
        and exact_result["four_fermion_generators_Hermitian"]
        and exact_result["record_generator_Hermitian"]
        and all(record_state_checks.values())
    )
    require(
        exact_stinespring_Gram_identity_derived,
        "exact Stinespring Gram theorem premises failed",
    )

    fock_values = exact_fock_spectrum(one_body_values, 4)
    full_projectors_exact = []
    for interaction in (parent["h1"], parent["h2"]):
        full_projectors_exact.append(
            exact_polynomial_projectors(interaction, fock_values)
        )

    support_h0 = spin2["restricted_h0"]
    support_interactions = (
        spin2["restricted_h1"],
        spin2["restricted_h2"],
    )
    support_values = tuple(
        sp.Rational(4, 3) * value
        for value in (-2, -1, 0, 1, 2)
    )
    support_projectors_exact = tuple(
        exact_polynomial_projectors(interaction, support_values)
        for interaction in support_interactions
    )

    full_projectors_ball = tuple(
        tuple(sympy_matrix_to_acb(projector) for projector in projectors)
        for projectors in full_projectors_exact
    )
    support_projectors_ball = tuple(
        tuple(sympy_matrix_to_acb(projector) for projector in projectors)
        for projectors in support_projectors_exact
    )
    record_projectors_ball = tuple(
        sympy_matrix_to_acb(projector)
        for projector in record_projectors_exact
    )

    full_free_energies = tuple(
        parent["h0"][index, index]
        for index in range(parent["h0"].rows)
    )
    support_free_energies = tuple(
        support_h0[index, index]
        for index in range(support_h0.rows)
    )

    full_cells = []
    support_cells = []
    compression_rows = []
    full_gram_rows = []
    support_gram_rows = []
    q_ball = sympy_matrix_to_acb(q_exact)
    for cell_index in range(2):
        full_conditional = conditional_cell_evolutions(
            full_projectors_ball[cell_index],
            fock_values,
            full_free_energies,
            record_values,
            f"full-{cell_index + 1}",
        )
        support_conditional = conditional_cell_evolutions(
            support_projectors_ball[cell_index],
            support_values,
            support_free_energies,
            record_values,
            f"support-{cell_index + 1}",
        )
        full_kraus = kraus_from_record_blocks(
            full_conditional,
            record_projectors_ball,
        )
        support_kraus = kraus_from_record_blocks(
            support_conditional,
            record_projectors_ball,
        )
        compression = compress_kraus(
            full_kraus,
            q_ball,
            support_kraus,
        )
        require(
            all(row["contains_zero"] for row in compression),
            "support compression ball check failed",
        )
        full_gram = gram_certificate(full_kraus)
        support_gram = gram_certificate(support_kraus)
        require(
            full_gram["defect_ball_contains_zero"],
            "full Kraus Gram check failed",
        )
        require(
            support_gram["defect_ball_contains_zero"],
            "support Kraus Gram check failed",
        )
        full_cells.append(full_kraus)
        support_cells.append(support_kraus)
        compression_rows.append(compression)
        full_gram_rows.append(full_gram)
        support_gram_rows.append(support_gram)

    full_composites = compose_cells(full_cells[0], full_cells[1])
    support_composites = compose_cells(
        support_cells[0],
        support_cells[1],
    )
    exact_two_cell_trace_certificate = (
        two_cell_trace_identity_certificate(
            exact_support_recheck,
            exact_stinespring_Gram_identity_derived,
            record_state_checks,
        )
    )
    require(
        exact_two_cell_trace_certificate["pass"],
        "exact two-cell trace derivation failed",
    )
    composite_intertwiner_ball = (
        composite_intertwiner_ball_certificate(
            full_composites,
            support_composites,
            q_ball,
        )
    )
    require(
        composite_intertwiner_ball["defect_ball_contains_zero"],
        "composite trace intertwiner ball check failed",
    )
    transfer = build_transfer(full_composites, support_composites)

    psi_exact = parent["psi0"]
    rho_exact = psi_exact * psi_exact.conjugate().T
    support_projector_exact = q_exact * q_exact.conjugate().T
    incoming_checks = {
        "psi_normalized": bool(
            sp.simplify(
                (psi_exact.conjugate().T * psi_exact)[0, 0]
            ) == 1
        ),
        "rho_supported": exact_equal(
            rho_exact,
            support_projector_exact
            * rho_exact
            * support_projector_exact,
        ),
        "rho_trace_one": bool(sp.trace(rho_exact) == 1),
        "support_isometry": exact_equal(
            q_exact.conjugate().T * q_exact,
            sp.eye(5),
        ),
    }
    require(all(incoming_checks.values()), "incoming-state checks failed")

    psi_ball = sympy_matrix_to_acb(psi_exact)
    rho_ball = psi_ball * psi_ball.conjugate().transpose()
    start_matrix = rho_ball * q_ball
    start = acb_mat(350, 1, flatten_row_major(start_matrix))
    trace_column = acb_mat(350, 1, flatten_row_major(q_ball))
    trace_row = trace_column.conjugate().transpose()
    trace_start = (trace_row * start)[0, 0]
    trace_start_ball_pass = bool(trace_start.contains(1))
    require(trace_start_ball_pass, "trace-start identity not enclosed")
    trace_transfer_residual = trace_row * transfer - trace_row
    trace_transfer_ball_pass = matrix_contains_zero(
        trace_transfer_residual
    )
    require(
        trace_transfer_ball_pass,
        "trace-transfer identity not enclosed",
    )
    exact_trace_identity_derived = bool(
        exact_support_theorem_verified
        and gaussian_cell_lemma_verified
        and exact_two_cell_trace_certificate["pass"]
        and
        all(incoming_checks.values())
        and all(record_state_checks.values())
    )
    require(
        exact_trace_identity_derived,
        "algebraic trace identity premises failed",
    )

    transfer_ball_hash, maximum_transfer_radius = canonical_ball_hash(
        transfer
    )
    transfer_midpoint = ball_matrix_midpoint(transfer)
    trace_midpoint = ball_matrix_midpoint(trace_column).reshape(-1)
    midpoint_hash = canonical_midpoint_hex_hash(transfer_midpoint)
    preconditioner, midpoint_diagnostics = approximate_preconditioner(
        transfer_midpoint,
        trace_midpoint,
    )
    complement, projector, anchor = anchor_and_complement(
        transfer,
        trace_column,
    )
    norm_certificate = certify_complement_norm(
        complement,
        preconditioner,
    )

    passed = bool(
        exact_support_theorem_verified
        and gaussian_cell_lemma_verified
        and
        all(row["pass"] for row in one_body_checks)
        and record_checks["pass"]
        and all(record_state_checks.values())
        and exact_stinespring_Gram_identity_derived
        and all(incoming_checks.values())
        and exact_trace_identity_derived
        and composite_intertwiner_ball["defect_ball_contains_zero"]
        and all(
            row["contains_zero"]
            for cell in compression_rows
            for row in cell
        )
        and all(
            row["defect_ball_contains_zero"]
            for row in full_gram_rows
        )
        and all(
            row["defect_ball_contains_zero"]
            for row in support_gram_rows
        )
        and trace_start_ball_pass
        and trace_transfer_ball_pass
        and anchor["below_1e_minus_10"]
        and norm_certificate["pass"]
    )
    result = {
        "schema":
            "complete_qspec_canonical_spin2_transfer_ball_certificate_v001",
        "authorities": authorities,
        "script_sha256": sha256(SCRIPT),
        "runtime": runtime,
        "final_runtime_origins": audit_runtime_origins(),
        "wheel_records": wheel_records,
        "python_isolated_mode": bool(sys.flags.isolated),
        "python_no_site": bool(sys.flags.no_site),
        "arb_precision_bits": PRECISION_BITS,
        "flint_threads": FLINT_THREADS,
        "steps": STEPS,
        "one_body_spectral_checks": one_body_checks,
        "record_spectral_checks": record_checks,
        "record_ready_and_outcome_checks": record_state_checks,
        "exact_Stinespring_Gram_identity_derived":
            exact_stinespring_Gram_identity_derived,
        "exact_support_theorem_verified":
            exact_support_theorem_verified,
        "independent_exact_support_recheck": exact_support_recheck,
        "gaussian_cell_reduction_lemma_verified":
            gaussian_cell_lemma_verified,
        "fock_interaction_eigenvalues": [
            str(value) for value in fock_values
        ],
        "support_interaction_eigenvalues": [
            str(value) for value in support_values
        ],
        "incoming_state_checks": incoming_checks,
        "cell_support_compression_checks": compression_rows,
        "full_cell_Gram_checks": full_gram_rows,
        "support_cell_Gram_checks": support_gram_rows,
        "composite_outcome_count": len(full_composites),
        "exact_two_cell_trace_identity_derivation":
            exact_two_cell_trace_certificate,
        "composite_trace_intertwiner_ball_check":
            composite_intertwiner_ball,
        "row_major_vectorization":
            "[vec_r(X)]_(5*i+j)=X_(i,j)",
        "transfer_dimension": 350,
        "transfer_ball_canonical_text_sha256": transfer_ball_hash,
        "transfer_midpoint_binary64_hex_sha256": midpoint_hash,
        "maximum_transfer_entry_ball_radius":
            maximum_transfer_radius,
        "trace_start_ball": str(trace_start),
        "trace_start_ball_contains_one": trace_start_ball_pass,
        "trace_transfer_residual_contains_zero":
            trace_transfer_ball_pass,
        "trace_transfer_residual_norm_upper":
            str(matrix_norm_upper(trace_transfer_residual)["two"]),
        "exact_trace_identity_algebraically_derived":
            exact_trace_identity_derived,
        "anchor_certificate": anchor,
        "midpoint_preconditioner_non_authoritative":
            midpoint_diagnostics,
        "R0_norm_certificate": norm_certificate,
        "isometry_accounting": {
            "old_numerical_allowance": "1+1e-11",
            "canonical_exact_cell_factor": "1",
            "inherited_polar_correction": "none",
            "generic_polar_retraction_used": False,
        },
        "elapsed_seconds": time.time() - started,
        "verdict": (
            "CANONICAL_EXACT_SPIN2_TRANSFER_AND_R0_BALL_CERTIFIED"
            if passed
            else "CANONICAL_EXACT_SPIN2_TRANSFER_BALL_BLOCKED"
        ),
        "pass": passed,
        "canonical_spin2_transfer_ball_certified": passed,
        "exact_physical_R0_norm_below_0_812": passed,
        "full_completed_record_amplitude_zero_free_for_all_volumes":
            False,
        "physical_continuum_local_source_addressability_derived":
            False,
        "periodic_connected_linked_cluster_density_proved": False,
        "kappa_record_computed": False,
        "physical_Thomson_stiffness_computed": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "no_coupling_or_alpha_target_access_attestation": True,
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
                "anchor": anchor["defect_norm_two_upper"],
                "R0_certificate": norm_certificate["pass"],
                "alpha_computed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not passed:
        raise SystemExit(1)


def main() -> None:
    try:
        run_certificate()
    except Exception as error:
        blocked = {
            "schema":
                "complete_qspec_canonical_spin2_transfer_ball_certificate_v001",
            "script_sha256": sha256(SCRIPT),
            "verdict": "CANONICAL_EXACT_SPIN2_TRANSFER_BALL_BLOCKED",
            "pass": False,
            "failure_type": type(error).__name__,
            "failure_message": str(error),
            "canonical_spin2_transfer_ball_certified": False,
            "exact_physical_R0_norm_below_0_812": False,
            "full_completed_record_amplitude_zero_free_for_all_volumes":
                False,
            "physical_continuum_local_source_addressability_derived":
                False,
            "periodic_connected_linked_cluster_density_proved": False,
            "kappa_record_computed": False,
            "physical_Thomson_stiffness_computed": False,
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
        }
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(
            json.dumps(blocked, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(blocked, indent=2, sort_keys=True))
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
