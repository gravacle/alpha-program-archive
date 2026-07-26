# Condition-1 Same-Apparatus Argument — Sealed Transcript
Claude lane · 2026-07-26 · verbatim return of the fresh-context operator-level
analysis lane chartered by STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_
AUTHORIZATION_V001. Verdict SAME APPARATUS (Outcome A). The verdict rests on
the exact Duhamel identity and the tau-grading of the connection space — the
lane's numerics are an independent reconstruction from sealed spec text and
are disclosed as order-of-magnitude, not seal-grade.

---

All seals verified; the algebra and numerics are complete. Here is the argument.

---

# CONDITION 1 — TYPED OPERATOR-LEVEL ARGUMENT

**Lane:** fresh-context operator-level analysis. Read-only on the workspace; scratch confined to `/private/tmp/claude-501/-Users-bgm-MB-Work/578abe61-ea1d-48e6-8fb1-b06509d933a1/scratchpad/cond1/`. No measured physical constant read or used. Runtime: pinned `/Users/bgm/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` (3.12.13, numpy 2.3.5, **scipy absent**); own scaling-and-squaring `expm` per the sealed apparatus note.

**Seals verified before use** (computed SHA-256 == adjacent `.seal.sha256`, all eight):

| Artifact | Seal |
|---|---|
| `STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001.md` | `67bb5cff…` PASS |
| `STAGE8_T7_RECORD_PARITY_LEMMAS_RESULT_V001.md` | `8dd121e8…` PASS |
| `STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md` | `5f7e9965…` PASS |
| `STAGE8_T7_GAMMA_GATE_CONTROL4_REPAIR_AMENDMENT_V001.md` | `f7f93be8…` PASS |
| `STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md` | `83ff0d4f…` PASS |
| `STAGE8_T7_GAMMA_REFUTATION_GATE_RESULT_V001.md` | `fce4a19b…` PASS |
| `STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md` | `789338ad…` PASS |
| `stage8_execution/work/GAMMA_GATE_LEMMA_PROOFS_DRAFT_V001B.md` | `c0eb6458…` PASS |

---

## 1. CHARTER, STATED EXACTLY

The sealed text. From `STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_LEMMAS_GATE_SPEC_V001.md`, Part A, obligation A3 (second teeth control), verbatim:

> `(A3) the two teeth controls: the lambda-odd weight vector`
> `(0, -1/(2 sqrt 2), +1/(2 sqrt 2)) must give exactly zero completed sum`
> `(machine <= 1e-14), and a predeclared P_x-BROKEN variant (b_D center`
> `displaced to x_0 = 1/10 along x) must produce Z'(0) != 0 at a scale`
> `exceeding 1e3 x its unbroken counterpart.`

Sharpened to absolute floors by `STAGE8_T7_GAMMA_GATE_SPEC_REPAIR_AMENDMENT_V001.md` R6, verbatim:

> `Broken-P_x teeth: absolute floors — broken variant |Z'(0)| >= 1e-9 AND`
> `unbroken |Z'(0)| <= 1e-12, separately.`

Redesigned once by `STAGE8_T7_GAMMA_GATE_CONTROL4_REPAIR_AMENDMENT_V001.md`, verbatim:

> `Control 4 v2 (double-symmetry-broken falsifier): the broken variant`
> `displaces b_D's center to x_0 = 1/10 along x AND multiplies the`
> `connection term J(t) by the time-asymmetry factor (1 + t/3) — breaking`
> `BOTH the unitary (P_x) and antiunitary (Theta, via time symmetry)`
> `protections. Floors unchanged: broken |Z'(0)| >= 1e-9 AND unbroken`
> `|Z'(0)| <= 1e-12, separately.`

**Reading the charter as a claim about a measurement.** Note first what the charter does *not* say: it names no mechanism, no symmetry-attribution obligation, no component of any kernel. Both versions state **two floors on one scalar**, `|Z'(0)|`. The obligation is titled *teeth* — it exists to establish that the number is capable of being nonzero, so that Lemma 2's `Z'(0) = 0` is a fact about the object and not about a dead instrument.

Your paraphrase is correct, and I verify it against the sealed chain rather than adopting it. From spec A4 (`789338ad…`):

```
K_pointer(a) = sum_lambda w_lambda Gamma(u_lambda(a))
```

with `w_lambda = <pointer|P_lambda|ready>`, recovered exactly in the primary JSON as `w = (-1/4, +1/2, -1/4)` on the sealed ordering `(-sqrt2, 0, +sqrt2)`. The completed-record object is the state evaluation of that Kraus operator, so with quasifree covariance `C`,

```
Z(a) = sum_lambda w_lambda D_lambda(a),   D_lambda(a) = omega(Gamma(u_lambda(a))) = det(1 - C + C u_lambda(a))
```

This is confirmed independently by `GAMMA_GATE_LEMMA_PROOFS_DRAFT_V001B.md` §B1(4): *"Lemma 1 collapses the pointer sum to Z = -(1/2)(D_sqrt2 - D_0)"* — which is exactly `sum_lambda w_lambda D_lambda` with `w = (-1/4, 1/2, -1/4)` under `D_{-lambda} = D_{lambda}`.

**Charter restated precisely.** Control 4 certifies:

> the derivative `d/da` at `a = 0` of `Z(a) = sum_lambda w_lambda det(1 - C + C u_lambda(a))`, read on the pointer-weighted completed-record object, through the single first-order-in-`a` contraction of the quasifree state against the Duhamel-transported connection insertion, is a **live** reading: it clears `1e-9` when the `a`-dependence is genuinely odd, and sits under `1e-12` when it is not.

Which quantity: `Z'(0)`. On which object: the pointer-weighted completed record, both pinned states. Through which contraction: the one described in §2.

---

## 2. DECOMPOSITION OF `Z'(0)` AT THE OPERATOR LEVEL

Generator (spec A2): `h_lambda(t;a) = h_0 + lambda v(t) M(t) (x) S + a J(t)`, `J(t) = -B_D(t) (x) alpha_x`.

Write `u_lambda(t)` for the record-dressed flow at `a = 0` and `u_lambda := u_lambda(1)`. Duhamel in `a` around that flow:

```
d/da u_lambda(1;a)|_0  =  -i u_lambda * Jcal_lambda ,
      Jcal_lambda := integral_0^1 dt  u_lambda(t)^dagger J(t) u_lambda(t)
```

Jacobi's formula on `D_lambda(a) = det(1 - C + C u_lambda(a))`:

```
D'_lambda(0) = -i D_lambda(0) * tr[ G_lambda  Jcal_lambda ],
      G_lambda := (1 - C + C u_lambda)^{-1} C u_lambda
```

`G_lambda` is **the** contraction of the quasifree state — and it is the only one. `J` enters the determinant exactly once at first order, so there is one Wick contraction, not a family. Cycling the transport onto the state:

```
Z'(0) = integral_0^1 dt  tr[ Phi(t) J(t) ],
      Phi(t) := -i sum_lambda w_lambda D_lambda(0) * u_lambda(t) G_lambda u_lambda(t)^dagger          (**)
```

**This is the apparatus.** `Z'(0)` is a single **linear functional** `L[J] = integral tr[Phi(t) J(t)] dt` on Hermitian connection profiles. The kernel `Phi(t)` is assembled entirely from `a = 0` data — `h_0`, `M(t)`, `v(t)`, `lambda`, `w_lambda`, `D_lambda(0)`, `C` — and **contains no reference to `J` whatsoever**. There is one slot, and `J` goes into it.

In the sealed Strang discretization (`Step_k(a) = F A_k(a) G_k A_k(a) F`, `A_k(a) = exp(-i a J_k dt/2)`), the same identity holds exactly, slot-resolved by record eigenvalue `lambda` and time step `k`:

```
Z'(0) = sum_{lambda,k} T_{lambda,k},
   T_{lambda,k} = w_lambda D_lambda(0) tr[ Phi_{lambda,k} J_k ]
   Phi_{lambda,k} = -i (dt/2) ( G_k X_{lambda,k} + X_{lambda,k} G_k ),
   X_{lambda,k}   = F U_{<k} (1-C+C U_lambda)^{-1} C U_{>k} F
```

**Which contributions the reality class annihilates, and by what mechanism.** Let `tau(X) = Omega X^T Omega`, `Omega = I (x) alpha_y` (the primary lane's L4 form; `tau` is the transpose-class anti-automorphism, equal to conjugation by the antiunitary `Theta_0 = Omega K` on Hermitian operators). Machine-exact, this run:

```
Omega^2 - I = 0.00e+00 ;  Omega purely imaginary, antisymmetric (0.00e+00)
tau(h_0) - h_0                                  = 0.00e+00
tau(M (x) S) - (M (x) S)                        = 0.00e+00
tau(B (x) alpha_x) + (B (x) alpha_x),  B real symmetric      = 0.00e+00   [tau-ODD]
tau(B'(x) alpha_x) - (B'(x) alpha_x),  B' = i(real antisym)  = 0.00e+00   [tau-EVEN]
```

`tau` preserves the trace pairing (`tr[tau(X)tau(Y)] - tr[XY] = 1.2e-34`), hence its `+1` and `-1` eigenspaces are **orthogonal** in that pairing (checked directly: `tr[(B (x) a_x)(B' (x) a_x)] = 0 + 6.0e-35 i`).

Every Hermitian spatial factor splits uniquely as `B = B_R + i B_I` with `B_R` real symmetric, `B_I` real antisymmetric. Therefore the connection space splits into exactly two `tau`-eigenspaces:

```
tau-ODD :  {real symmetric} (x) alpha_x    <- the L4 reality class (the sealed J, and every v1/v2 variant)
tau-EVEN:  {i * real antisym} (x) alpha_x  <- the class-leaving direction
```

Restricting `(**)` to the `alpha_x` channel: define the **spatial detector matrix**
`Psi^{(lambda,k)}_{mn} := tr_spinor( Phi_{lambda,k}[m,n] * alpha_x )`, an `8 x 8` complex matrix, so that `tr[Phi (B (x) alpha_x)] = tr[Psi B]`. Then

```
tr[Psi B] = <sym(Psi), B_R>  +  i <antisym(Psi), B_I>
```

and, by the orthogonality just established,

```
sym(Psi)     <->  the tau-ODD part of Phi     <->  reads the reality class
antisym(Psi) <->  the tau-EVEN part of Phi    <->  reads the class-leaving direction
```

**L4, restated as a property of the detector: `sym(Psi^{(lambda,k)}) = 0`, pointwise in `t`, per `lambda`, for the sealed `a = 0` data.** That is the whole mechanism, and it is the only thing the reality class annihilates. Nothing else in the chain — not the Duhamel insertion, not `G_lambda`, not `D_lambda(0)`, not the `lambda`-sum — is touched.

---

## 3. THE DECIDING TEST

Verified first what the witnessed positive control actually was. `STAGE8_T7_GAMMA_REFUTATION_GATE_RESULT_V001.md`: *"a positive control (a complex-Hermitian spatial connection factor, outside the class, yields |dD| ~ 1e-4 **under the same apparatus**)"*. `GAMMA_GATE_LEMMA_PROOFS_DRAFT_V001B.md`: *"a complex-Hermitian spatial factor escapes the protection at first order (|dD| ~ 1e-4 under the same apparatus — the apparatus demonstrably has teeth)"*. Confirmed: the class-leaving falsifier is `J' = -B' (x) alpha_x` with `B'` Hermitian, `B'^T != B'` — i.e. it turns on the `i B_I` part. Its normalization is **not recorded** in any artifact on disk; I flag that as a real gap in §6.

Now the crux. Write the nonzero term for `J'` and check whether that same term exists-but-vanishes for `J`.

For `J`: `T_{lambda,k} = w_lambda D_lambda(0) tr[Psi^{(lambda,k)} B_D(t_k)]`, `B_D` real symmetric
&nbsp;&nbsp;&nbsp;&nbsp;`= w_lambda D_lambda(0) <sym(Psi^{(lambda,k)}), B_D(t_k)>` = **0**, because `sym(Psi) = 0`.

For `J'`: `T_{lambda,k} = w_lambda D_lambda(0) tr[Psi^{(lambda,k)} (i B_I(t_k))]`
&nbsp;&nbsp;&nbsp;&nbsp;`= i w_lambda D_lambda(0) <antisym(Psi^{(lambda,k)}), B_I(t_k)>` = **nonzero**.

**Same term.** Same index pair `(lambda, k)`. Same `Phi_{lambda,k}`, hence the same `u_lambda(t)`, the same `G_lambda`, the same `D_lambda(0)`, the same `w_lambda`. Same trace. Same one Wick contraction. Same spinor channel `alpha_x`. Same tensor factor — the *spatial* one — with the only difference being **which half of one matrix `Psi` the input happens to project onto**.

This is the principal's criterion (i) verbatim: *"the same term merely vanishes for J … by a reality/imaginary-part argument."* Indeed it is literally a reality argument: `sym` vs `antisym` of one `8 x 8` matrix, equivalently real vs imaginary part of the Hermitian spatial factor. It is **not** criterion (ii): there is no different Wick contraction (only one exists at first order in `a`), no different sector (same `lambda`, same state, same determinant), no different tensor factor (both live in the spatial factor of the `alpha_x` channel).

**The steelman for DIFFERENT, stated fairly, and why it fails.** One could object: `sym(Psi)` and `antisym(Psi)` are *orthogonal* components; certifying `antisym(Psi) != 0` says nothing about `sym(Psi)`, and since every conforming connection lies in the class, only `sym(Psi)` is "the relevant half." Hence the control lights a lamp in a room nobody enters.

Two answers, and the second is decisive.

*(a)* The objection conflates two obligations. Certifying *"the symmetry is what causes the zero"* is indeed now impossible — that is exactly L4's content and it is already sealed. But the charter's control 4 is a **teeth** control and its frozen conditions are two floors on the scalar `|Z'(0)|`. Its job is to exclude the artifact space: `J` never assembled (`max_k ||J||_2 = 5.749e-4`, spec gate `> 1e-6`: PASS); tangent machinery differentiating a constant; `D_lambda(0) = 0` or `G_lambda = 0` degenerate state functional; the `lambda`-sum collapsing; the trace contraction returning zero identically. The class-leaving probe excludes **every** one of these, because it drives them all and returns a number. The single item it does not exclude is `sym(Psi) = 0` — and that is not an artifact. It is the theorem.

*(b)* More decisively: **`sym(Psi)` is a live slot, not an empty one.** A structurally absent channel would be DIFFERENT apparatus. A live channel that the sealed configuration happens to fill with zero is SAME apparatus reading zero. I tested this directly (§4, Tests 1 / 2b / 2c): holding the **in-class** `J` fixed and perturbing the `a = 0` data by any `tau`-odd amount — moving the base point off `a = 0`, or adding a `tau`-odd offset to `h_0` — makes `sym(Psi)` nonzero and makes the same slots `T_{lambda,k}` read nonzero, linearly in the perturbation. The channel exists, accepts a value, and is set to zero by L4. A `tau`-**even** offset (which leaves `h_0` `tau`-fixed) does not unlock it — the negative control confirming the mechanism is `tau` and nothing else.

So the correct picture is not two detectors. It is one detector matrix `Psi`, nonzero (`||Psi||_F = 6.80e-2`), with one of its two halves set to zero by a theorem about the sealed data — and the class-leaving falsifier reading the other half through the identical contraction.

---

## 4. NUMERICAL CORROBORATION

Sealed Hermite carrier `n = 2`, `ell = 1` (spatial dim 8, spinor 4, total 32), basis order `(a,b,c,s)` with `s` fastest; `h_0 = sum_j p_j (x) alpha_j` verified against the sealed identity `h_0^2 = (3/(2 ell^2)) I` exactly; `S = -i gamma^0 gamma^5 = sigma_y (x) I_2`, `{S, alpha_x} = 0` verified; `M(t)`, `B_D(t)` by the sealed causal-diamond profile on the sealed quadrature shape (10 radial x 10 polar x 20 azimuthal); `tau_R = pi/sqrt2` (pinned by `lambda v_B = 24` exactly); state = Dirac-sea projector (on this carrier the pinned mixed covariance `(1/2)(1 - sum_j phat_j (x) alpha_j)` coincides with it, since `h_0^2 = const * I`); `N_t = 48`; all step exponentials by own scaling-and-squaring. Floats inform; the conclusion rests on §2–§3.

Scales: `max_k ||B_D||_2 = 5.749123e-4`, `max_k ||J||_2 = 5.749123e-4` (non-vacuity gate PASS), `max_k ||M||_2 = 7.660e-2`, `max_k lambda v_A = 11.7972`, `|D_lambda(0)| = 0.987449 (lambda = +-sqrt2) / 1.000000 (lambda = 0)`.

**(i) The detector is the same object, bitwise.**

```
max over all (lambda,k) and all four runs of || Phi_class - Phi_other ||_inf  =  0.000e+00
```

Not merely the same code path — the same numbers. `Phi` never sees `J`.

**(ii) The detector is loaded even when the reading is zero.**

```
lambda = -sqrt2 : ||Phi||_2 = 2.090e-02   ||Phi||_F = 8.340e-02
lambda =  0     : ||Phi||_2 = 2.083e-02   ||Phi||_F = 8.333e-02
lambda = +sqrt2 : ||Phi||_2 = 2.090e-02   ||Phi||_F = 8.340e-02
```

**(iii) Slot-by-slot readings `T_{lambda,k}` — the discriminator.** Per-`lambda` maximum over the 48 time slots, and the per-`lambda` sums:

| input | `lambda` | `max_k |T|` | `sum_k T` | slots `>1e-12` |
|---|---|---|---|---|
| **IN-CLASS** sealed `J = -B_D (x) alpha_x` | `-sqrt2` | `2.136e-38` | `-7.54e-39 + 3.33e-38 i` | 0/48 |
| | `0` | `2.865e-38` | `-1.09e-37 - 1.37e-38 i` | 0/48 |
| | `+sqrt2` | `2.081e-38` | `-5.03e-39 + 3.21e-38 i` | 0/48 |
| | | | **`|Z'(0)| = 1.322e-37`** | |
| **IN-CLASS** control-4 v2 (`b_D` at `x_0=1/10`, `J x (1+t/3)`) | `-sqrt2` | `5.887e-22` | | 0/48 |
| | `0` | `1.101e-21` | | 0/48 |
| | `+sqrt2` | `5.888e-22` | | 0/48 |
| | | | **`|Z'(0)| = 2.932e-21`** | |
| **CLASS-LEAVING** `B' = B_D + i||B_D||A_0` | `-sqrt2` | `1.519e-07` | `-7.07e-7 + 7.49e-7 i` | 22/48 |
| | `0` | `3.163e-07` | `+1.45e-6 - 1.57e-6 i` | 22/48 |
| | `+sqrt2` | `1.519e-07` | `-7.07e-7 + 7.49e-7 i` | 22/48 |
| | | | **`|Z'(0)| = 7.547e-08`** | |
| **CLASS-LEAVING** pure `B' = i||B_D||A_0` | | *identical to the row above, to every printed digit* | | |

Reading the table:

- The in-class vanishing is **per-slot**, not a `+lambda / -lambda` cancellation: every one of the 144 individual slots is at `~1e-38`. (This also reproduces the sealed v2 finding: my v2 run gives `2.9e-21` against the lane's tangent-accumulation `<= 8.8e-21`.)
- The class-leaving falsifier lights up the **same slots**, individually, at `1.5e-7` to `3.2e-7`.
- `B_D + i||B_D||A_0` and `i||B_D||A_0` give *identical* `Z'(0)`: the in-class part of a mixed connection contributes exactly nothing, and the class-leaving part contributes everything, superposed in the same slots.

**(iv) The mechanism, exhibited.** `Psi^{(lambda,k)}` symmetry, all 48 slots, all `lambda`:

```
lambda = -sqrt2 : max_k ||sym(Psi)||_F = 4.741e-17   max_k ||antisym(Psi)||_F = 6.809e-02   ratio 6.96e-16
lambda =  0     : max_k ||sym(Psi)||_F = 1.029e-16   max_k ||antisym(Psi)||_F = 6.804e-02   ratio 1.51e-15
lambda = +sqrt2 : max_k ||sym(Psi)||_F = 4.741e-17   max_k ||antisym(Psi)||_F = 6.809e-02   ratio 6.96e-16
```

Machine epsilon against a detector of norm `6.8e-2`, at **every** time slot including those where the profile on `[0,t]` is strongly asymmetric (`t = 0.0104 … 0.9896` all shown, all `||sym|| ~ 3e-17`). `Psi` is antisymmetric; it is not small.

Corresponding `tau`-parity content of `Phi` (which is the same statement one level up):

```
lambda = -sqrt2 : ||Phi||_F = 8.340e-02   ||Phi_tau-EVEN|| = 8.340e-02   ||Phi_tau-ODD|| = 2.345e-03
lambda =  0     : ||Phi||_F = 8.333e-02   ||Phi_tau-EVEN|| = 8.333e-02   ||Phi_tau-ODD|| = 7.205e-17
lambda = +sqrt2 : ||Phi||_F = 8.340e-02   ||Phi_tau-EVEN|| = 8.340e-02   ||Phi_tau-ODD|| = 2.345e-03
```

At `lambda = 0` the kernel is exactly `tau`-even — this is the elementary mechanism the sealed draft identifies (`tr(P_-(R (x) alpha_j)) = 0`). At `lambda = +-sqrt2` the kernel *does* carry a `tau`-odd part (`2.345e-03`), but that part has no `alpha_x` channel at `a = 0` — which is precisely the record-dressed annihilation the sealed draft leaves to the mechanism-identification obligation, here localized to a single statement: `sym(Psi) = 0`.

**(v) The zero-reading slot is LIVE.** Same in-class `J`, same machinery, base point moved off `a = 0` (`Z'(a_0)` must be odd in `a_0` by L2/L4):

```
   a_0        |Z'(a_0)|        max slot |T|      max_k ||sym(Psi)||_F
 0.0000      1.322e-37         2.865e-38            1.029e-16
 0.0100      3.665e-13         4.839e-12            1.944e-08
 0.0400      1.466e-12         1.935e-11            7.778e-08
 0.0700      2.566e-12         3.387e-11            1.361e-07
 0.1300      4.765e-12         6.290e-11            2.528e-07
 0.5000      1.833e-11         2.419e-10            9.722e-07
 2.0000      7.331e-11         9.677e-10            3.889e-06
```

Exactly linear in `a_0` (ratio 200 across a 200x span, both columns). Equivalently, adding a constant in-class background connection `delta * M_ref (x) alpha_x` to the `a = 0` data:

```
 delta = 1e-3 :  ||sym(Psi)|| = 2.369e-05   |Z'(0)| = 3.723e-10
 delta = 1e-2 :  ||sym(Psi)|| = 2.369e-04   |Z'(0)| = 3.723e-09
 delta = 1e-1 :  ||sym(Psi)|| = 2.370e-03   |Z'(0)| = 3.712e-08
```

and a `tau`-odd offset elsewhere in `h_0` (`delta * M_ref (x) alpha_z`) also populates it (`||sym(Psi)|| = 9.402e-06` at `delta = 1e-3`, linear). **Negative control:** a `tau`-**even** offset `delta * (i A_0) (x) alpha_x` in `h_0` leaves `h_0` `tau`-fixed (`tau(h_0') - h_0' = 0.000e+00`) and does **not** unlock the channel — `||sym(Psi)|| <= 4.08e-16`, `|Z'(0)| <= 5.73e-22`, at `delta` up to `1.0`. The channel is live and it is `tau`, and only `tau`, that gates it.

**(vi) Independent checks.**

```
central finite difference of Z(a) vs the slot sum, class-leaving:
      slot-sum = 3.307316759e-08 - 6.784123767e-08 i
      fin-diff = 3.302358387e-08 - 6.782907569e-08 i     |diff| = 5.1e-11  (O(h^2), h=1e-5)
exact linearity in the class-leaving amplitude eps:
      eps = 1, 0.5, 0.1, 0.01  ->  |Z'(0)|/eps = 7.547362e-08  (all digits identical)
additivity of the single functional:
      | Z'[J_in + J_leave] - Z'[J_in] - Z'[J_leave] | = 1.497e-22
Lemma 1 survives the class-leaving falsifier (T J T = +J for ANY spatial factor):
      | D'_{+sqrt2}(0) - D'_{-sqrt2}(0) | = 2.841e-21
robustness:
      envelope B : in-class 1.224e-37   class-leaving 8.485e-07
      N_t = 24   : in-class 7.598e-38   class-leaving 7.323e-08
      N_t = 96   : in-class 2.152e-38   class-leaving 7.605e-08
```

---

## 5. VERDICT

```
SAME APPARATUS
```

**Reason, for a future reader.** At first order in `a` the entire reading collapses to one exact identity: `Z'(0) = integral dt tr[Phi(t) J(t)]`, where the detector kernel `Phi(t) = -i sum_lambda w_lambda D_lambda(0) u_lambda(t) G_lambda u_lambda(t)^dagger` is assembled purely from `a = 0` data and is provably — and here, bitwise — the same object for every connection profile fed to it. `Z'(0)` is therefore a single linear functional with a single slot; the class-preserving connections lie in its kernel and the class-leaving ones do not. Restricted to the `alpha_x` channel the functional is `tr[Psi B]` for one `8 x 8` detector matrix `Psi`, and Lemma L4 is exactly the statement `sym(Psi) = 0` while `||antisym(Psi)||_F = 6.8e-2`. The class-leaving falsifier does not open a second path: it pairs against the other half of the same matrix, through the same Duhamel insertion, the same single Wick contraction, the same state kernel `G_lambda`, the same `D_lambda(0)`, the same pointer weights, the same `lambda`-sum, in the same per-`(lambda,k)` slots — which, verified directly, are live slots that read nonzero the instant `tau` is broken anywhere in the `a = 0` data while the connection stays strictly in class. The zero is a value in an existing slot, not an absent term. **Outcome A.** Control-4 v3 is a legitimate control, and Condition 2 follows.

**Scope, stated so the v3 spec cannot overclaim.** What v3 would certify is the teeth proposition — that the `Z'(0)` path on the completed-record object is live, and that Lemma 2's zero is a fact about the object rather than a dead instrument. What v3 would **not** certify is the original charter *intent* of A3, namely that breaking `P_x` (or `Theta`) is what causes the zero. That intent is now known false by L4 and is unachievable by any design; v2 already migrated away from it and v3 migrates further. The spec must say this plainly, or the control will be read as proving more than it does.

---

## 6. INPUTS FOR CONDITION 2 — magnitude derivation, honestly bounded

**Structural result that governs the magnitude.** Lemma 1 survives the class-leaving falsifier (verified above, `2.8e-21`), so exactly

```
Z'(0) = -(1/2) ( D'_{sqrt2}(0) - D'_{0}(0) )
```

The prediction is therefore a **difference of two near-equal record-dressed responses**, not a per-history response. Measured on `ell = 1`, envelope A, sea state, with the class-leaving part at 100% of the sealed connection strength:

```
D'_{+-sqrt2}(0) = 2.828733e-06 - 2.994512e-06 i     |D'| = 4.119e-06
D'_{0}(0)       = 2.894879e-06 - 3.130194e-06 i     |D'| = 4.264e-06
fractional difference = 3.5%   ->   |Z'(0)| = 7.547e-08
suppression relative to max_lambda |w_lambda D'_lambda| = 28.2 x
suppression relative to max_lambda |dD_lambda|          = 56.5 x   (|Z'| / |dD| = 0.0177)
```

Second normalization, `delta B = i A_0` at unit operator norm:

```
max_lambda |dD_lambda| = 5.282e-02     |Z'(0)| = 4.823e-04     |Z'| / |dD| = 0.0091
```

**Derivation from the witnessed `|dD| ~ 1e-4`.** The transfer coefficient measured two ways is `|Z'(0)| / |dD| = 0.0091` and `0.0177`. Applying it:

```
central prediction:  |Z'(0)|  ~  (1e-2) x 1e-4  =  1e-6      [order 1e-6, spanning 1e-6 to 2e-6]
```

**Uncertainty, and why the window must be widened well past that.** Four independent sources, each documented:

1. **Envelope dependence of the suppression.** At fixed class-leaving amplitude, envelope B gives `|Z'(0)| = 8.485e-07` against envelope A's `7.547e-08` — an **11x** spread from the envelope alone, because `lambda v_B = 24` constant dresses the flow harder than envelope A's peak `11.80`, widening the `D'_{sqrt2} - D'_0` difference. The suppression factor is not a constant of the apparatus.
2. **Unrecorded normalization of the witnessed positive control.** The `|dD| ~ 1e-4` figure appears in `STAGE8_T7_GAMMA_REFUTATION_GATE_RESULT_V001.md` and `GAMMA_GATE_LEMMA_PROOFS_DRAFT_V001B.md` with **no recorded normalization** of the complex-Hermitian spatial factor, and the gate executor is not on disk. My own two normalizations span `|dD| = 4.3e-6` to `5.3e-2` — four decades — for the same physical apparatus. Anchoring a prediction to `1e-4` inherits that ambiguity in full unless v3 pins the class-leaving amplitude explicitly.
3. **Exact linearity in the class-leaving amplitude** (`|Z'(0)|/eps` constant to all digits). This is good news for design and bad news for evidential value: the magnitude is *dialable*. The v3 spec must pin `eps` before execution or the prediction is vacuous.
4. **Standing calibration debt.** Per the authorization: this lane's magnitude predictions have MISSED TWICE CONSECUTIVELY (P2 on the gate: predicted `O(1e-1)-O(1)` shape coefficient, measured `0.0202` / `0.0198`), while sign/outcome-class predictions have been reliable. The window must be stated **explicitly widened** for that reason and that reason named in the spec.

**Recommended frozen window for Condition 2(a):**

```
predicted |Z'(0)| under the class-leaving falsifier, with the class-leaving spatial
component pinned at 100% of the sealed connection strength (|| i B_I(t) ||_2 = || B_D(t) ||_2):

      CENTRAL   ~ 1e-6
      WINDOW      1e-8  <=  |Z'(0)|  <=  1e-4        (+-2 decades, EXPLICITLY WIDENED)

reason for the widening, to be stated in the spec: (i) an 11x envelope spread measured
directly in this lane; (ii) the unrecorded normalization of the witnessed |dD| ~ 1e-4,
which alone spans four decades in this lane's own runs; (iii) two consecutive
magnitude-scaling misses by this prediction family, per the standing calibration
requirement.
```

Additional inputs Condition 2 will want:

- **2(b) predicted unbroken behaviour:** `|Z'(0)| <= 1e-12` with enormous margin. Measured this run: `1.322e-37` (sealed `J`), `2.932e-21` (v2 variant), against the `1e-12` ceiling. Predict `<= 1e-18`; window `<= 1e-12` as pinned. No risk on this half.
- **Floor headroom warning:** the sealed floor is `|Z'(0)| >= 1e-9`. My most-suppressed measured value at 100% sealed strength is `7.5e-8` — only **1.9 decades** of headroom. A v3 that pins the class-leaving amplitude much below the sealed connection strength can fall under the floor for structural reasons having nothing to do with teeth. Pin the amplitude at or above 100%.
- **2(c) what would REFUTE teeth:** `|Z'(0)| < 1e-9` for the pinned class-leaving falsifier at 100% amplitude while `||J'||_2` clears the non-vacuity gate and `||antisym(Psi)||_F` is `O(1e-2)`. That combination would mean the `alpha_x` channel is annihilated in *both* `tau` gradings, i.e. a fifth protection, and the control would have no teeth. It is not what this lane predicts.
- **2(d):** the spec must record, in one place, that the falsifier was selected after three defeats, that the principal authorized it knowing this (`STAGE8_T7_GAMMA_GATE_CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001`), and that the frozen prediction plus the widened window is what restores its evidential value.

---

## Caveats on this lane's own numerics

My carrier is an **independent reconstruction from the sealed spec text** (A1/A2/A3 of `789338ad…`), not the sealed executor — which is not present on disk. Verified against sealed invariants where they exist (`h_0^2 = (3/(2 ell^2)) I` exact; `{S, alpha_x} = 0`; `lambda v_B = 24` exact; `w = (-1/4, 1/2, -1/4)`; v2 in-class protection reproduced at `2.9e-21` against the sealed lane's `<= 8.8e-21`). Absolute scales that depend on my quadrature — notably `||B_D||_2 = 5.75e-4` — are order-of-magnitude faithful, not seal-grade, and the magnitude window in §6 is widened partly on that account. **The verdict in §5 does not depend on any of these numbers**: it rests on the exact Duhamel identity `(**)`, on the `tau`-grading of the connection space, and on the fact that `Phi` is `J`-independent — all of which are algebra.
