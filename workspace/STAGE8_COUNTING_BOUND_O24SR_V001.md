# STAGE 8 — THE SINGULAR-VALUE COUNTING BOUND FOR THE DRESSED COMPOSITES — COMMISSION O24SR — V001

## O24SR-BUILD, 2026-08-15 — ONE MATHEMATICAL QUESTION, ANSWERED AS MATHEMATICS

THE QUESTION, exact. For each `n` let `A_n` be a dressed composite at stage `n`
(the object W-1 §4 names by that letter), let `s_1 >= s_2 >= ... >= s_{r_n} >= 0`
be its singular values, and let

```text
        N_n(s)  :=  #{ k : s_k > s }.
```

`N_n(s) <= r_n = 4 n^3` is already known (rank cap). ASKED: is there a constant
`c`, independent of `n`, and some `d > 0`, with

```text
        N_n(s)  <=  c * n^(3-d) * s^(-2)        for all n and all s > 0 ?        (Q)
```

```text
THIS ARTIFACT DECLARES NOTHING, ADOPTS NOTHING, LANDS NOTHING.  No gate moves, no
witness is created or retired, no failure point is discharged, no absence closed.
RATE_CERTIFIED = false is untouched.  It answers one operator-theory question on
the sealed stock and displays exactly where the answer stops.
```

Fences held from the first byte: no value, no magnitude, no unit, no dimensional
quantity, no scale, no measured constant, no comparison to any empirical or
physical quantity, no imported GR, no authored physics. **Every number below is an
exponent in the counting parameter `n`, a rank count, an index, or a rational
coefficient inside a symbolic inequality.** Exact symbolic only (CAS appendix §8,
fresh venv, sympy 1.14.0). No `register` / `tracker` / `road` / `plan` /
`continuation` / `ledger` / `lens` file opened. No git action.

**OUTPUT-PATH PROBE:** the output path and its `.seal.sha256` sidecar were both
probed **ABSENT** before any write (`ls` exit 1 on both, 2026-08-15T20:57:47Z).

**SWEEP CUTOFF: 2026-08-15T21:12:00Z.** Every exhaustiveness sentence below is
sweep-relative to this cutoff and to its own displayed key set. Nothing absolute
is claimed.

---

## §0 — VERDICT IN ONE LINE

**OUTCOME 3 — (Q) NEITHER FOLLOWS NOR FAILS on what is established**, and the
reason is sharp rather than accidental: **(Q) is EQUIVALENT to the open problem
itself.** Theorem T-A below proves that, for any operator sequence obeying only
the two sealed facts `rank A_n <= 4n^3` and `||A_n||_op <= 2`,

```text
        (Q) holds for some d > 0   <==>   ||A_n||_2^2 <= C n^(3-delta) for some delta > 0
```

with `delta = d` in one direction and any `delta' < d` in the other — i.e. the two
statements have the **same critical exponent** (T-A3). The right-hand side is
verbatim FP-1's demanded certified sub-volume HS rate, which W-1 §8 records as
`RATE_CERTIFIED = false` and which W-1's T-1 proves is not a consequence of the
class data at any strength. So (Q) cannot be proved from the established stock
(T-B gives an explicit countermodel inside the established class), cannot be
refuted from it (T-C: the stock exhibits no lower bound on any `N_n`, and W-1 §8
carries all four relevant quantities as UNDECIDED), and is not weakened by any
decomposition trick (T-D: by Eckart–Young the small-rank/small-norm splitting IS
`N_n`, not a tool for bounding it). The single additional fact that settles it is
named exactly at §6: the **singular-value density of the dressed composites at a
fixed threshold**, i.e. the value of `limsup_n log N_n(s_*) / log n` for one fixed
`s_* in (0,2)` — `= 3` refutes (Q) outright, `< 3` with a rate proves it.

Additional exact yield, not in the swept stock at the cutoff: (Q) also discharges
FP-1's **trace** budget, at exponent `3 - d/2`, and that half-loss is sharp (T-A4).

---

## §1 — GROUND CONSUMED, SEALS VERIFIED

Verified THIS session by `shasum -a 256 -c` run from the artifact's own directory
against each `.seal.sha256` sidecar, full digest, BEFORE any reliance.
**3/3 OK, zero mismatches, none unverifiable.**

```text
  STAGE8_W1_SUBVOLUME_RATE_O5SR_V001.md              OK   (the construction of A_n; T-1, T-2)
  STAGE8_W1_SUBVOLUME_RATE_O5SR_AUDIT_V001.md        OK   (CONFIRMED-WITH-REFUTATIONS; finding A-1)
  STAGE8_MO3_P_EXPONENT_S9AD_V001.md                 OK   (the standing sub-volume result; p = -3)
```

**DECLARED SCOPED SWEEP (1), at the stated cutoff.**

```text
SW-1  OUTPUT-COLLISION PROBE + DEFINITION SWEEP.  Keys: the exact output path and
      its sidecar (`ls`); and the tokens `A_n`, `N_n`, `dressed composite`,
      `K_H,n`, `H_A,n`, `4n^3`, `rank`, `_op <=` inside the three named files.
      RESULT: output path ABSENT, sidecar ABSENT.  The definitional locus of `A_n`
      is W-1 :254-271 and nowhere else in the three files; the two sealed facts
      about it are W-1 :156 (operator enclosure) and W-1 :163 (rank).
      Exhaustiveness claimed at this key set only.
```

---

## §2 — WHAT `A_n` IS, AND EXACTLY WHICH FACTS ABOUT IT ARE ESTABLISHED

### §2.1 The object

W-1 §4 (:254-255) introduces the letter:

```text
"Let A_n be a dressed composite at stage n, with singular values
 s_1 >= ... >= s_{r_n} >= 0 and counting function N_n(s) := #{k : s_k > s}."
```

`n` is the **stage / carrier index** — a counting parameter, not a magnitude
(W-1 :162). The dressed composites are the two operators the boundary-closure
names, `K_{H,n}` and `H_{A,n}`, acting on the stage-`n` carrier; `A_n` denotes
either, or any member of that class, uniformly in `n`. The ambient space is
`L^2(R^3) tensor C^4` and the stage-`n` carrier is `ran C_n` (W-1 §5.1, and the
boundary-closure's `rank <= 4n^3 on ran C_n` at `80db260f` :302).

### §2.2 The norms in use

```text
  ||.||_op   operator norm            = s_1
  ||.||_2    Hilbert-Schmidt norm     ||A||_2^2 = sum_k s_k^2
  ||.||_1    trace norm               ||A||_1   = sum_k s_k
  N_n(.)     the counting function above (a nonincreasing, right-continuous,
             integer-valued function, constant = r_n near 0 if all s_k > 0)
```

### §2.3 The established facts — the complete list

At the cutoff, and across the three named files, exactly **two** facts about
`A_n` are established. Nothing else about `A_n` is available at any grade.

```text
  (F1)  RANK CAP.       rank A_n <= r_n = 4 n^3.
        Source: W-1 :163 (PA / FHB §3.2, consumed at sealed grade); re-sourced
        independently by the audit at :162-167 to the boundary-closure's own
        bytes, "rank <= 4n^3 on ran C_n (of record)".
        Consequence: N_n(s) <= 4 n^3 for every s > 0.
  (F2)  OPERATOR ENCLOSURE.   ||K_{H,n}||_op <= 2 and ||H_{A,n}||_op <= 2,
        EXACT and n-uniform.  Source: W-1 :156, "stands DELIVERED MEANWHILE".
        Consequence: N_n(s) = 0 for every s >= 2 (W-1 T-2b).
```

And the complete list of what is **NOT** established, carried verbatim from
W-1 §8's closing clause (:653-656):

```text
"NOT REFUTED, carried in full: every negative above is ONE-SIDED.  No divergence
 of tr K_H, tr H_A, ||K_H||_2^2, or ||H_A||_2^2 is exhibited; no sealed +infinity
 attaches to any of the four quantities; all four remain UNDECIDED."
```

**So no lower bound of any kind on any singular value of `A_n`, and no upper bound
on `||A_n||_2` beyond what (F1)+(F2) force, exists in the stock.** This is the
single most load-bearing fact in this artifact and it is why §5's non-refutation
goes through.

### §2.4 What (F1)+(F2) give at a fixed threshold — exactly nothing beyond the cap

The natural first move is to feed the sealed HS budget into Chebyshev. The sealed
budget is `||A_n||_2^2 <= 16 n^3` (W-1 :166, `4n^3 . 4`), so W-1's T-2c gives
`N_n(s) <= 16 n^3 / s^2`. Compare with the cap on the only interval where `N_n`
can be nonzero:

```text
        16 n^3 / s^2  vs  4 n^3        on  0 < s < 2
        16/s^2 - 4  =  4(4 - s^2)/s^2  >  0   for all s in (0,2),  = 0 at s = 2.
                                                                  [CAS A1, exact]
```

> **OBSERVATION O-1 [DERIVED].** On `(0,2)` the Chebyshev consequence of the sealed
> HS budget is **strictly weaker** than the rank cap, at every threshold, and the
> two agree only at the endpoint `s = 2`, where both are already superseded by
> (F2)'s `N_n = 0`. Hence the established budgets contribute **exactly zero**
> counting information beyond (F1)+(F2) themselves, and the best bound of the
> shape (Q) they yield is
>
> ```text
>         N_n(s)  <=  16 n^3 s^(-2)          i.e.  c = 16,  d = 0.
> ```
>
> The question (Q) asks for `d > 0`. So the answer is not obtainable by inserting
> the established bounds into the established inequality: that route returns the
> boundary value `d = 0` and no more. [CAS A1, A2]

This already disposes of the first natural approach. The remaining three are §§3-5.
