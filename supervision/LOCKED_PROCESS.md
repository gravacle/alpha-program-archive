LOCKED PROCESS — FOUR STEPS. NOT TO BE REVISED.

Ruled by the principal 2026-08-01: "lock one simple process structure that ensures the integrity of
the results. Nothing more."

---

## THE FOUR STEPS — *** THESE ARE **REVIEWER** STEPS. LANES DO NOT DO THEM. ***

*** LANES: SEAL, MIRROR ARTIFACT AND SIDECAR, REPORT HASHES, **STOP**. DO NOT REGISTER. DO NOT
COMMIT. DO NOT PUSH. DO NOT ASK FOR AUTHORITY TO — IT WILL NOT BE GRANTED. Q-91 MAKES THE REVIEWER
SOLE REGISTRAR AND COMMITTER, AND TWO LANES STALLED ON THIS AMBIGUITY ON 2026-08-01 BECAUSE THIS
HEADING DID NOT SAY SO. THAT WAS A REVIEWER DEFECT. ***


```text
1  VERIFY THE HASH.  shasum -a 256 the artifact against the hash the lane stated.
                     MISMATCH -> STOP. Do not read further, do not register.

2  FENCE-SCAN.       grep for a computed alpha, kappa_record, kappa_Thomson, coupling, scale,
                     root, eigenvalue, or any comparison to a measured constant.
                     HIT -> STOP and report it.

3  REGISTER ONE ENTRY.  Q-number, artifact name, hash, the flag block, ONE sentence of what
                     changed. *** NOT AN ESSAY. THE ARTIFACT HOLDS THE DETAIL. ***

4  COMMIT AND PUSH.  Mirror artifact and sidecar. Push. Done means pushed.
```

## LANES — 2026-08-01. *** EINSTEIN RETIRED. NOT A RESERVE — IDLE. ***

```text
CODEX 1 . CODEX 2 . BOHM   -- THREE LANES. ALL THREE CONSTRUCT.
*** BOHM IS A WORKING LANE, NOT ONLY A REVIEWER. When both Codex lanes are busy, Bohm computes. ***
*** WHEN BOHM CONSTRUCTS, A CODEX LANE VERIFIES IT under the adversarial brief below.
Q-91's separation of constructor and verifier does not lapse because a lane was retired. ***
```

## PREFLIGHT — THREE LINES, BEFORE ANY RELAY SHIPS

```text
DOES THE OBJECT EXIST?   IS THE VERSION CURRENT?   ARE ITS INPUTS PRESENT?
*** IF ANY ANSWER IS NO, **THAT** IS THE RELAY. ***
```

*** AND PREFLIGHT RUNS AT **SEND TIME**, NOT ONLY AT WRITE TIME. A relay loaded later than the
register head it was written under is RE-CHECKED against every entry since, before pbcopy.
Installed 2026-08-01 after relay 270 shipped four hours stale across fifteen register entries and
needed a mid-run addendum (283) to repair — a defect the principal caught, not the reviewer. ***

*** ADDED 2026-08-01 AFTER FOUR RELAYS ON TARGET 2 (259, 261, 263, 265) EACH RETURNED "THE THING
UNDERNEATH YOU DOES NOT EXIST." THE FOURTH QUESTION SHOULD HAVE BEEN THE FIRST. AND THE WHOLE
RESEARCH PLAN WAS BUILT ON A `Gamma_K` FORMULA TWO LANES LATER FOUND SUPERSEDED. ***

**AND: the reviewer tests his own hypotheses BEFORE they become relays.** Eight collapse proposals,
six refuted. Seam 10 cost a full lane cycle to refute what a three-second computation would have
killed. *** LANES ARE FOR WHAT THE REVIEWER CANNOT DO IN MINUTES. ***

## PLAN GOVERNANCE — RULED BY THE PRINCIPAL 2026-08-01

```text
THE GOVERNING PLAN IS  alpha_supervision/TASK_LIST_HERE_TO_ALPHA_2026-08-01_V002.md
*** EVERY RELAY HEADER CARRIES A TASK NUMBER (1-6, or SUPPORT) FROM ITS SECTION 9. WORK WITH NO TASK ID DOES
NOT SHIP. A NEEDED CHANGE IS LOGGED IN THE PLAN'S SECTION 10 FIRST, SURFACED TO THE PRINCIPAL, AND
ONLY THEN EXECUTED. THE PLAN IS WHAT WE FOLLOW. ***
```

## FENCES — ACT-BASED, NOT TOKEN-BASED (implements Q-198 + DoR 006's scoping; C19)

```text
*** WHAT IS BARRED IS THE ACT, NEVER THE WORD: ***
BARRED   computing or bounding ALPHA, kappa_record, kappa_Thomson, or K_* / any root of the
         physical residual . comparing ANYTHING to a measured constant . choosing a physical
         fork that must be derived (Misner-Sharp/Brown-York etc.) . fitting any construction
         toward a known target . touching a32_holdout/custodian_private/
PERMITTED, EXPLICITLY: all structural mathematics of DECLARED objects -- spectra and
         eigenvalues of declared finite/fixture objects (DoR 004 precedent) . operator
         comparisons . existence/uniqueness arguments . gap-existence arguments . proofs about
         infinite families (the Q-205 precedent: A PROOF ABOUT A FAMILY COUNTS AS
         INSTANTIATION; the Q-200 rule bars SCHEMAS-PASSED-AS-INSTANCES, not structural
         arguments)
```

*** THE MACHINERY-APPEAL RULE: ANY LANE THAT STOPS BECAUSE A FENCE (NOT PHYSICS) BLOCKS A
STRUCTURAL RESULT MUST SAY SO IN ITS ARTIFACT WITH THE FLAG
`FENCE_BLOCKED_STRUCTURAL_RESULT = true | what: ... | fence: ...`
-- SO ARTIFICIAL CONSTRAINTS SURFACE AS FINDINGS INSTEAD OF DISSOLVING INTO NO_VERDICTs. The
reviewer routes every such flag to the principal. A fence that blocks a non-fitting result is a
DEFECT (DoR 004's ruling) and gets scoped or lifted, never silently obeyed. ***

## THE THREE THINGS IN A RELAY THAT PROTECT THE RESULT

*** THESE EARNED THEIR KEEP. NOTHING ELSE IN A RELAY DID. ***

```text
A  "HUNT YOUR OWN COUNTEREXAMPLE, AND LEAD WITH IT IF YOU FIND ONE."
B  TYPE EVERY NEGATIVE:  TYPE-R refuted . TYPE-U unbuilt . TYPE-S scope-empty . TYPE-C
                         constraint-blocked CHECKS ONLY . TYPE-P premise-conditional (DoR 006).
                         ONLY TYPE-R IS PHYSICAL CONTENT.
C  NAME THE SYMBOL COLLISIONS THAT BEAR ON THIS QUESTION. Nothing generic.
```

## WHAT IS RETIRED

```text
the pre-commit corpus_check GATE   -- blocked 5 commits on 2026-08-01, found 0 real defects
four parallel status documents     -- EXECUTION_TRACKER.md is the only one maintained
relay boilerplate                  -- the standing fences are read once, not repeated per relay
register entries as essays         -- capped at the flag block plus one sentence
```

*** THIS FILE IS NOT REVISED. IF SOMETHING HERE IS WRONG, IT IS RULED ON BY THE PRINCIPAL AND
REPLACED WHOLE — NOT AMENDED, NOT EXTENDED, NOT VERSIONED. ***

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.

## MIRROR-VERIFY RULE (2026-08-01, after the C5-C25 loss)
After EVERY edit to the plan, register, or tracker: cp to the archive mirror, then VERIFY the
mirror is byte-identical (shasum both) BEFORE committing. On session resume: verify the plan's
section-10 head (highest Cnn) matches the tracker's recorded C-head before any new work.
C5-C25 were written, announced, and then lost because the pushed mirror never carried them.

## LOCAL-SIDECAR RULE (added 2026-08-03, Q-351)

The reviewer-owned seal sidecars that live NEXT TO the supervision files
(alpha_supervision/*.seal.sha256) must be refreshed in the SAME step as every
write to those files — the mirror-side sidecars alone are not enough. Lanes
preflight against the local sidecars; five were stale for two days and produced
repeated false custody alarms (Q-349, Q-351). The register/tracker/plan write
step is: edit file -> refresh LOCAL sidecar -> cp to mirror -> write mirror
sidecar -> shasum-verify both -> commit -> push.

## SURFACE-GEOMETRY-VERSUS-RAILS RULE (principal's steer, 2026-08-04, Q-427)

Every review of an exhibit, witness, or new-physics typing must separate two
questions and answer both explicitly:
1. SURFACE GEOMETRY: does the object prove something about the actual record
   surface's geometry (its real incidence/cycle/refinement structure), with
   the proof anchored in ratified surface data?
2. RAILS: or does it merely satisfy conditions our own formalism installed
   (the categories, functors, refinement machinery, certificate shapes) —
   conditions that could be met by formal bookkeeping with no geometric
   content?
Additionally: any object previously typed GENUINELY_NEW_PHYSICS must be
re-examined for RAIL-ARTIFACT status — a requirement imposed by our
scaffolding rather than by the physics is not new physics and must not cost
declaration; it is a candidate for removal or derivation at the rail level.
A review verdict that does not state the geometry/rails split is incomplete.

## FABLE CHECKPOINT-REVIEW RULE (principal + registrar, 2026-08-04; in force for the spark era and after)

At the following checkpoints, the registrar (Fable) performs a DIRECT
mathematical review of the artifact(s) — full read, recomputation of the
load-bearing steps, independent verdict — BEFORE the checkpoint proceeds:

1. Before any DoR ruling or amendment reaches the principal.
2. Before any DoR-020 escrow license opens (member binding, fixed-point
   execution, the end test).
3. At every witness certification (scoped or full [EQ6]).
4. On any spark-vs-spark disagreement, and on any verdict that reverses a
   prior Sol-era verdict.
5. At every SPARK-VERDICT registration (standing: full artifact read).

Custody: reviewing lane work is the registrar's original role (Q-91); the
constraint remains that Fable's own CONSTRUCTIONS receive lane verification.
A Fable checkpoint review supplements, never replaces, the Sol re-check
discipline for spark verdicts.

## THE NO-CLOBBER RULE (added 2026-08-04, after the 531 dual-run overwrite)
Every relay's OUTPUT section carries the clause: "If the output filename already exists in the
workspace, STOP and report — do not overwrite." A lane that finds its target filename present
stops there. Registrar duty on any dual-run event: snapshot the first return's bytes to the
supervision mirror IMMEDIATELY on report, before any other action. (In the 531 event the second
run overwrote the first in the shared worktree before the snapshot landed; the first return's
bytes survive only as its reported hash 2c8bb753.)

## THE RECORD-FIRST COMMISSIONING RULE (added 2026-08-05, after the seed arc)
Any relay that demands proof of a value-like or coupling-like property (a nonvanishing, a
magnitude class, an anchor, a threading) must OPEN with the determination question — does the
sealed stock decide this at all? — framed explicitly against the program's founding record-level
differences: couplings are OUTPUTS of self-consistency (K = B_ind(K)), not stock contents; laws
carry addresses/supports; no selection; the record carries conservation laws, not source laws.
Only if the stock decides it does a proof demand follow; otherwise the property is typed
(derivable / authorable / end-test-structural / obstructed) and carried accordingly. Origin: the
seed arc (Q-493–Q-498) reached END_TEST_STRUCTURAL correctly but through continuum-first
commissions; the determination-first framing (the 541 lesson) applies to VALUES, not only objects.
The registrar checks every commission against this rule as it checks fence gates.

## THE SURFACE-ANCHOR RULE (added 2026-08-05, per the principal; strengthens the surface-geometry-versus-rails rule)
Every build and review relay MANDATES a SURFACE ANCHOR section in its output artifact:
(i) every PASS names the actual surface objects it was computed on — stages, cycles, arrows, orbit
members, by name; a PASS computed only on rails notation is not a PASS;
(ii) every NEW construct carries the geometry/rails split explicitly (which part is physical raw
material, which part is organizing notation);
(iii) the clause-level quantification check: no clause may quantify over structure the surface does
not provide — the (R9) lesson as a standing test (universal quantification over a family the
surface carries as an orbit is the named hazard).
Origin: the rails-residue ledger — R-linearity vs the integral lattice; (R9)'s universal rendering;
the unconditional jump claim; "locally constant away from 0"; addressless U^H — each caught one
round after writing. Prevention at draft time, not only catch at review. The registrar checks the
section's presence as it checks fence gates.

## THE LIVING-FILE PIN RULE (added 2026-08-06, from the 600 review)
A living document (the questions register, the tracker, any append-under-way file) cannot bear a
file-hash pin — its hash advances by design. Relay preflights and artifact authority tables cite
living documents BY ENTRY (the entry ID and, where needed, the entry's own content hash), never by
whole-file hash. Sealed artifacts retain whole-file pins. Origin: the 600 review's source-10 note —
the register's hash "changed" because the entry recording the very prep under review was appended.

## THE CARRIAGE RULE (C-V3, adopted 2026-08-06 from the DoR V003's self-charge)
No artifact may assert carriage over a class of clauses by summary sentence ("everything else
carried verbatim") — that is precisely the assertion that has now failed in both directions across
lanes. Carriage is shown, not claimed: clause blocks reproduced in full; every change enumerated
individually; a delta board listing what moved and what did not. A shortened guard is a weakened
guard: deletions of regression rows or not-computed qualifications are substantive defects, not
formatting. Reviewers test carriage mechanically (the Q-528 standard).

## SWEEP PROTOCOL ADDENDUM (2026-08-06, from the 614 disclosures)
Fixed-string searches defeat regex-metacharacter false negatives but not LINE-WRAP ones: token
presence checks run against whitespace-normalized copies. And the C-V5 CARRIAGE INSTRUMENT is
RATIFIED as standing (registrar ratification, principal informed): carriage is a finite equality
over a NAMED diff — diff hunks enumerated, row-sets summing exactly, verified by re-diff — the one
form a sweep can verify rather than merely fail to falsify. Remedy substitutions by lanes remain
subject to ratification (the three-tier rule); the C-V5 substitution was ratified WITH its ordered
predecessor enumeration still executed as an addendum.

## APPEAL PREFLIGHT RULE (added 2026-08-06, Q-556)

Before raising a MACHINERY-APPEAL on a conflict between two sealed statements,
the lane MUST search the questions-settled register and the supervision decision
files for a superseding ruling on either statement, and must quote the LATEST
registered state. A true historical quote consumed after its supersession is a
defect, not an appeal. (Origin: relay 618's S06/S12 appeal, dissolved at Q-556
by a principal ruling registered 2026-07-30 that the assembly did not consult.)

## M-2 ADDENDUM: THE FOURTH FALSE-NEGATIVE MODE (added 2026-08-06, Q-561)

Hyphenation variance joins regex-metacharacter, line-wrap, and self-reference as
a known M-2 false-negative mode: "open-event" vs "open event" vs "open_event".
Guard 2 (whitespace normalization) does NOT catch hyphen/space/underscore
variance; normalize `[-_ ]` jointly, and treat guard 3 (reading in context) as
the only reliable closure. A zero hit under guards 1-2 alone is never an absence.

## ONE-CLIPBOARD DISCIPLINE (added 2026-08-06, after the third missed paste)

The clipboard holds exactly one relay. The registrar MUST NOT pbcopy a new relay
while any tracker row reads LOADED — NOT SENT: write the new relay to disk,
mark it QUEUED, and load it only after the pending paste is confirmed sent.
When a lane's return arrives while another lane's relay is pending on the
clipboard, the pending relay keeps the clipboard. (Origin: relays 620, 627, and
632 were each overwritten before first paste; each cost an idle-lane round.)

## PRE-SEAL PIN CHECK (added 2026-08-07, after the third near-false certificate)

A certificate is a report about intent unless recomputed from the bytes. Before
sealing, every builder MUST, on the FINAL written artifact:
1. regenerate the diff mechanically and derive the delta table FROM it (never
   from memory of the edits);
2. for every claim of the form "field/content F present at location L", run a
   fixed-string search of L on disk and display the hit;
3. for every pair of locations required to agree (lead board vs final board),
   diff the two blocks explicitly — paired blocks regenerated independently
   drift, and this sub-mode has appeared four times;
4. run one adversarial re-read of the finished artifact against its own
   certificate claims.
Origin: the false carriage certificates of the DoR arc and Q-566, and the V003
near-miss self-caught on 2026-08-07 by exactly this procedure. Failure mode is
mechanical, not motivational: warnings do not prevent it; only the displayed
post-write checks do.

## VERDICT-LINE SCOPE RULE + DECLARED-CONVENTIONS RULE (added 2026-08-07, Q-573)

1. A final-line verdict may not claim coverage that the artifact's own scope
   statement disclaims. If the scope says "21 of 28 verified mechanically only,"
   the verdict line carries that qualifier — the headline must match the caveat,
   because the headline is what gets read alone.
2. Before measuring an artifact (diff hunks, counts, spans), read and use ITS
   declared conventions (-U context, counting rules, licensed prose forms). Two
   near-misses of record: a -U 0 measurement against a declared -U 3 spec almost
   charged a false carriage; a mechanical atom test flagged 33 rows where the
   spec's own license made 31 of them lawful.

## C-V5a: THE LINE-LEVEL ATTRIBUTION AMENDMENT (registrar amendment 2026-08-07, principal informed; Q-577)

C-V5's "row-sets summing exactly" is hereby fixed at the LINE level, not the hunk
level. Diff merges adjacent edits from different logical changes into one hunk
(the more so under context settings like -U 3), so hunk-level disjointness cannot
be honored honestly. The amended invariant:
1. hunk-to-row assignment must be TOTAL and SURJECTIVE (every hunk assigned;
   every delta row exhibited);
2. a hunk MAY be assigned to multiple rows ONLY IF the artifact decomposes that
   hunk's changed lines into DISJOINT SPANS, each span assigned to exactly one
   row — disjointness and exact summation hold at the line level;
3. line counts in certificates are computed by a stated method robust to blank
   lines and verified against total line arithmetic.
Origin: the Q-577 adjudication — Codex 2 correctly read the sealed instrument's
disjointness demand; Dario correctly displayed that merged hunks lawfully serve
multiple rows; both readings are honored one level apart. Prior artifacts using
hunk-level shared assignment WITH lawfulness grounds displayed (assembly V004's
Z2) are read under this amendment as requiring the line-level decomposition in
their next version, not as false certificates.

## SWEEP COVERAGE RULE + TEST-CLASS RULE (added 2026-08-07, Q-578)

1. A conformance/sweep transcript must display its PER-ITEM coverage, not just
   its conclusion. `failures = []` without the row-by-row account fails the way
   a carriage certificate fails when it reports a count without its partition.
2. Every conformance test is classified MECHANICAL (pattern-decidable; two
   independent implementations agree) or ADJUDICATED (requires per-row reading
   of which demand the forcer must carry). Misclassifying an adjudicated test
   as mechanical produces honest-wrong zeros: the next lane reruns the pattern,
   reports zero, and is wrong again. (Origin: BR-2 proved mechanical — two runs
   agreed at zero; BR-1 proved adjudicated — two implementations by the SAME
   reviewer erred in opposite directions, +5 and 16 against a true 'at least 7'.)

## THE FIRST-TIME-RIGHT RULES (principal directive, 2026-08-07)

Prevention, not detection. Effective immediately for all build/tranche work:

1. PINS ARE GENERATED, NEVER TRANSCRIBED. One machine-readable pin manifest
   per package; every digest, filename reference, and const derives from it
   mechanically; any state change regenerates the full pin closure IN THE SAME
   DELTA (grep the value AND the name). A hand-written pin is a defect on
   sight.
2. INTERFACES ARE SCHEMAS, NEVER PROSE. Any field one builder emits and the
   other consumes is defined once, in a sealed schema file both sides validate
   against. A prose write-out of a shape is not a contract.
3. NO UNEXECUTED PATH SHIPS. Every emission and validation path in a shipped
   component is demonstrated against a fixture before sealing — success paths,
   fail-closed paths, and every document kind. "Static-clean" without path
   execution does not close a relay that adds a path.
4. STATE CHANGES SHIP WHOLE. A change to spec, root, census, or contract
   ships with every dependent artifact updated in the same relay — pins,
   spans, manifests, both builders' consts enumerated in the relay text so
   neither side discovers the cascade at run time.

Origin: the principal's directive after the run-023..029 cascade; the defect
classes these address are pin sprawl, prose-shape drift, first-contact path
failures, and split-relay state changes.

## THE CROSS-BOUNDARY PREFLIGHT (registrar law, 2026-08-08, after the run-032 false start)

Before EVERY chain invocation, the registrar sweeps every A-side pin of B bytes
(and any B-side pin of A bytes) against the current sealed bytes of the pinned
files — all of them, with correct path bases, counting pins checked. A stale pin
is a ROUTED FIX BEFORE the invocation, not a run stop after it. Rationale: the
boundary firewall pins the other builder's exact bytes by design, so every B
re-pin obligates an A re-pin; the registrar is the only actor who sees both
current packages at once, so this staleness is the registrar's to catch. The
run-032 false start (HASH_MISMATCH on the verdict schema; a second stale pin on
the manifest instance found by the same sweep) is the incident of record.

## THE JURISDICTION CHECK (7A process law, 2026-08-08, principal directive: "we need a way to stop getting in our own way")

The program's self-obstructions share one shape: a rule protective in its home
context, applied where it censors (divergence-as-failure at the junction;
classical tests at the record level; binary verdicts collapsing "cannot see
this" into "false"; the B0 origin hunt). The cure is not looser rules — it is
rules that carry their jurisdiction. Before any criterion, typing, or halt
condition enters a 7A relay, it passes three questions OF RECORD:

1. WHAT WAS THIS RULE WRITTEN TO PROTECT — and is that risk present here?
2. DOES ITS OUTCOME SPACE distinguish "false" from "cannot see this"?
3. IF THE THEORY IS RIGHT, WOULD THIS RULE PERMIT THE EVIDENCE TO APPEAR?
   A rule that would halt on the true signal has failed before it runs.

Nothing is weakened: a rule in its jurisdiction keeps full force; kill
conditions stay preregistered. The check stops rules from answering questions
they were never written to ask. The registrar applies it to every 7A relay
header; lanes apply it to every criterion they author; failures are findings.

## THE RELAY QUEUE PROTOCOL (2026-08-08, principal-initiated efficiency change)

Transport changes; custody does not. The relay content moves by FILE; the
principal's paste shrinks to the relay NUMBER; the STOP gate and one-task-one-
relay boundedness are unchanged. Autonomous lane polling is REJECTED of record
(the seven-hour dead-workflow stall; STOP-after-seal is load-bearing).

- Registrar writes each sealed relay to the lane's inbox BEFORE announcing it:
  Codex 2: <cleanroom>/relay_inbox/   Dario: <archive>/relay_inbox/
- The principal sends the lane a bare number N. The lane's standing rule (
  installed once via a relay header): read relay_inbox/RELAY_PASTE_N_*.md,
  verify its seal, execute under all standing session rules, seal outputs as
  usual, write the completion report to relay_outbox/N_DONE.md, STOP.
- The registrar runs a background watcher on both outbox directories; a
  completion file is the return signal — the principal relays nothing back.
  The registrar still verifies at the artifact level (the DONE file is a
  pointer, not the evidence).
- The clipboard is retired for relay transport; the LOADED — NOT SENT state
  becomes QUEUED — NOT ANNOUNCED. One relay per lane in flight, as ever.

## THE LANE-GUARD CLAUSE (queue protocol amendment, 2026-08-08)

Cross-lane pickup is prevented by three layers: (1) physically separate inboxes
under each lane's OS permissions — Codex 2 cannot reach the archive tree,
Dario cannot reach the Documents tree; (2) one global relay number sequence —
a number never matches two inboxes legitimately; (3) lane-named filenames and
headers. The residual risk is registrar misdelivery, closed two ways:
- REGISTRAR LAW: a relay file is written to exactly ONE inbox — its lane's;
  the supervision/ record copy is not an inbox and lanes never read it as one.
- LANE GUARD (installs via each lane's next relay header): before executing a
  queued relay, verify the header names YOUR lane; if it names another lane,
  write a misdelivery report to the outbox and STOP. Executing another lane's
  relay is a custody breach even when the work succeeds.

## THE PICKUP-ACK CLAUSE (queue protocol amendment, 2026-08-08, principal-initiated)

The standing queue rule gains one step: ON PICKING UP A NUMBER N, the lane
writes `relay_outbox/N_ACK.md` (one line: relay number, lane name, inbox file
digest) BEFORE beginning work; the DONE file still follows at completion.
Three observable states per relay: SENT (the principal reports it), PICKED UP
(the ACK, ~a minute after send), DONE (the completion). A number with no ACK
after a minute means the lane never received it — caught immediately. The
registrar's watcher covers ACK files as well as DONE files. Installs via each
lane's next relay header (Dario from 714; Codex 2 from its next relay); relay
713 predates the clause and runs without it.

## THE SEARCHED-SPACE CLAUSE (2026-08-08, from Q-620)

Any claim of absence states THE SEARCHED SPACE IN THE SAME SENTENCE — "zero
hits in workspace/" is a different fact from "zero hits in the archive", and
concluding the second from the first is the M-2 defect class in search
clothing. Applies to lanes and registrar alike; an absence without its space
is not a finding.

## THE SPAN-COVERAGE RULE (2026-08-08, from Q-622 — the third scope-class law)

A citation pin check tests that the span COVERS THE WHOLE DISPLAYED BLOCK,
never merely that a short probe occurs inside the span. Probe-in-span passed
10/10 while four citations were truncated mid-word. Every pin check of a
span-plus-display pair recomputes the display from the span's bytes, with a
negative control showing a truncated span fails. Companions: the SEARCHED-SPACE
CLAUSE (absence names its space) and byte-not-character offsets on non-ASCII
sources. Scope, not reasoning, is the recurring failure mode; these three laws
are its closure.

## THE OBJECT-NAMES PROBE (2026-08-08, from Q-624 — the fourth scope-class law)

A search for prior work probes THE OBJECT'S OWN NAMES, never only the demand's
vocabulary — the demand says Ref_a where the prior work says T_ref/C_ref, and
a demand-vocabulary search reports an untouched ground that is in fact sealed.
Companion: span end offsets are GENERATED from the quote's last token, never
estimated. With the searched-space clause, the span-coverage rule, and
byte-offsets, this closes the four named scope-failure kinds.

## THE WRITER-EXCLUSION RULE (2026-08-08, from Q-632 — third occurrence, now law)

A census, count, or co-occurrence claim computed over a corpus that includes
the artifact being written EXCLUDES THE WRITER, and says so. Post-seal counts
that differ from pre-seal counts are displayed together (the 715 precedent).

## STATE THE GLOB (2026-08-08, from Q-637 — the fifth scope-class law)

A searched-space declaration states its RECURSION and pattern, not just its
directories — "workspace + supervision, recursive" over a top-level-only glob
is a FALSE declaration. With the searched-space clause, span coverage, byte
offsets, and the object-names probe, this closes the five named scope-failure
kinds. The check code obeys the same law as the prose.

## THE MEANING-PROBE RULE (2026-08-08, from Q-642 — the sixth scope-class law)

A NEGATIVE EXISTENTIAL is probed by MEANING, not phrase: enumerate the ways
the corpus could state the condition (name-forms, condition-forms, verb-forms)
and probe each — or do not claim absence. Zero counts on two phrasings of the
claimant's own coinage are not evidence of absence. Sixth instrument law; the
pattern of record: reasoning holds, instruments fail — every verification pass
that reversed a headline was commissioned by the lane it reversed, which is
the discipline working.

## THE CHAINED-PICKUP CLAUSE + OVERNIGHT PROTOCOL (2026-08-08, principal-initiated)

CHAINED PICKUP (amends the standing queue rule, delivered by principal message
to each lane): upon writing N_DONE.md, the lane immediately checks its
relay_inbox for the SMALLEST relay number greater than N addressed to its own
lane (lane guard applies); if present, it executes it as if the number had
been typed; if absent, it STOPS cleanly. No idle waiting, ever — continuation
happens only when work already exists. All custody (seals, lane guard, ACK,
DONE, STOP-on-empty) unchanged.

OVERNIGHT PROTOCOL (registrar law while the principal is away):
- The registrar stocks inboxes ONLY with ruling-free work (derivations,
  verifications, grind). ANYTHING ruling-shaped (adoption, fork, contested
  result requiring the principal) is PARKED with a morning brief; the lane's
  inbox is left empty at that point so it stops cleanly.
- The registrar verifies, registers, and pushes on each DONE via the watcher,
  and pre-queues the next lawful relay before the current one completes where
  the plan determines it.
- A send with no ACK within its check window is retried once as a queue-stock
  (the chained pickup will find it); a stopped lane stays stopped until
  morning. The morning brief lists: completions, registrations, parked
  rulings, lane states.

## Codex approval-tier note (2026-08-09)

Codex 2 runs under the app's "Approve for me" tier (auto-approves routine actions; still prompts on potentially-unsafe ones). This tier can silently reset to "Ask for approval" (observed after a new project/chat was created), which makes every external action prompt — from outside this looks like a multi-hour ACK-only stall. DIAGNOSTIC: if a Codex relay sits ACK-only for hours with no DONE, check the approval tier in the composer before diagnosing a turn-stall. "Full access" is never used.

## Alignment laws (2026-08-09, after Q-685 — making discoveries enforceable)

1. FLATTENING CHECK: before sealing, every derivation artifact checks its load-bearing
   identifications against DECLINE_REGISTER_V001.md. Any identification matching a
   registered decline must be displayed as CONDITIONAL (with the decline cited) or the
   artifact STOPS with the element named. (Class of Q-685: sealed 768 declined the
   +1/Phi^dagger Phi identification; 775 substituted it anyway.)

2. FREEDOMS-CONSUMED BLOCK: every derivation artifact ends with a block listing every
   free datum it touched, each tagged CARRIED-AS-PARAMETER / CONDITIONED-ON /
   SUBSTITUTED (substitution lawful ONLY with a decision-of-record cited). An empty
   block is itself a claim and is auditable.

3. CLAIM-STATUS DISCIPLINE (binds the REGISTRAR): headline claims enter the register
   as CLAIMED and upgrade to PROVED only after the other lane's adversarial
   re-derivation returns clean. Builder-never-verifies applies to registration too.

4. STATE-BRIEF PINNING: every relay names the current PROGRAM_STATE_BRIEF version and
   digest as a required preflight read; the lane verifies its seal and loads it before
   task work. The registrar re-versions the brief on every material change of law,
   plan, or campaign state. (Answers: the whole picture available to each lane.)

5. RULING-LAST (2026-08-09, principal-endorsed): no question routes to the principal
   as a ruling until three passes have returned empty, in order: (a) the register grep
   (was it answered under another name), (b) the hunt (does the sealed record display
   the answer), (c) the forcing classification (do sealed constraints force it). The
   routing message must cite all three results. Corollary: the rulings that remain
   are the genuine allow-stratum freedoms — the ruling rate is itself a measurement.

6. PE-POINTER-ONLY (2026-08-09, from 777's custody finding): governing documents,
   decisions, and relays cite preregistered expectations by NAME AND DIGEST ONLY —
   never restating their content. A mandatory-read document that restates a PE defeats
   hash-only isolation for every lane that must read it.

7. CORRECTION PROPAGATION (2026-08-09, from 781's disclosure "an adopted refutation
   does not propagate itself"): every registered correction or refutation names its
   known downstream consumers — the artifacts whose formulas consumed the corrected
   object — and marks them corrected/pending. When the consumer set is unknown, a
   consumer sweep is queued before any of those artifacts is consumed further.

4a. PIN GOVERNS FOR THE RELAY'S DURATION (2026-08-09, from 782's custody finding iii):
    the state-brief version a relay PINS is its contract for the whole relay, even if
    the registrar re-versions mid-flight; newer versions may be read and disclosed but
    never silently substituted. 782's handling (comply with pin, disclose successors)
    is the model.
4b. LIVE REGISTRAR FILES (2026-08-09, from 782's custody finding i): EXECUTION_TRACKER
    is a live file; its seal is recomputed IN THE SAME OPERATION as every write. A
    stale tracker sidecar is a registrar defect.

2a. WEIGHTS ARE FREEDOMS (2026-08-09, from 787's beta-sector refutation): the SCALING
    WEIGHT of every carried operator freedom (e.g. w_Phi under beta rescaling) is
    itself a freedom and gets its own row in the freedoms-consumed block. Writing a
    sector table that fixes a weight implicitly is the same invisible substitution
    the block exists to expose.

8. SEAL-PROBE BOTH SPELLINGS (2026-08-09, third occurrence of the trap — 753, 770, 792):
   sidecars attach as <name>.md.seal.sha256 AND as <name>.seal.sha256 (dropping the .md),
   and packet-manifest membership is a third sealing mode. Every seal-existence probe
   tests all three before reporting UNSEALED. A false NO-SIDECAR finding nearly graded
   a sealed demand as ungraded.

## Chain-stall addendum (2026-08-09, second stall signature)

Observed: a lane can write N_DONE and then END ITS TURN without executing the chained
pickup (796 sat queued after 794's DONE; no ACK appeared; approval tier was correct).
DIAGNOSTIC: DONE present + next queued relay unACKed = chain died at turn end, not an
approval stall. FIX: re-type the number. The registrar's watcher flags this by pairing
every DONE with the expected next ACK.

9. ENUMERATION-COMPLETENESS (2026-08-09, from 828's refutation of 827): a positive
   absence is only as strong as the completeness of the enumeration it is absent
   from. Before any "not in the list, therefore not on the path" argument is
   registered, the lane must display why the checked enumeration is the COMPLETE
   requirement set (or find the sibling enumerations — content lists and slot lists
   are distinct governing sources and both must be checked).

## LAW 9b — AUTHORITY TABLES ARE PART OF THE BUNDLE (added 2026-08-10, after the third instance)

A positive absence claimed over a bundle is only as strong as its coverage of the bundle's PINNED AUTHORITY TABLE. Prose-token sweeps of the top-level SPEC/RESULT files do NOT suffice: pinned authorities are consumed content, and a supplier sitting behind a pin defeats the absence exactly as if it sat in the prose. Three instances of record: 827 (slots vs content), 857/860 (the grading under "Typed record-odd superconnection and its square", pinned and in front of the lane), 860 (relabeling stock across 15 authorities). Every absence-shaped final line must state whether authority tables were enumerated.

### LAW 9b REFINEMENT — CLOSURE-FIRST BINDING (added 2026-08-10, per 869's method finding)

The stronger form, now preferred: DECLARE the search closure first (the exact bounded set of sources over which the absence is claimed) and BIND every "missing"/"absent" to that declared closure — "missing" never means a prose-token search over an unbounded corpus. Enumerating tables and stating strength after the fact remains the minimum; closure-first is the standard for new work.

## LAW 10 — THE FORCING-ORDER DISCIPLINE (added 2026-08-10, principal-directed)

Before any NEW BLOCK of work opens, its objects are classified FIRST — INPUT / FORCED-DOWNSTREAM / SELECTOR / MIXED — by a forcing-order audit of the 900 pattern (forcing chains displayed; the minimal basis extracted; basis elements typed derivable vs supply-shaped; the cascade ordered). THE STOP RULE GOVERNS THROUGHOUT: no runs are spent arriving at a downstream value before its basis carriers, laws, maps, or prescriptions exist. Selector-typed values are brought to the principal as prospective freezes at the earliest safe moment (before anything downstream is computed), never reverse-fit. A block's relay budget goes to its basis; everything else falls out. Principal's directive of record: "When we know a value is going to be forced once we have the full terms, why would we spend countless runs trying to arrive at it?" / "let's make sure that we use this approach for the next block of work."
