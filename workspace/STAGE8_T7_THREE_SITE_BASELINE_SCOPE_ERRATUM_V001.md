# Stage-8 T7 Three-Site Baseline Scope Erratum v001

Date: 2026-07-24

## Correction

The following sealed calculations are algebraically and numerically valid:

```text
STAGE8_T7_FINITE_FOCK_COMPLETED_RECORD_AMPLITUDE_RESULT_V001.md
STAGE8_T7_GAUSSIAN_PATH_SUM_REDUCTION_RESULT_V001.md
```

They use the nonzero spectral subspace of the old three-site periodic
operator regression. That regression was expressly excluded as the
physical state regulator by:

```text
STAGE8_T7_PARENT_STATE_REGULATOR_RESTRICTION_RESULT_V001.md.
```

No existing theorem identifies its eight nonzero eigenvectors with one of
the nested continuum restrictions `Q_n C Q_n`. The phrases "inherited
finite quasifree state" and "same inherited regulator" in the two later
specifications therefore overstate provenance.

## Retained result

The three-site calculations establish:

```text
the exact CAR fixed-number construction;
the nonzero one- and two-cell toy-regulator amplitudes;
the exclusion of one single-Gamma determinant shortcut; and
the exact signed Gaussian record-history formula.
```

The history formula is representation-theoretic and remains valid for every
finite parent satisfying its stated hypotheses.

## Withdrawn inference

The three-site values may not be used as:

```text
a member of the physical continuum exhaustion;
evidence of continuum-regulator convergence;
the primitive T7 amplitude;
an all-volume nonzero-baseline result;
or evidence for the zero-free/cluster thermodynamic gates.
```

The next admissible calculation must construct the causal-cell
multiplication operators and propagators on a genuinely nested restriction
of the continuum one-particle space. Until then:

```text
physical_regulator_completed_record_baseline_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
