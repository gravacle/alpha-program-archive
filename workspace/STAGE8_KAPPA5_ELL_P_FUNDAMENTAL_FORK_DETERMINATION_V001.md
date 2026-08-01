# Stage 8 kappa5 / ell_P Fundamental Fork Determination

Status: APPEND-ONLY DETERMINATION / NOT AN ADOPTION

Relay: PASTE 232, CODEX LANE 1, 2026-07-31

Register head at issue: Q-94.

Custody: Q-91 applies. No git command, corpus gate, or deploy-status command is part of this
artifact's production.

Forbidden outputs not produced: alpha, kappa_record, kappa_Thomson, any coupling, scale, root,
eigenvalue, beta function, E_R, T_R, k_R, absolute interval, measured-constant comparison, or any
numerical value of kappa5, ell_P, beta, rho, or phi.

## Lead

The sealed corpus does not force one of `kappa5` or `ell_P` to be fundamental.

The new parent KK artifact makes `kappa5` upstream inside a **standard KK import / explicit
choice**: it writes a five-dimensional Einstein-Hilbert action with coefficient `1/(2 kappa5^2)`
and then defines

```text
ell_P^2 := kappa5^2 / (2 pi R0).
```

That is the standard KK ordering, but it is not a derived record-cell law. The same artifact says the
parent action is chosen, the numerical value and microscopic relation of `kappa5` are absent, and the
reduction alone holds fixed neither `kappa5` nor `ell_P`
(`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:12-28`,
`:30-41`, `:63-73`).

The live reduced route, by contrast, has silently used the branch where `ell_P` is fixed. That branch
preserves the old `beta^2` statement. The fixed-`kappa5` branch does not. Therefore the `beta^2`
diagnosis is branch-conditional, not sealed branch-free structure.

```text
kappa5_vs_ell_P_branch_forced = false | TYPE-S |
  roots: cleanroom workspace, alpha-program-archive/workspace,
         alpha-program-archive/cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git, sidecar-only hits when resolving source text |
  query: "kappa5", "kappa_5", "ell_P", "G_5", "M_5", "ell_5",
         "five-dimensional Newton", "5D Newton", "parent normalization",
         "fiber volume", "2 pi R", "circumference", "held fixed", "K_KK", "beta^2"
```

## 1. Source Text

### 1.1 Parent KK construction

The parent construction opens by saying the corpus search found no named parent normalization or
`ell_P` definition, and that it therefore introduces a symbolic KK specification, not a numerical
result (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:5-9`).

It chooses the parent action as a standard KK import:

```text
S5[g5, matter] = (1/(2 kappa5^2)) integral_{M4 x S1} d4x dtheta sqrt(-G) R5[G]
                 + S5,matter.
```

The artifact marks this as a standard KK import / explicit choice
(`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:12-16`).

It defines the five-dimensional normalization and records its absence from the prior corpus:

```text
kappa5^2 is the parent gravitational normalization, defined here as the coefficient inverse
of the five-dimensional Einstein-Hilbert density. Its numerical value and relation to any
microscopic theory are ABSENT.
```

Source: `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:25-28`.

It then defines `ell_P` from `kappa5` and the reference fiber radius:

```text
ell_P^2 := kappa5^2 / (2 pi R0).
```

and states that `ell_P` is a function of the parent normalization, fiber period, and reference
radius, not an independently imported corpus fact
(`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:30-41`).

The reduction shows the fiber factor entering the four-dimensional coefficient:

```text
(2 pi R0)/(2 kappa5^2) integral d4x sqrt(-g)
  [R4[g] - (R0^2/4) F_mu_nu F^mu_nu + ...].
```

Source: `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:43-61`.

The held-fixed fork is explicit:

```text
Under R -> beta R, the reduction alone holds fixed neither kappa5 nor ell_P:
the four-dimensional EH coefficient scales with the fiber volume if kappa5 is held fixed,
while it is constant only if the parent normalization is rescaled with the fiber extent.
```

Source: `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:63-70`.

### 1.2 Existing reduced route

The coupled modulus gate grants a principal circle and strict metric-only five-dimensional ansatz:

```text
ds_5^2 = g_mu_nu dx^mu dx^nu + R^2 (d theta + A_mu dx^mu)^2,
theta equivalent to theta + 2 pi.
```

It also grants the two-derivative five-dimensional Einstein-Hilbert action and no independent
connection term (`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:15-33`).

For constant `R`, it displays the reduced form:

```text
S_4/hbar = [1/(16 pi ell_P^2)] integral sqrt(-g)
  [R_4 - (R^2/4) F_mu_nu F^mu_nu],

K_KK = R^2/(16 pi ell_P^2).
```

Source: `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:35-43`.

It then states the beta obstruction:

```text
R = beta c Delta tau, beta > 0
```

preserves the listed kinematic data while changing `K_KK` by `beta^2`
(`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:49-65`).

The held-fixed artifact later sharpened the scope: the frame lead is refuted at constant `R`, but the
corpus has silently displayed a reduced form with `ell_P` constant, and that is the assumption beneath
`beta^2` (`STAGE8_HELD_FIXED_AND_FRAME_DETERMINATION_EINSTEIN_V001.md:25-52`,
`:54-80`, `:138-164`).

### 1.3 Record-cell structure

The record-cell and projective-bundle sources do not force either normalization branch.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` derives the local projective line bundle, comparison
connection, curvature form, and primitive comparison character, but it explicitly does not choose a
connection, a curvature, a kinetic coefficient, a unique induced Maxwell stiffness, or exterior EM
matching (`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:16-43`, `:45-93`, `:94-117`).

`BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md` derives a dimensionless public-record
counting metric and composition law, but states that it does not derive the deeper action, durability
dynamics, source pole, or alpha (`BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md:38-63`,
`:96-118`).

`BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md` records an exact scale orbit: first-opening
kinematics fix a dimensionless action interval, not one absolute duration; the absolute interval
closes only if the complete parameter-free parent supplies a Lorentz-scalar equation with one
isolated positive stable solution (`BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:10-64`,
`:66-90`).

`STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md` says prior work names but does not
derive the rule converting internal/projective geometry to dimensional spacetime length, and it
targets a beta or equivalent length map without deriving or choosing it
(`STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md:15-69`, `:71-103`).

These sources fix internal dimensionless structure and identify the conversion gap. They do not
state a parent-normalization law.

## 2. Standard KK Reading

Imported standard reading: in textbook Kaluza-Klein reduction, the higher-dimensional gravitational
normalization is the parent parameter; the lower-dimensional gravitational coefficient is derived
from it plus the compactification volume. In this notation, the standard reading is:

```text
kappa5 fundamental
ell_P^2 = kappa5^2 / (2 pi R0)
```

This reading applies conditionally to the **imported KK parent action** because that artifact writes
exactly this action and definition (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:12-41`).

It does not automatically apply as a derived law of this corpus, because this fiber is not just a
generic extra dimension already equipped with a physical metric. The coupled modulus gate says the
canonical Hopf fiber is not automatically the active relative-phase `U(1)_rel`, and that a free
relative-phase lift and physical metric require additional structure
(`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:3-13`). The record bundle supplies a comparison
connection and character, but not a kinetic coefficient or physical stiffness
(`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:94-117`).

Thus standard KK favors `kappa5` as the fundamental datum **inside the imported parent model**. It
does not force `kappa5` as a theorem of the record-cell construction.

## 3. Branch Pricing

### 3.1 Branch A: `kappa5` fixed

If `kappa5` is fixed under `R -> beta R`, then `ell_P` is not constant. It is defined from
`kappa5` and the fiber extent, so changing the reference fiber extent changes the reduced
four-dimensional coefficient.

In the raw parent reduction, the `F^2` coefficient carries both:

```text
fiber volume factor: R
gauge block factor:  R^2
```

Therefore the gauge coefficient that was written as `K_KK = R^2/(16 pi ell_P^2)` scales as

```text
K_KK -> beta^3 K_KK
```

when it is re-expressed with the branch-dependent `ell_P(R)`. If the simultaneous field map also
uses `A -> beta^-1 A`, then the action term `K_KK F^2` scales by the remaining fiber-volume factor
rather than staying invariant term-by-term. That is the parent-reduction version of the earlier
"Jordan branch" observation: the action may co-scale as a whole, but the reduced `beta^2`
diagnosis is not the correct branch-free statement
(`STAGE8_HELD_FIXED_AND_FRAME_DETERMINATION_EINSTEIN_V001.md:138-155`).

Consequences:

1. `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:60-61`, the statement that the family changes
   `K_KK` by `beta^2`, becomes branch-conditional and false on this branch.
2. The radion coordinate `phi = ln(R/ell_P)` used in the previous route is no longer the same
   shift coordinate. The claim that the map is exactly `phi -> phi + ln beta` depends on fixed
   `ell_P` (`STAGE8_RADION_POTENTIAL_MECHANISM_SCREEN_AND_CANDIDATE_V001.md:94-106`).
3. `rho = R_*/ell_P` is no longer a ratio of an independent radius to a fixed denominator; the
   denominator is itself tied to the numerator through the parent reduction. The held-fixed
   artifact names this price explicitly (`STAGE8_HELD_FIXED_AND_FRAME_DETERMINATION_EINSTEIN_V001.md:144-147`).
4. The positive/negative radion-potential screens, any `K_KK` weighting, and every downstream use of
   the old `beta^2` sentence must be re-examined before being used as a blocker.

Cost: this branch follows the standard parent-normalization reading, but it breaks the old `beta^2`
diagnosis. It does not by itself compute or select anything. It also does not make the beta orbit
unphysical: beta remains a dimensionless invariant of one five-geometry, as the held-fixed artifact
already refuted (`STAGE8_HELD_FIXED_AND_FRAME_DETERMINATION_EINSTEIN_V001.md:25-52`,
`:149-155`).

### 3.2 Branch B: `ell_P` fixed

If `ell_P` is fixed under `R -> beta R`, then the parent normalization cannot also be fixed. The
definition

```text
ell_P^2 := kappa5^2 / (2 pi R0)
```

forces `kappa5^2` to rescale with the fiber extent. The parent construction states this directly:
the four-dimensional coefficient is constant only if the parent normalization is rescaled with the
fiber extent (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:63-70`).

Consequences:

1. The old reduced-level `K_KK` scaling by `beta^2` survives.
2. The existing reduced route's `phi = ln(R/ell_P)` shift coordinate survives.
3. The price is that the five-dimensional parent is not one fixed-normalization parent action across
   the beta family. It is either a family of parent normalizations or a missing frame/field-redefinition
   law.
4. Complete-parent-action uniqueness becomes harder, because the parent normalization law is part of
   what must be unique.

What would have to supply it:

```text
parent_normalization_scaling_law_derived = false | TYPE-U |
  would-build: independent parent-normalization/frame law proving that kappa5^2 rescales with
               fiber extent while ell_P remains fixed
```

No current record-cell, bundle, or Hilbertization source supplies that law.

## 4. Is The Fork Derivable?

No. The fork is not derivable from sealed text as of this artifact.

The corpus contains:

1. a conditional standard-KK candidate in which `kappa5` is upstream and `ell_P` is defined;
2. a live reduced-level route that silently holds `ell_P` fixed;
3. record-cell/projective structures that fix dimensionless internal data but do not select the
   parent gravitational normalization;
4. explicit reopen conditions demanding a physical lift, unique action class, parameter-free saddle,
   full spectrum/measure, and threshold matching before the route computes anything
   (`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:86-100`;
   `STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:55-73`).

There is no theorem that chooses between the two held-fixed laws.

```text
held_fixed_branch_derived = false | TYPE-U |
  would-build: independent parent-normalization/frame law, derived before any beta/rho/coupling
               evaluation, specifying whether kappa5 or ell_P is held fixed under R -> beta R

ell_P_fixed_branch_adopted_by_reduced_route = true | TYPE-C |
  constraint: live reduced artifacts display the branch but do not derive the parent law

kappa5_fixed_branch_standard_import = true | TYPE-C |
  constraint: valid inside the imported standard KK parent action, not a record-cell theorem
```

Under Q-82/Q-92, this is axiom-shaped: a node with no discharge route is terminal unless and until a
derivation is supplied. Naming the missing law is the complete result of this relay.

## 5. What Changes To The beta Diagnosis

The beta diagnosis splits:

```text
if ell_P fixed:
  K_KK -> beta^2 K_KK
  old beta^2 statement survives

if kappa5 fixed:
  ell_P varies with R
  K_KK -> beta^3 K_KK  (raw coefficient)
  K_KK F^2 under A -> beta^-1 A co-scales by the remaining fiber-volume factor
  old beta^2 statement does not hold as written
```

Thus the correct status is:

```text
beta2_obstruction_branch_free = false | TYPE-R |
  test: substitute the parent KK definition of ell_P into the reduced coefficient and compare
        the held-fixed branches

beta2_obstruction_under_ell_P_fixed = true | TYPE-C |
  constraint: depends on the reduced-level held-fixed adoption

beta2_obstruction_under_kappa5_fixed = false | TYPE-R |
  test: fixed parent normalization makes the reduced coefficient carry the fiber-volume factor
```

This does not refute the beta orbit itself. It refutes only the branch-free use of the `beta^2`
sentence as the diagnosis of the whole geometric route.

## 6. Search Scope

Roots searched:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
```

Custodian-private material was neither opened nor searched.

Representative queries:

```text
kappa5
kappa_5
ell_P
G_5
M_5
ell_5
five-dimensional Newton
5D Newton
parent Newton
parent normalization
fiber volume
internal volume
circumference
2 pi R
fiber integration
held fixed
K_KK
beta^2
Einstein-frame
Jordan-frame
Weyl
```

The search found a standard KK candidate and the reduced-level held-fixed adoption. It did not find a
derived parent-normalization law.

