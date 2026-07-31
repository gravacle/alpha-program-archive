# Stage 8 JSON Authority Ledger Sweep v001

CODEX 1 artifact for Paste 170.

Register head at issue: Q-70.

Status: SWEEP / COMPARISON ONLY. No ledger is amended, merged, retired,
adopted, or repaired here.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No computation or evaluation of alpha, `kappa_record`, `kappa_Thomson`, a
coupling, a radius, a scale, a root, an eigenvalue, a beta function, `E_R`,
`T_R`, or any absolute interval was performed. No measured constant comparison
was performed. `a32_holdout/custodian_private/` was not opened.

## Scope

Roots searched:

```text
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Exclusions:

```text
/a32_holdout/custodian_private/
Codex 2 live CTP_PHYS_INPUT_PACKAGE internals and B0
Einstein live boundary axiom/debt classification
```

Queries and methods:

```text
find ... -name '*.json' with custodian_private pruned
fixed-string CURRENT_AUTHORITY_LEDGER_V*.json
word-boundaried/key-level scan for: derived, proved, excluded, selected,
  PASS, authorized, computed, sealed, adopted, rejected, superseded
JSON structural parse of all 13 ledger files
exact markdown assignment scan for whole flag names:
  flag = true/false or flag: true/false
dependency-key scan for parent_authority, current_authority,
  subordinate_result_bindings, superseded/rejected, blocked_by, would-build,
  prerequisite, requires
```

Negative scope note:

```text
ledger_contradiction_found = false | TYPE-S
roots: /Users/bgm/MB Work/alpha-program-archive/workspace;
       /Users/bgm/MB Work/alpha_supervision
exclusions: /a32_holdout/custodian_private/; live Codex 2 B0/package internals;
            Einstein boundary axiom/debt classification
query: exact CURRENT_AUTHORITY_LEDGER_V001..V013 JSON structural parse plus
       exact whole-flag markdown assignment scan
```

## 1. The Thirteen

The count is verified: exactly 13 uppercase JSON authority ledgers matching
`CURRENT_AUTHORITY_LEDGER_V*.json` exist in the archive workspace.

The lower-case `results/current_authority_*` JSON files are result payloads,
not the thirteen named authority ledgers. They were not counted as ledgers.

| # | Path | Lines | SHA-256 | Claims authority over |
|---|---:|---:|---|---|
| V001 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V001.json` | 24 | `e9345f6860b439696aa3e129bdb8fe5c5f8faccc0d7ade7973cc82fe2f1a0cf0` | sealed pre-alpha authority; 3 current results; 2 superseded results; 5 execution flags |
| V002 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V002.json` | 29 | `7fc4f8eef53119ed58de8cd58175ded61e206ae80140897ecd93c00ed3d9025d` | sealed pre-alpha authority; 4 current results; 3 superseded results; 8 execution flags |
| V003 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V003.json` | 43 | `5cccc5587027e3686652c818081eb5e8076a88d2645d0038ddc61d39a22995eb` | sealed pre-alpha authority; 4 current derived results; 3 Level-1 postulates; 1 conditional lemma; 5 superseded/retired results; 12 execution flags |
| V004 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V004.json` | 47 | `59f5e3f38f74df5f4c88674ffef19b7a9ef122e3a03c3706919b104bba4df8b7` | sealed pre-alpha authority; 5 current derived results; 2 Level-1 postulates; 2 conditional/diagnostic items; 6 superseded/retired results; 14 execution flags |
| V005 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V005.json` | 49 | `2b57caf33945314f4d4809f184309fd340470c42abf5d28bfe198f49fdf2b755` | sealed pre-alpha authority; 6 current derived results; 2 Level-1 postulates; 2 conditional/diagnostic items; 7 superseded/retired results; 14 execution flags |
| V006 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V006.json` | 68 | `00b801eac0ecc24e77d88c52c2a53a3c116ad9e6c18869d311c30271c315e462` | sealed pre-alpha authority; 10 current derived results; 2 Level-1 postulates; 2 external route audits; 4 conditional/diagnostic items; 8 superseded/retired results; 22 execution flags |
| V007 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V007.json` | 73 | `066617aaec3b6a5d23480bba9cfbafe6719688c98ed5d1d643451672059c54d5` | sealed pre-alpha authority; 10 current derived results; 2 Level-1 postulates; 3 external route audits; 5 conditional/diagnostic items; 10 superseded/retired results; 23 execution flags |
| V008 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V008.json` | 81 | `2baf60337ea5bb6c896344e73c03a75935b3cfb38043b3f0304553fcc17ef1bc` | sealed pre-alpha authority; 10 current derived results; 3 Level-1 postulates; 3 external route audits; 5 conditional/diagnostic items; 11 superseded/retired results; 29 execution flags |
| V009 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V009.json` | 84 | `8897888cc7b7b64cd5f3c442d0f878e14a68d38b548a3ad32d877ae56806a22b` | sealed pre-alpha authority; 11 current derived results; 3 Level-1 postulates; 3 external route audits; 7 conditional/diagnostic items; 14 superseded/retired results; 26 execution flags |
| V010 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V010.json` | 122 | `5c6c09064d5d4e58ead79108498655891890ea95d1a3cb8350b04f4f8d34b7cc` | sealed pre-alpha authority; 15 current derived results; 4 Level-1 postulates; 3 external route audits; 7 conditional/diagnostic items; 20 superseded/retired results; 53 execution flags |
| V011 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V011.json` | 61 | `21f4bbd41c71b3ab060dd07820d1d2a8e0b1eb56d79b23e042feae85676eb12b` | parent authority from V010; 4 new sealed results; 2 new Level-1 postulates; 6 superseded/rejected items since V010; 18 execution additions; 8 protected parent flags |
| V012 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V012.json` | 61 | `f25091c2c7909e2b659fb7191365623b12de2371c4b19514b37f357ca00c048a` | same shape as V011; later rejected by V013 |
| V013 | `/Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V013.json` | 77 | `6a8c14b12c69c113e4ef0d8a9741d5ffbe481aabf7938f4bb9bf595798060a8c` | current authority tuple; parent authority from V010; 4 new sealed results; 4 subordinate result bindings; 2 new Level-1 postulates; 10 superseded/rejected items since V010; 18 execution additions; 8 protected parent flags |

Count finding:

```text
json_authority_ledger_count = 13
json_authority_ledger_count_matches_Q66_escalation = true
```

## 2. What They Assert

The ledgers assert four different kinds of things. These must not be merged.

### A. Current derived-result authority

V003 through V010 contain `current_derived_results`. V010 is the largest parent
authority set and lists 15 entries at
`CURRENT_AUTHORITY_LEDGER_V010.json:8-23`, including:

```text
primitive_record_carrier
ordered_endpoint_projective_stabilizer
microscopic_exhaustion_scope
public_charged_action_nonselection
complete_one_cell_ctp_kernel_gate
bcc_parent_candidate_gate
complete_parent_action_underdetermination_gate
source_record_mass_transfer_gate
source_record_chiral_operator_gate
source_record_chiral_operator_result
source_record_closure_magnitude_nonderivation_gate
source_record_closure_magnitude_nonderivation_result
coupled_record_bundle_modulus_gate
absolute_stiffness_route_ledger
finite_cell_response_protocol
```

Typing note: `current_derived_results` is a result-artifact authority section.
It does not by itself assert that the object named inside the result is
positively derived. Example: V010 lists
`complete_parent_action_underdetermination_gate` as a current derived result
artifact while V010 also records
`complete_parent_action_uniquely_derived = false` at line 106. Treating the
section name as the object's discharge would violate Q-69's flag/object fence.

### B. Level-1 postulates

V003 through V013 carry Level-1 postulate sections. V010 lists four at
`CURRENT_AUTHORITY_LEDGER_V010.json:25-29`:

```text
fundamental_boundary_record_action_principle
primitive_vectorlike_source_branch
transport_only_phase_complete_generator_principle
source_record_odd_component_identification_principle
```

V013 adds two new Level-1 postulates at
`CURRENT_AUTHORITY_LEDGER_V013.json:31-33`:

```text
relative_record_onset_saturation
zero_flux_no_charged_write
```

These are plainly axiom/postulate-shaped leaves, but Einstein owns the
boundary axiom/debt classification under relay 169. This sweep records their
presence only.

### C. Conditional or diagnostic-only authority

V004 through V010 carry conditional/diagnostic-only sections. V010 lists seven
at `CURRENT_AUTHORITY_LEDGER_V010.json:36-43` and explicitly fences several
objects away from physical-connection or selector status.

This section adds authority information that markdown-only graph sweeps can
miss, but it is not a construction dependency section.

### D. Execution state flags

Across the 13 ledgers there are 284 boolean flags:

| Ledger | Bool flags | True | False | `_derived=true` | `_derived=false` | `authorized=true` | `computed=true` |
|---|---:|---:|---:|---:|---:|---:|---:|
| V001 | 5 | 0 | 5 | 0 | 1 | 0 | 0 |
| V002 | 8 | 1 | 7 | 1 | 3 | 0 | 0 |
| V003 | 12 | 4 | 8 | 1 | 3 | 0 | 0 |
| V004 | 14 | 4 | 10 | 1 | 3 | 0 | 0 |
| V005 | 14 | 4 | 10 | 2 | 3 | 0 | 0 |
| V006 | 22 | 7 | 15 | 3 | 5 | 0 | 0 |
| V007 | 23 | 7 | 16 | 3 | 6 | 0 | 0 |
| V008 | 29 | 9 | 20 | 3 | 6 | 0 | 0 |
| V009 | 26 | 9 | 17 | 2 | 8 | 0 | 0 |
| V010 | 53 | 20 | 33 | 3 | 16 | 0 | 0 |
| V011 | 26 | 5 | 21 | 1 | 13 | 0 | 0 |
| V012 | 26 | 5 | 21 | 1 | 13 | 0 | 0 |
| V013 | 26 | 5 | 21 | 1 | 13 | 0 | 0 |

Protected flags are consistently false. V013 records at
`CURRENT_AUTHORITY_LEDGER_V013.json:67-75`:

```text
complete_source_record_closure_action_uniquely_derived = false
record_generated_source_mass_derived = false
complete_parameter_free_Q_spec_frozen = false
unique_causal_record_cell_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```

## 3. Contradictions Against Markdown Rulings

No substantive contradiction was found in the scoped comparison.

The exact whole-flag markdown assignment scan produced 29 raw
contradiction-candidates. All were rejected as false positives in one of three
classes:

1. Guard or negative-test payloads that intentionally mention forbidden
   `alpha_computed=true` / `proof_authorized=true` mutations.
2. Sentences saying no artifact carries a protected true flag.
3. Hypothetical "would refute if an artifact set X=true" rows.

The one substantive-looking family was the mutation/finiteness class. It is
not a contradiction. V008-V010 distinguish:

```text
finite_c_F2_deformation_excluded_inside_adopted_primitive_branch = true
finite_c_F2_deformation_excluded_as_universal_theorem = false
```

V010 carries that pair at `CURRENT_AUTHORITY_LEDGER_V010.json:115-116`. This
matches the sealed V011-style distinction that primitive F2/Pauli exclusions
are axiomatically disallowed inside the adopted branch but not theorem-excluded
as universal statements.

V012 is not treated as active authority. V013 explicitly rejects V012 and its
audit/test/result chain at `CURRENT_AUTHORITY_LEDGER_V013.json:42-45`:

```text
CURRENT_AUTHORITY_LEDGER_V012.json =
  REJECTED_INCOMPLETE_PARENT_SEMANTIC_FREEZE_AND_UNBOUND_SUBORDINATE_RESULTS
scripts/audit_current_authority_v012.py =
  REJECTED_PARENT_DRIFT_HARDLINK_ALIAS_AND_SNAPSHOT_GAPS
tests/test_current_authority_v012.py =
  SUPERSEDED_INCOMPLETE_ADVERSARIAL_COVERAGE
results/current_authority_v012.json =
  REJECTED_RESULT_OF_UNSEALED_FAILED_V012_AUTHORITY
```

Contradiction finding:

```text
substantive_json_vs_markdown_contradiction_found = false | TYPE-S
roots: /Users/bgm/MB Work/alpha-program-archive/workspace;
       /Users/bgm/MB Work/alpha_supervision
query: exact whole-flag assignment scan over all ledger boolean keys, followed
       by manual classification of opposite markdown hits
finding: no ledger flag was found to assert derived/proved/PASS/authorized
         where a current scoped markdown ruling asserts the opposite
```

This is a scoped negative, not a principal adjudication of precedence.

## 4. Nodes And Edges Added To The Dependency Graph

The ledgers add authority/provenance nodes and edges. They do not add
construction `would-build` dependency edges of the kind Q-64 used.

Ledger edge types found:

```text
current_authority -> ledger/audit/test/result
parent_authority -> ledger/audit/test/result/seals
new_sealed_results -> artifact paths
subordinate_result_bindings -> result JSON paths
new_level_1_postulates -> artifact paths
superseded_or_rejected_since_v010 -> rejected/superseded artifact paths
superseded_or_retired_results -> superseded/retired artifact paths
external_target_independent_route_audits -> external audit paths
conditional_or_diagnostic_only -> fenced artifact paths
```

Scope for the following negative: roots are the 13
`CURRENT_AUTHORITY_LEDGER_V001.json` through
`CURRENT_AUTHORITY_LEDGER_V013.json` files listed above; query is a JSON
key/value scan for the exact construction-dependency markers below.

Construction dependency keys not found in that scoped scan:

```text
blocked_by
would-build
would_build
prerequisite
requires
depends_on
```

Typed graph finding:

```text
ledger_construction_dependency_edge_found = false | TYPE-S
roots: /Users/bgm/MB Work/alpha-program-archive/workspace/CURRENT_AUTHORITY_LEDGER_V001.json
       through CURRENT_AUTHORITY_LEDGER_V013.json
query: JSON key/value scan for construction-dependency markers
finding: the ledgers add authority/supersession/result-binding edges, not
         construction dependency edges
```

Cycle finding:

```text
ledger_construction_cycle_found = false | TYPE-S
roots: the 13 JSON authority ledgers
query: construction-dependency edge scan
finding: no construction dependency edge was found, so no construction cycle
         can be formed from these ledgers alone
```

Authority-graph note: V013 points to V010 as parent authority and rejects V012.
That is an authority lineage edge, not a construction dependency. Q-64's
construction graph is incomplete if the intended graph includes authority
lineage, but no evidence here forces a change to the construction DAG.

## 5. Ledger Leaves That Reach Derived Or Axiom Ground

The JSON ledgers do contain derived-looking ground and axiom-looking ground.
This narrows the earlier "no chain reaches derived ground" wording: the
ledgers have local derived flags and derived-result authorities, but this sweep
found no bridge/value-path construction chain terminating in them.

Plain derived-looking leaves include, without claiming they discharge the
current bridge:

```text
pointwise_projective_stabilizer_derived = true
pointwise_active_relative_U1_derived = true
complete_two_outcome_point_comparator_kernel_derived = true
coupled_record_bundle_tree_relation_derived = true
free_mass_shell_relation_for_supplied_background_derived = true
relative_orthogonalization_bound_derived = true
```

The latest active V013 additions include one `_derived=true` flag:

```text
relative_orthogonalization_bound_derived = true
```

at `CURRENT_AUTHORITY_LEDGER_V013.json:55`.

Plain axiom/postulate-looking leaves include the V010 Level-1 postulates at
`CURRENT_AUTHORITY_LEDGER_V010.json:25-29` and the V013 Level-1 postulates at
`CURRENT_AUTHORITY_LEDGER_V013.json:31-33`.

Boundary-classification fence:

```text
boundary_axiom_debt_classification_performed = false | TYPE-C
constraint: Einstein owns the boundary axiom/debt classification under relay 169
release: principal/lane assignment clears that fence
```

## Verdict

```text
json_authority_ledgers_swept = true
json_authority_ledger_count = 13
substantive_json_vs_markdown_contradiction_found = false | TYPE-S
ledger_construction_dependency_edge_found = false | TYPE-S
ledger_construction_cycle_found = false | TYPE-S
ledger_derived_ground_exists_locally = true
ledger_authority_edges_exist = true
dependency_graph_needs_authority-edge_decision = true
```

The program has not been contradicted by the JSON ledgers in this scoped pass.
It has, however, been under-reporting what the JSON layer contains: local
derived flags, Level-1 postulate leaves, V013's rejection of V012, and
authority/result-binding edges that no markdown-only dependency walk can see.
