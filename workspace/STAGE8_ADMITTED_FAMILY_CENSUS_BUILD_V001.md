# CODEX 2 — Admitted-family census build (pre-freeze)

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

This is a constructed **candidate manifest**, not a census freeze. All newly written members are marked
`derived = false` and are structural schemas only.

## Class 1 — higher-derivative source terms

Generating schema (candidate):

```text
S_HD[n,c] = ∫ d^4x sqrt(-g) c_n O_n[J, A, record],   n >= 2,
```

where `O_n` is a local covariant source/record operator of derivative order `n` and `c_n` its coefficient.
Ordering parameter: derivative order `n` (mass dimension is not fixed by the corpus). Leading candidate
members are `O_2 = (∇F)^2` and `O_4 = (∇²F)^2`, with the displayed forms treated as **CHOICES**, not corpus
derivations. Domains, codomains, embeddings, provenance, adoption time, and target-awareness declarations
are MISSING. Mutation relation: candidate action-partition alternatives.

No response-changing bound is supplied. Therefore:

`higher_derivative_response_changing_bound = NO_VERDICT | TYPE-U | would-build: a pre-root equivalence theorem
or finite derivative-order cutoff proving which O_n alter the response.`

## Class 2 — finite causal updates

The corpus supplies no closed finite list. Candidate schemas (not derived members) are:

* `U_Δ^ret`: retarded update on `J^-(x) ∩ [t,t+Δ]`, mapping source history to record state.
* `U_Δ^loc`: local causal update on the past light cone, mapping the same source record to the next cell.

Their exact domains/codomains, source/record embeddings, provenance, branch choices, and target-awareness are
MISSING. The word “finite” alone does not prove closure or cardinality.

`finite_causal_update_closed = false | TYPE-U | would-build: enumerate every admissible update rule and prove
closure under the sealed causal equivalence relation.`

## Class 3 — record-curvature and dissipative mutations

Candidate record-curvature operator (derived = false, hypothetical):

```text
O_curv[ρ] = ∫_cell sqrt(h) R_record[h] ρ,
```

Candidate dissipative operator (derived = false, hypothetical):

```text
O_diss[ρ] = ∫_cell dt dt' ρ(t) K_ret(t,t') ρ(t'),
```

Both have missing domains, codomains, embeddings, provenance, adoption time, and target-awareness. The
curvature branch is held out by **adoption** (`TYPE-C` branch exclusion), not derivation. Dissipation is held
out by the unitary phase-protection premise unless a unitary dilation/complete carrier is derived; that is a
premise exclusion, not a derived no-go.

## Controls: S₀ and S₁

Independent control re-derivation: `S_0` and `S_1` are the two displayed parameter-free parent-action
completions in `STAGE8_ACTION_FORM_UNDERDETERMINATION_INVENTORY_V001.md:90-159`. They are response-changing
action-partition alternatives and therefore admitted mutation candidates. Their exact domains, embeddings,
complete provenance, adoption timestamps, and target-awareness declarations remain MISSING.

## Coverage position

Useful status is: class 2 **open, not proven finite**; class 1 **bounded-not-listed only by this schema, with
no response-changing bound**; class 3 **open and partly held out by adoption/premise**. The manifest is not
complete and is not frozen. A separate coverage proof over all envelope axes and an adversarial omitted-member
countermodel are required before freezing.

`admitted_family_census_frozen = false | TYPE-C | constraint: coverage proof and independent countermodel absent.`
`manifest_completeness = NO_VERDICT | TYPE-U | would-build: independent all-axis coverage audit.`

No root or response effect was evaluated. No git, commit, push, gate, or deploy action was performed.
