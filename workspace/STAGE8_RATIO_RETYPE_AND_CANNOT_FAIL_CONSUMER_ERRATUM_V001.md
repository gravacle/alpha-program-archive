# Stage 8 Ratio Retype and Cannot-Fail Consumer Erratum v001

## Status

```text
erratum_record = true
sealed_sources_edited = 0
ratio_values_changed = false
ratio_type_reclassified = true
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## Retype

The ratios

```text
K_H/K_Q = 3/2
K_QH/K_Q = 1
```

remain exact. This artifact records that, per
`/Users/bgm/MB Work/alpha_supervision/RESULT_TRACE_COLLAPSE_THEOREM_AND_GRAVITY_GAUGE_IMPOSSIBILITY_2026-07-29.md`
(`a7b82f9a180945844b95dc3931a649591e7c7ad7449e26f035ce7f270cb50d5e`),
they are Cartan inner-product / trace-orthogonality facts, not dynamical
evidence.

The source records at lines 44-48 that, with `H = Q + C` and
`C = diag(1/3,1/3,-2/3,0,0)`, `Tr(QC)=0` gives `K_QH = K_Q`, while
`Tr(C^2)/Tr(Q^2)=1/2` gives `K_H/K_Q = 3/2`.

## Parent Producer Cannot-Fail Gates

The parent producer
`/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/scripts/derive_alpha_br_common_induced_coefficients_v001.py`
uses the ratios as pass predicates. Lines 242-244 compute

```text
projection_error = relative_error(
    data["em_stiffness"], (8.0 / 3.0) * data["su5_stiffness"]
)
```

and lines 263-272 include these pass clauses:

```text
projection_error < 2.0e-14
relative_error(data["parent_flux_stiffness"], 1.5 * data["em_stiffness"]) < 2.0e-14
relative_error(data["qh_cross_stiffness"], data["em_stiffness"]) < 2.0e-14
```

The parent report
`/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/reports/alpha_br_common_induced_coefficients_v001.md`
states the resulting marker at line 3:

```text
PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN
```

and line 25 states:

```text
K_Q=(8/3)K_5
K_H=(3/2)K_Q
K_QH=K_Q
```

The registered retype is:

```text
producer_ratio_checks_are_cannot_fail_identity_checks = true
PASS_COMMON_BR_LOCAL_COEFFICIENT_FUNCTIONS_DEPTH_OPEN_is_weaker_than_it_reads = true
cannot_fail_class_new_seed_count = 2
```

The two seed cases are:

```text
seed_3 = K_Q=(8/3)K_5 identity over common inventory
seed_4 = K_H=(3/2)K_Q and K_QH=K_Q identity over common inventory
```

## Parent-Flux Saddle Consequence

The parent flux saddle report
`/Users/bgm/Documents/Documents - Brian’s MacBook Pro/New project/gravity_emergence_evidence_program/reports/alpha_br_parent_flux_local_saddle_v001.md`
uses, at lines 8 and 11:

```text
s(y,x)=C_V(x)y-2C_R(x)+K_H(x)/(8y).
y=C_R/C_V
K_H C_V=8 C_R^2
```

Line 15 says the report uses `H` and does not replace it with electromagnetic
`Q`. Under the trace collapse, the saddle's `y=C_R/C_V` equation is independent
of the cocharacter choice, and the `H` versus `Q` distinction enters this local
coefficient subsystem only through the rational trace factor `2` versus `4/3`.

This artifact records that fact as a consumer retyping. It does not alter or
rerun the parent report.

## Supervision Consumers Still Carrying the Old Reading

The following supervision artifacts still cite the ratios as executed dynamical
evidence:

- `/Users/bgm/MB Work/alpha_supervision/GRAVITY_EVIDENCE_REGISTER_V001_2026-07-29.md`,
  lines 117-119: "forced-ratio mechanism has been EXECUTED in-tree".
- `/Users/bgm/MB Work/alpha_supervision/WHAT_THE_GRAVITY_DISCOVERY_MEANS_2026-07-29.md`,
  lines 27-30: "forced ratios ... executed numerically".
- `/Users/bgm/MB Work/alpha_supervision/PLAN_TO_ALPHA_V006_2026-07-29.md`,
  lines 98-100: "forced ratios ... ALREADY EXECUTED".
- `/Users/bgm/MB Work/alpha_supervision/BOHM_CTP_ABSOLUTE_RESPONSE_ROUTE_SWEEP_2026-07-28.md`,
  lines 246-250: "not a hope - it is an executed in-tree result".

The single-source retraction at `/Users/bgm/MB Work/alpha_supervision/CONTINUATION_STATE.md`
lines 2347-2353 says those ratios were reported as executed in-tree but are
Cartan inner-product ratios carrying no dependence on `x`, the `I_n` integrals,
or the heat-kernel computation. That retraction is supervision-state only; this
artifact records the inconsistency in the governing chain and edits none of the
supervision sources.

## Detector Gap

Before this task, `corpus_check.py` reported two `cannot_fail_checks` findings.
It was blind to the two parent-tree ratio seeds for two reasons:

```text
blind_reason_1 = original cannot_fail_checks scanned archive scan_roots, not parent recovery files
blind_reason_2 = original patterns targeted scale-orbit and hand-entered exponent cancellations, not relative_error predicates over identities from the same inventory
```

The detector is extended in the archive task to scan bounded parent recovery
files and catch these two seed patterns. The detector remains a reporter; it
does not decide the scientific status of any result.

## Register Payload

```text
ratios_exact = true
ratios_dynamical_evidence = false
producer_pass_predicates_retyped_as_cannot_fail = true
four_supervision_consumers_inconsistent_with_retype = true
sealed_supervision_consumers_edited = 0
detector_seed_cases_named = true
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

