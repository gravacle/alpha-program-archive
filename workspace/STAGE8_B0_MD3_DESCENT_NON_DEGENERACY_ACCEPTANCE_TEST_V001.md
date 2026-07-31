# Stage 8 B0 MD-3 Descent Non-Degeneracy Acceptance Test v001

Date: 2026-07-31
Lane: CODEX 1
Register head at issue: Q-114 / relay 209
Road justification: Q-83, UNBLOCKS STEP 1

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false; coupling_evaluation_authorized = false; production_authorized = false.`

## 0. Premises, scope, and non-actions

This artifact specifies MD-3, `B0_DESCENT_NON_DEGENERACY`, as an
acceptance test over the already named `DESCEND_B0` interface. It does not
construct `B0`, does not evaluate a response, and does not claim a uniqueness
theorem.

Premises declared at the outset:

1. No new physical premise is adopted.
2. `B0` is not identified with P0, with a flag, with an incidence structure,
   with `C0`, with `Gamma_K`, or with `C_record(K)`.
3. MD-3 is an acceptance test schema. It is not a construction rule.
4. The test is allowed to be specified in order to make a future construction
   testable; `MD3_derived_from_prior_corpus = false | TYPE-U`.
5. No value, scale, root, eigenvalue, beta function, response coefficient,
   absolute interval, or measured constant is computed.
6. No git, gate, baseline, deploy, commit, or push action is performed.

Search and citation scope:

```text
roots:
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program
  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
  /Users/bgm/MB Work/alpha-program-archive/workspace
  /Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md
  /Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_203_2026-07-31.md
  /Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_208_2026-07-31.md
  /Users/bgm/MB Work/alpha_supervision/RELAY_PASTE_209_MD3_DESCENT_NON_DEGENERACY_CODEX1_V001.md

exclusions:
  a32_holdout/custodian_private/
  Codex 2 response-extraction/package internals not needed to state MD-3
  Einstein incidence-construction work except its settled Q-114 result

queries actually run:
  "CM-3"
  "constant-descent" / "constant descent"
  "opaque-carrier" / "opaque carrier"
  "B0_DESCENT_NON_DEGENERACY"
  "CodomainCompatibleBoundaryOriginRealizer"
  "IprimPresentedCodomainCompatibleBoundaryOriginRealizer"
  "DESCEND_B0"
  "C_record(K)" / "C_record"
  "incidence" x {"B0","Obj_B0","B_0"} through Q-114 citations
```

No new Q-80 class is introduced. TYPE-R/TYPE-U/TYPE-S/TYPE-C plus
`NO_VERDICT` are sufficient.

## 1. Lead result

```text
MD3_acceptance_test_specified = true [SPECIFICATION]

MD3_derived_from_prior_corpus = false | TYPE-U |
  would-build: a prior sealed clause already imposing descent faithfulness on
  DESCEND_B0

CM3_passes_MD3 = false | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE

CM3_accepted_as_B0_after_MD3 = false | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE or, if CM-3 refuses a nontrivial probe
  suite, MD3-APPLICABILITY-NO-VERDICT-NOT-PASS

residual_fiber_acts_on_C_record = NO_VERDICT |
  blocked_by: no constructed B0 candidate, no B0 candidate-equivalence
  relation, no completed C_record(K) extraction/evaluation map, and no
  response-layer structures

residual_fiber_is_gauge = NO_VERDICT |
  blocked_by: same missing C_record(K) extraction/evaluation map and same
  missing equivalence relation
```

The result is intentionally two-layered.

At the `DESCEND_B0` interface layer, MD-3 is now specified and it rejects
CM-3. At the road-action layer, the question whether distinct realizers in
`IprimPresentedCodomainCompatibleBoundaryOriginRealizer` produce different
`C_record(K)` values is not yet decidable. The scalar residual is still an
output of the completed on-shell `Gamma_K`/BR stationary problem, and that
problem is not built.

## 2. Source facts MD-3 consumes

### 2.1 The residual fiber

Q-113 records that the joint system does not determine `B0`
(`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4558-4578`):

```text
joint_system_determines_B0 = false | TYPE-R
0/9 collapse; 3/9 shrink; 0/9 conflict
Residual fiber: IprimPresentedCodomainCompatibleBoundaryOriginRealizer
```

The same row says the open slots include descent maps and the equivalence
relation (`:4572-4578`). Those are exactly the coordinates MD-3 probes.

### 2.2 The descent interface

The B0 load-bearing stop spec states the production codomain at
`/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:977-1037`:

```text
DESCEND_B0 :
  CompleteMicroscopicBoundaryOriginCandidate
    ->
  SingleOriginPackageInputs(
    C0,
    U1,
    U2,
    U3,
    d_C0,
    d_U1,
    d_U2,
    d_U3
  )
```

and:

```text
d_C0 : B0_candidate -> C0
d_Ui : (B0_candidate,C0) -> Ui,  i in {1,2,3}

C0 = d_C0(B0_candidate)
Ui = d_Ui(B0_candidate,C0),  i in {1,2,3}
```

The same source says `DESCEND_B0_derived = false | TYPE-U` at `:1032-1037`.
MD-3 therefore cannot pretend descent already exists. It specifies how a
future descent witness is tested.

### 2.3 The existing T6B leg is one-sided

The B0 spec's T6B test at
`STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md:1363-1373`
has:

```text
failure_condition =
  an undeclared physical input changes a descendant
```

Relay 203 verified why that does not catch CM-3: under a constant descent map
no input changes any descendant
(`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_B0_BLIND_ADVERSARIAL_COUNTERMODEL_SUITE_EINSTEIN_V001.md:53-58`).

MD-3 supplies the missing dual: not "extra dependence changes a descendant",
but "nontrivial candidate variation must not be invisible to all descendants."

### 2.4 CM-3

Relay 203 defines CM-3 at
`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_B0_BLIND_ADVERSARIAL_COUNTERMODEL_SUITE_EINSTEIN_V001.md:46-58`:

```text
CM-3 = opaque-carrier constant-descent root
```

with four descent maps that are total constant maps onto the reference
`C0*`, `U1*`, `U2*`, and `U3*`. It further records that no sealed test
requires varying `Obj_B0` to change a descendant (`:53-54`).

The same artifact records CM-3 and CM-4 as surviving countermodels at
`:159-163`, and names MD-3 as the missing discriminator at `:227-232`.

### 2.5 Incidence does not supply MD-3

Q-114 records that there is no arrow from incidence objects to `B0`
(`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4596-4605`).
The incidence artifact states that non-degeneracy in `K` is not
non-degeneracy in `B0`
(`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_INCIDENCE_STRUCTURE_DETERMINATION_TEST_EINSTEIN_V001.md:64-68`).

It also records that CM-3 survives a combinatorially rich interior because
CM-3 constrains only outgoing constant descent maps, not the atom's interior
(`:184-188`).

### 2.6 C_record(K) is downstream and unbuilt

`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:432-506` says `C_record(K)` must be
derived from the complete on-shell problem and not defined to vanish at a
desired value. It also says the scalar projection cannot hide a failed full
operator.

`STAGE8_P1_P7_CONSUMER_STRUCTURE_REQUIREMENT_AUDIT_V001.md:213-246` states
that `Gamma_K`/`C_record(K)` consume structure, not bare existence, and that
scalar/root execution cannot start without the response layer.

Therefore the fiber-action question over `C_record(K)` is not executable
today.

## 3. MD-3 input contract

MD-3 consumes a proposed B0 acceptance packet:

```text
B0_MD3_PACKET :=
  (
    r,
    Probe_B0(r),
    Eq_B0,
    Eq_DESC,
    DescendantPhysicalFieldList,
    DESCEND_B0,
    optional C_record_extractor when it exists
  )
```

where:

```text
r =
  (Obj_B0, Sig_B0, Carrier_B0, Core_B0, Prov_B0, DESCEND_B0)
  in IprimPresentedCodomainCompatibleBoundaryOriginRealizer
```

and:

```text
DESCEND_B0(r) =
  D(r) =
  (C0, U1, U2, U3, d_C0, d_U1, d_U2, d_U3).
```

The probed descendants are all physical fields of:

```text
C0, U1, U2, U3,
d_C0, d_U1, d_U2, d_U3
```

as fixed by the descendant inventory. Pure labels, charts, display
conventions, or branch-ordering conventions do not count as physical
differences unless a downstream test has predeclared them as physical data.

`Probe_B0(r)` must be frozen before descendant outputs or response-facing
quantities are inspected. It is a target-independent family of admissible
candidate variations, adversarial twins, or mutations of the B0 candidate
within the same acceptance context. It may include another realizer
`r'` from the Q-113 residual fiber.

`Eq_B0` is the candidate equivalence relation. `Eq_DESC` is the descendant
equivalence/equality relation over the full package `D(r)`. Both must be
frozen before execution. If either relation is missing, MD-3 returns
`NO_VERDICT`, not PASS.

## 4. MD-3 acceptance test

### MD3-0 Applicability

The test applies only if all of the following are frozen before execution:

1. a B0 candidate packet `r`;
2. a target-independent `Probe_B0(r)`;
3. `Eq_B0`;
4. `Eq_DESC`;
5. executable `DESCEND_B0` maps;
6. a descendant physical-field inventory.

If any are missing:

```text
MD3_executable = false | TYPE-C |
  constraint: candidate/probe/equivalence/descent inputs not all frozen
  release: freeze all MD3-0 inputs before any descendant or response output
```

### MD3-1 Nonempty physical probe requirement

`Probe_B0(r)` must contain at least one nontrivial physical probe unless a
separate rigidity theorem proves that the acceptance context has only one
candidate equivalence class.

If `Probe_B0(r)` is empty and no rigidity theorem is supplied:

```text
MD3_verdict = NO_VERDICT
```

This is not evidence against `B0`. It is also not a pass.

### MD3-2 Descent non-degeneracy condition

For every `r' in Probe_B0(r)`:

```text
if well_typed(r') and not Eq_B0(r,r'):
    D(r)  := DESCEND_B0(r)
    D(r') := DESCEND_B0(r')

    if Eq_DESC(D(r),D(r')):
        FAIL MD3
```

Equivalently:

```text
DESCEND_B0 must be faithful on the tested B0 quotient:

  r not~_B0 r'  ==>  DESCEND_B0(r) not~_DESC DESCEND_B0(r')

for every nontrivial tested physical variation.
```

This is an acceptance condition over the tested family, not a global
uniqueness theorem over all possible future B0 constructions.

### MD3-3 Physical descendant difference

A descendant difference counts only if at least one required physical datum in
`C0`, `U1`, `U2`, `U3`, or one provenance/descent witness `d_C0`, `d_U1`,
`d_U2`, `d_U3`, differs under its frozen equality predicate.

Differences only in names, labels, display conventions, file paths, or
self-asserted provenance strings do not discharge MD-3.

### MD3-4 CM-3 discrimination

CM-3 fails at MD3-2.

Reason: relay 203 defines CM-3's four descent maps as total constant maps onto
the reference descendants
(`/Users/bgm/MB Work/alpha-program-archive/workspace/STAGE8_B0_BLIND_ADVERSARIAL_COUNTERMODEL_SUITE_EINSTEIN_V001.md:46-49`).
For any nontrivial probe `r'` that changes the opaque carrier or chooses the
descent-equivalent twin CM-4, constant descent gives:

```text
DESCEND_B0(r') = DESCEND_B0(r)
```

while `r'` is not accepted as `Eq_B0`-equivalent unless an independently
frozen equivalence relation proves that the entire difference is gauge.

Thus:

```text
CM3_fails_MD3 = true | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE
```

If CM-3 refuses all nontrivial probes by declaring no physical variation
available, it still does not pass. It returns `NO_VERDICT` at MD3-1 unless a
rigidity theorem is supplied. A `NO_VERDICT` candidate cannot be accepted as
B0.

## 5. The fiber-action question

Q-114 states that MD-3 and the question whether the residual fiber acts on
`C_record(K)` are the same acceptance object
(`/Users/bgm/MB Work/alpha_supervision/QUESTIONS_SETTLED_REGISTER_V001.md:4648-4652`).

This artifact makes that connection executable, but not executable today.

When a `C_record(K)` extraction/evaluation map exists, MD-3 must be extended
by the road-action check:

```text
for r,r' in IprimPresentedCodomainCompatibleBoundaryOriginRealizer:
    if not Eq_B0(r,r') and not Eq_DESC(D(r),D(r')):
        compare C_record_r(K) and C_record_r'(K)
```

Possible future verdicts:

```text
fiber_acts_on_road = true
  iff at least one MD3-distinct pair produces a non-equivalent C_record(K)
  functional under the frozen C_record equality predicate

fiber_is_gauge_relative_to_road = true
  iff every MD3-distinct pair produces the same C_record(K) functional and a
  sealed equivalence theorem says that equality is not an artifact of a
  missing extractor or collapsed test domain
```

Present verdict:

```text
fiber_action_on_C_record_today = NO_VERDICT |
  blocked_by: C_record(K) extraction/evaluation map absent; response layer
  absent; candidate equivalence relation absent; no pair r,r' has been
  constructed and run
```

This is not a degeneracy result. The stronger result "B0 underdetermination is
gauge" would require the same descendants-or-road-output theorem MD-3 is now
designed to demand. It is not available.

## 6. What MD-3 does not claim

MD-3 does not claim:

1. that `B0` exists;
2. that `B0` is unique;
3. that a passing candidate is correct;
4. that descendant sensitivity alone makes `C_record(K)` evaluable;
5. that incidence non-degeneracy is B0 non-degeneracy;
6. that two candidates with different descendants must produce different
   `C_record(K)`;
7. that two candidates with the same `C_record(K)` are gauge;
8. that any response, root, scale, or value is authorized.

MD-3 claims only this:

```text
No future B0 candidate may be accepted if nontrivial tested physical variation
of the candidate is invisible to every descendant in DESCEND_B0.
```

## 7. Consequences for acceptance

```text
B0_candidate_acceptance_requires_MD3 = true [SPECIFICATION]

B0_candidate_with_constant_DESCEND_B0_acceptance = false | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE

B0_candidate_with_missing_probe_or_equivalence_acceptance = false | TYPE-C |
  constraint: MD3 returns NO_VERDICT, not PASS

B0_candidate_passing_old_battery_without_MD3_acceptance = false | TYPE-C |
  constraint: Q-114 records that without MD-3 the battery cannot distinguish
  a real B0 from an object that does no work
```

This is an acceptance gate, not a construction gate. It can reject bad
objects. It cannot build a good one.

## 8. Typed negatives

```text
MD3_derived_from_prior_corpus = false | TYPE-U |
  would-build: a prior sealed descent-faithfulness clause on DESCEND_B0

CM3_passes_MD3 = false | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE

CM3_accepted_as_B0_after_MD3 = false | TYPE-R |
  test: MD3-CONSTANT-DESCENT-FAILURE or MD3-APPLICABILITY-NO-VERDICT-NOT-PASS

fiber_action_on_C_record_today = NO_VERDICT |
  blocked_by: missing C_record(K) extraction/evaluation map, missing response
  layer, missing B0 candidate-equivalence relation, and no constructed pair

fiber_is_gauge_relative_to_road_today = NO_VERDICT |
  blocked_by: same missing extraction/equivalence data

B0_constructed_by_MD3 = false | TYPE-U |
  would-build: a complete B0 candidate and descent maps; MD-3 supplies only
  the acceptance discriminator

MD3_executes_against_real_B0_today = false | TYPE-C |
  constraint: no real B0 candidate packet is frozen
```

## 9. Relay answers

1. **What MD-3 consumes.** A B0 candidate packet in the Q-113 residual fiber,
   the executable `DESCEND_B0` maps, `C0/U1/U2/U3` and their provenance
   witnesses, a frozen target-independent probe family, and frozen candidate
   and descendant equivalence relations.
2. **The non-degeneracy condition.** `DESCEND_B0` must be faithful on the
   tested B0 quotient: a nontrivial tested physical variation of the candidate
   must change at least one physical descendant or descent witness.
3. **The discrimination claim.** CM-3 fails because its descent maps are total
   constant maps; nontrivial opaque-carrier variation or the CM-4 twin leaves
   all descendants unchanged.
4. **What MD-3 does not claim.** It is an acceptance test, not a construction
   or uniqueness theorem. It does not evaluate `C_record(K)` and does not
   decide the road-action/gauge question today.
5. **Fiber action.** `NO_VERDICT` today. MD-3 specifies the future check, but
   `C_record(K)` is not yet an evaluable output and no candidate pair has been
   run.

No git, commit, push, gate, baseline, deploy, value, scale, root, eigenvalue,
beta function, response coefficient, absolute interval, or measured constant
action was performed.
