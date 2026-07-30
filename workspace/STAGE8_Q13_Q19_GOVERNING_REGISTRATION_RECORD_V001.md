# Stage 8 Q13-Q20 Governing Registration Record v001

Date: 2026-07-30

Status: APPEND_ONLY_GOVERNING_CHAIN_REGISTRATION. This artifact registers
supervision rows Q-13 through Q-20 and the paired principal rulings into the
governing cleanroom chain. The filename reflects the Paste-130 work package,
which asked for Q-13 through Q-19; the live-register check required by that
same package found Q-20 before this artifact sealed, so Q-20 is included here
to avoid publishing a stale "unruled consequence" record. This artifact does
not edit, amend, retire, or re-pose any sealed source directly. It records the
row authority that postdates the Paste-129 cleanroom artifacts.

## Timing Ground

`/Users/bgm/MB Work/alpha_supervision/EXECUTION_TRACKER.md:90-140` states the
standing timing guard. The key rule is at lines 133-136:

```text
before registering any supervision result into the governing chain, check its
write time against this table. If an artifact predates a register row that
touches its subject, register the row, not the artifact. Append-only means a
later row supersedes an earlier one -- it does NOT mean the most recently
registered text wins.
```

The same tracker records at lines 97-112 that Paste 129 was written at 03:07,
the cleanroom rows R-41 through R-45 were written 03:18-03:22, and Q-11 through
Q-15 landed later, through 06:08. Lines 115-120 state the consequence:

```text
ALL FIVE REGISTER ROWS Q-11 THROUGH Q-15 POSTDATE EVERY CLEANROOM ARTIFACT CODEX
WROTE TODAY.
```

Therefore this record registers the row/ruling state, not the earlier artifacts
as if they remained current. During the final live-register check for this
record, `QUESTIONS_SETTLED_REGISTER_V001.md` contained Q-20, which supersedes
Q-19's "unruled consequence" status for R-30/F2. The current register hash at
that check was `dfb2efe2823fb2483b3dda8ba53199aaea6bf8f32f8cb5b9c5c0c99146db8a49`.

## Q-13 Registered: Slot Classification And Three Freedoms

Source: `/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md`
(`5bdddc8cf8586411752720c91c5c15c60dd79f6d2c09b7fb213cae264f42b883`),
row Q-13.

Q-13 states the test at lines 461-463:

```text
does discharging the slot introduce a NEW DIMENSIONFUL, INDEPENDENTLY FIXED
quantity (scale-breaking, could select), or only an invariance / limit /
exhaustion / matching / protocol requirement (scale-covariant, cannot select)?
```

It classifies the slots at lines 465-477:

```text
FOUR SLOTS CAN BREAK A SCALE: 1 (absolute `T_R`), 2 (full gravitational action),
6 (functional regulator + finite renormalization), 13 (charged pole /
infraparticle threshold -- POLE BRANCH ONLY).
```

```text
TWELVE CANNOT FIX A NORMALIZATION UNDER ANY CIRCUMSTANCES: 3, 4, 5, 7, 8, 10,
11, 12, 15, 16, 17, 18.
```

It also states that slot 9 and slot 14 act on other freedoms at lines 468-470.
The three-freedom correction is at lines 504-513:

```text
F-scale, a multiplicative normalization -- the scaling orbit.
F-shift, an ADDITIVE offset (`c_R` / `K0`).
F-ratio, the dimensionless depth `x`, which is ALREADY scale-invariant.
```

The monotonicity caveat is registered from lines 527-534: at least eight
imposed conditions break scaling and fail by monotonicity with no interior root.
Thus a scale-breaker is necessary but not sufficient.

Reopen condition registered from lines 580-581:

```text
the slot classification is challenged at a specific slot with the obligation
text quoted, or a thirteenth slot is shown to carry a dimensionful
independently-fixed quantity.
```

## Q-14 Registered: Departure 2 Re-Scoped

Source: `QUESTIONS_SETTLED_REGISTER_V001.md` row Q-14 and
`/Users/bgm/MB Work/alpha_supervision/DEPARTURE_2_RESCALING_EXCLUSION_FOUR_CHANNEL_AUDIT_V002.md`
(`831878e241669677f5d3c6f26a1d8c136268e7becc5aefc337a2e8feb0ab44ab`).

Q-14 states the ruling at lines 593-595:

```text
THE DELETION WAS SUPERSEDED, NOT SILENT; THE REQUIREMENT IS LIVE AND STRONGER;
THE CHANNEL LIST IS FIVE, NOT FOUR; AND THE AUDIT IS AN ACCEPTANCE CHECK ON AN
OPERATOR THAT WAS NEVER BUILT.
```

The supersession note is quoted in the source at lines 597-602, citing
`primitive_record_cell_selection_principle_v002.md:3-16`; that file states at
lines 12-16:

```text
is valid only if the selected field configuration and the action partition are
already independent of `K_R`. A coupled matter-electromagnetic-gravitational
saddle need not have that property. Version 002 therefore replaces the direct
division rule with a joint saddle-and-closure selection problem. No numerical
cell or alpha value was evaluated between the two versions.
```

The live requirement is registered from `primitive_record_cell_selection_principle_v002.md:131-133`:

```text
changing an admitted boundary condition, measure, regulator, or action
partition changes `K_*` without a theory-derived exclusion;
```

The live target is registered from `results/primitive_record_cell_joint_selector_readiness_v001.json:54`:

```text
derive one complete target-independent Gamma_K and BR closure operator whose
joint stationary problem outputs Delta_tau(K) and a scalar C_record(K)
```

Reopen condition registered from Q-14 lines 634-635:

```text
`Gamma_K` and `C_record(K)` are constructed, at which point the five-channel
mutation audit becomes the acceptance criterion and should be run in full.
```

## Q-15 Registered: Beta Arm Refuted, K-Star Arm Unbuilt

Q-15 states the ruling at `QUESTIONS_SETTLED_REGISTER_V001.md:648-649`:

```text
NO. TWO DIFFERENT TARGETS, TWO DIFFERENT VERDICTS. The `beta` arm is refuted;
the `K_*` arm is unbuilt.
```

The parameter-count ground is at lines 651-653: `beta` does not appear in
`L_open`, so that argument is silent on `K_*`. The route-retirement ground is
also carried by the cleanroom recovery index at
`STAGE8_FIRST_OPENING_ROOT_PRINCIPLE_RECOVERY_INDEX_V001.md:69-79`:

```text
Whether a first-opening root can be formed from one microscopic CTP functional
is open, and the retired `L_open` subtraction may not be reused by renaming its
terms.
```

The live same-shape object is carried by
`primitive_record_cell_selection_principle_v002.md:91-104`, which introduces
`C_record(K)` and the positive-root condition. This registration preserves the
prohibition on reusing `L_open`.

## Q-16 Registered: Slot 12 Re-Posed As Scheme-Covariance

Authority:
`/Users/bgm/MB Work/alpha_supervision/SLOT12_SCHEME_COVARIANCE_PRINCIPAL_DECISION_2026-07-30.md`
(`028e355afc5f5d078ee39beb18de01269c57e09b85ba39a1721ebbf8e56ad451`).

The ruling is stated at the authority lines 27-31:

```text
Physical outputs must be independent of the regulator FAMILY. Exactly ONE
finite renormalization condition is permitted, and it is admissible only if it
is DERIVED from the parent rather than chosen. A condition forced by the theory
is not a hidden finite selector; a condition selected by its outcome is, and
remains forbidden.
```

The contradiction ruled on is grounded in `EM_DEPENDENCY_ORDER_FREEZE_V001.md:32-34`:

```text
Because zero bare `F^2` is adopted, the functional-regulator and finite
renormalization step is where response normalization can originate.
```

The new obligations are registered from the authority lines 58-64:

```text
O-SC1. DERIVE THE FINITE RENORMALIZATION CONDITION FROM THE PARENT.
```

and

```text
O-SC2. EXHIBIT THE COVARIANCE.
```

The frozen falsifiers F-SC1, F-SC2, and F-SC3 are registered from authority
lines 68-75. Scope limits are registered from lines 78-87: no slot is
discharged, no regulator/scheme/subtraction point is named or adopted, and no
response/coupling/root/scale/eigenvalue computation is authorized.

## Q-17 Registered: Slot 6 Released To Lane, O-SC1 First

Authority:
`/Users/bgm/MB Work/alpha_supervision/SLOT6_RELEASE_PRINCIPAL_DECISION_2026-07-30.md`
(`774600d10d58bc67ebf6565222a1ed04e6efaf2d1195767c448152ecb84ec5be`).

The ruling is stated at authority lines 8-13:

```text
THE PRINCIPAL GUARD ON SLOT 6 IS LIFTED. THE LANE IS CHARTERED TO WORK IT, IN A
FIXED ORDER.
```

```text
O-SC1 MUST BE ATTEMPTED BEFORE ANY RESPONSE IS EVALUATED.
```

The fixed order is stated at lines 33-43:

```text
O-SC1 -> O-SC2 -> response evaluation, never any other order.
```

The authority's scope at lines 50-67 states that this does not discharge any
slot, does not assert the condition is derivable, names no regulator/scheme or
condition, and does not reorder the frozen electromagnetic dependency sequence.
The frozen falsifier F-S6 is registered from lines 70-74.

## Q-18 Registered: Floor Boundary Value Is The Induced-Only Axiom

Source:
`/Users/bgm/MB Work/alpha_supervision/RESULT_FLOOR_BOUNDARY_VALUE_SETTLED_2026-07-30.md`
(`5c3ee7355bb5c744192cbefd046ffc85b53e64b0b41e859bca6c101f55b46554`).

The decisive type distinction is stated at lines 48-61:

```text
THE CAPACITY CONDITION IS A STATEMENT ABOUT THE BOTTOM OF THE SPECTRUM. THE
PROPER-TIME FLOOR IS A CUT AT SMALL `s`. THOSE ARE DIFFERENT ENDS OF THE SAME
INTEGRAL, AND NEITHER ENTAILS THE OTHER.
```

The operational consequence for the prior operator-floor chain is stated at
lines 63-69:

```text
Closing both would still not yield the floor.
```

The induced-only principle itself states at
`alpha_induced_only_boundary_action_principle_v001.md:16-19`:

```text
The prime removes Boundary-Resolved null/private modes. `STr` carries the
statistics and ghost signs. The lower proper-time boundary is the first durable
record scale; `Gamma_BR,k_R=0` states that no separate public stiffness is
installed before the record branch opens.
```

The alpha-path conditionality finding is registered from the floor result
lines 114-129: the conditionality of alpha equals the induced-only axiom's
status, and slot 18 is load-bearing for epistemic status while irrelevant to
the value.

The repair condition F-FL1 is registered from floor result lines 180-182:

```text
Exhibit an operator condition that fixes the SMALL-`s` end of the proper-time
integral. A bottom-of-spectrum condition cannot do this; a statement about the
domain, the measure, or the admissible mode content might.
```

## Q-19 Registered: Slot 9 Retired As Posed, F2 Consequence Carried

Authority:
`/Users/bgm/MB Work/alpha_supervision/SLOT9_RETIRED_AS_POSED_PRINCIPAL_DECISION_2026-07-30.md`
(`95db1bc8c92b838135f7fa358edb4a5c42d9eb6b5896be7d745967ac099c197b`).

The ruling is stated at authority lines 8-17:

```text
SLOT 9 IS RETIRED AS POSED. THE OBLIGATION "EXCLUDE THE FINITE `c F^2`
DEFORMATION" IS WITHDRAWN AS THE OPERATIVE REQUIREMENT AND REPLACED BY TWO:
```

Those two obligations are S9-A, determination of the total physical stiffness by
a derived and overdetermined condition, and S9-B, the exit question. The
reasoning at lines 23-37 states that exclusion and determination are different
demands, and only determination is what alpha needs.

The guards are registered from authority lines 42-55: no adopted determining
condition, no selection by outcome, "moot" is not discharge of the epistemic
obligation, no claim that a scale-breaker reaches the additive freedom, and no
silent answer to S9-B.

Q-19 carried the R-30/F2 consequence as unruled at authority lines 57-72:

```text
ON ITS FACE F2 HAS FIRED, AND THE PRIMARY-ROUTE DECLARATION LAPSES
AUTOMATICALLY BY ITS OWN TERMS.
```

The two possible readings were recorded there: F2 fires, or F2 is explicitly
restated against S9-A. That state is superseded by Q-20 below.

## Q-20 Registered: R-30 F2 Fired; Primary-Route Declaration Lapsed

Authority:
`/Users/bgm/MB Work/alpha_supervision/R30_F2_FIRED_PRIMARY_ROUTE_LAPSED_PRINCIPAL_DECISION_2026-07-30.md`
(`990de4606303202a0a1b2d61d3ba071cac03a45dde02185e05939db6c8fb6c3d`).

Q-20 states the ruling at `QUESTIONS_SETTLED_REGISTER_V001.md`:

```text
NO. F2 FIRED AND R-30's PRIMARY-ROUTE DECLARATION LAPSED ON 2026-07-30.
```

The authority states the ruling:

```text
F2 FIRES. THE PRIMARY-ROUTE DECLARATION OF 2026-07-29 (R-30) LAPSES AS OF
2026-07-30. THE PROGRAM HAS NO DECLARED PRIMARY ROUTE.
```

The same authority states what does not lapse: the route is not refuted; its
executed results stand; slot 2 remains required; F1 is untouched and live; and
work on the route is un-privileged rather than prohibited.

The rejected reading is also recorded: restating F2 against S9-A after the
firing condition arrived would let a declared label survive on a technicality.
The current governing state is therefore: no declared primary route, no route
refutation, and no prohibition on BR / EM-GR work.

## Protected Status

```text
q13_registered = true
q14_registered = true
q15_registered = true
q16_registered = true
q17_registered = true
q18_registered = true
q19_registered = true
q20_registered = true
slot12_reposed_as_scheme_covariance_registered = true
slot6_released_to_lane_registered = true
slot9_retired_as_posed_registered = true
r30_f2_fired_primary_route_lapsed_registered = true
declared_primary_route_exists = false
alpha_computed = false
kappa_record_computed = false
proof_authorized = false
```
