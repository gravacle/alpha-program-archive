# Stage-8 Route-2 CAR-State Bridge Scope Correction v001

## Status

Append-only correction to:

```text
STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md
STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md
```

The prior files remain sealed and unchanged. This correction narrows their
operator-to-state claim before any zero-free, cluster, Hessian, coupling,
or alpha computation.

## Corrected type statement

The executed primitive operator response is on the finite three-site
one-source regression carrier:

```text
H_S,3site = C^3 tensor C^4,
R_all,3site^(1) in End(H_S,3site).
```

It is not an operator on the continuum one-particle carrier `K_Sigma`, nor
on the inherited regulated carrier `Q_n K_Sigma`. The latter requires a new
same-carrier construction:

```text
R_all,n^(1) in End(Q_n K_Sigma).
```

The disclosed incoming state is quasifree on the full source CAR algebra.
It is not, without a derived bridge, a state acting directly on an
arbitrary one-source matrix. The expressions

```text
omega(dGamma(R_all^(1)));
omega(Gamma(R_all^(1)));
Tr(C R_all^(1));
```

are different constructions and may not be selected or normalized after
comparison.

Therefore the prior notation

```text
omega_source(R_all)
```

is retained only as abstract complete-algebra notation. It is not an
executed actual-parent equality for the sealed one-source regression.

The abstract complete-`Q_spec` identity

```text
Z_K[A_+,A_-]
 =omega_in(W_K[A_-]^dagger W_K[A_+])
```

remains valid once `W_K` and `omega_in` are defined on the same complete
CAR-record algebra.

## Existing repair authorities

| Role | Path | SHA-256 |
|---|---|---|
| State-regulator restriction | `STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md` | `3a6ff6173573a7d9dd99bdd1a6bb7eaa02c433ab50bc769e144d94c983b4f0ff` |
| Finite-Fock completed-record baseline | `STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md` | `907a274ab3a43766f8ed0250561284952dd1cd6fb3adb68330a97286dc2423f6` |
| Three-site one-source operator regression | `STAGE8_T7_PRIMITIVE_OPERATOR_RESPONSE_RESULT_V001.md` | `76f5505e3aa1fdc11102f782ed8ee40e49787bb38e3a2524e17b92fd8de46740` |
| Sealed state binding being narrowed | `STAGE8_ROUTE2_COMPLETE_QSPEC_STATE_BINDING_V001.md` | `5cbcd28ee493ba43e3d36158d80c4202230f056808caf2b36420f08c38fbd0d7` |
| Sealed architecture amendment being narrowed | `STAGE8_T7_OPERATOR_VALUED_PRIMITIVE_RESPONSE_ARCHITECTURE_AMENDMENT_V001.md` | `8a7f52ffa2500d20ad834b11e3762ed114ee1a201f2fec18bcb119e3c7ead860` |

The state-regulator result requires inherited nonzero-mode restrictions

```text
C_n=Q_n C Q_n
```

and forbids treating the three-site periodic operator fixture as a
complete state regulator. No zero-mode occupation is added.

The finite-Fock baseline already constructs the CAR lift on eight inherited
nonzero one-particle modes, fills the four negative-energy modes, and
agrees across independent occupation-basis implementations. It establishes
that the repair is executable, but it computes a completed-record
amplitude rather than the exhaustive relative-history state functional.

## Required next gate

The Actual-Parent CAR Lift and State-Evaluation Gate must:

1. use the inherited nonzero-mode carrier and state, without a new
   zero-mode prescription;
2. rebuild the same finite source-record parent on that carrier;
3. construct `H_(K,n)=dGamma_R(h_(K,n))` and its full Fock-record
   propagator;
4. construct and seal the new one-source response
   `R_all,n^(1) in End(Q_n K_Sigma)` on that same carrier;
5. form the exhaustive relative-history operator
   `R_all^(CAR)=I_r^dagger W_-^dagger W_+ I_r`;
6. prove its one-source-sector restriction reproduces the new
   same-gate response `R_all,n^(1)`;
7. retain `R_all,3site^(1)` only as a separate structural and
   implementation regression unless an explicit carrier intertwiner is
   independently derived;
8. evaluate
   `Z_(K,n)=omega_(C_n)(R_all^(CAR))` directly and independently; and
9. prohibit a determinant shortcut unless the relevant complete operator
   is first proved to be the corresponding second-quantized Gaussian
   operator.

Only after this gate passes may the finite zero-free-neighborhood gate
begin.

## Corrected status

```text
finite_primitive_operator_response_bundle_derived = true
finite_primitive_operator_Duhamel_tangent_derived = true
abstract_complete_Qspec_CTP_scalar_closure_derived = true
complete_Qspec_state_hash_pinned_for_route2 = true
actual_finite_parent_CAR_response_lift_derived = false
actual_finite_parent_state_evaluation_derived = false
actual_finite_parent_operator_to_scalar_bridge_derived = false
primitive_source_scalarization_derived = false
stage8_route2_architecture_amended = true
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
ER_fork_closed = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
