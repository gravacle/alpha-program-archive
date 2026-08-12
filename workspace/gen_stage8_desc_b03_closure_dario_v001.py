#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_B03_CLOSURE_DARIO_V001.md   (relay 1066, DARIO lane)

This relay DISPOSITIONS; it does not construct. Its verifiable content is therefore custody and
anchoring: that both guards hold, that every declared member is at its pinned digest, that the
re-pinned span still rehashes, that every leg row carries an anchor, and that the arithmetic of the
remainder is internally consistent.

REFUSAL PATHS:
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member
  R3  GUARD 1: the delivery artifact is absent or fails its sidecar
  R4  GUARD 2: the entry addendum is absent or moved
  R5  the re-pinned span does not rehash to its declared digest, or lacks the d_U2 witness text
  R6  a leg row (L1..L6) is missing, or lacks a disposition keyword
  R7  the six dispositions do not sum to 6, or the tally line disagrees with the rows
  R8  body member-number citations do not resolve against the table
  R9  fence balance
  R10 residue
  R11 closure fixed point
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_DESC_B03_CLOSURE_DARIO_V001.md"; SIDE = Path(str(ART) + ".seal.sha256")
DELIVERY = WS / "STAGE8_DESC_THETA_HIST_DARIO_V001.md"
DELIVERY_DIGEST = "47f7c1248bcb46f631584fe647feb5e614a32ca8a894557d245d06ed343a64ba"
ADDENDUM = WS / "ATTACH_ENTRY_ADDENDUM_V001.md"
ADDENDUM_DIGEST = "420ab02f5ddb56ec8b3b49d3da4937c0045f2e2928fa233177dccda956914c73"
SPANSRC = WS / "STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md"
SPAN = (6266, 6883, "e6093b0f48c11d3f05d3c6fd3692b6ea2c4b320746bb92eebe72ef28ed697efe")
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
    if not DELIVERY.exists() or hf(DELIVERY)!=DELIVERY_DIGEST:
        return fail(3,"GUARD 1: delivery artifact absent or moved")
    if not ADDENDUM.exists() or hf(ADDENDUM)!=ADDENDUM_DIGEST:
        return fail(4,"GUARD 2: entry addendum absent or moved")
    print(f"GUARD 1 = PASSED (delivery {DELIVERY_DIGEST[:16]}…)")
    print(f"GUARD 2 = PASSED (addendum {ADDENDUM_DIGEST[:16]}…)")
    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    for _,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE")
    lo,hi,exp=SPAN
    seg=SPANSRC.read_bytes()[lo:hi]; d=hashlib.sha256(seg).hexdigest()
    if d!=exp: return fail(5,f"span digest {d} != {exp}")
    if b"d_U2" not in seg: return fail(5,"re-pinned span lacks the d_U2 witness text")
    print(f"RE-PINNED SPAN [{lo},{hi}) = {d[:32]}…  (d_U2 witness present)")
    # R6/R7 the six legs
    disp={}
    for n in range(1,7):
        m=re.search(rf"^\s*L{n}\s+(CLOSED-CONDITIONALLY|OPEN|CLOSED)\b",t,re.M)
        if not m: return fail(6,f"leg L{n} has no disposition row")
        disp[f"L{n}"]=m.group(1)
    closed=sum(1 for v in disp.values() if v=="CLOSED")
    cond=sum(1 for v in disp.values() if v=="CLOSED-CONDITIONALLY")
    op=sum(1 for v in disp.values() if v=="OPEN")
    if closed+cond+op!=6: return fail(7,f"dispositions do not sum to 6: {disp}")
    tally=f"LEGS = {closed}/6-CLOSED ; {cond}/6-CLOSED-CONDITIONALLY ; {op}/6-OPEN"
    if tally not in t: return fail(7,f"tally line disagrees with the rows; expected {tally!r}")
    print(f"LEGS = {closed} closed / {cond} conditional / {op} open  — rows agree with the tally")
    for k in sorted(disp): print(f"    {k}: {disp[k]}")
    # R8 citations
    ids={r[0] for r in rows}
    body=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",body):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(8,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")
    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(9,"fence left open")
    low=prose(t).lower(); hits=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in hits); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in hits: print(f"    {x!r}: {k}")
    if tot: return fail(10,"output-inspection token in authored prose")
    mk="CLOSURE_DECLARATION_END"
    for _ in range(8):
        b=ART.read_text(); i=b.find(mk)
        if i<0: return fail(11,"closure marker absent")
        v=f"{len(b[:i+len(mk)].encode()):08d}"
        nw=re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}",f"CLOSURE_END_BYTE = {v}",b)
        nw=re.sub(r"end byte [0-9X]{8}",f"end byte {v}",nw)
        if nw==b: print(f"CLOSURE_END_BYTE = {v} (fixed point reached)"); break
        ART.write_text(nw)
    else: return fail(11,"closure byte did not converge")
    dg=hf(ART); SIDE.write_text(f"{dg}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {dg}")
    return 0

if __name__=="__main__": raise SystemExit(main())
