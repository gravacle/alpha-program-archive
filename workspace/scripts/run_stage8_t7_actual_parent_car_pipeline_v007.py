#!/usr/bin/env python3
"""Run one sealed Stage-8 T7 production lane and issue a local execution receipt.

v007 — GENERATION G7 CONTROLLER, authored in the cycle-7 package under
STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001 (Part A
A1-A5, Part B B1/B2/B5, Part B MAJORs) and
STAGE8_T7_DIRECTORY_PERMISSION_FENCE_EVALUATION_AND_PROBES_V001 (the
directory-permission write fence, its limitations L1-L4, and its four
required work items).  Base v006.  The changes are enumerated below, in
full, with no "sole change" claim of the kind erratum E-2 falsified: item
1 alone repoints THREE pins, and every repoint is a functional change.

  1. GENERATION G7 REPOINTS (Part B B1's chosen fix).  The runtime
     launcher advances to launcher v007; the comparison target advances to
     comparator v006; the controller's own implementation authority
     advances to the sealed G7 manifest (provenance/..._implementation_
     v006.json); REQUIRED_MANIFEST_ROWS becomes the twelve-row G7
     inventory.  Controller, launcher, comparator and manifest now all
     name generation G7, and the byte-frozen v002 derive lanes are reached
     ONLY through the v001-path bridge manifest, exactly as before.  This
     is the wedge B1 named: comparator v005 pinned manifest v004 (whose
     launcher row is launcher v005) while controller v006 launched every
     lane under launcher v006.
  2. A1 GENERATION-COHERENCE CHECK (the systemic fix; see the
     GENERATION_COHERENCE_PINS table below).  A mechanical check reads
     EVERY generation pin in the chain FROM DISK -- the controller's
     launcher/manifest/bridge/target/row pins, the launcher's allowlist,
     the comparator's manifest/launcher/bridge/executor pins, the frontier
     manifest's row set, the bridge manifest's row set, and both frozen
     derive lanes' manifest pin -- and BLOCKS unless every one of them
     names the frozen generation.  It runs as precondition step 2, before
     any lane and before the fence is raised.  Six cycles were each ONE
     pin lagging ONE bump; this check is the mechanism that makes a single
     lagging pin fail loudly.  The pin table is a module-level frozen
     structure and the check requires the table to cover every pin it
     knows how to discover, so a future bump cannot silently orphan a row.
     Tests that drive it, named per discipline rule 4:
     test_stage8_t7_controller_v007.py::test_pin_table_is_total,
     ::test_coherent_generation_passes,
     ::test_single_lagging_pin_blocks (EIGHT one-pin skews of real
     component files, each required to block naming its pin), and
     ::test_manifest_row_skew_blocks.
  3. THE DIRECTORY-PERMISSION WRITE FENCE (fence record items 1 and 3).
     stage8_execution/work and provenance are mode 555 AT REST.  This
     controller RAISES them to 755 as its FIRST gated action after ALL
     preconditions pass, and DROPS them back in a finally path that
     covers every exit -- success, exception, and SIGINT/SIGTERM/SIGHUP.
     Per limitation L3 (the hard-kill window) the at-rest read-only state
     is asserted as a PRE-FLIGHT CONDITION: if the directories are found
     writable, the fence is DROPPED and the anomaly is RECORDED before
     anything proceeds, which makes the invariant self-healing on the next
     invocation.  The fence is a row of the coherence table.
     LIMITATIONS NOT CLAIMED AWAY: it is a write fence, not an execution
     fence (L1); it stops routes, not an operator with chmod (L2); SIGKILL
     between raise and drop still leaves the directories open until the
     next invocation self-heals (L3); the construction lane must raise and
     drop deliberately (L4).
     Tests that drive it, named per discipline rule 4:
     test_stage8_t7_controller_v007.py::test_fence_raise_and_drop_cycle,
     ::test_fence_at_rest_preflight_self_heals,
     ::test_l3_sigterm_during_the_raised_window_drops_the_fence, and
     test_stage8_t7_real_chain_rehearsal_v001.py (the raise/drop cycle end
     to end, the superseded-route write refusal, and the fence's adoption
     probe).
  4. A4 RECEIPT ORDER (recurred in v006's run_lane).  In v006 the receipt
     was SEALED BEFORE the returncode and target-intact checks, so the
     first blocked lane permanently consumed the canonical receipt path.
     In v007 both checks run FIRST and the receipt is sealed only after
     they pass: a blocked lane leaves ZERO canonical artifacts and the
     retry path stays open.  The block reason is reported on stderr.
     Driven by test_stage8_t7_controller_v007.py::
     test_a4_blocked_lane_seals_no_receipt (behavioural) and ::
     test_a4_receipt_seal_follows_the_checks_in_source (ordering).
  5. COMPARATOR-AUTHORITY HOIST (Part B MAJOR), condition-identical per
     A3 and verified by READING comparator v006's enforcement point: the
     comparator's OWN manifest verification -- adjacent seal present and
     matching, comparator's own row equal to the comparator on disk, and
     every row hash-equal to its file on disk -- plus the comparator's
     bundle-binding-bridge conditions including its symlink refusal, are
     verified in the controller pre-flight as the comparator_authority
     step.  Comparator v006 additionally hoists them into its own
     prologue, out of the try that seals a BLOCKED verdict; the two
     hoists are the same conditions on the same manifests.
  6. A5 seal coverage, the launcher docstring erratum (E-3) and the stale
     v005-era comment sweep are handled in the artifacts they belong to
     (the sealed G7 coherence table, launcher v007's docstring, and
     comparator v006 item 4 respectively).

PRECONDITION COUNT: the frozen tuple grows from ten steps to thirteen
(generation_coherence, fence_at_rest and comparator_authority are new);
--preflight-only still executes exactly that tuple in order and still
performs NO artifact write anywhere.  One honest exception is documented
at the fence: --preflight-only WILL drop the permission bits if it finds
them raised, because L3 mandates the self-heal; dropping a directory mode
bit writes no artifact, and the anomaly is reported in the pre-flight
JSON.  PREFLIGHT_OK IS NOT STARTABILITY EVIDENCE (A2): the only accepted
startability evidence is the no-stub end-to-end rehearsal in
scripts/test_stage8_t7_real_chain_rehearsal_v001.py.

The v006 header is retained below as history.

v006 (STAGE8_T7_CONTROLLER_V006_REPAIR_BINDING_V001, implementing the
reviewer batch-audit BLOCKING 3 and MAJORs M-a/M-b under the sealed
standing discipline STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001
and its rule-4 supplement; base v005, sole changes enumerated here):

  a. BLOCKING 3 (comparison-lane bundle-provenance hoist): all FOUR
     bundle/receipt provenance conditions comparator v005 enforces per
     bundle -- the executor manifest row, the runtime-launcher manifest
     row, the runtime-attestation target hash, and the bundle's
     implementation-manifest stamp -- are verified in the comparison-lane
     pre-flight against BOTH lane bundles on disk BEFORE the canonical
     comparison path is consumed.  The manifest-stamp member is the
     retained v005 comparison_bundle_stamps step (M1); the executor-row,
     launcher-row, and attested-target-hash members are the new
     comparison_bundle_provenance step.  The hoist enumeration is
     mechanical per the binding: every require() of the comparator's
     bundle-provenance section maps to a pre-flight step, and the mapping
     table comparator-require -> pre-flight step is part of this cycle's
     change report / verification artifact.
  b. M-a/M-b (primary-lane readiness hoist): the primary derive lane's
     pinned-digest, input-inventory, and Route-1-rerun preconditions are
     hoisted into the controller pre-flight as the new
     primary_route1_readiness step: the pinned canonical Route-1 result
     digest, the isolated-rerun snapshot absence, and the existence of
     every snapshot input (including the children enumerated by the two
     seal-list files) are verified from disk, in the byte-frozen lane's
     own order, BEFORE the primary lane runs.  Previously any of these
     failures surfaced only inside the lane, where write_blocked_result
     would already have consumed the canonical primary output path.
  c. IMPLEMENTATION MANIFEST v005: the controller's implementation
     authority is the sealed v005 manifest (provenance/stage8_t7_actual_
     parent_regulated_car_operator_response_implementation_v005.json,
     built by the manifest-v005 cycle AFTER verification of this file;
     until it exists on disk, pre-flight blocks precisely at the
     implementation_manifest step naming the absent manifest).
     REQUIRED_MANIFEST_ROWS is the ten-row v006 inventory below: the
     controller row advances to this file and the controller-test row
     advances to test_stage8_t7_controller_v006.py; every other row is
     unchanged from the v005 inventory.
  d. PRECONDITIONS: the frozen tuple is extended to ten steps in the
     documented order at the tuple; --preflight-only executes exactly
     this tuple in order with no write anywhere, and the verification
     ordering is proven by the real-component end-to-end tests in
     test_stage8_t7_controller_v006.py.

Everything else is retained from v005 byte-for-byte (launcher v005,
comparator v005 as the comparison target, the bridge v001-path manifest
binding, the M2 authority-digest pre-flight, the M1 bundle-stamp
pre-flight member, the push-capability pre-flight, receipt-existence lane
ordering, and --preflight-only).  The v005 header is retained below as
history.

v005 (STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001 + the v004
re-audit return, EXTERNAL_REAUDIT_2026-07-26_fable_v004_return.md; base
v004, sole changes enumerated here):

  a. REPOINTS (B1/Blocking-2 cycle): the runtime launcher is
     launch_stage8_t7_content_addressed_runtime_v006.py (whose rebuilt
     allowlist carries a row for THIS controller, closing the B1
     launcher-vs-controller deadlock); the comparison target is comparator
     v005; the controller's own implementation authority is the sealed v004
     manifest (provenance/..._implementation_v004.json); the required
     manifest row set is the ten-row v005 inventory below.  [v006:
     superseded by header item c -- the authority is now the sealed
     v005 manifest and the ten-row v006 inventory.]
  b. M1 BUNDLE-STAMP MEMBER: the comparison-lane pre-flight verifies the
     FULL manifest-binding bridge condition INCLUDING the bundle-stamp
     member — the v001-path manifest digest is recomputed from disk and
     compared against the implementation_manifest_sha256 stamped in BOTH
     lane bundle JSONs on disk — BEFORE the canonical comparison path is
     consumed (closes the inter-invocation regeneration hazard).
  c. M2 AUTHORITY-DIGEST PRE-FLIGHT: pre-flight recomputes and verifies,
     from disk, the sealed Phase-A spec digest and EVERY authority digest
     the byte-frozen derive lanes and the comparator verify at runtime
     (the frozen AUTHORITY_DIGESTS inventory below), BEFORE any canonical
     consumption in any lane. Previously these were verified only after
     canonical path commitment, inside the lanes.
  d. --preflight-only (per the sealed discipline's mandated instrument):
     runs EVERY enumerated precondition for the given --lane and exits 0
     with a one-line PREFLIGHT_OK json (or exits nonzero with the precise
     block reason) BEFORE any canonical write. The enumerated precondition
     list is the module-level frozen tuple PRECONDITIONS; the verification
     order is documented at that tuple, pre-flight executes the tuple in
     order, and every canonical write in this module occurs only after
     run_preflight() has returned (provable by the real-component
     end-to-end startability test in test_stage8_t7_controller_v005.py).

Retained from v004: the FIX 1 manifest-binding bridge pre-flight (now one
member richer, M1); the push-capability pre-flight (git push --dry-run,
fail-closed, pushes nothing); RECEIPT-EXISTENCE lane ordering only (external
anchoring between invocations is a cooperative operator procedure, not
enforced here; anchor_receipt_before_next_lane is a cooperative reminder);
GPG fully removed; per-lane invocation (--lane); every fail-closed
precondition verified BEFORE any canonical output path is consumed; receipts
record paths_verified_absent; the comparison lane passes both lane-receipt
digests to the comparator and cross-checks the recorded values. Recorded
fields are RECORDINGS for the externally anchored receipt chain, not
self-authentication.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import signal
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
RUNTIME_MARKER = "_stage8_t7_content_addressed_runtime_v001"
RUNTIME_MANIFEST_SHA256 = (
    "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b"
)
PINNED_PYTHON = Path(
    "/Users/bgm/.cache/codex-runtimes/"
    "codex-primary-runtime/dependencies/python/bin/python3"
).resolve()
RUNTIME_LAUNCHER = (
    ROOT / "scripts/launch_stage8_t7_content_addressed_runtime_v007.py"
)
IMPLEMENTATION_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v006.json"
)
IMPLEMENTATION_SEAL = Path(f"{IMPLEMENTATION_MANIFEST}.seal.sha256")
BRIDGE_MANIFEST = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_regulated_car_operator_response_implementation_v001.json"
)
BRIDGE_SEAL = Path(f"{BRIDGE_MANIFEST}.seal.sha256")
ARCHIVE_REPOSITORY = Path("/Users/bgm/MB Work/alpha-program-archive")
CONTROLLER_CONTEXT_ENVIRONMENT_KEY = "STAGE8_T7_CONTROLLER_CONTEXT"
RECEIPT_SCHEMA = "stage8_t7_local_sealed_execution_receipt_v003"

# M2: the sealed Phase-A specification digest, recomputed in pre-flight.
SPEC_RELATIVE = (
    "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md"
)
SPEC_SHA256 = "789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3"

# M2: EVERY authority digest the byte-frozen v002 derive lanes and the
# comparator verify at runtime (the union of both lanes' AUTHORITIES
# inventories plus the comparator's spec and runtime-manifest pins; the
# sealed Phase-A spec row and the sealed NumPy runtime-manifest row are
# members). Pre-flight recomputes each from disk BEFORE any canonical
# consumption in any lane, so a lane's own authority verification cannot
# fail after this pre-flight passes.
AUTHORITY_DIGESTS = {
    SPEC_RELATIVE: SPEC_SHA256,
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md":
        "6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md":
        "40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9",
    "STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md":
        "5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e",
    "STAGE8_ROUTE1_SPECIAL_CASE_CONSISTENCY_BINDING_V001.md":
        "460e87522884e703968025081cceccc0153af3cda27410c397fc2a09a0b367e3",
    "STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001.md":
        "4e1282bc800c47441d255e9d9d576958608d955dce15f02969261cd6e601e268",
    "STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md":
        "5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7",
    "STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md":
        "a1258dcf40732f0e3fce358a68ffdbd34bc347d70283550440582a1129bec510",
    "STAGE8_T7_EXACT_HERMITE_MIXED_COVARIANCE_RESULT_V001.md":
        "235246abd1c4df69c80bda8f79494c342e30178504dadec411612c18d6f8685b",
    "STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md":
        "1fd82d0d42c7d7b1369adfa0e0061c80044afc847f7dae2f066bdfb89165e56f",
    "STAGE8_T7_HERMITE_GALERKIN_BASELINE_SPEC_V001.md":
        "80aa4e1722c117e8195ce0fb2ae3fc37262bc8fc2ba5d79a6dd38cd1029bc26d",
    "STAGE8_T7_HERMITE_GALERKIN_NUMERICS_PROTOCOL_V001.md":
        "950e957ec2aa1022509b57df48f4f701e717e5dcbb18731332abbf55bf57dadd",
    "STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_"
    "AMENDMENT_V001.md":
        "8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md":
        "76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md":
        "2f2aa7f7397b70616fa5c9e8ed628ca1d1e819bb698133a169c6d544086b3cde",
    "STAGE8_T7_PURE_HERMITE_VACUUM_STRONG_CONVERGENCE_RESULT_V001.md":
        "a79939adf1d7185fdf4d6ec5ccb929de2e4f5997bee2ed085c0d63164dc8e370",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json":
        "f2e820d5d7a53335f1a6aacdbc03331d18e6afa350f99b7d2f2abd59d77bc46b",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py":
        "3d8aea1a4779b0bfe7a472dca1fab0642750e8e010e339b9e3b100197b75a18c",
    "stage8_execution/work/T07_hermite_galerkin_baseline.json":
        "87593740c5f35f68ea1c484c7ab304fbd12ee7b54f62f48f38417c80a2e33f7c",
    "stage8_execution/work/T07_hermite_galerkin_baseline_verification.json":
        "fc55cdedb059d31843b2490a9af2a74902c20acaed08793d64ff5c1e2a7f32f8",
}

# M-a/M-b: the primary derive lane's hoisted launch preconditions.  Every
# literal below mirrors the byte-frozen primary lane
# (derive_stage8_t7_actual_parent_regulated_car_operator_response_
# primary_v002.py, isolated_route1_rerun()) exactly: the pinned canonical
# Route-1 result digest, the isolated-rerun snapshot path (derived from
# the executor authority digest already frozen in AUTHORITY_DIGESTS), and
# the snapshot input inventory (fixed + direct + seal-list files, plus
# every child path the two seal-list files enumerate at pre-flight time).
ROUTE1_CANONICAL_RESULT = (
    ROOT / "stage8_execution/work/T07_primitive_operator_response_v001.json"
)
ROUTE1_CANONICAL_SHA256 = (
    "6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc"
)
ROUTE1_EXECUTOR_RELATIVE = (
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py"
)
ROUTE1_SNAPSHOT_DIRECTORY = (
    ROOT
    / "stage8_execution/isolated_route1_rerun"
    / AUTHORITY_DIGESTS[ROUTE1_EXECUTOR_RELATIVE][:16]
)
ROUTE1_FIXED_INPUTS = (
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py",
    "scripts/derive_stage8_t7_primitive_operator_response_v001.py.seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_SPEC_V001.md.seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_EXACT_DERIVATION_V001.md"
    ".seal.sha256",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md",
    "STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_AUTHORITY_AMENDMENT_V001.md"
    ".seal.sha256",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json",
    "provenance/stage8_t7_numpy_runtime_manifest_v001.json.seal.sha256",
    "scripts/build_stage8_t7_numpy_runtime_manifest_v001.py",
)
ROUTE1_DIRECT_INPUTS = (
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md",
    "R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md",
    "BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md",
    "BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md",
    "COMPLETE_ONE_CELL_CTP_KERNEL_GATE_V001.md",
    "STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md",
    "STAGE8_T7_FOUR_AXIS_SCOPE_EXTENSION_ADJUDICATION_RESULT_V001.md",
)
ROUTE1_SEAL_LIST_INPUTS = (
    "stage8_execution/t7_actual_parent_record_amplitude/"
    "T07_ACTUAL_PARENT_RECORD_AMPLITUDE_V001.seal.sha256",
    "STAGE8_T7_SOURCE_SCALARIZATION_NO_GO_RESULT_V001.seal.sha256",
)

WORK = ROOT / "stage8_execution/work"
INDEPENDENT_JSON = (
    WORK
    / "T07_actual_parent_regulated_car_operator_response_"
    "independent_precomparison_v001.json"
)
INDEPENDENT_NPZ = INDEPENDENT_JSON.with_suffix(".npz")
PRIMARY_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_primary_v001.json"
)
PRIMARY_NPZ = PRIMARY_JSON.with_suffix(".npz")
COMPARISON_JSON = (
    WORK / "T07_actual_parent_regulated_car_operator_response_comparison_v001.json"
)
INDEPENDENT_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_independent_execution_receipt_v001.json"
)
PRIMARY_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_primary_execution_receipt_v001.json"
)
COMPARISON_RECEIPT = (
    ROOT
    / "provenance/"
    "stage8_t7_actual_parent_car_comparison_execution_receipt_v001.json"
)

LANE_SEQUENCE = ("independent", "primary", "comparison")

TARGETS = {
    "independent": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py"
    ),
    "primary": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    ),
    "comparison": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v006.py"
    ),
}

LANE_OUTPUTS = {
    "independent": (INDEPENDENT_JSON, INDEPENDENT_NPZ),
    "primary": (PRIMARY_JSON, PRIMARY_NPZ),
    "comparison": (COMPARISON_JSON,),
}

LANE_RECEIPTS = {
    "independent": INDEPENDENT_RECEIPT,
    "primary": PRIMARY_RECEIPT,
    "comparison": COMPARISON_RECEIPT,
}

# ==========================================================================
# GENERATION G7 — the frozen membership.  ONE tag, and every pin in the
# chain must name a member of it (or, for the three bridge pins, a member of
# the bridge generation below).  This is the A1 invariant's data.
# ==========================================================================
GENERATION_TAG = "stage8_t7_generation_g7"
BRIDGE_GENERATION_TAG = "stage8_t7_generation_bridge_v001"

# The byte-frozen derive lanes and their byte-frozen suites are SHARED: they
# are members of the frontier generation AND of the bridge generation, which
# is exactly why the bridge exists.  They are never renamed or reversioned.
FROZEN_DERIVE_MEMBERS = {
    "derive_primary": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    ),
    "derive_independent": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py"
    ),
    "derive_primary_test": (
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "primary_v002.py"
    ),
    "derive_independent_test": (
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_response_"
        "independent_v002.py"
    ),
}

GENERATION_MEMBERS = {
    **FROZEN_DERIVE_MEMBERS,
    "controller": "scripts/run_stage8_t7_actual_parent_car_pipeline_v007.py",
    "launcher": "scripts/launch_stage8_t7_content_addressed_runtime_v007.py",
    "comparator": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v006.py"
    ),
    "manifest": (
        "provenance/"
        "stage8_t7_actual_parent_regulated_car_operator_response_"
        "implementation_v006.json"
    ),
    "controller_test": "scripts/test_stage8_t7_controller_v007.py",
    "launcher_test": "scripts/test_stage8_t7_launcher_v007.py",
    "comparator_test": (
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v006.py"
    ),
    "rehearsal_test": "scripts/test_stage8_t7_real_chain_rehearsal_v001.py",
    "manifest_builder": (
        "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_"
        "v006.py"
    ),
}

# The bridge generation: the row set of the sealed v001-path manifest that
# the byte-frozen derive lanes verify AT CANONICAL PATHS and stamp into
# every bundle.  It is frozen forever; it is NOT the frontier and must
# never be conflated with it.
BRIDGE_GENERATION_MEMBERS = {
    **FROZEN_DERIVE_MEMBERS,
    "controller": "scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py",
    "launcher": "scripts/launch_stage8_t7_content_addressed_runtime_v002.py",
    "comparator": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_"
        "v002.py"
    ),
    "manifest": (
        "provenance/"
        "stage8_t7_actual_parent_regulated_car_operator_response_"
        "implementation_v001.json"
    ),
    "controller_test": "scripts/test_stage8_t7_controller_v002.py",
    "launcher_test": "scripts/test_stage8_t7_launcher_v002.py",
    "comparator_test": (
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v002.py"
    ),
}

# The COMPONENT FAMILIES: frozen (prefix, suffix) patterns that recognise
# ANY generation's member of each family.  A family is how the coherence
# check detects a LAGGING pin: a pin that names
# scripts/launch_..._runtime_v006.py names the "launcher" family with a
# non-member value, and that blocks.  Families are patterns, not lists, so a
# file authored in a future cycle is recognised automatically and cannot
# slip past as an unclassified string.
COMPONENT_FAMILIES = {
    "controller": ("scripts/run_stage8_t7_actual_parent_car_pipeline_v", ".py"),
    "launcher": (
        "scripts/launch_stage8_t7_content_addressed_runtime_v",
        ".py",
    ),
    "comparator": (
        "scripts/compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v",
        ".py",
    ),
    "manifest": (
        "provenance/stage8_t7_actual_parent_regulated_car_operator_response_"
        "implementation_v",
        ".json",
    ),
    "controller_test": ("scripts/test_stage8_t7_controller_v", ".py"),
    "launcher_test": ("scripts/test_stage8_t7_launcher_v", ".py"),
    "comparator_test": (
        "scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_"
        "response_v",
        ".py",
    ),
    "derive_primary": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_"
        "response_primary_v",
        ".py",
    ),
    "derive_independent": (
        "scripts/derive_stage8_t7_actual_parent_regulated_car_operator_"
        "response_independent_v",
        ".py",
    ),
    "derive_primary_test": (
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_"
        "response_primary_v",
        ".py",
    ),
    "derive_independent_test": (
        "scripts/test_stage8_t7_actual_parent_regulated_car_operator_"
        "response_independent_v",
        ".py",
    ),
    "rehearsal_test": ("scripts/test_stage8_t7_real_chain_rehearsal_v", ".py"),
    "manifest_builder": (
        "scripts/build_stage8_t7_actual_parent_car_implementation_manifest_v",
        ".py",
    ),
}

# The twelve-row G7 inventory: controller v007, launcher v007, comparator
# v006, the byte-frozen v002 derive lanes, and the seven remaining G7
# members (test_compare v006, test_launcher v007, test_controller v007, the
# rehearsal suite, the manifest builder, and the two byte-frozen v002
# derive-lane suites).  Derived from GENERATION_MEMBERS so the inventory and
# the coherence table cannot disagree.  The manifest itself is excluded: a
# manifest cannot carry a row for its own bytes.
MANIFEST_EXCLUDED_MEMBER_KEYS = frozenset({"manifest"})
REQUIRED_MANIFEST_ROWS = frozenset(
    path
    for key, path in GENERATION_MEMBERS.items()
    if key not in MANIFEST_EXCLUDED_MEMBER_KEYS
)
# The launcher's allowlist is the manifest inventory minus the launcher: a
# launcher never launches a launcher.
REQUIRED_ALLOWLIST_ROWS = frozenset(
    path
    for key, path in GENERATION_MEMBERS.items()
    if key not in (MANIFEST_EXCLUDED_MEMBER_KEYS | {"launcher"})
)

# ==========================================================================
# THE DIRECTORY-PERMISSION WRITE FENCE (fence record V001, items 1 and 3).
# ==========================================================================
# At rest the two canonical output directories are read-only, so NO route --
# including a superseded controller, a superseded launcher, or a byte-frozen
# derive lane invoked directly -- can create an artifact in them.  This
# controller raises them as its first gated action after ALL preconditions
# pass and drops them on every exit path.  Directory permission bits are not
# hashed by any seal or manifest row, so the fence touches no frozen file.
FENCED_DIRECTORIES = (
    ROOT / "stage8_execution/work",
    ROOT / "provenance",
)
FENCE_AT_REST_MODE = 0o555
FENCE_RAISED_MODE = 0o755
# The permission bits that make a directory writable by anyone.
FENCE_WRITE_BITS = stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH

# ==========================================================================
# A1 GENERATION-COHERENCE TABLE (module-level FROZEN structure).
# ==========================================================================
# Every row is ONE GENERATION PIN THAT EXISTS ON DISK.  The check reads each
# pin from the named file (never from this process's own constants, and never
# by re-deriving the intent -- A3), classifies every path string the pin
# names into a COMPONENT FAMILY, and requires the named path to equal that
# family's member of the pin's declared generation.  A single lagging pin
# therefore fails loudly and by name.
#
# Row fields:
#   file        member key of the file the pin LIVES IN
#   symbol      module-level name to read from that file (source pins), or
#               the literal "@rows" for a manifest's JSON row set
#   generation  "frontier" (generation G7) or "bridge" (the frozen v001
#               manifest's generation)
#   families    the families this pin is REQUIRED to name; a pin that names
#               no member of a required family is an incomplete pin and
#               blocks (this is what stops a bump from orphaning a row)
#   exact       True if the pin's family coverage must be EXACTLY `families`
#               (a set-valued pin such as an allowlist or a manifest row
#               set); False if the pin may name a subset (a scalar pin)
GENERATION_COHERENCE_PINS = (
    {
        "id": "P01_controller_launcher_pin",
        "file": "controller",
        "symbol": "RUNTIME_LAUNCHER",
        "generation": "frontier",
        "families": ("launcher",),
        "exact": True,
    },
    {
        "id": "P02_controller_manifest_pin",
        "file": "controller",
        "symbol": "IMPLEMENTATION_MANIFEST",
        "generation": "frontier",
        "families": ("manifest",),
        "exact": True,
    },
    {
        "id": "P03_controller_bridge_manifest_pin",
        "file": "controller",
        "symbol": "BRIDGE_MANIFEST",
        "generation": "bridge",
        "families": ("manifest",),
        "exact": True,
    },
    {
        "id": "P04_controller_lane_targets_pin",
        "file": "controller",
        "symbol": "TARGETS",
        "generation": "frontier",
        "families": ("derive_primary", "derive_independent", "comparator"),
        "exact": True,
    },
    {
        # The controller's declared generation membership, read from its own
        # bytes on disk.  REQUIRED_MANIFEST_ROWS and REQUIRED_ALLOWLIST_ROWS
        # are DERIVED from this dict in this same file, so pinning the dict
        # pins them; the derivation itself is asserted structurally by
        # verify_pin_table_is_total().
        "id": "P05_controller_generation_membership_pin",
        "file": "controller",
        "symbol": "GENERATION_MEMBERS",
        "generation": "frontier",
        "families": (
            "controller",
            "launcher",
            "comparator",
            "manifest",
            "controller_test",
            "launcher_test",
            "comparator_test",
            "rehearsal_test",
            "manifest_builder",
            "derive_primary",
            "derive_independent",
            "derive_primary_test",
            "derive_independent_test",
        ),
        "exact": True,
    },
    {
        "id": "P06_launcher_allowlist",
        "file": "launcher",
        "symbol": "ALLOWED_TARGETS",
        "generation": "frontier",
        "families": (
            "controller",
            "comparator",
            "controller_test",
            "launcher_test",
            "comparator_test",
            "rehearsal_test",
            "manifest_builder",
            "derive_primary",
            "derive_independent",
            "derive_primary_test",
            "derive_independent_test",
        ),
        "exact": True,
    },
    {
        "id": "P07_comparator_manifest_pin",
        "file": "comparator",
        "symbol": "IMPLEMENTATION_MANIFEST",
        "generation": "frontier",
        "families": ("manifest",),
        "exact": True,
    },
    {
        "id": "P08_comparator_launcher_pin",
        "file": "comparator",
        "symbol": "RUNTIME_LAUNCHER_PATH",
        "generation": "frontier",
        "families": ("launcher",),
        "exact": True,
    },
    {
        "id": "P09_comparator_bundle_binding_pin",
        "file": "comparator",
        "symbol": "BUNDLE_BINDING_MANIFEST",
        "generation": "bridge",
        "families": ("manifest",),
        "exact": True,
    },
    {
        "id": "P10_comparator_executor_paths_pin",
        "file": "comparator",
        "symbol": "EXECUTOR_PATHS",
        "generation": "frontier",
        "families": ("derive_primary", "derive_independent"),
        "exact": True,
    },
    {
        "id": "P11_frontier_manifest_rows",
        "file": "manifest",
        "symbol": "@rows",
        "generation": "frontier",
        "families": (
            "controller",
            "launcher",
            "comparator",
            "controller_test",
            "launcher_test",
            "comparator_test",
            "rehearsal_test",
            "manifest_builder",
            "derive_primary",
            "derive_independent",
            "derive_primary_test",
            "derive_independent_test",
        ),
        "exact": True,
    },
    {
        "id": "P12_bridge_manifest_rows",
        "file": "bridge_manifest",
        "symbol": "@rows",
        "generation": "bridge",
        "families": (
            "controller",
            "launcher",
            "comparator",
            "controller_test",
            "launcher_test",
            "comparator_test",
            "derive_primary",
            "derive_independent",
            "derive_primary_test",
            "derive_independent_test",
        ),
        "exact": True,
    },
    {
        "id": "P13_derive_primary_manifest_pin",
        "file": "derive_primary",
        "symbol": "IMPLEMENTATION_MANIFEST",
        "generation": "bridge",
        "families": ("manifest",),
        "exact": True,
    },
    {
        "id": "P14_derive_independent_manifest_pin",
        "file": "derive_independent",
        "symbol": "IMPLEMENTATION_MANIFEST",
        "generation": "bridge",
        "families": ("manifest",),
        "exact": True,
    },
)

# The FENCE row of the coherence table (fence record item 3): recorded here
# so a future generation bump cannot silently orphan the fence.  It is not a
# path pin, so it carries its own field set and its own checker.
GENERATION_COHERENCE_FENCE_ROW = {
    "id": "P15_directory_permission_write_fence",
    "at_rest_mode": FENCE_AT_REST_MODE,
    "raised_mode": FENCE_RAISED_MODE,
    "fenced_directories": tuple(
        str(directory.relative_to(ROOT)) for directory in FENCED_DIRECTORIES
    ),
    # WHO MAY RAISE: exactly two components, both generation-G7 members.
    "may_raise": (
        GENERATION_MEMBERS["controller"],
        GENERATION_MEMBERS["manifest_builder"],
    ),
    # WHERE THE DROP IS ENFORCED, by name, in this file.
    "drop_enforced_at": (
        "main(): finally path around every lane invocation",
        "main(): signal handlers for SIGINT/SIGTERM/SIGHUP",
        "preflight_fence_at_rest(): L3 self-heal when found writable",
    ),
    "limitations_not_claimed_away": ("L1", "L2", "L3", "L4"),
}

# Every generation the coherence check knows about, by tag.
COHERENCE_GENERATIONS = {
    "frontier": (GENERATION_TAG, GENERATION_MEMBERS),
    "bridge": (BRIDGE_GENERATION_TAG, BRIDGE_GENERATION_MEMBERS),
}

# THE ENUMERATED PRECONDITIONS (sealed discipline rule 2; frozen tuple).
# run_preflight() executes exactly this tuple, in exactly this order, for
# every invocation mode (--preflight-only and production alike); every
# canonical write in this module occurs only in run_lane()/run_comparison_
# lane(), which main() reaches only after run_preflight() has returned
# (provable by the real-component end-to-end tests in
# test_stage8_t7_controller_v006.py).
# Verification order and rationale:
#   1. runtime_attestation      — the launcher's cooperative marker and the
#                                 sealed runtime-manifest digest must be
#                                 present first: nothing else is trusted
#                                 outside the sealed runtime.
#   1a. generation_coherence    — A1: EVERY generation pin in the chain, read
#                                 from disk (controller launcher/manifest/
#                                 bridge/targets/membership pins, launcher
#                                 allowlist, comparator manifest/launcher/
#                                 bridge/executor pins, both manifests' row
#                                 sets, both frozen derive lanes' manifest
#                                 pin) must name the SAME generation.  Runs
#                                 before any manifest verification so a
#                                 lagging pin is named as such, and before
#                                 the fence is touched.
#   1b. fence_at_rest           — fence L3: the fenced directories must be at
#                                 their at-rest read-only mode; if found
#                                 writable they are dropped and the anomaly
#                                 is recorded (self-healing).
#   2. implementation_manifest  — the controller's own sealed v006 manifest:
#                                 adjacent seal, complete ten-row set,
#                                 self-binding, and row-by-row disk
#                                 equality (includes launcher, targets, and
#                                 the v005 comparator row).
#   3. authority_digests        — M2: the sealed Phase-A spec digest and
#                                 every runtime authority digest of the
#                                 derive lanes and comparator, recomputed
#                                 from disk.
#   4. bridge_binding           — FIX 1: the sealed v001-path manifest the
#                                 frozen lanes verify and stamp: adjacent
#                                 seal, derive-executor row equality with
#                                 the own manifest, launcher-on-disk row,
#                                 row-by-row disk equality.
#   5. push_capability          — git push --dry-run to the archive
#                                 repository (pushes nothing, fail-closed).
#   6. prior_receipts           — receipt-existence lane ordering for every
#                                 lane before --lane.
#   7. primary_route1_readiness — M-a/M-b (primary lane; documented no-op
#                                 for the other lanes): the primary derive
#                                 lane's hoisted launch preconditions, in
#                                 the byte-frozen lane's own order — the
#                                 pinned canonical Route-1 result digest,
#                                 the isolated-rerun snapshot absence, and
#                                 the full snapshot input inventory
#                                 (including seal-list children) — all
#                                 verified from disk BEFORE the primary
#                                 lane can consume its canonical path.
#   8. comparison_bundle_stamps — M1 (comparison lane; no-op earlier lanes
#                                 have no bundles): the manifest-stamp
#                                 member of the four hoisted bundle-
#                                 provenance conditions (BLOCKING 3): the
#                                 implementation_manifest_sha256 stamped in
#                                 BOTH lane bundle JSONs on disk equals the
#                                 bridge digest recomputed in step 4.
#   9. comparison_bundle_provenance — BLOCKING 3 (comparison lane; no-op
#                                 earlier lanes): the executor-row,
#                                 launcher-row, and attested-target-hash
#                                 members of comparator v005's per-bundle
#                                 provenance conditions, verified against
#                                 BOTH lane bundle JSONs on disk.
#   9a. comparator_authority    — Part B MAJOR: the comparator's OWN manifest
#                                 authority conditions (its own row equals
#                                 its bytes on disk; neither manifest is a
#                                 symlink), enumerated by reading comparator
#                                 v006's enforcement point.
#  10. canonical_absences       — the lane-appropriate canonical outputs,
#                                 receipts, and seals are absent.
# All THIRTEEN steps precede the first canonical write AND precede the fence
# raise, so no step can run with the canonical directories open.  Steps 6-9a
# additionally precede any consumption of the canonical comparison path; step
# 7 additionally precedes any consumption of the canonical primary path.
PRECONDITIONS = (
    "runtime_attestation",
    "generation_coherence",
    "fence_at_rest",
    "implementation_manifest",
    "authority_digests",
    "bridge_binding",
    "push_capability",
    "prior_receipts",
    "primary_route1_readiness",
    "comparison_bundle_stamps",
    "comparison_bundle_provenance",
    "comparator_authority",
    "canonical_absences",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def strict_json(path: Path) -> dict[str, Any]:
    def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    value = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=object_pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(
            RuntimeError(f"non-finite JSON constant in {path}: {value}")
        ),
    )
    require(isinstance(value, dict), f"JSON document is not an object: {path}")
    return value


def atomic_sealed_json(path: Path, payload: dict[str, Any]) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(not path.exists(), f"immutable receipt already exists: {path}")
    require(not seal.exists(), f"immutable receipt seal already exists: {seal}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)
    digest = sha256(path)
    seal_temporary = seal.with_suffix(seal.suffix + ".tmp")
    seal_temporary.write_text(f"{digest}  {path.name}\n", encoding="ascii")
    os.replace(seal_temporary, seal)
    for artifact in (path, seal):
        artifact.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return digest


def verify_adjacent_seal(path: Path) -> str:
    seal = Path(f"{path}.seal.sha256")
    require(path.is_file(), f"expected output is absent: {path}")
    require(seal.is_file(), f"expected output seal is absent: {seal}")
    fields = seal.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, f"malformed output seal: {seal}")
    digest = sha256(path)
    require(fields[0] == digest, f"output seal digest mismatch: {path}")
    require(fields[1] == path.name, f"output seal filename mismatch: {path}")
    return digest


# --------------------------------------------------------------------------
# A1 GENERATION-COHERENCE CHECK (the systemic fix).
#
# Reads every pin of GENERATION_COHERENCE_PINS from the file it lives in, on
# disk, and requires the set of component paths it names to be EXACTLY the
# declared generation's members of the declared families.  Nothing is
# re-derived from intent: source pins are read out of the file's own bytes
# with ast (no import, no exec, so reading a pin can never run code), and
# manifest pins are read out of the manifest JSON.
# --------------------------------------------------------------------------


def normalise_relative(value: str) -> str:
    return value.replace("//", "/").strip("/")


def resolve_path_literals(node: ast.AST) -> set[str]:
    """Collect every ROOT-relative path literal a pin expression names.

    Handles exactly the shapes the production pins use: string constants
    (including implicit concatenation, which the parser already folds),
    `ROOT / "a" / "b"` path joins, string addition, set/frozenset/tuple/list
    literals, and dict literals (keys and values, plus ** unpacking of
    another dict literal).  Anything else contributes nothing, so an
    unrecognised shape shows up as an ABSENT family and blocks -- it can
    never be silently accepted.
    """
    if isinstance(node, ast.Constant):
        return {node.value} if isinstance(node.value, str) else set()
    if isinstance(node, ast.Name):
        # ROOT is the clean-room root, i.e. the empty relative prefix.
        return {""} if node.id == "ROOT" else set()
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.Add)):
        left = resolve_path_literals(node.left)
        right = resolve_path_literals(node.right)
        if not left or not right:
            return set()
        separator = "/" if isinstance(node.op, ast.Div) else ""
        joined: set[str] = set()
        for prefix in left:
            for suffix in right:
                if prefix == "":
                    joined.add(normalise_relative(suffix))
                else:
                    joined.add(normalise_relative(prefix + separator + suffix))
        return joined
    if isinstance(node, (ast.Set, ast.List, ast.Tuple)):
        collected: set[str] = set()
        for element in node.elts:
            collected |= resolve_path_literals(element)
        return collected
    if isinstance(node, ast.Dict):
        collected = set()
        for key, value in zip(node.keys, node.values):
            if key is None:
                # ** unpacking of another dict literal or of a Name we cannot
                # resolve here; the Name case contributes nothing and shows
                # up as an absent family.
                collected |= resolve_path_literals(value)
                continue
            collected |= resolve_path_literals(key)
            collected |= resolve_path_literals(value)
        return collected
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id in {"frozenset", "set", "tuple", "list", "dict", "Path"}:
            collected = set()
            for argument in node.args:
                collected |= resolve_path_literals(argument)
            return collected
    return set()


def read_source_pin(path: Path, symbol: str) -> set[str]:
    """Read one module-level pin out of a file's bytes on disk.

    The file is PARSED, never imported and never executed, so reading a pin
    from a foreign generation cannot run that generation's code.  A symbol
    that is absent, or assigned more than once at module level, blocks: an
    ambiguous pin is not a pin.
    """
    require(path.is_file(), f"coherence: pin source is absent: {path}")
    try:
        tree = ast.parse(path.read_bytes(), filename=str(path))
    except SyntaxError as error:
        raise RuntimeError(f"coherence: pin source does not parse: {path}: {error}")
    values: list[ast.AST] = []
    for statement in tree.body:
        targets: list[ast.expr] = []
        if isinstance(statement, ast.Assign):
            targets = list(statement.targets)
        elif isinstance(statement, ast.AnnAssign):
            targets = [statement.target]
        for target in targets:
            if isinstance(target, ast.Name) and target.id == symbol:
                require(
                    getattr(statement, "value", None) is not None,
                    f"coherence: pin {symbol} has no value in {path.name}",
                )
                values.append(statement.value)
    require(
        len(values) == 1,
        f"coherence: pin {symbol} is assigned {len(values)} times at module "
        f"level in {path.name}; exactly one assignment is required",
    )
    # A dict-literal pin that ** -unpacks a Name (GENERATION_MEMBERS unpacks
    # FROZEN_DERIVE_MEMBERS) is resolved by also resolving that Name's own
    # module-level assignment, so the pin's full membership is read from disk.
    resolved = resolve_path_literals(values[0])
    for unpacked in unpacked_names(values[0]):
        resolved |= read_source_pin(path, unpacked)
    return {normalise_relative(value) for value in resolved if value}


def unpacked_names(node: ast.AST) -> tuple[str, ...]:
    if not isinstance(node, ast.Dict):
        return ()
    names: list[str] = []
    for key, value in zip(node.keys, node.values):
        if key is None and isinstance(value, ast.Name):
            names.append(value.id)
    return tuple(names)


def read_manifest_row_pin(path: Path) -> set[str]:
    """Read a manifest's row-path set from the manifest JSON on disk."""
    require(path.is_file(), f"coherence: manifest pin source is absent: {path}")
    manifest = strict_json(path)
    rows = manifest.get("files")
    require(
        isinstance(rows, list) and bool(rows),
        f"coherence: manifest pin source has no rows: {path.name}",
    )
    return {normalise_relative(str(row["path"])) for row in rows}


def family_of(relative: str) -> str | None:
    """Classify a path into exactly one component family, or None."""
    matches = [
        family
        for family, (prefix, suffix) in COMPONENT_FAMILIES.items()
        if relative.startswith(prefix) and relative.endswith(suffix)
    ]
    require(
        len(matches) <= 1,
        f"coherence: path classifies into multiple component families "
        f"{sorted(matches)}: {relative}; the family patterns are ambiguous",
    )
    return matches[0] if matches else None


def pin_source_path(file_key: str) -> Path:
    if file_key == "bridge_manifest":
        return ROOT / BRIDGE_GENERATION_MEMBERS["manifest"]
    require(
        file_key in GENERATION_MEMBERS,
        f"coherence: pin table names an unknown file key: {file_key}",
    )
    return ROOT / GENERATION_MEMBERS[file_key]


def verify_pin_table_is_total() -> None:
    """Structural guard against an ORPHANED ROW on a future bump.

    Requires: every component family has a frontier member; every family is
    named by at least one pin; every pin's declared families exist; the
    derived row/allowlist sets are exactly the declared derivations; and the
    fence row is present with both fenced directories.  A future generation
    that adds a component family without adding it to this table therefore
    blocks here instead of running with an unchecked pin.
    """
    for family in COMPONENT_FAMILIES:
        require(
            family in GENERATION_MEMBERS,
            f"coherence: component family {family} has no generation member",
        )
    covered: set[str] = set()
    for pin in GENERATION_COHERENCE_PINS:
        require(bool(pin["families"]), f"coherence: pin {pin['id']} declares no family")
        require(
            pin["exact"] is True,
            f"coherence: pin {pin['id']} is not an exact pin; every pin in "
            "this table must be exact",
        )
        require(
            pin["generation"] in COHERENCE_GENERATIONS,
            f"coherence: pin {pin['id']} names an unknown generation",
        )
        for family in pin["families"]:
            require(
                family in COMPONENT_FAMILIES,
                f"coherence: pin {pin['id']} names an unknown family: {family}",
            )
            covered.add(family)
    orphaned = sorted(set(COMPONENT_FAMILIES) - covered)
    require(
        not orphaned,
        f"coherence: component families are not covered by any pin: {orphaned}",
    )
    require(
        REQUIRED_MANIFEST_ROWS
        == frozenset(
            path
            for key, path in GENERATION_MEMBERS.items()
            if key not in MANIFEST_EXCLUDED_MEMBER_KEYS
        ),
        "coherence: REQUIRED_MANIFEST_ROWS is not the declared derivation of "
        "GENERATION_MEMBERS",
    )
    require(
        REQUIRED_ALLOWLIST_ROWS
        == frozenset(
            path
            for key, path in GENERATION_MEMBERS.items()
            if key not in (MANIFEST_EXCLUDED_MEMBER_KEYS | {"launcher"})
        ),
        "coherence: REQUIRED_ALLOWLIST_ROWS is not the declared derivation of "
        "GENERATION_MEMBERS",
    )
    require(
        tuple(GENERATION_COHERENCE_FENCE_ROW["fenced_directories"])
        == tuple(
            str(directory.relative_to(ROOT)) for directory in FENCED_DIRECTORIES
        ),
        "coherence: the fence row does not enumerate the fenced directories",
    )
    require(
        GENERATION_MEMBERS["controller"]
        in GENERATION_COHERENCE_FENCE_ROW["may_raise"],
        "coherence: the fence row does not name this controller as a raiser",
    )


def evaluate_generation_coherence() -> dict[str, Any]:
    """Read EVERY pin from disk and require ONE coherent generation.

    Returns the evaluated table (pin id -> named paths) for recording.
    Raises RuntimeError naming the offending pin, the family, the value it
    names and the value the generation requires, on the FIRST incoherence.
    """
    verify_pin_table_is_total()
    evaluated: dict[str, Any] = {
        "generation_tag": GENERATION_TAG,
        "bridge_generation_tag": BRIDGE_GENERATION_TAG,
        "pins": {},
    }
    for pin in GENERATION_COHERENCE_PINS:
        generation_tag, members = COHERENCE_GENERATIONS[pin["generation"]]
        source = pin_source_path(pin["file"])
        if pin["symbol"] == "@rows":
            named = read_manifest_row_pin(source)
        else:
            named = read_source_pin(source, pin["symbol"])
        classified = {
            value: family_of(value)
            for value in sorted(named)
            if family_of(value) is not None
        }
        expected: dict[str, str] = {}
        for family in pin["families"]:
            require(
                family in members,
                f"coherence: pin {pin['id']} requires family {family}, which "
                f"generation {generation_tag} does not define",
            )
            expected[members[family]] = family
        for value, family in sorted(classified.items()):
            required = members.get(family)
            require(
                value == required,
                f"GENERATION INCOHERENCE at pin {pin['id']} "
                f"(read from {source.name}, symbol {pin['symbol']}, "
                f"generation {generation_tag}): it names {value!r} for the "
                f"{family} family, but this generation's {family} is "
                f"{required!r}. THIS IS THE LAGGING-PIN DEFECT; the pin must "
                "be advanced in the same change as the generation bump.",
            )
        missing = sorted(set(expected) - set(classified))
        require(
            not missing,
            f"GENERATION INCOHERENCE at pin {pin['id']} "
            f"(read from {source.name}, symbol {pin['symbol']}): it does not "
            f"name the required generation members {missing}. An incomplete "
            "pin is an orphaned row and blocks.",
        )
        extra = sorted(set(classified) - set(expected))
        require(
            not extra,
            f"GENERATION INCOHERENCE at pin {pin['id']} "
            f"(read from {source.name}, symbol {pin['symbol']}): it also "
            f"names {extra}, which generation {generation_tag} does not "
            "include. A pin that spans generations is the wedge B1 named.",
        )
        evaluated["pins"][pin["id"]] = {
            "source": str(source.relative_to(ROOT)),
            "symbol": pin["symbol"],
            "generation": generation_tag,
            "named": sorted(classified),
        }
    evaluated["fence_row"] = dict(GENERATION_COHERENCE_FENCE_ROW)
    return evaluated


# --------------------------------------------------------------------------
# THE DIRECTORY-PERMISSION WRITE FENCE.
# --------------------------------------------------------------------------


def directory_mode(directory: Path) -> int:
    return stat.S_IMODE(directory.stat().st_mode)


def fence_is_writable(directory: Path) -> bool:
    return bool(directory_mode(directory) & FENCE_WRITE_BITS)


def drop_fence() -> list[str]:
    """Return every fenced directory to its at-rest read-only mode.

    Called from the finally path, from the signal handlers, and from the L3
    self-heal.  Idempotent, and never raises for a directory that is already
    at rest, so it is safe on every failure path.
    """
    dropped: list[str] = []
    for directory in FENCED_DIRECTORIES:
        if not directory.is_dir():
            continue
        if directory_mode(directory) != FENCE_AT_REST_MODE:
            directory.chmod(FENCE_AT_REST_MODE)
            dropped.append(str(directory.relative_to(ROOT)))
    return dropped


def raise_fence() -> list[str]:
    """Raise write permission on the fenced directories.

    THE FIRST GATED ACTION AFTER ALL PRECONDITIONS PASS, and the only place
    in this module that grants write permission anywhere.
    """
    raised: list[str] = []
    for directory in FENCED_DIRECTORIES:
        require(
            directory.is_dir(),
            f"fence: fenced directory is absent: {directory.relative_to(ROOT)}",
        )
        directory.chmod(FENCE_RAISED_MODE)
        require(
            fence_is_writable(directory),
            f"fence: raise did not take effect: {directory.relative_to(ROOT)}",
        )
        raised.append(str(directory.relative_to(ROOT)))
    return raised


def install_fence_signal_handlers() -> None:
    """Drop the fence on SIGINT/SIGTERM/SIGHUP.

    This narrows -- it does NOT close -- the L3 hard-kill window: SIGKILL
    cannot be caught, so the L3 pre-flight self-heal remains the mitigation
    of record.  Driven by test_stage8_t7_controller_v007.py::
    test_l3_sigterm_during_the_raised_window_drops_the_fence.
    """

    def handler(signal_number: int, frame: Any) -> None:
        drop_fence()
        raise SystemExit(128 + signal_number)

    for signal_name in ("SIGINT", "SIGTERM", "SIGHUP"):
        signal_number = getattr(signal, signal_name, None)
        if signal_number is not None:
            signal.signal(signal_number, handler)


# --------------------------------------------------------------------------
# Precondition steps (each takes the lane and the shared pre-flight context;
# dispatched by run_preflight() in PRECONDITIONS order).
# --------------------------------------------------------------------------


def preflight_runtime_attestation(lane: str, context: dict[str, Any]) -> None:
    attestation = getattr(sys, RUNTIME_MARKER, None)
    require(
        isinstance(attestation, dict),
        "pipeline requires the sealed runtime launcher",
    )
    require(
        attestation.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        "pipeline runtime manifest mismatch",
    )


def preflight_generation_coherence(lane: str, context: dict[str, Any]) -> None:
    """A1: read EVERY generation pin from disk and block unless they all name
    the frozen generation.  Runs before the implementation manifest is
    verified and before the fence is touched, so a lagging pin is reported as
    a named coherence failure rather than as an opaque row mismatch."""
    context["generation_coherence"] = evaluate_generation_coherence()


def preflight_fence_at_rest(lane: str, context: dict[str, Any]) -> None:
    """Fence limitation L3: assert the at-rest read-only state, and SELF-HEAL.

    If a fenced directory is found writable -- the signature of a hard-kill
    between a previous raise and its drop, or of a manual chmod (L2) -- the
    fence is DROPPED here and the anomaly is RECORDED before anything
    proceeds.  The anomaly is carried in this invocation's JSON output and,
    for a production invocation, in the sealed lane receipt, so a legitimate
    run leaves an auditable trace of why the state was open.  This step
    writes no artifact; it only changes directory permission bits, which no
    seal or manifest row covers.
    """
    anomalies: list[dict[str, Any]] = []
    for directory in FENCED_DIRECTORIES:
        require(
            directory.is_dir(),
            f"fence pre-flight: fenced directory is absent: "
            f"{directory.relative_to(ROOT)}",
        )
        mode = directory_mode(directory)
        if mode != FENCE_AT_REST_MODE:
            anomalies.append(
                {
                    "directory": str(directory.relative_to(ROOT)),
                    "observed_mode": f"{mode:04o}",
                    "expected_at_rest_mode": f"{FENCE_AT_REST_MODE:04o}",
                    "writable_at_rest": bool(mode & FENCE_WRITE_BITS),
                    "action": "dropped_to_at_rest_mode",
                    "cause_class": (
                        "hard-kill window (L3) or manual chmod (L2); this "
                        "invocation self-healed the invariant"
                    ),
                }
            )
    if anomalies:
        drop_fence()
        for directory in FENCED_DIRECTORIES:
            require(
                directory_mode(directory) == FENCE_AT_REST_MODE,
                "fence pre-flight: self-heal did not restore the at-rest mode: "
                f"{directory.relative_to(ROOT)}",
            )
    context["fence_anomalies"] = anomalies


def preflight_implementation_manifest(lane: str, context: dict[str, Any]) -> None:
    require(
        IMPLEMENTATION_MANIFEST.is_file(),
        "implementation manifest is absent: "
        f"{IMPLEMENTATION_MANIFEST.relative_to(ROOT)}",
    )
    require(
        IMPLEMENTATION_SEAL.is_file(),
        f"implementation seal is absent: {IMPLEMENTATION_SEAL.relative_to(ROOT)}",
    )
    manifest_digest = sha256(IMPLEMENTATION_MANIFEST)
    fields = IMPLEMENTATION_SEAL.read_text(encoding="ascii").strip().split()
    require(len(fields) == 2, "malformed implementation seal")
    require(fields[0] == manifest_digest, "implementation seal digest mismatch")
    manifest = strict_json(IMPLEMENTATION_MANIFEST)
    rows = manifest.get("files")
    require(
        isinstance(rows, list) and bool(rows),
        "implementation file inventory is empty",
    )
    row_map = {str(row["path"]): str(row["sha256"]) for row in rows}
    missing_rows = sorted(REQUIRED_MANIFEST_ROWS - set(row_map))
    require(
        not missing_rows,
        f"implementation manifest is missing required rows: {missing_rows}",
    )
    require(
        row_map.get(str(SELF.relative_to(ROOT))) == sha256(SELF),
        "pipeline is not implementation-bound",
    )
    for relative, expected in row_map.items():
        path = ROOT / relative
        require(path.is_file(), f"implementation input is absent: {relative}")
        require(sha256(path) == expected, f"implementation drift: {relative}")
    require(
        (ROOT / TARGETS["comparison"]).is_file(),
        "v005 comparator is not reachable",
    )
    context["implementation_digest"] = manifest_digest
    context["implementation_rows"] = row_map


def preflight_authority_digests(lane: str, context: dict[str, Any]) -> None:
    """M2: recompute, from disk, the sealed Phase-A spec digest and every
    authority digest the byte-frozen derive lanes and the comparator verify
    at runtime, BEFORE any canonical consumption in any lane."""
    spec = ROOT / SPEC_RELATIVE
    require(
        spec.is_file(),
        f"authority pre-flight: sealed Phase-A spec is absent: {SPEC_RELATIVE}",
    )
    require(
        sha256(spec) == SPEC_SHA256,
        f"authority pre-flight: sealed Phase-A spec digest mismatch: {SPEC_RELATIVE}",
    )
    for relative, expected in sorted(AUTHORITY_DIGESTS.items()):
        path = ROOT / relative
        require(
            path.is_file(),
            f"authority pre-flight: authority is absent: {relative}",
        )
        require(
            sha256(path) == expected,
            f"authority pre-flight: authority digest mismatch: {relative}",
        )


def preflight_bridge_binding(lane: str, context: dict[str, Any]) -> None:
    """FIX 1 bridge pre-flight (retained from v004): verify the manifest-
    binding bridge condition from disk BEFORE any lane runs.

    The byte-frozen derive lanes verify and stamp the sealed manifest at the
    canonical v001 path; the comparator accepts exactly bundles whose
    stamped digest equals that manifest's recomputed digest AND whose
    executing code's authority rows agree with the comparator's own
    manifest. This pre-flight proves, before any canonical path is
    consumed: the v001-path manifest is sealed on disk with a verifying
    adjacent seal (digest recomputed, not copied); the derive-lane executor
    rows are hash-equal row-by-row across the v001-path manifest and this
    controller's own manifest; the own-manifest launcher row equals the
    launcher on disk (the hash the runtime attestation will record); and
    every v001-path manifest row matches its on-disk file, so the frozen
    lanes' own manifest verification cannot fail later. The bundle-stamp
    member of the bridge condition is verified by the comparison_bundle_
    stamps step against the digest recorded here. Failure blocks with zero
    artifacts.
    """
    implementation_rows = context["implementation_rows"]
    require(
        BRIDGE_MANIFEST.is_file(),
        "bridge pre-flight: v001-path implementation manifest is absent",
    )
    require(
        BRIDGE_SEAL.is_file(),
        "bridge pre-flight: v001-path implementation seal is absent",
    )
    bridge_digest = sha256(BRIDGE_MANIFEST)
    fields = BRIDGE_SEAL.read_text(encoding="ascii").strip().split()
    require(
        len(fields) == 2,
        "bridge pre-flight: malformed v001-path implementation seal",
    )
    require(
        fields[0] == bridge_digest,
        "bridge pre-flight: v001-path implementation seal digest mismatch",
    )
    require(
        fields[1] == BRIDGE_MANIFEST.name,
        "bridge pre-flight: v001-path implementation seal filename mismatch",
    )
    bridge = strict_json(BRIDGE_MANIFEST)
    rows = bridge.get("files")
    require(
        isinstance(rows, list) and bool(rows),
        "bridge pre-flight: v001-path implementation file inventory is empty",
    )
    bridge_rows = {str(row["path"]): str(row["sha256"]) for row in rows}
    for relative in (TARGETS["independent"], TARGETS["primary"]):
        require(
            relative in bridge_rows,
            f"bridge pre-flight: v001-path manifest lacks the executor row: {relative}",
        )
        require(
            relative in implementation_rows,
            f"bridge pre-flight: own manifest lacks the executor row: {relative}",
        )
        require(
            bridge_rows[relative] == implementation_rows[relative],
            f"bridge pre-flight: manifest row mismatch for {relative}",
        )
    launcher_relative = str(RUNTIME_LAUNCHER.relative_to(ROOT))
    require(
        implementation_rows.get(launcher_relative) == sha256(RUNTIME_LAUNCHER),
        "bridge pre-flight: launcher row inconsistent with the launcher on disk: "
        f"{launcher_relative}",
    )
    for relative, expected in sorted(bridge_rows.items()):
        path = ROOT / relative
        require(
            path.is_file(),
            f"bridge pre-flight: v001-path implementation input is absent: {relative}",
        )
        require(
            sha256(path) == expected,
            f"bridge pre-flight: v001-path implementation drift: {relative}",
        )
    context["bridge_digest"] = bridge_digest


def preflight_push_capability(lane: str, context: dict[str, Any]) -> None:
    """Retained from v004: prove push capability to the archive repository
    BEFORE any canonical path is consumed, fail-closed. A push failure
    discovered only after sealing would reproduce the GPG wedge (sealed
    artifacts that cannot be anchored). The dry run pushes nothing."""
    require(
        ARCHIVE_REPOSITORY.is_dir(),
        f"push-capability pre-flight: archive repository is absent: "
        f"{ARCHIVE_REPOSITORY}",
    )
    completed = subprocess.run(
        [
            "git",
            "-C",
            str(ARCHIVE_REPOSITORY),
            "push",
            "--dry-run",
            "origin",
            "main",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    require(
        completed.returncode == 0,
        "push-capability pre-flight failed "
        f"(returncode {completed.returncode}); anchoring would wedge after "
        f"sealing: {completed.stderr[-2000:]}",
    )


def preflight_prior_receipts(lane: str, context: dict[str, Any]) -> None:
    lane_index = LANE_SEQUENCE.index(lane)
    for prior_lane in LANE_SEQUENCE[:lane_index]:
        verify_prior_receipt(prior_lane)


def preflight_primary_route1_readiness(lane: str, context: dict[str, Any]) -> None:
    """M-a/M-b: the primary derive lane's hoisted launch preconditions.

    The byte-frozen primary lane (derive_stage8_t7_actual_parent_
    regulated_car_operator_response_primary_v002.py, isolated_route1_
    rerun()) verifies, in this order: the pinned digest of the canonical
    Route-1 result, the absence of the immutable isolated-rerun snapshot,
    and the existence of every snapshot input (the fixed, direct, and
    seal-list files plus every child path the two seal-list files
    enumerate).  Inside the lane any such failure surfaces only after
    write_blocked_result has permanently consumed the canonical primary
    output path, so this step verifies all three preconditions from disk,
    in the lane's own order, BEFORE the primary lane runs.  The ROUTE1_*
    constants mirror the byte-frozen lane's literals exactly.  Documented
    no-op for the independent and comparison lanes: the independent lane
    performs no Route-1 rerun, and by the comparison lane the snapshot
    legitimately exists (the primary lane created it)."""
    if lane != "primary":
        return
    require(
        ROUTE1_CANONICAL_RESULT.is_file(),
        "route1 pre-flight: canonical Route-1 result is absent: "
        f"{ROUTE1_CANONICAL_RESULT.relative_to(ROOT)}",
    )
    require(
        sha256(ROUTE1_CANONICAL_RESULT) == ROUTE1_CANONICAL_SHA256,
        "route1 pre-flight: canonical Route-1 result digest mismatch: "
        f"{ROUTE1_CANONICAL_RESULT.relative_to(ROOT)}",
    )
    require(
        not ROUTE1_SNAPSHOT_DIRECTORY.exists(),
        "route1 pre-flight: immutable isolated Route-1 snapshot already "
        f"exists: {ROUTE1_SNAPSHOT_DIRECTORY.relative_to(ROOT)}",
    )
    inventory: list[str] = list(
        ROUTE1_FIXED_INPUTS + ROUTE1_DIRECT_INPUTS + ROUTE1_SEAL_LIST_INPUTS
    )
    for seal_list in ROUTE1_SEAL_LIST_INPUTS:
        path = ROOT / seal_list
        require(
            path.is_file(),
            f"route1 pre-flight: snapshot input is absent: {seal_list}",
        )
        for line in path.read_text(encoding="ascii").splitlines():
            if line.strip():
                _, child = line.split(maxsplit=1)
                inventory.append(child)
    seen: set[str] = set()
    for relative in inventory:
        if relative in seen:
            continue
        seen.add(relative)
        require(
            (ROOT / relative).is_file(),
            f"route1 pre-flight: snapshot input is absent: {relative}",
        )


def preflight_comparison_bundle_stamps(lane: str, context: dict[str, Any]) -> None:
    """M1: the bundle-stamp member of the bridge condition. For the
    comparison lane, the implementation_manifest_sha256 stamped in BOTH
    lane bundle JSONs on disk must equal the v001-path manifest digest
    recomputed by the bridge_binding step in THIS invocation, so a bundle
    regenerated against a different manifest between invocations cannot
    reach the comparator. Earlier lanes have no bundles yet; the step is a
    documented no-op for them."""
    if lane != "comparison":
        return
    bridge_digest = context["bridge_digest"]
    for bundle_lane, bundle_json in (
        ("independent", INDEPENDENT_JSON),
        ("primary", PRIMARY_JSON),
    ):
        require(
            bundle_json.is_file(),
            f"bundle-stamp pre-flight: {bundle_lane} bundle JSON is absent: "
            f"{bundle_json.relative_to(ROOT)}",
        )
        payload = strict_json(bundle_json)
        stamped = payload.get("implementation_manifest_sha256")
        require(
            stamped == bridge_digest,
            f"bundle-stamp pre-flight: {bundle_lane} bundle stamp does not "
            "equal the recomputed v001-path manifest digest",
        )


def preflight_comparison_bundle_provenance(
    lane: str, context: dict[str, Any]
) -> None:
    """BLOCKING 3: the executor-row, launcher-row, and attested-target-
    hash members of comparator v005's per-bundle provenance conditions,
    hoisted into the comparison-lane pre-flight (the manifest-stamp
    member is the comparison_bundle_stamps step).  BOTH lane bundle JSONs
    on disk must record: executor_sha256 equal to the manifest row of
    that lane's executor; a runtime_attestation whose launcher_sha256
    equals the manifest's launcher row; and whose target_sha256 equals
    the executor row — the exact equalities comparator v005 enforces —
    all BEFORE the canonical comparison path is consumed.  The manifest
    rows come from the sealed manifest verified row-by-row against disk
    in the implementation_manifest step; the comparator re-verifies the
    same conditions at runtime against its own sealed manifest, which its
    own row-by-row disk equality pins to the identical digests.  Earlier
    lanes have no bundles yet; the step is a documented no-op for them."""
    if lane != "comparison":
        return
    implementation_rows = context["implementation_rows"]
    launcher_relative = str(RUNTIME_LAUNCHER.relative_to(ROOT))
    launcher_row = implementation_rows.get(launcher_relative)
    require(
        isinstance(launcher_row, str) and bool(launcher_row),
        "comparison-provenance pre-flight: runtime-launcher manifest row "
        "is absent",
    )
    for bundle_lane, bundle_json in (
        ("independent", INDEPENDENT_JSON),
        ("primary", PRIMARY_JSON),
    ):
        executor_relative = TARGETS[bundle_lane]
        executor_row = implementation_rows.get(executor_relative)
        require(
            isinstance(executor_row, str) and bool(executor_row),
            f"comparison-provenance pre-flight: {bundle_lane} executor "
            "manifest row is absent",
        )
        require(
            bundle_json.is_file(),
            f"comparison-provenance pre-flight: {bundle_lane} bundle JSON "
            f"is absent: {bundle_json.relative_to(ROOT)}",
        )
        payload = strict_json(bundle_json)
        require(
            payload.get("executor_sha256") == executor_row,
            f"comparison-provenance pre-flight: {bundle_lane} bundle "
            "executor provenance mismatch",
        )
        attestation = payload.get("runtime_attestation")
        require(
            isinstance(attestation, dict),
            f"comparison-provenance pre-flight: {bundle_lane} bundle "
            "runtime attestation is absent",
        )
        require(
            attestation.get("launcher_sha256") == launcher_row,
            f"comparison-provenance pre-flight: {bundle_lane} bundle "
            "runtime-launcher provenance mismatch",
        )
        require(
            attestation.get("target_sha256") == executor_row,
            f"comparison-provenance pre-flight: {bundle_lane} bundle "
            "runtime-attestation target-hash binding mismatch",
        )


def preflight_comparator_authority(lane: str, context: dict[str, Any]) -> None:
    """Part B MAJOR: hoist the COMPARATOR'S OWN authority verification.

    Enumerated by READING comparator v006's enforcement point (A3), not by
    re-deriving intent.  Comparator v006's verify_implementation_manifest()
    requires, in order: its manifest is a file; the adjacent seal is a file;
    the seal has two fields; the recomputed manifest digest equals the seal's
    first field; the manifest parses strictly; its `files` list is non-empty;
    THE COMPARATOR'S OWN ROW EQUALS THE COMPARATOR ON DISK; and every row is
    hash-equal to its file on disk.  Its verify_bundle_binding_bridge()
    additionally requires the v001-path manifest NOT to be a symlink, and
    its seal's filename field to equal the manifest's name.

    Of those, the comparator's own-row condition and the symlink refusal are
    NOT implied by this controller's implementation_manifest and
    bridge_binding steps, which pin the CONTROLLER's own row.  Both are
    checked here, against the SAME manifests -- which the generation-
    coherence check has already proved are the same files the comparator
    pins.  Comparator v006 also hoists these into its own prologue, ahead of
    the try that seals a BLOCKED verdict; the two hoists are the same
    conditions on the same manifests.

    Runs for EVERY lane, not only the comparison lane: the check is cheap,
    and discovering the comparator's authority skew before the first derive
    lane runs is strictly better than discovering it two lanes later.
    """
    comparator_relative = TARGETS["comparison"]
    comparator = ROOT / comparator_relative
    require(
        comparator.is_file(),
        f"comparator-authority pre-flight: comparator is absent: "
        f"{comparator_relative}",
    )
    row_map = context["implementation_rows"]
    require(
        row_map.get(comparator_relative) == sha256(comparator),
        "comparator-authority pre-flight: the comparator is not the presealed "
        "implementation (its own manifest row does not equal its bytes on "
        f"disk): {comparator_relative}",
    )
    require(
        not BRIDGE_MANIFEST.is_symlink(),
        "comparator-authority pre-flight: the v001-path bundle-binding "
        "manifest may not be a symlink",
    )
    require(
        not IMPLEMENTATION_MANIFEST.is_symlink(),
        "comparator-authority pre-flight: the implementation manifest may not "
        "be a symlink",
    )


def preflight_canonical_absences(lane: str, context: dict[str, Any]) -> None:
    """Verify absence of every canonical output and receipt that must not yet
    exist before this lane runs, and record the exact list verified (written
    into the receipt as paths_verified_absent)."""
    lane_index = LANE_SEQUENCE.index(lane)
    pending = LANE_SEQUENCE[lane_index:]
    checked: list[Path] = []
    for pending_lane in pending:
        checked.extend(LANE_OUTPUTS[pending_lane])
    for pending_lane in pending:
        checked.append(LANE_RECEIPTS[pending_lane])
    for path in checked:
        require(
            not path.exists(),
            f"pre-flight: canonical path already exists before the {lane} lane: {path}",
        )
        require(
            not Path(f"{path}.seal.sha256").exists(),
            f"pre-flight: canonical seal already exists before the {lane} lane: {path}",
        )
    context["paths_verified_absent"] = [
        str(path.relative_to(ROOT)) for path in checked
    ]


PRECONDITION_STEPS: dict[str, Callable[[str, dict[str, Any]], None]] = {
    "runtime_attestation": preflight_runtime_attestation,
    "generation_coherence": preflight_generation_coherence,
    "fence_at_rest": preflight_fence_at_rest,
    "implementation_manifest": preflight_implementation_manifest,
    "authority_digests": preflight_authority_digests,
    "bridge_binding": preflight_bridge_binding,
    "push_capability": preflight_push_capability,
    "prior_receipts": preflight_prior_receipts,
    "primary_route1_readiness": preflight_primary_route1_readiness,
    "comparison_bundle_stamps": preflight_comparison_bundle_stamps,
    "comparison_bundle_provenance": preflight_comparison_bundle_provenance,
    "comparator_authority": preflight_comparator_authority,
    "canonical_absences": preflight_canonical_absences,
}
# Structural guard: the frozen tuple and the dispatch table may never drift.
assert set(PRECONDITIONS) == set(PRECONDITION_STEPS)
assert len(PRECONDITIONS) == len(set(PRECONDITIONS))


def fence_state() -> dict[str, str]:
    """The observed mode of each fenced directory, for the record."""
    return {
        str(directory.relative_to(ROOT)): (
            f"{directory_mode(directory):04o}" if directory.is_dir() else "absent"
        )
        for directory in FENCED_DIRECTORIES
    }


def run_preflight(lane: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
    """Execute EVERY enumerated precondition, in PRECONDITIONS order, for
    the given lane. Writes no artifact anywhere (the fence L3 self-heal may
    drop directory permission bits; see preflight_fence_at_rest). Every
    canonical write in this module happens only after this function has
    returned AND the fence has been raised.

    The caller may pass the context dict so that partial results -- notably
    the recorded fence anomalies -- survive a block and can be reported.
    """
    if context is None:
        context = {}
    for name in PRECONDITIONS:
        PRECONDITION_STEPS[name](lane, context)
    return context


def verify_prior_receipt(lane: str) -> tuple[str, dict[str, Any]]:
    receipt = LANE_RECEIPTS[lane]
    require(
        receipt.is_file(),
        f"lane-order violation: the {lane} receipt is absent; "
        f"run --lane {lane} (and anchor it) first",
    )
    digest = verify_adjacent_seal(receipt)
    payload = strict_json(receipt)
    require(
        payload.get("schema") == RECEIPT_SCHEMA,
        f"{lane} receipt schema mismatch",
    )
    require(payload.get("lane") == lane, f"{lane} receipt lane mismatch")
    require(
        payload.get("status") == "SUCCEEDED",
        f"{lane} receipt does not record a SUCCEEDED lane",
    )
    require(
        payload.get("runtime_manifest_sha256") == RUNTIME_MANIFEST_SHA256,
        f"{lane} receipt runtime manifest mismatch",
    )
    return digest, payload


def receipt_output_digests(lane: str, payload: dict[str, Any]) -> dict[str, str]:
    rows = payload.get("outputs")
    require(isinstance(rows, list) and bool(rows), f"{lane} receipt has no output rows")
    digests: dict[str, str] = {}
    for row in rows:
        relative = str(row["path"])
        expected = str(row["sha256"])
        require(
            verify_adjacent_seal(ROOT / relative) == expected,
            f"{lane} output drifted from its sealed receipt: {relative}",
        )
        digests[relative] = expected
    for output in LANE_OUTPUTS[lane]:
        require(
            str(output.relative_to(ROOT)) in digests,
            f"{lane} receipt does not cover the canonical output: {output}",
        )
    return digests


def lane_command(target: str, arguments: list[str]) -> list[str]:
    return [
        str(PINNED_PYTHON),
        "-I",
        "-S",
        str(RUNTIME_LAUNCHER),
        target,
        *arguments,
    ]


def run_lane(
    *,
    lane: str,
    target: str,
    arguments: list[str],
    outputs: tuple[Path, ...],
    receipt: Path,
    implementation_digest: str,
    implementation_rows: dict[str, str],
    paths_verified_absent: list[str],
    fence_anomalies: list[dict[str, Any]],
) -> dict[str, str]:
    require(target == TARGETS[lane], f"unexpected {lane} target")
    for output in outputs:
        require(not output.exists(), f"immutable output already exists: {output}")
        require(
            not Path(f"{output}.seal.sha256").exists(),
            f"immutable output seal already exists: {output}",
        )
    require(not receipt.exists(), f"immutable receipt already exists: {receipt}")
    require(
        not Path(f"{receipt}.seal.sha256").exists(),
        f"immutable receipt seal already exists: {receipt}",
    )

    expected_target_sha256 = implementation_rows[target]
    target_sha256_pre_execution = sha256(ROOT / target)
    require(
        target_sha256_pre_execution == expected_target_sha256,
        f"{lane} target drift before execution: {target}",
    )
    command = lane_command(target, arguments)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    target_sha256_post_execution = sha256(ROOT / target)
    target_intact = target_sha256_post_execution == expected_target_sha256

    # =====================================================================
    # A4 (STANDING INVARIANT): THE RETURNCODE AND TARGET-INTACT CHECKS COME
    # FIRST.  NOTHING IS SEALED ABOVE THIS BLOCK.
    #
    # In v006 the receipt was sealed before these two checks, so the FIRST
    # blocked lane permanently consumed the canonical receipt path and
    # canonical_absences then blocked every retry.  Here a blocked lane
    # leaves ZERO canonical artifacts: the reason is raised (and reaches the
    # operator on stderr), the receipt path stays free, and the run can be
    # retried once the cause is fixed.  The cost, stated honestly: a blocked
    # lane produces no sealed receipt of its own failure.  That is the
    # invariant's intent -- an immutable artifact must never be the price of
    # discovering a failure.
    #
    # Driven by test_stage8_t7_controller_v007.py::
    #   test_a4_blocked_lane_seals_no_receipt (behavioural, real components)
    #   test_a4_receipt_seal_follows_the_checks_in_source (ordering)
    # =====================================================================
    require(
        target_intact,
        f"{lane} target drifted across execution: {target} "
        f"(pre {target_sha256_pre_execution}, post {target_sha256_post_execution}); "
        "no receipt was sealed",
    )
    require(
        completed.returncode == 0,
        f"{lane} lane blocked (returncode {completed.returncode}); no receipt "
        f"was sealed: {completed.stderr[-2000:]}",
    )

    output_rows: list[dict[str, str]] = []
    for output in outputs:
        digest = verify_adjacent_seal(output)
        output_rows.append(
            {
                "path": str(output.relative_to(ROOT)),
                "sha256": digest,
                "seal_sha256": sha256(Path(f"{output}.seal.sha256")),
            }
        )

    payload = {
        "schema": RECEIPT_SCHEMA,
        "lane": lane,
        "status": "SUCCEEDED",
        "returncode": completed.returncode,
        "target": target,
        "target_sha256": implementation_rows[target],
        "target_sha256_pre_execution": target_sha256_pre_execution,
        "target_sha256_post_execution": target_sha256_post_execution,
        "controller": str(SELF.relative_to(ROOT)),
        "controller_sha256": implementation_rows[str(SELF.relative_to(ROOT))],
        "runtime_launcher": str(RUNTIME_LAUNCHER.relative_to(ROOT)),
        "runtime_launcher_sha256": implementation_rows[
            str(RUNTIME_LAUNCHER.relative_to(ROOT))
        ],
        "runtime_manifest_sha256": RUNTIME_MANIFEST_SHA256,
        "implementation_manifest_sha256": implementation_digest,
        "paths_verified_absent": paths_verified_absent,
        "outputs": output_rows,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
        "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
        "local_execution_receipt_not_remote_attestation": True,
        "fence_at_rest_mode": f"{FENCE_AT_REST_MODE:04o}",
        "fence_anomalies": fence_anomalies,
        "generation_tag": GENERATION_TAG,
        "alpha_computed": False,
        "proof_authorized": False,
    }
    # A4: the seal happens HERE, after both checks above have passed.
    atomic_sealed_json(receipt, payload)
    return {row["path"]: row["sha256"] for row in output_rows}


def run_comparison_lane(
    *,
    controller_context: str,
    implementation_digest: str,
    implementation_rows: dict[str, str],
    paths_verified_absent: list[str],
    fence_anomalies: list[dict[str, Any]],
) -> dict[str, Any]:
    independent_receipt_sha256, independent_payload = verify_prior_receipt(
        "independent"
    )
    primary_receipt_sha256, primary_payload = verify_prior_receipt("primary")
    independent_hashes = receipt_output_digests("independent", independent_payload)
    primary_hashes = receipt_output_digests("primary", primary_payload)
    comparison_arguments = [
        "--independent-json",
        str(INDEPENDENT_JSON),
        "--independent-npz",
        str(INDEPENDENT_NPZ),
        "--primary-json",
        str(PRIMARY_JSON),
        "--primary-npz",
        str(PRIMARY_NPZ),
        "--independent-json-sha256",
        independent_hashes[str(INDEPENDENT_JSON.relative_to(ROOT))],
        "--independent-npz-sha256",
        independent_hashes[str(INDEPENDENT_NPZ.relative_to(ROOT))],
        "--primary-json-sha256",
        primary_hashes[str(PRIMARY_JSON.relative_to(ROOT))],
        "--primary-npz-sha256",
        primary_hashes[str(PRIMARY_NPZ.relative_to(ROOT))],
        "--output",
        str(COMPARISON_JSON),
        "--controller-context",
        controller_context,
        "--independent-receipt-sha256",
        independent_receipt_sha256,
        "--primary-receipt-sha256",
        primary_receipt_sha256,
    ]
    comparison_hashes = run_lane(
        lane="comparison",
        target=TARGETS["comparison"],
        arguments=comparison_arguments,
        outputs=LANE_OUTPUTS["comparison"],
        receipt=COMPARISON_RECEIPT,
        implementation_digest=implementation_digest,
        implementation_rows=implementation_rows,
        paths_verified_absent=paths_verified_absent,
        fence_anomalies=fence_anomalies,
    )
    comparison = strict_json(COMPARISON_JSON)
    require(
        comparison.get("overall_verdict")
        == "ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_COMPARISON_PASSED",
        "sealed comparator did not return the Phase-A PASS verdict",
    )
    require(
        comparison.get("comparison_supports_actual_parent_regulated_CAR_operator_response")
        is True,
        "comparator did not set comparison_supports_actual_parent_regulated_CAR_operator_response",
    )
    require(
        comparison.get(
            "comparison_supports_actual_parent_same_carrier_one_source_restriction"
        )
        is True,
        "comparator did not set comparison_supports_actual_parent_same_carrier_one_source_restriction",
    )
    canonical_input_paths = {
        "independent_json": str(INDEPENDENT_JSON.resolve()),
        "independent_npz": str(INDEPENDENT_NPZ.resolve()),
        "primary_json": str(PRIMARY_JSON.resolve()),
        "primary_npz": str(PRIMARY_NPZ.resolve()),
    }
    require(
        comparison.get("resolved_input_paths") == canonical_input_paths,
        "comparator resolved input paths do not match the canonical pinned paths",
    )
    require(
        comparison.get("resolved_output_path") == str(COMPARISON_JSON.resolve()),
        "comparator resolved output path does not match the canonical pinned path",
    )
    require(
        comparison.get("controller_context") == controller_context,
        "comparator did not record the controller context",
    )
    require(
        comparison.get("independent_receipt_sha256") == independent_receipt_sha256,
        "comparator did not record the independent receipt digest verbatim",
    )
    require(
        comparison.get("primary_receipt_sha256") == primary_receipt_sha256,
        "comparator did not record the primary receipt digest verbatim",
    )
    return {
        "schema": "stage8_t7_actual_parent_car_pipeline_summary_v003",
        "lane": "comparison",
        "overall_verdict": comparison["overall_verdict"],
        "implementation_manifest_sha256": implementation_digest,
        "independent_receipt_sha256": independent_receipt_sha256,
        "primary_receipt_sha256": primary_receipt_sha256,
        "comparison_receipt_sha256": sha256(COMPARISON_RECEIPT),
        "comparison_output_sha256":
            comparison_hashes[str(COMPARISON_JSON.relative_to(ROOT))],
        "phase": "A",
        "alpha_computed": False,
        "proof_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Run exactly one Stage-8 T7 production lane (v007, generation G7)."
        )
    )
    parser.add_argument("--lane", required=True, choices=LANE_SEQUENCE)
    parser.add_argument(
        "--preflight-only",
        action="store_true",
        help=(
            "Run EVERY enumerated precondition (the frozen PRECONDITIONS "
            "tuple, in order) for the given lane and exit before any "
            "canonical write: exit 0 with a one-line PREFLIGHT_OK json, or "
            "exit 1 with the precise block reason."
        ),
    )
    arguments = parser.parse_args()
    lane = arguments.lane
    controller_context = str(SELF.relative_to(ROOT))
    os.environ[CONTROLLER_CONTEXT_ENVIRONMENT_KEY] = controller_context

    if arguments.preflight_only:
        # Sealed-discipline instrument: every enumerated precondition, in
        # the documented order, with NO ARTIFACT WRITE anywhere and NO
        # canonical consumption; the outcome is a single line of JSON.  The
        # one documented exception is the fence L3 self-heal, which may drop
        # directory permission bits (no artifact, no seal, no manifest row)
        # and reports what it did in fence_anomalies.
        #
        # PREFLIGHT_OK IS NOT STARTABILITY EVIDENCE (A2).  The only accepted
        # startability evidence is the no-stub end-to-end rehearsal in
        # scripts/test_stage8_t7_real_chain_rehearsal_v001.py.
        context = {}
        try:
            run_preflight(lane, context)
        except RuntimeError as error:
            print(
                json.dumps(
                    {
                        "schema": "stage8_t7_preflight_only_summary_v002",
                        "status": "PREFLIGHT_BLOCKED",
                        "lane": lane,
                        "generation_tag": GENERATION_TAG,
                        "preconditions": list(PRECONDITIONS),
                        "reason": str(error),
                        "fence_anomalies": context.get("fence_anomalies", []),
                        "fence_state": fence_state(),
                        "preflight_ok_is_not_startability_evidence": True,
                        "alpha_computed": False,
                        "proof_authorized": False,
                    },
                    sort_keys=True,
                )
            )
            print(f"preflight blocked: {error}", file=sys.stderr)
            return 1
        print(
            json.dumps(
                {
                    "schema": "stage8_t7_preflight_only_summary_v002",
                    "status": "PREFLIGHT_OK",
                    "lane": lane,
                    "generation_tag": GENERATION_TAG,
                    "preconditions": list(PRECONDITIONS),
                    "implementation_manifest_sha256":
                        context["implementation_digest"],
                    "bridge_manifest_sha256": context["bridge_digest"],
                    "paths_verified_absent": context["paths_verified_absent"],
                    "generation_coherence": context["generation_coherence"],
                    "fence_anomalies": context["fence_anomalies"],
                    "fence_state_after_preflight": fence_state(),
                    "preflight_ok_is_not_startability_evidence": True,
                    "alpha_computed": False,
                    "proof_authorized": False,
                },
                sort_keys=True,
            )
        )
        return 0

    # PRE-FLIGHT (the frozen PRECONDITIONS tuple, in order; all thirteen
    # fail-closed preconditions BEFORE any canonical output path is consumed
    # AND BEFORE the write fence is raised).
    context = run_preflight(lane)
    implementation_digest = context["implementation_digest"]
    implementation_rows = context["implementation_rows"]
    paths_verified_absent = context["paths_verified_absent"]
    fence_anomalies = context["fence_anomalies"]

    # ===================================================================
    # THE FENCE: raise as the FIRST GATED ACTION after ALL preconditions
    # have passed, and drop in a finally path that covers every exit --
    # success, RuntimeError, any other exception, and the caught signals.
    # ===================================================================
    install_fence_signal_handlers()
    fence_raised = raise_fence()
    try:
        if lane == "comparison":
            summary = run_comparison_lane(
                controller_context=controller_context,
                implementation_digest=implementation_digest,
                implementation_rows=implementation_rows,
                paths_verified_absent=paths_verified_absent,
                fence_anomalies=fence_anomalies,
            )
        else:
            hashes = run_lane(
                lane=lane,
                target=TARGETS[lane],
                arguments=[],
                outputs=LANE_OUTPUTS[lane],
                receipt=LANE_RECEIPTS[lane],
                implementation_digest=implementation_digest,
                implementation_rows=implementation_rows,
                paths_verified_absent=paths_verified_absent,
                fence_anomalies=fence_anomalies,
            )
            summary = {
                "schema": "stage8_t7_actual_parent_car_lane_summary_v004",
                "lane": lane,
                "implementation_manifest_sha256": implementation_digest,
                "receipt": str(LANE_RECEIPTS[lane].relative_to(ROOT)),
                "receipt_sha256": sha256(LANE_RECEIPTS[lane]),
                "outputs": hashes,
                "anchor_receipt_before_next_lane": True,
                "phase": "A",
                "alpha_computed": False,
                "proof_authorized": False,
            }
    finally:
        dropped = drop_fence()
        # The post-drop state is VERIFIED, not merely intended.  This runs on
        # every exit path, including the failure paths.
        for directory in FENCED_DIRECTORIES:
            if directory.is_dir() and fence_is_writable(directory):
                print(
                    "FENCE DROP FAILED: "
                    f"{directory.relative_to(ROOT)} is still writable",
                    file=sys.stderr,
                )
        print(
            json.dumps(
                {
                    "schema": "stage8_t7_directory_permission_fence_record_v001",
                    "generation_tag": GENERATION_TAG,
                    "lane": lane,
                    "raised": fence_raised,
                    "dropped": dropped,
                    "fence_state_after_drop": fence_state(),
                    "fence_anomalies": fence_anomalies,
                },
                sort_keys=True,
            ),
            file=sys.stderr,
        )
    summary["generation_tag"] = GENERATION_TAG
    summary["fence_anomalies"] = fence_anomalies
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
