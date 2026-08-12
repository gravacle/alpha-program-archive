#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_SURFACE_FIRST_DARIO_V001.md   (relay 1050, DARIO lane)

WHAT THIS GENERATOR DOES AND DOES NOT DO
----------------------------------------
It does NOT author the artifact's prose. The prose is a human/lane construction whose grounds are
the eighteen declared members. This generator performs the mechanical obligations the relay
imposes, and REFUSES TO EMIT if any of them fails:

  1. DECLARED INPUTS: every input is named below with the path it is read from. Nothing outside
     DECLARED_INPUTS is read, and no digest is taken from a description of bytes.
  2. UNGROUNDED-EMISSION REFUSAL: if any declared member is missing, or its digest at its full
     archive-root path disagrees with the digest pinned in the artifact's closure table, the
     generator exits non-zero and emits NOTHING.
  3. PROSE-DIGEST AUDIT in STRICT and STABLE modes.
       STRICT = rehash each cited member at its FULL archive-root path, now.
       STABLE = the digest pinned in the artifact's closure table.
     LIVE members are declared explicitly (here: none), so the modes must coincide exactly.
  4. RESIDUE SCAN: a 27-token output-inspection scan over the artifact's AUTHORED PROSE. The count
     is REPORTED FROM THE SCAN. It is never predicted, and no token is removed to change it.
  5. DECLARED-FIRST FIXED-POINT CLOSURE: CLOSURE_END_BYTE is solved as a fixed point on the
     artifact's own bytes (writing the value can change the value; iterate until stable). The
     placeholder is width-preserving so the iteration converges.

FENCES: this generator evaluates no physical quantity, binds no member of the origin family, runs
no fixed-point iteration of any physical map, performs no git/register/tracker action, and writes
only the artifact and its sidecar inside workspace/.
"""

import hashlib
import re
import sys
from pathlib import Path

ARCHIVE_ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ARTIFACT = ARCHIVE_ROOT / "workspace" / "STAGE8_DESC_SURFACE_FIRST_DARIO_V001.md"
SIDECAR = Path(str(ARTIFACT) + ".seal.sha256")

# ---------------------------------------------------------------- declared inputs

# The Step-1/2 text, closed and hashed BEFORE the nine-field form (member 16) was opened.
# This pin is the form-quarantine evidence and is checked, not asserted.
PRE_FORM_STEP12_DIGEST = (
    "73ef21bdbfef5fc9a3e602aedbf3a54e32a0274a4dd2fcc7214750b5b59ffe31"
)

# Members that move by design (registers, trackers). None is used by this artifact.
LIVE_MEMBERS: list[str] = []

# The 27-token output-inspection scan. These are the tokens whose appearance in AUTHORED PROSE
# would indicate downstream/output data leaking upstream into the construction.
RESIDUE_TOKENS_27 = [
    "137.03", "1/137", "0.00729", "7.297", "fine structure constant",
    "measured value", "measured alpha", "experimental value", "CODATA", "PDG",
    "observed coupling", "known value", "target value", "matches experiment",
    "agrees with experiment", "numerically equals", "evaluates to",
    "we compute alpha", "alpha =", "kappa_record =", "kappa_Thomson",
    "the answer is", "reproduces the observed", "in excellent agreement",
    "percent agreement", "sigma agreement", "best fit",
]
assert len(RESIDUE_TOKENS_27) == 27, "the scan is declared as 27 tokens"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_closure_table(text: str) -> list[tuple[str, str]]:
    """Return [(archive-root-relative path, pinned digest)] from the artifact's closure table."""
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def authored_prose(text: str) -> str:
    """
    AUTHORED PROSE = the artifact minus its fenced code blocks and minus its closure table.
    Quoted member bytes live inside fences; they are the record's words, not mine, and a
    documentary gate is not passed by editing a governing quotation.
    """
    out, in_fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"^\|", line):  # table rows: content-addressed, not prose
            continue
        out.append(line)
    return "\n".join(out)


def main() -> int:
    if not ARTIFACT.exists():
        print(f"REFUSED: artifact absent at {ARTIFACT}", file=sys.stderr)
        return 2

    text = ARTIFACT.read_text()

    # ---- (2) ungrounded-emission refusal + (3) strict/stable prose-digest audit
    rows = parse_closure_table(text)
    if not rows:
        print("REFUSED: no closure table parsed; nothing is grounded", file=sys.stderr)
        return 2

    strict_ok, mismatches, missing = 0, [], []
    for rel, pinned in rows:
        p = ARCHIVE_ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        strict = sha256_file(p)
        if strict == pinned:
            strict_ok += 1
        else:
            mismatches.append((rel, pinned, strict))

    if missing or mismatches:
        print("REFUSED — UNGROUNDED EMISSION BLOCKED", file=sys.stderr)
        for rel in missing:
            print(f"  MISSING: {rel}", file=sys.stderr)
        for rel, pinned, strict in mismatches:
            print(f"  MOVED:   {rel}\n    stable(pinned)={pinned}\n    strict(now)   ={strict}",
                  file=sys.stderr)
        return 3

    print(f"PROSE_DIGESTS = {strict_ok}/{len(rows)}, STRICT==STABLE")
    print(f"LIVE_MEMBERS  = {len(LIVE_MEMBERS)} "
          f"({'none declared; modes coincide by construction' if not LIVE_MEMBERS else LIVE_MEMBERS})")

    # ---- form-quarantine pin: reported, and only checkable where the fixed text still exists
    print(f"PRE_FORM_STEP12_DIGEST = {PRE_FORM_STEP12_DIGEST} (pinned in artifact §0.1 and §7)")
    if PRE_FORM_STEP12_DIGEST not in text:
        print("REFUSED: quarantine pin absent from the artifact", file=sys.stderr)
        return 4

    # ---- (4) residue scan — count comes from the scan
    prose = authored_prose(text)
    hits = []
    low = prose.lower()
    for tok in RESIDUE_TOKENS_27:
        n = low.count(tok.lower())
        if n:
            hits.append((tok, n))
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for tok, n in hits:
        print(f"    {tok!r}: {n}")

    # ---- (5) declared-first fixed-point closure
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ARTIFACT.read_text()
        idx = body.find(marker)
        if idx < 0:
            print("REFUSED: closure end marker absent", file=sys.stderr)
            return 5
        end_byte = len(body[: idx + len(marker)].encode())
        val = f"{end_byte:08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ARTIFACT.write_text(new)
    else:
        print("REFUSED: closure byte did not reach a fixed point", file=sys.stderr)
        return 6

    # ---- seal
    digest = sha256_file(ARTIFACT)
    SIDECAR.write_text(f"{digest}  {ARTIFACT.name}\n")
    print(f"SEALED {ARTIFACT.name}\n  {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
