# Stage-8 T7 Gamma-Gate Spec Repair Amendment V001

Date: 2026-07-25 (late night)

## Status

```text
APPEND_ONLY_PRE_EXECUTION_AMENDMENT
```

Repairs the sealed gate spec STAGE8_T7_GAMMA_REFUTATION_AND_PARITY_
LEMMAS_GATE_SPEC_V001 (5f7e9965…, seal verified) per its hostile
pre-execution review (verdict NOT_READY; four blocking findings, five
conditions; recorded in the supervision directory). The spec is
preserved unexecuted; every repair below narrows or corrects
pre-execution; no prediction is revised (P1 NONZERO stands, per the
principal's non-revision order).

## R1 - Lemma 2 operator (review finding 1)

T' is redefined as the genuine involution

```text
T' := P_x (x) (i gamma^1),    T'^2 = +I,  T' Hermitian,
```

with identical conjugation action (verified by the review): [T', h_0] = 0,
T' (M (x) S) T'^{-1} = +(M (x) S), T' J T'^{-1} = -J. All Lemma-2
identities are stated and verified in conjugation form T' X T'^{-1}.
Lemma 1 is untouched (T = I (x) gamma^5 is already involutive; its
statement stands as sealed).

## R2 - Lambda-odd control tuple (review finding 2)

The lambda-odd weight vector is pinned by an explicit lambda-indexed
table under the sealed ordering (-sqrt2, 0, +sqrt2):

```text
w~(-sqrt2) = -1/(2 sqrt 2);  w~(0) = 0;  w~(+sqrt2) = +1/(2 sqrt 2)
(w~(lambda) = lambda/4; moments 0, 1, 0).
```

The spec's unindexed tuple text is void; no executor may re-pair it.

## R3 - Toy closed form corrected (review finding 3)

The pinned toy assembly is corrected of record to the general-phase
form (theta = sqrt2 sigma(1)):

```text
kappa = Jbar^2 * Re{ [1 - 2 e^{-i theta} Phi(sqrt2)] / [1 - e^{-i theta}] }.
```

The gamma memo's displayed formula is valid only at real e^{-i theta}
(all its checks were at theta = pi); its published kappa_B = 1.802 is
SUPERSEDED — the true toy value is kappa_B = 0.534 (verified two ways
by the review). The memo's conclusion is UNAFFECTED: the envelope
difference persists (kappa_A = 0.707 vs 0.534, difference 0.173, inside
the O(1e-1)-O(1) window), and B3/control-5 requires the corrected
assembly to exhibit it symbolically. Prediction P2's window is
unchanged and still traced.

## R4 - B1 definition cluster frozen (review finding 4)

For the three-site fixture computation B1:

```text
(a) RECORD: single qutrit record with the sealed A3 spectral data
    (c, P_lambda, p, w) — a single-record adaptation of the fixture;
    the sealed two-record regression is NOT re-executed and its
    correlated-record structure stays out of scope (control 6).
(b) MASK: the M analogue is the sealed fixture mask diag(1,1,0), one
    unit pulse, with the fixture's sealed S analogue -i gamma^0 gamma^5
    and connection direction as sealed in its executor (3d8aea1a…).
(c) FIXTURE PARITY: the T' analogue is (ring reflection j -> 1-j)
    (x) (i gamma^1) — the reflection that fixes mask diag(1,1,0)
    (review-verified); the Lemma-2 fixture residual check uses exactly
    this operator.
(d) STATE: the verdict-deciding functional omega is the fixture
    Dirac-sea projector with the 4-dim kernel EXCLUDED (kernel
    occupation 0); this convention is manifestly invariant under both
    T and T' (the kernel is a symmetry-invariant subspace) and the
    executor must verify that invariance at machine precision. A
    second emission with kernel occupation 1/2 (mixed analogue) is
    computed and reported; agreement is NOT required for the verdict —
    any disagreement is emitted and preserved.
(e) The Hermite-carrier A2 residual checks stand as sealed (both
    pinned states there are review-verified T- and T'-invariant; the
    n=2 carrier has no zero modes).
```

## R5 - New GATE_BLOCKED triggers and fences (review findings 5, 6, 9)

```text
ZERO_DENOMINATOR: F_v(sqrt2) = F(0) exactly on any test bed => blocked,
  labeled obstruction (the completed-modulus zero case).
RE_IM_CORNER: kappa_A - kappa_B = -Re[Delta_Xi] exactly; the verdict
  arms are re-scoped to Re[Delta_Xi]: GAMMA_REFUTED_NONZERO fires only
  on Re[Delta_Xi] != 0 certified. The corner Re[Delta_Xi] = 0 with
  Im[Delta_Xi] != 0 (record-level kappa insensitivity HOLDS while Xi
  differs) is mapped to GATE_BLOCKED_PENDING_PRINCIPAL — it is
  escalated to Brian with both parts reported, never silently resolved
  in either direction. Re and Im are always reported separately.
B2 EXPECTATION PINNED: on the one-dimensional comparator everything
  commutes, log D is linear in a, hence H_v = H(0) = 0 and
  Xi(v_A) = Xi(v_B) = 0 identically; any B2 deviation from exact zero
  is a GATE_BLOCKED trigger (apparatus fault, not evidence).
```

## R6 - Remaining conditions (review findings 7, 8, 11, 14)

```text
Hashes pinned: envelope comparison spec = 4059eff522426d06d41d2a0542
ddf6be309867bd077491d84c6998b2098ede31 (no adjacent seal exists on
disk; this pin is its authority of record for this gate); critical-path
scope correction = 9410ee80ff89beed4e133f75fcdb952d059f3386df12069793
b5d60895d15486; principal disposition file hash computed and recorded
by the executor before execution.
Broken-P_x teeth: absolute floors — broken variant |Z'(0)| >= 1e-9 AND
unbroken |Z'(0)| <= 1e-12, separately.
Part-B result artifact: STAGE8_T7_GAMMA_REFUTATION_RESULT_V001.
Certified-enclosure clarification: exact-rational outward enclosures
(Fraction arithmetic) that exclude zero ARE admissible nonzero
certificates; the fence forbids only uncertified floating-point values
deciding a verdict. GAMMA_SURVIVES_EXACT_ZERO remains reachable only
via a genuine closed form (the review's decidability analysis is
adopted: the v_B branch is closed-form; the v_A branch certifies
NONZERO by certified partial sums with the pi^(N+1)/(N+1)! tail bound,
and routes truth-is-zero-or-too-small to GATE_BLOCKED).
```

## Protected status

```text
ER_A_selected = false
ER_B_selected = false
record_parity_lemmas_sealed = false
gamma_refutation_computed = false
kappa_record_computed = false
alpha_computed = false
proof_authorized = false
```
