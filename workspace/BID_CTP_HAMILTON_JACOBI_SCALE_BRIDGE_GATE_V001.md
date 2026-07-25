# BID CTP Hamilton-Jacobi Scale-Bridge Gate v001

Date: 2026-07-24

## Question

Does the active Gravacle authority derive the physical identity

```text
Delta S_record = E_R T_R
```

needed by the conditional causal-cell calculation, with `E_R` the same
energy that enters the gravitational recoverability condition?

## What Hamilton-Jacobi theory actually gives

For a completely specified Lorentzian CTP action, state, boundary
conditions, and time-flow vector, the on-shell action obeys a boundary
Hamilton-Jacobi relation of the form

```text
d Delta S_CTP / dT = -Delta E_HJ(T).
```

Consequently,

```text
Delta S_CTP(T_R)-Delta S_CTP(0)
  = -integral_0^T_R Delta E_HJ(T) dT.
```

The product form `|Delta S_record|=E_R T_R` follows only after the same
microscopic theory proves all of the following:

1. the relevant Hamilton-Jacobi energy is constant on the stationary
   record trajectory;
2. the CTP branch-energy difference equals the complete gravitating cell
   energy after one fixed reference subtraction;
3. no spectator, vacuum, binding, edge, or environment energy contributes
   to compactness without also entering the record action difference;
4. the time parameter conjugate to that energy is the tip-to-tip proper
   interval `T_R`; and
5. the energy is the one used by the chosen gravitational closure
   condition.

The relative action marker `|Delta S_record|=pi hbar` establishes none of
these identifications by itself.

## Explicit energy ambiguity

In a spherical Schwarzschild exterior, define

```text
C = 2 G E_MS / (c^4 R),  0 <= C <= 1,
```

where `E_MS` is the Misner-Sharp energy. The reference-subtracted
Brown-York energy on a round timelike boundary of areal radius `R` is

```text
E_BY
  = (c^4 R/G) [1-sqrt(1-C)]
  = E_MS * 2/[1+sqrt(1-C)].
```

Thus:

```text
E_BY/E_MS -> 1  as C -> 0,
E_BY/E_MS = 2   at C = 1.
```

These are both standard, geometrically meaningful energies, but they are
conjugate to different boundary/time choices. The present causal diamond is
declared to be the support of a CTP history difference, not a material
timelike boundary. Therefore neither finite-boundary Brown-York energy nor
asymptotic ADM/Misner-Sharp energy is automatically the Hamiltonian conjugate
to the local tip-to-tip proper interval.

At the presently adopted marginal spherical selector

```text
C=1,
R=c T_R/2,
|Delta S_record|=s hbar,
```

the two choices give different exact roots:

```text
E_MS T_R=s hbar  -> T_R=2 sqrt(s) t_P,
E_BY T_R=s hbar  -> T_R=sqrt(2s) t_P.
```

For `s=pi`, these are respectively

```text
T_R=2 sqrt(pi) t_P,
T_R=sqrt(2pi) t_P.
```

The ratio is `sqrt(2)`. The existing `2 sqrt(pi) t_P` result therefore
cannot be promoted by Hamilton-Jacobi language alone.

## Causal-diamond action does not select the missing normalization

Treating the null edge of the history-support diamond as an auxiliary
gravitational subregion does not repair the ambiguity. For a flat spherical
diamond of waist area `A=4 pi R^2`, affinely normalized null generators with
arbitrary positive normalizations `alpha_n` and `beta_n` give a joint term of
the form

```text
I_L,bare
  = epsilon (A c^3/8 pi G)
    [log(alpha_n beta_n)+a_0].
```

The null-normal product and the allowed fixed joint scalar `a_0` are not
selected by the Lorentzian variational principle. Equating this action to the
record marker gives

```text
R^2 = 2 pi l_P^2/eta,
eta = epsilon [log(alpha_n beta_n)+a_0],
```

so every positive radius can be obtained by a normalization choice.

The standard reparametrization-restoring null counterterm removes the
generator normalization but introduces an arbitrary length `ell_ct`. With
intrinsic boundary additions suppressed, the marker equation becomes

```text
R^2 [1+2 log(2 ell_ct/R)] = 2 pi l_P^2.
```

Depending on `ell_ct`, this equation has zero, one repeated, or two positive
roots. It therefore replaces one freedom with another instead of selecting a
record cell. Additional intrinsic null-boundary functionals enlarge the
family.

Other prescriptions do not agree on a unique coefficient: the point-tip
Lorentzian imaginary action vanishes, while Euclidean puncture and
replica/monodromy prescriptions produce different area coefficients. These
are useful thermodynamic constructions, but they do not provide the missing
unique Lorentzian CTP normalization.

This conclusion is also consistent with the active global-domain rule: the
diamond is the support of the CTP history difference, not a reflecting
material boundary. A null-subregion action cannot silently become the
physical record Hamiltonian.

## Reference-energy obstruction

The record phase is insensitive to adding the same constant Hamiltonian to
both CTP branches, while total gravitational compactness is not generally
insensitive to adding physical spectator energy. Therefore the map

```text
record branch-energy difference -> total gravitating energy
```

requires a derived state, reference subtraction, and no-spectator theorem.
It cannot be supplied by a convention chosen after the record phase is
known.

## Exact closure condition

Stage 3 closes only when one target-independent complete source-record-
gravity action:

1. fixes the global/subregion boundary terms and time-flow vector;
2. derives the CTP Hamilton-Jacobi energy;
3. proves that this energy is constant on the first durable-record saddle;
4. proves that it equals the gravitating energy entering the closure
   condition;
5. derives the baseline/reference subtraction and excludes spectator
   energy;
6. derives, rather than assumes, the marginal closure condition; and
7. yields one isolated stable positive `T_R/t_P`.

Until then the causal-cell formulas are exact conditional algebra, not an
absolute scale derivation.

## Status

```text
CTP_Hamilton_Jacobi_identity_available_conditionally = true
complete_CTP_action_and_boundary_data_derived = false
record_energy_constant_on_stationary_cell_derived = false
record_energy_equals_total_gravitating_energy_derived = false
reference_subtraction_and_no_spectator_theorem_derived = false
Misner_Sharp_and_Brown_York_candidates_coincide_at_marginality = false
energy_choice_changes_T_R_by_sqrt_2 = true
bare_null_diamond_action_normalization_unique = false
reparametrized_null_diamond_action_scale_unique = false
causal_diamond_action_selects_absolute_radius = false
absolute_record_interval_derived = false
alpha_computed = false
proof_authorized = false
```
