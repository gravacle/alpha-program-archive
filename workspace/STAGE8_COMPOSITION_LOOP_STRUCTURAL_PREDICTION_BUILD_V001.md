# Composition-Loop Structural Prediction Build v001

Date: 2026-08-01  
Lane: CODEX 2  
Register head at issue: relay 260  
Road justification: **THE MANDATED COMPOSITION-LOOP CARRIER; bears on Step 1 and CORE-RESULT-SEAL.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## 1. Lead determination

**The oriented square is protocol-mandated and its structural loop prediction
builds, but the loop is only permitted—not forced—by the sealed composition
law.** Once the square is supplied, its underlying cycle rank is exactly one.
What is missing is a derivation of the square from composition: V011 supplies
no commuting/confluence theorem that forces two orders through distinct
intermediate vertices to share one terminal vertex.

The distinction is visible in the verbs used by the sources:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1858` — under “Fully
> specified composition-loop prediction,” the text says “**Use** the unfilled
> oriented `1`-skeleton `K_square`” and then lists the four vertices, four
> edges, and two forward paths.

The earlier provenance is even more explicit that this is an instruction:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V002.md:276-280` — “After deriving
> the first-incidence operator, **form** the minimal commuting two-handle
> composition square. Let `Phi` be its gauge-invariant loop action.”

By contrast, the general sealed composition law only composes maps:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:337-369` — a morphism is
> `(i,eta)` and composition is `(j compose i,
> {zeta_(i(v)) compose eta_v}_v)`; the text derives associativity and identity
> laws from ordinary map composition.

Its explicit sequential example supplies a chain, not a diamond:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:633-655` — for
> `L_s --U--> L_t --V--> L_u`, sequential composition gives the three-input
> colimit map and “does not identify the three input records or omit the
> intermediate endpoint.”

Nothing in those composition clauses requires two distinct handles, requires
their orderings to commute, or identifies the two terminal composites. Thus:

```text
K_square_protocol_mandated = true
K_square_forced_by_general_composition = false | TYPE-R |
  test: compare V011's general and sequential composition laws with the
        square's required two-path commuting/confluence shape
K_square_forced_if_commuting_two_handle_diamond_is_supplied = true | CONDITIONAL
```

The V011 algebraic experiment is fully specified once `K_square` is accepted.
The **compositional semantics that selects it** are not derived. “Fully
specified” is therefore true of the matrix experiment and false if read as a
theorem that composition itself selects the carrier.

## 2. Search scope, exclusions, and object separation

### 2.1 Roots entered

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/
/Users/bgm/MB Work/alpha-program-archive/workspace/
/Users/bgm/MB Work/alpha_supervision/
```

The first root includes the current cleanroom and the older gravity arm.
`cleanroom_output/` was entered separately because it is outside archive
`workspace/` and contains the passed Gate 1–4 result artifacts.

### 2.2 Exclusions and fences

```text
excluded: .git, node_modules, vendor, binary/non-Markdown payloads
review-packet duplicates: provenance only, not independent current authority
every custodian_private directory: excluded from recursion
a32_holdout/custodian_private/: not entered, read, or listed
```

### 2.3 Word-boundaried, case-insensitive query families

```text
composition[- ]loop | K_square | ordered loop holonomy |
two-handle composition | composition square | sequential composition

quarter[- ]turn | unit[- ]flux | record-changing holonomy | K_write,rel

temporal plaquette | two-skeleton | unfilled 1-skeleton | curvature |
Wilson loop | face holonomy | first-opening loop
```

The bounded two-list intersection between composition-loop files and
quarter-turn/unit-flux files returned only taxonomy/adjudication artifacts,
their archive mirrors, the settled-question register, and relay instruction
files. The unique substantive authorities were:

```text
STAGE8_HOLONOMY_FIRST_OPENING_TENSION_ADJUDICATION_EINSTEIN_V001.md
STAGE8_LOAD_BEARING_HOLONOMY_DERIVABILITY_DETERMINATION_V001.md
QUESTIONS_SETTLED_REGISTER_V001.md
```

All three distinguish the objects; none supplies an identity or a map from the
composition-loop phase to the source-flux record-write phase.

```text
composition_Phi_identified_with_record_write_quarter_turn = false | TYPE-S |
  roots: the four roots above |
  exclusions: stated in section 2.2 |
  query: word-boundaried intersection of
         {composition-loop, K_square} with
         {quarter-turn, unit-flux, record-changing holonomy, K_write,rel} |
  file_list: the three unique substantive authorities above |
  would-build: an explicit cross-carrier map proving preservation of phase,
               orientation, normalization, and order
```

No such identity is used below.

## 3. Exact recovered specification

### 3.1 Carrier and orientation

V011 states:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1840-1851` — “Use the
> unfilled oriented `1`-skeleton `K_square` with no `2`-cell” with vertices
> `v_00, v_10, v_01, v_11` and edges
> `e_a0: v_00 -> v_10`, `e_0b: v_00 -> v_01`,
> `e_ab: v_10 -> v_11`, and `e_ba: v_01 -> v_11`.

The two paths are:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1853-1858` —
> `v_00 --e_a0--> v_10 --e_ab--> v_11` and
> `v_00 --e_0b--> v_01 --e_ba--> v_11`.

V002 names their intended provenance “the minimal commuting two-handle
composition square” (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V002.md:276-280`).
V011 does not define the physical identities of handles `a` and `b`, prove
that both ordered composites exist, or prove that they share `v_11`.

### 3.2 Holonomy definition

V011 defines `Phi` only through the ratio of the two path transports:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1860-1873` — “Let the ordered
> loop holonomy be”
> `u_ab u_a0 (u_ba u_0b)^(-1) = exp(i Phi)`, then fix three edge transports
> to the identity and place the residual phase on `u_ba`.

For each edge, the twisted incidence map is:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1875-1888` —
> `partial_rho,e x = u_e x v_target - x v_source`, and
> `B_square(Phi)` is the off-diagonal block matrix built from `partial_rho`
> and its adjoint.

The carrier and bases are fixed:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1881-1901` — “No filled
> `2`-cell is included in the trace carrier”; the full space is
> `C_0(K_square) direct-sum C_1(K_square)`, with ordered vertex and edge bases
> printed explicitly.

Finally, V011 prints the exact twisted incidence and block-matrix convention
at `:1903-1921`, preregisters one later phase evaluation at `:1923-1927`, and
requires the characteristic polynomial, ordered spectral list, kernel
multiplicity, two trace moments, and their normalized ratio at `:1929-1941`.
This lane does not reproduce or execute the preregistered phase value because
relay 260 expressly forbids evaluating `Phi` and forbids computing any
eigenvalue.

## 4. Structural build: incidence and cycle rank

The cycle rank is established from the oriented incidence, not from the counts.
In the frozen edge order `(e_a0,e_0b,e_ab,e_ba)`, forget only the connection
weights and retain the orientations. The ordinary boundary matrix is:

```text
partial_1 =
[[-1, -1,  0,  0],
 [ 1,  0, -1,  0],
 [ 0,  1,  0, -1],
 [ 0,  0,  1,  1]].
```

An exact rational elimination was executed. The first three columns are pivot
columns, so `rank(partial_1)=3`. Equivalently, a displayed `3 x 3` minor has
unit magnitude, while the row sum is zero, giving the matching upper bound.

The oriented chain

```text
c_square = e_a0 - e_0b + e_ab - e_ba
```

has exact zero boundary. In the frozen edge basis its coefficient vector is
`(1,-1,1,-1)`, and direct multiplication gave `(0,0,0,0)`. Because the
boundary rank is three on four edge generators, this cycle spans the whole
kernel:

```text
underlying_graph_incidence_rank = 3
underlying_graph_cycle_rank = 1
underlying_graph_cycle_generator = e_a0 - e_0b + e_ab - e_ba
```

This is the topological cycle of the unfilled graph. It must not be confused
with the kernel of the **twisted** incidence `D_square(Phi)`: nontrivial loop
transport can lift a twisted parallel section without removing the graph's
cycle. The prediction's phase dependence is precisely why V011 uses the
twisted matrix rather than the ordinary boundary.

## 5. Is the loop forced?

There are three different verdicts:

| Claim | Verdict | Evidence |
|---|---|---|
| The selected `K_square` has a loop | **YES, forced once selected.** | Section 4's exact incidence proof gives a one-dimensional cycle space. |
| V011 requires this carrier for its internal prediction | **YES, protocol-mandated.** | V011 `:1836-1841` says “Use” it; `:1789-1792` requires “the composition-loop result” for `CORE-RESULT-SEAL`. |
| General composition necessitates this carrier | **NO.** | V011 `:337-369` defines ordinary morphism composition; `:633-655` explicitly produces a sequential chain. No commuting/confluence axiom forces a square. |

The missing antecedent can be stated exactly. A square would be forced if the
theory derived all of:

```text
two distinct admissible handles a and b;
both ordered composites ab and ba;
distinct intermediate public states v_10 and v_01;
a common terminal public state v_11;
no identification or collapse of either intermediate path;
and no filled 2-cell included in the carrier.
```

V002 supplies the phrase “commuting two-handle composition square” but does not
derive those six clauses. V011 supplies the resulting graph as an instruction.
Thus the square is a **preselected test carrier**, not a mathematical
consequence of the category's general composition operation.

```text
composition_forces_some_sequential_composite = true
composition_forces_commuting_two_handle_diamond = false | TYPE-R |
  test: general-law/sequential-example implication check
composition_loop_prediction_conditional_on_carrier_selection = true
```

## 6. What `Phi` depends on

Structurally, `Phi` is a functional of:

```text
the four oriented edge transports of the discrete U(1) connection;
the two ordered paths from v_00 to v_11;
their relative path composition;
the chosen loop orientation;
and vertex-gauge equivalence.
```

Under a vertex gauge transformation, each path transport acquires the same
terminal factor on the left and the same initial inverse factor on the right.
Their ratio therefore cancels both factors. This is the gauge-invariant
content of the definition at V011 `:1860-1873` and agrees with the Gate-4
theorem:

> `alpha-program-archive/cleanroom_output/32_GATE4_DIFFERENTIAL_UNIQUENESS_RESULT_V001.md:17-25`
> — vertex rephasing removes tree phases, while “loop holonomy is
> gauge-invariant and survives.”

Composition alone does not set `Phi`. V011 also expressly imposes no face
flatness:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:294-304` — each edge carries
> unitary transport and “No flatness around a filled two-cell is imposed.”

No numeral, bound, or comparison for `Phi` is produced here.

## 7. Relation to the temporal plaquette and curvature

The composition loop and temporal plaquette are **different objects**:

| Feature | Composition loop | Temporal plaquette diagnostic |
|---|---|---|
| Carrier | Unfilled oriented one-skeleton; V011 `:1840-1851`. | A complete-Qspec two-cell object; `COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_RESULT_V001.md:13-20`. |
| Structural datum | Relative holonomy of two paths; V011 `:1860-1873`. | Finite temporal response to connection histories, including endpoint-trivial holonomy histories; result `:13-20`. |
| Output class | Parameterized finite block-operator spectral prediction mandated by V011. | Temporal electric-sector response diagnostic; diagnostic spec `:217-231`. |
| Scope ceiling | No filled face and therefore no local face curvature or density. | Does not establish spatial magnetic plaquette, full local Maxwell tensor, continuum independence, linked-cluster density, matching limit, or proof authorization; diagnostic spec `:217-231`. |

An unfilled one-skeleton **can carry global loop holonomy** because the cycle
space is nonzero. It **cannot by itself carry the local curvature-level object
needed for a Maxwell construction**. V011's own curvature definition starts
with an oriented elementary two-cell and its boundary word:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:864-904` — for an “oriented
> elementary two-cell” it defines positive and negative boundary transports,
> their holonomy, and `F_BR` by a local logarithm.

But the composition-loop carrier says “no `2`-cell” (`:1840`) and “No filled
`2`-cell is included in the trace carrier” (`:1881-1882`). Therefore it has no
face generator, no face area, no local curvature two-cochain, and no local
quadratic curvature density. It could become boundary data for a later filled
cell only through an additional, explicit carrier-extension map.

```text
composition_loop_carries_global_holonomy = true
composition_loop_is_curvature_plaquette_carrier = false | TYPE-R |
  test: degree/carrier check against V011's own two-cell curvature definition
composition_loop_alone_closes_curvature_localization_bridge = false | TYPE-R |
  test: C_2 is absent and no filled face exists
composition_loop_to_temporal_plaquette_identity_derived = false | TYPE-S |
  roots: the four roots in section 2 |
  exclusions: section 2.2 |
  query: word-boundaried composition-loop/K_square and temporal-plaquette/two-cell sweep |
  would-build: an explicit carrier-extension or functor from K_square to the
               complete-Qspec temporal two-cell preserving connection and response
```

This agrees with the parallel localization result without importing its target:

> `STAGE8_PRPS_GATE4_LOCALIZATION_BRIDGE_ATTEMPT_V001.md:279-290` — loops are
> not needed at transport/gauge level, are needed at curvature/plaquette level,
> and the later temporal diagnostic does not establish local Maxwell form or
> the continuum response objects.

## 8. “Fully specified” test and build boundary

### 8.1 What is complete

The following execution inputs are fixed in V011:

```text
carrier vertices, edges, and orientation;
two path orderings;
holonomy functional and fixed gauge;
edge differential;
Gate-3 Hilbert forms;
ordered bases;
exact twisted incidence matrix;
block-operator convention;
one preregistered evaluation point;
and the complete required output list.
```

Gate 3's referenced forms exist:

> `alpha-program-archive/cleanroom_output/38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md:8-33`
> — the constraints force the canonical Hilbert-form pair modulo overall
> congruence and make the normalized transition operator canonical.

Therefore the **matrix experiment** has no missing algebraic input.

### 8.2 What is not complete

The composition-to-carrier derivation is absent, as section 5 proves. In
addition, this relay's fence prevents executing the full V011 output list:
V011 `:1929-1941` requires a spectral list, while relay 260 forbids computing
any eigenvalue and forbids evaluating `Phi`.

```text
V011_matrix_experiment_fully_specified = true
V011_carrier_selection_derived_from_composition = false | TYPE-R |
  test: composition implication check in section 5
V011_composition_loop_prediction_sealed = false | TYPE-U |
  would-build: execute and seal every output required at V011:1929-1941
this_lane_authorized_to_complete_spectral_would_build = false | TYPE-C |
  constraint: relay 260 no-eigenvalue and no-Phi-evaluation fences |
  release: NONE WRITTEN
composition_loop_structural_carrier_result_built = true
```

Q-69 is observed: this sidecar-sealed structural artifact is not identified
with, and does not flip, V011's governing
`composition_loop_prediction_sealed` flag.

## 9. What full sealing would require

For the composition-loop result itself:

1. Preserve the V011 carrier, bases, gauge convention, phase point, and output
   list without retuning (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1945`).
2. Produce the exact characteristic polynomial, complete ordered spectral
   output with multiplicity, exact kernel multiplicity, both required full-
   carrier trace moments, and the normalized moment ratio (`:1929-1941`).
3. Treat the symbolic result as authority and use a separately coded
   high-precision diagonalization only as a check (`:1940-1941`).
4. Seal the result and independent reconstruction without modifying BID
   (`:1943-1945`).

For `CORE-RESULT-SEAL`, V011 additionally requires:

> `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1781-1792` — three distinct
> reviewer/process identities, verified hashes, `SPEC-SEAL`, executed Gates
> 1–5, the composition-loop result, three unanimous core reports, and an
> independent core reconstruction.

Those requirements are not silently collapsed into this lane artifact.

## 10. Version differences, reported and not repaired

```text
V001: no composition-loop section found.
V002: introduces a verbal “minimal commuting two-handle composition square”
      and explicitly says the first-opening tree carries no loop holonomy
      (V002:276-304).
V008: first located “Fully specified composition-loop prediction” with K_square.
V009/V010/V011: retain the fully specified K_square section.
V008-V011: the explicit V002 first-opening-tree disclaimer is absent.
```

The regression does not change this result: the first-opening tree and the
composition square remain differently ordered carriers. The missing sentence
would have made that separation harder to misread, but this lane does not edit
or restore it.

The adjacent Gate-4 tree-test instrumentation issue is not worked here. It does
not affect the exact K-square incidence proof above and is not folded into this
result.

## 11. Test wiring

| Test | Verdict owned | Result |
|---|---|---|
| T1 exact edge/vertex incidence reconstruction | `K_square_incidence_matches_V011` | PASS |
| T2 rational rank and cycle-vector multiplication | `underlying_graph_cycle_rank_is_one` | PASS |
| T3 path-ratio vertex-gauge cancellation | `Phi_is_gauge_invariant_functional` | PASS |
| T4 general-composition implication attack | `composition_forces_K_square` | FAIL — refuted |
| T5 cross-holonomy identity sweep | `composition_Phi_equals_record_write_phase` | SCOPE-EMPTY; no identity used |
| T6 carrier-degree curvature test | `unfilled_K_square_is_curvature_plaquette` | FAIL — refuted |
| T7 algebraic specification completeness | `V011_matrix_experiment_fully_specified` | PASS |
| T8 current-fence authorization check | `full_spectral_execution_authorized_this_lane` | BLOCKED BY CONSTRAINT |

Each test reports only into the verdict named in its middle column.

## 12. Fence and custody ledger

```text
a32_custodian_private_touched = false
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
kappa_Thomson_computed = false
coupling_evaluation_authorized = false
production_authorized = false
scale_computed = false
root_computed = false
eigenvalue_computed = false
beta_function_computed = false
Phi_evaluated = false
measured_constant_comparison_performed = false
Misner_Sharp_Brown_York_fork_resolved = false
```
