#!/usr/bin/env python3
"""Freeze exact normal/optimized output records for source-parent audits."""

from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json"
AUDITS = (
    "audit_bid_elementary_record_hilbert_functor_classification_v001.py",
    "audit_bid_source_decorated_first_opening_classification_v001.py",
    "audit_bid_charged_handle_activation_v002.py",
    "audit_bid_primitive_boundary_superconnection_classification_v001.py",
    "audit_bid_full_source_map_commutant_classification_v001.py",
    "audit_bid_global_car_charge_and_activation_v001.py",
    "audit_bid_public_record_hilbertization_derivation_v001.py",
    "audit_bid_graded_boundary_superconnection_repair_v001.py",
    "audit_bid_boundary_metric_transport_derivation_v001.py",
    "audit_bid_first_opening_graph_refinement_quotient_v001.py",
    "audit_bid_chiral_source_record_incidence_parent_v001.py",
    "audit_bid_active_handle_control_v001.py",
    "audit_bid_physical_record_amplitude_zero_free_v001.py",
    "audit_bid_many_record_parent_identifiability_v001.py",
    "audit_bid_root_incidence_identity_derivation_v001.py",
    "audit_bid_complete_normal_dependent_endpoint_map_classification_v001.py",
    "audit_bid_complete_one_normal_zero_form_enumeration_v001.py",
    "audit_bid_full_dirac_car_source_typing_v001.py",
    "audit_bid_charged_cellular_cpt_intertwiner_v001.py",
    "audit_bid_axial_phase_cp_reduction_v001.py",
    "audit_bid_unique_charged_controlled_coupling_v001.py",
    "audit_bid_global_boundary_descent_quasi_free_v001.py",
    "audit_bid_lorentzian_source_schur_pole_v001.py",
    "audit_bid_lorentz_covariant_source_boundary_map_v001.py",
    "audit_bid_distinguishable_record_cell_composition_v001.py",
    "audit_bid_global_car_record_composition_v001.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def clean_environment() -> dict[str, str]:
    allowed = {}
    for key in ("HOME", "PATH", "TMPDIR", "LANG", "LC_ALL"):
        if key in os.environ:
            allowed[key] = os.environ[key]
    allowed.update(
        {
            "PYTHONPATH": "",
            "PYTHONSTARTUP": "",
            "PYTHONOPTIMIZE": "",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
        }
    )
    return allowed


def run(script: str, optimized: bool) -> str:
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command.extend(["-B", str(ROOT / "scripts" / script)])
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        env=clean_environment(),
    )
    require(
        result.returncode == 0,
        f"{script} failed in {'optimized' if optimized else 'normal'} mode",
    )
    require(not result.stderr, f"{script} wrote stderr")
    return result.stdout


def parse_record(output: str, script: str) -> dict[str, str]:
    record: dict[str, str] = {}
    for line in output.splitlines():
        require(line == line.strip() and bool(line), f"{script} has malformed line")
        key, separator, value = line.rpartition("=")
        require(bool(separator and key and value), f"{script} has non-record line: {line}")
        require(key not in record, f"{script} has duplicate output key: {key}")
        record[key] = value
    require(record.get("alpha_computed") == "FALSE", f"{script} lost alpha firewall")
    return record


def main() -> None:
    if OUTPUT.exists():
        raise FileExistsError(f"refusing to overwrite {OUTPUT}")
    records = {}
    for script in AUDITS:
        path = ROOT / "scripts" / script
        tree = ast.parse(path.read_text(encoding="utf-8"))
        require(
            not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
            f"{script} contains Python assert",
        )
        normal = run(script, optimized=False)
        optimized = run(script, optimized=True)
        require(normal == optimized, f"{script} changes under python -O")
        records[script] = parse_record(normal, script)
    payload = {
        "schema": "gravacle.bid-source-parent-subordinate-output.v001",
        "alpha_computed": False,
        "records": records,
    }
    with OUTPUT.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(OUTPUT)
    print(f"frozen_subordinate_records={len(records)}")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
