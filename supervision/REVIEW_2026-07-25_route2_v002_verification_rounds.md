# v002 Repair Verification — Two Hostile Rounds
Claude construction/supervision lane · 2026-07-25 · fresh-context subagent returns
Scope: the ten v002 repair scripts authored under the sealed repair binding
(STAGE8_T7_ACTUAL_PARENT_CAR_IMPLEMENTATION_REPAIR_BINDING_V001, dc7cdd15…).

## Round 1 (post-authoring): NOT_READY

Fresh hostile verification of the three parallel authoring lanes' output.
Physics/numerics verified sound: lineage integrator proven genuinely
second-order (4.00 error ratios against a 200k-step reference); assembly
matches spec text exactly; budgets match binding R3; fabricated-propagator
fixture blocks ONLY on the lineage gate (verified algebraically invisible
to every v001-checkable identity); comparator AST clean; v001 immutability
verified; forbidden constants clean; all five test suites green.

Two BLOCKING integration seams between parallel-authored files:
1. Output naming: derive lanes wrote v002-named production outputs while
   the controller pins canonical v001-named paths — guaranteed append-only
   wedge on first production run (sealed outputs, no receipt).
2. Controller-context transport: controller exported an env var; the real
   comparator reads only a --controller-context CLI argument; the
   controller test stub implemented the env contract (stub matched the
   intent, not the code) — comparison receipt sealed, then cross-check
   failure after all outputs sealed.
Plus CONDITION-3 (vacuous None==None provenance checks in the standalone
comparator) and CONDITION-4 (dead v002-attestation acceptance branch in
both lanes, unenumerated).

## Fixes applied by the construction lane (to unsealed drafts)

Output names reverted to canon in both lanes; --controller-context added
to the controller's comparator invocation + stub aligned to the real CLI
mechanism; non-empty-string manifest-row requires added before provenance
equality checks (target_sha256 check uses the validated row); dead branch
and its constants deleted, primary fence test rewritten to the v001-only
contract; launcher-test scratch helper canonicalized (macOS /var vs
/private/var, test-only).

## Round 2 (post-fix, fresh context): V002_READY

All five prior findings verified FIXED with end-to-end code traces (the
controller-context chain traced link-by-link through launcher argv
handoff to the sealed output and back to the cross-check). No remaining
vacuous .get() comparisons. Zero v002-named production outputs. All five
suites re-run green by the verifier (launcher 4/4, controller 6/6,
primary PASS with 4 fences, independent 13/13, comparator 27/27 incl.
lineage/Kraus/adjoint/pinning/flag-rename gates). Full-root sweep: only
the four sealed binding/custody docs and the ten v002 scripts changed
since custody transfer; all 261 seal files verify (444 rows, zero
failures); all 8 inherited v001 script hashes still match custody
Section 3. Production outputs, receipts, and implementation manifest
confirmed absent, as R4 requires before step 3. Non-blocking notes:
controller retains a truthful dead env-var export (candidate for removal
in a future successor); comparator RESULT_SCHEMA string is v002 inside
the v001-named output (coherent).

## Disposition

R4 step 2 satisfied. Proceeding to R4 step 3: implementation manifest
covering all ten v002 files (a superset of the controller's required
eight), adjacent seal, detached GPG signature, external trust anchor via
archive push BEFORE production.
