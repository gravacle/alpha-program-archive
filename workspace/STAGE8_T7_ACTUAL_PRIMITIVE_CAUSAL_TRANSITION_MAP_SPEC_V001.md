# Stage-8 T7 Actual Primitive Causal Transition-Map Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This target-free gate attempts the one remaining derivable object identified
by the primitive scalarization dichotomy: the connected completed-record
transition map of the actual finite Lorentzian primitive parent.

It uses the one-source sector of the already-adopted global boundary descent.
It uses no source state, Fock expectation, CAR determinant, normalized trace,
final source ray selected after evolution, response value, or new principle.

## Hash-pinned authorities

```text
949181d78aca143ebef06eacc4ab1018d43cdf79962ee8c78c350f654a7555dd  BID_GLOBAL_BOUNDARY_DESCENT_QUASI_FREE_COMPLETENESS_V001.md
b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
b786db3adec8cc335967d49ec13b59923d67f424644f72c535b27b579dd1489f  BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md
7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476  BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
52187f8174b203d3cf2acb641d800f45ae733331cc0f3d56658898ed7daec244  BID_BOUNDARY_METRIC_TRANSPORT_DERIVATION_V001.md
5096f4cc2421574badf392cad591787e12928d27335683b5c77d0d98cd8e5918  STAGE8_T7_CAUSAL_LINE_CONNECTION_RETURN_LIFT_RESULT_V001.md
52401eefc3ff84e22f04bbc329a619b830058661db7f969d2d43d167d97d893d  STAGE8_T7_RELAYED_FAMILY_RESOLUTION_RESULT_V001.md
df2f478b936df96bd9e5cc4cf980231a88859f098528e4ca3923a3add27345da  STAGE8_T7_PRIMITIVE_CONNECTED_SCALARIZATION_DICHOTOMY_RESULT_V001.md
9410ee80ff89beed4e133f75fcdb952d059f3386df12069793b5d60895d15486  STAGE8_T7_CRITICAL_PATH_SCOPE_CORRECTION_V001.md
```

Any mismatch aborts execution.

## P1 - Actual primitive one-source parent

For a causally ordered chain of primitive cells, let:

```text
u_j = normalized oriented incidence vector;
P_j = |u_j><u_j|;
B_j = P_j tensor gamma^5 tensor c_j.
```

Each `c_j` acts on its own ready/pointer/intermediate record factor. Causal
Incidence Support gives one-use pulse support with integrated action

```text
tau_R = pi/sqrt(2).
```

The finite parent is the time-ordered product of the actual controlled
unitaries:

```text
W_N = U_(N-1)...U_0,
U_j = exp(-i tau_R B_j).
```

This is the exact primitive one-source restriction of the global parent, not
the source-Fock completion and not a substituted projector chain.

## P2 - Endpoint compression theorem

The exact local record unitary at `tau_R` must be derived from the sealed
first-opening polynomial. For both eigenvalues of `gamma^5`, prove:

```text
exp(-i tau_R (plus_or_minus c_j)) |r_j> = |p_j>.
```

Using the projector functional calculus:

```text
U_j
 =(I-P_j) tensor I
  +P_j tensor exp(-i tau_R gamma^5 tensor c_j),
```

prove that the completed-record endpoint compression is:

```text
E_j
 =(I_source,spin tensor <p_j|) U_j
  (I_source,spin tensor |r_j>)
 =P_j tensor I_spin.
```

Therefore compression of the actual causal parent onto all predeclared
completed record labels gives:

```text
T_N
 =E_(N-1)...E_0
 =(P_(N-1)...P_0) tensor I_spin.
```

The projector product is an output of the actual endpoint compression. It
may not be inserted as a replacement for `W_N`.

## P3 - Output-range and return theorem

For the rank-one incidence chain, prove:

```text
P_(N-1)...P_0
 =c_N |u_(N-1)><u_0|,
c_N=product_(j=1)^(N-1) <u_j,u_(j-1)>.
```

The range of `T_N` is consequently fixed by the transition itself:

```text
im(T_N) is contained in L_(N-1) tensor S_Dirac.
```

It is not a final source line selected after seeing a response.

Use only the already-derived oriented metric-compatible source connection:

```text
V_N:L_0->L_(N-1).
```

The returned transition on the initial source-spin fiber must be:

```text
(V_N^dagger tensor I_spin) T_N
 =a_N I_(L_0 tensor S_Dirac).
```

At the flat chain baseline:

```text
<u_j,u_(j-1)>=-1/2,
a_N(0)=(-1/2)^(N-1).
```

Every finite baseline must be nonzero and `N=1` must reduce to the pinned
one-handle amplitude.

## P4 - Connectedness and competitor scope

Adjacent `P_j` do not commute and the scalar contains their incidence
overlaps. This is a connected causal transition, not a tensor product of
disjoint one-cell amplitudes.

The `B_lambda` record-only counterfamily remains a valid mathematical
counterfamily to one-cell data alone. It is excluded from the declared
primitive parent only by the already-adopted Global Boundary Descent and
Quasi-Free Completeness Principle, which forbids an independent primitive
record-only/contact kernel. This exclusion must be labeled premise-based,
not theorem-based. Generated descendants remain downstream.

## Verdicts

`ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_DERIVED` requires P1-P4, an exact
arbitrary-finite-`N` formula, nonzero baselines, and an independent
reconstruction.

`ACTUAL_PRIMITIVE_CAUSAL_TRANSITION_MAP_BLOCKED` is mandatory if endpoint
compression does not yield `P_j tensor I_spin`, its range is not the final
incidence line, the return is not scalar on the full spin fiber, or a source
state/trace/final ray is required.

Passing this gate derives only the finite connected scalar amplitude. It does
not prove a volume-uniform zero-free neighborhood, linked-cluster density,
or Duhamel/intensive-Hessian equality.

## No-target attestation and fixed status

```text
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
Duhamel_intensive_Hessian_equality_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
