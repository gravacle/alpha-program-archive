# Stage 8 Rescaling Exclusion Recovery Erratum v002

Date: 2026-07-30

Status: APPEND_ONLY_SUCCESSOR_ERRATUM. This artifact corrects
`STAGE8_RESCALING_EXCLUSION_RECOVERY_ERRATUM_V001.md` without editing V001 in
place. V001 remains sealed as the state of knowledge when it was written. This
successor records Q-14's correction: the requirement was superseded in the
immediate successor version and later lost by citation graph, not silently
deleted without a supersession note.

## Corrected Timeline

Measured mtimes:

```text
2026-07-20 15:10  primitive_record_cell_selection_principle_v001.md
2026-07-20 15:13  primitive_record_cell_selection_principle_v002.md
2026-07-22 22:13  primitive_record_cell_selection_principle_v003.md
2026-07-22 22:58  primitive_record_cell_selection_principle_v004.md
```

Search result over `primitive_record_cell_selection_principle_v001.md` through
`v004.md`: the heading `## Rescaling exclusion` occurs in V001 at line 95 and
does not occur in V002, V3, or V4. Therefore the deletion is at V002, not at
"the v003 edit." V004 is also missing the heading.

## Supersession Note Exists

`primitive_record_cell_selection_principle_v002.md:3-16` is headed
`## Correction to v001` and states:

```text
Version 001 was externally sealed before numerical work and is retained as an
audit record. Its explicit rearrangement

    K_R = 4 (Phi_* - Gamma_rest,*) / I_F,*

is valid only if the selected field configuration and the action partition are
already independent of `K_R`. A coupled matter-electromagnetic-gravitational
saddle need not have that property. Version 002 therefore replaces the direct
division rule with a joint saddle-and-closure selection problem. No numerical
cell or alpha value was evaluated between the two versions.
```

The provenance preregistration restates the correction. In
`provenance/primitive_record_cell_selection_preregistration_v002.json:4-5`:

```text
"supersedes": "primitive_record_cell_selection_v001 before numerical cell construction",
"correction": "The field configuration may depend on K. The protocol now requires a joint solution of the complete coupling-indexed saddle and durable-record closure equation rather than a post-saddle division formula."
```

Therefore the V001 sentence
`v001_rescaling_exclusion_dropped_silently_relative_to_working_set = true`
is restated as:

```text
v001_rescaling_exclusion_lost_by_citation_graph_relative_to_working_set = true
v001_rescaling_exclusion_dropped_without_supersession_note = false
deletion_version = v002
v004_checked_and_heading_absent = true
```

## Live Requirement

The requirement survives in V002 as a blocking rule. At
`primitive_record_cell_selection_principle_v002.md:124-133`, the construction
blocks if, among other things:

```text
changing an admitted boundary condition, measure, regulator, or action
partition changes `K_*` without a theory-derived exclusion;
```

The live preregistered construction list is five-channel, not four-channel. At
`provenance/primitive_record_cell_selection_preregistration_v002.json:15-23`,
the required construction includes:

```text
one complete microscopic Gamma_K functional and measure
derived BR boundary conditions and operator domains
the K-indexed stationary cell X_K including its proper duration
the public closure operator and spectrum on X_K
a derived scalar closure residual C_record(K)
a unique simple positive root K_star
a mutation audit over admitted geometry, clock, measure, regulator, and action-partition alternatives
```

## Field-Energy Integral Retyped

The field-energy integral survives as an implementation identity, not as a live
selector channel. `primitive_record_cell_selection_principle_v002.md:111-122`
states:

```text
d Gamma_K[X_K] / dK
  = (1/4) integral_(Omega_K) sqrt(|g_K|) F_K^2 d^4x.
```

and then:

```text
This identity checks the implementation. It does not select `K_*`; the
durable-record closure equation must do that.
```

Thus the V001 erratum's channel list is corrected from clock/source/measure/
field-energy/cell/action variants to the live V002 list:

```text
geometry
clock
measure
regulator
action-partition
```

## Sequencing Correction

`results/primitive_record_cell_joint_selector_readiness_v001.json:31-37` lists
five failed authorization checks:

```text
complete_joint_operator_is_present
joint_operator_derives_stationary_proper_interval
joint_operator_derives_closure_residual
joint_operator_proves_unique_simple_positive_root
joint_operator_passes_mutation_audit
```

The same result states at lines 54-60 that the next gate is to derive one
complete target-independent `Gamma_K` and BR closure operator whose joint
stationary problem outputs `Delta_tau(K)` and scalar `C_record(K)`, and lists
the missing `Gamma_K` functional/measure, stationary interval, closure spectrum,
closure residual, and unique positive root.

Therefore the mutation audit is an acceptance check on an unbuilt operator, not
the next executable construction by itself.

## Protected Status

```text
v001_preserved = true
v002_successor_erratum = true
deletion_at_v002_not_v003 = true
v004_checked_heading_absent = true
supersession_note_exists = true
citation_graph_loss_not_unrecorded_deletion = true
live_channels = ["geometry", "clock", "measure", "regulator", "action-partition"]
field_energy_integral_live_selector_channel = false
mutation_audit_executable_before_Gamma_K_and_C_record = false
alpha_computed = false
kappa_record_computed = false
proof_authorized = false
```
