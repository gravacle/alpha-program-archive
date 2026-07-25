# 04 — Operator Construction Record (Gate D)

Operators actually built and evaluated in this run (spectra/determinants/
traces computed directly, never identity/dimension counts):

1. **Two-endpoint comparison family** — full overlap functional over
   (p, φ, θ); minimum structure and orthogonality manifold computed
   directly; 200 random trials, max error < 1e-12.
2. **Binary closure generator** H = Δ·P₁ — autocorrelation ζ_p(t) evaluated
   on a 1e5-point grid for p ∈ {0.1,…,0.9}: min|ζ_p| = |2p−1| confirmed;
   exact zero only at (p=1/2, Δt/ħ=π).
3. **Star operator B_h** (7-dim, handle-conditioned) — characteristic
   polynomial λ(λ²−2) computed; spectrum {−√2, 0, √2}; root-to-endpoint
   transfer at τ_R verified (Gram = I₃); full-star contrast case D†D = I+J
   with singular values {2,1,1} computed to expose the conditioning
   dependence.
4. **Lorentzian Schur compression** — 12×12 kernel built from explicit
   Euclidean/Lorentzian gammas (Clifford (+−−−) verified numerically);
   K⁻¹ computed and compressed: P₁K⁻¹P₁ = slash(p)/(p²−2μ²)⊗P₁ verified at
   the packaged momentum and at **50 independent random (μ,p) samples**;
   pole-proximity guard honored; both negative controls exercised.
5. **Chiral operator gate algebra** — det K_H = [p²−(a²+b²)]²,
   {Γ_ch, C_H} = 0, C_H² = (a²+b²)I₄, Hermiticity: verified over 100 random
   (p, a, b) trials (the file's claimed audit script is absent from the
   package; this run's independent implementation is the only executable
   evidence).
6. **Closure trial potentials V1/V2** — exact rational stationarity,
   curvature 8n > 0, distinct radii {1, √2}: re-executed; outputs
   byte-identical to sealed results.
7. **Many-record counterfamily B_λ** = |10⟩⟨01| + |01⟩⟨10| + λ|11⟩⟨11| —
   5 distinct spectra with identical vacuum/one-record restrictions
   confirmed: one-record data do **not** fix the connected parent.

## Gate-D findings on packaged executables

- Genuinely computing: Schur-pole audit (with negative controls),
  first-opening audit (spectra, transfer, π/24 quadrature),
  underdetermination/magnitude gates (exact integer algebra), action
  multiplier's character classification, many-record counterfamily.
- **Vacuous or tautological checks found**: the first-opening
  "least-positive root" check can never fail ((1+cos)/2 ≥ 0 always) —
  mitigated here by an independent 200k-point interval scan; the
  root-incidence audit re-checks its own definition (tautological); part of
  the first-opening audit greps required prose from the markdown
  (consistency, not derivation).
- **Status strings broader than computations**: the underdetermination v001
  top-line string asserts "current premises do not select" while the code
  verifies only the trial algebra and distinctness (the JSON's scope field
  is honest); "primitive_mass_rate_times_T_R = PI" is arithmetic
  restatement, not derivation.
- **Optimization-safety violations**: underdetermination v001 (5 load-bearing
  asserts) and action-multiplier audit (3) are stripped under `python -O`,
  contradicting the package's own SP14 conversion claim; magnitude v003 is
  clean (0 asserts, require(), optimized-run test).
- **21 of 26 subordinate audit scripts frozen in
  BID_SOURCE_PARENT_SUBORDINATE_OUTPUT_CONTRACT_V001.json are absent from
  the package** (including CPT intertwiner, axial CP reduction, unique
  controlled coupling, one-normal zero-form enumeration, commutant
  classification). Their PASS labels are frozen strings here — unverifiable
  in-package. The 5 present scripts all re-executed and reproduced their
  contract-frozen outputs exactly.
