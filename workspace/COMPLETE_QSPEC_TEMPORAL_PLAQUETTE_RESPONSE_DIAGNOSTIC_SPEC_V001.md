# Complete-Qspec Temporal-Plaquette Response Diagnostic Specification v001

Date: 2026-07-25

## Purpose

Determine whether the already frozen finite complete-Qspec parent responds to
an endpoint-trivial connection history with nonzero temporal-spatial
curvature, and whether that finite response already has the quadratic form
of a local Maxwell electric sector.

This is the next step after the independently confirmed finite global-
holonomy diagnostic. It changes no action, state, record interaction,
envelope, regulator subspace, or normalization.

No coupling target, alpha value, endpoint value, or measured electromagnetic
constant may be read or used.

## Frozen authorities

```text
69fa91955337a0b9c74aa4d4bbb78e42bc9d1e825eef4b5c47585742885db106  COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_RESULT_V001.md
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6  STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md
3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff  STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
0fe3905aa14ed744bda883dd68aa799dc9bb90f4f5647b477be3f6de65330f57  BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md
```

Any mismatch aborts execution.

## P1 - Frozen endpoint-trivial connection histories

The total two-cell duration is `0 <= t <= 2`. For each positive integer
`n` in `{1,2,3}`, define:

```text
f_n(t) = sin(n pi t/2)/(n pi/2).
```

These profiles obey:

```text
f_n(0)=f_n(2)=0;
integral_0^2 dot(f_n) dot(f_m) dt = delta_nm.
```

For a scalar test amplitude `a`, use the same uniform-link representative as
the global-holonomy diagnostic:

```text
theta_v(t)=a f_v(t);
U_(j,j+1)(t)=exp(i theta_v(t)/3).
```

Here `v` ranges over:

```text
f_1, f_2, f_3,
f_1+f_2, f_1+f_3, f_2+f_3.
```

The initial and final loop holonomies are exactly the identity. The
connection history nevertheless has:

```text
F_0x proportional to dot(theta_v)(t).
```

No profile may be replaced or rescaled after a response is seen.

## P2 - Frozen finite parent

Use the same:

```text
three-site periodic source regulator;
fixed eight-dimensional active one-particle subspace;
four-particle incoming Slater state selected at zero connection;
two intrinsic source-record interactions;
ER-A causal-diamond envelope;
two record quadratures;
complete final source-record identity.
```

At global time `0 <= t < 1`, apply the first intrinsic interaction with
local cell time `t`. At `1 <= t <= 2`, apply the second with local cell time
`t-1`. The time-dependent free source operator is evaluated from
`theta_v(t)` at every integration stage.

No completed-record outcome or final source state is postselected.

## P3 - Frozen numerical grid

Use:

```text
RK4 steps per cell: N = 800 and 1600
amplitude steps: a = 1/80 and 1/160
branches: +a and -a for every declared profile
```

For each profile `v`, compute:

```text
Z_v(+a)=<Psi_0|Psi_(+a,v)>
Z_v(-a)=<Psi_0|Psi_(-a,v)>

H_v(N,a)
 = [-log|Z_v(+a)|-log|Z_v(-a)|]/a^2.
```

First extrapolate fourth-order time error:

```text
H_inf(a)=H_1600(a)+(H_1600(a)-H_800(a))/15.
```

Then extrapolate the centered amplitude response:

```text
H_v(0)=[4 H_inf(1/160)-H_inf(1/80)]/3.
```

The uncertainty radius is:

```text
max absolute time correction
+ absolute amplitude correction
+ 1e-8.
```

No tolerance may be altered after execution.

## P4 - Temporal response matrix

In the derivative-orthonormal basis `{f_1,f_2,f_3}`, define:

```text
M_ii = H_(f_i);
M_ij = [H_(f_i+f_j)-H_(f_i)-H_(f_j)]/2.
```

Propagate interval radii by the triangle inequality. Let `R` be the
entrywise nonnegative radius matrix. Weyl's inequality gives the certified
positive-definiteness lower bound:

```text
lambda_min(M_true) >= lambda_min(M_center)-||R||_2.
```

## P5 - Two separate verdicts

### Curvature-response verdict

Return:

```text
FINITE_TEMPORAL_PLAQUETTE_RESPONSE_PRESENT
```

only if:

```text
all authority and structural checks pass;
all endpoint holonomies are identity;
all state norm errors are below 2e-9;
all diagonal response intervals are strictly positive;
lambda_min(M_center)-||R||_2 > 0.
```

Otherwise return:

```text
FINITE_TEMPORAL_PLAQUETTE_RESPONSE_BLOCKED
```

### Local-Maxwell verdict

The derivative-orthonormal profiles all have the same local Maxwell norm. A
time-local constant-coefficient electric response therefore requires:

```text
every off-diagonal response interval contains zero;
the three diagonal response intervals have a nonempty common intersection.
```

If those conditions hold, return:

```text
FINITE_TEMPORAL_LOCAL_MAXWELL_FORM_SUPPORTED
```

Otherwise return:

```text
FINITE_TEMPORAL_RESPONSE_NONLOCAL_OR_INHOMOGENEOUS
```

The second verdict is diagnostic, not repairable by selecting a preferred
profile. A failure means this finite parent has not yet earned a local
Maxwell interpretation.

## Negative controls

Verify:

```text
a=0 gives Z=1;
every profile vanishes at t=0 and t=2;
the total loop holonomy is the identity at both endpoints;
the connection remains anti-Hermitian;
the stripped open-tree zero-stiffness result remains untouched;
no determinant or final-state postselection is introduced.
```

## Scope ceiling

Even both positive verdicts would establish only a finite temporal electric-
sector diagnostic. They would not establish:

```text
the spatial magnetic plaquette sector;
electric-magnetic equality;
the full local Maxwell tensor;
continuum, cellulation, or packing independence;
the linked-cluster density;
the Thomson limit;
kappa_record;
alpha;
or proof authorization.
```

## Fixed status

```text
complete_Qspec_CTP_scalar_closure_derived = true
finite_Qspec_holonomy_response_diagnostic_passed = true
finite_temporal_plaquette_response_computed = false
local_Maxwell_response_derived = false
interacting_continuum_CTP_amplitude_derived = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
