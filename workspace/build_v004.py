#!/usr/bin/env python3
# Reproducible construction of STAGE8_DESC_DEMAND_DARIO_V004.md from sealed V003.
# Third-party replay:  shasum -c STAGE8_DESC_DEMAND_DARIO_V003.md.seal.sha256 && python3 build_v004.py
# Every change is a NAMED REPLACEMENT on the sealed V003 bytes; no free-hand editing.
import sys
SRC = 'STAGE8_DESC_DEMAND_DARIO_V003.md'
DST = 'STAGE8_DESC_DEMAND_DARIO_V004.md'
t = open(SRC, encoding='utf-8').read()

R = []  # (old, new) named replacements, applied in order, each asserted present exactly once

R.append(("VERDICT_BEARING_SET = exactly the 16 content-addressed members below",
          "VERDICT_BEARING_SET = exactly the 16 content-addressed members below\nPATH_RULE = an unqualified member name resolves in workspace/; a member written with a leading\n  <archive-root>/ resolves at the alpha-program-archive root.  Every member rehashes under this rule."))

R.append(("| 01 | `relay_inbox/RELAY_PASTE_993_DEMAND_V003_DARIO_V001.md` | `9dc354c6b56b7faf75ddbee1263f06f6bf0da91e89ba50989245449c0266f6a7` | assignment |",
          "| 01 | `<archive-root>/relay_inbox/RELAY_PASTE_995_DEMAND_V004_DARIO_V001.md` | `542e579f9ed98cfee3d03656c0d7e26f3594cdd9da83c4ea9aebd66f7700d1d7` | assignment (path root-anchored per PATH_RULE; rehashed at seal) |"))

R.append(("| 02 | `STAGE8_DESC_DEMAND_DARIO_V001.md`; `STAGE8_DESC_DEMAND_DARIO_V002.md` | `da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9`; `c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3` | my V001 and V002, both superseded here |",
          "| 02 | `STAGE8_DESC_DEMAND_DARIO_V001.md`; `STAGE8_DESC_DEMAND_DARIO_V002.md`; `STAGE8_DESC_DEMAND_DARIO_V003.md` | `da32dc9dfff38a32668b673e0c1b9e05fee27d02cd49b2f7ed99a78b71c51da9`; `c883d3732af61800f6ac2219e87406ccbbae60f7928172a80281e2e2cae951e3`; `fbf76d210bfc0981f51ead63d0e31de4c63785c845c61cc8d005100f2793e31e` | my V001, V002 and V003, all superseded here |"))

R.append(("| 03 | `STAGE8_DESC_DEMAND_CHECK_CODEX2_V001.md`; `STAGE8_DESC_DEMAND_V002_CHECK_CODEX2_V001.md` | `f3704df1bc4d7b2f45833fb12a40352117751e8f1b036ba0ab7de9fd4cfa1414`; `8f42e7dc3590bd0ba746f55c6ec9e055357c9c91b973306b334e37692fdaf91c` | the V001 check this folded, and **the V002 check this repairs against** |",
          "| 03 | `STAGE8_DESC_DEMAND_CHECK_CODEX2_V001.md`; `STAGE8_DESC_DEMAND_V002_CHECK_CODEX2_V001.md`; `STAGE8_DESC_DEMAND_V003_CHECK_CODEX2_V001.md` | `f3704df1bc4d7b2f45833fb12a40352117751e8f1b036ba0ab7de9fd4cfa1414`; `8f42e7dc3590bd0ba746f55c6ec9e055357c9c91b973306b334e37692fdaf91c`; `ba67264055f9191e864e2757a5380a5bdbfe3d5e5104ebb77d8f2f4b047429a1` | the three checks; **the V003 check supplies this pass's four custody items** |"))

R.append(("# STAGE 8 — DESCENT SECTION — THE DEMAND AT BYTES — DARIO LANE — V003",
          "# STAGE 8 — DESCENT SECTION — THE DEMAND AT BYTES — DARIO LANE — V004"))
R.append(("## RELAY 993 — `[PLAN:DESC-9]` — THE U12 SPAN AND AN HONEST CARRIAGE CERTIFICATE",
          "## RELAY 995 — `[PLAN:DESC-11]` — THE FOUR CUSTODY ITEMS, ONE PASS"))

# --- item 1: the diff triples, replayed with the tool the convention names ---
R.append(("""```text
DIFF V001 -> V002   (GNU unified, 3 context lines)
  V001 lines = 505 ; V002 lines = 530
  HUNKS      = 2
  INSERTIONS = 457
  DELETIONS  = 422

DIFF V002 -> V003
  HUNKS      = 10
  INSERTIONS = 158
  DELETIONS  = 37
```""",
"""```text
DIFF V001 -> V002   (GNU `diff -u`, the convention this certificate names)
  HUNKS = 2 ; INSERTIONS = 372 ; DELETIONS = 347

DIFF V002 -> V003   (same tool)
  HUNKS = 10 ; INSERTIONS = 158 ; DELETIONS = 38

DIFF V003 -> V004   (same tool; computed as a fixed point over this file)
  HUNKS = @@H34@@ ; INSERTIONS = @@I34@@ ; DELETIONS = @@D34@@
```

**Why V003's numbers were wrong, stated plainly.** V003 declared the convention *"GNU unified, 3
context lines"* and then computed with **python `difflib.unified_diff`**, which emits larger change
blocks and counts 457/422 and 160/39 on the same files. The certificate was of a different tool than
the one it named -- a certificate of memory rather than of the files, which is exactly what this pass
exists to remove. All three triples above were re-replayed with `diff -u` against the sealed bytes
immediately before sealing, and the first two reproduce the check's values independently."""))

# --- item 3: the set claim ---
R.append(("""**For V002 -> V003 the claim "nothing removed" is TRUE at the set level**, and it is stated only
because it was checked: V003's sixteen members are V002's fourteen plus two restorations.""",
"""### 6.5 The V002 -> V003 set claim, corrected

V003 said *"nothing removed is TRUE at the set level."* **That was wrong, and it is withdrawn.** The
true delta, by set comparison:

```text
V002 -> V003:  RETAINED 13 ; ADDED 7 ; DROPPED 1
DROPPED: relay_inbox/RELAY_PASTE_989_DEMAND_V002_DARIO_V001.md
```

That single drop is the **assignment row being REPLACED** -- the 989 assignment gave way to the 993
assignment -- which is lawful and routine, but it is a replacement and not an addition, so a file did
leave the set and "nothing removed" was false a second time. Stated exactly: **V002 -> V003 replaced
one row and added seven.**

For **V003 -> V004** the same replacement occurs once more and is declared rather than discovered:
the 993 assignment gives way to the 995 assignment at member 01; members 02 and 03 each gain a file;
nothing else changes. **V003 -> V004: one row REPLACED, two rows EXTENDED, none dropped beyond the
replaced assignment.**"""))

# --- item 2: the reproducible invocation ---
R.append(("""**CARRIED = SEMANTIC, precisely stated at §6.1:**""",
"""**METHOD = REPRODUCIBLE.** V004 is built from sealed V003 by named replacement only, via the script
`build_v004.py` reproduced verbatim at §6.6. A third party replays it with:

```bash
shasum -c STAGE8_DESC_DEMAND_DARIO_V003.md.seal.sha256 && python3 build_v004.py
```

Each replacement asserts its target is present exactly once before applying, so a drifted source
aborts the build rather than producing a silently different file.

- **CARRIED = SEMANTIC, precisely stated at §6.1:**"""))

for old, new in R:
    n = t.count(old)
    if n != 1:
        sys.exit('ABORT: target occurs %d times, expected 1:\n%s' % (n, old[:110]))
    t = t.replace(old, new)

open(DST, 'w', encoding='utf-8').write(t)
print('built %s from %s via %d named replacements' % (DST, SRC, len(R)))
