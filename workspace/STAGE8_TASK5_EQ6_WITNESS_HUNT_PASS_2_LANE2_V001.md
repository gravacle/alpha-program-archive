# STAGE 8 TASK 5 / EQ6 — WITNESS HUNT, PASS 2 — LANE 2 V001

Date: 2026-08-04  
Task: Paste 513 / Task 5 / EQ6  
Lane: Codex Lane 2  
Custody: construction on DoR-020-A1's adopted where-law; hostile check follows

## Lead result

```text
GENERATOR_MEMBER = BUILT |
  FIRST_CYCLE_CREATING_ORBIT r_01:
    one-edge tree -> two-parallel-path cycle;
  FULL_X4_TUPLE =
    (Gamma_r01,P_r01,S_r01,Cof_r01,Dens_r01,
     eta_conn,r01,eta_curv,r01);
  BUNDLE_LIFT = identity;
  FULL_RANK = exact;
  CHARACTERISTIC_CLASS = identity;
  OLD_FID + RNL + LR = exact/vacuous on K_G0={0};
  NEW_CYCLE_KERNEL = retained and nonzero;
  COVARIANT_NO_SELECTION_FAMILY = retained.

FULL_B_Q408_REFINEMENT_FIBER = PARTIAL / TYPE-U |
  the constructed family covers every first-cycle orbit and its
  rank-preserving path subdivisions, but not cycle-rank-increasing arrows
  from a source with K_G != {0};
  exact stop = NONEMPTY_COVARIANT_ALL_RANK_SUBFAMILY_PASSING
               (OLD_FID,RNL,LR)
               + ACTUAL_COMMON_REFINEMENT_DIAMONDS.

FIBER_LEDGER =
  B_Q408: first-cycle subfiber inhabited, full root partial;
  B_C1: P4 core gains the first-cycle arrow; the already-built finite/orbit
        bounds persist, but no cross-rank bound is created;
  B_FAITHFULNESS: finite/first-cycle-orbit faithfulness built;
  B_C2: finite old-image zero discrepancy built, full response fiber open;
  B_C3: finite Ward on the new cycle and its subdivisions built;
  B_R1: unchanged full-scope obstruction.

JOINT_EQ6 = PARTIAL |
  the new P4 term closes the geometric/density rows on r_01 only;
  no full six-fiber term and no J1--J15 equalizer term exists.

MEMBER_BOUND = false
P_COMPUTATION_MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
```

The positive object is a complete physical generator member, not an abstract
stand-in: its new cycle is a difference of two actual causal paths on a
ratified DoR-015 surface, and its field coordinates use the actual U(1)
bundle and connection.  It is also the maximal result forced by current
structure.  Adoption of a membership law does not prove that every
cycle-rank-increasing orbit has a member.  The Q-430 old-to-new mixer remains
an admitted-carrier counterexample to that promotion.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
measured_constant_compared = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

---

## 0. Preflight, authorities, and register sweep

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST?  The adopted law exists.  A complete first-cycle P4
                        member is constructed below; the all-rank root is not.
IS_THE_VERSION_CURRENT? YES, through send-time register head Q-438.
ARE_ITS_INPUTS_PRESENT? YES: DoR-020-A1, the adopted/check-verified clauses,
                        V004 constructions, pass 1, frontier, and bedrock.
PREFLIGHT = PASS
```

The locked process was read in full.  The supervision register and every
load-bearing sidecar were verified before the corresponding artifact was
read.

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody, fences, surface/rails rule |
| register at Q-438 | `4ea3b3706b3de2f9b5709b0212076d9dee446675c65ab816e08a8af985aec451` | current scope |
| DoR-020-A1 | `c4dc5976d7e65fe8a6597870629e64cabe6a031b95de97f5572bb36379abb588` | adopted law and unchanged witness burden |
| adopted where-clauses | `19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec` | exact W1/W4 law |
| final clause check | `b4c901f512379251b55d31aae6914d1fce9af6280c8f65081afeabfd4e75f219` | bundle and flat-holonomy standard |
| V004 constructions | `c5254f663a1e3a6d1079027184c6dea96a35ab7255a856aa39e584b3d7c32dc2` | canonical test map and relative predicates |
| pass-1 hunt | `452f1bb87aeb7f7bfe4ab4556134cf723ab6df697f93c1a59c33671146cb0083` | six-fiber starting ledger |
| frontier map | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | dependency order and root scopes |
| six-bedrock theorem | `288a3d4147cb10f2e51180b21f7c6b2b4749503504c57b8a1121e3925c70c94c` | irreducibility and joint-equalizer discipline |
| field signature / DoR-015 object | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | actual surfaces, paths, bundles, fields, currents |
| Q-408 kernel realization | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual path currents and finite kernels |
| Q-425 C1 build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | P4-core handoff |
| J1--J15 constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | joint step |

### 0.2 Register sweep

```text
Q-408  actual finite conserved path currents, faithful kernels, and Ward
       annihilation exist;
Q-418  rank-preserving physical path subdivision and exact squares exist;
Q-421  six independent roots, with a joint rather than componentwise witness;
Q-423  pass 1 builds finite/Ref_path projections and stops at six full roots;
Q-425  Ref_0 is the maximal P4 core then available to C1;
Q-430  an old-to-new Riesz mixer can satisfy algebraic squares while failing
       actual locality;
Q-432  relative OLD_FID+RNL+LR, not global orthogonality, is the lawful test;
Q-434  the canonical transport and relative predicates are constructed;
Q-435  W1/W4 require law-only bundle typing;
Q-437  those clauses survive every check, including flat holonomy;
Q-438  DoR-020-A1 adopts W1/W4 as law; inhabitance remains an EQ6 burden.
```

No settled entry proves a nonempty all-rank cycle-creating family, an action
restriction cube on the new arrow, or a completed six-fiber equalizer.

### 0.3 Bearing symbol distinctions

```text
generator member       = one full seven-coordinate P4/X4 term;
full B_Q408 root       = a family over every required primitive orbit with
                         composition/common refinement;
P4 fiber inhabitant    != the P-member eventually bound for computation;
old-image restriction != upward map onto a new cycle;
graph cycle current    != first Chern class;
bundle identity lift   != selected gauge trivialization;
finite kernel square   != completed response naturality;
law adoption           != nonemptiness.

B=(M,g,...)            = a background-family member;
B_G                    = the graph incidence operator, not B;
P->M                   = the principal U(1) bundle;
P_r01                  = the constructed test transport, not the bundle;
F=Curv(A)              = curvature;
F_r01                  = the local-support map, not curvature;
A                      = the U(1) connection;
A_G                    = the Q-408 cycle-analysis map, not A.
```

---

## 1. D1 — the cycle-creating member

### 1.1 Actual first-cycle geometry

Fix only for the proof an arbitrary member

```text
B=(M,g,o,t; pi:P->M, e,mu,A,F=Curv(A))          (D1-1)
```

of the ratified no-selection DoR-015 family.  No such member is bound.
Inside a convex normal neighborhood choose temporarily `x<<y`.  The local
Lorentzian cone is open, so there are two future-directed smooth timelike
arcs from `x` to `y` with different interior images.  Retain the full
covariant family of all tuples

```text
(B,x,y,gamma_0,gamma_1),
gamma_0 != gamma_1 as distributional path currents. (D1-2)
```

No point, chart, path, frame, orientation representative, or bundle gauge is
selected.  Nonemptiness is proved locally: after taking one timelike arc, a
small compactly supported transverse perturbation inside the timelike cone
gives the second; a compactly supported one-form in a tube met by only one
perturbed segment separates their path currents.

Define the source and target incidence stages

```text
G_0: V={x,y}, E={a:x->y}, gamma_a=gamma_0;

G_1: V={x,y}, E={a:x->y,b:x->y},
     gamma_a=gamma_0, gamma_b=gamma_1.           (D1-3)
```

Their conserved carriers are computed, not asserted:

```text
B_G0^T(s a)=s(delta_y-delta_x),
K_G0=ker(B_G0^T)={0};

B_G1^T(s a+t b)=(s+t)(delta_y-delta_x),
K_G1=R c_01,
c_01=(1,-1).                                    (D1-4)
```

The target current is the actual Q-408 distribution

```text
<J_c01,q>=integral_gamma0 q-integral_gamma1 q.   (D1-5)
```

It is conserved by `(D1-4)` and nonzero by the separating one-form in
`(D1-2)`.  Thus the new cycle is record-visible; it is not a formal graph
coordinate or a zero extension.

### 1.2 W1 path/current tuple

Let `r_01:G_0->G_1` be the same-carrier attachment horn and set

```text
f_r01=id_M,
F_r01=id on every old local support,
s_r01(a)=a,
S_r01:K_G0={0}->K_G1 the unique zero-domain injection,
Gamma_r01=(gamma_a |-> gamma_a; new gamma_b retained). (D1-6)
```

Then

```text
partial_G1 s_r01=s_r01^0 partial_G0,
J_G1(S_r01 c)=J_G0(c) for the only c=0,
Supp_G1(S_r01 c) subset F_r01(Supp_G0(c)).       (D1-7)
```

The new current `(D1-5)` lies outside `image(S_r01)` and survives.  The full
family `(D1-2)` is closed under admitted relabeling, frame torsors,
orientation/reality, and simultaneous surface/bundle covariance.  Its
rank-preserving path subdivisions use Q-418 and compose exactly.

In particular the target edge exchange `sigma:a<->b` sends

```text
c_01 |-> -c_01,
J_c01 |-> -J_c01,
H_1 |-> sigma H_1 sigma^*,                       (D1-7a)
```

so the two-leg kernel transforms covariantly and no orientation of the new
cycle is selected.  The source zero carrier and identity bundle data are
fixed by the same simultaneous relabeling.

```text
W1_r01 = INHABITED / TYPE-P
W1_MEMBER_SELECTED = false
```

### 1.3 W4 U(1)-bundle field tuple

The graph attachment changes the finite record stage, not the underlying
DoR-015 surface member.  Use the same physical bundle and fields at both
ends:

```text
M_G0=M_G1=M,
P_G0=P_G1=P,

tilde_f_r01=id_P,
iota_r01:P isomorphic_to id_M^*P the canonical identity,

e_G1=e_G0=e,
mu_G1=mu_G0=mu,
A_G1=A_G0=A,
F_G1=F_G0=F.                                    (D1-8)
```

Every bundle certificate is exact:

```text
pi compose id_P=id_M compose pi;
rank(d id_M)=dim(M), rank(d id_P)=dim(P);
c_1(P)=id_M^*c_1(P);

Cof_r01=id,
Dens_r01=id,
eta_conn,r01(A)=id_P^*A=A,
eta_curv,r01(F)=id_P^*F=F,
eta_curv,r01 Curv=Curv eta_conn,r01.             (D1-9)
```

Density positivity, units, E_post, reality, and characteristic-class
restriction are inherited without choosing a trivialization.  The
flat-holonomy regression passes because the old-image connection equality
is literal; no closed non-gauge-exact one-form is inserted.

```text
W4_r01 = INHABITED / TYPE-P
BUNDLE_OR_GAUGE_MEMBER_SELECTED = false
```

### 1.4 Canonical test transport and relative certificates

Q-408's surface-visible finite test quotient is isomorphic through its
analysis map to `K_G^*`.  Hence `(D1-4)` gives

```text
Tbar_G0={0},
P_r01=Phi_G1^(-1) S_r01 Phi_G0=0.               (D1-10)
```

The complete relative certificate is now executed:

```text
OLD_FID_r01:
  S_r01^*R_K,G1 S_r01=R_K,G0=0;                 PASS

RNL_r01:
  g_K,G1(S_r01 Phi_G0(a),n)=0
  for all a in Tbar_G0 and all disjoint n;        PASS

LR_r01(O):
  P_r01(Tbar_G0(O))={0}
  subset Tbar_G1(F_r01(O));                       PASS. (D1-11)
```

These are exact zero-domain statements, not weakened or assumed versions of
the tests.  For every target profile `H_1`, the old-image kernel square is

```text
Kern_G1^fin(H_1)[P_r01 a,P_r01 b]
 =0
 =Kern_G0^fin(S_r01^*H_1S_r01)[a,b].            (D1-12)
```

For any nonzero one-dimensional profile `H_1`, Q-408 gives

```text
Kern_G1^fin(H_1)=h_tilde J_c01 tensor J_c01 !=0,
h_tilde !=0,                                    (D1-13)
```

where `h_tilde` includes the two fixed Riesz inverses; it is not evaluated.
Faithfulness and `(D1-5)` make it nonzero on suitable target tests.  Thus
`(D1-12)` is an honest old-image
restriction and does not annihilate the new cycle.

### 1.5 The full P4/X4 term on the minimal orbit

Collecting the preceding rows gives

```text
x_r01=(Gamma_r01,P_r01,S_r01,Cof_r01,Dens_r01,
       eta_conn,r01,eta_curv,r01)
      in X4_where(r_01).                         (D1-14)
```

All seven coordinates are actual or derived from actual carriers.  The
bundle lift/isomorphism and `c_1` equation are attached certificates, not an
eighth field.  Every rank-preserving subdivision of either path inherits a
member by Q-418; identity, composition, reality, batching, and exact finite
restriction commute.

```text
FIRST_CYCLE_GENERATOR_MEMBER = BUILT
FIRST_CYCLE_GENERATOR_FAMILY =
  full_covariant_family_over_(B,x,y,gamma_0,gamma_1)
  plus_each_rank_preserving_subdivision_orbit
ABSTRACT_STANDIN_USED = false
```

### 1.6 All-rank extension attack and exact stop

Now start with `K_G != {0}` and add a genuinely new cycle.  W1/W4 can type a
candidate, and the field identity horn can still pass.  But the fixed
DoR-019 metric can mix the transported old analysis image with a physically
disjoint new cycle.  The Q-430 finite witness remains:

```text
K_G=R,
K_G'=R e_U direct-sum R e_V,
S_R x=(x,0),
R_K,G=1,
R_K,G'=[[1,epsilon],[epsilon,1]],
0<|epsilon|<1.                                   (D1-15)
```

It satisfies old-block fidelity but gives

```text
g_K,G'(S_R Phi_G(1),e_V)=epsilon !=0,           (D1-16)
```

so `RNL_R` and local range fail.  DoR-020-A1 correctly rejects this tuple;
it does not prove that some different actual attachment passes at every
rank.  Selecting an attachment or changing `R_K,G'` to make `(D1-16)` vanish
would be witness-by-certificate tuning and is forbidden.

Likewise, the union of two different first-cycle path choices is a
rank-two common target.  The path/bundle union is typeable, but the two
rank-increasing arrows into it must independently pass OLD_FID, RNL, LR and
the actual diamond.  No ratified theorem supplies that joint passage.

Therefore the exact remaining object is

```text
F_Q408^all :=
  a nonempty covariant all-rank subfamily of the adopted W1/W4 law,
  containing actual cycle-rank-increasing members,
  passing OLD_FID+RNL+LR,
  closed under composition and actual common-refinement diamonds. (D1-17)
```

`F_Q408^all` is witness data under the adopted law, not a missing clause and
not a new declaration.  Its nonemptiness is unproved.

```text
FULL_B_Q408_REFINEMENT = PARTIAL / TYPE-U
EXACT_STOP = NONEMPTY_F_Q408^all
LAW_REVISION_NEEDED = false
MACHINERY_APPEAL = false
```

---

## 2. D2 — updated six-fiber ledger and dependency cascade

### 2.1 Enlarged physical core

Let

```text
Ref_01 := Ref_0
          union all r_01 families in (D1-14)
          union their rank-preserving Q-418 subdivisions. (D2-1)
```

This is a genuine stagewise physical subcategory.  It is not declared
directed across different first-cycle choices and is not the full primitive
refinement category.

Each `G_1` was already an actual finite Q-408 object; the new content is the
physical arrow `r_01`, not the target object's finite kernel.  Q-425's C1
local-seminorm construction can therefore be posed on `Ref_01`, with the
previously attained finite bound at `G_1` and Q-418's invariant bound along
its rank-preserving orbit.  Because `P_r01` has zero source domain, the new
arrow supplies no estimate on the target's new-cycle direction.  No estimate
compares distinct path-pair or cycle-rank orbits.

### 2.2 Fiber ledger

| Fiber | Pass-2 status | New positive content | Exact remaining object |
|---|---|---|---|
| `B_Q408_REFINEMENT` | **PARTIAL / TYPE-U** | complete `x_r01` family and every rank-preserving subdivision orbit | `F_Q408^all` in `(D1-17)` |
| `B_R1_NATURAL` | **PARTIAL / TYPE-U** | unchanged `Adm_base` family on ratified old arrows | action/Hessian/reducing-domain naturality on `r_01`, then all-rank arrows |
| `B_C1_COMPLETION` | **PARTIAL / TYPE-U** | actual `r_01` P4 arrow added to its domain; pre-existing finite bounds and one invariant bound per subdivision component retained | cross-rank/component bounded-geometry estimates, one separating topology, attained family bounds, Hilbertizable `W5` |
| `B_FAITHFULNESS` | **PARTIAL / TYPE-U** | Q-408 faithfulness at `G_1` and on each constant subdivision orbit | completed lower separation or safe quotient on the joined carrier |
| `B_C2_RESPONSE_BOUNDARY` | **PARTIAL / TYPE-U** | finite old-image kernel discrepancy on `r_01` is zero; Q-418 zero cocycles retained | action-derived response transport on the new-cycle direction, common-refinement solution, safe ideal, subextensivity |
| `B_C3_MAXWELL_HODGE` | **PARTIAL / TYPE-U** | finite Ward annihilation for `J_c01` and its subdivisions | completed local symbol, closed ranges, Hodge/Maxwell projections, magnetic partner, nonzero normalization |

No full six-bedrock fiber is promoted to inhabited.  The genuine change is
that the `B_Q408` projection now contains a complete cycle-creating P4 term,
and C1's physical core contains an actual arrow from the zero-cycle object
to a previously existing first-cycle finite object.

### 2.3 Executed cascade

```text
x_r01
  -> loads the already-built actual Q-408 A_G1 and Kern_G1^fin on one
     physical cycle-creating arrow
  -> retains the finite target seminorm bounds and faithfulness
  -> rank-preserving orbit bounds/faithfulness by Q-418
  -> finite Ward annihilation for the new cycle
  -> exact old-image zero discrepancy on r_01.
```

The cascade stops before:

```text
an action/Hessian cube on r_01;
a cross-orbit C1 estimate or W5;
a completed faithful kernel;
an action-derived response map on the new cycle;
a completed Maxwell/Hodge symbol.
```

These stops reproduce the six-bedrock independence theorem.  The P4 member
is necessary input to later constructions; it does not derive the other
five roots.

---

## 3. D3 — joint step and remaining EQ6 distance

### 3.1 Equalizer rows on the enlarged subdiagram

| J-family | Result on `Ref_01` | Status |
|---|---|---|
| J1 | algebraic normalized-reader family retained | **family-level only** |
| J2 | `pi_Mx Loc Kernbar Q` absent | **open** |
| J3 | algebraic reader covariance and contravariant finite restriction retained | **verified projection only** |
| J4 | `Adm_base` cubes exist on old arrows; no action/Hessian cube on `r_01` | **open on new arrow** |
| J5 | `h(K_0)=0` remains a rule once a common action term exists | **rule-level only** |
| J6 | Shape-K prepared-direction scope unchanged | **rule-level only** |
| J7 | exact R1-reader pairing has no common R1/P2 term | **uninstantiated** |
| J8 | every displayed C/K crossing uses only R4 | **verified** |
| J9 | the new family batches componentwise; no scalar contraction | **verified** |
| J10 | actual path/current functoriality holds on each `r_01` subdivision component | **verified with component scope** |
| J11 | identity coframe/density normalization and current pushforward hold on `r_01` | **verified with component scope** |
| J12 | finite Q-408 old-image square `(D1-12)` commutes; completed `Eta_r01` absent | **finite projection only** |
| J13 | finite kernel discrepancy is zero; response cocycle/closed ideal/subextensivity remain open | **finite projection only** |
| J14 | finite and component-orbit upper bounds/faithfulness hold; completion horns open | **partial** |
| J15 | tree bottom, first-cycle bottom, and every claimed Q-418 restriction are exact | **verified on built subdiagram** |

### 3.2 Joint regression

The new P4 term does not weaken the permanent equalizer counterexample:

```text
X={x:x=0}, Y={y:y=1}, compatibility x=y.         (D3-1)
```

Here the concrete missing equalities are already visible: no `J4` action
restriction exists on `r_01`, no `J2` reader factorization exists, and no
single completed topology carries J12--J14.  Separate finite P4, kernel,
and Ward terms therefore cannot form an EQ6 witness.

### 3.3 Exact remaining distance

```text
JOINT_EQ6 = PARTIAL

NEW_JOINT_POSITIVE_CONTENT =
  one complete first-cycle P4/X4 family
  + its finite Q-408 kernel square
  + identity density/bundle transport
  + first-cycle finite bounds, faithfulness, and Ward rows.

REMAINING_FRONTIER_IN_DEPENDENCY_ORDER =
  1  F_Q408^all: all-rank/common-refinement P4 family;
  2  B_R1_NATURAL on Ref_01 and then F_Q408^all;
  3  B_C1_COMPLETION on the resulting directed core;
  4  B_FAITHFULNESS on that completion;
  5  B_C2_RESPONSE_BOUNDARY in the same topology;
  6  B_C3_MAXWELL_HODGE;
  7  derived physical reader;
  8  one simultaneous J1--J15 certificate.

FULL_EQ6_TERM = absent
EQ6_DISCHARGED = false
```

The clause layer remains complete.  None of the remaining rows asks for a
new law; each asks for an inhabitant or construction under the adopted law.

---

## 4. D4 — falsifiers, regressions, anti-tuning, and custody

### 4.1 Nine geometric regressions

| Regression | Pass-2 execution | Result |
|---|---|---|
| pure new-cycle profile | `(D1-13)` remains nonzero outside the zero old-image pullback | **PASS** |
| covariance orbit/moduli | all background, path-pair, frame, gauge, and relabeling members retained | **PASS** |
| all-stage skeleton | only actual stagewise `G_0,G_1` and Q-418 subdivisions used | **PASS** |
| rank-preserving `Ref_path` | exact Q-418 squares used after `r_01` | **PASS** |
| cycle-creating upward quotient | none defined; target new-cycle class is its own physical class | **PASS** |
| arbitrary-profile restriction | `(D1-12)` holds for every target profile on the old image | **PASS** |
| Q-430 old-to-new mixer | still rejected by `(D1-16)`; establishes the full-root stop | **PASS** |
| Q-432 `P=id` witness | admitted unchanged on rank-preserving arrows | **PASS** |
| Q-435 bundle/topology | identity lift, full rank, `c_1`, connection equality, and curvature naturality all computed | **PASS** |

### 4.2 Permanent and fresh falsifiers

| Attack | Execution | Result |
|---|---|---|
| abstract kernel | current `(D1-5)` and kernel `(D1-13)` are actual Q-408 objects | **PASS** |
| circular reader | no reader constructs a path, bundle, test, or field | **PASS** |
| misstated nonemptiness | only the explicitly exhibited `r_01` subfamily is called inhabited | **PASS** |
| Hodge from isometry | finite Ward is not promoted to closed-range Hodge data | **PASS** |
| objectwise minimum/selection | no least path, field, lift, or realization chosen | **PASS** |
| joint equalizer | partial terms are not promoted | **PASS** |
| identical-path attack | `gamma_0=gamma_1` or equal distributional currents makes `(D1-5)` zero and is excluded before admission | **PASS** |
| flat-holonomy attack | identity connection equality passes; a non-gauge-exact mismatch would be rejected | **PASS** |
| rank-positive leakage attack | Q-430 rejects the attempted all-rank promotion | **PASS / EXACT STOP** |
| common-refinement union attack | no union diamond is called admitted before both rank-increasing legs pass the relative tests | **PASS / OPEN** |

### 4.3 Surface geometry versus rails

| Territory | Actual surface geometry | Rail/certificate | Status |
|---|---|---|---|
| first cycle | two actual timelike paths with distinct distributional currents | parallel-edge incidence presentation | **BUILT PHYSICALLY** |
| U(1) fields | actual DoR-015 bundle, coframe, density, connection, curvature | identity pullback certificates | **BUILT PHYSICALLY** |
| test transport | zero old test carrier and target-visible new cycle | canonical `P_r01` formula | **BUILT/DERIVED** |
| all-rank continuation | actual rank-positive attachments not exhibited family-wide | W1/W4 merely type candidates | **OPEN PHYSICAL WITNESS DATA** |
| common refinement | Q-418 within each orbit | formal graph union alone is insufficient | **OPEN ACROSS ORBITS** |

No rail-only object is charged as new physics.  The exact stop concerns the
existence of actual surface-supported members satisfying a fixed physical
metric test.

### 4.4 Anti-tuning ledger

```text
1  Freeze DoR-020-A1, Q-408, the relative certificate, and all regressions.
2  Start at the smallest source carrier K_G0={0}; do not inspect a response.
3  Derive the first nonzero cycle from two actual same-endpoint paths.
4  Keep the entire covariant path/background/bundle family; select none.
5  Use identity surface and bundle fields before constructing P_r01.
6  Execute OLD_FID, RNL, LR, the kernel square, and DoR-008 restriction.
7  Feed only the proved P4 core into C1's already registered route.
8  Attempt rank-positive continuation and lead with the Q-430 failure.
9  Re-run all six fibers and the joint equalizer without inherited credit.
10 Bind no computation member and inspect no fixed point, end test, or value.
```

No process fence blocks a structural result.  The all-rank stop is caused by
an unproved nonemptiness statement and a live physical counterexample class.

---

## 5. Final board

```text
GENERATOR_MEMBER = BUILT / FIRST_CYCLE_ORBIT
GENERATOR_MEMBER_X4_COORDINATES = 7/7
BUNDLE_CERTIFICATES = PASS
RELATIVE_CERTIFICATE = PASS
NEW_CYCLE_KERNEL_RETAINED = true

FULL_B_Q408_REFINEMENT = PARTIAL / TYPE-U
FULL_B_Q408_EXACT_STOP = NONEMPTY_F_Q408^all

B_R1_NATURAL = PARTIAL / TYPE-U
B_C1_COMPLETION = PARTIAL / TYPE-U
B_FAITHFULNESS = PARTIAL / TYPE-U
B_C2_RESPONSE_BOUNDARY = PARTIAL / TYPE-U
B_C3_MAXWELL_HODGE = PARTIAL / TYPE-U

JOINT_EQ6 = PARTIAL
FULL_EQ6_TERM = absent
EQ6_DISCHARGED = false

CLAUSE_LAYER_COMPLETE = true
LAW_REVISION_NEEDED = false
NEW_DECLARATION_NEEDED = false

P_COMPUTATION_MEMBER_SELECTED = false
P_COMPUTATION_MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false
MEASURED_CONSTANT_COMPARED = false

TARGET_TUNING_USED = false
ABSTRACT_STANDIN_USED = false
CIRCULAR_CERTIFICATE_USED = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Seal this artifact, mirror artifact and sidecar byte-identically to
`alpha-program-archive/workspace/`, report hashes, and stop.  No register,
plan, tracker, git, commit, or push action belongs to this lane.
