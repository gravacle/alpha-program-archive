# STAGE 8 / TASK 6 / STEP 2 — THE EVALUATION DoR: THE SCOPE DECLARATION (DRAFT)

Lane: Dario (Claude Opus 5), drafting lane
Task: PASTE 604 / Task 6, Step 2
Authority to draft: DoR-020-A8 + the ratified A32 instrument. **THIS ARTIFACT IS A DRAFT.
IT ADOPTS NOTHING, RULES NOTHING, LIFTS NO GATE, AND COMPUTES NOTHING.**
Custody: I draft; Codex 3 reviews; the principal rules — and **not before the
`(M5a-V002)` subgate supplies what this declaration requires of it.**

## Lead — the declaration's type, stated first

```text
THE PRODUCT OF THIS DECLARATION IS TYPED, BEFORE ANY VALUE EXISTS:

  COMPUTATION_SCOPE = LOCAL
  PRODUCT_TYPE      = LOCAL-SHADOW
  TRIAL             = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE
  PERIOD_NATIVE     = false
  A7_BRANCH         = carried per branch; see (V1-6)
  ARITHMETIC        = EXACT RATIONAL OR EXACT SYMBOLIC ONLY

IT IS NOT alpha, NOT kappa_Thomson, NOT K_*, NOT a global period, NOT a
holonomy charge, NOT a period-native Maxwell quantity, and NOT a two-sided
trial.                                                             (DOR-0)

DECLARATION = DRAFTED
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
```

[PROVABLE] The type block is the ratified instrument's `SUBJECT` block carried
verbatim; the anti-rename clause is its own. This declaration **may not promote
it**, and the ratified text is explicit that `LOCAL-SHADOW` *"is not promoted by
passing through A32."*

## 0. Preflight, standing, and what this draft may not do

| Check | Result |
|---|---|
| Register head Q-537 | verified |
| A32 instrument RATIFIED — `DECISION_A32_INSTRUMENT_RATIFIED_2026-08-06.md` = `67100877ffea4124b50d1ea220df4f00c499089b59064e6ca2ac6b37f5a0305d` | verified and read |
| Ratified gate text (prep V002) = `c5d1090b1ec1862c59c1281845c9ad74d0b143e9a57f195c099adb16e56ae4ea` | verified |
| Chain V004 = `1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a` | verified |
| DoR-020-A2 adopted (Arm A) = `5c945cae9ae8afa60080ee08d569324d350d6717bf2a3058460bc00451b86f8e` | verified and read |
| Witness certification §II/§III | read |
| Output name collision | none — clear to write |

[PROVABLE] **The ratification's own limit on this document.** The decision states
that the evaluation DoR *"may DRAFT in parallel against the ratified gate text but
may not be ruled before the subgate's own gate conditions are met where it
requires them,"* and that `(M5a-V002)` *"is the tracked work before Step 2 of the
evaluation or ANY numerical execution; its STATUS COLUMN is the first tracked
item."* This draft is written to be ruled later, not now.

**Tag legend.** `[PROVABLE]` = carried from a sealed source at its sealed verb.
`[PART-PROVABLE]` = holds on a named subscope. `[YOURS]` = drafted here, not law.
`[TYPE-U]` = a lawful object with no member produced; emptiness not proved.

---

## V1. WHAT IS COMPUTED, EXACTLY

### (V1-1) The subject and its domain — [PROVABLE from chain V004]

The subject is the certified **LOCAL chain**, steps 8–11, on the certified
complete domain:

```text
(D_w, d_w) complete;  D_w subset K_amb;  D_w closed in complete K_amb;
B_w := ell_w o Pi_w o Schur o S_w ;   B_w : D_w -> D_w.        (V1-1a)
```

[PROVABLE] Two independent obligations are **not** discharged by ambient
completeness and must be carried as named gates, per the chain's own text:
`D_w` nonemptiness is *"carried only by explicit `C_ret` clause"*, and
*"Completeness of the ambient scalar carrier does not imply completeness of
`D_w`; `domain_complete_cert_w` is an independent item."*

### (V1-2) Step 8–9: the modulus — [PROVABLE from chain V004]

```text
RetExtract[dot Schur] = a_loop Rhat_K                            (step 8)
A_loop := sup_(D_w) |a_loop|
q_loop  = sup_(D_w) |dot B_w| = |chi_K| A_loop   under C_RET_SCOPE_w   (step 9)
```

[PROVABLE] **`MODULUS_COMPATIBILITY_CERT[w]` sits at the Step 8/9 seam and is a
separate falsifiable gate**, discharged by exactly one of two witnesses:
`DIFF_TO_METRIC` (a certified chart equivalence plus exact chain-rule transport
of the Step-8 bound to `d_w`) or `DIRECT_MODULUS` (`A_loop` defined by
`d_w`-difference quotients directly, the Step-8 derivative used only as a
consistency witness). The failure mode it blocks is named in the source: a
complete `d_w` lacking both witnesses can make `sup|dot B_w|` disagree with the
true `d_w` modulus — the alternate-complete-metric attack.

[YOURS] **This declaration requires the witness to be named and sealed before
`A_loop` is evaluated, not after.** A modulus computed first and reconciled
afterwards is the attack, not a check against it.

### (V1-3) Step 10: the case-lattice cell determination — [PROVABLE]

The licensed lattice, carried verbatim:

| Cell | `A_loop` | `chi_K` | Consequence |
|---|---|---|---|
| 1 | `0` | `0` | `q_loop = 0`, strict contraction |
| 2 | `0` | `≠ 0` | `q_loop = 0`, strict contraction |
| 3 | `0 < A_loop < ∞` | `0` | `q_loop = 0`, strict contraction |
| 4 | `0 < A_loop < ∞` | `≠ 0` | strict **iff** `|chi_K| < A_loop^{-1}` |
| 5 | `∞` | `0` | `q_loop = 0`, strict contraction (pointwise finite branch) |
| 6 | `∞` | `≠ 0` | **excluded**; `q_loop = ∞`; not contractive |

[YOURS — INHERITED DISCREPANCY, FLAGGED NOT HARMONIZED] The chain's `P1` prose
says *"All eight lattice cells"* while the display carries **six**. Six is the
product of the three `A_loop` regimes and the two `chi_K` regimes; a count of
eight is reachable only by splitting cell 4 and one other. **I do not silently
reconcile this.** The declaration requires the cell count to be fixed of record
before Step 10 executes, because the cell determination is the object the
disposition plan at V4 keys on.

### (V1-4) Step 11: the Banach consequence — [PROVABLE]

Conditional existence/uniqueness of the fixed point, *"under Step 10 for the same
`w` and the same complete `D_w`."* [YOURS] The declaration carries the sameness
conditions as **operative**: a fixed point obtained on a different `w`, a
different domain, or a domain whose completeness certificate is not the one used
at Step 9 is not this chain's fixed point and may not be reported as it.

### (V1-5) The one-sided-trial rider, attached to `chi_K`'s reading — [PROVABLE]

```text
seed nonzero  -> chi_K finite; the computation remains INSIDE the licensed
                 lattice; a confirming outcome MAY CONFIRM.
seed zero     -> chi_K is a POLE / OUT-OF-LATTICE condition.
                 IT IS NOT A NEGATIVE VERDICT.                    (V1-5a)
```

[PROVABLE] This is the ratified rider verbatim, and its mechanism is of record:
`chi_K^Mx` carries `q_T,RL` in a denominator, and **the licensed case lattice has
no infinite-`chi_K` cell** — so a vanishing seed exits the licensed lattice rather
than refuting anything. The cure is carried `CARRIED-CONDITIONAL` and requires a
formed period route and the true `d^per` modulus certificate.

[YOURS] Therefore the declaration pre-commits: **on seed zero the payload records
`OUT_OF_LATTICE` or noncomputable, and no value is invented** — the ratified
instrument's own words.

### (V1-6) A7 branch carriage on the local route — [PART-PROVABLE / TYPE-U]

[PART-PROVABLE] A7 requires **both** `E_C` branches (`ZERO`: `E_C,RL c_RL = 0`;
`IDENTITY`: `E_C,RL c_RL = c_RL`) carried, neither selected, averaged, merged, nor
dropped. The ratified instrument requires them *"computed and reported per
branch"* if later computed.

[TYPE-U] **Whether contact enters the local route at all is not established by the
sealed local chain.** `B_w = ell_w ∘ Pi_w ∘ Schur ∘ S_w` exhibits no `E_C` factor;
`E_C` is a cochain-stage operator on the H route. Two dispositions, and the
declaration must take exactly one **before** execution:

```text
(a) contact DOES enter the local route at a named seam
      -> both branches computed and reported per branch; no aggregate verdict.

(b) contact does NOT enter the local route
      -> A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE, and the field is
         DISPLAYED WITH THAT VALUE, never omitted.                (V1-6a)
```

[YOURS] **Displaying the vacuity is mandatory; omitting the field is not the same
act.** A payload silently lacking the branch index cannot be distinguished later
from a payload whose branch was dropped, which is exactly the A7 failure mode.
The ratified instrument's rule governs the residual case: *"If the prediction-map
schema cannot carry both branches, that is an unresolved gate, not permission to
choose one."*

### (V1-7) `nu` symbolic throughout — [YOURS, binding on the declaration]

`nu` is carried as a **symbol** at every step of this declaration. No numeric
`nu` is substituted, defaulted, fitted, or set to a convenient value at any point
of steps 8–11 or the assembly. Any step that cannot proceed with symbolic `nu`
is a **stop**, reported as such, not a licence to instantiate one.

### (V1-8) The sensitivity ladder's place — [PROVABLE / YOURS]

[PROVABLE] Chain step 12 is *"Sensitivity-system and witness-to-number ladder
preparation: set up parameter-difference systems and record the consumer chain."*

[YOURS] Its place in this declaration is **after** the Step-11 conditional result
and **per A7 branch**, and it is theory-side only. It supplies theory sensitivity;
it does **not** repair the preselection measurement-metadata bridge — the sealed
record is explicit that *"`(M5)` is not repaired by sensitivity alone"* and that
Task-6 sensitivity *"cannot by itself supply the missing preselection
measurement-metadata bridge."*

### (V1-9) The rationality check's place — [PROVABLE]

All finite-`L` objects are computed in **exact rational or exact symbolic
arithmetic**, with the implementation **named and hashed**, and any enclosure
reported as exact rational strings (`lower`, `upper`). [YOURS] Its place is a
**precondition on every numeric step**, not a post-hoc audit: a float-path result
is not a defective value of this declaration, it is **not a value of this
declaration at all**.

### (V1-10) The assembly, symbolic-first — [PROVABLE / YOURS]

[PROVABLE] The ratified stiffness ruling: `K_*` — the onset root of the one-cell
closure condition, `C_record(K_*) = 0` with `dC_record/dK ≠ 0` at `K_*` and
`K_* > 0` — **is alpha's stiffness**, and `alpha_micro = 1/(4 π K_*)`.

[YOURS] The declaration's assembly discipline:

```text
1. Derive the assembly SYMBOLICALLY first: alpha_micro = 1/(4 pi K_*),
   with K_* the named onset root, nu symbolic, arithmetic exact.
2. The symbolic form is the deliverable of this declaration.
3. NO numeric alpha is produced by this declaration under any outcome.
4. Any numeric evaluation is a SEPARATE licensed act behind (G6), and it
   remains subject to every type in (DOR-0).                     (V1-10a)
```

[YOURS] **`alpha_micro` computed from a `LOCAL-SHADOW` input is a
`LOCAL-SHADOW`-typed expression, not physical alpha.** The type propagates
through the assembly; `1/(4π·)` is not a promotion operator.

---

## V2. THE ORDER OF OPERATIONS AND THE GATE MAP

### (V2-1) The authoritative ancestry — [PROVABLE]

The ruled 11-node graph governs; `stage_dependencies` is authoritative for node
set, edges, and fail-closed descendants; certification is **transitive**:
`Certified(node)` requires the node's token, its preserved non-seal conjuncts,
**and `Certified(p)` for every ruled parent `p`**. The ruling's binding phrase
travels: *"This act cannot loosen any gate."*

### (V2-2) The gate map — [YOURS, drafted; each binding cited]

| # | Operation | May not begin until | Certification point |
|---|---|---|---|
| 0 | **This declaration is ruled** | `(M5a-V002)` supplies the conjuncts this DoR requires of it | principal's Step-2 act |
| 1 | Any **numerical** execution whatsoever | `A32_PRE_EVALUATION_READY = true`, i.e. the full rail `SPEC-SEAL → {HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL} → PREDICTION-MAP-SEAL` with every non-seal conjunct at each node | evaluator-certified per `(G3)` |
| 2 | Step 8 (`a_loop` extraction) | gate 1; plus `C_RET_SCOPE_w` and differentiability on that branch | evaluator |
| 3 | Step 9 (`A_loop`, `q_loop`) | gate 2; **plus `MODULUS_COMPATIBILITY_CERT[w]` witness named and sealed** | evaluator |
| 4 | Step 10 (lattice cell) | gate 3; plus the cell count fixed of record per (V1-3) | evaluator |
| 5 | Step 11 (Banach consequence) | gate 4; plus `domain_complete_cert_w` and `D_w` nonemptiness by explicit `C_ret` clause | evaluator |
| 6 | Step 12 (sensitivity, per branch) | gate 5 | evaluator |
| 7 | Symbolic assembly `1/(4π·K_*)` | gate 6; `K_*` established as the onset root, `nu` still symbolic | evaluator |
| 8 | **Any numeric alpha value** | `ALPHA-RESULT-SEAL`, which by `(G6)` requires `THOMSON-RESULT-SEAL` **and** `PARENT-COMPARISON` **and** `HOLDOUT-UNIVERSE-SEAL` **and** `PREDICTION-MAP-SEAL`, each transitively certified | evaluator + a separate licensed act |
| 9 | **Any comparison to a measured value** | after the governed result seals; beacon, unmask and contamination only at their ruled positions | Step 9 of the escrow order |

[PROVABLE] Gate 8's parent list is the authoritative graph's, verified against
`stage_dependencies` directly. Gate 1's rail is exactly the ancestor set of
`PREDICTION-MAP-SEAL` — neither short nor padded.

[PROVABLE] **Step 8 of the board seals the assembled number; it does not
retroactively create the prerequisite prediction-map seal.** A map sealed after a
value exists is not a prediction map.

### (V2-3) Where `(M5a-V002)`'s conjuncts gate which step — [YOURS]

```text
instrument_ratified                                   -> gate 0   (SATISFIED)
schema_and_canonical_ID_tensions_resolved             -> gate 1
executable_eligibility_and_comparator_interfaces_frozen -> gate 1, and gate 9
Q25_current_scalar_commitment_disposition_carried     -> gates 1 and 9 (headline)
SPEC-SEAL + its non-seal conjuncts                    -> gate 1 (root; all others fail closed under it)
HOLDOUT-UNIVERSE-SEAL + conjuncts                     -> gate 1, and named again at gate 8
QSPEC-SPEC-SEAL + conjuncts                           -> gate 1
PREDICTION-MAP-SEAL                                   -> gate 1, and named again at gate 8
every_type_in_Task6TypedPayload_preserved             -> EVERY gate, 1 through 9   (V2-3a)
```

[YOURS] The type-preservation conjunct is deliberately placed on **every** gate
rather than once: type erasure is a failure mode that can occur at any handoff,
and the failure ladder arms it as `type erasure` without limiting it to a step.

[PART-PROVABLE] `SPEC-SEAL` is the root of the authoritative graph, and under the
fail-closed rule its failure fails **every** other node. The current record books
it `false_of_record`, so **no gate above 0 is presently open** — the ladder is
unformed at its root, not partway up.

---

## V3. WHAT IS NOT COMPUTED, AND WHY — enumerated in the declaration

| # | Not computed | Why, with its citation |
|---|---|---|
| 1 | **The period-native functional** | `Γ` is unformed on **both** routes (witness certification §II); `PERIOD_NATIVE = false` is in the ratified type block. Nothing here forms it. |
| 2 | **Anything requiring `ExtSrc`** | `ExtSrc` is `TYPE-U` at derivation level and is the named reopening object (§II). The J-II `(L0)` cross-sector arrow is not supplied by A32. |
| 3 | **Anything on the new-cycle factors** | A6 carries the projected old-image scope only; *"no upward new-cycle lift"* is absent **by law**. No cycle-creating comparison is computed, and none is inferred from the rank-preserving square. |
| 4 | **Any comparison before the seal** | comparison occurs only after the governed result seals; gate 9 above. `proof_authorized` remains equivalent only to `FINAL-CLAIM-SEAL`. |
| 5 | **`kappa_record`** | `kappa_record_computed = false` stands; and the stiffness ruling puts `K_*`, not `kappa_record`, on alpha's path. Slot 16 is re-posed, not discharged. |
| 6 | **The seed's value** | the seed is `END_TEST_STRUCTURAL`, unexecuted by design (§II); neither `(S28)` nor its negation is assumed. |
| 7 | **`A_RP^+` inhabitance** | `EMPTY_OF_RECORD` (§II). No step here inhabits it, and no result is reported as if it were inhabited. |
| 8 | **R9's identification** | `PENDING` its first common physical cell (§II). R9 is a falsifier, not a constructor, and this declaration forms no common cell. |
| 9 | **Any numeric `nu`** | (V1-7): symbolic throughout; inability to proceed symbolically is a stop. |

[YOURS] Items 1–3 are the ones a reader is most likely to think this declaration
quietly supplies. It does not: the local route is a **shadow** route, and its
product is typed as such in the lead precisely so that no downstream consumer can
mistake it for the period-native object.

---

## V4. THE FALSIFIER AND DISPOSITION PLAN — pre-registered before any value exists

[YOURS] Every disposition below is fixed **now**, while no value exists. That is
the point: a disposition chosen after seeing a value is not a disposition.

### (V4-1) Lattice-cell dispositions

| Outcome | Disposition — pre-registered |
|---|---|
| Cell 1, 2, 3, or 5 | `q_loop = 0`, strict contraction. Step 11 proceeds on the same `w` and domain. Record the cell **and** which of the four it was; do not report "contraction" without the cell. |
| Cell 4, `\|chi_K\| < A_loop^{-1}` | strict contraction. Step 11 proceeds. Record the inequality's two sides as exact rationals/symbols, not the verdict alone. |
| Cell 4, `\|chi_K\| ≥ A_loop^{-1}` | **not** strict by this threshold. Step 11 does **not** proceed. Record `NOT_CONTRACTIVE_BY_THRESHOLD`; do **not** search for an alternative metric to rescue it — that is the alternate-complete-metric attack the `MODULUS_COMPATIBILITY_CERT` exists to block. |
| Cell 6 (`A_loop = ∞`, `chi_K ≠ 0`) | **excluded of record**; `q_loop = ∞`; not contractive. Record `EXCLUDED_CELL`. No rescue. |
| Cell count discrepancy unresolved (V1-3) | **stop before Step 10.** The cell determination may not run against an unfixed lattice. |

### (V4-2) The `chi_K` one-sided readings

```text
chi_K = 0        -> cells 1/3/5; q_loop = 0; strict contraction.
                    This is a LATTICE CELL, not a seed verdict.
seed q_T,RL = 0  -> chi_K polar; OUT_OF_LATTICE.
                    Payload records OUT_OF_LATTICE or noncomputable.
                    NOT a negative verdict; no value invented.        (V4-2a)
```

[YOURS] These two must not be conflated in any report. `chi_K = 0` is *inside*
the licensed lattice and is a strict-contraction cell; a **vanishing seed** drives
`chi_K` polar and *exits* the lattice. A report that renders both as "chi is zero"
destroys the one-sided rider.

### (V4-3) Branch voids and the A7 dispositions

| Outcome | Disposition |
|---|---|
| Both branches computable | report **per branch**; no aggregate verdict is created; neither selected, averaged, merged, nor dropped |
| One branch exits the lattice | that branch records `OUT_OF_LATTICE`; the other reports normally; **the pair is still reported as a pair** |
| Contact absent from the local route | `A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE`, displayed, never omitted (V1-6a) |
| Schema cannot carry both branches | **unresolved gate**, not permission to choose one — the ratified instrument's rule |

### (V4-4) OBS-ledger dispositions and the armed falsifiers

[PROVABLE] Armed and unchanged: the axiom's `F0–F7`; the four A9-era falsifiers;
the A4/A5 voids; the counterexample regressions; `F-U1`/`F-U2`/`F-C3`. From the
ratified ladder, each of the following **fails the appropriate gate**: prior
outcome access; an empty eligible set; registry/universe drift; failed commitment;
beacon substitution; duplicate ambiguity; identical comparator prediction;
post-unmask map editing; **type erasure**; **undeclared cross-sector conversion**;
branch/route/member selection; and any attempted numerical execution before its
gate.

[YOURS] Two dispositions I fix explicitly because they are the ones most likely to
be argued away in the moment:

```text
EMPTY ELIGIBLE SET       -> FAILS CLOSED. An empty screen is not permission to
                            relax a rule, select a favorable branch, or strip
                            the shadow type.
A WRONG RESULT ON ONE
FUTURE BOUND MEMBER      -> refutes THAT INSTANCE. It does not refute the whole
                            family without a separate rigidity theorem.  (V4-4a)
```

---

## V5. BATTERY

### (V5-1) `F_PLDEC` and the false anchor

[YOURS] The only dependency direction this declaration uses is **downward from
sealed structure to the shadow value**. No step consumes: a desired reader value;
the false anchor; a seed outcome; an A7 branch choice; an R9 equality; a HOL
return; or any measured constant. In particular `pi_Mx ∘ Loc ∘ Kernbar ∘ Q = 1`
is a **forbidden** input here, as it is in the sealed regression — importing it
would run the normalization branch and the `F_PLDEC` hazard.

### (V5-2) Anti-tuning ledger, with the cross-sector-unit row

| Attack | Check in this declaration | Result |
|---|---|---|
| choose an `E_C` branch to open a route | both carried; vacuity displayed if absent | clean |
| tune the metric to rescue cell 4 | `MODULUS_COMPATIBILITY_CERT` sealed **before** `A_loop`; no post-hoc metric | clean |
| instantiate `nu` to make a step close | `nu` symbolic throughout; inability is a stop | clean |
| float arithmetic then round to a rational | exact rational/symbolic only, implementation named and hashed | clean |
| relax a rule because the screen is empty | empty fails closed, explicitly | clean |
| **set a cross-sector unit silently to one** | **every required cross-sector-unit factorization is displayed in the propagation trace; no conversion silently set to one; undeclared conversion is an armed falsifier** | clean |
| promote `LOCAL-SHADOW` by passing through A32 | forbidden by the ratified text; type propagates through `1/(4π·)` | clean |
| seal the map after the value | Step 8 does not retroactively create the map seal | clean |
| infer nonvanishing from cycle presence | no seed outcome inferred | clean |

[PROVABLE] The cross-sector-unit row is DoR-020-A2's frozen clause 8.

### (V5-3) Surface anchor

**Named actual objects:** `D_w`, `d_w`, `K_amb`, `B_w`, `S_w`, `Pi_w`, `ell_w`,
`Schur`, `a_loop`, `A_loop`, `q_loop`, `chi_K`, `Rhat_K`, `C_RET_SCOPE_w`,
`MODULUS_COMPATIBILITY_CERT[w]`, `domain_complete_cert_w`, `K_*`, `C_record`.

**Rails awaiting members:** the period-native functional; `ExtSrc`; `Γ` on either
route; `A_RP^+`; the R9 common cell; the P3 comparator; the P4 domain bridge.

[YOURS] The load-bearing distinction: the **left** column is what this declaration
computes with; the **right** column is what it must not pretend to have. The
declaration's whole discipline is keeping the assembly on the left column while
naming the right one in V3.

### (V5-4) Dependency re-audit

| Changed input | Direct consumers re-walked |
|---|---|
| A32 ratified (Q-536) | gate map V2-2 rows 0–1; the type block; the headline qualification |
| A2 Arm A adopted (Q-529) | the nine frozen clauses; clause 8 into V5-2; clause 3 into V1-5 |
| `(M5a-V002)` conjuncts | V2-3 mapping; gate 1 in full |
| Authoritative 11-node graph | gates 1 and 8; `(G6)`'s four parents |
| Witness certification §II | every row of V3 |

### (V5-5) Self verb audit

| My verb | Check |
|---|---|
| `DRAFTED` | A draft for later ruling. It adopts nothing, and the ratification's own limit on ruling it is quoted in §0. |
| "is computed" throughout V1 | Means **would be computed when licensed**. No step is executed here; `NUMERIC_EVALUATION = false`. |
| `GATE_MAP = BOUND` | Bound **as drafted**, each row cited. Rows are proposals for the reviewer, not certifications — no gate is asserted open, and gate 1 is presently closed at the root. |
| (V1-6) A7 | Typed **TYPE-U** on whether contact enters at all, with both dispositions displayed. I did not guess, and I did not let the likely answer (vacuous) become a silent omission. |
| (V1-3) the cell count | Flagged as an **inherited discrepancy, not harmonized** — the failure mode I audit in others' work applies to my own drafting. |
| "pre-registered" (V4) | Fixed while no value exists, which is the only sense in which a disposition is pre-registered. |
| `alpha_micro = 1/(4π K_*)` | Carried as the ratified **symbolic** assembly. No value, no comparison, and the `LOCAL-SHADOW` type propagates through it. |
| Sources | Every clause cites a sealed source or is tagged `[YOURS]`. I authored no physics law, candidate, comparator, number, branch selector, threshold, or seal. |

---

```text
DECLARATION = DRAFTED (+10 V1 clauses; +9 V2-2 gate rows; +8 V2-3a conjunct
  bindings; +9 V3 not-computed rows; +4 V4 disposition blocks; +5 V5 battery
  sections. Product typed LOCAL-SHADOW in the lead before any value exists;
  nu symbolic throughout; arithmetic exact rational or exact symbolic only)
GATE_MAP = BOUND (gate 0 the Step-2 ruling; gate 1 the full pre-evaluation rail
  SPEC -> {HOLDOUT, QSPEC} -> PREDICTION-MAP before ANY numerical execution;
  gates 2-7 the chain steps with MODULUS_COMPATIBILITY_CERT sealed before
  A_loop; gate 8 any numeric alpha behind (G6)'s four transitively certified
  parents; gate 9 comparison only after the governed result seals.
  SPEC-SEAL is false_of_record, so no gate above 0 is presently open)
NOT_COMPUTED = enumerated (9 rows, each cited: the period-native functional;
  anything requiring ExtSrc; the new-cycle factors; any comparison before the
  seal; kappa_record; the seed's value; A_RP^+ inhabitance; R9's identification;
  any numeric nu)
DISPOSITIONS = pre-registered (lattice cells incl. the no-rescue rule on cell 4
  and the excluded cell 6; the chi_K = 0 vs polar-seed distinction that must
  never be conflated; the A7 branch voids incl. mandatory vacuity display;
  the OBS ledger with empty-set fail-closed and the one-instance refutation
  scope)
VERB_AUDIT_SELF = CLEAN
```

**Two items I hand to the reviewer as the places this draft is most likely
wrong.** First, (V1-6): whether contact enters the local route is `TYPE-U` in my
reading of the sealed chain, and if Codex 3 can establish either disposition from
sealed text, that clause should be replaced rather than carried as a fork. Second,
(V1-3): the six-versus-eight lattice-cell count is an inherited discrepancy I
declined to resolve, and the disposition plan at V4 keys on the cell
determination — so it must be fixed of record before Step 10 can run, and the
fixing is not mine to do.
