#!/usr/bin/env python3
"""Target-free audit of the BID monoidal-extensivity derivation."""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DERIVATION = ROOT / "BID_MONOIDAL_EXTENSIVITY_DERIVATION_V001.md"


def direct_sum_negative_control() -> tuple[bool, float]:
    lengths = (9, 17, 33, 65, 129, 257)
    kappas = [
        1.0 / (4.0 * length**4 * math.sin(math.pi / length) ** 2)
        for length in lengths
    ]
    scaled_limit = lengths[-1] ** 2 * kappas[-1]
    target = 1.0 / (4.0 * math.pi**2)
    passed = (
        all(right < left for left, right in zip(kappas, kappas[1:]))
        and abs(scaled_limit - target) / target < 5e-5
        and kappas[-1] < 5e-7
    )
    return passed, scaled_limit


def monoidal_hessian_control() -> bool:
    # A nonzero normalized transition-amplitude fixture cos(s) is used only
    # to audit composition. It is not the BID survival amplitude.
    step = 1e-5

    def gamma(cell_count: int, value: float) -> float:
        return -math.log(abs(math.cos(value) ** cell_count))

    one_hessian = (gamma(1, step) - 2.0 * gamma(1, 0.0) + gamma(1, -step)) / (
        step**2
    )
    for cell_count in (2, 3, 7, 19):
        hessian = (
            gamma(cell_count, step)
            - 2.0 * gamma(cell_count, 0.0)
            + gamma(cell_count, -step)
        ) / (step**2)
        if abs(hessian / cell_count - one_hessian) > 2e-6:
            return False
    return True


def main() -> int:
    failures: list[str] = []
    if not DERIVATION.is_file():
        failures.append("missing monoidal derivation")
    else:
        text = DERIVATION.read_text(encoding="utf-8")
        required = (
            "H(K)=tensor_i H(K_i)",
            "<p(K)|U_K(A)|r(K)>",
            "Gamma_K(A)=sum_i Gamma_(K_i)(A_i)",
            "Gamma_N''(0)/N=Gamma_1''(0)",
            "kappa_L=1/[4 L^4 sin^2(pi/L)]",
            "No factor of `L^2`, `L^4`, cell count, or volume",
            "volume-independent open neighborhood",
            "connected_linked_cluster_density_proved = false",
            "root_survival_amplitude_used = false",
            "derived_public_transition_amplitude_used = true",
            "alpha_computed = false",
        )
        for item in required:
            if item not in text:
                failures.append(f"missing required derivation text: {item}")
        statuses = dict(
            re.findall(
                r"^([A-Za-z0-9_]+) = (true|false)$", text, flags=re.MULTILINE
            )
        )
        if statuses.get("exact_disjoint_monoidal_additivity_proved") != "true":
            failures.append("exact disjoint additivity not marked proved")
        if statuses.get("connected_linked_cluster_density_proved") != "false":
            failures.append("connected density is prematurely marked proved")
        if statuses.get("alpha_computed") != "false":
            failures.append("alpha is prematurely marked computed")

    direct_pass, scaled_limit = direct_sum_negative_control()
    if not direct_pass:
        failures.append("direct-sum zero-stiffness negative control failed")
    if not monoidal_hessian_control():
        failures.append("monoidal Hessian additivity control failed")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print("BID_MONOIDAL_EXTENSIVITY_AUDIT=FAIL")
        return 1

    print(f"direct_sum_L2_kappa_limit={scaled_limit:.16g}")
    print("V010_direct_sum_zero_stiffness=REPRODUCED_AND_REJECTED")
    print("disjoint_monoidal_Hessian_density=PASS")
    print("connected_linked_cluster_density=PENDING")
    print("BID_MONOIDAL_EXTENSIVITY_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
