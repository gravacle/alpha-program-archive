# RESULT — THE FIBER RADIUS IS NOT THE CELL RADIUS, AND WHAT THAT LEAVES

Ordered by the reviewer lane 2026-07-29 on the principal's claim that the program has already
projected a curvature term for the modulus radius in order to compute an event-horizon size.
Read-only sweep of PARENT, all three cleanrooms, SUPERVISION, and `_external_handoffs`, excluding
vendored dependency trees, `third_party/`, `external/`, `sources/`, `papers/`, `raw/`,
`extracted/`, and `*_review_packet_*` / `*_proof_packet_*` snapshots (checked separately: no
load-bearing artifact exists only inside a packet). Nothing was computed or evaluated.

Throughout, `C_R` is the CLEANROOM COMPACTNESS RATIO. Where the PARENT heat-kernel induced
Einstein coefficient is meant it is written `C_R(x) [PARENT-BR-INDUCED-EINSTEIN-COEFFICIENT-C-R]`.

## 1. WHAT THE PRINCIPAL GOT RIGHT

`C_R = 1` IS, IN CONTENT, A MARGINAL SELF-GRAVITATION CONDITION. It places the cell's areal
radius at the gravitational radius of its own energy content, and it is the corpus's ONLY
absolute-scale selector. `BID_MINIMAL_PUBLIC_CAUSAL_CELL_DERIVATION_V001.md:49-60` — "The allow/
require boundary is the first physically admissible public record cell. The least positive `T_R`
is attained at the boundary of the recoverable set: `C_R = 1`. This fourth input is the selector.
Without it, public recoverability gives a half-line of allowed durations and no absolute record
scale." Corroborated at `STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md:64-65`.

## 2. WHAT HE GOT WRONG — NO CURVATURE TERM WAS PROJECTED

`C_R = 1` IS AN ADOPTED LEVEL-1 RULE, NOT THE OUTPUT OF A PROJECTION. The Misner-Sharp
compactness enters as an admissibility INEQUALITY and the threshold is PASSED IN AS A FUNCTION
ARGUMENT: `scripts/derive_bid_minimal_public_causal_cell_v001.py:18-22` defines
`scale_ratios(action_marker, causal_radius_fraction, compactness_threshold)`, docstring `:4-5`
"This program verifies algebra and deformation sensitivity. It does not prove the physical
marginal-publicity premise." The result JSON records
`"compactness_threshold_chi_star": "1"`, `"marginal_public_closure_rule_status": "ADOPTED_LEVEL_1"`,
`"physical_premise_proved_by_script": false`. The gate says it outright at `:62-64`: "The use of
`C_R=1` is not inferred from alpha. It is the geometric meaning of the adopted 'first admissible
boundary' rule."

BOUNDED NEGATIVE, all roots with the stated exclusions: `marginally trapped` 0 files,
`apparent horizon` 0, `Schwarzschild radius` 0, `gravitational radius` 0, `quasi-local mass` 0,
`Hawking mass` 0, `Raychaudhuri` 0, `hoop conjecture` 0, `null expansion` 0. The only
trapped-surface language in the program is `BID:46`, and its own flag `:167` reads
`strict_untrapped_inequality_alone_selects_unique_scale = false`. THE CORPUS NEVER WRITES
"HORIZON" ABOUT THE CELL.

THE HORIZON WORK THE PRINCIPAL REMEMBERS DOES EXIST AND IT RUNS THE OTHER WAY. The parent EDM
family computes a Reissner-Nordstrom outer horizon radius
(`scripts/primitive_one_particle_edm_coupled_exterior_map_v003.py:377-382`), and its purpose is
EXCLUSION: `_v004.py:273-280` names the key literally `"no_horizon"`;
`compute_..._halfline_independent_local_v004.py:58` sets `MIN_EXTERIOR_HORIZON_MARGIN = 1.0` inside
a pass-conjunction; the gate lists the margin in "Frozen budgets" between two residual tolerances.
**THE PROGRAM COMPUTED HORIZON SIZES TO CERTIFY ITS SOLUTIONS ARE HORIZON-FREE.**

## 3. THE RULING — TWO OBJECTS, NO BRIDGE, AND THE FENCE IS A PROOF

`R` (modulus gate) is the metric length of a GRANTED INTERNAL FIBER DIRECTION in a 5-D total
space: `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:23-28`,
`ds_5^2 = g_mu_nu dx^mu dx^nu + R^2 (d theta + A_mu dx^mu)^2`; `:17` "Grant a principal circle".
`R_R` (BID cell) is an AREAL RADIUS INSIDE `g_mu_nu`: `BID:21-25`, `R_R = c T_R / 2`, "the maximum
areal radius of the causal diamond". **DIFFERENT TYPES OF LENGTH — one transverse to spacetime,
one inside it.**

FIVE INDEPENDENT LINES:
1. ZERO TOKEN OVERLAP. `BID` contains no instance of `bundle`, `fiber`, `fibre`, `circle`, `U(1)`,
   `Kaluza`, `K_KK`, `alpha_tree`, `rho`, `ell_P`, `modulus`. The gate contains no `cell`, `T_R`,
   `R_R`, `causal`, `diamond` (the two case-insensitive hits are the substrings for**bid**s and
   fibe**r_r**adius).
2. NO THIRD ARTIFACT CARRIES BOTH. Across PARENT and all three cleanrooms, the only files matching
   `K_KK|alpha_tree|charge_fiber|radion` are the modulus gate V001 and V002. `radion` occurs in
   ONE artifact in the entire program.
3. THE CORPUS EXPLICITLY FORBIDS THE COLLAPSE.
   `STAGE8_GRAVITY_EVIDENCE_ADMISSION_AND_FIVE_STRATA_BINDING_V001.md:138-143` — "The following
   are three independent scale obligations and must not be collapsed": `x` (BR depth), `rho`
   (charge-fiber radius ratio), `T_R` (absolute record interval). `:150` `routes_merged = false`.
4. TWO OTHER PRINCIPLES WOULD BE CONTRADICTED, NOT SUPPORTED.
   `primitive_causal_record_cell_domain_principle_v001.md:63-65` — "The compact `U(1)` phase is a
   fiber/connection on the spacetime cell, NOT an extra spacetime circle."
5. **THE DECISIVE ONE — THE GATE CONTAINS A PROOF, NOT A PREFERENCE.** `gate:53-61`: "Even if one
   unique base record interval `Delta tau` is granted, every `R = beta c Delta tau, beta > 0`
   preserves the base interval, phase periodicity, topology, gauge covariance, and unit character
   while changing `K_KK` by `beta^2`." **HANDING THE GATE A DERIVED RECORD INTERVAL LEAVES A
   ONE-PARAMETER FAMILY FREE.** This is not "we have not shown they are the same" — it is "they
   cannot be, because `beta` survives." A prior reviewer reached the same result independently on
   2026-07-28 (`RATIO_ROUTE_CROSS_CITATION_MAP_2026-07-28.md:96-101`).

ZERO OF THE FIVE REOPEN CONDITIONS MOVE. Not one is partially discharged. And S3 IS MEMO-ONLY:
bounded negative — the gate has no audit script, no result JSON, and no test; a whole-tree grep
for `COUPLED_RECORD_BUNDLE_MODULUS_GATE` returns only ledger entries, sidecar seals, the strata
binding, one external ledger copy, and supervision notes.

Independent blocks on condition 3 alone, all pre-existing:
`reports/alpha_first_durable_capacity_moduli_v001.md:3` `BLOCKED_CAPACITY_ONE_LEAVES_CONTINUOUS_MODULI`
(`:19` "the first-record condition supplies one equation but does not select the charge-circle
radius"); `alpha_capacity_constrained_induced_action_v001.md:3`
`NO_GO_CAPACITY_CONSTRAINED_LOGDET_HAS_NO_INTERIOR_RQ_STATIONARY_POINT`;
`alpha_coupled_flux_logdet_modulus_selection_v001.md:3`
`NO_GO_ONE_STATISTICS_COUPLED_LOGDET_NO_FINITE_RADIUS_SADDLE`;
`alpha_coupled_flux_first_capacity_moduli_v001.md:21` withdrawing the earlier `r=1` claims.

## 4. THE ROAD WAS TAKEN, AND IT STOPS ONE STRUCTURE SHORT BY CONSTRUCTION

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` BUILDS THE BUNDLE FROM THE RECORD CELL — `:18-20` "The
new principle places one primitive record degree on every admissible causal record cell." It
obtains the line bundle, the cocycle condition, a connection forced by covariant comparison
(`:72-73`), a globally defined curvature (`:76`), and the unit character (`:90`). IT HAS A
PRODUCER, A RESULT, AND A TEST — MORE MACHINERY THAN S3 HAS.

WHY IT CANNOT REACH THE RADIUS, AND THIS IS STRUCTURAL, NOT A LAPSE: `:96-97` "Connections on a
fixed line bundle form an affine space. Bundle geometry does not choose one `a`, one curvature, or
one kinetic coefficient." A bundle derived from record combinatorics is TOPOLOGICAL AND HOLONOMIC.
IT HAS NO FIBER METRIC. A radius is a metric datum, so no amount of bundle-from-record work
produces one.

It was then demoted: `FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md:19-20` — V001 and the
projective bundle artifact "remain provenance records, but they are not authority for a physical
charged connection"; ledger type `CONDITIONAL_PROJECTIVE_LIFT_BUNDLE_NOT_PHYSICAL_CONNECTION`.
And the gate records independently why the projective route cannot supply the fiber: `V002:5-10`
the canonical Hopf fiber of a normalized qubit is its COMMON phase, whereas the charged branch
uses the endpoint-preserving RELATIVE phase, whose Bloch action has fixed record poles.

The larger abandoned road is the `T2 x S2` carrier, where the coupling was read off a fiber-radius
ratio (`field_access_allow_require_unification_v001.md:1920-1927`). Formally retired at
`alpha_br_structure_provenance_declaration_v001.md:121-126`, with `:151-155` recording that it
"remains unsupported rather than physically disproved" and that metric, spin structure, radii and
operator category are all still required. The four no-gos above are that route's radius attempts.

## 5. THE ONE OBJECT THIS LEAVES, NAMED BY THE CORPUS AND NEVER ATTEMPTED

The `beta`-family proof localises the entire deficit in ONE missing datum: A DERIVED RELATION
BETWEEN THE INTERNAL (PHASE / FUBINI-STUDY) METRIC AND THE EXTERNAL (LORENTZIAN / DIAMOND) METRIC
ON ONE RECORD CELL. The gate names its absence exactly: `:63-66` "The Fubini-Study metric fixes
dimensionless distances in projective state space. IT DOES NOT FIX THEIR DIMENSIONAL CONVERSION
RELATIVE TO THE SPACETIME METRIC OR `ell_P`."

THE SAME OBJECT IS NAMED INDEPENDENTLY, BY A DIFFERENT HAND, AS THE CRUX — AND FLAGGED AS NEVER
ATTEMPTED. `_external_handoffs/fable_alpha_cleanroom/OUTPUT/45_STAGE10_HANDOFF_GEOMETRIC_BRIEF_V001.md:36-42`
— "**(A) The causal diamond is present but unconsulted.** ... The coupling chain (cycles 3-6) used
ONLY the star's internal spectral geometry and phase budgets — THE CELL'S LORENTZIAN GEOMETRY
NEVER ENTERED." And `:58-62` — "the `E_ref` fork is geometrically the question WHICH CELL GEOMETRY
NORMALIZES THE PUBLIC RESPONSE — the ratio of internal (Fubini-Study/phase) geometry to external
(Lorentzian/diamond) geometry of one record cell. THIS IS THE FIRST POINT IN THE PROGRAM WHERE THE
GRAVITY-FACING GEOMETRY BECOMES LOAD-BEARING FOR THE COUPLING."

WHY THIS TARGET IS DIFFERENT FROM EVERY CROSS-CONSTRUCTION IDENTIFICATION THAT FAILED TODAY: it
requires NO bridge between disjoint constructions. ONE record cell carries BOTH structures already
— it is a causal diamond (external) bearing a primitive projective record degree (internal). The
object to be derived lives on a single object that both constructions already agree exists.

HYPOTHESIS WORTH TESTING, RECORDED AS A HYPOTHESIS AND NOT AS A RESULT: the recovered
first-opening-root principle (`primitive_same_cell_opening_normalization_principle_v001.md`,
2026-07-21) defines stiffness as the first positive root of a first-opening operator acting on ONE
complete Lorentz-invariant record cell, with "no separate kappa to fit or identify with the
coupling." If the opening condition constrains the internal phase budget AND the external causal
geometry SIMULTANEOUSLY, then the onset condition IS a relation between the two metrics — i.e. it
is the missing datum. THIS IS UNVERIFIED. The scope limit already of record stands: RESTORING THE
PRINCIPLE DOES NOT RESTORE THE ROUTE, and whether the first opening root is COMPUTABLE is open.

## 6. TWO STANDING CAUTIONS ON THIS TARGET

- `BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:59-61` (2026-07-23) already locates the
  fix in this saddle and records it as absent: "Such an identification must follow from the coupled
  gravity-source-record saddle or another target-independent stationary condition", with `:90`
  `coupled_gravity_record_stationarity_equation_derived = false`.
- The length BID does supply is conditional twice over: the `sqrt(2)` energy-convention ambiguity
  (`BID_CTP_HAMILTON_JACOBI_SCALE_BRIDGE_GATE_V001.md:89-104`, "The existing `2 sqrt(pi) t_P`
  result therefore cannot be promoted by Hamilton-Jacobi language alone"), and the undischarged
  action identification (`BID:26-27`, `:164-166` three `..._derived = false` flags).
- `_external_handoffs/.../FORBIDDEN_INPUTS.md:10` bars "cosmological endpoint, de Sitter,
  Planck-chain, or horizon calculations" from the active line, so the horizon FRAMING cannot be
  imported as authority even where the content is apt.

alpha_computed = false; proof_authorized = false; kappa_record_computed = false.
