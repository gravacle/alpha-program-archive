# Stage 8 Bridge Item 0 Alias Precondition v001

CODEX 1 artifact for Paste 167, Item 0.

Status: ALIAS ADJUDICATION ONLY. No bridge object is derived or adopted here.

Register head at issue: Q-64.

Fences: no computation or evaluation of alpha, `kappa_record`,
`kappa_Thomson`, a coupling, a radius, a scale, a root, an eigenvalue, a beta
function, `E_R`, `T_R`, or any absolute interval was performed. No measured
constant comparison was performed. `a32_holdout/custodian_private/` was not
opened. Codex 2 and Einstein live-item artifacts were not opened.

## Question

Do these two identifiers name the same bridge obligation?

```text
C_R_marginal_selector_derived_rather_than_adopted
marginal_closure_condition_derived_rather_than_assumed
```

Paste 167 notes that both occur in the same file, both are TYPE-C, and no
sealed equation had merged them.

## Search Scope

```text
roots:
  /Users/bgm/MB Work/alpha-program-archive/workspace
  /Users/bgm/MB Work/alpha_supervision
exclusions:
  /a32_holdout/custodian_private/
  Codex 2 live CTP_PHYS_INPUT_PACKAGE artifacts
  Einstein live relay artifacts beyond the Q-64 register row
queries:
  exact fixed-string C_R_marginal_selector_derived_rather_than_adopted
  exact fixed-string marginal_closure_condition_derived_rather_than_assumed
  exact fixed-string C_R_equals_1_truth_status
  word-boundaried marginal public-closure / marginal closure / first durable
```

Exact hits:

- `C_R_marginal_selector_derived_rather_than_adopted` occurs in
  `STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:58` and the Paste 167
  relay text.
- `marginal_closure_condition_derived_rather_than_assumed` occurs in
  `STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:169`, the Q-64 census
  artifact, and the Paste 167 relay text.
- `C_R_equals_1_truth_status` occurs in
  `STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:54`, the Q-64 census
  artifact, and the Paste 167 relay text.

The Q-64 census artifact was not opened; the Q-64 register row was read.

## Source Text

`STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:54-59` records:

```text
C_R_equals_1_truth_status = NO_VERDICT
blocked_by:
  absolute_record_interval_derived_in_declared_branch = false | TYPE-U
  relative_marker_equals_complete_stationary_Hamiltonian_action_derived = false | TYPE-U
  C_R_marginal_selector_derived_rather_than_adopted = false | TYPE-C
```

The same artifact later expands the missing objects. At
`STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:169-173`:

```text
marginal_closure_condition_derived_rather_than_assumed = false | TYPE-C
constraint: `C_R = 1` is currently an adopted Level-1 marginal public-closure rule.
release: target-independent complete source-record-gravity action derives first durable/public
         closure at the marginal boundary without receiving marginality as an input.
source: BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-67;
```

`BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-60` identifies the
adopted rule itself: the allow/require boundary is the first physically
admissible public record cell; the least positive interval is attained at the
recoverable-set boundary `C_R = 1`; this fourth input is the selector.

`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:169-185` gives the
complete closure list and includes "derives, rather than assumes, the marginal
closure condition" as item 6.

## Determination

The alias resolves.

```text
alias_resolved = true
alias_type = SAME_OBLIGATION_DIFFERENT_LABEL
derivation_status_changed = false
```

Reason: the compact `blocked_by` label at
`STAGE8_C_R_SELECTOR_NONSELECTION_DIAGNOSIS_V001.md:58` says the `C_R`
marginal selector is not derived and remains blocked by adoption. The later
entry at `:169-173` states the same constraint and gives the release condition:
derive the first durable/public closure at the marginal boundary without
receiving marginality as an input. Both point to the same adopted Level-1
public-closure rule in `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-67`.

This is an alias resolution only. It does not make the condition derived.

## Released Node

For graph purposes the following two identifiers should be treated as one
node:

```text
marginal_closure_condition_derived_rather_than_assumed
```

with aliases:

```text
C_R_marginal_selector_derived_rather_than_adopted
```

Current typed status:

```text
marginal_closure_condition_derived_rather_than_assumed = false | TYPE-C
constraint: C_R = 1 is currently an adopted Level-1 marginal public-closure rule
release: target-independent complete source-record-gravity action derives
         first durable/public closure at the marginal boundary without
         receiving marginality as an input
```

## Negative Typing

```text
sealed_equation_merging_aliases_found = false | TYPE-S
roots: /Users/bgm/MB Work/alpha-program-archive/workspace;
       /Users/bgm/MB Work/alpha_supervision
query: exact fixed-string forms of both identifiers plus C_R_equals_1_truth_status
finding: no formal alias equation was found; the alias is resolved by local
         expansion and shared source text, not by a pre-existing alias table
```

## Terminal Status

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
