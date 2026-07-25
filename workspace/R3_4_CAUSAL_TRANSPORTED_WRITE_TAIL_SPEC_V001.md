# R3.4 Causal-Transported Write/Tail Specification v001

Date: 2026-07-24

## Purpose

Determine whether causal covariance uniquely joins the derived primitive
shared-source write parent to the derived free incidence tail without
changing either normalization or selecting a coupling.

An exploratory pre-seal diagnostic found that the naive static sum

```text
H_static=H_0+B
```

does not preserve the isolated first-opening endpoint. This formal gate is
therefore a result-aware consistency adjudication, not a blind prediction.
The static sum remains a mandatory negative control.

## Hash-pinned inputs

```text
R3_4_SHARED_SOURCE_CAUSAL_PARENT_RESULT_V001.md
  781608f2fe4c8753a0c06b1d87407b2a6c88caa0ab45329e1200160e56292a24

results/r3_4_shared_source_causal_parent_v001.json
  4f5beba98c55a7ee032664265f2af0e213fc2cd3201b76a701eb8a1cf0f4db48

R3_4_INCIDENCE_CONTINUUM_SCALING_SPEC_V001.md
  e25cc20a95a0b6318389348ceacac93eccd2aebb0720350f08131d9e988cb6d3

R3_4_INCIDENCE_CONTINUUM_SCALING_RESULT_V001.md
  3f18b011ef11cdde3b7c83a7bc7cc90a2cdfd82c64edf92b3b2e57b6254b520d

results/r3_4_incidence_continuum_scaling_v001.json
  1633a5f727be8a3d084c8ed12517ea279c7197dea0ae7c0589b9ce3e76330cfd

scripts/audit_r3_4_incidence_continuum_scaling_v001.py
  01315cfb7bcd11d1852dfd1621f3bcf82d5595ff4a1fdc356c72e5f6a4a69ecf

scripts/verify_r3_4_incidence_continuum_scaling_v001.py
  bc61b84b06ae976c228db39b5a6c5f3d1ffbae711fda3bd427eac7952c844025
```

## Covariance selector

Let

```text
U_0(t)=exp(-i H_0 t)
```

be the free incidence evolution. Separate a cell envelope `v_c(t)` from its
unit-normalized reference incidence operator `B_c`. Require the operator
part of the interaction to be transported with the same parent:

```text
tilde B_c(t+s)=U_0(s) tilde B_c(t) U_0(s)^*;
tilde B_c(0)=B_c.
```

The group law then has the unique solution

```text
tilde B_c(t)=U_0(t) B_c U_0(t)^*.
```

Thus the candidate complete primitive write-plus-tail parent is

```text
H(t)
 =H_0
  +sum_c v_c(t) U_0(t) B_c U_0(t)^*.
```

In the interaction picture,

```text
H_I(t)=sum_c v_c(t) B_c.
```

No relative coefficient is introduced.

## Required calculations

1. Prove uniqueness of the transported operator from the covariance
   functional equation and the initial condition.
2. Show that the static competitor violates covariance whenever
   `[H_0,B_c]` is nonzero.
3. On a finite incidence-chain regulator, construct `H_0` and `B_c` from the
   pinned inputs and reproduce the static-sum endpoint failure.
4. For several pulse profiles with the same integrated action, verify:

   ```text
   U(T,0)=U_0(T) exp[-i B_c integral v_c(t)dt].
   ```

   Confirm this independently by direct time slicing.
5. Verify that the first-opening record endpoint is restored by the
   transported parent without changing `tau_R`.
6. For multiple shared-source cells, prove that the interaction-picture
   causal product is exactly the already derived ordered product. Earlier
   public record persistence and the outgoing local endomorphism must
   therefore survive attachment of the tail.
7. Derive the finite-support Moller operator relative to `H_0`.
8. Report the remaining root-state, form-domain, physical in-state, and
   generated-descendant obligations without promoting them.

## Verdicts

```text
CAUSAL_TRANSPORT_UNIQUELY_JOINS_PRIMITIVE_WRITE_AND_FREE_TAIL
CAUSAL_TRANSPORT_CONDITIONAL
CAUSAL_TRANSPORT_BLOCKED
```

## Fixed statuses

```text
physical_in_state_selected = false
finite_energy_physical_root_derived = false
generated_descendant_durability_closed = false
complete_physical_durability_derived = false
complete_write_plus_tail_root_measure_derived = false
complete_parameter_free_Q_spec_frozen = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
