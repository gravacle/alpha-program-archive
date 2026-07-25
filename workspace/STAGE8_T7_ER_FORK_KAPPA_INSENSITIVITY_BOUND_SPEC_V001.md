# Stage-8 T7 ER-Fork Kappa-Insensitivity Bound Spec V001

Date: 2026-07-25 (evening)

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

Authorized by Brian's scope decision (relayed 2026-07-25): BEFORE any
selection spec, test the BOUNDED question — does the ER-A/ER-B difference
propagate to the kappa_record chain ABOVE or BELOW the resolution the
Stage-8 battery actually certifies? This gate SELECTS NOTHING. Its only
outputs are certified difference bounds against thresholds frozen here.
If the fork proves moot at battery resolution it dissolves without ever
being selected; if resolvable, the certified bound quantifies exactly
what the disclosed ER-A premise costs.

Recorded per the same decision: if the program ultimately carries ER-A as
a disclosed premise (option 3), every headline result downstream of
kappa_record is CONDITIONAL ON ER-A and must say so explicitly — this
conditionality may not be absorbed silently.

## Pinned authorities

| Role | Path |
|---|---|
| ER status (premise/alternative) | `STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md` |
| Superseded scalar adjudication | `STAGE8_T7_INTRINSIC_ACTION_ENVELOPE_ADJUDICATION_SPEC_V001.md` + result JSON |
| Sealed finite ER comparison (carrier, envelopes, tolerance) | `STAGE8_T7_ENVELOPE_REALIZATION_COMPARISON_SPEC_V001.md`, `..._NUMERICAL_FAILURE_V001.md`, `..._NUMERICS_SUCCESSOR_SPEC_V001.md`, `stage8_execution/work/T07_envelope_realization_comparison_v002.json` + verification |
| kappa_record semantics + battery resolution discipline | `STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md` (T7, T14, T15, Frozen Numerics) |
| Measure/marginal identities | `STAGE8_T7_INTRINSIC_ACTION_ENVELOPE_ADJUDICATION` result (rho M = w A retained as measure-level fact) |

Exact hashes of every authority above are computed and recorded by the
executor before any computation; drift blocks.

## Frozen definitions

Envelope candidates, exactly as sealed in the comparison spec (no
retyping here):

```text
ER-A: write envelope tau_R w(t) M(t)  (w(t)=32 r(t)^3; disclosed premise);
ER-B: write envelope tau_R rho M(t)   (rho=24/pi; unexcluded alternative).
```

Carrier and numerics: the SEALED comparison carrier and resolutions
(n=2, ell=1; primary Strang steps {24,48,96}; independent midpoint steps
{96,192}; both quadratures; pure and mixed states as sealed). Everything
identical between the two branches except the envelope. No new carrier,
state, gauge, or quadrature choice is admitted.

Susceptibility proxy (the kappa-chain-relevant functional; NOT
kappa_record — no intensive limit is taken and kappa_record_computed
stays false): with the sealed unit-charge connection J of the Phase-A
spec restricted to this carrier, frozen symmetric stencil

```text
a in {-7/100, 0, +7/100};
kappa_proxy(ER) =
  [ -log|Z_ER(+7/100)| + 2 log|Z_ER(0)| - log|Z_ER(-7/100)| ]
  / (7/100)^2;
```

where Z_ER(a) is the completed-record amplitude on the sealed carrier
under envelope ER with connection strength a, computed at each frozen
resolution. The stencil magnitude 7/100 reuses the sealed Phase-A
history value; no new discretionary constant is introduced. If any
|Z_ER(a)| vanishes or the log is otherwise undefined at any frozen
resolution, the gate returns BLOCKED (no stencil substitution).

## Frozen thresholds (the battery's operative resolution)

```text
theta_amp   = 5e-5
  (the predeclared tolerance of the sealed envelope-comparison gate —
   the finest amplitude distinction any sealed Stage-8 artifact
   certifies);
theta_kappa = 5e-5 * 4 / (7/100)^2   = 4.0816...e-2 exact rational 2000/49
  (theta_amp propagated through the frozen second-difference stencil:
   worst-case log-derivative amplification bounded by 1/min|Z| <= 4 on
   the sealed tables' completed amplitudes at a=0 — the factor 4 is
   frozen here from the sealed baseline |Z(0)| >= 1/4 on this carrier;
   if the executed |Z(0)| < 1/4 the gate BLOCKS rather than adjusts).
```

Both thresholds are frozen now, before any new number exists. They may
not be revised by outcome; a successor revising them must cite this seal.

## Obligations

```text
D1: recompute the sealed comparison rows (both envelopes, a = +7/100
    case as sealed) and verify agreement with the sealed v002 tables at
    the sealed 5e-5 discipline — drift blocks;
D2: compute Z_ER(a) for both envelopes at the three frozen stencil
    values, both states, all frozen resolutions, with the sealed
    primary/independent integrator pair and sealed tolerance 5e-5;
D3: form kappa_proxy(ER-A), kappa_proxy(ER-B) and the certified
    difference |Delta kappa_proxy| with outward-rounded error bounds
    from the observed integrator tails (second-order Richardson bound,
    the sealed convergence discipline);
D4: compare, per state: certified upper bound of |Delta kappa_proxy|
    against theta_kappa, and certified lower bound against theta_kappa;
    likewise |Delta Z| upper/lower bounds against theta_amp;
D5: emit every raw value, tail, and bound; the difference verdict per
    state; no aggregation that hides a state.
```

## Predeclared verdicts

```text
ER_FORK_MOOT_AT_BATTERY_RESOLUTION
  iff the certified UPPER bound of |Delta kappa_proxy| < theta_kappa
  AND every certified |Delta Z| upper bound < theta_amp, for BOTH states;
ER_FORK_RESOLVABLE_BY_BATTERY
  iff a certified LOWER bound of |Delta kappa_proxy| > theta_kappa
  OR a certified |Delta Z| lower bound > theta_amp, for ANY state;
ER_FORK_INDETERMINATE_AT_FROZEN_RESOLUTION
  otherwise (honest middle; no threshold motion);
ER_FORK_INSENSITIVITY_GATE_BLOCKED
  on authority drift, undefined log, |Z(0)| < 1/4, or any failed
  discipline check.
```

## Frozen predictions (calibration record; err toward differences)

```text
P1: verdict = ER_FORK_RESOLVABLE_BY_BATTERY (the sealed N=96 tables
    already show |Delta Z| = 6.1e-2 pure / 5.7e-3 mixed, three and two
    orders above theta_amp);
P2: |Delta kappa_proxy| certified lower bound exceeds theta_kappa in the
    pure state;
P3: the mixed state also resolves, with smaller margin.
```

Predictions bind nothing; refutation is reported, never repaired.

## Fences

No selection: neither ER_A_selected nor ER_B_selected may be set by this
gate under ANY verdict; a RESOLVABLE verdict only licenses a future,
separately sealed selection or premise-disclosure decision routed
through Brian. No kappa_record value is computed (finite proxy only; no
intensive limit; the battery's T15 single-occurrence rule is untouched).
No function of any proxy value beyond the frozen difference comparison.
No measured constant, coupling target, or alpha transform may be read,
used, or compared. Execution by a fresh-context lane from this sealed
text; load-bearing difference numbers get a commitment-first blind
reproduction before the result seals.

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
