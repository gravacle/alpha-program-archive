# STAGE8 TASK 4A: SQUARE V002 RE-ADJUDICATION - LANE 1 V001

Date: 2026-08-03  
Task: PASTE 444 / Task 4a / square V002 re-adjudication  
Lane: CODEX LANE 1  
Register head at preflight: Q-361  
Custody: adversarial re-adjudication by the derive arm's lane  
Reserved ruling: DoR-017; this artifact adopts nothing

```text
LEAD_RESULT = NOT_READY_ON_ONE_BOUNDED_REGRESSION

REPAIRS_CONFIRMED = M1,M2,M3,M4

MEMBER_RULE_DERIVABLE = no |
  the draft, DoR-009, DoR-008, and the fresh DoR-015 phase-calculus route
  do not select a transverse action member or normalization

KILLING_REGRESSION =
  V002 deleted V001's live realization-isomorphism covariance condition
  together with the algebraic-tensor package, but did not restore that
  condition inside R1.  The R1 fiber therefore admits cycle-label-selective
  members while the no-selection scan says it does not.

COUNTEREXAMPLE =
  phi_c1(q,t)=g(t)(Re H_c1(q)-1), with g all-orders flat at t=0;
  it passes every listed R1 certificate but an admitted edge exchange sends
  it to the distinct c2 member.

MERGED_CANDIDATE = NOT_READY (M6,M7)
MEMBER_RULE_DERIVABLE = no
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

V002 repairs the five defects identified in Q-360 at the level of the forced
diagram and the five residue packages.  The K5 uniqueness refutation is also
correct: no ratified structure tested here selects the member or its scale.
The remaining defect is narrower.  A certified R1 member is not required to
be natural under the retained realization family.  That missing condition
widens alternatives N and F to include forbidden presentation-selective
members.  The DoR-017 fiber is therefore not exactly typed yet.

---

## 0. Seal, preflight, and authorities

### 0.1 Locked process and register

`alpha_supervision/LOCKED_PROCESS.md` was read in full and its sidecar
verified.  The live questions-settled register sidecar verified before the
proposal was read.  Its head was exactly Q-361.

```text
DOES_THE_OBJECT_EXIST = yes | V002 under re-adjudication
IS_THE_VERSION_CURRENT = yes | Q-361
ARE_ITS_INPUTS_PRESENT = yes for the adjudication |
  no for an exactly typed DoR-017 member fiber
PREFLIGHT = PASS
```

### 0.2 Hash-verified objects

| Authority | Verified SHA-256 | Use |
|---|---|---|
| square proposal V002 | `5b4229fd4ba5cc5d8180a91a923c6293c95d71b929f003626363603803a6a30c` | object under review |
| Q-360 adjudication | `9521e9970704beca8818389df972e099dc1d2f7cd1c0c5b1254dd09fb25c9364` | five kills and repair standard |
| Q-358 derive arm | `a9b733c711a692d5eedad8ae6acb5e2829c357c2c6aa3870c1aca2c570604136` | forced diagram and five residues |
| transverse-action draft | `ed49624b6f5f0bcda94ee88a939a5751113b30d73192b2c28a5aec25829e1797` | member/normalization clause |
| descent V003 | `a03e836380cbbfa08d8763bf62d6104f70aec69ae484b3b69f63489a5ce1c68c` | all-rank descent and automorphism covariance |
| extension V002 | `eb3675d525af7d1420c4ed033a5e5b94eb7494c1bac1305029b25ac9169567a0` | scoped `T^char` |
| FIELD_SIGNATURE V005 / DoR-015 source | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | phase calculus and no-selection family |
| Q-408 stationary package | sidecar PASS | flat counterfamily and Q-408 placement |
| DoR-008, DoR-009, DoR-015, DoR-016 decisions | sidecars PASS | ratified scope |

The V002 hash matched before the file was read.  Every sidecar used in this
re-adjudication passed.

### 0.3 Symbol collisions

```text
Phi_c     = DoR-015 local cycle phase with d Phi_c=u_c;
phi_m     = proposed transverse action correction in Flat(S);
Phi_c     != phi_m.

D_G^*     = canonical pullback f |-> f compose D_G;
D_G^*     != an authored comparison member.

rho_f     = Q_M->Q_N;
rho_f^*   = F_N |-> F_N compose rho_f.

family naturality = covariance under signed realization isomorphisms;
stage covariance  = restriction behavior under N<=M;
these are different certificates.
```

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| M1 J1 repair | **PASS** | the forced diagram is premise-marked and carried exactly; `F_N o rho_f` is typed and directly proved; `D_G^*`, full Q-408 placement, and all five DoR-008 obligations are present. |
| M2 J3 repair | **PASS** | live authorship is exactly R1-R5; the tensor machinery is absent and no sixth live object appears. |
| M3 J4 repair | **PASS** | A3 is removed, A8/A10 are verbatim, and all QE fields are segregated with `QE_FIELDS_IN_LIVE_PACKAGE = none`. |
| M4 J6 repair | **PASS** | the restriction-square typecheck is correct and the bottom discrepancy is a failure-capable proposal certificate; the board labels its proposal-level scope honestly. |
| M5 K5 refutation chain | **PASS** | all three stated uniqueness routes fail, and the fresh DoR-015 phase-calculus route also fails to type as a member rule; uniqueness is not derivable. |
| M6 fiber statement | **KILL** | Z/N/F/reject are structurally the right four cases, but N and F are under-typed because R1 lacks realization-automorphism covariance and therefore admits forbidden cycle-selective members. |
| M7 battery and regressions | **KILL** | the stated regressions pass, but the fresh rank-two automorphism attack refutes V002's no-selection scan and the completeness of the R1 certificate. |

```text
PASS_ITEMS = M1,M2,M3,M4,M5
KILL_ITEMS = M6,M7
```

---

## 2. M1 - J1 repair

### 2.1 Forced diagram

V002 carries the derived sequence as premise-marked content:

```text
H_N^CTP
  | Tr_pref,N^009
  v
P_G^fam ---------------- D_G ----------------> Q_G
  |                                            |
  | evaluate D_G^* f                          | f in Act_N^quot
  v                                            v
C ---------------------- identity -----------> C.
```

The canonical comparison operation is installed with the correct type:

```text
D_G^*:Act_N^quot->Fun(P_G^fam,C),
(D_G^*f)(Z)=f(D_G(Z)).                           (M1-1)
```

It is not presented as proposal authorship.

### 2.2 Corrected contravariance

For

```text
rho_f:Q_M->Q_N,
F_N:Q_N->C,
P_f:P_M^fam->P_N^fam,
D_N P_f=rho_f D_M,
```

V002 uses the lawful pullback

```text
rho_f^*F_N=F_N o rho_f:Q_M->C.                   (M1-2)
```

For every `Z_M in P_M^fam`, its direct proof recomputes:

```text
[D_M^*rho_f^*F_N](Z_M)
 =F_N(rho_f(D_M Z_M))
 =F_N(D_N(P_f Z_M))
 =[P_f^*D_N^*F_N](Z_M).                          (M1-3)
```

Every domain and codomain matches.  V001's undefined `F_M o rho_f` is gone.

```text
CONTRAVARIANCE_TYPECHECK = PASS
CORRECTED_SQUARE_DIRECTLY_PROVED = true
```

### 2.3 Existing Map 1 scope

V002 retains

```text
D_G=T_G^char
```

only on the sealed square and `im(j_NM^Q)`.  It does not extend the equality
to pendant content or assert a cycle-creating upward map.

```text
TCHAR_SCOPE = PASS
```

### 2.4 Complete Q-408 placement

All forced terms are present:

```text
Delta H_CC=D_C^2 phi,
Delta H_CK=D_C D_K phi,
Delta H_KC=D_K D_C phi,
Delta H_KK=D_K^2 phi,

delta c_phi[psi]
 =-[D_C^2 Gamma_phi]^-1 D_C psi(c_phi,k).         (M1-4)
```

The inverse is explicitly complement-scoped and conditional on R5.

### 2.5 DoR-008 obligations

V002 carries the complete list:

```text
1. rho_Gamma,N compatible with naturality, reality, and batching;
2. differentiation commutes with rho_Gamma,N;
3. rho_H,N transports blocks/Schur to an independent finite bottom leg;
4. restriction/inversion requires a reducing intertwiner theorem;
5. Q-243/Q-279 shadows, identity, trace, mixed zero, noise,
   reality, extension, and batching reproduce exactly.
```

```text
FORCED_DIAGRAM_CONTAINMENT = PASS
M1 = PASS
```

---

## 3. M2 - J3 repair

The live package is

```text
ACS_017(m)=(R1_m,R2_m,R3_m,R4_m,R5_m).
```

The one-to-one map is:

| Derived residue | V002 field | Coverage |
|---|---|---|
| divergence/action datum and generated quotient member | R1 | complete as a proposal fiber, subject to M7's missing certificate |
| completed-to-finite action restrictions | R2 | `Act_phys^017`, `rho_Gamma,N`, topology, vertical cocycle |
| independent finite physical action bottom leg | R3 | jet carrier, role realization, base action, transverse bottom member |
| scalar comparison equality and normalization | R4 | independent-leg equality plus homogeneous normalizer |
| stationary physical 2PI package | R5 | domain, blocks, inverse, Schur, restrictions, contour/boundary/closure accounts |

The algebraic tensor family and collective-separation rule are absent.
`D_G^*` is correctly outside the authored count because it is derived.
QE is outside the live package.

Components such as R2's topology and R5's contour are internal fields of the
corresponding residue packages, not sixth top-level authored objects.

```text
LIVE_RESIDUE_COUNT = 5
SIXTH_AUTHORED_OBJECT = none
ALGEBRAIC_TENSOR_MACHINERY = absent
M2 = PASS
```

M7 narrows R1's admissibility certificate; it does not change this top-level
count.

---

## 4. M3 - J4 repair

### 4.1 A3 removed

V002 states:

```text
A3_V001_ALGEBRAIC_TENSOR_FAMILY = WITHDRAWN_AS_UNFORCED
A3_NATURALITY_PROOF = DELETED
A3_REPLACEMENT = none | canonical operation is derived D_G^*.
```

No live comparison-law row replaces it.

### 4.2 A8 and A10

A8 and A10 are textually carried at the required scope:

```text
A8: contravariant restriction; upward transport only on rank-preserving
    isomorphisms; cycle-creating upward square voids.

A10: member-sensitive results require family invariance or later member
     ratification; silent selection and averaging are excluded.
```

A10 is a downstream-use rule.  It does not by itself impose covariance on an
R1 member; that distinct omission is the M7 finding.

### 4.3 QE segregation

A1/A6/A7/A9 occur only in the banked section.  V002 states:

```text
QE_SECTION_STANDING = BANKED_NOT_ADOPTED
QE_FIELDS_IN_LIVE_PACKAGE = none
QE_COMPARISON_MEMBER = none
```

No live R1-R5 field consumes endpoint-matched QE data.

```text
A3_REMOVED = true
A8_VERBATIM = true
A10_VERBATIM = true
QE_FIELDS_IN_LIVE_PACKAGE = none
M3 = PASS
```

---

## 5. M4 - J6 repair

### 5.1 Restriction square

Let

```text
a_N^m=rho_Gamma,N(phi_m),
b_N^m=the independently supplied R3 transverse bottom member.
```

The discrepancy is

```text
E_N^m=D_N^*(b_N^m-a_N^m).                        (M4-1)
```

Using `(M1-3)`,

```text
D_M^*rho_f^*(b_N^m-a_N^m)
 =P_f^*D_N^*(b_N^m-a_N^m).                       (M4-2)
```

There is no variance defect.  Surjectivity of `D_N` makes `E_N^m=0`
equivalent to equality of the two physical finite quotient actions, not
equality on one selected history.

### 5.2 Independence and proposal scope

R3 declares the bottom leg independently; R4 does not define it by pullback.
R4 instead makes equality a failure-capable membership certificate.  This is
legitimate at proposal level:

```text
Z member: b_N=a_N=0, concretely executable;
N member: admissible only when the independently supplied b_N and a_N pass
          E_N=0 at every stage;
F member: nonclosing;
reject: no member.
```

Thus the nonzero test is not a derived numerical result.  It is an admission
test that must accompany any N member offered to the principal.  V002 labels
the result `PASS_WITHIN_PROPOSAL`, not `TYPE-P`, which is honest.

### 5.3 Regressions

```text
one-edge tree: Q_G is a point, b_1(*)=a_1(*)=0                 PASS
prefix N=2: full (1,u,uv) data used, not terminal uv only      PASS
pendant w: D(Z_w)=D(Z_1), no T^char import                     PASS
S8-A c3: full quotient coordinate retained                     PASS
Q-243/Q-279: base owns exact finite jets; flat correction none PASS
```

```text
RESTRICTION_SQUARE_DOMAIN_CHECK = PASS
BOTTOM_LEG_FALSIFIER = PASS_WITHIN_PROPOSAL
BOARD_SCOPE_HONEST = true
M4 = PASS
```

---

## 6. M5 - K5 refutation chain

### 6.1 Draft normalization clause

The draft first proves that for a flat-factor attempt

```text
phi_N=D_N f_N,
```

neither a compatible `f_N` nor a renormalization is sealed, and even after
postulating them, multiplying by a symbolic scalar or replacing `f` by
another member of `Flat(S)` leaves a family.

Its would-build then requires:

```text
proof that the rule generates a member, and either uniqueness or an
explicit residual family with no member selected.
```

The second branch is explicit.  The draft does not demand uniqueness and
does not fix a member, a normalizer, or its symbolic normalization.

```text
UNIQUE_MEMBER_FROM_DRAFT_CLAUSE = false | TYPE-R
```

### 6.2 DoR-009 conventions

DoR-009 ratifies:

```text
E_post endpoint orientation;
finite locality;
external-parent exclusions;
the exact finite source-coupled transition law and eight certificates.
```

These determine the input history, faithful trace, and orientation used by
`D_G`.  They contain no map

```text
Q_G -> Flat(S)
```

and no action-member or action-unit normalization.  The no-contact statement
is likewise a law-side result, not a transverse action generator.

```text
UNIQUE_MEMBER_FROM_DOR009 = false | TYPE-R
```

### 6.3 DoR-008 scaling blindness

Let `phi` be an admitted all-orders-flat correction and let `lambda` be any
nonzero real symbolic scalar.  Then for every finite active-section point
and every derivative order `k`,

```text
D^k(lambda phi)|_S=lambda D^k phi|_S=0.           (M5-1)
```

With

```text
b_N -> lambda b_N,
Norm -> lambda-compatible Norm,
nu -> lambda nu,
```

the R4 equality, anchor, reality, batching, pendant result, and all exact
base-action Q-243/Q-279 jets remain unchanged.  The base action owns those
finite jets; the flat member does not rescale them.

DoR-008 therefore cannot distinguish `phi` from `lambda phi` on the sealed
finite active section.  Q-324 separately established that no sealed
source-to-physical-action identification closes this freedom off section.

```text
UNIQUE_MEMBER_FROM_DOR008 = false | TYPE-R
```

### 6.4 Fresh route: DoR-015 phase calculus

The fresh ratified candidate is the physical cycle-phase identity

```text
d Phi_c=u_c,
```

with `Phi_c` anchored by a local logarithm of the cycle holonomy.  This fixes
the differential of the **phase coordinate** for each cycle.  It does not fix
the transverse action.

The direct identification

```text
phi_m=Phi_c                                      (M5-2)
```

fails the R1 form: `d Phi_c=u_c` is generally nonzero on the active cycle
direction, whereas an R1 member is all-orders flat there.

One can restore flatness by composing with a flat profile, for example

```text
phi(q,t)=g(t)F(Phi_c(q)),
g(t)=exp(-1/t^2) for t!=0 and 0 for t=0.          (M5-3)
```

But `(M5-3)` leaves all of the following free:

```text
the cycle c;
the smooth function F;
the flat profile g;
the overall real scale.
```

V005 itself states that the source norm is not forced by Gate 4 and would
require an independent normalization theorem.  No canonical sum over cycles
is available without a basis, measure, or new invariant rule.

Therefore DoR-015 narrows the carrier but does not collapse the member fiber.

```text
UNIQUE_MEMBER_FROM_DOR015_PHASE_CALCULUS = false | TYPE-R
FRESH_DERIVATION_ROUTE_FORCES_MEMBER = false
```

### 6.5 M5 verdict

```text
MEMBER_RULE_DERIVABLE = no
NORMALIZATION_RULE_DERIVABLE = no
M5 = PASS
```

The failure of the fresh route is not the M7 defect.  M7 concerns which
members may lawfully remain in the residual fiber, not whether one is unique.

---

## 7. M6 - the four-alternative fiber

### 7.1 Structural partition

Ignoring the M7 admissibility omission, the four alternatives are the
correct exhaustive decision shapes:

```text
Z = adopt the zero member;
N = adopt one fully certified nonzero member;
F = retain the family with no selected member;
reject = adopt no member.
```

Their stated consequences are correct:

```text
Z: all transverse Q-408 shifts vanish; base action remains;
N: Q-408 shifts are those of the ratified member, with no value computed;
F: member-sensitive shifts are forbidden and the physical square does not
   close, by Q-360/J7;
reject: the forced map remains but the action/2PI square stays TYPE-U.
```

No alternative is recommended.

### 7.2 Exact-typing failure

V002 defines an R1 member by the certificates:

```text
smooth;
reality-covariant;
quotient-compatible;
all-orders flat;
identity anchored;
target-independent;
common-origin depth/accumulation fields;
declared homogeneous normalizer.
```

It does **not** require the generated member to commute with every signed
realization isomorphism or to be basis-free on the complete cycle family.
Thus alternatives N and F include members forbidden by the standing
no-selection discipline.

A8 controls stage restriction and cycle-creating extensions.  A10 controls
whether a downstream claim may be emitted before member ratification.
Neither clause says

```text
phi_(G') o alpha_Q = phi_G                     (M6-1)
```

for every admitted signed realization isomorphism `alpha:G->G'`, nor requires
the generator and normalizer to be natural under the same action.

The four labels remain useful, but the fiber beneath N and F is too large.

```text
FOUR_ALTERNATIVE_PARTITION = correct
CONSEQUENCES = correct conditionally
ALTERNATIVE_RECOMMENDED = none
FIBER_EXACTLY_TYPED = false
M6 = KILL
```

---

## 8. M7 - battery, regressions, and fresh attack

### 8.1 Repaired battery

The stated battery recomputes:

| Check | Verdict |
|---|---|
| target-tuning scan | PASS |
| scaling/normalization countermodel | PASS_BY_DISCLOSURE |
| source/action distinction | PASS |
| corrected pullback variance | PASS |
| no live QE/contact double count | PASS |
| family-only alternative marked nonclosing | PASS |
| pendant witness | PASS |
| cycle-creating extension | PASS |
| F7 endpoint witness | PASS |
| prefix inverse, S8-A, reality, E_post, identity extension | PASS |

### 8.2 Fresh rank-two automorphism attack

Use the admitted S8-A rank-two stage with cycle characters

```text
H_(c1), H_(c2), H_(c3),
```

and the admitted edge-exchange automorphism `sigma` satisfying

```text
sigma(c1)=c2,
sigma(c2)=c1,
sigma(c3)=-c3.                                   (M7-1)
```

Let

```text
g(t)=exp(-1/t^2) for t!=0,
g(0)=0,

phi_c1(q,t)=g(t)(Re H_(c1)(q)-1).                (M7-2)
```

`(M7-2)` satisfies every certificate explicitly listed for R1:

```text
smooth:                    yes;
real/reality-covariant:    Re(H^-1)=Re(H);
quotient-compatible:       H_c is a function on Q_G;
all-orders flat on S:      every derivative carries the flat factor g;
identity anchored:         H_c(identity)=1;
target-independent:        no response, p, alpha, K_*, or measured datum;
finite-visible off section: generally nonzero for t!=0.
```

It may be supplied a homogeneous normalizer and an authored generator, so no
listed R1 row excludes it.

Under the admitted automorphism,

```text
phi_c1(sigma q,t)=g(t)(Re H_(c2)(q)-1),           (M7-3)
```

which differs from `phi_c1(q,t)` for generic `q` with
`Re H_(c1)(q)!=Re H_(c2)(q)`.  The member selects `c1` from a retained
basis-free family.  It is therefore not a physical family-natural scalar.

V001 had an explicit realization-isomorphism covariance condition.  V002's
delta table removes A3 but does not list this certificate as moved into R1;
the only occurrences left are A8 stage covariance and the unsupported
no-selection assertions.

```text
R1_BAD_MEMBER_EXISTS = true | TYPE-R against fiber completeness
REALIZATION_AUTOMORPHISM_COVARIANCE_IN_R1 = absent
CYCLE_BASIS_SELECTION_SCAN = false_as_stated
M7 = KILL
```

### 8.3 Why A10 does not rescue the member

A10 prevents reporting a member-sensitive output before ratification.  It
does not authorize the principal to ratify a presentation-gauge-dependent
member without disclosing a new physical symmetry-breaking datum.  Nor does
ratification make `(M7-3)` covariant.  The member must satisfy the physical
carrier's no-selection law before it enters alternative N.

---

## 9. Bounded repair and merged-candidate status

The forced diagram and R1-R5 architecture need not be rebuilt.  The repair is
to add one certificate inside R1 and propagate it to R2-R4:

```text
For every admitted signed realization isomorphism alpha:G->G':

1. Gen is natural on the transformed divergence/depth datum;
2. phi_(G') o alpha_Q = phi_G;
3. Norm_(G') o alpha_Act = Norm_G;
4. rho_Gamma and the independently supplied bottom legs commute with alpha;
5. any member requiring a selected cycle, cycle basis, realization label,
   or non-natural persistent path is VOID.
```

The K5 fiber then remains non-unique but becomes lawfully scoped:

```text
Z = invariant zero member;
N = one certified nonzero family-natural member;
F = complete family-natural residual fiber, nonclosing;
reject = no member.
```

The explicit member `(M7-2)` must be rejected unless its generator supplies a
new disclosed physical datum that distinguishes `c1` covariantly and that
datum passes its own choice table and falsifiers.  A bare label is not enough.

```text
M1_J1_REPAIR = PASS
M2_J3_REPAIR = PASS
M3_J4_REPAIR = PASS
M4_J6_REPAIR = PASS
M5_K5_UNIQUENESS_REFUTATION = PASS
M6_FIBER = KILL | missing realization-automorphism covariance
M7_FRESH_ATTACK = KILL | explicit cycle-selective admitted member

MERGED_CANDIDATE = NOT_READY (M6,M7)
MEMBER_RULE_DERIVABLE = no
READY_FOR_DOR017_RULING = no

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `K_*`, root, physical response value, rank ratio, or measured
constant was evaluated.  No register, plan, tracker, git, commit, or push
action was performed.
