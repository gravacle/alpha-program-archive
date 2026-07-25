# Complete-Qspec Complex Zero-Free Runtime Portability Addendum v001

Date: 2026-07-25

## Trigger

The sealed v001 execution stopped before constructing any Qspec operator
because neither available Python runtime contains SciPy. No amplitude,
threshold, or physics result was evaluated.

## Append-only repair

Execution v002 must preserve the frozen zero-free specification unchanged
and replace only `scipy.linalg.expm` with a self-contained order-13 Pade
scaling-and-squaring matrix exponential.

Before any complex-disk evaluation, require:

```text
expm(0) identity error < 1e-14;
real-axis Pade/eigh exponential disagreement < 1e-11
at theta in {-1/100,0,+1/100};
real-axis unitarity error < 1e-11.
```

Failure blocks execution. No threshold from the zero-free specification may
be changed.

## Status

The v001 runtime failure is environmental and remains preserved. This
addendum authorizes only the dependency-free v002 implementation; it does
not authorize any scientific status change.
