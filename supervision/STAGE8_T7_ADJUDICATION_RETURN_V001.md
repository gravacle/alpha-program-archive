# Stage-8 T7 Independent Adjudication Return v001
Fable lane → Codex (via Brian) · 2026-07-24 · serving STAGE8_T7_BLOCKER_RETURN_TO_FABLE_V001.md
Executed in fresh contexts (two adjudication lanes + one theory lane), read-only, no construction artifact edited.

## Verdict

```
CONFIRM_T7_BLOCKED
```

## 1. Verification (request items 1–2)

All six listed hashes recomputed and match; the seal file verifies
(shasum -c, 4/4 OK); T07.json's content address verifies exactly
(recomputed digest equals the claimed field). Beyond the request: all nine
authority pins inside T07.json's audit block recomputed and match, and the
two extra hashes in the superseded audit resolve to unmodified files. The
local verifier passes 11/11 in isolated mode.

The B_lambda witness was rebuilt from scratch in exact integer/Fraction
arithmetic (no construction code reused): identical vacuum and one-record
restrictions for lambda = 0, 1; only the diagonal two-record element
differs (0 vs 1); characteristic polynomials x⁴−x² = x²(x−1)(x+1) and
x⁴−x³−x²+x = x(x−1)²(x+1) confirmed coefficient-by-coefficient via exact
Faddeev–LeVerrier. The witness is genuine.

## 2. No refuting theorem exists (request item 3)

Corpus-wide scans (all md + json, both text-form and JSON colon-form flag
spellings — the latter closing a gap in the construction lane's own
corpus_closure_scan): ZERO true-valued occurrences of
volume_uniform_zero_free_neighborhood_proved,
connected_linked_cluster_density_proved, or
thermodynamic_log_hessian_authorized. Phrase-level sweeps (zero-free,
linked-cluster, cluster expansion, analyticity, thermodynamic density,
volume-uniform, Hessian equality, Kotecky/Dobrushin/Mayer/Kirkwood) find
only obligations and conditionals. Named-file checks: the Stage-7 candidate
V002 discloses the in-state and finite propagator only (and rule 5 excludes
those from counting); the superconnection parent result keeps all four
continuum flags false; monoidal extensivity's Theorem 1 is disjoint-only
(the part T7 rightly credits as PASS) and its Theorem 3 is explicitly
conditional — it IS the obligation, not its discharge.

## 3. The missing derivation, precisely (request item 4)

For the derived one-cell amplitude Z_h and its Duhamel generator, no sealed
theorem supplies: (ii) a volume-uniform zero-free neighborhood of A = 0
containing the response point, uniform in the exhausting cell set;
(iii) an absolutely convergent connected linked-cluster/cumulant density
gamma(A) = lim Γ_K/N₄(K) on the declared causally-sequential cellulations,
certified on a domain containing τ_R; (iv) the equality of the declared
Duhamel covariance with the intensive Hessian of gamma — correctly
NOT_EXECUTABLE until (ii)/(iii) exist.

## 4. Target-free repair specification (the conditional deliverable)

Item-by-item adjudication of what the EXISTING adopted stack supplies
(global-boundary-descent parent + sealed superconnection parent + PSC +
CISP + the Stage-7 disclosed in-state + record axioms):

| Item | Status | Basis |
|---|---|---|
| Connected preparation | **YES_DERIVABLE — no new premise** | see below |
| Local connected generator | **YES_DERIVABLE** | quasifree lift uniqueness (sealed) on the declared exhaustion |
| Zero-free domain at τ_R | PLAUSIBLE_WITH_WORK | the single genuine math item (with iii) |
| Linked-cluster density | PLAUSIBLE_WITH_WORK | same work item |
| Duhamel–Hessian intertwiner | PLAUSIBLE_WITH_WORK | follows once (ii)/(iii) exist |

**The key finding — the B_lambda freedom lives OUTSIDE the adopted class.**
Within the adopted primitive class (operator-valued number-preserving
quasifree CAR lifts of one-particle superconnections, vacuum-normalized),
the vacuum and one-source compressions FORCE every higher-source block —
verified numerically in this lane: the two-source diagonal block equals
b₀₀+b₁₁ with zero residual freedom. The witness's λ|11⟩⟨11| term is a
primitive record-only/overlap kernel, excluded VERBATIM by the parent
principle's "no independent primitive higher-CAR, record-only, contact, or
overlap kernel" clause — exactly parallel to the already-sealed rejection
of the quartic H_λ competitor. So the witness proves underdetermination for
GENERIC extensions, and simultaneously the adopted class proves rigidity:
disjoint data DO fix the connected matrix elements inside the class. This
converts B_lambda from a blocker into the mandatory rejected competitor of
a rigidity theorem.

State side: the finite-stage preparation ω_prep = ω₀ ⊗ (⊗_c |r_c⟩⟨r_c|) is
forced by the disclosed stationary quasifree in-state (already a sealed
disclosure, not a new premise), the record axioms + CISP (no incidence has
acted → ready states), purity of every record marginal (all-pure marginals
admit only the product joint), and PSC's no-separate-selection rule.

Closure side: the linear closure is forced — consistent with, and by the
same anchors as, the closure-selection derivation spec now executing
(reduction to the pinned complex one-handle amplitude; FS identity;
holonomy sensitivity). Predicted verdict there:
RESPONSE_CLOSURE_SELECTION_DERIVED.

**Proposed repair gate** — `STAGE8_T7_CONNECTED_RESPONSE_REPAIR_GATE_SPEC_V001`
(construction lane forward-seals, verbatim or minimally adapted):
- O1: class-rigidity theorem (higher-block forcing inside the adopted
  class; B_lambda as mandatory rejected competitor, NC-R1).
- O2: preparation derivation (disclosed state ⊗ ready records, forced as
  above; alternative preparations rejected via PSC, NC-R2).
- O3: closure inheritance from the closure-selection derivation gate
  (no re-derivation; hash-pin its result when sealed).
- O4/L1: THE mathematical work item — volume-uniform zero-free neighborhood
  + absolutely convergent linked-cluster density on the declared class,
  attacked first on the finite-buffer Huygens-exact subclass (where the
  expansion truncates and both statements should follow cleanly), then the
  maximal declared class; then the Duhamel–Hessian equality (NC-R3: a
  deliberately non-clustering exhaustion must fail).
- T7 stays BLOCKED until O4 lands; no kappa_record evaluation, no
  downstream charged-CTP work meanwhile.

**Contingency premise (held in reserve, NOT adopted):**
BUFFERED_EXHAUSTION_CLUSTERING_PRINCIPLE — invoked ONLY on a sealed
O4-failure verdict; narrows the admissible exhaustion class to buffers
growing at the minimal provably-summable rate (rate DERIVED, never fitted);
six falsifiers drafted (inequivalent densities across buffered exhaustions;
cofinality failure; empty class; KP bound still failing; any buffer-rate
dependence of the response; target access). Per the return document's rule:
named, classified, forward-sealed, independent consequence before use.

## Honoring the request's constraints
No principle adopted post-failure; the disclosed in-state and finite
propagator were NOT counted as linked-cluster/zero-free theorems (rule 5);
the complete charged CTP amplitude stays downstream (rule 6); no
construction artifact was edited; no target value accessed.
