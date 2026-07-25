# Complete-Q_spec Finite-Holonomy Response Numerics Protocol v001

Date: 2026-07-25

This protocol is sealed before the response is evaluated.

## Frozen grid

```text
theta_coarse = 1/20;
theta_fine   = 1/40;
time_steps_coarse = 200;
time_steps_fine   = 400.
```

At each grid point compute complete normalized output states for
`theta in {0,+h,-h}`.

## Estimators

```text
Z_h=<Psi_0|Psi_h>;
Gamma_h=-log|Z_h|;
H(h)=[Gamma(+h)+Gamma(-h)]/h^2;

dot_Psi(h)=[Psi_(+h)-Psi_(-h)]/(2h);
g_FS(h)=<dot_Psi|dot_Psi>-|<Psi_0|dot_Psi>|^2.
```

## Error enclosures

Use the expected second-order parameter and time tails:

```text
parameter_tail_X
 =|X(time_fine,theta_fine)-X(time_fine,theta_coarse)|/3;

time_tail_X
 =|X(time_fine,theta_fine)-X(time_coarse,theta_fine)|/3;

radius_X=parameter_tail_X+time_tail_X+1e-8.
```

Define:

```text
I_H=[H_fine-radius_H,H_fine+radius_H];
I_g=[g_fine-radius_g,g_fine+radius_g].
```

Pass requires:

```text
lower(I_H)>0;
lower(I_g)>0;
I_H intersects I_g;
|Z(0)-1|<1e-12;
all output-state norm errors <2e-10;
and all one-particle/Fock Hamiltonian Hermiticity errors <1e-12.
```

No tolerance may be changed after seeing the response. A numerical failure
is reported separately from a physics-zero failure.

## Fixed status

```text
finite_Qspec_holonomy_response_diagnostic_passed = false
kappa_record_computed = false
physical_Thomson_stiffness_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
