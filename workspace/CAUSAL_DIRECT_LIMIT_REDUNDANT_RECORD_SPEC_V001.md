# Causal Direct-Limit Redundant-Record Specification v001

Date: 2026-07-24

Frozen before execution. This specification uses the already adopted
Primitive Reversible Record-Write Principle; it adds no interaction
coefficient and evaluates no coupling.

## Inputs and their status

For each pointer label `h in {0,1}`:

```text
P_h=|h><h|;
each future record cell begins in |0>;
U_e=P_0 tensor I + P_1 tensor X
```

on a causally oriented write edge `e`. `U_e` is the previously adopted
nondemolition controlled endpoint swap. Its interaction window closes after
the write, and later admissible interactions preserve the written pointer
projectors.

The causal architecture is any locally finite future-directed acyclic
complex with an unbounded sequence of ready cells. Gates sharing no
causal support commute. Gates with causal dependence are applied in the
causal order. No branching number is selected.

## Sealed predictions

1. Starting from label `h` and `N` ready descendants, repeated causal writes
   produce

   ```text
   |h>_source tensor |h>^tensor_N.
   ```

2. Conditional environment states for `h=0,1` are orthogonal for every
   `N>=1`.
3. Tracing an unobserved copied cell removes the off-diagonal source
   coherence exactly in the ideal pointer branch.
4. Every copied cell independently reveals the same pointer label.
5. For an imperfect one-cell conditional overlap `|gamma|<1`, the
   `N`-cell overlap is `|gamma|^N` and the squared overlap is
   `|gamma|^(2N)`.
6. The macroscopic pointer average

   ```text
   M_N=(1/N) sum_(j=1)^N Z_j
   ```

   is a central sequence: for every observable `O` supported on at most `m`
   cells,

   ```text
   ||[M_N,O]|| <= 2m ||O||/N.
   ```

7. Distinct pointer labels define distinct asymptotic sectors through the
   limits of `M_N`.
8. Different linear extensions of the same causal partial order give the
   same unitary whenever they differ only by swaps of spacelike-disjoint
   gates.

## Failure and scope

The gate fails if the adopted write does not copy the pointer basis, if the
record labels are not recoverable, or if the central-sequence bound fails.

A pass does not derive:

```text
the physical causal-complex refinement;
the ready-state/low-entropy boundary condition;
the interaction-window rule, which is inherited as adopted;
the covariant spectral measure;
the gauge-dressed source spectrum;
or an electromagnetic response.
```

The result may close only the outgoing-record-recoverability component of
Fork 8. It cannot promote the entire hypothesis while the spectral measure
remains free.

```text
target_values_used = false
coupling_evaluated = false
alpha_computed = false
```
