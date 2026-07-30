# Stage 8 S8 Write-Tail Join Specification And Test v001

Date: 2026-07-30

Lane: CODEX 1

Register head consulted: Q-54. No ruling later than Q-54 was consulted.

Status: APPEND-ONLY LANE FINDING. This artifact specifies a test object under
Q-52. The test object is not a derived physical write-tail law.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## At-Outset Declarations

Q-52 authorizes a missing object to be specified for the purpose of a test if it
is declared at the outset, marked underived, and never reported as derived. This
artifact uses that permission only for the test object below.

```text
s8_test_object_derived = false | TYPE-U | would-build: physical write-tail join derivation
physical_write_tail_join_derived = false | TYPE-U | would-build: physical write-tail join derivation
exchange_magnitude_derived = false | TYPE-U | would-build: upstream derivation of the S8 integrated action
```

Added test premises, each test-only and underived:

```text
P_TEST_1: The R3.4 transported write/tail candidate may be used as a diagnostic
          test object for S8.
P_TEST_2: The scalar integrated action A_c := integral v_c(t) dt may be varied
          inside the diagnostic object unless an independently sealed branch
          condition fixes it.
P_TEST_3: Endpoint restoration may be checked after A_c is supplied, but is not
          itself a derived selection rule for A_c unless a sealed authority says
          so before the check.
```

## Answer 1 - What The Write-Tail Join Is In Sealed Text

The sealed R3.4 specification states the candidate join as follows. It lets

```text
U_0(t)=exp(-i H_0 t)
```

be the free incidence evolution, separates a scalar cell envelope `v_c(t)` from
the unit-normalized reference incidence operator `B_c`, and requires the
operator part to satisfy the transport equation

```text
tilde B_c(t+s)=U_0(s) tilde B_c(t) U_0(s)^*,
tilde B_c(0)=B_c.
```

The group law gives the unique transported operator

```text
tilde B_c(t)=U_0(t) B_c U_0(t)^*,
```

and the candidate complete primitive write-plus-tail parent is

```text
H(t)=H_0 + sum_c v_c(t) U_0(t) B_c U_0(t)^*.
```

In the interaction picture,

```text
H_I(t)=sum_c v_c(t) B_c.
```

Source: `R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md:48-83`.

Type: a time-dependent finite-regulator parent operator built from a free
incidence tail `H_0`, its free evolution `U_0`, a unit-normalized primitive
write operator `B_c`, and scalar cell envelopes `v_c(t)`. It joins the free
outgoing incidence tail to the primitive write by transporting the write
operator with the free tail rather than leaving it static.

The fixed-integrated-action qualifier enters at the exactness calculation:

```text
U(T,0)=U_0(T) exp[-i B_c integral v_c(t)dt].
```

That calculation is explicitly for pulse profiles with the same integrated
action. Source: `R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md:93-99`.

The result records the same limitation: given the covariance rule, the
interaction-picture write is exact and profile-independent for fixed integrated
action, but the adopted upstream principles do not force the covariance equation
as the physical joining law; the ordinary static interaction is not excluded.
Source: `R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_RESULT_V001.md:22-41`.

The actual primitive causal transition-map spec separately records one-use
pulse support with integrated action

```text
tau_R = pi/sqrt(2)
```

and finite primitive factors

```text
U_j = exp(-i tau_R B_j).
```

Source: `STAGE8_T7_ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_SPEC_V001.md:45-58`.

## Answer 2 - Is The Exchange Magnitude Free Or Determined Upstream?

There are two different readings, and they must not be collapsed.

### 2.1 Current ordinary-parent branch

Under the current ordinary-parent branch, the scalar integrated action is
specified upstream by the disclosed ER-A branch condition:

```text
v_c(t)=(tau_R/T_R) w((t-t_c)/T_R)
integral_cell_time v_c(t) dt = tau_R.
```

The same authority says the current ordinary parent adopts ER-A as a disclosed
branch premise and does not relabel it as derived. Source:
`STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md:24-64`. The Stage-7 review
candidate records the same amplitude clause and separately states that the
physical duration `T_R` remains unfixed. Source:
`STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md:95-130`.

Therefore the exchange magnitude is not an open scalar inside the current
ER-A ordinary-parent branch: its cell integral is fixed to `tau_R`. But the
ground is branch-supplied, not a theorem of the physical write-tail join.

```text
exchange_magnitude_free_in_current_ER_A_branch = false | TYPE-C | constraint: disclosed ER-A amplitude clause | release: derived alternate parent branch or supersession of ER-A
exchange_magnitude_theorem_derived = false | TYPE-U | would-build: derivation that ER-A or another upstream principle uniquely fixes the S8 integrated action
```

### 2.2 Transported S8 candidate as a diagnostic object

The R3.4 covariance equation determines the operator transport
`B_c -> U_0(t) B_c U_0(t)^*`. It does not determine the scalar

```text
A_c := integral v_c(t) dt.
```

The exactness statement is parametric in `A_c`: after `A_c` is supplied, the
profile shape drops out and the interaction-picture write depends on the single
integrated action. Source:
`R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_SPEC_V001.md:93-99` and
`R3_4_CAUSAL_TRANSPORTED_WRITE_TAIL_RESULT_V001.md:22-25`.

The source-record generator gate also shows why "magnitude present" is not the
same as "magnitude selected." Under a conditional exchange reduction it leaves
one positive magnitude, exact transfer fixes only the product
`g tau/hbar = pi/2`, and neither `g` nor `tau` is separately fixed. Source:
`SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V001.md:54-76` and
`SOURCE_RECORD_GENERATOR_STRUCTURE_GATE_V001.md:118-145`.

Thus the diagnostic transported candidate contains an unselected magnitude if
ER-A is not imposed. That is a test fact about the diagnostic object, not a
physical refutation by itself.

```text
transport_covariance_selects_A_c = false | TYPE-R | test: solve the sealed covariance equation; it fixes transported B_c(t) and leaves A_c external to the equation
diagnostic_S8_magnitude_free_without_ER_A = true | TYPE-R | test: vary A_c in the diagnostic H_I(t)=sum_c v_c(t)B_c while preserving the covariance transport equation
theory_001_negative_half_refuted_by_S8 = NO_VERDICT | blocker: physical_write_tail_join_derived = false | TYPE-U
```

## Answer 3 - Test Specification Under Q-52

The diagnostic S8 test object is:

```text
INPUT:
  H_0       free incidence-tail generator;
  B_c       unit-normalized primitive write operator;
  v_c(t)    smooth one-use scalar envelope;
  A_c       := integral v_c(t) dt.

TRANSPORT:
  U_0(t)    := exp(-i H_0 t);
  Btilde_c(t):=U_0(t) B_c U_0(t)^*.

TEST HAMILTONIAN:
  H_A(t) := H_0 + sum_c v_c(t) Btilde_c(t).

INTERACTION-PICTURE TEST:
  H_{A,I}(t) := sum_c v_c(t) B_c.

TEST EXACTNESS TARGET:
  U_A(T,0) = U_0(T) exp[-i B_c A_c]
  for an isolated cell and fixed A_c.
```

This is a specification for testing, not a derivation of the physical parent.

```text
S8_TEST_SPEC_DERIVED = false | TYPE-U | would-build: physical parent derivation selecting this diagnostic object
```

The test separates three questions:

```text
Q_A: Does covariance transport determine Btilde_c(t)?  YES, by R3.4.
Q_B: Does covariance transport determine A_c?          NO, by the equation's type.
Q_C: Does the current ER-A ordinary-parent branch fix A_c? YES, as a branch-supplied amplitude clause A_c=tau_R.
```

Therefore the current corpus supports this typed conclusion:

```text
S8_magnitude_status = BRANCH-FIXED-NOT-THEOREM-DERIVED
physical_coupling_host_status = NO_VERDICT | blocker: physical_write_tail_join_derived = false | TYPE-U
```

## Answer 4 - What Would Falsify This Answer?

The answer above would be falsified by any one of the following sealed acts:

```text
F1: A derived physical write-tail law proving that the R3.4 transported
    candidate, or another law, is forced by pinned upstream principles and
    uniquely fixes A_c without relying on target-selected endpoint matching.

F2: A derived replacement for ER-A or a derived proof of ER-A that changes
    A_c's status from disclosed branch premise to theorem.

F3: A sealed admissible S8 family with the same upstream authorities and
    different A_c values, plus a proof that the family is physical rather than
    diagnostic.

F4: A sealed proof that the ER-A amplitude clause does not apply to the S8
    write-tail join at all.
```

If F1 or F2 lands, the magnitude is determined upstream in the strong sense. If
F3 lands, the theory candidate's negative half is refuted as physical content.
If F4 lands without F1-F3, S8 returns to unpinned magnitude status.

## Bounded Search For Upstream Determinants

Search roots:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Exclusions: `third_party/**`, `a32_holdout/**`, and
`a32_holdout/custodian_private/`. No custodian-private path was opened.

Primary query:

```text
integrated action|fixed integrated action|v_c(t)|integral v_c|exchange magnitude|physical_write_tail_join|write-tail|write tail|transported write
```

Additional file reads: the Q-52/Q-54 register block, OBS-07, the R3.4
transported write-tail spec/result, the Stage-7 ER-A successor/review texts, the
actual primitive causal transition-map spec, the source-record generator gate,
the OBS-05 finite reversible write test, and the Q-53 enumeration audit.

No upstream theorem deriving the S8 integrated action was found in that scope.

```text
upstream_theorem_selecting_S8_A_c_found = false | TYPE-S | roots: listed above | excl: third_party/**, a32_holdout/**, a32_holdout/custodian_private/ | fences: no Codex 2 artifacts edited, no reviewer registers edited | query: "integrated action|fixed integrated action|v_c(t)|integral v_c|exchange magnitude|physical_write_tail_join|write-tail|write tail|transported write"
```

## Verdict

```text
S8_WRITE_TAIL_JOIN_VERDICT = NO_VERDICT_AS_PHYSICAL_REFUTATION
physical_write_tail_join_derived = false | TYPE-U | would-build: physical write-tail join derivation
exchange_magnitude_derived = false | TYPE-U | would-build: upstream derivation of the S8 integrated action
exchange_magnitude_free_in_current_ER_A_branch = false | TYPE-C | constraint: disclosed ER-A amplitude clause | release: derived alternate parent branch or supersession of ER-A
diagnostic_S8_magnitude_free_without_ER_A = true | TYPE-R | test: vary A_c in the diagnostic transported candidate while preserving covariance transport
```

Plain-language summary: S8 does not currently refute theory 001's negative
half, because the physical write-tail law is still unbuilt. The diagnostic
transported candidate exposes where a magnitude would sit, and covariance alone
does not determine it. The current ER-A ordinary-parent branch fixes the cell
integral to `tau_R`, but as branch-supplied parent data rather than as a derived
S8 theorem.
