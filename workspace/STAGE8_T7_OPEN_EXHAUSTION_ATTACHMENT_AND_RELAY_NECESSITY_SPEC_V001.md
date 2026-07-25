# Stage-8 T7 Open-Exhaustion Attachment and Relay-Necessity Spec v001

Date: 2026-07-24

## Status

```text
SPECIFICATION_SEALED_BEFORE_EXECUTION
```

This target-free gate implements O1-O4 from the independent Stage-8 T7 lift
adjudication. It tests whether the apparent open-exhaustion choice is really
a dependency inversion into the already-declared Q_spec durability lineage.
It adopts no principle and evaluates no response coefficient.

## External adjudication authority

```text
34ebb4dbc2903b91231bd4253dba78c0012c4be4eac062b8145f970fee808eb2  /Users/bgm/MB Work/alpha_supervision/STAGE8_T7_LIFT_ADJUDICATION_RETURN_V001.md
```

## Workspace authorities

```text
aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a  BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md
7471988138233218430c6b6dd07b39f33508a75907557723654dbc712c0c4476  BID_FIRST_OPENING_INTERVAL_DERIVATION_V001.md
b0c636f3b2b00f0694ad001cb32a3a84c5d4fc09c25c57fd4fdb8885e8206b30  CAUSAL_INCIDENCE_SUPPORT_PRINCIPLE_V001.md
202f8d8db60046a8069b1cd8fcc38f505eb95fa29578e094e005f56e967c3a35  STAGE7_QSPEC_SCOPE_AND_PREMISE_SUCCESSOR_V001.md
2be95d5b58ea000df9a30b717a809374a90693f78a893d87b73a12e4be97fa21  R3_4_CHARGED_INCIDENCE_OUTGOING_STATE_RESULT_V002.md
1d114e71c29c3a39b7afd1b7a80b47afb52fe77e8ee1e4e19b604defe3c69305  R3_4_CAUSAL_SHARED_SOURCE_MOLLER_DURABILITY_RESULT_V001.md
10909b5c21e73ecf655462339a27bd645b8d35e3ad11fb6f8cb204c601992995  R3_4_OUTGOING_RECORD_GNS_COMPLETION_RESULT_V001.md
e12fffcc0f94d6896bc5607898db6b3a1ea343aeaf557b1f6f70e58db061fab6  STAGE8_T7_RESPONSE_CLOSURE_SELECTION_DERIVATION_RESULT_V001.md
eb83e5450928bf148cae58b3b553c9dff482b07172aa8aeb182e0834bb869723  STAGE8_T7_PRIMITIVE_CONNECTED_LIFT_DERIVATION_RESULT_V001.md
30903a1623718fd0ecb3cb2ad50765792c20f402710454e43cfbbccb42048af8  STAGE8_T7_COMPLETED_EFFECT_ZERO_BASELINE_RESULT_V001.md
93b4a836962a177301d0338c8e81c3203cc52136a2123ca3e11a3c9a844b95a8  stage8_execution/t7_primitive_connected_lift/T07_PRIMITIVE_CONNECTED_LIFT_VERIFIER_V002.seal.sha256
```

Any mismatch aborts execution.

## Surviving family notation

After the independently adjudicated exclusions, denote the residual
open-exhaustion family by:

```text
F(S,chi,beta,sigma,I),
```

where:

```text
S     assigns bulk transport to finite cell factors;
chi   places the active branch-conditioned handle;
beta  selects a completed endpoint when multiple future handles exist;
sigma chooses per-branch or branch-summed conditioning;
I     supplies the interval rule for any mixed carrier.
```

This notation records an unresolved family; it does not authorize choosing a
member.

## O1 - Branch-conditioned exactness dichotomy

For the rooted unit-incidence star `K_(1,m)`, construct:

```text
D_m:C^m -> C^(m+1),
D_m e_j=|p_j>-|r>,
B_m=[[0,D_m],[D_m^dagger,0]].
```

Starting from `|r>`, derive:

```text
s_m(t)=<r|exp(-itB_m)|r>
      =1/(m+1)+m/(m+1) cos(sqrt(m+1)t),

q_m(t)=<p_j|exp(-itB_m)|r>
      =[1-cos(sqrt(m+1)t)]/(m+1).
```

At `tau_R=pi/sqrt(2)`, execute the sealed competitor set:

```text
m=1: one branch-conditioned handle;
m=2: one handle plus one simultaneous bulk incidence;
m=3: the three-handle joint star.
```

Pass O1 only if:

```text
m=1 gives s_1(tau_R)=0 and q_1(tau_R)=1 exactly;
m=2 and m=3 fail exact closure;
and the failure is certified without decimal equality tests.
```

The `m=2` and `m=3` numerical values are reported only as regression
witnesses. Exact symbolic expressions and certified enclosures are
authoritative.

## O2 - Dependency-inversion theorem

### Type obstruction

For pure block `c`, the exact closure map has type:

```text
U_c(tau_R):L_(r_c)->L_(p_c).
```

The next block begins on a distinct ready line:

```text
U_(c+1)(tau_R):L_(r_(c+1))->L_(p_(c+1)).
```

Prove that the composition `U_(c+1) compose U_c` is undefined unless a
typed relay is supplied. Root and endpoint lines may not be identified by
notation, because `OpenRec_2` morphisms preserve first-opening status and
the no-output rule distinguishes unresolved from completed sectors.

### Durable relay

To advance while preserving the old public record, the relay must have the
form:

```text
R_c:L_(p_c)->E_c tensor L_(r_(c+1)),
R_c |p_(c,h)>=|e_(c,h)> tensor |r_(c+1)>,
```

up to branchwise phase, with orthogonal durable labels `|e_(c,h)>`.

Prove:

```text
R_c is an isometry;
the old branch label remains recoverable in E_c;
the new block receives the unique ready root;
and no map L_p->L_r alone can both advance and preserve the record.
```

### Q_spec realization

Test whether the existing charged-incidence/Q_spec lineage already realizes
this structure through:

```text
iota_N(psi)=psi tensor |r_(N+1)>;
S_(N+1)|r_(N+1)>=|p_(N+1)>;
later-cell operators commuting with all earlier public-record observables;
and restriction compatibility of rho_(N+1) with rho_N.
```

The realized map may be called a **primitive relay/durability map** only
inside the already-declared pure-charge primitive branch. It must not be
promoted to complete physical durability; generated descendants remain open.

O2 verdicts:

```text
DEPENDENCY_INVERSION_DERIVED
  iff the relay is necessary and the existing Q_spec lineage supplies it;

GENUINE_RELAY_THEORY_DECISION
  iff relay necessity fails or the existing Q_spec lineage does not supply
  the required typed isometry and preservation.
```

## O3 - Mixed-branch interval adjudication

For every `m>1` in the sealed mixed-star competitor set, prove or disprove
the existence of any positive `t` such that:

```text
exp(-itB_m)|r>=phase*|p_j>
```

for one designated endpoint.

Use the exact bound:

```text
|q_m(t)| <= 2/(m+1) < 1,  m>1.
```

Also test the normalized branch-summed endpoint:

```text
|p_sym>=m^(-1/2) sum_j |p_j>,
|<p_sym|exp(-itB_m)|r>| <= 2 sqrt(m)/(m+1) < 1,  m>1.
```

Therefore no mixed block may receive a replacement interval selected by
search. If a counterexample exists, O3 fails and its exact matrix must be
reported.

## O4 - Residual-family witnesses

Seal two independent facts without choosing an `F` member:

1. **S is load-bearing.** Reconstruct the existing two-cell shared-source
   finite parent and verify that reversing the two causally ordered cell
   assignments changes its unitary. The norm difference must be strictly
   nonzero and independently reproduced. This witnesses that transport/cell
   assignment is physical before any response value is formed.
2. **beta/sigma are load-bearing.** On `K_(1,2)`, report separately the two
   endpoint amplitudes and the normalized symmetric endpoint amplitude.
   Prove that naming one endpoint, retaining the endpoint vector, and
   branch-summing are distinct operations even though symmetry can make two
   scalar components equal.

O4 records that the residual family is real. It does not license selecting a
member. If O2 passes, the family is handed to the pulled-forward Q_spec relay
derivation rather than to a new premise.

## Overall dispositions

```text
STAGE_ORDERING_AMENDMENT_REQUIRED
  iff O1, O2, O3, and O4 pass with DEPENDENCY_INVERSION_DERIVED;

GENUINE_THEORY_DECISION_REQUIRED
  iff O2 returns GENUINE_RELAY_THEORY_DECISION;

OPEN_EXHAUSTION_GATE_BLOCKED
  iff any exact theorem, authority hash, or negative control fails.
```

No adoption packet may be created by this execution.

## No-target attestation

No alpha, measured coupling, endpoint, cosmological value, or
response-selected coefficient may be read or used.

## Fixed flags

```text
stage_ordering_amendment_derived = false
primitive_relay_durability_map_derived = false
complete_physical_durability_derived = false
connected_primitive_amplitude_derived = false
volume_uniform_zero_free_neighborhood_proved = false
connected_linked_cluster_density_proved = false
kappa_record_computed = false
coupling_evaluation_authorized = false
alpha_computed = false
proof_authorized = false
```
