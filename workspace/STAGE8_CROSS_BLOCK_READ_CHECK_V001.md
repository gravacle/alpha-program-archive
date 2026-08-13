# STAGE 8 — CROSS-BLOCK READ: ADVERSARIAL CHECK (READ-CHECK)

BLIND ADVERSARIAL VERIFICATION, cross-lineage, DEFAULT = REFUTE.
Codename READ-CHECK. Date: 2026-08-13. Under test:
STAGE8_CROSS_BLOCK_READ_V001.md, digest recomputed at path THIS session =
f3165db1a3b88a4d0667d3e3b214a55020aef31d424c5e3fce32d03cdb7774b1 — MATCHES the
tasked digest and the file's own .seal.sha256 sidecar. The tasked flag block was
diffed byte-for-byte against the in-file flag block: IDENTICAL (85 lines, zero
differences).

---

## §0 — SEAL RE-VERIFICATION (independent; shasum -a 256 at path BEFORE reliance)

All 17 seals in the read's §0 table recomputed by this check, independently of
the read, and compared both to the read's typed digests and to each file's
.seal.sha256 sidecar:

  38bbb9fc AND-CLASS ; a3bedc7e B1-INSTANCE ; 86b6134d B1-CHECK ; 92dba8d3
  BOTH-BLOCKS ; 22f69dd3 BB-CHECK ; f1881511 MIN-CARRIER ; bb2e6570 MC-CHECK ;
  f7fd0c60 G2-STATE-PORT ; c8bde5c9 G2-PANEL-OVER ; 2bf4c1a2 G2-PANEL-UNDER ;
  18af3dee TWO-TIME ; 6a2aa0fd TT-CHECK ; 0a10c030 ASSEMBLY-QUANTIFIER ;
  331035d3 AQ-CHECK ; 5e49d209 FORM ; 52f2490b RL2B-REFUTED ; 46846730 E1-SPEC.

RESULT: 17/17 MATCH. The read's §0 table was also diffed row-by-row against my
recomputed digests: BYTE-EXACT, 17/17 rows. NONE UNVERIFIABLE. Additionally
verified beyond the read's own set: ATTACH_ENTRY_ADDENDUM_V001.md recomputed =
420ab02f5ddb... MATCHES its sidecar (the read cites 420ab02f only as carried in
a3bedc7e/f1881511 seals; this check confirmed it directly at path).

Span spot-checks performed DIRECTLY at bytes (not through the carrying seal):
  - E1 span [57212,58506) recomputed sha256 prefix = 162e30a6 — MATCH (B-L2*).
  - E1 :2191 verbatim: "record_vertex_two_time_HS_certified = false (B-L2*, the
    common wall)" — MATCH.
  - E1 :1123-1124 verbatim: "whose only repair would be to soften M(t) — a
    SEALED PHASE-A A1 DEFINITION, NOT A LANE'S TO CHANGE." — MATCH.
Remaining span digests (ba7d1013, 57bd3233, 7ed9e192, f7c7261e, 7d81c132,
96e164af, 9bbd9525, 7103582e, a6cc611f) verified as carried inside seals
verified above (38bbb9fc, 92dba8d3, f1881511, bb2e6570, 22f69dd3, 331035d3),
exactly the chain of custody the read discloses in its own §0 — the disclosure
is honest and the custody model holds.

---

## §1 — ATTACK 1: ASSEMBLY FIDELITY

Every load-bearing input claim re-read at its sealed source's flag block or
cited span. Findings:

1.1 WORKING-CLASS (38bbb9fc): PHI_H_VANISHING = IDENTICAL, dim H = 0 EXACTLY on
    every sealed complex of the working class; the consequence clause "Phi_H ≡ 0
    makes the cross pairing Phi_f^T C Phi_H vanish for EVERY Gate-5 kernel C"
    is VERBATIM in the sealed flag block; kinematic/member/kernel-independent
    reading exact; spans ba7d1013/57bd3233/7ed9e192 all present in that seal;
    the reopening condition ("a sealed record complex with dim H > 0, which
    nothing of record supplies") verbatim. CONFIRMED.
1.2 b1=1 CELL (a3bedc7e + 86b6134d): dim H = 1 EXACT; phi_H FORCED nonzero;
    im(d_1^dagger) = {0} because the premise mandates F = 0, phi_f ≡ 0 — "the
    MIRROR of the working-class collapse, with the opposite dead block"
    verbatim; PROVENANCE_CARRIED = TYPE-P on 420ab02f, voids with it, verbatim;
    check verdict INSTANCE_VERDICT = SOUND verbatim. CONFIRMED.
1.3 COEXISTENCE + TYPING (92dba8d3 + 22f69dd3): K3_BLOCKS = gauge 80 / flux 240
    / harmonic 4 EXACT at the audit stratum; T0/T2 SATISFIABLE, T1
    UNSATISFIABLE with the collapse mechanism reproduced; COMPOSITION =
    UNBUILT-UNSPECIFIED with "The barrier is absence of construction, not
    sealed prohibition" VERBATIM; hunt :324-326 and NONE_SEALED (glued check
    :288-291) carried as sealed; NET = one construction (derived connected
    b_1 >= 2 filled-face complex, O11/O12/O-D1) + two supplies (selector
    V007 :170-171 "does not supply and may not freeze"; the unwritten
    cell-local typing rule) — the read's D1/D2/D3 are these, verbatim;
    BB_VERDICT = SOUND; GC :124-131/:229 (T1 not forced) carried by the check
    exactly as the read cites it. CONFIRMED.
1.4 MIN-CARRIER (f1881511 + bb2e6570): K_dd V/E/F = 4/5/1, b_1 = 2, blocks
    3/1/1, candidate-not-of-record; FINITE_N_CROSS_FORM per FN span
    [20396,20529) f7c7261e (rehashed by both the candidate and its check):
    Phi_f^T C_N Phi_H = n^2·mu·phi_f ⊗ phi_H; T2 witness = chi_j itself with
    exact split h/4 + (3/4)w and cross coefficient (3/16)·n^2·mu on (w,h); T0
    coefficient n^2·mu; GLUING_LEDGER L-1..L-5 with "every identification in
    the ledger is performed, not licensed" VERBATIM; CONDITIONALITY carries
    the D2 reduction (K_dd: domain extension alone; NOT reduced on A5) and
    "NONE_SEALED at the physical write-carrier stratum SURVIVES" VERBATIM;
    MC_VERDICT = SOUND. CONFIRMED.
1.5 MU (f7fd0c60 + panels): MU_BEARING OUTCOME C "NO sealed outcome pins
    mu = 0; asserting it from the unbuilt field face is barred (DoR-006 via
    M06 :464-469)" VERBATIM; OUTCOME A mu != 0 PINNED SYMBOLICALLY, magnitude
    and sign NOT pinned; selector AUTHORED PHYSICS BY PRINCIPAL ACT, sealed
    non-derivable (D13 :34-38); (r_0, r_ch) NO_VERDICT (D14 :14-17); value
    selection BARRED (D14 :25-27); TYPE-P premises DoR-008/009/013/014 + A0 +
    the entry's three open conditions, voiding on the neutrality/restriction
    falsifier; field-face independence rider verbatim. Panels: c8bde5c9
    OVER_LENS_VERDICT = BUILD_SOUND; 2bf4c1a2 UNDER_LENS_VERDICT = REFUTED
    with scope verbatim "refutation scoped to SELECTOR_TYPE_IF_NONE(F1), the
    C8 absence claim, and the reconciliation-flag framing; CONSTRAINT_
    INVENTORY, SELECTOR=PARTIAL(C6), and MU_BEARING are individually CONFIRMED
    and survive" — the read's "mu bearing individually CONFIRMED and not
    disturbed" is the panel's own finding. CONFIRMED. (Two notes, §3.)
1.6 TWO-TIME + QUANTIFIER (18af3dee + 6a2aa0fd; 0a10c030 + 331035d3): NET =
    FAILS at the sealed per-pair S2 quantifier; degree-0 survivor,
    "HS-norm^2 scales as the carrier momentum volume... this IS the
    carrier-uniformity failure" VERBATIM; TT_VERDICT = CONFIRMED with the HS
    shape "verified as shape only" — the read's "shape-only" is exact.
    Quantifier SPLIT-BY-OBJECT-EXPLICIT; per-pair FIXED dead as architected
    (survivor + 52f2490b's "NO SUCH M EXISTS... R-L2b's UNIFORMITY IS
    REFUTED", re-read at path); summed FIXED live blocked on EXACTLY B-L2*
    (span 162e30a6, E1 :2191) + F'-14 (Route B "exists nowhere sealed") +
    summed-S2' ("a spec-author act, not a lane's, not performed here"
    VERBATIM); RUNNING a lean only, unforced; sole running-shaped clause ECO
    §4 = NAMED_NOT_PURSUED / would_be_a_NEW_PRINCIPLE, "a fallback shape, not
    a target" per the AQ-check's hostile hunt, VERBATIM; AQ_VERDICT = SOUND.
    CONFIRMED.
1.7 FORM (5e49d209): FACTORIZES = UNDETERMINED; "No third case exists"
    VERBATIM (binary dichotomy); the fork compresses to ONE unsealed datum —
    G3's write-chain block decomposition (RA27-3 fields NOT SUPPLIED);
    WINDING_FORCED = NOT-FORCED with "n enters the derived form exactly once,
    as the global quadratic prefactor n^2 of an n-blind form" and BOTH sealed
    comparand candidates unavailable (energy-form comparand fork-gated, both
    settlement paths SPEC-GAPPED; kappa_record-to-physical conversion sealed
    UNAUTHORIZED until Z_Q) — the read's rider is VERBATIM-faithful; G2 pair
    sealed TYPE-R/TYPE-U in FORM's G2 line, matching the read's D8 typing.
    CONFIRMED.

NO mis-quoted flag, NO claim resting on an unsealed statement, NO dropped
LOAD-BEARING rider found. Every conditionality named in the fences (entered
Attach TYPE-P; candidate-not-of-record; the two supplies; the gluing license;
the spec-author act; mu's disclosed-input chain) appears in the verdict's own
statement (V1-V5 + the D-list). ASSEMBLY = CONFIRMED.

---

## §2 — ATTACK 2: VERDICT STRENGTH (both directions)

ROUNDED UP? Hunted for any conditional stated as a verdict:
  - V1 is scoped "AT THAT STRATUM... not the program verdict" — licensed by
    dim H = 0 exact + the kernel-independent consequence clause. Not rounded.
  - V2 carries the TYPE-P entry and its void trigger inline. Not rounded.
  - V3 carries ALL of: audit/candidate stratum, typing T0-or-T2, ratified
    mu-chain (TYPE-P), gluing performed-not-licensed, supplies granted AS
    POSED, mu magnitude/sign open, T1 unsatisfiability. Nothing silent.
  - V4 states UNDECIDED with the exact three blockers and keeps RUNNING a
    lean. V5 keeps FACTORIZES undetermined and the winding rider on BOTH
    branches. NOTHING ROUNDED UP.
ROUNDED DOWN? Hunted for established pieces under-stated:
  - Working-class FREE kept unconditional at its stratum (not weakened to
    conditional); per-pair FIXED kept DEAD (not softened to open); the
    b1-cell mirror kept identically-vanishing; the finite-N structural
    nonzero kept structural (not degraded to "open"). The refusal to convert
    two-carrier vanishing into program-level FREE is CORRECT of record: the
    sealed record contains built both-blocks objects with a satisfiable
    nonzero cross term under two of three typings and NO composition bar.
    NOTHING ROUNDED DOWN.
STRENGTH = EXACT.

---

## §3 — ATTACK 3: COMPLETENESS OF THE CONDITIONALITY MAP

Hunted both directions:
MISSING? D1-D9 were mapped one-to-one onto sealed NET/CONDITIONALITY/OPEN
clauses (§1.3, §1.4, §1.5, §1.6, §1.7). The provenance riders (TYPE-P entry,
candidate status, V007 selector gap, typing hinge, gluing ledger, mu's chain
with open sign/magnitude, quantifier split, G2 port, G3 datum, winding
comparand) are ALL present. Two items the read does not carry, examined and
judged NON-dependencies:
  N-1 f7fd0c60's RECONCILIATION FLAG (ready-sandwich anchor vs forced mixed
      marginal, TH :134): the UNDER panel (FC11) types that framing STALE of
      record (composition ill-posed until a second rule or an effect instance
      exists) and FC12 CONFIRMS MU_BEARING; both panels are in the read's
      verified seal set, so the flag is superseded of record, not a live
      dependency. The OVER panel's P6 PLAUSIBLE-level exposure targets one
      overbroad sentence of the build's §6, "none converting a claim" (panel's
      words). NON-REFUTING.
  N-2 The AQ-check's R-L0b completeness note (a second sealed mention of the
      same one-way bridge, "equally blocked per-pair and NOT a sealed Route
      B", "verdict unchanged"): adds no dependency beyond D7's three named
      blockers. NON-REFUTING.
OVER-LISTED? Hunted for any listed dependency already discharged of record:
none is. D2 correctly carries its own K_dd reduction (domain extension alone;
not reduced on A5); D5 stands ("voids with it" in both carrying seals); D8's
port remains TYPE-R/TYPE-U with K4 NOT-MET (panel-confirmed); NONE_SEALED
survives per f1881511 + bb2e6570. NOTHING OVER-LISTED.
MAP_COMPLETE = YES.

---

## §4 — ATTACK 4: THE UPGRADE MAP

Attributions re-derived against the sealed holders:
  U-F1 lane (92dba8d3: absence-of-construction) — CONFIRMED. U-F2 spec-author
  (the unwritten rule is a SUPPLY of record; 22f69dd3 confirms T1 not forced,
  so writing it is an authoring act, not a derivation) — CONFIRMED. U-F3
  principal via the DoR-013/014 falsifier only, assertion barred (DoR-006;
  D14 :25-27), OUTCOME B yielding UNDETERMINED not FREE — CONFIRMED.
  U-D1 lane; U-D2 principal-at-the-entry / spec-author (V007 "may not
  freeze"); U-D3 spec-author; U-D4 lane, same constructor; U-D5 principal;
  U-D6 rank-pinning lane (D14 "derivable-new-work ONLY") with value selection
  barred and the chain itself principal (D13 non-derivable); U-D7 B-L2* lane
  (softening M(t) sealed away from lanes, E1 :1123-1124 verified at bytes) +
  summed-S2'/Route B E1-successor spec-author (0a10c030 SETTLING ACT
  verbatim) + G1 lane; U-D9 lane (RA27-3); U-R1 principal/spec-author
  (would_be_a_NEW_PRINCIPLE) — ALL CONFIRMED.
  U-D8 — ONE CORRECTION (non-converting): the read carries the UNDER panel's
  FC8 (the RATIFIED measure-supply mandate b9716661 pre-assigns F1's supply
  slot to authored PROPOSED PHYSICS, Attach pattern) but NOT its FC9: the
  stock-level joint construction named by the build (the SM-1..SM-8-conformant
  joint state, TH :275-277) is REFUTED of record at the stock level
  (ec124183 §4 sealed + producer check 56692b5e + witness e650076c), residue
  "E3 + the forcing slot only" (2bf4c1a2, in the read's own verified seal
  set). U-D8's primary holder is therefore the mandate's authored-physics
  channel, with lane derivation live only on the E3 structural escape; the
  read's "lane construction ... consult that mandate before assigning" points
  at the mandate but under-states the sealed stock-level refutation. This
  corrects an upgrade ROUTE attribution only: dependency D8 itself (port
  TYPE-R/TYPE-U, omega_phys STOPPED, K4 NOT-MET) is exactly right and
  panel-confirmed, and no branch verdict moves.
UPGRADE_MAP = CORRECTED(U-D8 as above); all other entries CONFIRMED.

---

## §5 — ATTACK 5: PROVENANCE + INJECTION

PROVENANCE: 17/17 seals + the artifact under test + its sidecar + 420ab02f
recomputed at path by this check before reliance; the read's digest table
byte-exact against my recomputation; the B-L2* span digest recomputed directly
from E1 bytes; every verbatim quotation I relied on re-read at its source; the
read's disclosed custody model for the remaining span digests (carried through
verified seals' own certified span tables) checked and holds; no reliance on
substring presence anywhere in this check (flag-block and clause-level reads
only, against recomputed digests). CLEAN.
INJECTION: directive-pattern scan of the read: the only hits are its own fence
declarations and the panels' verdict names; no verdict cites the tasking as
authority; no register/tracker/plan/road/ledger/lens content appears in or was
consumed by the read (all its citations trace into the 17-seal set); the tasked
flag block is byte-identical to the sealed in-file flag block. none.

---

## §6 — NET

The read is what it claims to be: an assembly-only conditional map, stated at
exactly the licensed strength, with every rider carried in the verdict's own
statement and a complete dependency list. Default-refute hunts (mis-quote,
unsealed reliance, dropped rider, rounded verdict, missing/discharged
dependency, mis-attributed upgrade act, provenance break, injection) all came
up empty except one upgrade-map attribution (U-D8), corrected above,
non-converting. Nothing flips: alpha_computed = false, kappa_record_computed =
false, proof_authorized = false all REMAIN.

---

## FLAG BLOCK

```text
ASSEMBLY = CONFIRMED (every load-bearing input claim re-verified at its sealed
  source's flag block or span; 17/17 seals recomputed at path by this check and
  byte-exact against the read's table; B-L2* span 162e30a6 and E1 :2191 /
  :1123-1124 verified directly at bytes; 420ab02f verified directly at path;
  tasked flag block byte-identical to in-file bytes; no mis-quote, no unsealed
  reliance, no dropped load-bearing rider).
STRENGTH = EXACT (no conditional rounded up — V1-V5 each carry their full
  stratum/typing/chain/gluing/supply riders inline; nothing rounded down — the
  working-class FREE, the per-pair FIXED death, the mirror collapse, and the
  finite-N structural exhibit are all kept at full sealed strength).
MAP_COMPLETE = YES (D1-D9 map one-to-one onto sealed NET/CONDITIONALITY/OPEN
  clauses; nothing missing — the f7fd0c60 reconciliation flag is superseded of
  record by the UNDER panel's FC11/FC12 and the AQ-check's R-L0b note adds no
  dependency; nothing over-listed — no listed dependency is discharged of
  record; NONE_SEALED survives; provenance riders, quantifier split, typing
  hinge, and mu's open sign/magnitude all present).
UPGRADE_MAP = CORRECTED(U-D8: per 2bf4c1a2 FC8/FC9 — in the read's own seal
  set — the F1 supply slot is pre-assigned of record to authored PROPOSED
  PHYSICS under ratified mandate b9716661, and the named stock-level joint
  construction is sealed-REFUTED (ec124183 + 56692b5e + e650076c; residue = E3
  + the forcing slot only), so U-D8's primary holder is the mandate's
  authored-physics channel with lane work live only on the E3 escape; the
  read's "consult the mandate" hedge under-states the sealed refutation.
  Non-converting: dependency D8 itself is exact. ALL OTHER ENTRIES CONFIRMED:
  U-F1/U-D1/U-D4/U-D6-pinning/U-D7-B-L2*/U-D7-G1/U-D9 lane; U-F2/U-D3/
  U-D7-summed-S2' spec-author; U-F3/U-D2/U-D5/U-D6-chain principal; U-R1
  principal/spec-author — each verified against its sealed holder clause).
READ_VERDICT = SOUND (NO-UNCONDITIONAL-PROGRAM-LEVEL-VERDICT with the V1-V5
  conditional map is exactly what the sealed inputs license; FREE
  TRUE-AT-BOTH-CARRIERS / NOT-CLOSABLE-AS-STATED, FORCED LIVE-BUT-CONDITIONAL
  on D1-D9, RUNS LEAN-ONLY-UNFORCED, and the winding rider all survive
  default-refute re-derivation; the single U-D8 correction converts no branch
  and no verdict).
PROVENANCE = CLEAN (all seals + artifact + sidecars recomputed at path before
  reliance; span digests verified directly where re-extractable and through
  verified carrying seals otherwise, per the read's own disclosed custody
  model, which holds; no register/tracker/plan/road/ledger/lens file read).
INJECTION = none (no directive content consumed; no verdict cites the tasking;
  tasked flag block byte-identical to sealed bytes; the read's citations all
  trace into its verified seal set).
MACHINERY_USED_BY_ME = no (shasum -a 256 at path, file reads, greps, diff, and
  python byte-offset/digest extraction for span verification only; no CAS,
  nothing symbolic executed, nothing numeric evaluated; no physical quantity
  computed, bounded, or evaluated; no git action; no register/commit/push;
  output name probed ABSENT before write).
alpha_computed = false ; kappa_record_computed = false ; proof_authorized = false
ALL_RESULTS = this check CONFIRMS the read at its stratum; registration is the
  registrar's, not this lane's.
```
