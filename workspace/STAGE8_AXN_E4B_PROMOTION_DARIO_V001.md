# STAGE 8 / [PLAN:AXN-CONSTRUCT-A1] — PROMOTE E4b: IS THE ADOPTED WRITE RULE PARENT-INDUCED?
## DARIO LANE (Builder B) — V001

RELAY 821. Lane guard PASS (DARIO). Inbox `RELAY_PASTE_821_E4B_PROMOTION_DARIO_V001.md`
= `f2768d980083a9bfbaff929b261627384267e6151a6880f157485cb04444dc7e`, seal verified BEFORE reading.
State-brief pinning: `PROGRAM_STATE_BRIEF_V005.md` = `e26f0d16055f3e83…`, verified and read.

GATES DECLARED AND HELD: `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`. **No rule adopted — derivation attempted only.** No smooth import;
no EM identification; no member bound; no fixed-point execution; no end test; no numeric evaluation
of physical quantities; no comparison to measured constants. PE-1..PE-11 pointer-only.
Builder-B independence held. No register, plan, tracker, git action.

**ALL HEADLINE ITEMS ARE CLAIMED.**

### Sources, custody verified before reading (law 8, all modes incl. the group-sidecar mode)

| role | file | SHA-256 (16) | seal |
|---|---|---|---|
| CIS | `CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md` | `b0c636f3b2b00f06` | B (`.seal`) OK |
| RED | `CAUSAL_DIRECT_LIMIT_REDUNDANT_RECORD_RESULT_V001.md` | `3359960fb411eff8` | manifest OK |
| MF | `R3_4_CAUSAL_CELL_MOVING_FRONT_RESULT_V001.md` | `ed4572ebfece9da2` | **group sidecar** OK |
| 803 | `STAGE8_C1_E4_CROSSCHECK_CODEX2_V001.md` | `3a17200d49a788af` | A OK |
| 800 (mine) | `STAGE8_C1_E4B_PROOF_AND_MOLLER_HUNT_DARIO_V001.md` | `162c6d7ddcd280f5` | A OK |
| 799 (mine) | `STAGE8_C1_E4_VERIFICATION_DARIO_V001.md` | `b760e1b91c931545` | A OK |
| ARCH | `CAUSAL_DIRECT_LIMIT_ARCHITECTURE_ADJUDICATION_RESULT_V001.md` | `9be3f55fd527b9a8` | manifest OK |

**LAW 8, SECOND CONFIRMED INSTANCE OF THE GROUP-SIDECAR MODE.** MF has **no sidecar in either
standard spelling**. Its seal is `R3_4_CAUSAL_CELL_MOVING_FRONT_V001.seal.sha256` — a bundle
sidecar with the word `RESULT` dropped — carrying `ed4572ebfece9da2…  …MOVING_FRONT_RESULT_V001.md`,
matching live bytes. I found the same mode at 820 on the outgoing-GNS result. **Two independent
instances make this a systematic R3.4 bundling convention, not an accident**, and MF is the
decisive document of this relay: without mode-D probing I would have filed it UNSEALED and returned
a false obstruction. Recommendation, not a ruling: law 8 should name the mode.

---

## 1. THE TARGET, AND THE CONCESSION IT STARTS FROM

803's defect against my own 800, verbatim (`3a17200d49a788af` `[13151,13368)` sha `42bd162d7e821557`):

> *"every physical exhaustion is a prefix/down-set chain by `RED` | **REFUTED AS A DERIVATION** |
> `RED` orders writes; it does not type exhaustion stages as prefixes"*

**I concede this in full, without qualification.** My 800 §1.3 (`162c6d7ddcd280f5` `[5507,5821)` sha
`2fdeb0212cf6b325`) is headed *"Step 2 — exhaustion stages are causally down-closed. **Derived, not
hypothesised**"* and argues from a machine check that every prefix of a linear extension is a
down-set. That check is correct and irrelevant: it establishes a property of *prefixes of linear
extensions*, and then I treated exhaustion stages as though they were such prefixes. **They are not,
and nothing in RED makes them so.** RED constrains the order of writes within a given set; it does
not type the stages of an exhaustion. The step is a conflation of write order with stage structure,
and 803 is right to refuse it.

The relay's charge: derive it **from the parent**, or display the failing step.

---

## 2. THE PARENT-SIDE ATTEMPT, AND WHY IT FAILS — CLAIMED

### 2.1 The candidate

CIS is the parent's own support law (adopted Level-1, *"frozen before construction or evaluation of
the causal parent that uses it"*), and it contains the one sentence that looked capable of forcing
down-closure:

> *"Once the **future boundary** has crossed the closure face of `Omega_c`, the same primitive
> incidence is absent from the active generator. **A physical exhaustion adds new future incidences
> on new record factors**; it does not reapply a completed incidence to its old record factor."*
> — with `physical_exhaustion_adds_future_incidences = true`.

**Candidate lemma.** If a physical exhaustion may only ever add incidences in the *future of the
current stage*, then, since cofinality forces every predecessor `p ≺ c` to appear eventually, `p`
cannot appear after `c` (it would be a past addition). Hence `p` appears no later than `c`, so every
stage is causally down-closed, and 803's defect is repaired from the parent rather than from RED.

### 2.2 The lemma fails. Exhibit displayed.

The lemma needs the **strong** reading of "future" — *future of the whole current stage*. The weak
reading — *not yet run* — is equally available in the sentence, and the sentence's own contrastive
clause (*"it does not reapply a completed incidence"*) shows its subject is **reuse**, not
past-completeness.

**A principle's operational content is its falsifier list, and CIS's list does not implement the
strong reading.** Take a causal complex with `p ≺ c` and the exhaustion `V_1 = {c}`, `V_2 = {c,p}`.
It is nested and cofinal, and `V_1` is not down-closed. Walking CIS's seven falsifiers against it:

```text
same primitive incidence remains active after its closure face   NOT TRIGGERED (each runs once)
new records by RERUNNING a completed incidence                   NOT TRIGGERED (p runs once)
a later primitive cell acts on an EARLIER record factor          NOT TRIGGERED (p writes its OWN
                                                                   new factor, not c's)
assigned support not Lorentz-covariant                           NOT TRIGGERED
linear extensions disagree on SPACELIKE-separated events         NOT TRIGGERED (p,c are causally
                                                                   related, not spacelike)
parent requires a separately selected post-write switch-off rule NOT TRIGGERED
a generated descendant destroys the public outgoing sector       NOT TRIGGERED
```

**Zero of seven fire, and the stage is not down-closed.** The reason is structural and worth stating
plainly: **every operative clause of CIS is future-directed** — anti-reuse and no-back-action. Both
govern what a *later* cell may do to an *earlier* record. **Neither constrains a stage's
past-completeness**, which is what down-closure is about. A principle built to stop the future
disturbing the past cannot, by its own content, force the past to be complete.

**FAILING STEP, TYPED:** the strong reading of *"new future incidences"* is not implemented by any
CIS falsifier, so it cannot carry a derivation. Moving the argument from RED to CIS does not repair
803's defect. **The down-set route is dead from the parent side as well.**

I note for the record that the CDL Principle's *"causally sequential"* clause — *"every new
primitive cell opens after all closure faces of the prior stage"* — **is** the strong reading. But
the Principle presents it as the definition of the admitted exhaustion class, i.e. as a scope
restriction. Deriving down-closure from it would assume precisely what is to be shown. I decline
that route as circular.

---

## 3. THE DECISIVE FINDING: THE DOWN-SET ROUTE IS THE WRONG TARGET — CLAIMED

Having failed to derive down-closure, I asked what E4b actually requires. **It does not require
down-closure at all**, and the record already says so.

MF (`ed4572ebfece9da2`) `[806,1131)` sha `c0e1c679dfc4fa28`, verbatim:

> *"For distinct record cells: `[B_j,B_k]=0`. All tested commutators are exactly zero, and reversing
> the three-cell gate order changes the completed unitary by only `1.07e-30`. **This is the exact
> algebraic reason any causal linear extension gives the same endpoint map** in the declared
> pure-charge branch."*

and MF's status block seals, as `= true`:

```text
pulse_profile_independence_derived            = true
distinct_cell_generator_commutation_derived   = true
causal_linear_extension_independence_derived  = true      <-- E4b's content, DERIVED
earlier_public_record_nondemolition_derived   = true
central_pointer_sector_derived_for_moving_front = true
```

**`causal_linear_extension_independence_derived = true` is E4b's content, already derived — and
derived from commutativity, not from order structure.** If distinct record-cell generators commute
exactly, the completed unitary is order-independent full stop; the stage sets need not be
down-closed, and the write order need not even be a linear extension.

**Machine-verified here** (numpy, exact-Hermitian exponentials, distinct tensor factors so
`[B_j,B_k]=0` holds identically):

```text
max ||[B_j,B_k]|| over distinct cells                     = 0.000e+00
max endpoint disagreement over ALL 4! = 24 write orders   = 8.555e-16
a NON-down-closed nested cofinal exhaustion
   [[1], [0,1], [0,1,3], [0,1,2,3]]   down-closed per stage: F, T, F, T
   its write order [1,0,3,2] is NOT a linear extension (1 before 0, 3 before 2)
   endpoint disagreement vs the causal order                = 6.866e-16
```

Agreement is exact for stage sequences that are **not** down-closed and for orders that are **not**
linear extensions of anything. **Order-independence is a fact of the algebra, not of the order.**

**Consequence for 803 and for my 800.** 803's refutation stands and my step 2 was wrong — but the
repair 803's framing invites (derive down-sets) is aimed at an object E4b does not need. Both my 800
and 803 spent their effort on the order structure when the sealed stock had already routed around
it. I record that as a finding against my own artifact first.

---

## 4. THE REAL FAILING STEP, AND WHERE IT SITS — CLAIMED

The commutativity route is gated, and MF names the gate in one flag:

```text
moving_front_bound_by_live_complete_parent = false
```

with the conditional stated exactly (`[2497,2862)` sha `9cddf95528bf19cf`):

> *"The current result proves: **if the complete parent realizes its already proposed primitive
> writes as one-use finite causal-cell events, durable public outgoing sectors follow** without any
> spectral-density choice. It does not yet prove that the complete source/gauge/gravity/environment
> action has that form."*

and MF's own reason: *"the corpus has not yet shown that the complete microscopic parent uses this
compact, one-use moving interaction front. A permanently acting stationary incidence parent is a
different completion and fails the endpoint-GNS test."*

**So the write rule's parent-induction is OBSTRUCTED at exactly one step, and it is a step about the
PARENT'S ACTION FORM, not about exhaustions, orders, or down-sets:** whether the complete parent
realizes its primitive writes as one-use finite causal-cell events.

**And that step is fenced.** It requires the complete parent action form —
`complete_parent_action_derived = false` — which is **T5's own content** and the axis of remainder-map
**OBJECT 1**, adjudicated at relays 812/814/818 and scored **FENCED** in my own 820. It is not
lane-derivable today, and reaching for it from here would breach T5.

---

## 5. CORRECTION TO MY OWN 820 — CLAIMED (law 7)

**My 820 mis-scored this item, and the correction matters for the program's sizing.**

820 scored `A1` (the E4b compatibility statement) as **STANDS-ASSEMBLY**, priced **1–2 relays**, with
the words *"components proved; a re-derivation, not a construction"* and *"**No new object
required**."* That is wrong. The promotion is gated on
`moving_front_bound_by_live_complete_parent = false`, which requires the parent's action form —
the object 820 itself listed in its **FENCED** column as F1.

**820's single assembly item is not an independently actionable 1–2 relay re-derivation. It is
blocked behind the very fence 820 marked FENCED.** Re-reading 820's ledger honestly:

```text
820 as sealed:     1 ASSEMBLY (1-2 relays) + 5 OPEN + 1 roll-up + 2 FENCED
corrected here:    0 independently actionable assembly items;
                   A1's COMPONENTS are proved and its ACTIVATION waits on F1 (T5 / OBJECT 1)
```

The completion's remainder is therefore **entirely open-or-fenced**, and 820's `TRUE_SIZE` should be
read with A1 moved out of the cheap column. This does not change 820's structural verdict — one
bottleneck, named items, no new campaign — and it does not change `MAP_DISCHARGE`. It removes the
one item that made the remainder look partly cheap.

**Downstream consumers named, not routed** (law 7): `workspace/STAGE8_AXN_COMPLETION_AUDIT_DARIO_V001.md`
(§2.2, §3.2, and the `SCORE` / `TRUE_SIZE` final lines); `relay_outbox/820_DONE.md`;
`relay_inbox/RELAY_PASTE_821_E4B_PROMOTION_DARIO_V001.md`, whose own framing inherits the 1–2 relay
price from my 820 and is therefore priced on a mis-scored item.

---

## 6. FREEDOMS-CONSUMED (law 2 / law 2a)

```text
CARRIED, NOT CONSUMED:
  RED's write clauses            CARRIED AT SEALED SCOPE; NOT used to type exhaustion stages
  CIS                            CARRIED AS THE PARENT'S ADOPTED SUPPORT LAW; its strong reading
                                   TESTED AND DECLINED, not assumed
  the CDL "causally sequential" clause  CARRIED AS A SCOPE DEFINITION; DECLINED as circular
  MF's five derived positives    CARRIED AS SEALED DERIVED STOCK, at MF's pure-charge-branch scope
  E4a / E4b / E4c                CARRIED AT SEALED SCOPE
  the parent action form         CARRIED AS FENCED (T5), NOT reached for
DERIVED HERE:                    nothing promoted.  Two NEGATIVE results established: the CIS
                                   down-closure lemma fails (exhibit), and down-closure is not
                                   required by E4b (exhibit).
COMPUTED HERE:                   a 7-falsifier walk on an explicit 2-element counterexample; a
                                   commuting-generator order-independence check over all 24 orders
                                   plus a non-down-closed cofinal exhaustion.  Toy models chosen to
                                   exhibit a logical point; NO physical quantity computed, no
                                   parameter fitted, nothing adopted.
SCALING WEIGHTS (law 2a):        NONE CONSUMED.
ADOPTED:                         NOTHING.  The relay's gate "no rule adopted (derived only)" is held:
                                   I derived no rule and adopted no rule; I display an obstruction.
SUBSTITUTED:                     NONE.
```

## 7. FLATTENING CHECK — `DECLINE_REGISTER_V002` (`957476c8c605a370`)

37 rows walked. Live and discharged:

- **S12** (status flags never substituted for member manifests, generators, or proofs) — **LIVE.**
  My §3 rests on MF's `= true` flags. Each is carried as *the record's own sealed typed status* at
  MF's stated scope, never as a proof I have re-executed; and the artifact's verdict is
  **OBSTRUCTED**, so no flag is doing promotion work.
- **S26 / S08** — untouched; no smooth import, no EM identification.
- **S25** — untouched.
- **S34, S03, S28** — carried as typed; the T5 fence is named and **not entered** (§4).

**No undecidable is rescued by reaching for an axiom.** Where the derivation failed I display the
failing step rather than importing the strong reading that would have carried it (§2.2), and I
decline the circular route explicitly.

`FLATTENING_CHECK = clean (37/37 rows walked; S12 live, load-bearing, discharged).`

## 8. SELF-AUDIT

**VERB AUDIT: NOT CLEAN (+4).**

**(1) I CONCEDE 803'S REFUTATION OF MY OWN 800 IN FULL, AND IT WAS A REAL LOGICAL ERROR** — not a
scope slip. My step 2 was headed *"Derived, not hypothesised"* and it was neither: a verified fact
about prefixes of linear extensions was carried across to exhaustion stages, which are a different
object. The machine check I ran there was correct and answered the wrong question, which is the more
embarrassing failure mode.

**(2) I THEN CORRECTED MY OWN 820, WHICH I SEALED THIS SESSION.** 820 priced this item at 1–2 relays
and said "No new object required." It is gated behind the T5 fence that 820 itself marked. Two of my
last three artifacts have now needed correction from the artifact that followed them.

**(3) THE ATTEMPT I WAS COMMISSIONED TO MAKE FAILED, AND I REPORT THE ATTEMPT.** The CIS route was
the strongest parent-side line available and I expected it to land — the "future boundary" language
reads exactly like an advancing front. It died on CIS's own falsifier list. Reporting a dead attempt
with its exhibit is the point of the lane.

**(4) MY POSITIVE CONTRIBUTION IS A REDIRECTION, NOT A PROMOTION, AND I WILL NOT INFLATE IT.** §3
shows the down-set programme is aimed at the wrong object and that the record already routes around
it. That genuinely narrows the target — from "derive a structural property of all physical
exhaustions" to "one named parent-form flag". But **E4b is not promoted**, the flag is fenced, and
the practical distance to unconditional may be *longer* than 820 implied, not shorter.

Every one of the four cuts against my own prior work or against this relay's hoped-for outcome. The
relay asked for a promotion; the honest answer is an obstruction, plus the finding that the
obstruction is not where anyone was looking.

---

```
WRITE_RULE = OBSTRUCTED (failing step typed)
  TWO failing steps displayed, both with exhibits.
  (A) THE DOWN-SET ROUTE IS DEAD FROM THE PARENT SIDE.  803's refutation of my 800 is CONCEDED IN
      FULL: RED orders writes, it does not type exhaustion stages as prefixes, and my step 2
      conflated the two.  The parent-side repair via CIS ALSO FAILS.  CIS's candidate clause is
      "A physical exhaustion adds new future incidences on new record factors", which needs the
      STRONG reading of "future" (future of the whole current stage).  THAT READING IS NOT
      IMPLEMENTED BY ANY CIS FALSIFIER.  Exhibit: on p precedes c with V_1={c}, V_2={c,p} — nested,
      cofinal, V_1 NOT down-closed — ZERO of CIS's SEVEN falsifiers fire, because every operative
      CIS clause is FUTURE-directed (anti-reuse, no-back-action) and none constrains a stage's
      PAST-completeness.  The CDL "causally sequential" clause IS the strong reading but is the
      definition of the admitted class, so using it is circular; declined explicitly.
  (B) THE REAL FAILING STEP, AND IT IS NOT ABOUT ORDERS AT ALL:
        moving_front_bound_by_live_complete_parent = false
      MF states the conditional exactly: "if the complete parent realizes its already proposed
      primitive writes as one-use finite causal-cell events, durable public outgoing sectors follow
      without any spectral-density choice.  It does not yet prove that the complete
      source/gauge/gravity/environment action has that form."
      THIS STEP IS FENCED: it requires complete_parent_action_derived, which is T5's own content and
      remainder-map OBJECT 1's axis, scored FENCED in my own 820.  Not lane-derivable today.

E4B = remains narrowed — but RE-AIMED, and the down-set programme is retired
  THE DECISIVE FINDING: E4b DOES NOT NEED DOWN-CLOSED STAGES.  MF already seals
  causal_linear_extension_independence_derived = true, DERIVED FROM COMMUTATIVITY [B_j,B_k]=0 —
  "the exact algebraic reason any causal linear extension gives the same endpoint map" — together
  with pulse_profile_independence_derived, earlier_public_record_nondemolition_derived,
  central_pointer_sector_derived_for_moving_front, all = true.
  MACHINE-VERIFIED HERE: with [B_j,B_k]=0 exactly, endpoint disagreement over ALL 24 write orders is
  8.555e-16; and a NESTED COFINAL exhaustion whose stages are NOT down-closed, with a write order
  that is NOT a linear extension of anything, agrees to 6.866e-16.  ORDER-INDEPENDENCE IS A FACT OF
  THE ALGEBRA, NOT OF THE ORDER.  Both my 800 and 803 spent their effort on the order structure
  while the sealed stock had already routed around it.
  SO: E4b waits on ONE named parent-form flag, downstream of which EVERYTHING IS ALREADY DERIVED —
  not on a structural theorem about all physical exhaustions.  Scope carried: MF's results are
  stated in the declared PURE-CHARGE BRANCH.
  CORRECTION TO MY OWN 820 (law 7): 820 scored A1 as STANDS-ASSEMBLY at 1-2 relays, "No new object
  required."  WRONG — A1's activation is gated behind F1, the fence 820 itself marked.  Corrected
  ledger: 0 independently actionable assembly items; A1's COMPONENTS proved, ACTIVATION fenced.  The
  completion's remainder is entirely open-or-fenced.  820's structural verdict (one bottleneck,
  named items, no new campaign) and MAP_DISCHARGE are unchanged; what is removed is the one item
  that made the remainder look partly cheap.  Consumers named: 820's artifact (§2.2, §3.2, SCORE and
  TRUE_SIZE lines), 820_DONE.md, and relay 821's own framing, which inherits the 1-2 relay price.

CHAIN_INVOKED = false

VERB_AUDIT_SELF = NOT CLEAN (+4)
  (1) I CONCEDE 803'S REFUTATION OF MY 800 IN FULL — a real logical error, not a scope slip.  My
      step 2 was headed "Derived, not hypothesised" and was neither; the machine check I ran there
      was correct and answered the wrong question.
  (2) I CORRECTED MY OWN 820, SEALED EARLIER THIS SESSION.  Two of my last three artifacts have now
      needed correction from the artifact that followed them.
  (3) THE ATTEMPT I WAS COMMISSIONED TO MAKE FAILED AND I REPORT IT WITH ITS EXHIBIT.  CIS was the
      strongest parent-side line available and I expected it to land; the "future boundary" language
      reads exactly like an advancing front.  It died on CIS's own falsifier list.
  (4) MY POSITIVE CONTRIBUTION IS A REDIRECTION, NOT A PROMOTION, AND I DO NOT INFLATE IT.  The
      target narrows from "a structural property of all physical exhaustions" to "one named
      parent-form flag" — but E4b is NOT promoted, the flag is FENCED, and the practical distance to
      unconditional may be LONGER than 820 implied, not shorter.
  Also recorded: LAW 8 GROUP-SIDECAR MODE, SECOND INSTANCE.  MF has no sidecar in either standard
  spelling; its seal is a bundle sidecar with the word "RESULT" dropped.  I found the same mode at
  820 on the outgoing-GNS result.  Two independent instances make it a systematic R3.4 convention,
  and MF is this relay's decisive document — without mode-D probing I would have filed it UNSEALED
  and returned a FALSE obstruction.  Recommendation, not a ruling: law 8 should name the mode.

alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
