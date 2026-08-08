# RELAY 729 — DONE — DARIO LANE

Task: PASTE 729 / [7A / STEP 8] — the refinement bridge: `F` under subdivision, derived
from its own sealed definition.
Lane guard: header names **DARIO**; satisfied. PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted. No register, plan, tracker, or
git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_729_REFINEMENT_BRIDGE_DARIO_V001.md
         587aae713f8295fd9e0d8ce3c0fc36549c09db5234f02ef76067ff89609bfbd2   sidecar OK

OUTPUT   workspace/STAGE8_7A_REFINEMENT_BRIDGE_DARIO_V001.md
         972eae9ac7bbc66203fb43c547eebc68b85fe7ebcfc2f22780ed82340668cf4f
         450 lines / 20,990 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT before the write)
```

Seven source pins verified. Pin check **12/12**.

## Final lines

```text
F_DEFINITION = assembled (5 statements N1–N5, block-covered; A26 corroboration)
SUBDIVISION = UNDERDETERMINED — free datum named
DIVERGENCE_NOTE = none (lens applied and declined)
LEDGER_ENTRIES = 4
VOID = clean
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+5 disclosures at §5.3)
```

## NN1 — what `F` is

`F` is a **derived functional**, not a face primitive and not a restriction of anything
global. V011 defines it upward from edges:

```text
(d_1 a)_f = sum_(e in boundary f) incidence(f,e) a_e,   d_1 d_0 = 0
F_phys = im(d_1)
```

with the lift unique on `F_phys` and *"individual unit faces outside `F_phys` are never
assigned a lift"* — corroborated independently in A26. A free per-face value would make
`F_phys` the whole 2-cochain space, which N3 excludes.

**So the relay's framing — "F's definition must say what F is on a sub-face, or say
nothing" — resolves as: it says.** `d_1`'s formula is stated for a general face of a
general complex and applies verbatim to a sub-face. What is silent is one level down.

## NN2 — UNDERDETERMINED, and the free datum is not where anyone was looking

`xi'` on every sub-face is determined by `a'` on the refined edges. The whole question is
what `a'` is.

**The boundary-edge split is pure gauge.** Subdividing a parent edge at a new vertex
leaves a one-parameter freedom that is exactly a gauge transformation at that vertex —
and `d_1 d_0 = 0` makes the flux invariant under it. **It moves nothing.** This was my
first answer and it was wrong; §2.2/§2.4 record the correction rather than smoothing it
away. Reporting it would have aimed a repair at an object that cannot affect the result.

**The real locus is the interior edges** a subdivision creates — edges with no parent,
unconstrained by `a`, and not absorbed by gauge (gauge is one parameter per vertex; the
interior edges are more numerous). The shape of the freedom is exact:

- the **sum** of sub-face fluxes is fixed by the parent — interior edges cancel by
  opposite incidence, so **the total flux transports**;
- the **individual** sub-face fluxes carry **k−1 free parameters** for `k` sub-faces.

And that is precisely why the measure fails while the flux passes: `V_cell · sum F²` is
**quadratic**, and a quadratic form is not a function of the sum of its arguments. The
same k−1 parameters that leave the total alone move the measure.

**That is why T11's gap is real and why it looked closed** — including to me at 725.
*Flux adds* is true and is the thing everyone checks. The measure squares.

**Free datum, named:** the 1-cochain on interior edges — equivalently, the distribution
of the parent's flux among its k sub-faces at fixed total. **Smallest sealed addition:**
a connection-refinement rule on interior edges; once `a'` is fixed, `xi'` is *forced* by
`d_1` and functoriality becomes decidable. **Not adopted** — and I note the obvious
candidates (equidistribution, proportional-to-area) are exactly what the void condition
governs. **Not OBSTRUCTED**: the definition admits many extensions and selects none.

Nothing supplies it — writer-excluded counts: `sub-edge` 0, `subdivided edge` 0,
`holonomy split` 0; the three non-zero near-carriers were opened and none assigns `a'`.

## NN3 — divergence: none

**The lens does not fit and I say so.** What §2 produces is an underdetermination — a
k−1-parameter family — not a divergence: nothing was computed, nothing runs in a
variable, there is no coefficient to place in a class. Typing a missing datum as a
physical signal is precisely the fitter's move Requirement 5's second half pre-names.

One adjacency logged at zero weight and explicitly not promoted: a *chosen* scheme
iterated could in principle make `sum F²` scheme-dependent in the limit — the
refinement-dependence BATT names. That is a conditional about an object nobody built, on
a rule nobody adopted; computing it would need both an adopted rule and the downstream
evaluation the void condition bars.

## Custody

**VOID = clean.** No downstream numeric consulted, computed, or estimated. The k−1
freedom is reported as a parameter count, never evaluated; no scheme was chosen; §3's
adjacency is left conditional.

One thing marked honestly: §2.3's interior-edge cancellation is **PART-PROVABLE**, not
PROVABLE — it needs the subdivision to carry the standard incidence data. That is what a
subdivision *is*, but I did not find it sealed, and I would rather flag the one line
than let a structural convenience pass as a citation. **If you want §2 airtight, that is
the line to seal.**

Disclosed (five, §5.3): my first answer was the tidy wrong one; my **727 framing pointed
at the wrong object too** and this relay inherited it — the missing rule is about `a` on
interior *edges*, not `F` on sub-*faces*; and I declined the K-axes on a result that
would have read stronger inside them, because "refinement-dependence measured under
K-1/K-3" is a better sentence than "no divergence surfaced" and would have been false.

Nothing written archive-side but the ACK, the artifact, and its seal.
