# R-L4 / C-L4 Rebuild Charter And Balance Result V001

Date: 2026-07-28

Status: construction-lane rebuild charter and exact colour-weight balance
result after C-L1 withdrawal. This artifact does not discharge R-L4a,
R-L4b, R-L4, H-B, or H-B0. It supplies the corrected input and the exact
replacement balance over the real partition.

Authorities:

```text
468467303a109dc825b015107897dacc107800fc981030377c3f006b384cccb5  STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md
efb08860b888e24acaa50fdafdbe4afdb868450f79ec23120c2bd3eb1d40ddbb  STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md
789338adb7d3d36da453113e98f371a4f92543cf2652b047f8481c407bed5bc3  STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md
```

Fence statement:

```text
F'-1 observed: no decay, clustering, preparation, or independence hypothesis is assumed.
F'-5 observed: the exact colour-weight arithmetic below is not a carrier-indexed bound constant.
R-9 observed: kappa_bal is a baseline balance symbol and is NOT kappa_record.
alpha_computed = false
proof_authorized = false
```

## 1. What C-L1 Withdrew

`STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:746-752` supplied the old
two-sector pair structure:

```text
V_{mu lambda}(0) - 1 = (phase_mu * phase_lambda - 1) P
same-phase pair weight total     = 1/2
opposite-phase pair weight total = -1/2 signed, 1/2 absolute
```

`STAGE8_CL1_ATTEMPT_RESULT_REFUTED_V001.md` withdraws that supply. Its
replacement, with `n := (lambda-mu)/sqrt2`, is:

```text
V_{mu lambda}(0) =
  (-1)^n [ cos(n theta) I + i sin(n theta) S ]   on rho <= 1/2,
  I                                             beyond,
theta = 16 pi rho^4.
```

The old "same-phase / opposite-phase" split is not a partition of the actual
object. The actual partition is by `n in {-2,-1,0,1,2}`.

## 2. Exact Real Partition

The sealed pointer weights are, for `lambda/sqrt2 in {-1,0,+1}`:

```text
w_- = -1/4,  w_0 = 1/2,  w_+ = -1/4.
```

Summing pair weights by `n = lambda/sqrt2 - mu/sqrt2` gives:

```text
n = -2: signed total =  1/16, absolute total = 1/16
n = -1: signed total = -1/4,  absolute total = 1/4
n =  0: signed total =  3/8,  absolute total = 3/8
n = +1: signed total = -1/4,  absolute total = 1/4
n = +2: signed total =  1/16, absolute total = 1/16

all classes: signed total = 0, absolute total = 1.
```

The only class with `V_{mu lambda}(0)=I` identically is `n=0`.

Therefore the replacement balance over the corrected surviving class is:

```text
kappa_bal = (absolute n=0 total) / |signed n=0 total|
          = (3/8) / (3/8)
          = 1.
```

This is not the old derivation. The old value `1 = (1/2)/(1/2)` was computed
over a false partition. The replacement value is `1 = (3/8)/(3/8)` over the
actual `n=0` surviving class.

## 3. Corrected Nonzero-Class Targets

For `n = +/-1`:

```text
V_n(0) - I = -2 cos(8 pi rho^4) exp(+/- i 8 pi rho^4 S)
```

on `rho <= 1/2`, and zero beyond. This is the replacement for the old
opposite-phase target `-2P`.

For `n = +/-2`:

```text
V_n(0) - I = +/- 2 i sin(16 pi rho^4) exp(+/- i 16 pi rho^4 S) S
```

on `rho <= 1/2`, and zero beyond. This is the class the old same-phase
"surviving" sector incorrectly treated as `V(0)=I`.

Neither nonzero-class target is a multiple of the old sharp projector `P`.

## 4. R-L4a Check

R-L4a's corrected qualitative conclusion survives this rebuild as an
obligation target, not as a certified theorem of this artifact.

Reason: `STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md:353-368` locates the
fatal obstruction at the volume diagonal `x = y`, not at the sharp boundary.
The corrected nonzero-class profiles soften boundary behaviour, but each
nonzero class is nonzero on a positive-volume subset of the causal ball. A
boundary-softened profile therefore does not by itself make the baseline
perturbation trace-class or give a Fredholm determinant.

Thus the corrected R-L4a wording remains:

```text
D is undefined as a Fredholm determinant, not D = 0,
unless an explicitly named regularization proves a different statement.
```

This artifact does not supply that regularization and does not assign a value
to any nonzero-class determinant.

## 5. Rebuilt Charter

R-L4 / C-L4 must now be rebuilt as follows:

```text
R-L4a:
  For each nonzero class n in {-2,-1,+1,+2}, establish existence or
  non-existence of det(1 + C(V_n(0)-I)C), naming the regularization if any.
  The unregularized Fredholm determinant target is "undefined", not "0",
  at the C6 volume-diagonal obstruction.

R-L4b:
  Replace the old opposite-phase target -2P by the n=+/-1 target above.
  Also treat the n=+/-2 class as non-surviving unless a separate determinant
  statement proves otherwise. The old same-phase surviving-sector claim is
  unavailable.

R-L4:
  Perform baseline bookkeeping by n-class, not by same-phase/opposite-phase.
  If R-L4a/R-L4b exclude the nonzero classes, the corrected surviving balance
  is kappa_bal = 1 by (3/8)/(3/8), never by (1/2)/(1/2).
```

## 6. Flags

```text
C_L1_pair_structure_supply_withdrawn = true
replacement_partition = "n = (lambda-mu)/sqrt2 in {-2,-1,0,1,2}"
old_same_opposite_partition_valid = false
old_kappa_bal_derivation_valid = false
kappa_bal_replacement_value_over_corrected_surviving_class = 1
kappa_bal_replacement_source = "(3/8)/(3/8), not (1/2)/(1/2)"
baseline_determinant_existence_certified = false
opposite_phase_sector_vanishing_certified = false
baseline_collapse_certified = false
nonzero_class_regularization_supplied = false
R_L4a_unregularized_target = "D undefined, not D = 0"
alpha_computed = false
proof_authorized = false
```
