# STAGE 8 TASK 5 / EQ6 — Q-408 PRIMITIVE GENERATOR EXHIBIT — LANE 2 V004

Date: 2026-08-04  
Lane: Codex Lane 2  
Task: 5 / EQ6 / `B_Q408_REFINEMENT`  
Custody: corrected-spec builder after Q-432; hostile check required

## Lead result

```text
CONSTRUCTIONS =
  R_TEST_TRANSPORT:
    BUILT_AS_CANONICAL_MAP
    + FAILURE_CAPABLE_SUPPORT_LOCAL_RANGE_CERTIFICATE;

  R_RIESZ_LOCALITY:
    BUILT_AS_RELATIVE_OLD_IMAGE_FIDELITY
    + RELATIVE_NO_LEAKAGE_CERTIFICATE

P_ID_OVERREACH_WITNESS = ADMITTED
Q430_OLD_TO_NEW_SECTOR_MIXER = REJECTED

CLAUSE_CANDIDATES =
  R_PATH_CURRENT_SUPPORT_CORRESPONDENCE:
    COMPLETE_DOR_GRADE_CANDIDATE / PROPOSED_NOT_ADOPTED;

  R_LOCAL_FIELD_MEMBER_FAMILY:
    COMPLETE_DOR_GRADE_CANDIDATE / PROPOSED_NOT_ADOPTED;
    TRANSPORT_AFTER_MEMBER = CONDITIONALLY_DERIVED

ACTUAL_FINITE_AND_Ref_path_CORE = BUILT / TYPE-P
Ext_cycle_FULL_MEMBER = OPEN / TYPE-U
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN
C1_RESUMPTION = N/A
MEMBER_BOUND = false

READY_FOR_HOSTILE_CHECK = yes
```

V004 deletes V003's global Riesz-orthogonality postulate.  Locality is now
relative to what the generator actually transports.  A nonlocal metric on
two already-present disjoint cycles is allowed when the same metric appears
at both ends and the physical test transport is `P=id`.  What is forbidden
is **new leakage caused by the refinement**: the transported local-analysis
image may not acquire pairing or test support on a physically disjoint new
sector.

The correction separates the four Package-R territories exactly as Q-432
requires.  The test map and its locality predicates are constructions from
ratified carriers once a candidate path/current relation is supplied.  The
path/current relation itself and the compatible new-cell field members are
physical declarations.  Neither declaration candidate is selected or
adopted here.

---

## 0. Preflight, authorities, and register sweep

### 0.1 Three-line preflight

```text
DOES THE OBJECT EXIST?  The two constructions and two clause candidates are
                        built below; no full Ext_cycle member is bound.
IS THE VERSION CURRENT? YES, through send-time register head Q-433; Q-433
                        adds future Task 7 and does not alter this Task-5
                        construction.
ARE ITS INPUTS PRESENT? YES: the sealed Q-432 check, V003, V005, Q-408,
                        DoR-019, Ref_path, C1, and DoR-020.
PREFLIGHT = PASS
```

The Q-432 check was hash- and seal-verified before reading:

```text
STAGE8_TASK5_EQ6_V003_CHECK_AND_PACKAGE_R_TYPING_LANE1_V001.md
SHA-256 = 99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757
SEAL = PASS
```

Verified authorities:

| Authority | SHA-256 | Use |
|---|---|---|
| locked process with Q-427 rule | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody and geometry/rails split |
| register at send-time Q-433 | `f82c4e28938a4471fd4dadc91153637d8b2ad6c20e9f4a3a9a935409f8c18eb4` | current scope; Q-433 reconciled |
| V003 check and corrected typing | `99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757` | governing correction and two/two split |
| V003 | `74d88d6d450e15a8aed2c0f3db6d2d8c8b80f440b8cb0eab81845dfebcb6069d` | bounded source; overreach removed |
| field signature V005 / DoR-015 object | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | actual paths, currents, supports, fields |
| Q-408 current/kernel realization | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | analysis maps, physical kernels, support |
| carrier metric V005 / DoR-019 object | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed Riesz maps and units |
| derived `Ref_path` square | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | physical rank-preserving transport |
| C1 completion build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | maximal built physical core |
| frontier map | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | B_Q408 root contract |
| DoR-020 | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | conditional package and no-binding rule |

### 0.2 Register sweep

```text
Q-297  complete conserved ker(B^T) current family is physical;
Q-355  general cycle-creating upward quotient is unavailable;
Q-384  carrier metric/Riesz maps exist with their stated W3 scope;
Q-408  finite physical currents, analysis maps, kernels, and supports exist;
Q-418  rank-preserving path subdivision has P=id and exact squares;
Q-425  Ref_0 is the maximal built physical refinement category;
Q-427  actual surface geometry and rail compliance must be separated;
Q-428  V001 killed on the new-cycle kernel and surface claims;
Q-430  V002 killed by old-to-new support leakage through the Riesz map;
Q-431  V003 names locality/support as the governing issue;
Q-432  V003 global orthogonality refuted; relative no-leakage governs;
Q-433  future Task 7 added; Tasks 1-6 and this Task-5 scope unchanged.
```

No entry constructs a physical cycle-creating path relation or declares
compatible local fields on genuinely new cells.  Those are the two clause
candidates below.

### 0.3 Bearing symbols

```text
M_G                 = actual source surface member;
gamma_(G,e)         = actual oriented edge path;
K_G=ker(B_G^T)      = complete conserved current carrier;
J_G(c)              = actual Q-408 current distribution;
Supp_G(c)           = its physical support;

Tbar_G              = Q-408 surface-visible connection-test quotient;
Tbar_G(O)           = classes with representatives supported in O;
Abar_G:Tbar_G->K_G* = finite analysis isomorphism;
R_G:K_G->K_G*       = fixed DoR-019 Riesz map;
Phi_G=R_G^(-1)Abar_G;

f_R,F_R             = proposed actual path/region relation;
S_R                 = its induced injective old-current map;
P_alg,R             = canonical constructed test transport;

OLD_FID_R           = old-image metric fidelity predicate;
RNL_R                = relative no-leakage predicate;
LR_R                 = support-local range predicate;

global g(K(O),K(V)) orthogonality != relative no-leakage;
metric locality != physical test-transport locality;
constructible map/certificate != declared physical member.
```

---

## 1. Z1 — the two constructibles

### 1.1 Ratified local-analysis carriers

At each actual finite stage, retain the V003 objectwise local sectors

```text
K_G(O):={c in K_G:Supp_G(c) subset O},
Tbar_G(O):=q_G{a:supp(a) subset O}.              (Z1-1)
```

These are constructed from V005 paths and Q-408 distributions.  They do not
impose any condition on `g_K` between arbitrary disjoint current vectors.

Let a candidate path/current clause provide `f_R,F_R,S_R` as typed in
Section 2.  Every operation below then uses only fixed ratified maps.

### 1.2 Construction A — canonical test transport

Define

```text
P_alg,R
 :=Phi_G'^(-1) S_R Phi_G
  =Abar_G'^(-1)R_G'S_RR_G^(-1)Abar_G.           (Z1-2)
```

This is not an authored coordinate.  `Abar` and `R` are isomorphisms on the
finite surface-visible carrier, so `(Z1-2)` exists uniquely and is bounded.
The actual orientation/path clause fixes the otherwise possible component
signs.

The construction carries the following certificates.

**T-1 — arbitrary-profile kernel square.**  For every fine profile `H'`,

```text
Kern_G'(H')[P_alg,R a,P_alg,R b]
 =Kern_G(S_R^*H'S_R)[a,b].                      (Z1-3)
```

This follows by substituting `Phi_G'P_alg,R=S_RPhi_G` into Q-408's actual
kernel formula.  New-cycle profiles remain visible on target tests outside
`image(P_alg,R)`.

**T-2 — old-current pairing.**  Define the relative old-image fidelity test

```text
OLD_FID_R:
S_R^* R_G' S_R=R_G.                             (Z1-4)
```

When `(Z1-4)` passes,

```text
Abar_G=S_R^*Abar_G'P_alg,R,                     (Z1-5)
J_G'(S_Rc)[P_alg,R a]=J_G(c)[a].                (Z1-6)
```

This is a test of fixed carrier data, not permission to change either
metric.

**T-3 — support-local range.**  Define the failure-capable predicate

```text
LR_R(O):
P_alg,R(Tbar_G(O)) subset Tbar_G'(F_R(O))        (Z1-7)
```

for every actual local source region.  A candidate is physically admitted
only if all `(Z1-7)` checks pass.  The construction does not call an
algebraic map support-local before this test.

**T-4 — covariance, reality, units, and composition.**  Ratified covariance
of `Abar,R,S` gives covariance of `(Z1-2)`.  Conjugation and orientation act
on both sides together.  The two Riesz maps provide exactly the declared R4
unit conversion, with no implicit cross-sector unit.  For composable
candidates,

```text
P_alg,S P_alg,R
 =Phi_G''^(-1)S_S Phi_G' Phi_G'^(-1)S_R Phi_G
 =P_alg,(S compose R).                           (Z1-8)
```

Thus the map construction is complete.  Whether a proposed physical clause
candidate passes its local-range and old-pairing tests remains genuinely
failure-capable.

```text
R_TEST_TRANSPORT =
  CONSTRUCTED_UNIQUELY_FROM_RATIFIED_CARRIERS_AFTER_R1_CANDIDATE
R_TEST_TRANSPORT_AUTHORSHIP = false / TYPE-R
R_TEST_TRANSPORT_PHYSICAL_ADMISSIBILITY = OLD_FID_R + LR_R
```

### 1.3 Construction B — corrected relative Riesz locality

For `a in Tbar_G(O)`, the transported local-analysis vector is

```text
x_R(a):=S_R Phi_G(a) in K_G'.                   (Z1-9)
```

For every target cycle `n in K_G'(V)` whose physical support is disjoint
from the mapped source support, define

```text
RNL_R(O,V):
g_(K,G')(x_R(a),n)=0
for all a in Tbar_G(O), n in K_G'(V),
whenever F_R(O) intersect V=empty.              (Z1-10)
```

This is Q-432's relative no-leakage condition.  It tests only the image that
the generator actually transports.  It says nothing about
`g_(K,G')(c_1,c_2)` for arbitrary pre-existing localized currents.

The condition is constructible on the fixed ratified carriers: form the
finite subspace `Phi_G(Tbar_G(O))`, apply `S_R`, restrict `R_G'` to it, and
evaluate against the finite target sector `K_G'(V)`.  Equivalently,

```text
g_(K,G')(S_RPhi_G(a),n)
 =<Abar_G'P_alg,R a,n>.                          (Z1-11)
```

Hence `RNL_R` is the exact test that the constructed old test acquires no
pairing with a physically disjoint target current.  `LR_R` checks the
stronger geometric statement that the test class itself has a supported
representative in the mapped region.  Both are decidable finite predicates
once the R1 candidate supplies `F_R`.

The complete corrected Riesz/test admissibility certificate is

```text
REL_R={OLD_FID_R,RNL_R,LR_R}.                    (Z1-12)
```

It is relative and failure-capable.  No global orthogonality axiom is
present.

### 1.4 The `P=id` overreach witness is admitted

Take two already-present cycles with disjoint supports `U,V` and

```text
K_G=R e_U direct-sum R e_V,
Abar_G=id,
R_G=[[1,epsilon],[epsilon,1]],
0<|epsilon|<1.                                   (Z1-13)
```

Apply a rank-preserving physical `Ref_path` map and identify its carriers:

```text
S_R=id,
R_G'=R_G,
P_alg,R=R_G^(-1)R_G=id.                         (Z1-14)
```

`OLD_FID_R` passes.  `LR_R` passes because `P=id`.  Although

```text
g_K(e_U,e_V)=epsilon !=0,                        (Z1-15)
```

the relative condition uses the local-analysis vector.  For a local test
coordinate `a=e_U^*`,

```text
g_K(Phi_G(a),e_V)
 =<R_G R_G^(-1)e_U^*,e_V>
 =<e_U^*,e_V>=0.                                (Z1-16)
```

Thus `RNL_R` passes exactly as Q-432 requires.  The off-diagonal metric is
not outlawed; refinement has introduced no leakage.

```text
P_ID_OVERREACH_COUNTEREXAMPLE = ADMITTED
GLOBAL_RIESZ_ORTHOGONALITY_REQUIRED = false / TYPE-R
```

### 1.5 The original old-to-new mixer still fails

Take the Q-430 cycle-creating carrier

```text
K_G=R,
K_G'=R e_U direct-sum R e_V,
S_Rx=(x,0),
R_G=1,
R_G'=[[1,epsilon],[epsilon,1]],
0<|epsilon|<1,                                   (Z1-17)
```

with the new target cycle supported in disjoint `V`.  Then

```text
P_alg,R(1)=(1,epsilon),                         (Z1-18)
g_(K,G')(S_RPhi_G(1),e_V)=epsilon !=0.          (Z1-19)
```

So both `RNL_R` and `LR_R` fail.  `OLD_FID_R` alone passes because the old
block is unchanged; this confirms why all three relative tests are needed.

```text
Q430_SECTOR_MIXER = REJECTED
RELATIVE_NO_LEAKAGE_REGRESSION = PASS
```

---

## 2. Z2 — the two declaration candidates

Neither candidate below is selected.  Each is a DoR-grade clause candidate
whose alternatives, void conditions, geometry anchors, and downstream proof
obligations are explicit.

### 2.1 Clause candidate R1 — path/current support correspondence

#### Clause text

For every primitive cycle-creating rail arrow `r:G->G'`, declare a nonempty
covariant family `PathRel(r)` of actual local surface refinements.  Each
member consists of

```text
f_R:M_G->M_G'             proper orientation-compatible local map,
F_R:Loc_G->Loc_G'         induced support map,
s_R:C_1(G)->C_1(G')       signed path-chain map,
S_R=s_R|K_G               injective old-current map,                (Z2-1)
```

and satisfies

```text
f_R compose gamma_(G,e)
 = ordered target-child path chain prescribed by s_R;

partial_G' s_R=s_R^0 partial_G;

J_G'(S_Rc)=f_(R*)J_G(c);
Supp_G'(S_Rc) subset F_R(Supp_G(c));             (Z2-2)
```

with E_post orientation, reality, relabeling, composition, and actual
common-refinement covariance.  DoR-008 restriction to every sealed finite
path/current result is exact.  All old record-visible cycles survive; new
target cycles remain physical outside `image(S_R)`.

This clause declares the missing **where-content**.  It does not declare a
test map, alter the Riesz metric, or choose a field member.  Those operations
belong to the construction and R4 rows.

#### Choice table

| Alternative | Declared geometry | Minimal carrier rationale | Void condition |
|---|---|---|---|
| R1-E embedded local subdivision family | proper local embeddings; each old path is an ordered union of target child paths | strongest literal realization of refinement | unrelated supports, deleted old cycle, failed orientation, or empty covariant family |
| R1-I same-carrier local attachment family | `f_R=id` on the old physical carrier; old paths subdivide in place and new target paths/cells attach with actual local support | permits cycle creation without inventing a cross-carrier identification | nonlocal attachment, overlapping support that defeats the declared incidence, or failure of `(Z2-2)` |
| R1-X reject cycle-creating primitive | no physical generator on that rail arrow | honest alternative if no physical correspondence exists | any later use of the rejected arrow as physical |

No alternative is recommended.  A declared family must remain family-wide;
no path, chart, orientation, refinement, or orbit representative is chosen.

#### Geometry anchor and falsifier

The source and target paths are V005 A2 paths, the current is Q-408's actual
distribution, and the cycle carrier is V005's complete `ker(B^T)`.  The
unrelated-path witness is the standing falsifier: a signed injection between
cycles in unrelated regions satisfies the rail but cannot inhabit R1.

```text
R1_PATH_CURRENT_CLAUSE = COMPLETE_CANDIDATE
R1_TYPING = DECLARABLE_ONLY / PROPOSED_NOT_ADOPTED / TYPE-U
```

### 2.2 Clause candidate R4 — compatible local-field member family

#### Clause text

For every R1 member, declare a nonempty covariant family `FieldExt(R)` of
target new-cell field members

```text
(e_G',mu_G',A_G',F_G')                          (Z2-3)
```

where `e` is the ratified coframe species, `mu` the positive density,
`A` the connection, and `F=Curv(A)` the curvature.  Each member:

1. agrees with the source fields on the old image under `f_R`;
2. has the declared R4 unit classes and positive density;
3. preserves local support, E_post orientation, reality, and endpoint
   covariance;
4. is covariant over the full R1 family and composes on actual refinement
   diamonds;
5. satisfies coframe/density duality and curvature formation before it may
   enter the physical generator;
6. restricts to every sealed finite field/current result exactly under
   DoR-008.

The new-cell values are member data.  Transport on the old image is not an
independent choice.

#### Choice table

| Alternative | Declared member family | Minimal carrier rationale | Void condition |
|---|---|---|---|
| R4-E compatible extension family | full family of positive, unit-correct coframe/density and connection members extending source data | declares exactly the missing new-cell fields | empty family, failed old-image agreement, failed units/reality, or curvature mismatch |
| R4-T compatible torsor family | affine connection-extension torsor with all compatible coframe/density members retained | preserves no-selection where connection extensions are nonunique | selected torsor member, noncovariant stabilizer, or no curvature-compatible element |
| R4-X reject the R1 member | no local-field lift for that path/current relation | prevents a geometric path relation from being mislabeled a full field generator | subsequent use of the rejected relation in P4/Q-408 |

Again no alternative is recommended and no member is selected.

#### Conditional derivation of transport

Fix only for the proof an arbitrary declared pair `(R,FieldExt member)`.  The
physical restriction maps are forced by the actual local map:

```text
eta_cof,R   =f_R^* on coframes,
eta_dens,R  =f_R^* on densities,
eta_conn,R  =f_R^* on connections,
eta_curv,R  =f_R^* on curvature.                (Z2-4)
```

Functorial pullback gives identity and composition.  Locality of `f_R`
gives support preservation.  Reality and E_post commute because the clause
requires `f_R` to preserve their structures.  Naturality of curvature gives

```text
eta_curv,R(F_A)
 =f_R^*(F_A)
 =F_(f_R^*A)
 =F_(eta_conn,R A),                              (Z2-5)
```

and pullback of the coframe/density pairing gives its duality square.
Therefore field transport is derived after the member is declared; it is not
another authored coordinate.

At an actual common-refinement diamond, functoriality of pullback makes both
routes agree provided the R1 and R4 clause members satisfy their declared
diamond equalities.  DoR-008 is exact on the bottom finite member.

```text
R4_LOCAL_FIELD_CLAUSE = COMPLETE_CANDIDATE
R4_MEMBER_TYPING = DECLARABLE_ONLY / PROPOSED_NOT_ADOPTED / TYPE-U
R4_TRANSPORT_AFTER_MEMBER = DERIVED_CONDITIONALLY / TYPE-P
```

### 2.3 Package-R board after the two/two split

| Row | Status | What remains at ratification |
|---|---|---|
| R1 path/current support | clause candidate complete | adopt one family-level alternative or reject; no member selected here |
| R2 test transport | canonical construction complete | run `OLD_FID_R` and `LR_R` on the adopted R1 family |
| R3 Riesz locality | relative certificate construction complete | run `RNL_R` on the fixed DoR-019 metric; no metric choice permitted |
| R4 local fields | clause candidate complete; transport derived conditionally | adopt one family-level member clause or reject; prove nonempty joint family |

```text
PACKAGE_R_DECLARATION_COUNT = 2
PACKAGE_R_CONSTRUCTION_COUNT = 2
NEW_ROOT_CREATED = false
```

---

## 3. Z3 — surviving content on the corrected specification

### 3.1 Actual finite and `Ref_path` core

For a rank-preserving subdivision of an already realized path, the target
children are parameter subpaths whose ordered union is the parent.  With
`S_R` the oriented child-current map and `P=id`,

```text
Abar_G=S_R^*Abar_G'P,
J_G'(S_Rc)[Pa]=J_G(c)[a],
S_R^*R_G'S_R=R_G.                               (Z3-1)
```

The actual current distribution and its support are unchanged.  The
constructed `(Z1-2)` gives `P_alg=P=id`; all of `OLD_FID_R`, `RNL_R`, and
`LR_R` pass.  Q-408's physical kernel square follows exactly.  No global
orthogonality between disjoint pre-existing currents is asserted.

Identity, admitted surface isomorphisms, finite restriction,
zero-extension, Gate-4 descent, and `Ref_path` retain the V003 proofs after
deleting its X1-10 overreach.

```text
Ref_0_GEOMETRY_LOCALITY_SUPPORT = PROVEN / TYPE-P
GLOBAL_DISJOINT_CURRENT_ORTHOGONALITY = false / TYPE-R
```

### 3.2 Cycle creation and real target kernels

For every R1 candidate, `P_alg` and the relative tests are now defined.  If
`OLD_FID_R`, `RNL_R`, and `LR_R` all pass and an R4 member exists, then
`(Z1-3)` is a physical old-image restriction square.  It does not claim
equality on every fine test.

If a fine profile is supported only on a new target cycle, its pullback to
the old image can vanish while its target Q-408 kernel remains nonzero.
Nothing in R1--R4 deletes or quotients that new physical support.

```text
Ext_cycle_RAIL_SQUARE = PROVEN
Ext_cycle_PHYSICAL_SQUARE = CONDITIONAL_ON_R1_R4_AND_REL_R
NEW_CYCLE_KERNEL_RETAINED = PROVEN_AS_CONDITIONAL_REQUIREMENT
Ext_cycle_MEMBER_INSTANTIATED = false
```

### 3.3 Stagewise anchors, covariance, and skeleton scope

Each finite object remains

```text
S_G=(G,B_G,K_G,Q_G,Tbar_G,Abar_G,R_G,Kern_G),    (Z3-2)
```

with actual V005/Q-408/DoR-019 anchors.  R1 and R4 require their relation
data to be anchored at definition.  R2/R3 use no added carrier.

The one-orbit fiction remains deleted.  Every clause is a covariant family;
every construction is natural on that family.  No realization, frame,
orientation, cycle basis, path, or field member is selected.

No all-stage embedded master skeleton is restored.  Supports and fields are
stagewise actual.  Cross-stage claims require an R1 relation and, for fields,
an R4 member.

```text
STAGEWISE_OBJECT_ANCHORS = PROVEN
RELATION_ANCHORS = REQUIRED_BY_R1_R4_CLAUSES
COVARIANCE_ONE_ORBIT = false / TYPE-R
ALL_STAGE_MASTER_SKELETON = false / TYPE-R
```

### 3.4 Composition

For composable admitted members, R1 declares

```text
f_(S compose R)=f_S compose f_R,
F_(S compose R)=F_S compose F_R,
S_(S compose R)=S_S S_R.                        (Z3-3)
```

Equation `(Z1-8)` proves test-map composition.  Conditional field transport
composes by functorial pullback.  Support-local range composes because

```text
P_R Tbar_G(O) subset Tbar_G'(F_R(O)),
P_S Tbar_G'(F_R(O)) subset Tbar_G''(F_SF_R(O)). (Z3-4)
```

Current pairing and arbitrary-profile kernel squares then compose.  The
relative predicates are rerun on the composite; no theorem promotes
componentwise success without that check.

```text
COMPOSITION_Ref_0 = PROVEN
COMPOSITION_Ext_cycle = CONDITIONALLY_DERIVED_ON_ADMITTED_MEMBERS
```

### 3.5 Common refinement

Actual `Ref_path` diamonds remain proved by common parameter subdivision.
For a diamond containing cycle creation, R1 declares a common actual target
and path/current equality on both routes; R4 declares compatible target
field members.  R2 transport and R4 pullback then agree by composition, and
R3 is checked routewise and on the common composite.

A formal signed-chain diamond without R1/R4 geometry is still not physical.

```text
COMMON_REFINEMENT_Ref_path = PROVEN
COMMON_REFINEMENT_Ext_cycle = CONDITIONALLY_DERIVED_AFTER_R1_R4
FORMAL_OVERLAY_IS_PHYSICAL = false / TYPE-R
```

### 3.6 Surface geometry versus rails

| Territory | Surface geometry | Rail/construction | Honest status |
|---|---|---|---|
| finite and `Ref_path` | actual paths, currents, supports, `P=id` | exact restriction square | **BUILT** |
| cycle-creating paths | R1 declares actual relation | signed-chain map alone insufficient | **CLAUSE CANDIDATE** |
| test transport | local range is physical check | canonical `P_alg` constructed | **CONSTRUCTIBLE** |
| Riesz locality | no new leakage relative to transported analysis image | fixed-metric predicate | **CONSTRUCTIBLE** |
| local fields | R4 declares compatible new-cell members | pullbacks derived afterward | **CLAUSE CANDIDATE** |

The three V002 rail-only clause removals remain lawful.  No full root is a
rail artifact.  The two declarations are distinguished by actual supports
and fields, so both remain physical content inside `B_Q408_REFINEMENT`.

```text
RAIL_ARTIFACT_ROOTS = none
RAIL_ARTIFACT_CLAUSES_REMOVED = 3
ROOT_COUNT_CHANGE = 0
```

---

## 4. Z4 — regressions, falsifiers, anti-tuning, and exact stop

### 4.1 Eight cumulative regressions

| Regression | V004 execution | Result |
|---|---|---|
| pure new-cycle profile | retained outside old-image pullback | **PASS** |
| covariance orbit/moduli | full family retained; no orbit representative | **PASS** |
| all-stage skeleton | stagewise only | **PASS** |
| rank-preserving `Ref_path` | `P=id`; current/support/kernel calculation rerun | **PASS** |
| cycle-creating upward quotient | none defined | **PASS** |
| arbitrary-profile restriction | physical on `Ref_path`; conditional old-image square on `Ext_cycle` | **PASS WITH SCOPE** |
| Q-430 old-to-new Riesz mixer | fails `RNL_R` and `LR_R` | **PASS — REJECTED** |
| Q-432 `P=id` overreach counterexample | equations `(Z1-13)`--`(Z1-16)`; global cross term tolerated | **PASS — ADMITTED** |

### 4.2 Permanent regressions and joint condition

| Regression | Result |
|---|---|
| abstract-kernel substitution | **PASS** — R2 uses actual Q-408 `Abar,Kern` |
| circular `pi_Mx` | **PASS** — no reader defines paths, tests, or fields |
| misstated nonemptiness | **PASS** — R1/R4 candidates are not called inhabited |
| Hodge from isometry | **PASS** — no Hodge or locality inferred from W3 |
| objectwise minimum/restriction | **PASS** — no least member or representative selected |
| joint equalizer | **PASS** — clause candidates plus constructions do not bind EQ6 |

### 4.3 Finite and standing restriction suite

| Check | Result |
|---|---|
| Q-408 bottom object | **PASS** — neither construction changes a finite current or kernel |
| DoR-008 `Ref_path` restriction | **PASS** — `(Z3-1)` is exact |
| one-edge/connected tree | **PASS** — `K=0`; both constructed maps have the scope-empty cycle part |
| pendant/tree quotient | **PASS** — Gate-4 removes the coboundary presentation before R2/R3 act |
| S8-A rank-two exchange | **PASS** — the full covariant pair is retained; the exchange-invariant off-diagonal metric is allowed and tested relatively |
| reality/orientation | **PASS** — conjugation and signs commute with `P_alg`, `RNL`, and the clause families |
| batching | **PASS WITH RATIFIED SCOPE** — componentwise constructions; no new batching isometry inferred |
| identity zero-extension | **PASS** — old support and tests are unchanged; identity cells add no cycle current |

### 4.4 Fresh falsifiers

1. **Old-image fidelity failure.**  If `S_R^*R_G'S_R != R_G`, the constructed
   test map fails the old current-pairing square and the candidate is void.
2. **Relative leakage with local global metric.**  Even if unrelated target
   sectors are globally orthogonal, a nonlocal `S_RPhi_G` can fail `RNL_R`;
   the relative test, not a metric label, decides.
3. **Local-range failure without pairing leakage.**  An analysis quotient
   may annihilate all tested disjoint cycles yet lack a representative
   supported in `F_R(O)`; `LR_R` independently rejects it.
4. **Curvature mismatch.**  Support-local maps with
   `eta_curv Curv != Curv eta_conn` fail R4.
5. **Unrelated paths.**  The Q-430 unrelated-surface injection fails R1.
6. **Cycle deletion.**  Noninjective `S_R` fails the V005 separation clause.
7. **Formal common refinement.**  A rail overlay without R1/R4 members fails
   before composition is claimed.

### 4.5 Anti-tuning ledger

```text
1  Verify Q-432 and freeze both finite counterexamples.
2  Delete global X1-10 before constructing the corrected predicates.
3  Freeze Abar, Riesz maps, actual currents, and supports.
4  Construct P_alg uniquely; do not author an alternative.
5  Define OLD_FID, RNL, and LR as failure-capable tests.
6  Admit the P=id witness and reject the old-to-new mixer.
7  Type R1 and R4 from carrier geometry only.
8  Derive field transport only after an arbitrary declared member is fixed
   for proof, never selected physically.
9  Re-run composition, refinement, and all eight regressions.
10 Inspect no response, threshold, fixed point, end test, or measured datum.
```

### 4.6 Honest stopping point

The constructions are complete as maps and predicates.  The full physical
generator still requires:

```text
1  ratification or rejection of one R1 family-level clause alternative;
2  a nonempty covariant R1 family;
3  passage of OLD_FID_R, RNL_R, and LR_R for every admitted member;
4  ratification or rejection of one R4 family-level clause alternative;
5  a nonempty joint R1/R4 family satisfying field and refinement diamonds.
                                                        (Z4-1)
```

No member is bound, and none of `(Z4-1)` is inferred from the rail category.
The stopping point is exactly two physical declaration decisions plus their
joint inhabitance proof.  R2 and R3 add no ratification freedom.

```text
MISSING_DECLARATIONS = R1_PATH_CURRENT + R4_LOCAL_FIELDS
CONSTRUCTIBLE_ROWS_COMPLETE = R2_TEST_TRANSPORT + R3_RELATIVE_NO_LEAKAGE
MISSING_JOINT_OBJECT = NONEMPTY_COVARIANT_R1_R4_FAMILY_PASSING_REL_R
MISSING_TYPE = CLAUSE_RATIFICATION_PLUS_INHABITANCE / TYPE-U
NEW_SEVENTH_ROOT = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

### 4.7 Delta versus V003

| V003 content | V004 disposition |
|---|---|
| global disjoint-current orthogonality X1-10 | deleted / TYPE-R by Q-432 witness |
| local sectors and actual support definitions | retained |
| canonical test-map uniqueness | retained and executed as R2 construction |
| Riesz locality | replaced by `OLD_FID_R + RNL_R`; local range kept in R2 |
| `P=id` off-diagonal metric | newly admitted as permanent regression |
| old-to-new sector mixer | still rejected |
| path/current correspondence | retyped as complete R1 clause candidate |
| local fields | retyped as complete R4 member clause; transport derived |
| finite/`Ref_path` core | retained after deleting overreach |
| stagewise anchors/covariance/skeleton | retained |
| composition/refinement | re-proved on corrected predicates |
| three rail-clause removals | retained |

## Final board

```text
CONSTRUCTIONS =
  R2_TEST_TRANSPORT = BUILT;
  R3_RELATIVE_NO_LEAKAGE = BUILT

RELATIVE_CERTIFICATE = OLD_FID_R + RNL_R + LR_R
P_ID_OVERREACH_WITNESS = ADMITTED
Q430_SECTOR_MIXER = REJECTED

CLAUSE_CANDIDATES =
  R1_PATH_CURRENT = COMPLETE / PROPOSED_NOT_ADOPTED;
  R4_LOCAL_FIELDS = COMPLETE / PROPOSED_NOT_ADOPTED;
  R4_TRANSPORT_AFTER_MEMBER = CONDITIONALLY_DERIVED

ACTUAL_FINITE_AND_Ref_path_CORE = BUILT / TYPE-P
Ext_cycle_FULL_MEMBER = OPEN / TYPE-U
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
RAIL_ARTIFACT_ROOTS = none
JOINT_EQ6 = OPEN
C1_RESUMPTION = N/A
READY_FOR_HOSTILE_CHECK = yes

TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MEMBER_SELECTED = false
MEMBER_BOUND = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
```

Seal this artifact, mirror artifact and sidecar byte-identically to
`alpha-program-archive/workspace/`, report hashes, and stop.  No register,
plan, tracker, git, commit, or push action belongs to this lane.
