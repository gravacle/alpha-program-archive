# 19 — Cycle 4 Specification: Is the Dimensionless Coupling Ratio Structural? v001

Frozen before execution. The question from OUTPUT/18: in the full package —
not the minimal model — is the dimensionless combination
**ρ = c · g_N²/(h_s · E_ref)** structural, where c = 1/4 is the cycle-3
coefficient and (g_N, h_s, E_ref) must be identified with sealed package
quantities?

## Anti-numerology guardrails (binding on every step)

- G1: identification candidates for each slot may be drawn ONLY from sealed
  or package-stated relations, each with file citation. No quantity may be
  invented, rescaled, or combined beyond its sealed form.
- G2: ALL candidate combinations are computed. None may be selected,
  preferred, dropped, or highlighted for its numerical value. The output is
  the full table.
- G3: NO comparison of any output to any measured constant. Stage 12
  remains unauthorized. `alpha_computed = false` regardless of outcome.
- G4: if any slot admits two or more sealed candidates with no in-package
  selector, the honest verdict is a DISCRETE SURVIVING FAMILY —
  BLOCKED-at-identification with the family exhibited. A unique number may
  be claimed only if every slot is uniquely forced by citation.
- G5: the enumeration is performed by a fresh-context lane reading only the
  workspace, so that no prior hand-assembly biases the candidate list.

## Sealed predictions

- **P1 (T_R-cancellation).** Every sealed rate/scale in the package is
  relational in the single free interval (m_*·T_R = π; E_*·T_R = πħ;
  holonomy phases dimensionless). Therefore each identification of
  (g_N, h_s, E_ref) scales as 1/T_R and **ρ is T_R-independent**: the
  continuous Families A/C do NOT infect the dimensionless ratio. If any
  candidate combination retains T_R dependence, that combination is
  malformed and must be reported (not repaired).
- **P2 (finite discreteness).** The candidate set per slot is finite and
  small (sealed candidates include, without prejudice: the unit-flux
  holonomy phase π/2; the action marker πħ; the FS budget πħ/2; the mass
  relation π; the Schur factor √2; the orthogonality interval π/√2). The
  assembly therefore yields a finite set of pure numbers.
- **P3 (expected honest outcome).** At least one slot will admit ≥ 2 sealed
  candidates with no in-package selector (e.g., E_ref as E_* vs m_* vs μ),
  so the expected verdict is a discrete surviving family — the reduction of
  a continuous freedom to a finite identification fork, not a unique
  number. If instead every slot is forced, the unique ρ is reported with
  its citation chain and no comparison.

## Method

1. Fresh-context enumeration lane: for each slot (g_N = phase-type
   source-to-record coupling rate; h_s = mediator/source gap scale;
   E_ref = reference record rate), list every sealed package quantity that
   could occupy it, with verbatim citation and the reason it qualifies —
   and equally, any reason it fails to qualify. No arithmetic.
2. Assembly script (this run): compute ρ for the full Cartesian product of
   candidates in exact symbolic form (fractions and powers of π, √2);
   verify P1 T_R-cancellation symbolically; output the complete table.
3. Result document: verdict per G4; family exhibited if discrete fork
   survives; every number carried with its full citation chain.

## Failure conditions

- F1: enumeration lane finds a slot with NO qualifying sealed candidate —
  the identification map does not close; report (the interface is not yet
  connected to the package's sealed layer).
- F2: any guardrail violation voids the cycle; no post-hoc repair.
