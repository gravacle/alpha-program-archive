# Duhamel Independent Verifier Return — Sealed Transcript
Claude lane · 2026-07-26 (autonomous window) · verbatim. All runnable obligations PASS in this independent lane (six exact anchors; conditioned F-A crosscheck with H_att = -0.0426 < 0 vs g_D,c = +0.00845 > 0 — the diagonal correction dominating, exactly the predicted F2.2 structural departure; M2 anchors reproduced to all figures; independent schema proof confirming the D-2 repair necessary+sufficient). Findings F1 (D-5 reading pin needed), F2 (F-C leg victory-class ordering block), F3, F4. The PRIMARY lane was killed by the session limit and must re-run fresh; this verifier's commitment stands.

---

All verification lanes complete. Final report follows.

---

# DUHAMEL-GATE INDEPENDENT VERIFIER REPORT

**Lane:** fresh-context independent verifier per S7 (sealed verifier-protocol pattern; no executor import; own code throughout).
**Commit discipline:** all values committed to `/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/duhamel_verifier/VERIFIER_COMMIT.json` (sha256 `dff9bd83...4625362f`) **before** any comparison; comparison in `VERIFIER_COMPARISON.json` in the same directory. Own scripts: `verifier_exact_lane.py`, `verifier_fa_crosscheck.py`, `verifier_m2_controls.py` (pinned runtime python 3.12.13, numpy 2.3.5; exact lane uses only `fractions` — no floats decide).

## M1 — Authority hashes
All 24 pinned authorities verified (19 cleanroom-root incl. D-4's diagnostic spec `d1b5ab24...`, 5 supervision-root). **No drift.** The F-A write realization (site masks `diag(1,1,0)`/`diag(0,1,1)`, Dirac rep pairing α_x with S_n) was taken from the hash-pinned Route-1 executor artifact `scripts/derive_stage8_t7_primitive_operator_response_v001.py` (verified `3d8aea1a...`, pinned in 789338ad's authority table) as a frozen model reference only; all verification code is my own.

## Formal lane (M7) — own symbolic algebra
- **FK-1** (both displayed forms), **P1** (reality; L_mm = conj L_pp), **FK-2** (incl. the `Re[c²]=2(Re c)²−|c|²` step), **FK-3**, **L-ADD** (generic and q=1 endpoint): re-derived by hand and verified **exactly** on 20 randomized Gaussian-rational second-order jets each (exact complex-rational jet algebra; all identities hold with zero residual). P2 is Cauchy–Schwarz on the HS Gram form; P4 (rank-one ⇒ g=0) confirmed exactly on F-B.
- **C1 DERIVES** on the Phase-A A2 generator: `h = h₀ + λv(t)M(t)⊗S_n + aJ(t)` is affine in `a` with J independent of λ; `d²h/da² = 0` identically. The three-site fixture generator is non-affine (`d²h/dθ²|₀ = −i D″₀⊗α_x ≠ 0`, entries ∓1/18) — correctly exploited as the contact control, not a C1 failure.
- **C2 DERIVES**: i_r is the ready-record embedding (no A argument); the final PVM is the qutrit product-basis/c-matrix spectral data (no A argument); relay isometries are built from incidence projectors/tuple maps with no history argument (52401eef §S, 0df721a1 §O2); envelope clause (d): the ER profile enters only through the scalar v(t) multiplying the λ-write term (A2 display), never through i_r/PVM/relays.

## F-B exact anchors (M4) — own exact rational arithmetic from the sealed O6/D6 closed forms
g_c = **0** (exact; degenerate-endpoint control S6.5 passes: rank-one ⇒ mixed covariance exactly zero while H_att,c = 1/4); (log q_c)″(0) = **−1/2**; H_att,c = **1/4**; g_all = **1/4**; H_att,all = **1/4**; ‖η_r‖² = |A₋′(0)|² = g_all − g_c = **1/4**; L-ADD endpoint residual = **0**. Sigma-witness reproduction: (FS, linear-amplitude attenuation, endpoint probability, inclusive sandwich) = **(1/4, 1/4, 1/2, 0)** — all exact, all matching e12fffcc and the spec's predeclared values.

## F-A conditioned crosscheck (M3/M5) — own bit-mask CAR lift, unsplit RK4 200/400 steps/cell, negative-energy Slater fill (wedge⁴C⁸, dim 70, record dim 9), enclosure radius |v₄₀₀−v₂₀₀|/3 + 1e−8
| scalar | enclosure |
|---|---|
| q | 0.2541064940 ± 2.86e−7 — excludes 0, margin 8.9e5 ≥ 10³ ✓ |
| g_D,c | 0.008450951 ± 4.93e−8 — **lower bound > 0** ✓ (non-scalar witness) |
| (log q)″ | 0.10210007 ± 1.01e−6 (stencil: 0.1021001 ± 1.49e−6, intersects ✓) |
| H_att | **−0.04259908** ± 5.50e−7 (independent stencil −0.04259908 ± 1.04e−6, intersects ✓; FK-2 algebraic residual exactly 0) |
| g_all | 0.06481887 ± 7.59e−8 |
| g_r | 0.08402196 ± 1.06e−7 |
| α_c, α_r | both ≈ 0 (|·| < 1e−16; enclosures ± 1e−8) |
| FK-3 FS pullback | 0.008450951 ± 9.02e−8, intersects g_D,c ✓ |
| **L-ADD residual (M5)** | −5.4e−10 ± 1.56e−8 — **contains 0** ✓ |

Note: H_att < 0 on F-A while g_D,c > 0 — the completed diagonal correction (½·0.1021) dominates; this is exactly the F2.2 structural departure the spec predicts, and it gives the wrong-form control real teeth.

## Controls (M6)
- **S6.1 GHZ**: my (H1)-checker (amended D-1 form, per-K zero-freeness) returns **H1_VIOLATED** for every fixed polydisc (zero π/(2Nτ_R) enters); schema **REFUSES**, naming independent-record-colors as the violated premise. ✓
- **S6.2 V010**: κ_L = 1/[4L⁴sin²(π/L)] ≤ 1/(16L²) (exact bound, sin(π/L) ≥ 2/L) → 0; **stays failed**, no extensive factor. ✓
- **S6.3(a) contact omission**: broken H_att = +0.015978 vs stencil −0.042599; mismatch 0.058578 > 3×radius (3.5e−6) ✓; discrepancy enclosure and independently integrated contact-term enclosure agree to 5e−11 — the mismatch **is** the contact term at second order. ✓
- **S6.3(b) wrong ordering**: pair-evaluated Im z_c(7/100,−11/100) = +3.1503e−4, flips sign exactly under the swap, enclosure excludes zero ✓. **FINDING F1 below on the D-5 wording.**
- **S6.3(c) wrong form**: |H_att − g_D,c| = 0.051050 = ½|(log q)″| > 3×radius (1.8e−6), with (log q)″ enclosure excluding zero — flat-diagonal stencil fails detectably. ✓
- **S6.4 Route-1 re-execution**: my own generic-compression path vs closed forms at both frozen pairs: max completed error 4.45e−16, max exhaustive error 3.34e−16 (matches sealed 4.45e−16/3.34e−16); no all-outcome substitution. ✓

## M2 epsilon-halving regression (own 96-step midpoint implementation, own Frechet + independently accumulated adjoint branch)
plus/all = minus/all = **8.19415e−8**; plus/comp = minus/comp = **6.69468e−8** — sealed anchors reproduced to all printed figures; strictly decreasing, halving factors ≈ 3.9996–4.0000 ≥ 2; finest ≤ 2e−5; adjoint-exchange residuals exactly 0. ✓

## S5.2 schema proof (written independently from the AMENDED hypotheses)
(1) By amended (H1), Ghat_K is holomorphic and zero-free on the closed pair polydisc P; the open polydisc is contractible, so a holomorphic logarithm anchored at Ghat_K(0,0)=1 exists; γ_K := −Log Ghat_K/N₄(K) is holomorphic on the open polydisc. (2) (H2)(i) gives sup_K sup_P |γ_K| ≤ Γ_*: {γ_K} is a normal family (Montel, several variables). (3) Uniqueness of subsequential limits: any two locally-uniform limits agree on the amended product set E₁×E₂; for fixed w₀∈E₂ the difference vanishes on E₁ (accumulation point in the open disc) hence identically in z by the one-variable identity theorem; then for every z it vanishes on E₂ hence identically — the Osgood/iterated step, which **requires the product-set form**: the review counterexample i(−1)^K(z−w) on the diagonal confirms the original per-variable clause was genuinely too weak (D-2 repair necessary and sufficient). (4) Normality + unique limit ⇒ γ_K → γ_inf locally uniformly (Vitali–Porter); γ_inf holomorphic. (5) Cauchy integrals on distinguished boundaries strictly inside P transport every mixed partial; hence the interchange at (0,0) is valid, and FK-2 passes to the limit as three separately normalized limits (D-9 reading). **No step uses clustering, decay, δ-uniformity, or any parent property beyond (H1)/(H2)/C1/C2.** I independently confirm D-1's decisive claim: the deleted K-uniform δ is never used — only per-K zero-freeness (for the log) and Γ_*.

## Findings (reported, not repaired)
- **F1 (S6.3(b)/D-5, spec-text weakness):** on F-A the baseline first derivative ⟨X₀,η⟩ vanishes to machine precision (|Re|,|Im| < 1e−16; enclosure ±1e−8 contains 0 — apparently an exact fixture symmetry). Under the literal S3.1-baseline reading of "the Im⟨X_0,eta⟩ enclosure must EXCLUDE ZERO", the amended tooth is **unsatisfiable on F-A**; only the pair-evaluated reading (Im z_c at the frozen pair, 3.15e−4, sign-certified) is dischargeable. The amended statement is still too weak/ambiguous here; a successor must pin the reading. Named: `S63B_D5_BASELINE_READING_UNSATISFIABLE_ON_FA`.
- **F2 (D-4 F-C leg, blocked by ordering):** no Phase-A sealed result bundle is hash-pinned in the authority closure (Phase-A execution is still open), and this gate forbids a fresh Phase-A production run; the F-C conditioned crosscheck with the two Phase-A pinned states is therefore **not runnable as sealed**. Named: `F_C_INPUT_BUNDLE_NOT_YET_SEALED` — a victory-class block, not a failure of the identities.
- **F3 (provenance note, non-blocking):** the concrete F-A/O7 write realization (cell site-masks, Dirac representation) is pinned only via the hash-pinned Route-1 executor artifact, not displayed in sealed prose; recommend a successor display it textually.
- **F4 (minor derivable obligation):** (H1)'s well-formedness tacitly uses finite-K entirety of the pair-holomorphic extension (finite-dimensional Dyson series + adjoint-continued bra branch); one-line derivable, should be stated in the majorant supplier.

## Verifier verdict
On everything runnable from the sealed texts: **M1, M2, M3 (F-A), M4, M5, M6 (S6.1, S6.2, S6.3a, S6.3c, S6.4, S6.5), M7 all PASS** in this independent lane; predeclared predictions S9.1–S9.5 confirmed. Qualified passes/blocks: S6.3(b) passes only under the pair-evaluated reading (**F1**); F-C leg **blocked by ordering** (**F2**). All protected flags remain false; (H1)/(H2) remain named underived inputs; no coupling, kappa_record, or alpha target was read; no sealed/production file was modified — all outputs under `/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/duhamel_verifier/`.
