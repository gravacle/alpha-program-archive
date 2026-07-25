# Complete-Qspec Relative-History Transfer-Map Specification v001

Date: 2026-07-25

## Purpose

Derive an exact source-space transfer representation of the connected
many-record relative-history CTP amplitude. This is the scalable construction
needed before zero-free, linked-cluster, and thermodynamic-response questions
can be asked.

No response value, coupling target, alpha value, or measured constant may
enter.

## Frozen authorities

```text
273e1473a1a8bf0be0467634411cec1b7daeee0c9f24c330fad5d288d191dcbb  COMPLETE_QSPEC_RELATIVE_HISTORY_CTP_AMPLITUDE_RESULT_V001.md
082a56a6cac2be75322209626a6086901cad7b5e9900cf1d1d021e99b46b7b0c  COMPLETE_QSPEC_TEMPORAL_PLAQUETTE_RESPONSE_RESULT_V001.md
907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6  STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
```

## T1 - Per-cell cross-history map

Let one causally ordered cell act on the shared source Hilbert space
`H_S` and one fresh record factor `H_R,c`. Let the record enter in the
declared ready state `|r_c>`, and let:

```text
U_c^+ = U_c[A_+]
U_c^- = U_c[A_-].
```

For a source cross-density `X`, define:

```text
T_c^(+,-)(X)
 = Tr_R [
     U_c^+
     (X tensor |r_c><r_c|)
     U_c^- dagger
   ].
```

For any orthonormal record basis `|q>`, define:

```text
K_(c,q)^+ = <q|U_c^+|r_c>
K_(c,q)^- = <q|U_c^-|r_c>.
```

Then:

```text
T_c^(+,-)(X)
 = sum_q K_(c,q)^+ X K_(c,q)^- dagger.
```

This is a cross-history linear map. On the diagonal `A_+=A_-`, it is the
ordinary completely positive trace-preserving reduced source channel.

## T2 - Exact connected composition theorem

For `N` causally ordered cells with:

```text
one shared source;
one fresh ready record per cell;
no later interaction with an already closed record;
complete final identity on source and every record;
```

define:

```text
X_0 = rho_source,in;
X_c = T_c^(+,-)(X_(c-1));
Z_N[A_+,A_-] = Tr_S X_N.
```

The execution must prove by induction that:

```text
Z_N[A_+,A_-]
 = Tr [
     W_N[A_+]
     (rho_source,in tensor |r_1...r_N><r_1...r_N|)
     W_N[A_-] dagger
   ].
```

No final source ray, record outcome, normalized source trace, determinant, or
inclusive completed-record probability is inserted. The final source trace
is exactly the complete final identity already present in the relative-
history CTP functional.

## T3 - Finite physical equality check

On the existing two-cell finite parent:

1. build each cell's three Kraus operators directly from its discretized
   source-record unitary;
2. verify `sum_q K_q dagger K_q=I` for each diagonal branch;
3. evaluate the two-cell overlap once in the full `70 x 9` source-record
   state space;
4. evaluate it again by composing the two source-space cross-history maps;
5. require agreement below `1e-10`;
6. require diagonal normalization `Z_2[A,A]=1` below `1e-10`.

This numerical check verifies the implementation of the theorem. The theorem
itself is the finite-dimensional partial-trace identity and does not depend
on the chosen test angle.

## Verdict

Return:

```text
COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_DERIVED
```

only if T1-T3 pass. Otherwise return:

```text
COMPLETE_QSPEC_RELATIVE_HISTORY_TRANSFER_MAP_BLOCKED
```

## Scope ceiling

A pass supplies an exact scalable representation of the connected amplitude.
It does not prove:

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
relative_history_transfer_map_derived = false
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
