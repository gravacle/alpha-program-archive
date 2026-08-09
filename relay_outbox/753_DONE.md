# RELAY 753 — DONE — DARIO LANE

Task: PASTE 753 / [7A / STEP 8] — derive the simplicial frame data from the sealed
construction's own coordinates; test it against V011's general-coframe clause; update the board.
Lane guard: header names **DARIO**; satisfied. PICKUP-ACK written before source work.
Status: **COMPLETE, SEALED, STOPPED.** Nothing adopted. No register, plan, tracker, or
git action.

## Hashes

```text
INBOX    relay_inbox/RELAY_PASTE_753_SIMPLICIAL_COFRAME_DARIO_V001.md
         7d9ea2000c31ac69b30e3d5188b9b283bd8f1921eabe6b094537180d62a2c58d   sidecar OK

OUTPUT   workspace/STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md
         d6f490b80e8d8775af9ee54095e34da03a4af01541736e2cb138f366c2caa75e
         383 lines / 18,922 bytes
SEAL     ...md.seal.sha256   shasum -c OK   (name probed ABSENT, recursively, before the write)
```

Nine source pins verified. Pin check **9/9**.

## Final lines

```text
FRAME_DATA = derived (24 simplices, exact)
V011_CLAUSE = bars (one-line need named)
BOARD = updated
VOID = clean    CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 disclosures at §4.3)
```

## AE1 — the frame data derives, and nothing is chosen

From `MAJ`'s sealed definition alone: one simplex per permutation of `(0,1,2,3)`, edge-vector
matrix = the staircase of partial sums, entries `0`/`1`. Computed in exact rationals over all
24:

- **`det E_p = sgn(p)` for all 24** — verified, not asserted, so orientation is canonical and
  `MAJ`'s word *"oriented"* is satisfied without a choice
- **`|det E_p| = 1`** every one
- **four-volume `= |det E_p|/4! = 1/24`** every one
- **sum of the 24 volumes `= 1`**

That reproduces **all three** of MAJ's sealed invariants — count, per-cell volume, total —
from the coordinates. This is verification of what is sealed, not authorship: the commission's
premise was right that the sealed construction already determines the coordinates.

## AE2 — the clause bars it, by exactly `4!`

`V011`'s general clause encodes the cell's volume factor as **`|det e|`**. That identification
is **exact for a box, because a box IS its edge-parallelepiped**. A simplex is `1/d!` of its
parallelepiped:

```text
|det E| = 1     against     V_cell = 1/24        ratio = 24 = 4!
```

**No frame repairs it.** The rescale needed is `E/24^(1/4)` — **irrational**, in a
construction the sealed sources carry in exact rationals throughout (`MAJ`: *"re-derived
exactly by iterated polynomial integration"*); unlicensed by any sealed text; and the wrong
shape besides, since the discrepancy is combinatorial and extent-independent. I checked the
last point: for anisotropic parent extents the frames become `E_p·diag(ell)` and the `4!` is
unchanged.

## The sharp form: this is a conflict, not a gap

751 called the simplicial coframe a spec gap. That was the weaker statement. The frame **is**
derivable; the obstruction is one integer in a clause written for boxes — and **two sealed
authorities disagree on `A2`'s children**:

| Authority | Volume factor on an `A2` child |
|---|---|
| `R33` (executed, packet-sealed, bound to row A27) + `MAJ` | `1/24` — the child's own four-volume |
| `V011`'s general-coframe clause | `\|det e\| = 1` |

They **agree exactly on boxes** and **diverge by `4!` on simplices**. So the one-line statement
needed is a **reconciliation**, not an invention, and `R33` — *"a subregion promoted to an
elementary cell must be evaluated by that child's intrinsic cell measure"* — already indicates
which way it falls. Two equivalent forms are displayed in the artifact. **I named it; I did not
make it.** That is a ruling.

## AE3 — the board

Coframe stays **PARTIAL**, sharpened: was *"no sealed coframe on simplicial cells"*, is now
*"the coframe is derived and the volume-factor convention conflicts."* **`R33` is not the
obstacle on `A2`** — it is the authority naming the correct factor, and once the reconciliation
exists it grounds `A2` exactly as it already grounds `A1`. All other fields unchanged from 751.

## Disclosed (three)

**The shortcut I refused, named because it was genuinely tempting:** rescaling the frame by
`24^(1/4)` makes `|det ẽ| = V_cell` and closes the coframe field in one line. Unlicensed,
irrational, and it absorbs a combinatorial constant into frame data — all three reasons stated
in the artifact rather than the refusal merely asserted. Also: §3's anisotropic extension is
one line past the sealed coordinates and is flagged unbooked, since `MAJ` seals the unit cube.

Nothing written archive-side but the ACK, the artifact, and its seal.
