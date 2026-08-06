# STAGE 8 / TASK 6 / STEP 2 — THE EVALUATION DoR: THE SCOPE DECLARATION — V005

Lane: Codex Lane 3 (SOL, high effort), drafting lane
Task: PASTE 613 / Task 6, Step 2
Authority to draft: DoR-020-A8 + the ratified A32 instrument. **THIS ARTIFACT IS A
DRAFT. IT ADOPTS NOTHING, RULES NOTHING, LIFTS NO GATE, AND COMPUTES NOTHING.**
Base: Dario V004 (`1e3e24289b97303bba1e8f57612e09dbace897e482ee9d25c2af35953524b000`).
Repair authority: Q-548 + Lane-3 sweep (`f651b34befdaa0f2410778e80c970f355e39cab733cdb64f9e37706950bfbedc`).
Custody: **DRAFT under the pen swap.** Close exactly F1–F4; Dario re-sweeps fresh.

## Lead — the declaration's type, stated first

```text
THE PRODUCT OF THIS DECLARATION IS TYPED, BEFORE ANY VALUE EXISTS.

The four fields below are carried VERBATIM from the ratified SUBJECT:

  COMPUTATION_SCOPE = LOCAL
  PRODUCT_TYPE      = LOCAL-SHADOW
  TRIAL             = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE
  PERIOD_NATIVE     = false                                        (W1-1)

It may not be renamed a global period, holonomy charge, period-native Maxwell
quantity, kappa_Thomson, physical alpha, or a two-sided trial.

THE FOLLOWING TWO FIELDS ARE NOT PART OF THE RATIFIED FOUR-FIELD SUBJECT:

  A7_BRANCH  = VACUOUS_ON_LOCAL_ROUTE   [PROVABLE — resolved at (V1-6), per W2]
  ARITHMETIC = EXACT RATIONAL OR EXACT SYMBOLIC ONLY   [PROVABLE — Gate-5 spec]

The further exclusion "NOT K_*" carried in V001 is [YOURS], not ratified
provenance, and is retained on that tag only.                       (W1-3)

DECLARATION = DRAFTED
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
MEMBER_BOUND = false ; FIXED_POINT_EXECUTED = false ; END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false ; MEASURED_CONSTANT_COMPARISON = none
```

```text
LOCAL-SHADOW --[K |-> 1/(4 pi K)]--> LOCAL-SHADOW,
1/(4 pi .) is not a promotion operator.                             (W1-2)
```

## 0. Preflight and the finite V004→V005 delta contract

| Check | Result |
|---|---|
| Register head Q-548 (live-append tolerant) | verified — Q-548 is the pen-swap authority |
| Base V004 | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V004.md`, SHA-256 `1e3e24289b97303bba1e8f57612e09dbace897e482ee9d25c2af35953524b000`, verified before reading |
| Finding artifact | `STAGE8_TASK6_DOR_V004_SWEEP_LANE3_V001.md`, SHA-256 `f651b34befdaa0f2410778e80c970f355e39cab733cdb64f9e37706950bfbedc`, verified before reading |
| V001 historical board source | `STAGE8_TASK6_EVALUATION_DOR_DRAFT_DARIO_V001.md`, SHA-256 `9704f27355ec97f447c23e180d0e52f1177b7bd713773c347061d8fe1b1616d8` |
| Certificate-mode sources | `STAGE8_TASK5_GAMMA_H_ROUTE_LANE3_V001.md`, `f2317e41367dc906ffa23f6055f2ed96a0f59f74b4e412966809d292c23e5402`; `STAGE8_TASK5_CHAIN_CONFORMANCE_AUDIT_LANE3_V002.md`, `44202c060821728fba2c46b81b82487002e639f3242565b7a5fed387e41fcae8`; both seals verified |
| Output collision | none — clear to draft |
| Protected operations | none performed |

### 0.1 C-V5 — the enumeration is the finite claim

```text
DELTA_DOMAIN
  := the ordered hunks emitted by `/usr/bin/diff -U 0`
     on V004 -> V005; H01,H02,... name those hunks in emitted order.

CONTROL_METADATA
  := title/version, lane/task, base/repair authority, custody, preflight,
     and final version identifiers.

SUBSTANTIVE_DELTA
  := DELTA_DOMAIN with CONTROL_METADATA separately identified, not discarded.

DELTA_ROWS
  := {M0, F1, F2, F3, F4, R1, F5, Z1}.

CLAIM_V005
  := DELTA_DOMAIN
       = disjoint_union_(R in DELTA_ROWS) EXACT_HUNKS(R).

PRESEAL_CHECK
  := UNASSIGNED_HUNKS = empty
     and MULTIPLY_ASSIGNED_HUNKS = empty.                         (C-V5)
```

`(C-V5)` is the named finite equality for this one version pair. It does not
claim verbatim carriage over an unnamed clause class or another version pair.
A nonempty side of `PRESEAL_CHECK` stops sealing.

### 0.2 V004→V005 delta rows

| Row | Exact edit class | Destination | Pre-seal hunk set |
|---|---|---|---|
| M0 | control metadata and preflight identifiers | header; §0 preflight | `{H01,H02,H03,H05}` |
| F1 | restore the V001 four-block final board verbatim; append the operative current overlay so K3/K4 and later gates are not rolled back | after V5-5 | `{H34,H35}` |
| F2 | replace Part D with the immediate V004→V005 diff domain, row taxonomy, hunk partition, pre-seal exceptional-set test, and §0 tag/ratification editorial reflow | §0 heading; §0.1–0.2 | `{H04,H09–H21}` |
| F3 | replace C-V4's contradictory carriage wording with C-V5's finite-equality scope; replace literal/full-block overclaims with accurate carriage verbs; restore E2's `are computed` predicate | §0.1; V1-5; V1-9; V2-3; V5-5 | `{H06–H08,H22,H25–H27}` |
| F4 | type P-1 availability by Q/FACTOR mode; scope H/direct-M2 vacuity; carry UNFORMED_OF_RECORD without proving nonexistence | V1-5; V5-2; V5-3; V5-5 | `{H23,H24,H28,H29}` |
| R1 | re-audit F1–F5 dependencies | V5-4 Table E | `{H30,H31}` |
| F5 | current self-verb audit and pre-seal re-diff display | V5-5; §V6 | `{H32,H33}` |
| Z1 | adjacent terminal hunk containing the E5 completion, operative overlay, re-diff display, current status board, and required final lines | E5 continuation; V6; final | `{H36}` |

```text
PRESEAL_DIFF_HUNKS   = 36;
PRESEAL_DIFF_ADDED   = 231;
PRESEAL_DIFF_DELETED = 105;
UNASSIGNED_HUNKS     = empty;
MULTIPLY_ASSIGNED_HUNKS = empty.                                 (D5-CLEAN)
```

**Tag legend.** `[PROVABLE]` = carried from a sealed source at its sealed verb.
`[PART-PROVABLE]` = holds on a named subscope. `[YOURS]` = drafted here, not
law. `[TYPE-U]` = a lawful object with no member produced; emptiness not proved.

[PROVABLE] The ratification's limit remains: this DoR *"may DRAFT in parallel …
but may not be ruled before the subgate's own gate conditions are met."*
`(M5a-V002)` remains `false_of_record`.
---

## V1. WHAT IS COMPUTED, EXACTLY

### (V1-1) The subject and its domain — [PROVABLE]

```text
(D_w, d_w) complete;  D_w subset K_amb;  D_w closed in complete K_amb;
B_w := ell_w o Pi_w o Schur o S_w ;   B_w : D_w -> D_w.        (V1-1a)
```

Two obligations are **not** discharged by ambient completeness and are carried as
named gates: `D_w` nonemptiness is *"carried only by explicit `C_ret` clause"*,
and *"Completeness of the ambient scalar carrier does not imply completeness of
`D_w`; `domain_complete_cert_w` is an independent item."*

### (V1-2) Step 8–9: the modulus — U1

```text
RetExtract[dot Schur] = a_loop Rhat_K                            (step 8)
A_loop := sup_(D_w) |a_loop|
q_loop  = sup_(D_w) |dot B_w| = |chi_K| A_loop   under C_RET_SCOPE_w   (step 9)
```

[PROVABLE] `MODULUS_COMPATIBILITY_CERT[w]` is a separate falsifiable gate at the
Step 8/9 seam, discharged by exactly one of two witnesses, with their conditions
displayed:

```text
DIFF_TO_METRIC:
  certified chart equivalence
  + exact chain-rule transport of the Step-8 bound to d_w;

DIRECT_MODULUS:
  A_loop defined by d_w-difference quotients directly
  + Step-8 derivative used only as a consistency witness;

without either witness, sup|dot B_w| may disagree with the true d_w modulus.
                                                                    (U1-V1)
```

[YOURS] The witness is named and sealed **before** `A_loop` is evaluated, not
after. A modulus computed first and reconciled afterwards is the
alternate-complete-metric attack, not a check against it.

### (V1-3) Step 10: the case-lattice cell determination — K4

```text
A_loop regime in {0, 0<A_loop<infinity, infinity}
  times
finite chi_K regime in {0, nonzero}                              (W3-1)

3 x 2 = 6.        CELLS = six_of_record.                         (W3-2)
```

| Cell | `A_loop` | finite `chi_K` | Status |
|---:|---|---|---|
| 1 | `0` | `0` | `q_loop = 0`, strict |
| 2 | `0` | nonzero | `q_loop = 0`, strict |
| 3 | finite positive | `0` | `q_loop = 0`, strict |
| 4 | finite positive | nonzero | strict iff `|chi_K| < A_loop^{-1}` |
| 5 | `infinity` | `0` | `q_loop = 0` by separate pointwise rule, strict |
| 6 | `infinity` | nonzero | `q_loop = infinity`, excluded / not contractive |

[PROVABLE] `C1` corrects the one `P1` prose numeral; this lattice governs Step 10
and every disposition; `CHAIN-X` independently enumerates the same six. **There is
no seventh or eighth cell.**

### (V1-4) Step 11: the Banach consequence — [PROVABLE]

Conditional existence/uniqueness *"under Step 10 for the same `w` and the same
complete `D_w`."* [YOURS] The sameness conditions are **operative**: a fixed point
obtained on a different `w`, a different domain, or a domain whose completeness
certificate is not the one used at Step 9 is not this chain's fixed point and may
not be reported as it.

### (V1-5) The one-sided-trial rider — **P-1 FAITHFULLY CARRIED; F4 MODE-PRECISE**

```text
seed nonzero  -> chi_K finite; the computation remains INSIDE the licensed
                 lattice; a confirming outcome MAY CONFIRM.
seed zero     -> chi_K is a POLE / OUT-OF-LATTICE condition.
                 IT IS NOT A NEGATIVE VERDICT.                    (V1-5a)
```

[PROVABLE] The mechanism of record: `chi_K^Mx` carries `q_T,RL` in a denominator,
and **the licensed case lattice has no infinite-`chi_K` cell** — so a vanishing
seed exits the licensed lattice rather than refuting anything. On seed zero the
payload records `OUT_OF_LATTICE` or noncomputable, **and no value is invented.**

[PROVABLE] **The cure, restored:**

```text
The cure is carried CARRIED-CONDITIONAL and requires
  a formed period route
  + the true d^per modulus certificate.                          (P-1)
```

[YOURS — P-1 mode-precise availability] The cure remains
`CARRIED-CONDITIONAL`. Carriage is not availability.

```text
CURE_AVAILABLE_OF_RECORD(a,epsilon,r;Q)
 := ROUTE_FORMED_TRUE_OF_RECORD(a,epsilon,r)
    and M2_SUBJECT_FORMED_TRUE_OF_RECORD(a,epsilon,r)
    and PERIOD_MODULUS_COMPATIBILITY_CERT_TRUE_OF_RECORD
          [a,epsilon,r;Q].

For r=H in the direct-M2 presentation only, the last conjunct is
VACUOUS_UNDER_M2 once that route's M2 subject is formed. This schema-level
vacuity is not exported to another route and does not form a route instance.

CURE_AVAILABLE_OF_RECORD(a,epsilon,r;FACTOR)
 := ROUTE_FORMED_TRUE_OF_RECORD(a,epsilon,r)
    and FIXED_PERIOD_FACTOR_CERT_TRUE_OF_RECORD(a,epsilon,r)
    and PERIOD_MODULUS_COMPATIBILITY_CERT_TRUE_OF_RECORD
          [a,epsilon,r;FACTOR].

CURRENT_ROUTE_STATUS = UNFORMED_OF_RECORD on both routes;
therefore neither availability predicate is established and no
route-specific certificate instance is consumed.                 (P-1-V005)
```

The H/direct-M2 Q schema remains `VACUOUS_UNDER_M2` at schema level; FACTOR
retains its fixed-factor and factor-modulus debts. Consequently P-1 may not be
invoked now. A polar/`OUT_OF_LATTICE` local reading remains `OUT_OF_LATTICE` or
noncomputable; it is not converted into a negative, confirming, or other
verdict.

### (V1-6) Contact on the local route — K3, **+E1 RESTORED**

```text
LOCAL_CHAIN_FACTORS = {S_w, Schur_w, Pi_w, ell_w};

E_C,N in Hom(C_N^k,C_N^k);

C_N^k is not a declared interface of LOCAL_CHAIN_FACTORS;
E_C,N is not a declared field or argument of any local factor;

LOCAL_CHAIN_C_N^k_INTERFACE   = none_of_record;
LOCAL_CHAIN_E_C_CONSUMER_SEAM = none_of_record;

therefore, for this declared LOCAL-SHADOW composite contract,
A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE.                              (W2-5)

CONTACT_LOCAL_ROUTE = VACUOUS_ON_LOCAL_ROUTE
CONTACT             = VACUOUS_PROVEN.                            (W2-6)
```

**Scope of `VACUOUS_PROVEN`:** the declared local-chain contract consumes no
sealed `E_C` seam. No equality of stationary families across A7 branches is
asserted; no `S_(w,epsilon)` family is formed; no branch is computed, chosen, or
bound. **`A7` continues to carry ZERO and IDENTITY through any later formed period
machinery.**

[YOURS] The field is **DISPLAYED, never omitted**: a payload silently lacking the
branch index cannot be distinguished later from one whose branch was dropped.

[PROVABLE] **The residual rule for the later period machinery, restored to this
clause block:** *"If the prediction-map schema cannot carry both branches, that is
an unresolved gate, not permission to choose one."* It governs where A7 is **not**
vacuous. The matching disposition is also displayed at (V4-3); both are retained.

### (V1-7) `nu` symbolic throughout — [YOURS]

`nu` is carried as a **symbol** at every step. No numeric `nu` is substituted,
defaulted, fitted, or set to a convenient value at any point of steps 8–11 or the
assembly. Any step that cannot proceed with symbolic `nu` is a **stop**, reported
as such, not a licence to instantiate one.

### (V1-8) The sensitivity ladder's place — U2

[PROVABLE] Chain step 12 is *"Sensitivity-system and witness-to-number ladder
preparation."* Its place is **after** the Step-11 conditional result, and it is
theory-side only. **Both limitations bind, and they are independent:**

```text
(M5) is not repaired by sensitivity alone;
Task-6 sensitivity cannot itself supply the missing preselection
measurement-metadata bridge.                                    (U2-V1)
```

[PART-PROVABLE] Under `(W2-6)` there is no A7 branch index on this route, so
"per A7 branch" is withdrawn **for the local route only**. Branch-indexed
sensitivity returns with the period machinery.

### (V1-9) The rationality check's place — **E2 CONTENT FAITHFULLY CARRIED**

[PROVABLE] All finite-`L` objects are computed in **exact rational or exact symbolic
arithmetic**, with the implementation **named and hashed**, and any enclosure
reported as exact rational strings (`lower`, `upper`).

[YOURS] Its place is a **precondition on every numeric step, not a post-hoc
audit**: a float-path result is not a defective value of this declaration, it is
**not a value of this declaration at all**.

### (V1-10) The assembly, symbolic-first

[PROVABLE] `K_*` — the onset root of `C_record(K_*) = 0` with `dC_record/dK ≠ 0`
and `K_* > 0` — **is alpha's stiffness**, and `alpha_micro = 1/(4 π K_*)`.

```text
1. Derive the assembly SYMBOLICALLY first, nu symbolic, arithmetic exact.
2. The symbolic form is the deliverable of this declaration.
3. NO numeric alpha is produced by this declaration under any outcome.
4. Any numeric evaluation is a SEPARATE licensed act behind (G6), and it
   remains subject to every type in the lead.                    (V1-10a)
```

[YOURS] `alpha_micro` computed from a `LOCAL-SHADOW` input is a
`LOCAL-SHADOW`-typed expression, per `(W1-2)`. `(V1-10a)`'s symbolic-first
requirement is **also** enforced in the gate table at row 8.

---

## V2. THE ORDER OF OPERATIONS AND THE GATE MAP

### (V2-1) The authoritative ancestry — [PROVABLE]

The ruled 11-node graph governs; `stage_dependencies` is authoritative for node
set, edges, and fail-closed descendants; certification is **transitive**. The
ruling's binding phrase travels: *"This act cannot loosen any gate."*

### (V2-2) The gate map — D1 at row 8, K2 at row 2

| # | Operation | May not begin until | Certification point |
|---|---|---|---|
| 0 | **This declaration is ruled** | `(M5a-V002)` supplies the conjuncts this DoR requires of it | principal's Step-2 act |
| 1 | Any **numerical** execution whatsoever | `A32_PRE_EVALUATION_READY = true`, i.e. the full rail `SPEC-SEAL → {HOLDOUT-UNIVERSE-SEAL, QSPEC-SPEC-SEAL} → PREDICTION-MAP-SEAL` with every non-seal conjunct at each node | evaluator-certified per `(G3)` |
| 2 | Step 8 (`RetExtract[dot Schur]`, `a_loop`) | `A32_PRE_EVALUATION_READY` + successful chain Steps 0–7 on the same `w` and `D_w` + `C_RET_SCOPE_w` + differentiability on that branch `(W1-7)` | evaluator |
| 3 | Step 9 (`A_loop`, `q_loop`) | gate 2; **plus `MODULUS_COMPATIBILITY_CERT[w]` witness named and sealed** | evaluator |
| 4 | Step 10 (lattice cell) | gate 3; the governing six-cell identity `(W3-1)`/`(W3-2)` | evaluator |
| 5 | Step 11 (Banach consequence) | gate 4; plus `domain_complete_cert_w` and `D_w` nonemptiness by explicit `C_ret` clause | evaluator |
| 6 | Step 12 (sensitivity) | gate 5 | evaluator |
| 7 | Symbolic assembly `1/(4π·K_*)` | gate 6; `K_*` established as the onset root, `nu` still symbolic | evaluator |
| 8 | **Any numeric alpha value** | **gate 7 + `ALPHA-RESULT-SEAL` with its four `(G6)` parents transitively certified + the separate licensed act** `(K2-R)` | evaluator + a separate licensed act |
| 9 | **Any comparison to a measured value** | after the governed result seals; beacon, unmask and contamination only at their ruled positions | Step 9 of the escrow order |

[PROVABLE] Row 2 carries the chain's mathematical entrance; **rows 3–8** inherit
it transitively. Row 8 additionally names gate 7, so no numeric act can issue on
custody alone.

[PROVABLE] Step 8 of the board seals the assembled number; **it does not
retroactively create the prerequisite prediction-map seal.**

### (V2-3) Where `(M5a-V002)`'s conjuncts gate which step — **E3 CONTENT FAITHFULLY CARRIED**

```text
instrument_ratified                                   -> gate 0   (SATISFIED)
schema_and_canonical_ID_tensions_resolved             -> gate 1
executable_eligibility_and_comparator_interfaces_frozen -> gate 1, and gate 9
Q25_current_scalar_commitment_disposition_carried     -> gates 1 and 9 (headline)
SPEC-SEAL + its non-seal conjuncts                    -> gate 1 (root)
HOLDOUT-UNIVERSE-SEAL + conjuncts                     -> gate 1, again at gate 8
QSPEC-SPEC-SEAL + conjuncts                           -> gate 1
PREDICTION-MAP-SEAL                                   -> gate 1, again at gate 8
every_type_in_Task6TypedPayload_preserved             -> EVERY gate, 1 through 9
```

[YOURS] **The rationale, restored:** the type-preservation conjunct is
deliberately placed on **every** gate rather than once, because **type erasure is
a failure mode that can occur at any handoff**, and the failure ladder arms it as
`type erasure` **without limiting it to a step**.

[PART-PROVABLE] `SPEC-SEAL` is `false_of_record` and is the graph root, so under
the fail-closed rule **no gate above 0 is presently open** — the ladder is
unformed at its root, not partway up.

---

## V3. WHAT IS NOT COMPUTED, AND WHY — U5

| # | Not computed | Why, with its citation |
|---|---|---|
| 1 | The period-native functional | `Γ` unformed on **both** routes; `PERIOD_NATIVE = false` is ratified |
| 2 | Anything requiring `ExtSrc` | `TYPE-U` at derivation level; the named reopening object. **`J-II (L0)` is not supplied by A32.** |
| 3 | Anything on the new-cycle factors | A6 carries the projected old-image scope only; no upward new-cycle lift **by law**; **no new-cycle comparison is inferred from a rank-preserving square** |
| 4 | Any comparison before the seal | gate 9; `proof_authorized` ≡ `FINAL-CLAIM-SEAL` only |
| 5 | `kappa_record` | `kappa_record_computed = false`; `K_*`, not `kappa_record`, is on alpha's path |
| 6 | The seed's value | `END_TEST_STRUCTURAL`, unexecuted by design; **neither `(S28)` nor its negation is assumed** |
| 7 | `A_RP^+` inhabitance | `EMPTY_OF_RECORD`; no result is reported as if it were inhabited |
| 8 | R9's identification | `PENDING` its first common physical cell. **R9 is a falsifier, not a constructor, and no common cell is formed here.** |
| 9 | Any numeric `nu` | (V1-7): symbolic throughout; inability to proceed symbolically is a stop |

[YOURS] Items 1–3 are the ones a reader is most likely to think this declaration
quietly supplies. It does not: the local route is a **shadow** route, and its
product is typed as such in the lead precisely so that no downstream consumer can
mistake it for the period-native object.

---

## V4. THE FALSIFIER AND DISPOSITION PLAN — pre-registered before any value exists

[YOURS] Every disposition below is fixed **now**, while no value exists. That is
the point: a disposition chosen after seeing a value is not a disposition.

### (V4-1) Lattice-cell dispositions — **E4 RESTORED**

| Outcome | Disposition — pre-registered |
|---|---|
| Cell 1, 2, 3, or 5 | `q_loop = 0`, strict contraction. Step 11 proceeds on the same `w` and domain. Record the cell **and** which of the four it was. |
| Cell 4, `\|chi_K\| < A_loop^{-1}` | strict contraction. Step 11 proceeds. Record the inequality's two sides as exact rationals/symbols, not the verdict alone. |
| Cell 4, `\|chi_K\| ≥ A_loop^{-1}` | **not** strict by this threshold. Step 11 does **not** proceed. Record `NOT_CONTRACTIVE_BY_THRESHOLD`; **no search for an alternative metric to rescue it** — that is the alternate-complete-metric attack the `MODULUS_COMPATIBILITY_CERT` exists to block. |
| Cell 6 | **excluded of record**; `q_loop = ∞`; record `EXCLUDED_CELL`. No rescue. |

[PROVABLE] **V001's fifth row — a stop before Step 10 pending the count — is
deleted, and no count ambiguity remains:** `CELLS = six_of_record` by `C1`.

### (V4-2) The `chi_K` one-sided readings

```text
chi_K = 0        -> cells 1/3/5; q_loop = 0; strict contraction.
                    This is a LATTICE CELL, not a seed verdict.
seed q_T,RL = 0  -> chi_K polar; OUT_OF_LATTICE.
                    NOT a negative verdict; no value invented.      (V4-2a)
```

[YOURS] These must not be conflated in any report. `chi_K = 0` is *inside* the
licensed lattice and is a strict-contraction cell; a **vanishing seed** drives
`chi_K` polar and *exits* it. A report rendering both as "chi is zero" destroys
the one-sided rider.

### (V4-3) Branch dispositions — D2

| Route | Outcome | Disposition |
|---|---|---|
| **Local route** | always | `A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE`, **displayed** in every payload, never omitted. No branch is computed, chosen, averaged, merged, or bound. |
| **Later period machinery** | both branches computable | report **per branch**; no aggregate verdict is created; neither selected, averaged, merged, nor dropped |
| **Later period machinery** | **one branch exits the certified lattice** | **that branch records `OUT_OF_LATTICE`; the other branch reports normally; the pair is still reported as a pair; neither branch is selected, averaged, merged, or dropped** `(K3-R)` |
| **Later period machinery** | schema cannot carry both branches | **unresolved gate**, not permission to choose one |

### (V4-4) OBS-ledger dispositions and the armed falsifiers

[PROVABLE] Armed and unchanged: the axiom's `F0–F7`; the four A9-era falsifiers;
the A4/A5 voids; the counterexample regressions; `F-U1`/`F-U2`/`F-C3`. Each of the
following fails the appropriate gate: prior outcome access; an empty eligible set;
registry/universe drift; failed commitment; beacon substitution; duplicate
ambiguity; identical comparator prediction; post-unmask map editing; **type
erasure**; **undeclared cross-sector conversion**; branch/route/member selection;
and any attempted numerical execution before its gate.

```text
EMPTY ELIGIBLE SET  -> FAILS CLOSED. An empty screen is not permission to relax
                       a rule, select a favorable branch, or strip the shadow type.
A WRONG RESULT ON
ONE BOUND MEMBER    -> refutes THAT INSTANCE. It does not refute the whole family
                       without a separate rigidity theorem.          (V4-4a)
```

---

## V5. BATTERY

### (V5-1) `F_PLDEC` and the false anchor

[YOURS] The only dependency direction used is **downward from sealed structure to
the shadow value**. No step consumes a desired reader value, the false anchor, a
seed outcome, an A7 branch choice, an R9 equality, a HOL return, or any measured
constant. `pi_Mx ∘ Loc ∘ Kernbar ∘ Q = 1` is a **forbidden** input here, as in the
sealed regression — importing it would run the normalization branch and the
`F_PLDEC` hazard.

### (V5-2) Anti-tuning ledger — U3

| Attack | Check in this declaration | Result |
|---|---|---|
| use A32 readiness as chain entrance | row 2 requires successful Steps 0–7 on the same `w` and `D_w`; `(W4-2)` records the implication is absent from every cited rule | clean |
| use A32 seal ancestry as the symbolic assembly | row 8 additionally requires gate 7; `(F-1)` no longer satisfies the prerequisite column | clean |
| choose an `E_C` branch to open a route | vacuity **proven** on this route and displayed; both branches carried in the period machinery | clean |
| tune the metric to rescue cell 4 | `MODULUS_COMPATIBILITY_CERT` sealed **before** `A_loop`, with `(U1-V1)`'s conditions displayed | clean |
| instantiate `nu` to make a step close | `nu` symbolic throughout; inability is a stop | clean |
| float arithmetic then round to a rational | exact rational/symbolic only, implementation named and hashed; precondition, not post-hoc audit | clean |
| relax a rule because the screen is empty | empty fails closed, explicitly | clean |
| set a cross-sector unit silently to one | every required factorization displayed in the propagation trace; undeclared conversion is an armed falsifier. **Sealed provenance: DoR-020-A2's frozen clause 8.** | clean |
| promote `LOCAL-SHADOW` through A32 | forbidden; type propagates through `1/(4π·)` per `(W1-2)` | clean |
| seal the map after the value | Step 8 does not retroactively create the map seal | clean |
| invent a seventh or eighth cell | `CELLS = six_of_record`; `C1` governs | clean |
| invoke the `CARRIED-CONDITIONAL` period cure as if available, or export H/direct-M2 Q-vacuity to another route | availability is mode-specific by `(P-1-V005)`: both routes are `UNFORMED_OF_RECORD`; H/direct-M2 Q-vacuity applies only after its M2 subject is formed and is not route-generic; FACTOR additionally requires `FIXED_PERIOD_FACTOR_CERT` and its FACTOR-mode modulus certificate; no `OUT_OF_LATTICE` reading becomes a verdict | clean |
| infer nonvanishing from cycle presence | no seed outcome inferred | clean `(U3-V1)` |

### (V5-3) Surface anchor

**Named actual objects:** `D_w`, `d_w`, `K_amb`, `B_w`, `S_w`, `Schur_w`, `Pi_w`,
`ell_w`, `a_loop`, `A_loop`, `q_loop`, `chi_K`, `Rhat_K`, `C_RET_SCOPE_w`,
`MODULUS_COMPATIBILITY_CERT[w]`, `domain_complete_cert_w`, `K_*`, `C_record`.

**Rails awaiting members:** the period-native functional; `ExtSrc`; `Γ` on either
route; `A_RP^+`; the R9 common cell; the P3 comparator; the P4 domain bridge;
formed route/M2 subjects; a route-specific Q certificate where it is not
H/direct-M2-vacuous; and the fixed-factor plus FACTOR-certificate debts.

[YOURS] The left column is what this declaration computes with; the right column
is what it must not pretend to have. `E_C,N` and `C_N^k` appear in **neither**
column for this route — that is the content of `(W2-6)`.

### (V5-4) Dependency re-audit — U4, with all later tables appended

**Table A — the confirmed V001 re-walk `(U4-V1)`:**

| Changed input | Direct consumers re-walked |
|---|---|
| A32 ratified (Q-536) | gate map rows 0–1; the type block; the headline qualification |
| A2 Arm A adopted (Q-529) | the nine frozen clauses; clause 8 into (V5-2); clause 3 into (V1-5) |
| `(M5a-V002)` conjuncts | (V2-3) mapping; gate 1 in full |
| Authoritative 11-node graph | gates 1 and 8; `(G6)`'s four parents |
| Witness certification §II | every row of V3 |

**Table B — the K1–K4 re-walk, appended:**

| Rendering | Direct consumers re-walked |
|---|---|
| K1 `(W1-3)` | the lead block; later references to "the ratified type block" |
| K2 `(W1-7)` | gate row 2; **rows 3–8** which inherit it; (V5-2) |
| K3 `(W2-5)`/`(W2-6)` | (V1-6); the lead field; (V1-8); (V4-3); (V5-3) |
| K4 `(W3-1)`/`(W3-2)` | (V1-3); gate row 4; (V4-1); (V5-5) |

**Table C — the V003 fixes, appended:**

| Fix | Direct consumers re-walked |
|---|---|
| D1 `(K2-R)` | gate row 8; the inheritance statement; (V5-2); `(V1-10a)` |
| D2 `(K3-R)` | (V4-3) |
| U1–U5 | (V1-2), (V1-8), (V5-2), (V5-4), (V3) |

**Table D — V004's restorations, carried:**

| Item | Direct consumers re-walked |
|---|---|
| P-1 | (V1-5) one-sided rider; (V4-2); (V5-2)'s new cure row; (V5-3) rails |
| E1 | (V1-6); (V4-3)'s matching row confirmed retained |
| E2 | (V1-9); (V5-2)'s float row |
| E3 | (V2-3) |
| E4 | (V4-1) |
| E5 | (V5-5); the final board |

**Table E — V005's four repairs and pre-seal audit, appended:**

| Repair | Direct consumers re-walked |
|---|---|
| F1 — E5 final board | (V5-5); verbatim historical board; operative overlay; current final board |
| F2/F3 — finite delta contract and carriage verbs | §0.1–0.2; (V1-5); (V1-9); (V2-3); (V5-5); V6 |
| F4 — certificate-mode precision | (V1-5); (V5-2) cure row; (V5-3) rails; (V5-5) P-1 row; operative overlay |
| F5 — self-audit and re-diff | §0.2 hunk partition; (V5-5); V6; current final board |

[PROVABLE] No re-walk changed any cell's mathematics, any gate's ancestry, or any
protected flag.

### (V5-5) Self verb audit — **E5: V001 rows restored, later rows appended**

**Rows carried from V001:**

| My verb | Check |
|---|---|
| `DRAFTED` | A draft for later ruling. It adopts nothing, and the ratification's own limit on ruling it is quoted in §0. |
| "is computed" throughout V1 | Means **would be computed when licensed**. No step is executed here; `NUMERIC_EVALUATION = false`. |
| `GATE_MAP = BOUND` | Bound **as drafted**, each row cited. Rows are proposals for the reviewer, not certifications — no gate is asserted open, and gate 1 is presently closed at the root. |
| "pre-registered" (V4) | Fixed while no value exists, which is the only sense in which a disposition is pre-registered. |
| `alpha_micro = 1/(4π K_*)` | Carried as the ratified **symbolic** assembly. No value, no comparison, and the `LOCAL-SHADOW` type propagates through it. |
| Sources | Every clause cites a sealed source or is tagged `[YOURS]`. I authored no physics law, candidate, comparator, number, branch selector, threshold, or seal. |
| ~~(V1-6) A7 typed TYPE-U~~ | **SUPERSEDED by K3**: the fork is withdrawn and the value is proven `VACUOUS_ON_LOCAL_ROUTE`. Row retained here as superseded, not dropped. |
| ~~(V1-3) cell count flagged unresolved~~ | **SUPERSEDED by K4**: `CELLS = six_of_record` via `C1`. Row retained here as superseded, not dropped. |

**Rows appended by V002/V003/V004/V005:**

| My verb | Check |
|---|---|
| "carried **verbatim** from the ratified SUBJECT" | Scoped to the **four** fields `(W1-1)` only (K1). |
| `A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE` | PROVABLE at the declared local-composite contract, with the scope paragraph carried. Not a claim that A7 is discharged. |
| `CELLS = six_of_record` | PROVABLE via `C1`. |
| row 2 / row 8 | Row 2 names the chain's cumulative entrance; row 8 names gate 7. I record that V002 conflated custody with chain entrance, and that V002's row 8 permitted what my own `(V1-10a)` forbade. |
| (V4-3) period one-branch-exit row | **Displayed**, not asserted as retained. |
| `(P-1)` / `CARRIED-CONDITIONAL` | A carriage status only. Current route status is `UNFORMED_OF_RECORD`; neither mode-specific availability predicate is established. No nonexistence is claimed and no out-of-lattice reading is promoted to a verdict. |
| P-1 / E2 / E3 carriage | Their complete load-bearing content is faithfully re-rendered. They are not called verbatim or literal full-block reproductions. |
| `DELTA = ENUMERATED` | Means only the finite equality `(C-V5)` on the named V004→V005 line-level diff. It is falsified by an unassigned or multiply assigned hunk and says nothing about an unnamed version pair or clause class. |
| V001 final board reproduced verbatim | Historical carriage quotation only. It is not an operative rollback; the current overlay immediately below controls every superseded field. |
| V001 `(V1-6)` A7 `TYPE-U` row | **SUPERSEDED by K3**. Local contact is proven `VACUOUS_ON_LOCAL_ROUTE`; ZERO and IDENTITY remain carried for later period machinery. |
| V001 `(V1-3)` count-discrepancy row | **SUPERSEDED by K4/C1**. `CELLS = six_of_record`; the old count-stop does not regain force. |
| carried `GATE_MAP = BOUND` | Bound as drafted and read through current rows 2 and 8; it certifies no gate open and does not instantiate the P-1 period cure. |
| carried `NOT_COMPUTED = enumerated` | A summary of the nine current V3 rows; quotation forms none of their missing subjects. |
| carried `DISPOSITIONS = pre-registered` | Read through six-cell C1 and K3's local/period split; no obsolete fork or count stop is revived. |
| quoted V001 `VERB_AUDIT_SELF = CLEAN` | Historical token only. The current draft's audit is independently rerun after the overlay and finite delta audit. |
| `DOR_V005 = DRAFTED` | A draft under Q-548's pen swap. It rules nothing; `(M5a-V002)` remains `false_of_record`. |
| pre-seal re-diff | `(REDIFF-V005)` displays the computed V004→V005 hunk partition; sealing is barred unless both exceptional hunk sets are empty. |
| current `VERB_AUDIT_SELF = CLEAN` | Audits V005 only after F1–F5, the operative overlay, and `(REDIFF-V005)` are displayed; it is not inherited from the quoted V001 token. |

---

## E5 — V001 final board restored in its full block

**V001 final board, reproduced verbatim for E5 carriage. This is a historical
carriage quotation, not an operative rollback; the current overlay immediately
below governs every superseded field.**

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

**Current operative overlay:**

```text
DECLARATION:
  V005 remains DRAFTED and opens no gate.

GATE_MAP:
  row 2 carries successful Steps 0-7 on the same w and D_w
    + C_RET_SCOPE_w + differentiability;
  rows 3-8 inherit row 2;
  row 8 additionally requires gate 7
    + ALPHA-RESULT-SEAL with all four G6 parents transitively certified
    + the separate licensed act;
  SPEC-SEAL remains false_of_record; no gate above 0 is open;
  no local gate certificate instantiates the P-1 period cure.

NOT_COMPUTED:
  the nine current V3 rows remain operative with their U5 qualifications;
  this historical quotation forms none of their absent subjects.

DISPOSITIONS:
  CELLS = six_of_record;
  the V001 count-discrepancy stop is deleted and does not revive;
  local contact is proven VACUOUS_ON_LOCAL_ROUTE and must be displayed;
  the V001 V1-6 TYPE-U fork does not revive;
  later period machinery carries ZERO and IDENTITY per branch,
    including the one-branch-exits disposition;
  no selection, averaging, merging, or dropping is licensed.

P-1:
  availability is mode-specific by (P-1-V005);
  H/direct-M2 Q-vacuity is schema-level and not route-generic;
  FACTOR retains its fixed-factor and factor-certificate debts;
  CURRENT_ROUTE_STATUS = UNFORMED_OF_RECORD;
  no out-of-lattice reading is promoted to a verdict.

HISTORICAL_VERB_TOKEN:
  the quoted VERB_AUDIT_SELF = CLEAN audits V001 only;
  it does not certify V005.                                      (E5-OVERLAY)
```

```text
E5_V5_5_ROWS   = RESTORED_WITH_SUPERSEDED_ROWS_MARKED;
E5_FINAL_BOARD = RESTORED_VERBATIM_WITH_CURRENT_OVERLAY;
E5             = PASS.                                           (E5-V005)
```

## V6. Pre-seal re-diff and current status

```text
PRESEAL_DIFF_HUNKS      = 36;
PRESEAL_DIFF_ADDED      = 231;
PRESEAL_DIFF_DELETED    = 105;
M0                      = {H01,H02,H03,H05};
F1                      = {H34,H35};
F2                      = {H04,H09-H21};
F3                      = {H06-H08,H22,H25-H27};
F4                      = {H23,H24,H28,H29};
R1                      = {H30,H31};
F5                      = {H32,H33};
Z1                      = {H36};
UNASSIGNED_HUNKS        = empty;
MULTIPLY_ASSIGNED_HUNKS = empty.                                 (REDIFF-V005)
E5_BLOCK_TEXT_COMPARE   = equal (20 lines; 1,344 code units).
```

The eight sets in `(REDIFF-V005)` are pairwise disjoint and their union is
`{H01,...,H36}`. The two exceptional sets are empty, so the finite equality
`(C-V5)` holds on the displayed pre-seal diff.

```text
DOR_V005 = DRAFTED (+4/4 closed, +re-diff clean)
F1_E5 = CLOSED
F2_PART_D = CLOSED_BY_FINITE_HUNK_PARTITION
F3_C_V5 = CLOSED
F4_CERTIFICATE_MODE = PRECISE_AND_CLOSED
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARISON = none
MACHINERY_APPEAL = none
```

DOR_V005 = DRAFTED (+4/4 closed, +re-diff clean)
VERB_AUDIT_SELF = CLEAN
