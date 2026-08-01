# Stage 8 V011 Composition-Loop Matrix Experiment Result v001

Date: 2026-08-01
Lane: CODEX 1
Register head at issue: Paste 271

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
coupling_evaluation_authorized = false
production_authorized = false
```

## Scope and authorization

This artifact executes only the matrix experiment authorized by
`DECISION_OF_RECORD_004` as relayed in Paste 271. The lifted fence applies only
to `B_square(Phi)` over `C_0(K_square) direct-sum C_1(K_square)` at the frozen
evaluation point `Phi = pi`.

The six permitted outputs are:

```text
1. p_Phi(z) = det(z I_8 - B_square(Phi))
2. the eight real eigenvalues in nondecreasing order, with multiplicity
3. the exact kernel multiplicity
4. Tr[B_square^2] over the full eight-dimensional carrier
5. Tr[B_square^4] over the full eight-dimensional carrier
6. R_square = Tr[B_square^4] / Tr[B_square^2]^2
```

No alpha, `kappa_record`, `kappa_Thomson`, coupling, scale, root of
`C_record`, beta function, `E_R`, `T_R`, `k_R`, or absolute interval is
computed. No comparison to any measured constant is made. No result modifies
BID. Computing this spectrum is not the same act as sealing the prediction.

V011 itself declares the standing of this computation:

```text
This is a new forward mathematical consequence, not an empirical holdout.
It remains target-aware because the broader program knows its desired
structures.
```

## Source object

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1945` specifies the
composition-loop prediction.

The unfilled oriented `1`-skeleton `K_square` has vertices

```text
v_00, v_10, v_01, v_11
```

and edges

```text
e_a0: v_00 -> v_10
e_0b: v_00 -> v_01
e_ab: v_10 -> v_11
e_ba: v_01 -> v_11
```

The ordered loop holonomy is

```text
u_ab u_a0 (u_ba u_0b)^(-1) = exp(i Phi).
```

The fixed gauge is

```text
u_a0 = 1
u_ab = 1
u_0b = 1
u_ba = exp(-i Phi)
```

and the preregistered point is exactly

```text
Phi = pi
exp(-i Phi) = -1
```

`BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1881-1894` requires the Hilbert
forms produced by Gate 3 and no filled `2`-cell in the trace carrier.
`cleanroom_output/38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md:8-33` records that
Gate 3 forces identity fiber forms and a canonical normalized transition
operator modulo overall congruence.

With the frozen ordered bases

```text
C_0: (v_00, v_10, v_01, v_11)
C_1: (e_a0, e_0b, e_ab, e_ba)
```

the evaluated incidence matrix is

```text
D_square(pi) =
[[-1, -1,  0,  0],
 [ 1,  0, -1,  0],
 [ 0,  1,  0, -1],
 [ 0,  0,  1, -1]]
```

and

```text
B_square(pi) =
[[ 0,  0,  0,  0, -1, -1,  0,  0],
 [ 0,  0,  0,  0,  1,  0, -1,  0],
 [ 0,  0,  0,  0,  0,  1,  0, -1],
 [ 0,  0,  0,  0,  0,  0,  1, -1],
 [-1,  1,  0,  0,  0,  0,  0,  0],
 [-1,  0,  1,  0,  0,  0,  0,  0],
 [ 0, -1,  0,  1,  0,  0,  0,  0],
 [ 0,  0, -1, -1,  0,  0,  0,  0]]
```

`B_square(pi)` is real symmetric, hence Hermitian. Its bipartite block form
predicts spectrum pairing about zero; the symbolic and numerical computations
both confirm that pairing.

## Symbolic computation

The symbolic path used exact integer arithmetic. Since `B_square(pi)` has block
form

```text
B = [[0, D],
     [D^T, 0]],
```

its square is block diagonal with `D D^T` and `D^T D`. The exact intermediate
matrix is

```text
D D^T =
[[ 2, -1, -1,  0],
 [-1,  2,  0, -1],
 [-1,  0,  2,  1],
 [ 0, -1,  1,  2]]
```

The exact characteristic polynomial of `D D^T` is

```text
q(y) = y^4 - 8 y^3 + 20 y^2 - 16 y + 4
     = (y^2 - 4 y + 2)^2.
```

Therefore the exact characteristic polynomial of `B_square(pi)` is

```text
p_pi(z) = z^8 - 8 z^6 + 20 z^4 - 16 z^2 + 4
        = (z^4 - 4 z^2 + 2)^2.
```

The exact square-spectrum roots are

```text
2 - sqrt(2)    with multiplicity 2
2 + sqrt(2)    with multiplicity 2
```

Therefore the exact eigenvalues of `B_square(pi)`, in nondecreasing order with
multiplicity, are

```text
-sqrt(2 + sqrt(2))
-sqrt(2 + sqrt(2))
-sqrt(2 - sqrt(2))
-sqrt(2 - sqrt(2))
 sqrt(2 - sqrt(2))
 sqrt(2 - sqrt(2))
 sqrt(2 + sqrt(2))
 sqrt(2 + sqrt(2))
```

The exact kernel multiplicity is

```text
0
```

The exact trace outputs over the full eight-dimensional carrier are

```text
Tr[B_square(pi)^2] = 16
Tr[B_square(pi)^4] = 48
R_square = 48 / 16^2 = 3/16
```

For auditability, the exact matrix powers used for the traces are:

```text
B_square(pi)^2 =
[[ 2, -1, -1,  0,  0,  0,  0,  0],
 [-1,  2,  0, -1,  0,  0,  0,  0],
 [-1,  0,  2,  1,  0,  0,  0,  0],
 [ 0, -1,  1,  2,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  2,  1, -1,  0],
 [ 0,  0,  0,  0,  1,  2,  0, -1],
 [ 0,  0,  0,  0, -1,  0,  2, -1],
 [ 0,  0,  0,  0,  0, -1, -1,  2]]

B_square(pi)^4 =
[[ 6, -4, -4,  0,  0,  0,  0,  0],
 [-4,  6,  0, -4,  0,  0,  0,  0],
 [-4,  0,  6,  4,  0,  0,  0,  0],
 [ 0, -4,  4,  6,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  6,  4, -4,  0],
 [ 0,  0,  0,  0,  4,  6,  0, -4],
 [ 0,  0,  0,  0, -4,  0,  6, -4],
 [ 0,  0,  0,  0,  0, -4, -4,  6]]
```

## Separate 100-decimal numerical diagonalization

The numerical check was coded separately from the symbolic path as a real
symmetric Jacobi diagonalization using Python `decimal` arithmetic at 140-digit
precision. It did not use the symbolic factorization. It diagonalized the
integer `8x8` matrix displayed above.

Numerical run diagnostics:

```text
Jacobi iterations: 132
final maximum off-diagonal magnitude:
1.7141423134721409757023146879192244004485149117081876051321281800857322456754218367789537644882294703625456839212675293193804519374211754114E-122
```

The numerical eigenvalues in nondecreasing order were:

```text
-1.84775906502257351225636637879357657364483325172728497223019546256107001500220471742967986970068919219592605156
-1.84775906502257351225636637879357657364483325172728497223019546256107001500220471742967986970068919219592605156
-0.76536686473017954345691996806079773352268912497125408286760127125509206792017938447402757068456709429684857732
-0.76536686473017954345691996806079773352268912497125408286760127125509206792017938447402757068456709429684857732
 0.76536686473017954345691996806079773352268912497125408286760127125509206792017938447402757068456709429684857732
 0.76536686473017954345691996806079773352268912497125408286760127125509206792017938447402757068456709429684857732
 1.84775906502257351225636637879357657364483325172728497223019546256107001500220471742967986970068919219592605156
 1.84775906502257351225636637879357657364483325172728497223019546256107001500220471742967986970068919219592605156
```

The numerical `+/-` pair sums were at residual size:

```text
-8.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000E-139
 1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000E-139
-4.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000E-140
-2.80000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000E-139
```

The numerical diagonalization agrees with the exact symbolic eigenvalues to at
least 100 decimal places.

## What this discharges and what it does not

This run computes the mandated V011 composition-loop matrix experiment output:

```text
V011_composition_loop_matrix_experiment_computed = true
```

Under Q-69, this is not the same as claiming the prediction is sealed:

```text
V011_composition_loop_prediction_sealed = false | TYPE-C |
constraint: sealing is a separate reviewer/principal custody act; release:
reviewer verification, baselining, commit, push, and the applicable seal-ladder
process.
```

This run does not make the composition loop forced:

```text
V011_carrier_selection_derived_from_composition = false | TYPE-R |
test: the standing sealed result says V011's composition law permits sequential
chains and never derives the commuting two-handle diamond that would
necessitate K_square.

K_square_protocol_mandated = true
```

Thus:

```text
structure_derived = true
selection_derived = false | TYPE-R
evaluating_the_spectrum_changes_neither = true
```

## Roots, exclusions, and search/read record

Roots entered:

```text
/Users/bgm/Documents/New project/gravity_emergence_evidence_program/alpha_fundamental_record_action_cleanroom_v003
/Users/bgm/MB Work/alpha-program-archive/cleanroom_output
```

Files read for source authority:

```text
BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md:1836-1945
cleanroom_output/36_GATE3_HILBERT_FUNCTOR_SPEC_V001.md:1-52
cleanroom_output/38_GATE3_HILBERT_FUNCTOR_RESULT_V001.md:1-42
```

Exclusions:

```text
a32_holdout/custodian_private/
git commands
any computation outside the six authorized matrix outputs
measured constants
Misner-Sharp / Brown-York choice
```

## Final output block

```text
Phi = pi
exp(-i Phi) = -1
B_square(pi)_Hermitian = true
spectrum_real = true
spectrum_symmetric_about_zero = true

p_pi(z) = z^8 - 8 z^6 + 20 z^4 - 16 z^2 + 4
        = (z^4 - 4 z^2 + 2)^2

eigenvalues_nondecreasing_with_multiplicity =
  -sqrt(2 + sqrt(2))
  -sqrt(2 + sqrt(2))
  -sqrt(2 - sqrt(2))
  -sqrt(2 - sqrt(2))
   sqrt(2 - sqrt(2))
   sqrt(2 - sqrt(2))
   sqrt(2 + sqrt(2))
   sqrt(2 + sqrt(2))

kernel_multiplicity = 0
Tr_B_square_squared = 16
Tr_B_square_fourth = 48
R_square = 3/16

symbolic_numerical_agreement_100_decimal = true
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```
