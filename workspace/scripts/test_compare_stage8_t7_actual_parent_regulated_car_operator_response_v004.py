#!/usr/bin/env python3
"""Synthetic fence tests for the Stage-8 T7 bundle comparator (v004).

v004 successor authorized by
STAGE8_T7_MANIFEST_BINDING_BRIDGE_AMENDMENT_V001.md (A2 item 3).  Ports
every v003 fence test against the v004 comparator and adds the enumerated
new material:

- MANIFEST-BINDING BRIDGE FIXTURES (A1): setUp now creates BOTH a
  bundle-side sealed manifest at a fixture canonical-v001 path (the
  manifest fixture bundles stamp, patched over
  COMPARATOR.BUNDLE_BINDING_MANIFEST) and the comparator-side own
  manifest, with consistent executor authority rows and with launcher
  rows at DIFFERENT paths (mirroring the real sealed manifests, where the
  v001-path manifest carries the v002 launcher and the comparator's own
  manifest carries the v003 launcher — the bridge must not require
  launcher-row equality across manifests, which no authorized production
  pair could satisfy).
- BRIDGE NEGATIVES: a bundle stamping the comparator's OWN manifest
  digest (the v003 rule) must now BLOCK; mismatched executor authority
  rows between the two manifests must BLOCK; a broken bundle-binding
  seal must BLOCK.
- FIX-2 TEST (re-audit MAJOR): one test drives the REAL production
  reconstruction oracle end-to-end — NO monkeypatch — with the
  strengthened surrogate (typed alpha_stack/S_n copied verbatim from the
  comparator source, exact ladder-formula p, h0 = sum_j kron(p_j,
  alpha_j), M_stack = 0, constant fabricated B_stack, closed-form eigh
  propagators) and asserts the gate BLOCKS specifically on the M/B
  quadrature comparison — not on alpha, S_n, p, h0, or lineage.  This
  test executes the real Hermite/causal-ball/b_D quadrature
  reconstruction at production dimensions (it takes seconds; that is the
  point — the load-bearing code finally executes in the suite) and
  subsumes the wrong-quadrature negative for the production oracle.

The v003 material below is otherwise ported unchanged.  v003 was
authorized by STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_
V002.md (S1 item 4); it ports every v002 fence test and adds the
mandatory new negatives:

- SURROGATE-PAIR TEST (the audit's missing class): a fully self-consistent
  surrogate bundle pair (zero M, constant diagonal B, diagonal p/alpha,
  closed-form exponential propagators with NO ODE integration, per the
  auditor's reproduced exploit) MUST BLOCK on the piece-reconstruction
  gate;
- a wrong-quadrature piece set (correct construction, wrong declared rule)
  MUST BLOCK;
- basis_overlap_key != the pinned literal MUST BLOCK;
- an untied diag_connection MUST BLOCK;
- the new required receipt-digest CLI inputs are enforced and recorded.

GENUINE-FIXTURE PASS TESTS ARE REBUILT PER THE BINDING'S EXPLICIT
INSTRUCTION: real Hermite/causal-ball/b_D construction at fixture scale is
not possible on the 8-dimensional spatial fixture carrier, so setUp
MONKEYPATCHES the comparator's piece-reconstruction oracle
(typed_alpha_and_incidence / reconstruct_spatial_momenta /
reconstruct_cell_and_bump) with a labeled fixture oracle whose values the
fixture bundles store.  The patch is restored in tearDown, and
test_production_oracle_blocks_synthetic_pieces proves that WITHOUT the
patch the same fixture blocks — no test demonstrates arbitrary pieces
passing the production gate.

Fixture bundles live only in temporary directories; the canonical workspace
is never written.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import numpy as np


SCRIPT = (
    Path(__file__).resolve().parent
    / "compare_stage8_t7_actual_parent_regulated_car_operator_response_v004.py"
)
MODULE_SPEC = importlib.util.spec_from_file_location("stage8_t7_comparator_v004", SCRIPT)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError("unable to load comparator module")
COMPARATOR = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = COMPARATOR
MODULE_SPEC.loader.exec_module(COMPARATOR)

# These unit tests may run either under the sealed v003 launcher (which
# installs the real attestation marker) or under a bare interpreter.  In the
# latter case, install a fixture attestation carrying the exact honesty flags
# the comparator requires, bound to the real v003 launcher file hash so the
# fixture manifest row matches.  Under a sealed launcher the real marker is
# used unchanged.
V003_LAUNCHER = COMPARATOR.ROOT / COMPARATOR.RUNTIME_LAUNCHER_PATH
if not hasattr(sys, COMPARATOR.RUNTIME_MARKER):
    setattr(
        sys,
        COMPARATOR.RUNTIME_MARKER,
        {
            "schema": "stage8_t7_content_addressed_runtime_attestation_v001",
            "launcher_sha256": hashlib.sha256(
                V003_LAUNCHER.read_bytes()
            ).hexdigest(),
            "runtime_manifest_sha256": COMPARATOR.RUNTIME_MANIFEST_SHA256,
            "python_isolated": True,
            "python_no_site": True,
            "python_standard_library_trusted_host_boundary": True,
            "accelerate_framework_trusted_host_boundary": True,
            "loaded_native_dependencies_content_addressed": False,
            "malicious_interpreter_or_kernel_resistance_claimed": False,
            "fixture_attestation_for_unit_tests_only": True,
        },
    )

# Fixture receipt digests for the S1-1d recording gate: arbitrary fixed
# hex64 values (the comparator records them verbatim; the controller, not
# the comparator, authenticates them against its sealed receipts).
FIXTURE_INDEPENDENT_RECEIPT_SHA256 = "1a" * 32
FIXTURE_PRIMARY_RECEIPT_SHA256 = "2b" * 32

PROTECTED_FLAG_NAMES = (
    "actual_parent_regulated_CAR_operator_response_derived",
    "actual_parent_same_carrier_one_source_restriction_derived",
    "route1_special_case_reexecution_passed",
    "actual_finite_parent_state_evaluation_derived",
    "actual_finite_parent_operator_to_scalar_bridge_derived",
    "kappa_record_computed",
    "coupling_evaluation_authorized",
    "alpha_computed",
    "proof_authorized",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def typed_envelope(time: float) -> float:
    return (math.pi / math.sqrt(2.0)) * 32.0 * min(time, 1.0 - time) ** 3


def exp_hermitian(operator: np.ndarray, interval: float) -> np.ndarray:
    hermitian = 0.5 * (operator + operator.conjugate().T)
    values, vectors = np.linalg.eigh(hermitian)
    return (
        vectors
        @ np.diag(np.exp(-1j * interval * values))
        @ vectors.conjugate().T
    )


def synthetic_pieces() -> dict[str, Any]:
    """Deterministic small Hermitian generator pieces (no randomness)."""
    ladder = np.zeros((8, 8), dtype=complex)
    for index in range(7):
        ladder[index, index + 1] = 1.0
    pauli_x = np.array([[0, 1], [1, 0]], dtype=complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    pauli_z = np.array([[1, 0], [0, -1]], dtype=complex)
    identity_2 = np.eye(2, dtype=complex)
    alpha_stack = np.stack(
        [
            np.kron(pauli_x, identity_2),
            np.kron(pauli_y, identity_2),
            np.kron(pauli_z, identity_2),
        ]
    )
    incidence = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)
    base_p_stack = np.stack(
        [
            0.05 * (ladder + ladder.conjugate().T),
            0.04 * 1j * (ladder - ladder.conjugate().T),
            0.03 * np.diag(np.linspace(-1.0, 1.0, 8)).astype(complex),
        ]
    )
    envelope_vector = np.cos(0.9 * np.arange(8))
    cell_matrix = (
        0.003 * np.outer(envelope_vector, envelope_vector)
        + 0.003 * np.diag(np.linspace(0.2, 1.0, 8))
    ).astype(complex)
    bump_matrix = (
        0.05 * (ladder + ladder.conjugate().T)
        + 0.02 * np.diag(np.linspace(1.0, 2.0, 8))
    ).astype(complex)
    return {
        "alpha_stack": alpha_stack,
        "incidence": incidence,
        "base_p_stack": base_p_stack,
        "cell_matrix": cell_matrix,
        "bump_matrix": bump_matrix,
    }


def surrogate_pieces() -> dict[str, Any]:
    """The auditor's surrogate-pair exploit shape (audit Blocking 1): zero
    cell matrix M, constant diagonal connection B, diagonal p and alpha, so
    every generator is diagonal, every internal identity holds exactly, and
    closed-form exponential "propagators" satisfy the lineage gate with NO
    ODE integration and no contact with the sealed Galerkin parent."""
    return {
        "alpha_stack": np.stack(
            [
                np.diag([1.0, -1.0, 1.0, -1.0]).astype(complex),
                np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex),
                np.diag([1.0, -1.0, -1.0, 1.0]).astype(complex),
            ]
        ),
        "incidence": np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex),
        "base_p_stack": np.stack(
            [
                0.05 * np.diag(np.linspace(-1.0, 1.0, 8)).astype(complex),
                0.04 * np.diag(np.linspace(1.0, -1.0, 8)).astype(complex),
                0.03 * np.diag(np.linspace(-0.5, 0.5, 8)).astype(complex),
            ]
        ),
        "cell_matrix": np.zeros((8, 8), dtype=complex),
        "bump_matrix": 0.4 * np.diag(np.linspace(0.5, 1.5, 8)).astype(complex),
    }


def strengthened_pieces() -> dict[str, Any]:
    """FIX-2 strengthened surrogate (re-audit MAJOR; amendment A2 item 3):
    the surrogate that matters against the REAL production oracle.  The
    typed alpha_stack and S_n are copied VERBATIM from the comparator
    source (typed_alpha_and_incidence), so the first two production checks
    pass identically; p is built by the exact ladder formula per ell (in
    the fixture below), so the p and h0 checks pass; M_stack is zero and
    B_stack is a constant fabricated Hermitian matrix, so every generator
    is time independent and closed-form eigh propagators satisfy the
    lineage gate with no ODE integration.  Only the untested M/B
    quadrature comparison can reject this bundle."""
    alpha_stack = np.array(
        [
            [
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0],
            ],
            [
                [0, 0, 0, -1j],
                [0, 0, 1j, 0],
                [0, -1j, 0, 0],
                [1j, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 0, -1],
                [1, 0, 0, 0],
                [0, -1, 0, 0],
            ],
        ],
        dtype=complex,
    )
    incidence = np.array(
        [
            [0, 0, -1j, 0],
            [0, 0, 0, -1j],
            [1j, 0, 0, 0],
            [0, 1j, 0, 0],
        ],
        dtype=complex,
    )
    bump = 0.35 * np.diag(np.linspace(0.4, 1.8, 8)).astype(complex)
    bump[0, 7] = bump[7, 0] = 0.02
    return {
        "alpha_stack": alpha_stack,
        "incidence": incidence,
        "bump_matrix": bump,
    }


def strengthened_ladder_momenta(ell_value: float) -> np.ndarray:
    """The exact ladder formula p = i (a_dagger - a) / (sqrt(2) ell) on the
    n=2 Hermite basis, lifted to the canonical spatial product order —
    written here verbatim so the production reconstruction finds zero
    residual and the block cannot land on the p or h0 checks."""
    one_dimensional = np.zeros((2, 2), dtype=complex)
    one_dimensional[1, 0] = 1j * math.sqrt(1) / (math.sqrt(2.0) * ell_value)
    one_dimensional[0, 1] = -1j * math.sqrt(1) / (math.sqrt(2.0) * ell_value)
    identity = np.eye(2, dtype=complex)
    return np.stack(
        [
            np.kron(np.kron(one_dimensional, identity), identity),
            np.kron(np.kron(identity, one_dimensional), identity),
            np.kron(np.kron(identity, identity), one_dimensional),
        ]
    )


def ell_scale(ell_index: int) -> float:
    return 1.0 + 0.1 * ell_index


def fixture_reconstruction_oracle(fixture: "FixtureData") -> tuple[Any, Any, Any]:
    """LABELED FIXTURE ORACLE FOR MONKEYPATCHING ONLY (repair binding V002
    S1 item 4): real Hermite/causal-ball/b_D construction at fixture scale
    is not possible on the 8-dimensional spatial fixture carrier, so the
    genuine-fixture PASS tests substitute this oracle for the comparator's
    production piece-reconstruction oracle.  It returns exactly the values
    the fixture bundles store, keyed by the comparator's typed ell values
    and quadrature declarations, so the piece-authenticity gate logic (not
    the sealed constructions themselves) is exercised.  Production runs
    never see this oracle."""

    def ell_index_for(ell_value: float) -> int:
        for index, label in enumerate(("ell0", "ell1")):
            if abs(ell_value - COMPARATOR.EXPECTED_ELL_VALUES[label]) <= 1e-9:
                return index
        raise AssertionError(f"unexpected oracle ell value: {ell_value}")

    def patched_typed_alpha_and_incidence() -> tuple[np.ndarray, np.ndarray]:
        return (
            fixture.pieces["alpha_stack"].copy(),
            fixture.pieces["incidence"].copy(),
        )

    def patched_reconstruct_spatial_momenta(ell_value: float) -> np.ndarray:
        return (
            fixture.pieces["base_p_stack"] / ell_scale(ell_index_for(ell_value))
        ).astype(complex)

    def patched_reconstruct_cell_and_bump(
        time: float,
        ell_value: float,
        quadrature: tuple[int, int, int],
    ) -> tuple[np.ndarray, np.ndarray]:
        return fixture.cell_and_bump(time, ell_index_for(ell_value), quadrature)

    return (
        patched_typed_alpha_and_incidence,
        patched_reconstruct_spatial_momenta,
        patched_reconstruct_cell_and_bump,
    )


def integrate_propagator(
    h0: np.ndarray,
    stacks: dict[str, np.ndarray],
    pieces: dict[str, Any],
    record_value: float,
    history: float,
) -> np.ndarray:
    """Genuine midpoint product integrator, written independently of the
    comparator implementation: an explicit chronological per-step loop."""
    times = stacks["times"]
    steps = len(times)
    dt = 1.0 / steps
    value = np.eye(32, dtype=complex)
    for index in range(steps):
        time = float(times[index])
        hamiltonian = (
            h0
            + record_value
            * typed_envelope(time)
            * np.kron(stacks["m_stack"][index], pieces["incidence"])
            - history * np.kron(stacks["b_stack"][index], pieces["alpha_stack"][0])
        )
        value = exp_hermitian(hamiltonian, dt) @ value
    return value


class FixtureData:
    """Class-level cache of the synthetic fixtures (each variant built once).

    variant "genuine": deterministic Hermitian pieces with genuinely
    midpoint-integrated propagators (the v002 fixture, made
    quadrature-aware so the labeled fixture oracle can reproduce it).
    variant "surrogate": the auditor's self-consistent surrogate-pair
    exploit with closed-form exponential propagators and no integration.
    variant "strengthened": the FIX-2 surrogate against the REAL
    production oracle — verbatim typed alpha/S_n, exact ladder p, exact
    assembled h0, zero M_stack, constant fabricated B_stack, closed-form
    eigh propagators (amendment A2 item 3).
    """

    _instances: dict[str, "FixtureData"] = {}

    @classmethod
    def instance(cls, variant: str = "genuine") -> "FixtureData":
        if variant not in cls._instances:
            cls._instances[variant] = cls(variant)
        return cls._instances[variant]

    def cell_and_bump(
        self,
        time: float,
        ell_index: int,
        quadrature: tuple[int, int, int],
    ) -> tuple[np.ndarray, np.ndarray]:
        """Fixture stand-in for the sealed M(t)/B(t) constructions.  The
        genuine variant carries a small quadrature-rule-dependent term so a
        piece set computed under the WRONG declared rule differs from the
        declared-rule value at ~2e-7 (far above the 2e-11/5e-11 pins, far
        below every other tolerance), mirroring how the production oracle
        distinguishes the two sealed quadrature rules."""
        scale = ell_scale(ell_index)
        if self.variant == "strengthened":
            # FIX-2 surrogate: zero cell matrix, constant fabricated bump
            # matrix, independent of time, ell, and declared rule.
            zero = np.zeros((8, 8), dtype=complex)
            return zero, self.pieces["bump_matrix"].astype(complex)
        if self.variant == "surrogate":
            zero = np.zeros((8, 8), dtype=complex)
            return zero, (scale * self.pieces["bump_matrix"]).astype(complex)
        quadrature_shift = (float(sum(quadrature)) - 40.0) * 2.5e-8
        cell = (
            scale
            * (math.sin(math.pi * time) ** 2 + quadrature_shift)
            * self.pieces["cell_matrix"]
        )
        bump = (
            scale
            * (math.sin(math.pi * time) + quadrature_shift)
            * self.pieces["bump_matrix"]
        )
        return cell.astype(complex), bump.astype(complex)

    def build_time_stacks(
        self,
        steps: int,
        ell_index: int,
        quadrature: tuple[int, int, int],
    ) -> dict[str, np.ndarray]:
        times = (np.arange(steps, dtype=np.float64) + 0.5) / steps
        cells: list[np.ndarray] = []
        bumps: list[np.ndarray] = []
        for time in times:
            cell, bump = self.cell_and_bump(float(time), ell_index, quadrature)
            cells.append(cell)
            bumps.append(bump)
        return {
            "times": times,
            "m_stack": np.stack(cells),
            "b_stack": np.stack(bumps),
        }

    def closed_form_surrogate_propagator(
        self,
        h0: np.ndarray,
        ell_index: int,
        history: float,
    ) -> np.ndarray:
        """The exploit's closed form: with zero M and constant diagonal B,
        every generator commutes, so U = exp(-i (h0 - a kron(B, alpha_x)))
        exactly — a few diagonal exponentials, no ODE integration."""
        connection = -np.kron(
            (ell_scale(ell_index) * self.pieces["bump_matrix"]).astype(complex),
            self.pieces["alpha_stack"][0],
        )
        generator = h0 + history * connection
        return np.diag(np.exp(-1j * np.diag(generator).real))

    def closed_form_strengthened_propagator(
        self,
        h0: np.ndarray,
        history: float,
    ) -> np.ndarray:
        """FIX-2 closed form: with M_stack = 0 and a CONSTANT B_stack the
        generator h(t) = h0 - a kron(B, alpha_x) is time independent, so
        the exact chronological propagator is one Hermitian eigh
        exponential — no ODE integration ever runs, yet the lineage gate
        is satisfied exactly."""
        connection = -np.kron(
            self.pieces["bump_matrix"], self.pieces["alpha_stack"][0]
        )
        return exp_hermitian(h0 + history * connection, 1.0)

    def __init__(self, variant: str = "genuine") -> None:
        self.variant = variant
        self.overlap = COMPARATOR.expected_basis_overlap()
        record = np.array(
            [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
            dtype=complex,
        )
        self.record_values, vectors = np.linalg.eigh(record)
        self.record_projectors = {
            f"l{index}": np.outer(
                vectors[:, index],
                vectors[:, index].conjugate(),
            )
            for index in range(3)
        }
        ready = np.array([1.0, 0.0, 0.0], dtype=complex)
        pointer = np.array([0.0, 1.0, 0.0], dtype=complex)
        self.probabilities = np.asarray(
            [
                np.vdot(ready, self.record_projectors[f"l{index}"] @ ready)
                for index in range(3)
            ]
        )
        self.pointer_weights = np.asarray(
            [
                np.vdot(pointer, self.record_projectors[f"l{index}"] @ ready)
                for index in range(3)
            ]
        )
        self.history_values = (0.0, 0.07, -0.11, 0.13, 0.04)
        if variant == "surrogate":
            self.pieces = surrogate_pieces()
        elif variant == "strengthened":
            self.pieces = strengthened_pieces()
        else:
            self.pieces = synthetic_pieces()
        self.p_stacks: dict[str, np.ndarray] = {}
        self.h0: dict[str, np.ndarray] = {}
        self.stacks: dict[tuple[str, str], dict[str, np.ndarray]] = {}
        self.propagators: dict[tuple[str, str, int, int], np.ndarray] = {}
        for ell_index, ell in enumerate(("ell0", "ell1")):
            if variant == "strengthened":
                # Exact ladder formula at the comparator's own typed ell
                # values, so the production p/h0 checks find zero residual.
                p_stack = strengthened_ladder_momenta(
                    COMPARATOR.EXPECTED_ELL_VALUES[ell]
                )
            else:
                p_stack = (
                    self.pieces["base_p_stack"] / ell_scale(ell_index)
                ).astype(complex)
            self.p_stacks[ell] = p_stack
            self.h0[ell] = sum(
                np.kron(p_stack[j], self.pieces["alpha_stack"][j])
                for j in range(3)
            )
            for lane, steps in (("primary", 48), ("independent", 384)):
                stacks = self.build_time_stacks(
                    steps, ell_index, COMPARATOR.LANE_QUADRATURES[lane]
                )
                self.stacks[lane, ell] = stacks
                for history_index, history in enumerate(self.history_values):
                    for record_index, record_value in enumerate(
                        self.record_values
                    ):
                        if variant == "surrogate":
                            propagator = self.closed_form_surrogate_propagator(
                                self.h0[ell], ell_index, float(history)
                            )
                        elif variant == "strengthened":
                            propagator = (
                                self.closed_form_strengthened_propagator(
                                    self.h0[ell], float(history)
                                )
                            )
                        else:
                            propagator = integrate_propagator(
                                self.h0[ell],
                                stacks,
                                self.pieces,
                                float(record_value),
                                float(history),
                            )
                        self.propagators[
                            lane, ell, history_index, record_index
                        ] = propagator
        self.lane_matrices = {
            lane: self.build_lane_matrices(lane)
            for lane in ("primary", "independent")
        }

    def build_lane_matrices(self, lane: str) -> dict[str, dict[str, np.ndarray]]:
        """Canonical-convention matrix categories derived from the genuinely
        integrated propagators of the given lane grid."""
        result: dict[str, dict[str, np.ndarray]] = {
            category: {} for category in COMPARATOR.MATRIX_CATEGORIES
        }
        result["record_projectors"] = {
            key: value.copy() for key, value in self.record_projectors.items()
        }
        pair_indices = ((0, 0), (1, 2), (3, 4))
        for ell in ("ell0", "ell1"):
            propagators: dict[tuple[int, int], np.ndarray] = {}
            kraus: dict[tuple[int, int], np.ndarray] = {}
            for history_index in range(len(self.history_values)):
                for record_index in range(3):
                    propagator = self.propagators[
                        lane, ell, history_index, record_index
                    ]
                    propagators[history_index, record_index] = propagator
                    result["propagators"][
                        f"{ell}.a{history_index}.l{record_index}"
                    ] = propagator
                for outcome in range(3):
                    member = sum(
                        self.record_projectors[f"l{record_index}"][outcome, 0]
                        * propagators[history_index, record_index]
                        for record_index in range(3)
                    )
                    kraus[history_index, outcome] = member
                    result["direct_kraus_members"][
                        f"{ell}.a{history_index}.x{outcome}"
                    ] = member
            for pair_index, (plus, minus) in enumerate(pair_indices):
                cross: dict[tuple[int, int], np.ndarray] = {}
                for left in range(3):
                    for right in range(3):
                        matrix = (
                            propagators[minus, left].conjugate().T
                            @ propagators[plus, right]
                        )
                        cross[left, right] = matrix
                        result["cross_operators"][
                            f"{ell}.p{pair_index}.mu{left}.l{right}"
                        ] = matrix
                aggregate_all = sum(
                    self.probabilities[index] * cross[index, index]
                    for index in range(3)
                )
                aggregate_pointer = sum(
                    self.pointer_weights[left].conjugate()
                    * self.pointer_weights[right]
                    * cross[left, right]
                    for left in range(3)
                    for right in range(3)
                )
                direct_all = sum(
                    kraus[minus, outcome].conjugate().T
                    @ kraus[plus, outcome]
                    for outcome in range(3)
                )
                direct_pointer = (
                    kraus[minus, 1].conjugate().T @ kraus[plus, 1]
                )
                for kernel, aggregate, direct in (
                    ("all", aggregate_all, direct_all),
                    ("pointer", aggregate_pointer, direct_pointer),
                ):
                    identifier = f"{ell}.p{pair_index}.{kernel}"
                    result["aggregate_kernels"][identifier] = aggregate
                    result["direct_responses"][identifier] = direct
        return result


class ComparatorFenceTests(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = FixtureData.instance()

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        implementation_files = (
            COMPARATOR.EXECUTOR_PATHS["primary"],
            COMPARATOR.EXECUTOR_PATHS["independent"],
            COMPARATOR.RUNTIME_LAUNCHER_PATH,
            "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v004.py",
            "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_response_v004.py",
        )
        implementation_manifest = self.root / "implementation.json"
        implementation_manifest.write_text(
            json.dumps(
                {
                    "schema": "stage8_t7_actual_parent_car_implementation_test_v004",
                    "files": [
                        {
                            "path": relative,
                            "sha256": sha256(COMPARATOR.ROOT / relative),
                        }
                        for relative in implementation_files
                    ],
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        implementation_seal = self.root / "implementation.json.seal.sha256"
        implementation_seal.write_text(
            f"{sha256(implementation_manifest)}  {implementation_manifest.name}\n",
            encoding="ascii",
        )
        COMPARATOR.IMPLEMENTATION_MANIFEST = implementation_manifest
        COMPARATOR.IMPLEMENTATION_SEAL = implementation_seal
        self.implementation_manifest_sha256 = sha256(implementation_manifest)
        self.implementation_rows = {
            row["path"]: row["sha256"]
            for row in json.loads(
                implementation_manifest.read_text(encoding="utf-8")
            )["files"]
        }
        # A1 manifest-binding bridge fixture: the bundle-side sealed
        # manifest at a fixture canonical-v001 path.  Its executor
        # authority rows are consistent with the comparator-side manifest
        # above; its launcher row sits at a DIFFERENT path (the sealed
        # v002 launcher), mirroring the real sealed pair — the bridge must
        # accept this shape, because the real v001-path manifest predates
        # the v003 launcher.
        self.bridge_rows = {
            COMPARATOR.EXECUTOR_PATHS["primary"]: self.implementation_rows[
                COMPARATOR.EXECUTOR_PATHS["primary"]
            ],
            COMPARATOR.EXECUTOR_PATHS["independent"]: self.implementation_rows[
                COMPARATOR.EXECUTOR_PATHS["independent"]
            ],
            "scripts/launch_stage8_t7_content_addressed_runtime_v002.py":
                sha256(
                    COMPARATOR.ROOT
                    / "scripts/launch_stage8_t7_content_addressed_runtime_v002.py"
                ),
        }
        self.bridge_manifest_sha256 = self.write_bridge_manifest(
            self.bridge_rows
        )
        self.output = self.root / "comparison.json"
        fixture = self.fixture
        self.overlap = fixture.overlap
        self.record_values = fixture.record_values
        self.record_projectors = fixture.record_projectors
        self.probabilities = fixture.probabilities
        self.pointer_weights = fixture.pointer_weights
        self.history_values = fixture.history_values
        # MONKEYPATCH THE PIECE-RECONSTRUCTION ORACLE (repair binding V002
        # S1 item 4, explicit instruction): the genuine synthetic fixture
        # cannot satisfy the production oracle's sealed Hermite/causal-ball/
        # b_D constructions at fixture scale, so the ported PASS tests run
        # with the labeled fixture oracle installed.  The production oracle
        # is saved here, restored in tearDown, and reinstated inside
        # production-gate tests via restore_production_oracle().
        self._production_oracle = (
            COMPARATOR.typed_alpha_and_incidence,
            COMPARATOR.reconstruct_spatial_momenta,
            COMPARATOR.reconstruct_cell_and_bump,
        )
        (
            COMPARATOR.typed_alpha_and_incidence,
            COMPARATOR.reconstruct_spatial_momenta,
            COMPARATOR.reconstruct_cell_and_bump,
        ) = fixture_reconstruction_oracle(fixture)

    def write_bridge_manifest(self, rows: dict[str, str]) -> str:
        """(Re)write the fixture bundle-binding manifest + adjacent seal at
        the fixture canonical-v001 path, patch the comparator's bridge
        constants, and return the manifest digest fixture bundles stamp."""
        bridge_manifest = self.root / "bundle_binding_v001.json"
        bridge_manifest.write_text(
            json.dumps(
                {
                    "schema":
                        "stage8_t7_actual_parent_car_bundle_binding_test_v001",
                    "files": [
                        {"path": path, "sha256": digest}
                        for path, digest in sorted(rows.items())
                    ],
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        bridge_seal = Path(f"{bridge_manifest}.seal.sha256")
        bridge_seal.write_text(
            f"{sha256(bridge_manifest)}  {bridge_manifest.name}\n",
            encoding="ascii",
        )
        COMPARATOR.BUNDLE_BINDING_MANIFEST = bridge_manifest
        COMPARATOR.BUNDLE_BINDING_SEAL = bridge_seal
        self.bridge_manifest_sha256 = sha256(bridge_manifest)
        return self.bridge_manifest_sha256

    def restore_production_oracle(self) -> None:
        """Reinstate the comparator's sealed production reconstruction
        oracle for tests that must exercise the production gate."""
        (
            COMPARATOR.typed_alpha_and_incidence,
            COMPARATOR.reconstruct_spatial_momenta,
            COMPARATOR.reconstruct_cell_and_bump,
        ) = self._production_oracle

    def tearDown(self) -> None:
        self.restore_production_oracle()
        self.temporary.cleanup()

    def bundle_paths(self, lane: str) -> tuple[Path, Path]:
        return self.root / f"{lane}.json", self.root / f"{lane}.npz"

    def transport(self, matrix: np.ndarray) -> np.ndarray:
        return self.overlap.conjugate().T @ matrix @ self.overlap

    def bundle_content(
        self,
        lane: str,
        fixture: FixtureData | None = None,
    ) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
        fixture = fixture if fixture is not None else self.fixture
        arrays: dict[str, np.ndarray] = {}
        matrix_components: dict[str, dict[str, str]] = {
            category: {} for category in COMPARATOR.MATRIX_CATEGORIES
        }

        lane_matrices = fixture.lane_matrices[lane]
        for category, values in lane_matrices.items():
            for identifier, canonical_matrix in values.items():
                key = f"{category}__{identifier.replace('.', '_')}"
                if category == "record_projectors" or lane == "primary":
                    arrays[key] = canonical_matrix.copy()
                else:
                    arrays[key] = self.transport(canonical_matrix)
                matrix_components[category][identifier] = key

        if lane == "independent":
            arrays["basis_overlap_primary_from_independent"] = self.overlap.copy()
            arrays["primary_labels"] = COMPARATOR.expected_primary_labels()
            arrays["independent_labels"] = COMPARATOR.expected_independent_labels()
            arrays["independent_phases"] = (
                COMPARATOR.expected_independent_phases(
                    COMPARATOR.expected_independent_labels()
                )
            )
        else:
            for ell in COMPARATOR.EXPECTED_DISCRETE_LABELS["ell"]:
                arrays[f"basis_labels__{ell}"] = (
                    COMPARATOR.expected_primary_labels()
                )

        steps = COMPARATOR.GENERATOR_MIDPOINT_COUNTS[lane]
        for ell in COMPARATOR.EXPECTED_DISCRETE_LABELS["ell"]:
            stacks = fixture.stacks[lane, ell]
            arrays[f"genpiece_midpoint_times__{ell}"] = stacks["times"].copy()
            arrays[f"genpiece_M_stack__{ell}"] = stacks["m_stack"].copy()
            arrays[f"genpiece_B_stack__{ell}"] = stacks["b_stack"].copy()
            # The stored h0 is the ACTUAL matrix in the lane's own basis: the
            # independent lane stores its lifted (own-convention) h0, as the
            # production independent lane does.
            if lane == "independent":
                arrays[f"genpiece_h0__{ell}"] = self.transport(fixture.h0[ell])
            else:
                arrays[f"genpiece_h0__{ell}"] = fixture.h0[ell].copy()
            arrays[f"genpiece_p_stack__{ell}"] = fixture.p_stacks[ell].copy()
        arrays["genpiece_alpha_stack"] = fixture.pieces["alpha_stack"].copy()
        arrays["genpiece_Sn"] = fixture.pieces["incidence"].copy()

        for ell_index, ell in enumerate(COMPARATOR.EXPECTED_DISCRETE_LABELS["ell"]):
            if lane == "independent":
                # Production convention: the independent lane stores its
                # connection diagnostic at the EXACT cell midpoint t = 1/2
                # (not a point of its 384-midpoint grid), in its own basis;
                # the comparator ties it, after pinned transport, to its
                # reconstruction oracle at t = 1/2 under the declared
                # independent quadrature (S1-1c).
                _, bump_half = fixture.cell_and_bump(
                    0.5,
                    ell_index,
                    COMPARATOR.LANE_QUADRATURES["independent"],
                )
                connection = -np.kron(
                    bump_half, fixture.pieces["alpha_stack"][0]
                )
                arrays[f"diag_h0__{ell}"] = self.transport(fixture.h0[ell])
                arrays[f"diag_connection_midpoint__{ell}"] = self.transport(
                    connection
                )
            else:
                # Production convention: the primary lane stores the
                # connection at its stored midpoint index steps//2, built
                # from the SAME b_stack entry it stores as a generator
                # piece (S1-1c tie).
                midpoint = steps // 2
                connection = -np.kron(
                    fixture.stacks[lane, ell]["b_stack"][midpoint],
                    fixture.pieces["alpha_stack"][0],
                )
                arrays[f"diag_h0__{ell}"] = fixture.h0[ell].copy()
                arrays[f"diag_connection_midpoint__{ell}"] = connection
            for pair in ("p1", "p2"):
                for kernel in ("all", "pointer"):
                    target = fixture.lane_matrices[lane]["aggregate_kernels"][
                        f"{ell}.{pair}.{kernel}"
                    ]
                    lane_target = (
                        target if lane == "primary" else self.transport(target)
                    )
                    if lane == "primary":
                        arrays[
                            f"diag_primary__{ell}__n48__{pair}__{kernel}"
                        ] = lane_target.copy()
                        arrays[
                            f"diag_primary__{ell}__n24__{pair}__{kernel}"
                        ] = lane_target + 1.0e-6 * np.eye(32)
                        arrays[
                            f"diag_primary__{ell}__n12__{pair}__{kernel}"
                        ] = lane_target + 5.0e-6 * np.eye(32)
                        arrays[
                            f"diag_primary_secondary_quadrature__{ell}"
                            f"__n48__{pair}__{kernel}"
                        ] = lane_target + 1.0e-6 * np.eye(32)
                    else:
                        arrays[
                            f"diag_independent__{ell}__n384__{pair}__{kernel}"
                        ] = lane_target.copy()
                        arrays[
                            f"diag_independent__{ell}__n192__{pair}__{kernel}"
                        ] = lane_target + 1.0e-6 * np.eye(32)

        route1_ready = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
        route1_other = np.array([1.0, -1.0], dtype=complex) / np.sqrt(2.0)
        arrays["diag_route1_ready"] = route1_ready
        arrays["diag_route1_projector__completed"] = np.outer(
            route1_ready,
            route1_ready.conjugate(),
        )
        arrays["diag_route1_projector__other"] = np.outer(
            route1_other,
            route1_other.conjugate(),
        )
        route1_histories = self.history_values[1:]
        route1_unitaries = {
            theta: np.diag([1.0, np.exp(1j * theta)]).astype(complex)
            for theta in route1_histories
        }
        for history_index, theta in enumerate(route1_histories, start=1):
            arrays[f"diag_route1_unitary__a{history_index}"] = (
                route1_unitaries[theta]
            )
        for route_index, (plus, minus) in enumerate(
            ((0.07, -0.11), (0.13, 0.04))
        ):
            plus_amplitudes = np.array(
                [
                    vector.conjugate() @ route1_unitaries[plus] @ route1_ready
                    for vector in (route1_ready, route1_other)
                ]
            )
            minus_amplitudes = np.array(
                [
                    vector.conjugate() @ route1_unitaries[minus] @ route1_ready
                    for vector in (route1_ready, route1_other)
                ]
            )
            arrays[
                f"diag_route1_current__r{route_index}__completed"
            ] = np.array(
                [[np.conjugate(minus_amplitudes[0]) * plus_amplitudes[0]]],
                dtype=complex,
            )
            arrays[
                f"diag_route1_current__r{route_index}__all"
            ] = np.array(
                [[np.vdot(minus_amplitudes, plus_amplitudes)]],
                dtype=complex,
            )

        manifest: dict[str, Any] = {
            "dimensions": dict(COMPARATOR.EXPECTED_DIMENSIONS),
            "discrete_labels": json.loads(
                json.dumps(COMPARATOR.EXPECTED_DISCRETE_LABELS)
            ),
            "scalar_components": {
                "record_eigenvalues": {
                    f"l{index}": float(value)
                    for index, value in enumerate(self.record_values)
                },
                "coefficients": {
                    **{
                        f"p.l{index}": [
                            float(value.real),
                            float(value.imag),
                        ]
                        for index, value in enumerate(self.probabilities)
                    },
                    **{
                        f"w.l{index}": [
                            float(value.real),
                            float(value.imag),
                        ]
                        for index, value in enumerate(self.pointer_weights)
                    },
                    "ell.ell0": 1.0,
                    "ell.ell1": float(np.sqrt(2.0)),
                    **{
                        f"history.a{index}": float(value)
                        for index, value in enumerate(self.history_values)
                    },
                },
            },
            "matrix_components": matrix_components,
            "basis_overlap_key": (
                "basis_overlap_primary_from_independent"
                if lane == "independent"
                else None
            ),
        }
        return manifest, arrays

    def write_bundle(
        self,
        lane: str,
        *,
        fixture: FixtureData | None = None,
        mutate_manifest: Any | None = None,
        mutate_arrays: Any | None = None,
        mutate_payload: Any | None = None,
        stale_manifest_hash: bool = False,
    ) -> tuple[Path, Path]:
        json_path, npz_path = self.bundle_paths(lane)
        manifest, arrays = self.bundle_content(lane, fixture=fixture)
        if mutate_manifest is not None:
            mutate_manifest(manifest)
        if mutate_arrays is not None:
            mutate_arrays(manifest, arrays)
        np.savez(npz_path, **arrays)
        manifest["npz_keys"] = sorted(arrays)
        manifest_hash = canonical_sha256(manifest)
        if stale_manifest_hash:
            manifest_hash = "0" * 64
        payload = {
            "schema": COMPARATOR.BUNDLE_SCHEMA,
            "lane": lane,
            "spec_sha256": COMPARATOR.SPEC_SHA256,
            "executor_sha256": self.implementation_rows[
                COMPARATOR.EXECUTOR_PATHS[lane]
            ],
            # A1 bridge: a production lane verifies and stamps the sealed
            # manifest at the canonical v001 path, NOT the comparator's own
            # manifest (whose digest it can never know: the own manifest
            # includes rows for this comparator and its tests).
            "implementation_manifest_sha256": self.bridge_manifest_sha256,
            # A production lane's attestation records the lane executor as
            # the launcher-hashed target (repair binding R1 item 4).
            "runtime_attestation": {
                **dict(getattr(sys, COMPARATOR.RUNTIME_MARKER)),
                "target_sha256": self.implementation_rows[
                    COMPARATOR.EXECUTOR_PATHS[lane]
                ],
            },
            "npz_sha256": sha256(npz_path),
            "manifest_sha256": manifest_hash,
            "manifest": manifest,
            "generator_pieces_schema": COMPARATOR.GENERATOR_PIECES_SCHEMA,
            "generator_midpoint_count": {
                ell: COMPARATOR.GENERATOR_MIDPOINT_COUNTS[lane]
                for ell in COMPARATOR.EXPECTED_DISCRETE_LABELS["ell"]
            },
            "sealed": True,
            "immutable_bundle": True,
            "precomparison_committed": lane == "independent",
            "primary_output_paths_readable_during_construction": (
                False if lane == "independent" else None
            ),
            "coupling_evaluation_authorized": False,
            "alpha_computed": False,
            "proof_authorized": False,
            "comparison_diagnostics": self.comparison_diagnostics(lane),
            "route1_current_route2_architecture_reduction": {
                "construction": "synthetic_current_architecture_fixture",
                "maximum_completed_component_error": 0.0,
                "maximum_exhaustive_kernel_error": 0.0,
                "passed": True,
                "actual_parent_route1_line_restriction_derived": False,
            },
            "route1_current_route2_architecture_reduction_passed": True,
            "actual_parent_route1_line_restriction_derived": False,
        }
        if lane == "primary":
            payload["route1_isolated_reexecution"] = {
                "maximum_completed_component_error": 0.0,
                "maximum_exhaustive_kernel_error": 0.0,
                "passed": True,
            }
        if mutate_payload is not None:
            mutate_payload(payload)
        json_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        Path(f"{npz_path}.seal.sha256").write_text(
            f"{sha256(npz_path)}  {npz_path.name}\n",
            encoding="ascii",
        )
        Path(f"{json_path}.seal.sha256").write_text(
            f"{sha256(json_path)}  {json_path.name}\n",
            encoding="ascii",
        )
        return json_path, npz_path

    @staticmethod
    def comparison_diagnostics(lane: str) -> dict[str, Any]:
        if lane == "primary":
            return {
                "local_gate_maxima": {
                    "maximum_hermiticity": 0.0,
                    "record_eigenvalue_error": 0.0,
                    "record_spectral_completeness": 0.0,
                    "record_projector_idempotence": 0.0,
                    "probability_sum": 0.0,
                    "maximum_gaussian_direct": 0.0,
                    "maximum_kraus_component": 0.0,
                    "maximum_kraus_compression": 0.0,
                    "maximum_unitarity": 0.0,
                    "maximum_direct_isometry": 0.0,
                    "maximum_same_identity": 0.0,
                    "maximum_pointer_bound": 0.0,
                    "maximum_adjoint": 0.0,
                    "maximum_contraction": 0.0,
                },
                "primary_convergence": {
                    "ell1": {
                        f"p{pair}.{kernel}": {
                            "d_12_24": 4.0e-6,
                            "d_24_48": 1.0e-6,
                            "ratio": 4.0,
                        }
                        for pair in (1, 2)
                        for kernel in ("all", "pointer")
                    }
                },
                "primary_quadrature_differences": {
                    "ell1": {
                        f"p{pair}.{kernel}": 1.0e-6
                        for pair in (1, 2)
                        for kernel in ("all", "pointer")
                    }
                },
                "connection": {
                    "ell1": {
                        "signal_norm": 0.1,
                        "maximum_connection_norm": 0.2,
                    }
                },
            }
        return {
            "local_gate_maxima": {
                "maximum_primitive_hermiticity_residual": 0.0,
                "record_eigenvalue_error": 0.0,
                "spectral_completeness_residual": 0.0,
                "probability_sum_residual": 0.0,
                "maximum_direct_spectral_kraus_residual": 0.0,
                "maximum_direct_spectral_aggregate_residual": 0.0,
                "maximum_spectral_unitarity_residual": 0.0,
                "maximum_direct_unitarity_residual": 0.0,
                "maximum_adjoint_exchange_residual": 0.0,
                "maximum_same_history_identity_residual": 0.0,
                "maximum_contraction_or_positivity_violation": 0.0,
            },
            "independent_rk4_tails": {
                "ell1": {
                    f"p{pair}.{kernel}": 1.0e-6
                    for pair in (1, 2)
                    for kernel in ("all", "pointer")
                }
            },
            "connection": {
                "ell1": {
                    "signal_norm": 0.1,
                    "maximum_connection_norm": 0.2,
                }
            },
        }

    def run_comparison(
        self,
        *,
        fixture: FixtureData | None = None,
        mutate_primary_manifest: Any | None = None,
        mutate_independent_manifest: Any | None = None,
        mutate_primary_arrays: Any | None = None,
        mutate_independent_arrays: Any | None = None,
        mutate_primary_payload: Any | None = None,
        mutate_independent_payload: Any | None = None,
        stale_independent_manifest_hash: bool = False,
        wrong_expected_hash: str | None = None,
        controller_context: str | None = None,
    ) -> dict[str, Any]:
        self.output.unlink(missing_ok=True)
        Path(f"{self.output}.seal.sha256").unlink(missing_ok=True)
        independent_json, independent_npz = self.write_bundle(
            "independent",
            fixture=fixture,
            mutate_manifest=mutate_independent_manifest,
            mutate_arrays=mutate_independent_arrays,
            mutate_payload=mutate_independent_payload,
            stale_manifest_hash=stale_independent_manifest_hash,
        )
        primary_json, primary_npz = self.write_bundle(
            "primary",
            fixture=fixture,
            mutate_manifest=mutate_primary_manifest,
            mutate_arrays=mutate_primary_arrays,
            mutate_payload=mutate_primary_payload,
        )
        result = COMPARATOR.compare_bundles(
            independent_json=independent_json,
            independent_npz=independent_npz,
            primary_json=primary_json,
            primary_npz=primary_npz,
            independent_json_sha256=wrong_expected_hash or sha256(independent_json),
            independent_npz_sha256=sha256(independent_npz),
            primary_json_sha256=sha256(primary_json),
            primary_npz_sha256=sha256(primary_npz),
            output=self.output,
            independent_receipt_sha256=FIXTURE_INDEPENDENT_RECEIPT_SHA256,
            primary_receipt_sha256=FIXTURE_PRIMARY_RECEIPT_SHA256,
            controller_context=controller_context,
        )
        stored = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertEqual(result, stored)
        return result

    def assert_blocked(self, result: dict[str, Any]) -> None:
        self.assertEqual(result["overall_verdict"], COMPARATOR.BLOCKED_VERDICT)
        self.assertFalse(result["comparison_complete"])
        self.assertFalse(result["comparison_passed"])
        self.assertFalse(result["alpha_computed"])
        self.assertFalse(result["proof_authorized"])

    # ------------------------------------------------------------------
    # Ported v001/v002 fence tests.  PASS cases run under the LABELED
    # monkeypatched fixture reconstruction oracle installed in setUp (see
    # the module docstring); the production oracle is exercised by the
    # production-gate tests below.
    # ------------------------------------------------------------------

    def test_matching_transported_bundles_pass(self) -> None:
        # REBUILT PASS TEST (binding V002 S1 item 4): runs with the
        # monkeypatched fixture oracle, explicitly labeled — the fixture
        # pieces are spec-conforming with respect to the patched oracle,
        # not the sealed constructions, so this test exercises the gate
        # logic without demonstrating arbitrary pieces passing the
        # production gate (see
        # test_production_oracle_blocks_synthetic_pieces).
        result = self.run_comparison(controller_context="fixture-controller")
        self.assertEqual(result["overall_verdict"], COMPARATOR.PASS_VERDICT)
        self.assertTrue(result["comparison_complete"])
        self.assertTrue(result["comparison_passed"])
        self.assertEqual(result["component_failure_count"], 0)
        self.assertTrue(
            result["route1_consistency_falsifier"][
                "current_route2_architecture_reduces_to_O6"
            ]
        )
        self.assertFalse(result["actual_parent_route1_line_restriction_derived"])
        self.assertEqual(result["controller_context"], "fixture-controller")
        self.assertEqual(
            set(result["resolved_input_paths"]),
            {"independent_json", "independent_npz", "primary_json", "primary_npz"},
        )
        self.assertEqual(
            result["resolved_output_path"], str(self.output.resolve())
        )
        # S1-1d: the receipt digests are recorded verbatim in the sealed
        # output under the frozen top-level keys.
        self.assertEqual(
            result["independent_receipt_sha256"],
            FIXTURE_INDEPENDENT_RECEIPT_SHA256,
        )
        self.assertEqual(
            result["primary_receipt_sha256"],
            FIXTURE_PRIMARY_RECEIPT_SHA256,
        )
        # A1 bridge: the sealed output records the comparator's own
        # manifest digest AND the recomputed bundle-binding digest the
        # bundles stamped — two different sealed manifests, as in
        # production.
        self.assertEqual(
            result["implementation_manifest_sha256"],
            self.implementation_manifest_sha256,
        )
        self.assertEqual(
            result["bundle_binding_manifest_sha256"],
            self.bridge_manifest_sha256,
        )
        self.assertNotEqual(
            self.implementation_manifest_sha256,
            self.bridge_manifest_sha256,
        )
        # S1-1a / S1-1c: the piece-authenticity and tied-diagnostic gate
        # reports are recorded per lane and passed.
        for lane in ("primary", "independent"):
            self.assertTrue(result["piece_authenticity"][lane]["passed"])
            self.assertEqual(
                result["piece_authenticity"][lane]["declared_quadrature"],
                list(COMPARATOR.LANE_QUADRATURES[lane]),
            )
            self.assertTrue(result["tied_diagnostics"][lane]["passed"])

    def test_current_route2_route1_fences_block(self) -> None:
        def mutate_response(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["diag_route1_current__r0__all"][0, 0] += 1.0e-3

        self.assert_blocked(
            self.run_comparison(mutate_primary_arrays=mutate_response)
        )
        self.assert_blocked(
            self.run_comparison(
                mutate_primary_payload=lambda payload: payload.update(
                    actual_parent_route1_line_restriction_derived=True
                )
            )
        )

    def test_runtime_attestation_fence_blocks(self) -> None:
        def mutate(payload: dict[str, Any]) -> None:
            payload["runtime_attestation"]["runtime_manifest_sha256"] = "0" * 64

        self.assert_blocked(
            self.run_comparison(mutate_independent_payload=mutate)
        )

    def test_external_hash_fence_blocks(self) -> None:
        self.assert_blocked(self.run_comparison(wrong_expected_hash="f" * 64))

    def test_manifest_self_hash_fence_blocks(self) -> None:
        self.assert_blocked(
            self.run_comparison(stale_independent_manifest_hash=True)
        )

    def test_npz_inventory_fence_blocks(self) -> None:
        independent_json, independent_npz = self.write_bundle("independent")
        payload = json.loads(independent_json.read_text(encoding="utf-8"))
        payload["manifest"]["npz_keys"] = payload["manifest"]["npz_keys"][:-1]
        payload["manifest_sha256"] = canonical_sha256(payload["manifest"])
        independent_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        primary_json, primary_npz = self.write_bundle("primary")
        result = COMPARATOR.compare_bundles(
            independent_json=independent_json,
            independent_npz=independent_npz,
            primary_json=primary_json,
            primary_npz=primary_npz,
            independent_json_sha256=sha256(independent_json),
            independent_npz_sha256=sha256(independent_npz),
            primary_json_sha256=sha256(primary_json),
            primary_npz_sha256=sha256(primary_npz),
            output=self.output,
            independent_receipt_sha256=FIXTURE_INDEPENDENT_RECEIPT_SHA256,
            primary_receipt_sha256=FIXTURE_PRIMARY_RECEIPT_SHA256,
        )
        self.assert_blocked(result)

    def test_independent_precommit_attestation_fences_block(self) -> None:
        fields = (
            ("immutable_bundle", False),
            ("precomparison_committed", False),
            ("primary_output_paths_readable_during_construction", True),
        )
        for field, value in fields:
            with self.subTest(field=field):
                self.output.unlink(missing_ok=True)
                Path(f"{self.output}.seal.sha256").unlink(missing_ok=True)
                independent_json, independent_npz = self.write_bundle("independent")
                payload = json.loads(independent_json.read_text(encoding="utf-8"))
                payload[field] = value
                independent_json.write_text(
                    json.dumps(payload, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                primary_json, primary_npz = self.write_bundle("primary")
                result = COMPARATOR.compare_bundles(
                    independent_json=independent_json,
                    independent_npz=independent_npz,
                    primary_json=primary_json,
                    primary_npz=primary_npz,
                    independent_json_sha256=sha256(independent_json),
                    independent_npz_sha256=sha256(independent_npz),
                    primary_json_sha256=sha256(primary_json),
                    primary_npz_sha256=sha256(primary_npz),
                    output=self.output,
                    independent_receipt_sha256=FIXTURE_INDEPENDENT_RECEIPT_SHA256,
                    primary_receipt_sha256=FIXTURE_PRIMARY_RECEIPT_SHA256,
                )
                self.assert_blocked(result)

    def test_input_path_alias_fence_atomically_blocks(self) -> None:
        independent_json, independent_npz = self.write_bundle("independent")
        primary_json, _primary_npz = self.write_bundle("primary")
        result = COMPARATOR.compare_bundles(
            independent_json=independent_json,
            independent_npz=independent_npz,
            primary_json=primary_json,
            primary_npz=independent_npz,
            independent_json_sha256=sha256(independent_json),
            independent_npz_sha256=sha256(independent_npz),
            primary_json_sha256=sha256(primary_json),
            primary_npz_sha256=sha256(independent_npz),
            output=self.output,
            independent_receipt_sha256=FIXTURE_INDEPENDENT_RECEIPT_SHA256,
            primary_receipt_sha256=FIXTURE_PRIMARY_RECEIPT_SHA256,
        )
        self.assert_blocked(result)

    def test_dimension_and_label_fences_block(self) -> None:
        cases = (
            lambda manifest: manifest["dimensions"].update(source_dimension=3),
            lambda manifest: manifest["discrete_labels"].update(ell=["sqrt(2)"]),
        )
        for mutation in cases:
            with self.subTest(mutation=mutation):
                self.assert_blocked(
                    self.run_comparison(mutate_primary_manifest=mutation)
                )

    def test_scalar_fences_block_separately(self) -> None:
        for category in COMPARATOR.SCALAR_CATEGORIES:
            with self.subTest(category=category):
                def mutate(manifest: dict[str, Any], selected: str = category) -> None:
                    key = next(iter(manifest["scalar_components"][selected]))
                    manifest["scalar_components"][selected][key] = 0.125

                self.assert_blocked(
                    self.run_comparison(mutate_primary_manifest=mutate)
                )

    def test_basis_unitarity_fence_blocks(self) -> None:
        def mutate(_manifest: dict[str, Any], arrays: dict[str, np.ndarray]) -> None:
            arrays["basis_overlap_primary_from_independent"][0, 0] = 0.1

        self.assert_blocked(
            self.run_comparison(mutate_independent_arrays=mutate)
        )

    def test_unitary_but_unprovenanced_basis_overlap_blocks(self) -> None:
        def mutate(_manifest: dict[str, Any], arrays: dict[str, np.ndarray]) -> None:
            arrays["basis_overlap_primary_from_independent"][:, 0] *= -1.0

        self.assert_blocked(
            self.run_comparison(mutate_independent_arrays=mutate)
        )

    def test_executor_provenance_fence_blocks(self) -> None:
        def mutate(payload: dict[str, Any]) -> None:
            payload["executor_sha256"] = "0" * 64

        self.assert_blocked(
            self.run_comparison(mutate_primary_payload=mutate)
        )

    def test_attestation_target_hash_fence_blocks(self) -> None:
        def mutate(payload: dict[str, Any]) -> None:
            payload["runtime_attestation"]["target_sha256"] = "0" * 64

        result = self.run_comparison(mutate_independent_payload=mutate)
        self.assert_blocked(result)
        self.assertIn("target-hash", result["reason"])

        def drop(payload: dict[str, Any]) -> None:
            del payload["runtime_attestation"]["target_sha256"]

        self.assert_blocked(
            self.run_comparison(mutate_independent_payload=drop)
        )

    def test_each_matrix_component_fence_blocks(self) -> None:
        for category in COMPARATOR.MATRIX_CATEGORIES:
            with self.subTest(category=category):
                def mutate(
                    manifest: dict[str, Any],
                    arrays: dict[str, np.ndarray],
                    selected: str = category,
                ) -> None:
                    key = next(iter(manifest["matrix_components"][selected].values()))
                    arrays[key] = arrays[key].copy()
                    arrays[key][0, 0] += 1.0e-2

                self.assert_blocked(
                    self.run_comparison(mutate_primary_arrays=mutate)
                )

    def test_diagnostic_gates_block_individually(self) -> None:
        def bad_convergence(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["diag_primary__ell0__n12__p1__all"] = arrays[
                "diag_primary__ell0__n24__p1__all"
            ].copy()

        def bad_tail(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["diag_independent__ell0__n192__p1__all"] += (
                1.0e-3 * np.eye(32)
            )

        def bad_sensitivity(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays[
                "diag_primary_secondary_quadrature__ell0__n48__p1__all"
            ] += 2.0e-2 * np.eye(32)

        def bad_local_identity(
            manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            key = manifest["matrix_components"]["direct_responses"][
                "ell0.p1.all"
            ]
            arrays[key] = arrays[key] + 1.0e-5 * np.eye(32)

        self.assert_blocked(
            self.run_comparison(mutate_primary_arrays=bad_convergence)
        )
        self.assert_blocked(
            self.run_comparison(mutate_independent_arrays=bad_tail)
        )
        self.assert_blocked(
            self.run_comparison(mutate_primary_arrays=bad_sensitivity)
        )
        self.assert_blocked(
            self.run_comparison(mutate_primary_arrays=bad_local_identity)
        )

    def test_missing_component_and_unmanifested_npz_fences_block(self) -> None:
        def remove_component(manifest: dict[str, Any]) -> None:
            manifest["matrix_components"]["aggregate_kernels"].pop(
                next(iter(manifest["matrix_components"]["aggregate_kernels"]))
            )

        self.assert_blocked(
            self.run_comparison(mutate_primary_manifest=remove_component)
        )

        def missing_basis(manifest: dict[str, Any]) -> None:
            manifest["basis_overlap_key"] = "not_present"

        self.assert_blocked(
            self.run_comparison(mutate_independent_manifest=missing_basis)
        )

    def test_nonfinite_and_firewall_fences_block(self) -> None:
        def nonfinite(_manifest: dict[str, Any], arrays: dict[str, np.ndarray]) -> None:
            key = next(key for key in arrays if key.startswith("propagators__"))
            arrays[key] = arrays[key].copy()
            arrays[key][0, 0] = np.nan

        self.assert_blocked(
            self.run_comparison(mutate_independent_arrays=nonfinite)
        )

        self.output.unlink(missing_ok=True)
        Path(f"{self.output}.seal.sha256").unlink(missing_ok=True)
        independent_json, independent_npz = self.write_bundle("independent")
        payload = json.loads(independent_json.read_text(encoding="utf-8"))
        payload["alpha_computed"] = True
        independent_json.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        primary_json, primary_npz = self.write_bundle("primary")
        result = COMPARATOR.compare_bundles(
            independent_json=independent_json,
            independent_npz=independent_npz,
            primary_json=primary_json,
            primary_npz=primary_npz,
            independent_json_sha256=sha256(independent_json),
            independent_npz_sha256=sha256(independent_npz),
            primary_json_sha256=sha256(primary_json),
            primary_npz_sha256=sha256(primary_npz),
            output=self.output,
            independent_receipt_sha256=FIXTURE_INDEPENDENT_RECEIPT_SHA256,
            primary_receipt_sha256=FIXTURE_PRIMARY_RECEIPT_SHA256,
        )
        self.assert_blocked(result)

    # ------------------------------------------------------------------
    # Ported v002 fences (lineage, spectral-Kraus, adjoint exchange, B2/B3).
    # ------------------------------------------------------------------

    def test_genuine_fixture_passes_lineage_gate(self) -> None:
        result = self.run_comparison()
        self.assertEqual(result["overall_verdict"], COMPARATOR.PASS_VERDICT)
        lineage = result["generator_propagator_lineage"]
        for lane in ("primary", "independent"):
            report = lineage[lane]
            self.assertTrue(report["passed"])
            self.assertEqual(report["cases"], 30)
            self.assertEqual(
                report["midpoint_count"],
                COMPARATOR.GENERATOR_MIDPOINT_COUNTS[lane],
            )
            self.assertEqual(
                report["budget_operator_2_norm"],
                COMPARATOR.LINEAGE_BUDGETS[lane],
            )
            self.assertLessEqual(
                report["maximum_residual"],
                COMPARATOR.LINEAGE_BUDGETS[lane],
            )

    def test_fabricated_propagators_block_on_lineage_gate(self) -> None:
        # Correct generator pieces, internally self-consistent responses,
        # but propagators NOT integrated from the pieces: every stored
        # propagator and Kraus member is left-multiplied by a fixed unitary,
        # which preserves every algebraic identity the v001 comparator
        # checked (cross operators, aggregates, direct responses, Kraus
        # completeness, unitarity, cross-lane transport) and is caught only
        # by the generator-to-propagator lineage gate.
        canonical_twist = np.diag(
            np.exp(-1j * 0.3 * np.linspace(0.0, 1.0, 32))
        ).astype(complex)
        independent_twist = self.transport(canonical_twist)

        def twist_lane(twist: np.ndarray) -> Any:
            def mutate(
                _manifest: dict[str, Any],
                arrays: dict[str, np.ndarray],
            ) -> None:
                for key in list(arrays):
                    if key.startswith("propagators__") or key.startswith(
                        "direct_kraus_members__"
                    ):
                        arrays[key] = twist @ arrays[key]

            return mutate

        result = self.run_comparison(
            mutate_primary_arrays=twist_lane(canonical_twist),
            mutate_independent_arrays=twist_lane(independent_twist),
        )
        self.assert_blocked(result)
        self.assertIn("lineage", result["reason"])

    def test_missing_generator_pieces_block(self) -> None:
        def drop_schema(payload: dict[str, Any]) -> None:
            del payload["generator_pieces_schema"]

        result = self.run_comparison(mutate_independent_payload=drop_schema)
        self.assert_blocked(result)
        self.assertIn("generator-pieces schema", result["reason"])

        def wrong_grid(payload: dict[str, Any]) -> None:
            payload["generator_midpoint_count"] = {"ell0": 48, "ell1": 48}

        self.assert_blocked(
            self.run_comparison(mutate_independent_payload=wrong_grid)
        )

        def drop_array(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            del arrays["genpiece_M_stack__ell0"]

        result = self.run_comparison(mutate_primary_arrays=drop_array)
        self.assert_blocked(result)
        self.assertIn("genpiece_M_stack__ell0", result["reason"])

    def test_tampered_generator_pieces_block(self) -> None:
        def non_hermitian_piece(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["genpiece_B_stack__ell0"] = arrays[
                "genpiece_B_stack__ell0"
            ].copy()
            arrays["genpiece_B_stack__ell0"][0, 0, 1] += 1.0e-6

        result = self.run_comparison(
            mutate_primary_arrays=non_hermitian_piece
        )
        self.assert_blocked(result)

        def inconsistent_h0(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["genpiece_h0__ell0"] = arrays["genpiece_h0__ell0"].copy()
            arrays["genpiece_h0__ell0"][0, 0] += 1.0e-6

        result = self.run_comparison(mutate_primary_arrays=inconsistent_h0)
        self.assert_blocked(result)
        self.assertIn("tensor assembly", result["reason"])

        def wrong_times(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["genpiece_midpoint_times__ell0"] = (
                arrays["genpiece_midpoint_times__ell0"] + 1.0e-6
            )

        result = self.run_comparison(mutate_primary_arrays=wrong_times)
        self.assert_blocked(result)
        self.assertIn("midpoint grid", result["reason"])

    def test_spectral_kraus_gate_blocks_on_perturbation(self) -> None:
        # A common phase on every stored Kraus member preserves every gate
        # the v001 comparator enforced (direct responses, completeness,
        # Gaussian/direct agreement, cross-lane transport at 3e-4) and is
        # caught only by the finding-5 spectral-Kraus rebuild at 3e-9.
        phase = np.exp(1j * 1.0e-6)

        def mutate(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            for key in list(arrays):
                if key.startswith("direct_kraus_members__"):
                    arrays[key] = phase * arrays[key]

        result = self.run_comparison(mutate_primary_arrays=mutate)
        self.assert_blocked(result)
        self.assertIn("spectral_kraus_reconstruction", result["reason"])

    def test_adjoint_exchange_gate_blocks_on_perturbation(self) -> None:
        def mutate(
            manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            key = manifest["matrix_components"]["aggregate_kernels"][
                "ell0.p1.all"
            ]
            perturbation = np.zeros((32, 32), dtype=complex)
            perturbation[0, 1] = 1.0e-5
            arrays[key] = arrays[key] + perturbation

        result = self.run_comparison(mutate_primary_arrays=mutate)
        self.assert_blocked(result)

        # Load the mutated bundle directly and confirm the adjoint-exchange
        # residual itself exceeds the sealed 3e-9 threshold.
        self.output.unlink(missing_ok=True)
        Path(f"{self.output}.seal.sha256").unlink(missing_ok=True)
        json_path, npz_path = self.write_bundle(
            "primary",
            mutate_arrays=mutate,
        )
        bundle = COMPARATOR.load_bundle(
            "primary",
            json_path,
            npz_path,
            sha256(json_path),
            sha256(npz_path),
        )
        maxima = COMPARATOR.recompute_bundle_internal_gates(bundle)
        self.assertGreater(
            maxima["adjoint_exchange"],
            COMPARATOR.INTERNAL_IDENTITY_TOLERANCE,
        )

    def test_same_history_identity_all_five_histories_gated(self) -> None:
        # Execution binding B3: a same-history defect at a history value that
        # is NOT part of any stored pair (a3) must still block, via the
        # widened propagator-rebuilt identity set.
        def mutate(
            manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            for record_index in range(3):
                key = manifest["matrix_components"]["propagators"][
                    f"ell0.a3.l{record_index}"
                ]
                arrays[key] = (1.0 + 1.0e-6) * arrays[key]

        result = self.run_comparison(mutate_primary_arrays=mutate)
        self.assert_blocked(result)

        self.output.unlink(missing_ok=True)
        Path(f"{self.output}.seal.sha256").unlink(missing_ok=True)
        json_path, npz_path = self.write_bundle("primary", mutate_arrays=mutate)
        bundle = COMPARATOR.load_bundle(
            "primary",
            json_path,
            npz_path,
            sha256(json_path),
            sha256(npz_path),
        )
        maxima = COMPARATOR.recompute_bundle_internal_gates(bundle)
        self.assertGreater(
            maxima["same_history_identity"],
            COMPARATOR.INTERNAL_IDENTITY_TOLERANCE,
        )

    def test_e_conn_history_pair_pinning_recorded(self) -> None:
        result = self.run_comparison()
        self.assertEqual(result["overall_verdict"], COMPARATOR.PASS_VERDICT)
        rows = result["diagnostic_gates"]["connection_sensitivity"]
        self.assertEqual(len(rows), 2)
        for row in rows:
            self.assertEqual(row["pinned_history_pair"], ["a1", "a2"])
            self.assertEqual(row["pinned_history_values"], [0.07, -0.11])

    def test_flag_renaming_no_protected_flag_true(self) -> None:
        result = self.run_comparison()
        self.assertEqual(result["overall_verdict"], COMPARATOR.PASS_VERDICT)
        self.assertTrue(
            result[
                "comparison_supports_actual_parent_regulated_CAR_operator_response"
            ]
        )
        self.assertTrue(
            result[
                "comparison_supports_actual_parent_same_carrier_one_source_restriction"
            ]
        )
        for name in PROTECTED_FLAG_NAMES:
            self.assertFalse(
                bool(result.get(name, False)),
                f"protected flag appears true in comparator output: {name}",
            )

    # ------------------------------------------------------------------
    # New v003 fences (repair binding V002 S1 item 4 mandatory negatives).
    # ------------------------------------------------------------------

    def test_production_oracle_blocks_synthetic_pieces(self) -> None:
        # PRODUCTION-GATE TEST: with the monkeypatch removed, the same
        # genuine synthetic fixture that passes above MUST BLOCK on the
        # piece-authenticity gate, proving the fixture oracle patch is
        # load-bearing and that no test demonstrates arbitrary pieces
        # passing the production gate.
        self.restore_production_oracle()
        result = self.run_comparison()
        self.assert_blocked(result)
        self.assertIn("piece-authenticity", result["reason"])

    def test_surrogate_pair_bundle_blocks_on_piece_reconstruction(self) -> None:
        # SURROGATE-PAIR TEST (binding S1 item 4; the audit's missing
        # class, run against the PRODUCTION oracle): a fully
        # self-consistent surrogate bundle pair — zero M, constant diagonal
        # B, diagonal p/alpha, closed-form exponential propagators built
        # with no ODE integration — MUST BLOCK on the piece-reconstruction
        # gate.
        self.restore_production_oracle()
        surrogate = FixtureData.instance("surrogate")
        result = self.run_comparison(fixture=surrogate)
        self.assert_blocked(result)
        self.assertIn("piece-authenticity", result["reason"])

        # Demonstrate the exploit really is self-consistent at every
        # pre-existing (v002-class) gate: the surrogate primary bundle
        # loads, passes the structural generator-piece gates, and PASSES
        # the lineage gate (its closed-form propagators solve its own
        # declared pieces' ODE exactly) — only the new v003
        # piece-reconstruction gate rejects it.
        json_path, npz_path = self.write_bundle("primary", fixture=surrogate)
        bundle = COMPARATOR.load_bundle(
            "primary",
            json_path,
            npz_path,
            sha256(json_path),
            sha256(npz_path),
        )
        COMPARATOR.validate_generator_pieces(bundle)
        lineage = COMPARATOR.validate_generator_propagator_lineage(bundle, None)
        self.assertTrue(lineage["passed"])
        self.assertLessEqual(
            lineage["maximum_residual"],
            COMPARATOR.LINEAGE_BUDGETS["primary"],
        )
        with self.assertRaises(COMPARATOR.ComparisonBlocked) as context:
            COMPARATOR.validate_piece_reconstruction(bundle)
        self.assertIn("piece-authenticity", str(context.exception))

    def test_wrong_quadrature_pieces_block(self) -> None:
        # Binding S1 item 4: a wrong-quadrature piece set (correct
        # construction formula, wrong DECLARED rule) MUST BLOCK.  The
        # primary lane's stored M/B stacks are recomputed under the
        # independent lane's declared rule; the ~2e-7 deviation passes the
        # lineage budgets and every transported tolerance and is caught
        # only by the 2e-11 piece-reconstruction pin against the declared
        # primary rule.
        fixture = self.fixture
        wrong_rule = COMPARATOR.LANE_QUADRATURES["independent"]

        def wrong_quadrature(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            for ell_index, ell in enumerate(("ell0", "ell1")):
                times = arrays[f"genpiece_midpoint_times__{ell}"]
                cells: list[np.ndarray] = []
                bumps: list[np.ndarray] = []
                for time in times:
                    cell, bump = fixture.cell_and_bump(
                        float(time), ell_index, wrong_rule
                    )
                    cells.append(cell)
                    bumps.append(bump)
                arrays[f"genpiece_M_stack__{ell}"] = np.stack(cells)
                arrays[f"genpiece_B_stack__{ell}"] = np.stack(bumps)

        result = self.run_comparison(mutate_primary_arrays=wrong_quadrature)
        self.assert_blocked(result)
        self.assertIn("piece-authenticity", result["reason"])
        self.assertIn("quadrature", result["reason"])

    def test_unpinned_basis_overlap_key_blocks(self) -> None:
        # Binding S1 item 4 / S1-1b (audit Blocking 2): a
        # basis_overlap_key naming ANY array other than the pinned literal
        # MUST BLOCK, even when the honestly named pinned array is also
        # present and the alternate array is unitary.
        def rekey(manifest: dict[str, Any]) -> None:
            manifest["basis_overlap_key"] = "alternate_transport_unitary"

        def add_alternate(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            twist = np.diag(
                np.exp(1j * 0.5 * np.linspace(0.0, 1.0, 32))
            ).astype(complex)
            arrays["alternate_transport_unitary"] = (
                twist @ arrays["basis_overlap_primary_from_independent"]
            )

        result = self.run_comparison(
            mutate_independent_manifest=rekey,
            mutate_independent_arrays=add_alternate,
        )
        self.assert_blocked(result)
        self.assertIn("pinned literal", result["reason"])

    def test_untied_diag_connection_blocks(self) -> None:
        # Binding S1 item 4 / S1-1c: an untied diag_connection (O(1)
        # Hermitian junk) MUST BLOCK.  With honest stored B_stack (fixture
        # oracle active) the block comes from the tied-diagnostic gate,
        # closing the audit's unlinked-diagnostic hole.
        def junk_diagnostic(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["diag_connection_midpoint__ell0"] = np.diag(
                np.linspace(1.0, 2.0, 32)
            ).astype(complex)

        result = self.run_comparison(mutate_primary_arrays=junk_diagnostic)
        self.assert_blocked(result)
        self.assertIn("tied-diagnostic", result["reason"])

        # The audit's exact exploit shape (O(1) Hermitian junk diagnostic
        # with B_stack ~ 0) is caught even earlier: the zeroed B_stack
        # itself fails the piece-reconstruction pin.
        def audit_shape(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            for ell in ("ell0", "ell1"):
                arrays[f"genpiece_B_stack__{ell}"] = np.zeros_like(
                    arrays[f"genpiece_B_stack__{ell}"]
                )
            arrays["diag_connection_midpoint__ell0"] = np.diag(
                np.linspace(1.0, 2.0, 32)
            ).astype(complex)

        result = self.run_comparison(mutate_primary_arrays=audit_shape)
        self.assert_blocked(result)
        self.assertIn("piece-authenticity", result["reason"])

    def test_untied_diag_h0_blocks(self) -> None:
        # S1-1c second tie: diag_h0 must be the stored generator h0 at
        # 2e-15; a 1e-13 offset (invisible to every other gate) blocks.
        def stale_h0(
            _manifest: dict[str, Any],
            arrays: dict[str, np.ndarray],
        ) -> None:
            arrays["diag_h0__ell0"] = arrays["diag_h0__ell0"] + 1.0e-13

        result = self.run_comparison(mutate_primary_arrays=stale_h0)
        self.assert_blocked(result)
        self.assertIn("tied-diagnostic", result["reason"])

    def test_receipt_digest_cli_required_and_recorded(self) -> None:
        # S1-1d: both receipt-digest flags are required=True on the CLI,
        # and the digests are recorded verbatim even in a BLOCKED sealed
        # output.
        base_arguments = [
            "--independent-json", "independent.json",
            "--independent-npz", "independent.npz",
            "--primary-json", "primary.json",
            "--primary-npz", "primary.npz",
            "--independent-json-sha256", "0" * 64,
            "--independent-npz-sha256", "0" * 64,
            "--primary-json-sha256", "0" * 64,
            "--primary-npz-sha256", "0" * 64,
            "--output", "comparison.json",
        ]
        parser = COMPARATOR.parser()
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(
            io.StringIO()
        ):
            parser.parse_args(base_arguments)
        parsed = parser.parse_args(
            base_arguments
            + [
                "--independent-receipt-sha256",
                FIXTURE_INDEPENDENT_RECEIPT_SHA256,
                "--primary-receipt-sha256",
                FIXTURE_PRIMARY_RECEIPT_SHA256,
            ]
        )
        self.assertEqual(
            parsed.independent_receipt_sha256,
            FIXTURE_INDEPENDENT_RECEIPT_SHA256,
        )
        self.assertEqual(
            parsed.primary_receipt_sha256,
            FIXTURE_PRIMARY_RECEIPT_SHA256,
        )
        blocked = self.run_comparison(wrong_expected_hash="f" * 64)
        self.assert_blocked(blocked)
        self.assertEqual(
            blocked["independent_receipt_sha256"],
            FIXTURE_INDEPENDENT_RECEIPT_SHA256,
        )
        self.assertEqual(
            blocked["primary_receipt_sha256"],
            FIXTURE_PRIMARY_RECEIPT_SHA256,
        )

    # ------------------------------------------------------------------
    # New v004 fences (manifest-binding bridge amendment A1 / A2 item 3).
    # ------------------------------------------------------------------

    def test_fix2_strengthened_surrogate_blocks_on_real_oracle_m_b_quadrature(
        self,
    ) -> None:
        # FIX-2 (re-audit MAJOR; amendment A2 item 3): drive the REAL
        # production reconstruction oracle end-to-end — NO monkeypatch —
        # with the strengthened surrogate: typed alpha_stack/S_n copied
        # verbatim from the comparator source, exact ladder-formula p,
        # h0 = sum_j kron(p_j, alpha_j), M_stack = 0, constant fabricated
        # B_stack, closed-form eigh propagators.  Every check the v003
        # suite ever exercised (typed alpha/Sn equality, p, h0, lineage,
        # every internal identity) is satisfied by construction; ONLY the
        # previously untested Hermite/causal-ball/b_D quadrature
        # reconstruction of M/B can reject it.  This test therefore
        # executes that load-bearing code at production dimensions (it
        # takes seconds — that is the point) and must block with a reason
        # naming the M/B quadrature comparison and nothing upstream of it.
        # It subsumes the wrong-quadrature negative for the production
        # oracle.
        self.restore_production_oracle()
        strengthened = FixtureData.instance("strengthened")
        result = self.run_comparison(fixture=strengthened)
        self.assert_blocked(result)
        reason = result["reason"]
        self.assertIn("piece-authenticity", reason)
        self.assertIn("genpiece_M_stack", reason)
        self.assertIn("causal-ball/b_D quadrature", reason)
        for upstream_token in (
            "alpha_stack",
            "genpiece_Sn",
            "p_stack",
            "h0",
            "lineage",
        ):
            self.assertNotIn(
                upstream_token,
                reason,
                "FIX-2 block must land on the M/B quadrature comparison, "
                f"not on {upstream_token}",
            )

        # The exploit is genuinely upstream-clean: the primary surrogate
        # bundle loads, passes every structural generator-piece gate, and
        # PASSES the lineage gate (its closed-form eigh propagators solve
        # its own declared pieces' time-independent ODE exactly) — only
        # the real M/B quadrature reconstruction rejects it.
        json_path, npz_path = self.write_bundle("primary", fixture=strengthened)
        bundle = COMPARATOR.load_bundle(
            "primary",
            json_path,
            npz_path,
            sha256(json_path),
            sha256(npz_path),
        )
        COMPARATOR.validate_generator_pieces(bundle)
        lineage = COMPARATOR.validate_generator_propagator_lineage(bundle, None)
        self.assertTrue(lineage["passed"])
        self.assertLessEqual(
            lineage["maximum_residual"],
            COMPARATOR.LINEAGE_BUDGETS["primary"],
        )
        with self.assertRaises(COMPARATOR.ComparisonBlocked) as context:
            COMPARATOR.validate_piece_reconstruction(bundle)
        self.assertIn("genpiece_M_stack", str(context.exception))
        self.assertIn("causal-ball/b_D quadrature", str(context.exception))

        # The independent lane's declared 12/12/24 rule is exercised for
        # real as well and rejects the same surrogate on M/B.
        independent_json, independent_npz = self.write_bundle(
            "independent", fixture=strengthened
        )
        independent_bundle = COMPARATOR.load_bundle(
            "independent",
            independent_json,
            independent_npz,
            sha256(independent_json),
            sha256(independent_npz),
        )
        with self.assertRaises(COMPARATOR.ComparisonBlocked) as context:
            COMPARATOR.validate_piece_reconstruction(independent_bundle)
        self.assertIn("genpiece_M_stack", str(context.exception))
        self.assertIn("causal-ball/b_D quadrature", str(context.exception))

    def test_bridge_authority_row_mismatch_blocks(self) -> None:
        # A1 bridge negative (amendment mandate): mismatched executor
        # authority rows between the bundle-binding manifest and the
        # comparator's own manifest must BLOCK.  The bundle honestly
        # stamps the (sealed, recomputed-from-disk) bundle-binding
        # manifest, so only the row-by-row cross-check can reject it.
        rows = dict(self.bridge_rows)
        rows[COMPARATOR.EXECUTOR_PATHS["primary"]] = "0" * 64
        self.write_bridge_manifest(rows)
        result = self.run_comparison()
        self.assert_blocked(result)
        self.assertIn("manifest-binding bridge", result["reason"])
        self.assertIn("authority", result["reason"])

    def test_bridge_stamp_row_absence_and_seal_fences_block(self) -> None:
        # A bundle stamping the comparator's OWN manifest digest — the
        # v003 rule the amendment replaced, which no bundle produced by
        # the byte-frozen derive lanes can ever satisfy — must BLOCK.
        def stamp_own_manifest(payload: dict[str, Any]) -> None:
            payload["implementation_manifest_sha256"] = (
                self.implementation_manifest_sha256
            )

        result = self.run_comparison(mutate_primary_payload=stamp_own_manifest)
        self.assert_blocked(result)
        self.assertIn("canonical v001 path", result["reason"])

        # An executor row absent from the bundle-binding manifest must
        # BLOCK (non-vacuity: absence can never satisfy the bridge).
        rows = dict(self.bridge_rows)
        del rows[COMPARATOR.EXECUTOR_PATHS["independent"]]
        self.write_bridge_manifest(rows)
        result = self.run_comparison()
        self.assert_blocked(result)
        self.assertIn(
            "absent from the bundle-binding manifest", result["reason"]
        )

        # A broken bundle-binding adjacent seal must BLOCK before any
        # bundle stamp is honored.
        self.write_bridge_manifest(self.bridge_rows)
        COMPARATOR.BUNDLE_BINDING_SEAL.write_text(
            f"{'0' * 64}  {COMPARATOR.BUNDLE_BINDING_MANIFEST.name}\n",
            encoding="ascii",
        )
        result = self.run_comparison()
        self.assert_blocked(result)
        self.assertIn("bundle-binding manifest seal mismatch", result["reason"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
