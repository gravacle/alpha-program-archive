# RELAY 711 — DONE — DARIO LANE

Task: PASTE 711 / [TASK 6 / L-V2] — cross-confirm the lineage V2 board (W1 board
recomputation, W2 the four refusals, W3 baseline integrity).
Status: **COMPLETE, SEALED, STOPPED.** No register, plan, tracker, or git action taken.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_711_LINEAGE_V2_CROSSCONFIRM_DARIO_V001.md
         f1b84c597badc8e77cd457b9e85a11d4cbedea5957fc1c32abded096565781c0   sidecar OK
         (verified before the body was read)

OUTPUT   workspace/STAGE8_TASK6_LINEAGE_V2_CROSSCONFIRM_DARIO_V001.md
         c617dcbf2ebb092599ecc45ad357bcef2eb8d421e9016172bfc0529f867449d2
         672 lines / 35,895 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT before the write)

SUBJECT  workspace/STAGE8_TASK6_LINEAGE_V2_MATRIX_CODEX2_V001.md
         fe4c083d915c00824575fe6ae53339500a805f4c1fd0b5f3174a74fdb8c9dba8
         = the digest the relay states
```

## Final lines

```text
BOARD_CONFIRMED = 24/0/6 (differs: none; A21 PASS is carried, not recomputable from the declared binding)
REFUSALS_RECHECKED = A25, A27, A35 + A21 (control, forced -- the only PASS row with new evidence)
BASELINE_SPOT = 48/48 verified (40 against archive bytes, 8 against the sealed V011 authority table)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+4 disclosures at §6)
FINDINGS = F1 missing_A35_V2 under-inclusive; F2 binding is an authority chain, not an evidence inventory; F3 A10 evidence sentence unsupported
FLIPS = none
SPEC_SEAL = false
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

## The board

**Every verdict in the V2 board survives independent recomputation. Nothing moved.**
24 PASS / 0 FAIL / 6 BLOCKED, blocked set `{A23,A24,A25,A27,A28,A35}`, no flips.

I recomputed it two ways, because each covers the other's blind spot.

**Invariance.** The criteria are byte-identical between the boards — `D007` is pinned
in the old ledger at `78f6bb08…`, the same bytes the V2 manifest carries. Closing the
document set transitively (packet members bind through `D001`, inherited authorities
through `D002`), the genuinely new documents are `D009`–`D030`. Distributing those
over the row bindings: **23 rows received no new document** and their verdicts carry
by construction; **7 rows must be re-adjudicated** — A21, A23, A24, A25, A27, A28,
A35. A21 is the only PASS row among them, so the control the relay let me choose was
in fact forced.

**Blind re-derivation.** Invariance can only carry a verdict, never catch one that was
wrong before it — so I re-derived all 30 rows from the criteria and bound documents
with the deriving readers blind to both boards. I had already read the V2 board and
could not un-read it; blinding was the only way to get an uncontaminated second
opinion. Result: **28/30 agreement**, and **all six BLOCKED rows reproduced
independently**. Each of the seven changed rows was then attacked by two adversarial
lenses — one hunting a missed witness, one testing whether each claimed witness
actually discharges its conjunct. **All 14 returned; none refuted any BLOCKED
verdict.**

The two disagreements were mine to adjudicate, and I did, from the bytes:

- **A10** — blind BLOCKED overruled. It applied a completion standard to a
  specification row; A10's own contrast clause ("not asserted by status") names
  status-smuggling as the failure mode, and `D002` does the opposite of that. Verdict
  PASS stands. Its factual findings were real and became F3.
- **A21** — I book neither. Verdict PASS **carries**, but the declared baseline cannot
  re-derive it. See F2.

## W2 — the four refusals

- **A25**: `D012` states the PASS condition as RA25-1+2+3+response subject+5; `D013`
  closes RA25-2 and records C25.1, C25.3, C25.4 untouched in its own words. One of
  five. BLOCKED.
- **A27**: PASS needs RA27-1…6; `D013` closes RA27-1 and leaves C27.3–C27.6 untouched.
  One of six. BLOCKED.
- **A35**: BLOCKED, overdetermined — see below.
- **A21** (control): `D011` does not re-adjudicate the row. It closes a residual
  objection as `NOT_OF_RECORD` for want of a locator and says so with proper limits.
  The control did its job: it distinguished a PASS that was re-established from one
  that was merely carried, and A21 is the second kind.

On A35 I can sharpen the record. Codex's counts are exact to the unit (55/56 absent,
3/3 fixtures absent), and the evidence manifest is **complete for its partition** — its
56 check records are set-equal to the spec's 56 STRUCTURAL IDs, no gap. But mapping
A35's *named* demands onto evidence status shows **all six carry zero machine
evidence**: three because the envelope is absent, three because the gate has never
opened. The one certified row, `C-B-V009-06`, is not among them.

## Findings — three, none of which moves a row

All three are the same defect class: **a sound verdict carrying a warrant that does
not support it.** That is why they are stated together.

**F1 — `missing_A35_V2` is under-inclusive.** All 58 named carriers are real and
correctly counted, but the spec's own A35 rule requires all 66 checks PASS *and* all 6
fixtures at expected verdict, and says in sealed words that before the gates open the
aggregate cannot be PASS. Delivering all 58 would still leave 10 checks at
`NOT_RUN_GATE` and 3 fixtures unobserved — and no quantity of structural evidence
opens a gate. As published, the blocker reads as a delivery list, which invites the
expectation that A35 flips when delivery completes. It does not: A35 is downstream of
the physics rows. The artifact's own prose sees this and then omits the stronger half.

**F2 — the row binding is an authority chain, not an evidence inventory.** The artifact
says each row binding *is* the evidence-source inventory for its row, and describes
the method as checking every conjunct against that binding. For A21 both cannot hold:
applied literally, the stated method yields BLOCKED, because the conjunct-level
carriers are not in the binding. `D031`'s own build chain declares 24 source-parent
members; **4 are in the 48-document baseline.** Among the 20 outside it is
`BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md`, which carries A21's heaviest block.

This is a design, not a forgotten file — 4-of-24 is deliberate, and binding a closure
gate rather than inlining its members is coherent. The defect is the two sentences
that describe the result as a conjunct-level inventory. And the consequence is not
merely descriptive: `D007`'s invalidation rule says an edit to a row's input
invalidates that row, but an edit to the axial derivation would move neither the
document root nor any of the nine closure checks. **The baseline's tamper-evidence
does not reach A21's actual carriers.** BR-1 in new clothes — the binding is
producer-declared and it carries a criterion's direction by deciding what counts as
evidence.

I declined to book A21 as BLOCKED, because the axial derivation exists and I found it
— booking BLOCKED would assert an absence I had just disproved. I booked PASS
**carried, not re-derived**, on the same law this lane established for R9: a FAIL that
was never evaluated is not a verdict, and a PASS the declared baseline cannot
re-derive is not a recomputed PASS.

**F3 — the A10 evidence sentence is unsupported.** The cell cites "the displayed Gram
derivation". `D002` contains exactly one "Gram", at line 1184, about the public-closure
criterion — a different row's subject. There is no displayed Gram derivation of the
identity metrics. The verdict is right for a different reason than the cell gives, in a
row whose whole subject is not claiming derivations you do not have.

## What I confirm

The board row for row; the baseline 48/48 with a canonical manifest and a root that
recomputes and moves under perturbation; all nine of Codex's closure checks retested
and holding; and every citation I could test resolving to the bytes it claims, with the
single exception at F3. The A35 disposition in particular — that fail-closed refusals
on missing input do not discharge "reproduce and reject" — is correct, is the same law
as BR-2, and is the right call. The producing lane did not flip a row it had every
incentive to flip.

## Custody

Independence law held: `manifests/` and `inputs/` read; `checks/` off limits, so
`D027` was digest-verified and **never parsed** — the RAW_GROUNDING role from the 686
work applied to myself. `parent.py` and `producer.py` were not opened; Codex's
citations of them were confirmed against their inventory rows in `D023`. `D010` is
this lane's own prior review and was used only to read off what the old board said; no
verdict rests on it.

Pin check on my own artifact: **30/30 ALL TRUE** — every digest, span, count, and
quotation re-derived from bytes.

Disclosed against myself (§6): my first newness test was wrong and would have inflated
the re-adjudication set from 7 rows to most of the board; I ran the blind derivation
because I was already contaminated; A21 is where I most want to be sure I have not
over-read, and I record the fork rather than hide it; and **one commissioned check —
the binding-completeness critic — did not return**, so F2 rests on my own derivation
with no independent corroboration.

## Gates

No member bound, no fixed point, no end test, no numeric evaluation of any physical
quantity, no comparison to a measured constant, no evaluator child launched, no chain
invoked. Nothing was written archive-side except the artifact and its seal.
