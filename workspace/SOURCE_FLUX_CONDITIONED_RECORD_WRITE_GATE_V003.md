# Conditional Source-Flux Record-Holonomy Gate v003

Date: 2026-07-23

## Why v003 exists

Version 001 used a global active-branch sign as if it demonstrated a physical
relative phase. Version 002 corrected that with a coherent zero/one-flux
calculation, but it still overreached:

```text
the coherent flux superposition may be forbidden by charge superselection;
no admissible source phase reference was supplied;
the executable audit did not independently validate its partial trace;
the generic equatorial classification was analytic prose, not computed code.
```

Version 003 separates the analytic classification, executable representative,
and unresolved physical observability. Versions 001 and 002 are not
authority.

## Declared primitive flux sector

On the declared zero-or-one local unit-character source-crossing sector,
inherit

```text
Q_Sigma = integral_Sigma j^mu dSigma_mu,
spec(Q_Sigma)={0,1}.
```

This is a local branch input, not a derivation of every current-flux
spectrum.

For the charged record handle, adopt:

```text
Q_Sigma=0  => no charged-record write;
Q_Sigma=1  => the charged-record channel reaches first orthogonal onset.
```

Other interactions and record handles can still evolve in the zero-flux
branch.

## Analytic holonomy classification

For an affine constant-axis representative on the primitive record factor,

```text
h' = v_x X + v_y Y + v_z Z.
```

The ready-state survival amplitude is

```text
cos(theta)-i(v_z/|v|)sin(theta),
theta=|v| tau_*/hbar.
```

First orthogonal onset gives

```text
theta=pi/2,
v_z=0.
```

Endpoint rephasing rotates the equatorial pair `(v_x,v_y)`. Choosing `Y_R` as
representative, the conditional integrated record-changing holonomy is

```text
K_write,rel = (pi/2) Q_Sigma tensor Y_R
```

up to endpoint rephasing and orientation reversal.

The equatorial classification is an analytic consequence imported into the
executable gate. The executable audit verifies the chosen `Y` representative,
not a symbolic derivation of the full generic formula.

The ready-subspace unitary is

```text
U_write
  = (I-Q_Sigma) tensor I_R
    + Q_Sigma tensor (-iY_R).
```

This is conditional on the inherited/adopted rules above. It is not a
complete microscopic action or a durable record instrument.

## Algebraic identity-phase family

The family

```text
U_chi
  = (I-Q_Sigma) tensor I_R
    + exp(-i chi) Q_Sigma tensor (-iY_R)
```

has the same conditional record projectors for every `chi`.

In a fixed source basis, a coherent zero/one-flux superposition produces
different joint source-record density matrices for different `chi`, while
the reduced record density is unchanged. The audit verifies this using
unnormalized density numerators of trace `2`; division by `2` gives the
normalized density matrices and preserves both statements.

This algebra does **not** establish that the phase is physically observable.
Coherence between the local-flux alternatives must belong to one admissible
total-charge sector, and an allowed phase reference or recombination
operation must exist. If the two alternatives are different total-charge
sectors, a charge-superselection rule can obstruct the comparison.

Therefore the current conclusion is only:

```text
chi is not fixed by the conditional record projectors.
```

Its gauge-invariant physical effect is open.

## What is fixed

```text
conditional record-changing holonomy class on the declared ready subspace;
the selected Y representative passes exact unitary and flux-sector checks.
```

## What is not fixed

```text
physical admissibility of coherent zero/one-flux comparison;
a source phase reference;
gauge-invariant observability of chi;
the complete source-record-environment operator;
physical action, durability, source mass, response, or alpha.
```

## Exact next gate

Determine from the complete charge/CPT/source branch whether `chi` is
forbidden, fixed, or physically irrelevant to the final response. Do not set
it to zero merely because the record-only reduced density cannot see it.

## Status

```text
unit_source_flux_sector_inherited = true
zero_flux_no_charged_write_adopted = true
relative_onset_saturation_inherited_as_adopted = true
equatorial_holonomy_classification_imported_analytic_result = true
chosen_Y_representative_verified = true
conditional_record_changing_holonomy_fixed = true
candidate_write_preserves_declared_flux_sector = true
physical_source_flux_nondemolition_derived = false
joint_density_changes_in_fixed_source_basis = true
reduced_record_density_invariant = true
coherent_flux_superposition_physically_admissible_derived = false
source_phase_reference_supplied = false
source_relative_phase_observability_derived = false
gauge_invariant_phase_effect_derived = false
complete_physical_write_operator_derived = false
physical_dynamical_action_fixed = false
complete_source_record_environment_operator_derived = false
physical_durability_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
