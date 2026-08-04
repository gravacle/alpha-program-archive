# STAGE 8 TASK 5 / EQ6 - DIAMOND CHECK AND JOINT-ADMISSION TYPING - LANE 1 V001

Date: 2026-08-04
Task: Paste 516 / Task 5 / EQ6
Lane: Codex Lane 1
Custody: hostile review of Lane 2 all-rank build; no adoption or member binding

## Lead result

```text
BUILD = KILLED(G2_CONTACT_SCOPE)

G1 = PASS
G2 = KILL |
  D-sub passes and D-disjoint stops exactly at OLD_FID/RNL/LR;
  D-contact does not stop at LR alone.  OLD_FID remains unproved, and RNL
  still applies on exclusive old/new path regions away from the shared
  endpoint.  Contact silences only some RNL instances.
G3 = PASS / CONSTRUCTION_GAP
G4 = PASS_WITH_CORRECTED_CONTACT_SCOPE
G5 = PASS_WITH_KILLING_FRESH_ATTACK

JOINT_ADMISSION = GAP(
  build a covariant LOCAL_ORTHOGONAL_EXCISION_CERT subfamily whose fixed
  DoR-019 current form is old-image isometric and relatively orthogonal,
  and whose Q-408 Phi map and inverse preserve the actual support split;
  then OLD_FID, RNL, LR, and the diamonds hold jointly
)

JOINT_UNSATISFIABLE = false / TYPE-R |
  the diagonal-metric, support-direct-sum model in Section 3 satisfies all
  three tests simultaneously and is compatible with the adopted clauses.

ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U
```

The Lane 2 build gets the main physical boundary right: W1 path/current and
W4 bundle/field laws commute on actual cycle-creating surface diamonds, but
P4 admission is a joint condition on the fixed metric and support-local
analysis.  Its one defect matters because the task asks for the exact stop.
Endpoint contact does not globally remove relative no-leakage, and it does
not prove old-image fidelity.

The three tests are not mutually contradictory.  A support-direct-sum fixed
carrier makes them commute exactly.  What is missing is an actual,
family-wide construction of that carrier behavior from the retained
DoR-019/Q-408 data, not a revision of the where-law.

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
IS_THE_VERSION_CURRENT = yes, register head Q-441
ARE_ITS_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

The reviewed artifact was verified before reading:

```text
STAGE8_TASK5_EQ6_ALLRANK_W1W4_MEMBERS_LANE2_V001.md
dec994976774bf598e79cd496f6b424d777d2321df2b41c0393219a3247c3ad6
sidecar verification = OK
```

The sealed register is current at Q-441:

```text
QUESTIONS_SETTLED_REGISTER_V001.md
3876e88b9e863867b084227d5369475e4d0f900e64ec0bf5cd630d522a30f791
sidecar verification = OK
```

Load-bearing standards:

| Authority | Verified SHA-256 | Use |
|---|---|---|
| `LOCKED_PROCESS.md` | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | surface geometry versus rails |
| prior all-rank typing | `166002e9178faefe4464f504810553a606ec6465a0e3739a70e50a5d29d8604e` | exact positive-source need; no batching shortcut |
| adopted where-clauses | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | W1/W4 membership |
| final where-clause check | `b4c901f512379251b55d31aae6914d1fce9af6280c8f65081afeabfd4e75f219` | nine regressions; flat holonomy |
| metric V005 / DoR-019 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed `g_K`, Riesz maps, W3 scope |
| continuum package V005 / DoR-020 | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | P4 primitive rule and joint equalizer |

All available sidecars for these workspace artifacts verified `OK`.

### 0.2 Verdict table

| Item | Verdict | Reason |
|---|---|---|
| G1 rank-preserving diamond | **PASS** | actual path subdivision, current additivity, W3 isometry, support, and U(1) pullbacks commute at geometry |
| G2 cycle-creating diamonds | **KILL** | disjoint stop is exact; contact stop is understated because OLD_FID and exclusive-region RNL remain open before LR |
| G3 gap or theorem | **PASS / GAP** | a joint satisfying model exists, refuting structural impossibility; actual nonemptiness waits on a local-orthogonal/excision construction |
| G4 W1/W4 stop and EQ6 | **PASS WITH CORRECTION** | raw W1/W4 family and global `F_Q408^all` stop are right after D-contact is restored to all three tests |
| G5 discipline and attacks | **PASS WITH FINDING** | no tuning or selection; contact-localization attack kills the scope statement; Gram-Schmidt attack confirms that `S` cannot be repaired algebraically |

---

## 1. G1 - rank-preserving subdivision diamond

### 1.1 Geometry and incidence

Start with one admitted first-cycle member.  Subdivide one actual oriented
path at two distinct interior parameters `s` and `t`.  The two one-step
subdivisions have a common physical refinement at the ordered union of the
cut parameters.  No chord is added or removed, so every carrier has the same
cycle rank.

For every test one-form `a`, path-current additivity gives

```text
integral_gamma a
 = sum_(children at s) integral_child a
 = sum_(common children) integral_child a
 = sum_(children at t) integral_child a.        (G1-1)
```

In the conserved-carrier identifications, each `S` is the identity.  On the
physical test quotient Q-418 supplies `P=id`; W3 gives

```text
S^* R_K,target S = R_K,                         (G1-2)
```

and the adjoint restriction square.  Consequently

```text
OLD_FID = PASS,
RNL = PASS,
LR = PASS,
P_t,st P_0,t = id = P_s,st P_0,s.              (G1-3)
```

### 1.2 Geometry attacks

**Support.**  The union of child images equals the parent image.  A
self-intersection does not change the current identity because the
parameter-ordered children retain orientation and multiplicity.

**Rank-two/relabeling.**  Edge and child relabeling conjugate both routes;
no child ordering is selected beyond the physical path parameter order.

**Pendant interaction.**  Subdivision adds only bivalent vertices.  It does
not create a conserved pendant coefficient or change the cycle quotient.

**Reality/orientation.**  Reversal reverses child order and all signs
together.  Complex conjugation acts on both bundle routes identically.

**Bundle geometry.**  The same actual bundle is pulled back through the same
subdivided path image.  Bundle lifts, coframe, density, connection,
curvature, and `c_1` obey pullback associativity at the common target.

This is an actual surface diamond, not a free-category or batching
surrogate.

```text
G1 = PASS
D_SUBDIVISION = ADMITTED
```

---

## 2. G2 - the two cycle-creating diamonds

### 2.1 Disjoint two-corridor diamond

Let actual nonzero cycle currents `c_U,c_V` lie in disjoint relatively
compact surface corridors.  Tree edges may connect the record graph without
changing its cycle carrier.  The four carriers are

```text
K_G0 = 0,
K_GU = R c_U,
K_GV = R c_V,
K_GUV = R c_U direct-sum R c_V.                 (G2-1)
```

The positive-source maps are the geometrically fixed inclusions

```text
S_UV(c_U)=c_U,
S_VU(c_V)=c_V.                                  (G2-2)
```

W1 incidence, support, actual-current pushforward, covariance, and
restriction all pass.  W4's same-surface bundle lifts, coframe/density,
connection/curvature, characteristic class, reality, and common pullbacks
also pass.  The raw diamond commutes.  Its outer cycle map is `0=0`, but
both target cycles remain nonzero and visible.

Write the fixed source and target current forms as

```text
g_U(c_U,c_U)=alpha_0,
g_V(c_V,c_V)=delta_0,

[g_UV]_(c_U,c_V)
  = [[alpha,zeta],[conj(zeta),delta]],
alpha>0,
delta>0,
alpha*delta-|zeta|^2>0.                         (G2-3)
```

Then OLD_FID on the two upper legs is exactly

```text
alpha=alpha_0,
delta=delta_0.                                  (G2-4)
```

W3 is rank-preserving and proves neither equation for these rank-increasing
legs.  On the favorable slice `(G2-4)`, a source-local test with
`Phi_U(a_U)=theta_U c_U` gives

```text
g_UV(S_UV Phi_U(a_U),c_V)=theta_U zeta.         (G2-5)
```

Since the corridors are disjoint, RNL forces `zeta=0`; the other leg gives
the conjugate condition.  In an `Abar=id` chart the canonical test has

```text
P_UV(a_U) proportional to
  (1,conj(zeta)/alpha_0),                       (G2-6)
```

so nonzero `zeta` also violates LR.  Even at `zeta=0`, LR requires the
independent support-excision equation

```text
Phi_UV^(-1) S_UV Phi_U(Tbar_U(O))
  subset Tbar_UV(F_UV(O)).                     (G2-7)
```

No ratified all-rank theorem supplies `(G2-7)`.

Therefore the disjoint diamond stops exactly and jointly at:

```text
OLD_FID + RNL + LR.                             (G2-8)
```

Nothing derivable was left before the stop: the complete W1/W4 geometry,
bundle data, and raw diamonds were already executed.

```text
D_DISJOINT = CONFIRMED_STOP
```

### 2.2 Endpoint-contact diamond: the scope defect

Now let the closures of the old and new corridors meet only at one recorded
endpoint `q`.  The W1/W4 calculations above still pass.  However, this
geometric change proves neither old-image fidelity nor global relative
no-leakage.

First, the stage metrics are still of the form `(G2-3)`, so OLD_FID still
requires `(G2-4)`.  Endpoint contact has no bearing on source and target
current norms.

Second, RNL quantifies over every local old region `O` and every target
cycle region `W` disjoint from `F(O)`.  If `O` contains `q`, the antecedent
can be false, exactly as Lane 2 states.  But each distinct cycle has an
exclusive interior segment away from `q`.  Choose `O_U` around an exclusive
old segment and `W_V` around an exclusive new segment.  Then

```text
F(O_U) intersect W_V = empty,                  (G2-9)
```

and `(G2-5)` applies unchanged.  Thus nonzero `zeta` still fails RNL.
Contact silences only the subset of RNL tests whose chosen regions contain
the shared endpoint.

Finally, even after granting OLD_FID and `zeta=0`, the canonical test can
have a representative on an exclusive new-path segment.  LR remains the
independent final test.

The correct contact statement is therefore:

```text
D_CONTACT =
  W1/W4 PASS;
  P4/X4 STOPPED_AT(OLD_FID + RNL + LR),
  with RNL silent only on contact-containing local pairs
  and LR independently load-bearing.            (G2-10)
```

Lane 2 instead records `STOPPED_AT(LR_on_each_positive_source_leg)`.  That
scope is not established.  It would be a valid conditional statement only
after explicitly granting OLD_FID and every non-contact RNL instance.

```text
G2 = KILL(CONTACT_STOP_UNDERSTATED)
D_SUBDIVISION = PASS
D_DISJOINT = PASS_AS_STOP
D_CONTACT = KILLED_AND_CORRECTED
```

---

## 3. G3 - decisive joint-admission typing

### 3.1 The three tests are jointly satisfiable

To test structural impossibility, use the same actual two-corridor geometry
but equip its fixed-carrier model with the allowed support-direct-sum data:

```text
K_UV = K_U direct-sum K_V,
R_UV = R_U direct-sum R_V,

Tbar_UV = Tbar_U direct-sum Tbar_V,
Phi_UV = Phi_U direct-sum Phi_V,                (G3-1)

S_U(x)=(x,0),
S_V(y)=(0,y).
```

The forms are positive, real/Hermitian, covariant under exchange, and use
the same units as the sources.  They are permitted by DoR-019; that decision
does not force a nonzero off-diagonal term.

Direct computation gives

```text
S_U^* R_UV S_U = R_U,
S_V^* R_UV S_V = R_V,                           (G3-2)

g_UV(S_U Phi_U(a),c_V)=0,
g_UV(S_V Phi_V(b),c_U)=0,                       (G3-3)

P_U=Phi_UV^(-1) S_U Phi_U = support inclusion_U,
P_V=Phi_UV^(-1) S_V Phi_V = support inclusion_V. (G3-4)
```

Equations `(G3-2)` through `(G3-4)` are OLD_FID, RNL, and LR.  The path,
bundle, field, and test maps commute componentwise around the diamond.

This is not an inhabitance proof for the program's fixed data: the current
stack does not prove that an actual retained surface member realizes
`(G3-1)`.  It is a model of the adopted clauses and metric constraints.
Therefore it decisively refutes a theorem that the three tests are jointly
unsatisfiable.

```text
JOINT_UNSATISFIABLE = false / TYPE-R
STRUCTURAL_HORN = REFUTED_BY_(G3-1)--(G3-4)
```

### 3.2 Exact construction route

The missing constructive object can be stated without selecting a metric
coefficient or weakening a test:

```text
LOCAL_ORTHOGONAL_EXCISION_CERT(r) :=
  LOE1  S_r^* R_target S_r = R_source;
  LOE2  the transported local-analysis image is orthogonal to every
        disjoint new-cycle support sector;
  LOE3  Phi_target^(-1) S_r Phi_source preserves the mapped local-support
        subspaces;
  LOE4  LOE1-LOE3 are covariant, reality-compatible, restriction-natural,
        and commute on actual common-refinement diamonds. (G3-5)
```

A route to `(G3-5)` is:

1. choose no path or metric by a response consequence;
2. construct an actual geometric two-corridor refinement family first;
3. compute the fixed A4 current form on its realized current images;
4. prove an isometric, relatively orthogonal old/new decomposition on a
   nonempty covariant subfamily;
5. prove Q-408 support excision for `Phi` and `Phi^-1` on that same family;
6. run the contact-relative version on exclusive segments modulo the shared
   endpoint;
7. verify all actual diamonds before admitting any member.

If steps 4 or 5 fail on a candidate, reject it.  Do not change `R_K`, rotate
the physical current embedding, enlarge support artificially, or select a
path after inspecting the desired certificate.  Nonemptiness of the
subfamily produced by this route is the unresolved construction.

This is more informative than merely restating `OLD_FID+RNL+LR`: it names
the two generators the joint condition needs - a fixed-form local
orthogonal decomposition and support excision of the Q-408 analysis map.

```text
G3 = PASS
JOINT_ADMISSION = GAP(LOCAL_ORTHOGONAL_EXCISION_CERT)
```

---

## 4. G4 - exact W1/W4 and EQ6 stop

The raw W1/W4 positive-source family is genuinely nonempty on the two
surface constructions.  It contains actual paths and currents, actual
bundle lifts, positive density, full-rank coframes, connection/curvature,
and characteristic-class pullbacks.  The relative certificates are not W1
or W4 fields; they are the physical P4 admission gate over the fixed
DoR-019/Q-408 carrier.

After correcting D-contact, the exact subfamily remains

```text
F_pos^actual = {
  actual positive-source W1/W4 tuples x_r:
  OLD_FID_r and RNL_r and LR_r,
  all bundle certificates,
  all actual diamonds
}.                                               (G4-1)
```

No artifact proves `(G4-1)` nonempty.  The all-rank object is therefore

```text
F_Q408^all =
  a nonempty covariant family over every required positive-source primitive
  orbit, contained in F_pos^actual, closed under composition and actual
  common refinement.                            (G4-2)
```

The corrected fiber distance is unchanged in substance:

1. construct `(G4-2)`;
2. extend B_R1 action/Hessian/reducing-domain naturality over it;
3. extend C1, completed faithfulness, and C2 response boundary in one
   topology;
4. construct C3/Maxwell-Hodge and the physical reader;
5. prove one simultaneous J1-J15 equalizer term.

The first-cycle family and rank-preserving subdivision diamond remain
banked.  No downstream object consumes a stopped cycle-creating candidate.

```text
G4 = PASS_WITH_CORRECTED_CONTACT_SCOPE
ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U
LAW_REVISION_NEEDED = false
```

---

## 5. G5 - discipline, geometry/rails split, and fresh attacks

### 5.1 Smuggling and the "too easy" audit

The construction order is target-blind: actual surface paths and bundles
are fixed before the metric/test equations are inspected.  No response,
threshold, fixed point, alpha consequence, or measured number appears.  No
rank, path, frame, orientation, gauge, metric coefficient, or computation
member is selected.

The raw W1/W4 diamonds are easy because same-surface pullback functoriality
is exact.  P4 admission is not made easy by that rail equality.  The outer
`0=0` base square is correctly prevented from laundering either positive-
source side.

### 5.2 Surface geometry versus rails

| Layer | Surface geometry | Rail/certificate | Determination |
|---|---|---|---|
| subdivision | actual path cut and common ordered refinement | identity carrier squares | **ADMITTED PHYSICAL DIAMOND** |
| disjoint fusion | actual nonzero currents in disjoint corridors | outer incidence/bundle squares | **RAW W1/W4 BUILT; P4 STOPPED** |
| contact fusion | actual cycles sharing one endpoint | same outer rail square | **RAW W1/W4 BUILT; P4 STOPPED AT ALL THREE TESTS** |
| current metric | fixed A4-derived source/target forms | OLD_FID and RNL equations | **FAILURE-CAPABLE / OPEN** |
| local analysis | actual Q-408 support classes | LR equation | **FAILURE-CAPABLE / OPEN** |

The stop is not a rail artifact.  It concerns a fixed physical current form
and actual support transport.  Conversely, path/current and bundle
commutation alone are rails and do not prove admission.

### 5.3 Fresh attack 1 - contact localization

The shared endpoint does not make the two whole cycles support-identical.
Choose exclusive old/new interior neighborhoods as in `(G2-9)`.  RNL becomes
active again and detects the same `zeta` term as the disjoint diamond.  This
fresh attack kills the LR-only contact classification while leaving the raw
geometry intact.

```text
FRESH_ATTACK_1 = KILL_OF_D_CONTACT_SCOPE
```

### 5.4 Fresh attack 2 - forbidden Gram-Schmidt repair

Try to repair a nonzero `zeta` by changing the old current embedding to

```text
S'_U(c_U)=c_U-(conj(zeta)/delta)c_V.             (G5-1)
```

This can make the metric pairing with `c_V` vanish algebraically.  But its
actual target current is

```text
J(S'_U c_U)=J(c_U)-(conj(zeta)/delta)J(c_V),    (G5-2)
```

which differs from the pushforward of the source current and has support in
the new corridor.  It violates W1 current equality and support before any
relative certificate is tested.  Thus the gap cannot be closed by rotating
`S`; it must be closed by a genuine fixed-carrier member satisfying
`(G3-5)`.

```text
FRESH_ATTACK_2 = PASS_AS_ATTACK /
  ALGEBRAIC_ORTHOGONALIZATION_FORBIDDEN
```

### 5.5 Regression board

| Regression | Result |
|---|---|
| abstract-kernel substitution | **PASS** |
| circular `P`/reader construction | **PASS** |
| false nonemptiness | **PASS** |
| cycle-creating restriction | **PASS; target cycles retained** |
| covariance-orbit overclaim | **PASS** |
| all-stage skeleton overclaim | **PASS; all-rank remains partial** |
| Q-430 mixer | **PASS; rejected by RNL/LR** |
| Q-432 `P=id` | **PASS on D-sub** |
| clause nonemptiness overreach | **PASS** |
| flat holonomy | **PASS; bundle equality is not metric admission** |
| generic batching shortcut | **PASS; not used** |
| outer-square laundering | **PASS; rejected** |
| joint-equalizer regression | **PASS** |

```text
G5 = PASS_WITH_KILLING_FRESH_ATTACK
TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MACHINERY_APPEAL = false
```

---

## 6. Final disposition

```text
G1 = PASS
G2 = KILL(CONTACT_STOP_UNDERSTATED)
G3 = PASS / CONSTRUCTION_GAP
G4 = PASS_WITH_CORRECTED_CONTACT_SCOPE
G5 = PASS_WITH_KILLING_FRESH_ATTACK

BUILD = KILLED(G2_CONTACT_SCOPE)

JOINT_ADMISSION = GAP(
  LOCAL_ORTHOGONAL_EXCISION_CERT:
    old-image isometry
    + relative old/new orthogonality
    + support-local Phi/Phi^-1 transport
    + covariance/restriction/actual-diamond naturality
)

JOINT_UNSATISFIABLE = false / TYPE-R
ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

SURVIVES =
  rank-preserving admitted diamond;
  actual disjoint and contact W1/W4 candidate geometry;
  disjoint OLD_FID/RNL/LR stop;
  corrected contact OLD_FID/RNL/LR stop;
  exact local-orthogonal/excision construction route.

LAW_REVISION_NEEDED = false
NEW_CLAUSE_NEEDED = false
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
