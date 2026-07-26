# Stage-8 T7 Control-4 Condition-1 Result — SAME APPARATUS V001

Date: 2026-07-26

## Verdict

```text
CONDITION_1_SAME_APPARATUS
```

Answering the principal's gating question in STAGE8_T7_GAMMA_GATE_
CONTROL4_V3_CONDITIONAL_AUTHORIZATION_V001: a perturbation leaving the
L4 antiunitary reality class DOES exercise the same apparatus control-4
is chartered to certify. Outcome A. Condition 2 follows.

The full typed argument is recorded verbatim at
/Users/bgm/MB Work/alpha_supervision/CONDITION1_SAME_APPARATUS_ARGUMENT_
SEALED_TRANSCRIPT_V001.md. Its verdict rests on algebra, not on the
lane's numerics (which are an independent reconstruction from the sealed
spec text and are disclosed as order-of-magnitude, not seal-grade).

## The argument in one identity

At first order in a, the whole reading collapses to

```text
Z'(0) = integral_0^1 dt  tr[ Phi(t) J(t) ],
Phi(t) = -i sum_lambda w_lambda D_lambda(0) u_lambda(t) G_lambda u_lambda(t)^dagger,
G_lambda = (1 - C + C u_lambda)^{-1} C u_lambda.
```

Phi is assembled ENTIRELY from a = 0 data and contains no reference to J.
Z'(0) is therefore a SINGLE LINEAR FUNCTIONAL WITH ONE SLOT, and J is
what goes into it. Verified bitwise: max over all (lambda, k) and all
four probe runs of ||Phi_class - Phi_other||_inf = 0.000e+00 — not the
same code path, the same numbers.

Restricted to the alpha_x channel, tr[Phi (B (x) alpha_x)] = tr[Psi B]
for one 8x8 detector matrix Psi. The connection space splits into
exactly two eigenspaces of the transpose class tau(X) = Omega X^T Omega
(Omega = I (x) alpha_y), orthogonal in the trace pairing:

```text
tau-ODD  : {real symmetric} (x) alpha_x   <- the L4 class (sealed J, v1, v2)
tau-EVEN : {i real antisym} (x) alpha_x   <- the class-leaving direction
sym(Psi)     reads the class ;  antisym(Psi) reads the class-leaving part.
```

LEMMA L4 RESTATED AS A DETECTOR PROPERTY: sym(Psi) = 0 pointwise in t,
per lambda, for the sealed a = 0 data — while ||antisym(Psi)||_F =
6.809e-02. The detector is antisymmetric; it is not small.

## Why this is SAME and not DIFFERENT

The class-leaving falsifier pairs against the OTHER HALF OF THE SAME
MATRIX: same index pair (lambda, k), same Phi, same u_lambda(t), same
single Wick contraction (only one exists at first order in a), same
state kernel G_lambda, same D_lambda(0), same pointer weights, same
lambda-sum, same spinor channel, same tensor factor. The only difference
is which half of one matrix the input projects onto — literally a
reality argument (real vs imaginary part of the Hermitian spatial
factor). This is the principal's criterion (i), not (ii).

THE DECIDING EVIDENCE — the zero-reading slot is LIVE, not absent:
holding the IN-CLASS J fixed and perturbing the a = 0 data by any
tau-ODD amount populates sym(Psi) and makes the same slots read nonzero,
exactly linearly (base point a_0: |Z'| 3.7e-13 -> 7.3e-11 over a 200x
span, ratio 200; in-class background delta: ||sym(Psi)|| 2.4e-5 ->
2.4e-3 over 100x). NEGATIVE CONTROL: a tau-EVEN offset leaves h_0
tau-fixed and does NOT unlock the channel (||sym(Psi)|| <= 4.1e-16,
|Z'(0)| <= 5.7e-22, at delta up to 1.0). The channel exists, accepts a
value, and is set to zero by L4 — a value in an existing slot, not an
absent term.

Slot-resolved corroboration (144 slots): in-class sealed J reads
~1e-38 in EVERY slot (per-slot vanishing, not a +-lambda cancellation);
control-4 v2 reads ~1e-21 (reproducing the sealed lane's <= 8.8e-21);
the class-leaving probe reads 1.5e-7 to 3.2e-7 in the SAME slots
(22/48 above 1e-12 per lambda). A mixed connection B_D + i||B_D||A_0
gives Z'(0) identical to the pure class-leaving part to every printed
digit: the in-class component contributes exactly nothing.

## Scope — binding on the v3 spec, so it cannot overclaim

```text
v3 WOULD certify the TEETH proposition: the Z'(0) path on the completed-
   record object is live, so Lemma 2's zero is a fact about the object
   and not a dead instrument.
v3 WOULD NOT certify A3's original INTENT — that breaking P_x (or
   Theta) is what CAUSES the zero. That intent is known false by L4 and
   is unachievable by ANY design; v2 already migrated away from it and
   v3 migrates further. The v3 spec must state this plainly.
```

## Protected status

```text
control4_v3_condition1_satisfied = true
control4_v3_condition2_spec_sealed = false
gamma_refutation_computed = false
alpha_computed = false
proof_authorized = false
```
