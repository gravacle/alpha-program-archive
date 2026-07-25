"""Independent numerical checks of the reduced source-record structure."""

from __future__ import annotations

import cmath
import importlib.util
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_source_record_generator_structure_v002.py"

I2 = ((1 + 0j, 0j), (0j, 1 + 0j))
X = ((0j, 1 + 0j), (1 + 0j, 0j))
Y = ((0j, -1j), (1j, 0j))
Z = ((1 + 0j, 0j), (0j, -1 + 0j))
PAULI = {"I": I2, "X": X, "Y": Y, "Z": Z}


def load_audit_module():
    spec = importlib.util.spec_from_file_location("source_record_v002", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load source-record structure audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def kron(left, right):
    return tuple(
        tuple(
            left[lr][lc] * right[rr][rc]
            for lc in range(len(left[0]))
            for rc in range(len(right[0]))
        )
        for lr in range(len(left))
        for rr in range(len(right))
    )


def add(left, right):
    return tuple(
        tuple(left[r][c] + right[r][c] for c in range(len(left[0])))
        for r in range(len(left))
    )


def subtract(left, right):
    return tuple(
        tuple(left[r][c] - right[r][c] for c in range(len(left[0])))
        for r in range(len(left))
    )


def multiply(left, right):
    return tuple(
        tuple(
            sum(left[r][k] * right[k][c] for k in range(len(right)))
            for c in range(len(right[0]))
        )
        for r in range(len(left))
    )


def scale(scalar, matrix):
    return tuple(
        tuple(scalar * value for value in row)
        for row in matrix
    )


def identity(size):
    return tuple(
        tuple(1 + 0j if row == column else 0j for column in range(size))
        for row in range(size)
    )


def matrix_exponential(matrix, terms=80):
    result = identity(len(matrix))
    term = identity(len(matrix))
    for order in range(1, terms):
        term = scale(1 / order, multiply(term, matrix))
        result = add(result, term)
    return result


def dagger(matrix):
    return tuple(
        tuple(matrix[c][r].conjugate() for c in range(len(matrix)))
        for r in range(len(matrix[0]))
    )


def flatten_pair(left, right):
    return [
        component
        for matrix in (left, right)
        for row in matrix
        for value in row
        for component in (value.real, value.imag)
    ]


def numeric_rank(columns, tolerance=1e-10):
    rows = [list(row) for row in zip(*columns)]
    pivot_row = 0
    rank = 0
    for column in range(len(columns)):
        candidate = max(
            range(pivot_row, len(rows)),
            key=lambda row: abs(rows[row][column]),
            default=pivot_row,
        )
        if pivot_row >= len(rows) or abs(rows[candidate][column]) <= tolerance:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            rows[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        rank += 1
        if pivot_row == len(rows):
            break
    return rank


def test_independent_full_domain_ranks() -> None:
    products = [kron(PAULI[a], PAULI[b]) for a, b in itertools.product(PAULI, repeat=2)]
    z_source = kron(Z, I2)
    z_record = kron(I2, Z)
    odd_columns = [
        flatten_pair(
            add(multiply(operator, z_source), multiply(z_source, operator)),
            add(multiply(operator, z_record), multiply(z_record, operator)),
        )
        for operator in products
    ]
    if numeric_rank(odd_columns) != 12:
        raise AssertionError("Independent odd-map rank is not 12")

    odd_basis = [kron(X, X), kron(X, Y), kron(Y, X), kron(Y, Y)]
    z_total = add(z_source, z_record)
    conserved_columns = [
        flatten_pair(
            subtract(multiply(operator, z_total), multiply(z_total, operator)),
            ((0j,),),
        )[:-2]
        for operator in odd_basis
    ]
    if numeric_rank(conserved_columns) != 2:
        raise AssertionError("Independent restricted commutator rank is not 2")


def test_record_rephasing_rotates_exchange_plane() -> None:
    e1 = add(kron(X, X), kron(Y, Y))
    e2 = subtract(kron(X, Y), kron(Y, X))
    theta = cmath.pi / 2
    u_record = (
        (cmath.exp(-0.5j * theta), 0j),
        (0j, cmath.exp(0.5j * theta)),
    )
    u = kron(I2, u_record)
    rotated = multiply(multiply(u, e1), dagger(u))
    max_error = max(
        abs(rotated[r][c] - e2[r][c])
        for r in range(4)
        for c in range(4)
    )
    if max_error > 1e-12:
        raise AssertionError("Record rephasing does not rotate E1 into E2")


def test_first_transfer_propagator_on_all_basis_states() -> None:
    e1 = add(kron(X, X), kron(Y, Y))
    normalized_generator = scale(0.5, e1)
    angle = cmath.pi / 2
    propagator = matrix_exponential(
        scale(-1j * angle, normalized_generator)
    )
    expected_columns = (
        (1 + 0j, 0j, 0j, 0j),
        (0j, 0j, -1j, 0j),
        (0j, -1j, 0j, 0j),
        (0j, 0j, 0j, 1 + 0j),
    )
    actual_columns = tuple(
        tuple(propagator[row][column] for row in range(4))
        for column in range(4)
    )
    max_column_error = max(
        abs(actual_columns[column][row] - expected_columns[column][row])
        for column in range(4)
        for row in range(4)
    )
    if max_column_error > 1e-12:
        raise AssertionError(
            "Exponentiated generator has wrong first-transfer basis action"
        )
    unitary = multiply(dagger(propagator), propagator)
    max_unitarity_error = max(
        abs(unitary[row][column] - identity(4)[row][column])
        for row in range(4)
        for column in range(4)
    )
    if max_unitarity_error > 1e-12:
        raise AssertionError("First-transfer propagator is not unitary")


def test_fail_closed_result_scope_and_optimized_require() -> None:
    module = load_audit_module()
    result = module.build_result()
    if result["minimal_product_carrier_derived"] is not False:
        raise AssertionError("Reduced carrier promoted to derived")
    if result["complete_closure_operator_space_dimension_derived"] is not False:
        raise AssertionError("Reduced dimension promoted to full closure")
    if result["combined_grading_conservation_derived"] is not False:
        raise AssertionError("Conditional conservation promoted to derived")
    if result["source_mass_derived"] is not False:
        raise AssertionError("Source mass promoted prematurely")
    if result["spectral_evaluation_authorized"] is not False:
        raise AssertionError("Spectral evaluation promoted prematurely")
    if result["alpha_computed"] is not False:
        raise AssertionError("Alpha promoted prematurely")
    if result["proof_authorized"] is not False:
        raise AssertionError("Proof promoted prematurely")
    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")
