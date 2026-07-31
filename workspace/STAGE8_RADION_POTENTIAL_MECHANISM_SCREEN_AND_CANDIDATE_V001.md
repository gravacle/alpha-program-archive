# STAGE8_RADION_POTENTIAL_MECHANISM_SCREEN_AND_CANDIDATE_V001

LANE: CODEX 1
RELAY: 225 ("WHAT LIFTS THE FLAT DIRECTION? THE RADION POTENTIAL")
DATE: 2026-07-31

GATES: alpha_computed = false; proof_authorized = false; kappa_record_computed = false;
coupling_evaluation_authorized = false; production_authorized = false.

No numerical value of beta, rho, phi, T_R, E_R, k_R, any coupling, any root, any eigenvalue,
or any absolute interval is computed here. No measured constant is used or compared. The
Misner-Sharp / Brown-York fork is not resolved. This artifact screens mechanisms and writes a
symbolic candidate target; it does not derive or adopt a stabilizing potential.

---

## 0. Lead

Nothing sealed currently lifts the flat direction. The corpus identifies beta as the shift
direction of a massless radion and says pure circle reduction supplies no stabilizing
potential, but every candidate mechanism with the right qualitative shape is either absent,
adopted rather than derived, or unbuilt.

The cheapest next target is a two-term radion competition, not a one-term correction:

```text
R = ell_P exp(phi)

V_candidate(phi)
  = A_- exp(-p phi) + A_+ exp(q phi) + V_0

p > 0, q > 0.
```

An interior stationary point is possible only if the two derivative contributions oppose:

```text
dV_candidate/dphi
  = -p A_- exp(-p phi) + q A_+ exp(q phi).
```

With `A_- > 0` and `A_+ > 0` this has an interior stationary point symbolically. With only
one monomial, or with all surviving terms scaling the same way as the already invariant
`R^2 F^2` combination, there is no beta-fixing condition. This is not a minimization and no
value is solved.

The likely negative-power side would come from a fixed flux / fixed charged-current / compact
mode contribution. The likely positive-power side would come from a derived surface,
boundary, or spectrum term. The corpus has not derived either side as a radion potential.

---

## 1. Source Ground

The governing modulus gate grants a strict metric-only five-dimensional ansatz

```text
ds_5^2 = g_mu_nu dx^mu dx^nu + R^2 (d theta + A_mu dx^mu)^2
```

and, for constant `R`, the reduced term

```text
S_4/hbar = [1/(16 pi ell_P^2)] integral sqrt(-g)
  [R_4 - (R^2/4) F_mu_nu F^mu_nu],

K_KK = R^2/(16 pi ell_P^2).
```

Source: `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:23-43`.

The same file states the obstruction: the action-phase period fixes the coordinate period
and integer character lattice, but not the proper radius `R`; every

```text
R = beta c Delta tau, beta > 0
```

preserves the base interval, phase periodicity, topology, gauge covariance, and unit
character while changing `K_KK` by `beta^2`. Source:
`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:49-61`.

The same gate states the physics of the missing term:

```text
The radius is also a dynamical radion. Pure circle Einstein-Hilbert reduction
does not generate a potential that selects one constant value. Freezing it
without stabilization is not a complete reduction when electromagnetic stress
sources that mode.
```

Source: `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:67-70`.

The prior joint-saddle posing executed the degeneracy map:

```text
M_beta : (g_mu_nu, A_mu, R) -> (g_mu_nu, beta^{-1} A_mu, beta R)
```

and reported that the reduced form is exactly invariant because
`beta^2 R^2 * beta^{-2} F^2 = R^2 F^2`. Source:
`STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:38-51`. It also states that with
`phi := ln(R/ell_P)`, the map is the constant shift `phi -> phi + ln beta`; a term is
beta-sensitive exactly when it contains non-derivative `phi`; and the missing term is a
radion potential. Source:
`STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:78-92`.

The closure bar is stronger than "touches both geometries." The beta fixer must break the
sealed beta-degeneracy, act as radion stabilization, and be derived jointly with the complete
parent action class, spectrum, and matching rule. Source:
`STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md:168-200`;
`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:83-97`.

---

## 2. Mechanism Screen

### 2.1 Flux quantization / winding over the fiber

What is sealed:

- The primitive active stabilizer has an integer character lattice and primitive unit
  winding, but this is pointwise and does not itself localize a connection:
  `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:32-43`.
- The ordinary branch adopts a smooth principal `U(1)_rel` bundle and compact connection
  `a`, and holonomy is normalized by the primitive unit character:
  `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:47-68`.
- A local zero-or-one source-crossing sector carries
  `Q_Sigma = integral_Sigma j^mu dSigma_mu` with spectrum `{0,1}` as a local branch input:
  `SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md:22-33`.

R-scaling if it were a true fixed flux: if a flux through an R-scaled surface were fixed,
then schematically `F ~ n/R^2`, and the existing reduced factor would scale like

```text
R^2 F^2 ~ n^2 R^{-2} = n^2 ell_P^{-2} exp(-2 phi).
```

That is the right sign of scaling for an inverse-power side of a radion potential.

Status: NOT DERIVED. The corpus seals a character/holonomy lattice and a local charge-sector
input; it does not seal a quantized curvature flux through the R-scaled fiber or a rule that
holds that flux fixed under `R -> beta R`. The prior joint-saddle artifact already typed this
as character-not-flux: `STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:161-170`.

Missing: a derived statement that the fixed integer character becomes a fixed geometric flux
or current through the beta-sensitive surface, with domain, measure, and held-fixed rule.

Typed negative:

```text
flux_quantization_radion_term_derived = false | TYPE-U |
would-build: fixed geometric flux/current rule over the beta-sensitive fiber or surface
```

### 2.2 Casimir / vacuum energy of compact direction

What is sealed:

- The modulus gate's exact reopen list requires "the full Kaluza-Klein/record spectrum and
  unitary Lorentzian measure": `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:94-97`.
- The prior joint-saddle result classifies Casimir energy of the KK/record spectrum as
  unbuilt and warns that, if the spectrum arrives as vacuum/Casimir energy, the fork fires:
  `STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:167-173` and
  `STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:242-255`.

R-scaling if it existed: a compact-direction vacuum term would generically give

```text
V_Cas(phi) = C_Cas exp(-s phi)
```

for some `s > 0`, or a related logarithmic term, but the exponent, sign, subtraction scheme,
and Lorentzian measure are spectrum-dependent and not sealed here.

Status: UNBUILT. There is no sealed compact-direction spectral determinant that produces a
radion potential term. A candidate Casimir contribution would also consume energy/measure
data and therefore must declare the Misner-Sharp / Brown-York fork rather than silently pick
one.

Typed negative:

```text
casimir_radion_potential_derived = false | TYPE-U |
would-build: full KK/record spectrum, Lorentzian measure, subtraction, and fork-safe energy reading
```

### 2.3 Matter or record loops with different R scaling

What is sealed:

- The record-fidelity action "may generate a curvature stiffness after the continuum limit,"
  but no extra `c F^2` term may be added:
  `PRIMITIVE_ADDITIVE_RECORD_FIDELITY_ACTION_V002.md:110-120`.
- The finite holonomy response diagnostic is positive on the existing finite regulator, but
  its own scope excludes local Maxwell response, continuum/regulator independence,
  packing independence, linked-cluster density, kappa_record, Thomson stiffness, and alpha:
  `COMPLETE_QSPEC_FINITE_HOLONOMY_RESPONSE_RESULT_V001.md:131-153`.
- The induced-kernel cycle computes a leading interaction shape and selection rule, while
  explicitly leaving absolute magnitude to open scale families:
  `18_INDUCED_KERNEL_RESULT_V001.md:46-66`.

R-scaling if it existed: a loop determinant over a beta-sensitive tower could produce
`C_loop exp(-s phi)`, `C_loop exp(q phi)`, or `C_log phi`, depending on the spectrum and
subtraction. A loop over data that does not see `R` gives no radion potential.

Status: UNBUILT. The corpus has finite diagnostics and induced-form statements, but no
complete beta-sensitive determinant or loop functional that maps to a non-derivative
`phi` term.

Typed negative:

```text
loop_generated_radion_potential_derived = false | TYPE-U |
would-build: complete beta-sensitive spectrum/determinant or loop functional and its R-scaling
```

### 2.4 Boundary / brane-like term at the cell surface

What is sealed:

- Localized boundary terms are explicitly one of the mutation channels in which the
  metric-only tree relation becomes ambiguous:
  `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:72-84`.
- The record-cell surface audit says the null edge is not a reflecting material wall, records
  the waist area and null-edge action as failing to select because every positive radius can
  be obtained by normalization, and keeps the energy fork untouched:
  `STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md:89-102`.

R-scaling if it existed: a fixed surface tension or localized boundary action would
schematically contribute

```text
V_surf(phi) = A_+ exp(q phi), q > 0,
```

where `q` depends on whether the derived surface measure is spatial area, null boundary
measure, or another cell-surface functional. The corpus does not seal that exponent or
coefficient.

Status: ABSENT AS DERIVED PHYSICS; ADMISSIBLE ONLY AS A MUTATION CHANNEL UNTIL THE parent action
class is uniquely derived. A boundary term could supply the positive-power side of the
competition, but adding it would currently move the adoption rather than discharge it.

Typed negative:

```text
boundary_surface_radion_term_derived = false | TYPE-U |
would-build: target-independent localized boundary/surface action with derived measure and sign
```

### 2.5 Thresholded durability

What is sealed:

- Incident many-cell durability is intrinsically thresholded, not exact:
  `29_DURABLE_INTERVAL_LIMIT_RESULT_V001.md:21-39`.
- Future many-cell response constructions inherit thresholded `(T, delta)` quantifiers:
  `29_DURABLE_INTERVAL_LIMIT_RESULT_V001.md:47-55`.

R-scaling: none is sealed. Thresholded durability is currently a pass/fail or quantifier
structure over record dynamics, not an energy or action term of `phi`.

Status: NOT A POTENTIAL AS WRITTEN. It may constrain admissible many-cell constructions, but
it does not supply a non-derivative term `V(phi)`. Turning a durability threshold into a
radion cost would be a new construction.

Typed negative:

```text
thresholded_durability_radion_potential_derived = false | TYPE-U |
would-build: a derived action/cost functional from thresholded durability with explicit R-scaling
```

### 2.6 Charged current

What is sealed:

- The conserved Dirac current gives `Q_Sigma`; charged Dirac matter is a disclosed input:
  `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md:32-33`.
- The physical charge/current construction passes with disclosed Dirac/CAR input:
  `BID_SOURCE_PARENT_CLOSURE_GATE_V003.md:41-42`.
- The source-flux gate fixes a conditional write on the declared local unit-character sector,
  but it is not a complete microscopic action or durable record instrument:
  `SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md:80-89`.

R-scaling if it existed: a source term of the schematic form `integral J . A` is
beta-sensitive if `J` is held fixed while `A -> beta^{-1} A`; it is not beta-sensitive if the
current, measure, or source normalization co-scales with the field. The prior joint-saddle
posing states exactly this fork: what is held fixed under `R -> beta R` at parent-action level
is nowhere stated, and on one resolution a derived charged current could break the family:
`STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md:59-66`.

Status: CONSTRAINT-BLOCKED. The current exists as source structure, but the beta-breaking
claim depends on the held-fixed rule and complete parent action, neither sealed.

Typed negative:

```text
charged_current_breaks_beta_degeneracy = false | TYPE-C |
constraint: held-fixed rule under M_beta is unstated |
release: sealed parent-level statement of what is fixed under (g,A,R)->(g,beta^{-1}A,beta R)
```

### 2.7 Record structure: discrete seat / occupancy count

What is sealed:

- Seat occupancy is typed as a projector-coefficient slot and yields `g_N * T_R = pi hbar`:
  `26_SEAT_OCCUPANCY_RESULT_V001.md:8-30`.
- The pre-Stage-10 chain is complete except for the `E_ref` matching fork, which may not be
  decided by interface argument:
  `26_SEAT_OCCUPANCY_RESULT_V001.md:56-70`.
- Stage 10 is where the cell geometry normalizes the public response:
  `45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:34-61`.

R-scaling: the seat count itself carries no `R`; as a pure discrete count or relational
action marker it is `R^0`. A constant term has `d/dphi = 0` and cannot lift a shift
direction by itself. It could enter a beta-sensitive term only after a derived response or
cell-geometry map couples it to an R-dependent measure.

Status: SEALED AS RECORD STRUCTURE, NOT AS A RADION POTENTIAL.

Typed negative:

```text
seat_occupancy_lifts_radion = false | TYPE-R |
test: inspect the sealed seat relation; it contains T_R and action/energy seats, not R or beta
```

---

## 3. Leading Candidate, Written but Not Claimed

The first plausible target is a flux/current-plus-surface/spectrum competition:

```text
V_rad(phi)
  = A_flux n^2 exp(-2 phi)
    + A_surf exp(q phi)
    + A_loop exp(-s phi)
    + V_const

R = ell_P exp(phi),   q > 0, s > 0.
```

Interpretation:

- `A_flux n^2 exp(-2 phi)` is the fixed-flux or fixed-current inverse-power side. It exists
  only if the character/charge data are derived to be a fixed geometric flux/current under
  `M_beta`.
- `A_surf exp(q phi)` is a boundary/surface positive-power side. It exists only if a
  localized surface action with derived measure, sign, and admissibility is supplied by the
  complete parent action class.
- `A_loop exp(-s phi)` is a compact-spectrum loop/Casimir side. It exists only if the full
  KK/record spectrum and Lorentzian measure are derived, with fork exposure.
- `V_const` covers beta-blind record-seat and relational chain data.

Stationarity:

```text
dV_rad/dphi
  = -2 A_flux n^2 exp(-2 phi)
    + q A_surf exp(q phi)
    - s A_loop exp(-s phi).
```

A stationary point is possible only if at least two nonzero terms with different powers
survive and their derivative signs oppose. A single inverse-power flux term is monotone; a
single surface term is monotone; the already sealed `R^2 F^2` term under co-scaling is
constant along `M_beta`. Therefore no one-side candidate closes beta.

This candidate is a specification target under Q-92, not a derived potential. It is
conditional on unbuilt or constraint-blocked objects and may not be reported as a beta
derivation.

---

## 4. Missing Objects

To turn the symbolic target into a derivation, the corpus would need all of the following:

1. **Held-fixed rule under `M_beta`.** Decide by derivation what is held fixed at the parent
   action level when `(g,A,R)->(g,beta^{-1}A,beta R)`. Without this, charged-current and
   flux terms cannot be typed.
2. **Flux/current geometricization.** A theorem mapping unit character / `Q_Sigma` data to a
   fixed beta-sensitive geometric flux or current with domain and measure.
3. **Boundary or spectrum side.** A target-independent positive-power or opposite-scaling
   term: derived localized surface action, or derived full KK/record spectrum and
   determinant/Casimir functional.
4. **Joint parent action class.** V002 requires action class, radion stabilization,
   spectrum, and matching rule together; no isolated stabilizer can pass:
   `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:83-97`.
5. **Fork declaration.** Any energy-consuming or vacuum-energy reading must carry the
   Misner-Sharp / Brown-York fork rather than selecting it silently.

---

## 5. Search Scope and File Lists

Roots searched:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
/Users/bgm/MB Work/alpha_supervision
/Users/bgm/Documents/Documents - Brian's MacBook Pro/New project/gravity_emergence_evidence_program
```

Exclusions:

```text
a32_holdout/custodian_private/
.git/
external/ and third_party/ on the broad source-line sweeps
```

Queries, word-boundaried or exact phrase where appropriate:

```text
radion potential | radion_stabilization_derived | radion stabilization |
massless radion | stabilizing potential

flux quantization | quantized flux | unit character | primitive unit winding |
Q_Sigma | charged current | conserved current | Hol_gamma | holonomy

Casimir energy | vacuum energy | compact direction | full Kaluza-Klein/record spectrum |
matter loop | record loop | determinant | loop

localized boundary terms | boundary term | brane | cell surface | surface term |
thresholded durability | seat occupancy | MARKER_OCCUPIES | occupancy
```

The narrow radion/stabilization file list resolves to the live current cluster:

```text
COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md
STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md
STAGE8_JOINT_SADDLE_SYSTEM_POSING_EINSTEIN_V001.md
STAGE8_RECORD_CELL_SURFACE_AND_BETA_CLOSURE_HUNT_EINSTEIN_V001.md
QUESTIONS_SETTLED_REGISTER_V001.md
RELAY_PASTE_221_BUILD_JOINT_SADDLE_SYSTEM_EINSTEIN_V001.md
RELAY_PASTE_224_WHAT_IS_HELD_FIXED_AND_THE_FRAME_EINSTEIN_V001.md
RELAY_PASTE_225_RADION_POTENTIAL_CODEX1_V001.md
TASK_LIST_TO_ALPHA_2026-07-31_V001.md
BOHM_RATIO_ROUTE_ADJUDICATION_RESULTS_2026-07-28.md
BOHM_TWO_STEPS_WORKFLOW_RESULTS_2026-07-28.md
```

The broad flux/current, loop/determinant, and surface/boundary queries return many older,
parent, diagnostic, and review hits. The current load-bearing files for this determination
are the ones cited in Sections 1-3 plus the cleanroom-output files `18`, `24`, `26`, `29`,
and `45`. No hit supplied a derived non-derivative `phi` potential with an R-scaling and a
stationarity condition.

---

## 6. Verdict

```text
sealed_radion_lifting_mechanism_exists = false | TYPE-S |
roots: listed in Section 5 |
exclusions: a32_holdout/custodian_private, .git, external/third_party on broad source-line sweeps |
query: listed in Section 5

leading_candidate_written = true
leading_candidate_derived = false | TYPE-U |
would-build: fixed flux/current inverse-power side plus derived surface/spectrum opposite-scaling side

radion_stabilization_derived = false | TYPE-U |
would-build: complete parent action class + radion potential + spectrum + matching, jointly derived
```

Only one physical negative is claimed: sealed record-seat occupancy is R-blind and cannot lift the
radion by itself. The broader result is a specification negative: the corpus currently has no
derived stabilizing potential, and the first candidate requires missing held-fixed, flux/current,
surface/spectrum, and joint-action inputs.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
