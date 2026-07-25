# Stage-8 T7 Parent-State Regulator Restriction Result v001

Date: 2026-07-24

## Verdict

```text
PARENT_STATE_REGULATOR_RESTRICTION_DERIVED
```

The incoming finite quasifree state is not selected from the spectrum of the
three-site regression. It is the restriction of the already-disclosed
continuum covariance:

```text
C=1_(-infinity,0)(h_0);
C_n=Q_n C Q_n.
```

The point `p=0` has zero Lebesgue measure, so its spectral representative
does not alter the continuum multiplication operator. Nested finite
spectral subspaces supported away from that point are cofinal and satisfy:

```text
Q_n C_m Q_n=C_n,  m>=n.
```

The executable verifies two nested inversion-symmetric momentum cohorts.
Both have exact half-rank negative-energy covariances, no zero eigenvalue,
and projection/Hermiticity errors below `7e-16`. A direct finite-Fock Slater
construction independently reproduces the smaller covariance to
`4.5e-16`, and a second verifier reproduces both covariances from:

```text
C(p)=(I-h_0(p)/|p|)/2.
```

No zero-mode filling, antiperiodic boundary condition, thermal parameter, or
new state principle was introduced. The old periodic three-site model
remains an operator regression but is not used as the state regulator.

This closes only the same-parent finite-state compatibility gap. The
completed-record operator must next be constructed on the complete finite
Fock space and evaluated in this inherited state. No determinant shortcut
is authorized unless the record-compressed operator is proved to be a
single second quantization.

All coupling and proof statuses remain false.
