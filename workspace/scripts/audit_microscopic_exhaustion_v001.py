#!/usr/bin/env python3
"""Test whether a finite public record forces a finite microscopic carrier."""

from __future__ import annotations

import hashlib
import json
import re
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "MICROSCOPIC_EXHAUSTION_IDENTIFIABILITY_GATE_V001.md"
PRIMITIVE_RESULT = ROOT / "results" / "primitive_record_carrier_v001.json"
SEAL = ROOT / "PREREGISTRATION_V003.seal.sha256"
RESULT = ROOT / "results" / "microscopic_exhaustion_v001.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal() -> bool:
    rows = SEAL.read_text(encoding="utf-8").splitlines()
    if not rows:
        return False
    for row in rows:
        expected, relative = row.split(maxsplit=1)
        sealed_path = (ROOT / relative.strip()).resolve()
        if not sealed_path.exists() or sha256(sealed_path) != expected:
            return False
    return True


def public_coherence(
    mode_count: int, marker: Decimal, variance: Decimal
) -> Decimal:
    with localcontext() as context:
        context.prec = 100
        exponent = -(variance * marker * marker) / (2 * mode_count)
        return exponent.exp() ** mode_count


def mode_weight_derivative(
    mode_count: int, marker: Decimal, variance: Decimal
) -> Decimal:
    """Derivative magnitude with respect to one mode's variance weight."""
    total = public_coherence(mode_count, marker, variance)
    return abs(-(marker * marker * total) / 2)


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    primitive = json.loads(PRIMITIVE_RESULT.read_text(encoding="utf-8"))

    mode_counts = (1, 2, 3, 4, 7, 16, 64)
    markers = tuple(
        Decimal(value)
        for value in ("0", "0.125", "0.5", "1", "1.75", "3")
    )
    variance = Decimal(1)
    with localcontext() as context:
        context.prec = 100
        expected = {
            marker: (-(variance * marker * marker) / 2).exp()
            for marker in markers
        }

    errors: list[Decimal] = []
    response_rows: list[dict[str, str | int]] = []
    all_modes_nonzero = True
    for mode_count in mode_counts:
        for marker in markers:
            actual = public_coherence(mode_count, marker, variance)
            error = abs(actual - expected[marker])
            errors.append(error)
            derivative = mode_weight_derivative(
                mode_count, marker, variance
            )
            if marker != 0:
                all_modes_nonzero = all_modes_nonzero and derivative > 0
            response_rows.append(
                {
                    "mode_count": mode_count,
                    "marker": str(marker),
                    "public_coherence": str(actual),
                    "expected_coherence": str(expected[marker]),
                    "absolute_error": str(error),
                    "single_mode_weight_derivative_magnitude": str(derivative),
                }
            )

    forbidden = (
        re.compile("137" + r"[.]0[0-9]+"),
        re.compile("0" + r"[.]00729[0-9]+"),
        re.compile("17" + r"[.]543"),
    )
    target_hits = [
        pattern.pattern for pattern in forbidden if pattern.search(note)
    ]

    required_status = (
        "finite_public_record_implies_finite_microscopic_carrier = false",
        "microscopic_record_exhaustion_derived = false",
        "complete_g_A_psi_record_specification_derived = false",
        "coupling_evaluation_authorized = false",
        "alpha_computed = false",
        "proof_authorized = false",
    )
    missing_status = [
        phrase for phrase in required_status if phrase not in note
    ]

    checks = {
        "sealed_v003_authority_unchanged": verify_seal(),
        "primitive_public_record_gate_passes": (
            primitive["overall"]
            == "PASS_PRIMITIVE_RECORD_CARRIER_KINEMATICS_COMPLETE_ACTION_FALSE_ALPHA_FALSE"
        ),
        "arbitrary_mode_counts_give_same_complete_public_response": (
            max(errors) < Decimal("1e-90")
        ),
        "every_mode_has_nonzero_public_influence_away_from_origin": (
            all_modes_nonzero
        ),
        "microscopic_mode_count_varies_while_public_carrier_is_fixed": (
            len(set(mode_counts)) == len(mode_counts)
            and primitive["primitive_single_handle_real_carrier_dimension"] == 2
        ),
        "scope_flags_fail_closed": not missing_status,
        "target_literal_guard_passes": not target_hits,
    }
    failed = [name for name, passed in checks.items() if not passed]
    overall = (
        "PASS_CURRENT_PRE_ALPHA_PRINCIPLES_DO_NOT_DERIVE_MICROSCOPIC_EXHAUSTION_ALPHA_FALSE"
        if not failed
        else "FAIL_MICROSCOPIC_EXHAUSTION_IDENTIFIABILITY_GATE"
    )
    payload = {
        "overall": overall,
        "checks": checks,
        "failed_checks": failed,
        "maximum_public_response_error": str(max(errors)),
        "mode_counts_tested": list(mode_counts),
        "markers_tested": [str(marker) for marker in markers],
        "response_rows": response_rows,
        "primitive_public_record_carrier_derived": True,
        "finite_public_record_implies_finite_microscopic_carrier": False,
        "microscopic_record_exhaustion_derived": False,
        "unique_UV_completion_derived": False,
        "complete_g_A_psi_record_specification_derived": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(overall)
    print(f"maximum_public_response_error={max(errors):.3E}")
    print("microscopic_record_exhaustion_derived=false")
    print("alpha_computed=false")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
