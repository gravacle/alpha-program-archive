"""Independent tests for the record-onset action gate."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "audit_boundary_record_onset_saturation_action_v001.py"


def load_module():
    spec = importlib.util.spec_from_file_location("record_onset", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load record-onset audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_write_and_pointer_roles_independently() -> None:
    # -iY at angle pi/2 is the exact real matrix below.
    endpoint_unitary = ((0j, -1 + 0j), (1 + 0j, 0j))
    ready = (1 + 0j, 0j)
    written = (
        endpoint_unitary[0][0] * ready[0] + endpoint_unitary[0][1] * ready[1],
        endpoint_unitary[1][0] * ready[0] + endpoint_unitary[1][1] * ready[1],
    )
    if written != (0j, 1 + 0j):
        raise AssertionError("Independent geodesic endpoint check failed")

    y = ((0j, -1j), (1j, 0j))
    contrast = ((-1 + 0j, 0j), (0j, 1 + 0j))
    hs = sum(
        y[row][column].conjugate() * contrast[row][column]
        for row in range(2)
        for column in range(2)
    )
    if hs != 0j:
        raise AssertionError("Write and pointer directions were conflated")


def test_fail_closed_status() -> None:
    module = load_module()
    result = module.build_result()
    if result["integrated_write_action"] != "pi*hbar/2":
        raise AssertionError("Wrong integrated write action")
    if result["write_contrast_hilbert_schmidt_inner_product"] != 0:
        raise AssertionError("Write and contrast directions are not independent")
    for false_flag in (
        "historical_target_blindness_established",
        "unique_causal_record_interval_numerically_derived",
        "complete_source_record_environment_action_derived",
        "physical_durability_derived",
        "write_energy_identified_with_pointer_coefficient",
        "write_energy_identified_with_source_mass",
        "record_generated_source_mass_derived",
        "spectral_evaluation_authorized",
        "coupling_evaluation_authorized",
        "alpha_computed",
        "proof_authorized",
    ):
        if result[false_flag] is not False:
            raise AssertionError(f"Premature promotion: {false_flag}")
    try:
        module.require(False, "sentinel")
    except RuntimeError:
        pass
    else:
        raise AssertionError("Fail-closed require did not raise")


def test_mutated_write_generator_is_detected() -> None:
    module = load_module()
    module.Y = module.I2
    try:
        module.build_result()
    except RuntimeError:
        pass
    else:
        raise AssertionError("Identity mutation passed as a write generator")
