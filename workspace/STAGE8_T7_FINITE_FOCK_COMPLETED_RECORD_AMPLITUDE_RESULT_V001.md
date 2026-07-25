# Stage-8 T7 Finite-Fock Completed-Record Amplitude Result v001

Date: 2026-07-24

## Verdict

```text
FINITE_FOCK_COMPLETED_RECORD_BASELINE_DERIVED
```

The actual time-dependent CAR parent was restricted by the previously
derived continuum-state regulator rule to eight nonzero one-particle modes.
Its inherited negative-energy state occupies four modes, so the calculation
was executed exactly on:

```text
wedge^4 C^8,  dim = 70
```

with two record qutrits. No determinant formula, ideal projector chain, or
source ray selected after evolution was used.

## Primary calculation

The split-operator calculation produced:

```text
a_p(0)  = -0.49783734936846613 - 0.19428764927664235 i
|a_p(0)|  = 0.5344059478408374

a_pp(0) =  0.30800852070998297 + 0.24716523618271335 i
|a_pp(0)| = 0.3949175898933960
```

The `100/200/400` time-step comparison gave a second-order convergence
ratio of `3.999961095641164`. Norm errors remained below `6.1e-13`, and all
many-source lift Hermiticity errors remained below `1.0e-15`.

The zero-particle completed-record amplitude is exactly zero because
`dGamma(B)` has a zero vacuum block. A separately executed one-particle
sector has completed-transfer norm `0.714899583886226`, so the
record-compressed operator cannot be a single `Gamma(k)` and the Gaussian
determinant shortcut remains excluded.

## Independent verification

The independent verifier rebuilt the active range in a canonical-column
basis, constructed the CAR lift from occupation-bit signs, represented the
incoming state by Slater determinants, and used RK4 rather than the primary
split integrator.

Before independent amplitudes were evaluated, the complex comparison
tolerance was frozen at `1e-4`, based on the primary second-order tail
estimate.

The sealed execution history is retained:

1. v001 failed before physics execution because Python 3.9 lacks
   `int.bit_count()`.
2. v002 made only the portable population-count repair. It executed the
   physics but failed its unchanged `2e-9` RK4-tail gate with
   `2.624963099407436e-8`.
3. v003 retained every physics choice, tolerance, and tail gate while
   doubling both RK4 resolutions from `800/1600` to `1600/3200`.

The sealed v003 verifier passed:

```text
RK4 tail       = 1.639e-9
|delta a_p|    = 7.395e-6
|delta a_pp|   = 1.775e-5
```

Thus two independently coded Fock constructions and time integrators agree
on nonzero one- and two-cell completed-record amplitudes within the
predeclared error budget.

## Scope

This closes the finite-Fock baseline only. It does not establish
factorization, regulator independence, a volume-uniform zero-free
neighborhood, connected linked-cluster density, or the thermodynamic
Duhamel identity.

```text
finite_fock_completed_record_baseline_derived = true
finite_actual_parent_record_amplitude_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
