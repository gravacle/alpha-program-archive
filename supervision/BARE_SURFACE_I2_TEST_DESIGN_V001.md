# BARE-SURFACE TEST DESIGN — I-2 — V001 (2026-08-14)

**Commitment instrument.** This design is sealed and pushed BEFORE the test runs (F2
ordering; the ledger row updates in the same commit). It stages the ledger's protocol
for instinct **I-2** — *the bare surface fixes α's dimensionless value from its own
dimensionless content* — with bearing on I-3, I-5, I-6, I-9. The machinery-reversion
guard is enforced by construction: the forbidden imports are NAMED below; the build
works on bedrock only; `MACHINERY_INVOKED` is a mandatory output; the audit determines
`REVERTED_TO_MACHINERY` explicitly.

## THE QUESTION (posed neutrally; no outcome classification)
Working from the defined surface alone: does the surface's own dimensionless content
DETERMINE a unique dimensionless invariant occupying α's role — with no scale, no
scale-conversion, no Thomson/S16 bridge, no carrier machinery? "Determine" means:
derive fixing conditions on bedrock whose solution is proven to exist and be unique.
The test STOPS at that pre-numeric gate (see FENCE).

## GROUND (all the build may stand on)
1. `SURFACE_DEFINITION_OF_RECORD_V001.md` (seal 20ee87c0d064…), clauses §I–§II taken
   AS the surface of record (it is sealed registrar consolidation of booked, verified
   entries): connection-only, no native metric; continuous fibers over a discrete
   base; unit-modulus holonomy characters z_j^(n) = χ_n(h_j[a_j]), n ∈ {+1,−1},
   U(1) transitions; affine connection space (no fiber metric; a radius is a metric
   datum, not a surface datum); the exact refinement law; phase-rich/amplitude-poor
   (unit-modulus write weights, no amplitude structure); the scale orbit free with
   `absolute_SI_record_duration_derived = false`; every DERIVED junction β-invariant.
2. The booked surface-derived dimensionless locks, as quoted in that document:
   τ_R = π/√2; |ΔS_record| = πℏ (an action — dimensionless in ℏ units); m_* T_R = π;
   the balanced-geodesic identities; the onset bound; the thirteen sealed interface
   quantities' derived/β-invariant statuses.
3. Nothing else. The build does not open the register, road, ledger, lens, plan, or
   tracker files.

## FORBIDDEN IMPORTS (named, per the guard — use of ANY is a reversion)
The Λ^even(C⁵) carrier and all carrier/cellulation machinery; K_KK; the fiber proper
radius R; any metric or fiber metric; ℓ_P; any length/scale object or internal↔external
conversion (β); the S16/Thomson matching bridge, κ_Thomson, and any spacetime
cross-section matching; "α rides an absolute scale" (Q-01) in any form; the imported
KK gravitational action; the Finish-A/Finish-B framing; the E1-successor / Carleman /
S2′ analytic chain and its objects (C, K_n, Δ, ρ); the lens (GR readings, the sphere,
4π-as-the-sphere); any continuum-diamond import; any measured/empirical constant.

## FENCE (absolute)
alpha_computed = false · proof_authorized = false · kappa_record_computed = false.
NO numeric evaluation of any physical constant; NO comparison, explicit or implied,
to any measured value. If a derivation chain terminates in fixing conditions with a
unique solution, the build STOPS at the statement "the invariant is the unique
solution of ⟨derived conditions⟩" — it does NOT solve, display a closed form of, or
evaluate the solution. Any surface-determined value, if one day computed, rides the
SAME fences and the SAME one-shot preregistered end test as the machinery track — no
second peek exists on any branch.

## HONEST OUTCOME MENU (none preferred; all publishable)
- **DETERMINES** — fixing conditions derived on bedrock; existence + uniqueness proven;
  stopped at the pre-numeric gate.
- **DOES-NOT-DETERMINE** — the exact freedom exhibited (e.g., every candidate invariant
  provably rides the free scale orbit, on the surface's own terms).
- **UNDERDETERMINED-AT** — the exact missing surface datum, named.
- **ILL-POSED** — α's role has no surface-native referent; say precisely what referent
  is missing and what would supply it.

## OUTPUTS REQUIRED
Build artifact: `workspace/BARE_SURFACE_I2_DETERMINATION_V001.md` (+ `.seal.sha256`),
with a terminal flag block containing `I2_STATUS`, `MACHINERY_INVOKED = <no | yes: what>`,
`SCALE_TOUCHED = <no | yes: where>`, `VALUE_EVALUATED = no` (mandatory), and a
claim-by-claim DERIVED/CLAIMED/CONDITIONAL marking. Audit artifact:
`workspace/BARE_SURFACE_I2_DETERMINATION_AUDIT_V001.md` (+ sidecar), default-refute,
with `REVERTED_TO_MACHINERY = <no | yes: where>` determined independently, a
defeat-provenance check (a refutation must itself stand on bedrock), and the standard
provenance/injection/fence sections.

## ACCEPTANCE (registrar note — this design covers the TEST, not the acceptance)
Per the ledger: the result logs CLAIMED; I-2 moves only on a reversion-clean test
(`REVERTED_TO_MACHINERY = no`, checked) — and instinct CONFIRMATION additionally
requires the ledger's panel discipline (external axis; provenance-clean dependency
audit; cold re-derivation for a positive). A machinery-reverted result is logged
INCONCLUSIVE (reverted) and settles nothing.
