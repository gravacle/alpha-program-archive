#!/usr/bin/env python3
"""Non-production tests for the Stage-8 T7 independent PRECOMPARISON lane."""

from __future__ import annotations

import importlib.util
import ast
import math
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SUBJECT_PATH = (
    ROOT
    / "scripts"
    / "derive_stage8_t7_actual_parent_regulated_car_operator_response_"
    "independent_v001.py"
)
SPEC = importlib.util.spec_from_file_location(
    "stage8_t7_independent_precomparison_subject",
    SUBJECT_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load independent PRECOMPARISON subject")
SUBJECT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SUBJECT
SPEC.loader.exec_module(SUBJECT)


class SmoothSupportTests(unittest.TestCase):
    def test_smooth_bump_has_only_time_oriented_diamond_support(self) -> None:
        self.assertEqual(float(SUBJECT.smooth_diamond_bump(-0.1, 0.0)), 0.0)
        self.assertEqual(float(SUBJECT.smooth_diamond_bump(1.1, 0.0)), 0.0)
        self.assertEqual(float(SUBJECT.smooth_diamond_bump(0.25, 0.25**2)), 0.0)
        self.assertEqual(float(SUBJECT.smooth_diamond_bump(0.25, 0.3**2)), 0.0)
        self.assertAlmostEqual(
            float(SUBJECT.smooth_diamond_bump(0.5, 0.0)),
            1.0,
            places=14,
        )
        inside = float(SUBJECT.smooth_diamond_bump(0.25, 0.1**2))
        self.assertGreater(inside, 0.0)
        self.assertLessEqual(inside, 1.0)

    def test_smooth_bump_vectorization_preserves_support(self) -> None:
        radii_squared = np.array([0.0, 0.1**2, 0.3**2])
        values = SUBJECT.smooth_diamond_bump(0.25, radii_squared)
        self.assertEqual(values.shape, radii_squared.shape)
        self.assertGreater(values[0], 0.0)
        self.assertGreater(values[1], 0.0)
        self.assertEqual(values[2], 0.0)


class RK4TableauTests(unittest.TestCase):
    def test_constant_diagonal_control_has_fourth_order_tail(self) -> None:
        hamiltonian = np.diag([0.25, -0.7]).astype(complex)
        exact = np.diag(np.exp(-1j * np.array([0.25, -0.7])))
        coarse = SUBJECT.rk4_propagate(lambda _t: hamiltonian, 2, 16)
        medium = SUBJECT.rk4_propagate(lambda _t: hamiltonian, 2, 32)
        fine = SUBJECT.rk4_propagate(lambda _t: hamiltonian, 2, 64)
        coarse_error = np.linalg.norm(coarse - exact, ord=2)
        medium_error = np.linalg.norm(medium - exact, ord=2)
        fine_error = np.linalg.norm(fine - exact, ord=2)
        self.assertGreater(coarse_error / medium_error, 14.0)
        self.assertGreater(medium_error / fine_error, 14.0)
        self.assertLess(fine_error, 1.0e-9)


class SpectralCompletenessTests(unittest.TestCase):
    def test_record_spectral_resolution_is_complete(self) -> None:
        record = np.array(
            [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
            dtype=complex,
        )
        eigenvalues, projectors, probabilities, weights = (
            SUBJECT.record_spectral_data(record)
        )
        np.testing.assert_allclose(
            eigenvalues,
            np.array([-math.sqrt(2.0), 0.0, math.sqrt(2.0)]),
            atol=2.0e-14,
        )
        np.testing.assert_allclose(
            projectors.sum(axis=0),
            np.eye(3),
            atol=2.0e-14,
        )
        self.assertAlmostEqual(float(probabilities.real.sum()), 1.0, places=14)
        self.assertLess(float(np.max(np.abs(probabilities.imag))), 2.0e-14)
        self.assertLess(abs(weights.sum()), 2.0e-14)
        for left in range(3):
            for right in range(3):
                product = projectors[left] @ projectors[right]
                expected = projectors[left] if left == right else np.zeros((3, 3))
                np.testing.assert_allclose(product, expected, atol=2.0e-14)


class Route1ArchitectureReductionTests(unittest.TestCase):
    def test_current_route2_architecture_reduces_to_frozen_O6(self) -> None:
        arrays: dict[str, np.ndarray] = {}
        result = SUBJECT.current_route2_route1_architecture_reduction(arrays)
        self.assertTrue(result["passed"])
        self.assertFalse(result["actual_parent_route1_line_restriction_derived"])
        self.assertLessEqual(
            float(result["maximum_completed_component_error"]),
            1.0e-10,
        )
        self.assertLessEqual(
            float(result["maximum_exhaustive_kernel_error"]),
            1.0e-10,
        )
        self.assertIn("diag_route1_current__r0__completed", arrays)
        self.assertIn("diag_route1_current__r1__all", arrays)


class SchemaAndFenceTests(unittest.TestCase):
    def test_schema_and_protected_flags_are_precomparison_only(self) -> None:
        self.assertEqual(
            SUBJECT.SCHEMA,
            "stage8_t7_actual_parent_regulated_car_operator_response_bundle_v001",
        )
        tree = ast.parse(SUBJECT_PATH.read_text(encoding="utf-8"))
        imported_modules = {
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        imported_modules.update(
            node.module or ""
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        )
        self.assertFalse(
            any("primary" in module for module in imported_modules),
            imported_modules,
        )

    def test_read_allowlist_rejects_future_primary_and_unknown_paths(self) -> None:
        for relative in SUBJECT.READ_ALLOWLIST:
            self.assertFalse(
                any(
                    marker in relative
                    for marker in SUBJECT.FORBIDDEN_FUTURE_READ_MARKERS
                )
            )
        with self.assertRaises(RuntimeError):
            SUBJECT.assert_read_allowed(
                "stage8_execution/work/"
                "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
            )
        with self.assertRaises(RuntimeError):
            SUBJECT.assert_read_allowed("unsealed_unknown_input.txt")

    def test_basis_overlap_is_prepropagation_and_unitary(self) -> None:
        overlap = SUBJECT.prepropagation_overlap()
        residual = np.linalg.norm(
            overlap.conjugate().T @ overlap - np.eye(SUBJECT.SOURCE_DIMENSION),
            ord=2,
        )
        self.assertLessEqual(residual, 2.0e-11)
        self.assertNotEqual(SUBJECT.primary_labels(), SUBJECT.independent_labels())

    def test_common_component_inventory_is_complete(self) -> None:
        dummy_arrays: dict[str, np.ndarray] = {
            f"record_projector__l{record_index}": np.eye(3, dtype=complex)
            for record_index in range(3)
        }
        dummy_arrays["basis_overlap_primary_from_independent"] = np.eye(
            SUBJECT.SOURCE_DIMENSION,
            dtype=complex,
        )
        for ell_index in range(len(SUBJECT.ELLS)):
            ell_tag = f"ell{ell_index}"
            for history_index in range(len(SUBJECT.HISTORIES)):
                for record_index in range(SUBJECT.RECORD_DIMENSION):
                    dummy_arrays[
                        f"common_u__{ell_tag}__a{history_index}__l{record_index}"
                    ] = np.eye(SUBJECT.SOURCE_DIMENSION, dtype=complex)
                for outcome in range(SUBJECT.RECORD_DIMENSION):
                    dummy_arrays[
                        f"common_direct_kraus__{ell_tag}"
                        f"__a{history_index}__x{outcome}"
                    ] = np.eye(SUBJECT.SOURCE_DIMENSION, dtype=complex)
            for pair_index in range(len(SUBJECT.HISTORY_PAIRS)):
                for left in range(SUBJECT.RECORD_DIMENSION):
                    for right in range(SUBJECT.RECORD_DIMENSION):
                        dummy_arrays[
                            f"common_cross__{ell_tag}__p{pair_index}"
                            f"__mu{left}__l{right}"
                        ] = np.eye(SUBJECT.SOURCE_DIMENSION, dtype=complex)
                for kernel in ("all", "pointer"):
                    dummy_arrays[
                        f"common_direct_{kernel}__{ell_tag}__p{pair_index}"
                    ] = np.eye(SUBJECT.SOURCE_DIMENSION, dtype=complex)
                    dummy_arrays[
                        f"common_gaussian_{kernel}__{ell_tag}__p{pair_index}"
                    ] = np.eye(SUBJECT.SOURCE_DIMENSION, dtype=complex)
        record = np.array(
            [[0, 0, -1j], [0, 0, 1j], [1j, -1j, 0]],
            dtype=complex,
        )
        values, _projectors, probabilities, weights = (
            SUBJECT.record_spectral_data(record)
        )
        manifest = SUBJECT.common_component_manifest(
            dummy_arrays,
            values,
            probabilities,
            weights,
        )
        counts = {
            category: len(entries)
            for category, entries in manifest["matrix_components"].items()
        }
        self.assertEqual(
            counts,
            {
                "record_projectors": 3,
                "propagators": 30,
                "cross_operators": 54,
                "direct_kraus_members": 30,
                "direct_responses": 12,
                "aggregate_kernels": 12,
            },
        )
        expected_propagators = {
            f"ell{ell}.a{history}.l{record_index}"
            for ell in range(2)
            for history in range(5)
            for record_index in range(3)
        }
        expected_cross = {
            f"ell{ell}.p{pair}.mu{left}.l{right}"
            for ell in range(2)
            for pair in range(3)
            for left in range(3)
            for right in range(3)
        }
        expected_kraus = {
            f"ell{ell}.a{history}.x{outcome}"
            for ell in range(2)
            for history in range(5)
            for outcome in range(3)
        }
        expected_responses = {
            f"ell{ell}.p{pair}.{kernel}"
            for ell in range(2)
            for pair in range(3)
            for kernel in ("all", "pointer")
        }
        self.assertEqual(
            set(manifest["matrix_components"]["propagators"]),
            expected_propagators,
        )
        self.assertEqual(
            set(manifest["matrix_components"]["cross_operators"]),
            expected_cross,
        )
        self.assertEqual(
            set(manifest["matrix_components"]["direct_kraus_members"]),
            expected_kraus,
        )
        self.assertEqual(
            set(manifest["matrix_components"]["direct_responses"]),
            expected_responses,
        )
        self.assertEqual(
            set(manifest["matrix_components"]["aggregate_kernels"]),
            expected_responses,
        )

    def test_atomic_bundle_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            npz_path = root / "precomparison.npz"
            json_path = root / "precomparison.json"
            arrays = {"control": np.eye(2)}
            metadata = {
                "schema": SUBJECT.SCHEMA,
                "proof_authorized": False,
                "alpha_computed": False,
            }
            SUBJECT.atomic_write_bundle(arrays, metadata, npz_path, json_path)
            self.assertTrue(npz_path.is_file())
            self.assertTrue(json_path.is_file())
            with self.assertRaises(RuntimeError):
                SUBJECT.atomic_write_bundle(arrays, metadata, npz_path, json_path)


if __name__ == "__main__":
    unittest.main()
