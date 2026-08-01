# Stage 8 Held-Fixed Branch Derivability And Axiom Price

Status: APPEND-ONLY DETERMINATION / NOT AN ADOPTION

Relay: PASTE 234, CODEX LANE 1, 2026-07-31

Register head at issue: Q-94.

Custody: Q-91 applies. No git command, corpus gate, or deploy-status command is part of this
artifact's production.

Forbidden outputs not produced: alpha, kappa_record, kappa_Thomson, any coupling, scale, root,
eigenvalue, beta function, E_R, T_R, k_R, absolute interval, measured-constant comparison, or any
numerical value of kappa5, ell_P, beta, rho, or phi.

## Lead

The held-fixed branch is not derivable from the sealed corpus. It is axiom-shaped.

The corpus has one imported parent model in which `kappa5` is upstream and `ell_P` is defined from
the parent normalization and fiber extent. It also has a live reduced route that silently holds
`ell_P` fixed. It does not have a theorem choosing between those two held-fixed laws.

```text
held_fixed_branch_derived = false | TYPE-U |
  would-build: independent parent-normalization/frame law,
               derived before beta/rho/coupling evaluation,
               specifying whether kappa5 or ell_P is held fixed under R -> beta R

held_fixed_branch_axiom_shaped = true
```

This is not a preference statement. It is a pathlessness result under Q-82/Q-92: the required
parent-normalization law is named, its possible sources were checked, and no discharge route is
present.

## 1. The Fork To Be Settled

The parent KK construction writes the five-dimensional action as an explicit standard-KK import:

```text
S5[g5, matter] = (1/(2 kappa5^2)) integral_{M4 x S1} d4x dtheta sqrt(-G) R5[G]
                 + S5,matter.
```

It marks the action as a "STANDARD KK IMPORT / EXPLICIT CHOICE"
(`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:10-16`).

It then defines `ell_P` by convention:

```text
ell_P^2 := kappa5^2 / (2 pi R0).
```

and states that `ell_P` is a function of the parent normalization, the fiber period, and the
reference radius (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:30-41`).

The reduction displays the fiber factor in the four-dimensional coefficient:

```text
(2 pi R0)/(2 kappa5^2) integral d4x sqrt(-g)
  [R4[g] - (R0^2/4) F_mu_nu F^mu_nu + ...].
```

Source: `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:43-61`.

The held-fixed fork is then stated explicitly:

```text
Under R -> beta R, the reduction alone holds fixed neither kappa5 nor ell_P:
the four-dimensional EH coefficient scales with the fiber volume if kappa5 is held fixed,
while it is constant only if the parent normalization is rescaled with the fiber extent.
```

Source: `STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:63-70`.

Thus the object to derive is not a value. It is a transformation law for the parent normalization.

## 2. Candidate Derivation Sources

### 2.1 Record-cell construction

The record-cell construction does not constrain the parent gravitational normalization.

`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md` derives the local projective record bundle, comparison
connection, curvature form, and primitive comparison character. But it says connections form an
affine space and the complete action must still derive the current, state/measure, public
connection, finite response, unique induced Maxwell stiffness, exterior EM identification, matching
scale, and running (`LOCAL_PROJECTIVE_RECORD_BUNDLE_V001.md:16-43`, `:45-93`, `:94-117`).

`BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md` derives the public-record counting Hilbert
metric and composition laws, but says it does not derive a deeper action, durability dynamics, a
source pole, or alpha (`BID_PUBLIC_RECORD_HILBERTIZATION_DERIVATION_V001.md:38-63`, `:96-118`).

`BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md` records that first-opening kinematics fix a
dimensionless action interval but not an absolute duration; absolute scale closes only if the
complete parameter-free parent supplies a Lorentz-scalar equation with one isolated positive stable
solution (`BID_ABSOLUTE_RECORD_SCALE_IDENTIFIABILITY_GATE_V001.md:10-64`, `:66-90`).

These facts fix internal record structure. They do not restrict whether `kappa5` may depend on the
fiber extent, cell data, or a frame law.

```text
record_cell_constrains_parent_normalization = false | TYPE-S |
  roots: cleanroom workspace, alpha-program-archive/workspace,
         alpha-program-archive/cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git, sidecar-only hits |
  query: "parent normalization", "kappa5", "kappa_5", "ell_P", "record cell",
         "fiber volume", "4D gravitational", "Einstein-Hilbert coefficient"
```

### 2.2 Is `kappa5` constant by construction?

Within the imported parent action, `kappa5^2` is written as the coefficient inverse of the
five-dimensional Einstein-Hilbert density. That makes it a parameter of the imported action. But the
artifact also says its numerical value and relation to any microscopic theory are absent, and the
action is an explicit choice rather than a sealed consequence
(`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:12-28`).

That is enough to say how standard KK normally reads the action. It is not enough to state how the
coefficient transforms across the `R -> beta R` family of candidate geometries. The parent artifact
itself says the reduction alone holds fixed neither `kappa5` nor `ell_P` and requests an independent
normalization/frame law (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:63-73`).

```text
kappa5_fixed_by_construction = NO_VERDICT | TYPE-U |
  would-build: a parent action derivation or frame law stating that kappa5 is invariant across
               the R -> beta R family, not merely a coefficient inside one chosen action
```

### 2.3 Does a downstream R-independent 4D coefficient force the branch?

The live reduced route displays an R-independent four-dimensional Einstein-Hilbert coefficient:

```text
S_4/hbar = [1/(16 pi ell_P^2)] integral sqrt(-g)
  [R_4 - (R^2/4) F_mu_nu F^mu_nu].
```

Source: `COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:35-43`.

But this is not a derived held-fixed theorem. The held-fixed determination states that the reduced
level is stated and uniform with `ell_P` fixed, while the parent-level rule remains unstated; the
corpus has silently displayed the reduced form with `ell_P` constant and never supplied the parent
law beneath it (`STAGE8_HELD_FIXED_AND_FRAME_DETERMINATION_EINSTEIN_V001.md:54-80`,
`:138-164`, `:171-188`).

The inside/outside consistency artifact later corrected the older "ell_P never defined" claim:
`ell_P` is defined by the parent KK artifact, but only as declared, not derived; the conclusion that
an adopted held-fixed rule cannot force a number survives
(`STAGE8_INSIDE_OUTSIDE_CONSISTENCY_CONDITION_EINSTEIN_V001.md:179-185`, `:219-222`,
`:235-244`).

Therefore a downstream R-independent coefficient does not derive the branch. It is evidence that
the reduced route has chosen the `ell_P`-fixed branch.

```text
R_independent_4D_coefficient_derives_ell_P_fixed = false | TYPE-R |
  test: compare parent artifact's fork with reduced artifact's displayed coefficient;
        the displayed coefficient is the branch, not a theorem deriving it
```

### 2.4 Diffeomorphism invariance and covariance

Diffeomorphism invariance does not choose the held-fixed branch.

The modulus gate says the metric-only two-derivative parent forbids a separate tree-level `F^2` term
only under full higher-dimensional diffeomorphism invariance, but then lists the ambiguity channels:
distinguished connection, higher-curvature or localized boundary terms, record-section curvature
action, and undetermined finite matching term. It concludes that the complete parent action class,
radion stabilization, spectrum, and matching rule must be derived together
(`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:72-84`).

This covariance statement constrains admissible action terms. It does not specify the global
normalization coefficient's transformation law across the beta family. An overall
Einstein-Hilbert coefficient can be written in a diffeomorphism-invariant density on either branch.

```text
diffeomorphism_invariance_selects_held_fixed_branch = false | TYPE-S |
  roots: cleanroom workspace, alpha-program-archive/workspace,
         alpha-program-archive/cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git |
  query: "diffeomorphism", "covariance", "covariant", "parent normalization",
         "kappa5", "ell_P", "held fixed", "fiber volume"
```

### 2.5 Fiber as the record cell's internal direction

The special record-cell nature of the fiber does not derive the branch.

It actually weakens direct import of the textbook reading. The modulus gate states that the canonical
Hopf fiber of a normalized qubit is its common phase, while the active endpoint-preserving
relative-phase `U(1)_rel` is not automatically that canonical principal fiber. A free
relative-phase lift and physical metric require additional structure
(`COUPLED_RECORD_BUNDLE_MODULUS_GATE_V002.md:3-13`).

The cross-sector metric spec says prior work names the gap but does not derive the rule converting
internal/projective geometry to dimensional spacetime length; the target is beta or an equivalent
length map, and the spec itself does not derive or choose beta
(`STAGE8_CROSS_SECTOR_METRIC_RULE_ADMISSIBILITY_SPEC_V001.md:15-69`, `:71-103`).

So the fact that the fiber is a record-cell internal direction is physically relevant, but it does
not determine `kappa5` vs `ell_P`. It says more structure is needed before either branch can be
called the record-cell theorem.

```text
record_internal_fiber_selects_branch = false | TYPE-S |
  roots: cleanroom workspace, alpha-program-archive/workspace,
         alpha-program-archive/cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git |
  query: "Hopf fiber", "relative U1", "cross-sector metric", "dimensional conversion",
         "fiber metric", "R = beta", "ell_P"
```

## 3. Derivability Verdict

No derivation is available.

The strongest affirmative route would be:

```text
standard KK import -> kappa5 is parent-normalization parameter -> hold kappa5 fixed.
```

But that route stops at "standard import." It is valid inside the imported parent model and not a
derived law of the record-cell construction. The parent artifact itself marks the action and
definition as imported/declared and says the held-fixed rule still requires an independent
normalization/frame law.

The strongest preserving route would be:

```text
live reduced route displays R-independent 4D EH coefficient -> ell_P fixed.
```

But that route is circular. It identifies the branch currently used by the reduced expression and
then treats that expression as proving the branch. The parent artifact explicitly blocks that move:
defining `ell_P` cannot answer the held-fixed question without circularity because the definition
precedes the scaling test (`STAGE8_PARENT_KK_ACTION_ELL_P_DEFINITION_AND_REDUCTION_V001.md:63-70`).

Therefore:

```text
held_fixed_branch_derivable_now = false | TYPE-U |
  would-build: parent-normalization/frame theorem that is independent of preserving beta2,
               independent of current reduced-route practice, and derived before response
               or geometric-route evaluation
```

## 4. Branch Prices

### 4.1 Adopt `kappa5` fixed

What it makes true:

```text
kappa5 is the fixed parent gravitational normalization across R -> beta R.
ell_P depends on fiber extent through ell_P^2 = kappa5^2/(2 pi R0).
This matches the standard KK reading inside the imported parent model.
```

What it makes false:

```text
The branch-free statement "K_KK changes by beta^2" is false.
The fixed-ell_P radion coordinate phi = ln(R/ell_P) is not the same shift coordinate.
rho = R_*/ell_P is no longer a ratio to a fixed denominator.
```

What must be retyped branch-conditional:

```text
beta^2 obstruction
phi = ln(R/ell_P) shift-symmetry diagnosis
rho = R_*/ell_P
radion potential screens using fixed ell_P
positive/negative power classification written in fixed-ell_P coordinates
inside/outside consistency conditions consuming ell_P/(c Delta tau)
```

Cost:

This branch contradicts the live reduced route's silent practice. It does not by itself select beta,
rho, a coupling, or a value. It forces a re-examination of the geometric route's existing weights.

### 4.2 Adopt `ell_P` fixed

What it makes true:

```text
The reduced route's old K_KK -> beta^2 K_KK statement survives.
phi = ln(R/ell_P) shifts by ln beta.
rho = R_*/ell_P remains a ratio to a fixed denominator.
```

What it makes false or costly:

```text
kappa5 is not fixed across the R -> beta R family.
The parent normalization must scale with fiber extent.
The imported standard-KK parent model is no longer one fixed-normalization parent across beta.
```

What must be supplied but is absent:

```text
parent_normalization_scaling_law_derived = false | TYPE-U |
  would-build: theorem proving kappa5^2 rescales with fiber extent while ell_P stays fixed
```

Cost:

This branch preserves the live reduced route and the `beta^2` diagnosis, but it does so by adopting
an underived parent-normalization scaling law. Complete-parent-action uniqueness then must include
that law rather than inheriting it silently.

## 5. Disclosure Required On Any Geometric-Route Number

If a number is ever computed on the geometric route before the branch law is derived, it must travel
with an explicit branch conditionality:

```text
GEOMETRIC_ROUTE_HELD_FIXED_BRANCH_CONDITIONALITY:
  The result is conditional on adopting [KAPPA5_FIXED] or [ELL_P_FIXED] as the parent-normalization
  law under R -> beta R.

If KAPPA5_FIXED:
  the previous beta^2, fixed-ell_P phi, fixed-denominator rho, and fixed-ell_P radion screens do
  not apply as written.

If ELL_P_FIXED:
  the result assumes an underived scaling of the parent normalization with fiber extent; the
  beta^2 sentence and fixed-ell_P radion language survive only under that adoption.
```

The disclosure is not optional bookkeeping. It is part of the value path because the held-fixed law
sits beneath the beta diagnosis, both sides of the radion potential, rho, and every weight downstream
of `K_KK`.

## 6. Typed Summary

```text
parent_normalization_frame_law_derived = false | TYPE-U |
  would-build: independent theorem choosing kappa5-fixed or ell_P-fixed under R -> beta R

kappa5_fixed_forced_by_standard_KK = false | TYPE-C |
  constraint: standard KK applies only as imported parent-model reading, not record-cell theorem

ell_P_fixed_forced_by_reduced_coefficient = false | TYPE-R |
  test: reduced coefficient is the branch display; parent reduction says it requires rescaling
        parent normalization

diffeomorphism_invariance_forces_branch = false | TYPE-S |
  roots: cleanroom workspace, archive workspace, cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git |
  query: "diffeomorphism", "covariance", "parent normalization", "kappa5", "ell_P",
         "fiber volume", "held fixed"

record_cell_internal_fiber_forces_branch = false | TYPE-S |
  roots: cleanroom workspace, archive workspace, cleanroom_output, alpha_supervision |
  exclusions: a32_holdout/custodian_private, .git |
  query: "record cell", "Hopf fiber", "relative U1", "fiber metric",
         "dimensional conversion", "cross-sector metric"

held_fixed_branch_axiom_shaped = true
```

## 7. Search Scope

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
parent normalization
kappa5
kappa_5
ell_P
G_5
M_5
ell_5
five-dimensional Newton
5D Newton
4D gravitational
Einstein-Hilbert coefficient
fiber volume
2 pi R
circumference
held fixed
diffeomorphism
covariance
Einstein frame
Jordan
Weyl
record cell
Hopf fiber
relative U1
dimensional conversion
cross-sector metric
```

The sweep found declared/imported parent structure and reduced-route usage. It did not find a
derived parent-normalization/frame law.

