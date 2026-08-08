# RELAY 738 — DONE — DARIO LANE

Task: PASTE 738 / [7A / STEP 8] — confirm or contest the Freudenthal counterexample,
then the corrected verdict.
Lane guard: header names **DARIO**; satisfied. PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted. No register, plan, tracker, or
git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_738_COUNTEREXAMPLE_CONTEST_DARIO_V001.md
         edbcd0e6071a556d17b7d38c156e1ca5b9bf829785f821cf2af94ad82fe27ade   sidecar OK

OUTPUT   workspace/STAGE8_7A_COUNTEREXAMPLE_CONTEST_DARIO_V001.md
         c854c8b25dcc4e9e5bc2845925f9c197853aa9958f18cffb42c13b436cedc1e6
         429 lines / 22,854 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT before the write)
```

Six source pins verified. Pin check **15/15**.

## Final lines

```text
COUNTEREXAMPLE = CONFIRMED (exact)
REQUIRE_KILL = none found
CORRECTED_VERDICT = forced: the ENERGY; free: the SIMPLICIAL ASSIGNMENT (dim 32)
DOWNSTREAM_NEEDS = NOT energy-only — the generated face response takes the assignment
VOID = clean    CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+6 disclosures at §4.4)
```

## TT1 — confirmed, exactly, from a reconstruction of my own

I did not check Codex's arithmetic by reading it. I built the object from nothing — my
own Kuhn complex, my own barycentric gradients by exact 5×5 inversion, my own Whitney
forms, my own quadratic — and compared only at the end. **Every displayed value
reproduces:**

24 simplices · 16 vertices · 65 edges · 32 fixed · **33 free** · rank **33** ·
`E(Branch-F) = 1` · **`E_min = 191/252`** · `E(x_alt) = 1` · **22 of 33** differing ·
the three named edge values `1/7`, `−1/7`, `1/3` · and the simplex-0 component vector
`(1, −43/84, −13/84, 43/84, 13/84, 0)`. **No arithmetic divergence anywhere.**

Two checks I ran that were asserted rather than displayed, and both went against me:

- **All 24 coarse square-face fluxes reproduce** — verified, not assumed.
- **`x_alt − x_F` is NOT a coboundary.** I solved `d_0 λ = x_alt − x_F` over all 65
  edges and 16 vertices by exact elimination: **inconsistent.** The difference is
  **physical, not gauge**. That was the escape that would have saved my verdict, I ran
  it before writing anything, and it failed.

**My FORCED(Branch F) of 733 falls.**

## TT2 — no require kill, and the reason matters

`x_alt` satisfies **all nine** of my 733 requires — including all three locks that
carried the verdict. R6 in particular is *satisfied*, not evaded: the residual is
**exactly zero**. R7 bars an inserted weight and R9 bars an inherited parent profile;
`x_alt` is neither — it is a different admissible configuration at equal energy. **I
generalized two bars past the object type they name**, which is the error I have charged
in other lanes.

I hunted for a kill by meaning — locality, cell-local determination, covariance — and
opened every candidate. R3.3's *"computed using that cell's own V_cell…"* governs how
the response is **assembled on a cell**, not how the configuration is **chosen**;
reading it as a locality constraint would stretch a require past its text.

**There is exactly one clause that kills `x_alt`:** C_ref's *"preserving the same smooth
coframe and connection"*, which would force the refined field to be one global form's
sampling. **It is BARRED as a source**, and DoR-007 forecloses lifting the bar. So the
survivor survives because of a bar the program imposed on itself — a structural feature,
not a latent escape.

## TT3 — the corrected verdict, and the question that reframes the road

**FORCED: the energy.** `Σ F²` per cell transports exactly across the Freudenthal move
on the *whole* equal-energy set. Functoriality of the measure was never at risk from
this freedom.

**FREE: the simplicial assignment — a 32-dimensional set.** `E` is a rank-33
positive-definite quadratic with `E_min = 191/252 < 1`, so `{E = 1}` through `x_F` is a
32-sphere and Branch F is one point on it. Once `E_min < 1` strictly, an equal-energy
non-F point exists **automatically** — the reflection is just the easiest witness, and no
finer construction removes it.

**Scope flag both lanes owe:** "the cubical assignment is forced" is the natural reading
of both artifacts and **neither of us has earned it in general**. My 733 argument and
Codex's §2.1 both quantify over a one-parameter share family; the cubical move has its
own free space and it is untested.

**And the decisive answer — it is not uniform:**

| Consumer | Takes |
|---|---|
| RA27-2's discharge | **energy** |
| T_ref's instance transport | **energy** |
| J2 / the junction's one-object comparison | **energy** (`u(e)` is a scalar) |
| **V011's generated face response** `mathcal_K_L(ξ,ζ) = R_record,L(Q_flux ξ, Q_flux ζ)` | **THE ASSIGNMENT** |

For the first three the freedom is **gauge in the program's own sense** and no ruling is
needed. The response is a **bilinear form evaluated at particular fluxes**, not a
function of `Σ F²` — equal-energy cochains supply different arguments. **That is where
the ruling lives**, and by the subject ruling's own words the response sits **upstream**
of the coefficient: fixing the assignment for the response settles the chain; fixing only
the coefficient does not.

**What I do not claim:** that the response's dependence is *material* — that
`mathcal_K_L` actually differs on the pairs the program will evaluate. Settling that
requires evaluating the response, which the gates and the void condition both bar here.
I name the consumer and its type; the materiality question is the next one and it is not
mine to compute in this relay.

## Disclosed (six, §4.4)

Two beyond the above: **RA27-2's discharge no longer waits on a branch ruling** — it
consumes the energy, which the whole class supplies. And the most useful thing in this
artifact is §3.2, which **the commission had to tell me to ask**: the reframing from
"which branch" to "which consumer" came from the relay, not from me.

Nothing written archive-side but the ACK, the artifact, and its seal.
