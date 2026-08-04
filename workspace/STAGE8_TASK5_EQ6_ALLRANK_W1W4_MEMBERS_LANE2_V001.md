# STAGE 8 TASK 5 / EQ6 — ALL-RANK W1/W4 MEMBERS — LANE 2 V001

Date: 2026-08-04  
Lane: Codex Lane 2  
Task: 5 / EQ6 / all-rank closure  
Custody: builder; hostile check required

## Lead result

```text
W1_W4 = STOPPED_AT(
  NONEMPTY_POSITIVE_SOURCE_RELATIVE_CERTIFICATE_SUBFAMILY)

PATH_CURRENT_AND_BUNDLE_CANDIDATES = BUILT |
  actual positive-source, cycle-rank-increasing W1/W4 tuples exist on the
  two concrete surface diamonds below

OLD_FID_RNL_LR = NOT_PROVEN_FAMILY_WIDE |
  OLD_FID requires a cycle-creating A4-isometry not supplied by W3;
  even on the favorable OLD_FID slice, a live off-diagonal Riesz term
  violates RNL and the canonical test can violate LR

DIAMONDS = EXECUTED(3) |
  rank-preserving path-subdivision diamond = ADMITTED / PASS;
  disjoint-cycle common-refinement diamond = W1/W4 COMMUTES,
    P4/X4 ADMISSION STOPS AT OLD_FID/RNL/LR;
  contact-cycle common-refinement diamond = W1/W4 COMMUTES,
    P4/X4 ADMISSION STOPS AT LR

ALL_RANK = PARTIAL |
  first-cycle covariant family and its subdivision orbits remain inhabited;
  no nonempty family of positive-source primitive members has been proved

JOINT_EQ6 = PARTIAL |
  B_Q408_REFINEMENT remains inhabited only on the verified first-cycle and
  rank-preserving subdivision subcategory; the remaining five-fiber
  equalizer cannot advance beyond that physical subcategory

GENERIC_BATCHING_USED = false
NEW_CLAUSE_REQUESTED = false
MEMBER_BOUND = false
MACHINERY_APPEAL = false
```

This is a construction attempt with an exact stop, not an impossibility
theorem.  The adopted W1/W4 laws admit the actual surface and bundle data.
What is not proved is that their fixed DoR-019 carrier data contain a
nonempty all-rank subfamily passing the three physical relative tests on
every positive-source leg and every actual common-refinement diamond.

---

## 0. Preflight, authorities, and register sweep

### 0.1 Three-line preflight

```text
DOES THE OBJECT EXIST?  The verified zero-source first-cycle member exists.
                        The requested all-rank positive-source family does
                        not; two actual candidate diamonds are built below.
IS THE VERSION CURRENT? YES, through register head Q-440.
ARE ITS INPUTS PRESENT? YES: the Q-440 hostile check, the verified Q-439
                        member, adopted W1/W4 clauses, DoR-019, DoR-020+A1,
                        Q-408 analysis/kernel data, and pass-1 subpackages.
PREFLIGHT = PASS
```

The locked process was read in full before task action.  The Q-440 hostile
check was seal-verified before reading.

| Authority | SHA-256 | Use |
|---|---|---|
| locked process | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody; surface-geometry rule; seal/mirror/stop |
| register at Q-440 | `563ebf6a9c4cd79805de08d75dd35a29fca43cb1ece39be550608c969dfdede1` | current head |
| Q-440 hostile check | `166002e9178faefe4464f504810553a606ec6465a0e3739a70e50a5d29d8604e` | exact all-rank need; no generic batching shortcut |
| verified first-orbit member | `c0cc95112bf8c213b0e2c4095a06c4e4658fa3950641b9a21fa51950a9f818fa` | surviving first-cycle construction |
| adopted where-clauses | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | W1/W4 laws |
| pass-1 witness hunt | `452f1bb87aeb7f7bfe4ab4556134cf723ab6df697f93c1a59c33671146cb0083` | six-fiber subpackages and equalizer |
| DoR-020 decision | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | conditional package and `[EQ6]` custody |
| DoR-020-A1 | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` | adopted law-only where-clauses |
| metric V005 / DoR-019 object | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed A4-derived cycle metric, Riesz maps, units, W3 scope |

### 0.2 Register sweep

```text
Q-408  finite current/kernel realization and analysis maps exist;
Q-418  actual rank-preserving Ref_path subdivision square exists with P=id;
Q-422  DoR-020 adopts the package only conditional on joint [EQ6];
Q-425  Ref_0 was the maximal then-built physical refinement category;
Q-427  generators must be anchored in actual surface geometry, not rails;
Q-430  an old-to-new Riesz mixer can commute algebraically while leaking;
Q-432  relative no-leakage, not global Riesz orthogonality, is the law;
Q-435  W1/W4 were repaired to law-only, bundle-typed clauses;
Q-438  DoR-020-A1 put those laws in force without asserting inhabitance;
Q-439  the first-cycle, zero-source member was built;
Q-440  that member survived; positive-source members plus actual diamonds
       are the exact all-rank residue; batching supplies no generic isometry.
```

No settled entry proves a rank-increasing A4 isometry, a nonempty family of
positive-source relative certificates, or an all-rank common-refinement
equalizer.

### 0.3 Bearing symbol distinctions

```text
calB                   = retained background/surface member;
B_G                    = graph incidence operator;
P_bundle -> calB       = U(1) bundle;
P_R                    = canonical test transport;
A_conn                 = bundle connection;
Abar_G                 = Q-408 analysis isomorphism;
F_conn=Curv(A_conn)    = connection curvature;
F_R                    = support/region map of a refinement;
c_1(P_bundle)          = first Chern class;
c_U,c_V                = graph-cycle generators;
R_K,G                  = DoR-019 Riesz map;
r                       = refinement arrow;
actual diamond         = four specified surface members and four arrows,
                         not merely equality of two formal composites.
```

Ranks, orientations, frames, paths, and representatives remain families.
The named members below are generic elements of covariant orbit-families,
not selected members for the DoR-020 computation.

---

## 1. F1 — positive-source W1/W4 construction attempt

### 1.1 The disjoint-cycle surface diamond

Fix symbolically a retained surface member `calB`, two disjoint relatively
compact surface corridors `U,V subset calB`, and actual oriented timelike
path data in each corridor.  Join the corridors by tree edges if a connected
record graph is required.  The joining tree creates no cycle.  Let

```text
G_0   = the connected base tree;
G_U   = G_0 plus an actual chord/path gamma_U creating cycle c_U in U;
G_V   = G_0 plus an actual chord/path gamma_V creating cycle c_V in V;
G_UV  = G_0 plus both actual chords.
```

The path interiors and the resulting distributional cycle currents obey

```text
Supp(c_U) subset U,
Supp(c_V) subset V,
closure(U) intersect closure(V)=empty,
K_G0={0},
K_GU=span{c_U},
K_GV=span{c_V},
K_GUV=span{c_U,c_V}.                            (F1-1)
```

The currents are nonzero because the adopted path/current law uses actual
path line currents and the retained fullness/separation certificate.  Thus
both upper legs below have strictly positive source cycle rank:

```text
                 r_0U                 r_UV
        G_0 --------------> G_U ----------------> G_UV
         |                                          ^
     r_0V|                                          |r_VU
         v                                          |
        G_V ----------------------------------------+

K_GU != 0 and K_GV != 0.                           (F1-2)
```

This is actual surface geometry.  No formal direct sum or generic batching
operator defines `(F1-2)`.

### 1.2 W1 path/current tuples

For every arrow in `(F1-2)`, define `Gamma_r` to be the inclusion of the
actual oriented paths and let `S_r` be its induced map on conserved cycle
currents.  In the displayed bases,

```text
S_0U: 0 -> span{c_U},
S_0V: 0 -> span{c_V},
S_UV(c_U)=c_U,
S_VU(c_V)=c_V.                                  (F1-3)
```

The exact W1 certificates are:

1. incidence: `B_GUV^T S_UV(c_U)=0` and
   `B_GUV^T S_VU(c_V)=0`;
2. support: `Supp(S_UV c_U) subset U` and
   `Supp(S_VU c_V) subset V`;
3. current equality: the pushed path currents are the same distributions
   as their target representatives;
4. restriction: deleting the newly added chord returns the corresponding
   source path/current tuple;
5. covariance/reality: relabeling and orientation reversal carry paths and
   current signs together; no orientation is fixed;
6. units: all current maps remain within the ratified current unit class.

The raw W1 diamond commutes on every retained current:

```text
S_UV S_0U = 0 = S_VU S_0V.                     (F1-4)
```

Equation `(F1-4)` does not erase either target cycle: both `c_U` and `c_V`
remain visible on target tests.  It only records that the common base has
zero cycle carrier.

```text
W1_DISJOINT_DIAMOND_CANDIDATES = BUILT / TYPE-P
W1_POSITIVE_SOURCE_LEGS = BUILT / TYPE-P
```

### 1.3 W4 U(1)-bundle field tuples

Carry the full covariant family of bundle-typed data admitted by DoR-020-A1:

```text
P_bundle -> calB,
Cof_G, Dens_G>0, A_conn,G, F_conn,G=Curv(A_conn,G).
```

On each inclusion, use the actual restriction/pullback bundle map.  In the
minimal identity-bundle chart it is the identity bundle lift; family-wide it
is the admitted smooth equivariant pullback-bundle isomorphism.  Then

```text
eta_conn,r(A_conn,target)=A_conn,source,
eta_curv,r(F_conn,target)=F_conn,source,
c_1(P_source)=r^*c_1(P_target).                 (F1-5)
```

The coframe stays smooth and full rank, the density stays positive, and
connection/curvature units are unchanged.  Pullback functoriality gives the
actual field diamond

```text
eta_UV eta_0U = eta_VU eta_0V                  (F1-6)
```

separately for bundle, coframe, density, connection, curvature, and
characteristic class.  Reality is complex conjugation on the U(1) data and
commutes with both routes.

```text
W4_DISJOINT_DIAMOND_CANDIDATES = BUILT / TYPE-P
POSITIVE_DENSITY = PASS
SMOOTH_FULL_RANK = PASS
BUNDLE_LIFT_AND_C1 = PASS
```

These statements build W1/W4 clause members.  A physical P4/X4 member also
requires the fixed-carrier relative certificate below.

### 1.4 The positive-source relative tests

For each candidate arrow `r:G->G'`, the canonical test map is fixed, not
authored:

```text
Phi_G = R_K,G^(-1) Abar_G,
P_r   = Phi_G'^(-1) S_r Phi_G.                 (F1-7)
```

It must pass

```text
OLD_FID_r: S_r^* R_K,G' S_r = R_K,G;

RNL_r(O,W):
  g_K,G'(S_r Phi_G(a),n)=0
  for a in Tbar_G(O), n in K_G'(W),
  whenever F_r(O) intersect W=empty;

LR_r(O):
  P_r(Tbar_G(O)) subset Tbar_G'(F_r(O)).       (F1-8)
```

Let the actual fixed DoR-019 forms on the two sources and target be
represented symbolically by

```text
g_K,GU(c_U,c_U)=alpha_0 >0,
g_K,GV(c_V,c_V)=delta_0 >0,

[g_K,GUV]_(c_U,c_V)
  = [[alpha,zeta],[conj(zeta),delta]],
alpha>0, delta>0, alpha*delta-|zeta|^2>0.       (F1-9)
```

Reality makes the appropriate real slice real-symmetric; keeping the
conjugate form in `(F1-9)` records the general covariance law.  Nothing is
evaluated.

The two `OLD_FID` equations are exactly

```text
alpha=alpha_0,
delta=delta_0.                                 (F1-10)
```

DoR-019 W3 proves isometry for its ratified rank-preserving maps.  Neither
positive-source arrow in `(F1-2)` is rank preserving.  It supplies no
generic batching isometry and therefore does not prove `(F1-10)`.

Now grant the favorable slice `(F1-10)` to isolate the next obstruction.
Choose a nonzero source-local test `a_U` with

```text
Phi_GU(a_U)=theta_U c_U, theta_U !=0.
```

Because `c_V` is supported in the disjoint corridor `V`, RNL on `r_UV`
requires

```text
0=g_K,GUV(S_UV Phi_GU(a_U),c_V)
 =theta_U zeta.                                (F1-11)
```

Thus this actual leg requires `zeta=0`.  The other leg gives the conjugate
condition.  Q-430 and Q-440 show that a positive off-diagonal Riesz class is
live under the ratified metric law; DoR-019 does not force `zeta=0`.
Changing the fixed metric or choosing only an outcome-friendly attachment
would be witness-by-certificate tuning.

In the transparent finite chart `Abar=id`, `(F1-7)` makes the same failure
visible in the test itself.  On the favorable OLD_FID slice,

```text
P_UV(a_U) has target coordinates proportional to
  (1,conj(zeta)/alpha_0),                       (F1-12)
```

with `conj(zeta)=zeta` on the real slice.  For `zeta!=0`, the test spills
into the disjoint `V` corridor and LR fails.
For `zeta=0`, LR still requires the independent support-naturality fact

```text
Phi_GUV^(-1) S_UV Phi_GU(Tbar_GU(O))
 subset Tbar_GUV(F_UV(O))                      (F1-13)
```

for every actual region.  No all-rank theorem in the adopted stack proves
`(F1-13)`.

The constructed candidates therefore stop at the exact joint condition

```text
C_pos(r) := OLD_FID_r and RNL_r and LR_r.

F_pos^actual := {
  actual positive-source W1/W4 tuples x_r:
  C_pos(r), all bundle certificates, and all actual diamonds hold
}.                                             (F1-14)
```

```text
F_pos^actual_NONEMPTY = UNPROVED / TYPE-U
POSITIVE_SOURCE_P4_X4_MEMBER = NOT_YET_BUILT
```

This is not caused by absent W1/W4 laws.  It is the remaining inhabitance
burden under those laws.

### 1.5 Contact-cycle construction: why RNL alone is insufficient

Build a second actual surface diamond with two cycle-creating corridors
whose closures meet only at one recorded endpoint `q`.  The path/current
and bundle constructions in Sections 1.2–1.3 repeat, and both positive
source carriers are nonzero.  For local regions containing `q`, the RNL
antecedent can be false because the mapped old and new supports meet.

The canonical test may nevertheless acquire a representative on an
exclusive segment of the newly added path.  The required check is still

```text
P_r(Tbar_G(O)) subset Tbar_G'(F_r(O)).          (F1-15)
```

The fixed carrier data contain no theorem excluding that exclusive-path
spill.  Consequently the contact diamond stops at LR even when RNL is
silent.  This is the Q-440 contact-only attack executed on actual surface
members, not stated as a generic warning.

---

## 2. F2 — actual common-refinement diamonds

### 2.1 Diamond D-sub: rank-preserving path subdivision

Take an admitted first-cycle member with two actual paths and subdivide one
path at two different interior points.  Let `G_s` and `G_t` be the two
one-step subdivisions and `G_st` their actual common subdivision.  All four
cycle carriers have rank one.  Q-418's actual subdivision construction has

```text
S=id, P=id,
R_K preserved by W3,
```

and the path, current, bundle, connection, curvature, support, and finite
kernel maps agree on the common refinement.  Member-by-member,

```text
OLD_FID = id^* R_K id = R_K;
RNL     = PASS because the transported local image is unchanged;
LR      = Tbar_G(O) subset Tbar_Gst(F(O));

P_t,st P_0,t = id = P_s,st P_0,s.              (F2-1)
```

This is an admitted actual diamond, not a batching inference.

```text
D_SUBDIVISION = EXECUTED / PASS / ADMITTED
```

### 2.2 Diamond D-disj: two disjoint cycle additions

For `(F1-2)`, direct calculation gives the raw W1/W4 equalities

```text
S_UV S_0U = S_VU S_0V = 0,
Gamma_UV Gamma_0U = Gamma_VU Gamma_0V,
eta_UV eta_0U = eta_VU eta_0V.                 (F2-2)
```

The outer base-to-target test map is zero because `Tbar_G0={0}`.  That
vacuous outer equality does not certify either positive-source side.  The
side calculations are:

| Leg | source rank | target rank | OLD_FID | RNL | LR |
|---|---:|---:|---|---|---|
| `r_UV:G_U->G_UV` | 1 | 2 | requires `alpha=alpha_0` | requires `zeta=0` | requires `(F1-13)` |
| `r_VU:G_V->G_UV` | 1 | 2 | requires `delta=delta_0` | requires `zeta=0` | symmetric support condition |

The adopted fixed data prove none of these requirements family-wide.
Accordingly the actual path/bundle diamond exists and commutes, but the
physical P4/X4 common-refinement diamond is not admitted.

```text
D_DISJOINT = EXECUTED |
  W1/W4 = PASS;
  P4/X4 = STOPPED_AT(C_pos(r_UV) and C_pos(r_VU))
```

### 2.3 Diamond D-contact: endpoint-contact cycle additions

The contact construction of Section 1.5 has the same actual W1/W4
commutation equations as `(F2-2)`.  On the positive-source sides, endpoint
contact can make RNL inapplicable while `(F1-15)` remains failure-capable.
Because no local-range theorem covers the exclusive new-path segment, the
member diamond stops there.

```text
D_CONTACT = EXECUTED |
  W1/W4 = PASS;
  P4/X4 = STOPPED_AT(LR_on_each_positive_source_leg)
```

### 2.4 Diamond count and non-shortcut statement

```text
ACTUAL_DIAMONDS_COMPUTED = 3
ACTUAL_DIAMONDS_ADMITTED = 1
CYCLE_CREATING_DIAMONDS_COMPUTED = 2
CYCLE_CREATING_DIAMONDS_ADMITTED = 0
```

No direct-sum metric, block-diagonal Riesz map, generic batching isometry,
or formal union functor has been inserted.  The two cycle-creating failures
are edge failures on concrete diamonds.  Equality of the outer zero-source
composites is not promoted to positive-source membership.

---

## 3. F3 — all-rank determination

### 3.1 What is now exhibited

The following nonempty covariant family remains proved:

```text
F_first :=
  verified first-cycle members over the full retained background/path/
  bundle/gauge/orientation/frame family,
  plus every Q-418 rank-preserving subdivision orbit.               (F3-1)
```

Sections 1–2 also exhibit actual W1/W4 clause candidates on positive-source
rank-increasing arrows.  Thus the surface and bundle laws are not empty on
those raw coordinates.

### 3.2 Exact remaining stop

All-rank induction requires at least one admitted step from rank one to
rank two.  The actual disjoint and contact diamonds do not supply it.  The
remaining object is exactly

```text
F_Q408^all :=
  a nonempty covariant family over every required positive-source
  primitive orbit such that

  (i)   its W1 path/current and W4 bundle/field tuples are actual;
  (ii)  each primitive passes OLD_FID + RNL + LR using the fixed
        DoR-019 Riesz/analysis data;
  (iii) its bundle lift, full-rank, positive-density, characteristic-class,
        covariance, reality, units, and finite restriction certificates pass;
  (iv)  it is closed under composition and actual common refinement;
  (v)   every common-refinement diamond commutes on path/current,
        bundle/field, canonical test, and finite-kernel maps.        (F3-2)
```

The earliest newly isolated necessary data are a family-wide
cycle-rank-increasing old-image isometry and a support-local extension of
the Q-408 analysis map.  These are witness certificates, not permission to
author a new metric or a new where-law.

```text
ALL_RANK = PARTIAL / TYPE-U
EXACT_STOP = NONEMPTY(F_Q408^all)
FIRST_UNRESOLVED_LEG = rank_1_to_rank_2_positive_source_primitive
LAW_REVISION_NEEDED = false
NEW_PHYSICS_CLAUSE_NEEDED = not_proven
```

The live Q-430 class shows that all-rank extension is not forced.  It does
not show that `(F3-2)` is empty.

---

## 4. F4 — cascade and joint `[EQ6]`

### 4.1 Updated fiber ledger

| Fiber | Built after this task | Exact residue | Standing |
|---|---|---|---|
| `B_Q408_REFINEMENT` | `F_first`; actual raw W1/W4 positive-source candidates; one admitted subdivision diamond | nonempty `F_Q408^all`, beginning with an admitted rank-1-to-rank-2 leg and its actual diamonds | **PARTIAL / TYPE-U** |
| `B_R1_NATURAL` | pass-1 old-arrow naturality subpackage | action/Hessian/reducing-domain naturality on an admitted positive-source refinement, then all ranks | **PARTIAL / TYPE-U** |
| `C1` / P4 primitive core | pass-1 core plus the Q-439 first-cycle physical orbit | response-natural completed kernel on an admitted positive-source primitive and its refinements | **PARTIAL / TYPE-U** |
| completed faithfulness | pass-1 orbitwise bounds and finite faithfulness | faithful passage on the missing all-rank physical category | **PARTIAL / TYPE-U** |
| `B_C2_RESPONSE_BOUNDARY` | pass-1 boundary cocycle subpackage on built arrows | positive-source/all-rank response-boundary naturality | **PARTIAL / TYPE-U** |
| `C3` / joint stationary return | pass-1 conditional interface | full common-refinement equalizer after the preceding rows inhabit jointly | **PARTIAL / TYPE-U** |

### 4.2 Executed dependency cascade

The raw W1/W4 candidate data feed no downstream physical theorem because
P4/X4 membership is conjunctive.  An arrow failing or not proving one of
`OLD_FID`, `RNL`, or `LR` is not in the response-natural refinement
category.  Therefore:

```text
positive-source W1/W4 candidates
  -> C_pos not discharged
  -> no positive-source B_Q408 physical arrow
  -> no new B_R1 naturality square
  -> no new completed C1 kernel leg
  -> no new faithfulness/boundary leg
  -> no enlarged C3 equalizer.                 (F4-1)
```

The Q-439 first-cycle member and D-sub remain banked and valid.  Nothing
previously proved is withdrawn.

### 4.3 Joint distance

On the actually inhabited subcategory, the pass-1 finite equalizer and the
Q-439 joint rows continue to commute.  On the all-rank category, `[EQ6]`
still first consumes `(F3-2)`, then the remaining five fiber extensions in
the order shown in Section 4.1.

```text
JOINT_EQ6 = PARTIAL

NEXT_DEPENDENCY_ORDER =
  1. exhibit nonempty F_Q408^all;
  2. extend B_R1 naturality across its admitted arrows;
  3. extend C1/faithfulness and response-boundary packages;
  4. prove the full common-refinement equalizer and C3 return.

EQ6_WITNESS_BOUND = false
CONTINUUM_P_MEMBER_BOUND = false
FIXED_POINT_LICENSED = false
```

---

## 5. F5 — falsifiers, regressions, and anti-tuning

### 5.1 Nine inherited geometric regressions

| Regression | Execution on this artifact | Result |
|---|---|---|
| abstract-kernel substitution | every kernel/test statement uses Q-408 `Abar`, `Phi`, and `Kern`; no abstract stand-in | **PASS** |
| circular projection/map | `P_r` is derived by `(F1-7)` after actual `S_r`; it is not used to define `S_r` | **PASS** |
| false nonemptiness | raw W1/W4 nonemptiness is separated from physical P4/X4 nonemptiness | **PASS** |
| cycle-creating restriction | target cycles remain nonzero; the outer zero map is not called a target annihilation | **PASS** |
| covariance-orbit overclaim | covariance transports candidates and failures; it does not create positive-source certificates | **PASS** |
| all-stage skeleton overclaim | all-rank is explicitly partial at the first rank-1-to-rank-2 leg | **PASS** |
| Q-430 old-to-new sector mixer | `(F1-11)` rejects nonzero `zeta` on disjoint supports | **PASS — REJECTED** |
| Q-432 `P=id` overreach | D-sub admits `P=id`; no global orthogonality is demanded | **PASS — ADMITTED** |
| V004/V005 clause nonemptiness overreach | adopted laws are used as membership laws; witness inhabitance is proved only where executed | **PASS** |

### 5.2 Task-specific falsifiers

| Attack | Computation | Result |
|---|---|---|
| generic batching shortcut | would require an unratified block-diagonal A4/Riesz isometry | **REJECTED** |
| favorable OLD_FID attack | even granting `(F1-10)`, `(F1-11)` leaves `zeta=0` and LR unproved | **STOP SURVIVES** |
| outer-square laundering | `0=0` on the rank-zero base does not certify either positive-source side | **REJECTED** |
| contact-only leakage | RNL can be silent at the shared endpoint while `(F1-15)` fails | **REJECTED** |
| componentwise nonempty attack | W1 and W4 tuples exist separately, but membership requires their joint relative certificates and diamond | **REJECTED** |
| target-cycle deletion | `c_U,c_V` remain target-visible and no target kernel is quotiented away | **PASS** |
| hidden metric selection | `alpha_0,delta_0,alpha,delta,zeta` are the fixed symbolic metric entries; none is assigned | **PASS** |
| hidden support selection | the construction ranges over the full covariant orbit of actual corridor/path data | **PASS** |

### 5.3 Fresh attack — zero-cross-term is not enough

Suppose a future candidate happens to satisfy `zeta=0`.  It may still fail
if `Abar_GUV` sends the canonical old test to a representative with support
outside the mapped old region.  Equation `(F1-13)` is not implied by the
Gram matrix.  Therefore a metric-only witness, including a diagonal Gram
matrix advertised as “local,” does not inhabit `(F3-2)` without the LR
proof.  This attack prevents the next build from replacing physical
support transport by one favorable coefficient.

### 5.4 Surface geometry versus rails

| Layer | What was executed | Status |
|---|---|---|
| actual surface geometry | real path chords/currents in disjoint or endpoint-contact corridors | **BUILT** |
| actual U(1) data | pullback bundle, full-rank coframe, positive density, connection, curvature, `c_1` | **BUILT** |
| rail equality | incidence and outer composite squares | **COMMUTES** |
| fixed physical carrier | DoR-019 metric and Q-408 analysis/test support | **FAILURE-CAPABLE; STOP HERE** |

The stop is not a rail artifact: the actual positive-source test can pair
with a disjoint actual current or leave the mapped surface support.  Nor is
it a request for new clauses: DoR-020-A1 already states the correct laws.

### 5.5 Anti-tuning ledger

```text
1  Read and verify Q-440's all-rank requirement.
2  Fix the actual surface diamonds and their covariant orbit-families.
3  Construct W1 path/current data from incidence and actual paths.
4  Construct W4 bundle/field data from the adopted bundle law.
5  Derive P_r from the fixed Riesz and analysis maps.
6  Evaluate OLD_FID, RNL, LR and the actual diamonds.
7  Only after the failures were located, state the all-rank and EQ6 boards.
```

No response, threshold, fixed point, end test, alpha consequence, or
measured constant entered steps 1–6.  No metric coefficient, rank, path,
orientation, frame, bundle member, refinement, or computation member was
selected for its outcome.

---

## 6. Final board

```text
W1_W4 = STOPPED_AT(NONEMPTY_POSITIVE_SOURCE_RELATIVE_CERTIFICATE_SUBFAMILY)
DIAMONDS = EXECUTED(3) / ADMITTED(1)
ALL_RANK = PARTIAL / TYPE-U
JOINT_EQ6 = PARTIAL / TYPE-U

SURVIVES =
  verified first-cycle family;
  rank-preserving subdivision orbits;
  actual positive-source W1/W4 candidate geometry;
  actual bundle/field diamonds;
  exact OLD_FID/RNL/LR obstruction equations.

EXACT_REMAINING_OBJECT = F_Q408^all as defined in (F3-2)
LAW_REVISION_NEEDED = false
MEMBER_BINDING = false
FIXED_POINT_EXECUTION = false
END_TEST = false
NUMERIC_EVALUATION = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
