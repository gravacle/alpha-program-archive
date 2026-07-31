# CODEX 2 — Stage-10 geometric matching layer scope

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## Layer definition

The sealed Stage-10 brief names a causal-diamond/skeleton-to-cell embedding whose purpose is to normalize
the public response and select the `E_ref` branch (`45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:34-45`). It
consumes the causal diamond, canonical `K_(1,3)` skeleton, cellulation/boundary conditions, and a public
transverse response; it produces a derived matching relation selecting `E_*` or `mu` as the reference rate.
The exact map is **not specified**: the brief gives work items and discipline requirements, not a typed
domain/codomain or matching equation.

## Ingredients

| Ingredient | Status |
|---|---|
| causal-diamond geometry | **SEALED/DERIVED**: shape and volume are recorded in the Stage-10 brief (`:34-39`) |
| skeleton/cellulation | **ADOPTED/DERIVED conventions**: `K_(1,3)` and three-axis embedding are named (`:40-45`), but the physical embedding map is absent |
| response being normalized | **ABSENT** as a completed Stage-10 public transverse response; the separate BR/CTP response object is not identical (comparison audit) |
| Ward/causal test | **ABSENT** as an executed Stage-10 test; only discipline requirements are listed (`:26-33`) |
| pre-frozen predictions | **ADOPTED REQUIREMENT**: predictions and hashes must be frozen before computation (`:26-33`), but no prediction package exists |
| matching condition | **ABSENT**: “Thomson/matching selects E_ref” is named, not typed as a map or regime equation (`21_DIMENSIONLESS_RATIO_RESULT_V001.md:20-39`) |

## Existing output sweep

The `alpha-program-archive/cleanroom_output/` directory was searched separately (including its 87 files and
sidecars). Results 21, 26, and 45 exist and are sealed, but they are reports/specifications: result 21
reduces continuous freedom to the E_ref fork; result 26 leaves the fork open; brief 45 scopes Stage 10. None
constructs the geometric matching map or selects E_ref.

`stage10_matching_map_derived = false | TYPE-S | scope: cleanroom_output plus workspace and program roots;
query: Stage-10, E_ref, matching, causal diamond, skeleton embedding.`

## Minimal sufficient increment

The smallest sufficient build is not the whole Stage-10 program: it is a **pre-frozen, typed geometric
matching functional** on the causal-diamond cell and embedded `K_(1,3)` skeleton, with both candidate
normalizations evaluated symbolically (without choosing), a Ward/causal support test, and a derivation rule
that proves one candidate is forced. It must specify its domain/codomain, source/record embeddings, regime,
and prediction hash before either branch is evaluated. If this increment cannot be supplied, the full Stage-10
response/matching stage remains the blocker.

`E_ref_deciding_increment_present = false | TYPE-U | would-build: typed pre-root matching functional and
failure-capable Ward/causal tests.`
`E_ref_fork_resolved = false | TYPE-C | constraint: fork must be derived, never chosen.`

No matching was built or evaluated. No git, commit, push, gate, or deploy action was performed.
