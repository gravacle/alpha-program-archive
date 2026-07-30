# PROCESS HARDENING — WHAT BELONGS IN CODE, WHAT CANNOT (2026-07-29)

Reviewer design at the principal's question: "what do we need to clean up ... AND what do we
need to do to make sure that we don't repeat them again. Do we need to render some of the
process in code versus relying on hooks and model memory?"

## THE ANSWER, IN THE PROGRAM'S OWN VOCABULARY

The principal's standing test is [allow vs require]: permissions compose and never force a
number; only overdetermination does. THAT TEST APPLIES TO THIS PROGRAM'S OWN PROCESS, AND THE
PROCESS FAILS IT.

Nearly every process rule in this corpus is written as PROSE a lane is expected to follow.
Prose rules are ALLOW-SHAPED: they permit correct behaviour and forbid nothing mechanically.
Every process failure observed in the last two days is a case of a lane (or the reviewer)
being *permitted* to do the wrong thing by a rule that could not stop it.

CODE IS THE ONLY REQUIRE-SHAPED INSTRUMENT AVAILABLE. Hooks and model memory are better than
nothing, but a hook is local and uncloned, and memory is a disposition, not a gate.

## THE EVIDENCE — MEASURED, NOT ASSERTED (cleanroom, 2026-07-29)

- 481 markdown artifacts; 287 have NO seal sidecar (60% unsealed).
- Of 40 sampled sidecars, 40 verify. THE SEAL DISCIPLINE WORKS WHERE APPLIED — the failure is
  coverage, not correctness.
- 303 audit scripts; 34 certify at least one check by SUBSTRING MATCH against prose (11%).
- 233 scripts write literal True/False into result payloads (the hardcoded-flag class).
- 214 checker-shaped scripts already exist — the program is not short of checking machinery.
  IT IS SHORT OF A SINGLE THING THAT RUNS THE CHECKS TOGETHER AND CAN SAY NO.

That last line is the whole diagnosis. The corpus has extensive per-artifact verification and
ZERO corpus-wide gating.

## THE FAILURE INVENTORY, CLASSIFIED BY WHAT COULD HAVE PREVENTED IT

CLASS A — CODE-PREVENTABLE (deterministic, mechanically checkable):
 A1. Eleven commits sat unpushed while the record-integrity ruling made the push THE
     integrity mechanism. [FIXED 2026-07-29: post-commit auto-push hook + deploy_status.sh.
     Caveat: hooks are local and not cloned.]
 A2. Paste numbering collision — the sequence head lived in a directory the search missed.
 A3. Bounded negatives reported in corpus-wide language while scoped to one subtree. THIS
     ONE INVERTED A CONCLUSION OF RECORD.
 A4. Substring-certified audits (34 scripts) — "the markdown says what the markdown says".
 A5. Hardcoded claim flags in result payloads (233 producers) — a literal presented as a
     measurement.
 A6. A stale certification flag reading PASS while 8 of 58 tracked hashes mismatched.
 A7. A results/ PASS string voided by a later provenance/ failure record, with nothing
     cross-referencing them (the SP14 terminal).
 A8. An acceptance marker that is a strict PREFIX of another marker, under substring matching.
 A9. Scripts hardwired to a superseded artifact path (the census gate, found today).
 A10. Sealed-artifact coverage gaps (287 unsealed).
 A11. A sealed pass-condition file the evaluator never reads (predictions.json).
 A12. A field-name mismatch (subject_sha256 vs bundle_sha256) that invalidates 27 reports.

CLASS B — NOT CODE-PREVENTABLE; REQUIRES ADVERSARIAL AGENTS (semantic judgment):
 B1. Match-by-name/fail-by-type. ELEVEN logged instances, five of them the reviewer's, THREE
     TODAY. No linter detects "this is a real object but not the sealed one."
 B2. A synthesis claim outrunning its evidence (the reviewer's gate-6 typing, the
     all-negative-spectrum reading, the "one missing require" chain).
 B3. Whether a negative about a CONCEPT (not a token) holds — unsearchable by construction.
 B4. Whether a physics claim is correct.
 THE COUNTERMEASURE THAT DEMONSTRABLY WORKS is the one now in use: adversarial verification
 with a default-refute stance, quotes at producers, and verdicts of CONFIRMED/PARTLY/REFUTED.
 It has caught every Class-B failure recorded today — including all three of the reviewer's.

CLASS C — THE PRINCIPAL'S, AND MUST STAY THERE:
 C1. Every ruling. C2. Route adoption. C3. Amending a fence. C4. The blind wall.
 CODE MUST NEVER BE ABLE TO MAKE THESE. A checker that could rule would be a checker that
 could fit.

## WHAT TO BUILD — ONE SCRIPT, ONE GATE

`corpus_check.py`, executable, exit non-zero on RED. Checks, each independently reportable:
  1. SEAL INTEGRITY — every .seal.sha256 verifies; report the unsealed set by class.
  2. DEPLOY STATE — archive ahead-count is 0 and working tree clean.
  3. SUBSTRING CERTIFICATION — flag any audit script whose check-dict value is an `X in Y`
     expression over file text. (Detects A4; 34 known instances become a tracked baseline.)
  4. HARDCODED CLAIM FLAGS — flag literal True/False written to claim-shaped keys in result
     payloads. (Detects A5; 233 producers become a baseline, not an alarm.)
  5. VOIDED PASS — any results/ PASS whose hash is named by a later provenance/ failure
     record. (Detects A7.)
  6. MARKER PREFIX COLLISION — any acceptance marker that is a strict prefix of another under
     substring matching. (Detects A8.)
  7. SUPERSEDED-PATH HARDWIRE — any script referencing vNNN when vNNN+1 exists. (Detects A9.)
  8. FINGERPRINT CURRENCY — recompute every tracked-hash manifest. (Detects A6.)
  9. SCOPE DECLARATION — any artifact asserting a negative ("zero hits", "does not exist",
     "nowhere") must declare its search root within N lines. (Detects A3 — THE ONE THAT
     INVERTED A CONCLUSION.)
 10. RELAY SEQUENCE HEAD — report the max paste number across all roots. (Detects A2.)
 11. AUTHORITY CURRENCY — every principal ruling in the supervision layer is cited by at
     least one artifact in the governing chain. (Detects the recording debt class.)

GATING: a pre-commit hook runs `corpus_check.py --gate` and BLOCKS on RED categories
(1, 2, 5, 6, 8, 11). The rest report YELLOW with a tracked baseline that may not grow.
BASELINE DISCIPLINE: existing instances of 3, 4, 7, 10 are recorded once as a frozen
baseline; the gate fails if the count INCREASES. This avoids a 267-item cleanup blocking all
work while making the classes strictly non-worsening.

## WHAT THIS DOES NOT FIX, STATED PLAINLY

It cannot detect Class B, and it must not touch Class C. A green `corpus_check` means the
mechanical invariants hold — NOT that a claim is true. Anyone who reads a green check as
evidence about physics has made exactly the error the check exists to prevent, one level up.
The adversarial verification layer is not replaced by this and must not be reduced because
of it.

## HOOKS AND MEMORY — HONEST LIMITS

Hooks are LOCAL AND NOT CLONED: the auto-push hook installed today protects this machine and
no other. Memory is a disposition that survives sessions but binds nothing. Therefore the
script must be COMMITTED TO THE REPOSITORY (so it travels), the hook is a convenience, and
the report is the artifact. `deploy_status.sh` was committed for exactly this reason.

alpha_computed = false; proof_authorized = false. This design gates process; it can neither
compute nor authorize anything about physics.
