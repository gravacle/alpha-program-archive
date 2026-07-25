# R3.4 Regulator-Scheme and Ray-Sufficiency Result v001

## Verdict

```text
DECAY_CLASS_ROBUST_ALGEBRA_DERIVED_SPECTRAL_DYNAMICS_OPEN
```

The three discrete regulators share the exact late-time return-probability
class `t^-3`. This supports decay-class robustness. It does not establish
full spectral-measure or response equivalence.

The finite registration-counting ray also has the previously derived
quasi-local state home. That result fixes the outgoing public-record algebra
and its labels, but it does not fix the algebra's generator or spectral
measure.

## Exact regulator comparison

Closed-walk counting gives:

| regulator | `m2` | `m4` | `m6` | `m4/m2^2` | `m6/m2^3` |
|---|---:|---:|---:|---:|---:|
| half-line | 1 | 2 | 5 | 2 | 5 |
| radial tree | 3 | 18 | 135 | 2 | 5 |
| cubic lattice | 6 | 90 | 1860 | 5/2 | 155/18 |

The half-line and radial-tree measures are related by the already displayed
energy rescaling. The cubic-lattice root measure is not related to them by
one energy rescaling, because its scale-invariant moments differ.

The common decay class follows independently:

```text
J_1(2t)/t       = O(t^-3/2) in amplitude;
tree rescaling  preserves that exponent;
J_0(2t)^3       = O(t^-3/2) in amplitude.
```

All three therefore have return probability `O(t^-3)`, despite not sharing
one full measure.

## Consequence of the covector-ray lift

Countably many finite record factors produce the same abstract quasi-local
UHF algebra and the same product-label-state construction. The regulator
generators are different local automorphism choices on such record systems,
and the exact moment calculation shows that their root measures differ.

Therefore:

```text
outgoing algebra plus public-label state != outgoing generator;
outgoing algebra plus public-label state != root spectral measure.
```

The covector-ray theorem remains a real result: it closes the
outgoing-record-algebra obligation. The spectral dynamics must be supplied
by the complete microscopic parent action.

## Dependency consequence

The continuum waist-root calculation cannot be promoted merely because its
density is normalized and decays. Its physical root, generator, and
preparation map must descend from the same complete parent action that fixes
the connected write dynamics.

The next proof target is therefore not another freely selected density. It
is the parent-to-outgoing-dynamics map.

## Status

```text
three_regulators_share_t_minus_3_probability_class = true
three_regulators_have_one_common_full_measure = false
decay_class_robustness_supported = true
outgoing_record_algebra_subobligation_closed = true
covector_ray_and_quasilocal_state_fix_generator = false
covector_ray_and_quasilocal_state_fix_spectral_measure = false
spectral_dynamics_must_come_from_complete_parent_action = true
unique_covariant_spectral_measure_derived = false
hypothesis_promoted_to_principle = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
