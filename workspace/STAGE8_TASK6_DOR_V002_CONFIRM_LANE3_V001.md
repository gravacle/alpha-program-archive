# STAGE 8 / TASK 6 / STEP 2 — BOUNDED CONFIRM OF THE EVALUATION DoR V002

Lane: Codex Lane 3 (SOL, high effort)  
Date: 2026-08-06  
Register citation: living entry Q-543; the preflight head was Q-543  
Custody: bounded cross-family confirmation; no adoption, ruling, or execution

## Lead verdict

```text
DOR_V002
  = DEFECTIVE (+3 bounded findings)

D1  K2's corrected Step-8 row is exact, but its forced propagation stops at
    row 7: row 8 admits the separate numeric-alpha act without gate 7;

D2  K3's local-vacuity proof is exact, but one of the two former branch rows
    is only said to be retained for the period route: the one-branch-exits
    disposition is not displayed;

D3  DELTA=bounded / every-other-clause-carried-verbatim is false:
    V002 rewrites and deletes confirmed V001 material outside K1--K4,
    including load-bearing witness definitions and permanent audit rows.

RULING_READY_PENDING_SUBGATE = no.
```

The direct result per supplied rendering is:

```text
K1_DIRECT                 = PASS
K2_DIRECT_STEP8_ROW       = PASS
K2_FORCED_REWALK          = FAIL_AT_ROW8
K3_CORE_LOCAL_VACUITY     = PASS
K3_FORCED_REWALK          = INCOMPLETE_ONE_PERIOD_ROW
K4_FIVE_SURFACES          = PASS_5_OF_5
DELTA_BOUNDED             = false
V001_CONFIRMED_CONTENT    = not_intact
```

These are rendering and dependency failures. They do not change any source
mathematics and authorize no computation. Protected state remains:

```text
alpha_computed            = false
proof_authorized          = false
kappa_record_computed     = false
MEMBER_BOUND              = false
FIXED_POINT_EXECUTED      = false
END_TEST_EXECUTED         = false
NUMERIC_EVALUATION        = false
MEASURED_CONSTANT_COMPARE = none
```

## 0. Preflight and authority ledger

### 0.1 Preflight

| Check | Result |
|---|---|
| STEP 0 access | **PASS** — cleanroom, archive workspace, and supervision roots are readable. |
| Living register | **PASS** — Q-543 was terminal at preflight. Q-543 records this V002 and commissions this bounded confirm; the live-append tolerance requires no stop. |
| Artifact under review | **PASS** — `STAGE8_TASK6_EVALUATION_DOR_DARIO_V002.md`, SHA-256 `1f4834e67eb9f3819b26ea0339f10ec8dc7fdd649117ffa65af6ca58ac905ae4`, verified against its adjacent seal before reading. |
| Supplying review | **PASS** — `STAGE8_TASK6_DOR_REVIEW_LANE3_V001.md`, SHA-256 `20be8030aa69792e9ea963445f0a5844fcd27b593d2975c1d208f3bba6bdc93b`, verified against its adjacent seal before reading. |
| Output collision | **PASS** — this artifact and sidecar were absent from both the cleanroom and archive workspace before creation. |
| Fences | **PASS** — the work is textual and structural only; no protected act is required. |

### 0.2 Sealed comparison set

Every archive hash below was recomputed and its sidecar checked before the
cited content was consumed.

| Key | Source and SHA-256 | Use |
|---|---|---|
| `V2` | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V002.md` — `1f4834e67eb9f3819b26ea0339f10ec8dc7fdd649117ffa65af6ca58ac905ae4` | Subject under review. |
| `REV` | `STAGE8_TASK6_DOR_REVIEW_LANE3_V001.md` — `20be8030aa69792e9ea963445f0a5844fcd27b593d2975c1d208f3bba6bdc93b` | Exact K1–K4 supplied renderings and dependent-surface requirements. |
| `V1` | `STAGE8_TASK6_EVALUATION_DOR_DRAFT_DARIO_V001.md` — `9704f27355ec97f447c23e180d0e52f1177b7bd713773c347061d8fe1b1616d8` | Confirmed base whose non-delta content V002 says it preserves verbatim. |
| `CHAIN` | `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md` — `1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a` | Cumulative step inheritance and modulus witness forms. |
| `A32` | `STAGE8_TASK6_A32_PREP_LANE3_V002.md` — `c5d1090b1ec1862c59c1281845c9ad74d0b143e9a57f195c099adb16e56ae4ea` | Four-field subject, gate graph, and alpha-stop semantics. |
| `M5A` | `STAGE8_TASK6_M5A_STATUS_LANE3_V001.md` — `bcb8cced0a2d8a02083522623f12c838e9ea0035cf2f0d989f9d0b3dd21326a7` | Subgate remains false of record. |
| `C1` | `CHAIN_V004_CORRIGENDUM_C1_2026-08-06.md` — `cffbfce332c4e1b5ecd2e7e7c6b98db38331113875faba3f79a4aeedcf0afc39` | Six-cell correction governing every Step-10 consumer. |

### 0.3 Confirmation standard

- `PASS` means V002 exhibits the supplied rendering at the supplied strength
  and carries every forced direct consumer.
- `FAIL` means a required equality, disposition, or preserved clause is absent
  or contradicted by V002's own display.
- `[PROVABLE]` marks comparisons forced by the sealed texts above.
- `[YOURS]` marks this confirm's bookkeeping or repair wording; it adopts no
  clause and supplies no missing witness.
- A prose assertion that a row is “retained” is not a displayed row under the
  governing display standard.
- “Verbatim” means the actual words are preserved. “Content intact” is tested
  separately and fails if a load-bearing condition disappears even when a
  shorter paraphrase survives.

## 1. Y1 — the four supplied renderings and their forced re-walks

### 1.1 K1 — provenance of the lead block

`REV` supplied:

```text
The four fields in (W1-1) are carried verbatim from the ratified SUBJECT.
A7_BRANCH is resolved by W2 below; ARITHMETIC and the remaining exclusions
are separately sourced or tagged [YOURS].                         (K1-S)
```

`V2` applies `(K1-S)` in three displayed parts:

```text
RATIFIED SUBJECT:
  COMPUTATION_SCOPE = LOCAL
  PRODUCT_TYPE      = LOCAL-SHADOW
  TRIAL             = ONE-SIDED_ON_CURRENT_FINITE_CHI_LATTICE
  PERIOD_NATIVE     = false;

SEPARATE FIELDS:
  A7_BRANCH  = VACUOUS_ON_LOCAL_ROUTE [PROVABLE at V1-6]
  ARITHMETIC = EXACT RATIONAL OR EXACT SYMBOLIC ONLY [Gate-5 source];

NOT K_* = [YOURS], not ratified provenance.                       (K1-V2)
```

The later provenance audit also scopes “verbatim from the ratified SUBJECT” to
those four fields only. No later V002 sentence reattaches ratified provenance
to the additional fields.

`K1 = PASS / ADJUSTED_WITH_DISPLAY`.

### 1.2 K2 — cumulative mathematics before Step 8

`REV` supplied the operative row:

```text
Step 8 (RetExtract[dot Schur] and a_loop extraction)
  MAY NOT BEGIN UNTIL
    A32_PRE_EVALUATION_READY
    + successful chain Steps 0--7 on the same w and D_w
    + C_RET_SCOPE_w
    + differentiability on that branch.                          (K2-S)
```

`V2` gate-map row 2 reproduces all four conjuncts in `(K2-S)`. Its explanation
also carries the decisive non-implication:

```text
A32_PRE_EVALUATION_READY
  -/-> SUCCESSFUL_CHAIN_STEPS_0_THROUGH_7.                        (K2-1)
```

Rows 3–7 then explicitly depend on their predecessor:

```text
row 3 <- gate 2 + MODULUS_COMPATIBILITY_CERT[w];
row 4 <- gate 3 + six-cell identity;
row 5 <- gate 4 + completeness/nonemptiness;
row 6 <- gate 5;
row 7 <- gate 6 + established K_* + symbolic assembly.           (K2-2)
```

Therefore:

```text
K2_DIRECT_STEP8_ROW = PASS;
K2_PROPAGATION_ROWS_3_THROUGH_7 = PASS.                           (K2-3)
```

The propagation does not reach row 8. V002 displays:

```text
row 8, ANY NUMERIC ALPHA VALUE, requires
  ALPHA-RESULT-SEAL
  + its four transitively certified A32 parents
  + a separate licensed act;

row 8 does not require gate 7.                                    (K2-4)
```

`A32` establishes that `ALPHA-RESULT-SEAL` has no extra descriptive conjunct
beyond its four parents. None of those displayed parents is V002 gate 7, and
V002 supplies no implication from the alpha-stop token to its symbolic
assembly. Thus row 8 cannot inherit gate 7 silently.

The bounded rendering required to close the forced re-walk is:

```text
row 8, ANY NUMERIC ALPHA VALUE, MAY NOT BEGIN UNTIL
  gate 7
  + ALPHA-RESULT-SEAL with its four G6 parents transitively certified
  + the separate licensed act.                                   (K2-R)
```

The dependency re-audit must then say rows 3–8, not rows 3–7, inherit the
corrected mathematical entrance.

`K2 = FAIL_ON_FORCED_REWALK (+row8 bypass)`.

### 1.3 K3 — local contact vacuity and the period-only residues

The core supplied display lands exactly. V002 exhibits:

```text
LOCAL_CHAIN_FACTORS = {S_w, Schur_w, Pi_w, ell_w};
E_C,N in Hom(C_N^k,C_N^k);
C_N^k is not a declared interface of LOCAL_CHAIN_FACTORS;
E_C,N is not a declared field or argument of a local factor;
LOCAL_CHAIN_C_N^k_INTERFACE = none_of_record;
LOCAL_CHAIN_E_C_CONSUMER_SEAM = none_of_record;

therefore
A7_BRANCH = VACUOUS_ON_LOCAL_ROUTE;
CONTACT   = VACUOUS_PROVEN.                                      (K3-1)
```

The scope paragraph is also exact:

```text
declared LOCAL-SHADOW contract only;
no equality of stationary families across A7 branches;
no S_(w,epsilon) family;
no branch computation, binding, or selection;
ZERO and IDENTITY remain carried through later period machinery. (K3-2)
```

Its direct consumers genuinely re-walk:

| Consumer | Result |
|---|---|
| Lead `A7_BRANCH` field | **PASS** — displayed separately from the ratified four fields. |
| V1-6 fork | **PASS** — TYPE-U fork withdrawn at local-contract scope. |
| V1-8 sensitivity | **PASS at K3 scope** — “per A7 branch” withdrawn locally and retained for the later period route. |
| V4-3 local row | **PASS** — local vacuity is displayed and omission forbidden. |
| V4-3 both-branches-computable row | **PASS** — re-scoped to later period machinery with no aggregate verdict. |

But `REV` required **both** former branch rows to become period-route
conditionals:

```text
V4-3's “both branches computable” and “one branch exits” rows
  := period-route conditional rules.                              (K3-S)
```

V002 says in prose that both rows are retained, but it displays no
one-branch-exits disposition. The missing row is:

```text
LATER PERIOD MACHINERY / ONE BRANCH EXITS THE CERTIFIED LATTICE:
  that branch records OUT_OF_LATTICE;
  the other branch reports normally;
  the pair is still reported as a pair;
  neither branch is selected, averaged, merged, or dropped.       (K3-R)
```

The display standard makes a prose “retained” assertion insufficient.

`K3 = FAIL_ON_FORCED_REWALK (+missing period one-branch-exit row)`.

### 1.4 K4 — the five six-cell surfaces

All five surfaces named by `REV` are correctly re-keyed:

| # | Required surface | V002 landing | Verdict |
|---:|---|---|---|
| 1 | V1-3 | Displays the Cartesian `3 x 2`, enumerates cells 1–6, states `CELLS=six_of_record`, and withdraws the mismatch. | **PASS** |
| 2 | Gate-map row 4 | Requires gate 3 plus the governing six-cell identity; the unresolved-count gate is gone. | **PASS** |
| 3 | V4-1 | Retains the four lawful disposition rows and deletes the fifth unresolved-count stop. | **PASS** |
| 4 | V5-5 | Records C1 consumed and the old “not harmonized” verb withdrawn. | **PASS** |
| 5 | Final handoff | Removes the unresolved count handoff and states both handed questions resolved against sealed text. | **PASS** |

No live V002 consumer still asks for an eight-cell decision. Mentions of the old
count are corrective history. Cell 4 keeps both threshold dispositions; polar
`chi_K` remains outside the finite lattice.

`K4 = PASS_5_OF_5`.

## 2. Y2 — bounded-delta and confirmed-content audit

### 2.1 The claim under test

V002 makes three universal claims:

```text
CHANGED   = K1 lead provenance; K2 gate row 2; K3 V1-6 and dependents;
            five K4 surfaces;
UNCHANGED = every other clause of V001, carried verbatim;
DELTA     = bounded; no clause outside the delta board was altered. (D-1)
```

[PROVABLE] `(D-1)` is false both literally and substantively. The result does
not rest on line-count churn; the following named non-delta clauses disappear or
lose load-bearing content.

### 2.2 Exact non-delta witnesses

#### Witness U1 — modulus witness definitions removed

V1 explicitly displayed:

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

V2's V1-2 says “carried verbatim” but retains only the two witness names and the
generic alternate-metric label. It deletes the witness conditions and the exact
failure statement in `(U1-V1)`. K1–K4 do not authorize that deletion.

#### Witness U2 — independent sensitivity limitation shortened away

V1 required both:

```text
(M5) is not repaired by sensitivity alone;
Task-6 sensitivity cannot itself supply the missing preselection
measurement-metadata bridge.                                    (U2-V1)
```

V2 retains the first sentence but omits the independent bridge limitation while
calling V1-8 carried verbatim. K3 requires only the local/period branch re-scope;
it does not authorize deletion of `(U2-V1)`.

#### Witness U3 — permanent anti-tuning regression removed

V1's anti-tuning ledger carried:

```text
infer nonvanishing from cycle presence | no seed outcome inferred | clean.
                                                                    (U3-V1)
```

V2 removes `(U3-V1)`. It also drops the explicit sealed provenance sentence for
the cross-sector-unit row. Adding the new K2 custody/entrance row and a K4 cell
row does not preserve the removed permanent regression.

#### Witness U4 — prior dependency audit replaced, not extended

V1 re-walked these confirmed inputs:

```text
A32 ratification;
A2 Arm A adoption;
(M5a-V002) conjuncts;
the authoritative 11-node graph;
witness certification section II.                              (U4-V1)
```

V2 replaces that table with the K1–K4 re-walk. The new table is required, but it
must be appended to `(U4-V1)`, not used to delete it. The assertion that every
other V001 clause is unchanged is therefore refuted by direct exhibition.

#### Witness U5 — nine-row not-computed guards compressed

V2 retains the nine row labels but deletes confirmed qualifications, including:

```text
J-II (L0) is not supplied by A32;
no new-cycle comparison is inferred from a rank-preserving square;
neither S28 nor its negation is assumed;
R9 is a falsifier, not a constructor, and no common cell is formed. (U5-V1)
```

Those are guard content, not typography. Calling the shortened V3 “carried
verbatim from V001” is false.

### 2.3 Delta determination

Any one of U1–U5 refutes the universal unchanged/verbatim claim. U1, U2, U3,
and U5 additionally show that confirmed operational guards are no longer
present in the superseding declaration. Therefore:

```text
DELTA_BOUNDED          = false;
V001_CONTENT_INTACT    = false;
V2_VERBATIM_CLAIMS     = false;
V2_VERB_AUDIT          = not_clean.                              (D-2)
```

The bounded repair is not to paraphrase the omissions again. It is:

```text
start from sealed V1;
apply K1--K4 and only their displayed direct-consumer edits;
append the K1--K4 dependency re-audit to the prior dependency audit;
retain every other V1 clause and row verbatim;
add K2-R and K3-R above.                                         (D-R)
```

## 3. Y3 — fresh attack and verb audit

### 3.1 Fresh attack — downstream custody laundering

The fresh attack targets row 8, not the corrected row 2. Use the purely
structural valuation:

```text
ALPHA-RESULT-SEAL and its four parents = certified;
separate numeric act                  = licensed;
gate 7 / symbolic assembly            = false.                  (F-1)
```

No displayed implication from `ALPHA-RESULT-SEAL` and its four parents forces
gate 7: the alpha stop has no extra numeric-payload conjunct, and V002 row 8
does not name gate 7. Its literal prerequisite column therefore admits the
numeric act under `(F-1)`, while V1-10a separately forbids that act until the
symbolic assembly has run with `K_*` established and `nu` symbolic. The attack
exhibits an internal gate-table inconsistency, not a valuation satisfying every
V002 clause.

Thus:

```text
row8_prerequisites(F-1) = true;
symbolic_first(F-1)     = false;

FRESH_ATTACK = FIRES / NUMERIC_ACT_BYPASSES_GATE7.              (F-2)
```

`(F-1)` is a countermodel to row 8's rendered prerequisite sufficiency. It sets
no real gate, forms no seal, binds no member, and computes no value.

### 3.2 Surface and fence check

| Surface | Result |
|---|---|
| Four-field LOCAL-SHADOW subject | Preserved; no promotion. |
| Local contact contract | Vacuity proven at contract scope only; A7 globally undecided. |
| Six-cell lattice | Correct and complete at 6 cells. |
| Mathematical chain | Row 2 repaired; row 8 must additionally inherit gate 7. |
| A32 rails | No token inferred true; M5a remains false. |
| Reader/fixed point/end test | None consumed or executed. |
| Numbers/comparison | None formed or accessed. |
| Cross-sector unit | No bridge or implicit unit introduced by this confirm. |

`MACHINERY-APPEAL = none`.

### 3.3 Self verb audit

| Verb | Required witness | Audit |
|---|---|---|
| `PASS` | K1 direct comparison; K2 row 2; K3 core; K4 five-surface table | **CLEAN** |
| `FAIL` / `DEFECTIVE` | row-8 countermodel, missing K3-R display, U1–U5 | **CLEAN** |
| `verbatim` | Used only where the compared text/meaning is actually displayed; V2's contrary claims are quoted as claims under test. | **CLEAN** |
| `content not intact` | At least U1–U5, with four operational guards identified | **CLEAN** |
| `not ready` | D1–D3 remain and M5a is independently false of record | **CLEAN** |
| `fresh attack fires` | `(F-1)`–`(F-2)` give the explicit structural countermodel | **CLEAN** |

No draft is called adopted, no review is called a ruling, and no false gate is
called open.

## Final board

```text
REGISTER_HEAD_AT_PREFLIGHT       = Q-543
K1                               = PASS
K2_DIRECT                        = PASS
K2_FORCED_REWALK                 = FAIL_ROW8
K3_CORE                          = PASS
K3_FORCED_REWALK                 = FAIL_MISSING_PERIOD_EXIT_ROW
K4                               = PASS_5_OF_5
DELTA_BOUNDED                    = false
V001_CONFIRMED_CONTENT_INTACT    = false
FRESH_ATTACK                     = FIRES_ON_ROW8
M5A_SUBGATE                      = false_of_record
alpha_computed                   = false
proof_authorized                 = false
kappa_record_computed            = false
MEMBER_BOUND                     = false
NUMERIC_EVALUATION               = false
MEASURED_CONSTANT_COMPARISON     = none
MACHINERY_APPEAL                 = none
```

DOR_V002 = DEFECTIVE (+K2 row-8 propagation bypass; +K3 missing period one-branch-exit display; +UNBOUNDED_DELTA/V001 confirmed-content omissions)
RULING_READY_PENDING_SUBGATE = no
VERB_AUDIT_SELF = CLEAN
