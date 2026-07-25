# R3.4 Causal-Cell Moving-Front Result v001

## Verdict

```text
MOVING_FRONT_PUBLIC_RECORD_DYNAMICS_CONDITIONAL
```

The moving-front construction is mathematically sufficient for durable
public records and is independent of pulse profile and causal linear
extension. The current live parent authority has not yet derived that
moving-front action, so the physical result remains conditional.

## Profile independence

For one cell:

```text
H_j(t)=v_j(t) B_j,
integral v_j(t) dt=tau_R.
```

Because the operator is fixed throughout the pulse:

```text
[H_j(t),H_j(s)]=0
```

and therefore:

```text
T exp[-i integral H_j(t)dt]=exp(-i tau_R B_j).
```

Constant, uneven-positive, sign-changing, and five-segment profiles all
reproduce the same endpoint map, with maximum numerical disagreement
`8.91e-15`.

For distinct record cells:

```text
[B_j,B_k]=0.
```

All tested commutators are exactly zero, and reversing the three-cell gate
order changes the completed unitary by only `1.07e-30`. This is the exact
algebraic reason any causal linear extension gives the same endpoint map in
the declared pure-charge branch.

## Public-record stabilization

A later-cell pulse acts on a distinct record factor. Its commutator with
every earlier public-record observable is exactly zero at all intermediate
times. Hence, under the one-use moving-front construction, every fixed local
public observable eventually becomes constant.

The pointer averages satisfy:

```text
||[M_N,O]|| <= 2m ||O||/N.
```

The executable reaches the bound for a one-cell negative-control observable
at `N=2,3,4,5`. The limiting charged and neutral pointer expectations are
distinct, so the public label survives as an asymptotic central sector.

On the stabilized public-record algebra, the asymptotic derivation is:

```text
delta_out=0.
```

Its automorphism group is the strongly continuous identity group, and its
point spectrum is explicitly `{0}`. This is not the separately selected
continuous spectral density explored in earlier R3.4 candidates.

## Why the result is conditional

The relevant live authorities still report:

```text
unique_causal_record_cell_derived = false;
time_dependent_continuum_ordering_derived = false;
hypothesis_promoted_to_principle = false.
```

Accordingly, the corpus has not yet shown that the complete microscopic
parent uses this compact, one-use moving interaction front. A permanently
acting stationary incidence parent is a different completion and fails the
endpoint-GNS test.

The current result proves:

```text
if the complete parent realizes its already proposed primitive writes as
one-use finite causal-cell events, durable public outgoing sectors follow
without any spectral-density choice.
```

It does not yet prove that the complete source/gauge/gravity/environment
action has that form.

## Status

```text
pulse_profile_independence_derived = true
distinct_cell_generator_commutation_derived = true
causal_linear_extension_independence_derived = true
earlier_public_record_nondemolition_derived = true
central_pointer_sector_derived_for_moving_front = true
conditional_outgoing_public_dynamics_strongly_continuous = true
moving_front_bound_by_live_complete_parent = false
full_parent_state_covariance_derived = false
physical_durability_derived_unconditionally = false
complete_parent_action_derived = false
physical_response_spectral_measure_derived = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
