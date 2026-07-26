# Stage-8 T7 Gamma-Gate Control-4 Repair Amendment V001

Date: 2026-07-26 (autonomous window)

## Status

```text
APPEND_ONLY_CONTROL_REPAIR_AMENDMENT
```

Repairs one negative control of the sealed gamma gate (spec 5f7e9965… +
repair amendment) on a structural discovery made by the BLIND lane
during execution: the broken-P_x falsifier is UNSATISFIABLE AS PINNED.

## The discovery (recorded; to be sealed as Lemma 3 in the parity result)

a-parity of the completed amplitude is DOUBLY protected on this carrier:
besides the unitary T' = P_x (x) (i gamma^1) (Lemma 2), the ANTIUNITARY

```text
Theta = (I (x) alpha_y) o K        (K = complex conjugation)
```

together with the TIME-SYMMETRY of the sealed pulse (b_D invariant under
t -> 1-t) independently forces u_lambda(-a) = Theta u_lambda(a)^dagger
Theta^{-1} (blind lane: generator identity exactly 0; propagator
residual 3.5e-14; both pinned states Theta-invariant). Consequently
displacing b_D off x = 0 breaks P_x (conjugation residual 1.6e-6; B_D
odd part 14%) yet Z'(0) remains exactly 0 (measured <= 2.3e-13) — the
pinned floor |Z'(0)| >= 1e-9 cannot be met by ANY conforming
implementation. Per the frozen rule this is a control failure -> the
gate blocks honestly with the named witness CONTROL4_DESIGN_DEFECT.

This repair is control-design only: it does not touch the Delta_Xi
computation, the verdict rule, or the frozen predictions (P1 remains
non-revisable; both P1 outcomes remain reachable after this repair).

## The repaired control (frozen)

```text
Control 4 v2 (double-symmetry-broken falsifier): the broken variant
displaces b_D's center to x_0 = 1/10 along x AND multiplies the
connection term J(t) by the time-asymmetry factor (1 + t/3) — breaking
BOTH the unitary (P_x) and antiunitary (Theta, via time symmetry)
protections. Floors unchanged: broken |Z'(0)| >= 1e-9 AND unbroken
|Z'(0)| <= 1e-12, separately. If yet another symmetry protects the
broken variant, the gate blocks again with a new named witness — every
such block is itself a structural discovery and is preserved.
```

## Apparatus note (binding on both lanes)

Near-degenerate spectral clusters break eigh-based step-exponential
conjugation equivariance at ~7.9e-9 (observed at ell = sqrt2, envelope
A); scaling-and-squaring restores exact equivariance. Both lanes use
scaling-and-squaring for step exponentials wherever a parity/conjugation
residual is being certified against a <= 1e-12 bar.

## Execution consequence

The gate re-runs Part A's control 4 (v2) and re-assembles the verdict
under the sealed rule; all other Part A/B computations stand as
executed (they are control-independent). Both lanes re-run the repaired
control; the blind lane's commitment discipline applies to the new
control values.

## Protected status

```text
record_parity_lemmas_sealed = false
gamma_refutation_computed = false
alpha_computed = false
proof_authorized = false
```
