# Stage-8 T7 Manifest-Binding Bridge Amendment V001

Date: 2026-07-25 (night)

## Status

```text
APPEND_ONLY_AMENDMENT_SEALED_BEFORE_AUTHORING
```

Implements the reviewer lane's v003 re-audit disposition (relayed by
Brian, verdict NO-GO; FIX 1 blocking, FIX 2 major, one RE-SCOPE, three
RECORDs — recorded at /Users/bgm/MB Work/alpha_supervision/
EXTERNAL_REAUDIT_2026-07-25_fable_v003_return.md). Scope is EXACTLY the
re-audit list; nothing beyond it is authorized.

## A1 - FIX 1 mechanism decision (sealed before authoring)

DEFECT OF RECORD: the v002 derive lanes (byte-frozen per repair binding
V002 S1, twice audited clean) verify and stamp the manifest at the
canonical v001 path (digest f573ae21…); comparator v003 requires the
v002 manifest digest (cffcdf67…). No authorized production bundle can
ever match; the first run would write the sealed BLOCKED comparison
output and permanently consume the canonical comparison path — the
codified pre-flight rule was not applied to this precondition.

CHOSEN MECHANISM — comparator-side manifest BRIDGE (the derive lanes
remain byte-frozen; their twice-audited pedigree is preserved):

Comparator v004's bundle-binding rule becomes: the bundle's recorded
`implementation_manifest_sha256` must equal the digest, recomputed from
disk, of the sealed manifest at the canonical v001 path
(`provenance/..._implementation_v001.json`), whose adjacent seal must
verify, AND that manifest's row for the bundle's lane executor and for
the runtime launcher recorded in the bundle's attestation must equal
the corresponding rows of the comparator's OWN manifest (hash equality
row-by-row for those entries). The bridge therefore accepts exactly:
bundles stamped by lanes that verified a sealed on-disk manifest whose
authority rows for the executing code agree with the comparator's own
manifest. No copyable-string acceptance is introduced; both manifests
are re-hashed from disk.

PRE-FLIGHT (FIX 1 second half): controller v004 verifies the entire
bridge condition — both manifests sealed, digests recomputed, rows
consistent — BEFORE any lane runs and before any canonical path is
consumed. Failure blocks with zero artifacts.

## A2 - Enumerated authoring scope (nothing else)

1. `scripts/compare_stage8_t7_actual_parent_regulated_car_operator_response_v004.py`
   (base v003; sole changes: the A1 bridge rule; corrected docstring).
2. `scripts/run_stage8_t7_actual_parent_car_pipeline_v004.py` (base
   v003; sole changes: target comparator v004 and its manifest row;
   the A1 bridge pre-flight; RE-SCOPE of the docstring/S3 language to
   what the code actually enforces — receipt-existence lane ordering,
   cooperative anchoring; push-capability pre-flight (dry-run push to
   the archive repository at
   /Users/bgm/MB Work/alpha-program-archive, fail-closed) BEFORE any
   canonical path consumption; NO anchoring enforcement machinery).
3. `scripts/test_compare_stage8_t7_actual_parent_regulated_car_operator_response_v004.py`
   (base v003 test; sole addition: FIX 2 — one test driving the REAL
   production reconstruction oracle end-to-end, no monkeypatch, with
   the strengthened surrogate: typed alpha_stack/Sn copied verbatim,
   exact ladder p, h0 = sum kron(p_j, alpha_j), M_stack = 0, constant
   fabricated B_stack, closed-form eigh propagators; the gate must
   BLOCK specifically on the M/B quadrature comparison, asserted by
   failure-reason content, not on the alpha check. This test subsumes
   the wrong-quadrature negative for the production oracle.)
4. `scripts/test_stage8_t7_controller_v004.py` (base v003 test;
   updated for the bridge pre-flight and push pre-flight fences).
5. `provenance/stage8_t7_actual_parent_regulated_car_operator_response_implementation_v003.json`
   (+ seal): rows = controller v004, launcher v003, comparator v004,
   derive v002 x2, the v004 test files, launcher/controller tests,
   derive-lane v002 tests. Built only after the fixes verify.

The v001-path manifest stays sealed and in place (it is the object the
frozen derive lanes verify); the v002 manifest remains a sealed
superseded artifact.

## A3 - Records bound to this amendment (reviewer items R1-R3)

R1 (verification evidence): the v003 verification lane's return —
surrogate-attack results incl. the 3.1e-15 exploit re-reproduction, the
three variants, the honest control, the 1.7e-18 reconstruction
cross-check, and suite results — is transcribed as a sealed supervision
artifact so authorization rests on locatable numbers.
R2 (quadrature-rule-vs-operator scope): recorded in the sealed record
note adjacent to this amendment: the 2e-11 piece pin certifies
agreement with the lane's DECLARED quadrature rule, not proximity of
that rule to the defining integral Q b_D Q (measured rule bias up to
~8.2e-8 on B, ~3.5 orders below the cross-lane budget, invisible by
construction, affecting nothing currently claimed). No rule or
tolerance change.
R3 (S1-1c narrowing): binding V002's "every midpoint" diag-connection
tie is implemented at the single stored diagnostic midpoint per ell —
the derive lanes store only one diagnostic connection matrix per ell,
and they are byte-frozen; the narrowing is recorded append-only rather
than implemented. Piece-authenticity pins every B_stack entry, which
carries the per-midpoint load.

## A4 - Ordering

Author (A2) -> all suites green under the pinned runtime -> fresh
hostile verification (surrogate mandate retained; FIX-2 test must be
seen to exercise the real oracle) -> manifest v003 sealed -> anchor ->
reviewer-lane re-audit via Brian -> Brian's recorded typed
authorization -> production. Not before.

## Protected status

```text
actual_parent_regulated_CAR_operator_response_derived = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
