# Stage 8 Response–State Factorization Test Fixture Result v001

Date: 2026-08-01  
Lane: Codex lane 2  
Task: 2d  
Register head at construction start: Q-221

## Lead result

**The two full pre-projection induced operators are different. The difference
is in the connected second-response block itself. OBS-14 is refuted at that
consumer.**

One finite, explicit, target-independent CTP source fixture was frozen on the
ratified carrier before either state was applied. The two state arms use
exactly Q-211's distinguished scalarizations, with their Q-219 canonical
two-branch completions:

```text
omega_H       = tau_0,+ tensor tau_0,-,
omega_epsilon = epsilon_+ tensor epsilon_-.
```

On the fixed nontrivial character probe, `omega_epsilon` is multiplicative;
its connected second-response operator annihilates the entire fixture probe
space. `omega_H` has a nonzero centered character direction, so its connected
second-response operator does not. A zero operator cannot be carried to a
nonzero operator by branch exchange, reality involution, index reordering, or
the fixed CTP metric. The operators differ before any retarded extraction,
local projection, scalar coefficient, spectrum, or value is formed.

The localized new-physics requirement is therefore not necessarily a complete
density-matrix identity. It is at least a rule that fixes the
**response-relevant connected CTP two-point/cumulant functional** of the
physical state on the source-coupled character algebra. Positivity,
normalization, U1 reality, and the one-cell restriction do not fix that datum.

```text
FIXTURE_FROZEN_BEFORE_STATE_COMPARISON = true
FIXTURE_NOT_PHYSICAL = true
Q211_EXACT_TWO_STATES_PLACED = true | TYPE-P | premises: DoR-008

FULL_PREPROJECTION_OPERATOR_EQUAL = false | TYPE-R |
  witness: the fixed plus-branch nontrivial character probe is annihilated by
           K_epsilon^fix and not annihilated by K_H^fix
FULL_PREPROJECTION_OPERATOR_EQUIVALENT_UNDER_U1 = false | TYPE-R |
  test: every sealed U1 convention preserves zero-versus-nonzero operator rank

STATE_IDENTITY_CAN_AFFECT_INDUCED_RESPONSE = true | TYPE-P |
  premises: DoR-008 and the frozen fixture declaration
OBS14_STATE_IS_ROLE_ONLY_AT_RESPONSE_PRODUCER = false | TYPE-R |
  test: two admissible state identities on identical non-state inputs induce
        inequivalent full connected response operators

PHYSICAL_PACKAGE_RESPONSE_VALUE_COMPUTED = false | TYPE-S |
  scope: this fixture-only structural comparison
PHYSICAL_STATE_IDENTITY_SELECTED = false | TYPE-S |
  scope: this artifact

CONSTRUCTION_VERDICT = DIFFERENT__CONNECTED_SECOND_RESPONSE_CONSUMES_STATE_IDENTITY
```

## 1. Preflight, scope, and frozen authority

### 1.1 Three-line preflight

```text
DOES_THE_OBJECT_EXIST = YES
  object: Q-221 target-independent response-state factorization test

IS_THE_VERSION_CURRENT = true
  basis: register read through Q-221

ARE_THE_INPUTS_PRESENT = YES_FOR_FIXTURE_TEST
  carrier: C0_008
  conventions: U1_008
  states: Q-211 tau_0 and epsilon, branch-completed by Q-219
  non-state dynamics and boundary package: declared below as a finite fixture
```

### 1.2 Frozen authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_TASK2D_ALPHA_CHAIN_STATE_IDENTITY_DEPENDENCY_AUDIT_V001.md` | `5f3f585d9b8696d53d1a002245fe055019a59f72e248b627aa7ba6661f743dc7` | Q-221 test, legal verdicts, and pre-registered asymmetry |
| `STAGE8_FIELD_CTP_V002_SECOND_ADVERSARIAL_KILL_DETERMINATION_V001.md` | `58f2c82121e7fb34c91212ca0181c71c455eca077ce9f6d060835eb0407c3c93` | Q-211 exact one-factor states `tau_0` and `epsilon` |
| `STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md` | `d13920e2a7687ac53a896e70cd0d12168f74fe0f368425179a455a8ae249ae98` | Canonical two-branch completions and admissibility checks |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_C0_DOR008_ASSEMBLY_AND_FIRST_RESTRICTION_TEST_V001.md` | `1467ab9850022931e68dc9ffa625d95099d8f6bb74d734dc9d0466f169bd00b6` | Ratified carrier, algebra, representation, and bounded domain |
| `STAGE8_CTP_PHYS_INPUT_PACKAGE_U1_DOR008_ASSEMBLY_DETERMINATION_V001.md` | `1b0e928c452c10a8be72be22ff81fd7677f5045d2ad8d398a9f7f7f57b9ab3b0` | Branch orientation, metric, reality, order, and embeddings |
| `STAGE8_FILLED_TWO_CELL_CARRIER_CENSUS_AND_EXTENSION_DETERMINATION_V001.md` | `bf75f3929d739eccd2c0b495f3ec99e3db7564fbc2cdbf78eb503e63d4ee7082` | Precedent that a frozen test fixture need not be a forced physical carrier |

Every construction statement using the ratified carrier is conditional:

```text
TYPE-P | premises: DoR-008
```

The fixture is declared rather than derived and is marked
`FIXTURE_NOT_PHYSICAL` everywhere it bears. No fixture field is transported
into the physical package.

### 1.3 Scope exclusions

This test does not construct or evaluate:

```text
a physical rho_pre
the common-origin descent
the physical S_CTP or U_BR
the physical quotient or measure
the retarded Hessian
p_loc or Pi_loc
B_ind or any fixed-point/root object
any matching map or response value
```

## 2. Step 1 — fixture frozen before output

### 2.1 Fixed carrier and first character probe

The ratified field-label system is

```text
Lambda = direct-sum_(j>=1) Z e_j,
B = A_F,+ tensor_min (A_F,-)^op.
```

Freeze the first sequential generator

```text
lambda_fix := e_1 in Lambda.
```

This choice is made by label order alone. It uses no response, root, target,
or downstream output. Define its represented branch elements

```text
u_+ := e_+(U_lambda_fix),
u_- := e_-(U_lambda_fix),
X_+ := u_+ + u_+^*,
X_- := u_- + u_-^*.
```

`X_+` and `X_-` are bounded self-adjoint elements with commuting branch
ranges. U1 reality exchanges them according to the already sealed star/branch
rule.

### 2.2 Finite source space and fixed map

Freeze the finite real branch-probe space

```text
V_fix := span_R{q_+,q_-}
```

and the source insertion

```text
s_fix(q_+) := X_+,
s_fix(q_-) := X_-.
```

The branch orientation and sign are those of `U1_008`; no rival convention is
introduced. `V_fix` is the common domain and codomain of both induced
operators. The scalar Hilbert realizations of the two states may differ, but
the response operators are compared on this identical finite source space.

### 2.3 Declared dynamics and boundary fixture

For `v=v_+q_+ + v_-q_-`, declare the bounded source evolution

```text
U_fix(v)
  := exp(i [v_+ X_+ - v_- X_-]).
```

Freeze the remaining non-state data:

```text
P_fix := (
  carrier            = C0_008,
  conventions        = U1_008,
  source_space       = V_fix,
  source_map         = s_fix,
  dynamics_fixture   = U_fix,
  inclusive_effect   = I_inc_008,
  operator_domain    = D_C0=E_C0,
  endpoint_source    = zero,
  boundary_effect    = inclusive identity,
  extra_contacts     = empty for this bounded algebraic fixture,
  projection         = NONE,
  physical_claim     = FIXTURE_NOT_PHYSICAL
).
```

All entries are fixed before either state arm is applied. The empty contact
entry is not a physical assertion: it is part of this bounded fixture, which
contains no distributional field insertions or coincident-point operation.

```text
P_FIX_COMPLETE_FOR_DECLARED_TEST = true
P_FIX_TARGET_INDEPENDENT = true
P_FIX_USES_PHYSICAL_DYNAMICS = false | TYPE-S |
  scope: P_fix; U_fix is expressly a test fixture
P_FIX_CONTAINS_PROJECTION = false | TYPE-S |
  scope: P_fix
```

## 3. Step 2 — exact Q-211 state placements

### 3.1 The named scalarizations

Q-211 defines, on each field-character factor,

```text
tau_0(U_lambda)=0 for lambda!=0, tau_0(1)=1,
epsilon(U_lambda)=1 for every lambda.
```

Q-219 gives their exact two-branch placements:

```text
omega_H       := tau_0,+ tensor tau_0,-,
omega_epsilon := epsilon_+ tensor epsilon_-.
```

Both are positive, normalized, and U1-compatible. Neither is promoted to the
physical state.

### 3.2 Common source-record extension

The fixture source acts only on the field/CTP factor. To place the states on
the joined carrier without changing any non-state input, freeze the same
normalized source-record vector functional in both arms:

```text
xi_SR^fix := Omega_C tensor Omega_out,
varphi_SR^fix(a) := <xi_SR^fix,pi_SR(a)xi_SR^fix>,

Phi_H       := varphi_SR^fix tensor omega_H,
Phi_epsilon := varphi_SR^fix tensor omega_epsilon.
```

`Omega_C` and `Omega_out` are the inherited sectoral GNS cyclic vectors. Their
product use is a declared fixture placement, not a physical state-factorization
claim. The same `varphi_SR^fix` occurs in both arms, and all probes are the
identity on the source-record factor, so it cannot produce the observed
difference.

```text
STATE_ARMS_DIFFER_ONLY_IN_Q211_SCALARIZATION = true
SOURCE_RECORD_STATE_FACTOR_FIXED_IDENTICALLY = true
FIXTURE_PRODUCT_STATE_PROMOTED_TO_PHYSICAL_RHO_PRE = false | TYPE-S |
  scope: this artifact
```

## 4. Full induced operator before projection

### 4.1 Exact fixture functional

For either `Phi` in `{Phi_H,Phi_epsilon}`, define

```text
Z_Phi^fix(v) := Phi(U_fix(v)),
W_Phi^fix(v) := Log_0 Z_Phi^fix(v).
```

`Z_Phi^fix(0)=Phi(1)=1`, so the local logarithm exists on a neighborhood of
the zero source. The full fixture-induced connected operator

```text
K_Phi^fix : V_fix -> V_fix^*
```

is defined by the complete second source derivative

```text
<w,K_Phi^fix v>
  := (D_w D_v W_Phi^fix)|_(zero source).
```

Equivalently, up to the one common fixed CTP convention factor carried by both
arms, its sesquilinear form is the connected covariance

```text
Cov_Phi(s_fix(w),s_fix(v))
 := Phi(delta s_fix(w)^* delta s_fix(v)),

delta A := A-Phi(A)1.
```

This is the entire induced operator on `V_fix`. No component is projected out,
and no scalar coefficient is extracted.

### 4.2 The `omega_epsilon` arm

`epsilon` is a character. Its branch product `omega_epsilon` is multiplicative
on the algebra generated by `u_+` and `u_-`. Therefore

```text
delta A = 0 in the omega_epsilon GNS quotient
```

for every fixture probe polynomial `A`. Every connected second cumulant on
`V_fix` vanishes structurally:

```text
K_epsilon^fix = ZERO_OPERATOR_ON_V_FIX.
```

No response value is evaluated in reaching this statement; it follows from
multiplicativity.

### 4.3 The `omega_H` arm

For nonzero `lambda_fix`, the coefficient/Haar state makes the nonidentity
character `u_+` orthogonal to the identity in its GNS construction. The
centered vector represented by `u_+` is therefore nonzero. Positivity of the
GNS form implies that the connected covariance on the fixed plus-branch probe
does not vanish:

```text
K_H^fix(q_+) != 0.
```

This establishes that `K_H^fix` is a nonzero operator. No spectrum, rank
number, coefficient, response value, or projection is computed.

### 4.4 Operator comparison

The witness uses the same input vector `q_+` in the same fixed `V_fix`:

```text
K_epsilon^fix(q_+) = 0,
K_H^fix(q_+)       != 0.
```

Hence

```text
K_H^fix != K_epsilon^fix.
```

The comparison is stronger than convention-dependent matrix-entry inequality.
U1 branch exchange can move the nonzero witness from one branch to the other;
it cannot map the zero operator to a nonzero operator. Reality conjugation,
compound-index reordering, and the fixed branch metric likewise preserve this
distinction.

## 5. Exact structural verifier

An independent exact group-algebra check represented a character monomial by
its integer exponent, `tau_0` by coefficient extraction at the identity, and
`epsilon` by the character homomorphism. It tested the centered covariance of
the fixed nonidentity generator without floating-point arithmetic.

```text
states_distinguished                    true
haar_centered_probe_nonzero             true
trivial_character_centered_probe_zero   true
preprojection_operators_equal           false
```

This verifier is a check of the algebraic witness, not an evaluation of a
physical response.

## 6. Step 3 verdict and localization

Q-221 pre-registers the asymmetric inference:

```text
DIFFERENT on any honestly frozen fixed package
  -> the chain can consume state identity;
  -> OBS-14 dies at that consumer;
  -> the new-physics requirement is real and localized.
```

The test returns `DIFFERENT`. The first varying component is

```text
the connected second source derivative of the inclusive CTP functional,
equivalently the raw connected CTP two-point/source-response operator.
```

The variation occurs before the conditional `G -> H_R[G]` map and before
`p_loc`. Those later maps may be state-blind at fixed operator input, but they
receive an input that this fixture proves can depend on state identity.

The minimum new physical datum is therefore a common-origin rule selecting or
deriving the response-equivalence class

```text
[rho]_resp := states with the same connected CTP cumulant operator on the
              physically admitted source algebra.
```

It need not distinguish states that are identical on every response-relevant
connected cumulant. It must distinguish `omega_H` from `omega_epsilon` for the
fixture source algebra, or supply physical dynamics/source structure that
excludes one response class before use.

```text
FIRST_STATE_SENSITIVE_COMPONENT = CONNECTED_CTP_SECOND_RESPONSE_OPERATOR
OBS14_REFUTED_AT_FIRST_RESPONSE_PRODUCER = true | TYPE-R
NEW_PHYSICS_ASK_LOCALIZED = RESPONSE_RELEVANT_STATE_CUMULANT_CLASS

POSITIVITY_NORMALIZATION_REALITY_FIX_RESPONSE_CLASS = false | TYPE-R |
  witness: both Q-211 states satisfy those constraints and induce different
           K^fix operators
FULL_DENSITY_MATRIX_IDENTITY_PROVED_NECESSARY = false | TYPE-S |
  scope: this test distinguishes response classes, not every state datum
```

## 7. Adversarial attacks

### 7.1 Was the fixture chosen after the answer?

No. The first nonzero sequential character generator, two branch probes,
identity boundary effect, bounded domain, and identity/source-exponential
dynamics were frozen before either state output was derived. No response or
downstream target appears in their definitions.

```text
FIXTURE_NARROWED_AFTER_OUTPUT = false | TYPE-S |
  scope: frozen construction order in Sections 2–3
```

### 7.2 Did the two arms change dynamics or boundary data?

No. Both arms use exactly `P_fix`, `varphi_SR^fix`, `V_fix`, and `s_fix`.
Only `omega_H` versus `omega_epsilon` changes.

```text
NONSTATE_INPUT_CHANGED_BETWEEN_ARMS = false | TYPE-S |
  scope: P_fix field-by-field comparison
```

### 7.3 Is the difference only a projection artefact?

No projection occurs. The compared objects are the full connected operators
on `V_fix`.

```text
PROJECTION_USED_BEFORE_COMPARISON = false | TYPE-S |
  scope: response construction and comparison
```

### 7.4 Is the difference a branch-convention artefact?

No. Zero versus nonzero is invariant under every invertible branch/reality/
index convention in U1.

```text
U1_CONVENTION_IDENTIFIES_THE_TWO_OPERATORS = false | TYPE-R
```

### 7.5 Does the fixture prove the physical operator's value or magnitude?

No. The fixture is deliberately nonphysical. The pre-registered inference
from variance is only that the chain can consume state identity and that a
role-only theorem is false. The physical common-origin state and dynamics
remain unbuilt.

```text
FIXTURE_OPERATOR_TRANSPORTED_AS_PHYSICAL_OPERATOR = false | TYPE-R |
  test: P_fix is declared FIXTURE_NOT_PHYSICAL and has no common-origin descent
PHYSICAL_RESPONSE_MAGNITUDE_DETERMINED = false | TYPE-S |
  scope: this structural test
```

### 7.6 Could a weaker theorem survive?

Yes. A candidate physical theorem could prove that the actual dynamics couples
only to a subalgebra on which every admitted physical state has the same
connected cumulants. This fixture does not refute that narrower statement.

```text
PHYSICAL_SOURCE_SUBALGEBRA_FACTORIZATION_THEOREM_REFUTED = false | TYPE-S |
  scope: no such theorem or physical source algebra is instantiated here
```

## 8. Symbol collisions and non-transport

Only collisions bearing on this test are recorded:

1. `epsilon` here is the trivial-character scalarization. It is not U1's
   branch-orientation sign map, although both use the same spelling in nearby
   artifacts.
2. `K_Phi^fix` is the fixture induced operator. It is not the program's
   `K`, `K_*`, `B_ind(K)`, or any coupling-side object.
3. `Omega_C` and `Omega_out` are sectoral GNS cyclic vectors. They are not the
   common microscopic origin `Omega` required by the P5 descent presentation.

No identity is transported among these objects.

## 9. Search and execution scope

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/
  alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha_supervision
```

Excluded:

```text
.git
binary payloads
superseded response versions as current authority
a32_holdout/custodian_private
```

Word-boundaried, case-insensitive queries included:

```text
response-state factorization | state identity | induced operator
tau_0 | epsilon | Haar state | trivial character | omega_H | omega_epsilon
connected covariance | second derivative | Z_inc | W_inc | raw correlator
K_L | fixture | frozen test object | target-independent
```

The exact symbolic check used only finite-support group-algebra operations on
the fixed generator. `a32_holdout/custodian_private/` was not entered, listed,
searched, opened, summarized, or read.

## 10. Final status

```text
FIXTURE_FROZEN_BEFORE_STATE_COMPARISON = true
FIXTURE_NOT_PHYSICAL = true
P_FIX_COMPLETE_FOR_DECLARED_TEST = true
P_FIX_TARGET_INDEPENDENT = true

Q211_EXACT_TWO_STATES_PLACED = true | TYPE-P | premises: DoR-008
STATE_ARMS_DIFFER_ONLY_IN_Q211_SCALARIZATION = true
FULL_INDUCED_OPERATORS_COMPARED_BEFORE_PROJECTION = true

K_EPSILON_FIX_IS_ZERO_OPERATOR = true
K_H_FIX_IS_NONZERO_OPERATOR = true
FULL_PREPROJECTION_OPERATOR_EQUAL = false | TYPE-R
FULL_PREPROJECTION_OPERATOR_EQUIVALENT_UNDER_U1 = false | TYPE-R

STATE_IDENTITY_CAN_AFFECT_INDUCED_RESPONSE = true | TYPE-P |
  premises: DoR-008 and P_fix
OBS14_STATE_IS_ROLE_ONLY_AT_RESPONSE_PRODUCER = false | TYPE-R
FIRST_STATE_SENSITIVE_COMPONENT = CONNECTED_CTP_SECOND_RESPONSE_OPERATOR
NEW_PHYSICS_ASK_LOCALIZED = RESPONSE_RELEVANT_STATE_CUMULANT_CLASS

PHYSICAL_STATE_IDENTITY_SELECTED = false | TYPE-S |
  scope: this artifact
PHYSICAL_PACKAGE_RESPONSE_VALUE_COMPUTED = false | TYPE-S |
  scope: this fixture-only comparison
FIXTURE_OPERATOR_TRANSPORTED_AS_PHYSICAL_OPERATOR = false | TYPE-R

PHYSICAL_VERDICT = OBS14_REFUTED_AT_RESPONSE_PRODUCER__PHYSICAL_STATE_REMAINS_UNBUILT
CONSTRUCTION_VERDICT = DIFFERENT__CONNECTED_SECOND_RESPONSE_CONSUMES_STATE_IDENTITY

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

No state was selected as physical. No response value, spectrum, eigenvalue,
coupling, scale, root, beta function, absolute interval, or measured
comparison was computed or evaluated. No register, baseline, Git, commit,
push, deployment, or publication action was performed.
