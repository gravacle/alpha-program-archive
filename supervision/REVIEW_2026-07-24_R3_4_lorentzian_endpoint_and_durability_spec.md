# Supervision review — Lorentzian endpoint RESULT (blind-verified) + Møller/durability SPEC
Date: 2026-07-24 · Reviewer: Fable lane

## Part 1 — R3.4 Lorentzian Joint-Endpoint Compatibility RESULT v001: **CONFIRMED**

Verdict `EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED` landed
exactly as pre-registered. Two fresh-context blind lanes rebuilt the gate
from spec text alone (forbidden from reading any result/audit file):

| Quantity | Codex | Blind lanes | Match |
|---|---|---|---|
| P(p=0) | 0.9999999999999996 | 1 − 2.2e-16 | exact |
| P(0.25) | 0.9845052711696443 | 0.984505271169644 | digit-for-digit |
| P(0.5) | 0.9395566924273323 | 0.939556692427333 | digit-for-digit |
| P(1.0) | 0.7812082943003530 | 0.781208294300353 | digit-for-digit |
| P(2.0) | 0.4067339219700168 | 0.406733921970016 | digit-for-digit |
| P(4.0) | 0.2596535767624385 | 0.259653576762437 | digit-for-digit |
| Gaussian packet | 0.9442917391998132 | 0.944291738292 (amplitude-width convention) | see note |

Both lanes independently: built the 12×12 tensor Hamiltonian with explicit
Dirac gammas; verified H² = |p|²+μ²c_∂² (cross term dies because
{α_i, γ⁰γ⁵}=0); evolved by two methods (eigh vs functional calculus,
agreement ≤2.7e-15); and **derived the parity condition symbolically before
computing** — exact transfer forces sin(Et)=0 and e^{−i|p|t}=−cos(Et),
i.e. Et=nπ, |p|t=kπ, n+k odd. Lane 1 additionally derived the closed form

    P(p) = |½[e^{−i|p|t} − cos(Et) + i|p|·sin(Et)/E]|²,  E=√(p²+π²)

matching every matrix computation to ~1e-15. Impossibility for generic p:
E/|p| = √(1+π²/p²) is irrational for all rational p, so no time satisfies
both commensurability conditions; the exception set is measure-zero.

**One documentation nit (only discrepancy found):** the result says
"Gaussian packet with width 0.7". Under σ(|amplitude|²)=0.7 the lanes get
0.897966629237; under σ(amplitude)=0.7 (so |amp|² has σ=0.7/√2) they get
0.944291738292 — matching Codex to 9 digits. So Codex's "width" is the
amplitude Gaussian's σ. Substance unaffected; the result file's wording
should ideally say so. Flagged for the eventual Stage-7 review packet.

## Part 2 — R3.4 Causal Shared-Source Møller/Durability SPEC v001: **ACCEPT**

The right construction after the transport CONDITIONAL and the Lorentzian
negative. Three features of note:

1. **Ordinary local parent, transport demoted.** H_N = H_S⊗I + Σv_jB_j + D_N
   with H_S = dd* (source graph Laplacian — derived, not chosen). "No
   comoving transport equation is imposed. The conditional transported-tail
   candidate is a negative control and may not be used as authority." The
   underived rule is quarantined exactly as discipline requires.
2. **Pass condition honestly reframed.** After the Lorentzian gate, unit
   pointer probability is not available off the rest ray — so the gate tests
   *durability of whatever probability is produced*: the Heisenberg image of
   every completed pointer observable must be constant after its closure
   face. Explicitly: "permits the pointer probability… to be less than one;
   requires that whatever probability is produced is not subsequently
   rewritten." No required value is assigned — anti-tuning guard present.
3. **The pulse profile is DERIVED.** v_j(t) = τ_R·w(t−j) with
   w(s)=32(½−|s−½|)³ — the time marginal of the uniform measure on a unit
   3+1 causal diamond. Independently verified analytically: the diamond's
   constant-time cross-section is a ball of radius min(s,1−s), so the
   marginal ∝ min(s,1−s)³, and ∫₀¹min(s,1−s)³ds = 1/32 — normalization 32
   exact. The profile descends from the R3.3 uniform-measure derivation
   (hash-pinned); nothing is selected by endpoint performance.

Also clean: sealed before evaluation (blind, unlike the two disclosed
result-aware gates); descendants D_N present in the class but zeroed for the
primitive sector with the complete claim held false; may-close/may-not-close
lists explicit; Møller operator Ω_N = e^{+iH_S T_N}U_N(T_N,0) unitary by
construction.

**Pre-registered prediction:**
`PRIMITIVE_CAUSAL_MOLLER_AND_PUBLIC_DURABILITY_DERIVED` — the persistence
algebra ([H_S⊗I,Z_j]=0 trivially; [B_k,Z_j]=0 for k>j already proven)
is finite-rank and will pass; expect the reported first-pointer probability
to be well below 1 (the always-on H_S degrades transfer during the pulse,
the same physics as the static-sum 0.306 diagnostic, softened by the
pulsing); expect clean second-order slicing convergence.

## Tripwire dispositions this pass
- Contamination token (2 hits, June rollout): same benign critical-historical
  passage, 6th consecutive identical classification.
- NEEDS_THEORY_DECISION (2 hits June + 19 hits today's rollout): all are the
  protocol STOP RULE text, the historical Fork-8 relay instruction, or the
  known Fork-8 registration file — no live decision request.

## Standing
Transport-gate blind workflow (3 rebuild lanes + transport-rule derivability
theory lane) still in flight. `alpha_computed=false` everywhere; no seal
claims; append-only supersession intact.
