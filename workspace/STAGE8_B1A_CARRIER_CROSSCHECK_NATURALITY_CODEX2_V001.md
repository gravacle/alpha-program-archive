# STAGE 8 / 7A / [PLAN:B1a-4] — CARRIER CROSS-CHECK AND MIN-NORM NATURALITY TEST

## Lead determination — CLAIMED

The lane-opposite incidence carrier **stands**.  Independent coordinate-poset
constructions reproduce the direction theorem, the exact cochain-map identity,
the intertwining criterion, and the three carrier-level residual dimensions.

The minimum-norm lead does **not** survive the commissioned naturality test.
Using one unweighted counting inner product and one pseudoinverse procedure for
every complex, the identity

```text
sd*_1 o Q'_flux o (minimum-norm physical-flux section) = Q_flux
```

holds to numerical precision for cubical bisection and for the barycentric A2
instance, but fails on the licensed Freudenthal A2 instance with random-test
worst deviation `1.2029726825073028e-1`.  An `A1`-then-Freudenthal composite
also fails, at `1.3560931591152436e-1`.  A single admitted generator failure
refutes naturality over the generator class.  No generator-specific weight or
adjustment is permitted or used.

Thus the 788 observation remains a valid instance observation but its candidate
cannot define the demanded natural rule.  Every headline here is `CLAIMED`
pending registration/cross-check.

## 0. Preflight, custody, and pins

- Relay `794` was uniquely located, its adjacent seal verified, and
  `relay_outbox/794_ACK.md` written before the body was read. Lane guard:
  `CODEX 2`.
- `PROGRAM_STATE_BRIEF_V005.md` was verified and read at
  `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`.
- Subject `STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md` was verified and read
  at `97f073c101d8cf4a6743660b96e3861e21914ac48877ce538314616b51d70cb6`.
  Its incidence derivation is `[5151,9996)`, span SHA
  `4eb23669b793b5531388e9c506970c004f4e13e9f62060fa5f01190e9ed20d68`;
  its minimum-norm lead is `[13805,15517)`, span SHA
  `d03884e9f90a132b3c3657e754ed7c10844fc80c3d28c51db7e2dbdb9ddffa85`.
- The sealed packet copy alone was used:
  `review_packets/STAGE7_QSPEC_CANDIDATE_V001/BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`,
  `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a`,
  exactly `78,794` bytes.  The unsealed root copy was not read.
- Governing Ext/Flux display and obligations:
  `STAGE8_B1A_LIFT_FORCING_CODEX2_V001.md`,
  `3966fdb124c6fed887499ac56907510ed4bc5666be74f32f49f60875c61fc2f0`;
  `[7441,8790)`, span SHA
  `df76c235af0a2f96ce3656c578732f5d130ca6227b9225b06576835ff002016e`;
  `[9706,11861)`, span SHA
  `5b5d6b0e358e0663f725ee0498d5fd26f4d33bebab203058883d1fc9ab47ecb2`.
- The live register was seal-verified at
  `4c57babe0b3212813dc33dcbd0b7508c1f0457529e38bf16217d52627a9bbfe2`;
  its Q-698 entry was used only to locate the mirrored subject and not as proof.
- Existing-output stop check passed. `PE-1` through `PE-7` were not consulted
  and have zero weight.

Decisive packet spans, rehashed from the sealed bytes:

| content | byte span | span SHA-256 |
|---|---:|---|
| injective `BareRec_2` cellular map and induced `J_0,J_1,J_2` | `[14753,15668)` | `04985691732de5a288166a8afbc794cf7407d6197d4f40de193f15cf1f141b12` |
| `d_0`, `d_1`, counting products, `F_phys`, `Q_flux`, three defining properties | `[44530,45446)` | `9bbd9525cbd84a6b6365383da6cd6e38d33f945e01c98c1a0d3052f322b74efc` |
| exact `d_1` identity | `[44595,44690)` | `c6cd568bec678df676737009466e3537dfe64fd6962fdb3200b9f90b9dc14eb5` |
| `Q_flux` block itself | `[44801,45186)` | `4c3a09c08df8a80df3f1744f685df4d6beb518d992d87e3514305e21f012255b` |
| one counting metric; `C_ref` generators; common-refinement clause | `[46389,47446)` | `5e58b0750c069f0d9e553f3334f31aaaec7fe60f99d44b0815de1ab6ca3768b7` |
| licensed generator inventory | `[46772,47023)` | `cf173101542c3d7fb6a045d9c11cd955e89a81c143638a7b3996d8603e6dc849` |
| exact common-refinement conjunct and boundary-asymptotic conjunct | `[47025,47247)` | `9ff6852634e78e6d886896c27bce16b4ec9e092620642a86bae00848df2f276c` |

## 1. AS1 — independent incidence re-derivation — CLAIMED

### 1.1 Complexes and aggregation maps

The parent was the oriented unit 4-cube, built directly from coordinates:
`16` vertices, `32` positive-coordinate edges, `24` oriented square faces.
Its edge-to-face coboundary has rank `17`.

Three independent refined complexes were constructed without subject code:

| instance | construction | `V'` | `E'` | `F'_2` |
|---|---|---:|---:|---:|
| `A1` | grid `{0,1,2}^4`, unit cubical faces | 81 | 216 | 216 |
| `A2-F` | Freudenthal chains of Boolean vertices | 16 | 65 | 110 |
| `A2-B` | barycentric chains of nonempty 4-cube faces | 81 | 544 | 1232 |

For each parent edge and face the sealed fibre constraints uniquely determine
the aggregation maps:

```text
(sd*_1 a')_e  = sum_(e' subdividing e) orientation(e',e) a'_(e')
(sd*_2 xi')_f = sum_(f_i subset f) orientation(f_i,f) xi'_(f_i).
```

Cubical rows sum the two child edges or four child squares. Freudenthal rows
retain parent edges and sum the two oriented boundary triangles. Barycentric
rows sum the two half-edges and eight oriented vertex-edge-face triangles.

### 1.2 Direction theorem

All three `sd*_1` matrices have full row rank `32`, hence are surjective
`C^1(K') -> C^1(K)`.  Their kernel dimensions are respectively `184`, `33`,
and `512`; none is injective.  `A0` has `sd*_1=I_32`, and is injective.

Therefore a coarse-to-fine `J_1` satisfying `sd*_1 J_1=I` is a **section**.
It is uniquely determined by the subdivision map only when the aggregation is
injective, which here occurs precisely in the `A0` case.  The V011 map at
`[14753,15668)` instead starts with an injective cellular embedding sending
each domain face to one target face.  That is a different variance/type and
cannot instantiate a nontrivial subdivision section.

```text
DIRECTION_THEOREM = CONFIRMED
```

### 1.3 Exact cochain-map identity and independent trials

The integer matrices satisfy, entry by entry,

```text
sd*_2 d'_1 - d_1 sd*_1 = 0.
```

Nonzero entries in the difference matrix: `0` for each of `A1`, `A2-F`, and
`A2-B`.  This exact matrix comparison covers every edge contribution to all
24 parent squares, including transverse/off-plane edges.

Independent randomized confirmation used seed `79420260809`, integer cochains
with coefficients in `[-9,9]`, and **257 trials per instance**:

| instance | parent squares per trial | trials | mismatches |
|---|---:|---:|---:|
| `A1` | 24 | 257 | 0 |
| `A2-F` | 24 | 257 | 0 |
| `A2-B` | 24 | 257 | 0 |

Total single-generator trials: `771`; mismatches: `0`.  Two composite
refinements were also checked below with another `514` trials and zero
cochain-map mismatches.

The identity proves the same criterion as the subject:

```text
J_2(d_1 a):=d'_1 J_1 a
```

is well-defined exactly when `J_1(ker d_1) subseteq ker d'_1`; on
`im(d_1)`, `J_2` is then unique. Flux aggregation follows from the section
equation and the cochain-map identity; no quadratic conclusion follows.

### 1.4 Carrier-level forcing residuals

The independently derived ranks are:

| instance | `dim ker(sd*_1)` | new-vertex gauge | physical quotient | `rank(d_1) × physical` |
|---|---:|---:|---:|---:|
| `A2-F` | 33 | 0 | 33 | **561** |
| `A1` | 184 | 65 | **119** | **2023** |
| `A2-B` | 512 | 65 | 447 | **7599** |

The A1 quotient reproduces the earlier independent `119` census.  All three
residuals match the subject.  The result is carrier-level: closed-cochain
ambiguity is new-vertex gauge, while the displayed residual remains on the
physical non-closed sector.

```text
INCIDENCE_HALF = CONFIRMED
COCHAIN_MAP = REPLICATED
FORCING_LEMMA = CONFIRMED AT CARRIER LEVEL
```

## 2. AS2 — sealed `Q_flux` and naturality — CLAIMED

### 2.1 One implementation, one metric

The test used the packet's unweighted counting products: every oriented cell
has unit weight.  No rescaling, volume weight, generator-dependent factor, or
case-specific tolerance was introduced.

For each coboundary matrix `D=d_1`, contractibility was checked by
`dim ker D = rank d_0`.  Hence the packet formula

```text
P_h=I-d_0(d_0^dagger d_0)^+d_0^dagger,
Q_flux=P_h D^dagger(D P_h D^dagger)^+|im(D)
```

is the Moore-Penrose inverse of `D` on `im(D)`.  It was evaluated by one
economy-SVD routine.  The rank threshold was the standard generated value
`max(m,n) * machine_epsilon * largest_singular_value`, not an adjusted input.

If `U'` is an orthonormal basis of `im(D')`, the minimum-counting-norm physical
flux section of `sd*_2` is

```text
T_g = U' (sd*_2 U')^+ : im(D) -> im(D').
```

The candidate lead is `L_g=sd*_1 Q'_flux T_g`.  Naturality demands
`L_g=Q_flux` on all of `im(D)` for every generator and composite.

### 2.2 Three defining `Q_flux` properties

The full orthonormal image basis—not sampled vectors only—was checked for:

1. `D Q_flux xi = xi`;
2. horizontality, `d_0^T Q_flux xi=0`;
3. minimum norm, equivalently zero projection onto `ker D`.

Maximum absolute residuals `(right-inverse, horizontal, minimum-norm)`:

| complex | three residuals |
|---|---|
| parent | `(9.16e-16, 3.39e-16, 3.76e-16)` |
| `A1` | `(1.55e-15, 1.10e-15, 6.00e-16)` |
| `A2-F` | `(1.40e-15, 5.36e-16, 9.09e-16)` |
| `A2-B` | `(2.39e-15, 2.01e-15, 1.67e-15)` |
| `A1 o A1` | `(4.52e-15, 5.72e-15, 2.50e-15)` |
| `A1` then `A2-F` | `(1.36e-15, 2.25e-15, 9.54e-16)` |

The flux-section right-inverse residual was at most `4.17e-15`.  These checks
validate the implementation before the naturality verdict.

### 2.3 Generator and composite naturality transcript

For every row below, the operator difference was checked on a complete
orthonormal basis of the parent physical-flux space and on **401 independent
random physical fluxes**.  The displayed value is the random-test worst
absolute coordinate deviation; basis errors lead to the same classification.

| refinement | same counting metric? | basis max | random worst | verdict |
|---|---:|---:|---:|---|
| `A1` cubical bisection | yes | `1.04e-15` | `5.11e-15` | equality at numerical precision |
| `A2-F` Freudenthal | yes | `2.4579304868404647e-2` | **`1.2029726825073028e-1`** | **FAIL** |
| `A2-B` barycentric | yes | `1.78e-15` | `7.17e-15` | equality at numerical precision |
| composite `A1 o A1` (grid quarters) | yes | `1.33e-15` | `6.66e-15` | equality at numerical precision |
| composite `A1` then Freudenthal on all child cubes | yes | `2.869438635329976e-2` | **`1.3560931591152436e-1`** | **FAIL** |

Each composite comparison aggregated all refined cells back to the same 24
parent squares.  Each also passed the exact cochain-map identity and 257 random
integer-cochain tests with zero mismatches.  The naturality failures therefore
do not come from an incidence defect.

The same metric and algorithm succeed on two instances and fail on another.
Allowing a Freudenthal-only adjustment would be exactly the prohibited
generator-specific rule.  Since Freudenthal is an admitted oriented simplicial
instance of A2, the universal naturality claim is refuted.

```text
NATURALITY = NOT NATURAL
```

This does not refute the subject's reported single-instance equality. It refutes
the proposed promotion of that equality to one natural carrier over the whole
licensed generator class. The known correction consumers are:

- `STAGE8_B1A_REFINEMENT_CARRIER_DARIO_V001.md` §3.3: candidate lead does not
  survive cross-generator naturality;
- `QUESTIONS_SETTLED_REGISTER_V001.md` Q-698: its conditional “if natural” branch
  is now answered negatively, pending registrar recording.

The incidence half and its residuals are unaffected.

## 3. AS3 — scope, freedoms, flattening, and audit

### 3.1 Scope discipline

- The counting inner product is **consumed and flagged**.  The failure is already
  conditional on that exact Gate-3 input; no metric is adopted or endorsed.
- The coframe half is out of scope and was not attempted.  No `F'/F` relation was
  defined.
- O1 identity/existence clauses are out of scope and were not supplied by this
  check.
- No physical coefficient, volume, response, alpha-facing value, or measured
  constant was evaluated. Floating residuals are diagnostics of commissioned
  finite structural linear algebra.

### 3.2 `FREEDOMS-CONSUMED`

| free datum touched | alignment-law tag | treatment |
|---|---|---|
| counting inner product / unit cell weights | **CONDITIONED-ON** | consumed exactly as sealed; no endorsement or alternative tested |
| choice of minimum-norm representative | **CONDITIONED-ON** | uniquely fixed after the counting metric; not independently selected |
| coarse-to-fine section outside the min-norm lead | **CARRIED-AS-PARAMETER** | no section adopted |
| A2 representative | **CARRIED-AS-PARAMETER** | both Freudenthal and barycentric instances tested; neither substituted for the licensed class |
| refined interior-edge values | **CARRIED-AS-PARAMETER** | no equidistribution, area rule, or field member chosen |
| common-refinement relation | **CONDITIONED-ON** | packet's exact relation retained; no relation authored |
| coframe half / `F'/F` relation | **CARRIED-AS-PARAMETER** | out of scope and absent, not filled |
| O1 generator family | **CARRIED-AS-PARAMETER** | out of scope; no family selected |

`SUBSTITUTED` entries: **none**. Random seeds and SVD rank thresholds are test
instrument settings, not physical freedoms; they are disclosed above and do not
vary by generator.

### 3.3 Flattening check

- S26 (`DECLINE_REGISTER_V002.md[10631,10949)`, span SHA
  `9cfa74c5031c4690348c9b3cf79ace86549ce8dce0c81a78194d018e9b438ec7`)
  remains intact. No `C_ref` smooth constituent, smooth coframe, or smooth
  connection was used as a source.
- S08 (`DECLINE_REGISTER_V002.md[3879,4287)`, span SHA
  `15fdbb0216cd7066b37b2b884bba0f2f9116d8e1118fae24af4f7541fcffd5d1`)
  remains intact. The discrete matrices are not identified with electromagnetism,
  Maxwell data, a response object, or a smooth public field.
- No common cell was formed and no junction map was evaluated.

### 3.4 Battery and self verb audit

- **Adversarial first:** the subject's incidence claims were treated independently;
  the minimum-norm lead was tested only after their reproduction.
- **Exact-before-floating:** integer cochain identities and ranks were checked before
  pseudoinverse residuals.
- **Anti-tuning:** identical weights, code path, rank rule and trial count across
  generators; the failing instance received no adjustment.
- **PIN CHECK:** all load-bearing source and packet spans were independently hashed.
- **Claim-status discipline:** `confirmed` and `refuted` below are this lane's
  `CLAIMED` determinations pending registrar/cross-lane handling.
- No register, plan, tracker, git, member-binding, fixed-point, end-test, common-cell,
  junction-map, or chain action occurred.

INCIDENCE_HALF = CONFIRMED
DIRECTION_THEOREM = CONFIRMED
COCHAIN_MAP = replicated (257 trials each on A1, A2-Freudenthal, A2-barycentric; 771 total, 0 mismatches; exact matrix mismatches 0)
FORCING_LEMMA = CONFIRMED (residuals match: 561 Freudenthal / 2023 A1 with physical quotient 119 / 7599 barycentric)
QFLUX_PROPERTIES = validated (complete image-basis checks; worst residual 5.72e-15)
NATURALITY = NOT NATURAL (A2-Freudenthal random worst deviation 1.2029726825073028e-1; A1-then-Freudenthal composite 1.3560931591152436e-1; same counting metric, no adjustment)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (all headlines CLAIMED; metric dependence consumed and flagged; coframe/O1 out of scope; zero substitutions)
