# Supervision review — blind-lane results: transport gate, durability gate, and the transport-rule derivability question
Date: 2026-07-24 (afternoon) · Reviewer: Fable lane (3 rebuild lanes + 1 theory lane + 1 durability lane, all fresh-context)

## 1. Transport gate (CAUSAL_TRANSPORT_CONDITIONAL): qualitative claims CONFIRMED; digits not reproducible — spec underdetermines the regulator

Three independent blind lanes rebuilt the gate from spec text. All three
agree with each other and with every qualitative claim in the sealed result:

- Static sum destroys the endpoint: all lanes get **0.307114** (three
  constructions, 9-digit mutual agreement); Codex reported 0.306222.
- Transported parent restores the endpoint **exactly** (probability 1;
  Codex 0.9999999999999982).
- Finite-support Møller operator is an **exact identity** (two lanes prove
  U(T,0)=U_0(T)exp(−iB_c∫v) analytically; interaction-picture generator
  self-commutes at unequal times).
- Profile independence exact across square/sin²/triangle/ramp envelopes.
- Uniqueness given the rule: two-line proof (set t=0 in the functional
  equation; group law gives existence). Certified by all lanes.
- Second-order slicing convergence (ratio 4 per doubling); causal order
  load-bearing.

**Why digits differ from Codex:** the spec pins no regulator size, cell
location, boundary condition, or spin-carrier dimension. The lanes measured
the sensitivity precisely: commutator norm is 4√6 (interior cell, 4-dim γ⁵),
4√5 (boundary cell), 4√3/2√10 (2-dim carrier variants) vs Codex's 2√30;
static probability shifts 0.3071→0.3127 interior→boundary. Every mutual
lane agreement at 0.307114 used an interior/ring cell. **Finding (minor,
process):** sealed specs that want digit-exact reproducibility must pin the
regulator (the Møller and Lorentzian gates did — and those reproduced
digit-for-digit). Substance of the sealed verdict unaffected.

## 2. Durability gate (…DURABILITY_DERIVED): CONFIRMED, two notes

Independent 27-dim rebuild (spin factor proven immaterial, both chiral
signs, max Δ=3.2e-14): persistence is exact (later cell and free evolution
never move record 0, to the 1e-12/1e-15 integrator floor), Møller unitary,
causal-order sensitivity **4.8061 matching Codex's 4.806**, reversal exactly
mirrors the path reflection e0↔e2 (a nice check Codex didn't state), clean
second-order convergence, RK4 cross-check to ~1e-12.

- **Note 1 (numeric):** natural in-state gives 0.806674786 (Richardson +
  RK4 agree to 1e-12) vs Codex's 0.806674023 — a 7.6e-7 offset that looks
  like unconverged midpoint slicing in the producer value (their stability
  error 2.7e-14 measures persistence at fixed discretization, not absolute
  accuracy). Harmless here because no downstream claim uses the digits —
  but worth a verify-script upgrade before anything ever consumes them.
- **Note 2 (process):** the in-state is underdetermined by the spec;
  candidates give 0.81 / 0.41 / 0.49 / 0. The durability/Møller/order
  conclusions are candidate-independent (checked all four).

## 3. Transport-rule derivability: **PLAUSIBLY_DERIVABLE_WITH_WORK — no third adoption needed yet**

The theory lane's verdict, with two short derivation routes, each one
unpinned lemma from closing:

- **Route R1 (strongest — derives equivariance):** CISP makes the write a
  cell-supported envelope; PSC's exhaustion clause attaches only the
  intrinsic cell measure (the integrated action ∫v) as parent data — the
  within-cell profile is a regulator representative (Lemma L1); PSC's
  no-separate-selection list forbids outgoing data depending on "a cutoff
  or regulator weight" (Lemma L2, direct reading of pinned text); then a
  delta-concentration argument forces B̃(t)=U_0(t)B_cU_0(t)* uniquely, no
  relative coefficient. Gap: pin L1 against the upstream measure result.
- **Route R2:** if exhaustion inclusions act on stabilized interiors as the
  free advance (Lemma L3 — natural but not literally pinned), the
  functional equation follows and its uniqueness is already certified.
- **Sharp bookkeeping correction:** CISP's own text ("the incidence is an
  event, not a permanent Hamiltonian term" + falsifier 1) already rejects
  the PERMANENT static sum — the gate's static_sum_rejected=false is
  over-cautious for that variant. The genuinely surviving competitor is the
  ENVELOPED static join H_0+v_c(t)B_c, which CISP alone does not kill; what
  kills it is its profile-DEPENDENCE at fixed ∫v, which under R1 is a PSC
  violation. The mandatory negative control should be upgraded to the
  enveloped static join.
- **Rival exclusion complete:** five third-attachment alternatives all fall
  (full-flow transport violates CISP's later-cell/earlier-record falsifier
  in the multi-cell case — with the single-cell free-vs-full equivalence
  worth recording as a robustness lemma; anti-comoving violates
  future-directedness; dressed K(t) is either forbidden selection or an
  already-reserved descendant obligation; rescalings hit no-relative-
  coefficient).
- **Recommended next move:** a derivation spec
  (R3_4_WRITE_JOIN_ATTACHMENT_DERIVATION_V001) that pins L1, proves the
  delta-concentration theorem, runs R2 as an independent check, upgrades
  the negative control, and on success reissues the gate as V002 with
  causal_transport_rule_derived_from_pinned_principles=true. Adoption of a
  narrow "Causal Attachment Covariance" principle (falsifier list F1–F7
  drafted) only if both lemmas resist derivation.

## 4. Threshold-return theorem: blind lane CONFIRMED (appended on lane completion)

Algebra all machine-exact (S²=I, {α,S}=0, spec(c_∂)={0,±√2}, band
commutation, no flat band). Theorem chain sound: the coarea Jacobian power
is exactly right for R³ (p²dp = E·p_λ dE), the (λ,σ) projector family is
complete (Σ=I to 8e-16), densities nonnegative with total mass = ‖Ψ‖²
(so L¹ by Tonelli), no atoms for L² roots. The lane's regression methods
agree to 2e-15 and the negative control recurs with period exactly 2·T_R
(√2μ=π). Two sharpenings beyond the sealed result: (i) the threshold
behavior is √(E−E_th) VANISHING, stronger than the spec's "integrable
singularities"; (ii) the late-time tail follows the √-threshold law
t^(−3/2) (ratios 2.60→2.76 toward 2√2), a decay-rate datum the program may
later want as a derived (not fitted) prediction. Absolute A(t) values are
in-state-dependent (lane chose its own state, as designed), so no digit
comparison with the producer's regression samples is meaningful; the
theorem-level content is what was verified, and it holds.

## Standing watch
- Codex v002 correction wave in progress (endomorphism algebra-closure
  overclaim, self-flagged; conditional-expectation fix expected; my Møller
  review shares the overclaim and will be annotated when v002 lands).
- Threshold-return blind lane still in flight.
- All statuses false; no seal claims; manifest intact.
