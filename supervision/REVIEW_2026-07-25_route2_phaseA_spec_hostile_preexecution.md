# Hostile Pre-Execution Review — Route-2 Artifacts + Phase-A Spec
Claude construction/supervision lane · 2026-07-25 · fresh-context subagent return (verbatim below)
Scope: STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001,
STAGE8_ROUTE2_CAR_STATE_BRIDGE_SCOPE_CORRECTION_V001,
STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001 — reviewed against
the four approved Route-2 conditions and custody-note Sections 5/6.
This closes the item flagged in CONTINUATION_STATE as "NOT yet reviewed against the
four conditions — FIRST TASK for the successor supervision function."

Companion lane (implementation/O6-refactor hostile re-review) launched separately;
its return will be recorded in its own file.

---

VERDICT: READY_WITH_CONDITIONS

FINDINGS:
1. CONDITION — Phase-A spec (STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md), whole document vs custody note Section 6 — the spec nowhere binds its own production execution to the custody note's prerequisites ("Bind production inputs to canonical sealed paths and independently issued execution receipts", "Establish the generator-to-propagator lineage", "Obtain hostile review of the refactored Route-2-to-O6 production compression", implementation manifest sealed before production). An executor honoring only the sealed spec text could run production while custody blockers 1–4 are open and the implementation seal is, by the custody note's own Section 4, absent. Exploit: a caller-selected self-consistent bundle can still manufacture a local PASS exactly as blocker 1 describes. Repair (append-only): a one-page pre-execution gate note pinning Phase-A production behind custody Section 6 items 1–3 plus a sealed, externally anchored implementation manifest.
2. CONDITION — Phase-A spec, A6, "E_conn(ell) = max { d_24_48(all), ... }" — the history pair for every E_conn component is unpinned. d_12_24/d_24_48 were defined per history pair; S_conn is pinned to (7/100,-11/100), but E_conn's four elements are not. An executor can evaluate E_conn components at whichever pair minimizes them, easing the S_conn > 20 E_conn non-vacuity gate (or at the other pair to force a block). This is a discretionary choice surviving sealing on a preregistered gate. Repair (append-only): pin all E_conn components to the same pair (7/100,-11/100).
3. CONDITION — Phase-A spec, A6, "The independent lane executes first, while the future primary output paths are absent from its read allowlist" — the ordering is asserted but has no proof mechanism: no commit-reveal against an external anchor, no independently issued receipt, no third party attesting lane order. Post hoc, a gamed run (primary first, independent bundle crafted after) is indistinguishable from a compliant run. Same root cause as finding 1; repair folds into the receipts requirement.
4. NOTE — Phase-A spec, A5, "require equality to the independently propagated direct response" — within either lane this check is near-tautological: H_direct is exactly block-diagonalized by the (t-independent) spectral resolution of c, so any linear one-step integrator produces direct-vs-Gaussian-sum agreement to roundoff regardless of whether h_0, M, or B_D are correct. Its evidential content is limited to spectral-resolution/Kraus-coefficient bookkeeping; the real burden is carried by the cross-lane Strang-vs-RK4 comparison. Spec's own framing ("same-carrier one-source restriction") is honest; record the limitation so the 3e-9 residual is not cited as physics evidence.
5. NOTE — Phase-A spec, A6, "For both ell values and every frozen history pair verify: R_all^(1)(a,a)=I" — only (0,0) is a frozen pair, so the set of same-history checks is ambiguous (the five frozen a values are the natural set). Repair: pin the check set in the successor.
6. NOTE — Phase-A spec, A5 — the snapshot Route-1 re-execution is compared to the frozen closed-form comparator formulas at 1e-10 (a fixed analytic target; the moving-target attack probed does not exist), but it is never value-compared to the canonical sealed result (6dbda44a..., which matched at ~4e-16). Silent drift up to ~2e-10 against the sealed values is tolerated. Add an explicit value-comparison sentence in the successor.
7. NOTE — Phase-A spec, A6, "S_conn(ell) > 20 E_conn(ell)" — no sealed prior evidence that the doubly-exponentially narrow b_D bump at |a| <= 13/100 yields connection response exceeding 20x the sealed n=2 tail scale (measured baseline tails 1.06e-5 to 1.16e-4). A correct implementation may BLOCK here. That is fail-closed and frozen ("the multiplier 20 may not be revised in this version"), so it is discipline-consistent, but a BLOCK on this gate should be read as a preregistered sensitivity failure, not an implementation error.
8. NOTE — Phase-A spec, A6, "may not be revised in this version" implicitly licenses a successor to revise the multiplier after seeing a failure; supersession review must require the retained failure to be disclosed in any such successor.
9. NOTE — Phase-A spec, A1, "spinor dimension=32" mislabels the total one-particle dimension (8 spatial x 4 spinor); harmless but sloppy typing in a type-discipline program (the baseline JSON uses the same field name, so it is an inherited convention).
10. NOTE — Phase-A spec, A6, the "independent overlap quadrature" for S is unpinned (rule/order unspecified); benign because n=2 Hermite-product overlaps are exactly integrable by any adequate Gauss rule, the 2e-11 unitarity residual bounds it, and the independent source is sealed before either lane runs.

CONDITION_CHECK:
1. State pinned by hash: SATISFIED — STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md (5cbcd28e..., verified) pins omega_in; Phase-A spec pins both finite covariance schemes (235246ab..., a79939ad..., both verified) and applies neither ("neither covariance is applied during Phase A").
2. Operator response sealed before downstream use: SATISFIED at spec level — A4 requires every matrix as a content-addressed artifact in the result seal; A7 forbids Phase B recomputing/replacing/selecting the response after seeing either scalar; actual enforcement is pending the custody-note receipt infrastructure (finding 1).
3. Route 1 retained as frozen consistency falsifier: SATISFIED — A5 mandates unchanged re-execution against the O6 closed forms at the two frozen pairs with 1e-10, canonical result hash 6dbda44a... pinned and pre/post-verified; binding 460e8752... verified.
4. Every amendment append-only: SATISFIED — all three artifacts are new files; every previously sealed file they narrow or cite recomputes to its recorded hash (amendment 8a7f52ff..., scope correction 4e1282bc..., all unchanged); the correction narrows by supersession (renamed flag abstract_complete_Qspec_CTP_scalar_closure_derived), not by edit.

HASH_CHECK: PASS — all 19 entries of the Phase-A spec's Frozen authorities table, all 7 of the amendment's, and all 5 of the scope correction's recompute exactly (shasum -a 256); the Phase-A spec itself matches both its adjacent seal and the custody note's pinned 789338ad...; the canonical Route-1 result stage8_execution/work/T07_primitive_operator_response_v001.json recomputes to 6dbda44a0f21a28b57f114654a6df79fc091ccfd601c38518fd5cf5f21697dcc matching its adjacent seal; custody note matches its adjacent seal (d8b587a1...). No mismatch.

MATH_CHECK:
- R_all Gaussian sum: CORRECT — rederived; cross terms (mu != lambda) cancel at operator level via P_mu P_lambda = delta P_lambda (spectral projectors of Hermitian c), equivalently sum_x <ready|P_mu|x><x|P_lambda|ready> = <ready|P_mu P_lambda|ready> = delta_{mu,lambda} p_lambda; uses Gamma(u)^dagger Gamma(v) = Gamma(u^dagger v), valid for the number-preserving lift; all cross operators u_mu^dagger u_lambda are unitary, so each Gamma is legitimate.
- R_pointer double sum: CORRECT — cross terms properly retained with w_mu^* w_lambda.
- Record data: CORRECT — c matches the sealed parent's c_c = i Gamma_c b_c exactly; c^2 = diag-block{[[1,-1],[-1,1]],2} gives eigenvalues {0, +/-sqrt(2)}; rederived p = (1/2, 1/4, 1/4) and w = (1/2, -1/4, -1/4), matching the sealed pointer weights (w_-,w_0,w_+)=(-1/4,1/2,-1/4).
- b_D: CORRECT — s = 1/16 at (1/2,0) so exp(16-16)=1 confirmed; C-infinity zero extension valid (exp(-1/s) argument); the "0<t<1 and s_->0 and s_+>0" clause correctly excludes both the spurious both-factors-negative region and the t<0 / t>1 quadratic branches — the drafting survived this attack.
- v(t) = (pi/sqrt(2))*32*r(t)^3: VERIFIED, not unmotivated — equals tau_R * w(t) where w(s)=32 min(s,1-s)^3 is the sealed parent's normalized time marginal of the uniform diamond 4-volume measure ((4/3)pi r^3 / (pi/24) = 32 r^3; integral_0^1 w = 1 verified in exact rationals); integrated write action tau_R = pi/sqrt(2) consistent with the Route-1 O7 value.
- A6 identities: CORRECT — R_all^(1)(a,a)=I (convex sum of u^dagger u), adjoint exchange, norm <= 1 (convex combination of unitaries), 0 <= R_pointer^(1)(a,a) <= I (single Kraus member of a channel with unital Kraus sum).
- Route-1 closed form [1+exp(i(theta_+ - theta_-))]/2: rederived, CORRECT.
- Thresholds: internally consistent — ratio floor 3.2 vs asymptotic 4 for second order (measured baseline ratios ~3.85); quarter-tolerance tail rule 7.5e-5 sits orders above expected RK4-192/384 tails; 3e-4 sits above the sealed n=2 tail maximum 1.16e-4 as claimed; S_conn > 20 E_conn is well-posed at E_conn = 0 (pure multiplication, no 0/0; the d_24_48 <= 1e-15 guard separately blocks the unresolved-tail case) but carries the over-tight risk of finding 7 and the pair ambiguity of finding 2.
- Measured-constant fence: CLEAN — the only regex hits for the forbidden digit patterns in all three artifacts are hex substrings inside SHA-256 strings; the frozen values {0, 7/100, -11/100, 13/100, 4/100}, their differences and products, and every threshold were checked against the forbidden constant and its elementary transforms; no encoding found.

BLOCKER_MAP:
1. Caller-selected bundle PASS: OPEN_UNADDRESSED — sealed-allowlist and lane-ordering language mitigates on paper, but canonical input binding and independently issued receipts are absent from the spec and, per the custody note itself, "not yet complete".
2. Generator-to-propagator lineage: OPEN_UNADDRESSED — partially mitigated in design (independent lane regenerates propagators from parent operators at every displayed RK4 stage, no midpoint cache), but the comparator still consumes path/hash-selected bundles with no lineage proof.
3. Route-2-to-O6 refactor hostile re-review: OPEN_UNADDRESSED — none of the three artifacts mentions it; the A5 falsifier's value depends on that refactor genuinely routing the comparator through shared production compression, which is exactly what remains unreviewed.
4. Implementation manifest / signature / external anchor: OPEN_UNADDRESSED — custody Section 4 confirms absent; Phase-A spec requires only the runtime manifest.
5. Runtime provenance narrower than content-addressed host: OPEN_UNADDRESSED — same disclosed boundary, inherited unchanged; not worsened.

---

## Disposition by the construction lane (recorded, not yet executed)

- Verdict accepted: READY_WITH_CONDITIONS. No execution until all three CONDITIONS
  are discharged append-only.
- Findings 1+3 route to the pre-execution gate note (production bound behind custody
  Section-6 items 1–3, sealed implementation manifest with external anchor, and
  independently issued execution receipts). The inherited draft controller implements
  much of this design; it remains gated on the implementation review lane's verdict.
- Finding 2 (E_conn pair pinning), finding 5 (same-history check set), and finding 6
  (Route-1 canonical value comparison) route to one append-only Phase-A execution
  binding successor, sealed BEFORE execution, none outcome-based.
- Findings 4, 7, 8, 9, 10 recorded as standing interpretive notes; finding 7 in
  particular: an S_conn BLOCK is a preregistered sensitivity failure, honestly
  reportable, not an implementation defect.
