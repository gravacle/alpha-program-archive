# Stage-8 T7 ER-Fork Kappa-Insensitivity Bound Spec V002

Date: 2026-07-25 (late evening)

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

Append-only successor to STAGE8_T7_ER_FORK_KAPPA_INSENSITIVITY_BOUND_
SPEC_V001 (seal 277654ee…), which the hostile pre-execution review
returned NOT_READY with three blocking findings (review record:
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-25_er_insensitivity_
spec_v001_NOT_READY.md). V001 is preserved as a failed draft; it was
never executed. Every V001 defect is repaired here exactly as the review
prescribed. Brian's scope decision (option 2 first; the gate selects
nothing; option-3 conditionality never absorbed silently) carries over
unchanged, as do the pinned authorities, the sealed carrier (n=2,
ell=1 — the only independently verified comparison carrier), the frozen
stencil, and the no-selection fences.

## Corrections of record (review findings 1-3)

1. AMPLITUDE CONVENTION (finding 1): Z denotes the RAW completed-record
   amplitude as stored in the sealed v002 comparison tables. The sealed
   N=96 baseline moduli on this carrier are witnessed as approximately
   5.918e-4 (ER-A mixed), 6.467e-3 (ER-A pure), 6.265e-3 (ER-B mixed),
   6.791e-2 (ER-B pure) — far below 1/4. The V001 fence |Z(0)| >= 1/4 is
   DELETED. The stencil below is invariant under any constant amplitude
   normalization (its coefficients sum to zero), so no BID normalization
   is applied or needed; error propagation uses witnessed raw moduli.
2. THRESHOLD REFOUNDATION (findings 2, 4): theta_amp = 5e-5 is the
   certified tolerance of the SEALED FINITE COMPARISON LANE on this
   carrier — explicitly NOT the battery's resolution (the battery
   demands certified enclosures of width < 1e-8). Consequently this gate
   can certify RESOLVABLE_BY_BATTERY (a fortiori: the battery is
   strictly finer) but can NEVER certify battery-moot. The V001 MOOT
   verdict is removed as unreachable in principle at this precision.
3. D1 RESTATEMENT (finding 3): the sealed comparison executor contains
   no connection term; its rows are a = 0. The regression obligation is
   restated accordingly.

## Frozen definitions

Stencil (unchanged): a in {-7/100, 0, +7/100}; h = 7/100; coefficients
c = (-1, +2, -1) applied to -log|Z|, divided by h^2 = 49/10000. The
magnitude 7/100 reuses the sealed Phase-A value; the negative node is
symmetry-determined (review note 7).

```text
kappa_proxy(ER, state) =
  [ -log|Z_ER(+h)| + 2 log|Z_ER(0)| - log|Z_ER(-h)| ] / h^2
```

computed at each frozen resolution; the N=96 primary value is the
headline, with certified error from the frozen formula below.

Connection assembly (review finding 5 / connection check — all four
choices pinned):

```text
(i)   Strang step order imported from the sealed Phase-A spec exactly:
      F = exp(-i h0 dt/2); A_op = exp(-i a J(t_k) dt/2);
      G_lambda = exp(-i lambda v(t_k) M(t_k) (x) S dt);
      Step_lambda = F A_op G_lambda A_op F, chronological over the
      sealed comparison midpoints;
(ii)  the record-eigenvalue-0 history (lambda = 0) is propagated by full
      time-stepping F A_op A_op F at every midpoint whenever a != 0; the
      sealed exp(-i h0 T) shortcut remains valid and is used ONLY at
      a = 0 (where it is exact);
(iii) B_D(t_k) = Q b_D(t_k, .) Q matrix elements are evaluated with the
      sealed comparison lane's own frozen ball quadratures (primary and
      independent realizations as sealed; supp b_D(t, .) is exactly the
      ball of radius r(t)); J(t) = -B_D(t) (x) alpha_x per the Phase-A
      spec, unit charge, restricted to this carrier;
(iv)  certified per-amplitude error at each stencil node, per envelope
      and state (frozen formula, outward-rounded):
        e(node) = |Z_96 - Z_48|/3
                  + |Z_96_primary - Z_192_independent|
                  + 1e-12;
      per-node log error bound: e(node)/(|Z_96(node)| - e(node));
      delta_kappa(ER, state)
        = [ sum_i |c_i| * e(node_i)/(|Z_96(node_i)| - e(node_i)) ] / h^2.
```

Integrator resolutions: sealed comparison pair — primary Strang
{24,48,96}, independent midpoint {96,192} — both states (pure, mixed),
both envelopes, all three stencil nodes.

## Frozen thresholds (per-state floors from witnessed moduli)

The resolution floor of the 5e-5 finite lane, per state, is frozen as a
FORMULA evaluated in exact rational arithmetic on witnessed values (the
V001 numeric constant is void; review finding 2 repair):

```text
theta_amp = 1/20000  (= 5e-5, exact rational);
minZ(ER, state) = certified lower bound of min over the three stencil
                  nodes of |Z_ER,96(node)|
                  (outward-rounded: |Z_96| - e(node));
floor(ER, state) = (2/49) / ( minZ(ER, state) - 1/20000 );
floor(state)     = max( floor(ER-A, state), floor(ER-B, state) ).
```

Derivation recorded (review THETA_CHECK adopted): per-amplitude error
e propagates to each log node as at most e/(|Z|-e); the stencil
numerator carries coefficient sum |c| = 4; dividing by h^2 = 49/10000
gives 4*(1/20000)*(10000/49) = 2/49 as the exact prefactor.
Self-check 1: at minZ = 1/4, floor = (2/49)/(1/4 - 1/20000)
= 0.1633... — the review's 16e/h^2 worst case, recovered.
Self-check 2: at minZ = 6.791e-2 (ER-B pure witnessed), floor
= 0.6016... — the review's ~0.60, recovered.
Expected floors from the witnessed a=0 moduli (context, not binding):
pure ~ 6.4 (dominated by ER-A), mixed ~ 75 (dominated by ER-A).

Division-safety fence: if any witnessed node has
|Z_96(node)| - e(node) <= 2 * theta_amp, the gate BLOCKS (no stencil
substitution, no threshold motion).

## Obligations

```text
D1: recompute the sealed comparison rows AT a = 0 (the sealed gate's
    actual content), both envelopes, both states; agreement with the
    sealed v002 tables at the sealed 5e-5 discipline — drift blocks;
D2: compute Z_ER(a) at the three stencil nodes, both envelopes, both
    states, all frozen resolutions, with the pinned assembly (i)-(iii);
D3: form kappa_proxy per envelope and state at N=96; certified
    difference interval |Delta kappa_proxy(state)| with error
    delta_kappa(ER-A) + delta_kappa(ER-B) per formula (iv), lower bound
    floored at 0;
D4: per state, compare the certified LOWER bound of
    |Delta kappa_proxy(state)| against floor(state), both computed in
    exact rational arithmetic from the emitted witnessed values;
D5: emit every raw amplitude, tail, witnessed modulus, floor, bound,
    and per-state comparison; no aggregation that hides a state; the
    already-sealed amplitude-level facts (|Delta Z| = 6.1e-2 pure /
    5.7e-3 mixed at a = 0, both far above theta_amp) are recorded as
    CONTEXT and trigger no verdict (review finding 6 repair).
```

## Predeclared verdicts

```text
ER_FORK_RESOLVABLE_BY_BATTERY
  iff for ANY state the certified lower bound of
  |Delta kappa_proxy(state)| > floor(state)
  (a fortiori: the battery's certified enclosures are strictly finer
   than this lane);
ER_FORK_NOT_RESOLVED_AT_FINITE_LANE_PRECISION
  otherwise. This verdict is explicitly NOT battery-moot: it certifies
  only that the 5e-5 finite lane cannot distinguish the two envelopes'
  kappa-proxy curvatures. Establishing true battery-moot would require
  battery-grade certified enclosures on this difference — a separate
  gate requiring Brian's decision;
ER_FORK_INSENSITIVITY_GATE_BLOCKED
  on authority drift, D1 failure, undefined log, or the
  division-safety fence.
```

## Frozen predictions (calibration record; grounds stated)

```text
P1: mixed state returns NOT-resolved (floor ~ 75 from the witnessed
    5.918e-4 ER-A modulus; a curvature difference that large is not
    supported by any sealed fact);
P2: pure state is the only plausible RESOLVABLE channel (floor ~ 6.4);
    grounds for exceeding it are weak — no sealed artifact constrains
    the connection curvature on this carrier — so per the calibration
    ledger (this lane errs optimistic) the frozen prediction is
    NOT_RESOLVED for the pure state as well;
P3: overall verdict = ER_FORK_NOT_RESOLVED_AT_FINITE_LANE_PRECISION.
```

If P3 holds, the recorded follow-up fork is Brian's: (α) battery-grade
exact-enclosure gate on the difference (costly, could still certify
either way), or (β) carry ER-A as the disclosed premise with the
conditionality clause stated on every downstream headline. Neither
follows automatically.

## Fences

Unchanged from V001 (no selection under any verdict; no kappa_record;
no function of any proxy beyond the frozen comparisons; no measured
constant; fresh-context execution from this sealed text; commitment-
first blind reproduction of the load-bearing difference numbers before
the result seals). Additionally: no threshold, floor formula, stencil,
or assembly choice may be revised after any Z_ER(a != 0) value exists.

## Protected status

```text
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
er_fork_insensitivity_bound_computed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
