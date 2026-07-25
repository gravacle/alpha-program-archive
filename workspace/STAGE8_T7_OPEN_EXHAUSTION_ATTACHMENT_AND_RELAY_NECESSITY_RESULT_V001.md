# Stage-8 T7 Open-Exhaustion Attachment and Relay-Necessity Result v001

Date: 2026-07-24

## Verdict

```text
STAGE_ORDERING_AMENDMENT_REQUIRED
```

All four sealed obligations pass. The primitive connected-lift obstruction is
not resolved by adopting another principle or selecting a member of
`F(S,chi,beta,sigma,I)`. It is a dependency inversion: exact pure-cell
closure requires a relay that preserves the completed record while supplying
the next ready root, and the existing primitive Q_spec lineage already
constructs that typed relay.

This result does not establish complete physical durability or a connected
primitive amplitude.

## O1 - Exact branch-conditioned closure

For the rooted star `K_(1,m)`, the closed formulas

```text
s_m(t)=1/(m+1)+m/(m+1) cos(sqrt(m+1)t),
q_m(t)=[1-cos(sqrt(m+1)t)]/(m+1)
```

were compared with a direct matrix evolution. At
`tau_R=pi/sqrt(2)`:

```text
m=1: s_1=0, q_1=1;
m=2: s_2=-0.1739508403368207, q_2=0.5869754201684104;
m=3: s_3= 0.0503084934689383, q_3=0.3165638355103539.
```

Only the one-arm, branch-conditioned block closes exactly. This is not a
decimal-search result. For every `m>1`,

```text
|q_m(t)| <= 2/(m+1) < 1,
|<p_sym|exp(-itB_m)|r>| <= 2 sqrt(m)/(m+1) < 1.
```

## O2 - Relay necessity and Q_spec realization

A pure cell closes with type

```text
U_c(tau_R):L_(r_c) -> L_(p_c),
```

while the next cell requires `L_(r_(c+1))`. Direct composition is therefore
undefined. Advancement without erasing the prior public record requires:

```text
R_c |p_(c,h)> = |e_(c,h)> tensor |r_(c+1)>.
```

The existing Q_spec construction realizes this primitive map:

```text
iota_N(psi)=psi tensor |r_(N+1)>;
S_(N+1)|r_(N+1)>=|p_(N+1)>;
```

with exact isometry, restriction compatibility, and commutation with earlier
pointer observables. The finite checks for `N=1 -> 2` and `N=2 -> 3` all
returned zero error. A separate tuple-level verifier reproduced the record
preservation and ready-root supply without using the construction's dense
matrix helpers.

Thus:

```text
DEPENDENCY_INVERSION_DERIVED
primitive_Qspec_relay_realizes_required_type = true
complete_physical_durability_derived = false
```

## O3 - No mixed replacement interval

The exact bounds above exclude perfect transfer to either a designated
endpoint or a normalized branch-summed endpoint for every mixed star
`m>1`. No replacement interval may be selected by search.

## O4 - The residual family is real

The two-cell shared-source parent was rebuilt. Reversing the two cell
assignments changes the unitary:

```text
||U_1 U_0-U_0 U_1||_F^2 = 24
Tr(P_0 P_1) = 1/4.
```

The independent verifier obtained both values using exact rational
arithmetic.

On `K_(1,2)`, the two endpoint components are equal by symmetry, but the
operations remain distinct:

```text
individual component            = 0.5869754201684103
normalized symmetric amplitude  = 0.8301085999818119
inclusive endpoint probability  = 0.6890802877637636
```

Therefore transport assignment and endpoint conditioning cannot be erased or
silently identified. The unresolved family must be handled by the
pulled-forward Q_spec relay construction.

## Independent verification

The independent verifier:

- imported no construction code;
- used closed-form star amplitudes;
- represented the relay as tuple maps;
- evaluated the causal-order witness with exact rational matrices;
- verified all sealed hashes and protected flags.

It returned:

```text
pass = true
```

## Artifact hashes

```text
1836c808eef24ce0a4dab994f4d9857d77396bbbecc4830c6289d63db7144803  STAGE8_T7_OPEN_EXHAUSTION_ATTACHMENT_AND_RELAY_NECESSITY_SPEC_V001.md
64607e147a55744d9c701874e2ecf9e1eea1ad6108f017232f99e4aeb3e8a732  scripts/derive_stage8_t7_open_exhaustion_relay_necessity_v001.py
dc75298c2a8b6614b634e2e54a456ccdb6dc6519a554bee01f6e3d9253bc7b04  stage8_execution/work/T07_open_exhaustion_relay_necessity.json
1d6c8412d568c22230898f2b6c99d7759919bf8fa24ada2bad63015f9a9fcc34  scripts/verify_stage8_t7_open_exhaustion_relay_necessity_v001.py
3a55b87ee459ecbe539c19de4804a98af2617cef8ff2be96fc7e4a07e4d566b0  stage8_execution/work/T07_open_exhaustion_relay_necessity_verification.json
```

## Fixed status

```text
stage_ordering_amendment_derived = true
primitive_relay_durability_map_derived = true
complete_physical_durability_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
