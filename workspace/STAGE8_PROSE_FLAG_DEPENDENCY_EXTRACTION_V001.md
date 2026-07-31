# Stage 8 Prose/Flag Dependency Extraction V001

LANE: CODEX 1. CHARTER: Paste 172. DATE: 2026-07-31.
REGISTER HEAD AT ISSUE: Q-73. STATUS: EXTRACTION RECORD.

Fences: `alpha_computed = false`; `proof_authorized = false`;
`kappa_record_computed = false`. No alpha, `kappa_record`,
`kappa_Thomson`, coupling, radius, scale, root, eigenvalue, beta function,
`E_R`, `T_R`, `k_R`, absolute interval, or measured-constant comparison was
computed or evaluated. `a32_holdout/custodian_private/` was not opened. B0
and `CTP_PHYS_INPUT_PACKAGE` internals are recorded only as dependency
surfaces already stated by Codex 2 artifacts; this artifact does not specify
B0. Boundary leaves are not classified as axioms or debts; Einstein owns that
classification.

## 0. Scope

```text
roots:
  /Users/bgm/MB Work/alpha-program-archive/workspace
  /Users/bgm/MB Work/alpha-program-archive/supervision
file types:
  *.md, *.json, *.csv
files swept:
  1081
exclusions:
  a32_holdout/custodian_private/
queries:
  word-boundaried flag forms:
    *_have_derived_bridge
    *_bridge_derived
    *_relation_derived
    *_map_derived
    *_identified
    *_equals_*_derived
    *_consistent_with_*
  prose forms:
    "appears in the equation"
    "enters the"
    "is required by"
    "cannot be written without"
    "is built from"
    "carries the"
    "feeds into"
    "is an input to"
    "is fixed by"
    "is derived from"
    "depends on"
    "upstream of"
    "gated by"
```

Raw extraction returned 200 relation-shaped flag hits and 1400 prose phrase
hits. Most prose hits are candidate evidence, not edges: e.g. a sentence can
say "requires" without naming a direction-bearing object pair. Following Q-69,
flags are not identified with the objects that discharge them.

## 1. Lead Result

No enlarged-graph construction cycle was found.

The graph is nevertheless materially larger than Q-64's `would-build` graph.
Q-64 recorded 122 stated edges over 172 nodes. The current extraction adds a
conservative lower bound of 41 direction-bearing edges that Q-64 could not
use:

```text
Q-64 stated construction edges:                         122
new package-internal direction-bearing edges:           39
new scale-to-response bridge edges:                       2
enlarged lower-bound construction/bridge edge count:    163
missing share of enlarged lower-bound graph:          25.2%
missing share relative to Q-64's original count:       33.6%
```

The exact total over all prose candidates is `NO_VERDICT`: Q-64's complete
machine-readable edge manifest is not committed as a standalone edge list, and
the 1400 prose hits include many non-edge sentences. The 163 count above is a
direction-bearing lower bound only.

Q-64's parallelism claim is therefore unsafe. With prose and flag edges
included, the Hamilton-Jacobi scale bridge and the response-extraction path
are connected by a named missing bridge:

```text
T_R --[missing derived bridge]--> k_R
k_R --[appears in the equation fixing]--> K_*
```

The response-extraction path remains:

```text
Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE
```

and Codex 2's package artifacts now expose a named internal graph under that
package. The scheduling fact changes from "two disjoint paths can proceed in
parallel" to "three bridges exist, and one connects the scale side to the
equation fixing `K_*`."

## 2. Flag-Stated Edges

### 2.1 Scale-to-response bridge

| Edge | Status | Evidence |
|---|---:|---|
| `T_R -> k_R` via `T_R_and_k_R_have_derived_bridge` | MISSING-AND-REQUIRED, TYPE-U | `supervision/EXECUTION_TRACKER.md:78`: `T_R_and_k_R_have_derived_bridge = false | TYPE-U` (same-line type added here; source line is pre-typed); `supervision/QUESTIONS_SETTLED_REGISTER_V001.md:3012-3014`: "`T_R` is what `C_R = 1` would select on the scale side (issue 1); `k_R` is the floor appearing in the `K_*` equation (issue 2); the bridge between them does not exist." |

This edge is the Q-73 counterexample. It is not a value computation. It is a
missing relation stated by a flag and by prose.

### 2.2 Response-extraction flags

| Edge | Status | Evidence |
|---|---:|---|
| `raw_correlator -> retarded_Hessian` via `raw_correlator_to_retarded_Hessian_map_derived` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:16`: the flag is `false | TYPE-U` and would build "one completed gauge-fixed physical CTP bilocal-source package..." |
| `raw_correlator -> retarded_Hessian` via same flag | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:1093`: `raw_correlator_to_retarded_Hessian_map_derived = false | TYPE-U | would-build: Section 5 from CTP_PHYS_INPUT_PACKAGE...` |
| `CTP_PHYS_INPUT_PACKAGE -> P1..P8` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:1094`: `CTP_PHYS_INPUT_PACKAGE_derived = false | TYPE-U | would-build: P1-P8 in Section 0` |

These are response-layer edges. They do not specify `CTP_PHYS_INPUT_PACKAGE`;
they record that the map consumes it.

### 2.3 Hamilton-Jacobi scale-bridge flags

| Edge | Status | Evidence |
|---|---:|---|
| `relative_marker -> complete_stationary_Hamiltonian_action` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:57,89`: `relative_marker_equals_complete_stationary_Hamiltonian_action_derived = false | TYPE-U` |
| `record_energy -> total_gravitating_energy` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:158`: `record_energy_equals_total_gravitating_energy_derived = false | TYPE-U` |
| `record_energy -> total_gravitating_energy` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_BRIDGE_ITEM2_COMPLETE_CTP_ACTION_BOUNDARY_TIMEFLOW_SPEC_V001.md:218`: `record_energy_equals_total_gravitating_energy_derived = false | TYPE-U` |
| `record_energy -> total_gravitating_energy` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_BRIDGE_ITEM3_CONSTANT_HJ_RECORD_ENERGY_SPEC_V001.md:212`: `record_energy_equals_total_gravitating_energy_derived = false | TYPE-U` |

These edges stay on the Hamilton-Jacobi scale side. They do not by themselves
touch the response path; Q-73's `T_R -> k_R` bridge is what makes the contact.

### 2.4 Other relation flags found

These flags are relation-shaped and direction-bearing, but are not load-bearing
for the three-chain question in Paste 172:

| Edge | Status | Evidence |
|---|---:|---|
| `complete_parent -> outgoing_GNS` | MISSING-AND-REQUIRED, TYPE-U | `workspace/R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md:159`: `complete_parent_to_outgoing_GNS_map_derived = false` (typed here as TYPE-U because the line is pre-Q-54 and names a missing map) |
| `actual_finite_parent_operator -> scalar` | MISSING-AND-REQUIRED, TYPE-U | `workspace/STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md:508`: `actual_finite_parent_operator_to_scalar_bridge_derived = false` (typed here as TYPE-U) |
| `orientation_blind_B_plus -> B_minus` | MISSING-AND-REQUIRED, TYPE-U | `workspace/BID_CHARGED_CELLULAR_CPT_INTERTWINER_DERIVATION_V001.md:293`: `orientation_blind_B_plus_equals_B_minus_derived = false` (typed here as TYPE-U) |
| `primitive_mass_relation_m_star_T_R -> pi` | PRESENT | `workspace/BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md:171`: `primitive_mass_relation_m_star_T_R_equals_pi_derived = true`; no value inference is drawn here |

## 3. Prose-Stated Edges

Every line below is used as evidence because it literally states an edge or a
dependency surface. Paraphrases are not used as evidence.

### 3.1 `k_R` enters the equation fixing `K_*`

| Edge | Evidence |
|---|---|
| `k_R -> K_*` | `workspace/STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:66-67`: "The closure residual is built from an action carrying the `A_4` log, so `k_R` -- the floor -- appears in the equation that fixes `K_*`." |
| `k_R -> K_*` | `supervision/RESULT_FFL1_SMALL_S_END_2026-07-30.md:100-101`: "The closure residual is built from an action carrying the `A_4` log, so `k_R` -- the floor -- appears in the equation that fixes `K_*`." |
| `k_R -> K_*` | `supervision/QUESTIONS_SETTLED_REGISTER_V001.md:3008-3009`: "residual is built from an action carrying the `A_4` logarithm, **\"so `k_R` -- the floor -- appears in the equation that fixes `K_*`.\"**" |
| `k_R -> K_*` | `supervision/EXECUTION_TRACKER.md:86-88`: "`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:64-67`: the closure residual is built from an action carrying the `A_4` logarithm, **\"so `k_R` -- the floor -- appears in the equation that fixes `K_*`.\"** ... the connector is named and absent: `T_R_and_k_R_have_derived_bridge = false`." The quoted absent connector is typed here as TYPE-U. |

This is the prose edge Q-64 could not see.

### 3.2 Gamma_K response-extraction surface

| Edge | Evidence |
|---|---|
| `Gamma_K/C_record(K) -> response-extraction objects` | `workspace/STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:119-122`: "FOUR OBJECTS SIT UPSTREAM OF Gamma_K / C_record(K): the complete BR/CTP fluctuation-response operator; the exact induced kernel; the raw-correlator-to-retarded-Hessian map G -> H_R[G]; and the covariant local projector." |
| `Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE` | `workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM3_P_ROW_DEPTH_AND_DERIVED_FLOOR_AUDIT_V001.md:247`: `Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE` |
| `Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE` | `supervision/EXECUTION_TRACKER.md:76`: `RESPONSE-EXTRACTION LAYER      package -> map -> Gamma_K; gives C_record(K) a function` |

These lines are not B0 specifications. They are response-layer dependency
statements.

### 3.3 Package internal edge surface from Codex 2 output

The package lane output is covered for edges only. The package artifact states
the strict exact-ID core manifest:

`workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM4_INTERNAL_CONSTRUCTION_CYCLE_CHECK_V001.md:195-215`
states these direct mandatory-prerequisite rows:

| Target | Mandatory prerequisites |
|---|---|
| `CTP_PHYS_INPUT_PACKAGE` | `P1,P2,P3,P4,P5,P6,P7,P8` |
| `CTP_PHYS_INPUT_PACKAGE` | `B0,C0,U1,U2,U3,item 1,D1,D2,D3,D4,D5` |
| `P4` | `P1,P2,P3` |
| `C0` | `B0` |
| `U1` | `B0,C0` |
| `U2` | `B0,C0` |
| `U3` | `B0,C0` |
| `item 1` | `B0,C0,U1,U2,U3` |
| `D1` | `item 1,U3` |
| `D2` | `D1` |
| `D3` | `D1,D2,U2,U3` |
| `D4` | `D1,D2,U3` |
| `D5` | `D2,D3,D4` |

The same package lane states the lower-bound path at
`workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_ITEM3_P_ROW_DEPTH_AND_DERIVED_FLOOR_AUDIT_V001.md:217-247`:

```text
CTP_PHYS_INPUT_PACKAGE
  -> D5
  -> D3
  -> D2
  -> D1
  -> item 1
  -> U3
  -> C0
  -> B0
```

This artifact does not classify B0 and does not specify B0's internals.

## 4. Do The Three Chains Still Separate?

No. On Q-64's `would-build` edges, the Hamilton-Jacobi scale bridge and the
response-extraction layer shared zero nodes. With the literal prose and flag
edges included, that separation no longer holds.

The extracted connection is:

```text
Hamilton-Jacobi scale side:
  C_R = 1 would select T_R on the scale side

missing connector:
  T_R_and_k_R_have_derived_bridge = false | TYPE-U

response equation side:
  k_R appears in the equation that fixes K_*
  Gamma_K -> raw-correlator map -> CTP_PHYS_INPUT_PACKAGE
```

Evidence for the chain-connection statement is
`supervision/QUESTIONS_SETTLED_REGISTER_V001.md:3012-3018`, which states:

```text
`T_R` is what `C_R = 1` would select on the scale side (issue 1);
`k_R` is the floor appearing in the `K_*` equation (issue 2);
the bridge between them does not exist.
...
there are three missing bridges, not two:
(1) the Hamilton-Jacobi scale bridge...
(2) the response-extraction layer...
and (3) the `T_R`-to-`k_R` bridge...
```

Thus Q-64's "two disjoint critical paths" was true only for one syntactic edge
class. It is false as a scheduling claim once prose-stated and flag-stated
dependencies are included.

## 5. Cycle Detection

Cycle test scope:

```text
graph input:
  Q-64 baseline construction graph, reported acyclic over 122 stated edges
  plus the direction-bearing prose/flag edges listed in Sections 2-3
held out by kind:
  test/would-execute edges
  hypothetical alias/merge edges
  flag-to-discharge-object merges forbidden by Q-69
method:
  Tarjan SCC over direction-bearing construction/bridge edges
```

Result:

```text
enlarged_graph_cycle_found = false | TYPE-R | test: Tarjan SCC over the scoped enlarged graph found no SCC of size > 1 and no non-test self-loop
```

The known Q-69 hazards remain held out: a cycle can be manufactured by
identifying a flag with its discharge object, but no such merge is ratified and
this artifact does not perform one.

## 6. Edge Count And Parallelism Consequence

Q-64:

```text
nodes = 172
edges = 122
edge source = stated would-build/release/ordering fields
```

New extraction:

```text
package strict core manifest = 47 direct edges
package edges already visible to Q-64 as P-row prefix = at most 8
new package-internal lower-bound edges = at least 39
scale-to-response bridge edges = 2
new lower-bound edges not in Q-64 = at least 41
enlarged lower-bound edge count = at least 163
exact enlarged edge count = NO_VERDICT | prerequisite: committed machine-readable Q-64 edge list plus an adjudication rule for the remaining prose candidates
```

Was 122 a serious undercount? Yes. At least one quarter of the enlarged
lower-bound graph was missing, and the missing part includes the scheduling
edge that invalidates the "parallel critical paths" claim.

Parallelism claims suspect under this extraction:

1. Q-64's statement that the bridge side and response side share zero nodes on
   stated edges remains true only for `would-build` syntax, not for the sealed
   corpus as dependency text.
2. Q-64's scheduling conclusion that the two paths can proceed in parallel is
   not supported after Q-73.
3. Any plan treating the Hamilton-Jacobi scale bridge, response-extraction
   layer, and `T_R -> k_R` bridge as independent workstreams is unsafe unless
   it explicitly scopes "independent" to the old `would-build` graph.

## 7. Typed Negatives

```text
enlarged_graph_cycle_found = false | TYPE-R | test: Tarjan SCC over scoped direction-bearing construction/bridge edges; test/would-execute edges and Q-69-prohibited flag/discharge merges held out by kind
exact_enlarged_edge_count_computed = NO_VERDICT | prerequisite: committed machine-readable Q-64 edge table and principal/lane rule for whether each remaining prose candidate is direction-bearing
three_chains_still_separate = false | TYPE-R | test: extracted Q-73 flag/prose bridge connects T_R to k_R and k_R to K_*
B0_specified_here = false | TYPE-C | constraint: Paste 172 off-limits to CODEX 1; release: Codex 2/principal path, not this artifact
boundary_leaf_classification_performed = false | TYPE-C | constraint: Einstein owns relay 169; release: Einstein/principal path, not this artifact
custodian_private_opened = false | terminal fence declaration
```

## 8. Discipline

Extraction only. No edge was inferred from physical expectation. Candidate
sentences without two direction-bearing named objects were not added to the
cycle graph. No flag was merged with the object that would discharge it. No
object was adopted, retired, reposed, specified, or constructed.
