#!/usr/bin/env python3
"""Fail-closed provenance audit for the Level-1 action-premise ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "LEVEL1_MICROSCOPIC_ACTION_PREMISE_LEDGER_V001.json"
OUTPUT = ROOT / "results" / "level1_microscopic_action_premise_ledger_v001.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_seal(target: Path, seal: Path) -> None:
    fields = seal.read_text(encoding="ascii").strip().split()
    require(fields == [sha256(target), target.name], f"Seal failed: {target.name}")


def exact_status(text: str, key: str, expected: bool) -> None:
    pattern = re.compile(rf"^{re.escape(key)}\s*=\s*(true|false)\s*$", re.MULTILINE)
    matches = pattern.findall(text)
    require(len(matches) == 1, f"Expected exactly one {key}")
    require((matches[0] == "true") is expected, f"Wrong value for {key}")


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="ascii"))
    require(
        ledger["schema"] == "level1-microscopic-action-premise-ledger-v001",
        "Wrong ledger schema",
    )
    require(
        set(ledger["premises"])
        == {
            "fundamental_boundary_record_action",
            "parent_state_covariance",
            "causal_incidence_support",
        },
        "Premise inventory drift",
    )

    verified = {}
    combined = []
    for name, item in ledger["premises"].items():
        target = ROOT / item["path"]
        seal = ROOT / item["seal"]
        require(item["status"] == "ADOPTED_LEVEL_1", f"{name} not adopted")
        require(sha256(target) == item["sha256"], f"{name} digest drift")
        verify_seal(target, seal)
        verified[name] = item["sha256"]
        combined.append(target.read_text(encoding="utf-8"))

    causal = (ROOT / ledger["premises"]["causal_incidence_support"]["path"]).read_text(
        encoding="utf-8"
    )
    exact_status(causal, "causal_incidence_support_principle_adopted_Level_1", True)
    exact_status(causal, "completed_primitive_incidence_reuse_allowed", False)
    exact_status(causal, "shared_source_support_allowed", True)
    exact_status(causal, "durability_assumed", False)
    exact_status(causal, "physical_durability_derived", False)
    exact_status(causal, "alpha_computed", False)
    require("## Falsifiers" in causal, "Causal principle lacks falsifiers")
    require(
        re.search(r"does not reapply\s+a completed\s+incidence", causal) is not None
        and "absent from the active generator" in causal,
        "Primitive-incidence reuse rule missing",
    )

    for key, value in ledger["derivation_obligations"].items():
        require(value is False, f"Prematurely closed obligation: {key}")
    for key, value in ledger["authorization"].items():
        require(value is False, f"Premature authorization: {key}")

    forbidden = (
        re.compile(r"137[.]0[0-9]+"),
        re.compile(r"0[.]00729[0-9]+"),
        re.compile(r"17[.]543"),
    )
    text = "\n".join(combined)
    require(not any(pattern.search(text) for pattern in forbidden), "Target literal found")

    result = {
        "schema": ledger["schema"],
        "ledger_sha256": sha256(LEDGER),
        "verified_premise_digests": verified,
        "premise_count": len(verified),
        "explicit_causal_falsifiers_present": True,
        "durability_remains_derivation_obligation": True,
        "target_literal_guard_passes": True,
        "spectral_evaluation_authorized": False,
        "coupling_evaluation_authorized": False,
        "alpha_computed": False,
        "proof_authorized": False,
        "status": "PASS_LEVEL1_PREMISES_BOUND_DERIVATIONS_BLOCKED",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(result["status"])


if __name__ == "__main__":
    main()
