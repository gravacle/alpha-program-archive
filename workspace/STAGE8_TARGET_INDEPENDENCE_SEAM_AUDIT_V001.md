# CODEX 2 — Q-? Target-independence seam audit

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false; coupling_evaluation_authorized = false; production_authorized = false.`

## Determination

The corpus does **not** fix whether “target-independent” means input-blindness or specification-blindness.
The seam therefore remains open. Existing anti-fit language is stronger than mere no-target-input in some
places, but no corpus-wide definition or release condition makes that stronger reading uniformly binding.

## Scope and queries

Roots: historical full program, current cleanroom, and `/Users/bgm/MB Work/alpha_supervision`. Excluded
`.git`, dependencies, `external`, `third_party`, `node_modules`, `.proof_deps`, and `a32_holdout` (including
`custodian_private`, never read or listed). Review packets were discovery-only. Word-boundaried/exact queries:
`target-independent`, `target_blind`, `target_independence`, `target-dependent`, `historical_target_blindness`,
`admitted family`, `narrowing`, `after seeing the root`, `K_(1,3)`, and
`first_opening_accounting_gate_passed`.

No definition was found that states both the admissible inputs and the target-independent specification
selection rule. The uses are assertions or flags, not a common glossary or release test.

`target_independence_definition_found = false | TYPE-S | scope/query: this section; no corpus-wide definition
or release condition.`

## Load-bearing uses

Section 5.3 says uniqueness is invalid if obtained “only by narrowing the admitted family after seeing the
root” (`STAGE8_SECTION_5_3_UNIQUENESS_GATE_PASSABILITY_DETERMINATION_V001.md:105-110`; the broader audit is
at `:79-95`). This clearly constrains specification choice, not merely numerical inputs. Yet the same
artifact records the admitted family is not the whole allowance envelope and that the action-form slice is
not enumerated (`:79-95`). Thus the anti-fit defense survives only under the specifications reading; under
inputs-only it still permits preselected, target-aware family design.

Other uses (“target-independent operator/principle”) establish no common stronger test; they can satisfy the
weaker inputs reading while leaving class selection and gate authorship untested.

`Section_5_3_under_specifications_reading = NO_VERDICT | TYPE-U | deciding evidence: frozen family census and
pre-root specification provenance.`
`Section_5_3_under_inputs_only = false | TYPE-R | test: its own after-root narrowing clause is violated by
an inputs-only interpretation.`

## K_(1,3) premise

The rooted-star premise fixes the minimal first-opening complex as `K_(1,r)` with `r=3`, and therefore fixes
the stated dimensions (`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:260-263`). It is explicitly described
as a target-aware postulate consequence, not a new prediction. Its downstream gate
`first_opening_accounting_gate_passed = false` is recorded at `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:2317`.

Target-awareness here is specification-level: the premise designates the admitted sub-object and thereby
fixes its dimensions and first-opening inventory. The road consumes that designation through the first-opening
accounting and subsequent gate chain; no legitimacy ruling is made here.

`K_(1,3)_target_aware_specification = true | TYPE-C | evidence: V011:260-263.`
`K_(1,3)_gate_passed = false | TYPE-U | would-build: execute the first-opening accounting gate.`

## Exposure and non-repair conclusion

The weakest reading (inputs-only) permits a construction to avoid numerical target input while still choosing
the admitted class, object designation, and gate form with target knowledge. Under the stronger specifications
reading, the existing anti-fit clause is directionally sound but not presently executable because the corpus
does not freeze the family census or provenance. This is an unresolved seam, not a new category.

No repair or definition was introduced. No git, commit, push, gate, or deploy action was performed.
