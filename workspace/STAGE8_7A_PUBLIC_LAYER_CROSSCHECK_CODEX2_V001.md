# STAGE 8 / 7A / Q-126 ROUTE — ADVERSARIAL CROSS-CHECK OF THE PUBLIC-LAYER CORE

Lane: CODEX 2 (independent cross-check). Relay 778.

## Lead verdict

The sphere-sector algebra survives, but the claimed scalar trace and its uniform
`+1` positivity do not.

The sealed tower authority does **not** identify `Phi^dagger Phi` with `1`. It
defines

```text
H_0 = D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent
```

and writes the corresponding tower with `[Phi^dagger Phi]`, while expressly
withdrawing the earlier identification of the separate `+1` with
`Phi^dagger Phi`. The subject instead substitutes `+1` and then treats the
result as a scalar exact spectrum. That substitution has no receiver in the
sealed stock and is contradicted by the cited source. The same source also says
that the factor `x16` is flat **only if** the flux `U(1)` is external to
`Spin(10)` with flat parent connection, while the parent bundle/class remains
unselected.

Consequently:

- the arithmetic `32 = 2 x 16` and the displayed sphere weights are correct
  under the source's stated flat-parent condition;
- the unconditional trace formula in the subject is **REFUTED**;
- the universal bound `lambda >= 1 + C2_parent` is **REFUTED** by an admissible
  symbolic completion with a torus zero mode, a nonempty monopole zero mode,
  and `Phi` acting as zero;
- the `S^2` branch partition itself is **CONFIRMED**;
- the `q=0` endpoint reproduces the displayed untwisted squared-Dirac levels
  and degeneracies exactly;
- the one-kind/two-kind fork is structural for the `S^2` carrier, but the
  subject's asserted full-`H_0` bottom values are not established.

No determinant was formed. No bundle class was adopted or eliminated. The
counterexample below is a universal-claim test across the open family, not a
selection of its witness.

---

## 0. Preflight and custody

### 0.1 Relay, output, and subject

- Relay bytes: `RELAY_PASTE_778_PUBLIC_LAYER_CROSSCHECK_CODEX2_V001.md`,
  SHA-256 `98a45cf8958aa9d1750d368a6095f111c84506dca657ec39220c13eaa4e25391`;
  sidecar verified before reading.
- Pickup acknowledgement: `relay_outbox/778_ACK.md`.
- Output artifact and sidecar were absent before the first output write.
- Subject: `STAGE8_7A_DBR_PUBLIC_LAYER_CAMPAIGN_DARIO_V001.md`,
  SHA-256 `083e86e357a63e0ae6cec707e966f14e4161f9c6ece169f852c3231f8df5c450`;
  adjacent seal verified before reading.

### 0.2 Subject pin list: 9/9

| ID | Pinned object | Verified SHA-256 | Custody result |
|---|---|---|---|
| DEC | `DECISION_SELECTOR_OPEN_AND_GAP_CLASSIFICATION_2026-08-09.md` | `cbdc9432de77b29b4ec5fcf1f4f1e9bfb4a185f661b656b98b56103a39257bfb` | adjacent seal `shasum -c`: OK |
| 762 | `STAGE8_7A_DBR_PUBLIC_LAYER_DARIO_V001.md` | `beff9f11263e6d9069d77980ea5fc455ae0ea65e1f4ee9629ba6415937a8b075` | adjacent seal: OK |
| 768 | `STAGE8_7A_TOWER_CONTEST_DARIO_V001.md` | `03db8d3da273f42c62acdea5d453ec0b780934c73aa897fdf2cfb986c0e7bc9b` | adjacent seal: OK |
| 770 | `STAGE8_7A_FLUX_CORRESPONDENCE_DARIO_V001.md` | `3c6cd9a2ee1b6ea1093370e9868c93a200c3631317bb91ecaf3ec9153a744c0b` | adjacent seal: OK |
| 773 | `STAGE8_7A_MAGNETIC_SECTOR_HUNT_DARIO_V001.md` | `54d9cb5af3c6bb3d1dddd79a00f5f7954c167fb76f65d60272f480275d7ef2d2` | adjacent seal: OK |
| PRIN | `alpha_global_record_surface_superconnection_principle_v001.md` | `ae1d04922cb37f8b5631a11551b7db57f483bd6b0d8b7c54d59b4f4ae593768f` | byte-exact to the pin in the sealed subject and SPEC manifest; this mirrored foundational source has no adjacent sidecar |
| SPEC | `STAGE8_COMPLETE_PUBLIC_DBR_LBR_SPECTRAL_THEOREM_SPEC_V001.md` | `a751b72cf64625bf4140806b351fd7d06a2065febeb405cc1021ca3975f6dbec` | adjacent seal: OK |
| GAP | `STAGE8_BR_CLOSURE_OPERATOR_STRUCTURAL_SPECTRAL_GAP_DETERMINATION_V001.md` | `e2fc00d21fdc4a1844648b7248140ab05d9205a652a2b42330c1a366d53e33ed` | adjacent seal: OK |
| SPEC1 | `STAGE8_BR_CLOSURE_OPERATOR_SPECTRUM_AND_SEAM10_IDENTITY_DETERMINATION_V001.md` | `de88ba684da719dcd5b2d37b781b2d85d10ef15dbb2043c6191b5f1e6f140804` | adjacent seal: OK |

The PRIN custody form is not silently upgraded: 768 itself records that its
`ae1d0492...` bytes are digest-matched to SPEC's sealed manifest. The exact
bytes reproduced that content pin here.

PE-5 and PE-6 were recorded as zero-weight exclusions and were **not opened,
searched, or consulted**.

### 0.3 Gates

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member binding = none
fixed-point execution = none
end test = none
physical-quantity numeric evaluation = none
measured-constant comparison = none
determinant evaluation = none
bundle-class adoption/elimination = none
```

All arithmetic below concerns exact integer/rational spectral labels and
multiplicities only.

---

## 1. Half-open evidence spans and meaning probes

All span digests cover the exact half-open byte interval stated.

| Ref | Source digest; span; span digest | Meaning probe |
|---|---|---|
| T1 | subject `083e86e3...`; `[7072,8519)`; `6da83b9032d8644378183271b53e11df33b2ff07ff65066934a2436af781f340` | The target trace, `32`, both `d_S2` formulas, and the exactly-two assertion—not merely a later summary. |
| T2 | subject `083e86e3...`; `[8994,11222)`; `7ad316e6b7916459f3cc5e9fa44cdbcd38a8e2682d21a91450038b1ba8684512` | The target Z/P branches, bottom table, `q=0` endpoint test, and both-class admissibility claim. |
| T3 | subject `083e86e3...`; `[11316,12616)`; `4fe2976b4ad19fb68151b276ed504d2db5dace09337a553dfc8ea5ac14bf5a8a` | The target universal positivity inequality and its claimed `+1` source. |
| S1 | 768 `03db8d3d...`; `[10764,11705)`; `d08cccc778b13b4422097cefba00247c28f7dbe960668481328684ec16274dc2` | The corrected definition of `H_0`, the exact twisted-product term, multiplicity, both `d_S2` cases, flat-`x16` condition, and the non-scalar status of the full operator. |
| S2 | 768 `03db8d3d...`; `[6410,6885)`; `4b6102e985b7a7228333083e8f6a222c369f0609c32a150f9ede315538d889b7` | Express withdrawal of the identification `+1 = Phi^dagger Phi`; it is not merely absence of a binding. |
| S3 | 768 `03db8d3d...`; `[6886,8591)`; `b182f64260d8391a2c8387c0ea48814ae953ba12417c21ee88f582d427595638` | Piecewise multiplicity and exact untwisted-floor algebra, including why `q=0` remains admissible. |
| S4 | 768 `03db8d3d...`; `[12531,13738)`; `2311f816cbe5f133a6b6d972ebbeeb0bb1666ce04f7a4567c97cc25fc3a57ce4` | The five unselected data classes, including torus spin structure, parent bundle/class, odd profile, and chiral index. |
| S5 | 770 `3c6cd9a2...`; `[9917,10510)`; `a51a7a8d30582435f0926f67c8b60d74ab7d44f5d724c61c5b71a5ab02aab07c` | `deg L=2q` and the orientation/chirality sign; distinguishes signed chirality from magnitude dependence. |
| S6 | 770 `3c6cd9a2...`; `[12123,13036)`; `321b8ba66cbb8337fbfa2a75403f3a946aa9d3f7f8cf1c96d48ad281a3e67207` | `q=0` remains in the surviving set and differs from `|q|=1/2` in zero-level occupancy. |
| S7 | PRIN `ae1d0492...`; `[867,1483)`; `f15851ffccd6d14b959b0fb7d33799bdb663da4a33dea4cf8c6c2af92a3ff19b` | The actual superconnection square and rank-16 parent carrier; contains `Phi^dagger Phi`, not an identity substitution. |
| S8 | PRIN `ae1d0492...`; `[1484,2361)`; `98a5fc88fc1914a7c80e657497fc6dbe1aaa10d0933983adc7ecf454b5f0e70f` | The unselected radii, spin structure, parent bundle/class, odd profile, and index, plus the route's hard-failure rule. |
| S9 | GAP `e2fc00d2...`; `[10402,11576)`; `7c15e2129d58ec21e66c259fc7ab4afb3bc132c6016567b3653b3255dd3ea403` | Positive-semidefinite terms do not force a uniform strictly positive public bottom; the `Phi`-kernel countermodel is explicitly admitted. |
| S10 | DEC `cbdc9432...`; `[55,945)`; `5ffe62af47f95ddd767fec065af9c53ce8bb9ff38a54bcb83ea373546afdc02a` | The class stays open and selector-before-determinant bars adoption and determinant evaluation. |

M-2 controls were applied to `Phi^dagger Phi` / `Phi†Phi`, `zero mode` /
`zero-mode`, `C2_parent` / `C2,parent`, and the split-line forms of the trace and
multiplicity statements. No meaning-bearing hit used a glossary, requirement,
or same-name/different-object collision as evidence.

---

## 2. AS1 — trace form and the third-entry hunt

### 2.1 What the sealed tower actually supplies

From S1, the cited tower is

```text
H_0 := D_(Sigma,A)^2 + Phi^dagger Phi + C2_parent

spec(H_0) = {p_t^2 + p_q^2 + ell(ell+2|q|)}
            + [Phi^dagger Phi] + C2_parent,

multiplicity = [2 N_lattice(p_t,p_q)] d_S2(ell) 16,
d_S2(0) = 2|q|,
d_S2(ell>=1) = 4(ell+|q|).
```

S2 expressly says that the separate `+1` displayed in an earlier background
formula is **not bound** to `Phi^dagger Phi`. S7 independently displays the
superconnection square with `Phi^dagger Phi`. S4/S8 leave `Phi` unselected.

Therefore the subject's replacement

```text
[Phi^dagger Phi]  ->  +1
```

is not a reparametrization. It changes an unselected positive-semidefinite
operator into a fixed scalar. Without a proof that it is the identity and
commutes with the remaining tower, the scalar spectral sum for `Tr f(H_0)` does
not follow.

There are two further bounded qualifications:

1. `32 = 2 x 16` is exact arithmetic and agrees with the multiplicity carrier,
   but S1 makes flatness of `x16` conditional on an external flux `U(1)` and a
   flat parent connection. The parent bundle/class is unselected (S4/S8), so
   `32` is not established uniformly over every admissible completion.
2. The source writes `N_lattice(p_t,p_q)`. A sum over a declared lattice
   **multiset** could absorb it, but the subject declares only
   `SUM_(p_t,p_q in Lambda)` and supplies no multiset convention. The constant
   `32` is correct; suppression of `N_lattice` is not independently bound.

The target trace is thus **REFUTED** by the fixed-`+1` substitution alone, with
the parent-flatness and lattice-counting issues reinforcing the failure.

### 2.2 Affine-entry census

For the sealed `S^2` squared-Dirac data in S1, exact expansion gives

```text
d_S2(0)       = 2|q|,
d_S2(ell>=1)  = 4ell + 4|q|,
ell(ell+2|q|) = ell^2 + 2ell|q|.
```

No third **magnitude** entry appears in those displayed eigenvalue and
multiplicity formulas. The four requested surfaces were checked:

| Surface | Result |
|---|---|
| normalization/radii | radii rescale the momentum and angular terms but the displayed scaling weights carry no additional `|q|` factor |
| measure | no separate `q`-dependent measure is present in the sealed trace data; degeneracy is already in `d_S2` |
| label set | `ell=0,1,2,...` is the displayed uniform reindexing; occupancy at `ell=0` is encoded by `d_S2(0)` |
| parity pairing | `ell>=1` is paired and `ell=0` is unpaired for every magnitude; the **sign** of `q`, not `|q|`, selects the zero-mode chirality (S5) |

The narrow two-magnitude-entry statement is therefore confirmed **for the
displayed `S^2` spectral/multiplicity law**. Its promotion to the *entire*
`H_0` trace is not confirmable: S1's `x16` is conditional, and the unselected
parent embedding/connection and `Phi` operator are outside that two-slot
census. This is an exhaustion boundary, not a manufactured third formula.

Verdicts:

```text
TRACE FORM: REFUTED.
32: exact under the stated flat-parent condition; not uniform over the open family.
d_S2 forms: CONFIRMED.
THIRD |q| ENTRY in displayed S^2 data: none found.
GLOBAL exactly-two claim for H_0: UNVERIFIABLE from stock; parent embedding/flatness
and Phi action are the named open elements.
```

---

## 3. AS2 — branch claims and counterexample search

Define only the sphere-sector contribution

```text
a_q(ell) := ell(ell+2|q|).
```

### 3.1 Branch Z

At `ell=0`,

```text
a_q(0) = 0,
d_S2(0) = 2|q| = |deg L|.
```

S1 labels this the zero-mode level and S3 records it as unpaired. S5 records
that its chirality is selected by orientation/sign. Hence, whenever the level
is occupied, it is an unpaired single-chirality sector and its `S^2` squared
eigenvalue contribution is exactly zero.

### 3.2 Branch P

For every admissible `ell>=1` and every `|q|>=0`,

```text
ell >= 1,
ell + 2|q| >= 1,
therefore ell(ell+2|q|) >= 1 > 0.
```

S1 gives the paired multiplicity `4(ell+|q|)`. The attempted boundary
counterexamples fail:

- `q=0, ell=0` has zero multiplicity and is not a state;
- `|q|>=1/2, ell=0` belongs to Z, not P;
- no admissible P label has `ell<1`;
- neither torus momentum nor spin structure can make the positive **sphere
  contribution** negative.

The Z/P branch claim is **CONFIRMED as a statement about the sealed `S^2`
factor**. It does not repair the subject's scalarization of the whole `H_0`.

---

## 4. AS3 — positivity bound: explicit admissible witness

The subject proves `lambda >= 1+C2_parent` only after inserting its unsupported
`+1`. The sealed operator instead permits the following completion for the
purpose of testing the universal quantifier:

```text
q = 1/2                    -> d_S2(0)=1, so the ell=0 state exists
ell = 0                    -> ell(ell+2|q|)=0
periodic torus spin data   -> p_t=p_q=0 is an allowed torus zero label
Phi = 0                    -> Phi^dagger Phi=0 and the cross term is also zero
flat external parent arm  -> choose any C2_parent eigenstate in the conditional
                              flat-x16 realization recorded by S1
```

This is a standard member of the open family: S4/S8 leave the spin structure,
parent bundle/class, and odd profile unselected; S9 expressly says the corpus
permits a `Phi^dagger Phi` kernel. No sealed condition requires a nonzero odd
profile or excludes periodic torus spin data. The test does not adopt the
completion; it asks whether a claim quantified over **every** admissible class
survives one allowed member.

For that state, using the actual S1 operator,

```text
lambda = 0 + 0 + 0 + C2_parent = C2_parent,
```

so

```text
lambda >= 1 + C2_parent
```

is false by the exact symbolic difference `-1`. No value of `C2_parent` is
evaluated; the same term occurs on both sides. Changing any of the other four
free-data classes cannot rescue a universal statement after this admissible
witness. The best bound supplied by positive semidefiniteness on this completion
is `lambda >= C2_parent`, not `1+C2_parent`.

`POSITIVITY = REFUTED` for the claimed uniform `+1` bound.

---

## 5. AS4 — exact `q=0` validation and structural fork

### 5.1 Untwisted endpoint

At `q=0`, branch Z has

```text
d_S2(0)=0,
```

so it contains no state. The nonempty ladder begins at `ell=1`. For
`ell=1,2,3,4`, exact substitution in S1 gives

| `ell` | `ell(ell+2|q|)=ell^2` | `d_S2(ell)=4ell` |
|---:|---:|---:|
| 1 | 1 | 4 |
| 2 | 4 | 8 |
| 3 | 9 | 12 |
| 4 | 16 | 16 |

These are exactly the requested untwisted `S^2` squared-Dirac levels and total
squared-level degeneracies. This check evaluates no physical quantity; it is
integer substitution into the displayed spectrum.

### 5.2 Nonzero quantized class

The displayed degree relation is `deg L=2q`. For `|q|>=1/2`,

```text
d_S2(0)=2|q| >= 1,
a_q(0)=0.
```

Thus Z is nonempty. For `q=0`, it is empty. S6 and S10 confirm that both class
kinds remain in the open admissible family.

The fork is therefore structural in the precise bounded sense:

```text
q=0         -> only the paired nonempty S^2 ladder P
|q|>=1/2    -> unpaired zero-mode sector Z plus paired ladder P
```

What does **not** follow is the subject's full-operator bottom
`p_min^2 + {0 or 1} + 1 + C2_parent`: its second `+1` is the refuted
scalarization of `Phi^dagger Phi`, and the open spin structure controls
`p_min`. The fork in sphere-sector kind is confirmed; the asserted full-`H_0`
bottom formula is refuted.

---

## 6. Battery and self audit

### 6.1 Adversarial controls

- **F_PLDEC:** only symbolic family statements and exact dimensionless labels
  were manipulated. No member was bound as the physical class.
- **Counterexample direction:** the universal positivity claim was attacked at
  the most permissive edge—nonempty monopole zero mode, torus zero mode, and
  odd-profile kernel.
- **Rescue direction:** the source's conditional `32`, exact `d_S2` laws, P/Z
  partition, and `q=0` arithmetic were retained rather than discarded with the
  scalar trace.
- **Family-before-determinant:** no `f` was chosen, no sum was evaluated, and no
  determinant was formed.
- **Selector-open:** the witness is not an adopted class and changes neither the
  bundle ledger nor the board.
- **PE exclusion:** PE-5/PE-6 were not consulted.
- **Pre-seal pin check:** subject plus source list reproduced at 9/9; all eight
  adjacent source seals returned `OK`, PRIN reproduced the sealed-manifest
  content pin, and the cited span digests were recomputed from the final source
  bytes.

### 6.2 Verb audit

`derived`, `confirmed`, and `refuted` above are scoped to the cited operators
and exact formulas. “Admissible witness” means a countermodel not excluded by
the sealed open-family constraints; it is not a principal selection. “Standard
untwisted spectrum” is reproduced from the sealed parametrization itself, not
imported as an uncited external theorem. No authorization, proof completion,
physical evaluation, bundle selection, or determinant result is claimed.

---

TRACE_FORM = REFUTED (sealed H_0 carries unselected Phi^dagger Phi, not +1; flat x16 is conditional)
THIRD_Q_ENTRY = none found (in displayed S^2 law; global H_0 exclusivity unverified because parent/Phi are open)
BRANCH = CONFIRMED
POSITIVITY = REFUTED (witness: q=1/2, ell=0, p_t=p_q=0, Phi=0 gives lambda=C2_parent)
FORK_STRUCTURAL = CONFIRMED (S^2 branch kind; asserted full-H_0 bottoms not confirmed)
Q0_VALIDATION = reproduced exactly
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+bounded trace, branch, witness, and fork scopes displayed)
