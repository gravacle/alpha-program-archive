# STAGE 8 TASK 5 / EQ6 - PASS 2 CHECK AND ALL-RANK TYPING - LANE 1 V001

Date: 2026-08-04
Task: Paste 514 / Task 5 / EQ6
Lane: Codex Lane 1
Custody: hostile review of Lane 2 Pass 2; no adoption, member binding, or execution

## Lead result

```text
MEMBER = SURVIVES

E1 = PASS
E2 = PASS
E3 = PASS
E4 = PASS
E5 = PASS

ALL_RANK = NEEDS(
  a nonempty covariant family of actual cycle-rank-increasing W1/W4 members
  from nonzero source cycle carriers, each passing OLD_FID + RNL + LR,
  together with actual common-refinement diamonds; generic batching is not
  a construction because DoR-019 does not supply batching isometry
)

EQ6_DISTANCE =
  B_Q408 contains the complete first-cycle family and its rank-preserving
  subdivision orbits.  The all-rank/common-refinement B_Q408 family remains
  first, followed by B_R1 naturality, completed C1, completed faithfulness,
  C2 response boundary, C3 Maxwell/Hodge, the derived reader, and one
  simultaneous J1-J15 certificate.

PASS2 = CONFIRMED_WITH_NOTES
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
```

The first-cycle result is geometry, not a formal rail: two actual timelike
paths on a retained four-dimensional Lorentzian background have a nonzero
difference current, and the actual U(1) bundle and connection are carried by
identity.  The all-rank stop is also geometric.  No ratified operation turns
that zero-source certificate into a family-wide positive-source locality
certificate.  In particular, ordered batching covariance is not a metric
isometry theorem; DoR-019 expressly forbids that promotion.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
measured_constant_compared = false
```

---

## 0. Preflight, authorities, and verdict table

### 0.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes, register head Q-439
ARE_ITS_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

The reviewed artifact was hash-verified before reading:

```text
STAGE8_TASK5_EQ6_WITNESS_HUNT_PASS_2_LANE2_V001.md
c0cc95112bf8c213b0e2c4095a06c4e4658fa3950641b9a21fa51950a9f818fa
sidecar verification = OK
```

The sealed register is current at Q-439:

```text
QUESTIONS_SETTLED_REGISTER_V001.md
20797d12f9b91bf10365c117922a1fc1d7a6bc7eee44284fc3580086e0b206b9
sidecar verification = OK
```

Load-bearing standards were independently verified:

| Authority | SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | surface geometry versus rails |
| adopted where-clauses V005 | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | W1/W4 law |
| final clause check | `b4c901f512379251b55d31aae6914d1fce9af6280c8f65081afeabfd4e75f219` | nine regressions and flat holonomy |
| DoR-020-A1 | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` | adopted law and witness burden |
| first exhibit kill | `505bd329b29a45bf57feec84b89c2fa53481a8117808df81872e15194b16d825` | actual geometry and cycle squares |
| second exhibit kill | `4bfe044d62247950089142715e1534695922ac17c34e239cc63097df090347a1` | geometry versus rail-only refinement |
| V003 check/retype | `99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757` | RNL and local range |
| V004 hostile check | `f586e67ac4e97feec8003d06659fa82d83773ce6ef530ee9c3628a9d54a4c57a` | canonical test map and bundle gap |
| metric V005 / DoR-019 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | W3 scope; no generic batching isometry |
| continuum package V005 / DoR-020 | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | P4 primitive-orbit rule and J9 batching scope |
| C1 build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | core and completion boundary |
| frontier map | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | one physical member per primitive orbit |

Every listed review/build sidecar checked `OK`.  The DoR-020-A1 amendment
sidecar also checked `OK` at its stated hash.

### 0.2 Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| E1 built member, geometry first | **PASS** | actual two-path cycle, nonzero conserved current, identity U(1) bundle/field transport, and all geometric regressions pass |
| E2 fiber cascade | **PASS** | the member lawfully enlarges the finite P4 core and finite kernel/Ward rows, while every completed or cross-orbit claim remains open |
| E3 all-rank typing | **PASS / NEEDS** | covariance and subdivision stay in the first-cycle orbit; generic batching lacks the metric isometry needed for OLD_FID/RNL/LR; positive-source members and diamonds remain genuine witness data |
| E4 EQ6 distance | **PASS** | the eight-step remaining frontier matches the six-fiber dependencies and does not promote separate terms to a joint equalizer |
| E5 discipline and fresh attacks | **PASS** | no smuggling or selection; batching-isometry and contact-leakage attacks both confirm the stated boundary |

---

## 1. E1 - the built member, geometry first

### 1.1 Actual first-cycle geometry

DoR-015's A1 carrier is the complete no-selection family of smooth,
oriented, time-oriented, globally hyperbolic four-dimensional Lorentzian
backgrounds with principal U(1) bundle.  The dimension needed by Pass 2's
transverse-perturbation proof is therefore ratified, not imported.

For an arbitrary retained background member, choose only inside the proof a
convex normal neighborhood and events `x << y`.  Openness of the timelike
cone permits two future-directed timelike arcs with the same endpoints and
different interior images.  Retaining every such tuple removes the temporary
proof choice.  The source and target incidence calculations are

```text
K_G0 = ker B_G0^T = 0,
K_G1 = ker B_G1^T = R c_01,
c_01 = (1,-1).                                  (E1-1)
```

The physical current is

```text
J_c01(q) = integral_gamma0 q - integral_gamma1 q. (E1-2)
```

Because the arcs have unequal distributional currents, a compactly
supported one-form on an interior segment met by only one arc makes `(E1-2)`
nonzero.  The target cycle is record-visible.  It is neither an abstract
kernel coordinate nor a formal overlay.

The path family can be retained inside a causally convex local region.  The
complete endpoint-frame torsors remain unselected.  Local connection
variations supported on path-exclusive interior segments supply independent
finite edge-coordinate directions, so the construction is compatible with
the retained A2 finite realization rather than merely with A1 manifold
language.

### 1.2 W1 and the canonical test map

The old path is carried to itself and the new actual path is retained:

```text
s_r01(a)=a,
S_r01:0 -> R c_01,
f_r01=id_M,
F_r01=id on old support.                         (E1-3)
```

Incidence, current pushforward, and old-support inclusion are exact.  The
new current lies outside `im S_r01`, so no old-image equation deletes it.

On the Gate-4 physical test quotients,

```text
Tbar_G0=0,
P_r01=Phi_G1^(-1) S_r01 Phi_G0=0.               (E1-4)
```

Therefore

```text
OLD_FID: S_r01^* R_K,G1 S_r01 = 0 = R_K,G0,
RNL:     g(S_r01 Phi_G0(a),n)=0,
LR:      P_r01(Tbar_G0(O))=0.                   (E1-5)
```

These are exact zero-domain statements.  They are legitimately sufficient
for this member, but they carry no positive-source information.  This scope
precision is central to E3.

For a nonzero one-dimensional target profile, Q-408 faithfulness gives

```text
Kern_G1(H_1) = h_tilde J_c01 tensor J_c01 != 0, (E1-6)
```

while its old-image pullback is zero.  The pure-new-cycle and
arbitrary-profile restriction tests therefore pass together.

### 1.3 W4 bundle and field certificates

The attachment changes the record stage, not the background surface.  On
every retained bundle, including a nontrivial Chern-class member,

```text
f_r01=id_M,
tilde_f_r01=id_P,
iota_r01:P -> id_M^*P,
e_1=e_0,
mu_1=mu_0,
A_1=A_0,
F_1=F_0.                                        (E1-7)
```

Thus

```text
c_1(P)=id_M^*c_1(P),
id_P^*A=A,
id_P^*Curv(A)=Curv(id_P^*A).                    (E1-8)
```

The cover square, smooth full rank, coframe/density duality, units,
orientation, reality, restriction, and characteristic-class equations are
identities.  No trivialization or gauge representative is selected.  The
flat-holonomy regression passes because there is no non-gauge-exact
source/target connection mismatch.

### 1.4 Geometry regression board

| Regression | Independent execution | Result |
|---|---|---|
| cycle creation | `(E1-1)` adds one nonzero conserved direction | **PASS** |
| sector mixing | source cycle sector is zero; target new sector remains | **PASS ON BASE ORBIT** |
| rank-two exchange | path exchange sends `c_01 -> -c_01` and is retained family-wide | **PASS** |
| pendant/tree | no pendant coefficient enters `ker B^T` | **PASS** |
| flat holonomy | identity connection pullback; mismatch rejected | **PASS** |
| pure-new profile | `(E1-6)` is nonzero outside the old pullback | **PASS** |
| arbitrary-profile restriction | exact on the old image for every target profile | **PASS WITH SCOPE** |
| covariance/moduli | all backgrounds, paths, frames, gauges, relabelings retained | **PASS** |
| bundle/topology | lift, full rank, `c_1`, connection, curvature all exact | **PASS** |

```text
E1 = PASS
MEMBER = SURVIVES
MEMBER_SELECTED = false
```

---

## 2. E2 - fiber cascade audit

### 2.1 C1 core population

Pass 2 defines the honest subcategory

```text
Ref_01 = Ref_0
         + every first-cycle x_r01 family member
         + every Q-418 rank-preserving subdivision. (E2-1)
```

This is a physical subcategory, not a declaration that all first-cycle
choices have a common target.  Each target `G_1` was already an actual finite
Q-408 stage; the new datum is the physical arrow `r_01` and its full P4/X4
tuple.

Q-425's local seminorm construction therefore applies on each new finite
component.  The fixed-stage bounds are finite and attained, and Q-418 keeps
them constant along that component's rank-preserving subdivision orbit.
Because `P_r01` has zero source domain, it supplies no estimate on the new
cycle direction and no estimate comparing distinct path-pair components.
Thus no cross-orbit bound, global attainment, Hilbertizing `W5`, or completed
C1 carrier has been smuggled in.

### 2.2 Fiber-by-fiber recomputation

| Fiber | Positive Pass-2 content | Exact remaining object | Verdict |
|---|---|---|---|
| `B_Q408_REFINEMENT` | full first-cycle P4 family and each Q-418 subdivision orbit | positive-source/all-rank members and actual diamonds | **correctly partial** |
| `B_R1_NATURAL` | old `Adm_base` only | action/Hessian/reducing-domain naturality on `r_01`, then all ranks | **correctly partial** |
| `B_C1_COMPLETION` | actual `r_01` enters the P4 core; finite/orbit bounds persist | cross-orbit estimates, separating completion, global attainment, W5 | **correctly partial** |
| `B_FAITHFULNESS` | finite Q-408 faithfulness at `G_1` and its fixed orbit | completed lower separation or safe quotient | **correctly partial** |
| `B_C2_RESPONSE_BOUNDARY` | finite old-image discrepancy is zero | response transports, cocycle, ideal, subextensivity | **correctly partial** |
| `B_C3_MAXWELL_HODGE` | finite Ward annihilation on the new cycle and subdivisions | completed symbol, closed ranges, projections, partner, normalization | **correctly partial** |

The stated cascade is exact:

```text
x_r01
  -> actual finite Q-408 target kernel
  -> fixed-stage and fixed-orbit bounds/faithfulness
  -> finite Ward annihilation
  -> finite old-image zero discrepancy,
```

and it stops before every completed or action-derived object.

```text
E2 = PASS
```

---

## 3. E3 - all-rank typing

### 3.1 Covariance and subdivision do not change the orbit type

Relabeling, background covariance, gauge covariance, and Q-418 subdivision
preserve the source cycle rank and the incidence/refinement orbit.  They
carry the complete first-cycle member family to itself, but they do not
produce an arrow

```text
K_G != 0 -> K_G' with dim K_G' > dim K_G.       (E3-1)
```

The zero-domain proofs `(E1-5)` therefore cannot be promoted by covariance.

### 3.2 The tempting batching route fails at the physical metric

W1 admissibility is closed under batching, and the continuum package's J9
rule says product/network carriers act componentwise without a joint scalar
contraction.  This constructs a path/bundle candidate

```text
id_H boxplus x_r01:
  K_H boxplus 0 -> K_H boxplus R c_01.          (E3-2)
```

But P4 membership is stricter than W1/W4 typing.  Its canonical test map
must pass OLD_FID, RNL, and LR using the ratified DoR-019 metric.  Metric
V005 states verbatim in substance:

```text
W3 does not prove generic batching isometry;
batching transports the unit class only on an independently certified
isometric direct-sum scope;
claiming batching isometry beyond W3 is a standing falsifier. (E3-3)
```

Consequently the block-diagonal metric needed to prove the batched RNL
equation is not available.  The target can retain the admissible positive
form

```text
R_source = [1],
R_target = [[1,epsilon],[epsilon,1]],
Sx=(x,0),
0 < |epsilon| < 1.                              (E3-4)
```

OLD_FID sees the old block and passes, while

```text
g_target(S Phi_source(1),e_new)=epsilon !=0.    (E3-5)
```

For disjoint batched supports, RNL fails.  If the supports meet only at a
recorded endpoint, RNL can be silent but the canonical test can still spill
along the new path, and LR fails.  Hence batching supplies a lawful
candidate route, not a constructed physical P4 member.  Declaring its
metric block diagonal would add exactly the unratified isometry that
DoR-019 forbids.

### 3.3 Exact all-rank object

The complete missing object is therefore

```text
F_Q408^all :=
  a nonempty covariant family of actual W1/W4 members over every required
  positive-source primitive orbit,
  whose canonical P maps pass OLD_FID + RNL + LR jointly,
  and whose path/current, bundle/field, test, and finite-kernel maps commute
  on actual common-refinement diamonds.          (E3-6)
```

The family must retain all rank, path, support, background, bundle, gauge,
orientation, and frame members.  Separate objectwise nonemptiness is not
enough; `(E3-6)` is one family/equalizer requirement.

This is witness data under the adopted law.  It is neither a missing clause
nor a theorem of impossibility.  The live Q-430 metric class proves only
that extension from the first orbit is not forced.

```text
E3 = PASS
ALL_RANK = NEEDS(F_Q408^all)
LAW_REVISION_NEEDED = false
NEW_DECLARATION_NEEDED = false
```

---

## 4. E4 - exact EQ6 distance

The enlarged first-cycle subdiagram verifies only the corresponding finite
projections.  In particular:

1. no J4 action/Hessian cube exists on `r_01`;
2. no J2 physical reader factorization exists;
3. no completed topology carries J12-J14;
4. no action-derived response map acts on the new-cycle direction;
5. no completed Maxwell/Hodge projection exists.

The joint-equalizer regression therefore remains active.  A P4 term, a
finite faithful kernel, and a finite Ward identity do not form one EQ6 term.

The remaining frontier is correctly ordered:

```text
1  F_Q408^all: all-rank/common-refinement P4 family;
2  B_R1_NATURAL on Ref_01 and then F_Q408^all;
3  B_C1_COMPLETION on the resulting directed core;
4  B_FAITHFULNESS on that completion;
5  B_C2_RESPONSE_BOUNDARY in the same topology;
6  B_C3_MAXWELL_HODGE;
7  the derived physical reader;
8  one simultaneous J1-J15 certificate.          (E4-1)
```

No item in this list is already supplied by the first-cycle member.  The
clause layer remains complete; all eight rows are construction or witness
burdens.

```text
E4 = PASS
JOINT_EQ6 = PARTIAL
FULL_EQ6_TERM = absent
EQ6_DISCHARGED = false
```

---

## 5. E5 - discipline, geometry/rails split, and fresh attacks

### 5.1 Smuggling and the "too easy" question

No response, threshold, fixed point, end-test result, or measured number is
used.  The order is carrier-first: retained background family, actual paths,
actual currents, identity bundle fields, then canonical tests and
certificates.  The full covariant path/background/bundle/frame family is
retained.  No rank, ratio, path, frame, orientation, gauge, or bundle member
is selected.

The member is easy because its source physical cycle carrier is zero, but
the target current and target kernel are nonzero.  It is therefore a real
base inhabitant, not a degenerate member that satisfies all conditions
vacuously.  Pass 2 openly stops before using its vacuous old-image equations
as positive-rank evidence.

### 5.2 Surface geometry versus rails

| Territory | Surface geometry | Rail/certificate | Determination |
|---|---|---|---|
| first cycle | two actual timelike paths with nonzero difference current | parallel-edge incidence | **BUILT PHYSICALLY** |
| U(1) fields | actual retained bundle, coframe, density, connection, curvature | identity pullback equations | **BUILT PHYSICALLY** |
| base test map | no source cycle observable; target cycle visible | `P=0`, zero OLD_FID/RNL/LR | **VALID BASE CERTIFICATES** |
| batching candidate | componentwise paths and fields | product/batching covariance | **TYPED CANDIDATE ONLY** |
| batching metric | no physical direct-sum isometry theorem | formal block diagonal would make squares pass | **NOT BUILT / FORBIDDEN TO ASSUME** |
| all-rank continuation | no positive-source family-wide attachment exhibited | W1/W4 only type candidates | **OPEN PHYSICAL WITNESS** |
| common refinement | Q-418 within each fixed orbit | formal graph union is insufficient | **OPEN ACROSS ORBITS** |

### 5.3 Fresh attack 1 - batching-isometry attack

Try to construct the all-rank family by batching `x_r01` with identity
members.  The W1/W4 coordinates batch, but the RNL proof requires the target
Riesz form to have no old/new cross block.  DoR-019 supplies no such generic
batching isometry and lists its unauthorized promotion as a falsifier.
Choosing `(E3-4)` makes the attack fail exactly at `(E3-5)`.

```text
FRESH_ATTACK_1 = PASS_AS_ATTACK /
  BATCHING_ROUTE_DOES_NOT_CONSTRUCT_P4_MEMBERS
```

### 5.4 Fresh attack 2 - contact-only leakage attack

Let a positive-source old cycle and a new path share only a recorded
endpoint.  Because supports are not disjoint, RNL's antecedent can be false.
Choose an admissible target metric with an old/new cross block as in
`(E3-4)`.  The canonical transported test then has a component along the
new path outside the mapped old region.  LR rejects it even though RNL is
silent.  This confirms that all-rank construction must retain both tests;
neither the identity field horn nor recorded contact closes the gap.

```text
FRESH_ATTACK_2 = PASS_AS_ATTACK /
  LR_IS_INDEPENDENTLY_LOAD_BEARING
```

### 5.5 Regression board

| Regression | Result |
|---|---|
| pure new-cycle profile | **PASS** |
| covariance orbit/moduli | **PASS** |
| all-stage skeleton | **PASS on claimed subcategory** |
| rank-preserving Ref_path | **PASS** |
| cycle-creating upward quotient | **PASS; none used** |
| arbitrary-profile restriction | **PASS with old-image scope** |
| Q-430 old-to-new mixer | **PASS; remains the all-rank obstruction** |
| Q-432 P=id witness | **PASS on rank-preserving scope** |
| bundle/topology and flat holonomy | **PASS** |
| abstract-kernel regression | **PASS** |
| circular-reader regression | **PASS** |
| misstated-nonemptiness regression | **PASS** |
| Hodge-from-isometry regression | **PASS** |
| objectwise-selection regression | **PASS** |
| joint-equalizer regression | **PASS** |

```text
E5 = PASS
TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MACHINERY_APPEAL = false
```

---

## 6. Final disposition

```text
MEMBER = SURVIVES

E1 = PASS
E2 = PASS
E3 = PASS
E4 = PASS
E5 = PASS

ALL_RANK = NEEDS(
  nonempty covariant positive-source primitive-orbit W1/W4 members
  + canonical P passing OLD_FID/RNL/LR
  + actual family-wide common-refinement diamonds;
  generic batching cannot supply them without an unratified metric isometry
)

EQ6_DISTANCE =
  first-cycle B_Q408 and its fixed-rank subdivisions are built;
  full all-rank B_Q408 remains, then B_R1, completed C1, completed
  faithfulness, C2, C3, the derived reader, and one joint J1-J15 term.

PASS2 = CONFIRMED_WITH_NOTES
LAW_REVISION_NEEDED = false
NEW_DECLARATION_NEEDED = false
JOINT_EQ6 = PARTIAL
EQ6_DISCHARGED = false

MEMBER_SELECTED = false
MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARED = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No register, plan, tracker, git, commit, or push action belongs to this lane.
