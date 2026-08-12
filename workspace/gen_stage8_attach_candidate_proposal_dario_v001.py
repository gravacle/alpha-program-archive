#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md   (relay 1052, DARIO lane)

DECLARED INPUTS: the twenty members pinned in the artifact's own closure table, plus the re-pinned
Attach span (member 05, lines 314-334) that the ATTACH SUPPLY MANDATE requires be re-pinned under
CLOSURE_MEMBER_CITATION_RULE_V001.

REFUSAL PATHS — the generator emits NOTHING and exits non-zero if any of these fires:
  R1  a declared member is absent at its full archive-root path;
  R2  a declared member's digest disagrees with the digest pinned in the closure table
      (STRICT != STABLE);
  R3  the re-pinned Attach span does not rehash to the digest the artifact pins for it;
  R4  the MANDATE is absent, or fails the digest the artifact pins for it — authoring without a
      live mandate is exactly what this relay may not do;
  R5  the verbatim PROPOSED_NOT_ADOPTED header required by the assignment is missing;
  R6  the ingredient-ledger invariant fails: the artifact must contain both ledger tables and the
      closed-claim sentence that binds them (§8.4);
  R7  the residue scan finds an output-inspection token in authored prose;
  R8  the declared-first closure byte does not reach a fixed point.

FENCES: evaluates no physical quantity, binds no member, runs no physical fixed point, performs no
git/register/tracker action, writes only inside workspace/.
"""

import hashlib
import re
import sys
from pathlib import Path

ARCHIVE_ROOT = Path("/Users/bgm/MB Work/alpha-program-archive")
ARTIFACT = ARCHIVE_ROOT / "workspace" / "STAGE8_ATTACH_CANDIDATE_PROPOSAL_DARIO_V001.md"
SIDECAR = Path(str(ARTIFACT) + ".seal.sha256")

MANDATE_REL = "workspace/ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "ad9fc14e1f07494f7527d95f2a94ee7a26da9d49cc784c409f31325f54572213"

ATTACH_SPAN_SOURCE_REL = (
    "workspace/STAGE8_TASK2D_SOURCE_HISTORY_MAP_COVARIANT_INCIDENCE_DERIVATION_ADJUDICATION_V001.md"
)
ATTACH_SPAN_LINES = (314, 334)
ATTACH_SPAN_DIGEST = "be0be903041fcface7336a2facf157c5459d7e4ccb8e3d1deb0785fbf08d52ad"

REQUIRED_HEADER = (
    "PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
    "(ATTACH_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, ad9fc14e1f07…)"
)

# The ledger invariant: both tables plus the closed claim that binds them.
LEDGER_MARKERS = [
    "### 5.1 FORCED — with spans",
    "### 5.2 AUTHORED — the minimal core, counted and justified",
    "There is no third category",
]

LIVE_MEMBERS: list[str] = []

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


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_closure_table(text: str) -> list[tuple[str, str]]:
    rows = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", line)
        if m:
            rows.append((m.group(2), m.group(3)))
    return rows


def authored_prose(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or re.match(r"^\|", line):
            continue
        out.append(line)
    return "\n".join(out)


def fail(code: int, msg: str) -> int:
    print(f"REFUSED (R{code}): {msg}", file=sys.stderr)
    return code


def main() -> int:
    if not ARTIFACT.exists():
        return fail(1, f"artifact absent at {ARTIFACT}")
    text = ARTIFACT.read_text()

    # R4 — the mandate must be live. Authoring without it is unlawful for this relay.
    mpath = ARCHIVE_ROOT / MANDATE_REL
    if not mpath.exists():
        return fail(4, "the ATTACH SUPPLY MANDATE is absent; authoring is not authorized")
    if sha256_file(mpath) != MANDATE_DIGEST:
        return fail(4, "the ATTACH SUPPLY MANDATE does not match its pinned digest")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")

    # R5 — verbatim header
    if REQUIRED_HEADER not in text:
        return fail(5, "the verbatim PROPOSED_NOT_ADOPTED header is missing")
    print("HEADER = VERBATIM-PRESENT")

    # R6 — ledger invariant
    missing_markers = [m for m in LEDGER_MARKERS if m not in text]
    if missing_markers:
        return fail(6, f"ingredient-ledger invariant broken; missing {missing_markers}")
    print("LEDGER_INVARIANT = BOTH-TABLES-PRESENT + CLOSED-CLAIM-PRESENT")

    # R1/R2 — strict vs stable
    rows = parse_closure_table(text)
    if not rows:
        return fail(1, "no closure table parsed; nothing is grounded")
    ok, missing, moved = 0, [], []
    for rel, pinned in rows:
        p = ARCHIVE_ROOT / rel
        if not p.exists():
            missing.append(rel)
            continue
        s = sha256_file(p)
        if s == pinned:
            ok += 1
        else:
            moved.append((rel, pinned, s))
    if missing:
        return fail(1, f"declared members absent: {missing}")
    if moved:
        for rel, pinned, s in moved:
            print(f"  MOVED: {rel}\n    stable={pinned}\n    strict={s}", file=sys.stderr)
        return fail(2, "STRICT != STABLE")
    print(f"PROSE_DIGESTS = {ok}/{len(rows)}, STRICT==STABLE")
    print(f"LIVE_MEMBERS  = {len(LIVE_MEMBERS)} (none declared; modes coincide by construction)")

    # R3 — the re-pinned Attach span
    src = (ARCHIVE_ROOT / ATTACH_SPAN_SOURCE_REL).read_text().splitlines(keepends=True)
    lo, hi = ATTACH_SPAN_LINES
    span = "".join(src[lo - 1: hi])
    span_digest = sha256_bytes(span.encode())
    if span_digest != ATTACH_SPAN_DIGEST:
        return fail(3, f"Attach span digest mismatch: {span_digest} != {ATTACH_SPAN_DIGEST}")
    if "No such `Attach` exists" not in span:
        return fail(3, "the re-pinned span does not contain the absence adjudication")
    print(f"ATTACH_SPAN = RE-PINNED ({span_digest[:16]}…, lines {lo}-{hi}, absence text present)")

    # R7 — residue
    low = authored_prose(text).lower()
    hits = [(t, low.count(t.lower())) for t in RESIDUE_TOKENS_27 if low.count(t.lower())]
    total = sum(n for _, n in hits)
    print(f"RESIDUE_SCAN(27 tokens over authored prose) = {total} hit(s)")
    for t, n in hits:
        print(f"    {t!r}: {n}")
    if total:
        return fail(7, "output-inspection token found in authored prose")

    # R8 — declared-first fixed point
    marker = "CLOSURE_DECLARATION_END"
    for _ in range(8):
        body = ARTIFACT.read_text()
        idx = body.find(marker)
        if idx < 0:
            return fail(8, "closure end marker absent")
        val = f"{len(body[: idx + len(marker)].encode()):08d}"
        new = re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}", f"CLOSURE_END_BYTE = {val}", body)
        new = re.sub(r"end byte [0-9X]{8}", f"end byte {val}", new)
        if new == body:
            print(f"CLOSURE_END_BYTE = {val} (fixed point reached)")
            break
        ARTIFACT.write_text(new)
    else:
        return fail(8, "closure byte did not reach a fixed point")

    digest = sha256_file(ARTIFACT)
    SIDECAR.write_text(f"{digest}  {ARTIFACT.name}\n")
    print(f"SEALED {ARTIFACT.name}\n  {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
