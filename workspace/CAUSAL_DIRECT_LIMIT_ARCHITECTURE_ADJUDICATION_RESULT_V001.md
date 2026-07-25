# Causal Direct-Limit Architecture Adjudication Result v001

Date: 2026-07-24

Specification:

```text
CAUSAL_DIRECT_LIMIT_ARCHITECTURE_TEST_SPEC_V001.md
sha256 e8635914554741333f05db3fea8b055bfb76df2cfca322c1c177c53a99a50317
```

No measured coupling, mass, endpoint, or cosmological value entered the
specification, computation, or adjudication.

## 1. Covariance selector

The disclosed `3+1` Lorentzian ordinary branch supplies a **class-level
selector**:

| Architecture | Blind classification | Reason |
|---|---|---|
| causal half-line | regulator/radial reduction | no faithful microscopic `3+1` Lorentz action |
| three-branch causal tree | regulator/radial reduction | preferred branching foliation |
| cubic spatial lattice | regulator | discrete spatial symmetry and preferred frame |
| Lorentz-covariant causal-complex continuum | physical class | admits the disclosed continuum covariance and causal composition |
| effective continuum environment | effective description | its spectral density must be derived from the covariant parent |

This is genuine progress. Lorentz covariance prevents the first three
objects from being promoted directly to physical microscopic architectures.
It does **not** select a unique causal complex, refinement, or spectral
measure within the surviving covariant class.

The finite regulators can remain useful if their continuum observables are
shown to converge to the same covariant limit. They are not competing
fundamental ontologies after this classification.

## 2. Five decay laws

The common computed quantity was

```text
P_root(t)=|<r|exp(-itB)|r>|^2.
```

Late-time interval averaging gave:

| Architecture | fitted probability exponent |
|---|---:|
| causal half-line | 2.96649 |
| three-branch causal tree | 2.99634 |
| cubic spatial lattice | 3.05060 |
| covariant continuum representative | 5.98466 |
| effective continuum representative | 1.99515 |

These agree with the analytic structures:

```text
A_half(t)=J_1(2t)/t                         -> averaged P ~ t^-3;
A_tree(t)=A_half(sqrt(3)t)                  -> averaged P ~ t^-3;
A_lattice(t)=J_0(2t)^3                     -> averaged P ~ t^-3;
A_cov(t)=(1+it)^-3                          -> P=(1+t^2)^-3 ~ t^-6;
A_env(t)=(1+it)^-1                          -> P=(1+t^2)^-1 ~ t^-2.
```

All five were computed and reported in the sealed order. No winner or ranking
field exists.

Finite-regulator convergence improved monotonically over the tested sizes
for the half-line, radial tree, cubic lattice, and quadrature representation
of the covariant continuum. The sampled `(T,delta)` rows were explicitly
marked non-certified; they are numerical checks, not all-time proofs.

## 3. Direct-limit existence theorem

Let `V_n` exhaust a locally finite infinite causal complex `V`, let `P_n`
be the corresponding projections on `l2(V)`, and let `B` be the
unit-weight incidence generator. Under the cycle-7/DC3 bounded-incidence
condition,

```text
sup_n ||P_n B P_n|| <= ||B|| < infinity.
```

Define `B_n=P_nBP_n`, extended by zero outside `P_n H`. Since `P_n -> I`
strongly, for every `psi`:

```text
||B_n psi-B psi||
 <= ||P_n B(P_n psi-psi)||+||(P_n-I)B psi||
 -> 0.
```

Uniform boundedness and polynomial approximation of the exponential then
give

```text
exp(-itB_n)P_n psi -> exp(-itB)psi
```

strongly and uniformly for `t` in every compact interval. Thus the direct
limit exists for the declared bounded-degree operator class.

If the root spectral measure has an absolutely continuous `L1` density
`rho_r`, then

```text
A(t)=integral exp(-itE) rho_r(E) dE -> 0
```

by the Riemann-Lebesgue lemma. Consequently, for every `delta>0`, there is
`T_delta` such that

```text
sup_(t>=T_delta) P_root(t)<delta.
```

This establishes the cycle-7 thresholded local-return result **conditional
on** bounded incidence and an absolutely continuous root spectral measure.

## 4. Why the hypothesis is not yet a principle

The disclosed inputs do not currently force:

1. one unique Lorentz-covariant causal complex or refinement measure;
2. an absolutely continuous root spectral measure;
3. one unique spectral density within the covariant class;
4. absence of point spectrum or bound record modes;
5. a label-preserving outgoing or tail algebra from which the written
   alternative is publicly recoverable.

The spectral freedom is explicit. With the boundary normal `n`, every
positive normalized family

```text
rho_f(E) = N_f E^2 f(E T_R),   E=p dot n,
```

with admissible scalar preparation function `f`, is Lorentz covariant when
`n` is transformed with the boundary. Different low-energy behavior,
thresholds, atoms, or form factors give inequivalent decay laws. Covariance
therefore cannot select `rho_4(E)=E^2 exp(-E)/2` by itself.

Likewise, root-amplitude decay proves information left the root; it does not
prove that a public record label remains recoverable. A direct sum of
label-preserving outgoing channels would provide such recovery, but selecting
that channel decomposition now would assume the object the gate must derive.

## 5. Adjudication

The hypothesis has earned two components:

```text
finite recurrent BID dynamics is insufficient;
the bounded-incidence causal direct limit exists under its stated operator
conditions and can support thresholded local irreversibility.
```

It has not earned promotion to a principle. Fork 8 remains open at a narrower
and now explicit point:

```text
derive the covariant root spectral measure and the recoverable outgoing
record algebra from the complete microscopic parent action.
```

This is not an invitation to add a spectral-density principle. The next
valid construction must obtain both objects from the same target-independent
source-record-gravity-gauge action required by R3.

## Status

```text
fork_8_registered = true
covariance_selects_physical_class = true
unique_microscopic_causal_complex_selected = false
five_architecture_decay_lane_executed = true
bounded_class_direct_limit_exists = true
thresholded_local_return_decay_conditional = true
unique_covariant_spectral_measure_derived = false
recoverable_outgoing_record_algebra_derived = false
fork_8_closed = false
hypothesis_promoted_to_principle = false
complete_parent_action_derived = false
alpha_computed = false
proof_authorized = false
```
