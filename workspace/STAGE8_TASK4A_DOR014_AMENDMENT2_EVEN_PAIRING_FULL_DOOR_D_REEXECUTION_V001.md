# Stage 8 Task 4a DoR-014 Amendment 2 Even Pairing and Full Door-D Re-execution V001

Date: 2026-08-02  
Task: PASTE 386 / Task 4a  
Lane: CODEX LANE 2  
Status: **FULL DOOR D FAILS ON THE ENDPOINT-COVARIANT SAME-CORRELATOR SUBTEST**

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended (2), DoR-015

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead verdict

**Amendment 2 repairs the parity and breaks the normalization.** The even
pairing is bounded, quotient-compatible, W3-natural, and U1-real. It also
passes the cycle identity because the cycle witness lies in `ker L`. It fails
the same-correlator identity on every admitted endpoint-covariant pair with
nonzero `L(f)L(h)`.

The exact four-subtest result is:

| Subtest | Verdict |
|---|---|
| bounded extension | **PASS / TYPE-P** |
| same-correlator identity on cycles | **PASS** |
| same-correlator identity on endpoint-covariant open paths | **FAIL / TYPE-R** |
| U1 reality, `Q_(-n)(Theta_R R)=conjugate(Q_n(R))` | **PASS / TYPE-P** |

The failing residual is

```text
D_J Abar[f,h]-(i/hbar)G_even(f,h)
  =hbar q(1-i)L(f)L(h).                              (D386-1)
```

This is not an omitted factor in the write-up. The complete chain shows both
appearances of `i`: one from `W=-i hbar Log Z`, and one from Door D's
`(i/hbar)` prefactor. Their product changes the bilocal leading coefficient
to a real minus sign; it does not reproduce the imaginary coefficient of the
J-Hessian.

```text
DOOR_D_BOUNDED_EXTENSION = PASS
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = FAIL | TYPE-R
DOOR_D_U1_REALITY = PASS
DOOR_D_EXECUTION = FAIL
DOR015_FREEZE_LIFTS = false | TYPE-R

LIFTED_PHYSICAL_CHAIN_EXECUTED = false | TYPE-C |
  constraint: the full Door-D antecedent failed
PHYSICAL_RETHESS_P_CLEAN = NO_VERDICT
```

No alternate coefficient, source/output map, involution, character member,
or physical source restriction is chosen.

## 1. Preflight, scope, and currency

### 1.1 Three-line preflight

```text
DOES THE OBJECT EXIST?
  Amendment 2, the even tensor, and all Door-D inputs exist. The requested
  clean four-subtest object does not survive execution.

IS THE VERSION CURRENT?
  Yes through Q-303 and DoR-014 Amendment 2 / C37.

ARE ITS INPUTS PRESENT?
  Yes. No missing datum blocks the four exact subtests.
```

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace  [mirror destination only]
```

Files read at source:

1. `alpha_supervision/LOCKED_PROCESS.md`
2. `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `alpha_supervision/DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md`
4. `alpha_supervision/DECISION_OF_RECORD_014_AMENDMENT_1_CB_DERIVED_PAIRING_2026-08-02_V001.md`
5. `alpha_supervision/DECISION_OF_RECORD_014_AMENDMENT_2_EVEN_PAIRING_NORMALIZATION_2026-08-02_V001.md`
6. `alpha_supervision/DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md`
7. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md`
8. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V005.md`
9. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V006.md` (emitted with this run)
10. `STAGE8_TASK4A_RATIFIED_BILOCAL_INVOLUTION_REALITY_LAW_DETERMINATION_V001.md`
11. `STAGE8_TASK4A_RAW_G_RERUN_ON_RATIFIED_SIGNATURE_AND_DOOR_D_EXECUTION_V001.md`
12. `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md`
13. `STAGE8_TASK4A_DOR014_AMENDMENT1_DERIVED_PAIRING_AND_DOOR_D_REEXECUTION_V001.md`
14. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md`
15. `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md`
16. `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md`
17. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`
18. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
19. `STAGE8_FIELD_SIGNATURE_PHYS_V005_THIRD_PASS_ADVERSARIAL_REVIEW_DETERMINATION_V001.md`
20. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
21. `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md`
22. `../primitive_record_cell_selection_principle_v004.md`

`a32_holdout/custodian_private/` was not entered.

### 1.3 Exact authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| DoR-014 Amendment 2 | `460da8c34e8a33503c0a5737f1d94b7a68cbb31fe636cd74c49e59a493efc282` | corrected coefficient and four-subtest release condition |
| Q-303 parity determination | `323852e8835175c30d503f0383ef735405d8bc40a98109e09f5974e49c603c22` | source-even/output-odd parity proof |
| source germ v004 | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` | unchanged exponent and W calculus |
| attempted v005 | `b3b0a7d8f6694221a2857b0ed68fe295f2a99232cf1d6a2ba5f32d810c12f67e` | tensor machinery and previous parity failure |
| Amendment-1 Door D | `365db191e3867129a02b2216fcf10b5fc83f53b0a03cef590dfe0671c63588d9` | four-domain execution template |
| Q-300 Door D | `bffd7ef240204232a957422d60ce164151131fdbb46433def7d943d21b915382` | original bounded/restriction suite |
| Q-301 diagnosis | `b105a2c9f769c19bad420e4cbc71a23e4fcb5dcc4fc2365a825c331fad1eac97` | exact same-correlator iff reduction |
| field signature v005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | physical carrier and bilinear class |
| raw-map specification | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | unchanged raw identity and domain |

The register head at construction start was Q-303, SHA-256
`fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3`.

### 1.4 Exclusions

```text
rank or source-family member selection             NOT PERFORMED
background/evaluation-point selection              NOT PERFORMED
physical inverse or response evaluation            NOT PERFORMED
coupling, scale, root, or measured comparison      NOT PERFORMED
register, plan, tracker, git, commit, or push      NOT TOUCHED
```

## 2. Amendment-2 content and version relation

Amendment 2 (`:4-22`) supersedes only Amendment 1's coefficient:

```text
superseded: b_odd =i hbar L tensor L,
live:       b_even=  hbar L tensor L.
```

It explicitly retains:

```text
Xi=L(J)-(1/2)Q(R),
W=-i hbar Log Z,
G=2D_R W-Abar tensor Abar,
D_J Abar=(i/hbar)G,
```

and says the source/output identification is untouched. Therefore this run
does not insert an additional map or normalization between `b_even` and `Q`.

Q-303 proves the parity part: `b_even` is suitable for the exponent slot.
Q-301 independently proves the unchanged identity's coefficient condition.
The present execution tests whether those two statements combine; it does not
assume that the reviewer's proposed combination is valid.

## 3. Even tensor precertificate

Let

```text
ell_n:=L_n^Theta compose K_J^(-1),
b_n^even:=hbar ell_n tensor ell_n,
Q_n^even(R):=<b_n^even,K_R(R)>_(Bil,S_1).             (D386-2)
```

### 3.1 Certificate table

| Certificate | Proof | Verdict |
|---|---|---|
| derivation/no choice | exact Amendment-2 coefficient and existing `L` only | **PASS** |
| boundedness | `|b(f,h)|<=|hbar| ||ell||^2||f||||h||` | **PASS / TYPE-P** |
| symmetry | `ell(f)ell(h)=ell(h)ell(f)` | **PASS** |
| quotient descent | a physical source null lies in `ker ell` | **PASS / TYPE-P** |
| W3 adjoint naturality | `b_N=i_NM^*b_Mi_NM` | **PASS / TYPE-P** |
| trace-class source dual | A6 bounded/trace-class dual pairing | **PASS / TYPE-P** |
| finite-core determination | finite corners are dense and determine `b` | **PASS / TYPE-P** |
| created tail | none | **ZERO / TYPE-R** |
| Theta parity | Section 3.2 | **PASS / TYPE-P** |

### 3.2 Exact Theta-even proof

Using the sealed law

```text
L_(-n)(Theta_J f)=conjugate(L_n(f))
```

and real `hbar`,

```text
b_(-n)^even(Theta_J f,Theta_J h)
 =hbar conjugate(L_n(f))conjugate(L_n(h))
 =conjugate(b_n^even(f,h)).                           (D386-3)
```

By symmetric finite-rank density,

```text
Q_(-n)^even(Theta_R R)=conjugate(Q_n^even(R))
```

on the complete admitted source class.

```text
EVEN_TENSOR_PRECERTIFICATE = PASS
EVEN_TENSOR_THETA_EVEN = true | TYPE-P
AMENDMENT1_ODD_TENSOR_RETAINED = false | TYPE-R |
  test: exact Amendment-2 supersession
```

## 4. Full normalization bookkeeping

### 4.1 Stepwise differentiation

For

```text
Xi=L(J)-(1/2)Q_even(R),
Z=(1-p)+p exp(Xi),
q=p exp(Xi)/Z,
W=-i hbar Log Z,
```

the individual steps are:

```text
D_J Xi[f]=L(f),
D_R Xi[f symtensor h]=-(1/2)b_even(f,h),

D_J Log Z[f]=qL(f),
D_R Log Z[f symtensor h]=-(q/2)b_even(f,h),

Abar(f)=D_J W[f]=-i hbar qL(f),

D_J Abar[f,h]
 =-i hbar q(1-q)L(f)L(h).                            (D386-4)
```

The bilocal route gives:

```text
2D_R W[f symtensor h]
 =2(-i hbar)(-q/2)b_even(f,h)
 =i hbar q b_even(f,h)
 =i hbar^2 qL(f)L(h).                                (D386-5)
```

The connected subtraction is:

```text
Abar(f)Abar(h)
 =(-i hbar q)^2L(f)L(h)
 =-hbar^2q^2L(f)L(h),

G_even(f,h)
 =2D_R W-Abar(f)Abar(h)
 =i hbar^2qL(f)L(h)+hbar^2q^2L(f)L(h).               (D386-6)
```

Now apply the **separate** Door-D normalization:

```text
(i/hbar)G_even(f,h)
 =-hbar qL(f)L(h)+i hbar q^2L(f)L(h).                (D386-7)
```

Subtracting (D386-7) from (D386-4) gives (D386-1).

### 4.2 Why the W-convention does not supply the missing coefficient

The W-convention does supply an `i` in (D386-5). Door D then multiplies that
term by another `i` in (D386-7). The product is `-1`. In contrast, the
J-Hessian's leading term in (D386-4) retains `-i`. Therefore the claimed
normalization does not follow from W; it conflicts with the unchanged
identity.

The Q-301 exact reduction remains mechanically visible:

```text
D_J Abar=(i/hbar)G
iff
b=i hbar L tensor L.
```

Amendment 2 changes the left member of this iff without changing the right
identity or adding a source-to-output map.

### 4.3 Independent exact coefficient check

A separately coded Gaussian-integer polynomial check returned:

```text
even pairing:
  D_J Abar coefficients in (q,q^2) =(-i,+i),
  (i/hbar)G coefficients           =(-1,+i),
  residual                         =(1-i,0),
  PASS=false;

superseded odd control:
  left=(-i,+i), right=(-i,+i), PASS=true;

Theta-even source check:
  transformed=+1, conjugated=+1, PASS=true.
```

No floating-point value or physical parameter was used.

## 5. Four Door-D subtests

### 5.1 Subtest 1 — bounded extension

The source transport and A6 target are unchanged. `b_even` is a bounded
rank-one form; connected subtraction combines two bounded rank-one forms.
Thus

```text
G_even=hbar^2 q(i+q)L tensor L
```

is bounded on every admitted local-germ neighborhood.

```text
DOOR_D_BOUNDED_EXTENSION = PASS | TYPE-P |
  premises: DoR-014 as amended (2), DoR-015 A4/A6
```

### 5.2 Subtest 2 — closed cycles

For the sealed square cycle,

```text
c_square=e_a0-e_0b+e_ab-e_ba,
L(c_square)=0.
```

Consequently all terms in (D386-4)-(D386-7) vanish on
`(c_square,c_square)`. The cycle identity passes exactly.

```text
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
CYCLE_FAMILY_RESTRICTED_TO_FORCE_PASS = false | TYPE-R |
  test: the complete ratified cycle family is retained
```

This pass is not evidence for the normalization away from `ker L`.

### 5.3 Subtest 3 — endpoint-covariant open paths

Choose the already-admitted hostile pair of distinct edge directions
`e_1,e_2` with

```text
L(e_1)L(e_2)!=0.
```

The local nonzero `Log_0` germ, positive rank-family weights, and exponential
ensure `q` is nonzero on the admitted neighborhood. Equation (D386-1) then
has a nonzero right side. Therefore

```text
D_J Abar[e_1,e_2]!=(i/hbar)G_even(e_1,e_2).
```

No endpoint frame or scalarization is selected; the comparison is made as an
equivariant tensor identity.

```text
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = FAIL | TYPE-R
OPEN_PATH_NORMALIZATION_CLAIM = false | TYPE-R |
  test: exact residual D386-1
```

### 5.4 Subtest 4 — U1 reality

Equation (D386-3) proves the exact sealed law

```text
Q_(-n)(Theta_R R)=conjugate(Q_n(R))
```

for every finite-rank symmetric source and hence on the continuous
completion. Slot exchange remains the separate `tau_R`; no omitted swap is
used.

```text
DOOR_D_U1_REALITY = PASS | TYPE-P |
  premises: DoR-008, DoR-014 as amended (2)
```

### 5.5 Full verdict

Door D is conjunctive. Three passes and one exact failure are a failure.

```text
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,FAIL,PASS)
DOOR_D_EXECUTION = FAIL
DOR015_FREEZE_LIFTS = false | TYPE-R |
  test: Amendment-2 clean-pass condition not satisfied
```

## 6. Q-243/Q-279 restrictions

### 6.1 Unchanged finite authority

At `R=0`, Amendment 2 contributes nothing. The exact J-only amplitude,
J-Hessian, Keldysh rotation, and ordered mixed zero reproduce Q-243 and the
J-only/R-zero Q-279 rows.

```text
Q243_R0_RESTRICTION = PASS | TYPE-P
Q279_J_ONLY_AND_R0_RESTRICTIONS = PASS | TYPE-P
```

### 6.2 Pairing-dependent rows

The original same-cell C-B rows were voided by Q-300/Q-301. Amendment 1's odd
rows are superseded by Amendment 2. The live finite nonzero-`R` rows are
therefore recomputed from `Q_even`, not compared to a void coefficient:

```text
D_R W=(i hbar/2)q Q_even,
D_JD_R W=(i hbar/2)q(1-q)L tensor Q_even,
D_R^2W=-(i hbar/4)q(1-q)Q_even tensor Q_even,
```

with the sign/factor conventions inherited from the explicit differentiation
above. Each row commutes with W3 adjoint finite corners and is Theta-typed.

```text
Q279_HISTORICAL_CB_ROWS_REPRODUCED_UNCHANGED = false | TYPE-S |
  scope: C-B is void and both amendments are later specific authority
Q279_AMENDMENT2_ROWS_RECOMPUTED = PASS
Q279_AMENDMENT2_RESTRICTION_SQUARE = PASS
Q279_AMENDMENT2_THETA_PARITY = PASS
```

The finite square passes; its promotion to one physical raw correlator fails
only at Door D's condition 6.

## 7. Operation and class-formation accounting

| Operation | Kernel/null data | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| `L -> b_even` | `ker L` in either slot | bounded symmetric rank-one form | none | W3 adjoint **PASS** | zero | **PASS** |
| trace-dual `b_even -> Q_even` | annihilator of the rank-one form | continuous scalar bilocal functional | symmetric bilocal slot | finite corners **PASS** | zero | **PASS** |
| germ exponent and `Log_0` | usual `L/Q` kernels | norm-holomorphic scalar germ | source-even exponent to W-odd output | amended finite square **PASS** | `Tail_src=0` | **PASS** |
| J differentiation | `ker L` | odd rank-one J-Hessian | difference/noise block | Q-243 **PASS** | zero | **PASS** |
| bilocal differentiation | `ker Q_even` | bounded rank-one bilocal term | symmetric R to candidate raw form | amended Q-279 **PASS** | zero | **PASS** |
| connected subtraction | no extra kernel off `ker L` | `G_even=hbar^2q(i+q)L tensor L` | no common leg introduced | finite corners **PASS** | zero | **PASS as candidate** |
| same-correlator identification | cycle kernel passes; open nonkernel fails | no admissible full physical raw image | conflict precedes retarded transfer | cycle **PASS**, open **FAIL** | not a tail effect | **FAIL / TYPE-R** |
| U1 source class | non-real sources excluded as before | Theta-even admitted `Q_even` | no slot exchange | finite partner square **PASS** | zero | **PASS** |
| Keldysh ordered projection | DD/noise lies in finite ordered kernel | finite ordered zero | no p transfer | Q-243 **PASS** | physical `Tail_R` unformed | finite shadow only |

Every class act has a declared topology and finite square. No weak-star,
bidual, distributional, or nonseparating completion is used.

## 8. Lifted-chain standing and p-trace

### 8.1 What exists

The source germ supplies the bounded candidate

```text
G_even=hbar^2q(i+q)L tensor L.                       (D386-8)
```

It is not an admissible physical raw `G` because it disagrees with the J
definition on the open sector. Hence the physical lift does not receive an
input.

```text
BOUNDED_RAW_CANDIDATE_EXISTS = true | TYPE-P
ADMISSIBLE_PHYSICAL_RAW_G_EXISTS = false | TYPE-R
PHYSICAL_RAW_G_LIFT_EXECUTABLE = false | TYPE-C |
  constraint: Door-D condition 6 fails
PHYSICAL_TWO_SIDED_INVERSE_EXECUTABLE = false | TYPE-C |
  constraints: no admissible raw G; measure, contour, boundary/contact,
               and common unbounded domains remain unbuilt
PHYSICAL_RETHESS_INSTANCE_EXISTS = false | TYPE-C
```

The 382 continuation is therefore not run. Doing so would promote a failed
Door-D candidate.

### 8.2 Sector and p-content

```text
J common/common and ordered mixed block:  zero and p-free;
J difference/difference Hessian:           q(1-q)-weighted;
even bilocal raw candidate:                q(i+q)-weighted;
cycle directions in ker L:                 zero;
open directions outside ker L:             p-carrying and identity-mismatched;
Door-D tail:                               zero;
finite ordered retarded shadow:             zero and p-free.
```

Thus:

```text
P_ENTERS_BOUNDED_RAW_CANDIDATE = true [SYMBOLIC DEPENDENCE ONLY]
P_ENTERS_FINITE_ORDERED_RETARDED_SHADOW = false | TYPE-R |
  test: exact Q-243 projection
P_ENTERS_DOOR_D_TAIL = false | TYPE-R |
  test: finite-core-separated bounded class
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
P_SURVIVES_PHYSICAL_CONSUMER = NO_VERDICT
```

No rank ratio is evaluated.

## 9. Exact next object

The first unresolved object is now narrower than the Q-302 disposition:

```text
EVEN_SOURCE_TO_ODD_RAW_OUTPUT_NORMALIZATION_DISPOSITION := (
  an explicit decision whether the Theta-even exponent pairing and the
  Theta-odd raw output are directly identified or connected by a separate
  derived map,
  the exact coefficient/sign convention of that map,
  proof of D_J Abar=(i/hbar)G on the complete source family,
  the even source and odd output parity certificates,
  W3 finite restriction squares and the full Door-D rerun
).
```

The current direct-identification special case is refuted. Building a
separate map was Q-303's option Y4; Amendment 2 expressly left that
identification untouched, so this lane cannot add it.

After a successful disposition, the downstream list remains:

1. physical inverse/Schur package;
2. `STAT_BG_LIFT_FIBER` background map;
3. completed restriction and `Tail_R` accounting;
4. induced response;
5. consumer signature.

```text
NEXT_REQUIRED_OBJECT = EVEN_SOURCE_TO_ODD_RAW_OUTPUT_NORMALIZATION_DISPOSITION
NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U |
  would-build: the package exactly specified above
PRINCIPAL_DISPOSITION_REQUIRED = true | TYPE-C |
  constraint: Amendment-2 direct normalization failed its own Door-D test
```

## 10. Kill passes

### 10.1 No repair by insertion

No extra `i`, odd line, sesquilinear leg, altered involution, changed raw
identity, or source-to-output map is inserted. Any such step would exceed
Amendment 2 and require its own provenance and falsifier.

### 10.2 No selection

The full source, character, cycle, endpoint-torsor, anchor, and rank families
remain. The cycle and open directions are hostile witnesses for universal
claims, not selected physical outputs.

### 10.3 No unflagged completion

All constructions stop in the norm-continuous A4/A6 class. No inverse,
retarded class, background lift, weak-star completion, bidual, or physical
tail is formed.

### 10.4 No restriction substitution

Every finite restriction is the adjoint of an isometric inclusion or its
bilinear corner. Historical void C-B rows are not substituted for amended
rows, and amended rows are not back-labeled historical results.

## 11. Final typed ledger

```text
DOR014_AMENDMENT2_EXECUTED = true | TYPE-P
EVEN_PAIRING_BUILT = true | TYPE-P
EVEN_TENSOR_PRECERTIFICATE = PASS

DOOR_D_BOUNDED_EXTENSION = PASS
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = FAIL | TYPE-R
DOOR_D_U1_REALITY = PASS
DOOR_D_SUBTEST_VECTOR = (PASS,PASS,FAIL,PASS)
DOOR_D_EXECUTION = FAIL
DOR015_FREEZE_LIFTS = false | TYPE-R

SOURCE_GERM_INTERNAL_BATTERY_V006 = 11_PASS / 3_CONDITIONAL_TYPE_U / 0_FAIL
SOURCE_GERM_PHYS_V006_INSTALLED = false | TYPE-C |
  constraint: Door-D release certificate failed

BOUNDED_RAW_CANDIDATE_EXISTS = true | TYPE-P
ADMISSIBLE_PHYSICAL_RAW_G_EXISTS = false | TYPE-R
LIFTED_PHYSICAL_CHAIN_EXECUTED = false | TYPE-C

FINITE_ORDERED_RETARDED_SHADOW_P_CLEAN = true | TYPE-P
PHYSICAL_RETHESS_P_CLEAN = NO_VERDICT
BACKGROUND_AND_CONSUMPTION_ONLY_REMAIN = false | TYPE-R |
  test: source-to-output normalization precedes both

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: full amended source family and all four subtests |
  exclusions: witnesses used only to test universal claims |
  fences: no-selection discipline |
  query: selected character, rank, anchor, torsor, intertwiner, cycle,
         endpoint frame, background, or evaluation point

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: tensor, trace-dual, germ, and bounded candidate acts |
  exclusions: inverse/retarded/background classes not formed |
  fences: Q-288 six-account discipline |
  query: unnamed limit, weak-star, bidual, distributional, nonseparating

REGISTER_HEAD_AT_START = Q-303 |
  register_sha256=fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3
REGISTER_HEAD_AT_SEND_TIME = Q-303 |
  register_sha256=fb6aaad868bb109dbd0e67abd65ee34abb2bfe4b0a6a570c4c79eddb67d94bc3
LATER_BEARING_REGISTER_ENTRY_FOUND = false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md through Q-303 |
  exclusions: no later register row existed at send time |
  query: Amendment 2, even pairing, Door D, source germ v006

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The parity table and the normalization equation are both correct in their own
roles. Amendment 2 proves the even source tensor is admissible; execution
proves that tensor is not the unchanged raw-output tensor.
