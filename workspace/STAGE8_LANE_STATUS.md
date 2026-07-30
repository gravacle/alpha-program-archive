# STAGE 8 — LANE STATUS AND OPEN-DECISIONS REGISTER

**LIVING DOCUMENT. NON-CITABLE.** Same standing as the calibration ledger's living row:
it records state, it does not create authority. **No artifact may cite this file as a
source.** Every item below points at the sealed artifact that IS the authority.

Snapshot: **2026-07-26**, amended **2026-07-27** (R-16 added; see the counter block for why), amended **2026-07-29** (R-24 added; C4 clause-scoped strike; R-25--R-28 added for authority precedence, C1-C5 ratification, gravity evidence admission, and P2 precondition result).
Authorized by the principal 2026-07-26 ("STANDING OPEN-DECISIONS
ARTIFACT — YES. BUILD IT. Updated on seal."). First of its kind — a search over filenames
and bodies found no prior lane-status or register artifact, so this merges with nothing.

`production_authorized = false` · `alpha_computed = false` · `proof_authorized = false`

---

## HOW TO USE AND MAINTAIN THIS FILE

```text
UPDATE ON SEAL. Any lane sealing an artifact that opens, closes or changes a
principal-held decision updates the corresponding row IN THE SAME ACT. A seal that
changes a decision's state and does not touch this file is an incomplete seal.
THIS FILE IS NOT EVIDENCE. It is an index. If it and a sealed artifact disagree, THE
SEALED ARTIFACT GOVERNS and this file is wrong and must be corrected.
STALE-ITEM DISCIPLINE. A register that lists closed items as open is worse than no
register. Part 3 exists for items that look open but probably are not; nothing moves
from Part 3 to Part 1 without a citation, and nothing is deleted — it moves to Part 2.
```

**A correction carried on the face of the register.** The sweep that motivated this file
reported "exactly ONE machine-readable flag parked with the principal." **That was an
undercount produced by a too-narrow search pattern.** A proper sweep finds ~90 uppercase
status flags and four families tracking principal-held state: `D3_object_spec_status =
HELD_PENDING_PRINCIPAL` (5 artifacts), `kappa_record_carrier_typing = UNDECIDED_PRINCIPALS`
(2), `E_Q1_scoping_answer_from_principal = pending` (2), `F5_ruled_on = false` (1). The
*substance* — decisions are scattered across prose with no index — is why this file exists
and is unaffected. The *number* was wrong.

---

## PART 1 — GENUINELY OPEN. Blocking-and-live first.

### O-1 · Does F'-5 stand as written?  `RIPE — the hold condition is SATISFIED (2026-07-28)`

```text
*** THE TROTTER-KATO REFERRAL HAS RETURNED, AND SO HAVE TWO MORE. *** O-1 was HELD pending exactly
that referral. Three blind referrals (Trotter-Kato / C_n -> C / H-VU) plus this lane's two
source-checks have now discharged H1's antecedent: R-L2b's UNIFORMITY IS REFUTED
(STAGE8_RL2B_UNIFORMITY_REFUTED_RESULT_V001, `52f2490b…`). The trilemma's own reading is that
"keeping F'-5 selects the branch on which R-L2b is refuted" — AND THAT BRANCH HAS OCCURRED.
O-1 IS NOW RIPE, NOT RULED. THE RULING IS THE PRINCIPAL'S AND NO LANE HAS TAKEN IT.
Adjacent and also his: the fourth-horn question — whether a finite Hilbert-Schmidt bound was ever
the right obligation. Neither answered nor prejudged by the refutation.
```
- **Decision.** F'-5 forbids any constant carrying a carrier index `n`. Equivalently: is the
  theory the finite-carrier (Galerkin) theory or the continuum theory? *Not* "which carrier" —
  that earlier framing was corrected.
- **Blocks.** R-L2b's uniform bound; T7(iii) clause 2; E1 v002 (its own text forbids executing
  on a provably unsatisfiable obligation); hence kappa_record and all downstream.
- **Options with costs.** The trilemma, `STAGE8_RL2B_CONVERGENCE_HYPOTHESIS_RESOLUTION_AND_F5_TRILEMMA_V001.md:154-183`.
  **H1** requirement list discharged → R-L2b's uniformity REFUTED. **H2** list not dischargeable
  → the bound is on something that is not the parent's object, and its constant carries `n`,
  violating F'-5 directly. **H3** deny the continuum target → kappa_record acquires a carrier
  index and F'-5 must be weakened, which is the principal's alone. *No horn delivers R-L2b as written.*
- **Origin.** `STAGE8_RL2B_DIAGONAL_ATTACK_RESULT_V001.md:198`; narrowed at `…F5_TRILEMMA_V001.md:226`.
- **Held on.** The blind referral to the independent lane: *"Does the sealed successor Galerkin
  requirement list admit a Trotter-Kato discharge for a nested Hermite family on a Schwartz
  core?"* — **to be sent without the conclusion.** `F5_ruled_on = false`.

### O-2 · E-Q1 — is the pinned skeleton's cell 4-volume admissible under scoping clause 1?  `RULED 2026-07-26 → Part 2 R-14`
> **CLOSED. Option 3 granted, scoped.** Witness `E1_CELL_4VOLUME_ADMITTED_ONLY_ON_PINNED_SKELETON`.
> Kept here with its reasoning intact because the *constraints* the grant carries are live:
> every relying verdict must say "on the pinned skeleton" and may not say "over D3".
> Applied in `STAGE8_PRINCIPAL_RULINGS_APPLIED_EQ1_OPTION3_AND_O4_BLOCKED_V001.md`.
- **Blocks.** E1 v002 execution — and **it blocks by being UNRULED**: grant and decline both
  discharge the precondition. Deferral is the only state that keeps E1 frozen.
- **Options with costs.** `STAGE8_EQ1_DEPENDENCY_DETERMINATION_AND_OPTIONS_WITH_COSTS_V001.md:92-134`.
  **1 DECLINE** — R-L0 fails with its named witness, and R-L0 is F'-5's enforcement mechanism,
  so the failure is not cosmetic. **2 GRANT UNSCOPED** — guts that enforcement mechanism; not
  recommended. **3 GRANT SCOPED [recommended]** — uses the precedent already inside F'-5
  (lines 1678-1680); cost is that every affected verdict must say "on the pinned skeleton" and
  may not say "over D3". **4 DEFER** — the option the clause forbids in substance.
- **Origin.** `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:2286-2290`.
- **Determined INDEPENDENT of O-1**, so it does not wait on the referral.
- **Carry with any grant:** *"granting E-Q1 discharges an execution precondition. It supplies
  no physics."* Ruling it does not make E1 executable — three other gates remain.

### O-3 · C_ref vs D3 — two sealed authorities, determined SAME OBJECT  `OPEN — deferred by the principal`
- **Decision.** V011 freezes a shape-regular admissible class `C_ref`; the D3 quantifier ranges
  over the unrestricted class including all common refinements. Which governs?
- **Blocks.** Sealing of the D3 refinement-natural volume-weight/response-pullback object; T11
  naturality; A-L5 / recast Q6.
- **Options.** Not yet costed. One decisive input **devalues the restriction branch**: R-L0 and
  R-L2b are word-for-word the same obligations inside `C_ref`, and the recorded α=0 pathology
  arises under isotropic dilation *inside* the class.
- **Origin.** `STAGE8_T7_CREF_VS_D3_FACTUAL_DETERMINATION_V001.md:11-16`. Flag in 5 artifacts.

### O-4 · Corrected-status mechanism for the three over-claimed t_reports  `NARROWED 2026-07-26 — routing ruled, mechanism still open`
> **RULED, in part:** T01, T02 and T11 all route **BLOCKED**, not CONDITIONAL. Two lanes reached
> this independently. Adopted consequence: the honest battery outcome on current evidence is
> **`GATE5_CORE_BLOCKED`**. **Still open below:** which mechanism expresses a corrected status.
> The Rule-8 exception remains unspent and the append-only sub-decision is untouched.
- **Blocks.** Authoring the six missing t_reports — each authored onto the current contract
  "becomes another node whose status can never afterwards be corrected"; hence step 21.
- **Options with costs.** **Already sealed and sufficient** at
  `STAGE8_CORRECTED_STATUS_MECHANISM_OPTIONS_WITH_COSTS_V001.md:56-139`
  (`bb0a6c87d7a9133431bc77ade6696bab4f34f1c53f47e62b9ee5116d2a1d6529`). No restatement needed.
  **1** successor at the canonical path (no evaluator change; path stability lost). **2**
  supersession field ("it adds resolution to a script whose entire virtue is that it resolves
  nothing"; sits in the trust root). **3** authority list (a third manifest — "this program's
  manifest track record is poor: two manifests, two collateral breakages"). **4** no new
  mechanism (costs identical to 1; keeps the Rule-8 exception unspent).
- **Two gaps, which are an ADDENDUM not a rewrite.** (i) The memo twice declines to recommend,
  and **no recommendation of Option 4 exists anywhere in the corpus** — if the independent lane
  made one it arrived by relay and was never written down. (ii) The lettered binding constraints
  (a)–(e) the memo's decisive finding rests on are never defined in it or in the two artifacts
  it cites by hash.
- **Embedded sub-decision, separately the principal's.** Is replacing a file AT a canonical path,
  bytes and hash preserved elsewhere, "append-only"?
- **Must be visible before choosing.** Under constraint (b) no option can move T01/T02/T11 to
  CONDITIONAL: `honest_reachable_status_for_the_three = BLOCKED`;
  `battery_outcome_if_expressed_honestly = GATE5_CORE_BLOCKED`.

### O-5 · B4 — enumerate and fence every v001 invocation route that reaches the write  `OPEN — REOPENED THIS DATE`
- **Was about to be reported closed. It is not closed.** See
  `STAGE8_B3_B4_STATUS_AND_UNFENCED_V001_ROUTE_FINDING_V001.md`.
- **Blocks.** The production-gate NO-GO's clean closure. Not production itself, which is
  prohibited on both gates independently.
- **Origin.** `STAGE8_T7_PRODUCTION_GATE_NOGO_AND_PIPELINE_REPAIR_BINDING_V001.md:145-151`.
- **Independent confirmation, 2026-07-26.** The reviewer lane separately measured **both** canonical
  directories WRITABLE (`provenance` and `stage8_execution/work`) — reached by a different route than
  this lane's measurement, same conclusion. **The at-rest fence does not hold on this storage layer,
  and re-chmod is not a fix.** Carried as a **design matter for when production becomes live**, not
  as tonight's work; production is prohibited on two independent gates regardless.

### O-13 · Does Stage 8 emit kappa_record at all?  `OPEN — NEW 2026-07-27, two sealed authorities conflict`
- **Decision.** Master plan AMENDMENT_001 §D: Stage 8 ends by emitting `result.json` under schema
  `stage8-gate5-kappa-record-v002` with an exact-rational kappa_record enclosure excluding zero.
  The source-scalarization no-go: *"kappa_record is not emitted before that physical scalar
  closure exists"* — and that closure is in complete Q_spec, not Stage 8. **Both are sealed. They
  cannot both hold.** The no-go's own text says "battery verdict changes."
- **Blocks.** What Stage 8's completion *means*, and therefore step 21.
- **Origin.** `STAGE8_X_TO_KAPPA_RECORD_EXTRACTION_DETERMINATION_V001.md` §6 (`de8da188…`).
- **Note.** The recommended architecture amendment is authored
  (`STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001`) and, on a bounded
  search, **not marked accepted**.

### O-6 · Transport charter O-D4 — the source-independence unit  `OPEN — flagged, not accepted`
- Flagged in `STAGE8_TRANSPORT_FUNCTOR_CHARTER_V001.md` (`f58007a0f982343e9ed4`) as an obligation
  the lane declined to accept on its own authority.

### O-7 · Rule 6 recovery judgment for this lane's prediction family
- `rule6_recovery_judgment_holder = principal_on_reviewer_reading`. Not a blocker; it governs how
  future disagreements between the lanes are weighted.

### O-8 · Q2 (held) · O-9 · Q6 re-cast scheduling · O-10 · methods-record verbatim item
- `methods_record_verbatim_item_pending = true`. All three are small and none blocks.

### O-11 · Quarantine disposition for launchers v005/v006
- Open. Note the interaction with **O-5**: the v001 launcher at issue there is *not* quarantined
  and *not* sealed, so any quarantine policy must state whether it covers v001.

### O-12 · Charter or retire Stages 9/10/11 → **RULED THIS DATE. See Part 2.**

---

## PART 2 — RULED. Kept so they do not reappear as open.

| # | Decision | Ruling | Date |
|---|---|---|---|
| R-1 | U3 amendment into E1 v002's governing chain | **GRANTED.** Sealed `a861d452…` | 2026-07-26 |
| R-2 | Standing open-decisions artifact | **GRANTED.** This file | 2026-07-26 |
| R-3 | Stages 9/10/11 labels | **RETIRE.** Reversal condition checked and did not trigger — the prohibition has three label-free sealed carriers. **Count correction 2026-07-28:** source retirement artifact records `candidate_defeated_by = 3 label-free carriers`; prior `four` was a count error, not a substance change | 2026-07-26 |
| R-4 | A4(3) erratum | **SIGNED OFF.** Proceed | 2026-07-26 |
| R-5 | Extensivity contingency (would be a new principle) | **DEFERRED, unadopted** | 2026-07-26 |
| R-6 | D-1: does R-L2b gate A-L0 arm 2? | Neither gates the other; R-L2b is earliest-unmet-prerequisite, arm 2 is highest-risk-of-never-closing | AMENDMENT_001 §B |
| R-7 | D-2: is production on the critical path? | **No.** Steps 5–15 and 21 need none | AMENDMENT_001 §C |
| R-8 | D-3: Stage 8's ceiling | `GATE5_CORE_EXECUTED_SEAL_PENDING`; `BID_core_result_sealed` must be false | AMENDMENT_001 §D |
| R-9 | The kappa rule | **ADOPTED, binding.** Always `kappa_record` or `kappa_Thomson`, never bare | AMENDMENT_001 §E |
| R-10 | Transport charter | **Option 4** — disjoint causal-diamond decomposition, two conditions | `f58007a0…` |
| R-11 | D3 quantifier reading | **ALL common refinements.** Ratified | — |
| R-12 | Rule 7 ordering authority; Rule 8 pipeline feature freeze | **In force** | — |
| R-13 | Quarantine bridge-row conflict | **Ruled**; restoration record sealed | — |
| R-14 | E-Q1 — cell 4-volume under scoping clause 1 | **OPTION 3, GRANT SCOPED.** Witness `E1_CELL_4VOLUME_ADMITTED_ONLY_ON_PINNED_SKELETON`; verdicts say "on the pinned skeleton", never "over D3". F'-5 applied, not amended | 2026-07-26 |
| R-15 | Routing of the three over-claimed t_reports | **T01/T02/T11 → BLOCKED**, not CONDITIONAL. Honest battery outcome on current evidence is `GATE5_CORE_BLOCKED` | 2026-07-26 |
| R-16 | **Hessian-first supersession** — the same object as **route-list R1, the "Hessian-only re-posing"**: define the intensive Hessian directly as the volume-intensive limit of the second-order Duhamel/Dyson term, and require only that one term be volume-intensive and cellulation-independent. **INDEXED UNDER BOTH NAMES ON PURPOSE:** the ruling names the move, C.4 names the label, and that mismatch is what cost a full cycle | **NOT CHARTERED.** Would trade a provable-in-principle obligation for a weaker one on no evidence the original is unprovable, and would conceal the extensivity question, since nothing at second order tests all-orders extensivity. `hessian_first_supersession = NOT_CHARTERED`. **REVIVAL TRIGGER: available as FALLBACK ONLY IF R-L2b FAILS**, on the five terms F1–F5 recorded in advance "so they are not renegotiated later" — of which R1 as stated carries neither F2 (the V010-style zero-stiffness control) nor F5 (Theorem 3's open register). **TRIGGER UNFIRED:** `RL2b_closed = false`, `RL2b_refuted = false` (conditional only), `search_exhausted = FALSE`. **PROVENANCE, STATED: a TWO-LANE VERDICT OF RECORD — "both lanes agree" — and the artifact NEVER NAMES THE PRINCIPAL AS AUTHOR. This row does not assert a principal act.** Authority: `STAGE8_EXTENSIVITY_VERDICT_AND_RL2B_CAMPAIGN_OPENING_V001` **§3** — **§4 of that same artifact is already carried as R-5, and taking §4 without §3 is exactly why this row was missing.** The ruling reaches R1 by content and by the F1–F5 adoption chain, never by the label "R1"; reach established in erratum `f72ea760…` | 2026-07-26 |
| R-17 | **C-L3's outcome typing** — findable as **"C-L3 nonzero"** and as **"the sharp-kink log coefficient typing"** | **A CERTIFIED NONZERO COEFFICIENT IS NOT A FAILURE CONDITION. IT IS THE INDUCED COUPLING.** Retypes `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1149-1155`, where CERTIFIED NONZERO reads "UPGRADED to CERTIFIED DIVERGENT … TRIGGERS §Q2-STOP IMMEDIATELY". The sealed spec text is **NOT edited**. **PROVENANCE: THIS IS A PRINCIPAL ACT, stated by the principal in his own words, 2026-07-27 — unlike R-16, which is a two-lane verdict of record and says so.** Available to the principal because the prior typing was ADOPTED / spec-typed and **NOT DERIVED** (independent lane's Part A, A2), and under the verb calibration a premise is his to change. **MADE BLIND AND UNFITTABLE: C-L3 has never been evaluated (`IR_C_log_coefficient_evaluated = false`) and is NOT REACHABLE (`IR_C_record_phase_operator_collapse_certified = false`, C-L1; `IR_C_commutator_form_certified = false`, C-L2) — and BOTH readings predict the SAME FORM, an exact rational/algebraic multiple of 2/pi (A3), SO NO VALUE COULD EVER HAVE DISCRIMINATED THEM.** Ground (the principal's, **not** a sealed principle): gravity is the existence proof — Susskind–Uglum, Sakharov — and `K_bare_zero_adopted_as_compositeness_condition = true` with "no action term may be added because a coupling residual remains", so nothing is left for a counterterm to correct. **SCOPE:** does NOT make C-L3 reachable; does NOT touch R-L2b; does NOT identify the allow/require threshold (separate charter, **drafted and NOT ISSUED**; the Q2 scope limit is **in force and unamended**); does NOT authorize computing the coefficient, `kappa_record`, or alpha; adopts NO physical principle. Authority: `STAGE8_T7_CL3_NONZERO_TYPING_PRINCIPAL_DECISION_V001` `c7686d57…` | 2026-07-27 |
| R-18 | **The C-L3-nonzero bullet as a §Q2-STOP trigger** — findable as **"the Q2 tripwire disarm"** and as **`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:1354`** | **STRUCK.** *"We should disarm the tripwire. It is not valid given the theory. There will be non-zero."* **PROVENANCE: A PRINCIPAL ACT, in the principal's own words, 2026-07-27** (sealed 2026-07-28). **THE ACT IS AUTHORITY AND IS DISCLOSED AS AUTHORITY — IT IS NOT A READING OF THE SEALED TEXT.** A semantic ground (that under R-17 M(t) is the *source* rather than the *obstruction*) was tested in both directions and **FAILED**: "obstruction" is a definitional gloss for "a certified-divergent E1 against the sharp localizer" — E1 spec **v001:868-869** writes the clause with the "i.e." intact — and the act does **not** rest on it (`STAGE8_Q2STOP_DISARM_GROUND_VERIFICATION_STOP_V001` `b4b359e4…`). Reason of record, **not** a sealed physical principle: gravity as existence proof (Susskind–Uglum, Sakharov). **MADE BLIND: C-L3 unevaluated, unreachable behind C-L1/C-L2 (both false), and both readings predict the same form, so no value could have influenced it.** **SCOPE — ONE BULLET.** *** THE GENERAL CLAUSE REMAINS ARMED AND CAN STILL FIRE ON THIS ARM: deleting one entry from an open list of routes does not shrink the class it illustrates, so if a nonzero still yields a certified-divergent E1 — **which is O-A, and O-A is OPEN** — the general clause fires anyway and this act has no operative effect on this arm. *** Every other trigger stays armed; Q2 unresolved, options (i)/(ii)/(iii) open with (iii) still ordered first; the lane bar at `:1374-1377` and witness `Q2_ANSWERED_BY_A_LANE` stay live; Q2 scope limit unamended; C-L3 not reachable; IR-C's n=1 leg not closed; no computation of C-L3, `kappa_record` or alpha authorized. **Z.2:** the declaration's attachment to the *trigger* is removed for this arm; its attachment to the *arm's type* (§Z.2 header, "any certified-divergent arm") is **intact**, so `Z2_declaration_still_required` becomes **CONDITIONAL_ON_OA**. **A lane objection is on the record** (§8 of the authority). Authority: `STAGE8_Q2STOP_CL3_BULLET_DISARM_PRINCIPAL_DECISION_V001` `841c5e5f…` | 2026-07-27 |
| R-19 | **The §Q2-STOP divergence-stop** — findable as **"the Q2 tripwire"**, as **the general clause at `SPEC_V002:1349-1351`**, and as **standard `38e15177…:33-35`** | **STRUCK AT THE GENERAL CLAUSE.** *"We should disarm the tripwire. It is not valid given the theory. There will be non-zero."* / *"…this restriction doesn't fit the theory. We can[not] prove something if we are blocking our own testing."* *** THIS REACHES THE GENERAL CLAUSE AND THEREFORE THE WHOLE TRIGGER LIST — IT IS **NOT** ANOTHER EXAMPLE-DELETION. All four listed bullets are instances of one state, and that state is what is struck; **R-18 is SUBSUMED**, having been correctly executed at the narrower scope it was given. *** What is struck: the inference *M(t) diverges ⇒ M(t) is disqualified ⇒ halt*. **PROVENANCE: A PRINCIPAL ACT, 2026-07-28. THE ACT IS AUTHORITY AND IS DISCLOSED AS AUTHORITY — a textual ground was tested and FAILED (`b4b359e4…`) and is not reconstructed.** Reason of record, **not** a sealed principle: a divergence in an induced coupling with no counterterm available by construction **is** the coupling, and a rule halting on it forbids the measurement the theory requires (Susskind–Uglum, Sakharov). **MADE BLIND: C-L3 unevaluated, unreachable behind C-L1/C-L2, both readings predict the same form.** **NOT STRUCK:** *** Q2 REMAINS OPEN — options (i)/(ii)/(iii) all stand, (iii) still ordered first; the principal is NOT ruling the sharp localizer correct, only that a divergence is not evidence it is broken. *** *** ESCALATION IS NOT ABOLISHED, ONLY ITS AUTOMATIC TRIGGER — a defect found on any NON-DIVERGENCE ground still goes to the principal under §Q2-STOP's unchanged procedure. *** The lane bar at `:1374-1377` and witness `Q2_ANSWERED_BY_A_LANE` stay live; Q2 scope limit and §Z.2 unamended; option (i) not disarmed, only made discretionary; C-L3 not reachable; IR-C's n=1 leg not closed; no computation of C-L3, `kappa_record` or alpha authorized. **RESIDUAL ON THE RECORD:** §Q2-STOP now has **no armed automatic trigger**, and no non-divergence ground is specified anywhere — the detection burden has moved from the routes to the principal. **O-A: OPEN, consumers named** — this act removes consumer 1 (the stop); consumers 2 (Q2 option (i)), 3 (§Z.2 type-attachment) and 4 (the route-terminal witness) survive. Authority: `STAGE8_Q2STOP_DIVERGENCE_STOP_STRUCK_PRINCIPAL_DECISION_V001` `71439758…` | 2026-07-28 |
| R-20 | **Route 2 ratification** — findable as **"Route 2"**, as **the Stage-8 architecture route**, and as **the O-13 narrowing** | **RATIFIED.** *"ROUTE 2 IS RATIFIED, this date, by the principal, EXPLICITLY AND AS A NEW ACT."* **PROVENANCE: A PRINCIPAL ACT** — `ratified_by = principal`, `ratification_date = 2026-07-27`, `ratification_is_a_new_act = true`, `ratification_asserts_a_prior_approval_existed = false`. It **supplies** an approval the corpus lacked rather than restating one, on two and only two grounds, and the ruling falls if ground (a) is overturned. **WHY THIS ROW EXISTS (B1):** `STAGE8_MASTER_PLAN_AMENDMENT_002.md:72-73` states *"the register carries the ratification as its resolution"* — **and no such row existed.** That artifact is this lane's own seal and its own breach of the maintenance rule; **the row is written rather than the sealed clause corrected, so the clause becomes true.** Related and NOT carried by this row: the ratification's §5 (A5 restated and binding) and §7 (the evaluator successor expressly NOT AUTHORIZED) — both remain unindexed and are in the gap report. Authority: `STAGE8_ROUTE2_RATIFICATION_AND_FRAMING_CORRECTION_V001` `e0a55812…` | 2026-07-27 |
| R-21 | **The gamma-gate control-4 reversal — BOTH ENDS**, findable as **"control-4"**, **"gamma gate"**, and **"the decide-once reversal"** | **REFUSED, THEN CONDITIONALLY AUTHORIZED — SAME DATE.** *(i)* No control-4 v3 authorized; GATE_BLOCKED stands FINAL, **"APPEND_ONLY_PRINCIPAL_DECISION — DECIDE-ONCE, FINAL"**, `65d54d6c…`, flag at `:86` `gamma_gate_verdict_final = true`. *(ii)* **SUPERSEDED THE SAME DATE:** control-4 v3 **IS** authorized, conditionally, on three named conditions, superseding **item 1 only** — **"APPEND_ONLY_SUPERSEDING_PRINCIPAL_DECISION"**, `67bb5cff…`, `:102` `control4_v3_conditionally_authorized = true`, `:104` `gamma_gate_verdict_final = false (superseded: reopened under this authorization)`. **PROVENANCE: BOTH ARE PRINCIPAL ACTS.** *** READ THE SECOND OR NEITHER: `gamma_gate_verdict_final = true` STILL STANDS UNEDITED AT `:86` OF THE SUPERSEDED RECORD, AGAINST `= false` IN THE SUPERSEDING ONE. TWO LIVE SEALED FLAGS IN CONFLICT — append-only worked, the index did not. A reader who finds the first and not the second gets a REVERSED REFUSAL AS FINAL, which is exactly what one audit sweep did. *** Downstream and NOT ruled here: v3 was specced and executed to a null caused by the lane's own design defect, and **control-4 v4 is now an OPEN principal question** (`control4_v4_authorized = false`) with no Part 1 row. | 2026-07-26 |
| R-22 | **A32 holdout freeze** — findable as **"A32"**, **"holdout freeze"**, and **"external holdout registry/beacon/comparator/threshold freeze"** | **RATIFIED AND WRITTEN INTO V011.** Principal ratified four rulings one decision at a time on 2026-07-28: NIST CODATA 2022 fixed-vintage registry with lineage-only alpha exclusions and all-eligible family; drand mainnet primary beacon with NIST Randomness Beacon v2 fallback and fail-closed outage rule; published standard-theory same-alpha comparator class using `alpha(0) = 1/(4 pi kappa_Thomson)` with no refit, channel coefficient, or post-selection; and `D >= 5` distinctness threshold with covariance projection and fail-closed singular/empty cases. The thirteen mechanical items are ratified as written in `A32_FREEZE_DRAFT_V000_2026-07-28.md` (`13faf0bc9a455590bd99d1a40587d798bc558e87aa1d1bc6dcf6778731138123`). Authority: `/Users/bgm/MB Work/alpha_supervision/A32_FREEZE_V002_RATIFIED_2026-07-28.md` (`32dbfc33b4f07407903ec014627ea64de57b5b1a6dc017dd27c6504729c3a327`). **SCOPE:** V011 freeze fields written only; no `SPEC-SEAL`, `HOLDOUT-UNIVERSE-SEAL`, `PREDICTION-MAP-SEAL`, `ALPHA-RESULT-SEAL`, or ladder-grade flag claimed. The five drafting flags are not flipped here; ladder-grade flag computation remains blocked on the unimplemented evaluator (RD-22). `alpha_computed = false`; `proof_authorized = false`. | 2026-07-28 |
| R-23 | **A32 collection bootstrap index** — findable as **"A32 collection"**, **"a32_holdout"**, and **"NIST CODATA bootstrap"** | **INDEXED, NOT A LADDER SEAL.** Bootstrap directory: `/Users/bgm/MB Work/a32_holdout/`. Indexed hashes: `raw_allascii.txt` `77fb90e66c40db3e6eb16630bc9c88e4c7c8beddbe5e71be406f2f26e3f67e67`; `candidates.jsonl` `36ca855600ba64392085286b623cad3c0b5fcc53257ca27b35ccb85e5f10192c` (355 public value-free candidates; public structural check found only `canonical_id` and `record` keys); `commitments.jsonl` `66ac4250ded20e569a1b05a8658d42252c1098e250d73dfae21f52361197a752` (355 lines); `collector_v001.py` `645c5d2c67b1fc39588fbf237c645784abb18834cce014453e3ee87d4f8990e2`; `flags.jsonl` `e3e0af6c422b460c63768d748c1baa6d59e745011e497cea642892eddbb821ec` (2 `ALPHA_DATUM_NAME_MATCH`, flagged not dropped); `custodian_private/custodian.jsonl` `8488c1a1ad3b73eb3ae2a143af155645c02472c4902f9d57b0aeb99c4e441364` (**hash indexed only; contents not read by this lane**). Cites R-22 authority `A32_FREEZE_V002_RATIFIED_2026-07-28.md` (`32dbfc33b4f07407903ec014627ea64de57b5b1a6dc017dd27c6504729c3a327`). **SCOPE:** no `HOLDOUT-UNIVERSE-SEAL`, `PREDICTION-MAP-SEAL`, `ALPHA-RESULT-SEAL`, or ladder-grade flag claimed; no private custodian payload disclosed; `alpha_computed = false`; `proof_authorized = false`. | 2026-07-28 |
| R-24 | **C4 refuted-clause strike** — findable as **"C4 strike"**, **"ball-locus qualifier"**, **"sharp causal-ball projector promotion"**, **`efb08860`**, and **`0f76ab73`** | **CLAUSE-SCOPED STRIKE + RETAIN. PRINCIPAL ACT, 2026-07-29.** Struck from `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:346-352`: the ball-locus qualifier `"on the ball where M(t) = 1"` and the operator display/promotion claim `sum_lambda w_lambda u_lambda = m_0(I-P) + 1·P = P`, together with the same promotion claim in prose in C4's parent. **RETAINED AND STILL FROZEN:** C4 scalar clauses (`m_0 = m_1 = 0`; `m_{2j} = -2^{j-1}`; all odd moments zero; symmetric-second-difference completed per-cell Kraus form; annihilation of Dyson terms with fewer than two record insertions per CTP branch; vanishing bare a-linear tadpole; `lambda*tau_R in {0,+pi,-pi}` arithmetic; exact scalar saturation at full `tau_R`). **Ground:** struck text never had parent authority and first appears at `SPEC_V001:131-136`; witness `STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md` `efb08860b888e24acaa50fdafdbe4afdb868450f79ec23120c2bd3eb1d40ddbb`. **R1 registration:** `efb08860` (C-L1 refuted) and `0f76ab73` (T7(ii) obstruction) are registered here as lane findings required by the principal rider, **not** as new principal rulings; C1-C5 are now ratified by `/Users/bgm/MB Work/alpha_supervision/CONVENTIONS_C1_C5_RATIFIED_PRINCIPAL_DECISION_2026-07-29.md` (`4a679c26b94c60510724441cd57dbf5514f36ef74210e95e8ce9ac43fc934034`), so the flagged C1 dependency is DISCHARGED; R-24 remains a lane-finding registration, not a principal-ruling row. **R2:** Q2 option-(ii) cost block `SPEC_V002:1439-1447` restated in `STAGE8_C4_REFUTED_CLAUSE_STRIKE_REPAIR_BINDING_V001.md`; Q2 not decided or re-costed. **R3:** C-L4 / `kappa_bal` owner is Codex construction lane; rebuild `34c2123d...` supplies `kappa_bal = (3/8)/(3/8) = 1`, and `kappa_bal` is **NOT** `kappa_record`. **R4:** H-ANGLE as written is LAPSED; route class OPEN, citing `STAGE8_T7II_H_ANGLE_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md` `9f29088e...` and preserving its four reopen requirements. **R5:** PA-C1 at `SPEC_V002:2007` is a FALSIFIED PREDICTION OF RECORD; PA-B3's ground at `:1998` is half-withdrawn (C6 ground untouched, C4 promotion ground struck). **Lead flagged, not ruled:** `cos^2(8 pi rho^4)` radial profile is unassessed decay information and has not been ruled relevant to A-L0 arm 2. **SCOPE:** C1/C2/C6 untouched; C4 frozen status not revoked; C-L1 replacement identities not adopted as frozen inputs; O-1/F'-5 and C-L2 untouched; C-L3, `kappa_record`, and alpha not computed. Authority: `/Users/bgm/MB Work/alpha_supervision/C4_REFUTED_CLAUSE_STRIKE_PRINCIPAL_DECISION_2026-07-29.md` (`5c9b2819537fc3df99d9525426b10c4c2ce275fa967fa1d3364fc8355553d720`); repair binding `STAGE8_C4_REFUTED_CLAUSE_STRIKE_REPAIR_BINDING_V001.md`. | 2026-07-29 |
| R-25 | **Authority-chain precedence** — findable as **"authority precedence"**, **"cleanroom chain governs"**, and **"parent-tree evidence citation"** | **RECORDED. PRINCIPAL ACT, 2026-07-29.** Cleanroom chain governs all procedure; parent-tree material is admissible as evidence/input only by path and hash; conflicting parent ordering instructions are void, specifically alpha-before-Thomson and bare unsubscripted alpha_micro or unsubscripted k-symbol emissions; nothing parent-tree is retired; parent premises are not imported and must clear F'-1, F'-5, and R-9 before becoming load-bearing. Authority: `/Users/bgm/MB Work/alpha_supervision/AUTHORITY_CHAIN_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md` (`85bacbee7c9b6ef9f4e65e5eb898bd5273440d600fadd342c5556c2075f5dc8e`); cleanroom binding `STAGE8_AUTHORITY_CHAIN_PRECEDENCE_BINDING_V001.md`. **SCOPE:** no chain merge, no parent artifact correctness ruling, no C-L3, `kappa_record`, `kappa_Thomson`, or alpha computation. | 2026-07-29 |
| R-26 | **Construction conventions C1-C5 ratification** — findable as **"C1-C5"**, **"named obstruction sealable"**, and **"C3 stop-and-report guard"** | **RATIFIED AS WRITTEN. PRINCIPAL ACT, 2026-07-29.** C1 lane findings do not become Part 2 rows merely because they are findings; C2 named obstruction at file:line is a sealable result class; C3 writes a missing status row only when an existing authority supports it and otherwise stops and reports; C4 declined referral is provenance; C5 carrier-indexed numbers may be used refutationally but remain F'-5-inadmissible as bound constants. Authority: `/Users/bgm/MB Work/alpha_supervision/CONVENTIONS_C1_C5_RATIFIED_PRINCIPAL_DECISION_2026-07-29.md` (`4a679c26b94c60510724441cd57dbf5514f36ef74210e95e8ce9ac43fc934034`); cleanroom record `STAGE8_CONSTRUCTION_CONVENTIONS_C1_C5_RATIFICATION_RECORD_V001.md`. **Immediate effect:** R-24's C1 dependency discharged. | 2026-07-29 |
| R-27 | **Gravity evidence admission and five-strata route-class binding** — findable as **"gravity evidence"**, **"five strata"**, **"S1/S2 S3 S4 S5 ORPHAN"**, and **"x rho T_R"** | **ADMITTED AS EVIDENCE, ADOPTING NOTHING.** `GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md` (`18e337717878c4de0f44517670403e8c95399ff59c9735fbe019006fe318853a`) is now cited from the cleanroom chain as the path+hash surface for outside-the-cleanroom gravity material. Binding artifact `STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md` records S1/S2 BR induced coefficient functions (`f7caa5a...`, depth x unselected), S3 coupled record-bundle modulus gate (`52664ddd...`, five reopen conditions), S4 BID CTP Hamilton-Jacobi scale bridge (`b00683c...`, sqrt(2) ambiguity; derivation-only), S5 joint-handle character Hessian (`e10a92bd...`, CONDITIONAL; reduction ensemble open), and ORPHAN scale-critical fixed-point selector (`566a9c7e...` plus CSV `f6a94909...`) as one route class. **SCOPE:** merge nothing, rank nothing, x/rho/T_R are three independent scale obligations, no value computed. | 2026-07-29 |
| R-28 | **P2 public boson/odd/ghost Gaussian superdeterminant precondition result** — findable as **"P2"**, **"operator fingerprint v002"**, **"external prime superdeterminant"**, **"conformal contour"**, and **"external logdet tail"** | **PRECONDITION RESULT: BLOCKED, NOT EXECUTED.** Successor fingerprint `results/alpha_br_operator_artifact_fingerprint_v002.json` (`cad951f687dda61bcfe92eac92b3358fe373206ff99417b28f29518ad5a15f0f`) recomputes 58 tracked hashes: 50 same, 8 changed, 0 missing. Cleanroom result `STAGE8_P2_PUBLIC_SUPERDETERMINANT_PRECONDITION_RESULT_V001.md` records that v001 is stale, that existing census code is hardwired to the v001 fingerprint path, and that three hardwired deliverables are absent: external prime superdeterminant report, public conformal contour report, and external log-det tail report. **SCOPE:** no missing deliverable fabricated; no sign verdict from induced-only fixed-window spectra; no fitted depth potential; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-29 |

---

## PART 3 — LOOKS OPEN, PROBABLY IS NOT. Needs a confirming ruling, not fresh work.

```text
P-1  |C|_4 vs tau_R x |C|_3 insertion-domain binary. The transport charter's §2 item 3 fixes
     the weight to |C|_4, which appears dispositive, but no artifact says the plan's step-2
     binary is thereby settled, and the last explicit flag
     (insertion_domain_reading = UNRESOLVED_ON_SEALED_TEXT) PREDATES the charter.
     => almost certainly closed by the charter. WORTH ONE CONFIRMING LINE.
P-2  Step-1 transport-rule determination carries cross_check_returned = false and
     determination_is_final = false WITH A STATED REFUTATION CONDITION. So the charter that
     acted on it is provisional in the corpus's own terms. NOT a defect; a disclosure.
P-3  Master plan / completion plan ratification. plan_status = PROPOSAL_NOT_ADOPTED on the
     completion plan. A search for "ratif" found nothing; a ratification worded as "adopted"
     or "in force" elsewhere would have been missed. BOUNDED negative existential.
P-4  ~16 further items the sweep classified POSSIBLY_CLOSED. Not enumerated here on purpose:
     listing them as open would be the exact failure this register exists to prevent. They
     are recoverable from the sweep if ever needed.
```

---

## PART 4 — WHAT IS NOT A DECISION, AND SHOULD STOP BEING TREATED AS ONE

```text
"THE EXTRACTION-MAP WORK" AND "THE OVERNIGHT QUEUE" DO NOT EXIST IN THE CORPUS.
Searched: every spelling of extraction map / extraction-map / extraction_map, plus
"overnight queue", across the cleanroom, the supervision lane directory, the archive
mirror and the external-handoff trees. NEITHER FOUND.
The nearest real object is the AUTONOMOUS QUEUE (D0-D6), a seven-item queue run during the
autonomous window of 2026-07-25 -> 2026-07-26. It is FULLY EXECUTED AND DISPOSITIONED, not
outstanding.
STATUS: UNDETERMINED whether these name something issued by relay and never written to disk.
IF SO IT IS A RELAY GAP, and the construction lane does not hold the item. It will not
invent one. This row stays until the principal either supplies the item or withdraws it.
```

---

## Protected status

```text
register_is_citable = false
register_merges_with = nothing        (no prior STAGE8_LANE_STATUS.md found)
snapshot_date = 2026-07-26
prior_one_flag_finding = CORRECTED_WAS_AN_UNDERCOUNT
genuinely_open = 9     (O-1, O-3, O-4(mechanism only), O-5 .. O-11)
ruled = 23             (Part 2; R-23 added 2026-07-28 as a principal-directed
                        A32 collection bootstrap index; it is NOT a ladder seal and does not
                        disclose private custodian contents. R-22 added 2026-07-28 in the SAME ACT as writing the
                        ratified A32 freeze fields into V011; no SPEC-SEAL or ladder-grade flag
                        claimed. R-20 and R-21 added 2026-07-28 under the principal's B1/B3
                        authorization — R-20 closes the Route-2 ratification gap and thereby makes
                        AMENDMENT_002:72's sealed claim true; R-21 indexes BOTH ENDS of the
                        control-4 reversal, whose two sealed flags still conflict on their face.
                        *** THESE TWO CLOSE 2 OF ~50 KNOWN GAPS. THE SECTION-LEVEL SWEEP
                        (093f7179…) PUTS THE COUNT AT ~50 AND SAYS IT IS STILL A LOWER BOUND. ***
                        R-14 and R-15 added 2026-07-26; R-19 added 2026-07-28 in the SAME
                        ACT as the seal of its authority 71439758 — and R-19 SUBSUMES R-18, which
                        stays on the record as correctly executed at the narrower scope it was
                        given; R-18 added 2026-07-28 in the SAME
                        ACT as the seal of its authority 841c5e5f; R-17 added 2026-07-27 in the
                        SAME ACT as the seal of its authority c7686d57, per the maintenance rule
                        — the first row in this file written that way rather than retrofitted;
                        R-16 added 2026-07-27 —
                        an INDEX CORRECTION of a decision ruled 2026-07-26 and never indexed.
                        Authorized by the principal 2026-07-27 on the lane's recommendation.
                        THE MAINTENANCE RULE AT THE HEAD OF THIS FILE WAS VIOLATED IN THAT
                        SEAL: the extensivity verdict's §4 was captured as R-5 while §3, the
                        ruling itself, was not. A COMPLETENESS AUDIT OF THIS REGISTER IS IN
                        PROGRESS; until it returns, THIS FILE IS NOT AUTHORITATIVE ON WHAT
                        HAS BEEN RULED, and a lane finding no row for an object MUST NOT
                        infer the object is unruled — search the corpus by CONTENT, not by
                        label. No rows beyond R-16 are authorized.)
possibly_closed_not_listed_as_open = ~16   (Part 3)
most_consequential_open = O-1 (F'-5), *** RIPE 2026-07-28: hold condition SATISFIED, three
                          blind referrals returned, R-L2b uniformity REFUTED (52f2490b). NOT RULED. ***
F5_hold_premise = CHECKED_AND_FAILED — F'-5 IS LIVE, not moot (2026-07-27)
  the extraction is normalized, and the normalization is why X is the S2 operator, not why
  it cancels. R-L2b, the trilemma, U3 and Trotter-Kato are load-bearing, not beside the point.
superseded_hold_reason = O-1
  reason: if the extraction to kappa_record is a NORMALIZED RATIO, the divergence may cancel
  before it reaches the target, and F'-5 / R-L2b / the trilemma / U3 / Trotter-Kato would all
  be statements about a quantity that never reaches kappa_record. Not wrong — beside the point.
  Ruling F'-5 first would be ruling on a question that might not be live.
reopened_this_date = O-5 (B4)
fence_writable_confirmed_by_two_lanes = true   (design matter, deferred to production-live)
extraction_map_exists_in_corpus = false    (bounded search; UNDETERMINED off-disk)
production_authorized = false
alpha_computed = false
proof_authorized = false
```

---

## PART 2 ADDENDUM — 2026-07-29

| # | Decision | Ruling | Date |
|---|---|---|---|
| R-29 | **Preregistration stage-encoding precedence** — findable as **"stage_dependencies vs stage_dag"**, **"Q1"**, and **"preregistration encoding precedence"** | **PRINCIPAL ACT, APPLIED NOT AMENDED.** `stage_dependencies` is AUTHORITATIVE for graph structure: node set, edges, and fail-closed descendant computation. It is the stricter encoding and the evaluator-consumed encoding. `stage_dag` is DESCRIPTIVE, and **its non-seal preconditions REMAIN BINDING**: A-matrix rows passed, Gates 1-5 executed, composition-loop result, beacon rule, complete target-free Q_spec, unanimous report counts, and A33 reconstruction are not discarded by the precedence ruling. No bytes of `provenance/boundary_incidence_dynamics_preregistration_v011.json` are changed; immutability is intact. R-14 is the precedent: applied, not amended. Authority: `/Users/bgm/MB Work/alpha_supervision/PREREGISTRATION_ENCODING_PRECEDENCE_PRINCIPAL_DECISION_2026-07-29.md` (`70c4080eae018bd644a3f0694557f1c0e854d621aa61097c775737887fec528f`); cleanroom record `STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md`. **SCOPE:** no A-matrix row discharged, no SPEC-SEAL, no missing `--subjects` file supplied by this row, no computation authorized. `alpha_computed = false`; `proof_authorized = false`. | 2026-07-29 |

### A32 V001 Prepared-Template Citation

`A32_FREEZE_V001_PREPARED_2026-07-28.md`
(`13a3b8b28e3ccdceb7c3d19559985a1c4f4678e11b70e3deaf5e9b482ff32e08`) is
explicitly cited by the governing-chain record
`STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md`.
It is not elevated to a ladder authority. Its own status remains PREPARED IN
ANTICIPATION, immediately re-statused, NOT RATIFIED, and NOT SEALED; the ratified
A32 authority remains V002 as carried in R-22.

### Additional Authority-Currency Rows — Same Phase A Pass

| # | Decision | Ruling | Date |
|---|---|---|---|
| R-30 | **Primary route declaration** — findable as **"BR / EM-GR ratio route class"**, **"primary route"**, and **"Q2"** | **PRINCIPAL ACT, CONDITIONAL DECLARATION WITH FROZEN FALSIFIERS.** The BR / EM-GR ratio route class is the program's PRIMARY ROUTE effective 2026-07-29, located at Q_spec slot 2, full gravitational action and gravitational quantum measure. It focuses lane effort and makes the route citable as the target of record. Falsifiers F1 and F2 are frozen in the authority and cause automatic lapse if fired: F1 concerns the complete coupled-Hessian P2 execution failing to find a finite isolated stationary point with isolated positive branch, or retaining a continuous family through the capacity condition; F2 concerns Q_spec slot 9, finite c F^2 deformation exclusion, being underivable on this route except by adopted postulate. **SCOPE:** adopts no physical premise, coefficient, or value; does not discharge slot 1, slot 6, or slot 9; does not make slot 2 newly required; does not deprioritize Phase A; authorizes no computation of alpha, `kappa_record`, `kappa_Thomson`, x, rho, or T_R. Authority: `/Users/bgm/MB Work/alpha_supervision/PRIMARY_ROUTE_DECLARATION_PRINCIPAL_DECISION_2026-07-29.md` (`d481ada8b7c4c80b6d095be2a1e5cbf43ebb477d37589b8152959a53e09fcf59`); cleanroom citation record `STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md`. | 2026-07-29 |
| R-31 | **Fourth horn / finite Hilbert-Schmidt ceiling re-posing** — findable as **"fourth horn"**, **"R-L2b superseded / re-posed"**, and **"Q3"** | **PRINCIPAL ACT.** A finite Hilbert-Schmidt ceiling was not the right obligation. R-L2b as written is SUPERSEDED / RE-POSED, NOT SOLVED and NOT MERELY REFUTED. The H1 refutation remains a fact about the obligation as written; what changes is that the written obligation is no longer the target obligation. **SCOPE:** supplies no replacement; does not declare connected extensivity true or false; does not rule O-1 / F'-5; does not charter Hessian-first supersession or the running-`kappa_record` contingency; does not authorize computing C-L3, `kappa_record`, `kappa_Thomson`, or alpha; adopts no physical principle. Frozen falsifier: if a route is later found where the induced coupling's divergence is absorbable because a counterterm is available by construction after all, the ruling's ground fails and must be reopened. Authority: `/Users/bgm/MB Work/alpha_supervision/FOURTH_HORN_PRINCIPAL_DECISION_2026-07-29.md` (`7d5d56cff0932fa04d96be4f75515bee0ad29095e70e4d64b8c017e34f5a6d72`); cleanroom citation record `STAGE8_PREREGISTRATION_ENCODING_PRECEDENCE_AND_A32_PREPARED_TEMPLATE_AUTHORITY_RECORD_V001.md`. | 2026-07-29 |
| R-32 | **Phase A A7 census fingerprint path repair** — findable as **"A7"**, **"fingerprint v002 path"**, and **"external census hardwire"** | **PROCESS REPAIR RECORDED.** Local script `scripts/audit_alpha_br_external_irreducible_mode_census_v001.py` now accepts `--fingerprint-json`, defaults to the v002 successor when present, and validates both the original PASS payload and the successor recomputation payload without rerunning the census. Cleanroom record: `STAGE8_PHASE_A_A7_CENSUS_FINGERPRINT_PATH_REPAIR_RECORD_V001.md`; patched local script SHA-256 `251dc6eb1600dcd4dfb655d2e17e6036433edbb654859a225b130da0c529a5cb`. **SCOPE:** no P2 execution, no missing deliverable fabricated, no C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-29 |
| R-33 | **Corpus-check cannot-fail detector** — findable as **"cannot_fail_checks"**, **"tautological require"**, and **"A8"** | **PROCESS CHECK ADDED AS YELLOW BASELINE CLASS.** `corpus_check.py` now reports require/check patterns that may be tautological under their own construction. The first run reports two baseline findings: `workspace/scripts/audit_bid_absolute_record_scale_identifiability_v001.py` and `cleanroom_output/20_ratio_assembly_v001.py`. **SCOPE:** reports only; repairs nothing; does not rule, adopt, retire, seal, or compute physical values. | 2026-07-29 |
| R-34 | **Q_spec eighteen-slot status map** — findable as **"18 Q_spec slots"**, **"slot-to-status map"**, and **"A9"** | **STATUS MAP AUTHORED.** `STAGE8_QSPEC_SLOT_STATUS_MAP_V001.md` maps the eighteen slots from `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md:119-139` to current open, blocked, missing-spec, branch-dependent, or principal-level status. It records zero closed slots and preserves the correspondences slot 1/O2, slot 6/O3, and slot 9/O1. **SCOPE:** status ledger only; no `Q_spec` slot is discharged; no route selected; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-29 |
| R-35 | **Q_spec deep slot inventory** — findable as **"Task 11"**, **"deep slot inventory"**, and **"slots 3-8 parent material"** | **INVENTORY AUTHORED.** `STAGE8_QSPEC_SLOT_DEEP_INVENTORY_V001.md` extends A9 with parent-tree evidence, missing inputs, and next-act typing for all eighteen `Q_spec` slots, and records Task 19-24 groundwork for slots 3-8 as starting-point versus different-object material. Hash `336a752413c16283fe6c8728da703ee99c9aaf7b532bd17e1979e2937370b01a`. **SCOPE:** parent-tree material is evidence only; no slot is discharged; no external premise is imported; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-29 |
| R-36 | **Task 14 external-census deliverable obstruction** — findable as **"Task 14"**, **"external prime superdeterminant reports"**, and **"census deliverables blocked"** | **OBSTRUCTION RECORDED.** `STAGE8_TASK14_CENSUS_DELIVERABLE_REPORT_OBSTRUCTION_V001.md` records that the three census deliverable reports named by `scripts/audit_alpha_br_external_irreducible_mode_census_v001.py` cannot honestly be produced yet: the external prime superdeterminant report, public conformal contour report, and external logdet tail/subtraction report are each blocked by named missing inputs. Hash `a2d67ad5de79e2bf001d8cd1771ad599dbfb79991aed33ca25c230c2e51b87bc`. **SCOPE:** no report is fabricated, no gate marker is emitted, no route lapses, no project script is run, and no C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-29 |
| R-37 | **Action-form underdetermination inventory** — findable as **"S0/S1 Pauli pair"**, **"action-form underdetermination"**, and **"Paste 126 W1"** | **INVENTORY AUTHORED.** `STAGE8_ACTION_FORM_UNDERDETERMINATION_INVENTORY_V001.md` records that the exhibited parameter-free parent-action completions are exactly the displayed `S_0` and `S_1` pair under the scoped sweep; additional higher-derivative and finite-causal-update classes are named but not enumerated as concrete members. The two-completion claim is carried by displayed action/prose algebra and authority flags, not by an executable finite-response producer. Hash `cafad33ed99b04b5c95fb1e2c82750f25e567aba2c3c6c08dc7aa3be61c2b022`. **SCOPE:** no finite response is evaluated; no action-form mutation is adopted or excluded; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, c_R, x, rho, or T_R computation. | 2026-07-29 |
| R-38 | **Namespace register draft v002 / C_R collision** — findable as **"C_R compactness ratio"**, **"C_R induced Einstein coefficient"**, and **"C_R connected-kernel moment"** | **DRAFT SUCCESSOR AUTHORED.** `STAGE8_NAMESPACE_REGISTER_DRAFT_V002.md` preserves V001 and adds the demonstrated `C_R` collision: cleanroom compactness ratio, parent BR induced Einstein coefficient, and Q_spec connected-kernel second moment. It also records `T_R`/`k_R`, `K_bare`/`K_R`, and `X` as near-misses not promoted to global rows. Hash `c36c61151fb2fe0bf2c3cf02418f7b5b8eea5b772dbc104765885891d123de67`. **SCOPE:** draft only; no namespace rule is adopted; no artifact is renamed; no register row is amended by this draft; no physical value is computed. | 2026-07-29 |
| R-39 | **Schur ratio-protection scope attack** — findable as **"Schur ratio protection"**, **"su(5) invariant deformation class"**, and **"Paste 126 W3"** | **CONDITIONALITY RECORDED.** `STAGE8_SCHUR_RATIO_PROTECTION_SCOPE_ATTACK_V001.md` records that Schur protection survives inside a full `su(5)`-invariant symmetric-tensor deformation class, but the corpus does not establish that every admissible response-changing deformation or generated effective descendant lies in that class or survives transport below the breaking scale without independent per-factor threshold/local corrections. Hash `a84e7c9d67a1fdd5b266251b1875bdb4bd71c2d06f27d5b393491f3b8db4a2e9`. **SCOPE:** Schur arithmetic is not recomputed; no counterterm is chosen; no finite response or coupling is evaluated. | 2026-07-29 |
| R-40 | **GR-EM parameter-free relation refutation indexed** — findable as **"T_R ~ 1/k_R refuted"**, **"adoption by dimensional analogy foreclosed"**, and **"BOHM_GR_EM_RELATION_REFUTED"** | **REFUTATION RECORDED.** `STAGE8_GR_EM_RELATION_REFUTATION_REGISTER_RECORD_V001.md` indexes `/Users/bgm/MB Work/alpha_supervision/BOHM_GR_EM_RELATION_REFUTED_2026-07-29.md` (`dd4563d4630349bd4da4cc583ae6762c25fdaa5d669a648e374e94be2133c681`): the reviewer GR-EM parameter-free relation is refuted at the `T_R ~ 1/k_R` bridge; `T_R` and `k_R` are disjoint objects with no derived bridge; adoption by dimensional analogy is foreclosed. Hash `65fa66475dd8eca9e7a96452c481a2515fd39caecbdf7abb2a6086ff4fc3f98c`. **SCOPE:** status only; no derivation is performed and no C-L3, `kappa_record`, `kappa_Thomson`, alpha, c_R, x, rho, or T_R computation. | 2026-07-29 |
| R-41 | **Trace collapse and gravity/gauge impossibility registered** — findable as **"trace collapse theorem"**, **"second-moment condition"**, and **"depth selection unavoidable"** | **REGISTERED FROM SUPERVISION INTO THE GOVERNING CHAIN.** `STAGE8_TRACE_COLLAPSE_AND_GRAVITY_GAUGE_IMPOSSIBILITY_REGISTER_RECORD_V001.md` records `/Users/bgm/MB Work/alpha_supervision/RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md` (`a7b82f9a180945844b95dc3931a649591e7c7ad7449e26f035ce7f270cb50d5e`): `Tr_{Lambda^k}(XY)=C(N-2,k-1)Tr_fund(XY)` when at least one generator is traceless, with the central trace term in the general case; no x-independent gravity-to-gauge ratio exists on the `Lambda^even(C^5)` carrier because gauge and gravitational sectors are weighted by index and dimension, and the contradiction localizes on `Lambda^0`; depth selection is unavoidable on this carrier; the honest gauge-collapse criterion is the second-moment condition, not merely Casimir class-functionhood; the `|H|` block decomposition in the parent operator is a live inadmissible counterexample unless protected by the unitary `MASS_CHEVALLEY` uniform shift. **SCOPE:** registration only; ratio route not killed; no depth, coupling, C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-30 |
| R-42 | **Gauge-ratio retype and cannot-fail producer seeds** — findable as **"K_H/K_Q retyped"**, **"K_QH/K_Q retyped"**, and **"cannot_fail_checks parent seeds"** | **ERRATUM RECORD.** `STAGE8_RATIO_RETYPE_AND_CANNOT_FAIL_CONSUMER_ERRATUM_V001.md` records that `K_H/K_Q=3/2` and `K_QH/K_Q=1` are exact Cartan inner-product / trace-orthogonality facts, not dynamical evidence; parent producer gates in `derive_alpha_br_common_induced_coefficients_v001.py:242-244,263-272` are cannot-fail identity predicates over the same inventory; four supervision consumers still carry the old "executed dynamical evidence" reading; and `corpus_check.py` was extended so `cannot_fail_checks` scans bounded parent recovery scripts and fires on the two parent seed cases. **SCOPE:** ratios unchanged; sealed supervision consumers not edited; detector reports only; no finite response, coupling, C-L3, `kappa_record`, `kappa_Thomson`, alpha, x, rho, or T_R computation. | 2026-07-30 |
| R-43 | **G3 release defect, slot-18 ordering correction, and modulus ruling registered** — findable as **"G3 no release condition"**, **"slot 18 parallel"**, and **"modulus radius not cell radius"** | **PROCESS DEFECTS AND MODULUS RULING RECORDED.** `STAGE8_G3_SLOT18_MODULUS_PROCESS_DEFECTS_REGISTER_RECORD_V001.md` records that the old G3 comparison fence points to Stage 12 even though cleanroom records say Stage 12 never existed; the old G3 carriers are not cited by the governing cleanroom chain under the stated bounded search, and T15 v002 replaced the dangling G1-G5 reference with concrete anti-numerology rules; `STAGE6_PARENT_ACTION_AND_QSPEC_LEDGER_V002.md` does not seal "slot 18 last" and its JSON orders only the nine EM steps, so the unused structure-sensitive prediction can be worked in parallel; and `/Users/bgm/MB Work/alpha_supervision/RESULT_MODULUS_RADIUS_VS_RECORD_CELL_AND_THE_UNATTEMPTED_BRIDGE_2026-07-29.md` (`83b56b38ea5b7ad5b75043d2835a9ff24343f2ab26a51bd65ee87cfc082160f6`) records that the modulus `R` is not BID's cell radius `R_R`, S3 is memo-only, and cleanroom `C_R` is an adopted compactness rule, not a projected curvature term. **SCOPE:** no fence weakened; no stage-label repair made; no modulus candidate evaluated; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, c_R, x, rho, or T_R computation. | 2026-07-30 |
| R-44 | **Namespace register draft v003 / K_H collision** — findable as **"K_H stiffness"**, **"K_H Hermitised Dirac"**, and **"namespace v003"** | **DRAFT SUCCESSOR AUTHORED.** `STAGE8_NAMESPACE_REGISTER_DRAFT_V003.md` preserves V001/V002 and adds the demonstrated `K_H` collision: parent BR / parent-flux induced Maxwell stiffness for cocharacter `H` versus cleanroom Hermitised Dirac operator `K_H = gamma^0 D_SR = p_0 - H_SR` at `PRIMITIVE_SOURCE_RECORD_CHIRAL_OPERATOR_GATE_V002.md:39-42`. **SCOPE:** draft only; no namespace rule adopted; no artifact renamed; no register row amended by this draft; no physical value computed. | 2026-07-30 |
| R-45 | **Cross-sector metric-rule admissibility spec** — findable as **"cross-sector metric rule"**, **"beta overdetermination"**, and **"internal/projective to external/Lorentzian conversion"** | **PRE-CANDIDATE SPECIFICATION AUTHORED.** `STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md` discloses prior art first: the gap is already named in `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V001/V002`, the Fable handoff `45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001`, and the supervision modulus result, while parent `gravity_electromagnetism_surface_unification_v026.md` carries only downstream endpoint projection. The spec defines the target as a same-cell map from internal/projective record geometry to external/Lorentzian length normalization, equivalently a determination of `beta`; it requires two independent target-blind requirements with exactly one common positive `beta`; it lists F'-1, F'-5, A02, T15/R-9, scale-collapse, and dimensional-analogy fences; it freezes falsifiers; and it requires escape tests against prior modulus/radius no-gos. **SCOPE:** specification only; no candidate evaluated; no derivation attempted; no C-L3, `kappa_record`, `kappa_Thomson`, alpha, c_R, K, x, rho, T_R, root, eigenvalue, radius, scale, or coupling computation. | 2026-07-30 |
