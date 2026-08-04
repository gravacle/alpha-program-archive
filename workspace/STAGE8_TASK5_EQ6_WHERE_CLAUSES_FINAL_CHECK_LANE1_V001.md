# STAGE 8 TASK 5 / EQ6 - WHERE-CLAUSES V005 FINAL CHECK - LANE 1 V001

Date: 2026-08-04
Lane: Codex Lane 1
Task: 5 / EQ6
Custody: final hostile check of Lane 2 where-clause V005 and amendment text

## Lead result

```text
CLAUSES_V005 = SURVIVES
READY_FOR_WHERE_RULING = yes

C1_LAW_ONLY = PASS
C2_BUNDLE_TYPING = PASS
C3_AMENDMENT_TEXT = PASS
C4_REGRESSIONS_AND_FRESH_ATTACK = PASS

AMENDMENT_STATUS = PROPOSED_NOT_ADOPTED
PACKAGING = DOR020_AMENDMENT
MEMBER_BOUND = false
JOINT_EQ6 = OPEN
```

All three defects from Q-435 are repaired exactly.  The operative W1 and W4
clauses define admissible sets that may be empty; they assert no marginal or
joint inhabitance.  The field law now carries a smooth full-rank base map,
a U(1)-equivariant bundle lift or equivalent pullback-bundle isomorphism,
and first-Chern-class compatibility before any connection pullback is
formed.  The amendment text fills only the existing P4/X4 fields adopted by
DoR-020 and preserves the certified joint-witness requirement.

The fresh flat-holonomy attack also passes.  Equality of characteristic
class and curvature does not suffice for membership: a flat but
non-gauge-exact connection mismatch is rejected by the explicit old-image
connection equality.

---

## 0. Preflight, standards, and verdict table

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST?  yes: V005 contains both repaired laws and the
                        proposed DoR-020 amendment text.
IS_THE_VERSION_CURRENT? yes: send-time register head Q-436.
ARE_ITS_INPUTS_PRESENT? yes: Q-435's three defects, DoR-020, package V005,
                        V005 field/bundle data, Q-408, DoR-019, and Q-418.
PREFLIGHT = PASS
```

The artifact was hash-verified before reading:

```text
STAGE8_TASK5_EQ6_WHERE_CLAUSES_LANE2_V005.md
SHA-256 = 19b2060392b6e04448c1c13416b87b67decf401246e3414a783b288fdb5d80ec
SEAL = PASS
```

Verified standards:

| Object | SHA-256 | Use |
|---|---|---|
| locked process | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | geometry/rails rule and custody |
| register at Q-436 | `c361e5af943a8b932c983fb252fe99ab8e211da12f84073bbe2f24270fd01c64` | current scope |
| Q-435 V004 hostile check | `f586e67ac4e97feec8003d06659fa82d83773ce6ef530ee9c3628a9d54a4c57a` | three repair requirements |
| DoR-020 decision | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | conditional package and witness burden |
| continuum package V005 | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | exact P4/X4 carrier |
| field signature V005 | `7ecf04e903512c64af96922f3535f271176d9d376b7ee2d5645ed676dd841b12` | U(1) bundle, surface, path, current, and field types |
| Q-408 current/kernel build | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | actual analysis and finite kernel maps |
| carrier metric V005 | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | fixed Riesz maps and units |
| Q-418 Ref_path theorem | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | rank-preserving boundary |

### 0.2 Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| C1 law-only | **PASS** | operative clauses define possibly empty admissible sets; all inhabitance language is prohibitory, historical, or witness-reserved |
| C2 bundle typing | **PASS** | lift/isomorphism, smooth full rank, `c_1`, composition, restriction, and no-selection all typecheck under geometric attacks |
| C3 amendment text | **PASS** | it populates exactly the seven existing P4/X4 fields and derives transport only after an alleged bundle-typed member is supplied |
| C4 regressions and fresh attack | **PASS** | all nine regressions pass; flat-holonomy mismatch is independently rejected without selecting a gauge lift |

---

## 1. C1 - law-only verification

### 1.1 Operative clause semantics

For each primitive rail arrow, V005 defines

```text
PathRel_adm(r),
FieldExt_adm(R) for R in PathRel_adm(r).         (C1-1)
```

The text then states explicitly that either set may be empty and forbids

```text
law adoption => marginal inhabitance,
marginal inhabitance => joint EQ6 inhabitance.  (C1-2)
```

The W1 and W4 clause bodies use membership language only.  Their reject
horns permit an empty admissible set, and the amendment repeats that
`X4_where(r)` may be empty.  The final boundary leaves inhabitance to one
certified joint J1-J15 witness.

### 1.2 Diff against V004

The two operative V004 phrases were:

```text
"declare a nonempty covariant family PathRel(r)";
"declare a nonempty covariant family FieldExt(R)". (C1-3)
```

Neither appears in an operative V005 clause.  They occur only as quoted
historical text in the delta table, where V005 records their removal.  The
replacement is:

```text
PathRel_adm(r) may be empty;
FieldExt_adm(R) may be empty;
CLAUSE_ASSERTS_INHABITANCE=false.               (C1-4)
```

A text search found `inhabited` only in forbidden implications, explicit
non-assertion statements, historical delta entries, or the sentence saying
what the future witness must prove.  No clause asserts nonemptiness.

```text
NONEMPTY_OVERREACH_REMOVED = true
EQ6_WITNESS_BURDEN_UNCHANGED = true
MEMBER_BINDING_LICENSED = false
C1 = PASS
```

---

## 2. C2 - bundle typing recomputed at geometry

### 2.1 Base and bundle maps

An alleged W1 member supplies a proper smooth map

```text
f_R:M_G->M_G'                                    (C2-1)
```

whose differential has rank `dim(M_G)` on the old physical image.  In the
equal-dimensional DoR-015 family it is a local diffeomorphism there; the
embedded horn separately requires an embedding.  This is enough to pull a
target coframe back nondegenerately on the old image, subject to the
explicit orientation and positivity tests.

For the principal U(1) bundles

```text
pi_G:P_G->M_G,
pi_G':P_G'->M_G',                                (C2-2)
```

an alleged W4 member must supply either a smooth equivariant lift

```text
tilde_f_R:P_G->P_G',
pi_G' tilde_f_R=f_R pi_G,
tilde_f_R(pz)=tilde_f_R(p)z,                     (C2-3)
```

or equivalently an isomorphism

```text
iota_R:P_G isomorphic_to f_R^*P_G'.             (C2-4)
```

The equivalence is correct.  From (C2-3),

```text
p |-> (pi_G(p),tilde_f_R(p))                    (C2-5)
```

is a principal U(1)-bundle map over `id_(M_G)` into the pullback bundle.
Equivariance makes each fiber map an isomorphism of U(1) torsors.  Conversely,
projection of (C2-4) to `P_G'` yields (C2-3).  V005 retains the full
gauge-covariant family and selects neither presentation nor a lift member.

### 2.2 Characteristic class, composition, and restriction

An isomorphism (C2-4) requires

```text
c_1(P_G)=f_R^*c_1(P_G') in H^2(M_G;Z).          (C2-6)
```

V005 uses (C2-6) as a necessary membership test, not as an existence
theorem.  For composable R and S,

```text
f_R^*c_1(P_G')
 =f_R^*f_S^*c_1(P_G'')
 =(f_S compose f_R)^*c_1(P_G''),                (C2-7)
```

so the class condition composes in the correct contravariant order.  On a
restriction or actual common-refinement diamond, ordinary naturality of
cohomological pullback gives the same equality at the common source.

Under U(1) conjugation, both sides change sign:

```text
c_1(conj P)=-c_1(P),                            (C2-8)
```

so the law is reality-covariant rather than incorrectly invariant.

Bundle isomorphisms compose under the canonical pullback associator:

```text
iota_(S compose R)
 =(f_R^*iota_S) compose iota_R.                 (C2-9)
```

At a common target, two lawful composites differ at most by an admitted
U(1) gauge map; their connections agree as covariant classes and curvature
agrees exactly.

### 2.3 Conditional field transport

For an arbitrary alleged W4 member, not a selected member, define

```text
eta_conn,R(A_G')
 =tilde_f_R^*A_G'
 =iota_R^*(f_R^*A_G'),

eta_curv,R(F_G')=tilde_f_R^*F_G',
eta_cof,R(e_G')=f_R^*e_G',
eta_dens,R(mu_G')=f_R^*mu_G'.                  (C2-10)
```

Every expression is now on the correct carrier.  Functoriality gives

```text
eta_curv,R(Curv(A_G'))
 =Curv(eta_conn,R(A_G')),                       (C2-11)
```

and composition follows from (C2-9).  Full rank protects coframe
nondegeneracy; orientation compatibility protects density positivity;
coframe/density duality and R4 units remain explicit failure-capable tests.

### 2.4 Geometry attacks

**Cycle creation.**  A formal cycle-creating map with unrelated path
supports fails W1.  If paths pass but (C2-6) fails, the W4 set has no member
for that relation.  Neither the rail map nor a formal connection symbol can
repair the topological mismatch.  New target-cycle kernels remain outside
the old pullback.

**Rank-two exchange.**  Exchange/relabeling transports the entire path,
bundle-lift, and field family.  Equations (C2-6) and (C2-10) are natural,
and no cycle basis, bundle trivialization, or lift is selected.

**Pendant interaction.**  Gate-4 removes pendant/tree coefficients before
the cycle test map is constructed.  W4 may still test ordinary local fields
on a new pendant cell, but it cannot create a scalar cycle current or kernel
direction.  A field lift on a pendant is therefore geometric data, not a
back door into the physical cycle carrier.

```text
BUNDLE_LIFT_TYPING = PASS
SMOOTH_FULL_RANK = PASS
CHARACTERISTIC_CLASS_COMPOSITION = PASS
CHARACTERISTIC_CLASS_RESTRICTION = PASS
CYCLE_CREATING_ATTACK = PASS_WITH_EMPTY_HORN
RANK_TWO_ATTACK = PASS
PENDANT_ATTACK = PASS
C2 = PASS
```

---

## 3. C3 - amendment text and exact P4/X4 population

### 3.1 DoR-020 scope

DoR-020 adopted package V005's eight clauses, fifteen compatibility
families, derived path-subdivision square, PL refinement core, typed
P4/P5/P7/P8 rules, and permanent regressions, conditional on the joint
J1-J15 equalizer over six generators.  It forbids member binding,
fixed-point execution, and any end test before a certified witness.

Its P4 carrier is

```text
x_R=(Gamma_R,P_R,S_R,Cof_R,Dens_R,
     eta_conn,R,eta_curv,R) in X4(R).           (C3-1)
```

### 3.2 Field-by-field population

| Existing X4 field | V005 amendment source | Status |
|---|---|---|
| `Gamma_R` | W1 actual refined paths modulo admitted Q-408 line-integral equality | exact |
| `S_R` | injective conserved-current map induced by the same path relation | exact |
| `P_R` | canonical `Phi_G'^{-1}S_RPhi_G`, subject to old fidelity, RNL, and local range | derived, not declared |
| `Cof_R` | W4 smooth full-rank coframe relation | exact |
| `Dens_R` | positive unit-correct density dual to `Cof_R` | exact |
| `eta_conn,R` | bundle-typed connection pullback in (C2-10) | conditionally derived |
| `eta_curv,R` | curvature pullback/naturality in (C2-10)--(C2-11) | conditionally derived |

The lift/isomorphism and `c_1` data are certificates required to type the
existing connection/curvature fields.  They are not an eighth X4 field, a
new generator, or a new theory stratum.

### 3.3 Amendment boundary

The draft amendment:

1. preserves all six DoR-020 generators and J1-J15;
2. replaces only the uninstantiated P4/X4 where-slots by the possibly empty
   admissible subcarrier `X4_where(r)`;
3. states W1, canonical W2, and bundle-typed W4 exactly;
4. carries the old-fidelity, relative no-leakage, and local-range tests;
5. binds no member and asserts no marginal or joint inhabitance;
6. leaves C1 resumption, fixed-point execution, and the end test forbidden
   until a certified joint witness exists.

No response property, threshold, numerical consequence, Hodge operator,
reader, or additional physical field appears in the amendment.

```text
P4_X4_POPULATION = EXACT
EXTRA_AUTHORED_FIELD = none
SEVENTH_GENERATOR = false
CONDITIONAL_TRANSPORT = PASS
PACKAGING = DOR020_AMENDMENT
C3 = PASS
```

---

## 4. C4 - regression ledger, smuggling audit, and fresh attack

### 4.1 Nine cumulative regressions

| Regression | Independent result |
|---|---|
| pure new-cycle profile | **PASS** - retained outside old-image pullback |
| covariance orbit/moduli | **PASS** - complete admissible families retained |
| all-stage skeleton | **PASS** - stagewise actual surfaces only |
| rank-preserving Ref_path | **PASS** - `f=id`, identity bundle lift, `P=id` |
| cycle-creating upward quotient | **PASS** - none defined |
| arbitrary-profile restriction | **PASS WITH SCOPE** - old-image only; new target kernel survives |
| Q-430 old-to-new mixer | **PASS** - rejected by RNL/local range |
| Q-432 `P=id` witness | **PASS** - admitted; pre-existing metric cross term allowed |
| Q-435 bundle/topology attack | **PASS** - ill-typed or class-mismatched tuple rejected before pullback |

The permanent abstract-kernel, circular-reader, misstated-nonemptiness,
Hodge-from-isometry, objectwise-selection, and joint-equalizer regressions
also pass.  In particular, an empty admissible family leaves EQ6 open and
is not mislabeled a clause failure or a witness.

### 4.2 Smuggling and "too easy"

The two laws are anchored in actual V005 paths, the ratified U(1) bundle
family, Q-408 currents, and existing P4 fields.  The construction order
freezes those carriers before drafting membership conditions.  It uses no
response, reader, threshold, fixed point, end test, or measured datum.

The bundle lift does not make inhabitance easy: it adds a failure-capable
global compatibility condition and explicitly permits the family to remain
empty.  The repair therefore exposes rather than relocates the obstruction.

### 4.3 Fresh attack: flat-holonomy mismatch

Take the same base surface and isomorphic U(1) bundles with

```text
c_1(P_G)=c_1(P_G'),
F_G=F_G'.                                        (C4-1)
```

Let the target connection differ on the old image by a closed one-form
`alpha_flat` whose holonomy is not removable by an admitted U(1) gauge
transformation:

```text
A_G'=A_G+alpha_flat,
d alpha_flat=0,
[alpha_flat] not gauge-exact.                   (C4-2)
```

Characteristic-class and curvature tests alone pass.  Nevertheless no
retained lift/gauge member satisfies the required old-image equality

```text
A_G=tilde_f_R^*A_G'.                            (C4-3)
```

The tuple is rejected.  If `alpha_flat` is gauge-exact, the corresponding
lift remains in the full covariant family and no representative is selected.
Thus V005 does not confuse topological bundle compatibility with connection
compatibility.

```text
FLAT_HOLONOMY_ATTACK = PASS / mismatch_rejected
TARGET_TUNING_USED = false
SMUGGLED_FIELD = none
C4 = PASS
```

### 4.4 Surface geometry versus rails

| Territory | Surface geometry | Rails/certificates | Verdict |
|---|---|---|---|
| W1 path/current law | actual smooth path and support relation | incidence/composition equations | **PASS AS LAW** |
| W2 test transport | local supported range on actual surface | canonical carrier formula | **PASS CONDITIONALLY** |
| relative locality | recorded disjoint/connectivity support | fixed-metric predicates | **PASS CONDITIONALLY** |
| W4 field law | U(1) bundle lift, coframe/density, connection, curvature | `c_1`, pullback, covariance, diamond certificates | **PASS AS LAW** |

The two where-laws remain genuine surface/field content inside
`B_Q408_REFINEMENT`; the canonical maps and certificates remain derived
conditions.  No rail-only requirement is charged as a new declaration.

---

## 5. Final disposition

```text
CLAUSES_V005 = SURVIVES
READY_FOR_WHERE_RULING = yes

LAW_ONLY = PASS
BUNDLE_TYPING = PASS
AMENDMENT_TEXT = PASS
NINE_REGRESSIONS = PASS
FLAT_HOLONOMY_ATTACK = PASS

PACKAGING = DOR020_AMENDMENT
AMENDMENT_STATUS = PROPOSED_NOT_ADOPTED
MEMBER_SELECTED = false
MEMBER_BOUND = false
FULL_Ext_cycle_MEMBER = OPEN / TYPE-U
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN
C1_RESUMPTION = N-A

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

No register, plan, tracker, git, commit, or push action belongs to this lane.
