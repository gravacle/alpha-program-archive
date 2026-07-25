# Complete-Q_spec Finite-Holonomy Response Diagnostic Specification v001

Date: 2026-07-25

## Purpose

Test whether the derived relative-history CTP scalar closure carries a
nonzero gauge-holonomy response on the existing finite source-record
regression, and whether its Hessian agrees with the pure-state
Duhamel/Fubini-Study covariance.

This is a finite-regulator diagnostic. It cannot compute a local Maxwell
coefficient, a continuum stiffness, or a coupling.

No coupling target may be read or used.

## Frozen authorities

```text
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6  STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md
3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff  STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
0fe3905aa14ed744bda883dd68aa799dc9bb90f4f5647b477be3f6de65330f57  BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md
```

Any mismatch aborts execution.

## H1 - Frozen finite connection direction

Use the existing three-site periodic source regulator. Let `theta` be the
total `U(1)` Wilson-loop angle. Translation symmetry fixes the uniform-link
representative:

```text
U_(j,j+1)=exp(i theta/3).
```

The covariant central difference is:

```text
D_theta[j,j+1] += (1/2) exp(i theta/3);
D_theta[j,j-1] -= (1/2) exp(-i theta/3).
```

It must be anti-Hermitian, and the loop product must equal
`exp(i theta)`. The source Hamiltonian is:

```text
h_source(theta)=(-i D_theta) tensor alpha_x.
```

Use the pre-existing nonzero-mode regulator subspace and incoming
negative-energy Slater state defined at `theta=0`. Do not reselect the
subspace or state as `theta` varies.

This direction probes global finite holonomy. It is not relabeled as local
field strength.

## H2 - Complete parent and CTP overlap

Use the actual two-cell time-dependent CAR parent, intrinsic `ER-A` envelope,
record quadratures, and complete final source-record identity from the
finite-Fock authority.

For each `theta`, evolve the same normalized incoming state:

```text
|Psi_theta>=W_K[theta]|Psi_in>.
```

Compute:

```text
Z(theta)=<Psi_0|Psi_theta>;
Gamma(theta)=-log|Z(theta)|.
```

No completed-record outcome or final source state is postselected.

## H3 - Independent response identities

Using symmetric, predeclared steps and time-resolution convergence, compute:

```text
H_CTP=Gamma''(0);

|dot Psi> = d|Psi_theta>/dtheta at theta=0;
g_FS=<dot Psi|dot Psi>-|<Psi_0|dot Psi>|^2.
```

The two must agree within a tolerance frozen from the observed time-step and
parameter-step tails, not from a desired value.

The diagnostic passes only if:

```text
H_CTP>0;
g_FS>0;
H_CTP and g_FS converge;
and their certified intervals overlap.
```

## H4 - Negative controls

Verify:

```text
theta=0 gives Z=1;
common-branch CTP normalization remains one;
the stripped open tree remains zero-stiffness;
and replacing the complete overlap by one completed-record amplitude is not
performed.
```

## Verdict rule

Return:

```text
FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_PASS
```

only if H1-H4 pass.

Otherwise return:

```text
FINITE_QSPEC_HOLONOMY_RESPONSE_DIAGNOSTIC_BLOCKED
```

## Scope ceiling

Even a pass establishes only that the complete-`Q_spec` scalar closure can
carry gauge holonomy and that two finite response computations agree. It
does not establish:

```text
continuum-regulator independence;
local Maxwell tensor form;
packing independence;
linked-cluster density;
the Thomson limit;
kappa_record;
or alpha.
```

## Fixed status

```text
complete_Qspec_CTP_scalar_closure_derived = true
finite_Qspec_holonomy_response_diagnostic_passed = false
interacting_continuum_CTP_amplitude_derived = false
local_Maxwell_response_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
