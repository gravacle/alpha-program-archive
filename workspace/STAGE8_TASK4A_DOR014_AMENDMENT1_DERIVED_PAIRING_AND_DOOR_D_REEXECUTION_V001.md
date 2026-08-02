# Stage 8 Task 4a DoR-014 Amendment 1 Derived Pairing and Door-D Re-execution V001

Date: 2026-08-02  
Task: PASTE 384 / Task 4a  
Lane: CODEX LANE 2  
Status: **DOOR D REMAINS FAILED: THE SAME-CORRELATOR SUBTEST PASSES, BUT THE AMENDED GERM FAILS THE RATIFIED U1 REALITY DOMAIN**

Premise-dependent positives are marked:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013,
                   DoR-014 as amended, DoR-015
```

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead verdict

**The derived tensor cures exactly the Q-300/Q-301 source-port mismatch, on
cycles and endpoint-covariant open paths alike. Door D nevertheless does not
pass, because the same tensor has the wrong sign under the ratified
anti-linear U1 source involution.**

At a fixed character, the mandated replacement

```text
b(f,h)=i hbar L(f)L(h)
```

gives identically

```text
D_J Abar[f,h]=(i/hbar)G(f,h)
```

for every admitted pair. In particular:

* on the square cycle, `L(c_square)=0` now forces both sides to zero;
* on two distinct endpoint-covariant edge directions, the previously absent
  cross-cell term is exactly present and the identity holds.

But the raw-map domain separately requires the fixed CTP reality involution
(`STAGE8_RAW_CORRELATOR...:655-670`). Under the sealed relation

```text
L_(-n)(Theta_J f)=conjugate(L_n(f)),
```

the required pairing obeys

```text
b_(-n)(Theta_J f,Theta_J h)=-conjugate(b_n(f,h)),
```

whereas the v004 germ requires the plus sign in order that its exponent and
`Z_inc` be U1-real. Nontrivial charge/flux directions make the discrepancy
nonzero. Thus the attempted v005 is outside Door D's domain conditions 3 and
7 even though condition 6 now passes.

```text
DOOR_D_SAME_CORRELATOR_IDENTITY = PASS
DOOR_D_CYCLE_SUBTEST = PASS
DOOR_D_ENDPOINT_COVARIANT_SUBTEST = PASS

DOOR_D_CTP_REALITY_DOMAIN = FAIL | TYPE-R
DOOR_D_EXECUTION = FAIL
DOR015_FREEZE_LIFTS = false | TYPE-R |
  test: Amendment 1 condition requires Door D to pass, not one subtest

LIFTED_PHYSICAL_CHAIN_EXECUTED = false | TYPE-C |
  constraint: no admissible amended physical germ/raw G enters the chain
PHYSICAL_RETHESS_P_CLEAN = NO_VERDICT
```

No alternative sign, involution, character rule, or raw identity is selected
or installed.

## 1. Preflight, roots, and currency

### 1.1 Object, version, inputs

```text
DOES THE OBJECT EXIST?
  The amendment and exact tensor candidate exist. The attempted v005 does
  not survive its mandatory U1 certificate.

IS THE VERSION CURRENT?
  Yes through register head Q-301 and DoR-014 Amendment 1 / C36.

ARE ITS INPUTS PRESENT?
  Yes for the tensor derivation and Door-D rerun. Their conjunction is
  inconsistent with the retained U1 reality clause.
```

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace  [mirror destination only]
```

Files read at source included:

1. `alpha_supervision/LOCKED_PROCESS.md`
2. `alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
3. `alpha_supervision/DECISION_OF_RECORD_014_SOURCE_GERM_PHYS_RATIFIED_2026-08-02_V001.md`
4. `alpha_supervision/DECISION_OF_RECORD_014_AMENDMENT_1_CB_DERIVED_PAIRING_2026-08-02_V001.md`
5. `alpha_supervision/DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md`
6. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md`
7. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V004.md`
8. `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V005.md` (the attempted successor emitted with this run)
9. `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md`
10. `STAGE8_TASK4A_P2_PHYSICAL_SOURCE_TOPOLOGY_AND_DIFFERENTIAL_CALCULUS_CONSTRUCTION_V002.md`
11. `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md`
12. `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md`
13. `STAGE8_TASK4A_RAW_G_RERUN_ON_RATIFIED_SIGNATURE_AND_DOOR_D_EXECUTION_V001.md`
14. `STAGE8_TASK4A_DOOR_D_FALSIFIER_CARRIER_AND_CHECK_DIAGNOSIS_V001.md`
15. `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md`
16. `STAGE8_FIELD_SIGNATURE_PHYS_V005_THIRD_PASS_ADVERSARIAL_REVIEW_DETERMINATION_V001.md`
17. `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md`
18. `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md`
19. `../primitive_record_cell_selection_principle_v004.md`

`a32_holdout/custodian_private/` was not entered.

### 1.3 Authority hashes

| Authority | SHA-256 |
|---|---|
| DoR-014 Amendment 1 | `8191feb4316ddeb08ef832b644c41847b31698224f6ab16b65dc1e1e2a574e56` |
| source germ v004 | `d4cdbb6623797df6accb7dc9b24134d179bfc8e8d039c585d5c91ae23255869e` |
| Q-300 Door-D execution | `bffd7ef240204232a957422d60ce164151131fdbb46433def7d943d21b915382` |
| Q-301 diagnosis | `b105a2c9f769c19bad420e4cbc71a23e4fcb5dcc4fc2365a825c331fad1eac97` |
| field signature v005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` |
| raw-map spec | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` |

All available sidecars above were checked against the artifacts before use.
The register SHA-256 at construction start was
`37858be7b6162da6fc8ec020342ce5badf8840d9385a3a05b7679418a436705c`.

### 1.4 Exclusions

```text
rank or family-member selection                    NOT PERFORMED
background or evaluation-point selection           NOT PERFORMED
physical inverse, response, or output evaluation   NOT PERFORMED
coupling, scale, root, or measured comparison       NOT PERFORMED
register, plan, tracker, git, commit, or push       NOT TOUCHED
```

## 2. What the amendment ordered

DoR-014 Amendment 1 (`:4-25`) does four exact things:

1. voids Choice C-B;
2. declares the replacement a requirement, not a choice;
3. requires `b:=i hbar L tensor L` with an explicit tensor precertificate;
4. keeps all old falsifiers and requires the unchanged Door-D rerun to pass
   before the DoR-015 freeze lifts.

Q-301 had already proved the pointwise equivalence (`:255-303`):

```text
D_J Abar=(i/hbar)G
iff
b=i hbar L tensor L.
```

The execution therefore has no coefficient, kernel, orientation, or source
member to choose.

## 3. Tensor construction and precertificate

### 3.1 Construction

On the ratified physical source carrier let

```text
ell_n:=L_n^Theta compose K_J^(-1),
b_n:=i hbar ell_n tensor ell_n.
```

The corresponding bilocal functional on the A6 trace-class symmetric source
is its canonical bounded/trace-class dual:

```text
Q_n^L(R):=<b_n,K_R(R)>_(Bil,S_1).
```

On finite rank-one sources,

```text
Q_n^L(f symtensor h)=i hbar ell_n(f)ell_n(h).        (D384-1)
```

### 3.2 Certificate table

| Certificate | Proof | Verdict |
|---|---|---|
| no new choice | coefficient and tensor are fixed by Q-301 iff reduction | **PASS** |
| boundedness | `|b(f,h)| <= |hbar| ||ell||^2 ||f|| ||h||` | **PASS / TYPE-P** |
| symmetry | scalar products commute, so `b(f,h)=b(h,f)` | **PASS** |
| quotient descent | a physical null `v` has `ell(v)=0`, hence both slots vanish | **PASS / TYPE-P** |
| W3 finite restriction | `b_N=i_NM^* b_M i_NM=i hbar ell_N tensor ell_N` | **PASS / TYPE-P** |
| trace-class duality | bounded `b` acts continuously on the A6 trace-class source | **PASS / TYPE-P** |
| finite-core determination | boundedness plus dense finite core gives unique extension | **PASS / TYPE-P** |
| tail creation | no nonzero form is killed by every finite corner | **ZERO / TYPE-R** |
| U1/CTP reality | exact sign comparison in Section 5 | **FAIL / TYPE-R** |

The W3 row uses restrictions as adjoints of isometric inclusions. No naive
edge truncation appears.

## 4. Door-D same-correlator re-execution

### 4.1 General exact calculation

At an arbitrary admitted local-germ point set

```text
q:=p exp(Xi)/Z.
```

With the amended tensor,

```text
D_J W[f]
  =-i hbar q L(f),

D_J Abar[f,h]
  =-i hbar q(1-q)L(f)L(h),

2D_R W[f symtensor h]
  =i hbar q b(f,h)
  =-hbar^2 q L(f)L(h),

Abar(f)Abar(h)
  =-hbar^2 q^2 L(f)L(h).
```

Therefore

```text
G(f,h)
 =2D_R W[f symtensor h]-Abar(f)Abar(h)
 =-hbar^2 q(1-q)L(f)L(h),                       (D384-2)

(i/hbar)G(f,h)
 =-i hbar q(1-q)L(f)L(h)
 =D_J Abar[f,h].                                 (D384-3)
```

This identity is tensorial and holds before quotient, projection, rank
choice, or evaluation.

### 4.2 Independently coded exact check

A separately coded coefficient check represented Gaussian-integer
coefficients of `q` and `q^2`. It returned:

```text
same_correlator coefficients:
  left  =(-i,+i)
  right =(-i,+i)
  PASS

cycle substitution:
  left  =(0,0)
  right =(0,0)
  PASS

U1 pairing coefficient:
  transformed =+i
  conjugated  =-i
  FAIL
```

No floating-point or physical value entered this check.

### 4.3 Closed-cycle arm

For the sealed generator

```text
c_square=e_a0-e_0b+e_ab-e_ba,
L(c_square)=0,
```

the amended tensor gives

```text
b(c_square,c_square)=0,
D_J Abar[c_square,c_square]=0,
G[c_square,c_square]=0.
```

Thus the Q-300 cycle mismatch is removed without excluding the cycle.

```text
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
C_SQUARE_EXCLUDED_FROM_SOURCE_FAMILY = false | TYPE-R |
  test: the complete ratified cycle family is unchanged
```

### 4.4 Endpoint-covariant open-path arm

For distinct admitted directions `e_1,e_2`, the void C-B had
`b_old(e_1,e_2)=0` while `L(e_1)L(e_2)` was nonzero. The amended tensor gives

```text
b_new(e_1,e_2)=i hbar L(e_1)L(e_2),
```

so (D384-3) holds exactly. This is an equivariant tensor statement; no open
path is promoted to a scalar quotient coordinate.

```text
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = PASS
OPEN_PATH_SCALARIZATION_ADDED = false | TYPE-R |
  test: endpoint-covariant carrier and full torsor family retained
```

## 5. Door-D domain failure under U1 reality

### 5.1 Fixed source involution

U1_008 defines anti-linear maps (`...U1_DOR008...:244-264`) and admits only
the symmetric, `Theta_R`-real bilocal source domain (`:322-347,515-528`). The
v004 germ uses

```text
L_(-n)(Theta_J f)=conjugate(L_n(f)),
Q_(-n)(Theta_R R)=conjugate(Q_n(R)),                 (D384-4)
```

so its exponent satisfies the required reality relation.

### 5.2 Exact contradiction

For `R=f symtensor h`, the mandated tensor instead yields

```text
Q_(-n)^L(Theta_R R)
  =i hbar conjugate(L_n(f))conjugate(L_n(h)),

conjugate(Q_n^L(R))
  =-i hbar conjugate(L_n(f))conjugate(L_n(h)).       (D384-5)
```

Nontrivial charge/flux access ensures an admitted pair with nonzero product.
Thus (D384-4) and (D384-5) are incompatible. Equivalently, the two
requirements force `L tensor L=0`, contradicting the retained nontrivial
linear source.

```text
TENSOR_REQUIREMENT_AND_U1_REALITY_JOINTLY_SATISFIABLE = false | TYPE-R |
  hypotheses: current Theta_J/Theta_R, nontrivial L, exact i hbar tensor

AMENDED_GERM_D3_REAL = false | TYPE-R
RAW_MAP_DOMAIN_CONDITION_3 = FAIL | TYPE-R
RAW_MAP_DOMAIN_CONDITION_7 = FAIL | TYPE-R
```

### 5.3 Door-D accounting

Door D requires all domain conditions, not a majority vote.

| Door-D check | Re-execution |
|---|---|
| trace-norm source transport | **PASS / inherited TYPE-P** |
| bounded bilinear extension | **PASS / TYPE-P** |
| connected-subtraction typing | **PASS / TYPE-P** |
| W3 adjoint restriction squares | **PASS / TYPE-P** |
| Q-243 `R=0` finite shadow | **PASS / TYPE-P** |
| same-correlator identity, cycles | **PASS** |
| same-correlator identity, open paths | **PASS** |
| U1/CTP physical source reality | **FAIL / TYPE-R** |
| physical raw-G domain admissibility | **FAIL / TYPE-R** |

The amendment condition at `:20-25` says the freeze lifts only when Door D
passes. It does not authorize disregarding another unchanged raw-domain
condition after condition 6 is repaired.

## 6. Restriction checks and Q-243/Q-279 standing

### 6.1 Q-243

At `R=0`, the amended bilocal term vanishes. The J-only amplitude, its
difference/difference Hessian, and the ordered mixed retarded zero are
unchanged. Q-243 is reproduced exactly.

```text
Q243_R0_FINITE_RESTRICTION = PASS | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014 as amended
```

### 6.2 Q-279

DoR-014 Amendment 1 explicitly voids the old C-B nonzero-`R` placement. The
old Q-279 rows containing `Q_delta^Theta` therefore cannot simultaneously be
required unchanged. The lawful check splits:

* every J-only and `R=0` row is exactly reproduced;
* every C-B-dependent nonzero-`R` row is superseded by the amended tensor and
  recomputed through (D384-1)-(D384-3);
* the amended rows commute under W3 adjoint finite corners;
* their U1-related pair fails (D384-5).

```text
Q279_J_ONLY_AND_R0_ROWS_REPRODUCED = PASS | TYPE-P
Q279_VOID_CB_ROWS_REPRODUCED_UNCHANGED = false | TYPE-S |
  scope: DoR-014 Amendment 1 expressly supersedes C-B
Q279_AMENDED_NONZERO_R_ROWS_RECOMPUTED = PASS_ALGEBRAICALLY
Q279_AMENDED_U1_RESTRICTION = FAIL | TYPE-R
```

This does not refute Q-279's historical computation. It prevents calling the
amended tuple a valid U1-real physical restriction.

## 7. Six-account operation ledger

| Operation | Kernel/null data | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| `L -> b=i hbar L tensor L` | `ker b` contains `ker L` in either slot | bounded rank-one symmetric forms | none | W3 adjoint square **PASS** | zero created tail | **PASS** |
| trace-dual `b -> Q_L` | annihilator of the rank-one form | continuous scalar bilocal functional | symmetric bilocal only | finite corners **PASS** | zero | **PASS** |
| scalar germ differentiation | standard `L/Q_L` kernels | bounded first and second derivatives | no common-source leg added | Q-243/amended-Q-279 **PASS** | `Tail_src=0` | **PASS at fixed n** |
| connected subtraction | combines the two rank-one terms into (D384-2) | bounded candidate raw form | remains difference/noise typed | finite corners **PASS** | zero | **PASS** |
| same-correlator identification | exact equality on all source pairs | one tensor-consistent candidate | none | cycles/open paths **PASS** | not a tail effect | **PASS** |
| U1 class formation | nontrivial tensor is anti-real rather than real | no admitted U1 physical germ/raw form | character/branch partner has wrong sign | finite U1 pair **FAIL** | not a tail effect | **FAIL / TYPE-R** |
| Keldysh ordered projection | DD/noise block is in the finite ordered projection kernel | finite ordered zero | no p-carrying transfer | Q-243 **PASS** | physical `Tail_R` not formed | finite shadow only |

No class formation is omitted. The failure occurs before physical inversion,
Schur reduction, or retarded extraction.

## 8. Lifted chain and p-trace

### 8.1 Maximal lawful chain

The amended calculation supplies a **fixed-character bounded candidate**:

```text
G_n(f,h)=-hbar^2 q_n(1-q_n)L_n(f)L_n(h).             (D384-6)
```

It does not supply one U1-real physical `G` across the required partner
sectors. Therefore the physical lift cannot accept it.

```text
FIXED_CHARACTER_BOUNDED_RAW_CANDIDATE_EXISTS = true | TYPE-P |
  premises: DoR-014 as amended, DoR-015
U1_REAL_PHYSICAL_RAW_G_EXISTS = false | TYPE-R
PHYSICAL_RAW_G_LIFT_EXECUTABLE = false | TYPE-C |
  constraint: source object fails its U1/CTP domain certificate
CONNECTED_SUBTRACTION_PHYSICAL_INSTANCE = false | TYPE-C |
  constraint: only the nonadmissible fixed-character candidate exists
PHYSICAL_INVERSE_EXECUTABLE = false | TYPE-C |
  constraints: no admissible raw G; measure, contour, boundary/contact,
               and common unbounded domains also remain unbuilt
PHYSICAL_RETHESS_INSTANCE_EXISTS = false | TYPE-C
```

Because Door D did not pass, Task 382 steps 3-5 are not resumed as physical
constructions. Reporting the fixed-character candidate is an accounting
boundary, not a downstream lift.

### 8.2 Symbolic p-content

At fixed character:

```text
common/common and ordered mixed candidate:  zero and p-free;
difference/difference raw candidate:         q(1-q)-weighted;
cycle directions in ker L:                   zero;
endpoint directions outside ker L:           q(1-q)-weighted;
Door-D tail:                                 zero.
```

The finite ordered retarded shadow remains zero and p-free. There is no
physical retarded image on which to certify cancellation or survival.

```text
P_ENTERS_FIXED_CHARACTER_DD_CANDIDATE = true [SYMBOLIC DEPENDENCE ONLY]
P_ENTERS_FINITE_ORDERED_RETARDED_SHADOW = false | TYPE-R |
  test: exact Q-243 projection
P_ENTERS_DOOR_D_TAIL = false | TYPE-R |
  test: finite-core-separated bounded class
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
P_SURVIVES_PHYSICAL_CONSUMER = NO_VERDICT
```

No symbolic rank ratio is evaluated.

## 9. Exact remaining-objects list

The new first station is not the inverse package. It is:

```text
U1_REAL_TENSOR_PAIRING_COMPATIBILITY_DISPOSITION := (
  one declared relationship among the fixed U1 source involution,
  the exact i hbar L tensor L requirement,
  the character transformation rule,
  and the raw same-correlator normalization,
  together with finite U1 and Door-D certificates
).
```

Under the current four clauses their conjunction is refuted. A replacement
object is `TYPE-U`, but the present failure is `TYPE-R`. At least one current
clause must be explicitly superseded; that is principal territory, not a lane
choice.

After such a disposition and cross-lane verification, the previously known
downstream list resumes:

1. physical inverse/Schur package (measure, contour, boundary/contact, common
   unbounded domains);
2. `STAT_BG_LIFT_FIBER` background map;
3. completed restriction and `Tail_R` accounting;
4. induced response;
5. consumer signature.

```text
NEXT_REQUIRED_OBJECT = U1_REAL_TENSOR_PAIRING_COMPATIBILITY_DISPOSITION
NEXT_REQUIRED_OBJECT_BUILT = false | TYPE-U |
  would-build: the package exactly specified above
PRINCIPAL_DISPOSITION_REQUIRED = true | TYPE-C |
  constraint: the ordered amendment and retained U1 clauses are inconsistent
```

## 10. Kill passes

### 10.1 No repair by stealth

No character-dependent sign, altered involution, modified branch metric,
restricted source family, or superseded raw identity is introduced. Each
would change more than the ordered C-B replacement.

### 10.2 No selection

The tensor identity is proved for the complete source family. `c_square` and
the open-path pair are pre-existing hostile witnesses, not selected physical
members. No anchor, torsor, endpoint frame, intertwiner, rank pair, cycle
basis, or background is chosen.

### 10.3 No unflagged completion

The only class act is the declared bounded tensor/trace-dual formation. Its
domain, topology, kernel, image, restriction square, and tail are in Sections
3 and 7. No weak-star, bidual, distributional, or nonseparating completion is
used.

### 10.4 Exact restriction discipline

All restrictions are adjoints of isometric inclusions and their bilinear
corners. No raw coordinate truncation is used.

## 11. Final typed ledger

```text
DOR014_AMENDMENT1_EXECUTED = true | TYPE-P |
  premises: DoR-014 as amended
DERIVED_PAIRING_BUILT = true | TYPE-P |
  premises: DoR-014 as amended
EXPLICIT_TENSOR_PRECERTIFICATE_BUILT = true | TYPE-P

DOOR_D_BOUNDED_EXTENSION = PASS
DOOR_D_RESTRICTION_NATURALITY = PASS
DOOR_D_CYCLE_SAME_CORRELATOR = PASS
DOOR_D_ENDPOINT_COVARIANT_SAME_CORRELATOR = PASS
DOOR_D_SAME_CORRELATOR_IDENTITY = PASS

DOOR_D_U1_REALITY = FAIL | TYPE-R
DOOR_D_PHYSICAL_RAW_G_ADMISSIBILITY = FAIL | TYPE-R
DOOR_D_EXECUTION = FAIL
DOR015_FREEZE_LIFTS = false | TYPE-R

SOURCE_GERM_PHYS_V005_VALID = false | TYPE-R
LIFTED_PHYSICAL_CHAIN_EXECUTED = false | TYPE-C |
  constraint: no admissible U1-real raw input

FINITE_ORDERED_RETARDED_SHADOW_P_CLEAN = true | TYPE-P
PHYSICAL_RETHESS_P_CLEAN = NO_VERDICT
BACKGROUND_AND_CONSUMPTION_ONLY_REMAIN = false | TYPE-R |
  test: U1-real source-pairing compatibility precedes both

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: complete amended source family and all hostile tests |
  exclusions: witnesses used only to test universal claims |
  fences: no-selection discipline |
  query: selected character, anchor, torsor, intertwiner, rank, cycle basis,
         background, or evaluation point

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: tensor, trace-dual, germ derivative, and Door-D acts |
  exclusions: unbuilt inverse/retarded classes |
  fences: Q-288 six-account discipline |
  query: unnamed limit, weak-star, bidual, distributional, nonseparating

REGISTER_HEAD_AT_START = Q-301 |
  register_sha256=37858be7b6162da6fc8ec020342ce5badf8840d9385a3a05b7679418a436705c
REGISTER_HEAD_AT_SEND_TIME = Q-301 |
  register_sha256=37858be7b6162da6fc8ec020342ce5badf8840d9385a3a05b7679418a436705c |
  later_bearing_entry_found=false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md after Q-301 |
  exclusions: DoR-014 Amendment 1 already consumed as governing authority |
  fences: send-time currency check |
  query: any later Door-D, C-B, tensor-pairing, or U1 disposition

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The result is symmetric. The principal's tensor is exactly the right repair
for Door D's same-correlator equation and exactly the wrong reality parity for
the still-ratified U1 source involution. The first fact cannot be promoted
while the second is ignored.
