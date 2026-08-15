# Primitive Record-Cell Selection Principle v002

## Correction to v001

Version 001 was externally sealed before numerical work and is retained as an
audit record. Its explicit rearrangement

```text
K_R = 4 (Phi_* - Gamma_rest,*) / I_F,*
```

is valid only if the selected field configuration and the action partition are
already independent of `K_R`. A coupled matter-electromagnetic-gravitational
saddle need not have that property. Version 002 therefore replaces the direct
division rule with a joint saddle-and-closure selection problem. No numerical
cell or alpha value was evaluated between the two versions.

## Adopted Gravacle principle

A primitive first-record event is one complete Lorentz-covariant physical
saddle. The allow/require transition selects the coupling and the saddle
jointly: the physical coupling is the unique positive value for which the
complete Boundary-Resolved cell first satisfies the durable-record closure
condition.

This is an adopted theory principle. It is not inferred from a measured
coupling, particle mass, cosmological endpoint, retired four-state charge
projector, retired `3/16` seed, or target-aware full-operator lineage.

## Coupling-indexed microscopic problem

Use the compact connection normalization fixed by the primitive faithful U(1)
character: a unit charged line couples through `d+iA`. Put the electromagnetic
normalization only in its kinetic stiffness `K>0`. For complete cell data `X`,
write

```text
Gamma_K[X]
  = (K/4) integral_Omega sqrt(|g|) F_(mu nu) F^(mu nu) d^4x
    + Gamma_record,matter,gravity[X].
```

The second term may depend on `A` and on the other fields in `X`, but it may
not contain a separately adjustable local `F^2` coefficient. If the
microscopic theory generates another such term, it must be combined into the
single displayed `K` before selection.

For each `K`, the complete BR boundary conditions and stationarity equations
select, when it exists,

```text
X_K = [Omega_K, g_K, Delta tau_K, A_K, Psi_K]
```

modulo gauge, public isometry, charge-conjugate orientation, and
Boundary-Resolved equivalence. `Delta tau_K` is varied in the stationary
problem; it is not fixed by units.

## Durable-record selector

The same microscopic theory supplies a public closure operator

```text
D_BR(K; X_K)
```

and its Boundary-Resolved spectral counting function

```text
N_BR(K;k) = Tr_BR 1_[0,k^2](D_BR(K;X_K)^2).
```

The ordinary primitive charged branch opens at `K_*` only when the complete
selector establishes all of the following:

```text
no public charged record below the selected opening;
exactly one first public charged record at the opening;
an isolated next public mode;
stationarity of the complete cell, including Delta tau;
a simple positive root of the closure equation in K;
no second inequivalent positive root or continuous modulus.
```

The precise map from the spectrum to durable-record closure must be derived
from the record theory. The phrases "first record" and "allow/require" are not
numerical equations by themselves.

## Joint determination of the coupling

Let `C_record(K)` be the scalar closure residual derived from the complete
on-shell problem. The strict alpha route is authorized only if

```text
C_record(K_*) = 0,
d C_record / dK at K_* != 0,
K_* > 0,
```

and an exhaustive admitted-family audit finds no other inequivalent positive
root. The microscopic coupling is then

```text
alpha_micro = 1 / (4 pi K_*).
```

This is a joint eigenvalue/boundary-value problem. No field configuration is
chosen because it gives a desired value, and no on-shell field integral is
treated as independent of `K` unless the equations prove it.

## Useful on-shell identity

When the saddle is differentiable and boundary terms vanish under the derived
domain conditions, the envelope theorem gives

```text
d Gamma_K[X_K] / dK
  = (1/4) integral_(Omega_K) sqrt(|g_K|) F_K^2 d^4x.
```

This identity checks the implementation. It does not select `K_*`; the
durable-record closure equation must do that.

## Hard failure rules

The construction blocks if any of the following occurs:

1. the cell interval, geometry, field norm, or source depth is inserted rather
   than obtained from the joint stationarity problem;
2. the closure map is merely declared to equal zero at a convenient value;
3. changing an admitted boundary condition, measure, regulator, or action
   partition changes `K_*` without a theory-derived exclusion;
4. `A` is rescaled after the unit U(1) character is fixed;
5. a measured alpha, endpoint, mass, or same-pass constant selects among
   competing saddles or roots;
6. only existence is shown but the unique positive root is not computed;
7. the microscopic result is called the Thomson coupling before the complete
   threshold and RG matching map is derived.

`primitive_record_cell_principle_adopted=true`.
`joint_cell_and_stiffness_selector_defined=true`.
`joint_cell_and_stiffness_operator_constructed=false`.
`absolute_microscopic_stiffness_computed=false`.
`physical_thomson_alpha_computed=false`.
`alpha_computed=false`.
