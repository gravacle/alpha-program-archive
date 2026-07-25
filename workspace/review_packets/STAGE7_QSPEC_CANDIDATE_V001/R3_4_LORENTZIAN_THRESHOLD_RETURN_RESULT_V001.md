# R3.4 Lorentzian Threshold-Return Result v001

## Verdict

```text
LORENTZIAN_L2_THRESHOLD_RETURN_THEOREM_DERIVED
```

For the already derived translation-invariant Lorentzian source-record
Hamiltonian, every normalizable continuum root has an absolutely continuous
integrable spectral density. Its return amplitude therefore tends to zero.

This is a theorem about the stated Hamiltonian. It is not yet a theorem that
this Hamiltonian and a particular finite-energy root are the complete
physical outgoing sector of `Q_spec`.

## Exact bands

Write

```text
H(p)=alpha_D dot p + mu S tensor c_partial,
S=-i gamma^0 gamma^5.
```

The executable verifies

```text
S^2=I,
{alpha_D^j,S}=0,
spec(c_partial)={-sqrt(2),0,+sqrt(2)}.
```

On the record eigenspace `lambda`,

```text
H_lambda(p)^2=|p|^2+mu^2 lambda^2.
```

The nonnegative band magnitudes are therefore

```text
E_0(p)=|p|,
E_+/-sqrt(2)(p)=sqrt(|p|^2+2mu^2).
```

There is no flat band in this Dirac-record Hamiltonian.

## Spectral theorem

For an arbitrary normalized

```text
Psi in L2(R^3;C^4 tensor C^3),
```

the coarea formula on each signed band gives

```text
rho_(lambda,sigma)(E)
 =E p_lambda(E)
  integral_(S^2)
    Psi(p_lambda(E)Omega)^*
    Pi_(lambda,sigma)
    Psi(p_lambda(E)Omega)dOmega,
```

where

```text
p_lambda(E)=sqrt(E^2-mu^2 lambda^2).
```

The densities are nonnegative and their total integral is the squared norm
of the corresponding spectral component. They are consequently in `L1`.
Critical threshold points have momentum-space measure zero and introduce
integrable threshold singularities, not atoms.

Thus

```text
A_Psi(t)
 =sum_(lambda,sigma)
  integral exp(-i sigma E t)rho_(lambda,sigma)(E)dE
 ->0
```

by the Riemann-Lebesgue theorem. Equivalently:

```text
for every delta>0 there exists finite T_delta such that
sup_(t>=T_delta)|A_Psi(t)|^2<delta.
```

A momentum delta-function at `p=0` is a useful negative control: it recurs
and does not decay, but it is not an `L2` continuum root and is outside the
theorem.

## Numerical regression

A normalized isotropic Gaussian is used only as a test profile. Radial
spectral integration and direct matrix evolution on six
inversion-symmetric directions agree to `6.98e-16`. A separate
Gauss-Legendre verifier uses the exact massless Gaussian transform and an
independent massive-band quadrature.

The sampled amplitudes are:

```text
t=0:  1.0000000000000000
t=1: -0.2853795848992293
t=2:  0.2418875114958735
t=4:  0.2065195670736576
t=8:  0.0518277291571708
```

These samples are regression data, not the proof of the all-time limit.

## Scope

Closed here:

```text
nonflat Lorentzian source-record band structure;
absolute continuity for every L2 root under this H;
and thresholded local nonreturn under this H.
```

Still open:

```text
complete_outgoing_generator_identified = false
parent_selected_physical_root_derived = false
finite_energy_physical_root_derived = false
positive_frequency_state_derived_from_parent = false
generated_descendant_spectrum_exhausted = false
complete_write_defect_bound_states_excluded = false
complete_physical_durability_derived = false
complete_parameter_free_Q_spec_frozen = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
