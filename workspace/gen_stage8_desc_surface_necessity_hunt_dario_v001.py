#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_SURFACE_NECESSITY_HUNT_DARIO_V001.md   (relay 1081, DARIO lane)

A HUNT, not a candidate. It authors nothing, so the gates differ from the candidate generators:
there is no ledger, no selection disclosure and no PROPOSED_NOT_ADOPTED header to check. What is
checked instead is that the artifact stays a hunt, and that the ruling it reaches is not the
comfortable one taken cheaply.

REFUSAL PATHS:
  R1  a declared member is absent
  R2  STRICT != STABLE on a declared member (digest computed at the path, never from a display)
  R3  the measure mandate is absent or moved — the hunt's guard subject
  R4  a pinned span does not rehash at its own path and bounds, or the published count disagrees
  R5  a body member-number citation does not resolve
  R6  a numeric-evaluation path exists in this generator's own code
  R7  AUTHORING GATE: the artifact carries a candidate's apparatus (a ledger line, a selection
      disclosure, an adoption header) — a hunt that starts authoring must refuse
  R8  SELF-FAVOUR GATE: the ruling JOINT-SOURCE-RECORD-STATE is the one that validates this lane's
      own prior relays, so it may be sealed ONLY with its declared guard, its self-attack, and the
      correction this relay owes its own predecessor artifact all present
  R9  FORK GATE: an IMPLICATION that names a principal decision must name BOTH prongs
  R10 fence depth-walk
  R11 residue scan
  R12 closure fixed point
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_DESC_SURFACE_NECESSITY_HUNT_DARIO_V001.md"; SIDE = Path(str(ART)+".seal.sha256")
SELF = Path(__file__)
MANDATE = WS / "MEASURE_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "b9716661d1a03a16ec7fd06c836de2f74dbae0acafa0564c9241f96e791b420c"
AUTHORING_MARKERS = ["LEDGER = ", "SELECTION_DISCLOSED", "PROPOSED_NOT_ADOPTED",
                     "PENDING PRINCIPAL ENTRY", "CERT_SHAPE = "]
NUMERIC_PATH = ["random", "numpy", "cmath", "montecarlo", "monte carlo", "seed(", "sample",
                "tolerance", "math.", "statistics"]
TOK = ["137.03","1/137","0.00729","7.297","fine structure constant","measured value","measured alpha",
 "experimental value","CODATA","PDG","observed coupling","known value","target value",
 "matches experiment","agrees with experiment","numerically equals","evaluates to","we compute alpha",
 "alpha =","kappa_record =","kappa_Thomson","the answer is","reproduces the observed",
 "in excellent agreement","percent agreement","sigma agreement","best fit"]
assert len(TOK)==27
hf=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def fail(c,m): print(f"REFUSED (R{c}): {m}", file=sys.stderr); return c
def prose(t):
    o,f=[],False
    for l in t.splitlines():
        if l.strip().startswith("```"): f=not f; continue
        if f or re.match(r"^\|",l): continue
        o.append(l)
    return "\n".join(o)

def main():
    if not ART.exists(): return fail(1,"artifact absent")
    t=ART.read_text()

    # R6 first: a generator that could compute must not be trusted to say it did not. String
    # literals are stripped so the refusal list cannot satisfy the scan that looks for it.
    code=re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits=[k for k in NUMERIC_PATH if k in code]
    if hits: return fail(6,f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code): return fail(6,"numeric literal in generator code")
    print("NO_NUMERIC_PATH = CLEAN (generator scanned its own code; nothing is computed)")

    if not MANDATE.exists() or hf(MANDATE)!=MANDATE_DIGEST:
        return fail(3,"the measure mandate is absent or moved; the hunt's guard subject is gone")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")

    # R7 the artifact must remain a hunt
    found=[m for m in AUTHORING_MARKERS if m in t]
    if found: return fail(7,f"authoring apparatus in a hunt: {found}")
    if "AUTHORS NOTHING" not in t: return fail(7,"the authors-nothing declaration is missing")
    print("AUTHORING_GATE = CLEAN (no ledger, no selection, no entry header; authors-nothing declared)")

    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    paths={}
    for num,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
        paths[num]=p
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)} STRICT==STABLE (computed at path)")

    spans=re.findall(r"^\s*member (\d{2}) \[(\d+),(\d+)\)\s+([0-9a-f]{64})\s*$",t,re.M)
    if not spans: return fail(4,"no pinned spans declared")
    for num,a,b,dg in spans:
        if num not in paths: return fail(4,f"span cites unclosed member {num}")
        raw=paths[num].read_bytes()[int(a):int(b)]
        if len(raw)!=int(b)-int(a): return fail(4,f"span [{a},{b}) out of range in member {num}")
        got=hashlib.sha256(raw).hexdigest()
        if got!=dg: return fail(4,f"span digest mismatch member {num} [{a},{b}): {got}")
    if f"PINNED_SPANS = {len(spans)}/{len(spans)}" not in t:
        return fail(4,f"published span count != computed ({len(spans)})")
    print(f"PINNED_SPANS = {len(spans)}/{len(spans)} recomputed at path; published count matches")

    ids={r[0] for r in rows}
    doc=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",doc):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(5,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")

    # R8 the comfortable ruling may not be taken cheaply
    if "READOFF_CONSUMES = JOINT-SOURCE-RECORD-STATE" in t:
        need={"the declared guard":"THE GUARD, DECLARED BEFORE THE RULING",
              "the self-attack":"THE ATTACK I RAN ON MY OWN RULING",
              "the correction owed to the predecessor":"CORRECTION I OWE MY OWN PROBE",
              "the not-this section":"WHAT THIS HUNT DOES NOT SAY"}
        missing=[k for k,v in need.items() if v not in t]
        if missing:
            return fail(8,"the ruling that validates this lane's own prior work is missing "
                          f"{missing}")
        print("SELF_FAVOUR_GATE = CLEAN (guard, self-attack, predecessor correction and scope "
              "limits all present alongside the favourable ruling)")

    # R9 a fork must show both prongs
    if "CONDITIONAL ON A PRINCIPAL DECISION" in t:
        prongs=[p for p in ("RUN-FROM-TRACE-FEASIBILITY-HUNT","CLOSE-TO-MANDATE-DECISION")
                if p not in t]
        if prongs: return fail(9,f"a principal fork is declared but a prong is missing: {prongs}")
        print("FORK_GATE = CLEAN (both prongs named; the choice is left to the principal)")

    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(10,"fence left open")
    low=prose(t).lower(); h=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in h); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in h: print(f"    {x!r}: {k}")
    if tot: return fail(11,"output-inspection token in authored prose")

    mk="CLOSURE_DECLARATION_END"
    for _ in range(8):
        b=ART.read_text(); i=b.find(mk)
        if i<0: return fail(12,"closure marker absent")
        v=f"{len(b[:i+len(mk)].encode()):08d}"
        nw=re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}",f"CLOSURE_END_BYTE = {v}",b)
        nw=re.sub(r"end byte [0-9X]{8}",f"end byte {v}",nw)
        if nw==b: print(f"CLOSURE_END_BYTE = {v} (fixed point reached)"); break
        ART.write_text(nw)
    else: return fail(12,"closure byte did not converge")
    dg=hf(ART); SIDE.write_text(f"{dg}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {dg}")
    return 0

if __name__=="__main__": raise SystemExit(main())
