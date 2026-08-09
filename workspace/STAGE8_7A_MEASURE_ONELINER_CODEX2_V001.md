# Stage 8 / 7A Step 8 — forced measure one-liner and coframe closure

**Lane:** CODEX 2  
**Relay:** 756  
**Governing determination:** Q-660; forced content displayed in `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` §2.5

## 0. Preflight, custody, and gates

The relay inbox seal verified before its contents were read. The required output names and their sidecars were absent in the cleanroom and archive before the first write. All source hashes below were checked before use. Packet members were verified through the sealed Stage 7 packet manifest; workspace artifacts were verified through their adjacent seals.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_binding = false
fixed_point_execution = false
end_test = false
physical_quantity_numeric_evaluation = false
measured_constant_comparison = false
```

The determinant, permutation, and normalized-cell counts below are exact structural arithmetic commissioned by this relay. They do not evaluate a physical quantity or compare one to a measured constant.

## 1. Cross-family forcing-envelope check

The content of §2.5 was checked against every family it cites before the addendum was authored.

| Carrier | Sealed source and pin | Span checked | Span SHA-256 | Check result |
|---|---|---:|---|---|
| unique intrinsic flat-cell measure | packet `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md`, `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2` | `[98,309)` | `0019d614c9fa71668c5273aa4d7dca3698072532bb100e389d1cb10c4b53943f` | uniquely gives `mu_D(A) = Vol_4(A)/Vol_4(D)` |
| child-intrinsic selection | packet `R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md`, `e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59` | `[551,740)` | `fcc2db2591d172c912a071f9265fd39774ee2cb03061df2929bac4eb0a952b9b` | promoted child uses its intrinsic measure, not a parent weighting |
| general-coframe quantifier | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md`, `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | `[45718,46387)` | `22c1fd7bdb9500ea47236ea3b7328f0c0ed439a42a1e43ab881827b29b53e69f` | carries the orthogonal formula and the unchanged general-coframe quantifier |
| general-coframe volume multiplier | same V011 packet member | `[46074,46387)` | `dffd13b31d56c212bb69a86ff522600f0b95b5f229dd702f0e9886c96edc8c43` | multiplier is `|det e|` |
| working-class cell constructions | `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md`, `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | `[19632,19996)` | `b3c67e8c433385a4cb519c2f564649e98b2a9686491487db663592b4b48d6b43` | 16 cubical children at `1/16`; 24 order-simplices at `1/24` |

No cited span drifted. The five checks jointly force the displayed §2.5 denotation without a measure, weight, normalization, or convention choice.

## 2. Sealed finite addendum

The finite spec addendum is:

```text
STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md
SHA-256 = 9ae682eb7834304d329603d50f1b666152899e84f939324aa43d6f138660626d
seal sidecar SHA-256 = e99ea881e34a1dcaf39c44e4acdaabd3f2fb0bd0788c70d19337af924563d942
```

An exact byte comparison of the addendum's operative block against `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` lines 279–295 returned equality. The addendum therefore records, without amendment to V011, that the existing volume factor denotes the already-classified intrinsic four-volume: `|det e|` is its parallelepiped evaluation and `|det E|/d!` is its simplex evaluation.

## 3. The coframe transport, displayed whole

### 3.1 Generator `A1`

For a parent orthogonal coframe `e = diag(ell_0, ell_1, ell_2, ell_3)`, cubical bisection assigns each of its 16 children

```text
T_A1(e) = diag(ell_0/2, ell_1/2, ell_2/2, ell_3/2).
```

The child coframe is computed from the child's own extents, as required by the sealed R33 child-intrinsic rule. Iteration is composition: after `n` cubical bisections the carried coframe is `diag(ell_0/2^n, …, ell_3/2^n)`. This preserves the prior `A1 = DERIVED` determination.

### 3.2 Generator `A2`: construction

For each permutation `p` of `(0,1,2,3)`, the order-simplex has vertices

```text
v_0 = (0,0,0,0)
v_k = sum_(j=0)^(k-1) e_(p(j))       for k = 1,2,3,4
```

and its transported tetrad/frame datum is the edge-frame `E_p` whose rows are `v_k-v_0`. Thus the sealed coordinates select the frame; no normalization or additional datum is chosen. In a pre-existing parent coframe chart, this is the composition of the parent coframe with `E_p`; the table below uses the sealed unit-cube chart.

### 3.3 Generator `A2`: all 24 frames and the measure denotation

In the frame column, semicolons separate the four rows of `E_p`.

| `p` | `E_p` | `det E_p` | `|det E_p|` | intrinsic `Vol_4(C_p)=|det E_p|/4!` |
|---|---|---:|---:|---:|
| `(0,1,2,3)` | `1000;1100;1110;1111` | `+1` | `1` | `1/24` |
| `(0,1,3,2)` | `1000;1100;1101;1111` | `-1` | `1` | `1/24` |
| `(0,2,1,3)` | `1000;1010;1110;1111` | `-1` | `1` | `1/24` |
| `(0,2,3,1)` | `1000;1010;1011;1111` | `+1` | `1` | `1/24` |
| `(0,3,1,2)` | `1000;1001;1101;1111` | `+1` | `1` | `1/24` |
| `(0,3,2,1)` | `1000;1001;1011;1111` | `-1` | `1` | `1/24` |
| `(1,0,2,3)` | `0100;1100;1110;1111` | `-1` | `1` | `1/24` |
| `(1,0,3,2)` | `0100;1100;1101;1111` | `+1` | `1` | `1/24` |
| `(1,2,0,3)` | `0100;0110;1110;1111` | `+1` | `1` | `1/24` |
| `(1,2,3,0)` | `0100;0110;0111;1111` | `-1` | `1` | `1/24` |
| `(1,3,0,2)` | `0100;0101;1101;1111` | `-1` | `1` | `1/24` |
| `(1,3,2,0)` | `0100;0101;0111;1111` | `+1` | `1` | `1/24` |
| `(2,0,1,3)` | `0010;1010;1110;1111` | `+1` | `1` | `1/24` |
| `(2,0,3,1)` | `0010;1010;1011;1111` | `-1` | `1` | `1/24` |
| `(2,1,0,3)` | `0010;0110;1110;1111` | `-1` | `1` | `1/24` |
| `(2,1,3,0)` | `0010;0110;0111;1111` | `+1` | `1` | `1/24` |
| `(2,3,0,1)` | `0010;0011;1011;1111` | `+1` | `1` | `1/24` |
| `(2,3,1,0)` | `0010;0011;0111;1111` | `-1` | `1` | `1/24` |
| `(3,0,1,2)` | `0001;1001;1101;1111` | `-1` | `1` | `1/24` |
| `(3,0,2,1)` | `0001;1001;1011;1111` | `+1` | `1` | `1/24` |
| `(3,1,0,2)` | `0001;0101;1101;1111` | `+1` | `1` | `1/24` |
| `(3,1,2,0)` | `0001;0101;0111;1111` | `-1` | `1` | `1/24` |
| `(3,2,0,1)` | `0001;0011;1011;1111` | `-1` | `1` | `1/24` |
| `(3,2,1,0)` | `0001;0011;0111;1111` | `+1` | `1` | `1/24` |

The frame data are those independently derived and sealed in `STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md` §1.3: `det E_p = sgn(p)` for all 24 and `|det E_p|=1`. The new addendum supplies the previously missing receiving denotation:

```text
mu(C_p) = Vol_4(C_p) = |det E_p|/4! = 1/24
sum_(p in S_4) Vol_4(C_p) = 24 * (1/24) = 1.
```

The frame and measure now agree on the same child object. No rescaling of `E_p` occurs; the exact `1/4!` is simplex combinatorics, not a tetrad normalization. Therefore `A2 = DERIVED`.

### 3.4 Finite composites

The working class is generated by `A1` and `A2` and closed under finite composition. The coframe transport on a composite `g_n ∘ … ∘ g_1` is the ordered composition

```text
T_(g_n ∘ … ∘ g_1) = T_(g_n) ∘ … ∘ T_(g_1),     g_i in {A1,A2},
```

with the identity transport for the empty composite. Both receiving maps are now defined on their generator domains: `A1` takes child extents; `A2` takes the coordinate-determined edge-frame and the addendum's intrinsic simplex measure. Hence every finite composite has a derived coframe transport; no composite is inferred from a missing generator case.

```text
COFRAME_A1 = DERIVED
COFRAME_A2 = DERIVED
COFRAME_COMPOSITES = DERIVED by ordered composition
```

## 4. RA27-3 board update

This relay changes only the coframe row. The earlier frontier and the independent simplicial-coframe check supply the old state; the sealed addendum discharges their named `A2` measure-denotation gap.

| # | Field | Previous verdict over the working class | Updated verdict | Basis / change |
|---|---|---|---|---|
| 1 | incidence — four-volume half | **SUPPLIED** | **SUPPLIED** | unchanged |
| 1b | incidence — cochain half | **GAP NAMED** | **GAP NAMED** | unchanged; subdivision chain map remains unsealed |
| 2 | degree | **UNDERDETERMINED**, obstruction out of scope | **UNDERDETERMINED**, obstruction out of scope | unchanged |
| 3 | coframe | **PARTIAL** — `A1` derived; `A2` frame derived but measure denotation unresolved | **CLOSED / DERIVED** — `A1`, `A2`, and finite composites | `A2`'s 24 frames plus sealed intrinsic-volume denotation |
| 4 | connection | **UNDERDETERMINED** — refined edge assignment free on the recorded `A2` instance; `A1` untested | **UNDERDETERMINED** | unchanged |
| 5 | volume | **SUPPLIED** | **SUPPLIED** | unchanged |
| 6 | support | **UNDERDETERMINED** | **UNDERDETERMINED** | unchanged |
| 7 | current density | **UNSUPPLIED** | **UNSUPPLIED** | unchanged |

The coframe field closes. RA27-3 as a whole remains partial because the independently named incidence, degree, connection, support, and current-density remainders are untouched.

## 5. Pin closure, dry-run, and audit

Nine load-bearing authorities in this relay's two new records resolve to sealed bytes:

| Alias | Artifact | SHA-256 |
|---|---|---|
| `FORCING` | `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` | `9685af44cc48f01fb04e57329cedf4f9a871eb393c6d41396179776957287e9b` |
| `R33G` | packet `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md` | `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2` |
| `R33` | packet `R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md` | `e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59` |
| `V011` | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` |
| `MAJ` | `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` |
| `753` | `STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md` | `d6f490b80e8d8775af9ee54095e34da03a4af01541736e2cb138f366c2caa75e` |
| `751` | `STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md` | `4d072e7671113357764b61e11ef1d3d336ce34e307ba07c545ec7cf1a38a6abc` |
| `750` | `STAGE8_7A_RESTRICTED_BOOKING_DARIO_V001.md` | `57c5522109ef5bd48f7952a290df034b9c9d3c5c2db3d6b97f972172987b2ca9` |
| `ADDENDUM` | `STAGE8_7A_MEASURE_DENOTATION_SPEC_ADDENDUM_CODEX2_V001.md` | `9ae682eb7834304d329603d50f1b666152899e84f939324aa43d6f138660626d` |

There is no executable path in this relay: it authors one text addendum and one text disposition, so no dry-run applies. The chain was not invoked.

Self verb audit: **CLEAN**. The report derives only the commissioned structural transport, applies the principal-forced denotation, preserves every unaffected board row, and does not claim RA27-3 closure, proof authorization, or a physical result.

FORCING = envelope-checked (spans verified)
ADDENDUM = sealed (byte-faithful to §2.5)
COFRAME = CLOSED (both generators; displayed)
BOARD = updated
PIN_CLOSURE = 9 hits, all resolved
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
