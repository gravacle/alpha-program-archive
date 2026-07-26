# Stage-8 T7 Production-Gate NO-GO — Record and Pipeline Repair Binding V001

Date: 2026-07-26

## Status

```text
APPEND_ONLY_REPAIR_BINDING_SEALED_BEFORE_AUTHORING
+ ERRATA ON THIS LANE'S FALSE PROSE CLAIMS
+ TWO ESCALATIONS THE PRINCIPAL MUST DECIDE (B3, B4)
```

Production-gate audit verdict: NO-GO. 13 raised, 12 confirmed after
adversarial refutation (7 BLOCKING, 3 MAJOR, 2 MINOR), 1 refuted. Sixth
cycle of ONE defect class, now precisely named by the auditor:

```text
VERSION-BUMP DESYNCHRONIZATION — detected only at the enforcement point
AFTER path consumption, with tests stubbed at exactly the failing seam.
```

Production remains prohibited (NO-GO verdict; no typed authorization).

## PART A — the systemic prescription, ADOPTED as standing discipline

These are the condition for re-audit and are adopted verbatim in
substance, extending STAGE8_REAL_COMPONENT_PRECONDITION_DISCIPLINE_V001
and its rule-4 supplement:

```text
A1 GENERATION-COHERENCE INVARIANT. Every generation pin in the chain —
   controller's launcher + manifest, comparator's launcher-path +
   manifest, launcher's allowlist, and manifest rows — is enumerated in
   ONE SEALED TABLE PER GENERATION, and a MECHANICAL CHECK verifies they
   all name the SAME generation BEFORE any lane runs. Six cycles have
   each been one pin lagging one bump.
A2 FULL REAL-CHAIN REHEARSAL, NO STUBS ANYWHERE. One test runs the REAL
   controller under the REAL launcher driving the REAL derive lanes and
   the REAL comparator end-to-end on fixture data in a DISPOSABLE
   WORKSPACE COPY (never the canonical root). PREFLIGHT_OK IS NO LONGER
   ACCEPTED AS STARTABILITY EVIDENCE — only this rehearsal is.
A3 HOISTS MUST BE CONDITION-IDENTICAL: same field, same row, SAME
   MANIFEST as the enforcement point — verified by READING THE
   ENFORCEMENT POINT, never by re-deriving the intent.
A4 RECEIPTS NEVER SEAL BEFORE THE RETURNCODE / TARGET-INTACT CHECKS.
   (Recurred again in run_lane; this is now a standing invariant with a
   test that must fail if the order is inverted.)
A5 (this lane's addition, from B6) SEAL-COVERAGE CHECK: no artifact may
   claim "sealed" in its name or text without an adjacent .seal.sha256.
   A mechanical sweep runs each cycle. Executed this date: one violation
   found and fixed (CONTROLLER_V006_AUTHOR_RETURN_SEALED_TRANSCRIPT_V001,
   now sealed 10b4c657…); one unsealed route memo sealed (8130ae5d…);
   CONTINUATION_STATE.md and the inherited verification charters are
   INTENTIONALLY living/unsealed and are recorded as the only exceptions.
```

## PART B — repairs enumerated (authoring scope)

```text
B1 LAUNCHER VERSION SKEW — the wedge. Comparator v005 enforces
   manifest v004's launcher-v005 row (7e7b9179…) while controller v006
   launches every lane under launcher v006 (2b7bd64a…). Derive lanes
   succeed; the comparison seals a BLOCKED verdict at the canonical
   comparison path (chmod 444) and the controller then seals a BLOCKED
   receipt BEFORE the returncode check — both canonical comparison paths
   permanently consumed on the FIRST production run, with
   canonical_absences blocking every retry.
   CHOSEN FIX, sealed here before authoring: COMPARATOR v006, with pins
   repointed to launcher v006 + manifest v005. (The alternative —
   launching the comparison under launcher v005 — is impossible: v005
   does not allowlist the v006 controller.) A1's coherence table and
   check are authored in the same change so this cannot recur on the
   next bump.
B2 STUB-COMPARATOR TEST BLINDNESS (B1's enabler) — the controller
   suite's comparison tests use a no-check stub and the comparator suite
   uses v005-attested fixtures, so the production combination
   (v006-attested bundles into the real comparator) executes in NO test
   on disk. Fixed by A2's rehearsal test, which is the only accepted
   startability evidence henceforth.
B5 M-c teeth did not cross the generation seam — subsumed by A2.
B6 the missing v006 transcript seal — FIXED this date (above), with A5
   instituted so it cannot recur silently.
MAJORS: hoist the comparator's own manifest verification
   condition-identically (it currently consumes the canonical path on
   failure); enumerate the controller-v006 launcher repoint as the
   functional change it is; correct the launcher-v006 docstring's
   now-stale disarm claim; sweep stale v005-era comments once.
```

## PART B' — ERRATA: three false prose claims by this lane

```text
E-1 The bridge supplement's "the manifest v005 inventory pins both" is
    FALSE: manifest v005 has NO launcher-v005 row (auditor recomputed
    every row of v001/v004/v005 from disk). Corrected of record.
E-2 Controller v006's header "sole change" claim is FALSE: the launcher
    repoint is an undeclared functional change. Corrected of record and
    enumerated in the repair.
E-3 Launcher v006's docstring disarm-mechanism claim is STALE after Fix
    (B) and had no erratum. Corrected of record; discipline rule 4
    (prose claims are checkable claims) applied to it.
```

## PART C — TWO ESCALATIONS (I will not silently pick; costs only)

```text
B3 RESTORED LAUNCHER v002 IS A LIVE POISONING ROUTE.
   Fact: launcher v002's allowlist carries the byte-frozen DERIVE lanes.
   Launched directly under it they pass their own preconditions
   (manifest-v001 rows all match post-restoration; their attestation
   checks do not constrain launcher identity) and WRITE the canonical
   precomparison paths. The .asc lock lives in the v002 CONTROLLER only,
   so F1 probe #8 — which exercised only the controller route — did not
   cover this. My fix-(B) fencing is therefore INCOMPLETE, and per
   discipline rule 3 "accept-and-probe" is NOT acceptable for a live
   write route.
   CONSTRAINT BOX (verified, not asserted): the derive lanes are
   byte-frozen (no check can be added to them); they verify ALL
   manifest-v001 rows AT CANONICAL PATHS, so a quarantine-aware
   launcher-row-only bridge does NOT work as stated; re-quarantining
   launcher v002 reopens the bridge-row conflict; and a controller-v006
   pre-flight cannot help because the route bypasses the controller.
   RESIDUAL OPTIONS, with costs, for the principal:
     (a) Re-quarantine launcher v002 AND accept that the byte-frozen
         derive lanes can no longer verify manifest v001 at canonical
         paths — i.e. edit the derive lanes after all, forfeiting the
         byte-freeze whose preservation was the entire reason (A) was
         rejected. Cost: undoes the premise of three audits.
     (b) Supersede manifest v001 with a v001-successor whose launcher row
         points at the quarantine path, then re-quarantine launcher v002.
         Cost: a sealed manifest is superseded (append-only, but it is
         the bridge's own authority); the derive lanes' check then passes
         against the successor only if they read the successor — which,
         being byte-frozen, they do not. Likely non-viable; stated for
         completeness.
     (c) Accept the route as an ARMED WRITE ROUTE and fence it
         procedurally. Cost: violates discipline rule 3 explicitly;
         this lane recommends against it and records that.
     (d) Retire the bridge architecture itself in favour of a
         same-generation manifest for the derive lanes — i.e. a new
         derive-lane generation. Cost: the byte-freeze ends by decision
         rather than by accident, with fresh hostile review of the new
         lanes; but it removes the entire class permanently.
   NO OPTION IS SELECTED HERE.
B4 THE v001 CHAIN SELF-BLOCKS ONLY AFTER A WRITE-CAPABLE STEP: it seals
   an immutable BLOCKED artifact at a canonical path in the course of
   blocking. The disarm disposition's v001-exclusion rationale is
   therefore PARTIALLY REFUTED. Obligation accepted: re-verify which
   v001 invocation routes reach the write and fence them; the fix class
   is B3's, so it is escalated with B3 rather than decided separately.
```

## PART D — Q6, contamination fence, diff items (consumed)

```text
D1 Q6 IS CONFIRMED, TWO-LANE CONVERGENT (this lane's review + Codex's
   independent F-8). The repair binding for E1 must COMMIT TO ONE
   READING, and the commitment is made here:
     ADOPTED READING: M2 supplies the anchored-sum D5 bound DIRECTLY,
     so M3's closure is a GEOMETRIC SERIES and the KP paragraph is
     rewritten as that.
   CONSEQUENCE STATED HONESTLY: under this reading Q6 is not needed for
   M3's closure — but the burden moves ONTO M2, which is exactly the
   E1 obligation that is open. Q6 remains a named obligation for the
   alternative reading and may not be treated as retired.
D2 CONTAMINATION FENCE — ADOPTED AND ALREADY APPLIED. Codex's
   reconciliation bullet asserting "n >= 2 two-line, R^-6, convergent
   shell sums" ECHOES THIS LANE'S OWN REFUTED C3 CLAIM (it inherited the
   IR memo's frame on reveal and skipped the assigned cross-term
   question). THOSE SENTENCES MAY NOT BE CONSUMED AS INDEPENDENT
   CONFIRMATION. A refuted claim must not resurrect by echo. NOTE: the
   E1 repair binding sealed earlier consumed only Codex's ASSIGNMENT-A
   return, which does not contain the echo, and it explicitly recorded
   that Codex "never leaned on the two-line decomposition" — that record
   is correct for Assignment A and is now scoped to Assignment A only.
   The reserved CODEX_RECONCILIATION_ADDENDUM slot is hereby fenced:
   its two-line/R^-6/NC3 sentences are quarantined on arrival pending
   Codex's corrected restatement and its cross-term assessment.
D3 DIFF ITEMS bound into the E1 successor: O6's density-EQUALITY claim
   is stronger than R1-R4 force (re-verb or re-derive); the KP constant
   line is underspecified as written; F-8 remains undischarged with
   clause (3) blocked until Phase-A executes; Route-Q independence from
   O7 is now TRIPLE-confirmed and the re-scope stands.
```

## Ordering

```text
1. Author comparator v006 + the A1 coherence table/check + the A2
   rehearsal test + the A4 receipt-order test + the majors, per PART B.
2. Fresh-context hostile review chartered on A1-A5 and this binding.
3. Re-audit. PREFLIGHT_OK is not evidence; the rehearsal is.
4. B3/B4 await the principal; production cannot be authorized while a
   live write route exists.
```

## What held (recorded, per the auditor)

Fix-(B) restoration hashes correct (three files byte-identical to their
manifest-v001 rows); the controller-route .asc self-block is real; the F3
narrowing amendment sealed and anchored; the piece-reconstruction and
basis-pin regressions CLEAN in comparator v005; derive lanes still
byte-frozen; manifest v005 seal and digest verified (9f80aa63…); anchors
reachable from origin/main; production outputs still ZERO; protected flags
all false. THE WEDGE WAS CAUGHT BEFORE THE FIRST IRREVERSIBLE WRITE.

## Protected status

```text
production_gate_verdict = NO_GO
production_authorized = false
live_write_route_open = true   (B3; escalated)
generation_coherence_invariant_adopted = true
real_chain_rehearsal_authored = false
alpha_computed = false
proof_authorized = false
```
