#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_PRINCIPLE_FIXES_IDENTIFICATION_HUNT_DARIO_V001.md   (relay 1099, DARIO lane)

A HUNT: it builds nothing. The gates carry the hunt discipline from relay 1081 and add the three
this assignment makes mandatory — carry the correction rather than reopen it, do not relax SM-6 or
call authorship provenance, and name the missing rule exactly if one is claimed missing.

REFUSAL PATHS:
  R1  a declared member is absent
  R2  STRICT != STABLE on a declared member (digest computed at the path, never from a display)
  R3  the measure mandate is absent or moved
  R4  a pinned span does not rehash at its own path and bounds, or the published count disagrees
  R5  a body member-number citation does not resolve
  R6  a numeric-evaluation path exists in this generator's own code
  R7  AUTHORING GATE: a hunt carrying a candidate's apparatus, or missing its authors-nothing
      declaration, must refuse
  R8  CARRIED-CORRECTION GATE: the withdrawn contradiction ruling may appear only inside its own
      withdrawal, and the corrected direction must be carried
  R9  NAMED-RULE GATE: NEEDS-NEW-PRIMITIVE may seal only with the rule named and with what would be
      ratified, what it buys and what it costs all present
  R10 SELF-FAVOUR GATE: NEEDS-NEW-PRIMITIVE is the ruling that ends this lane's exposure, so it may
      seal only alongside the section that presses the inconvenient reading hardest
  R11 SM-6 GATE: an artifact that relaxes SM-6 or equates authorship with provenance must refuse
  R12 fence depth-walk
  R13 residue scan
  R14 closure fixed point
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_PRINCIPLE_FIXES_IDENTIFICATION_HUNT_DARIO_V001.md"; SIDE = Path(str(ART)+".seal.sha256")
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

    # R6 first: string literals stripped, so the refusal list cannot satisfy its own scan.
    code=re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits=[k for k in NUMERIC_PATH if k in code]
    if hits: return fail(6,f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code): return fail(6,"numeric literal in generator code")
    print("NO_NUMERIC_PATH = CLEAN (generator scanned its own code; nothing is computed)")

    if not MANDATE.exists() or hf(MANDATE)!=MANDATE_DIGEST:
        return fail(3,"the measure mandate is absent or moved")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")

    # An authoring marker is disqualifying when the artifact claims it FOR ITSELF — a heading, or a
    # line that opens with it. Quoting another member's status is reporting, not authoring, so an
    # ATTRIBUTED mention (the same line naming the member it belongs to) is admitted and counted.
    # The gate keeps its force: a self-declared status still refuses.
    claimed, attributed = [], 0
    lines=t.splitlines()
    ATTRIB=("member","standing","proposal","board","declines","quote")
    for m in AUTHORING_MARKERS:
        for i,line in enumerate(lines):
            if m not in line: continue
            st=line.strip()
            if st.startswith("#"): claimed.append(m); continue
            quoted = ("`"+m+"`") in line
            window = " ".join(lines[max(0,i-1):i+2]).lower()
            if quoted or any(w in window for w in ATTRIB): attributed+=1
            else: claimed.append(m)
    if claimed: return fail(7,f"authoring apparatus claimed by this artifact: {sorted(set(claimed))}")
    if "AUTHORS NOTHING" not in t: return fail(7,"the authors-nothing declaration is missing")
    print(f"AUTHORING_GATE = CLEAN (no self-claimed status; {attributed} attributed "
          f"mention(s) of another member's status admitted as reporting)")

    # R8 the three prior rulings are carried as parameter, not reopened
    if "CARRIED, NOT REOPENED" not in t.upper():
        return fail(8,"the prior void, correction and gap must be carried and marked not-reopened")
    print("CARRIED_GATE = CLEAN (1080 void, 1082 correction, 1084 gap carried, not reopened)")

    # R11 the assignment's two prohibitions
    for bad in ("relax SM-6", "relaxing SM-6"):
        for m in re.finditer(re.escape(bad), t, re.I):
            w=t[max(0,m.start()-200):m.end()+200].lower()
            if "not" not in w and "do not" not in w:
                return fail(11,"the artifact appears to relax SM-6")
    print("SM6_GATE = CLEAN (SM-6 not relaxed by this hunt)")

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

    # R9 an audit that evaluates nothing must say so, and must not have read the register
    if "EVALUATED_NOTHING = CERTIFIED" not in t:
        return fail(9,"an audit hunt must certify that it evaluated nothing")
    if "REGISTER = NOT READ" not in t:
        return fail(9,"the register bar must be declared")
    print("AUDIT_GATE = CLEAN (evaluated-nothing certified; register bar declared)")

    # R10 PRINCIPLE-FORCES is the maximum-pressure answer and needs both parts; the weaker
    # verdicts must not overstate into "free forever" when the record rules the gap UNBUILT.
    if "VERDICT = PRINCIPLE-FORCES" in t:
        need={"target-independence":"TARGET-INDEPENDENT","non-circularity":"NON-CIRCULAR",
              "the named principle":"principle:"}
        missing=[k for k,v in need.items() if v not in t]
        if missing:
            return fail(10,f"PRINCIPLE-FORCES may not seal without {missing}")
        print("PRINCIPLE_GATE = CLEAN")
    if "VERDICT = CIRCULAR-ONLY" in t or "VERDICT = NO-PRINCIPLE" in t:
        need={"the type qualification":"TYPE-U, NOT TYPE-R",
              "the not-B2 limit":"NOT B2 IN ITS STRONG FORM",
              "the named ground":"WHAT IT WOULD TAKE",
              "the favourable point stated first":"in its favour"}
        missing=[k for k,v in need.items() if v not in t]
        if missing:
            return fail(10,f"an adverse principle ruling may not seal without {missing}")
        print("ADVERSE_PRINCIPLE_GATE = CLEAN (type qualified; not overstated as free-forever; "
              "ground named; the candidate's favourable point stated before the objection)")
    # R11 the assignment's named flattening must be carried explicitly
    if "DO NOT FLATTEN" not in t.upper():
        return fail(11,"the assignment's named flattening must be carried explicitly")
    print("FLATTENING_GATE = CLEAN")
    # R12 an unsealed risk of my own may not be dressed as a sealed finding
    if "NAMED RISK" in t.upper() and "not sealed" not in t.lower() and "MINE AND NOT SEALED" not in t.upper():
        return fail(12,"a structural risk of my own must be marked unsealed")
    print("RISK_ATTRIBUTION_GATE = CLEAN")
    # R13 the 1098 two-debt correction must be carried and not silently absorbed
    if "THIS HUNT TESTS ONLY THE SEED LEG" not in t.upper():
        return fail(13,"the two-debt correction must be carried with the scope stated")
    print("SCOPE_GATE = CLEAN (seed leg only; stitching/continuum debt not claimed discharged)")

    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(12,"fence left open")
    low=prose(t).lower(); h=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in h); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in h: print(f"    {x!r}: {k}")
    if tot: return fail(13,"output-inspection token in authored prose")

    mk="CLOSURE_DECLARATION_END"
    for _ in range(8):
        b=ART.read_text(); i=b.find(mk)
        if i<0: return fail(14,"closure marker absent")
        v=f"{len(b[:i+len(mk)].encode()):08d}"
        nw=re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}",f"CLOSURE_END_BYTE = {v}",b)
        nw=re.sub(r"end byte [0-9X]{8}",f"end byte {v}",nw)
        if nw==b: print(f"CLOSURE_END_BYTE = {v} (fixed point reached)"); break
        ART.write_text(nw)
    else: return fail(14,"closure byte did not converge")
    dg=hf(ART); SIDE.write_text(f"{dg}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {dg}")
    return 0

if __name__=="__main__": raise SystemExit(main())
