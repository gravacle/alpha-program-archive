# Complete-Qspec Relative-History Transfer-Map Repair Specification v001

Date: 2026-07-25

## Purpose

Repair the three defects found by the first hostile review of the v001
relative-history transfer artifact:

1. the induction required by T2 was named but not supplied as a frozen proof;
2. the claimed scope did not distinguish strictly sequential completed records
   from concurrently open record incidences;
3. the physical scalar regression was too symmetric to detect reversed cell
   order.

This attachment is append-only. It does not alter the v001 specification or
its execution artifact. A repaired result may supersede their verdict only
after every gate below passes.

No response value, coupling target, alpha value, or measured constant may
enter.

## R1 - Exact sequential theorem

The admissible history has one shared source and fresh record factors
`R_1,...,R_N`. At the boundary between stages `c-1` and `c`:

```text
all R_1,...,R_(c-1) are closed;
U_c acts only on the source and fresh R_c;
U_c acts as identity on every closed record factor;
R_c begins in its declared ready state.
```

The execution must freeze an explicit induction proving:

```text
X_0 = rho_source,in
X_c = Tr_Rc [
        U_c^+ (X_(c-1) tensor |r_c><r_c|) U_c^- dagger
      ]
Z_N = Tr_S X_N.
```

The proof must state its base case, induction hypothesis, tensor ordering,
partial-trace commutation step, and conclusion. A string naming "induction"
is not sufficient.

## R2 - Concurrent-cell ceiling

The one-record map is not claimed during an interval in which two or more
record incidences remain open or a later stage acts on an earlier open
record. Such an interval requires a block transfer map retaining every open
record factor in the propagated state:

```text
X_c on H_source tensor H_open_records.
```

The current theorem closes only the strictly sequential completed-record
schedule. This is a scope boundary, not an approximation.

## R3 - Order-sensitive physical regression

On the existing two-cell finite parent:

1. retain the original source-ray scalar and diagonal normalization checks;
2. choose two deterministic nonsymmetric source vectors `|a>` and `|b>`;
3. set `X_0=|a><b|`;
4. compute the final source cross-operator in the full `70 x 9` evolution by
   tracing both record factors;
5. compute the same operator by the ordered map `T_2 o T_1`;
6. require relative Frobenius disagreement below `1e-10`;
7. reverse only the transfer-map order and require relative Frobenius
   disagreement above `1e-6`.

The reversed-order condition is a mandatory negative control. The chosen
probe vectors and threshold are frozen before executing the repair.

## R4 - Independent generic regression

An independent verifier must:

```text
use generic random unitaries rather than the Qspec Hamiltonian;
use different source and bra vectors;
compare the full reduced cross-operator, not only its scalar trace;
use at least three sequential cells;
confirm the ordered composition below 1e-12;
confirm reversed ordering changes the operator above 1e-6.
```

## Verdict

Return:

```text
COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_DERIVED
```

only if R1-R4 pass. Otherwise return:

```text
COMPLETE_QSPEC_SEQUENTIAL_RELATIVE_HISTORY_TRANSFER_MAP_BLOCKED
```

## Scope ceiling

A pass proves the exact source-space representation for a strictly
sequential fresh-record schedule at completed-stage boundaries. It does not
prove a one-record representation for overlapping open incidences. It also
does not prove:

```text
a volume-uniform zero-free neighborhood;
linked-cluster summability;
an intensive thermodynamic limit;
low-frequency locality;
the Maxwell tensor;
kappa_record;
the Thomson limit;
alpha;
or proof authorization.
```

## Fixed status

```text
complete_Qspec_CTP_scalar_closure_derived = true
sequential_relative_history_transfer_map_derived = false
concurrent_open_record_block_map_derived = false
connected_K_cell_amplitude_constructed = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
local_Maxwell_response_derived = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
