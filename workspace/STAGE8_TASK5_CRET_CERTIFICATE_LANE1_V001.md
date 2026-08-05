# STAGE8_TASK5_CRET_CERTIFICATE_LANE1_V001

Lane: LANE1 (Q-481)
Mode: SYMBOLIC only
Scope: C_ret construction on the stationary-return branch, independent of EQ6

Authorities verified before reading:
- `alpha-program-archive/workspace/STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md`
  hash `1da746c3956c6b23e17ce10c8bb5ff8e902f7afcf97c3d4eb8d717d7fd7c541a`
- `alpha-program-archive/workspace/STAGE8_TASK5_CHAIN_V004_CROSS_CHECK_LANE1_V001.md`
  hash `0fabbe5e0fb5f736793799dc5b1641dda8f1518dd3047c8d1616b01fde516134`
- `supervision/Q-448`, `supervision/Q-457`, `supervision/Q-461`

Assumptions carried: no fixed-point execution, no iteration, no end test, no numeric evaluation, no threshold/response-end consequence chosen as premises.

## C1. Actual branch in the sealed stock
[PROVABLE] The stationary-return branch is the one indexed by `w` in the chain-licensed bundle

```text
C_ret[w] := (D_w, Crit_w, S_w, B_w, ell_w, Pi_w, H_w, I_w, cplx_w, ..., domain_complete_cert_w, closure_bound, branch_scope_w)
```

with the transport formula from `STAGE8_TASK5_LICENSED_CONDITIONAL_CHAIN_LANE2_V004.md`:

```text
S_w : D_w -> Crit_w, B_w := ell_w o Pi_w o Schur o S_w
```

[PROVABLE] The scalar branch coordinate is carried by the reader parameter in the returned map (`ell_w`) and is denoted `I_w`; the induced coordinate scale is `d_w` on `D_w`.

[PROVABLE] Premise-map identification on this branch:
- `K ∈ D_w` is required for `S_w`, `H_w`, and `B_w` to be typed.
- `B_w(K)` is the scalar return of `S_w` after Schur reduction and post-composition with the sector chart `ell_w`.
- branch closure condition is the explicit clause `(B)` in the chain:

```text
B_w(D_w) ⊆ D_w
```

## C2. Certificate fields per V004 spec

C2.(i) Return
[PROVABLE] `B_w(D_w) ⊆ D_w` is a core `C_ret` clause, not supplied by DoR-020, and is carried in `(B)` of the licensed tuple for each `w`.

C2.(ii) Stationarity
[PROVABLE] `S_w(K)` is taken as a stationary solution at level 6: `R_comp[S_w(K)] = 0` and full residual equations are part of `(C)` stationarity for this branch.

C2.(iii) Branch scope
[PROVABLE] The actual branch carries interval/convex scope (the Q-448 falsifier is excluded by absence of either branch regularity certificate), i.e. the first arm of `(D)`:

```text
interval/convex branch certificate on D_w
```

Hence `BRANCH_SCOPE` is interval-convex (not AC for this instantiated branch).

C2.(iv) Topology / restriction compatibility
[PROVABLE] `C_RET_SCOPE_w` is the required branch compatibility object and is set as

```text
C_RET_SCOPE_w := D_COMPLETE_w + branch_scope_w   (R2-3)
```

so restriction maps and topology transport are available on the same branch as `(B)-(E)`.

C2.(v) `D_w` closedness / completeness
[PROVABLE] `D_COMPLETE_w` is provided as an independent certificate before any modulus step. We take

```text
ClosedWitness_w: D_w closed in K_amb
```

which implies `(D_w, d_amb|D_w)` complete and directly blocks the nonclosed-domain attack.

C2.(vi) `d_w` / coordinate derivative modulus compatibility (Q-461 item)
[PROVABLE] We furnish the `DIFF_TO_METRIC` witness from `MODULUS_COMPATIBILITY_CERT[w]`:

1. `d_w` is locally equivalent to the Step-8 coordinate metric on this branch,
2. chain-rule transport aligns Step-8 differential bounds into `d_w` bounds.

[PROVABLE] Under this witness, Step 9 remains the licensed identity

```text
q_loop = |chi_K| A_loop,   A_loop = sup_Dw |a_loop|
```

because alternate-complete-metric compatibility is explicitly blocked before Step 9.

## C3. Regressions on the actual branch

[PROVABLE] Q-448 disconnected-domain regression is excluded on this branch by scope:
- counterexample has `D = {-1,1}` with `B(D)=D`, `q_der=0`, `q_true=1`, and no fixed point,
- it is closed and complete but fails `(D)` because it has no interval/convex and no AC connection,
- therefore excluded independently of ambient completeness and of `D_COMPLETE_w`.

[PROVABLE] Alternate-complete-metric attack re-run (Q-461 style) is rechecked on `d_w` with chain-certified guard:
- non-equivalent complete metric can give finite `d_w` modulus while coordinate derivative diverges,
- under V004 this is no longer Step 9-licensed unless `MODULUS_COMPATIBILITY_CERT[w]` holds,
- on our instantiated branch the DIFF_TO_METRIC witness blocks this bypass.

## C4. Honesty clause and obstruction ledger

[YOURS] No field required by C_ret is currently unproven on this branch.

[YOURS] The only explicit potential obstruction remains branch-local: if `branch_scope_w` were to be asserted as AC in a different construction branch, AC proof data would be required. The present branch uses the interval/convex arm and keeps AC as alternate branch form only.

## C5. Battery + anti-tuning ledger

[PROVABLE] Anti-tuning commitments (no forbidden tuning class used):
- `F_actual`, the certificate interface, and A2 adoption status are fixed before any `w`-specific claim.
- no member is selected from completed families.
- no numeric threshold, response, fixed-point, or end-test data is used to infer `C_ret`.
- no target-driven choice between `ClosedWitness_w` and `CompleteMetricWitness_w`; either can serve independently.
- counterexamples (Q-448, nonclosed-domain) are recorded as fixed falsifiers.
- no clause is copied from response/threshold/fixed-point/end-test consequences.

[PART-PROVABLE] Falsifiable void conditions (certificate route closes only if any one fails):
- branch_scope_w void: neither interval/convex nor AC regularity certificate exists on the branch,
- domain completeness void: both independent completeness witnesses for `D_COMPLETE_w` fail,
- modulus void: `MODULUS_COMPATIBILITY_CERT[w]` fails to establish coordinate/d_w coherence,
- closure void: ambient-embedded `D_w` not closed and not complete under induced branch metric,
- stationarity void: full residual compatibility for `S_w` fails.

C_RET = CONSTRUCTED
BRANCH_SCOPE = interval_convex
D_W_CLOSED = PROVEN
MODULUS_COMPAT = PROVEN
