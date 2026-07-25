# Stage-8 T7 Actual-Parent Record-Amplitude Adjudication Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This gate asks whether the already-declared finite Lorentzian
source-record parent and its already-disclosed incoming state determine the
scalar complex completed-record amplitude required by T7. It introduces no
final source line, source trace, response coefficient, coupling target, or
new preparation principle.

The ideal incidence-projector chain has been sealed as a conditional
identity only. It is forbidden as a substitute for the finite parent in
this gate.

## Hash-pinned authorities

```text
5026afb89b52ead9f309168cb2fa4f06b81039f8dd01b8940f40e64aad679a7e  STAGE7_QSPEC_REVIEW_CANDIDATE_V002.md
532b0f0eac4ac749ba3e24954db356f7ca0f98c4f730030075c463efa3158efb  PARENT_STATE_COVARIANCE_PRINCIPLE_V001.md
40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
345d447eaf6d730caa6fa655b92a7b0cd93a68b5f86e0c8929cf969f40aeb7cb  R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md
6f6b822ac8ccf9ea19659f4ccf811268f60a27a361f817ee6513479d63b62546  BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
6e01e5bac60b0f9efdb6f964e2b2ea7727ca46e4cfd66153e8ef70baf240a6eb  BID_PUBLIC_RECORD_TRANSITION_AMPLITUDE_DERIVATION_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
21b782b50e9b0ddf1785727ff625a2b933d370aaf539c9fea74982025279b729  STAGE8_T7_RELAYED_CONNECTED_PREPARATION_RETEST_RESULT_V001.md
5096f4cc2421574badf392cad591787e12928d27335683b5c77d0d98cd8e5918  STAGE8_T7_CAUSAL_LINE_CONNECTION_RETURN_LIFT_RESULT_V001.md
9be712d5728a6c2f78671fec4a53d3f026327c56c28b736369e3b6d05800b298  stage8_execution/t7_causal_line_connection_return_lift/T07_CAUSAL_LINE_CONNECTION_RETURN_LIFT_V001.seal.sha256
```

## A1 - Actual finite parent

Use the finite Galerkin compression of

```text
h_K(t)
 =h_0[g,A]
  +sum_c v_c(t) M_c(t) tensor S_n tensor iota_c(c_c)
```

and its declared number-preserving operator-valued CAR lift

```text
H_K(t)=dGamma_R(h_K(t)).
```

The intrinsic diamond envelope, opening interval, cell masks, source
kinetic operator, spin incidence operator, record quadrature, causal order,
and ready record boundary are imported unchanged from the sealed complete
parent. The ideal product `P_(N-1)...P_0` is prohibited.

## A2 - Completed-record Kraus operator

For each declared completed public-record alternative `h`, let `E_h` be its
canonical record effect and `i_r` the ready-record injection. Compress the
actual finite propagator:

```text
M_h(A)
 =(I_source tensor <h|) U_K(A) i_r.
```

If the completed alternative is a higher-rank public effect rather than a
line, retain every Kraus component. Do not choose a source endpoint,
post-select a final source ray, or replace the complex amplitude by the
inclusive probability.

## A3 - Existing-state scalar functional

The only admissible scalarization is the state already attached to the
declared parent:

```text
a_h(A)=omega_K(M_h(A)).
```

The execution must distinguish:

```text
the disclosed stationary quasifree source state;
declared finite-energy charged incoming excitations as boundary data;
the neutral sector;
and an after-the-fact source trace or fitted final ray, both forbidden.
```

If the disclosed state is not defined on the same finite regulator, if a
new zero-mode filling convention is needed, or if more than one admissible
scalar functional survives, this gate is blocked.

## A4 - No Gaussian shortcut without proof

The familiar finite-dimensional quasifree identity

```text
omega_C(Gamma(k))=det(I-C+Ck)
```

may be used only after proving that the completed-record Kraus operator is
the second quantization `Gamma(k_h)` of one one-particle contraction.

Because projection on a record outcome can produce a sum of Gaussian
operators, the execution must compare any proposed determinant shortcut
against a direct finite-Fock calculation. A mismatch blocks the shortcut
and the direct finite-Fock value remains the only admissible finite result.

## A5 - Reduction, sectors, and normalization

The gate must:

1. recover the pinned one-handle completed-record amplitude on its declared
   charged root line;
2. report the neutral-sector completed-record amplitude rather than
   condition it away;
3. report every finite baseline used in normalization;
4. prove or refute that the declared branch baseline is nonzero without
   choosing a final source state; and
5. keep state dependence visible.

Define

```text
Z_h(A)=a_h(A)/a_h(0)
```

only where `a_h(0)` is derived nonzero.

## A6 - Verdicts

```text
FINITE_ACTUAL_PARENT_RECORD_AMPLITUDE_DERIVED
```

requires A1-A5, including a unique existing-state scalarization, exact
one-handle reduction, and nonzero declared-branch baseline.

```text
ACTUAL_PARENT_RECORD_AMPLITUDE_BLOCKED
```

is mandatory if the finite parent leaves an unresolved source operator, the
state is not defined on the same regulator, a new preparation is required,
the Gaussian shortcut fails without a direct replacement, or the baseline
vanishes.

Passing this finite adjudication would not prove a volume-uniform zero-free
neighborhood, linked-cluster density, source-inclusive thermodynamic limit,
or Duhamel/Hessian interchange.

## Fixed status

```text
finite_actual_parent_record_amplitude_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
