# STAGE 8 / TASK 6 / STEP 2 — RE-CONFIRM OF THE EVALUATION DoR V003 UNDER C-V3

Lane: Codex Lane 3 (SOL, high effort)  
Date: 2026-08-06  
Register citation: living entry Q-545; the preflight head was Q-545  
Custody: mechanical re-confirmation; no adoption, ruling, or execution

## Lead verdict

```text
DOR_V003
  = DEFECTIVE (+2 C-V3 items)

C1  FULL-BLOCK CARRIAGE FAILS:
    the confirm-targeted D1, D2, and U1-U5 payloads are present, but V001
    clause blocks are not reproduced in full; the fresh witness is the
    omitted CARRIED-CONDITIONAL period cure requiring a formed period route
    and a true d^per modulus certificate;

C2  CHANGE ENUMERATION FAILS:
    the V002->V003 mechanical diff contains substantive clause edits outside
    D1, D2, and U1-U5, including deletion of V1-6's residual A7 rule for later
    period machinery from that clause block (the matching V4-3 disposition
    remains), a shortened exact-arithmetic precondition, and a deleted
    type-erasure rationale.

RULING_READY_PENDING_SUBGATE = no.
```

The supplied repair targets themselves pass:

```text
D1_ROW8                         = PASS
F1_COUNTERMODEL                = CLOSED_BY_TWO_PROHIBITIONS
D2_PERIOD_EXIT_ROW             = PASS
U1_U5_CONFIRM_TARGETS          = RESTORED_5_OF_5
U3_REGRESSION_AND_PROVENANCE   = PRESENT
U5_FOUR_NAMED_QUALIFICATIONS   = PRESENT
C_V3_FULL_BLOCKS               = FAIL
C_V3_ENUMERATION               = FAIL
```

The distinction is load-bearing: restoration of the seven named targets does
not prove the universal carriage rule. A single uncarried clause or unenumerated
change refutes C-V3 mechanically.

Protected state remains:

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

## 0. Preflight, authorities, and mechanical method

### 0.1 Preflight

| Check | Result |
|---|---|
| STEP 0 access | **PASS** — cleanroom, archive workspace, and supervision roots are readable. |
| Living register | **PASS** — Q-545 was terminal at preflight. Q-545 records V003 and locks C-V3 into process; the live-append clause requires no stop. |
| Artifact under review | **PASS** — `STAGE8_TASK6_EVALUATION_DOR_DARIO_V003.md`, SHA-256 `da5b03e151bc1b391ba1c666b3c3500f3f474461d4f1e669184ad09ce905b913`, verified against its adjacent seal before reading. |
| Supplying confirm | **PASS** — `STAGE8_TASK6_DOR_V002_CONFIRM_LANE3_V001.md`, SHA-256 `93b516c57bd18ded9a52455c6272b5f5e9aebdea0b6d39e716b2add681fed192`, verified against its adjacent seal before reading. |
| Base texts | **PASS** — V001 and V002 verified against their adjacent seals before mechanical comparison. |
| Output collision | **PASS** — this artifact and sidecar were absent from both the cleanroom and archive workspace before creation. |
| Fences | **PASS** — textual comparison requires no protected operation. |

### 0.2 Sealed comparison set

| Key | Source and SHA-256 | Mechanical use |
|---|---|---|
| `V3` | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V003.md` — `da5b03e151bc1b391ba1c666b3c3500f3f474461d4f1e669184ad09ce905b913` | Subject under review. |
| `V2` | `STAGE8_TASK6_EVALUATION_DOR_DARIO_V002.md` — `1f4834e67eb9f3819b26ea0339f10ec8dc7fdd649117ffa65af6ca58ac905ae4` | Immediate predecessor for change enumeration. |
| `V1` | `STAGE8_TASK6_EVALUATION_DOR_DRAFT_DARIO_V001.md` — `9704f27355ec97f447c23e180d0e52f1177b7bd713773c347061d8fe1b1616d8` | Base clause blocks for carriage comparison. |
| `CONF` | `STAGE8_TASK6_DOR_V002_CONFIRM_LANE3_V001.md` — `93b516c57bd18ded9a52455c6272b5f5e9aebdea0b6d39e716b2add681fed192` | D1, D2, U1–U5 targets and exact repair displays. |
| `CHAIN` | `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md` — `1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a` | Cumulative inheritance and local `d_w` modulus conditions. |
| `A32` | `STAGE8_TASK6_A32_PREP_LANE3_V002.md` — `c5d1090b1ec1862c59c1281845c9ad74d0b143e9a57f195c099adb16e56ae4ea` | Alpha-stop parents and lack of an implied gate-7 conjunct. |
| `M5A` | `STAGE8_TASK6_M5A_STATUS_LANE3_V001.md` — `bcb8cced0a2d8a02083522623f12c838e9ea0035cf2f0d989f9d0b3dd21326a7` | Subgate remains false of record. |
| `C1` | `CHAIN_V004_CORRIGENDUM_C1_2026-08-06.md` — `cffbfce332c4e1b5ecd2e7e7c6b98db38331113875faba3f79a4aeedcf0afc39` | Six-cell law retained unchanged. |

### 0.3 C-V3 test protocol

The locked rule in Q-545 and V003 states:

```text
Clause BLOCKS from V001 are reproduced in full.
Every change is enumerated individually.
No summary sentence asserts carriage over a class of clauses.       (C-V3)
```

I tested its two universal claims separately:

1. `V1 -> V3`: compare each claimed restored block at line level and search for
   uncarried load-bearing clauses.
2. `V2 -> V3`: assign every substantive hunk to D1, D2, or U1–U5; version,
   task-number, preflight-head, and supersession metadata are not physics
   clauses and are excluded from the substantive-change verdict.

The raw mechanical sweep reports:

```text
V1 -> V3: 90 zero-context hunks; 295 added lines; 262 deleted lines.
V2 -> V3: 82 zero-context hunks; 205 added lines; 171 deleted lines. (M-1)
```

`(M-1)` is not itself a defect: required displays create legitimate churn. The
verdict uses exact substantive witnesses below, not the counts.

## 1. Z1 — the three fixes and five carriage witnesses

### 1.1 D1 — row 8 and the prior countermodel

V003 row 8 now displays the full conjunction supplied by `CONF`:

```text
NUMERIC ALPHA ACT MAY NOT BEGIN UNTIL
  gate 7
  + ALPHA-RESULT-SEAL
      with THOMSON-RESULT-SEAL,
           PARENT-COMPARISON,
           HOLDOUT-UNIVERSE-SEAL,
           PREDICTION-MAP-SEAL
      transitively certified
  + the separate licensed act.                                  (D1-1)
```

Rows 3–8 are now expressly in the inheritance chain. The anti-tuning ledger and
dependency tables carry the same requirement.

Rerun the old structural valuation:

```text
ALPHA-RESULT-SEAL and its four parents = certified;
separate numeric act                  = licensed;
gate 7 / symbolic assembly            = false.                  (F-1)
```

Under V003:

```text
row8_conjunction(F-1) = false, because gate 7 = false;
V1-10a_symbolic_first(F-1) = false;

therefore the numeric act is forbidden by the gate-table conjunction
AND independently forbidden by the symbolic-first clause.        (D1-2)
```

No custody-only bypass survives on `(F-1)`.

`D1 = PASS`; `F1_COUNTERMODEL = CLOSED_BY_TWO_PROHIBITIONS`.

### 1.2 D2 — one period branch exits

V003 displays, rather than merely references, the required period-only row:

```text
ROUTE   = later period machinery;
OUTCOME = one branch exits the certified lattice;

exiting branch -> OUT_OF_LATTICE;
other branch   -> reports normally;
pair           -> still reported as a pair;
neither branch -> selected, averaged, merged, or dropped.         (D2-1)
```

The local row remains `A7_BRANCH=VACUOUS_ON_LOCAL_ROUTE`, and the
both-branches-computable and schema-failure rows remain separately displayed.

The local contact determination is also carried by its displayed factor walk:

```text
LOCAL_CHAIN_FACTORS = {S_w, Schur_w, Pi_w, ell_w};
C_N^k is not a declared interface of LOCAL_CHAIN_FACTORS;
E_C,N is not a declared field or argument of any local factor;
LOCAL_CHAIN_E_C_CONSUMER_SEAM = none_of_record;

therefore, at the declared local-composite contract only,
CONTACT             = VACUOUS_PROVEN;
A7_BRANCH           = VACUOUS_ON_LOCAL_ROUTE.                    (D2-2)
```

`(D2-2)` asserts no cross-branch stationary-family equality, forms no
`S_(w,epsilon)`, and computes, chooses, or binds no branch. The `ZERO` and
`IDENTITY` branches remain carried for later period machinery.

`D2 = PASS`.

### 1.3 U1–U5 — confirm-target comparison

The five targets named by `CONF` are all present at their supplied semantic
scope:

| Witness | Required target | V003 line-level finding | Target verdict |
|---|---|---|---|
| U1 | Both modulus witness conditions plus the exact mismatch hazard | Both `DIFF_TO_METRIC` and `DIRECT_MODULUS` conditions are displayed; the true-`d_w` mismatch hazard is displayed. | **PASS** |
| U2 | `(M5)` limitation plus the independent preselection measurement-metadata bridge limitation | Both sentences are displayed together and branch sensitivity is still correctly re-scoped. | **PASS** |
| U3 | `infer nonvanishing from cycle presence -> no seed outcome inferred` and clause-8 cross-sector provenance | The regression row and provenance are both present. | **PASS** |
| U4 | The original five-row dependency audit retained, with the K1–K4 audit appended | Tables A and B are both displayed; Table C adds this relay's re-walk. | **PASS** |
| U5 | Four named guards: J-II/L0 not supplied by A32; no new-cycle inference from an RP square; neither S28 nor its negation; R9 falsifier/not constructor/no common cell | All four qualifications appear in the V3 table. | **PASS** |

```text
U1_U5_CONFIRM_TARGETS = RESTORED_5_OF_5.                       (U-1)
```

But `(U-1)` is not the universal C-V3 result. “Target present” and “the V001
clause block is reproduced in full” are different propositions.

### 1.4 Literal full-block comparison

V003's verb audit defines “restored in full” to mean **the V001 text is
reproduced, not summarized**. Mechanical comparison refutes that definition.

For U1, V001 says:

```text
a complete d_w lacking both witnesses can make sup|dot B_w|
disagree with the true d_w modulus — the alternate-complete-metric attack.
                                                                    (U1-V1)
```

V003 instead says:

```text
without either witness, sup|dot B_w| may disagree with the true d_w modulus.
                                                                    (U1-V3)
```

`(U1-V3)` restores the targeted hazard, but it is not the V001 line block: the
`complete d_w` scope, `can make` wording, and named attack are absent from that
display. Similar re-rendering occurs in U2 and U4.

U5 is more direct. The four target propositions are present, but the claimed
full V001 table block is not. Examples still absent from V003 include:

```text
J-II (L0) is a cross-sector arrow not supplied by A32;
no cycle-creating comparison is computed;
Slot 16 is re-posed, not discharged;
no step here inhabits A_RP+;
the full downstream anti-mistaking rationale.                    (U5-X)
```

Therefore:

```text
U1_U5_TARGET_PAYLOADS = pass_5_of_5;
U1_U5_FULL_V001_BLOCKS = not_reproduced_in_full.                 (U-2)
```

## 2. Z2 — C-V3 delta-board audit

### 2.1 Every enumerated item is genuine

| Delta row | Mechanical landing | Verdict |
|---|---|---|
| D1 | Row 8 adds gate 7; inheritance and anti-tuning consumers update. | **GENUINE** |
| D2 | Period one-branch-exit row added as a full display. | **GENUINE** |
| U1 | Modulus conditions and mismatch hazard added. | **GENUINE** |
| U2 | Independent measurement-metadata limitation added. | **GENUINE** |
| U3 | Nonvanishing regression and cross-sector provenance added. | **GENUINE** |
| U4 | Prior dependency table added before the K1–K4 table. | **GENUINE** |
| U5 | Four confirm-named V3 qualifications added. | **GENUINE** |

`ENUMERATED_CHANGES = GENUINE_7_OF_7`.

### 2.2 Nothing-unenumerated test

The second C-V3 leg fails. After excluding version/preflight metadata and the
seven listed repairs, the `V2 -> V3` diff retains substantive clause edits that
have no delta row:

| Witness | V002 clause | V003 result | Why unenumerated |
|---|---|---|---|
| E1 | V1-6's displayed residual A7 rule for later period machinery: if the prediction-map schema cannot carry both A7 branches, the gate is unresolved and no branch may be chosen. | The rule is deleted from V1-6. A matching V4-3 disposition survives, but the line-level clause block changed. | Not D1/D2/U1–U5; contradicts “K1–K4 unchanged.” |
| E2 | V1-9 states exact arithmetic is a **precondition on every numeric step, not a post-hoc audit**. | V1-9 is shortened to “a float-path result is not a value.” | Not U1 or any other listed row. |
| E3 | V2-3 explains why type preservation binds every gate: type erasure may occur at any handoff and the failure ladder is armed there. | The rationale is deleted; only the mapping row remains. | No delta item names V2-3. |
| E4 | K4's V4-1 consumer explicitly records that V001's count-stop is deleted and no ambiguity remains. | That dependent sentence is deleted. | K4 is claimed carried unchanged; D1/D2/U1–U5 do not name it. |
| E5 | V5-5 and the final declaration/gate/not-computed/disposition board carry the prior verb checks. | Those blocks are replaced wholesale by the V003 repair audit/summary. | The delta board does not enumerate the replaced rows individually. |

Any one of E1–E5 refutes `every change is enumerated individually`.

```text
C_V3_ENUMERATION = FAIL;
K1_K4_CARRIAGE_UNCHANGED = false_at_line_level.                  (E-1)
```

### 2.3 Full-carriage test: fresh unlisted V001 clause

Independent of the V2→V3 enumeration failures, the V1→V3 carriage sweep finds a
load-bearing clause outside U1–U5. V001's one-sided rider says:

```text
The cure is carried CARRIED-CONDITIONAL and requires
  a formed period route
  + the true d^per modulus certificate.                          (P-1)
```

V003's V1-5 ends after the polar/out-of-lattice/no-value rule. Mechanical search
finds no `CARRIED-CONDITIONAL` token and no `d^per` token anywhere in V003.
Neither D1, D2, nor U1–U5 enumerates V1-5.

Thus:

```text
C_V3_FULL_BLOCK_CARRIAGE = FAIL;
FRESH_CARRIAGE_WITNESS   = omitted_period_cure_P-1.              (P-2)
```

The required repair is exact and finite:

```text
restore (P-1) in V1-5;
enumerate that restoration in the delta board;
re-walk the one-sided rider, later period machinery,
type-preservation payload, and final carriage board;

then either:
  reproduce every claimed V001 clause block exactly and enumerate every
  V2->V3 clause edit,
or
  narrow C-V3's claim to the precisely listed target propositions and stop
  saying the V001 text is reproduced in full.                    (P-R)
```

## 3. Z3 — fresh attack, consequences, and verb audit

### 3.1 Fresh attack — remove the cure conditions

Assume a later reader consumes only V003. The reader sees:

```text
seed zero -> chi_K polar -> OUT_OF_LATTICE -> no local value.     (A-1)
```

Because `(P-1)` is absent, V003 does not itself carry:

```text
period cure is conditional;
period route must be formed;
d^per modulus certificate must be true.                           (A-2)
```

A consumer could therefore cite V003's one-sided rider while omitting one or
both cure prerequisites. This does not prove an unconditional cure, but it
removes **V003's displayed guard** against reporting one—the exact weakening
C-V3 exists to catch. The governing corpus guard remains in force.

```text
FRESH_ATTACK = FIRES / PERIOD_CURE_GUARD_NOT_CARRIED.             (A-3)
```

The attack is textual and structural. It forms no period route, checks no
certificate, evaluates no seed, and computes no value.

### 3.2 Consequence board

| Item | Re-confirm result |
|---|---|
| Row 8 | **PASS** — custody and gate-7 mathematics both required. |
| Old F-1 attack | **CLOSED TWICE** — row-8 conjunction and symbolic-first clause. |
| Period one-branch exit | **PASS** — pair carriage and no merge displayed. |
| U1–U5 named targets | **PASS 5/5**. |
| C-V3 full-block promise | **FAIL** — U blocks re-rendered and P-1 omitted. |
| C-V3 enumeration promise | **FAIL** — E1–E5 are unlisted substantive edits. |
| M5a | Still `false_of_record`; independent of this carriage failure. |
| Ruling readiness | **NO** — the DoR does not yet satisfy locked process. |

### 3.3 Surface, fences, and self verb audit

| Surface | Audit |
|---|---|
| LOCAL-SHADOW type | Preserved; no promotion. |
| A7 local/period split | Local vacuity and later two-branch carriage remain correctly typed. |
| Six-cell lattice | Preserved at six cells. |
| Row-8 numeric gate | Corrected; no execution performed. |
| Reader/fixed point/end test | None consumed or executed. |
| Cross-sector unit | No bridge or silent unit introduced. |
| Numeric or measured data | None formed or accessed. |

`MACHINERY-APPEAL = none`.

| My verb | Required display | Result |
|---|---|---|
| `PASS` | D1/D2 displays and U1–U5 target table | **CLEAN** |
| `FAIL` / `DEFECTIVE` | U-2, E1–E5, and P-1/P-2 | **CLEAN** |
| `mechanical` | Zero-context hunk counts plus line-level named witnesses | **CLEAN** |
| `restored target` | Used only for the five named target propositions, not universal block identity | **CLEAN** |
| `not ready` | Locked C-V3 fails and M5a remains false | **CLEAN** |
| `fresh attack fires` | A-1 through A-3 display the missing guard and consequence | **CLEAN** |

No draft is called adopted, no process failure is called a mathematical
refutation, and no gate is called open.

## Final board

```text
REGISTER_HEAD_AT_PREFLIGHT       = Q-545
D1_ROW8                          = PASS
F1_COUNTERMODEL                 = CLOSED_BY_TWO_PROHIBITIONS
D2_PERIOD_EXIT_ROW              = PASS
CONTACT_LOCAL_ROUTE             = VACUOUS_PROVEN (local contract only)
A7_PERIOD_CARRIAGE              = ZERO_AND_IDENTITY_RETAINED
U1_U5_CONFIRM_TARGETS           = RESTORED_5_OF_5
U3_REGRESSION_AND_PROVENANCE    = PRESENT
U5_FOUR_NAMED_QUALIFICATIONS    = PRESENT
ENUMERATED_CHANGES              = GENUINE_7_OF_7
C_V3_FULL_BLOCK_CARRIAGE        = FAIL
C_V3_CHANGE_ENUMERATION         = FAIL
FRESH_ATTACK                    = FIRES_ON_PERIOD_CURE_CARRIAGE
M5A_SUBGATE                     = false_of_record
alpha_computed                  = false
proof_authorized                = false
kappa_record_computed            = false
MEMBER_BOUND                    = false
NUMERIC_EVALUATION              = false
MEASURED_CONSTANT_COMPARISON    = none
MACHINERY_APPEAL                = none
```

DOR_V003 = DEFECTIVE (+C-V3 full-block carriage failure: omitted conditional period cure; +C-V3 unenumerated substantive edits)
RULING_READY_PENDING_SUBGATE = no
VERB_AUDIT_SELF = CLEAN
