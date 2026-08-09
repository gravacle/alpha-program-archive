# Stage 8 / 7A Step 8 — Intrinsic four-volume denotation addendum

**Lane:** CODEX 2  
**Relay:** 756  
**Scope:** finite denotation addendum; no alteration of the V011 formula or quantifier

## 1. Authority pin manifest

| Authority | Sealed artifact | SHA-256 | Load-bearing span |
|---|---|---|---|
| `FORCING` | `STAGE8_7A_SUPPORT_AND_FORCING_DARIO_V001.md` | `9685af44cc48f01fb04e57329cedf4f9a871eb393c6d41396179776957287e9b` | §2.5, lines 279–295 |
| `R33G` | packet `R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001.md` | `e4cfaef14309b3acf5674f8c8faee756f744fec4691d5e01d9de0fa422592be2` | `[98,309)` |
| `R33` | packet `R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001.md` | `e60aec3c44cfc5f1ef5715d3445e53783b0185ef93e54d94e442ff1df2ae9b59` | `[551,740)` |
| `V011` | packet `BOUNDARY_INCIDENCE_DYNAMICS_PRINCIPLE_V011.md` | `aa7c6d4904706276514728819df20f48e8fdca0ff83f97ad5f1724c5f81f108a` | `[45718,46387)`, including `[46074,46387)` |
| `MAJ` | `stage8_execution/work/MAJORANT_PHASE2_O3_O7_PROOF_DRAFT_V001.md` | `08b91543fdb72f656c756ca5f8df8233b87eb5487284c7fd2170cba67f7e0e3b` | `[19632,19996)` |
| `753` | `STAGE8_7A_SIMPLICIAL_COFRAME_DARIO_V001.md` | `d6f490b80e8d8775af9ee54095e34da03a4af01541736e2cb138f366c2caa75e` | §1.3 |

The three packet members reverified against `STAGE7_PACKET_MANIFEST_V001.sha256`. `MAJ`, `753`, and `FORCING` reverified against their adjacent seals. The operative statement below is copied byte-for-byte from the displayed content of `FORCING` §2.5.

## 2. Operative addendum

```text
The general map's volume factor is the cell's intrinsic four-volume Vol_4(C),
classified uniquely at R3_3_GLOBAL_INTRINSIC_MEASURE_CLASSIFICATION_RESULT_V001
(e4cfaef1…) as mu_D(A) = Vol_4(A)/Vol_4(D), and selected per cell by
R3_3_INTRINSIC_CELL_MEASURE_DERIVATION_RESULT_V001 (e60aec3c…).

  - On a parallelepiped cell with coframe e:   Vol_4 = |det e|.
    This is V011 aa7c6d49…[46074,46387) unchanged; the box case is recovered
    exactly and nothing in V011 is amended.
  - On a d-simplex with edge-frame E:          Vol_4 = |det E| / d!.
    For the sealed order-simplex subdivision of the unit 4-cube this gives
    1/24 per cell, 24 cells, total 1 — MAJ 08b91543…[19632,19996), reproduced
    exactly at 753 §1.3.

ZERO PHYSICS CHOICE: no new measure, weight, normalization or convention is
introduced.  The statement records which already-classified measure the
general map's volume factor denotes, and evaluates it on the two cell types
the working class produces.
```

## 3. Scope fence

This addendum records the denotation of the existing general-map volume factor. It introduces no new measure, weight, normalization, convention, physical quantity, or measured-constant comparison. It does not alter V011's formula, diagonal exact check, coframe quantifier, or box case.

AUTHORIZATION = Q-660 forced-content authoring only
PHYSICS_CHOICE = zero
CHAIN_INVOKED = false
