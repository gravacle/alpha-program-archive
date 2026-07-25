# Complete Parent-Action Underdetermination Gate v001

## Question

Do the currently sealed pre-alpha premises uniquely determine the microscopic
charged record action required by `Q_spec[g,a,psi,R]`?

## Shared premises

The compared completions retain:

```text
3+1 Lorentz covariance;
CPT compatibility;
the active compact U(1)_rel connection a;
one unit-character vectorlike Dirac source psi;
one primitive record carrier;
one physical record-cell scale ell_*;
zero independent bare Maxwell stiffness.
```

Neither completion uses alpha.

## Two admissible completions

The minimal source action is

```text
S_0
  = integral d^4x sqrt(-g)
      i hbar bar(psi) gamma^mu D_mu psi
    + S_record[R,a,g].
```

The following completion preserves the same declared spacetime, gauge, and
CPT symmetries:

```text
S_1
  = S_0
    + hbar ell_*
      integral d^4x sqrt(-g)
        bar(psi) sigma^(mu nu) psi F_(mu nu).
```

The displayed coefficient is the fixed integer one, not a tunable fit
parameter. Both actions remain parameter-free after `ell_*` is supplied by the
assumed unique record cell. Both have `K_bare=0`.

The second term changes the charged current vertex from the minimal vertex to

```text
Gamma^mu(p+q,p)
  = gamma^mu + 2 i ell_* sigma^(mu nu) q_nu.
```

Consequently the exact current-current response and its finite-cell
parity-even curvature differ between `S_0` and `S_1`. The present premises do
not select one completion over the other.

Equivalent countermodels can be made with gauge-covariant higher-derivative
source terms or different finite causal updates. The Pauli pair is sufficient:
one surviving pair of admissible actions with different response blocks
uniqueness.

## What the gate proves

The primitive carrier, unit action character, unique cell scale, and
compositeness condition do not by themselves specify the microscopic
generator. They therefore cannot yet determine the absolute charged
stiffness.

This is not the ordinary finite-`c_R F^2` counterterm objection. It survives
even after an independent bare Maxwell term is forbidden: distinct
parameter-free charged-record dynamics induce different finite responses.

## Exact reopen condition

Step 5 can close only if an upstream boundary principle derives a complete
microscopic generator and excludes the Pauli completion and all equivalent
mutations before response evaluation. Examples of sufficient outcomes are:

1. a derived first-order minimality theorem for the complete primitive
   generator;
2. a derived total-space geometric action in which all charged vertices are
   fixed components of one connection; or
3. a derived finite quantum-record update whose full gauge-covariant matrix is
   unique up to unitary equivalence.

Merely declaring one option "minimal" is not a derivation.

## Status

```text
current_premises_admit_two_response_inequivalent_parent_actions = true
complete_parent_action_uniquely_derived = false
finite_response_evaluation_authorized = false
finite_c_F2_deformation_excluded = false
alpha_computed = false
proof_authorized = false
```
