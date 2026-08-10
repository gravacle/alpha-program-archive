CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 8 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_RESULTS = CLAIMED until the opposite-lane check
```

| # | Closed member | SHA-256 / bounded span SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_949_SDN_CONSTRUCTION_DARIO_V001.md` | `4f18237a1ee5b4ab4a9a3420c4a41aa7eb6ef9eea2eb58b7b0ab72b31156525e` | assignment |
| 02 | `LINE6_SITTING_DECISION_OF_RECORD_V001.md` | `00b77a0887bb84ea2a87384b78d52a775c7e882ee99f054dac075c56697018b3` | the principal's SD-N entry and Galerkin deferral |
| 03 | `STAGE8_AXN_SLICING_DECISION_INSTRUMENT_CODEX2_V001.md` | `08a13df40f8f08deb2727e5313162c5362c2d03f0a19db0c3855cb7de451bd8b` | the governing instrument and the SD-N route fields |
| 04 | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` | the sealed parent |
| 05 | — branch `[3519,4287)`; carrier `[4287,5711)` | `1c7e13ae6b9605f152a19f944e014d627ee2675b8ce8d4ced0a3364bd58d411c`; `87e404a0a6d8a6dec443b7bdafb00b2c1ed60d115e781cb1b04443e6d1fa5c78` | the globally hyperbolic SPIN branch; `Sigma` and `K_Sigma` |
| 06 | — parent `[5711,6867)`; descend `[6867,7879)` | `eddc2e9ab66e1036e7defdc514b61214e0adef3b48fced3c3aa7a67b6df5f2c3`; `827cf361f052d36c62e7fc6ea57e61c04cf8c18fc552dcde18bd7ee5e5ef8e3a` | `h_K`, `S_n`; `D_K` and `C_K(x)` |
| 07 | `STAGE8_AXN_SUPPLEMENTS_DARIO_V001.md`, localisation `[6748,8128)` | `2a829a35eb5fb6cf0b8dc1ca8c4c07848684d1958a787cadb070f4dcc0df8ba9`; `92344fe5c004f460602c17edf2c95e2313e4b95ca347d636cf8412af220dd82e` | my 920 — what the slicing must supply, and what it must not re-author |
| 08 | `STAGE8_AXN_GALERKIN_CROSSCHECK_DARIO_V001.md`; `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `7dce7e71c21bba61157433bd63de6491aa66543a654665f1b0f4f70e0203b5b6`; `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | the confirmed sharp-cell `S_2` result; state pin, process law, S01-S37 |

```text
BOTH GOVERNING SEALS VERIFIED BEFORE READING.  NO PHYSICAL QUANTITY IS NUMERICALLY EVALUATED.
WHAT THE RECORD ALREADY SUPPLIES IS CARRIED AS GIVEN -- IN PARTICULAR S_n.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN SD-N SLICING INSTANCE — DARIO LANE — V001
## RELAY 949 — `[PLAN:AXN-BUILD-D48]` — THE PRINCIPAL'S ENTERED ROUTE, BUILT

Date: 2026-08-10
Status: **EIGHT OF NINE FIELDS COMPLETE. The write half of the slice identity is PROVED exactly and
lands on the record's own `S_n`. The differential half STOPS, with the freedom named: `h_0[g,a]` is a
sealed symbol with no sealed formula, so there is nothing to prove equality against. CLAIMED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Role and discipline

I am the **builder** here. I checked this instrument at 946 and ruled it READY; the principal then
entered SD-N on it. That gives this construction **no extra standing** — it is CLAIMED until the
opposite lane checks it, and I certify none of it.

The operative rule is the relay's stop discipline: **any field needing a datum beyond the entry and
the sealed spans stops with the freedom named.** At 920 I declined to write a textbook identity that
would have read like a derivation. §5.2 below is the same refusal at a smaller margin, and I make it
for the same reason.

## 2. `Sigma_0` — declared from sealed ground, not chosen [FIELD 1: COMPLETE]

Member 05's carrier span states, verbatim:

```text
On a Cauchy surface `Sigma`, let
K_Sigma=L2(Sigma,S tensor L^q);
```

**`Sigma_0 := Sigma`, the Cauchy surface the sealed carrier is already built on.** This is a naming
of a sealed object, not the selection of a new surface: `K_Sigma` — the codomain the whole receiver
argument runs through — is defined over it. No freedom is consumed. The branch span additionally
seals a **globally hyperbolic spin spacetime**, which is what makes a Cauchy surface available at all
and supplies the spin structure used in field 7.

## 3. The entered normal-flow data [FIELDS 2-6: COMPLETE]

```text
FIELD 2  hypersurface family : Sigma_s := exp_perp(Sigma_0 x {s}), the image of Sigma_0 under
                               normal geodesic flow at parameter s, on the scope of field 8
FIELD 3  T = n               : the flow vector is the sealed unit normal n (the parent's own n,
                               the one appearing in slash(n) and S_n)
FIELD 4  N = 1               : entered
FIELD 5  beta = 0            : entered
FIELD 6  normal-parameter    : s is proper time along the normal geodesics, s|_(Sigma_0) = 0,
         normalization         d/ds = n, <n,n> = -1 in the signature convention adopted below
```

**Convention adopted as part of the entered authorship** (SD-N's route field explicitly asks the
entry to author it, so this consumes no freedom beyond the entry): signature `(-,+,+,+)`; `n`
future-directed with `<n,n> = -1`, so `slash(n)^2 = -1`; extrinsic curvature `K_ij := (1/2) d_s h_ij`
with mean curvature `H := h^(ij) K_ij`.

With `N = 1` and `beta = 0` the metric on the scope takes Gaussian normal form
`g = -ds^2 + h_s`, and `d/ds = n` exactly. The normal curves are geodesics, `nabla_n n = 0`.

## 4. Transported frame and spin frame [FIELD 7: COMPLETE]

Construction displayed:

1. Choose any orthonormal frame `(e_1,e_2,e_3)` on `Sigma_0` and set `e_0 := n`.
2. Extend along the flow by parallel transport: `nabla_n e_a = 0`.
3. Parallel transport preserves the metric, so the frame stays orthonormal on every `Sigma_s`; and
   because `nabla_n n = 0`, the transported `e_0` **remains the unit normal** of `Sigma_s`. The frame
   is therefore adapted at every `s` without a second choice.
4. **Spin frame:** the branch is sealed as a *spin* spacetime, so a spin structure exists. Lift the
   transported frame through the spin connection along `n`, transporting the spinor frame by the same
   parallel transport.

The consequence that matters for §5: in this frame the Clifford generators are covariantly constant
along the flow, `nabla_n gamma^a = 0`, so **`slash(n) = gamma^0` is constant along the flow**. That
is what makes the converting factor a fixed matrix rather than an `s`-dependent one.

## 5. The slice map and the identity

### 5.1 The write half — PROVED, exactly, on the record's own `S_n` [FIELD 9a]

Member 06's descend span seals

```text
D_K = i gamma^mu nabla_mu + i gamma^5 C_K(x),
C_K(x) = sum_c v_c(x) M_c(x) iota_c(c_c).
```

`Slice` applies the record's converting factor `(-slash(n))`, which 920 established is **already
supplied and forced by Hermiticity at 916** — I do not re-author it. Every factor of `C_K` commutes
with the spinor matrices: `v_c(x)` is a scalar, `M_c(x)` is a spatial multiplier, and
`iota_c(c_c)` acts on the record factor. Therefore

```text
(-slash(n)) * ( i gamma^5 C_K(x) )
   = [ (-slash(n))(i gamma^5) ] * C_K(x)
   = S_n * sum_c v_c(x) M_c(x) iota_c(c_c)
   = sum_c v_c(t) M_c(t) tensor S_n tensor iota_c(c_c).
```

The last line is **the parent's write term, verbatim**. The bracket is exactly the sealed
`S_n = (-slash(n))(i gamma^5)`; I also checked the record's second spelling,
`S_n = -i slash(n) gamma^5`, and the two are identical since scalars commute.

**SD-04 is satisfied by the record's own factor, and nothing was re-authored.** This half is proved.

### 5.2 The differential half — STOPPED, with the freedom named [FIELD 9b]

Here I stop, and the reason is a fact about the record rather than about the construction.

`h_0[g,a]` is a **sealed symbol with no sealed formula**. My 920 established this; I re-tested it
independently for this build, in exact-name mode across the sealed corpus. Every occurrence — in the
parent, in the STAGE-7 candidate, in the modular-energy result, and in the 922 check — restates the
same phrase `h_K(t) = h_0[g,a] + sum_c v_c(t) M_c(t) tensor S_n tensor iota_c(c_c)`. **Not one
unpacks `h_0[g,a]` into an operator formula.**

What this means precisely. On the scope, the normal-flow split of `i gamma^mu nabla_mu` in the
transported frame produces a normal term carrying `slash(n)`, a tangential Dirac operator on
`Sigma_s`, and a mean-curvature term whose coefficient is fixed by the entered convention of §3.
Applying `(-slash(n))` returns an operator on `K_Sigma`. That much is construction.

But the identity `Slice(D_K)|_differential = h_0[g,a]` has **no independent sealed right-hand side to
land on**. It can only *constitute* `h_0[g,a]` at this slice. Writing out the standard 3+1 Dirac
split here and presenting it as a derivation of the sealed symbol would make a definition look like a
theorem — which is exactly the middle step I declined at 920, and declining it again is the same
judgement at a smaller margin.

```text
STOPPED FIELD      : the differential half of the Slice identity
FREEDOM NAMED      : h_0[g,a] has no sealed operator formula anywhere in the corpus; the entry
                     supplies N=1, beta=0 and the extrinsic convention, which is everything 920
                     said was missing FROM THE SLICING, but the receiver symbol itself is unpacked
                     nowhere, so the differential half is CONSTITUTIVE and not checkable
ROUTED TO          : whoever owns h_0[g,a]'s content -- either a sealed formula for it, or an
                     express ruling that the slicing constitutes it, is required before this half
                     can be called proved
NOT DONE HERE      : I did not author a formula for h_0[g,a], and I did not call the constitution
                     a derivation
```

### 5.3 What the receiver therefore gets [FIELD 9c]

The carrier landing — the thing 924 and 926 actually needed — **is achieved**: `Slice` is defined on
the entered scope and takes the covariant kernel `D_K` to an operator on `K_Sigma`, which is
`dGamma_R`'s domain carrier. On that basis

```text
dGamma_R( Slice(D_K) ) = dGamma_R( h_K )
```

is the sealed receiver and no new lift authority is created — the right-hand side is the parent's
existing `dGamma_R(h_K)`. But the identity's strength is exactly the strength of its two halves: the
write half is proved, the differential half is constitutive. **I state the receiver as landed on that
basis and not more strongly**, and the opposite lane should press §5.2 first.

## 6. Scope — the route's price, paid as a bounded domain [FIELD 8: COMPLETE]

SD-N's price is "a no-caustic/globality statement **or** an explicitly bounded domain". I searched
the sealed corpus for a no-caustic ground in exact-name mode: `focal point`, `conjugate point`,
`injectivity radius` and `Gaussian normal` return **zero** sealed files, and every `caustic`
occurrence is either the instrument naming this very requirement, my own 946 quoting it, or a
phrasing adjudication that sweeps the spelling. **No such ground is sealed.**

Global hyperbolicity is sealed, and it gives a Cauchy surface and the product topology — but it does
**not** prevent normal geodesics from developing caustics. So the price is paid the other way:

```text
SCOPE = BOUNDED
domain := N(Sigma_0) = exp_perp( Sigma_0 x (-s_*, s_*) ), the maximal normal neighbourhood on
          which exp_perp is a diffeomorphism -- i.e. strictly inside the first focal locus of
          Sigma_0.  On this domain (s,x) are Gaussian normal coordinates, g = -ds^2 + h_s, and
          N = 1, beta = 0 hold exactly.
s_* is NOT evaluated: it is a geometric quantity of the sealed metric and evaluating it would be
a numeric evaluation of a physical quantity, which the gates forbid and which nothing here needs.
```

Everything in §§3-5 is asserted **on this domain only**. Outside it the normal flow is not claimed to
be a foliation.

## 7. `SD-08` — the spatial-section profile, disclosed honestly [COMPLETE]

**The section is SHARP, and this instance says so rather than smoothing it.**

The parent's causal envelope span states that the spatial support at each time "is the corresponding
diamond section" — a sharp section — and the descend span independently records that the
opening/closure-face term "may be **distributional for the sharp causal support** and must be
recovered as the strong limit of smooth intrinsic approximants".

```text
PROFILE = SHARP (inherited from the parent; not altered by this slice)
CONSEQUENCE = the sharp-cell S_2 boundary divergence I re-derived at 942 is INHERITED IN FULL.
              Changing lapse, shift, or frame spelling does not touch a boundary singularity, and
              this normal-flow slice changes none of them in a way that could.
SMOOTHING = DEFERRED as a principal selector by decision 2 of member 02, to the joint smoothing
            sitting -- the same selector as SD-08's profile disclosure, one object at two receivers.
NOT DONE HERE = no smoothing profile, thickness, scale, or limiting rule was authored. A slice
                does not silently convert the parent's sharp M_c(t) into a smoothed multiplier.
```

## 8. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the principal's SD-N entry and the Galerkin deferral;
  the sealed Sigma and K_Sigma, the globally hyperbolic spin branch, n, D_K, C_K, h_K, and S_n;
  920's localisation of what the slicing must supply and must not re-author;
  the confirmed sharp-cell S_2 result.

AUTHORED-BY-THE-ENTERED-ROUTE (and by nothing else):
  the signature and slash(n)^2 convention; the extrinsic-curvature sign convention;
  the choice of initial orthonormal frame on Sigma_0, extended by parallel transport;
  the bounded scope statement.

SUBSTITUTED:
  NOTHING. I did not re-author S_n, did not author a formula for h_0[g,a], did not author a
  smoothing profile, and did not select a Galerkin family. I adopted nothing and registered nothing.

STOPPED AND ROUTED:
  the differential half of the Slice identity (section 5.2), with its freedom named.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 9. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A constitution was not identified with a derivation (§5.2) —
  the load-bearing refusal in this artifact. A naming of a sealed surface was not identified with the
  selection of a new one (§2). Global hyperbolicity was not identified with a global normal foliation
  (§6). An inherited sharp section was not identified with a smoothed one (§7). A carrier landing was
  not identified with a fully proved identity (§5.3).
- **F_PLDEC:** symbolic geometry and operator algebra only. **No physical quantity was numerically
  evaluated**; `s_*` in particular is left as a symbol.
- **M-2 / four modes:** exact-name, normalized-name and byte-span checks covered `h_0[g,a]`, `S_n` in
  both sealed spellings, `C_K`, `caustic`, `focal point`, `conjugate point`, `injectivity radius`,
  and `Gaussian normal`.
- **BLIND:** held. No rank, no ratio, no fiber comparison.
- **PE-1..PE-14:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** every result here is **CLAIMED**. I ruled the governing instrument
  READY at 946, and that gives this instance no standing. The opposite lane should press §5.2 first,
  then §6's bounded domain, then the frame transport in §4.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2688
PREDECLARATION_OUTPUT_SCAN = 0 hits
FIELDS_COMPLETE = 8/9 ; FIELDS_STOPPED = 1 (the differential half, freedom named)
SIGMA0 = declared from sealed ground ; SCOPE = bounded ; PROFILE = sharp, disclosed
S_n_REAUTHORED = false ; SMOOTHING_AUTHORED = false ; h_0_FORMULA_AUTHORED = false
```

Self verb audit: "proved" is used once, of the write half, whose computation is displayed and lands
on the record's own `S_n`. "Constitutive" and "stopped" are used of the differential half, and I do
not call it proved anywhere. "Declared" is used of `Sigma_0`, which names a sealed surface rather
than choosing one. "Bounded" states the scope the price was actually paid at. Everything is CLAIMED.
`VERB_AUDIT_SELF = CLEAN`.

## 10. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2688; scan 0 hits)
SIGMA0 = DECLARED (sealed ground). Sigma_0 := the Cauchy surface Sigma on which the sealed carrier K_Sigma = L2(Sigma, S tensor L^q) is already defined, at member 05's carrier span. This names a sealed object rather than choosing a new surface, so no freedom is consumed; the branch span additionally seals a globally hyperbolic SPIN spacetime, which supplies both the Cauchy surface and the spin structure the frame lift needs
FIELDS = 8/9 COMPLETE (Sigma_0; hypersurface family; T = n; N = 1; beta = 0; normal-parameter normalization; transported frame and spin frame; bounded-scope statement). STOPPED: the differential half of the Slice identity
SCOPE = BOUNDED (domain stated). SD-N's price is a no-caustic/globality statement OR an explicitly bounded domain. I searched the sealed corpus in exact-name mode: focal point, conjugate point, injectivity radius and Gaussian normal return ZERO sealed files, and every caustic occurrence is the instrument naming this requirement, my own 946 quoting it, or a phrasing sweep — NO no-caustic ground is sealed. Global hyperbolicity gives a Cauchy surface and the product topology but does not stop normal geodesics from focusing, so the price is paid the other way: the domain is the maximal normal neighbourhood exp_perp(Sigma_0 x (-s_*,s_*)) on which exp_perp is a diffeomorphism, strictly inside the first focal locus, where g = -ds^2 + h_s and N=1, beta=0 hold exactly. s_* is left a symbol — evaluating it would be a numeric evaluation of a physical quantity
SLICE_IDENTITY = SPLIT, and I report the halves separately rather than averaging them. WRITE HALF PROVED EXACTLY: (-slash(n))(i gamma^5 C_K) = [(-slash(n))(i gamma^5)] C_K = S_n * sum_c v_c M_c iota_c(c_c), which is the parent's write term VERBATIM — every factor of C_K commutes with the spinor matrices, and the bracket is the sealed S_n, whose two record spellings I checked and found identical. SD-04 is satisfied by the record's own forced factor and nothing was re-authored. DIFFERENTIAL HALF STOPPED, freedom named: h_0[g,a] is a SEALED SYMBOL WITH NO SEALED FORMULA — I re-tested 920's finding independently and every occurrence across the parent, the STAGE-7 candidate, the modular-energy result and the 922 check merely restates the same phrase without unpacking it. The entry supplies N=1, beta=0 and the extrinsic convention, which is everything 920 said the SLICING was missing, but the receiver symbol is unpacked nowhere, so the differential half can only CONSTITUTE h_0[g,a] and is not checkable against anything. Writing the textbook 3+1 split here and calling it a derivation of a symbol with no sealed content is the middle step I declined at 920, and I decline it again. RECEIVER: the carrier landing IS achieved — Slice takes the covariant kernel to an operator on K_Sigma, dGamma_R's domain carrier — so dGamma_R(Slice(D_K)) = dGamma_R(h_K) lands on the parent's existing authority with no new lift created; but its strength is exactly the strength of the two halves, and I state it on that basis and not more strongly
PROFILE = SHARP-DISCLOSED (S2 inherited, stated). The parent's spatial support at each time is the diamond section and the descend span independently records that the face term may be distributional for the sharp causal support. The sharp-cell S_2 boundary divergence I re-derived at 942 is therefore INHERITED IN FULL; changing lapse, shift or frame spelling does not touch a boundary singularity and this slice changes none of them in a way that could. The smoothing profile is DEFERRED as a principal selector by decision 2 — the same selector at two receivers, per my own 946 interaction note which the principal cited as the ground. No profile, thickness, scale or limiting rule was authored here
NEW_CONTENT = ONLY-THE-ENTERED-AUTHORSHIP (the signature and slash(n)^2 convention, the extrinsic-curvature sign, the initial frame on Sigma_0 extended by parallel transport, and the bounded-scope statement — each a field SD-N expressly asks the entry to author). S_n NOT re-authored; no h_0[g,a] formula authored; no smoothing profile authored; no Galerkin family selected
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
