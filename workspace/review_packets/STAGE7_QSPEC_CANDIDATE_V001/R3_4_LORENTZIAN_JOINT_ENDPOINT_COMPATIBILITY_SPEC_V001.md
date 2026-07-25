# R3.4 Lorentzian Joint-Endpoint Compatibility Specification v001

Date: 2026-07-24

## Purpose

Determine whether the primitive exact first-opening interval remains an exact
record endpoint for the already derived local Lorentzian source-record
Hamiltonian at arbitrary tangential momentum.

An exploratory pre-seal calculation showed momentum dependence. This is a
result-aware consistency gate, not a blind prediction.

## Hash-pinned inputs

```text
BID_LORENTZIAN_SOURCE_SCHUR_POLE_DERIVATION_V001.md
  dc0498615a94218c56ed91a3e679a2aa55e32d4fcb96220a50a7a88669a8fc34

scripts/audit_bid_lorentzian_source_schur_pole_v001.py
  4de9e7528b86682670373ac6f1e215706013300c94c5b9febb880096216c832b

BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
  6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546

scripts/audit_bid_free_quasifree_ctp_propagator_v001.py
  922260b10d026be0e8f9f13d48cc880fc2db56e9ba0f1e5ea6fd861a869adb0b

BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
  7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476

scripts/audit_bid_first_opening_interval_v001.py
  c5de96772a85f128df0a51a68d364a61c73b8c94c7e8e13e26b95964048651d5

CAUSAL_DIRECT_LIMIT_RECORD_HYPOTHESIS_V001.md
  60c82b021a7f5ffcb514ae8c20f083a7b2c9b42872586922b1c0464c4822d73f
```

## Frozen Hamiltonian

Use the derived local Hamiltonian

```text
H(p)
 =alpha_vec dot p
  -i mu gamma^0 gamma^5 tensor c_partial,

H(p)^2=|p|^2+mu^2 c_partial^2.
```

Set physical units only for the dimensionless check:

```text
T_R=1;
tau_R=pi/sqrt(2);
mu=tau_R/T_R.
```

No observed mass, coupling, endpoint, or alpha value is used.

## Required derivation

Decompose the record endpoints as

```text
z=(r+p)/sqrt(2),  c_partial z=0;
m=(r-p)/sqrt(2),
```

where `m` belongs to the two-dimensional massive record sector with
frequency

```text
E(p)=sqrt(|p|^2+2 mu^2).
```

Exact `r -> p` transfer requires:

```text
sin(E t)=0;
exp(-i alpha_vec dot p t) on the input spin ray
  has the parity opposite to cos(E t).
```

Equivalently, for a momentum-eigen spin ray,

```text
E t=n pi;
|p| t=k pi;
n+k is odd.
```

The gate must prove that `p=0,t=T_R` passes and that generic nonzero momentum
does not share one universal exact-transfer time. A continuous wavepacket
therefore cannot be promoted to an exact finite-cell endpoint by the
record-only interval.

## Interpretation gate

Failure of exact finite-wavepacket transfer does not authorize a transported
interaction chosen to restore it. The causal direct-limit program already
requires thresholded asymptotic durability:

```text
for every delta>0 there is T_delta such that
sup_(t>=T_delta) |A_infinity(t)|^2 < delta.
```

The result must therefore distinguish:

```text
primitive internal action interval;
exact rest-normal endpoint benchmark;
and physical thresholded outgoing durability.
```

## Verdicts

```text
EXACT_ENDPOINT_REST_NORMAL_ONLY_THRESHOLD_ROUTE_REQUIRED
EXACT_ENDPOINT_UNIVERSAL
JOINT_ENDPOINT_COMPATIBILITY_BLOCKED
```

## Fixed statuses

```text
universal_exact_finite_wavepacket_write_derived = false
physical_thresholded_durability_derived = false
physical_in_state_selected = false
complete_root_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
