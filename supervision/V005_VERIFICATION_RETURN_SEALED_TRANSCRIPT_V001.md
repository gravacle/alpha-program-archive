# v005 Verification Return — Sealed Evidence Transcript
Claude lane · 2026-07-26 (autonomous window) · verbatim transcript of the
mechanical-rule-chartered hostile verification of the v005 repair cycle.
Verdict NOT_READY on ONE residual (discipline rule 3: superseded chains
remain launchable — dispositioned pending principal authorization in
STAGE8_T7_SUPERSEDED_CHAIN_DISARM_DISPOSITION_V001); all six files sound;
B1/M1/M2/m4 closed with live probes; rules 1-2 SATISFIED. After manifest
v004 was sealed (187a0435…), the real-chain startability check returned
PREFLIGHT_OK with the full eight-step enumeration and zero writes —
recorded below the transcript.

---

All verification complete. Assembling the verdict.

---

VERDICT: NOT_READY — one blocking residual on B2/discipline rule 3. Everything else verified and confirmed; the six files themselves are sound and every other reported claim reproduced exactly.

## RULE_ENFORCEMENT (STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001)

- Rule 1 (real component, end-to-end): SATISFIED. `test_real_chain_startability` (test_stage8_t7_controller_v005.py:1243) drives the REAL launcher at its canonical path via subprocess (`PINNED_PYTHON -I -S REAL_LAUNCHER CONTROLLER_RELATIVE --lane independent --preflight-only`, cwd=ROOT) — no copy, no stub, no monkeypatch anywhere in that function (verified by full read; the fixture regime is confined to lane internals in the other 19 tests). The launcher regression fence (test_stage8_t7_launcher_v005.py:123) asserts on the REAL imported module's `ALLOWED_TARGETS` and drives the REAL `resolve_target` against the on-disk superseded v003/v004 files, proving the allowlist (not file absence) blocks.
- Rule 2 (enumerate + verify before first irreversible action, ordering proven): SATISFIED. `PRECONDITIONS` is a module-level frozen 8-tuple (run_stage8_t7_actual_parent_car_pipeline_v005.py:268): runtime_attestation, implementation_manifest, authority_digests, bridge_binding, push_capability, prior_receipts, comparison_bundle_stamps, canonical_absences. `run_preflight()` executes exactly this tuple in order; the only canonical writer is `atomic_sealed_json`, reachable solely through `run_lane`/`run_comparison_lane`, which `main()` reaches only after `run_preflight()` returns — in both production and `--preflight-only` modes (same `run_preflight` call). Code-order proof holds for every lane; `test_preconditions_enumerated` fences the tuple and one-dispatch-step-per-name.
- Rule 3 (superseded chains never launchable on canonical paths): VIOLATED — see BLOCKING below.

## BLOCKING FINDING (B2 / rule 3 residual)

The v005 rebuild removes superseded routes only from the NEW launcher. The superseded launchers remain on canonical paths, fully operational, and still launch their own chains:

- Launcher v003 (`--selftest` exit 0, verified live) allowlists `run_stage8_t7_actual_parent_car_pipeline_v003.py`; launcher v004 retains the same v003-controller row. Controller v003 has no GPG and no push pre-flight; its authority is `implementation_v002.json`, whose adjacent seal verifies and whose rows match disk row-for-row TODAY (verified). Its full pre-flight (marker, manifest, absences) passes right now. One stale invocation — `pinned_python -I -S scripts/launch_stage8_t7_content_addressed_runtime_v003.py scripts/run_stage8_t7_actual_parent_car_pipeline_v003.py --lane independent` — would run the real derive lane and seal chmod-444 artifacts on the SAME canonical v001 paths the v005 chain uses, permanently blocking the v005 production run (append-only workspace). The comparison lane of that chain reproduces B2's exact BLOCKED-artifact poisoning.
- Launcher v002 similarly allowlists controller v002 (single-invocation full pipeline, manifest v001 seal-valid and disk-equal, GPG signing AFTER canonical writes — defect class 1 still live in it).
- I established this statically/read-only; I did not run any stale lane.

Consequence: the launcher v005 docstring's claim that "the superseded chains are made unlaunchable on the canonical paths mechanically, in this same change" is true only for routes through launcher v005; B2 as written by the reviewer ("the known-defective v003 chain ... remains ARMED ... must be made unlaunchable mechanically") is not fully closed. Under rule 1's own mechanism, the inability to disarm v001–v004 files inside this change's no-touch constraint is itself a finding that must be dispositioned before sealing (byte-preserving mechanical disarm — e.g. mode change/quarantine — with Brian's authorization, or a sealed explicit disposition), and the v005 docstring's overbroad claim must be corrected or scoped.

## B1 / B2 / M1 / M2 / m4

- B1 CLOSED: launcher v005 row `scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py` present; my own real-chain probe: launcher resolved the controller (no allowlist fence), marker gate passed, block occurred at step 2 with exactly `implementation manifest is absent: provenance/stage8_t7_actual_parent_regulated_car_operator_response_implementation_v004.json`, exit 1, one-line PREFLIGHT_BLOCKED JSON carrying the frozen enumeration. Old deadlock reproduced: launcher v004 → controller v004 blocks "not allowlisted".
- B2 CLOSED FOR LAUNCHER v005 ONLY: zero earlier-generation controller/comparator rows (grep + exact set-equality fence + live subprocess blocks of compare/controller v003 and v004). Residual above is blocking.
- M1 CLOSED: `preflight_comparison_bundle_stamps` (step 7) requires both bundle JSONs' stamped `implementation_manifest_sha256` to equal the bridge digest recomputed from disk in step 4 of the SAME invocation, before the comparison path is consumed; `test_bundle_stamp_mismatch_blocks` reproduces the inter-invocation regeneration hazard with a valid-seal foreign-stamp bundle, blocked with zero comparison artifacts.
- M2 CLOSED: `preflight_authority_digests` (step 3) recomputes the sealed Phase-A spec digest (789338ad...) plus the 20-row AUTHORITY_DIGESTS inventory from disk before any canonical consumption in any lane; I verified all 20 pinned digests against canonical disk independently — all match. Tamper/absence tests fire with zero artifacts.
- m4 CLOSED: comparator v005 header's corrected statement verified against the actual sealed v003 manifest — it does carry launcher v004 (not v003) and v004/v002 test rows (no v003 test rows); the v005 header's ten-row v004-manifest statement and its own launcher-repoint enumeration are accurate.

## DIFF_AUDIT

- Launcher v005 vs v004: docstring + ALLOWED_TARGETS rebuild only; no logic change. Allowlist = exactly 9 rows = the ten-file implementation set minus the launcher itself. The "conditional tenth row" disposition is correct: v004's self-test is the `--selftest` flag (no allowlist row); fenced by exact set-equality in the launcher suite.
- Comparator v005 vs v004: exactly 4 hunks — docstring insert, m4 history annotation, manifest pointer v003→v004 (line 161), launcher pointer v004→v005 (line 303). Bridge rule, oracle, gates, RESULT_SCHEMA untouched. sha256 matches report (6682a268...b1d1f).
- Controller v005 vs v004: every hunk maps to the enumerated items (step-function refactor with (lane, context) signatures, M1/M2 steps, PRECONDITIONS tuple, `--preflight-only` branch, repoints, ten-row REQUIRED_MANIFEST_ROWS); bridge/push/lane-order/receipt logic retained (verbatim modulo signature/context plumbing).
- All six sha256 match the change reports (launcher 7e7b9179...3ba452; controller e9172d6b...74c3; tests d60554a5...4c156, 92c0aeb0...e4b8, 2b6699b2...2e30).

## TEST_RESULTS (pinned runtime /Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3)

- test_stage8_t7_launcher_v005.py: 6/6 (regression fence runs first).
- test_compare_..._v005.py via REAL launcher v005 (-I -S): Ran 37 tests — OK.
- test_stage8_t7_controller_v005.py: 20/20 including test_real_chain_startability.
- Derive v002 pair via REAL launcher v005: primary suite PASS; independent suite 13 tests OK.

## IMMUTABILITY

- Custody Section-3 (STAGE8_CODEX_STANDING_DOWN_CUSTODY_V001.md): all 8 snapshot hashes match disk.
- All 383 seal files in the workspace (739 rows, including multi-row shasum-format seals) verify; sealed implementation manifests v001/v002/v003 seal-valid and row-for-row disk-equal.
- provenance/..._implementation_v004.json correctly NOT created; all 8 canonical artifact paths absent before and after every probe; my independent stat-scan of provenance/ + stage8_execution/ was byte-identical (hash f1fd496d...29bb9) before/after the real-chain probe AND across the full controller suite.
- Forbidden-constant grep on all six files: clean (only protective `alpha_computed: false` flags).
- Refuted list untouched: no refuted item re-raised; the blocking finding above is B2-closure enforcement, not a refuted concern.

## REQUIRED BEFORE V005_READY

1. Disposition the rule-3 residual: mechanically disarm the retained launch routes of the v002/v003 chains (launchers v002/v003 and launcher v004's v003-rows) in a byte-preserving, Brian-authorized way, OR seal an explicit dispositioned finding stating why they must remain and what compensating mechanical control applies.
2. Correct or scope the launcher v005 docstring claim that superseded chains "are made unlaunchable on the canonical paths mechanically, in this same change" (currently true only of routes through launcher v005).

---

## Post-manifest real-chain startability (construction lane, canonical workspace)

Command: pinned python -I -S scripts/launch_stage8_t7_content_addressed_runtime_v005.py
scripts/run_stage8_t7_actual_parent_car_pipeline_v005.py --lane independent --preflight-only
Result: exit 0, status PREFLIGHT_OK, bridge_manifest f573ae21…, implementation
manifest 187a0435…, all eight preconditions in frozen order, all eight
canonical paths verified absent, zero writes. The v005 production chain is
startable and gated only by the two authorization requirements (reviewer
verdict + recorded typed principal authorization), which remain absent.
