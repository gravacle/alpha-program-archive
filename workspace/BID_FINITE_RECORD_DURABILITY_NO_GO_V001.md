# BID Finite Record-Durability No-Go v001

Date: 2026-07-24

## Purpose

Test whether the exact one-cell BID incidence Hamiltonian that produces the
first orthogonal endpoint also makes that endpoint durable.

## Exact one-cell evolution

In the ordered basis

```text
(|r>,|p>,|e>),
```

the normalized cellular incidence quadrature is

```text
c_partial =
  [[0, 0, -i],
   [0, 0, +i],
   [+i,-i, 0]],

spec(c_partial)={-sqrt(2),0,+sqrt(2)}.
```

Let

```text
tau_R=pi/sqrt(2),
U(tau)=exp(-i tau c_partial).
```

Direct evaluation gives

```text
U(tau_R)|r> = |p>,
U(tau_R)|p> = |r>,
U(2 tau_R) = I.
```

Thus the exact operation that writes the first orthogonal endpoint erases it
one equal interval later. The endpoint projector also fails the
nondemolition condition:

```text
[c_partial, |p><p|] != 0.
```

The one-cell operator therefore provides a reversible write, not a durable
record.

## General finite-system boundary

Adding a finite number of closed unitary record degrees does not by itself
establish irreversible persistence. A finite discrete spectrum is recurrent.
A completed record can nevertheless be durable if the full action derives
one of:

```text
an exact superselection/central sector;
an invariant post-write pointer algebra;
an infinite causal/environmental limit with asymptotic outgoing sectors;
or a derived open-system limit from a larger unitary theory.
```

These mechanisms are physically inequivalent and may not be selected after a
response is evaluated.

## Consequence for the parent action

The finite stationary quasi-free CAR lift remains a valid primitive
incidence skeleton. It is not the complete source-record-environment parent.
The next candidate must extend the same target-independent incidence law to a
causal direct limit and prove that a completed record becomes an asymptotic
recoverable sector. Merely increasing the finite cell count or calling
orthogonality durability does not pass.

## Status

```text
one_cell_first_orthogonal_write_derived = true
one_cell_endpoint_projector_nondemolition = false
one_cell_write_recurrence_period_equals_2_tau_R = true
finite_closed_BID_parent_establishes_durability = false
causal_direct_limit_or_superselection_completion_required = true
complete_parent_action_derived = false
alpha_computed = false
proof_authorized = false
```
