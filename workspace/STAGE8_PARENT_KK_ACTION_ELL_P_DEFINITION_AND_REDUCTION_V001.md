# CODEX 2 — Parent action, `ell_P`, and symbolic reduction

`alpha_computed = false; proof_authorized = false; kappa_record_computed = false.`

## Construction status

The corpus search established no named parent normalization or `ell_P` definition. This artifact therefore
introduces a **symbolic KK specification**, not a numerical result. Every imported convention is marked.

## 1. Parent action

Choose the five-dimensional Einstein-frame action (STANDARD KK IMPORT / EXPLICIT CHOICE):

```text
S5[g5, matter] = (1/(2 kappa5^2)) ∫_{M4×S1} d^4x dθ sqrt(-G) R5[G] + S5,matter.
```

The metric ansatz is the supplied geometry (SEALED GEOMETRIC FORM):

```text
ds5^2 = g_{μν}(x) dx^μ dx^ν + R(x)^2 (dθ + A_μ(x) dx^μ)^2,
θ ~ θ + 2π.
```

`kappa5^2` is the parent gravitational normalization, defined here as the coefficient inverse of the
five-dimensional Einstein-Hilbert density. Its numerical value and relation to any microscopic theory are
ABSENT. The circle period `2π`, omission of a cosmological term, and matter content are explicit CHOICES,
not sealed consequences.

## 2. Definition of `ell_P`

For a constant-radius reduction, define (DEFINITION/CONVENTION, not an evaluated value)

```text
ell_P^2 := kappa5^2 / (2π R0),
```

where `R0` is the reference fiber radius in the chosen four-dimensional Einstein-frame normalization.
Thus `ell_P` is a function of the parent normalization, the fiber period, and the reference radius. This
definition is not imported as a corpus fact; it is the declared convention needed to name the reduced
coefficient.

## 3. Symbolic reduction

For constant `R=R0`, the determinant factor is `sqrt(-G)=R0 sqrt(-g)` and the fiber integral is
`∫_0^{2π}dθ = 2π`. The Einstein-Hilbert term therefore has coefficient

```text
(2π R0)/(2 kappa5^2) ∫ d^4x sqrt(-g) [R4[g] - (R0^2/4) F_{μν}F^{μν} + ...].
```

The displayed `...` denotes the radion derivative terms that arise when `R(x)` is dynamical; no radion
potential is assumed here. Substituting the declared definition gives

```text
S4 ⊃ (1/(2 ell_P^2)) ∫ d^4x sqrt(-g) R4[g],
```

and the gauge term retains its explicit fiber-radius factor. The fiber extent lands in the four-dimensional
coefficient through `2πR0`; it does not disappear. Calling that coefficient `ell_P` is exactly the
normalization convention above.

## 4. Held-fixed question

Under `R → βR`, the reduction alone holds fixed neither `kappa5` nor `ell_P`: the four-dimensional EH
coefficient scales with the fiber volume if `kappa5` is held fixed, while it is constant only if the parent
normalization is rescaled with the fiber extent. Therefore the held-fixed rule is **NO_VERDICT | TYPE-U**.
The additional input required is a sealed parent normalization rule stating whether `kappa5^2` is invariant
under the radius deformation, or a compensating frame/field-redefinition law. Defining `ell_P` cannot itself
answer this without circularity; the definition precedes the scaling test.

`ell_P_held_fixed_under_R_scaling = NO_VERDICT | TYPE-U | would-build: independent parent-normalization/frame
law.`
`parent_action_derived_from_corpus = false | TYPE-S | scope: corpus roots and cleanroom_output; no parent
normalization was sealed.`

No beta, alpha, coupling, radius, or potential was evaluated. No git, commit, push, gate, or deploy action
was performed.
