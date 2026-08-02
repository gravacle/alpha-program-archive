# Stage 8 Task 4a Raw-G Rerun on the Ratified Signature and Door-D Execution V001

Date: 2026-08-02  
Task: PASTE 382 / Task 4a  
Lane: CODEX LANE 2  
Status: **DOOR D FAILS ON THE SAME-CORRELATOR IDENTITY; THE BOUNDED-EXTENSION SUBTEST ITSELF PASSES**

Premise-dependent positives are marked:

```text
TYPE-P | premises: DoR-008, DoR-009, DoR-013, DoR-014, DoR-015
```

```text
alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

## 0. Lead determination

**Door D fires. The failure is not the old unweighted-`T_cyl`
unboundedness: on the ratified A4/A6 topology the candidate raw bilinear
extends boundedly. It fails because the linear-source and bilocal-source
definitions do not describe the same connected correlator.**

The exact witness is already sealed and lies in the ratified physical response
family. On the composition-loop edge order, let

```text
c_square=(1,-1,1,-1) in ker(B_square^T).
```

The ratified germ's linear source covector is the accumulated difference
covector, while its bilocal source covector is the same-cell trace:

```text
L_n(c)=i n sum_e c_e,
Q_delta(R)=Tr(R_delta,delta).
```

Consequently, without evaluating any physical quantity,

```text
L_n(c_square)=0,
Q_delta(c_square tensor c_square)=||c_square||^2 !=0.
```

At every admitted local-germ point with symbolic nonzero `q`, this gives

```text
D_J W[c_square]=0,
D_J^2 W[c_square,c_square]=0,

2D_R W[c_square tensor c_square] !=0,
Abar[c_square]Abar[c_square]=0.
```

Hence the bilocal-source raw candidate satisfies

```text
G_R[c_square,c_square]
 =2D_R W[c_square tensor c_square]
  -Abar[c_square]Abar[c_square]
 !=0,
```

while the mandatory same-correlator identity would require

```text
D_J Abar[c_square,c_square]
 =(i/hbar)G_R[c_square,c_square].
```

Its left side is zero and its right side is nonzero. This is an exact finite
counterexample on the same physical carrier, source direction, branch
convention, and germ. It uses no selected cycle basis, background, rank member,
anchor, torsor member, or numerical value.

The seven frozen Door-D checks therefore split as follows:

| Door-D check | Execution |
|---|---|
| moving-support family | **PASS** in the ratified trace/bilinear codomain |
| trace-norm boundedness of `R -> U_B R U_B^*` | **PASS**; it is an isometry |
| A5-to-A6 quadratic-form continuity/closability | **PASS AS A BOUNDED FORM** |
| connected-subtraction typing | **PASS**; both terms lie in `Bil_phys` |
| adjoint restriction squares | **PASS** |
| Q-243/Q-279 finite tuple reproduction | **PASS COMPONENTWISE** |
| physical raw-`G` domain/admissibility | **FAIL / TYPE-R** on `c_square` |

Thus:

```text
RATIFIED_SIGNATURE_WEIGHTED_BILINEAR_EXTENDS_BOUNDEDLY = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014, DoR-015

DOOR_D_PHYSICAL_RAW_G_IMAGE_ADMISSIBLE = false | TYPE-R |
  test: exact c_square same-correlator mismatch

DOR015_STANDING_FALSIFIER_FIRED = true |
  authority: DoR-015:31-35

DOR015_DOWNSTREAM_PREMISE_USE_RELEASED = false | TYPE-C |
  constraint: the principal has not dispositioned the fired falsifier |
  release: principal records which premise/package is withdrawn or replaced
```

DoR-015 says Door D is judged in execution and voids on failure. This lane
does not edit that Decision of Record or the register. It reports that the
falsifier antecedent is discharged. Until the principal dispositions it, no
new downstream positive may use the full DoR-015 package as an unqualified
premise.

The failure does **not** refute Gate 4, the physical quotient, or cycle-current
separation. It localizes the incompatible joint use of:

1. DoR-014's C-B same-cell trace placement for `R`; and
2. DoR-015's promotion of the physical cycle source, bilocal source, field
   representation, and connected raw class.

The artifact reports the conflict and does not choose which premise to repair.

---

## 1. Preflight, roots, currency, and authorities

### 1.1 Currency

The settled-question register head at construction start was Q-299, with
SHA-256:

```text
5c11e0f257842bed7aeb28f082abc7d293f854dcc97b60df591223d4ae64aa05
```

DoR-015 is in force. It adopts V005, opens this exact rerun, and states that
Door D is the named open physical-image check, voiding on failure
(`DECISION_OF_RECORD_015...:4-35`).

### 1.2 Roots entered and exclusions

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/MB Work/alpha-program-archive/workspace   [mirror destination only]
```

```text
a32_holdout/custodian_private/                    NOT ENTERED
alpha/kappa/coupling/root/scale evaluation        NOT PERFORMED
rank-pair or family-member selection              NOT PERFORMED
measured-constant comparison                      NOT PERFORMED
register/plan/tracker/git/commit/push              NOT TOUCHED
```

### 1.3 Verified authorities

| Authority | SHA-256 | Load-bearing use |
|---|---|---|
| `DECISION_OF_RECORD_015_FIELD_SIGNATURE_PHYS_RATIFIED_2026-08-02_V001.md` | `617bd51a70860d2cfb2066640630ba37ec289d56255ebbe1433bc0dfcba0159d` | adoption, opening, and Door-D falsifier (`:4-37`) |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V005.md` | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | cycle carrier, A4/A6 domains, Door D, and finite restrictions (`:286-436,818-883`) |
| `STAGE8_FIELD_SIGNATURE_PHYS_V005_THIRD_PASS_ADVERSARIAL_REVIEW_DETERMINATION_V001.md` | `c2251ed0e903ef4a0841e4008c1da612a41c57ef6778eff42dea00629a9fc1b1` | W3 adjoint-restriction precision and ratification package |
| `STAGE8_FIELD_SIGNATURE_PHYS_ADOPTION_PROPOSAL_V002.md` | lineage authority retained by V005 | frozen seven-part post-ratification raw-`G` rerun (`:899-935`) |
| `STAGE8_SOURCE_GERM_PHYS_ADOPTION_PROPOSAL_V001.md` | live formulas retained through V004/DoR-014 | `L_n^Theta`, `Q_delta^Theta`, and `Xi_n` (`:260-306`) |
| `STAGE8_TASK4A_P4_PHYSICAL_LOG_GERM_ON_P2_CALCULUS_CONSTRUCTION_V001.md` | `b4c77ea948a02f3736fc824976f9ebd6381deff35f5c339a646739ea159725c5` | exact derivatives and explicit pre-Door warning (`:332-368`) |
| `STAGE8_TASK4A_FINITE_NONZERO_R_REFERENCE_EXACT_PROBE_SOURCE_COMPUTATION_V001.md` | `c7624d88aedaa0659755b5c566121b24c2ad0c29a0060daada43a31b22a6ddfb` | independent finite J/R derivative tuple (`:380-445`) |
| `STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md` | `5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79` | exact cycle witness (`:186-225`) |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | raw-`G` domain and same-correlator identity (`:639-673`) |
| `STAGE8_TASK4A_RAW_G_SOURCE_TO_PHYSICAL_FIELD_LIFT_CONSTRUCTION_AND_TCYL_VERDICT_V001.md` | pre-DoR-015 authority | old `T_cyl` no-go and port distinctions |

All listed sidecars available at source were verified before this execution.

### 1.4 Version and object distinctions

DoR-015 does not supersede the old unweighted-`T_cyl` no-go by contradiction.
It changes the target:

```text
old target: trace-class bilocal source -> T_cyl C-star/module observable;
new target: trace-class source -> transported physical trace class
            -> continuous scalar bilinear RawGClass^005.
```

The old map remains refuted. The new scalar-bilinear extension is tested here.
Likewise, Q-279's `R` source is a bilocal probe, not the common linear source;
Q-279 itself warned against name-matching them. The inconsistency arises only
when the two are promoted to the **same physical connected correlator**, as the
raw-map domain requires.

`p` below is the symbolic rank-family weight. No rank pair or value is selected.
No `kappa_record` is computed. Q-279's symbolic noise coefficient is never
identified with it.

---

## 2. Ratified transport and bounded-extension subtest

### 2.1 Source and target

V005 ratifies, through DoR-015:

```text
J_fin = directed union_N {u_c:c in ker(B_N^T)},
J_phys = completion in the retained transported source norm,

E_R,phys=S_1,sym(H_CTP),
Bil_phys=Bil_cont(J_phys x J_phys;C),
RawGClass=Bil_phys intersect D3-real symmetric forms.
```

The inherited A4 transport is:

```text
K_J(J)=U_B J,
K_R(R)=U_B R U_B^*.
```

On the ratified norm, `U_B` is isometric. Therefore unitary invariance of the
trace norm gives, exactly,

```text
||K_R(R)||_1=||R||_1.
```

The Q-287/Q-290 moving-support family is therefore harmless for Map 1: fixed
trace norm remains fixed trace norm. The prior blow-up occurred only after
mapping the source to products of unit-modulus `T_cyl` characters. That map is
not used by the ratified A6 target.

```text
DOOR_D_MAP1_TRACE_NORM_BOUNDED = true | TYPE-P |
  premises: DoR-015 A4
DOOR_D_MOVING_SUPPORT_TEST = PASS
OLD_UNWEIGHTED_TCYL_BILOCAL_EXTENSION_RESTORED = false | TYPE-R |
  test: Q-290 counterexample remains valid in its original codomain
```

### 2.2 Map 2 as a bounded form

Let `P_delta` denote the sealed difference/difference branch block. The
same-cell trace functional transported by `K_R` is represented on the Hilbert
source carrier by the symmetric form

```text
b_delta(f,h)=<P_delta f,h>_H.
```

Because the physical test space uses the transported `ell^1` norm and embeds
continuously into the Hilbert carrier,

```text
|b_delta(f,h)|
 <=||f||_H ||h||_H
 <=||f||_J ||h||_J.
```

The transported linear germ covector

```text
ell_phys := L_n^Theta compose K_J^(-1)
```

is bounded for the same reason the ratified P2 covector is bounded on `ell^1`.
Thus `ell_phys tensor ell_phys` is a bounded rank-one bilinear form.

At a germ point `s`, write symbolically

```text
q(s)=p exp(Xi(s))/Z(s).
```

The two source derivatives and connected subtraction land in the one A6 class:

```text
Abar_phys(f)=-i hbar q(s) ell_phys(f),

B_R,phys(f,h)=i hbar q(s)b_delta(f,h),

G_R,phys(f,h)
 =B_R,phys(f,h)-Abar_phys(f)Abar_phys(h).
```

Both summands are continuous bilinear forms. D3 reality follows from the
ratified U1 orbit symmetrization and branch involution. No measure, weak-star,
bidual, distributional, or nonseparating completion is invoked.

```text
DOOR_D_MAP2_BOUNDED_FORM_EXTENSION = true | TYPE-P |
  premises: DoR-014, DoR-015
CONNECTED_SUBTRACTION_WELL_TYPED_IN_A6 = true | TYPE-P |
  premises: DoR-015 A6
DOOR_D_BOUNDED_EXTENSION_SUBTEST = PASS
```

This pass is not yet the Door-D verdict. A bounded form must also satisfy the
raw-map domain, including agreement of the linear and bilocal connected
definitions.

---

## 3. Exact Door-D failure

### 3.1 The mandatory identity

The raw-map specification requires simultaneously:

```text
G=2D_R W-Abar tensor Abar,
D_J Abar=(i/hbar)G.
```

The second line is not optional normalization. It says that the independent
linear and symmetric-bilocal source ports produce one connected two-point
object. The specification states that an input lacking the relation is outside
the physical raw-to-retarded map (`STAGE8_RAW_CORRELATOR...:639-673`).

### 3.2 Frozen witness before output

The witness is not selected from a desired result. It was sealed before
DoR-015 and is V005's own surviving physical cycle:

```text
c_square=e_a0-e_0b+e_ab-e_ba,
B_square^T c_square=0.
```

Its coefficient sum vanishes structurally:

```text
sum_e (c_square)_e=0.
```

Its norm does not vanish because it is the generator of the nonzero
one-dimensional cycle space. Define the finite symmetric rank-one source

```text
R_square=c_square tensor c_square.
```

It is U1-real, trace class, physical after the Gate-4 quotient, and uses no
cycle-basis choice: one sealed witness is enough to falsify a universal domain
condition.

### 3.3 Two evaluations of the purported same correlator

The germ's exact formulas give:

```text
L_n^Theta(c_square)=0,
Q_delta^Theta(R_square)=||c_square||^2 !=0.
```

The U1 symmetrization changes neither statement: the first is zero and the
second is real and nonzero.

Using P4's exact derivative formulas,

```text
D_J W[c_square]=0,
D_J^2 W[c_square,c_square]=0.
```

Therefore:

```text
D_J Abar[c_square,c_square]=0.
```

For the bilocal port:

```text
2D_R W[R_square]
 =i hbar q(s)Q_delta^Theta(R_square) !=0.
```

Since `Abar[c_square]=0`, connected subtraction does not alter this witness:

```text
G_R,phys[c_square,c_square]
 =i hbar q(s)Q_delta^Theta(R_square) !=0.
```

Hence:

```text
D_J Abar[c_square,c_square]
 !=(i/hbar)G_R,phys[c_square,c_square].
```

No coefficient value is needed. The contradiction is zero versus nonzero.

### 3.4 Why this is a Door-D failure, not a missing-input `NO_VERDICT`

Before DoR-015, the three required objects were on different carriers, so the
same comparison was legitimately unexecutable. DoR-015 explicitly adopts:

* the physical cycle current and source norm;
* the source intertwiners;
* the field-coordinate representation;
* the symmetric bilocal source; and
* the continuous raw bilinear class.

The maps and both evaluations are now on the same ratified physical direction.
The witness is finite. No measure, inverse, stationary background, or
unbounded-domain choice is needed to compare the two finite continuous forms.
The raw-map specification says a certified mismatch on identical inputs is a
failure, whereas a merely absent datum would return `NO_VERDICT`.

```text
LINEAR_AND_BILOCAL_CONNECTED_DEFINITIONS_AGREE = false | TYPE-R |
  witness: c_square and R_square

PHYSICAL_RAW_G_DOMAIN_CONDITION_6 = FAIL | TYPE-R
DOOR_D_EXECUTION_VERDICT = FAIL
```

### 3.5 Q-279 restriction result

The completed construction restricts by **adjoints of isometric inclusions**,
not by naive truncation. For an inclusion `i_N:J_N->J_phys`, the bilinear
restriction is

```text
rho_G,N(G)(f,h)=G(i_N f,i_N h),
```

or equivalently the corresponding operator corner `i_N^* G i_N`. P2
derivative naturality then reproduces Q-279 componentwise:

```text
J_c blocks:                    zero;
J_delta first derivative:     omega-weighted;
R first derivative:           omega-weighted same-cell trace;
Jdelta/Jdelta Hessian:         noise-weighted ell_N tensor ell_N;
Jdelta/R and R/R blocks:       exact Q-279 forms;
ordered (delta,c) block:       zero and p-free.
```

The `c_square` test is part of that exact tuple:

```text
ell_square(c_square)=0,
Q_square(R_square)!=0.
```

Thus the restriction square **commutes** and reproduces Q-279; it is the
reproduced tuple that exposes the physical promotion failure. Q-279 is not
refuted. It expressly declined to identify its first `R` derivative with a
physical raw correlator. Door D is the later identification that fails.

```text
DOOR_D_ADJOINT_RESTRICTION_SQUARE = PASS | TYPE-P |
  premises: DoR-008, DoR-014, DoR-015
Q279_FULL_SOURCE_DERIVATIVE_TUPLE_REPRODUCED = PASS | TYPE-P |
  premises: same
Q279_TUPLE_IS_ONE_ADMISSIBLE_PHYSICAL_RAW_G = false | TYPE-R |
  witness: same-correlator mismatch on c_square
```

---

## 4. Class-formation and six-account ledger

### 4.1 Door-D class formation

```text
CLASS_FORMATION_DOOR_D_EXECUTED := (
  input_class=finite physical cycle-current bilinear forms,
  input_topology=A4 transported ell1 norm plus trace norm for R,
  input_restrictions=adjoints of isometric cycle inclusions,
  formation_operation=K_R transport, scalar-germ differentiation,
                      A6 continuous-bilinear realization,
  output_class=RawGClass^005 candidate,
  output_topology=bounded-bilinear norm,
  output_restrictions=finite bilinear corners,
  topology_changed=false after the ratified norm transports,
  every_limit_named=true,
  limit_topology=norm,
  weak_star_invoked=false,
  bidual_invoked=false,
  distributional_completion_invoked=false,
  nonseparating_extension_invoked=false,
  Tail_output={0} by finite-core density,
  created_tail_image=zero,
  class_separation_proved=true,
  quotient_exactness_proved=true on the Gate4/path quotient,
  closure_uniqueness_proved=true for each ratified norm-continuous form,
  restriction_square=PASS,
  Q279_full_tuple_reproduced=PASS,
  common_origin_provenance=PASS | premises: DoR-013, DoR-014,
  target_independence=PASS,
  kernel=contains common-source directions; exact witness c_square lies in
         the linear port kernel but not the bilocal port kernel,
  image=bounded D3-real symmetric forms, but the produced candidate lies
        outside the admissible physical-raw-G domain,
  sector_transfers=none; CTP common/difference typing preserved,
  Tail_R_action=zero at this Door-D norm-class formation,
  door_verdict=FAIL_ON_SAME_CORRELATOR_IDENTITY
).
```

### 4.2 Operation accounts

| Operation | Kernel/null data | Image | Sector transfer | Restriction square | Tail action | Verdict |
|---|---|---|---|---|---|---|
| `K_J,K_R` transport | zero on the ratified quotient; Gate-4 verticals already removed | physical cycle sources and physical trace-class bilocal sources | none; CTP blocks preserved | adjoint square **PASS** | no created tail | **PASS** |
| scalar `W` pullback | `L` kills accumulated-sum-zero directions, including `c_square`; `Q` kills trace-zero `R` | scalar germ derivatives | no common leg introduced | P2/Q-279 **PASS** | `Tail_src=0` | **PASS** |
| bilocal-form realization | trace-functional kernel maps to zero; `R_square` survives | bounded `b_delta` in `Bil_phys` | only difference/difference | finite corners **PASS** | Door-D tail zero | **PASS** |
| connected subtraction | rank-one subtraction kills no `R_square` term because `Abar(c_square)=0` | bounded candidate `G_R,phys` | none | **PASS** | no created tail | **PASS** |
| same-correlator identification | exact mismatch kernel: `c_square` is killed only by linear port | no admissible physical raw-`G` image | none; conflict precedes transfer | finite witness **FAIL** | not a tail effect | **FAIL / TYPE-R** |
| Keldysh ordered projection of the source Hessian | all difference/difference noise lies in projection kernel | finite ordered `(delta,c)` zero | no p-carrying transfer | Q-243/Q-279 **PASS** | physical `Tail_R` not formed | finite shadow only |

No operation is omitted. The failure occurs before physical inversion and is
not repairable by a later contour, measure, background, or consumer: those
operations cannot make two already-disagreeing finite definitions equal
without changing an upstream premise.

---

## 5. Chain and p-trace after the failure

### 5.1 What exists

```text
RATIFIED_PHYSICAL_SOURCE_AND_BILOCAL_CARRIERS_EXIST = true | TYPE-P |
  premises: DoR-015

BOUNDED_BILOCAL_CANDIDATE_FORM_EXISTS = true | TYPE-P |
  premises: DoR-014, DoR-015

CONNECTED_SUBTRACTION_FORMED = true | TYPE-P |
  premises: DoR-015 A6

ADMISSIBLE_PHYSICAL_RAW_G_EXISTS = false | TYPE-R |
  test: c_square same-correlator mismatch
```

### 5.2 Physical inverse and retarded extraction

The physical inverse/Schur chain requires an admissible raw `G` first. It does
not receive one. Independently, the produced form has a nontrivial common-source
kernel, and the physical two-sided convolution inverse still requires the
unbuilt measure, prescription, boundary/contact package, and common domains.

```text
PHYSICAL_TWO_SIDED_INVERSE_EXECUTABLE = false | TYPE-C |
  constraints: Door-D raw input failed; convolution measure, contour,
               boundary/contact data, and common domains remain unbuilt |
  release: an admissible raw G plus the named physical inverse package

PHYSICAL_SCHUR_REDUCTION_EXECUTABLE = false | TYPE-C |
  constraints: no admissible G, inverse, stationary G_* block, or domain

PHYSICAL_RETHESS_INSTANCE_EXISTS = false | TYPE-C |
  constraints: preceding raw/inverse/Schur operations do not exist
```

The exact finite source-Hessian projection still gives the ordered
`(delta,c)` zero. It must not be upgraded to `H_R[G]` because the latter is an
action-valued block of the inverse/Schur-reduced physical Hessian.

```text
FINITE_ORDERED_RETARDED_CANDIDATE = ZERO_AND_P_FREE | TYPE-P |
  premises: Q-243, Q-279
PHYSICAL_RETARDED_IMAGE_P_CLEAN = NO_VERDICT
```

### 5.3 Symbolic p trace

The lift itself introduces no new `p` dependence:

```text
common/common and common/difference:  zero;
difference/difference:                 p-carrying through q and the noise form;
difference/R and R/R:                  p-carrying through the exact germ derivatives;
finite ordered retarded candidate:     zero and p-free.
```

The Door-D completion is norm-separated and has zero finite-restriction tail,
so `p` does not hide in a Door-D tail. But no physical retarded image exists.
Therefore neither cancellation nor survival at the physical output can be
certified.

```text
P_ENTERS_DOOR_D_TAIL = false | TYPE-R |
  test: RawGClass is finite-core separated and this formation creates zero tail
P_ENTERS_FINITE_ORDERED_RETARDED_CANDIDATE = false | TYPE-R |
  test: exact Q-243/Q-279 projection
P_ENTERS_PHYSICAL_RETHESS = NO_VERDICT
P_SURVIVES_SELECTED_CONSUMER = NO_VERDICT
```

---

## 6. Consequence and next lawful station

The remaining distance is **not** merely the background fiber plus the
consumption signature. Door D failed before those consumers. The first station
is principal disposition of the upstream incompatibility.

The exact would-build, stated without repairing it, is:

```text
PHYSICAL_TWO_SOURCE_COMPATIBILITY_PACKAGE := (
  one common-origin scalar physical functional on the ratified field carrier,
  linear insertion and symmetric bilocal insertion on that same carrier,
  proof that D_J Abar=(i/hbar)(2D_R W-Abar tensor Abar),
  adjoint finite restriction squares reproducing Q-243/Q-279,
  no selected torsor/intertwiner/anchor/rank member,
  Door-D boundedness, kernel, image, and tail certificate
).
```

This package would have to state explicitly whether it changes:

* DoR-014's C-B trace placement;
* DoR-015's A4/A5/A6 source/field realization; or
* both through a newly ratified common physical scalar functional.

The present corpus supplies no sealed rule selecting among those dispositions.
This lane does not repair a refutation.

Only after that compatibility package passes can the prior downstream list
resume:

1. physical inverse/Schur package;
2. `STAT_BG_LIFT_FIBER` background map;
3. completed restriction and `Tail_R` accounting;
4. induced response and consumption signature.

```text
NEXT_REQUIRED_OBJECT = PHYSICAL_TWO_SOURCE_COMPATIBILITY_PACKAGE
NEXT_OBJECT_ALREADY_BUILT = false | TYPE-U |
  would-build: the package exactly specified above
PRINCIPAL_DISPOSITION_REQUIRED = true | TYPE-C |
  constraint: DoR-015's own standing falsifier has fired
```

---

## 7. Kill passes and final typed ledger

### 7.1 No selection or target tuning

The full cycle family remains ratified. `c_square` is a pre-existing sealed
counterexample witness, not a selected response direction. No torsor,
intertwiner, external background, anchor, rank pair, or cycle basis is chosen.
The test does not mention any desired output, measured value, or coupling.

### 7.2 No unflagged class formation

The only new class act is Door D's already-declared norm-continuous bilinear
formation. Its topology, restrictions, kernel, image, sector transfer, and tail
action are all recorded in Section 4. No weak-star, bidual, distributional, or
nonseparating extension is used.

### 7.3 No naive restriction

Every source restriction is the adjoint of the retained isometric inclusion.
Every bilinear restriction is the corresponding pullback/corner. No raw edge
truncation appears.

### 7.4 Final ledger

```text
DOOR_D_MAP1_TRACE_NORM_TEST = PASS
DOOR_D_MAP2_BOUNDED_FORM_TEST = PASS
DOOR_D_CONNECTED_SUBTRACTION_TYPING = PASS
DOOR_D_ADJOINT_RESTRICTION_SQUARE = PASS
DOOR_D_Q243_Q279_SOURCE_TUPLE = PASS
DOOR_D_TAIL_CREATION = ZERO

DOOR_D_SAME_CORRELATOR_IDENTITY = FAIL | TYPE-R
DOOR_D_EXECUTION = FAIL
DOR015_STANDING_FALSIFIER_FIRED = true

RAW_G_BOUNDED_BILINEAR_CANDIDATE_EXISTS = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-013, DoR-014, DoR-015
RAW_G_PHYSICAL_ADMISSIBILITY = false | TYPE-R
PHYSICAL_RAW_G_LIFT = false | TYPE-R

FINITE_RETARDED_CANDIDATE_P_CLEAN = true | TYPE-P
PHYSICAL_RETHESS_P_CLEAN = NO_VERDICT
BACKGROUND_AND_CONSUMPTION_ONLY_REMAIN = false | TYPE-R |
  test: upstream Door-D physical admissibility failed

SELECTED_MEMBER_FOUND = false | TYPE-S |
  roots: all active definitions and witness use |
  exclusions: c_square as a falsifier witness |
  fences: no-selection discipline |
  query: selected frame, torsor, intertwiner, anchor, rank, cycle basis,
         background, or physical value

UNFLAGGED_CLASS_FORMATION_FOUND = false | TYPE-S |
  roots: Door-D execution and all inherited doors |
  exclusions: operations left TYPE-U/TYPE-C |
  fences: Q-288 six-account taxonomy |
  query: unnamed limit, weak-star, bidual, distributional, nonseparating

REGISTER_HEAD_AT_START = Q-299
REGISTER_HEAD_AT_SEND_TIME = Q-299 |
  register_sha256=5c11e0f257842bed7aeb28f082abc7d293f854dcc97b60df591223d4ae64aa05 |
  later_bearing_entry_found=false | TYPE-S |
  roots: QUESTIONS_SETTLED_REGISTER_V001.md after Q-299 |
  exclusions: DoR-015 itself, already consumed as governing authority |
  fences: send-time currency recheck |
  query: any Q-300-or-later settled question bearing on Door D or raw G

alpha_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
proof_authorized = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION; Q54_EXEMPT]
```

The result is symmetric and exact: the signature did cure the old boundedness
obstruction by changing to the disclosed physical bilinear class, but execution
exposed a deeper incompatibility between the two source ports. The program
must disposition that incompatibility before transport can resume.
