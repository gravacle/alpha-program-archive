# T7(ii) H-ANGLE Attempt Result - Obstruction Named V001

Date: 2026-07-28

## Status

```text
LANE ATTEMPT RESULT.
Attempted target: H-ANGLE, a uniform Friedrichs-angle lower bound between
consecutive per-cell ranges, proved from parent acts.

Result: DOES NOT CLOSE.
Obstruction named. Nothing adopted. Nothing repaired in place.

alpha_computed = false
proof_authorized = false
production_authorized = false
```

## Authorities Read

```text
2c4eb207872cfb7d497a83ea134cee5cd1bb8fe244f8c5b5798d8841186d0398  EINSTEIN_HANDOFF_2026-07-28.md
0f76ab73d7b226899ad00e24a0be10636b49982620375bd10491b898ecc917c7  STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md
34e35b63fc41a3350322e5ee641dcd8b5e96155b536355962816260f510d4c96  STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_ERRATUM_001_IDEMPOTENCE_CORRECTION.md
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
f3b2259aa5200c63385ff452507e9f258e8ed0dd1a7d9b41eae66c8e37197390  STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md
48d0b88a6333f2c8eb7f1bd1647e67e08ecc25963c54f4a2ef055e878532ff86  STAGE8_COMPLETE_QSPEC_ZERO_FREE_NOT_T7II_DEAD_END_RECORD_V001.md
```

## What H-ANGLE Would Have To Supply

The T7(ii) attempt names:

```text
H-ANGLE = uniform Friedrichs-angle lower bound between consecutive per-cell ranges.
```

As used there, it is meant to remove the GHZ-like degeneracy obstruction: the transfer-gap route
needs a simple leading mode with a uniform gap. Assuming decay or clustering would trip F'-1; a
parent-derived angle theorem would instead be a property of a defined operator from which decay
could follow.

Therefore the first requirement is not a bound. It is typing:

```text
which closed subspaces are the "consecutive per-cell ranges"?
```

Without that object, a Friedrichs-angle statement has no subject.

## Sharp-Indicator Check First

The handoff warning requires checking the sharp-indicator disease before any obligation mentioning
`M(t)` or a projection.

The sealed E1 successor definition is:

```text
M(t) = Q 1_{|x| <= r(t)} Q
```

with sharp `1_{D_t}` frozen and not softenable by a lane. The collar charter records Defect A:

```text
the corpus displays M(t) both with and without Q
```

and says multiple load-bearing places reason as though `M(t)` were a bare sharp indicator, including
"on the ball where M(t) = 1".

At finite Hermite-Galerkin carrier, that sharp-indicator reading is unavailable. For any nonzero
finite Hermite vector `f`, real analyticity prevents `f` from vanishing on a nonempty open set.
Hence for a nonempty cell slice `D_t` with nonempty complement in the carrier's spatial domain:

```text
<f, Q 1_{D_t} Q f> = integral_{D_t} |f(x)|^2 dx > 0
<f, Q (1 - 1_{D_t}) Q f> > 0
```

on `ran(Q)`. Thus `Q 1_{D_t} Q` has no zero eigenvalue and no one eigenvalue on the finite carrier.
Its range is all of `ran(Q)`. The same holds for every nonempty admitted cell slice.

So if H-ANGLE's "per-cell ranges" are the ranges of the sealed localizers `M_c(t)`, then:

```text
range(M_c(t)) = ran(Q) = range(M_{c+1}(t'))
```

for the finite carrier. The Friedrichs angle between identical full ranges is zero, or degenerate
under conventions that quotient out the full intersection. Either way it supplies no uniform
positive separation and no transfer gap.

This is not a numerical weakness. It follows from the sealed Q-compressed sharp localizer plus the
analyticity of the finite Hermite carrier.

## Corrected Zero-History Kraus Candidate

The idempotence erratum corrected the zero-history in-cell Kraus operator:

```text
sum_lambda w_lambda R_lambda = cos^2(8 pi rho^4) * I
```

so the zero-history candidate is not the odd-parity projector `Pi_odd`. It is a scalar multiple of
the identity, except at special radii where the scalar is 0 or 1.

Therefore, if H-ANGLE's "per-cell ranges" are the ranges of the corrected zero-history in-cell
Kraus operators, then generically:

```text
range(cos^2(8 pi rho^4) * I) = full carrier
```

and at scalar-zero radii the range collapses to the zero subspace. Neither case supplies the required
uniform positive angle between consecutive per-cell ranges. Full-vs-full gives zero angle; zero
events are exceptional and cannot be the uniform gap mechanism.

## Other Candidate Range Objects

Three other readings were considered and do not close the attempt:

```text
1. Bare continuum sharp-indicator ranges:
   These ignore the sealed Q in M(t) and run directly into the reported-not-repaired Defect A.

2. Spectral subspaces of Q 1_D Q selected by a threshold:
   No threshold, spectral cut, or tail rule is sealed. Such a rule would introduce a new object and
   likely a carrier-dependent constant, so it cannot be silently treated as parent-derived H-ANGLE.

3. Ranges of an unspecified transfer-map component T_c:
   Lemma 0 supplies the product representation, but H-ANGLE does not define which component's
   range is meant. H-GAP and H-PREP remain separate named hypotheses. Selecting a component or
   preparation here would be construction, not derivation from parent acts.
```

## Obstruction

```text
OBSTRUCTION: H_ANGLE_RANGE_OBJECT_UNDEFINED_AND_NATURAL_PARENT_CANDIDATES_COLLAPSE

Location:
  STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_V001.md:105-106 names H-ANGLE but not its range object.
  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:465-470 seals M(t) = Q 1_D Q and forbids softening.
  STAGE8_COLLAR_CONJUNCTION_CHARTER_RESULT_V001.md:152-158 records Defect A: M(t) is displayed
    both with and without Q, while load-bearing reasoning treats it as a bare sharp indicator.
  STAGE8_T7II_ATTEMPT_RESULT_OBSTRUCTION_NAMED_ERRATUM_001_IDEMPOTENCE_CORRECTION.md:36-45
    corrects the zero-history Kraus operator to a scalar multiple of I, not a projector.
```

The attempt cannot prove a uniform positive Friedrichs-angle lower bound from parent acts because
the parent-act-visible range candidates do not carry separated ranges:

```text
Q 1_D Q candidate: full range on ran(Q), hence zero/degenerate angle.
zero-history Kraus candidate: scalar identity, hence full range generically.
bare 1_D candidate: not the sealed object once Q is in force.
spectral-cut candidate: unsealed new object.
transfer-component candidate: untyped by H-ANGLE as written.
```

## Object-vs-Bound Discipline

This is a failed attempt against the currently named H-ANGLE route. It is not a theorem that no
future angle theorem can exist. A future route would first need to seal the actual range object and
show that it is:

```text
1. derived from parent acts, not assumed as clustering or decay;
2. compatible with the Q-compressed sharp localizer;
3. not a thresholded carrier-dependent spectral cut unless F'-5 is addressed;
4. strong enough to produce the simple leading mode/gap T7(ii) needs.
```

## Protected Status

```text
H_ANGLE_attempt_closes = false
obstruction_named = H_ANGLE_RANGE_OBJECT_UNDEFINED_AND_NATURAL_PARENT_CANDIDATES_COLLAPSE
sharp_indicator_disease_checked_first = true
M_t_Q_compressed_candidate_supplies_positive_angle = false
zero_history_scalar_Kraus_candidate_supplies_positive_angle = false
bare_indicator_candidate_is_sealed_object = false
spectral_cut_candidate_sealed = false
transfer_component_range_object_sealed = false
T7ii_zero_free_neighbourhood = false
alpha_computed = false
proof_authorized = false
```
