# Stage-8 T7 Quarantine Narrowing — Restoration Record V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_AMENDMENT TO THE DISARM DISPOSITION (fence F3)
```

Executes the principal's decision on QUARANTINE_BRIDGE_ROW_CONFLICT:
FIX (B), selective restoration, with fences F1-F3. Amends
STAGE8_T7_SUPERSEDED_CHAIN_DISARM_DISPOSITION_V001 append-only; that
artifact is not altered.

## Why (A) was rejected — recorded reason

Fix (A) (quarantine-aware row resolution) required editing the
byte-frozen, twice-audited derive lanes — the files whose byte-freeze is
the load-bearing premise of the bridge architecture itself and of three
reviewer audits ("scope drift: zero findings"; custody Section-3
byte-identity). The bridge exists BECAUSE those files are not edited. A
fix that undoes the reason for the mechanism it is fixing is not a fix.

## The restoration (exactly three files; bytes preserved)

```text
scripts/run_stage8_t7_actual_parent_car_pipeline_v002.py
  before = after = 18070467f477dc96d949fa37ae429bcb8f3a5f4b7f0b9ad69f10824ee5f375ac
scripts/launch_stage8_t7_content_addressed_runtime_v002.py
  before = after = 240c6c02da3f1428693fbe1188556e1ad6169c23503dba74ae4ab97e539e29e8
scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v002.py
  before = after = ac75daaa469f2160f4612b779814df583eff81f35030a43c7b8446a8dba0607f
Each verified against BOTH its manifest-v001 row AND its quarantine-
manifest record: all three match on every comparison.
REASON: manifest-v001 bridge-row integrity for the byte-frozen derive
lanes, which verify that manifest's every row at runtime.
EIGHT ENTRY POINTS REMAIN QUARANTINED: compare v001/v003/v004,
launch v003/v004, run_pipeline v001/v003/v004.
```

## Fence F1 — self-block probe (probe #8; sealed here)

Run immediately after restoration, with artifact fingerprints taken
before and after:

```text
8a  launcher v002 -> controller v002   (THE FEARED ROUTE)
      RuntimeError: implementation signature is absent
      — raised inside verify_implementation, BEFORE any lane runs.
8b  direct controller v002
      RuntimeError: pipeline requires the sealed runtime launcher
      — the marker gate.
8c  launcher v002 -> comparator v002
      argparse: required arguments absent (no caller-supplied bundle
      paths) — exits before any computation.
provenance/*.asc on disk: NONE (verified).
ZERO ARTIFACTS: CONFIRMED (fingerprint identical before and after).
```

The exposure the construction lane flagged when proposing (B) —
"launcher v002 back on a canonical path where it allowlists controller
v002" — is thereby converted from an accepted exposure into a VERIFIED
NON-EXPOSURE.

## Fence F2 — the standing lock, explicit of record

```text
The restored v002 chain is dead because its GPG signature requirement is
MECHANICALLY UNSATISFIABLE:
  - the pinned key's passphrase is unrecoverable
    (STAGE8_T7_GPG_SIGNATURE_REQUIREMENT_SUPERSESSION_AMENDMENT_V001);
  - the signature requirement was superseded by principal decision for
    v005+ ONLY;
  - the v002 controller's requirement was DELIBERATELY NOT RELAXED.
PROHIBITIONS AND OBLIGATIONS, standing:
  1. Creating any provenance/*.asc for the v002-era manifest is
     PROHIBITED.
  2. The GPG supersession amendment (cited by seal) IS the standing
     mechanism keeping the restored chain unlaunchable.
  3. IF ANY FUTURE DECISION EVER REVISITS GPG SIGNING, THIS RESTORATION
     FENCE MUST BE RE-EVALUATED IN THE SAME DECISION, EXPLICITLY.
Consistent with sealed discipline rule 3: the protection rests on a
mechanically unsatisfiable precondition, not on operator discipline.
```

## Post-restoration verification

```text
REAL CHAIN (launcher v006 -> controller v006 --preflight-only
            --lane independent, canonical workspace, read-only):
  status PREFLIGHT_OK
  all TEN preconditions pass in frozen order: runtime_attestation,
    implementation_manifest, authority_digests, bridge_binding,
    push_capability, prior_receipts, primary_route1_readiness,
    comparison_bundle_stamps, comparison_bundle_provenance,
    canonical_absences
  bridge manifest f573ae21…; implementation manifest 9f80aa63…
  all eight canonical paths verified absent; ZERO WRITES.
  (Step 4, bridge_binding — the conflict's blocking step — now passes.)
v006 suites: launcher 6/6, controller 27/27 (no regression).
v004-ERA LAUNCHER SUITE: STILL FAILS, on the EIGHT still-quarantined
  files ("compare ..._v003.py should exist on disk"). The disclosure in
  STAGE8_T7_QUARANTINE_COLLATERAL_V005_SUITE_RECORD_V001 therefore
  STANDS AS WRITTEN — restoration did not restore that fence's
  precondition. Documented state, not a finding.
```

## Protected status

```text
superseded_chains_mechanically_disarmed = true
disarm_narrowed_by_three_enumerated_files = true
restored_v002_chain_self_blocks_verified = true
production_chain_startable = true
production_authorized = false
alpha_computed = false
proof_authorized = false
```
