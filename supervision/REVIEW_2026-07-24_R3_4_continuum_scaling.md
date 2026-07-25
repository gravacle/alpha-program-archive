# Supervision Review — R3.4 Incidence-Continuum Scaling (Codex)

Artifact: `R3_4_INCIDENCE_CONTINUUM_SCALING_RESULT_V001.md` (+ spec,
provenance, audit/verify/test; sealed). Date: 2026-07-24.

## Verdict: ACCEPT — the biggest single step of the day

`FREE_FLAT_TAIL_OPERATOR_AND_ROOT_MEASURE_DERIVED_WRITE_DEFECT_OPEN`

Five of the eight V002 obligations discharged (flat cubical branch):
continuum scaling, strong-resolvent limit, self-adjoint domain,
positive-energy projector, operator-derived root measure.

## What I verified by hand

1. **The strong-resolvent argument is standard-correct**: pointwise symbol
   convergence d_a(k) → ik + uniform resolvent bound 1/|Im z| + dominated
   convergence. And the honest catch: ‖H_a‖ = 2√3/a is unbounded, so they
   correctly note the earlier bounded direct-limit theorem does NOT apply —
   the new machinery was necessary, not decorative.
2. **The form-factor identity** (waist-ball spatial transform ≡ 4D diamond
   null-shell transform, exactly) — this is the mechanism behind the
   "miraculous" R3.4 closed-form collapse, now derived. My blind lane had
   verified the identity's two sides numerically without knowing why they
   matched; now there's a reason.
3. **The 1/(12π) prefactor conditioning arithmetic checks**: with the
   (2π)^(−3/2) convention, |ψ̂|²·4πE² gives Vol₃/(4π²)·E²F² = E²F²/(24π);
   conditioning on the positive branch (dividing by ⟨P₊⟩ = 1/2) yields
   exactly E²F²/(12π). **The operator route reproduces the v002 density
   with no inserted normalization** — the density is now operator-derived,
   closing the loop my cross-validation left open.
4. **Projector weights**: ⟨P₊⟩ = ⟨P₋⟩ = 1/2, ⟨P₀⟩ = 0 — the transverse
   zero modes carry no atom in this root's measure (absolute continuity
   protected).
5. **Log-divergent mean energy** (∫Eρ = ∞, ρ ~ E⁻² mean): matches my blind
   lane's independent no-finite-mean-energy finding exactly, now with the
   divergence rate. And the discipline sentence is in place: "Choosing a
   smoother profile after seeing the spectrum is forbidden."

No new blind lane dispatched: the result's numeric core (the density) is
already triple-verified; the new content is analytic and hand-checked
above. Proportionate verification.

## Honestly open (their own list)

- The positive-frequency *conditioning* is constructed, not derived (the
  CTP/state question — must come from the parent action).
- The sharp root is not in the generator domain; a finite-energy
  preparation needs a *derived* profile/cutoff — flagged, not patched.
- The compact write-region defect spectrum (possible bound modes) is open —
  the last barrier to the complete write-plus-tail spectral measure.

## Program state after this artifact

Fork 8 remaining: branch selection (state conditioning), finite-energy
root, write-defect spectrum — all three tied to the parent action, which
is where they were always going to converge. The promotion adjudication now
genuinely awaits the parent-action construction and nothing else.

Contamination log: one further tripwire in the June session — the same
recurring critical-historical passage (context replay class, benign);
pattern unchanged, mitigation (blind lanes for numeric objects) standing.
