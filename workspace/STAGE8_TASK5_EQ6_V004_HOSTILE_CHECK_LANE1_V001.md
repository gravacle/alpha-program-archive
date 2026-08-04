# STAGE 8 TASK 5 / EQ6 - EXHIBIT V004 HOSTILE CHECK - LANE 1 V001

Date: 2026-08-04
Lane: Codex Lane 1
Task: 5 / EQ6
Custody: hostile review of Lane 2 V004; where-clause placement determination

## Lead result

```text
V004 = KILLED(A3+A5)

A1_CANONICAL_TEST_TRANSPORT = PASS
A2_RELATIVE_CERTIFICATE = PASS

CLAUSES = DEFECTIVE(
  R1_NONEMPTY_WORDING_CONFLICTS_WITH_EQ6_WITNESS_CONDITION;
  R4_NONEMPTY_WORDING_CONFLICTS_WITH_EQ6_WITNESS_CONDITION;
  R4_CONNECTION_PULLBACK_HAS_NO_BUNDLE_LIFT_OR_PULLBACK_BUNDLE_ISOMORPHISM;
  R4_COFRAME_PULLBACK_HAS_NO_SMOOTH_FULL_RANK_MAP_CERTIFICATE;
  R4_TOPOLOGICAL_COMPATIBILITY_NOT_STATED
)

PACKAGING = DOR020_AMENDMENT |
  after repair, the clauses specialize the already adopted P4/X4 fields
  inside B_Q408_REFINEMENT; they do not create a seventh generator or a
  new theory layer.  The amendment must define admissible, possibly empty
  families and leave nonemptiness to the certified joint EQ6 witness.

READY_FOR_WHERE_RULING = no
C1_RESUMPTION = N-A
JOINT_EQ6 = OPEN
```

The construction layer is sound.  Once an actual path/current candidate is
given, the test transport is uniquely forced by the ratified analysis and
Riesz maps.  The corrected relative certificate admits the Q-432 `P=id`
witness, rejects the Q-430 old-to-new mixer, and handles the exact physical
connectivity boundary by combining pairing no-leakage with local supported
range.

The declaration layer is not yet DoR-grade.  Its clauses conflate an
admissibility law with nonemptiness, which DoR-020 deliberately reserves for
the certified `[EQ6]` witness.  The R4 derivation also writes `f_R^*A` for
connections on different U(1) bundles without supplying a bundle lift or an
isomorphism from the source bundle to the pullback target bundle.  That is a
typing failure before any curvature-naturality proof can begin.

---

## 0. Preflight, standards, and verdict table

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST?  yes: V004 and both clause candidates exist.
IS_THE_VERSION_CURRENT? yes: send-time register head Q-434.
ARE_ITS_INPUTS_PRESENT? yes: the three prior hostile results, corrected R
                        typing, DoR-020, V005, Q-408, DoR-019, and Q-418.
PREFLIGHT = PASS
```

V004 was hash-verified before reading:

```text
STAGE8_TASK5_EQ6_Q408_PRIMITIVE_GENERATOR_EXHIBIT_LANE2_V004.md
SHA-256 = c5254f663a1e3a6d1079027184c6dea96a35ab7255a856aa39e584b3d7c32dc2
SEAL = PASS
```

Verified standards:

| Object | SHA-256 | Use |
|---|---|---|
| locked process | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | geometry/rails rule and custody |
| register at Q-434 | `2003820ba0a1845cebe3fb8ba98ffe3bfd91e9aa318b824b6a537246e86bfb74` | current scope |
| first hostile kill | `505bd329b29a45bf57feec84b89c2fa53481a8117808df81872e15194b16d825` | real new-cycle kernel test |
| second hostile kill | `4bfe044d62247950089142715e1534695922ac17c34e239cc63097df090347a1` | support-separated Riesz mixer |
| corrected R typing / third kill | `99c34408b86f93a343b372595bb7f7b199501b1eaab4ef241d5aea2f853f9757` | relative condition and two/two split |
| DoR-020 decision | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | adopted package scope and EQ6 condition |
| field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | surface, bundle, path, field, current carriers |
| Q-408 kernel build | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual analysis and finite kernel maps |
| carrier metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed Riesz maps and W3 scope |
| Q-418 Ref_path theorem | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | rank-preserving physical square |

### 0.2 Register sweep

The sweep checked Q-297, Q-355, Q-384, Q-408, Q-418, Q-423 through Q-425,
and Q-427 through Q-434.  No new entry changes the Q-432 split:

```text
R1 path/current relation       = declared member data;
R2 physical test transport     = construction after R1;
R3 relative no-leakage         = fixed-carrier certificate;
R4 local field member          = declared member data;
R4 transport after member      = conditional derivation.
```

### 0.3 Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| A1 canonical test transport | **PASS** | the formula is uniquely forced and survives cycle-creating, exchange, and pendant attacks; physical use remains conditional on failure-capable certificates |
| A2 relative certificate | **PASS** | it matches Q-432, admits `P=id`, rejects the old-to-new mixer, and uses `LR` to resolve support at the connectivity boundary |
| A3 two clause candidates | **KILL** | both improperly declare nonemptiness, and R4 lacks the bundle/tangent data required to type its pullbacks |
| A4 packaging | **PASS AS DETERMINATION** | repaired clauses belong in a DoR-020 amendment because they fill already adopted P4/X4 slots within B_Q408 |
| A5 regressions and fresh attacks | **KILL** | the eight mathematical regressions pass, but bundle-lift and U(1) topological attacks defeat R4 as a DoR-grade clause |

---

## 1. A1 - canonical test transport

### 1.1 Recalculation

At an actual finite source and target let

```text
Abar_G:Tbar_G->K_G^*,
R_G:K_G->K_G^*,
Phi_G=R_G^(-1)Abar_G.                            (A1-1)
```

After a candidate actual path/current relation supplies an injective
`S_R:K_G->K_G'`, define

```text
P_R=Phi_G'^(-1)S_RPhi_G
   =Abar_G'^(-1)R_G'S_RR_G^(-1)Abar_G.          (A1-2)
```

All maps in (A1-2) are finite-dimensional isomorphisms on the
surface-visible quotients, so P_R exists uniquely and is bounded.  Directly,

```text
Phi_G'P_R=S_RPhi_G.                              (A1-3)
```

For every target profile H', Q-408 therefore gives

```text
Kern_G'(H')[P_Ra,P_Rb]
 =Kern_G(S_R^*H'S_R)[a,b].                      (A1-4)
```

If the old-image fidelity condition

```text
S_R^*R_G'S_R=R_G                                (A1-5)
```

passes, then

```text
S_R^*Abar_G'P_R=Abar_G,                         (A1-6)
```

which is the physical old-current pairing square.  The map is canonical as
an algebraic construction.  Calling it physical still requires its local
range and the actual R1 relation.

### 1.2 Cycle-creating attack

Let the target split as an old image plus a new cycle.  Equation (A1-4)
restricts only the old image.  A target profile supported on the new cycle
can have zero old pullback while its target kernel remains nonzero on target
tests outside `image(P_R)`.  No new-cycle content is deleted.  This meets the
first hostile kill.

### 1.3 Rank-two exchange

Let `U_G,U_G'` be an admitted exchange/relabeling on source and target
cycle carriers and `V_G,V_G'` the corresponding test actions.  Ratified
covariance has the typed form

```text
Phi_(UG) V_G=U_G Phi_G,
S_(URU^-1)=U_G' S_R U_G^(-1).                   (A1-7)
```

Substitution into (A1-2) gives

```text
P_(URU^-1)=V_G' P_R V_G^(-1).                  (A1-8)
```

Thus the full rank-two family transforms covariantly.  No exchange member,
cycle basis, or orientation is selected.

### 1.4 Pendant interactions

A pendant/tree coefficient is removed before this construction because the
physical scalar current carrier is `ker(B^T)` after Gate-4 descent.  On a
connected tree the cycle part is zero.  On a graph with a pendant attached
to a loop, (A1-2) acts only on the loop-visible quotient; test variations
annihilated by Abar remain zero classes.  Hence P_R neither manufactures a
pendant cycle nor assigns positive kernel content to one.

```text
A1_CYCLE_CREATING = PASS
A1_RANK_TWO_EXCHANGE = PASS
A1_PENDANT = PASS
A1_OVERALL = PASS
```

---

## 2. A2 - relative no-leakage and its boundary

### 2.1 Exact match to the corrected condition

For `a in Tbar_G(O)` define the transported local-analysis vector

```text
x_R(a)=S_RPhi_G(a).                              (A2-1)
```

V004's `RNL_R` is

```text
g_K,G'(x_R(a),n)=0
for all n in K_G'(V),
whenever F_R(O) intersect V=empty.              (A2-2)
```

This is exactly the Q-432 condition.  It quantifies over the transported
local-analysis image, not all localized old current vectors.  V004 also
keeps the independent local-range condition

```text
P_R(Tbar_G(O)) subset Tbar_G'(F_R(O)).           (A2-3)
```

Equation (A2-3) is stronger geometrically.  Under the actual current pairing
it implies (A2-2), but retaining both is useful: (A2-2) diagnoses metric
leakage, while (A2-3) verifies existence of a supported representative.

### 2.2 `P=id` witness admitted

For two already-present disjoint cycles take

```text
R_G=R_G'=[[1,epsilon],[epsilon,1]],
S_R=id,
Abar_G=Abar_G'=id,
0<|epsilon|<1.                                   (A2-4)
```

Then P_R=id.  For the U-local analysis covector a,

```text
g_K(Phi_G(a),e_V)
 =<R_GR_G^(-1)a,e_V>
 =<a,e_V>=0.                                    (A2-5)
```

The global cross term `g_K(e_U,e_V)=epsilon` is allowed.  Both (A2-2) and
(A2-3) pass, so the Q-432 witness is admitted.

### 2.3 Old-to-new mixer rejected

For one old cycle and one disjoint new target cycle,

```text
S_Rx=(x,0),
R_G=1,
R_G'=[[1,epsilon],[epsilon,1]].                 (A2-6)
```

The constructed test is `(1,epsilon)`, and

```text
g_K,G'(S_RPhi_G(1),e_new)=epsilon.              (A2-7)
```

Thus `RNL_R` fails.  Its test class also has support in the disjoint new
sector, so `LR_R` fails independently.

### 2.4 Fresh boundary attack: recorded connectivity

Let a new target current `n_W` have support W meeting `F_R(O)` at a recorded
incidence/contact region.

* If the transported test has a representative wholly supported in
  `F_R(O)`, then (A2-3) passes.  Because the supports are not disjoint, the
  antecedent of (A2-2) is false; pairing through the recorded contact is
  allowed.
* If the transported test extends along `W\F_R(O)`, (A2-2) may remain
  silent because the supports touch, but (A2-3) fails.  Mere endpoint
  contact cannot license support along an entire new path.
* If W is disjoint from `F_R(O)`, both predicates reject any nonzero
  leakage.

This is the correct three-way boundary: disjoint leakage is forbidden,
recorded contact is permitted, and nonlocal spill beyond the mapped region
is still rejected.

```text
A2_DEFINITION_MATCH = PASS
A2_P_ID = ADMITTED
A2_SECTOR_MIXER = REJECTED
A2_CONNECTIVITY_BOUNDARY = PASS
A2_OVERALL = PASS
```

---

## 3. A3 - DoR-grade audit of the two clause candidates

### 3.1 R1 path/current clause

The geometric content is correctly minimal:

```text
f_R:M_G->M_G',
F_R:Loc_G->Loc_G',
s_R:C_1(G)->C_1(G'),
S_R=s_R|K_G,
f_R gamma_(G,e)=ordered target-child path chain,
J_G'(S_Rc)=f_(R*)J_G(c).                        (A3-1)
```

It cites actual V005 paths and Q-408 current distributions, not a signed
chain rail as its geometry.  Its embedded, same-carrier attachment, and
reject alternatives are physically distinct in scope, although the final
wording should state that the identity attachment is the same-carrier horn
of the embedding family rather than pretending the sets are disjoint.
Its support, orientation, cycle-deletion, unrelated-path, covariance, and
common-refinement void conditions are finite and testable.

The defect is one phrase with major governance consequences:

```text
"declare a nonempty covariant family PathRel(r)". (A3-2)
```

DoR-020 is conditional on a certified joint-equalizer witness.  A where-law
may define the admissible `PathRel(r)` family, but it may not assert that the
family is nonempty and then continue to list nonemptiness as an unproved
EQ6 obligation.  The repaired clause must read:

```text
define the covariant admissible family PathRel(r), possibly empty until the
certified EQ6 witness exhibits a joint member.   (A3-3)
```

Ratification of (A3-3) chooses a law of admissibility, not an inhabitant and
not nonemptiness.

```text
R1_GEOMETRY_ANCHOR = PASS
R1_ALTERNATIVES_AND_VOID_CONDITIONS = PASS_WITH_SCOPE_PRECISION
R1_BLINDNESS = PASS
R1_DOR_GRADE = FAIL / nonemptiness_laundering
```

### 3.2 R4 local-field clause: base-map pullback is not enough

The field list and its intended compatibilities are appropriate: coframe,
positive density, connection, curvature, units, support, reality, E_post,
composition, and actual diamonds.  The construction order is also blind to
all downstream values.

However, V004 writes

```text
eta_conn,R=f_R^* on connections,
eta_curv,R=f_R^* on curvature.                  (A3-4)
```

Let

```text
pi_G:P_G->M_G,
pi_G':P_G'->M_G'                                (A3-5)
```

be the ratified U(1) bundles carrying the two connections.  A base map
`f_R:M_G->M_G'` pulls a target connection back to the pullback bundle
`f_R^*P_G'`.  It does not produce a connection on `P_G`.  To compare with
the source field and state old-image agreement, one needs either

```text
tilde_f_R:P_G->P_G' over f_R,                   (A3-6)
```

or an equivariant bundle isomorphism

```text
iota_R:P_G isomorphic_to f_R^*P_G'.             (A3-7)
```

No such family appears in R1 or R4.  Endpoint-frame intertwiners do not
automatically extend to a bundle map over an entire refined support region.
Without (A3-6) or (A3-7), (A3-4) and the curvature equation are ill-typed.

The coframe formula has an analogous base regularity requirement.  Pullback
preserves a nondegenerate coframe only when `f_R` is smooth with the required
full-rank tangent map on the old image.  R1's generic "proper
orientation-compatible local map" does not state that condition.

Finally, a U(1) bundle isomorphism has a topological obstruction:

```text
c_1(P_G)=f_R^* c_1(P_G').                       (A3-8)
```

The clause neither requires (A3-8) nor makes its failure a void condition.
The phrase "empty family" cannot repair an undefined pullback type; the
carrier and compatibility test must be stated first.

R4 repeats the nonemptiness problem in (A3-2): it declares a nonempty
`FieldExt(R)` while the final board still requires proof of a nonempty joint
R1/R4 family.  It must instead define a possibly empty admissible family and
leave inhabitance to EQ6.

A repaired R4 member must include:

```text
smooth full-rank f_R on the old image;
an equivariant bundle-lift/isomorphism family iota_R;
the topological compatibility (A3-8);
coframe/density old-image compatibility;
connection pullback through iota_R;
curvature naturality and all existing family certificates;
possible emptiness until a certified joint witness exists. (A3-9)
```

Then, and only then, field transport and
`eta_curv Curv=Curv eta_conn` follow functorially.

```text
R4_GEOMETRY_ANCHOR = INCOMPLETE
R4_ALTERNATIVES = GENUINE_BUT_UNTYPED_WITHOUT_BUNDLE_HORN
R4_VOID_CONDITIONS = INCOMPLETE / missing_bundle_and_topology_tests
R4_BLINDNESS = PASS
R4_CONDITIONAL_TRANSPORT_DERIVATION = FAIL_BEFORE_TYPECHECK
R4_DOR_GRADE = FAIL
```

### 3.3 Order-of-construction audit

V004 freezes the prior counterexamples, actual carriers, and local sectors;
constructs P_R; constructs the relative predicates; and only then drafts
the two clauses.  It inspects no response, threshold, fixed point, end test,
or measured datum.  The order is target-blind.

```text
ORDER_OF_CONSTRUCTION = PASS
TARGET_TUNING = false
CLAUSE_RESULT = DEFECTIVE_BY_TYPING_AND_EQ6_GOVERNANCE_NOT_BY_TUNING
```

---

## 4. A4 - packaging under DoR-020

### 4.1 What DoR-020 adopted

The decision of record states that the continuum package is adopted
conditionally on the joint J1-J15 equalizer over six named generators,
including `B_Q408_REFINEMENT`.  Its adopted content explicitly includes:

```text
package V005's eight clauses;
the fifteen derived compatibility families;
the derived path-subdivision square;
the PL refinement core;
the typed P4/P5/P7/P8 rules;
the permanent regressions.                      (A4-1)
```

Package V005's P4 carrier already has slots for actual paths, test/current
maps, coframe, density, connection transport, and curvature transport.  It
stops on nonemptiness of the actual Q-408 primitive-generator fiber.

### 4.2 Amendment versus new decision

The repaired R1 and R4 laws do not add a seventh generator, a new consumer,
or a new field species.  They specify admissible member data in the existing
P4/X4 slots of `B_Q408_REFINEMENT`.  Therefore their honest placement is:

```text
PACKAGING = DOR020_AMENDMENT.                    (A4-2)
```

The amendment must:

1. add the repaired R1 and R4 admissibility laws;
2. include the bundle/tangent conditions in (A3-9);
3. keep both admissible families possibly empty before the witness;
4. keep all R2/R3 tests and the eight regressions binding;
5. preserve DoR-020's joint-equalizer condition and pre-witness prohibitions;
6. bind no member and claim no C1 resumption until a certified joint witness
   inhabits the amended family.

A separate DoR-021 would misstate these clauses as physics beyond the
adopted continuum package and would make the same B_Q408 content look like a
new root.  A future numbered decision may record the principal's amendment
procedurally, but its mathematical status is an amendment to DoR-020.

```text
PACKAGING_DETERMINATION = PASS
CURRENT_CLAUSES_READY_FOR_PACKAGING = false
```

---

## 5. A5 - regressions, smuggling audit, and fresh attacks

### 5.1 Eight-regression ledger

| Regression | Independent result |
|---|---|
| pure new-cycle profile | **PASS** - target kernel remains outside old pullback |
| covariance orbit/moduli | **PASS** - no representative selected |
| all-stage skeleton | **PASS** - stagewise only |
| rank-preserving Ref_path | **PASS** - `P=id` and exact current/kernel square |
| cycle-creating upward quotient | **PASS** - none installed |
| arbitrary-profile restriction | **PASS WITH SCOPE** - old-image only until member admission |
| Q-430 old-to-new mixer | **PASS** - rejected by RNL and LR |
| Q-432 `P=id` counterexample | **PASS** - admitted |

The permanent abstract-kernel, circular-reader, misstated-nonemptiness,
Hodge-from-isometry, objectwise-selection, and joint-equalizer attacks also
remain active.  The current clause wording itself trips the
misstated-nonemptiness regression, despite the table marking it passed.

### 5.2 Smuggling and the formal "too easy" question

The construction layer does not smuggle geometry: P_R and RNL are openly
conditional on R1.  The exhibit does not claim a full member or C1
resumption.  Its success is therefore not definitionally vacuous.

The clause layer does relocate two difficulties into declarations, which is
lawful only if the declarations are exact.  R1 is geometrically meaningful;
R4 is not yet typed across the U(1) bundle, so its apparent completion is too
easy by one carrier level.

### 5.3 Fresh attack 1: bundle-lift ambiguity

Fix the same base map f_R and target connection.  Distinct equivariant bundle
lifts can differ by a U(1) gauge transformation over the old image.  Without
retaining the full covariant lift family or quotienting it by the ratified
gauge action, `f_R^*A` is ambiguous as source-bundle data.  Choosing one lift
would violate no-selection; omitting all lifts leaves the map undefined.

```text
BUNDLE_LIFT_ATTACK = FAIL / R4
```

### 5.4 Fresh attack 2: topological pullback obstruction

Choose admitted source and target U(1) bundles whose characteristic classes
do not satisfy (A3-8) for a proposed base refinement.  Objectwise fields,
paths, supports, and every rail equation may still exist, but no equivariant
isomorphism (A3-7) exists.  Hence the old-image connection agreement required
by R4 cannot be formed.  This is an actual field-geometry obstruction, not a
rail defect.

```text
U1_TOPOLOGY_ATTACK = FAIL / R4
```

### 5.5 Surface geometry versus rails

| Territory | Surface geometry | Rails/constructions | Verdict |
|---|---|---|---|
| finite and Ref_path | actual paths, currents, supports, `P=id` | exact squares | **PASS** |
| R2 test transport | physical only after local range | canonical algebraic map | **PASS AS CONSTRUCTION** |
| R3 relative locality | actual disjoint/connected support tested | fixed-metric predicate | **PASS AS CERTIFICATE** |
| R1 where-law | actual path/current relation stated | covariance/composition equations | **REPAIR nonempty wording** |
| R4 where-law | bundle/tangent realization incomplete | typed field slots and formal pullback symbols | **KILL** |

The R1 and repaired R4 member laws remain actual surface/field content, not
rail artifacts.  R2 and R3 remain constructions and do not cost separate
declarations.

---

## 6. Final disposition

```text
V004 = KILLED(A3+A5)

CLAUSES = DEFECTIVE(
  R1: replace declared_nonempty by admissible_possibly_empty_until_EQ6;
  R4: same EQ6 repair + smooth_full_rank_map + equivariant_bundle_lift
      or pullback_bundle_isomorphism + characteristic_class_compatibility
)

PACKAGING = DOR020_AMENDMENT |
  the repaired laws instantiate existing P4/X4 content inside the already
  adopted B_Q408_REFINEMENT generator; no seventh root is created.

READY_FOR_WHERE_RULING = no

A1_CANONICAL_TEST_TRANSPORT = PASS
A2_RELATIVE_NO_LEAKAGE = PASS
ACTUAL_FINITE_AND_Ref_path_CORE = PASS / TYPE-P
Ext_cycle_FULL_MEMBER = OPEN / TYPE-U
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN
C1_RESUMPTION = N-A

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

No register, plan, tracker, git, commit, or push action belongs to this lane.
