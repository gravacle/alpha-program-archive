# Stage-8 T7 ER-Fork Kappa-Insensitivity Result V001

Date: 2026-07-25 (night)

## Verdict

```text
ER_FORK_NOT_RESOLVED_AT_FINITE_LANE_PRECISION
```

Issued under the sealed spec V002 (1e79b0b7…) and its execution
narrowing binding (seal verified), by the construction lane after the
N5 two-lane protocol. All three frozen predictions (P1, P2, P3) held.
This verdict is explicitly NOT battery-moot (V002 corrections of
record, item 2): it certifies only that the 5e-5 finite comparison
lane cannot distinguish the two envelopes' kappa-proxy curvatures.

## Machine artifacts (hash-pinned)

```text
stage8_execution/work/T07_er_fork_kappa_insensitivity_primary_v001.json
  (primary execution lane; sealed adjacent)
stage8_execution/work/T07_er_fork_kappa_insensitivity_blind_commit_v001.json
  (blind lane commitment, written before any comparison; sealed adjacent)
scripts/derive_stage8_t7_er_fork_kappa_insensitivity_primary_v001.py
  (primary executor; machinery file-copied from the sealed comparison
   lane, no module import)
```

## Results (N=96 headline; exact-rational D4; N1 sum-floors; N2 budgets)

```text
                     mixed            pure
kappa_proxy ER-A     1.1489e-8        1.2740e-8
kappa_proxy ER-B     6.8691e-9        6.9385e-9
|Delta| point        4.62e-9          5.80e-9
|Delta| certified LB 0                0
sum-floor (N1)       82.275           6.983
verdict per state    NOT resolvable   NOT resolvable
```

D1 regression: primary lane bit-identical to the sealed v002 a=0
tables (drift 0.0); blind lane max drift 3.502e-14. Division-safety
fence passed at every node; max 50-digit log-enclosure contribution
2.0e-40 (N2 met). e(node) budgets 2.55e-6 … 5.95e-5 per the four-addend
formula. N4 digit-correction recorded in the primary artifact.

N5 blind comparison (construction lane): inter-lane kappa_proxy
agreement 2.4e-10 … 2.8e-9 against kappa-level budgets of order 1-10 —
agreement by ~9 orders of margin. Both lanes issued the same per-state
conclusions independently.

## Physical observation of record (no promotion)

Both lanes independently found the completed-record three-history sum
cancels connection curvature to ~1e-13 while individual history
determinants move at ~1e-10: the near-zero kappa-proxy curvature at
a=0 on this carrier is STRUCTURAL, not numerical noise. The kappa-proxy
values (~1e-8) sit ~9 orders below the finite lane's certified floors.
No claim about kappa_record follows (the proxy-to-kappa_record link is
underived); this observation is recorded for the Phase-B and battery
lanes, not promoted.

## Consequence (per the sealed V002 P3 clause)

The recorded follow-up fork now lies with Brian:

```text
(alpha) commission a battery-grade certified-enclosure gate on the
        envelope difference (could certify either direction); or
(beta)  carry ER-A as the disclosed premise, with the conditionality
        clause stated on every headline downstream of kappa_record.
```

Neither follows automatically. This gate selected nothing.

## Protected status

```text
ER_A_selected = false
ER_B_selected = false
envelope_realization_derived = false
er_fork_insensitivity_bound_computed = true
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
