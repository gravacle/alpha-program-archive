# Stage 8 Gamma_K Quasifree Root Route Attempt v001

Date: 2026-07-30

Status: APPEND-ONLY CONSTRUCTION ATTEMPT / SOURCE-QUASIFREE GNS CONSTRUCTED / ROOT PRODUCER NOT DERIVED.

Subject:
`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md`

Prior root attempt:
`STAGE8_GAMMA_K_ROOT_PRODUCER_ATTEMPT_F_RP1_V001.md`

## Fences

This attempt does not touch slot 16, Thomson matching, slot 18, A32, or
comparator artifacts. It does not read `a32_holdout/custodian_private/`. It
does not solve for `K_*`, evaluate a response, run the mutation audit, compute
C-L3, or use the withdrawn finite-rank Galerkin route.

Protected status:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## Hypothesis Tested

The root-producer falsifier F-RP1 may have fired against the wrong target. The
withdrawn construction in
`STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md` was the
finite-rank commuting family:

```text
[Q_n,h_0]=0;
Q_n -> I strongly.
```

That family is impossible for the free massless Dirac multiplier. The same
correction, however, preserves:

```text
continuum_covariance_formula_derived = true
momentum_block_covariance_regression_valid = true
genuine_finite_rank_continuum_restriction_constructed = false
parent_state_regulator_restriction_derived = false
```

The route tested here is therefore:

```text
continuum covariance C
  -> source CAR quasifree state
  -> source-sector GNS representation
  -> ask whether this is the completed Section-1 root producer.
```

No additional premise beyond the current stack is declared. Standard CAR and
quasifree/GNS use is already disclosed by the source-CAR and record-GNS
authorities cited below.

## 1. Quotation Check

The first quotation is verified. In
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md:228-231`:

```text
The asymptotic quasifree state is fixed by the positive/negative spectral
projectors of the same h_0. A finite-energy incoming source excitation may
vary as physical boundary data, but every durability theorem used for
promotion must hold for the complete declared class, not for one
outcome-selected profile.
```

The second quotation is verified. In
`STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_SPEC_V001.md:65-67`:

```text
The finite quasifree state is the CAR restriction determined by C_n.
It is inherited from the continuum state rather than selected from the
spectrum of a later finite toy Hamiltonian.
```

The same spec also says at
`STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_SPEC_V001.md:36-39` that the
continuum covariance is unambiguous on `L2(R^3;C^4)` because the `p=0` set has
Lebesgue measure zero.

Determination:

```text
quotation_check_passed = true
covariance_determines_source_quasifree_state_in_this_corpus = true
withdrawn_finite_rank_route_not_needed_for_the_continuum_source_state = true
```

This does not yet say that the resulting state is the full `rho_pre` required
by Section 1.

## 2. Source One-Particle Space, CAR Algebra, And GNS Construction

The source one-particle carrier is available from sealed/disclosed material.
`BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md:65-98` constructs the
positive Cauchy-data Hilbert space `H_q` from the hypersurface form and states
that completion gives the one-solution Hilbert space. Lines 102-144 then use
the stationary exterior spectral projectors and standard CAR quantization to
produce the fermionic source carrier.

For the flat source-free branch, the continuum parent result states at
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md:109-124`:

```text
h_0(p)=alpha_D dot p;
h_0(p)^2=|p|^2 I.
```

and identifies `L2(R^3;C^4)` as the source space with absolutely continuous
source spectrum and no source point spectrum.

Define, for `p != 0`,

```text
C(p) = (I - h_0(p)/|p|)/2.
```

At `p=0`, choose any representative; the multiplication operator on
`L2(R^3;C^4)` is unchanged because that set has measure zero. Then `C` is an
orthogonal projection with `0 <= C <= I`.

Let `A_src = CAR(H_src)` be the source CAR algebra, with
`H_src = L2(R^3;C^4)` in the flat branch or equivalently the stationary
one-solution Hilbert space representation supplied by the Cauchy-data
construction. The gauge-invariant quasifree state `omega_C` is determined by:

```text
omega_C(a^*(f)a(g)) = <g, C f>;
omega_C(a(f)a(g))   = 0;
omega_C(a^*(f)a^*(g)) = 0;
```

with odd monomials zero and even monomials given by the standard CAR
quasifree determinant/Pfaffian rule. The standard GNS theorem then gives:

```text
(pi_C, H_C, Omega_C).
```

This is not an invented finite-rank approximation. It is the continuum
source-sector quasifree representation determined by the sealed covariance.
It is the same type of standard GNS move used for completed records in
`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:65-70`, where compatible
states define a C-star state and the GNS theorem supplies the representation.

Determination:

```text
source_CAR_quasifree_state_constructed_from_covariance = true
source_sector_GNS_constructed = true
old_commuting_finite_rank_Qn_route_used = false
```

## 3. Type Check Against Section 1

The source-sector construction does not yield the completed algebra demanded
by Section 1.

`STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md:144-170` consumes
`primitive_record_cell_selection_principle_v004.md` and requires a positive
trace-class `rho_pre` on the full source-record-field Hilbert space, the
gauge-fixed physical quotient, a compound CTP/field/spacetime index, the
oriented CTP branch metric, and invariant spacetime measure. The same section
lists seven objects that must be derived before execution:

```text
complete S_CTP;
full source-record-field Hilbert space and rho_pre;
nonzero differentiable Log_0 neighborhood;
gauge-fixed physical quotient;
invariant spacetime/contour measure;
CTP branch metric, reality condition, and index ordering;
physical Dyson kernel obtained from the raw contour correlator.
```

The source CAR construction supplies only:

```text
source one-particle Hilbert space;
source CAR algebra;
source quasifree state;
source-sector GNS representation.
```

It does not include record factors, gauge/gravity field degrees of freedom,
the CTP quotient, the invariant measure, `S_CTP`, record effects, or the
raw-correlator-to-physical-Dyson map.

The adjacent completed-record result is also separately scoped. It derives an
outgoing record GNS, but
`R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md:157-183` says it does not
establish a projective limit of full source-record states or a complete
source-inclusive GNS. Likewise,
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md:126-142` withholds
the strongest complete-parent verdict because source-inclusive finite-state
convergence, an infinite-future Moller limit, and regulator independence of
the full limit remain unproved.

Determination:

```text
completed_section_1_algebra_derived = false
source_quasifree_GNS_is_the_completed_source_record_field_Hilbert_space = false
failure_step = STEP_3_DIFFERENT_ALGEBRA
```

This is the load-bearing failure. The covariance route rescues a real source
state, but not the completed root producer.

## 4. `rho_pre` And Allow/Require

The allow/require threshold does not select `rho_pre`.

`STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md:31-47` splits the
allow/require constraint from local minimality and saturation moves. It records
allow/require as a cell/support constraint, not as a standalone selector. Lines
49-55 further record that the physical threshold rule refuses automatic
denominator selection.

The parent spec also permits variation of physical incoming source data:
`R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md:228-232` states that
a finite-energy incoming source excitation may vary as physical boundary data
and that promotion must hold for the complete declared class, not one selected
profile.

Therefore the threshold can say what kind of pre-record state is required for
a durable public record test. It does not choose a unique state on the full
source-record-field algebra, and it does not turn the source-sector
quasifree vacuum into the full `rho_pre`.

Determination:

```text
allow_require_selects_rho_pre = false
allow_require_constrains_rho_pre_role = true
rho_pre_on_completed_algebra_identified = false
```

## 5. Quotient, Measure, And Record-Effect Family

These do not follow from the source quasifree GNS construction.

`primitive_record_cell_selection_principle_v004.md:17-35` requires the
gauge-fixed physical quotient, compound index, CTP metric, and invariant
spacetime measure. Lines 57-69 state that the 2PI identity is abstract on a
fixed nondegenerate gauge-fixed physical quotient, and that the quotient,
contour measure, nonzero differentiable source neighborhood, `i epsilon`
prescription, and raw-correlator-to-physical map remain Step-5 obligations.

`primitive_complete_boundary_transition_functional_principle_v002.md:18-29`
uses `rho_pre`, `U_BR`, and record effects `E_r` in the complete history
functional, while its hard gates at lines 106-118 require `U_BR`, `rho_pre`,
every admitted record effect, and their domains to follow from one complete
microscopic operator.

The source CAR construction does not derive those objects. It can be a source
input to a future completed producer, but it cannot replace the producer.

Determination:

```text
gauge_fixed_physical_quotient_derived_by_this_route = false
invariant_spacetime_contour_measure_derived_by_this_route = false
record_effect_family_derived_by_this_route = false
```

## Verdict

```text
ROOT_DERIVED = false
PRODUCER_FLAG_FLIPPED = false
SOURCE_QUASIFREE_GNS_DERIVED = true
FAILURE_STEP = STEP_3_DIFFERENT_ALGEBRA
SECONDARY_FAILURE = ALLOW_REQUIRE_CONSTRAINS_BUT_DOES_NOT_SELECT_RHO_PRE
F_RP1_STANDS_NARROWED = true
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

Plain-language outcome: the hypothesis survives the first check and produces
a legitimate source-sector quasifree GNS representation without the withdrawn
finite-rank route. It fails as a root producer because Section 1 needs a full
source-record-field CTP algebra and selected `rho_pre`, not only the source
CAR vacuum/polarization.

## Search Scope And File List

Roots inspected:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha_supervision
```

Excluded:

```text
**/a32_holdout/custodian_private/**
slot 16
Thomson matching
slot 18
A32
comparator artifacts
```

Primary files read:

```text
/Users/bgm/.codex/attachments/08f89150-bdc2-4360-830b-c59ff6660a21/pasted-text.txt
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_CONSTRUCTION_SPEC_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_CONSTRUCTION_SPEC_AMENDMENT_001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_ROOT_PRODUCER_ATTEMPT_F_RP1_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_GAMMA_K_Q22_Q38_RULING_COVERAGE_PASS_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_SPEC_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_T7_CONTINUUM_GALERKIN_PROVENANCE_CORRECTION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_RESULT_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_FULL_DIRAC_CAR_SOURCE_TYPING_DERIVATION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_FREE_QUASIFREE_CTP_PROPAGATOR_DERIVATION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/R3_4_PARENT_STATE_COVARIANCE_ADJUDICATION_RESULT_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003/STAGE8_ALLOW_REQUIRE_MINIMALITY_SPLIT_CORRECTION_V001.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_record_cell_selection_principle_v004.md
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/primitive_complete_boundary_transition_functional_principle_v002.md
```
