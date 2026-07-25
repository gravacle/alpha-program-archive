# Full-Carrier Dilation Selector Obstruction Gate v001

Date: 2026-07-23

## Question

Do the currently sealed source, record, and grading constraints select one
complete source-record-environment coupling ray and thereby tie the record
onset scale to the chiral-odd source self-energy?

This gate answers a narrower executable question on the smallest declared
three-factor reduction. It does not claim to construct the complete Lorentzian
field carrier or the axial-anomaly inflow sector.

## Reduced carrier under test

Declare only for this identifiability calculation:

```text
H_red
  = C^2_source-grading
    tensor C^2_record-endpoint
    tensor C^2_edge/witness.
```

The first two factors are the reduced factors already used in the sealed
source-record structure gate. The third is the smallest binary witness factor
on which one could test whether an additional closure/edge degree removes the
coefficient ambiguity.

This three-factor ansatz is not derived as the complete physical carrier.
Spin, spacetime, gauge transport, topology, ghosts, and a genuine environment
spectrum remain outside it.

## Exact unrestricted odd/odd space

Enumerate all `64` Hermitian Pauli products. Requiring the interaction to be
odd under both source and record gradings,

```text
{G,Z_S}=0,
{G,Z_R}=0,
```

leaves the exact `16`-dimensional real span

```text
{X_S,Y_S} tensor {X_R,Y_R} tensor {I_E,X_E,Y_E,Z_E}.
```

## Candidate finite grading laws

For an integer weight triple `w=(w_S,w_R,w_E)`, define the candidate
finite grading

```text
Z_w = w_S Z_S + w_R Z_R + w_E Z_E
```

and impose

```text
[G,Z_w]=0.
```

These finite-matrix commutators are not the axial Ward identity. They are a
controlled test of whether a proposed grading-accounting law would select the
coupling.

The exact kernel dimensions are:

```text
w=(1,1,0): nullity 8;
w=(1,1,1): nullity 4;
w=(2,1,-1): nullity 2.
```

For equal unit edge weight `(1,1,1)`, every surviving direction is diagonal on
the witness factor (`I_E` or `Z_E`); no surviving direction flips the witness.
It therefore cannot by itself produce the redundant witness transition that
motivated adding the factor.

The apparently attractive `(2,1,-1)` assignment leaves two real directions,
equivalent to one complex exchange amplitude, and includes witness-flipping
operators. But the weight triple is not selected by the sealed premises.

## Neighbor enumeration

Enumerate every primitive integer triple with `|w_i| <= 2`, identify overall
sign, and exclude the all-zero triple. The exact nullity distribution is:

```text
nullity 0: 22 triples
nullity 2:  8 triples
nullity 4: 12 triples
nullity 6:  4 triples
nullity 8:  3 triples
```

Thus the one-complex-amplitude result is not unique to one grading law. Eight
neighboring primitive assignments produce it. Choosing `(2,1,-1)` because it
has the desired dimension would move the selection problem into the grading
weights.

## Schur-complement scale obstruction

Even after a coupling ray is chosen, a reduced public/closure block contains
at least an off-diagonal matrix element `g` and a closure-sector gap `d`:

```text
G_block = [[0,g],[g,d]].
```

Eliminating the closure state gives

```text
Sigma(z) = g^2/(z-d).
```

The record holonomy may constrain an integrated product such as `g tau_*`.
It does not, from the current premises, fix `d`, `tau_*`, or the value of
`Sigma(0)=-g^2/d`. The exact target-free choices `d=1` and `d=2` already give
different reduced self-energies with the same displayed structural
symmetries. They are algebraic witnesses of missing selection, not promoted
physical models.

## Result

The current sealed constraints do not yet derive:

1. the complete edge/environment carrier;
2. the axial Ward/inflow realization on that carrier;
3. the physical grading weights;
4. the closure-sector spectrum;
5. one invariant coupling normalization.

Accordingly, the record-onset scale cannot yet be transferred to a unique
source self-energy. A one-norm superconnection would merely hide this
ambiguity unless its invariant-form space and full carrier are derived first.

## Exact reopen condition

The next constructive gate must derive, without alpha or mass input:

1. the physical edge/environment degrees required by durable closure;
2. their Lorentz, vector-`U(1)`, CPT, and axial/inflow transformations;
3. the full allowed operator space and its invariant positive forms;
4. a unique coupling ray up to an overall scale;
5. the closure-sector spectrum and causal-cell interval;
6. the exact record channel and chiral-odd Schur self-energy from the same
   unretuned matrix elements.

If the constrained coefficient space has dimension greater than one, or if an
independent rescaling leaves either output deformable, the route remains
blocked.

## Status

```text
reduced_three_factor_carrier_declared = true
complete_physical_carrier_derived = false
odd_odd_reduced_operator_dimension = 16
unit_weight_candidate_kernel_dimension = 4
unit_weight_candidate_writes_edge = false
source_doubled_candidate_kernel_dimension = 2
source_doubled_candidate_writes_edge = true
source_doubled_grading_weights_derived = false
neighbor_weight_assignments_with_same_nullity = 8
unique_full_carrier_coupling_ray_derived = false
axial_Ward_identity_with_inflow_derived = false
closure_sector_spectrum_derived = false
record_onset_to_source_self_energy_ratio_derived = false
complete_source_record_environment_operator_derived = false
physical_durability_derived = false
record_generated_source_mass_derived = false
spectral_evaluation_authorized = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
