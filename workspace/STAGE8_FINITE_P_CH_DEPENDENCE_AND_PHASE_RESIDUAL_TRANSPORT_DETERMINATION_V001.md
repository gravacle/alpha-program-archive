# Stage 8 Finite p_ch Dependence and Phase-Residual Transport Determination v001

Date: 2026-08-02
Lane: CODEX LANE 1
Task: Task 2d
Register head consulted: Q-236
Scoped authority: Decision of Record 010
Standing: `TYPE-P | premises: DoR-008, DoR-009` for the finite family and
`AUTHORIZED_SCOPE | authority: DoR-010` for the variations and structural
transport test

## 0. Lead determination

**VERDICT: `UNDECIDABLE-YET`.** The finite calculation is exact, but the
transport needed to answer the physical residual question is not sealed.

At every finite `N`, write the relative characters as

```text
Z_N = exp(i Theta_N),
Theta_N = sum_(j=1)^N theta_j,
A_N^(p) = 1-p+p exp(i Theta_N),             0<p<1,
Gamma_N^(p) = -log A_N^(p).
```

Then, at coincidence `theta_1=...=theta_N=0`,

```text
partial_(theta_j) Gamma_N^(p) = -i p,

partial_(theta_j) partial_(theta_k) Gamma_N^(p)
  = p(1-p)                                      for every j,k,

delta_1 delta_2 Gamma_N^(p)
  = p(1-p)
    (sum_j delta_1 theta_j)(sum_k delta_2 theta_k).
```

The exact connected-bilinear factor is therefore

```text
f_2(p) = p(1-p).
```

The equal-history normalization does **not** cancel it: `A_N^(p)(0)=1` for
every `p`, while the normalized Hessian still carries `p(1-p)`.

But this does not establish that `p(1-p)` survives into
`C_record(K)=DeltaPhi[K;X_K]-pi`. The calculated Hessian has only
difference-history directions. The sealed CTP decomposition types a
difference/difference quadratic term as the noise/attenuation sector, whereas
the coherent retarded response is a mixed difference/common derivative.
Neither that mixed derivative nor a map from the finite Hessian to
`DeltaPhi[K;X_K]` is supplied. The phase residual itself is displayed as an
additive difference, not a ratio, and its on-shell map remains unbuilt.

Thus two tempting conclusions are both unsupported:

```text
P_INDEPENDENT_BY_FINITE_NORMALIZATION_CANCELLATION = false | TYPE-R |
  test: exact normalized finite Hessian retains p(1-p)

P_DEPENDENT_AT_THE_PHYSICAL_PHASE_RESIDUAL = NO_VERDICT | TYPE-U |
  blocker: no sealed finite-Hessian-to-mixed-response-to-DeltaPhi transport,
           no sealed homogeneity/normalization rule for that transport, and
           no completed on-shell X_K map

P_DEPENDENCE_VERDICT = UNDECIDABLE-YET | TYPE-U |
  would-build: the complete finite-to-physical CTP response map, its mixed
               retarded Hessian, and an explicit on-shell DeltaPhi functional
               showing whether overall kernel scaling has degree zero or one
```

This artifact does not infer that `p_ch` is gauge-like, and it does not infer
that `p_ch` is a physical input to `K_*`. It identifies exactly what the
finite family proves and where the physical inference stops.

```text
FINITE_CONNECTED_BILINEAR_P_FACTOR = p_ch(1-p_ch)
FINITE_FIRST_PHASE_CUMULANT_P_FACTOR = p_ch

RELATIVE_PHASE_HESSIAN_IS_MIXED_RETARDED_RESPONSE_KERNEL = false | TYPE-R |
  test: its domain has difference-history directions only, while the sealed
        retarded kernel is the mixed difference/common derivative

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Preflight, scope, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = true
  Q-236 supplies the exact finite family A_N^(p)=1-p+p Z_N

IS_THE_VERSION_CURRENT = true
  register head Q-236 was rechecked before sealing; DoR-010 is in force

ARE_ITS_INPUTS_PRESENT = true
  p remains symbolic, Z_N is exact, and coincidence is an admitted point
```

The calculation uses the interior `0<p<1` required by the relay. The formulas
extend algebraically to the endpoints, but no endpoint is selected or used.
At coincidence `A_N^(p)=1`, so the logarithm has a nonzero local neighborhood
on the branch continued from coincidence. No global logarithm claim is made.

### 1.2 Governing sources

| Source | Lines / content used |
|---|---|
| `STAGE8_SHARED_FINITE_STATE_EFFECT_CONDITIONED_AMPLITUDE_SHARP_STOP_V001.md` | `18-36`, exact family; `185-223`, exact state quotient; `225-248`, one-cell formula; `416-457`, normalization and sequential checks |
| `primitive_complete_boundary_transition_functional_principle_v002.md` | `16-35`, normalized complex CTP functional; `37-65`, mixed retarded versus difference/difference noise kernels; `67-104`, primitive phase map and conditional phase residual |
| `primitive_record_cell_selection_principle_v004.md` | `115-168`, prospective physical residual and projected equation; `186-194`, phase condition is separate and does not replace the full residual |
| `STAGE8_C_RECORD_LIVE_DEFINITION_CURRENCY_AUDIT_V001.md` | `225-246`, phase form is sealed but conditional and not uniquely appointed; `375-407`, live abstract output and unresolved executable formula |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `16`, map unbuilt; `42-49`, missing physical package fields; `119-129`, four upstream response objects; `845-846`, induced kernel and local projector unbuilt |
| `STAGE8_DELTAPHI_PI_PROTECTION_DETERMINATION_V001.md` | `124-171`, structural `DeltaPhi` display; `189-200`, full-generator proviso; `231-240`, selector map unprotected/unbuilt |
| `DECISION_OF_RECORD_010_STRUCTURAL_P_DEPENDENCE_AUTHORIZED_2026-08-02_V001.md` | authorizes only finite symbolic variations and the structural cancellation/survival test |
| `QUESTIONS_SETTLED_REGISTER_V001.md` | Q-185 through Q-236 rechecked for later appointment or supersession of the phase form; none appears |

The three sealed cleanroom authorities with sidecars used here verify against
their recorded hashes. The parent principles have no adjacent sidecars; their
hashes and currency are reported in the sealed C-record audit.

### 1.3 Scope boundary

Performed:

```text
exact symbolic differentiation in theta_j;
coincidence expansion;
exact N=1 and arbitrary finite-N bilinear;
source-level type comparison against the sealed CTP decomposition;
structural trace into the displayed phase residual.
```

Not performed:

```text
no numerical kernel evaluation;
no finite-to-continuum limit;
no second variation in a physical gauge field;
no mixed A_delta/A_c response extraction;
no induced kernel or B_ind construction;
no residual evaluation or root solve;
no coupling, scale, or measured comparison.
```

## 2. Exact one-cell calculation

For one cell,

```text
A_1^(p)(theta) = 1-p+p exp(i theta).
```

Set

```text
q(theta) := p exp(i theta),
A(theta) := 1-p+q(theta).
```

Then

```text
dA/dtheta = i q,
d^2A/dtheta^2 = -q.
```

Using `Gamma=-log A`,

```text
dGamma/dtheta
  = -(1/A) dA/dtheta
  = -i q/A.
```

For the second derivative,

```text
d^2Gamma/dtheta^2
  = (1/A^2)(dA/dtheta)^2 - (1/A)(d^2A/dtheta^2)
  = -q^2/A^2 + q/A
  = q(A-q)/A^2
  = q(1-p)/A^2.
```

At coincidence, `q=p` and `A=1`, so

```text
(dGamma/dtheta)|_0 = -i p,
(d^2Gamma/dtheta^2)|_0 = p(1-p).
```

Equivalently,

```text
Gamma_1^(p)(theta)
  = -i p theta + (1/2)p(1-p) theta^2 + O(theta^3).
```

This is an exact symbolic expansion; no value of `p` or `theta` is chosen.

```text
N1_FIRST_VARIATION_DERIVED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-010 scope

N1_CONNECTED_SECOND_VARIATION_DERIVED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-010 scope
```

## 3. Exact arbitrary finite-N calculation

Each sealed relative character has unit form

```text
conjugate(z_(-,j)) z_(+,j) = exp(i theta_j).
```

Therefore

```text
Theta_N := sum_j theta_j,
Z_N = exp(i Theta_N),
A_N^(p) = 1-p+p exp(i Theta_N).
```

The functional depends on the `N` variables only through `Theta_N`. Define

```text
q_N := p exp(i Theta_N),
A_N := 1-p+q_N.
```

For every `j`,

```text
partial_j q_N = i q_N,
partial_j A_N = i q_N,

partial_j Gamma_N = -i q_N/A_N.
```

For every pair `j,k`, including `j=k`,

```text
partial_j partial_k Gamma_N
  = q_N(1-p)/A_N^2.
```

At coincidence,

```text
partial_j Gamma_N|_0 = -i p,
partial_j partial_k Gamma_N|_0 = p(1-p).
```

Hence for two arbitrary phase variations `delta_1 theta` and
`delta_2 theta`,

```text
delta_1 delta_2 Gamma_N|_0
  = p(1-p)
    (sum_j delta_1 theta_j)
    (sum_k delta_2 theta_k).
```

The Hessian therefore has one supported direction, the summed relative phase;
every redistribution with zero total relative phase lies in its null
directions. No spectral claim or value is needed for this statement.

For `N=2`, explicitly,

```text
Gamma_2^(p)
  = -i p(theta_1+theta_2)
    +(1/2)p(1-p)(theta_1+theta_2)^2
    +O(theta^3),
```

so the diagonal and cross connected bilinears carry the same factor
`p(1-p)`.

```text
GENERAL_N_CONNECTED_BILINEAR_DERIVED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-010 scope

CONNECTED_BILINEAR_FACTOR = p(1-p)
CONNECTED_BILINEAR_SUPPORT = summed relative-phase direction
```

## 4. Cumulant and CTP typing

The exact finite amplitude is the characteristic function of a two-sector
variable that is zero with weight `1-p` and one with weight `p`:

```text
A_N^(p) = (1-p) exp(i 0 Theta_N) + p exp(i 1 Theta_N).
```

Thus the first two connected phase cumulants are

```text
kappa_1 = p,
kappa_2 = p(1-p).
```

This explains the two different factors without identifying either with a
physical Maxwell coefficient.

The parent CTP principle uses

```text
Gamma_CTP = -i log Z = i Gamma_N
```

for the present `Gamma_N=-log A_N` convention. Its expansion is

```text
Gamma_CTP
  = p Theta_N + (i/2)p(1-p) Theta_N^2 + O(Theta_N^3).
```

The linear term is coherent phase. The quadratic term is imaginary and is the
connected phase variance/attenuation term. This matches the source-level CTP
typing at `primitive_complete_boundary_transition_functional_principle_v002.md:46-65`:

```text
mixed A_delta/A_c derivative  -> retarded coherent response;
two A_delta derivatives       -> noise/attenuation.
```

The finite family in this task has only the relative phases `theta_j`; it has
no independently varied common-history phase. Therefore its exact Hessian is
a difference/difference object. It cannot, by itself, instantiate the mixed
retarded kernel.

```text
P_FACTOR_OF_CONNECTED_PHASE_VARIANCE = p(1-p)
P_FACTOR_OF_LINEAR_COHERENT_PHASE = p

FINITE_RELATIVE_PHASE_FAMILY_DETERMINES_MIXED_RETARDED_KERNEL = false |
  TYPE-R |
  test: the family has no common-history argument, while the sealed mixed
        kernel requires one difference and one common variation

P_PAREN_ONE_MINUS_P_IS_ALREADY_A_MAXWELL_RESPONSE_FACTOR = false | TYPE-R |
  test: sealed CTP sector typing places it in the difference/difference
        connected variance at this finite interface
```

This type result is load-bearing. A phrase such as “the `p`-factor of the
kernel” is ambiguous here: the finite family supplies a coherent first
cumulant with factor `p` and a connected second cumulant with factor
`p(1-p)`. The corpus does not authorize moving the second factor into the
coherent phase condition by vocabulary alone.

## 5. The finite normalization test

The Q-236 family is already normalized at coincidence:

```text
A_N^(p)(0)=1
```

for every `p`. Equivalently, dividing by the zero-history amplitude changes
nothing, because that denominator is exactly one. Nevertheless,

```text
partial_j partial_k[-log A_N^(p)]|_0 = p(1-p).
```

Therefore the normalization carried by the finite amplitude does not remove
the factor.

```text
FINITE_EQUAL_HISTORY_NORMALIZATION_CANCELS_P_FACTOR = false | TYPE-R |
  test: exact normalized Hessian above

FINITE_ZERO_HISTORY_DENOMINATOR_SUPPLIES_A_P_DEPENDENT_CANCELLATION = false |
  TYPE-R |
  test: denominator A_N^(p)(0)=1 for every p
```

This kills one proposed cancellation mechanism. It does not decide whether a
different, downstream on-shell ratio cancels a factor, because no such ratio
has been specified.

## 6. Trace into the phase residual

### 6.1 What the phase source actually displays

The phase candidate at
`primitive_complete_boundary_transition_functional_principle_v002.md:67-104`
defines

```text
C_record(K) = DeltaPhi[K;X_K] - pi.
```

This is an additive residual. The display contains no response-kernel
denominator and no homogeneity rule under an overall kernel rescaling.
It also states that the complete dynamics must supply `X_K` and the action
partition and prove the first crossing.

The protection determination sharpens the boundary:

```text
pi is protected within the fixed primitive record map;
K -> DeltaPhi[K;X_K] is unbuilt and unprotected.
```

Thus the target `pi` cannot supply the missing cancellation rule.

```text
DISPLAYED_PHASE_RESIDUAL_IS_A_KERNEL_RATIO = false | TYPE-R |
  test: exact source display is DeltaPhi[K;X_K]-pi

DELTAPHI_KERNEL_HOMOGENEITY_DEGREE_SEALED = false | TYPE-S |
  roots: phase source, v004 selection principle, Gamma_K spec, response-map
         spec, C-record currency audit, settled-question register Q-185:Q-236 |
  excl: mirrors; private holdout never entered |
  query: DeltaPhi, C_record, ratio, normalization, Hessian, kernel, phase |
  fences: no residual or root evaluation
```

### 6.2 Why absence of a displayed ratio does not prove survival

The active v004 principle states at `:186-194` that the phase condition:

1. applies only after the complete generator supplies the physical spectral
   gap;
2. does not fix the ultraviolet subtraction;
3. does not replace the full residual equation; and
4. is evaluated in a separate record-probability sector.

It also leaves the raw-correlator-to-retarded-Hessian map, exact induced
kernel, local projector, complementary residual, boundary data, and complete
operator unbuilt. The sealed response-map spec separately confirms that the
finite scalar CTP object is only prospectively upstream of the physical raw
correlator and retarded Hessian.

Consequently, the following composition is absent:

```text
A_N^(p)
  -> completed physical CTP functional
  -> mixed retarded Hessian
  -> exact induced/local response operator
  -> complete on-shell X_K
  -> DeltaPhi[K;X_K].
```

Without this composition, even the relevant factor is undecided:

```text
coherent first-cumulant route: candidate factor p;
connected difference/difference route: factor p(1-p);
possible downstream normalized route: homogeneity not stated.
```

The statement “the finite Hessian retains `p(1-p)`” is proved. The statement
“the physical phase residual retains `p(1-p)`” is not its type-preserving
consequence.

### 6.3 Countermodel to premature transport

The underdetermination can be stated without adopting either completion.
Mark the following as `HYPOTHETICAL_NOT_ASSERTED`:

```text
SURVIVAL-SHAPED completion:
  DeltaPhi is degree one in the transported response object;
  an overall factor survives.

CANCELLATION-SHAPED completion:
  DeltaPhi is a degree-zero normalized ratio of two quantities with the same
  transported factor;
  the factor cancels.
```

The sealed phase display, response spec, and v004 provisos do not instantiate
either completion. Their coexistence as unexcluded shapes proves that the
transport verdict cannot be selected from the finite Hessian alone. These
lines are logical countermodels to an inference, not proposed physical maps.

## 7. Verdict and exact would-build

```text
P_DEPENDENCE_OF_FINITE_CONNECTED_SECOND_VARIATION
  = P-DEPENDENT VIA p_ch(1-p_ch) | TYPE-P |
    premises: DoR-008, DoR-009, DoR-010 scope

P_DEPENDENCE_OF_FINITE_LINEAR_COHERENT_PHASE
  = P-DEPENDENT VIA p_ch | TYPE-P |
    premises: DoR-008, DoR-009, DoR-010 scope

P_DEPENDENCE_OF_C_RECORD_PHASE_RESIDUAL
  = UNDECIDABLE-YET | TYPE-U |
    would-build:
      1. one completed finite-to-physical CTP intertwiner;
      2. one physical common/difference source family;
      3. the mixed retarded Hessian on that family;
      4. the exact induced kernel and covariant local projection;
      5. the complete on-shell cell X_K with state dependence retained;
      6. an explicit DeltaPhi functional of those outputs;
      7. a proof of its homogeneity under overall response scaling.
```

For the scoped phase candidate, items 1-7 decide cancellation versus survival.
For a program-wide executable `C_record`, the existing authority gap also has
to be resolved: the sealed currency audit says the phase form is a conditional
candidate and no authority appoints one unique live executable formula.

```text
P_CH_PROVED_GAUGE_LIKE_FOR_THE_TARGET = false | TYPE-U |
  would-build: a degree-zero transport theorem through the seven items above

P_CH_PROVED_PHYSICAL_INPUT_TO_K_STAR = false | TYPE-U |
  would-build: a type-preserving transport theorem showing nonzero dependence
               of the complete on-shell phase residual on p_ch
```

No value or selector for `p_ch` is proposed.

## 8. Adversarial checks

### 8.1 First-versus-second cumulant check

The transformation `p -> 1-p` leaves `p(1-p)` invariant but changes the
linear factor `p`. Therefore the connected second variation alone cannot
reconstruct the coherent phase weight or select between complementary source
occupations.

```text
SECOND_VARIATION_ALONE_DETERMINES_LINEAR_PHASE_WEIGHT = false | TYPE-R |
  test: p and 1-p have the same p(1-p) and generally different p
```

### 8.2 Interior-domain check

For `0<p<1`,

```text
p(1-p)>0.
```

Thus the connected finite bilinear does not vanish on the record-existence
interior. This establishes nontrivial finite dependence, not a selected value.

### 8.3 N-dependence check

Increasing finite `N` changes only `Theta_N=sum_j theta_j`. It does not change
the factor `p(1-p)`. Hence no finite-stage count or zero-extension can remove
the state dependence.

```text
P_FACTOR_DEPENDS_ON_FINITE_N = false | TYPE-R |
  test: exact arbitrary-N Hessian
```

### 8.4 Target-blindness check

The derivation uses only the sealed amplitude family, symbolic differentiation,
and source-level type declarations. It inspects no coupling, residual output,
root, scale, or measured value.

```text
TARGET_AWARE_INPUT_USED = false | TYPE-S |
  scope: derivation in Sections 2-6
```

## 9. Final flag block and custody

```text
FINITE_N_SYMBOLIC_FIRST_VARIATION_DERIVED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-010 scope

FINITE_N_SYMBOLIC_CONNECTED_SECOND_VARIATION_DERIVED = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-010 scope

EXACT_CONNECTED_BILINEAR_P_FACTOR = p_ch(1-p_ch)
EXACT_LINEAR_COHERENT_PHASE_P_FACTOR = p_ch

FINITE_NORMALIZATION_CANCELLATION = false | TYPE-R |
  test: A_N^(p)(0)=1 and Hessian=p(1-p)

PHYSICAL_PHASE_RESIDUAL_P_VERDICT = UNDECIDABLE-YET | TYPE-U |
  would-build: the seven-item transport in Section 7

NUMERICAL_KERNEL_EVALUATED = false | TYPE-S | scope: this artifact
MIXED_RETARDED_KERNEL_EXTRACTED = false | TYPE-S | scope: this artifact
B_IND_CONSTRUCTED = false | TYPE-S | scope: this artifact
PHYSICAL_RESIDUAL_EVALUATED = false | TYPE-S | scope: this artifact
ROOT_SOLVED = false | TYPE-S | scope: this artifact
MEASURED_COMPARISON_PERFORMED = false | TYPE-S | scope: this artifact

FENCE_BLOCKED_STRUCTURAL_RESULT = false
MACHINERY_APPEAL = NOT_TRIGGERED

alpha_computed = false [TERMINAL_FENCE_DECLARATION]
proof_authorized = false [TERMINAL_FENCE_DECLARATION]
kappa_record_computed = false [TERMINAL_FENCE_DECLARATION]
coupling_evaluation_authorized = false [TERMINAL_FENCE_DECLARATION]
production_authorized = false [TERMINAL_FENCE_DECLARATION]
```

Custody under `LOCKED_PROCESS.md`: this lane seals this append-only artifact,
verifies its sidecar, mirrors only the artifact and sidecar to the archive
workspace, reports, and stops. It does not register, commit, push, amend a
Decision of Record, or edit any prior result.
