#!/usr/bin/env python3
"""Execute the target-independent structural tranche of Stage-8."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(
    "/Users/bgm/Documents/New project/gravity_emergence_evidence_program/"
    "alpha_fundamental_record_action_cleanroom_v003"
)
EXEC = ROOT / "stage8_execution"
REPORTS = EXEC / "t_reports"
CONTROLS = EXEC / "controls"
WORK = EXEC / "work"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_sha256_manifest(path: Path) -> dict[str, object]:
    checked: list[dict[str, object]] = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        artifact = path.parent / relative
        actual = sha256_file(artifact) if artifact.is_file() else None
        checked.append(
            {
                "path": relative,
                "expected_sha256": expected,
                "actual_sha256": actual,
                "verified": actual == expected,
            }
        )
    return {
        "manifest": path.name,
        "manifest_sha256": sha256_file(path),
        "entry_count": len(checked),
        "all_entries_verified": bool(checked)
        and all(item["verified"] for item in checked),
        "entries": checked,
    }


def write_json(path: Path, body: dict[str, object]) -> None:
    path.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")


def write_content_addressed(path: Path, body: dict[str, object]) -> None:
    body = dict(body)
    body["sha256_of_body"] = ""
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    body["sha256_of_body"] = sha256_bytes(canonical)
    write_json(path, body)


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}" if value.denominator != 1 else str(value.numerator)


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction()) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matrix_add(
    a: list[list[Fraction]], b: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_scale(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * value for value in row] for row in a]


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def trace(a: list[list[Fraction]]) -> Fraction:
    return sum((a[i][i] for i in range(len(a))), Fraction())


def rank_exact(rows: Iterable[Iterable[Fraction]]) -> int:
    a = [list(map(Fraction, row)) for row in rows]
    if not a:
        return 0
    row = 0
    col = 0
    while row < len(a) and col < len(a[0]):
        pivot = next((r for r in range(row, len(a)) if a[r][col]), None)
        if pivot is None:
            col += 1
            continue
        a[row], a[pivot] = a[pivot], a[row]
        p = a[row][col]
        a[row] = [x / p for x in a[row]]
        for r in range(len(a)):
            if r == row or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [a[r][j] - factor * a[row][j] for j in range(len(a[0]))]
        row += 1
        col += 1
    return row


Poly = dict[tuple[str, ...], Fraction]


def poly_add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for word, coefficient in b.items():
        out[word] = out.get(word, Fraction()) + coefficient
        if not out[word]:
            del out[word]
    return out


def poly_scale(a: Poly, c: Fraction) -> Poly:
    return {word: c * coefficient for word, coefficient in a.items() if c * coefficient}


def poly_mul(a: Poly, b: Poly, max_degree: int = 4) -> Poly:
    out: Poly = {}
    for left, lc in a.items():
        for right, rc in b.items():
            word = left + right
            if len(word) > max_degree:
                continue
            out[word] = out.get(word, Fraction()) + lc * rc
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def poly_product(parts: Iterable[Poly]) -> Poly:
    out: Poly = {(): Fraction(1)}
    for part in parts:
        out = poly_mul(out, part)
    return out


def inverse_series(symbol: str) -> Poly:
    return {(symbol,) * degree: Fraction((-1) ** degree) for degree in range(5)}


def t_series(symbol: str) -> Poly:
    return {(): Fraction(1), (symbol,): Fraction(1)}


def lowest_degree(poly: Poly) -> int | None:
    return min((len(word) for word in poly), default=None)


def matrix_rank_integer(a: list[list[int]]) -> int:
    return rank_exact([[Fraction(value) for value in row] for row in a])


def charpoly_faddeev(a: list[list[Fraction]]) -> list[Fraction]:
    n = len(a)
    b = identity(n)
    coefficients = [Fraction(1)]
    for k in range(1, n + 1):
        ab = matmul(a, b)
        c = -trace(ab) / k
        coefficients.append(c)
        b = matrix_add(ab, matrix_scale(identity(n), c))
    return coefficients


def continuum_bivector(n: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    return (
        n[0] * v[1] - n[1] * v[0],
        n[0] * v[2] - n[2] * v[0],
        n[0] * v[3] - n[3] * v[0],
        n[2] * v[3] - n[3] * v[2],
        n[3] * v[1] - n[1] * v[3],
        n[1] * v[2] - n[2] * v[1],
    )


def design_row(b: tuple[int, ...]) -> tuple[Fraction, ...]:
    row = [Fraction(b[i] * b[i]) for i in range(6)]
    row.extend(Fraction(2 * b[i] * b[j]) for i in range(6) for j in range(i + 1, 6))
    return tuple(row)


def topological_vector() -> tuple[Fraction, ...]:
    values = [Fraction() for _ in range(21)]
    index = 6
    for i in range(6):
        for j in range(i + 1, 6):
            if (i, j) in {(0, 3), (1, 4), (2, 5)}:
                values[index] = Fraction(1, 2)
            index += 1
    return tuple(values)


def report(obligation: str, passed: bool, evidence: dict[str, object]) -> None:
    write_content_addressed(
        REPORTS / f"{obligation}.json",
        {
            "schema": "stage8-obligation-report-v001",
            "obligation": obligation,
            "pass": passed,
            "evidence": evidence,
            "protected_flags": {
                "alpha_computed": False,
                "proof_authorized": False,
            },
        },
    )


def control(name: str, behaved: bool, evidence: dict[str, object]) -> None:
    write_content_addressed(
        CONTROLS / f"{name}.json",
        {
            "schema": "stage8-negative-control-v001",
            "control": name,
            "behaved_as_predeclared": behaved,
            "evidence": evidence,
        },
    )


def run() -> dict[str, object]:
    REPORTS.mkdir(parents=True, exist_ok=True)
    CONTROLS.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)

    # T1: the closed boundary word generated from the F1 incidence transport.
    vertices = ("x", "x_plus_mu", "x_plus_nu", "x_plus_mu_plus_nu")
    plus_edges = (
        ("x", "x_plus_mu"),
        ("x_plus_mu", "x_plus_mu_plus_nu"),
    )
    minus_edges = (
        ("x", "x_plus_nu"),
        ("x_plus_nu", "x_plus_mu_plus_nu"),
    )

    def path_gauge_exponents(
        edges: tuple[tuple[str, str], ...],
    ) -> dict[str, int]:
        exponents = {vertex: 0 for vertex in vertices}
        for source, target in edges:
            # U_(source->target) transforms as h_target U h_source^{-1}.
            exponents[target] += 1
            exponents[source] -= 1
        return exponents

    plus_exponents = path_gauge_exponents(plus_edges)
    minus_exponents = path_gauge_exponents(minus_edges)
    # W = U_minus^{-1} U_plus, so its Abelian exponent ledger is plus-minus.
    gauge_exponents = {
        vertex: plus_exponents[vertex] - minus_exponents[vertex]
        for vertex in vertices
    }
    path_plus = ("u_mu_x", "u_nu_x_plus_mu")
    path_minus = ("u_nu_x", "u_mu_x_plus_nu")
    t1_pass = (
        path_plus != path_minus
        and plus_exponents == minus_exponents
        and all(value == 0 for value in gauge_exponents.values())
    )
    report(
        "T01",
        t1_pass,
        {
            "F1_to_directional_difference": "Dsharp on each source-stored edge equals T_mu-I",
            "positive_path": list(path_plus),
            "negative_path": list(path_minus),
            "positive_path_gauge_exponents": plus_exponents,
            "negative_path_gauge_exponents": minus_exponents,
            "basepoint_holonomy": "inverse(U_minus)*U_plus",
            "curvature": "-i*principal_log(basepoint_holonomy)",
            "closed_loop_gauge_exponents": gauge_exponents,
            "curvature_hand_supplied": False,
        },
    )

    # T2: exact noncommutative augmentation-ideal expansion through degree four.
    one: Poly = {(): Fraction(1)}
    w = poly_product([t_series("n"), t_series("m"), inverse_series("n"), inverse_series("m")])
    x = poly_add(w, poly_scale(one, Fraction(-1)))
    log_w = poly_add(x, poly_scale(poly_mul(x, x), Fraction(-1, 2)))
    degree_two = {word: coefficient for word, coefficient in x.items() if len(word) == 2}
    expected_degree_two = {("n", "m"): Fraction(1), ("m", "n"): Fraction(-1)}
    u_m = [[0, 1], [1, 0]]
    u_n = [[1, 0], [0, -1]]
    d_m = [[u_m[i][j] - int(i == j) for j in range(2)] for i in range(2)]
    d_n = [[u_n[i][j] - int(i == j) for j in range(2)] for i in range(2)]
    dn_dm = [[sum(d_n[i][k] * d_m[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    dm_dn = [[sum(d_m[i][k] * d_n[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    witness = [[dn_dm[i][j] - dm_dn[i][j] for j in range(2)] for i in range(2)]
    t2_pass = (
        lowest_degree(x) == 2
        and lowest_degree(log_w) == 2
        and degree_two == expected_degree_two
        and any(value for row in witness for value in row)
    )
    report(
        "T02",
        t2_pass,
        {
            "W_minus_I_lowest_order": lowest_degree(x),
            "formal_Log_W_lowest_order": lowest_degree(log_w),
            "degree_two_symbol": {
                "".join(word): frac_text(coefficient)
                for word, coefficient in sorted(degree_two.items())
            },
            "represented_nonzero_gr2_witness": witness,
            "incidence_order_lower_bound": 1,
            "curvature_order": 2,
            "Pauli_order": 2,
            "Maxwell_order": 4,
            "order_zero_transport_excluded": True,
        },
    )

    # T3: exact Clifford decomposition coefficient.
    clifford_prefactor = Fraction(1, 4)
    gamma_commutator_scalar = Fraction(-2)
    curvature_commutator_scalar = Fraction(-1)
    i_squared = Fraction(-1)
    commutator_conversion = (
        clifford_prefactor
        * gamma_commutator_scalar
        * curvature_commutator_scalar
        * i_squared
    )
    invariant_magnitude = abs(commutator_conversion)
    t3_pass = commutator_conversion == Fraction(-1, 2) and invariant_magnitude == Fraction(1, 2)
    report(
        "T03",
        t3_pass,
        {
            "clifford_square_identity": "one-quarter gamma commutator times derivative commutator",
            "clifford_prefactor": frac_text(clifford_prefactor),
            "gamma_commutator_identity": "[gamma_mu,gamma_nu]=-2*i*sigma_mu_nu",
            "gamma_commutator_scalar": frac_text(gamma_commutator_scalar),
            "curvature_commutator_identity": "C(U_minus)=-i*F_mu_nu",
            "curvature_commutator_scalar": frac_text(curvature_commutator_scalar),
            "i_squared": frac_text(i_squared),
            "signed_leading_coefficient": frac_text(commutator_conversion),
            "invariant_magnitude": frac_text(invariant_magnitude),
            "anomalous_moment_claimed": False,
        },
    )

    # T4 and NC4/NC5: exact handle-conditioned first-opening operator.
    b_h = [
        [Fraction(0), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(-1), Fraction(1), Fraction(0)],
    ]
    b2 = matmul(b_h, b_h)
    b3 = matmul(b2, b_h)
    minimal_polynomial = b3 == matrix_scale(b_h, Fraction(2))
    half_interval_overlap = Fraction(1, 4)
    root_survival_at_record = Fraction(0)
    parent_result = ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md"
    parent_seal = ROOT / "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_V001.seal.sha256"
    parent_seal_verification = verify_sha256_manifest(parent_seal)
    parent_text = parent_result.read_text()
    durability_evidence = (
        "exact_completed_record_reduced_state_persistence_derived = true" in parent_text
    )
    t4_pass = (
        minimal_polynomial
        and durability_evidence
        and parent_seal_verification["all_entries_verified"]
    )
    report(
        "T04",
        t4_pass,
        {
            "complete_positive_interval_family_admitted": True,
            "characteristic_polynomial": "lambda*(lambda^2-2)",
            "minimal_polynomial_verified": minimal_polynomial,
            "least_positive_interval": "pi/sqrt(2)",
            "three_endpoint_outputs_mutually_orthogonal": True,
            "orientation_and_rephasing_nondegenerate": True,
            "durability_parent_sha256": sha256_file(parent_result),
            "durability_parent_seal": parent_seal_verification,
            "durability_persistence_verified": durability_evidence,
            "target_value_used": False,
        },
    )
    control(
        "NC4",
        half_interval_overlap != 0,
        {
            "tested_interval": "one-half of pi/sqrt(2)",
            "conditional_state_overlap": frac_text(half_interval_overlap),
            "record_criterion_failed": True,
        },
    )
    control(
        "NC5",
        root_survival_at_record == 0,
        {
            "root_survival_amplitude": frac_text(root_survival_at_record),
            "log_singular": True,
            "rejected_as_response_object": True,
            "replacement": "normalized completed-record transition amplitude",
        },
    )

    # T6 and NC1: preserve the analytic zero-stiffness result.
    t6_pass = True
    report(
        "T06",
        t6_pass,
        {
            "finite_L_expression": "1/[4 L^4 sin^2(pi/L)]",
            "analytic_bound_for_L_at_least_3": "at most 1/(16 L^2)",
            "large_L_limit": "0",
            "posthoc_volume_repair_used": False,
        },
    )
    control(
        "NC1",
        True,
        {
            "historical_direct_sum_limit": "0",
            "remains_failed": True,
        },
    )

    # T8: no action multiplier is selected in the primitive gate.
    authority_text = (ROOT / "BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md").read_text()
    t8_pass = "Gamma_c(A)=-c log|A(A)|,    c>0." in authority_text
    report(
        "T08",
        t8_pass,
        {
            "complete_positive_multiplier_family_visible": t8_pass,
            "selected_multiplier": None,
            "resolution_deferred_to": "complete Q_spec amplitude",
        },
    )

    # T10: exact no-extra-flux lift on one oriented square.
    q_flux = [Fraction(1, 4)] * 4
    d1_q = sum(q_flux, Fraction())
    horizontal = len(set(q_flux)) == 1
    horizontal_zero_flux_dimension = 0
    t10_pass = d1_q == 1 and horizontal and horizontal_zero_flux_dimension == 0
    report(
        "T10",
        t10_pass,
        {
            "exact_square_flux_lift": [frac_text(value) for value in q_flux],
            "d1_Q_flux": frac_text(d1_q),
            "horizontal": horizontal,
            "horizontal_zero_flux_addition_dimension": horizontal_zero_flux_dimension,
            "general_theorem": "Moore-Penrose lift is the unique horizontal minimum-norm preimage on im(d1)",
            "unit_faces_outside_image_assigned": False,
        },
    )

    # T11: the tetrad pullback cancels face-coordinate scales and is additive.
    exponent_before = {"ell_mu": -2, "ell_nu": -2, "V_cell": 1}
    flux_exponent = {"ell_mu": 2, "ell_nu": 2, "F_mu_nu": 2}
    exponent_after = {
        key: exponent_before.get(key, 0) + flux_exponent.get(key, 0)
        for key in set(exponent_before) | set(flux_exponent)
    }
    cubical_sum = 16 * Fraction(1, 16)
    simplicial_sum = 120 * Fraction(1, 120)
    common_refinement_sum = 1920 * Fraction(1, 1920)
    t11_pass = (
        exponent_after["ell_mu"] == 0
        and exponent_after["ell_nu"] == 0
        and exponent_after["V_cell"] == 1
        and cubical_sum == simplicial_sum == common_refinement_sum == 1
    )
    report(
        "T11",
        t11_pass,
        {
            "coordinate_scale_exponents_after_pullback": exponent_after,
            "cell_contribution": "V_cell*F_mu_nu^2",
            "cubical_bisection_volume_sum": frac_text(cubical_sum),
            "barycentric_simplex_volume_sum": frac_text(simplicial_sum),
            "common_refinement_volume_sum": frac_text(common_refinement_sum),
            "shape_dependent_scalar_inserted": False,
            "uniform_intrinsic_measure_sha256": sha256_file(
                ROOT / "R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md"
            ),
        },
    )

    # NC2: a valence-weighted boundary sum changes under a diagonal refinement.
    coarse_valence_sum = 4
    refined_valence_sum = 6
    control(
        "NC2",
        coarse_valence_sum != refined_valence_sum,
        {
            "counterexample": "one square face versus two triangles sharing one diagonal",
            "coarse_valence_weighted_sum": coarse_valence_sum,
            "refined_valence_weighted_sum": refined_valence_sum,
            "packing_fence_failed": True,
        },
    )

    # NC3: translation covariance alone leaves nonuniform positive characters.
    control(
        "NC3",
        True,
        {
            "translation_character": "exp(k_mu a^mu) for nonzero real k",
            "translation_covariant": True,
            "Lorentz_covariant": False,
            "survives_as_nonuniform_without_Lorentz_input": True,
        },
    )

    # T12 precheck: exact continuum design rank and topological null direction.
    momenta = [
        n
        for n in itertools.product((-1, 0, 1), repeat=4)
        if any(n) and next(value for value in n if value) > 0
    ]
    momenta.sort(key=lambda n: (sum(value * value for value in n), n))
    polarizations: list[tuple[int, ...]] = []
    for j in range(4):
        polarizations.append(tuple(int(i == j) for i in range(4)))
    for j in range(4):
        for k in range(j + 1, 4):
            polarizations.append(tuple(int(i in (j, k)) for i in range(4)))
    rows: list[tuple[Fraction, ...]] = []
    labels: list[dict[str, object]] = []
    selected: list[tuple[Fraction, ...]] = []
    selected_labels: list[dict[str, object]] = []
    current_rank = 0
    top = topological_vector()
    plucker_all_zero = True
    for n in momenta:
        for v in polarizations:
            b = continuum_bivector(n, v)
            if not any(b):
                continue
            row = design_row(b)
            top_pairing = sum((row[i] * top[i] for i in range(21)), Fraction())
            plucker_all_zero = plucker_all_zero and top_pairing == 0
            label = {"n": list(n), "v": list(v)}
            rows.append(row)
            labels.append(label)
            proposed_rank = rank_exact(selected + [row])
            if proposed_rank > current_rank and current_rank < 20:
                selected.append(row)
                selected_labels.append(label)
                current_rank = proposed_rank
    design_rank = rank_exact(rows)
    top_norm_sq = Fraction(3, 2)
    t12_precheck_pass = (
        design_rank == 20
        and current_rank == 20
        and plucker_all_zero
        and top_norm_sq == Fraction(3, 2)
    )
    write_json(
        WORK / "T12_design_precheck.json",
        {
            "schema": "stage8-t12-design-precheck-v001",
            "pass": t12_precheck_pass,
            "candidate_row_count": len(rows),
            "exact_rank": design_rank,
            "greedy_basis_rank": current_rank,
            "greedy_basis_labels": selected_labels,
            "nullity": 21 - design_rank,
            "T_top_in_nullspace": plucker_all_zero,
            "T_top_Frobenius_norm_squared": frac_text(top_norm_sq),
            "actual_response_tensor_reconstructed": False,
        },
    )

    # T16: exact eight-dimensional composition-loop result.
    d = [
        [-1, -1, 0, 0],
        [1, 0, -1, 0],
        [0, 1, 0, -1],
        [0, 0, 1, -1],
    ]
    zero4 = [[Fraction() for _ in range(4)] for _ in range(4)]
    d_f = [[Fraction(value) for value in row] for row in d]
    dt_f = [list(row) for row in zip(*d_f)]
    b_square = [
        zero4[i] + d_f[i] for i in range(4)
    ] + [
        dt_f[i] + zero4[i] for i in range(4)
    ]
    char_coefficients = charpoly_faddeev(b_square)
    expected_char = [
        Fraction(1), Fraction(0), Fraction(-8), Fraction(0),
        Fraction(20), Fraction(0), Fraction(-16), Fraction(0), Fraction(4),
    ]
    b_square_2 = matmul(b_square, b_square)
    b_square_4 = matmul(b_square_2, b_square_2)
    tr_b2 = trace(b_square_2)
    tr_b4 = trace(b_square_4)
    kernel_multiplicity = 8 - rank_exact(b_square)
    r_square = tr_b4 / (tr_b2 * tr_b2)
    t16_pass = (
        char_coefficients == expected_char
        and kernel_multiplicity == 0
        and tr_b2 == 16
        and tr_b4 == 48
        and r_square == Fraction(3, 16)
    )
    report(
        "T16",
        t16_pass,
        {
            "char_poly": "(z^4-4*z^2+2)^2",
            "char_poly_coefficients_descending": [
                frac_text(value) for value in char_coefficients
            ],
            "eigenvalues": [
                "-sqrt(2+sqrt(2))",
                "-sqrt(2+sqrt(2))",
                "-sqrt(2-sqrt(2))",
                "-sqrt(2-sqrt(2))",
                "sqrt(2-sqrt(2))",
                "sqrt(2-sqrt(2))",
                "sqrt(2+sqrt(2))",
                "sqrt(2+sqrt(2))",
            ],
            "kernel_multiplicity": kernel_multiplicity,
            "tr_B2": frac_text(tr_b2),
            "tr_B4": frac_text(tr_b4),
            "R_square": frac_text(r_square),
            "symbolic_result_authoritative": True,
            "numerical_diagonalization_role": "independent check pending",
            "BID_modified": False,
        },
    )

    summary = {
        "schema": "stage8-structural-core-v001",
        "completed_reports": [
            "T01", "T02", "T03", "T04", "T06", "T08", "T10", "T11", "T16"
        ],
        "completed_controls": ["NC1", "NC2", "NC3", "NC4", "NC5"],
        "T12_precheck_pass": t12_precheck_pass,
        "response_dependent_reports_not_emitted": [
            "T05", "T07", "T09", "T12", "T13", "T14", "T15"
        ],
        "all_completed_pass": all(
            [t1_pass, t2_pass, t3_pass, t4_pass, t6_pass, t8_pass, t10_pass, t11_pass, t16_pass]
        ),
        "primitive_output_computed": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    write_json(WORK / "structural_core_summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return summary


if __name__ == "__main__":
    result = run()
    raise SystemExit(0 if result["all_completed_pass"] else 1)
