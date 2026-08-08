# STAGE 8 / TASK 6 / L-V2 — CROSS-CONFIRMATION OF THE LINEAGE V2 BOARD

**Lane:** Dario (Opus 5, cross-family from the Codex build lanes)
**Date:** 2026-08-08
**Scope:** PASTE 711 only — W1 board recomputation, W2 the four refusals, W3 baseline integrity
**Custody:** archive-side read and write; the registrar owns any mirror
**Charge:** re-derive, not trust. Builder never verifies own work.

## Lead determination

```text
BOARD_CONFIRMED       = 24 PASS / 0 FAIL / 6 BLOCKED
BLOCKED_SET           = {A23,A24,A25,A27,A28,A35}
VERDICTS_DIFFERING    = none
ROWS_NOT_RECOMPUTABLE = A21   (verdict carries; the declared baseline cannot re-derive it)
BASELINE_SPOT         = 48/48
DOCUMENT_ROOT         = recomputed, MATCH
MANIFEST_SHA256       = recomputed, MATCH
FINDINGS              = 3 (F1 A35 blocker under-inclusive; F2 binding is an authority
                        chain, not an evidence inventory; F3 the A10 evidence sentence
                        is not supported by its own cited bytes)
FLIPS                 = none — confirmed independently, by two methods
SPEC_SEAL             = false
```

Every verdict in the V2 board survives independent recomputation. Nothing in this
artifact moves a row. What does not survive intact is the *warrant* attached to
three cells: in each case the verdict is right and the stated ground for it is
narrower, or other, than the artifact says. Those are the three findings.

---

## 0. Preflight

### 0.1 Relay and output

[PROVABLE] The relay was read only after its sidecar verified.

```text
relay_inbox/RELAY_PASTE_711_LINEAGE_V2_CROSSCONFIRM_DARIO_V001.md
  f1b84c597badc8e77cd457b9e85a11d4cbedea5957fc1c32abded096565781c0   shasum -c OK
```

[PROVABLE] The output name `STAGE8_TASK6_LINEAGE_V2_CROSSCONFIRM_DARIO_V001.md`
and its seal sidecar were probed before the write and returned ABSENT. No file was
overwritten.

### 0.2 Subject under audit

[PROVABLE] Verified before reading, and equal to the digest the relay states:

```text
STAGE8_TASK6_LINEAGE_V2_MATRIX_CODEX2_V001.md
  fe4c083d915c00824575fe6ae53339500a805f4c1fd0b5f3174a74fdb8c9dba8   25832 B, sidecar OK
```

### 0.3 What this lane consumed, and what it refused

[PROVABLE] The independence law was applied to Builder A's package as follows.
`manifests/` and `inputs/` are lawful reads and were read. `checks/` is off limits.
`D027 = evaluator_build_A/checks/check_map.json` is a bound baseline document, so
it was **digest-verified and never parsed** — the RAW_GROUNDING role from the 686
replay discipline, applied to myself. Every claim in this artifact that could have
been taken from A's check map is instead derived from the sealed spec V012
(`D015`), which is a lawful read.

[PROVABLE] `parent.py` and `producer.py` were **not opened**. Where §5 confirms
Codex's citation of them, the confirmation is against their *inventory rows* in
`D023`, which is a manifest, not code.

[YOURS] One further recusal. `D010` is this lane's own prior review, and it is the
declared old-verdict source. I therefore used `D010` for exactly one thing — to
read off what the *old* board said — and for nothing else. No verdict below rests
on it. A lane may not verify its own construction, and the old board's labels are
not evidence for the new board's verdicts in any case.

### 0.4 Gates

```text
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```

No member was bound. No fixed point was executed, no end test run, no physical
quantity evaluated numerically, and no measured constant consulted. No register,
plan, tracker, git, commit or push action was taken. No evaluator child was
launched and no chain was invoked.

---

## 1. W3 — BASELINE INTEGRITY

The relay asks for `N >= 10` of the 48 document pins. I verified **48/48**, because
the board recomputation in §2 rests on the baseline and a spot check would have
left the rest of that foundation unexamined.

### 1.1 The manifest reproduces exactly

[PROVABLE] The canonical manifest bytes were extracted from the artifact's single
fenced JSON block and hashed independently:

```text
manifest_bytes    13061      declared 13061      MATCH
manifest_sha256   59e05791f7d68a3c1e8185ca4994d970edaff2d327b2142cc9cddfe101b60ef2   MATCH
```

[PROVABLE] The extracted bytes are *exactly* `json.dumps(obj, sort_keys=True,
separators=(',',':'))` — the manifest is canonical, not merely parseable. This was
tested by re-serialising the parsed object and comparing byte for byte.

### 1.2 The document root recomputes, and moves when perturbed

[PROVABLE] Recomputing the stated algorithm from the manifest's own rows:

```text
SHA256("LINEAGE-V2-DOCUMENT-ROOT-v1\0" + SORT_LEX(id \0 path \0 byte_length \0 sha256 \n))

recomputed  52c5e039e178102b1c17c4939dcec42e8e06d9329acb5dd95ce607c594c3a0f8
declared    52c5e039e178102b1c17c4939dcec42e8e06d9329acb5dd95ce607c594c3a0f8   MATCH
```

[PROVABLE] Negative controls, because a root that agrees is worth nothing until it
is shown to disagree: incrementing `D001.byte_length` by one moves the root;
perturbing one hex digit of `D008.sha256` moves the root. Both TRUE.

[YOURS] This check is internal-consistency only. Per BR-1 it cannot exculpate
anything: the manifest is a producer-declared object, and a root computed from
declared values proves the arithmetic, not the pins. §1.3 is the check that
touches reality.

### 1.3 All 48 pins against bytes

[PROVABLE] Every document was resolved archive-side and hashed. Results:

| Class | Count | How verified |
|---|---|---|
| Resolved archive-side, digest **and** byte length match | **40 / 48** | recomputed from the actual bytes |
| `program/` documents, not present archive-side | **8 / 48** | digest verified against the sealed V011 authority table in `D002` |
| Mismatches of any kind | **0** | — |

[PROVABLE] The eight are `D041`–`D048`. They are not archive-side at all — no
case-variant, no alternate path, nothing under `MB Work`. Their declared seal basis
is `packet-v011:pinned-inherited-authority`, so I verified them where that basis
says they live: each of the ten inherited-authority digests occurs in `D002`, and
occurs **on the same table row as its own filename** (lines 108–116 and 122), which
is the binding discipline from the 702 citation-key work — a digest that merely
co-occurs in a document is not pinned by it. All ten bind. `D002` itself hashes to
its own pin.

[PROVABLE] The nine packet members (`D002`, `D031`–`D038`) each bind by name and
digest inside `D001`, and every one of their `seal_basis` strings cites `D001`'s own
digest correctly.

[PART-PROVABLE] **Scope statement, offered as a limit on my own check and not as an
accusation.** For `D041`–`D048` I confirmed *pin-table agreement*, not bytes. The
row A01 cell reads "all ten inherited authority bytes match their V011 pins"; on the
archive side that sentence is dischargeable for two of the ten. The other eight are
presumably present cleanroom-side, where the registrar can close this in one pass.
Absent archive-side is not absent.

[PROVABLE] A related and smaller point: the `D002` authority table carries name,
role and SHA-256 — it carries **no byte length**. The `byte_length` field of
`D041`–`D048` therefore has no sealed witness anywhere I can reach, yet it is an
input to `document_root`. Eight of forty-eight lengths in the root are
producer-declared and unwitnessed. This is not exploitable — the digest is what
identifies bytes — and I record it only so the root's grounding is not overstated.

### 1.4 Codex's own closure checks, retested

[PROVABLE] All nine of the §6 pin-closure claims retested independently and hold:
document IDs unique (48/48); every row binding names an existing ID; all 30 rows
occur exactly once and are exactly A01–A29 + A35; exactly one evaluator spec, one
Builder B instance, one assembly and one scoping document are present, so no
superseded version is carried.

[PROVABLE] Two documents carry no row binding: `D009` and `D010`. That is correct —
they are the old-verdict source, not row evidence — but the manifest schema does not
mark the distinction, so a reader must infer it.

---

## 2. W1 — INDEPENDENT BOARD RECOMPUTATION

### 2.1 Method, and why it is two methods

The relay asks for my own derivation of each row's verdict, not a review of Codex's
text. I ran two, because each covers the other's blind spot.

**Track A — invariance.** A row's verdict can change only if its criterion changed
or its evidence changed. Both are byte-testable. This is exact where it applies, and
it applies to most of the board.

**Track B — blind re-derivation.** Track A can only ever *carry* a verdict; it cannot
detect a verdict that was wrong before. So I re-derived all 30 rows from the
criterion text and the bound documents, under the sealed verdict alphabet, with the
deriving readers **blind to Codex's board and blind to the old board**. I had already
read the V2 board myself and could not unsee it; blinding the derivation was the only
way to get a genuinely uncontaminated second opinion. Each of the seven rows whose
evidence changed was then attacked by two adversarial lenses — one trying to break
every claimed absence, one trying to break every claimed witness.

[YOURS] Track B is not delegation of my judgment. Every disagreement it produced I
adjudicated myself, from the bytes, and §2.4 records where I overruled it.

### 2.2 Track A — the invariance leg

[PROVABLE] **The criteria did not change.** The row criteria are the A01–A29 and A35
cells of `D007`. `D007` is pinned in the old ledger `D009` at
`78f6bb08b7ae89d700cf84a19ebf8e62fa489a4ec6762429ac46d027538cbfe3`, which is
byte-identical to the V2 manifest's `D007`. The old board and the V2 board were
decided against the same criterion bytes.

[PROVABLE] **What is actually new.** Digest-absence from `D009` is not newness:
`D031`–`D038` bind through `D001` and `D039`–`D048` through `D002`, both of which the
old board pinned. Transitively closing that, the old basis is 26 documents and the
genuinely new set is `D009`–`D030` (22 documents).

[PROVABLE] Distributing the new documents over the row bindings:

| | Rows | Consequence |
|---|---|---|
| No new document in the binding | A01–A20, A22, A26, A29 — **23 rows** | criterion and evidence both byte-identical; the verdict carries |
| New document in the binding | A21, A23, A24, A25, A27, A28, A35 — **7 rows** | must be re-adjudicated from the conjunct list |

[PROVABLE] The seven are exactly A25, A27, A35 — the three the relay names — plus
A21, A23, A24, A28. **A21 is the only PASS row that received new evidence.** The
control the relay asks me to choose is therefore not a choice: any other PASS row
would test nothing, because nothing about it changed. I take A21, and §3.4 is the
control.

[YOURS] The invariance argument has one dependency worth naming aloud, because it is
where BR-1 bites: it is only as good as the *bindings*, and the bindings are
producer-declared. If a row's binding omits evidence that bears on it, invariance will
carry a verdict that should have moved. I did not assume this away; F2 is what testing
it produced.

### 2.3 Track B — the blind board

[PROVABLE] Thirty rows derived blind, then compared:

```text
blind derivation   22 PASS / 0 FAIL / 8 BLOCKED
V2 board           24 PASS / 0 FAIL / 6 BLOCKED
agreement          28 / 30
disagreements      A10, A21   (both: blind BLOCKED vs board PASS)
```

[PROVABLE] The six BLOCKED rows of the board were reproduced blind, independently,
every one. Adversarial verification then attacked each of the seven changed rows
under both lenses: **no lens refuted any BLOCKED verdict**, including the lens whose
whole job was to find a witness the deriver had missed.

[YOURS] That is the strongest form of confirmation available here. The six refusals
are not being taken on Codex's word; they were re-found from the criteria by readers
who had never seen Codex's board, and then survived attack.

### 2.4 The two disagreements, adjudicated

Both blind BLOCKEDs are readings I decline to adopt, for different reasons. Both
derivations are displayed, as the relay requires.

#### A10 — I overrule the blind derivation; verdict PASS stands

**Blind derivation (BLOCKED, high confidence):** A10 demands identity cell metrics
*derived* from the declared conditions. `D002` reaches `M_0=M_1=M_2=I` only at
`[19640,19666)` — "If consistent, they force:" — a conditional whose antecedent is
never discharged, followed at `[19746,19977)` by "This is a new physical hypothesis,
not a result inherited from the action character. Gate 3 must classify coherent
Hilbert functors starting from all positive-definite forms and prove whether one
unitary equivalence class survives." A Gate-3 classification proof is a proof
package, and it is absent — which is BLOCKED under the sealed alphabet.

**Why I do not adopt it.** The derivation is factually right and the reading is too
strong. A10's criterion (`D007 [3551,3638)`) is *"Identity cell metrics are derived
from the declared conditions, **not asserted by status**."* The contrast clause names
the failure mode, and it is status-smuggling. A01–A29 are the SPEC-SEAL block, whose
own definition in `D007` is that the tests *"are completely and consistently
specified without a target value"* and that *"all unexecuted result rows are
PENDING-BY-DESIGN rather than silently passed"*; executed passes are A30's business,
not A10's. `D002` routes the metrics through six named conditions, labels the result a
hypothesis in its own words, and sets `Hilbert_functor_gate_passed = false`. That is
precisely the behaviour A10 rewards. The blind reader applied a completion standard
to a specification row, and said so itself: it flagged the interpretive fork
unprompted and marked only the reading, not the facts, as carrying risk.

[PROVABLE] The facts it found are nonetheless real, and they produce **F3**.

#### A21 — verdict carries, but the declared baseline cannot re-derive it

**Blind derivation (BLOCKED, high confidence):** A21's criterion is the longest on the
board, and roughly half of it is the axial block — construct C and P separately,
compute the combined action on the complete scalar/pseudoscalar family, disclose the
regulator and topological branch, prove the discrete axial map preserves the
regulated Dirac domain, account for boundary/eta phases, derive rather than insert
spectral pairing, evaluate the Fujikawa Jacobian and determinant ratio, reject a
nonzero-index control. In the bound set `{D002, D011, D031, D032}` the entire block is
carried by **one table row** — `D031`'s SP04 — plus boolean status flags.

[PROVABLE] I checked this myself rather than take it. Across all four bound
documents, whitespace-normalized: `Fujikawa` 1, `spectral pairing` 1, `eta phase` 1,
`rephas` 0 — and every hit sits inside that single SP04 cell. The cell's column
header, at `D031` line 25, is **`| ID | Obligation | Current state | Closure
condition |`**. The axial content occupies the *closure-condition* column: by the
table's own declared semantics, the condition that *would* close the obligation. That
is not an exhibit.

[PROVABLE] Both adversarial lenses failed to refute it, and the absence lens widened
scope to the entire sealed packet and the sealed evidence root before conceding.

**Why I do not book BLOCKED either.** Because the axial derivation **exists**:
`workspace/BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md`, 5748 B,
`8a68b5f269a5be1d9628be6058d7838c60c4e42d43ee167f19b86fdea80e9ab4`. Booking BLOCKED
would assert that A21's evidence is absent, and I have proved it is not absent — it is
*unbound*. An unearned BLOCKED is as false as an unearned PASS.

**What I book instead.** A21 = PASS, **carried by invariance, not re-derived.** Its
verdict cannot change on V2, because the criterion is byte-identical and the one new
document in its binding is verdict-neutral by its own words (`D011 [3542,3578)`: "A21
retains its recorded PASS state", and §2 of that artifact adds "no A21 row was
re-adjudicated"). But the V2 baseline as constructed cannot produce that PASS from its
own declared evidence. That is **F2**.

[YOURS] This lane has met this shape before and has a name for it. When the R9
precondition could not be replayed, the answer was not `true` and not `false` but a
third outcome, because *a FAIL that was never evaluated is not a verdict*. The same
applies upward: **a PASS the declared baseline cannot re-derive is not a recomputed
PASS.** I record A21's verdict as carried and its recomputation as unavailable, rather
than let a carried label pass for a derived one.

### 2.5 The board

| Row | Old | V2 | My route | My verdict |
|---|---|---|---|---|
| A01–A09, A11–A20, A22, A26, A29 | PASS | PASS | invariance + blind re-derivation, both agree | **PASS** |
| A10 | PASS | PASS | invariance; blind BLOCKED overruled on the criterion's own contrast clause (§2.4) | **PASS** |
| A21 | PASS | PASS | invariance only — not recomputable from the declared binding (§2.4, F2) | **PASS, carried** |
| A23 | BLOCKED | BLOCKED | re-derived + 2 lenses, unrefuted | **BLOCKED** |
| A24 | BLOCKED | BLOCKED | re-derived + 2 lenses, unrefuted | **BLOCKED** |
| A25 | BLOCKED | BLOCKED | §3.1, re-derived + 2 lenses, unrefuted | **BLOCKED** |
| A27 | BLOCKED | BLOCKED | §3.2, re-derived + 2 lenses, unrefuted | **BLOCKED** |
| A28 | BLOCKED | BLOCKED | re-derived + 2 lenses, unrefuted | **BLOCKED** |
| A35 | BLOCKED | BLOCKED | §3.3, re-derived + 2 lenses, unrefuted | **BLOCKED** |

```text
PASS_SET    = {A01-A22, A26, A29}
FAIL_SET    = {}
BLOCKED_SET = {A23,A24,A25,A27,A28,A35}
24 + 0 + 6  = 30                       differs from the V2 board on: nothing
```

---

## 3. W2 — THE FOUR REFUSALS, RE-DERIVED FROM THE CONJUNCT LISTS

### 3.1 A25 — no flip [PROVABLE]

The PASS condition is stated by `D012` itself at `[48603,48735)`:

```text
A25_PASS iff RA25-1 + RA25-2 + RA25-3 + a lawfully formed connected response
             subject + RA25-5 jointly satisfy every A25 quantifier.
```

`D013`'s own consequence board closes exactly one of those. §3.1 records RA25-2/C25.2
as "census display supplied inside this held-out certificate"; §3.2 at `[19928,20027)`
and following records C25.1 "untouched / TYPE-U", C25.3 "untouched", C25.4
"untouched / TYPE-U". Five conjuncts, one closed. **BLOCKED.**

[PROVABLE] `D013` §2.9 is titled "No admissibility or exclusion conclusion" — the
certificate declines to overreach in its own words. Codex's cited content checks out
against the bytes: `Fix_L` five-dimensional, whole projectivization `CP^4`, and the
document's own emphasis that "The **whole** `CP^4`, not five selected coordinate rays,
is the census."

### 3.2 A27 — no flip [PROVABLE]

`D012 [48748,48890)`:

```text
A27_PASS iff RA27-1 + RA27-2 + RA27-3 + RA27-4 + RA27-5 + RA27-6 jointly satisfy
             every elementary and common-refinement quantifier in C_ref.
```

`D013` §3.1 closes RA27-1/C27.2 — "generated six-by-six local Lorentzian `J_star` and
exact square" — and §3.2 leaves C27.3, C27.4, C27.5 and C27.6 untouched. Six
conjuncts, one closed. **BLOCKED.**

[PROVABLE] The square verifies in the document's own display, and its §1.5 scope
fence states the proved statement is exactly `J_star^2 = -I_6` on
`span_R{01,02,03,23,31,12}` with the frozen conventions — a local certificate that
declares its own limit.

[YOURS] Both certificates behave exactly as a held-out repair should: they close what
they can prove and say plainly what they have not touched. The reason A25 and A27 do
not flip is not that the repairs failed; it is that a conjunction of five and of six
does not close on one.

### 3.3 A35 — machinery real, row not earned, and the stated blocker is short [PROVABLE]

**The counts are exact.** From `D028` directly — a lawful `inputs/` read, parsed by
me: 56 check records, of which `available=true` for exactly one, `C-B-V009-06`; 3
fixture records, all `available=false`. Codex's "55 structural envelopes and 3
structural fixture observations" is right to the unit.

**The manifest is complete for its partition, and I record that as a pass.** Parsing
the class column of the sealed spec `D015` gives 66 check IDs partitioned 56
STRUCTURAL / 10 GATED-EXECUTION, and 63 `C-B-` + 3 `C-D-`. The set of `D028`'s 56
check records is **set-equal** to the spec's 56 STRUCTURAL IDs — no gap, no extra. The
3 fixture records are exactly the 3 STRUCTURAL fixtures. I went looking for an
under-declaration here and there is none.

**What the criterion actually names.** `D007`'s A35 cell demands, by name, that the
evaluator reproduce and reject the V010 zero-stiffness response and the zero
survival-amplitude response, admit `c` and `tau` competitors, reject primitive/Thomson
conflation, and reject a nonzero-index control. The spec ties those demands to six
fixtures and says so at `[141290,141339)`: *"The six named behaviors are demanded by
A35/V003."* Mapping each to its evidence status:

| A35's named demand | Fixture | Primary check | Class | Evidence |
|---|---|---|---|---|
| reproduce/reject V010 zero stiffness | FX-A35-01 | C-B-V010-01 | GATED | NOT_RUN_GATE |
| reproduce/reject zero survival amplitude | FX-A35-02 | C-B-V011-MR-08 | GATED | NOT_RUN_GATE |
| admit `c` competitors | FX-A35-03 | C-B-V010-02 | STRUCTURAL | absent |
| admit `tau` competitors | FX-A35-04 | C-B-V010-03 | STRUCTURAL | absent |
| reject primitive/Thomson conflation | FX-A35-05 | C-B-V010-04 | STRUCTURAL | absent |
| nonzero-index negative control | FX-A35-06 | C-B-V011-SP1-04 | GATED | NOT_RUN_GATE |

[PROVABLE] **All six of A35's named demands carry zero machine evidence** — three
because the envelope is absent, three because the gate has never opened. The one
certified row, `C-B-V009-06` (single-authority stage dependencies), is **not among
them**. A35 is BLOCKED, and overdetermined.

[PROVABLE] The certification is scrupulous about this and I confirm it: `D022` says
the aggregate verdict is "FAIL, lawfully", and that "NOTHING in this certification
extends the confirmation beyond the one row."

[YOURS] Codex's disposition — that treating fail-closed refusals as proof would
weaken "reproduce and reject" to "detect absent input" — is correct, and it is the
same law as BR-2: a reduction opcode's `.success` is not a truth value. I confirm
it independently. The row's blocker, however, is larger than the artifact states,
which is **F1**.

### 3.4 A21 — the control [PART-PROVABLE]

The control is forced (§2.2): A21 is the only PASS row that received new evidence, so
it is the only one that can test whether my method distinguishes *a row whose PASS was
re-established* from *a row whose PASS was merely carried*. It distinguishes them, and
A21 is the second kind.

[PROVABLE] `D011` does not re-adjudicate A21. It disposes of a residual objection leg
by finding it `NOT_OF_RECORD` for want of any locator — "no filename, digest, section,
line, display identifier, quotation, or other locator for its evidence" — and states
its own limits: "not a merits refutation and not a corpus-wide claim that no objection
could be formulated". It concludes at `[3542,3578)`: "A21 retains its recorded PASS
state."

[YOURS] Two observations, correctly weighted and neither of them a board change.

First, the closure is procedural. A21's PASS carries an open shoulder: the leg was
closed because it could not be located, not because it failed. Anyone who supplies the
locator reopens it. Codex's cell says exactly this and is accurate.

Second — and this is why the control earned its place — the blind reader, knowing
none of that history, went looking for A21's axial evidence and could not find it in
the binding. That is uncomfortably close to the objection that could not be located.
It does not resurrect the leg, whose content remains unrecorded. But it does mean the
gap the leg gestured at is a real gap in the *declared evidence basis*, and that gap is
now located, in F2.

[YOURS] Jurisdiction, recorded and not pressed: the objection leg was raised by this
lane and closed by the producing family. `D011` limits itself properly, so I have no
finding. I note it because the registrar, not either builder, owns that question.

---

## 4. FINDINGS

Three findings. None changes a verdict. All three are the same defect class — **a
sound verdict carrying a warrant that does not support it** — which is why I state
them together rather than as three unrelated notes.

### F1 — `missing_A35_V2` is under-inclusive [PROVABLE]

The artifact's §5.3 names A35's remaining blocker as:

```text
missing_A35_V2 = 55 structural evidence envelopes
               + 3 structural fixture observations
               + independent replay of the resulting criterion outcomes.
```

All 58 named carriers are real and correctly counted. But the sealed spec's own
A35 rule at `D015 [140777,140801)` requires **all 66 check rows PASS and all 6
fixture rows at expected verdict**, and continues at `[141079,141181)`: *"Before those
gates open, every affected row is `NOT_RUN_GATE`; therefore the aggregate cannot be
PASS."*

Delivering all 58 named carriers would leave 10 checks at `NOT_RUN_GATE` and 3
fixtures unobserved. Those are gated on the physical-evaluation, response, and
charged-access gates; **no quantity of structural evidence opens a gate.** The third
bullet does not absorb them either — a gated row produces no outcome to replay.

[YOURS] Why this matters beyond bookkeeping: as written, the blocker reads as a
delivery list, and a delivery list invites the expectation that A35 flips when
delivery completes. It does not. A35 is downstream of the physics rows, not merely of
the formalization remainder. The artifact's own prose sees this — §5.3 says the
criterion "is stronger than the old absence summary" — and then the blocker it
publishes omits the stronger half.

**Repair:** add the 10 gated check rows and the 3 gated fixtures (FX-A35-01, -02, -06)
to `missing_A35_V2`, marked as gate-blocked rather than evidence-blocked, so the two
kinds of absence are not conflated.

### F2 — the row binding is an authority chain, not an evidence inventory [PROVABLE]

The artifact states in §2 that *"Each row binding is also the evidence-source
inventory for the corresponding board row"*, and describes the rerun method in §3 as
asking *"whether every original conjunct has a current witness in that row's manifest
binding."*

For A21 those two sentences cannot both hold. Applying the stated method literally to
A21's declared binding yields BLOCKED (§2.4), because the conjunct-level carriers are
not in it.

[PROVABLE] The scale of it: `D031`'s own build chain
(`scripts/audit_bid_source_parent_closure_gate_v003.py`, and the sealed-manifest
builder alongside it) declares 24 source-parent members. **4 of the 24 are in the
48-document baseline.** The other 20 — including
`BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md` and
`BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md`, which carry A21's two heaviest
blocks — are archive-side, real, and unpinned by the baseline.

[YOURS] This is a design, not an oversight, and I say so plainly: 4-of-24 is not a
forgotten file. `D031` is a closure *gate*, and binding the gate rather than inlining
its members is a coherent choice. Codex also disclosed its inclusion rule in §2 —
packet members, inherited authorities, lineage roots, package members, sidecars —
and BID-era source-parent members are not among those classes. The defect is not the
choice; it is the two sentences that describe the result as a conjunct-level evidence
inventory when it is an authority chain.

[PROVABLE] The consequence is not merely descriptive. `D007`'s invalidation rule at
`[472,541)` reads *"An edit to a row's input invalidates that row and every row below
it."* An edit to `BID_AXIAL_PHASE_CP_REDUCTION_DERIVATION_V001.md` would change
`D031`'s content-addressed basis but move **neither** the baseline document root
**nor** any of the nine pin-closure checks, and would invalidate nothing — unless
`D031` is regenerated. **The baseline's tamper-evidence does not reach A21's actual
conjunct carriers.** That is a real gap in the guarantee the baseline is there to
provide.

[YOURS] This is BR-1 wearing new clothes. The row binding is a producer-declared
object, and it carries a criterion's direction — by deciding what counts as the row's
evidence. Hash-pinning prevents substitution, not fabrication; here it does not even
prevent substitution, because the bytes in question are outside the pinned set.

**Repair, in the registrar's gift, not mine:** either extend the baseline to the
conjunct-level carriers for rows whose binding is a gate, or restate §2 and §3 to say
that a gate document stands as the authority for its members, and record which rows
are consequently carried rather than re-derived. Either is honest; the current pairing
is not.

### F3 — the A10 evidence sentence is not supported by its own cited bytes [PROVABLE]

The A10 board cell reads: *"the displayed Gram derivation still gives the three
identity metrics"*, citing `D002`.

`D002` contains exactly **one** occurrence of "Gram", at line 1184, and it is about
the public-closure criterion — *"a finite projector/Gram-matrix equation"* for the
record condition — which is A13/A14 territory, not the cell metrics. There is no
displayed Gram derivation of `M_0=M_1=M_2=I` anywhere in `D002`. What `D002` actually
does is route the metrics through six declared conditions with a hedge ("If
consistent, they force"), label the result a new physical hypothesis, and defer the
classification to an unexecuted Gate 3.

[YOURS] The verdict PASS is right (§2.4) — and it is right *for a different reason
than the cell gives*. The correct evidence sentence is roughly: "the three identity
metrics are routed through the six declared Hilbertization conditions and openly
flagged as an unproved hypothesis, with Gate 3 unexecuted" — which is what A10's "not
asserted by status" clause actually rewards. As written, the cell claims a derivation
the corpus does not contain, in a row whose entire subject is not claiming derivations
you do not have.

### Not findings

[PROVABLE] Recorded so the negatives are visible, since a check that passed is worth
as much as one that failed and is easier to forget:

- I suspected the evidence manifest under-declared its fixtures, because the fixture
  IDs start at `03`. It does not. `01`, `02` and `06` are the GATED fixtures and are
  correctly outside the structural partition. The suspicion was mine and it was wrong.
- Every numeric claim in the artifact that I could retest is exact: 48 documents, 30
  rows, 66 = 63 + 3, the byte spans quoted for `D022`/`D025`/`D026`/`D027`/`D029`, the
  `D009 [43926,44103)` `missing_A35` quotation, `D023`'s parent and producer inventory
  rows, `D029`'s 14 members and root `2294dfe5…`, `D014`'s `SLOTS = 18 (0 filled / 18
  TYPE-U)`, and the `D013` content quoted in §5.1 and §5.2.
- The `D029` root recomputes from the member rows by the sealed formula. That one is
  my own package, so it is a check I am reporting, not a verification I am entitled to
  perform; the registrar should read it as such.

---

## 5. WHAT I CONFIRM OF THE V2 ARTIFACT

[PROVABLE] The board, row for row: **24 PASS / 0 FAIL / 6 BLOCKED**, blocked set
`{A23,A24,A25,A27,A28,A35}`, no flips. Reproduced by invariance and, independently,
by blind re-derivation that reproduced all six refusals without seeing the board.

[PROVABLE] The baseline: 48/48 pins, canonical manifest, root recomputes and moves
under perturbation, all nine closure checks retested and holding.

[PROVABLE] Every citation I could test resolves to the bytes it claims, with the
single exception at F3.

[YOURS] The three refusals the relay named were each re-derived from the row's own
conjunct list and each survives adversarial attack from two directions. The A35
disposition in particular — that fail-closed refusals on missing input do not
discharge "reproduce and reject" — is correct, is the same law as BR-2, and is the
right call. The producing lane did not flip a row it had every incentive to flip, and
declined to let a real machinery repair stand in for the evidence the row demands.
That is the behaviour the custody graph exists to produce.

---

## 6. SELF VERB AUDIT

| Verb or status | Warrant |
|---|---|
| `MATCH` | SHA-256 recomputed from bytes before any content was read |
| `48/48` | 40 recomputed from archive bytes; 8 verified against the sealed V011 authority table, with the narrower warrant stated in §1.3 |
| `confirmed` | reproduced by two independent methods, one of them blind to the artifact under audit |
| `BLOCKED` | the row's own conjunct list, with the missing conjuncts named and located |
| `carried, not re-derived` | A21 — invariance holds; recomputation from the declared binding does not |
| `overruled` | A10 — my adjudication against a blind derivation, with its reasoning displayed in full and my ground stated |
| `finding` | three, each with the exact bytes that fail to support the stated warrant |
| `not a finding` | one suspicion of mine that the bytes refuted, recorded as refuted |

[YOURS] Disclosures against myself:

1. **My first newness test was wrong.** I initially read digest-absence from `D009`
   as evidence that `D031`–`D038` and `D039`–`D048` were new, which would have made 29
   of 48 documents new and inflated the re-adjudication set from 7 rows to most of the
   board. They bind transitively through `D001` and `D002`. Caught by asking how a
   packet member could be new when the packet manifest is old; corrected before any
   verdict rested on it.
2. **I ran the blind derivation because I was already contaminated.** I had read the
   V2 board before deriving anything, and could not un-read it. The blinding is a
   correction for a limitation of mine, not a flourish.
3. **A21 is where I most want to be sure I have not over-read.** Two blind readers and
   two adversarial lenses said BLOCKED; I book PASS. I book it because the axial
   derivation exists and I found it, which makes BLOCKED false, and because A21 is a
   specification row. If the registrar reads A21's criterion as demanding the exhibit
   in the binding, F2 becomes a board change rather than a warrant defect, and that
   reading is available on the bytes. I record the fork rather than hide it.
4. **One check I commissioned did not return.** Alongside the 13 blind derivations and
   the 14 adversarial lenses (all of which returned; no lens refuted any BLOCKED
   verdict), I commissioned one reader whose sole job was to attack the row bindings
   for completeness. It did not come back. F2 therefore rests entirely on my own
   derivation from `D031`'s build chain, re-tested from bytes in the pin check, and
   carries no independent corroboration. I state this because F2 is the heaviest
   finding here and a reader is entitled to know which of its legs exist.
5. No verb in this artifact proves, authorizes, computes, binds a member, or grants a
   seal.

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
