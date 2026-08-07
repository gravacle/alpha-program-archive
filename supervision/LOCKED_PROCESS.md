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
