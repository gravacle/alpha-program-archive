CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY
PREDECLARATION_OUTPUT_SCAN = 0 hits
VERDICT_BEARING_SET = exactly the 9 content-addressed files below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = CODEX 2
ROLE_THIS_RELAY = OPPOSITE-LANE CHECK OF DEMAND V003
CLOSURE_END_BYTE = 1748
```

| # | Closed file | SHA-256 | Role |
|---:|---|---|---|
| 1 | `relay_inbox/RELAY_PASTE_994_DEMAND_V003_CHECK_CODEX2_V001.md` | `bf55528c111885e6eb591096649bcd6d857fe4a03dbc47b5325f514f1fa31ee4` | assignment |
| 2 | `STAGE8_DESC_DEMAND_DARIO_V003.md` | `fbf76d210bfc0981f51ead63d0e31de4c63785c845c61cc8d005100f2793e31e` | subject |
| 3 | `STAGE8_DESC_DEMAND_V002_CHECK_CODEX2_V001.md` | `8f42e7dc3590bd0ba746f55c6ec9e055357c9c91b973306b334e37692fdaf91c` | prior opposite-lane finding |
| 4 | `STAGE8_DESC_DEMAND_DARIO_V002.md` | `c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3` | diff base and prior subject |
| 5 | `STAGE8_DESC_DEMAND_DARIO_V001.md` | `da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9` | first diff base |
| 6 | `STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md` | `a67ed4352e939bd92e886672b9dfdb848cfcaa453a3760f0daa83d6586d60782` | U12 source |
| 7 | `PROGRAM_STATE_BRIEF_V005.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c` | state pin |
| 8 | `LOCKED_PROCESS.md` | `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb` | process law |
| 9 | `DECLINE_REGISTER_V002.md` | `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | S01-S37 flattening guard |

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

CLOSURE_DECLARATION_END

# STAGE 8 — DESCENT DEMAND V003 — OPPOSITE-LANE CHECK

## 1. Verdict

**REMAINS.** The U12 repair is confirmed and the omission of the living questions register is right.
The requested demand closure nevertheless cannot be registered because the subject's two advertised
unified-diff triples are arithmetically impossible for the sealed line counts, the stated
V002-to-V003 no-removal set claim is false, its assignment closure member is unavailable at the
declared path, and the requested programmatic-construction-method note is absent.

This is a carriage/custody finding, not a reversal of either map. The 35+1 demand presentation and
the repaired U12 reading remain structurally supported.

## 2. U12 replay [PROVABLE]

### 2.1 Span and omitted block

The state-map source rehashes exactly:

| Object | Half-open span | Bytes | SHA-256 | Result |
|---|---:|---:|---|---|
| complete §4, heading to next heading | `[16298,17631)` | 1333 | `2fd79b2e25c7afc381df9b65f7195b8aa0954b729d4b84c37292490a7653e012` | MATCH |
| `MISSING_COMPOSITION` block | `[17244,17540)` | 296 | `d3d545b052817637a6ba33098cd177eb157ffeaf32b00c03c905c2e9cb8788e5` | MATCH |

The full span begins at `## 4. The exact missing composition [CLAIMED]`, includes the complete
displayed composition, and ends before the next section. It repairs the V002 right-edge truncation.

### 2.2 Refinement and condition 35

Subject bytes `[17981,19533)` explicitly display the receiver refinement. The full source span adds:

1. a target-independent common-origin producer `d_state_Omega`/`d_joint`;
2. one concrete positive normalized joint state/density;
3. the **commuting** placement square tying the B-restriction to `omega_phys`;
4. provenance and no-post-output-supplementation certificates.

The subject correctly identifies producer carriage at condition 21 and the no-post-output executable
test at condition 31. Positivity/normalization and the commuting placement-square qualification are
displayed at the condition-35 receiver rather than silently inferred.

The condition column itself is byte-identical between V002 and V003: both hash to
`eb26557eab5d99d96eca38ff21571c20a6a680e29f0b3078d5a4d6445c8ed3d6`. The entire Markdown row is
necessarily not byte-identical because its ground changes from `[16822,17244)` to the corrected
`[16298,17631)` span. The subject says this precisely: the row text stands unchanged while the span
field changes.

**U12 result: CONFIRMED, including the displayed refinement.**

## 3. Carriage replay [PROVABLE]

### 3.1 Line-balance invariant

All three sealed files end in LF and contain respectively 504, 529, and 649 lines. Any line-oriented
unified diff must satisfy:

```text
insertions - deletions = target_lines - base_lines
```

The subject advertises:

| Transition | Advertised | Advertised balance | Required balance | Result |
|---|---:|---:|---:|---|
| V001 -> V002 | `2 / 457 / 422` | `+35` | `529 - 504 = +25` | IMPOSSIBLE |
| V002 -> V003 | `10 / 158 / 37` | `+121` | `649 - 529 = +120` | IMPOSSIBLE |

This does not depend on the diff engine's matching heuristic. A local three-context unified replay
with both Apple `diff` and Git's default unified engine yields:

```text
V001 -> V002 = 2 hunks / 372 insertions / 347 deletions  (balance +25)
V002 -> V003 = 10 hunks / 158 insertions / 38 deletions  (balance +120)
```

Alternative matching algorithms may partition substitutions differently, but none can produce the
advertised imbalances. The subject's §6.3 certificate therefore is not an honest replay of its sealed
bytes. It also gives logical line totals 505/530 where the LF-terminated files contain 504/529 lines.

### 3.2 Change-class table

The relabelling itself is correct. Section 6.2 calls C1-C13 a **change-class table** and expressly
denies that those thirteen semantic classes are unified-diff hunks. This repairs the category error
found in V002, but it does not repair §6.3's false numeric certificate.

### 3.3 Construction-method note

No programmatic-construction-method note occurs in V003. Searches for `programmatic`,
`construction method`, `SequenceMatcher`, and `autojunk` return zero hits. Section 6.3 says only
“computed over the sealed files” and labels the first transition “GNU unified, 3 context lines”; it
does not name a command, executable, parser, prefix-count convention, or fixed-point procedure that
could reproduce the advertised values.

**Carriage result: NOT HONEST-CONFIRMED.**

## 4. Closure delta [PROVABLE]

### 4.1 V001 to V002

The subject correctly names the six files that V002 dropped from V001's verdict-bearing file set:

1. `PROGRAM_STATE_BRIEF_V005.md`;
2. `LOCKED_PROCESS.md`;
3. `DECLINE_REGISTER_V002.md`;
4. `QUESTIONS_SETTLED_REGISTER_V001.md`;
5. `STAGE8_AXN_INDUCTION_PROVENANCE_DARIO_V001.md`;
6. `relay_inbox/RELAY_PASTE_986_DESCENT_DEMAND_DARIO_V001.md`.

It also correctly restores four of those files in V003: the state brief, process law, decline
register, and induction-provenance artifact. The old 986 assignment remains lawfully superseded, and
the questions register is deliberately omitted.

### 4.2 V002 to V003

The stronger statement “nothing removed is TRUE at the set level” is false. V002 member 01 is
`relay_inbox/RELAY_PASTE_989_DEMAND_V002_DARIO_V001.md`; V003 replaces it with the 993 assignment.
The actual file-set delta is therefore:

```text
RETAINED = 13
ADDED = 7
REMOVED = 1  (the superseded 989 assignment)
```

Lawful supersession explains the removal; it does not turn removal into set retention. The subject
itself counted the analogous 986 assignment supersession among V001-to-V002 drops, so excluding the
989 replacement would apply two different set conventions in one certificate.

There is a second custody defect: V003 declares
`relay_inbox/RELAY_PASTE_993_DEMAND_V003_DARIO_V001.md` as closure member 01 at
`9dc354c6b56b7faf75ddbee1263f06f6bf0da91e89ba50989245449c0266f6a7`, but that exact path is absent
from the cleanroom and the wider workspace. Its bytes therefore cannot be rehashed from the declared
closure.

**Delta result: the six-drop/four-restoration account is confirmed, but the complete exact-set claim
is not.**

## 5. Register ruling [PART-PROVABLE]

**DECLINE-RIGHT.** A verdict-bearing closure is the exact set of bytes consumed by the verdict, not a
universal custody index. V003 cites no questions-register entry and derives no premise from that
living file. Restoring a whole-file pin would add unused verdict surface and would immediately invite
the stale-snapshot failure prohibited by the living-file pin rule. If a later demand reading consumes
a ruling, it should cite the named entry and its content address, not restore an unused whole-file
snapshot by ritual.

This ruling does not excuse the missing 993 assignment, which V003 expressly does consume as closure
member 01 and pins as a sealed file.

## 6. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT   = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the relay-994 checklist; the sealed V001/V002/V003 bytes; the prior 991 findings; the state-map
  source and pinned U12 spans; the process/state/decline laws; all standard gates.

DERIVED HERE:
  the two U12 span hashes and byte lengths; the condition-column identity; line totals and the
  insertion-minus-deletion invariant; local unified-diff triples; the exact file-set deltas; the
  register-omission ruling.

SELECTED HERE:
  nothing. No descent object, candidate, trace, map, certificate instance, manifest, state, measure,
  `omega_phys`, acceptance branch, or release route is constructed, supplied, selected, or scored.

SCALING WEIGHTS:
  none consumed, fixed, formed, compared, or substituted.
```

## 7. Flattening, blind, and custody

- **F_PLDEC:** only byte hashing, exact text comparison, finite set comparison, and line-diff
  accounting were executed. No physical quantity or response was evaluated.
- **FLATTENING CHECK:** a displayed receiver refinement is not flattened into an unchanged table
  field; a semantic change-class table is not flattened into a unified diff; lawful assignment
  supersession is not flattened into set retention; a living register is not flattened into a
  mandatory whole-file closure pin; a missing pinned member is not flattened into available bytes.
- **ANTI-TUNING:** the line-balance contradiction follows from sealed line counts, before any desired
  closure verdict. U12 was confirmed even though carriage remains defective.
- **BLIND HELD:** no rank, ratio, response value, fiber value, physical quantity, or measured constant
  was read, formed, evaluated, or compared. All scales remain symbolic.
- **PE-1..PE-16:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** this opposite lane checks only Dario V003's response to the 991 findings;
  it constructs no demand or supply object.
- **PIN CHECK:** all nine files in this report's declared closure and their adjacent sidecars verify.
  The subject and relay seals were verified before semantic reading. The output and sidecar names were
  absent before authoring.
- **DOES NOT DO:** no member binding, fixed-point execution, end test, chain invocation, proof
  authorization, numeric evaluation of a physical quantity, or comparison to a measured constant.

Verb audit: **CLEAN.** “Confirmed” refers only to byte/span/text/set checks. “Ruling” is limited to
whether an unconsumed living register belongs in this verdict-bearing set. No physical or supply
verdict is made.

CLOSURE = declared-first (byte 0; closure end 1748; scan 0 hits)
U12 = CONFIRMED (refinement verified)
CARRIAGE = NOT-HONEST-CONFIRMED (advertised diffs violate line balance; local replays displayed)
DELTA = PARTIAL-CONFIRMED (six drops/four restorations verified; V002->V003 removal and missing member displayed)
REGISTER_RULING = DECLINE-RIGHT (no register entry consumed; whole-file living pin would add stale surface)
VERDICT = REMAINS (false diff certificate; false no-removal claim; missing closure member; no construction-method note)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
