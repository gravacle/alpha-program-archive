# BID Minimal Public Causal-Cell Derivation v001

Date: 2026-07-24

## Purpose

This gate addresses locked-plan Stage 3 only. It derives the absolute scale of
the primitive causal record cell in the declared ordinary, isotropic `3+1`
dimensional branch. It contains no electromagnetic coupling, measured mass,
cosmological endpoint, or alpha target.

## Inputs and status

The derivation uses four inputs whose logical status must remain visible:

1. **First-record action marker (relative marker derived; physical
   Hamiltonian identification open):**

   ```text
   E_R T_R = pi hbar.
   ```

   The clean-room derives the relative marker `Delta S_record=pi hbar`. The
   displayed equality additionally identifies that marker with the complete
   stationary boundary Hamiltonian carried by the cell. That identification
   is not yet derived by the active source-parent action and is therefore a
   Stage 3/4 interface obligation, not an input that may be silently passed.

2. **Causal-diamond support (declared ordinary branch):**

   ```text
   R_R = c T_R / 2.
   ```

   `R_R` is the maximum areal radius of the causal diamond with tip-to-tip
   proper-time separation `T_R`.

3. **Public recoverability condition (physical admissibility):**

   On the maximal spherical section, the Misner-Sharp compactness must obey

   ```text
   C_R = 2 G E_R / (c^4 R_R) <= 1.
   ```

   `C_R > 1` is trapped and cannot be the outwardly recoverable primitive
   comparison cell of this branch.

4. **Marginal public-closure rule (adopted Level-1 Gravacle rule):**

   The allow/require boundary is the first physically admissible public
   record cell. The least positive `T_R` is attained at the boundary of the
   recoverable set:

   ```text
   C_R = 1.
   ```

   This fourth input is the selector. Without it, public recoverability gives
   a half-line of allowed durations and no absolute record scale.

The use of `C_R=1` is not inferred from alpha. It is the geometric meaning of
the adopted "first admissible boundary" rule in the isotropic branch. A
reviewer may reject that rule, but the rule may not be hidden or replaced by
numerical agreement downstream. Likewise, the active theory must derive the
physical map `Delta S_record=E_R T_R`; the relative character calculation
alone does not supply it.

## Exact derivation

Substituting the first-record marker and causal radius into the compactness
gives

```text
C_R
  = 2 G (pi hbar/T_R) / [c^4 (c T_R/2)]
  = 4 pi G hbar / (c^5 T_R^2)
  = 4 pi t_P^2 / T_R^2,

t_P = sqrt(hbar G/c^5).
```

The marginal public-closure rule therefore has one positive root:

```text
T_R = 2 sqrt(pi) t_P.
```

The associated cell radius, energy, and mass are

```text
R_R = sqrt(pi) l_P,
E_R = (sqrt(pi)/2) E_P,
M_R = (sqrt(pi)/2) m_P,

l_P = c t_P,
E_P = hbar/t_P,
m_P = E_P/c^2.
```

The causal-diamond geometry is consequently

```text
V_3,max = (4/3) pi^(5/2) l_P^3,
V_4     = (2/3) pi^3 l_P^4.
```

No measured quantity selects these coefficients.

## Deformation control

To expose every load-bearing normalization, write

```text
E_R T_R = s hbar,
R_R = xi c T_R,
C_R = chi_*.
```

Then

```text
T_R/t_P = sqrt[2 s/(xi chi_*)].
```

The derived value uses exactly

```text
s = pi,
xi = 1/2,
chi_* = 1.
```

Changing the action marker, the causal support, or the marginal selector
changes the absolute scale. The audit must retain these deformations. In
particular, replacing `C_R=1` by only `C_R<=1` leaves

```text
T_R >= 2 sqrt(pi) t_P
```

and does not derive a unique cell.

## Scope and downstream role

The algebra fixes the primitive cell scale and local source threshold if the
complete source-parent dynamics derives
`Delta S_record=E_R T_R`. Until that interface is closed, the result is a
conditional candidate rather than a completed Stage 3 result. It also does
not yet establish physical durability, the complete dressed charged spectral
measure, the infrared form of the charged excitation, `Q_spec`, the Thomson
response, or alpha.

## Status

```text
first_record_action_marker_used = true
relative_action_marker_derived = true
relative_marker_equals_complete_stationary_Hamiltonian_action_derived = false
causal_diamond_support_used = true
spherical_Misner_Sharp_compactness_used = true
marginal_public_closure_rule_adopted_Level_1 = true
conditional_absolute_record_interval_formula_derived = true
absolute_record_interval_derived_in_declared_branch = false
primitive_record_radius_derived_in_declared_branch = false
primitive_record_energy_scale_derived_in_declared_branch = false
strict_untrapped_inequality_alone_selects_unique_scale = false
nonisotropic_global_cell_exhaustion_derived = false
physical_durability_derived = false
complete_Q_spec_sealed = false
physical_Thomson_stiffness_computed = false
alpha_computed = false
proof_authorized = false
```
