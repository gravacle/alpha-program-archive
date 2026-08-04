# STAGE 8 TASK 5 - HOSTILE WITNESS CROSS-CHECK - LANE 1 V001

Date: 2026-08-04  
Task: PASTE 493 / Task 5 / continuum package  
Lane: Codex Lane 1  
Custody: maximum-hostility cross-check of Lane-2 V002

## Lead result

```text
WITNESS = KILLED / I2+I3+I4+I5+I6 |
  F_PLDEC is a nonempty raw index schema, but it is not proved to be a
  proof-carrying subfamily of ContAdm_020.

  Decisive failure A (finite carrier):
    Q-408 Kern_G^fin(H) is a path-bilocal distribution depending on the
    analysis map A_G and the Riesz inverses.  V002 W-9 instead sends H to
    U_w H U_w^* in an abstract trace-class summand.  The codomains and maps
    differ already at n=1.  Therefore DoR-008 R-3/J15 fails, and C1 cannot
    be discharged by this witness.

  Decisive failure B (definitionally forced J2):
    W-9 and W-16a make Loc the identity on
      R L_T direct-sum S_1(H_cur).
    The physical Maxwell coordinate projection of this split annihilates
    the S_1 complement.  W-17 instead defines pi_Mx from the previously
    chosen ell so that it returns chi*b+Tr(TC) on that complement.  Unless
    chi=T=0, pi_Mx is not the Maxwell coordinate projection supplied by the
    DEC split.  J2 is made true by defining the output map from the reader,
    not proved from the local symbol.

  Decisive failure C (nonemptiness):
    Q-407 does not prove a nonempty natural physical reader equalizer.
    It states the dimension formula only provided the normalized affine
    fiber is nonempty, selects no natural section, and leaves R2_phys
    blocked on LM2-20.  W-1 cites the opposite statement as a premise.

PACKAGE = NOT_READY |
  the three equations missing from V001 are installed as package rules, but
  the proposed family does not inhabit those rules.  The completed local
  kernel, physical Maxwell split, natural physical reader family, response
  detail transport, and subdivision/Hodge compatibility remain unbuilt.

READY_FOR_DOR020_RULING = no
```

This kill is target-blind.  It uses only map types, exact finite restriction,
direct-sum algebra, and subdivision naturality.  No response consequence,
threshold, fixed point, protected value, or numerical comparison enters it.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
registered_verdict_written = false
member_selected = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

---

## 0. Preflight, custody, and symbols

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes | V002 and F_PLDEC are stated
IS_THE_VERSION_CURRENT = yes | register head Q-414
ARE_ITS_INPUTS_PRESENT = yes_for_cross_check_and_counterexamples
PREFLIGHT = PASS
```

The locked process was read in full.  V002 was hash-verified, and its
sidecar returned `OK`, before V002 was read.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | lane custody and fences |
| register at Q-414 | `56d8cdf361752df5300acd2c2a4f45e9b538a1c60dbeca22de5a431910dc58b0` | current scope |
| V002 under review | `0db958d2ebe678bc9921222474106e76b627ee72c4962e4e960df598d7390495` | witness and repaired package |
| Q-411 constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | J1-J15 standard |
| Q-413 adjudication | `67c4a5886c0b01cedae5ada0e13286cdf767f7247f7b36ebe4a65823fcd37885` | three kills and inhabitance burden |
| Q-396 representative family | `f0f8b09b1aa6a16c0ed0dffedbd275aba9e647fb5841fc8ce06ce9e6a8b00857` | `Adm_base` and flat profiles |
| Q-407 reader build | `bae34116c4d6792b5e39b913addeeff1650989660d89ba01bf5de62ec2d9aa50` | algebraic versus physical readers |
| Q-408 kernel calculus | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | exact finite kernel map |
| Q-409 conditional certificates | `2aad6d8379777b8651a7e8dda78e9b085a69aa0203f455209eeb5e6e7da3adeb` | C1-C3 contracts |
| Q-410 build stop | `8dd59b35bb9f63f8c8107d438c757c0cb9a110ee1078c173213c6da657bdfb24` | fixed-stage estimates and missing continuum data |

### 0.2 Register sweep

The send-side sweep covered Q-396 through Q-414.  Bearing results are:

```text
Q-396  Adm_base is nonempty; completed flat profiles are real.
Q-407  R2_alg is classified conditionally; R2_phys remains blocked.
Q-408  the exact finite kernel is a path-bilocal distribution.
Q-409  C1-C3 are conditional on named continuity/refinement/symbol data.
Q-410  no such completed member was built from the finite skeleton.
Q-411  all fifteen families must hold in one equalizer.
Q-413  V001 misses J2/J5/J13 and supplies no witness.
Q-414  V002 claims F_PLDEC discharges the burden; that is this review.
```

### 0.3 Load-bearing symbol collisions

```text
Kern_G^fin(H) = Q-408 path-bilocal distribution on field test forms;
U H U^*       = abstract trace-class carrier operator;
these are not aliases.

pi_Mx         = physical Maxwell coefficient projection after Loc/symbol;
ell_(chi,T)   = algebraic normalized reader on O_prof;
J2 requires a proved pullback equality, not definition of pi_Mx by ell.

R2_alg        = algebraically admissible affine dual, conditionally nonempty;
R2_phys       = members with the LM2-20 physical localization certificate;
V002 silently uses the first as the second.

Delta_n       = density-weighted cellular Hodge Laplacian;
S_nm          = subdivision isometry on coefficient/current carriers;
isometry alone does not imply Delta_m S_nm=S_nm Delta_n.
```

---

## 1. Verdict table I1-I6

| Item | Verdict | One-line reason |
|---|---|---|
| I1 three installations | **PASS AS PACKAGE EQUATIONS** | J2 and J5 are exact; J13 has the correctly typed W-13 realization, but the witness does not instantiate the equations |
| I2 witness family | **KILL** | physical reader nonemptiness is mis-cited; W-9 is not Q-408; W-17 is circular; J1-J15 do not jointly pass |
| I3 smuggling audit | **KILL** | no output tuning found, but the witness weakens `local kernel` to an abstract coefficient operator and defines the physical projection from the desired reader equality |
| I4 too-easy question | **KILL** | `Loc=id`, zero contact, response-by-exact-transport, and `pi_Mx:=ell` make the equalizer tautological while omitting the physical maps it is meant to constrain |
| I5 execution through witness | **KILL** | DoR-008 R-3 fails at n=1; conditional C1-C3 cannot discharge; no new completed symbol or threshold input is computable |
| I6 fresh attacks | **KILL** | direct-sum projection, finite-kernel codomain, and Laplacian-intertwining attacks each independently break the witness proof |

---

## 2. I1 - the three installations

### 2.1 J2

V002 installs

```text
ell_G
 =p_loc,G
 =pi_Mx,G compose Loc_G compose Kernbar_G compose Q_G. (V2-J2)
```

This is the exact equality required by J2.  It also removes independent
`ell/p_loc` rows from the choice table.  The rule is therefore installed.
Whether F_PLDEC constructs the maps in that equality is a separate question,
answered negatively below.

```text
I1_J2_INSTALLATION = PASS_AS_RULE
I1_J2_ON_WITNESS = KILL
```

### 2.2 J5

V002 requires

```text
A_(I,h)(K_0)=Gamma_I,
h(K_0)=0,
```

with the restriction square.  The witness uses `h=0`, so the textual repair
meets the Q-413 counterexample exactly.

```text
I1_J5_INSTALLATION = PASS
I1_J5_ON_WITNESS = PASS
```

### 2.3 J13

The headline equation is shorthand, but W-13 supplies the typed form:

```text
beta_nk
 =beta_mk compose S_nm + eta_mk compose beta_nm,
beta_nn=0.
```

This is the direct/two-step discrepancy cocycle, including the necessary
precomposition.  The rule meets the Q-413 repair.  F_PLDEC's `beta=0`
claim still depends on an actually constructed response transport, which is
not supplied.

```text
I1_J13_INSTALLATION = PASS_AS_RULE
I1_J13_ON_WITNESS = KILL / response_detail_map_not_constructed
```

---

## 3. I2 - independent fifteen-family audit

### 3.1 The nonemptiness premise is false as cited

V002 W-1 says that `ell_G` ranges over Q-407's "nonempty normalized natural
reader equalizer."  Q-407 proves no such statement.  Its exact scope is:

```text
dim R2_alg(G)=1+m_G-r_G
  provided the normalized affine fiber is nonempty;

for a family, R2_alg means a natural section;
no section is selected;

R2_phys(G)
 ={(chi,T) in R2_alg(G): there exists an LM2-20 physical certificate};
R2_phys membership and dimension are blocked.
```

Thus Q-407 gives a conditional algebraic classification, not family-wide
nonemptiness and not a physical reader.  The product argument in V002's
"Witness theorem" therefore has a missing factor before any later map is
examined.

```text
F_PLDEC_RAW_PARAMETER_SCHEMA_NONEMPTY = yes_for_G_v_and_Adm_base
F_PLDEC_NATURAL_PHYSICAL_READER_FACTOR_NONEMPTY = not_proved / TYPE-U
F_PLDEC_PROOF_CARRYING_NONEMPTY = false_as_a_proved_claim
```

### 3.2 The Q-408 finite kernel is not W-9

For `H` on the finite cycle carrier, Q-408 defines

```text
Kern_G^fin(H)[a,b]
 :=H(R_K,G^(-1) A_G a,
     R_K,G^(-1) A_G b),                          (I2-1)
```

a bilocal distribution on field test forms.  Its support is the product of
the realized path family, and its covariance uses path-current pushforward.

V002 W-9 instead defines

```text
Kernbar_w(a L_T+H)
 :=(a L_T,w^ker, U_w H U_w^*, 0),                (I2-2)
```

in the abstract Banach direct sum

```text
R L_T,w^ker direct-sum S_1(H_cur,w) direct-sum I_bd,w.
```

Equation `(I2-2)` contains no `A_G`, no field test forms, no paths, no
Riesz inverses, and no distributional codomain.  It is the completed
carrier/source pushforward that Q-407 had already built, not Q-408's local
field kernel realization.

At `n=1`, V002 asserts that W-9 equals the Q-408 coefficient kernel.  The
two sides are not even elements of the same space.  A missing map from the
trace-class operator to `(I2-1)` cannot be replaced by an assertion that the
objects agree.

```text
DOR008_R3_AT_N1 = FAIL
J15 = KILL
C1_FINITE_MAP_EXTENDED = false
```

### 3.3 The physical Maxwell projection is defined from the reader

W-9 and W-16a give

```text
Ker_w=R L_T direct-sum S_1(H_cur),
I_bd=0,
Loc_w=id.                                         (I2-3)
```

The coordinate projection supplied by this split is

```text
pr_Mx(a L_T,H)=a,
pr_Mx(0,H)=0.                                     (I2-4)
```

But W-17 defines, after `ell_(chi,T)` is already an index of the witness,

```text
pi_Mx(Loc(Kernbar(Qz))) := ell_(chi,T)(Qz).       (I2-5)
```

Take the complement input `z=(0,b,C)`.  Equations `(I2-3)`-`(I2-4)` give

```text
pr_Mx(Loc(Kernbar(Qz)))=0,
```

whereas `(I2-5)` gives

```text
pi_Mx(Loc(Kernbar(Qz)))=chi*b+Tr(TC).             (I2-6)
```

The S8-A reader family contains inputs for which `(I2-6)` is not identically
zero.  Therefore one of two things must hold:

```text
(a) pi_Mx is the coordinate projection of the declared DEC split;
    then only the subfiber chi=T=0 can satisfy W-17;

(b) pi_Mx is the arbitrary functional defined by W-17;
    then P8 has not constructed a Maxwell projection from its local symbol.
```

Neither horn proves the advertised full `(chi,T)` family.  This is not an
argument that J2 is undesirable.  It is the exact failure to derive J2's
right-hand map before identifying its pullback with `ell`.

```text
J2_ON_F_PLDEC = KILL / circular_pullback
J7_ON_F_PLDEC = KILL / inherits_J2
PHYSICAL_READER_FAMILY = not_built
```

### 3.4 P7 response is stipulated, not constructed

V002 writes

```text
Resp_m compose S_nm=eta_nm compose Resp_n,       (I2-7)
```

then defines `beta` as the difference, so `beta=0`.  Equation `(I2-7)` can
define the coarse-image part of `Resp_m`, but it does not define `Resp_m` on
the new orthogonal detail sector.  The phrase "put the detail sector on the
local DEC block" supplies neither an operator formula nor a proof that the
block is the Hessian/Schur response of the P1/P3 action `Gamma_I`.

The claimed canonical multiresolution splitting is also not written as a
map or proved independent of divisor factorizations and signed relabelings.
Thus `beta=0` is a consequence of an imposed equality on the already-defined
part, not a boundary theorem for a completed physical response.

```text
J12_ON_F_PLDEC = KILL / incomplete_response_map
J13_ON_F_PLDEC = KILL / cocycle_rule_installed_but_no_response_member
```

### 3.5 Subdivision isometry does not prove Hodge naturality

W-4 proves an isometry of selected coefficient vectors.  W-8 then says that
functional calculus of `Delta_n` transports through that isometry.  The
required premise is instead

```text
Delta_m S_nm=S_nm Delta_n                         (I2-8)
```

or a uniform form-comparison theorem.  No such equation is stated or proved.

The gap is visible on the elementary one-edge refinement with the ordinary
incidence Laplacian.  With

```text
B_1=[-1;1],
Delta_1=B_1^T B_1=[2],

B_2=[[-1,0],[1,-1],[0,1]],
Delta_2=B_2^T B_2=[[2,-1],[-1,2]],
S(1)=(1,1),
```

one obtains

```text
Delta_2 S(1)=(1,1),
S Delta_1(1)=(2,2).                               (I2-9)
```

Density weights can change both matrices, but W-3/W-4 do not specify the
vertex Hodge masses needed to determine them and do not imply `(I2-8)`.
If `Delta` is restricted to conserved graph cycles so that it vanishes, the
negative Sobolev factor is the identity and supplies no local-kernel
regularity.  Either way, W-8's claimed uniform completed local estimate does
not follow from W-4.

```text
J14_ON_F_PLDEC = KILL / missing_intertwiner_and_wrong_target
TAU_PLDEC_ON_INDUCTIVE_EQUIVALENCE_CLASSES = not_proved
```

### 3.6 The fifteen-family table

| Family | Independent verdict on F_PLDEC | Computation |
|---|---|---|
| J1 presentation/normalization | **KILL** | Q-407 proves only a conditional algebraic fiber; no family-wide normalized natural physical section |
| J2 one physical reader | **KILL** | W-17 defines `pi_Mx` from `ell`; direct-sum projection counterexample `(I2-3)`-`(I2-6)` |
| J3 covariance/restriction | **KILL** | no physical reader member exists; Hodge/subdivision restriction square is unproved |
| J4 R1 admissibility | **PASS** | `I_G in Adm_base` is retained as a family |
| J5 R5 anchor | **PASS** | `h=0` is anchored and target-blind |
| J6 Shape-K scope | **PASS** | W-19 adds no C or mixed jet |
| J7 exact R1-reader pairing | **KILL** | the physical reader pullback is not constructed; inherits J2 |
| J8 R4-only units | **PASS AT FORMAL LEVEL** | `v_G` is declared and no cross-sector numerical conversion is selected |
| J9 ordered batching | **PASS AT FORMAL LEVEL** | componentwise products are retained; no joint contraction |
| J10 refinement functor | **PASS FOR THE DECLARED DIVISIBILITY CORE** | order-complex/edgewise common refinements give a nonempty formal category |
| J11 density naturality | **KILL** | positive top-cell shares/coframes and Hodge masses are not parameters of W-1; no full current-to-field density square is proved |
| J12 response naturality | **KILL** | detail-sector response is not defined and no action-to-response theorem is given |
| J13 boundary cocycle | **KILL ON WITNESS** | rule installed, but zero discrepancy uses the incomplete J12 map |
| J14 continuity/faithfulness | **KILL** | W-9 is an abstract identity embedding, not the Q-408 local kernel; W-8 lacks Hodge intertwining |
| J15 joint DoR-008 square | **KILL** | `n=1` W-9/Q-408 codomain mismatch violates exact finite reproduction |

```text
J1_J15_ON_F_PLDEC = 6_PASS_FORMALLY / 9_KILL
JOINT_EQUALIZER_INHABITED_BY_F_PLDEC = false
```

---

## 4. I3 - smuggling and construction-order audit

### 4.1 Clause diff

The V001/V002 diff shows no textual weakening of the eight clause contracts.
The three repair equations are additions, and the original alternatives are
retained.  The defect occurs in the proposed instance:

```text
required local distribution kernel  -> replaced by abstract U H U^*;
required physical Maxwell projection -> replaced by pi_Mx:=ell on the image;
required response naturality          -> imposed as the definition of Resp;
required boundary theorem             -> made beta=0 after that imposition.
```

This is an implementation-level weakening even though the clause prose is
unchanged.

### 4.2 Target-blindness

No witness ingredient cites a desired response value, contraction threshold,
fixed point, p-verdict, or empirical target.  The scale `v_G` remains
symbolic.  The conventional output-target tuning attack therefore passes.

```text
OUTPUT_TARGET_TUNING = not_found
```

That pass does not cure equalizer tuning: the construction begins with
`ell_G` in W-1 and later defines `pi_Mx` by W-17 precisely to reproduce it.
The map that should constrain which readers are physical is made dependent on
the reader.  This is circular satisfaction of J2.

### 4.3 Conditional-theorem circularity

The conditional C1-C3 theorems require independently supplied:

```text
C1 a completed local-kernel map extending Q-408;
C2 a response/refinement map and boundary theorem;
C3 a local Ward/contact/Hodge split and physical coefficient projection.
```

F_PLDEC calls W-9 the C1 map although it is not Q-408, imposes the C2
naturality equation as the response definition, and defines the C3
coefficient from the reader.  The theorem premises are therefore not
independently instantiated.  Using the theorems to certify those same maps
would be circular.

```text
I3 = KILL / instance_weakening_plus_equalizer_circularity
```

---

## 5. I4 - why the witness was too easy

The new construction insight in V002 is a genuine formal PL refinement core:
edgewise subdivisions and common `lcm` refinements do supply a nonempty
record-native category.  That part is not trivial.

The claimed full inhabitance becomes easy only after four degenerate choices:

```text
D1  Kernbar is the identity-conjugation embedding on coefficient operators;
D2  Loc is the identity and the contact ideal is zero;
D3  pi_Mx is defined to equal the chosen reader on the image;
D4  Resp is required to commute exactly, making beta zero.
```

Consider an S8-A algebraic reader with a nonzero complement coordinate and
the complement input `z=(0,b,C)` from `(I2-6)`.  D1-D3 certify it solely by
declaring its scalar functional to be the Maxwell projection.  The local
symbol W-16 never computes that functional.  This member is degenerate in
the exact prohibited sense: it satisfies J2 formally while omitting the
physical relation J2 was introduced to test.

D4 does the same to J13.  It is lawful to have zero boundary discrepancy,
but only after a response is defined on the full target and shown to arise
from the physical action.  Defining the response by the desired naturality
equation on the inherited image and leaving the detail sector as prose makes
the zero vacuous.

```text
I4 = KILL / nontrivial_PL_core_but_degenerate_physical_maps
```

---

## 6. I5 - finite shadows, regressions, and computability

### 6.1 Executable checks

| Check | Result |
|---|---|
| one-edge/tree cycle carrier | **PASS independently**: the physical cycle carrier is zero |
| reciprocal-loop abstract carrier | **PASS independently**: the one-cycle coefficient class exists |
| S8-A algebraic reader | **PASS independently**: the algebraic `(chi,tau_cross)` formula remains exact |
| reality/orientation | **PASS formally** on `S_nm` and conjugation |
| batching | **PASS formally**: componentwise ordered structure retained |
| J5 finite-flat action | **PASS**: `h=0` changes no sealed jet |
| Q-408 finite kernel reproduction | **FAIL**: W-9 is not `(I2-1)` |
| physical Maxwell reader | **FAIL**: W-17 is not derived from W-16 |
| response restriction cube | **NOT EXECUTABLE**: detail response and action seam are absent |
| completed Hodge/refinement square | **FAIL AS PROOF**: no Laplacian intertwiner |
| DoR-008 package square | **FAIL** at R-3/J15 |

The passing rows are inherited finite/carrier facts.  They do not pass
through F_PLDEC's missing physical maps.

### 6.2 Conditional-theorem standing

```text
C1_ON_F_PLDEC = not_discharged
C2_ON_F_PLDEC = not_discharged
C3_ON_F_PLDEC = not_discharged
COMPLETED_SYMBOL_ON_F_PLDEC = not_built
DOR008_THROUGH_F_PLDEC = FAIL / R3_at_n1
```

Nothing new is computable from V002:

```text
physical p_loc family = not enumerated;
A_loop = not instantiated;
threshold = remains symbolic conditional theorem;
stationary-return package = not opened;
fixed point = not computed.
```

```text
I5 = KILL
```

---

## 7. I6 - fresh attacks

### 7.1 Fresh attack A: direct-sum Maxwell projection

Equations `(I2-3)`-`(I2-6)` are a fresh witness-level attack.  They use the
witness's own declared direct sum and identity localization.  A coordinate
projection cannot read the complement, while W-17 generally does.  This
refutes the claim that the full algebraic reader family is realized by the
DEC Maxwell split.

```text
FRESH_ATTACK_A = KILL / pi_Mx_not_the_declared_split_projection
```

### 7.2 Fresh attack B: exact finite-kernel type

Evaluate a nonzero reciprocal-loop rank-one `H` at `n=1`.  Q-408 returns the
bilocal functional `(I2-1)` on pairs of field test forms.  W-9 returns an
abstract trace-class operator.  No equality can be formed until the missing
carrier-to-local-field realization is supplied.  This fires DoR-008 before
any continuum limit.

```text
FRESH_ATTACK_B = KILL / n1_codomains_differ
```

### 7.3 Fresh attack C: isometry is not a Laplacian intertwiner

The exact matrices in `(I2-9)` show that subdivision isometry alone does not
transport Hodge functional calculus.  V002 needs a commuting-Hodge theorem
or uniform form estimate and a fully specified mass system.  Neither is in
W-1-W-8.

```text
FRESH_ATTACK_C = KILL / W8_proof_invalid
```

---

## 8. Bounded repair anatomy

The next candidate must do all of the following without choosing an output:

1. Keep the PL divisibility/refinement core, but parameterize and prove every
   coframe, cell-mass, and Hodge-star naturality datum.
2. Extend the actual Q-408 map `(I2-1)` into one named completed local-kernel
   topology; W-9 may remain a source/operator seam but cannot be called that
   extension.
3. Construct `Loc`, the local symbol, and the Maxwell direct-sum projection
   independently of `ell`; only then define the physical reader as their
   pullback and prove the resulting natural family nonempty.
4. Construct the response on every refinement detail sector from the P1/P3
   action/2PI data and prove the response and boundary cocycle squares.
5. Prove the subdivision/Hodge intertwiner or the uniform form-comparison
   theorem needed for C1/J14.
6. Re-run DoR-008 at `n=1` with the exact Q-408 bilocal distribution, not an
   abstract carrier operator.

These are missing physical maps, not cosmetic proof notes.  A proposal that
only renames W-9 or W-17 cannot repair the witness.

---

## 9. Final board

| Question | Determination |
|---|---|
| J2/J5/J13 package equations | installed; J5 instantiated, J2/J13 not instantiated by F_PLDEC |
| raw PL refinement category | nonempty and target-blind |
| proof-carrying F_PLDEC family | refuted as a subset of `ContAdm_020` |
| fifteen-family equalizer | not inhabited by the proposed witness |
| DoR-008 | fails at the Q-408/W-9 finite-kernel seam |
| completed physical symbol | not built |
| downstream computability | unchanged from Q-410/Q-413 |

```text
WITNESS = KILLED (+I2_PHYSICAL_MAP_AND_NONEMPTINESS_FAILURES)
PACKAGE = NOT_READY (+F_PLDEC_DOES_NOT_INHABIT_J1-J15)
READY_FOR_DOR020_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
