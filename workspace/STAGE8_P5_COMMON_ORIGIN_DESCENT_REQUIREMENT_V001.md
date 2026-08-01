# CODEX 2 — What P5 needs from the source V001

Date: 2026-08-01. Road role: ATTACKS THE PRIMARY BLOCKER.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## Lead result

**P5 requires a property weaker than full determination of the microscopic source.**

The property is a **P5 COMMON-ORIGIN DESCENT PRESENTATION**: one executable, target-independent descent rule
and provenance certificate must derive the pre-state, admitted record effects, their domains, and the
dynamics-facing compatibility data from the same microscopic construction trace. It must also certify
positivity, normalization, domain invariance, and whatever completeness relation the admitted effect family
claims.

The source need not be uniquely reconstructed in every detail. Distinct microscopic realizations may satisfy
P5 if they descend to isomorphic state/effect/domain/dynamics packages and carry valid common-origin
certificates. What P5 forbids is independently choosing `rho_pre`, effects, or domains after the dynamics is
fixed and merely placing them in the same container.

Nothing sealed currently supplies this presentation as a derived completed-object result. Formal P5 roles,
source-sector GNS data, isolated record effects, and adopted state/contour branches each supply only part of
the interface.

## Scope

Roots entered:

1. current cleanroom root;
2. parent gravity-program root;
3. `/Users/bgm/MB Work/alpha-program-archive/cleanroom_output/`;
4. `/Users/bgm/MB Work/alpha_supervision/`.

Excluded: `.git`, dependency/vendor directories, review packets as primary authority, and all of
`a32_holdout/`; `a32_holdout/custodian_private/` was neither entered nor listed.

Case-insensitive, word-boundaried queries included `P5`, `rho_pre`, `record effect`, `effect domain`, `same
microscopic source`, `common-origin certificate`, `effect descent`, `state effect descent`, `instrument`,
`record-compatible state`, and `P5 certificate`.

## 1. Sealed common-origin requirement

The controlling producer signature states:

> `P5. A positive normalized rho_pre on the completed object and admitted record effects E_r, with domains,
> all supplied by the same microscopic source as P0.`

Source: `STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md:251-253`.

Its failure-capable T4 rejects a candidate when the state, effects, effect domains, and operator domains are
not positive/normalized/compatible on one completed object, or are not supplied by the same microscopic
source as the candidate dynamics (`:343-358`).

The joint-P0 determination fixes the semantic force: P5 requires **derivational** common origin, while the
phrase does not by itself mean that the source temporally creates the antecedent carrier
(`STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md:546-572`). Independently postulated effects fail
the present P5 class; that does not prohibit a different producer class.

## 2. Operational unpacking

Let `Omega` denote a microscopic construction trace or presented source realization. P5 is operationally
satisfied only if there are typed descent maps

```text
d_state(Omega) = rho_pre,
d_effect(Omega,r) = E_r,
d_domain(Omega) = (D_dyn, {D_r}),
d_dynamics(Omega) = U_BR or S_CTP,
```

and one common-origin certificate `Cert_P5(Omega)` establishing all of the following:

1. **Common carrier:** all outputs act on, or are faithfully represented on, the same completed physical
   source-record-field object and quotient.
2. **State properties:** `rho_pre` is positive, trace-class where that formulation applies, and normalized.
3. **Effect properties:** each `E_r` is an admitted positive effect; when the family is declared exhaustive,
   the effects or instruments satisfy the corresponding completeness/trace-preservation relation.
4. **Domain compatibility:** the state, effects, dynamics, contacts, and observables have compatible common
   dense/invariant domains; the dynamics preserves the declared domain.
5. **Dynamic compatibility:** the functional

   ```text
   Tr(E_r U_BR rho_pre U_BR^dagger)
   ```

   and its normalized CTP version are well-defined with the same branch, quotient, and measure conventions.
6. **Covariance and causality:** source/record embeddings, gauge action, Ward rules, and causal/endpoint
   conditions commute with the descent maps.
7. **Provenance:** `rho_pre`, `E_r`, domains, and dynamics share the same primitive inputs and construction
   record; none is imported as an independent post hoc parameter.
8. **Target-independent admissibility:** the state/effect/domain family and its admission criteria are frozen
   before downstream response or root information exists.

The corpus supplies the basic property formulas: `rho_pre` is a positive normalized trace-class state
(`primitive_record_cell_selection_principle_v004.md:17-25`); record effects obey `0 <= E_r <= I`, with
`sum_r E_r=I` only for an exhaustive family (`:81-87`); and the complete-history functional consumes
`E_r`, `U_BR`, and `rho_pre` together
(`primitive_complete_boundary_transition_functional_principle_v002.md:16-29`).

## 3. The named property

The minimal property is:

```text
P5_COMMON_ORIGIN_DESCENT_PRESENTATION
  = (descent maps,
     common-origin construction trace,
     state/effect/domain property certificate,
     dynamics-compatibility certificate,
     target-independent admissibility manifest).
```

For one producer candidate, this is sufficient to make P5 attemptable. To close the **§5.3 P5 mutation
axis**, an additional coverage theorem is required: every admitted target-independent common-origin P5
package must be generated by the manifest, proven response-equivalent to a listed package, or excluded
upstream.

Thus “construct one valid P5 package” and “close every P5 alternative” are distinct verdicts.

## 4. Why full source determination is unnecessary

Let

```text
Q_P5 : Omega -> (rho_pre, {E_r}, domains, dynamics interface, Cert_P5)
```

be the descent map. P5 consumes the image of `Q_P5` and its certificate. It does not require `Q_P5` to be
injective. Two microscopic sources may differ in response-invisible auxiliary structure, off-shell
presentation, or unused sectors while descending to isomorphic P5 packages.

Therefore:

```text
P5_common_origin_descent_implies_full_source_determination = false | TYPE-R |
  test: a non-injective descent map can carry distinct source realizations to one certified P5 package

P5_logically_requires_unique_complete_origin = false | TYPE-R |
  test: P5/T4 inspect descended state/effect/domain/dynamics compatibility, not uniqueness of every source datum
```

This does not reduce common origin to a bare existential assertion. A concrete construction trace and
commuting descent data are required. “Some source exists” or “all fields appear in one file” is insufficient.

## 5. Does sealed text already supply it?

### 5.1 Formal P5 state/effect roles

`primitive_record_cell_selection_principle_v004.md` and
`primitive_complete_boundary_transition_functional_principle_v002.md` type the state, effects, instruments,
and probability/CTP functionals. They consume `rho_pre`, `E_r`, and `U_BR`; they do not derive them from one
microscopic source.

### 5.2 Source-sector GNS

The source quasifree GNS supplies source-sector state/covariance data but does not derive the completed
source-record-field `rho_pre`, effect operators, or effect domains. This dependency was tested in
`STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md:582-600,720-722`.

### 5.3 Record effects and state/contour branches

The inclusive identity effect, schematic `E_r=C_r^dagger C_r`, POVM/instrument rules, and an adopted
stationary quasifree state/contour branch are individually typed in the P5 census. No row supplies completed
domain/codomain, source/record embeddings, target-awareness, mutation relation, and common-origin provenance
together (`STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md:203-290`).

### 5.4 Joint-P0 result

The joint-P0 artifact already distinguishes the common-origin witness from the property certificate and
states that effects/domains must descend rather than be imported
(`STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md:1051-1074`). Its three P5 tests separately check
origin, properties, and preconstruction admissibility (`:1146-1148`). Those are exactly the components of the
presentation named here, but no candidate has executed them.

### Finding

```text
derived_completed_P5_common_origin_descent_presentation_found = false | TYPE-S |
  roots: four roots in Scope |
  query: P5/common-origin/effect-descent/certificate terms above |
  reason: sealed objects type or consume components but no completed artifact supplies all descent maps and certificates

P5_common_origin_descent_presentation_derived = false | TYPE-U |
  would-build: executable descent maps, actual common construction trace, property/dynamics certificates,
  and target-independent admissibility manifest
```

## 6. Relationship to the primary origin blocker

P5 is not logically blocked on **unique full determination** of the source. It is blocked on a smaller
source-facing interface: the certified P5 descent presentation.

However, the current corpus has no independent way to construct that smaller interface. Its named release is
still either:

1. construct a joint P0/P5 producer and execute the P5 tests; or
2. seal an upstream theorem proving uniqueness/equivalence/exclusion across the P5 family
   (`STAGE8_SECTION53_P5_AXIS_COVERAGE_AND_EXCLUSION_AUDIT_V001.md:23-70,187-194`).

Accordingly, the logical dependency is weaker while the current construction dependency remains unresolved:

```text
P5_and_full_origin_are_the_same_object = false | TYPE-R |
  test: P5 is a descended interface/attempt port, not the whole origin object

P5_weaker_interface_buildable_without_full_origin_now = NO_VERDICT |
  deciding evidence: an executable descent presentation constructed without consuming complete P0

P5_buildable_now_from_existing_derived_objects = false | TYPE-C |
  constraint: no completed carrier/common trace/descent maps/property certificate are available
```

## Conclusion

The first opening on P5 is conceptual and concrete: fund the **descent presentation**, not necessarily a
unique reconstruction of the entire microscopic source. It is a smaller deliverable with independently
testable pieces—origin trace, state/effect/domain properties, dynamics compatibility, and pre-root
admissibility. But it is not already built, and a valid single package would still need a separate coverage
theorem before §5.3 could call the complete P5 axis closed.

No object was constructed or evaluated. No root, coupling, scale, eigenvalue, beta function, absolute
interval, or measured comparison was computed. No fork was chosen. No git, commit, push, gate, or deploy
action was performed.
