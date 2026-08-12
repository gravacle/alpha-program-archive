#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_SURFACE_FIRST_DARIO_V002.md   (relay 1054, DARIO lane)

This generator does real work: it RECOMPUTES the quarantine diff manifest that §2 publishes, so the
manifest is reproducible rather than asserted. It prints full 256-bit digests for every span on both
sides; the artifact tabulates the leading 128 bits for width.

DECLARED INPUTS: the nine members pinned in the artifact's closure table. The two regions diffed are
  PREFORM BODY  = member 04, "## STEP 1 — THE BUILD" .. "END OF FIXED TEXT"
  V001 §§1-2    = member 02, "## 1. STEP 1 — THE BUILD" .. "## 3. STEP 3 — THE EXHIBITION"

REFUSAL PATHS — emits NOTHING and exits non-zero if any fires:
  R1  a declared member is absent;
  R2  STRICT != STABLE on any declared member;
  R3  V001 (member 02) does not hash to the digest this relay pins — the subject must be
      BYTE-UNTOUCHED; this relay is append-only and may not have moved it;
  R4  either diffed region cannot be delimited, or its recomputed digest disagrees with the
      artifact's published region digest;
  R5  the recomputed group counts disagree with the counts the artifact publishes;
  R6  any of the four substantive spans disagrees with a digest the artifact publishes;
  R7  the preform's Step-1/2 body contains any of the nine field names (the §1 scan);
  R8  residue scan finds an output-inspection token in authored prose;
  R9  the closure byte does not reach a fixed point.

FENCES: no physical quantity evaluated, no member bound, no git/register/tracker action, writes only
this artifact and its sidecar inside workspace/.
"""

import difflib
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ART = ROOT / "workspace" / "STAGE8_DESC_SURFACE_FIRST_DARIO_V002.md"
SIDECAR = Path(str(ART) + ".seal.sha256")

V001 = ROOT / "workspace" / "STAGE8_DESC_SURFACE_FIRST_DARIO_V001.md"
V001_DIGEST = "953aa85b3aa7eac5f4763a8b26d85754270a114a38094a234ba33750af3608bd"
PREFORM = ROOT / "workspace" / "STAGE8_DESC_SURFACE_FIRST_STEP12_PREFORM_DARIO_V001.md"

PREFORM_REGION = ("## STEP 1 — THE BUILD", "END OF FIXED TEXT")
V001_REGION = ("## 1. STEP 1 — THE BUILD", "## 3. STEP 3 — THE EXHIBITION")
PREFORM_REGION_DIGEST = "08a589057f307e6af96a35807b916a29b1df39b4c25ec30f832409a922d0d85e"
V001_REGION_DIGEST = "c76748bfb04894f9a4204eb3c7dc6152eb7c3768a25b6faa08e777fe4ab06a69"

EXPECTED_GROUPS = 42
EXPECTED_SUBSTANTIVE = 4

# (id, preform line range, V001 region line range, published 128-bit prefixes)
SUBSTANTIVE = [
    ("C1", (30, 80), (25, 29), "3fff9996bba00dd0b4e0ccd5aac88586", "7484e8808144fc94dd1b7beb29d7cab0"),
    ("C2", (83, 84), (32, 78), "aebda527cbfc9af1c5386bf914fbb5b5", "a3d3f74ba1d8a1c790b1deb31a51cd1b"),
    ("C3", (115, 119), (113, 138), "f7d145051d1458cacda4455038b93006", "ce376a3def863585c52cf000004144b4"),
    ("C4", (198, 200), (218, 239), "b304f5f7e45b321fbdde66ee7b151cf0", "d20f2f3c8259a1806e0ed9f9f8739ef5"),
]

NINE_FIELDS = [
    "PhysicalCategory_0", "PhysicalObjectType_0", "PhysicalArityAndOperations_0",
    "PhysicalOperationDomains_0", "PhysicalOperationCodomains_0", "PhysicalParameterRecord_0",
    "PhysicalSupportAndCommonCore_0", "PhysicalRepresentationData_0",
    "PhysicalAlgebraicCausalAnalyticConditions_0",
]

RESIDUE_TOKENS_27 = [
    "137.03", "1/137", "0.00729", "7.297", "fine structure constant",
    "measured value", "measured alpha", "experimental value", "CODATA", "PDG",
    "observed coupling", "known value", "target value", "matches experiment",
    "agrees with experiment", "numerically equals", "evaluates to",
    "we compute alpha", "alpha =", "kappa_record =", "kappa_Thomson",
    "the answer is", "reproduces the observed", "in excellent agreement",
    "percent agreement", "sigma agreement", "best fit",
]
assert len(RESIDUE_TOKENS_27) == 27


def h(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def hf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def region(text: str, start: str, end: str) -> str:
    i, j = text.index(start), text.index(end)
    return text[i:j]


def parse_table(text: str):
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def authored_prose(text: str) -> str:
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence or re.match(r"^\|", line):
            continue
        out.append(line)
    return "\n".join(out)


def fail(code: int, msg: str) -> int:
    print(f"REFUSED (R{code}): {msg}", file=sys.stderr)
    return code


def main() -> int:
    if not ART.exists():
        return fail(1, "artifact absent")
    text = ART.read_text()

    # R3 — the subject must be byte-untouched by this append-only relay
    if not V001.exists():
        return fail(1, "V001 absent")
    d = hf(V001)
    if d != V001_DIGEST:
        return fail(3, f"V001 MOVED: {d} != {V001_DIGEST}. This relay is append-only.")
    print(f"V001 = BYTE-UNTOUCHED ({d[:16]}…)")

    # R1/R2
    rows = parse_table(text)
    if not rows:
        return fail(1, "no closure table parsed")
    ok = 0
    for rel, pinned in rows:
        p = ROOT / rel
        if not p.exists():
            return fail(1, f"declared member absent: {rel}")
        s = hf(p)
        if s != pinned:
            return fail(2, f"STRICT!=STABLE for {rel}: {s} != {pinned}")
        ok += 1
    print(f"PROSE_DIGESTS = {ok}/{len(rows)}, STRICT==STABLE")

    # R4 — regions
    try:
        pbody = region(PREFORM.read_text(), *PREFORM_REGION)
        vbody = region(V001.read_text(), *V001_REGION)
    except ValueError as e:
        return fail(4, f"region delimiter not found: {e}")
    pd, vd = h(pbody), h(vbody)
    if pd != PREFORM_REGION_DIGEST:
        return fail(4, f"preform region digest {pd} != published {PREFORM_REGION_DIGEST}")
    if vd != V001_REGION_DIGEST:
        return fail(4, f"V001 region digest {vd} != published {V001_REGION_DIGEST}")
    print(f"REGION preform body : {len(pbody.encode()):>6} B  {pd}")
    print(f"REGION V001 §§1-2   : {len(vbody.encode()):>6} B  {vd}")

    # R5 — group counts
    pl = pbody.splitlines(True)
    vl = vbody.splitlines(True)
    sm = difflib.SequenceMatcher(
        None, [x.rstrip("\n") for x in pl], [x.rstrip("\n") for x in vl], autojunk=False
    )
    groups = [op for op in sm.get_opcodes() if op[0] != "equal"]
    if len(groups) != EXPECTED_GROUPS:
        return fail(5, f"group count {len(groups)} != published {EXPECTED_GROUPS}")
    print(f"NON-EQUAL EDIT GROUPS = {len(groups)}  "
          f"({len(groups) - EXPECTED_SUBSTANTIVE} presentational / {EXPECTED_SUBSTANTIVE} substantive)")

    # R6 — substantive spans, both sides
    for cid, (a1, a2), (b1, b2), pexp, vexp in SUBSTANTIVE:
        ptxt = "".join(pl[a1 - 1: a2])
        vtxt = "".join(vl[b1 - 1: b2])
        ph, vh = h(ptxt), h(vtxt)
        if not ph.startswith(pexp):
            return fail(6, f"{cid} preform span digest {ph} does not match published {pexp}…")
        if not vh.startswith(vexp):
            return fail(6, f"{cid} V001 span digest {vh} does not match published {vexp}…")
        print(f"  {cid}  preform L{a1}-{a2} ({len(ptxt.encode())}B) {ph}")
        print(f"      V001    L{b1}-{b2} ({len(vtxt.encode())}B) {vh}")

    # R7 — the preform form-vocabulary scan
    hits = {f: pbody.count(f) for f in NINE_FIELDS if pbody.count(f)}
    if hits:
        return fail(7, f"nine-field vocabulary present in the preform body: {hits}")
    print("PREFORM FORM-VOCABULARY SCAN = 0/9 field names in the Step-1/2 body")

    # R8 — residue
    low = authored_prose(text).lower()
    rh = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in rh)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in rh:
        print(f"    {t!r}: {n}")
    if total:
        return fail(8, "output-inspection token in authored prose")

    # R9 — declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ART.read_text()
        i = body.find(marker)
        if i < 0:
            return fail(9, "closure end marker absent")
        val = f"{len(body[: i + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ART.write_text(new)
    else:
        return fail(9, "closure byte did not reach a fixed point")

    # final: confirm V001 still untouched after all work
    if hf(V001) != V001_DIGEST:
        return fail(3, "V001 moved during the relay")
    print("V001 = BYTE-UNTOUCHED (rechecked after sealing work)")

    dg = hf(ART)
    SIDECAR.write_text(f"{dg}  {ART.name}\n")
    print(f"SEALED {ART.name}\n  {dg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
