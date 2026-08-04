# STAGE 8 TASK 5 / EQ6 - EXHIBIT V002 HOSTILE CHECK - LANE 1 V001

Date: 2026-08-04  
Task: PASTE 506 / Task 5 / EQ6  
Lane: Codex Lane 1  
Custody: adversarial review of Lane 2 exhibit V002  
Standing: DoR-020 conditional on `[EQ6]`; Q-427 geometry/rails rule binding

## Lead result

```text
EXHIBIT_V002 = KILLED(
  W1 + W2 + W5 + W7;
  anatomy = THE_EXT_CYCLE_REPAIR_IS_A_CORRECT_RAIL_PULLBACK
            BUT_NOT_AN_ACTUAL_SURFACE_REFINEMENT_MAP
)

GEOMETRY_VS_RAILS =
  GEOMETRY_PROVED:
    each ratified finite S_G has its actual Q408 paths/currents/kernel;
    Ref_path has its actual path restriction;
    a ratified target's new-cycle tests and kernels remain nonzero;

  RAILS_PROVED:
    any injective signed cycle map S_R induces
    I_R^T=Abar_G'^(-1) R_G' S_R R_G^(-1) Abar_G;
    the resulting kernel pullback, covariance, composition, and conditional
    diamonds commute algebraically;

  GEOMETRY_NOT_PROVED:
    that S_R is induced by an actual path/current refinement;
    that I_R^T is a support/locality-preserving physical test transport;
    coframe/density/connection/curvature transport on cycle-creating arrows;
    an actual interior-cell/common-refinement target.

C1_RESUMPTION = N-A
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

V002 correctly repairs the false V001 kernel identity and preserves the new
cycle's physical kernel.  It also correctly withdraws the one-orbit and
all-stage-skeleton claims.  The kill is the next layer: the new injection is
defined from rail data so that the kernel square commutes.  No actual
path-support/current-transport theorem makes the signed map a physical
refinement.  The artifact therefore overlabels a lawful algebraic pullback as
surface geometry.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
```

---

## 0. Preflight, authorities, and governing split

### 0.1 Three-line preflight

The revised locked process was read in full.  V002's artifact hash and seal
were verified before its contents were read.

```text
DOES_THE_OBJECT_EXIST = yes | V002 exists and is sealed
IS_THE_VERSION_CURRENT = yes | register head Q-429
ARE_ITS_INPUTS_PRESENT = yes | V002, Q-428 kill, frontier, regressions, Q-408
PREFLIGHT = PASS
```

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process with Q-427 rule | `d537e294c03b3fc50fa49844f5b166bdcee1d64fe1513b9201047f602cd1518f` | custody and geometry/rails split |
| register at Q-429 | `2acf3c1328319fdec4ead3adc31873e067f9dbe228f816b47787e06a8f0920e1` | current scope |
| exhibit V002 under review | `686b2c4a0e6c60f54a9173d8554efce116df4a332fc318cb1ffae32bb4cdf930` | target |
| V001 hostile kill | `505bd329b29a45bf57feec84b89c2fa53481a8117808df81872e15194b16d825` | repair anatomy |
| frontier row 1A | `b8294e917531dd4f1731aedd54fd1c52a320840335061bbb4ab872830d001028` | actual-generator contract |
| hostile regression source | `510ebda9c05220b3eb229e865a0a41868f5ce166ff2a5805762d540309a6ab1b` | five permanent regressions |
| minimal-six/equalizer theorem | `288a3d4147cb10f2e51180b21f7c6b2b4749503504c57b8a1121e3925c70c94c` | joint regression |
| C1 build | `5203347c9bba7f99c2f033467815defa7ac047f74ea73b313972f44975d250a5` | handoff test |
| Q-408 physical kernel | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | finite geometry and restriction scope |

### 0.2 The binding geometry/rails test

For every V002 claim this review asks separately:

```text
SURFACE GEOMETRY:
  is the map induced by actual incidence/path/current/local-support data on
  the record surface?

RAILS:
  or does the map commute because it was assembled from category, cycle,
  Riesz, and duality maps to make the square commute?
```

An actual source surface and an actual target surface do not by themselves
make an arbitrary signed map between them an actual geometric refinement.
The relation must also be surface-anchored.

---

## 1. Verdict table W1-W7

| Item | Verdict | One-line reason |
|---|---|---|
| W1 repaired square at geometry | **KILL** | the old counterexample, multi-cycle, exchange, and pendant cases pass algebraically; a support-separated two-surface witness shows `I_R^T` need not be a physical refinement transport |
| W2 stagewise anchors | **KILL** | finite objects and `Ref_path` are surface-anchored, but `Ext_cycle` cites V003's signed cellular restriction, a rail; target-stage physicality does not anchor the relation |
| W3 three removed clauses | **PASS** | all three are rail-only overreaches; removing them breaks no sealed surface theorem and leaves J10-J15 open on actual domains |
| W4 covariance orbit and skeleton | **PASS** | V002 retains the full ratified family, types residual moduli honestly, and replaces the impossible master skeleton by stagewise objects |
| W5 too-easy/smuggling/rail audit | **KILL_WITH_ROOT_AUDIT_PASS** | the three roots remain genuinely physical, but the `Ext_cycle` square is still presented as geometry although it is a tautological rail construction |
| W6 C1 handoff | **N-A** | the failed `Ext_cycle` exhibit cannot populate the full P4 core; C1 remains at its existing finite/Ref_path subpackage |
| W7 two fresh attacks | **KILL** | unrelated-path surfaces and Riesz-induced nonlocality satisfy every displayed rail equation while failing actual refinement/locality |

---

## 2. W1 - repaired square, geometry first

### 2.1 Algebraic identity behind the repair

For each actual finite surface set

```text
Phi_G:=R_G^(-1) Abar_G:Tbar_G -> K_G.             (W1-1)
```

V002 defines, for an injective signed cycle map `S_R`,

```text
I_R^T:=Abar_G'^(-1) R_G' S_R R_G^(-1) Abar_G.    (W1-2)
```

Therefore, by construction,

```text
Phi_G' I_R^T=S_R Phi_G.                          (W1-3)
```

For every fine bilinear profile `H'`, `(W1-3)` gives

```text
Kern_G'(H')[I_R^T a,I_R^T b]
 =H'(S_R Phi_G a,S_R Phi_G b)
 =Kern_G(S_R^* H' S_R)[a,b].                    (W1-4)
```

This proof is correct.  It is also purely a duality/Riesz construction: once
`S_R` is supplied, `(W1-2)` is the unique map that makes `(W1-3)` true.  The
identity contains no path support, cell neighborhood, density, coframe,
connection, or curvature statement.

### 2.2 V001 killing counterexample rerun

Use

```text
K_G=R,
K_G'=R^2,
S_R x=(x,0),
Abar_G=Abar_G'=id,
R_G=R_G'=id,
H_new=diag(0,1).                                 (W1-5)
```

Then `I_R^T(t)=(t,0)`, so

```text
S_R^* H_new S_R=0,
Kern_G'(H_new)[I_R^T t,I_R^T t]=0,               (W1-6)
```

while the actual new test `eta=(0,1)` satisfies

```text
Kern_G'(H_new)[eta,eta]=1.                       (W1-7)
```

V002 passes the old kill exactly.  It compares only the old image and does
not delete `(W1-7)`.

```text
OLD_KILL_REPAIRED_ALGEBRAICALLY = true
NEW_CYCLE_KERNEL_PRESERVED = true
```

### 2.3 Multi-cycle creation

Let

```text
K_G=R^m,
K_G'=S_R K_G direct-sum N,
dim N=n>=2.                                      (W1-8)
```

Write a fine profile in blocks

```text
H'=[[H_oo,H_on],[H_no,H_nn]].                    (W1-9)
```

The pullback `(W1-4)` sees exactly `H_oo`.  Fine tests outside
`image(I_R^T)` retain `H_on,H_no,H_nn`.  Hence multiple new cycles and their
mixed blocks are not deleted.  The algebraic repair passes.

### 2.4 Rank-two exchange

Let `U_G,U_G'` exchange two old cycle labels and suppose

```text
U_G' S_R=S_(fR) U_G,
Abar_(fG) V_G=U_G^(-*)Abar_G,
R_(fG)U_G=U_G^(-*)R_G.                           (W1-10)
```

Direct substitution into `(W1-2)` gives

```text
V_G' I_R^T=I_(fR)^T V_G.                        (W1-11)
```

Thus the full rank-two family transforms and no coordinate is selected.
This regression passes on the rails and on every already-anchored surface
isomorphism.

### 2.5 Pendant interactions

A true pendant edge carries no conserved coefficient in
`K_G=ker(B_G^T)`.  Therefore it contributes no scalar cycle direction to
`Phi_G` or `(W1-2)`.  If a later target edge closes a new loop, that loop is a
new direction in `K_G'` and is retained outside the old image exactly as in
`(W1-7)`.  No pendant class is promoted and no new loop is erased.

The pendant regression passes algebraically.

### 2.6 Geometry attack: unrelated actual paths

Now use actual finite Q-408 surfaces rather than only cycle coordinates.
Let `G` contain an old loop whose current `J_G(c)` is supported in physical
region `U`.  Let `G'` contain two loops in a disjoint region `V`, and let the
injective signed rail map send the old cycle to the first target cycle:

```text
S_R c=c_1',
supp J_G(c) subset U,
supp J_G'(c_1') subset V,
U intersect V=empty.                             (W1-12)
```

The signed incidence relation, injectivity, finite Riesz maps, `Abar`
isomorphisms, and every equation `(W1-2)`--`(W1-4)` still hold.  But there is
no physical refinement relation

```text
J_G(c)=physical_pullback_or_pushforward_of J_G'(S_R c), (W1-13)
```

because the current supports are disjoint.  `I_R^T` merely manufactures a
dual test-class injection for the rail map.  It does not move an old local
test form through an actual cell/path refinement.

This counterexample uses actual Q-408 kernels at both ends.  It proves that
the repaired square is insufficient to certify surface geometry.

```text
EXT_CYCLE_RAIL_SQUARE = PASS
EXT_CYCLE_ACTUAL_SURFACE_REFINEMENT = not_proved / TYPE-U
GENERATORS_RATIFIED_SURFACE_SCOPE_EXHIBITED = false | TYPE-R
W1 = KILL
```

---

## 3. W2 - stagewise anchor audit

### 3.1 Object anchors

The finite object

```text
S_G=(G,B_G,K_G,Q_G,Tbar_G,Abar_G,R_G,Kern_G)      (W2-1)
```

is correctly anchored:

| Entry | Surface authority | Result |
|---|---|---|
| `G,B_G,K_G,Q_G` | DoR-015/V005 incidence, cycles, Gate-4 quotient | **PASS** |
| `u_c,T_G,A_G,Kern_G` | actual Q-408 paths, currents, tests, kernels | **PASS** |
| `Tbar_G,Abar_G` | quotient of actual tests by `ker A_G` | **PASS** |
| `R_G` | DoR-019 finite carrier metric | **PASS** |

Identity, reality/relabeling, finite restriction, zero-extension, and
rank-preserving `Ref_path` use these actual objects and their already-proved
maps.  Their anchors pass.

### 3.2 `Ext_cycle` anchor is a rail

V002's `Ext_cycle` row cites:

```text
V003 contravariant cellular restriction
+ target finite V005/Q408 surface.               (W2-2)
```

The target is actual surface data.  The signed cellular map relating source
to target is the rail.  Neither citation proves that old paths refine into
target paths, that old current support is transported to the target, or that
coframe/density/connection/curvature transports relate the two stages.

Formula `(W1-2)` cannot supply that missing anchor because it is defined from
the rail map itself.  The witness `(W1-12)` satisfies `(W2-2)` while failing
physical refinement.

The common-refinement row has the same issue: two signed chain legs and an
actual target do not prove that either leg is a physical geometric
refinement.  Requiring an actual target is necessary, not sufficient.

```text
STAGEWISE_OBJECT_ANCHORS = PASS
Ref_path_ANCHOR = PASS
Ext_cycle_RELATION_ANCHOR = FAIL / cites_rail
COMMON_REFINEMENT_RELATION_ANCHOR = FAIL / cites_rails
W2 = KILL
```

### 3.3 Coframe/density/connection/curvature

DoR-015 supplies the external-background and realization families at each
actual stage.  Q-408 supplies connection tests and the finite Ward action.
Those are valid objectwise surface anchors.

What remains absent is their transport along an `Ext_cycle` relation.  V002
correctly lists that datum in `Mod_R^phys` and types its full nonemptiness
`TYPE-U`.  Therefore these fields support the full-root stop; they do not
repair the claimed built `Ext_cycle` surface arrow.

---

## 4. W3 - the removed rail clauses

### 4.1 Monolithic all-arrow identity restriction

V001 imposed `P_R=id` and literal all-fine-test restriction on cycle-creating
arrows.  Q-408 proves identity test transport only on the rank-preserving
actual-path scope.  The pure-new-profile witness refutes the wider clause.
No physical consumer needs an old surface to evaluate every new-cycle test.

```text
REMOVAL_1 = LAWFUL
```

### 4.2 Formal overlay called a physical common refinement

A formal PL overlay without an actual target surface has no physical paths,
kernel, density, connection, or response.  Removing its automatic physical
status deletes no geometric datum.  J10-J13 remain obligations on actual
surface arrows and actual diamonds.

```text
REMOVAL_2 = LAWFUL
```

### 4.3 Representative orbit called a natural family

One covariance orbit does not represent inequivalent density/Gram/connection
moduli.  Replacing it with the full ratified family and a separately typed
`Mod_R^phys` removes a false identification, not physical content.

```text
REMOVAL_3 = LAWFUL
```

### 4.4 Constraint-family audit after slimming

| Family | Slimmed lawful obligation | Result |
|---|---|---|
| J10 | functoriality on actual geometric refinements | retained; full member open |
| J11 | density/coframe naturality on actual refinements | retained; full member open |
| J12 | response naturality on actual common refinements | retained; C2 open |
| J13 | cocycle/contact coherence on actual response arrows | retained; C2 open |
| J14 | one completion topology, estimates, faithfulness horn | unchanged |
| J15 | DoR-008 squares on every built actual arrow | unchanged |

The removed clauses were either refuted V001 additions or requirements on
unphysical formal words.  No sealed theorem depends on them.  The joint
equalizer remains open rather than being weakened into a pass.

```text
W3 = PASS
```

This review does not itself amend DoR-020; it verifies the physical scoping
that any registrar disposition must record.

---

## 5. W4 - covariance-family and skeleton repairs

### 5.1 Covariance/moduli repair

V002 deletes `Q_o=[q]_Cov`, retains the full ratified surface family
`Surf_adm`, and types the genuinely new interior-cell carrier as the full
groupoid `Mod_R^phys`.  Conformal/density moduli are not identified and no
representative is selected.  Nonemptiness remains explicitly `TYPE-U`.

```text
COVARIANCE_ORBIT_REPAIR = PASS
```

### 5.2 Skeleton repair

V002 uses one finite object `S_G` per stage and a declared map per arrow.
Coarse and refined edge interiors may overlap across stages.  No infinite
embedded master graph or global disjoint-tube claim remains.

```text
ALL_STAGE_SKELETON_REPAIR = PASS
```

These repairs remove both independent U1/U6 failures from V001.  They do not
turn an unanchored signed map into actual surface geometry; that is the W2
finding, not a recurrence of the old skeleton defect.

```text
W4 = PASS
```

---

## 6. W5 - too-easy, smuggling, and rail-artifact audit

### 6.1 The too-easy question

V002 no longer claims the full root inhabited.  It stops at
`NONEMPTY Mod_R^phys` for every new interior-cell primitive.  That stop is
honest and avoids V001's schema-passed-as-instance failure.

The portion advertised as built remains too easy for a precise reason:
`I_R^T` is defined after `S_R` by solving the desired commutation equation.
It proves that the category of finite Hilbert cycle carriers has a canonical
contravariant pullback.  It does not prove that a signed cellular rail map is
realized by local record-surface geometry.

```text
FULL_ROOT_NONEMPTY_ASSERTED = false
RAIL_PULLBACK_THEOREM = genuine
RAIL_PULLBACK_IS_SURFACE_REFINEMENT = false | TYPE-R
```

### 6.2 Smuggling audit

No response value, threshold, fixed point, end test, or measured datum enters
the construction.  There is no outcome tuning.  The smuggled item is a type:
`actual signed surface arrow` is assigned to a signed rail map between two
actual objects without an actual path/current/local-support relation.

```text
TARGET_TUNING = false
TYPE_SMUGGLING = rail_map_labeled_surface_relation
```

### 6.3 Re-examination of the three new-physics roots

The no-false-root result survives independent review.

1. **`B_Q408_REFINEMENT`.**  The witness `(W1-12)` has the same rail map and
   commuting pullback for physically unrelated path supports.  The missing
   support/local-geometry relation is therefore real surface content, not a
   rail requirement.
2. **`B_R1_NATURAL`.**  Q-396 supplies equal finite shadows with distinct
   completed operator blocks.  Formal strict sections can be removed, but
   the representative-sensitive physical datum cannot.
3. **`B_C2_RESPONSE_BOUNDARY`.**  The finite Ward rail does not determine the
   physical bulk/contact/boundary split, density scaling, or subextensive
   boundary behavior.  Formal-word cocycles can be removed while the actual
   response datum remains.

```text
RAIL_ARTIFACT_ROOTS = none / PASS
RAIL_ARTIFACT_CLAUSES_REMOVED = 3 / PASS
ROOT_COUNT_CHANGE = 0
W5 = KILL_OF_EXHIBIT_GEOMETRY_CLAIM_WITH_ROOT_AUDIT_PASS
```

---

## 7. W6 - C1 handoff

Because the exhibit does not supply an actual cycle-creating P4 core, C1
cannot resume beyond its Q-425 stopping point.

The surviving geometry handed to C1 is unchanged:

```text
actual finite Q408 core
+ rank-preserving Ref_path local-seminorm orbit
+ fixed-stage and orbitwise attained bounds.     (W6-1)
```

A repaired full B_Q408 term would have to add:

```text
actual path/current/support-preserving Ext_cycle transports;
coframe/density/connection/curvature transports;
actual common-refinement targets and legs.        (W6-2)
```

Only then could C1 form the full physical seminorm orbit, test cross-orbit
bounded geometry and attained bounds, and seek a covariant Hilbertizing
`W5`.  None of those C1-local certificates is derived by V002.

```text
C1_RESUMPTION = N-A
HYPOTHETICAL_REPAIRED_ROUTE = (W6-2) -> P_phys -> BG -> attained_X5 -> W5
FULL_B_Q408_STILL_NEEDS = actual_surface_relation_data_in_(W6-2)
W6 = N-A
```

---

## 8. W7 - two fresh attacks

### 8.1 Fresh attack A: unrelated-path surfaces

The construction `(W1-12)` is a direct geometry falsifier.  Both endpoints
are actual Q-408 surfaces, the signed cycle map is injective, and V002's
kernel pullback commutes.  The old and target currents nevertheless have
disjoint support and no refinement relation.  Thus all rails pass while the
surface claim fails.

```text
FRESH_ATTACK_A = KILL
```

### 8.2 Fresh attack B: Riesz-induced nonlocal test transport

Let one old cycle live in region `U` and a new target cycle live in a
disjoint region `V`.  In cycle coordinates take

```text
S_R x=(x,0),
R_G=1,
R_G'=[[1,epsilon],[epsilon,1]],
0<|epsilon|<1,
Abar_G=Abar_G'=id.                               (W7-1)
```

Then V002 gives

```text
I_R^T(1)=R_G' S_R(1)=(1,epsilon).                (W7-2)
```

The injected "old" test class has nonzero line-integral coordinate on the
disjoint new cycle.  Equation `(W1-4)` still holds because `R_G'^(-1)`
cancels the metric dressing.  Covariance and positivity do not force
`epsilon=0` under V002's premises.

A true local refinement transport for a test form supported in `U` would
need a support theorem making its pairing with the disjoint cycle in `V`
zero.  No such theorem is supplied.  This attack shows explicitly how the
rail pullback can be nonlocal while every displayed algebraic certificate
passes.

```text
FRESH_ATTACK_B = KILL
W7 = KILL
```

---

## 9. Falsifiers, accounts, and final disposition

### 9.1 Regression board

| Check | Geometry result | Rail result |
|---|---|---|
| V001 pure-new profile | new kernel retained: **PASS** | pullback commutes: **PASS** |
| multi-cycle creation | new/mixed blocks retained: **PASS** | old block pullback: **PASS** |
| rank-two exchange | actual isomorphism covariance: **PASS** | formula natural: **PASS** |
| pendant/tree | no scalar pendant class: **PASS** | zero old carrier maps correctly: **PASS** |
| abstract kernel | actual endpoint kernels used: **PASS** | no substitute kernel |
| circular reader | no reader used | **PASS** |
| false nonemptiness | full moduli remains TYPE-U | **PASS** |
| Hodge from isometry | none claimed | **PASS** |
| objectwise minimum | none selected | **PASS** |
| joint equalizer | remains open | **PASS** |
| unrelated-path attack | **FAIL** | **PASS** |
| Riesz-nonlocality attack | **FAIL / locality unproved** | **PASS** |

### 9.2 Six-account rows

| Account | Surface geometry | Rails |
|---|---|---|
| measure | stagewise density exists; Ext_cycle transport open | density naturality equation typed |
| contour | stagewise CTP/reality present | componentwise covariance |
| boundary/contact | physical C2 datum open | formal-word cocycle removed |
| domain closure | no new completion | finite Hilbert duality only |
| stationary Schur | untouched | untouched |
| class formation | full family/moduli correctly retained | no weak-star/bidual step |

### 9.3 Anti-tuning and fence status

The review uses only actual path support, signed incidence, finite cycle
linear algebra, Riesz maps, and the ratified restriction scopes.  It performs
no response evaluation, member binding, fixed-point execution, end test, or
comparison to measured data.

```text
TARGET_TUNING_USED = false
MACHINERY_APPEAL = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```

### 9.4 Final lines

```text
EXHIBIT_V002 = KILLED(
  W1 + W2 + W5 + W7;
  anatomy = metric_dual_pullback_proves_rails_not_actual_surface_refinement
)

GEOMETRY_VS_RAILS =
  actual finite objects + Ref_path geometry survive;
  Ext_cycle injection/composition/diamonds survive only as rail theorems;
  physical path/current/support and geometry transports remain TYPE-U.

C1_RESUMPTION = N-A

LAWFUL_REMOVALS = 3 / W3_PASS
COVARIANCE_AND_SKELETON_REPAIRS = W4_PASS
RAIL_ARTIFACT_ROOTS = none
B_Q408_REFINEMENT_FULL_ROOT = OPEN / TYPE-U
JOINT_EQ6 = OPEN

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_executed = false
numeric_evaluation = false
measured_constant_compared = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```
