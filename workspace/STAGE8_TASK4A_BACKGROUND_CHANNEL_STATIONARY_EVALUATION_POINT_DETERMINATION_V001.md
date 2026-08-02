# Stage 8 Task 4a Background-Channel Stationary Evaluation-Point Determination v001

Date: 2026-08-02
Lane: CODEX LANE 2
Task: 4a
Authority: DoR-011, construction and symbolic trace only
Relay: 332
Register head at issue: Q-248
Register head consulted at completion: Q-250

## 0. Lead determination

**OUTCOME (iii): THE PHYSICAL EVALUATION SURFACE IS PARTLY FIXED, BUT THE
COMMON STATIONARY BACKGROUND IS NOT INSTANTIATED, AND ITS `p_ch` DEPENDENCE IS
`NO_VERDICT`.**

The exact finite relative-phase functional has a sharper result. For every
finite `N` and every interior `0<p_ch<1`, its stationary set on the full
ratified relative-holonomy domain is empty. Writing

```text
Theta_N := sum_j theta_j,
A_N^(p) := (1-p)+p exp(i Theta_N),
Gamma_N^(p) := -log A_N^(p),
```

one has, everywhere that the logarithm is defined,

```text
D Gamma_N^(p)
  = -i [p exp(i Theta_N)/A_N^(p)] w_N,

w_N(delta theta) := sum_j delta theta_j.
```

The scalar prefactor never vanishes for `0<p<1`, and `w_N` is a nonzero
covector. At the exceptional real-domain zero of `A_N^(p)` the logarithm is
undefined, not stationary. Therefore:

```text
FINITE_RELATIVE_PHASE_STATIONARY_SET = EMPTY | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011

FINITE_ZERO_HISTORY_IS_STATIONARY = false | TYPE-R |
  test: D Gamma_N^(p)|_0 = -i p w_N != 0 for 0<p<1

FINITE_STATIONARY_POINT_A_STAR_OF_P_EXISTS = false | TYPE-R |
  scope: the full independently varied finite relative-phase domain
```

This does **not** prove that the complete physical CTP action has no
stationary background. The finite object contains only the relative-history
phase summand and has no independently varied common-history argument. The
complete stationarity equation may contain other record, field, metric,
boundary, and source terms that are absent from the finite family.

The sealed physical response text fixes:

```text
A_delta = 0,     R = 0,
delta Gamma_2PI/delta G |_(G_*,R=0) = 0,
and, for a source-free stationary physical background, J = 0.
```

It does **not** fix `A_c=Abar` to zero. Nor does it construct
`Abar_*(p_ch)` or `G_*(Abar_*(p_ch))`. Three zeros that must not be identified
are:

```text
C1:              a=0       zero connection history in the finite law;
retarded extract: A_delta=0 equal forward/backward histories;
Legendre surface: J=R=0    vanishing external Legendre sources.
```

C1 is an operator-reduction certificate, not an evaluation prescription.
`A_delta=0` allows an arbitrary common background `A_c`. And `J=R=0` makes a
completed background stationary but does not say which stationary solution it
is. The state contained in the generating functional can affect that solution.

Thus the background channel remains open but unproved:

```text
PHYSICAL_COMMON_BACKGROUND_INSTANTIATED = false | TYPE-U |
  would-build: the common-origin completed source germ and its source-free
               stationary 2PI-to-1PI solution

PHYSICAL_EVALUATION_POINT_FORCED_TO_ZERO_CONNECTION = false | TYPE-R |
  test: C1, A_delta=0, and J=R=0 have distinct sealed meanings

PHYSICAL_BACKGROUND_DEPENDS_NONTRIVIALLY_ON_P_CH = NO_VERDICT |
  prerequisite: a completed common-origin functional and its stationary map

P_CH_REENTERS_COMPLETE_RETHESS_THROUGH_BACKGROUND = NO_VERDICT |
  prerequisite: the same stationary map plus the completed RetHess construction
```

Q-249 and Q-250 landed after the relay's Q-248 head. Q-249 confirms that the
stationary-background class is untyped. Q-250 proves response determination
only modulo a tail. Neither constructs the background or supersedes the result
here.

## 1. Preflight, scope, and authorities

### 1.1 Preflight

```text
DOES_THE_OBJECT_EXIST = SPLIT
  exact finite functional and stationary-condition question: yes;
  completed physical stationary background: no, TYPE-U.

IS_THE_VERSION_CURRENT = true_through_Q_250
  Q-249 and Q-250 were read before construction and incorporated.

ARE_ITS_INPUTS_PRESENT = SPLIT
  finite symbolic inputs: present as instances;
  completed physical source germ and background solver: absent.
```

### 1.2 Governing authorities

| Authority | SHA-256 | Use |
|---|---|---|
| `STAGE8_FINITE_P_CH_DEPENDENCE_AND_PHASE_RESIDUAL_TRANSPORT_DETERMINATION_V001.md` | `8a71b6cdeca839fb6e52dbac4c2d13f7b9d2dafc3531dc1cc8bdc9089b3410b0` | exact finite amplitude and derivatives |
| `STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md` | `2cd1ffcefd68ac03c6c09a4eca0dc9fe8d1adc8ac564cc0d050dfd41d79e6d0f` | C1 wording and connection-history typing |
| `STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md` | `57c06fcbedf4a486b87b42c02e6d13a92096ac6a56751d3ae5fd55f4b11deb57` | stationary reduction and retarded evaluation surface |
| `primitive_record_cell_selection_principle_v004.md` | `13d227ceb2198d96b0e4e2fef57b874cea71cb755320508fbf4c6d64a00c507e` | live 2PI identities and stationary background role |
| `primitive_complete_boundary_transition_functional_principle_v002.md` | `be79ca5e08010b53285cd157ba4c18d2029f08bc93bea2db02d5423b67428c34` | response near a stationary physical history |
| `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `20a3a17d44e15841baded9eaed3fdbecfde0ecb14bdb8162ea41a8bcd21d1a48` | distinct complete Thomson-response origin |
| `STAGE8_TASK4A_FINITE_HESSIAN_TO_DELTAPHI_TRANSPORT_MAP_CONSTRUCTION_AND_P_CH_TRACE_V001.md` | `70185aa842bc500724719c65bd66b5f07005e2214b97be0d35e07fd029d5c68c` | Q-243 CTP block typing |
| `STAGE8_TASK4A_CORRELATOR_COMPLETION_ARROW_AND_RESTRICTION_PINNING_DETERMINATION_V001.md` | `5b9a4a8b000c313049caa71aff4235cc9eb4b0f98bb2af9931fd8820930ed856` | Q-245 background channel |
| `STAGE8_TASK4A_PHYSICAL_RESPONSE_CLASS_SEALED_SIGNATURE_DETERMINATION_V001.md` | `8dc5e133c2cf857b1b6ea48c933717b29912b8a39bf192e946d2e36f0bef2e22` | Q-249 background-class stop |
| `STAGE8_TASK4A_RESPONSE_CLASS_FORCING_AND_TAIL_OUTPUT_INERTNESS_DETERMINATION_V001.md` | `fccd16a74269386a2fdb7bac122f907cd659c8eb09ae5f45eabf39e5e9180d79` | Q-250 later tail result; non-supersession check |

The cleanroom root, its parent principle root, and the supervision register
were entered. `a32_holdout/custodian_private/` was not entered.

### 1.3 Scope correction to the relay formula

The sealed finite authority uses

```text
Gamma_N^(p) = -log A_N^(p),
Gamma_CTP,N^(p) = -i log A_N^(p) = i Gamma_N^(p).
```

The relay's prose writes `Gamma_N=log A_N` while quoting the already-sealed
gradient with the minus sign. The calculation here follows the sealed formula.
Multiplication by the nonzero scalar `i` does not change the stationary set.
The version difference is reported, not repaired.

## 2. Exact finite stationary-set theorem

### 2.1 Domain

For finite `N`, the ratified relative characters obey

```text
conjugate(z_(-,j)) z_(+,j) = exp(i theta_j),
Theta_N = sum_j theta_j,
Z_N = exp(i Theta_N).
```

The local logarithm domain is the connected branch from coincidence inside

```text
D_p := {theta in (R/2pi Z)^N : A_N^(p)(theta) != 0}.
```

For interior `p`, a real-domain zero requires simultaneously

```text
|1-p|=|p|  and  exp(i Theta_N)=-1.
```

Hence only the midpoint weight has a real singular locus, and that locus is
excluded from `D_p`. No singular point is a stationary point of `log A`.

### 2.2 Gradient and Hessian

Let

```text
q_N := p exp(i Theta_N),
A_N := 1-p+q_N.
```

For each independently varied `theta_j`, exact differentiation gives

```text
partial_j Gamma_N = -i q_N/A_N,

partial_j partial_k Gamma_N
  = q_N(1-p)/A_N^2                 for every j,k.
```

Equivalently,

```text
D Gamma_N = -i(q_N/A_N) w_N,
D^2 Gamma_N = [q_N(1-p)/A_N^2] w_N tensor w_N.
```

For `0<p<1` and `theta in D_p`, `q_N` is nonzero and `A_N` is finite and
nonzero. Since `w_N` is nonzero, `D Gamma_N` cannot vanish. Therefore

```text
Stat_Dp(Gamma_N^(p)) = empty set.
```

The redistribution directions `ker w_N` are flat directions of this
functional, but they do not make any point stationary: the summed-phase
direction remains and has nonzero derivative.

At coincidence,

```text
D Gamma_N|_0 = -i p w_N,
D^2 Gamma_N|_0 = p(1-p) w_N tensor w_N.
```

For the complete CTP convention, multiply both expressions by `i`. Their zero
sets are unchanged.

### 2.3 Pullback to an underlying connection coordinate

If an independently supplied connection map `a -> Theta_N(a)` is used, the
chain rule gives

```text
D_a Gamma_N
  = -i[q_N/A_N] D_a Theta_N.
```

Thus, on the logarithm domain and for interior `p`, a pullback stationary point
exists exactly where `D_a Theta_N=0`. This condition is independent of `p`.
The ratified finite family does not seal a complete physical connection domain
or a map whose critical set could be identified with the physical background.

```text
PULLBACK_STATIONARY_SET_EQUALS_CRITICAL_SET_OF_THETA = true | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011 |
  scope: any independently supplied differentiable pullback

PHYSICAL_PULLBACK_MAP_INSTANTIATED = false | TYPE-U |
  would-build: the finite-to-completed physical source/connection map
```

This conditional pullback fact is not an `a_*(p)` selection. It gives no
`p`-dependent point and cannot be transported to the complete response without
the missing map.

### 2.4 Independent symbolic check

A separately entered symbolic differentiation from the defining expression,
using the vendored symbolic package rather than the hand derivation, returned

```text
d Gamma/dTheta = -i p exp(i Theta)/(p exp(i Theta)-p+1),
residual against the stated second-derivative identity = 0,
d Gamma/dTheta at Theta=0 = -i p,
d^2 Gamma/dTheta^2 at Theta=0 = p(1-p).
```

The symbolic check agrees with the authoritative derivation. It was not used
to select a point or evaluate a physical response.

## 3. What the sealed response is evaluated at

### 3.1 C1 does not force zero-history evaluation

The ratified result states at
`STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md:300-319`:

> At `a=0`, every `D_n[0]=I_3`, so `W_N[0]=S_N` and
> `U_N[0]=P_0 tensor I_(3^N)+P_ch tensor S_N=U_N^0`.

This is exact operator reduction of the source-coupled law to the sealed write.
It says what the law becomes at zero connection history. It contains no
instruction to take a response derivative there and no assertion that zero
connection is a stationary background.

The counterexample is internal: the same ratified finite functional satisfies
C1, yet its exact derivative at zero is nonzero for every interior `p`.
Therefore the implication `C1 => zero is the evaluation point` is refuted.

```text
C1_IS_ZERO_SOURCE_OPERATOR_REDUCTION = true | TYPE-P |
  premises: DoR-008, DoR-009

C1_IMPLIES_ZERO_IS_STATIONARY = false | TYPE-R |
  test: C1 passes while D Gamma_N|_0 != 0

C1_SELECTS_PHYSICAL_RESPONSE_BACKGROUND = false | TYPE-R |
  test: its signature returns an operator equality, not a stationary solution
```

### 3.2 The physical CTP/2PI prescription

The live 2PI principle gives
(`primitive_record_cell_selection_principle_v004.md:71-79`):

> `delta Gamma_2PI/delta Abar = -J - R Abar` and
> `delta Gamma_2PI/delta G = -R/2`. At vanishing physical sources, both
> derivatives vanish.

The raw-correlator-to-retarded-Hessian specification then requires
(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:724-755`):

> `Gamma_1PI[Abar] := Gamma_2PI[Abar,G_*(Abar)] |_(R=0)` and
> `delta Gamma_2PI/delta G |_(G_*,R=0)=0`.

Its retarded extraction is
(`STAGE8_RAW_CORRELATOR_TO_RETARDED_HESSIAN_MAP_SPEC_V001.md:785-819`):

> `H_R[G] = delta^2 Gamma_1PI/(delta A_delta delta A_c)` at
> `A_delta=0` and `R=0`.

These texts force a **surface and equation**, not a background instance:

```text
equal histories:           A_delta=0;
no bilocal Legendre source: R=0;
source-free saddle:         J=0;
stationary propagator:      G=G_*(Abar);
common background:          A_c=Abar, not fixed to zero.
```

At `J=R=0`, `Abar` is the expectation derived from the completed generating
functional, `Abar=delta W_inc/delta J`. Because `W_inc` consumes `rho_pre`, its
stationary solution may depend on state data. The corpus neither proves that
dependence nor proves its cancellation.

```text
PHYSICAL_RESPONSE_SURFACE_PARTLY_FIXED = true |
  fields: A_delta=0, R=0, and source-free J=0

PHYSICAL_COMMON_BACKGROUND_VALUE_FIXED = false | TYPE-U |
  would-build: solve the completed common-origin 2PI source and propagator
               equations on the physical quotient

PHYSICAL_COMMON_BACKGROUND_P_CH_INDEPENDENT = NO_VERDICT
PHYSICAL_COMMON_BACKGROUND_P_CH_DEPENDENT = NO_VERDICT
```

### 3.3 The older complete-history principle

`primitive_complete_boundary_transition_functional_principle_v002.md:39-55`
says only:

> Near a stationary physical history the quadratic functional has the form
> `integral A_delta D_R^(-1) A_c + ...`.

It presupposes a stationary physical history but does not identify one. Its own
hard-gate block records `stationary_record_cell_derived=false` at `:106-124`.

```text
OLDER_CTP_TEXT_SELECTS_A_STATIONARY_HISTORY = false | TYPE-S |
  roots: primitive_complete_boundary_transition_functional_principle_v002.md |
  query: stationary, background, evaluation, A_c, A_delta |
  result: role named; instance absent
```

### 3.4 Thomson text fixes a probe origin, not this background

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1613-1628` defines the separate
complete charged response through

```text
Z_Q[A]/Z_Q[0],
Gamma_Q[A]=-i Log(Z_Q[A]/Z_Q[0]),
```

with its logarithm branch fixed continuously at `A=0`, followed by its
quadratic response. This fixes the normalization and expansion origin of the
unbuilt complete charged probe functional. It does not identify:

```text
the finite relative-history variable theta with the complete probe A;
the zero probe with Abar_*=0;
or the finite amplitude A_N^(p) with Z_Q[A]/Z_Q[0].
```

No sealed bridge establishes any of those identities.

```text
THOMSON_TEXT_FORCES_FINITE_C1_BACKGROUND = false | TYPE-R |
  test: distinct carrier, functional, and role; no sealed identity map

COMPLETE_THOMSON_FUNCTIONAL_INSTANTIATED = false | TYPE-U |
  would-build: the Q_spec object listed at V011:1592-1606
```

## 4. Background-channel adjudication

The finite exact result does not realize outcome (ii): it supplies no
`a_*(p)` at which to evaluate its Hessian. It also refutes outcome (i): zero
history is not stationary for the finite functional, C1 does not appoint it,
and `A_delta=0` is not `A_c=0`.

The sealed record supports outcome (iii), with a refinement:

```text
EVALUATION_SURFACE = PARTLY_FORCED
  A_delta=0; R=0; source-free stationarity uses J=0.

EVALUATION_POINT_WITHIN_SURFACE = UNTYPED_AND_UNBUILT
  Abar_* and G_*(Abar_*) are not instantiated.

P_CH_DEPENDENCE_OF_EVALUATION_POINT = NO_VERDICT
```

The exact finite one-point term proves only that the isolated relative-phase
summand exerts a nonzero difference-direction gradient at coincidence. It does
not prove that the complete stationary equation has a `p_ch`-dependent
solution: other unbuilt terms may cancel, modify, or fail to admit the finite
term after completion.

The background channel therefore remains exactly one named construction wide:

```text
COMMON_ORIGIN_STATIONARY_BACKGROUND_MAP:
  (completed Z_inc/Log_0, rho_pre, effects, dynamics, physical source domain)
    -> (Abar_*, G_*(Abar_*)) at J=R=0
    -> H_R[G_*(Abar_*)] at A_delta=0
```

The map must declare the source topology/calculus, physical quotient, contour,
measure, contacts, boundary/domain data, and stationary-solution class. It must
then prove whether varying the response-visible source weight changes the
solution or is annihilated before evaluation. No output may be used to choose
the background.

## 5. Kill-passes and symbol collisions

### 5.1 No imported stationary-phase prescription

No stationary-phase approximation, vacuum choice, or background-selection
convention was imported. The only stationarity equations used are the sealed
2PI identities quoted above.

```text
IMPORTED_STATIONARITY_PRESCRIPTION_USED = false | TYPE-S |
  scope: this construction
```

### 5.2 No record-write/response-stationarity conflation

The finite write law, the finite relative-history functional, and the physical
2PI response occupy different signatures. The empty stationary set belongs
only to the finite relative-phase functional. The complete physical
stationarity verdict remains `NO_VERDICT`.

```text
FINITE_EMPTY_STATIONARY_SET_TRANSPORTED_TO_COMPLETE_PHYSICS = false | TYPE-S |
  scope: this construction
```

### 5.3 Load-bearing symbol collisions

1. `a=0` in C1 is a zero connection/holonomy history; it is not the source
   equation `J=R=0`.
2. `A_delta=0` means equal branches; it does not imply `A_c=0`.
3. `A_N^(p)` is a scalar finite amplitude; `Abar` is a physical mean field.
4. `G_*` is the stationary raw propagator; it is not the finite scalar Hessian.
5. The relay's `Gamma=log A`, the sealed `Gamma_N=-log A`, and the physical
   `Gamma_CTP=-i log A` differ by sign/nonzero scalar conventions. Their
   stationary zero sets agree where defined, but their values must not be
   interchanged.

## 6. Final verdict

```text
FINITE_RELATIVE_PHASE_STATIONARY_SET = EMPTY | TYPE-P |
  premises: DoR-008, DoR-009, DoR-011

ZERO_CONNECTION_HISTORY_FORCED_AS_PHYSICAL_EVALUATION_POINT = false | TYPE-R
C1_IS_A_RESPONSE_EVALUATION_RULE = false | TYPE-R
A_DELTA_ZERO_IMPLIES_A_C_ZERO = false | TYPE-R

PHYSICAL_RESPONSE_SURFACE_PARTLY_FIXED = true
PHYSICAL_STATIONARY_BACKGROUND_INSTANTIATED = false | TYPE-U
PHYSICAL_STATIONARY_BACKGROUND_P_CH_DEPENDENCE = NO_VERDICT
P_CH_BACKGROUND_REENTRY_IN_COMPLETE_RETHESS = NO_VERDICT

OUTCOME = III__EVALUATION_POINT_UNBUILT_WITHIN_A_PARTLY_FORCED_SURFACE

alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

The finite functional has no interior stationary point to select. The physical
corpus prescribes equal histories and vanishing Legendre sources, but not a
zero common background and not a completed stationary solution. Accordingly,
the background channel is neither proved real nor closed: it remains
`NO_VERDICT` at the one missing common-origin stationary-background map.
