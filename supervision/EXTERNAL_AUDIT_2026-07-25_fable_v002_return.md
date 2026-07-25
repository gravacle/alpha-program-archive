# External Independent Audit — v002 Files (Fable lane, relayed by Brian)
Received 2026-07-25 (evening) via Brian's relay. Different model family
(Fable, not Opus) — system-level independence this lane's own subagents
cannot provide. Read-only; nothing written to the workspace; no project
script executed. 21 agents, 15 findings raised, 8 confirmed after
adversarial refutation, 7 refuted.

Both BLOCKING findings were INDEPENDENTLY VERIFIED IN CODE by this lane
before any disposition (validate_generator_pieces checks confirmed
schema/Hermiticity/self-referential-assembly only; basis_overlap_key
confirmed lane-supplied with the 2e-11 pin applying only to the unused
literal-named array).

## Findings (as relayed, summarized; full text in the session record)

BLOCKING 1 — Lineage gate authenticates propagators against
ATTACKER-DECLARED generator pieces; nothing pins M/B/p/alpha/Sn to the
sealed spec constructions. Exploit numerically reproduced by the auditor:
zero/diagonal surrogate pieces + closed-form exponential propagators pass
every gate (lineage residual 2.9e-15 vs 5e-3 budget; internal identities
<=1.4e-15; ratio 4.0; sensitivity passes; cross-lane exactly zero) with a
few hundred 32x32 products, no ODE integration, no contact with the
sealed Galerkin parent. The repair binding's R2 fabrication-economics
paragraph is FALSE as written. The v002 test suite's own
synthetic_pieces fixture is a running existence proof (arbitrary
non-causal-ball generator passes the full comparator); the
self-consistent surrogate-pair class was never negative-tested.

BLOCKING 2 — Transport unitary is lane-supplied and unpinned:
basis_overlap_key may name any unitary array; the 2e-11 provenance pin
applies only to the literal name 'basis_overlap_primary_from_independent'
which the transport path never has to use. All transported comparisons
run through attacker-chosen W. One-line fix + false docstring correction.

MAJOR — GPG pre-flight wedge (lesson survives the GPG drop): fail-closed
preconditions must be PRE-FLIGHTED before irreversible path consumption;
the v002 controller would have consumed the canonical Phase-A paths and
only then failed at signing. Applies to the replacement anchoring
mechanism (pre-flight push capability).
MAJOR — R3 budgets give zero discrimination against generator-piece
substitution; "in-band closure" label for custody Section-6 item 2 not
earned; authenticity rests on out-of-band custody.
MAJOR — Connection non-vacuity gate enforced on an unlinked diagnostic
array (diag_connection never tied to genpiece_B_stack or propagators).
MAJOR — controller_context authenticates nothing (any standalone caller
supplies the literal); inline comment overclaims.
MAJOR — B1 receipt attestation gap: output_paths_absent_before_execution
hardcoded True but only the lane's OWN outputs are pre-checked; B1
designates absence of the PRIMARY outputs.
MINOR — Launcher TOCTOU: hash-then-runpy-re-read; read-once repair not
applied to the launcher.
CLEAN — Scope drift: ZERO findings; derive-lane v002 changes strictly
within R2/B3/B4; v001 files byte-identical to custody Section 3.

## Item 1 relayed with the audit: Brian's principal decision (GPG)

Pinned key 18488605D44F65A9B57B610AA5F3A86512A04D61 cannot sign
(passphrase unrecoverable; key predates the program, created 2026-05-05
for Memory Bank security disclosure). Requirement IMPOSSIBLE as sealed;
supersession forced. Decision: DROP GPG signing; do NOT mint a
replacement key; replace with (a) per-artifact external anchoring
(commit+push digest to github.com/gravacle/alpha-program-archive after
each receipt/sealed output), (b) recorded typed principal authorization
gating production launch, (c) archive repo made public with force-push
protection on main. Discovered pre-production with zero production
values in existence — cannot be outcome-shaped.

## Disposition by this lane (all append-only)

1. Production hold honored; signature watcher stopped; .asc will never
   exist; GPG supersession amendment sealed in the workspace.
2. BLOCKING 1 treated as a FALSIFIED SEALED CLAIM: honest-block erratum
   sealed against the repair binding's R2 paragraph; no silent patch.
3. Piece-authenticity mechanism decided and sealed in repair binding
   V002: the comparator reconstructs every generator piece from the
   sealed spec text with its own third implementation (both lanes'
   declared quadratures reproduced exactly), pinning stored pieces at
   frozen tolerances; hostile review + external re-audit required BEFORE
   any production authorization.
4. BLOCKING 2 one-line fix + docstring correction enumerated in V002.
5. Self-consistent surrogate-pair negative test enumerated in V002.
6. Pre-flight rule (all fail-closed preconditions before any canonical
   path consumption) enumerated in V002, including push-capability
   pre-flight for the anchoring mechanism; controller gains per-lane
   invocation so each receipt anchors before the next lane runs.
7. Report to Brian for relay to the reviewer lane after v003 authoring +
   fresh hostile verification complete.
