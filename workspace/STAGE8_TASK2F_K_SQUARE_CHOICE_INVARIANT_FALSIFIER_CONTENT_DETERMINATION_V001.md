# Stage 8 Task 2f K-Square Choice-Invariant Falsifier Content Determination v001

Date: 2026-08-01

Lane: CODEX LANE 1

Task: PASTE 323 -- comparison-map choice invariance for the DoR-008
`K_square` restriction arm

Status: RESULT -- ALL LISTED K-SQUARE VERDICTS ARE FILTRATION-INVARIANT;
THE DOR-008 RESTRICTION ARM REMAINS UNEXECUTABLE

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## 0. Lead determination

**The 1,088 admissible cellular filtrations do not create 1,088 different
`K_square` verdicts. Every listed sealed result on the completed square is
invariant under the filtration choice. In particular, the exact composition
operator for any two filtrations is related by unitary permutation conjugacy,
so its characteristic polynomial, spectrum with multiplicity, kernel
multiplicity, trace moments, and `R_square=3/16` are identical.**

That does **not** execute the DoR-008 falsifier. The completion still supplies
no finite scalar representation and no independently fixed source incidence
operator `X_K` whose restriction can be compared with `B_square`. The equation

```text
T_K X_K = B_square T_K
```

therefore has no left-hand operator. Defining `X_K` by pulling `B_square` back
through a chosen filtration would make the falsifier pass by definition and is
the tautology expressly refused in Q-217.

The corrected obstruction is consequently narrower and deeper:

```text
K_SQUARE_LISTED_RESULT_VERDICTS_CHOICE_INVARIANT = true
K_SQUARE_R_SQUARE_CHOICE_INVARIANCE_SUBTEST = PASS

FILTRATION_NONUNIQUENESS_BLOCKS_LISTED_RESULT_VERDICTS = false | TYPE-R |
  test: arbitrary-filtration unitary-conjugacy theorem in Section 3

K_SQUARE_COMPLETION_RESTRICTION_VERDICT = NO_VERDICT |
  prerequisite: an independently fixed completion-side finite representation,
                source incidence operator, and comparison intertwiner

K_SQUARE_DOR008_FALSIFIER_EXECUTED = false | TYPE-C |
  constraint: the C0 finite-incidence operator-preimage package is absent |
  release: the complete package displayed in Section 6

DOR008_VOIDED_BY_K_SQUARE_ARM = NO_VERDICT
```

Thus Q-217's 1,088-way nonuniqueness is moot **for the final sealed invariants**,
but not because the comparison problem is solved. The result-level choice has
collapsed; the object-level comparison remains unbuilt.

## 1. Preflight, currency, scope, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = yes; DoR-008 fixes the restriction obligation and the
                        sealed K_square result set is explicit
IS_THE_VERSION_CURRENT = yes through Q-239 at relay issue; Q-240 was read
ARE_ITS_INPUTS_PRESENT = yes for target-side choice invariance;
                        no for completion-side operator reproduction
```

Q-240 landed after the relay's stated head. It concerns the missing common
derivational origin of the finite law and ready state. It neither adds a finite
incidence operator nor changes the DoR-008 comparison interface, and therefore
does not bear on this determination.

### 1.2 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/
/Users/bgm/MB Work/alpha-program-archive/workspace/
/Users/bgm/MB Work/alpha_supervision/
```

### 1.3 Exclusions and query scope

```text
excluded: .git, binary/media payloads, duplicate mirrors as independent
          authorities, every custodian_private directory
a32_holdout/custodian_private/: not entered, read, or listed

word-boundaried, case-insensitive query families:
  K_square | composition-loop | B_square | D_square | R_square
  restriction | comparison | intertwiner | operator preimage
  filtration | linear extension | prefix | cell order
  quotient | relative phase | r_j | loop holonomy | vertex gauge
```

The bounded prefix/filtration search found no sealed `K_square` output whose
value depends on the order in which the eight cells are added. The only
substantive order-dependent object is Q-217's support-map family itself. The
sealed square results concern the completed four-vertex/four-edge complex.

```text
SEALED_K_SQUARE_PREFIX_HISTORY_RESULT_FOUND = false | TYPE-S |
  roots: the four roots above |
  exclusions: stated above |
  fences: exact K_square identifiers; no transport by name matching |
  query: word-boundaried K_square within bounded proximity of
         prefix, filtration, growth, stage, or order
```

### 1.4 Exact authorities

```text
DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md
  d51a6d5c5bb0020a081cfd2adfb545b9f5ed86ce660d3feacadc5ef68140fb19

BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
  20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48

BID_ELEMENTARY_RECORD_HILBERT_FUNCTOR_CLASSIFICATION_V001.md
  f583084bff8f50236b2695d1ce861b266a30dc584b2676a871e1bef8466384bd

cleanroom_output/35_GATE1_COMPARISON_GROUP_RESULT_V001.md
  7ec4e290201840a6e4a000c96d590fe08138d385afe2eb0f7a2c9887b1d46357

cleanroom_output/38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md
  ea707b3a5e5a93297c793c9f4227b456b97d7f8e184da95d96436299076915da

cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md
  a0d8b3f71632bd56cc3646fa59e84a2c2776539fadf04be733c7a1eaa997bdbb

STAGE8_COMPOSITION_LOOP_STRUCTURAL_PREDICTION_BUILD_V001.md
  5810377123b823e680891a3337855750ac8f362951dca048dad3a78a34c79d79

STAGE8_V011_COMPOSITION_LOOP_MATRIX_EXPERIMENT_RESULT_V001.md
  29fcbb76748cec8ecbaa8f9debb1e60736c85dbcf54823cb8076c3f17d6e3ffb

STAGE8_TASK2F_FINITE_INCIDENCE_REALIZATION_FUNCTOR_FORCING_PROTOCOL_RESULT_V001.md
  a4d8b9c44fd0705ba97fd49d1e0c8373c28e12e2c3acea9409b60217b274a0f8

STAGE8_CTP_PHYS_INPUT_PACKAGE_U3_DOR008_DOR009_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md
  b0118d89e0b4b321fbf9caab5bfb811a0b5fd572e808d02615ee8503db2bc1ac
```

DoR-008 states at lines 18-22 that the completed framework must reproduce
every sealed finite result on restriction, including the Gate 1-4 structures,
the composition-loop spectrum with `R_square=3/16`, the four kernel planes,
and later finite theorems. The present arm is only the `K_square` arm. Gate 2's
first-opening carrier, Gate 4's covector-ray functional, and the four S/R/E
kernel planes are different finite carriers and are not silently imported into
this comparison.

## 2. The bare K-square restriction test

### 2.1 The sealed K-square result set

The completed-square authority consists of the following result classes.

| Result class | Sealed content | Required preservation by a comparison map |
|---|---|---|
| Carrier and grading | The unfilled oriented square has four named vertices, four named edges, no `2`-cell, and carrier `C_0(K_square) direct-sum C_1(K_square)`; V011 `:1840-1901`. | Cell identity, degree, orientation, direct-sum carrier, and absence of `C_2`. |
| Gauge group and holonomy | Gate 1 fixes the compact `U(1)` comparison group; V011 `:1860-1873` fixes the ordered path-ratio holonomy `exp(i Phi)`; Gate 4 preserves loop holonomy modulo vertex gauge. | Vertex-gauge action, edge transports, path order, loop orientation, and path-ratio holonomy. |
| Hilbert forms and adjoint | Gate 3 fixes identity fiber forms and the canonical normalized transition operator modulo overall congruence; result `:8-33`. | Isometry of cell bases, degree forms, adjoint, and normalized operator class. |
| Differential class | Gate 4 fixes unit-weight covariant incidence modulo gauge with holonomy as the sole physical freedom; result `:9-31`. | Boundary, orientation involution, unit edge magnitude, gauge class, and operator intertwining. |
| Untwisted topology | The structural build proves ordinary incidence rank `3`, cycle rank `1`, and cycle generator `e_a0-e_0b+e_ab-e_ba`; structural result `:186-225`. | Chain-complex isomorphism and the resulting homological dimensions; the displayed generator may change coordinates only by the permitted basis transport. |
| Twisted composition operator | At `Phi=pi`, the exact `D_square` and Hermitian block operator `B_square` are fixed in the printed bases; matrix result `:46-127`. | A unitary carrier map that intertwines an independently fixed completion-side operator with `B_square`. |
| Six matrix outputs | Characteristic polynomial, ordered spectrum with multiplicity, kernel multiplicity, `Tr(B^2)=16`, `Tr(B^4)=48`, and `R_square=3/16`; matrix result `:129-197`. | Unitary-equivalence invariants of the operator restriction. |

The map needed to **pose the full falsifier** is therefore not merely a
bijection between eight labels and eight cells. It must preserve all of:

```text
cell identities and degrees;
orientation and cellular boundary;
the U(1) gauge action and edge transports;
Gate-3 Hilbert forms and adjoints;
the Gate-4 unit-weight differential class;
an independently fixed completion-side finite representation;
an independently fixed completion-side incidence operator X_K;
and the operator equation T_K X_K = B_square T_K.
```

### 2.2 Result-level versus object-level comparison

There are two distinct tests:

```text
RESULT-LEVEL TEST:
  if one only changes the admissible cellular filtration used to coordinatize
  the completed target K_square carrier, do its sealed verdicts change?

OBJECT-LEVEL DOR-008 TEST:
  does the restriction of the independently constructed completed framework
  produce an operator unitarily equivalent to the sealed B_square?
```

This artifact executes the first. The second is not reducible to it.

## 3. Arbitrary-filtration invariance theorem

Let `o` be any of Q-217's 1,088 linear extensions of the `K_square` face
poset. At the final stage, its support map is

```text
T_o : V_8 -> H_square,
T_o(e_i) = the normalized elementary-cell vector named by o_i.
```

Q-217's candidate definition preserves cell identity, degree, orientation
representative, and unit norm. Gate 3 makes the elementary-cell basis
orthonormal. Hence every full-stage `T_o` is unitary. Define the target
operator written in the sequential coordinates of `o` by

```text
B_o := T_o^* B_square T_o.
```

For two admissible filtrations `o` and `o'`, put

```text
P_(o,o') := T_o^* T_o'.
```

`P_(o,o')` is a unitary permutation/fiber matrix, and direct substitution
gives

```text
B_o' = P_(o,o')^* B_o P_(o,o').
```

This is a proof for an arbitrary pair, not an enumeration of selected
examples. Since all 1,088 final support maps are in this class, it reaches the
entire family.

The same argument gives degreewise row/column unitary equivalence for
`D_square`. Vertex-frame and orientation-representative changes add only the
sealed diagonal/unitary conventions, so they do not alter the conclusion.

Consequences:

```text
det(z I-B_o') = det(z I-B_o);
spec(B_o') = spec(B_o), with multiplicity;
dim ker(B_o') = dim ker(B_o);
Tr[(B_o')^m] = Tr[(B_o)^m] for every m;
R_square(B_o') = R_square(B_o);
rank(partial_1) and cycle rank are unchanged;
the Gate-3 form class and Gate-4 differential class are unchanged;
and the named path-ratio holonomy is unchanged by cell order.
```

The **literal displayed matrix entries** are not equal across filtrations. They
are permutation-conjugate. Literal coordinate equality is not a sealed
physical verdict and is not required by an isomorphism-respecting restriction
test.

### 3.1 Classification of every listed result

| Listed result | Across all 1,088 filtrations | Reason |
|---|---|---|
| Four vertices, four edges, no `2`-cell, dimension `8` | SAME | Every final map is a bijection onto the same complete cell basis. |
| Degree split `C_0 direct-sum C_1` | SAME after transported grading | Each coordinate retains the degree of its named cell. |
| Gate-1 `U(1)` group | SAME | Filtration does not change the comparison group. |
| Gate-3 identity forms/canonical adjoint | SAME modulo unitary congruence | Cell relabelings are unitary permutation/fiber maps. |
| Gate-4 unit-weight incidence class | SAME modulo gauge and orientation convention | The target differential and weights are fixed; order only changes coordinates. |
| Ordinary incidence rank `3` and cycle rank `1` | SAME | Chain-complex isomorphism preserves ranks and homology. |
| Named loop holonomy `exp(i Phi)` | SAME | The two named paths and their ratio are target cell data, not prefix-order data. |
| Exact `D_square`/`B_square` coordinate displays | DIFFERENT DISPLAYS, SAME OPERATORS UP TO UNITARY TRANSPORT | Row/column permutation or full carrier conjugacy. |
| Six sealed matrix outputs | SAME | Characteristic polynomial, spectrum, nullity, traces, and trace ratio are unitary invariants. |

```text
LISTED_SEALED_K_SQUARE_VERDICT_IS_FILTRATION_DEPENDENT = false | TYPE-R |
  test: arbitrary-pair conjugacy theorem plus the exhaustive result table above

RAW_COORDINATE_MATRIX_EQUAL_ACROSS_DISTINCT_FILTRATIONS = false | TYPE-R |
  test: the two named orders in Section 4 give different displays related by
        an explicit permutation conjugacy
```

## 4. Concrete finite check on the strongest sealed result

The general proof was checked on two named admissible filtrations:

```text
o_A = (v_00,v_10,v_01,v_11,e_a0,e_0b,e_ab,e_ba)

o_B = (v_10,v_00,e_a0,v_11,v_01,e_ab,e_0b,e_ba).
```

`o_B` is a valid linear extension: each edge appears after both endpoint
vertices. Let `P` send the sequential coordinates of `o_B` to the frozen cell
basis used by the sealed matrix result. Exact integer/rational arithmetic gave

```text
P^T P = I_8;
B_(o_B) = P^T B_(o_A) P;

charpoly(B_(o_A)) = charpoly(B_(o_B))
  = z^8 - 8 z^6 + 20 z^4 - 16 z^2 + 4;

rank(B_(o_A)) = rank(B_(o_B)) = 8;
nullity(B_(o_A)) = nullity(B_(o_B)) = 0;
Tr[B_(o_A)^2] = Tr[B_(o_B)^2] = 16;
Tr[B_(o_A)^4] = Tr[B_(o_B)^4] = 48;
R_square(o_A) = R_square(o_B) = 3/16.
```

The exact characteristic-polynomial coefficients were computed independently
from the displayed integer matrices by the Faddeev-LeVerrier recurrence; rank
used exact rational elimination. This check is illustrative. Section 3's
arbitrary-pair proof, not these two samples, reaches all 1,088 filtrations.

```text
K_SQUARE_STRONGEST_SEALED_RESULT = R_square=3/16
K_SQUARE_R_SQUARE_CHOICE_INVARIANCE_SUBTEST = PASS
K_SQUARE_FINAL_TARGET_INVARIANT_SUBSET_EXECUTED = true
```

## 5. Q-239 relative phases do not supply the comparison map

Q-239 constructs

```text
q_N(z_+,z_-)_j = r_j := conjugate(z_(-,j)) z_(+,j)
```

on the doubled sequential history carrier and proves
`Q_N = X_N/(G_N/U(1)_diag) isomorphic to U(1)^N`; see the U3 result
`:153-252`. The descended finite objects depend on `product_j r_j`; see
`:258-307`.

The `K_square` holonomy is a different typed object:

```text
u_ab u_a0 (u_ba u_0b)^(-1) = exp(i Phi),
```

the path ratio of one spatial/cellular connection on the unfilled square;
V011 `:1860-1873`.

Both are orbit-invariant, but under different actions on different domains:

| Object | Domain | Gauge quotient | Meaning |
|---|---|---|---|
| `r_j` | Pair of forward/backward sequential histories | Common CTP vertex-gauge action | Relative phase between two histories on one sequential link. |
| `exp(i Phi)` | Four edge transports on one `K_square` incidence complex | Vertex gauge on the square | Relative transport of two spatial/cellular paths with common endpoints. |

Orbit invariance alone does not identify the domains. No sealed map sends the
sequential relative phases to the four named square edge transports while
preserving degree, orientation, path order, incidence, and operator action.
Q-239 itself says at `:696-717` that `q_N` does not express the incidence
operator and does not close the Task-2f comparison maps.

```text
Q239_RELATIVE_PHASE_TO_K_SQUARE_EDGE_MAP_FOUND = false | TYPE-S |
  roots: the four roots in Section 1 |
  exclusions: Section 1.3 |
  fences: no name matching from the shared words phase, holonomy, or U(1) |
  query: bounded intersections of
         {q_N,r_j,relative phase,common gauge} with
         {K_square,u_ab,u_a0,u_ba,u_0b,B_square,incidence}

Q239_QUOTIENT_ALONE_CLOSES_K_SQUARE_COMPARISON = false | TYPE-R |
  test: domain/codomain and preserved-structure comparison above, confirmed by
        Q-239's own Task-2f boundary at lines 696-717
```

## 6. Why the DoR-008 arm still cannot run

The result-level invariance theorem removes the need to **select a preferred
one of the 1,088 filtrations before asking an invariant question**. One may
choose any filtration as coordinates after an actual source operator and
intertwiner exist; all choices would yield the same invariant verdict.

What is still absent is the completion-side object to put into those
coordinates. The required package, carried forward from Q-217, is

```text
C0_FINITE_INCIDENCE_OPERATOR_PREIMAGE_PACKAGE := (
  finite C0 algebra/subquotient A_C0,K,
  finite comparison-capable carrier E_C0,K,
  representation rho_C0,K,
  source incidence operator X_K,
  map T_K,
  equations
    T_K rho_C0,K(a) = rho_K(a) T_K,
    T_K X_K = B_K T_K,
  provenance fixing A_C0,K, E_C0,K, rho_C0,K, X_K, and T_K
    before the sealed B_K outcome is inspected
).
```

The filtration can now be treated as a coordinate choice **only after** this
package fixes `X_K` independently. Without `X_K`, setting

```text
X_K^o := (T_o)^(-1) B_square T_o
```

would construct the tested object from the answer. It would prove only the
choice-invariance theorem already established here, not reproduction by the
completion.

```text
C0_SOURCE_INCIDENCE_OPERATOR_FOUND = false | TYPE-S |
  roots: parent program, current cleanroom, archive workspace,
         cleanroom_output, alpha_supervision |
  exclusions: binary/media, duplicate mirrors as independent authority,
              every custodian_private directory |
  fences: D_C0 is a provenance descent map, not an incidence operator;
          no pullback from B_square is accepted as an independent source |
  query: C0_008 or A_C0 or E_C0 with incidence, boundary, D_square,
         B_square, source operator, preimage, or intertwiner

NONTAUTOLOGICAL_B_SQUARE_PREIMAGE_FIXED = false | TYPE-U |
  would-build: C0_FINITE_INCIDENCE_OPERATOR_PREIMAGE_PACKAGE

K_SQUARE_OPERATOR_RESTRICTION_CHECK = UNEXECUTABLE | TYPE-C |
  constraint: independently fixed source incidence operator and finite
              comparison representation absent |
  release: C0_FINITE_INCIDENCE_OPERATOR_PREIMAGE_PACKAGE

K_SQUARE_SEALED_RESULT_REPRODUCED_BY_C0 = NO_VERDICT
K_SQUARE_SEALED_RESULT_DISAGREES_WITH_C0 = NO_VERDICT
DOR008_FALSIFIER_FIRED = NO_VERDICT
```

This is not a fifth forcing attempt. No filtration is selected or forced, and
no source operator is created.

## 7. Final answer to the four relay questions

### 7.1 What the bare restriction test requires

It requires reproduction of the completed `K_square` carrier/grading,
U(1)-holonomy structure, Gate-3 forms, Gate-4 differential class, ordinary
cycle data, exact twisted operator, and all six matrix outputs. A map must
preserve the structures listed in Section 2 and intertwine an independently
fixed completion-side operator with `B_square`.

### 7.2 Does the verdict factor through the 1,088-way choice?

**Yes for every listed sealed `K_square` verdict.** The final operators are
unitarily permutation-conjugate. No listed result differs under two
filtrations. The only differing data are the prefix history and raw coordinate
display, neither of which is a sealed `K_square` verdict.

### 7.3 Does the invariant subset run concretely?

**Yes.** The strongest listed result, `R_square=3/16`, passes the target-side
choice-invariance subtest exactly, as do all five other matrix outputs and the
structural results.

### 7.4 Does the K-square DoR-008 arm now pass or fail?

**Neither. `NO_VERDICT`.** Choice invariance makes forcing a preferred
filtration unnecessary for invariant outputs, but does not supply the
completion-side operator. The arm remains constraint-unexecutable until the
operator-preimage package exists. No disagreement has been exhibited, so
DoR-008 is not voided by this result.

## 8. Fence and custody ledger

```text
artifact_status = RESULT
sealed_finite_spectrum_reused_not_recomputed_as_physical_target = true
structural_permutation_conjugacy_computed = true
fifth_forcing_attempt_run = false
filtration_selected_as_physics = false
source_operator_defined_by_target_pullback = false
a32_custodian_private_touched = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
kappa_Thomson_computed = false
coupling_evaluation_authorized = false
production_authorized = false
physical_root_computed = false
measured_constant_comparison_performed = false
Misner_Sharp_Brown_York_fork_resolved = false
git_command_run = false
register_edited = false
```

