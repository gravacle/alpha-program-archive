# R3.4 Shared-Source Causal Parent Specification v001

Date: 2026-07-24

## Purpose

Construct and adjudicate the causal completion of the currently frozen
primitive source-record incidence sector using:

```text
one global source carrier;
overlapping source-incidence projectors;
distinct even record factors;
finite one-use causal-cell support;
and the first-opening incidence interval.
```

This gate does not call that sector the complete `Q_spec`. Gauge, gravity,
environmental descendants, the physical in-state, and the nontrivial
outgoing tail remain separate obligations.

## Hash-pinned inputs

```text
CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
  b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30

PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
  532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb

BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md
  949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd

scripts/audit_bid_global_boundary_descent_quasi_free_v001.py
  f19892d5b87149f0627e17a118021670a1e54ab4c003f76641c364154b326097

BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md
  b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f

scripts/audit_bid_unique_charged_controlled_coupling_v001.py
  c0ee054d73e93cdcf3f909f65a989dff4a1377e892f71d5e657441640c48db58

BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
  7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476

scripts/audit_bid_first_opening_interval_v001.py
  c5de96772a85f128df0a51a68d364a61c73b8c94c7e8e13e26b95964048651d5
```

These hashes bind the exact upstream lineage. They do not promote an
upstream conditional result.

## Frozen finite parent

For a chain of `N` causal cells with vertices `v_0,...,v_N`, derive

```text
d_j=e_(j+1)-e_j;
P_j=|d_j><d_j|/<d_j,d_j>;
B_j=P_j tensor gamma^5 tensor c_partial,j.
```

There is one source orbital carrier and one spin carrier. The source is not
copied per record cell. Each `c_partial,j` acts on its own

```text
R_j=span{|r_j>,|p_j>,|e_j>}.
```

For an admissible pulse profile `v_j(t)`,

```text
support(v_j) is contained in Omega_j;
integral v_j(t) dt=tau_R=pi/sqrt(2).
```

The causal parent is

```text
H_N(t)=sum_j v_j(t) B_j
```

with event order inherited from the causal chain. No stationary reuse of a
completed `B_j` is admitted.

## Required calculations

1. Derive the source projectors from the chain incidence matrix. Verify:

   ```text
   Tr(P_j P_(j+1))=1/4;
   [B_j,B_(j+1)] != 0;
   [B_j,B_k]=0 for |j-k|>1.
   ```

2. Verify that each isolated pulse depends only on its integrated action and
   gives the already derived first-opening endpoint.
3. Show that adjacent-cell order is physically load-bearing and fixed by
   causal order, while spacelike/disjoint cells commute.
4. Prove for every earlier record observable `O_j` and every later primitive
   cell `k>j`:

   ```text
   [B_k,O_j]=0.
   ```

   This must hold even though the source projectors overlap.
5. Starting from a disclosed charge/source in-sector and ready records,
   compute the causal output. Later cells must leave the reduced state of all
   earlier record factors invariant.
6. For the finite causal products

   ```text
   W_N=U_(N-1)...U_1 U_0,
   ```

   test the local Heisenberg limit

   ```text
   Omega_+(A)=lim_N W_N^* A W_N.
   ```

   The limit must stabilize exactly on every local observable after a finite
   causal buffer. If the inverse limit fails or is not shown, report an
   outgoing endomorphism rather than an automorphism or same-Hilbert unitary.
7. Test finite-state restriction on the public record algebra and separately
   report whether a parent-selected source-inclusive state has been obtained.
8. Retain the stationary-reuse recurrence as a mandatory negative control.

## Pass boundary

The strongest admissible positive result is:

```text
the primitive shared-source causal parent derives an outgoing public-record
endomorphism and exact primitive pointer persistence.
```

It may not be promoted to complete physical durability unless all generated
descendants of the same complete parent are included and preserve the public
sector.

## Verdicts

```text
SHARED_SOURCE_CAUSAL_PARENT_PUBLIC_MOLLER_DERIVED
SHARED_SOURCE_CAUSAL_PARENT_CONDITIONAL
SHARED_SOURCE_CAUSAL_PARENT_BLOCKED
```

## Fixed statuses

```text
complete_parameter_free_Q_spec_frozen = false
parent_selected_physical_in_state_derived = false
generated_descendant_durability_closed = false
complete_physical_durability_derived = false
nontrivial_outgoing_tail_generator_derived = false
complete_write_plus_tail_spectrum_derived = false
physical_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
