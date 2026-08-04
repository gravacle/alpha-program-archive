# STAGE 8 TASK 5 — CONTINUUM PACKAGE V004 FINAL CHECK — LANE 1 V001

Date: 2026-08-04  
Task: PASTE 497 / Task 5 / final check before DoR-020  
Lane: Codex Lane 1  
Custody: adversarial final reviewer  
Standing: structural review only; no adoption, evaluation, or registered verdict

## Lead result

```text
PACKAGE = NOT_READY / N2,N4,N5
READY_FOR_DOR020_RULING = no

N1_PATH_SQUARE = PASS
ROUTE_A_BOUNDARY = EXACT

N2_P_CM020_BINDING = KILL |
  P_CM020 is a name plus an asserted certificate, not a defined member.
  DoR-019 supplies norms on the C/K carriers; it supplies no norm on the
  P4 path/coframe/density/refinement data, P5 topology choices, P7 contact
  ideals, or P8 Ward/Hodge/Maxwell packages.  No norm/topology is defined
  on the full natural-family product either.  Consequently the stated
  "carrier-minimal" rule does not type on all eight fields and cannot
  produce c_CM020.

N3_RIGIDITY_NONDERIVATION = PASS
N3_END_TEST_SEMANTICS = PASS_CONDITIONALLY |
  the member-scoped refutation/vindication semantics are correct, but no
  end test is executable until an actual certified member exists.

N4_PACKAGE_COHERENCE = KILL |
  J1--J15 are retained as obligations but are not proved through a member;
  placing their truth inside c_CM020 does not discharge inhabitance.

N5_FRESH_ATTACK = KILL |
  least-norm selection need not commute with restriction.  V004 defines no
  norm on the natural-section space that could repair this failure.
```

The two Q-417 defects are repaired at the level of **specification**: the
derived `Ref_path` square is installed, and the future end test is stated
with correct member scope.  The proposed Route-B member, however, is not
constructed.  Ratifying a symbol whose certificate includes its own
existence, uniqueness, naturality, and all J1--J15 rows would reinstate the
same inhabitance gap under a new name.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
numeric_evaluation = false
registered_verdict_written = false
measured_constant_compared = false
```

---

## 0. Preflight and authorities

### 0.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = yes
IS_THE_VERSION_CURRENT = yes | register head Q-418
ARE_ITS_INPUTS_PRESENT = yes
PREFLIGHT = PASS
```

The locked process was read in full before review.  The artifact and its
sidecar were verified before reading.

| Authority | Verified SHA-256 | Role |
|---|---|---|
| locked process | `e8a4c00d3cd13126bd8d20588419aba344a50d27c6d084a8243ed5494d7721f2` | custody and fences |
| questions-settled register at Q-418 | `a5fafd21a1314c2426c8536fdb3434b54281ac97aec94a7f764dc66bda4d75a2` | current head and commission |
| continuum package V004 | `fa73114214d7653d9a5d181a684b3bd65f0d6e9f91fd2256fb159ca97e56c4bf` | object under review |
| V003 final cross-check | `7465d6f42dcdee027c38cf89e5163e8ada63cfa69f326b794ea03ad7f02066bd` | two defects to repair |
| Q-411 constraint system | `d7dcbc3ad7c470c8aaf0d8407db625d3e910cf180cd7b035fbc96bdfe58471b4` | J1--J15 standard |
| Q-415 hostile witness check | `510ebda9c05220b3eb229e865a0a41868f5ce166ff2a5805762d540309a6ab1b` | permanent regressions |
| Q-408 kernel build | `ccb94dfa8927cf8d2ec76cf85ff2f402d02d5aa5673b9d39c214a6de4c92309c` | finite physical current/kernel |
| metric V005 / DoR-019 candidate | `2a3790989b55ecca3f244155a11486ad0fdcba25603f36e051567ba670cd8961` | C/K carrier metrics and R4 units |

The V004 hash was recomputed after reading and remained unchanged.

### 0.2 Register sweep

```text
Q-408  exact finite physical current and bilocal kernel;
Q-410  physical refinement/locality package absent;
Q-411  J1--J15 define an equalizer, not its inhabitance;
Q-415  the abstract F_PLDEC witness was killed;
Q-416  V003 retained physical and formal conditional routes;
Q-417  Ref_path square derivable; free-P execution and family-wide
       refutation invalid;
Q-418  V004 installs the square and proposes the P_CM020 binding.
```

No settled entry constructs a norm on the eight-field package or exhibits
`P_CM020` as an element of the J1--J15 equalizer.

---

## 1. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| N1 square derivation and boundary | **PASS** | current additivity, W3 isometry, and Q-408 bilocal transport prove the rank-preserving square; the first remaining datum is genuinely new/interior PL realization and geometry |
| N2 `P_CM020` binding | **KILL** | the minimization is ill-typed on P4/P5/P7/P8 and no natural-family norm is supplied; `c_CM020` is asserted rather than constructed |
| N3 rigidity and end-test reading | **PASS CONDITIONALLY** | the nonderivation sweep is genuine and the member-scoped semantics are correct, but the proposed member is not executable |
| N4 whole-package coherence | **KILL** | all 15 equalizer rows remain conditional obligations; no proof-carrying inhabitant runs through them |
| N5 fresh attack | **KILL** | unique objectwise minima can fail restriction naturality; V004 lacks the global norm needed even to pose simultaneous minimization |

---

## 2. N1 — recomputation of the derived square

### 2.1 Current square

For an already realized path `gamma_e:[0,1]->M`, its `q` child paths are
fixed by parameter restriction:

```text
gamma_(e,j)(t)=gamma_e((j-1+t)/q),  j=1,...,q.    (N1-1)
```

Concatenation and additivity of line integration give

```text
sum_j int_(gamma_(e,j)) a = int_(gamma_e) a.      (N1-2)
```

Let `S_nm` copy a coarse conserved-current coefficient to the oriented
children.  On the unchanged physical test-form space, `P_nm=id`, and

```text
J_m(S_nm c)(a)=J_n(c)(a),
A_n=S_nm^* A_m P_nm.                              (N1-3)
```

The subdivision introduces degree-two vertices but no independent cycle.
Conservation forces equal child coefficients, so `S_nm` is an isomorphism
between the full conserved carriers in this scope.  W3's rank-preserving
isometry therefore gives

```text
S_nm^* R_(K,m) S_nm=R_(K,n).                      (N1-4)
```

This is the precise scope on which V004 uses DoR-019; no cycle-creating
arrow is promoted to an isometry.

### 2.2 Bilocal square

From `(N1-3)`--`(N1-4)`,

```text
R_(K,m)^(-1) A_m P_nm
  =S_nm R_(K,n)^(-1) A_n.                         (N1-5)
```

For the transported profile defined by

```text
(j_nm^H H)(S_nm x,S_nm y)=H(x,y),                 (N1-6)
```

direct substitution into Q-408's finite kernel gives

```text
Kern_m^fin(j_nm^H H)[P_nm a,P_nm b]
  =Kern_n^fin(H)[a,b].                            (N1-7)
```

Composition is inherited from nested interval restriction.  Relabeling,
orientation reversal, reality, and batching act on both sides of the same
equations.  Identity zero-extension adds no current and commutes wherever
both operations are defined.  At `n=m`, `(N1-7)` is the exact Q-408 bottom
map, so the DoR-008 check passes by equality.

### 2.3 Boundary

Equations `(N1-1)`--`(N1-7)` do not create a physical path for a new
interior/barycentric edge that is not a subpath of an existing `gamma_e`.
They also do not supply cell volume, coframe, density, Hodge data, a new
cycle direction, or completed localization.  Therefore V004's moved stop is
exact:

```text
SQUARE = DERIVED
ROUTE_A_BOUNDARY =
  NEW_INTERIOR_PL_EDGE_CELL_PHYSICAL_REALIZATION_AND_GEOMETRY / TYPE-U
N1 = PASS
```

---

## 3. N2 — `P_CM020` binding audit

### 3.1 What a binding must provide

A lawful bound Route-B member needs an actual term

```text
P_CM020=(P1,...,P8) in ContAdm_020
```

and a proof object

```text
c_CM020:C(P_CM020),
```

where `C` includes J1--J15, the clause-local certificates, and the finite
regressions.  A rule that merely says "take the unique object satisfying
these properties" defines a term only after existence and uniqueness have
been proved in typed ambient spaces.

V004 instead makes existence, closedness, uniqueness, and J1--J15
compatibility clauses *inside* `c_CM020`.  That is the proposition the
certificate must establish, not a construction of the certificate.

### 3.2 Field-by-field type audit

| Field | V004 rule | Audit |
|---|---|---|
| P1 representative | least norm in `Adm_base` | meaningful only if the full natural constraint set is nonempty, closed, and convex; those properties are not proved here |
| P2 reader | least Riesz norm after P8 | conditionally meaningful on a built Maxwell line, but P8 is itself unbuilt |
| P3 K action | `h_CM=0` | well-defined and target-blind; this row passes |
| P4 refinement/geometry | least-norm physical extension of paths, cells, coframes, densities, and common refinements | **ill-typed**: DoR-019 gives C/K carrier norms, not a norm on path maps, coframes, positive densities, or refinement functors |
| P5 topology/bounds | coarsest Hausdorff complete topology generated by local seminorm orbits | not a least-norm problem; existence of a coarsest complete topology and the uniform bounds are not proved |
| P6 faithfulness | quotient by the completed physical-kernel null space | definable only after P5 and the completed kernel exist; the finite-visible intersection theorem is still an obligation |
| P7 boundary/response | smallest contact ideal and least-norm response solution | ideal inclusion is typed, but no existence theorem for the smallest admissible ideal or Hilbert norm/domain for the full response solution is supplied |
| P8 Ward/Hodge/Maxwell | least-norm normalized package | **ill-typed**: no norm on the tuple of Hodge, domain, projection, and Maxwell data is defined |

The R4 unit seam controls C/K unit conversion.  It does not turn geometric
realizations, topology choices, contact ideals, or Hodge packages into one
normed vector space.  Consequently “after R4 transport” does not repair the
missing types.

### 3.3 Natural-family minimization is undefined

V004 anticipates objectwise-selection trouble by saying that minimization
is performed on simultaneous natural-family objects.  But it supplies no:

```text
ambient section space;
norm or locally convex topology on that section space;
stage weighting for an infinite/refinement family;
closedness or convexity theorem for the J1--J15 equalizer;
existence theorem for a minimum;
uniqueness theorem after automorphism torsors.
```

Different stage weights generally produce different minima.  Choosing
those weights would be another authored field.  Without them, “simultaneous
least norm” is not an operation.

### 3.4 Choice table and anti-tuning

The binding table does correctly disclose alternatives `B-CM`, `B-EX`,
`B-FAM`, and `B-REJ`, and its stated dependency order does not cite a
response, threshold, sealed number, rank value, or desired outcome.  Thus
the *intent* is target-blind.

Target blindness is necessary but not sufficient.  An ill-typed selection
rule cannot become a member merely because its failure is listed as a void
condition.  The sentence

```text
existence, closedness, uniqueness, and J1--J15 compatibility are clauses
of c_CM020
```

is precisely the undischarged inhabitance assertion.

```text
P_CM020_TERM_DEFINED = false
c_CM020_CONSTRUCTED = false
P4_MINIMIZATION_TYPED = false
P8_MINIMIZATION_TYPED = false
N2 = KILL
```

---

## 4. N3 — rigidity nonderivation and end-test semantics

### 4.1 Genuine nonderivation sweep

V004 tests the available forcing routes rather than merely asserting
nonrigidity:

1. the Q-396 completed-representative fiber has identical finite shadows;
2. J2 identifies the three readings *within* one member but does not equate
   distinct compatible reader coordinates;
3. J5 anchors P3 without fixing completed off-section values;
4. DoR-017 retains member-sensitive tags through the Schur chain;
5. DoR-008 sees equal finite shadows and therefore cannot establish a
   completed-output equality.

These routes are independent and correctly show that the current premises
do not prove

```text
N_020(P)=N_020(Q) for all certified P,Q.            (N3-1)
```

They do not prove that two final values differ, and V004 does not claim
that stronger statement.

### 4.2 Collapse-to-bound-member semantics

The future logic is stated correctly:

```text
certified P_CM020 disagrees -> that member and the bound Route-B model fail;
certified P_CM020 agrees    -> that model survives that test only;
some other P disagrees      -> that other P fails;
the whole family fails      -> only after uniform failure, all-member
                               failure, or proved emptiness/inconsistency.
```

A sealed-number mismatch does not refute every pre-gate family member.  An
agreement does not establish them.  This repairs V003's quantifier error.

Because N2 finds no constructed `P_CM020`, however, the binding cannot yet
collapse the family and no end test is executable.  The semantics pass;
the proposed execution does not.

```text
RIGIDITY = NOT_DERIVED / PASS
BOUND_MEMBER_TEST_SEMANTICS = PASS_CONDITIONALLY
END_TEST_EXECUTABLE = false / inherited_from_N2
N3 = PASS_CONDITIONALLY
```

---

## 5. N4 — whole-package coherence

### 5.1 The 15-family check

V004 retains the correct equalizer target

```text
ContAdm_020=Eq(J1,...,J15) subset F_raw.           (N4-1)
```

It also preserves the substantive obligations: reader presentation and
factorization, covariance/restriction, R1/R5 anchoring, Shape-K scope,
exact reader pairing, R4-only units, ordered batching, refinement and
density functoriality, response naturality, the boundary cocycle,
continuity/faithfulness, and the joint DoR-008 square.

But the review cannot rederive these rows **through `P_CM020`**, because
its P4/P5/P7/P8 maps do not exist as defined terms.  In particular:

```text
J2 waits on P8 -> P2;
J10-J13 wait on the actual P4/P7 arrows and topology;
J14 waits on P5/P6 uniform estimates and the completed kernel;
J15 waits on all of those maps forming the joint bottom square.
```

Writing the rows into `c_CM020` leaves the equalizer membership
conditional.  It does not provide the proof object.

### 5.2 Regressions

| Regression | Result |
|---|---|
| abstract kernel | **PASS on `Ref_path`; CONDITIONAL on Route B** — V004 names the actual Q-408 map, but no completed P4/P5 member exists |
| circular `pi_Mx` | **PASS as dependency order** — P8 precedes P2, but neither map is constructed |
| false reader nonemptiness | **KILL at binding level** — V004 correctly calls existence failure-capable, then nevertheless labels the unproved object a bound member |
| Hodge from isometry | **PASS** — the one-edge witness remains and no Hodge theorem is inferred from `(N1-4)` |
| DoR-008 | **PASS on derived Route A; CONDITIONAL on Route B** |

The 15 families and four regressions remain a sound *specification*.  They
do not establish package inhabitance.

```text
J1_J15_RETAINED = true
J1_J15_VERIFIED_ON_P_CM020 = false
BOUND_MEMBER_INHABITANCE = OPEN
PACKAGE_COHERENCE = INCOMPLETE
N4 = KILL
```

---

## 6. N5 — fresh attack: minimization versus restriction

This attack is not in V004's battery.

Let a coarse stage have

```text
V_N=R,
C_N={1},
```

and a refined stage have

```text
V_M=R^2,
C_M={(x,y):x+y=1},
rho_MN(x,y)=x.                                     (N5-1)
```

Both constraint sets are nonempty, closed, and convex.  Their Euclidean
least-norm members are unique:

```text
m_N=1,
m_M=(1/2,1/2).                                     (N5-2)
```

Nevertheless,

```text
rho_MN(m_M)=1/2 != 1=m_N.                          (N5-3)
```

So even unique least-norm members at every stage need not form a natural
family.  A natural compatible pair does exist: `m_N=1`, `m_M=(1,0)`.
Selecting it by one simultaneous minimum requires a norm on the section
space, for example a weighted product norm.  V004 defines no such norm, and
different stage weights can change the selected family.  On an infinite
refinement category, the convergence and completeness of that product are
additional data as well.

This counterexample is stronger than a nonconvex tie: it survives closed,
convex constraint sets and unique objectwise minima.  Automorphism
isometry does not imply restriction naturality.  Merely inserting the
restriction equations “before minimization” relocates the missing object
to an unspecified normed space of natural sections.

The attack applies directly to V004's P1/P2 natural-family language and
more strongly to P4/P8, where even the objectwise norms are absent.

```text
FRESH_ATTACK = RESTRICTION_MINIMUM_NONCOMMUTATION
COUNTEREXAMPLE = (N5-1)--(N5-3)
GLOBAL_NATURAL_SECTION_NORM = absent
N5 = KILL
```

---

## 7. Exact repair boundary

The Route-A repair is complete and should be retained verbatim.

Route B needs one of the following, without mixing them:

1. **Exhibited member:** define every P1--P8 map, define all ambient
   topologies/norms, and supply an actual `c_CM020` proof of J1--J15 and the
   regressions.
2. **Typed global minimization:** define a target-blind norm/topology on the
   natural-section equalizer, prove the equalizer nonempty and closed,
   prove a unique minimum exists, and prove that its P4/P5/P7/P8 components
   have the required physical types.
3. **Honest conditional family:** return to `for all P, C(P)->T(P)` and do
   not license member-sensitive execution until a member is supplied.
4. **Reject Route B.**

No route, member, reader, geometry, scale, or result is selected by this
review.

---

## 8. Final board

```text
N1 = PASS
N2 = KILL / P_CM020_not_defined_and_c_CM020_not_constructed
N3 = PASS_CONDITIONALLY / correct_rigidity_and_test_scope
N4 = KILL / equalizer_obligations_not_discharged_on_a_member
N5 = KILL / least_norm_does_not_commute_with_restriction

ROUTE_A_BOUNDARY = EXACT
ROUTE_B_BOUNDING_RULE = ILL_TYPED
RIGIDITY = NOT_DERIVED
FAMILY_LEVEL_REFUTATION = not_licensed
BOUND_MEMBER_REFUTATION = not_yet_executable

PACKAGE = NOT_READY / N2,N4,N5
READY_FOR_DOR020_RULING = no

p_symbolic = true
nu_symbolic = true
rank_or_ratio_selected = none
orientation_frame_filtration_selected = none
numeric_evaluation = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
