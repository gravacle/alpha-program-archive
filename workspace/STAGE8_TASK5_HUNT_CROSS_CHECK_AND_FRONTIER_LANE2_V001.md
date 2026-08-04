# STAGE 8 TASK 5 — WITNESS-HUNT CROSS-CHECK AND FRONTIER — LANE 2 V001

Date: 2026-08-04  
Task: PASTE 501 / Task 5  
Lane: Codex Lane 2  
Custody: adversarial cross-check and frontier consolidation  
Standing: DoR-020 in force; `[EQ6]` open

## Lead result

```text
HUNT_PASS_1 = CONFIRMED

R1 = PASS_WITH_SCOPE_PRECISION |
  orbitwise bounds, finite/Ref_path faithfulness, zero kernel-discrepancy
  cocycles, and finite Ward transport are genuine exact subpackages.

R2 = PASS |
  all six full fibers stop exactly after their maximal finite/Ref_path
  positive content; no derivable full-scope object is left before a stop.

R3 = PASS_WITH_PROJECTION_PRECISION |
  the common finite/Ref_path diagram commutes on the claimed projections.
  J10 and J11 are not complete rows there: only the path/current/kernel and
  line-integral projections are built; coframe/density/connection/curvature
  remain absent exactly as the hunt states elsewhere.

FRONTIER = 6 gaps: 3 constructible / 3 new-physics / 0 reducible

  NEW_PHYSICS:
    B_Q408_REFINEMENT,
    B_R1_NATURAL,
    B_C2_RESPONSE_BOUNDARY.

  CONSTRUCTIBLE_WITH_ROUTE:
    B_C1_COMPLETION,
    B_FAITHFULNESS,
    B_C3_MAXWELL_HODGE.

  REDUCIBLE_ROOTS: none.

PHYSICAL_READER = REDUCIBLE_DOWNSTREAM_CONSEQUENCE |
  conditional on B_C1_COMPLETION + B_FAITHFULNESS
  + B_C3_MAXWELL_HODGE; not a seventh root.

DOR020_AMENDMENT_TRIGGER = no |
  three roots are not DERIVABLE from the other adopted clauses, but no root
  is proved empty or type-incompatible.  DoR-020 expressly adopted their
  joint nonemptiness as [EQ6]; genuine member data may inhabit those clauses
  without revising them.  Clause amendment becomes live only on an emptiness
  or incompatibility theorem.
```

No member is bound.  No fixed point or end test is executed.  The pass is a
scope-confirmed first-pass result, not a promotion of the partial subpackages
to a joint witness.

```text
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

---

## 0. Preflight and authorities

### 0.1 Three-line preflight

The locked process was read in full.  The register head is Q-423.  The hunt,
its sidecar, package V005, the bedrock theorem, the constraint system, and
DoR-020 were hash-verified before substantive review.

```text
DOES_THE_OBJECT_EXIST = yes | the first-pass hunt exists
IS_THE_VERSION_CURRENT = yes | through register head Q-423
ARE_ITS_INPUTS_PRESENT = yes | hunt, bedrock, V005, J1--J15, DoR-020
PREFLIGHT = PASS
```

| Authority | Verified SHA-256 | Use |
|---|---|---|
| locked process | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | custody and fences |
| register at Q-423 | `4d22b13440f569ce7da169f68607ad7083b3f2418c433c842c23cb53cb09ce5f` | current scope |
| witness hunt | `452f1bb87aeb7f7bfe4ab4556134cf723ab6df697f93c1a59c33671146cb0083` | artifact under review |
| bedrock theorem | `288a3d4147cb10f2e51180b21f7c6b2b4749503504c57b8a1121e3925c70c94c` | six-root minimality and independence |
| package V005 | `09883a0d7a5d1329033a09c59ff8d7c843a0098cba569d2a2b97f64f45b2dd95` | adopted clause/rule source |
| constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | exact J1--J15 equalizer |
| DoR-020 | `bead32b7a12dd70b48a5ddd729395f23914dce06047783226a33d3ccb1eafa31` | conditional adoption and prohibitions |
| Q-408 physical kernel | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | finite current, kernel, Ward, faithfulness |
| hostile witness check | `510ebda9c05220b3eb229e865a0a41868f5ce166ff2a5805762d540309a6ab1b` | permanent regressions |

### 0.2 Register sweep

```text
Q-408  finite physical kernel, Ward calculus, and faithfulness built;
Q-410  full geometric refinement, uniform estimates, and symbol absent;
Q-411  J1--J15 equalizer defined, inhabitance open;
Q-415  abstract kernel and circular reader witness killed;
Q-421  six roots minimal; componentwise nonemptiness not joint inhabitance;
Q-422  DoR-020 conditional on joint [EQ6]; binding/execution forbidden;
Q-423  first-pass partial subpackages and six full stops reported.
```

### 0.3 Review standard

```text
finite stage != completed family;
one Ref_path orbit != all primitive refinement orbits;
transported seminorm != full Hausdorff physical topology;
zero discrepancy != a global boundary theorem;
finite Ward kernel != local Maxwell/Hodge package;
six partial subpackages != one [EQ6] term.
```

---

## 1. Verdict table R1--R5

| Item | Verdict | Reason |
|---|---|---|
| R1 four positive subpackages | **PASS_WITH_SCOPE_PRECISION** | each follows by exact finite calculation or transport along a constant isomorphism orbit; none is promoted to completion |
| R2 six stopping fibers | **PASS** | each stop is backed by a type separation or countermodel; no lawful full-scope construction remains before it |
| R3 common-scope equalizer audit | **PASS_WITH_PROJECTION_PRECISION** | all claimed finite/path-current projections commute; no complete J10/J11/P2 row is inferred |
| R4 frontier map | **PASS / UPDATED** | six roots split into three member-data inputs and three analytic construction routes; none reduces entirely to another |
| R5 falsifiers and fresh attack | **PASS** | permanent regressions pass; cross-orbit batching refutes any hidden promotion of orbitwise bounds to C1 |

---

## 2. R1 — recomputation of the four positive subpackages

### 2.1 Orbitwise upper bounds

At a finite carrier `G`, Q-408 gives a linear map from a finite-dimensional
profile normed space to the physical bilocal distribution space.  For each
finite target seminorm `p_Q`, compactness of the profile unit sphere gives

```text
p_Q(Kern_G^fin H)<=C_(G,Q)||H||_prof,             (R1-1)
```

with finite attained `C_(G,Q)`.

For a pure rank-preserving path subdivision, the physical maps obey

```text
A_n=S_nm^* A_m,
S_nm^*R_(K,m)S_nm=R_(K,n),
Kern_m^fin(j_nm^H H)=Pull_nm Kern_n^fin(H).        (R1-2)
```

`S_nm` and `j_nm^H` are isomorphisms of the complete conserved/profile
carriers in this scope.  Pulling the same physical target seminorm along the
exact restriction gives

```text
p_(Q,m)(Kern_m^fin(j_nm^H H))
 =p_(Q,n)(Kern_n^fin H)
 <=C_(G,Q)||j_nm^H H||_prof.                      (R1-3)
```

Nested subdivisions compose, so `C_(G,Q)` does not grow along this one
orbit.  This is genuine orbitwise uniformity.  The pulled seminorm may be
degenerate off the transported image and is not called a separating full
P5 topology.  Constants may vary between nonisomorphic/cycle-creating
orbits.

```text
ORBITWISE_BOUNDS = CONFIRMED
FULL_FAMILY_UNIFORM_BOUND = not_claimed
```

### 2.2 Finite and Ref_path-orbit faithfulness

Q-408 proves finite injectivity:

```text
Kern_G^fin(H)=0 -> H=0.                            (R1-4)
```

Using the kernel square and invertibility of `j_nm^H`,

```text
Kern_m^fin(j_nm^H H)=0
 -> Kern_n^fin(H)=0
 -> H=0
 -> j_nm^H H=0.                                   (R1-5)
```

The direct system on one pure-subdivision orbit is isomorphic to a constant
finite-dimensional represented object; completing in the transported
isometric profile norm adds no tail direction.  The result is faithful on
that orbit.  It says nothing about a completion joining different ranks or
orbits.

```text
FINITE_FAITHFULNESS = CONFIRMED
REF_PATH_ORBIT_FAITHFULNESS = CONFIRMED
COMPLETED_FULL_FAITHFULNESS = not_claimed
```

### 2.3 Zero kernel-discrepancy cocycle

On `Ref_path`, define the actual discrepancy—not an authored response—by

```text
beta_nm(H)
 :=Kern_m^fin(j_nm^H H)-Pull_nm Kern_n^fin(H).     (R1-6)
```

Equation `(R1-2)` gives `beta_nm=0`.  For composable subdivisions,

```text
beta_nl=0=beta_ml+eta_ml(beta_nm).                 (R1-7)
```

The generated contact ideal is `{0}`, so no visible cycle is deleted.  This
is neither circular nor a blanket declaration about future new-edge
discrepancies.  The expression `beta/Vol` remains undefined until a positive
P4 volume exists; the hunt correctly leaves subextensivity conditional.

```text
REF_PATH_KERNEL_TRANSPORT = CONFIRMED
REF_PATH_ZERO_COCYCLE = CONFIRMED
REF_PATH_SUBEXTENSIVITY = conditional_on_P4_density
```

### 2.4 Finite Ward transport

The actual Q-408 kernel satisfies, at every finite stage,

```text
Kern_G^fin(H)(d alpha,v)=0,
Kern_G^fin(H)(u,d beta)=0.                         (R1-8)
```

`P_nm=id` on the same test-form space, and the kernel square transports
`(R1-8)` unchanged along `Ref_path`.  No Maxwell coefficient, closed range,
Hodge projection, or reader is extracted.

```text
FINITE_WARD = CONFIRMED
REF_PATH_WARD_TRANSPORT = CONFIRMED
COMPLETED_MAXWELL_HODGE = not_claimed
```

### 2.5 Stand-in and circularity scan

Every positive map above is the actual Q-408 path-current/bilocal map.  The
only transports are `S_nm`, the identity test-form map, and their proved
profile/kernel intertwiners.  No `UHU*` carrier replaces a physical kernel;
no reader defines a path, topology, contact ideal, or Maxwell projection;
and no physical-reader nonemptiness is asserted.

```text
R1 = PASS_WITH_SCOPE_PRECISION
```

---

## 3. R2 — exactness of the six stopping fibers

### 3.1 `B_Q408_REFINEMENT`

The hunt derives everything current/kernel-valued available on `Ref_path`.
The existing line-integral parameter does not determine a positive cell
coframe, volume density, connection, or curvature transport.  For a new
interior PL edge, there is no actual path or test-form map at all.

The remaining candidates fail: a formal edge or bounded operator is an
abstract stand-in; zero may delete a new visible cycle; boundary
concatenation selects a route; reader/response construction is circular;
and a smooth geodesic imports undeclared target geometry.

```text
STOP_Q408 = exact
REMAINDER_Q408 = Ref_path_geometry + actual_new_edge_generator
```

### 3.2 `B_R1_NATURAL`

`Adm_base` is a genuine nonempty covariant family on its ratified stage
arrows.  Neither the physical kernel square nor the P4 type supplies an
action/Hessian restriction cube on `Ref_path` or new refinements.  Q-396's
flat directions also refute finite-shadow selection of one extension.

```text
STOP_R1 = exact
REMAINDER_R1 = natural_action_and_Hessian_extension_on_full_Ref
```

### 3.3 `B_C1_COMPLETION`

Finite and constant-orbit boundedness are exhausted by `(R1-3)`.  A global
P5 term still needs one separating physical topology, cross-orbit uniform
constants, and a covariant Hilbertizable `W5`.  The bedrock model with
stage-`n` identity maps and target norm `max_k k|y_k|` has exact compatible
finite maps but unbounded family constants.  Therefore P4 does not close
C1.

```text
STOP_C1 = exact
REMAINDER_C1 = physical_topology + family_uniform_estimates + W5
```

### 3.4 `B_FAITHFULNESS`

`(R1-5)` exhausts finite/orbitwise injectivity.  The quotient
`ell^2 -> ell^2/span{v}` with infinite-support `v` is injective on the finite
core and continuous on completion but has nonzero completed kernel.  Hence
the next lawful object is exactly a lower separation theorem or the safe
quotient horn with finite-visible intersection and annihilator proofs.

```text
STOP_FAITHFULNESS = exact
REMAINDER_FAITHFULNESS = completed_lower_bound_or_safe_quotient
```

### 3.5 `B_C2_RESPONSE_BOUNDARY`

The exact path square proves the zero cocycle and nothing beyond it.  A new
common-refinement diamond can carry path discrepancies `0` and `b!=0`, so
P4 and C1 do not imply a response-natural solution.  The hunt therefore
stops exactly at an actual response transport, compatible primitive
cocycle, safe contact ideal, and subextensive boundary theorem.

```text
STOP_C2 = exact
REMAINDER_C2 = response_solution + actual_cocycle + safe_ideal + subextensivity
```

### 3.6 `B_C3_MAXWELL_HODGE`

Finite Ward annihilation is the last forced positive result.  The operator
`d e_n=(1/n)e_n` on `ell^2` has dense nonclosed range, showing that bounded
Ward data and prior continuum terms do not force closed-range Hodge theory.
No principal symbol, harmonic/contact quotient, Maxwell summand, magnetic
partner, or nonzero `L_T` normalization remains derivable before the named
P8 package.

```text
STOP_C3 = exact
REMAINDER_C3 = local_symbol + closed_range_Hodge_Maxwell + L_T_normalization
```

### 3.7 Exactness verdict

The countermodels prove nonimplications, not emptiness.  Each stop is the
maximal result on current authorities, and no stop is caused by a process
fence.

```text
R2 = PASS
```

---

## 4. R3 — joint finite/Ref_path equalizer audit

### 4.1 Common-scope table

| J-family | Verified common-scope content | Status |
|---|---|---|
| J1 | algebraic relation-annihilating normalized-reader family retained | **family-level only** |
| J2 | no physical pullback; no equality asserted | **open** |
| J3 | algebraic reader family stable under covariance, reality, and restriction | **verified as family** |
| J4 | `Adm_base` family obeys ratified stage cubes | **verified on old arrows only** |
| J5 | `h=0` anchors every retained P1 member | **verified as rule** |
| J6 | zero added action preserves Shape-K | **verified as rule** |
| J7 | algebraic formula retained; no P1/P2 member pair | **uninstantiated** |
| J8 | every displayed C/K crossing uses R4 | **verified** |
| J9 | batching remains ordered/componentwise | **verified** |
| J10 | nested `Ref_path` path/current/kernel projection is functorial | **verified projection only** |
| J11 | line-integral/current normalization commutes | **verified projection only; coframe/density absent** |
| J12 | actual finite/Ref_path kernel square commutes | **verified projection only** |
| J13 | `beta=0` is a cocycle and `{0}` deletes no visible cycle | **verified; volume theorem open** |
| J14 | finite/orbit upper bound and faithfulness | **verified projection only; completion horn open** |
| J15 | all claimed finite and Ref_path bottom squares are exact | **verified on built subdiagram** |

This precision repairs the only risky wording in the hunt: “J10/J11 hold on
`Ref_path`” means their path/current/kernel projections, not the complete
geometric rows.  The hunt's detailed fiber sections already state that
scope, so no substantive subpackage is killed.

### 4.2 Joint regression

The hunt correctly retains

```text
X={0}, Y={1}, compatibility x=y,                  (R3-1)
```

as the model showing that separately nonempty fibers can have an empty
equalizer.  Concretely, J2, the P1/P4 action square, the one-topology
J12--J14 system, and the joint J15 restriction remain cross-fiber equations.
No partial result is promoted to `[EQ6]`.

```text
JOINT_EQ6 = PARTIAL
FULL_EQ6_TERM = absent
R3 = PASS_WITH_PROJECTION_PRECISION
```

---

## 5. R4 — updated frontier map

### 5.1 Classification rule

```text
CONSTRUCTIBLE_WITH_ROUTE =
  after named upstream carriers exist, a target-blind mathematical
  construction/certificate can close the fiber without selecting a new
  physical member by its consequence; the construction may still fail.

GENUINELY_NEW_PHYSICS =
  current clauses type the datum but neither determine nor exhibit it;
  a witness must supply a physical member/transport not derivable from
  other roots.

REDUCIBLE_TO_ANOTHER =
  a proved theorem makes the entire root follow from other roots, so it is
  not independent in [EQ6].
```

The bedrock theorem proves that none of the six roots is wholly reducible.
It does not prove the new-physics fibers empty.

### 5.2 Six-root frontier

| Order | Fiber | Built base | Remaining need | Type | Next-pass route |
|---:|---|---|---|---|---|
| 1A | `B_Q408_REFINEMENT` | actual finite/Ref_path current and kernel projection | coframe/density/connection/curvature on Ref_path; actual path/test-form/current/coframe/density generators on new edges | **GENUINELY_NEW_PHYSICS** | exhibit one target-blind actual-Q408 primitive generator per orbit, then prove free-category composition and common refinement |
| 1B | `B_R1_NATURAL` | `Adm_base` on ratified stage arrows | action representative/Hessian/reducing-domain naturality on Ref_path and new arrows | **GENUINELY_NEW_PHYSICS** | construct a covariant retained-family restriction rule or section on the enlarged refinement category; do not select by finite shadows |
| 2 | `B_C1_COMPLETION` | finite and orbitwise upper bounds | separating physical topology, cross-orbit uniform constants, attained bounds, `W5` | **CONSTRUCTIBLE_WITH_ROUTE** | from the actual P4 core build its local seminorm orbit, prove bounded-geometry estimates, then construct/verify covariant Hilbertization |
| 3 | `B_FAITHFULNESS` | finite and orbitwise injectivity | completed lower separation or safe quotient with finite-visible and annihilator proofs | **CONSTRUCTIBLE_WITH_ROUTE** | compute `ker(Kernbar)` after C1; prove a lower bound, else take the canonical kernel quotient and discharge safety/annihilator conditions |
| 4 | `B_C2_RESPONSE_BOUNDARY` | exact Ref_path kernel transport and zero cocycle | response maps on new/common refinements, compatible primitive cocycle, safe ideal, subextensive boundary theorem | **GENUINELY_NEW_PHYSICS** | after 1A/1B/2, exhibit action-derived physical response transports; test every refinement diamond before forming the closed ideal |
| 5 | `B_C3_MAXWELL_HODGE` | finite Ward annihilation and transport | completed local symbol, closed ranges/domains, Hodge/Maxwell projections, magnetic partner, nonzero normalization | **CONSTRUCTIBLE_WITH_ROUTE** | close `d` on the C1 carrier, prove spectral-gap/closed-range estimates, run functional calculus, derive symbol from P4 coframes, then test normalization/refinement cubes |

### 5.3 Dependency order for the next pass

```text
PASS_2A, in parallel:
  B_Q408_REFINEMENT physical generator;
  B_R1_NATURAL action/Hessian extension on the maximal common category.

PASS_2B:
  B_C1_COMPLETION on the actual directed core.

PASS_2C, after C1:
  B_FAITHFULNESS lower-bound horn;
  if it fails, prepare the safe quotient horn and defer reader annihilation
  until C3 supplies the physical projection.

PASS_2D, after Q408 + R1 + C1:
  B_C2_RESPONSE_BOUNDARY; run diamond/cocycle checks before completion.

PASS_2E, after Q408 + C1 + C2 and with the faithfulness horn disclosed:
  B_C3_MAXWELL_HODGE.

PASS_2F, derived consequence:
  ell_phys=pi_Mx Loc Kernbar Q from C1 + faithfulness + C3.

PASS_2G, final joint step:
  instantiate and verify J1--J15 on one tuple; component passes are not
  inherited as joint credit.
```

### 5.4 Reducible consequences, not roots

| Object | Reduction | Status |
|---|---|---|
| physical P2 reader | C1 + faithfulness + C3 via `pi_Mx Loc Kernbar Q` | **reducible downstream** |
| zero Ref_path cocycle | exact Q-408 square | already built |
| orbitwise bounds | finite bound + Ref_path isometry | already built |
| orbitwise faithfulness | finite faithfulness + Ref_path isomorphism | already built |
| J1--J15 certificate | requires the six terms jointly; it is a final proof, not a seventh root | constructible final audit |

### 5.5 DoR-020 amendment test

The independence countermodels prove only

```text
other adopted roots do_not_force
  B_Q408_REFINEMENT, B_R1_NATURAL, or B_C2_RESPONSE_BOUNDARY. (R4-1)
```

They do not prove those fibers empty or inconsistent with J1--J15.  These
three therefore require genuine physical witness data, but DoR-020 already
adopted exactly their **joint nonemptiness** as a condition.  Supplying an
inhabitant is not a clause revision.

```text
PROVED_EMPTY_ROOTS = none
PROVED_TYPE_INCOMPATIBLE_ROOTS = none
DOR020_AMENDMENT_QUESTION = not_triggered
```

If the next pass proves one root empty under the adopted clauses, or proves
that every member violates a J-row, then `[EQ6]` cannot be inhabited and a
DoR-020 amendment/rejection question must go to the principal.  No such
theorem exists now.

```text
R4 = PASS / FRONTIER_UPDATED
```

---

## 6. R5 — falsifiers and fresh attack

### 6.1 Permanent falsifiers

| Falsifier | Re-execution | Verdict |
|---|---|---|
| abstract kernel | every positive map is Q-408 or its exact path subdivision | **PASS** |
| circular `pi_Mx` | physical reader remains absent until C3 | **PASS** |
| false nonemptiness | all six full fibers and `[EQ6]` remain open | **PASS** |
| Hodge from isometry | finite Ward/current isometry is not promoted; nonclosed-range witness retained | **PASS** |
| minimum/restriction | no minimum or member is selected | **PASS** |
| componentwise/joint equalizer | partial subpackages are not combined into a witness | **PASS** |
| finite/completed faithfulness | orbitwise proof and full tail obstruction are separated | **PASS** |
| DoR-008 | every claimed bottom square is an exact equality | **PASS** |

### 6.2 Fresh attack — cross-orbit batching blow-up

Let orbit `r` have an exact isometric subdivision system and kernel operator
bound `C_r=r`.  Every orbit separately satisfies the hunt's invariant bound
with no growth under repeated subdivision.  Form the ordered Hilbert direct
sum over the first `N` orbit types.  The block-diagonal operator norm is

```text
||Kern_(1 direct-sum ... direct-sum N)||=max_(r<=N) C_r=N. (R5-1)
```

Thus exact orbitwise uniformity and componentwise batching do not yield one
family-uniform C1 constant.  No abstract kernel, target tuning, or path
choice is used in the countermodel.

The hunt survives: it explicitly restricts `(Q2-10)` to each orbit and
lists cross-orbit family-uniform estimates as the C1 stop.  The attack is
installed as the next-pass C1 falsifier.

```text
FRESH_ATTACK = CROSS_ORBIT_BATCHING_BLOWUP
HUNT_RESULT = PASS
```

### 6.3 Anti-tuning and prohibitions

The frontier classification was made from type independence and explicit
construction routes before any response coefficient or consequence.  No
member, topology, reader, domain, or branch is selected.  No fixed-point
map or end test is run.

```text
R5 = PASS
```

---

## 7. Final board

```text
R1_ORBITWISE_BOUNDS = PASS_WITH_SCOPE
R1_FAITHFULNESS = PASS_WITH_SCOPE
R1_ZERO_COCYCLE = PASS_WITH_SCOPE
R1_FINITE_WARD = PASS_WITH_SCOPE

R2_SIX_STOPS = PASS_EXACT
R3_JOINT_SUBDIAGRAM = PASS_WITH_PROJECTION_PRECISION
R4_FRONTIER_MAP = COMPLETE_FOR_PASS_2
R5_FALSIFIERS = PASS

HUNT_PASS_1 = CONFIRMED

FRONTIER = 6 gaps: 3 constructible / 3 new-physics / 0 reducible
CONSTRUCTIBLE = B_C1_COMPLETION + B_FAITHFULNESS + B_C3_MAXWELL_HODGE
NEW_PHYSICS = B_Q408_REFINEMENT + B_R1_NATURAL + B_C2_RESPONSE_BOUNDARY
REDUCIBLE_ROOTS = none
PHYSICAL_READER = reducible_downstream_not_root

JOINT_EQ6 = PARTIAL
EQ6_DISCHARGED = false
DOR020_AMENDMENT_QUESTION = not_triggered

MEMBER_BOUND = false
FIXED_POINT_EXECUTED = false
END_TEST_EXECUTED = false
NUMERIC_EVALUATION = false

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
FENCE_BLOCKED_STRUCTURAL_RESULT = false
```
