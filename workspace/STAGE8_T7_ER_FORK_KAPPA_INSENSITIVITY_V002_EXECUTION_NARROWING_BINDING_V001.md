# Stage-8 T7 ER-Fork Kappa-Insensitivity V002 Execution Narrowing Binding V001

Date: 2026-07-25 (night)

## Status

```text
APPEND_ONLY_PRE_EXECUTION_NARROWING
```

Implements the four conditions of the hostile review of the sealed V002
spec (verdict READY_WITH_CONDITIONS; record:
/Users/bgm/MB Work/alpha_supervision/REVIEW_2026-07-25_er_insensitivity_
spec_v002_READY_WITH_CONDITIONS.md). Sealed BEFORE any Z_ER(a != 0)
value exists, as the review requires. It only narrows the sealed V002
spec (1e79b0b7…, seal verified); nothing is relaxed; no sealed number
changes.

## N1 - RESOLVABLE floor is the two-branch SUM (condition C1)

The verdict condition of V002 is narrowed to:

```text
ER_FORK_RESOLVABLE_BY_BATTERY
  iff for ANY state the certified lower bound of
  |Delta kappa_proxy(state)|
    > floor(ER-A, state) + floor(ER-B, state).
```

Rationale of record: a theta_amp-level ambiguity may shift each branch's
kappa_proxy independently; the max under-counts the coordinated case.
Expected sum-floors from the witnessed a=0 moduli (context, not
binding): pure ~ 6.96, mixed ~ 81.90.

## N2 - Error budget addend and log precision (condition C2)

The frozen per-node error formula gains the independent lane's own
error-to-truth addend, outward-rounded:

```text
e(node) = |Z_96 - Z_48|/3
          + |Z_96_primary - Z_192_independent|
          + |Z_192_independent - Z_96_independent|/3
          + 1e-12.
```

Log-enclosure precision is pinned: every transcendental evaluation
entering the exact-rational D4 comparison is carried at 50 significant
decimal digits with outward rounding to rational bounds; the enclosure
contribution per log node must be below 1e-12 and is emitted. Any
failure to meet it blocks rather than widens.

## N3 - RESOLVABLE scope note (condition C3)

Any result artifact reporting ER_FORK_RESOLVABLE_BY_BATTERY must carry,
verbatim:

```text
Scope: resolvable a fortiori at battery-grade precision on this same
finite proxy and carrier. This is NOT a demonstration that kappa_record
differs between envelopes (the proxy-to-kappa_record link is underived
and the intensive limit could contract a fixed-regulator difference),
and NOT an output of the sealed battery (which pins ER-A as disclosed
premise and never computes ER-B).
```

## N4 - Corrected self-check digit (condition C4)

The V002 self-check-2 display value is corrected of record: at
minZ = 6.791e-2 the floor evaluates to 0.60148 (4 s.f. 0.6015); the
V002 text's "0.6016..." was the 6.79e-2-rounded value. The floor is
frozen as a formula; no binding constant changes. The execution record
must carry this note.

## N5 - Execution and blind-reproduction protocol

Execution follows the program's derivation-gate precedent (the sealed
comparison v002 pattern): a fresh-context primary execution lane
implements from the sealed V002 text + this binding ONLY; a separate
fresh-context blind lane, running without access to any primary output,
independently computes the stencil amplitudes and kappa_proxy values
from the same sealed texts and emits its values BEFORE any comparison;
the construction lane compares, and the result seals only if the blind
lane's values agree with the primary within the sealed e(node) budgets.
Disagreement is preserved as a failure, never averaged.

## Protected status

```text
ER_A_selected = false
ER_B_selected = false
er_fork_insensitivity_bound_computed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
