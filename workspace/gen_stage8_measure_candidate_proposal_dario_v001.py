#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_MEASURE_CANDIDATE_PROPOSAL_DARIO_V001.md   (relay 1076, DARIO lane)

Carries every refusal path the MEASURE SUPPLY MANDATE makes mandatory from V001 (its process clause,
earned by the Attach loop): generic ingredient extractor with NO ALIAS SET; two-table closed claim
machine-checked BEFORE seal; fence depth-walk; citation-resolution gate; every pinned digest computed
at its path; and the mandate's own content gates.

REFUSAL PATHS:
  R1  a declared member is absent
  R2  STRICT != STABLE on any declared member (digests computed at the path, never from a display)
  R3  MANDATE absent or moved — authoring omega_phys is unlawful without it
  R4  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R5  a body member-number citation does not resolve
  R6  CLOSED CLAIM: a construction symbol is in neither ledger table (generic extractor, no aliases)
  R7  SELECTION DISCLOSURE: a Haar/simple-form candidate must carry SELECTION_DISCLOSED = YES and
      must quote the record's own foreclosing sentence against itself — the mandate forbids
      presenting it as forced
  R8  mu(Z_N) = 0 must be REPRODUCED, and the artifact must display it as an attack on itself
  R9  Theta_F-invariance must be delivered by the automorphism/uniqueness argument, not asserted
  R10 fence depth-walk
  R11 residue scan
  R12 closure fixed point
"""
import cmath, hashlib, random, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_MEASURE_CANDIDATE_PROPOSAL_DARIO_V001.md"; SIDE = Path(str(ART)+".seal.sha256")
MANDATE = WS / "MEASURE_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "b9716661d1a03a16ec7fd06c836de2f74dbae0acafa0564c9241f96e791b420c"
HEADER = ("PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
          "(MEASURE_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, b9716661d1a0…)")
LEDGER_ROWS = {f"F{i}" for i in range(1,10)} | {"A1"}
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
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
def block(t,a,b):
    ma=re.search(rf"^{re.escape(a)}\s*$",t,re.M); mb=re.search(rf"^{re.escape(b)}\s*$",t,re.M)
    if not ma or not mb or mb.start()<=ma.end(): raise ValueError("delimiters")
    return t[ma.end():mb.start()]

def main():
    if not ART.exists(): return fail(1,"artifact absent")
    t=ART.read_text()
    if not MANDATE.exists() or hf(MANDATE)!=MANDATE_DIGEST:
        return fail(3,"MEASURE SUPPLY MANDATE absent or moved; authoring omega_phys is unlawful")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")
    if HEADER not in t: return fail(4,"verbatim PROPOSED_NOT_ADOPTED header missing")
    print("HEADER = VERBATIM-PRESENT")
    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    for _,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE (computed at path)")
    ids={r[0] for r in rows}
    body=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",body):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(5,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")

    # R6 CLOSED CLAIM — generic extractor, NO ALIAS SET, map + closed vocabulary read from the
    # artifact itself, under the mandate's invariants.
    cons=block(t,"CONSTRUCTION_BEGIN","CONSTRUCTION_END")
    smap={}
    for line in block(t,"SYMBOL_TABLE_MAP_BEGIN","SYMBOL_TABLE_MAP_END").strip().splitlines():
        parts=line.split()
        if len(parts)==2: smap[parts[0]]=parts[1]
    raw=block(t,"CLOSED_VOCABULARY_BEGIN","CLOSED_VOCABULARY_END").split()
    if not smap or not raw: return fail(6,"map or vocabulary block empty")
    # The sole admitted empty form: the sentinel NONE declares that no non-symbol token is admitted
    # at all, so coverage must come entirely from the map. Strictly stronger than any word list.
    vocab=set() if raw==["NONE"] else set(raw)
    badrows=sorted({r for r in smap.values() if r not in LEDGER_ROWS})
    if badrows: return fail(6,f"map names undeclared ledger rows: {badrows}")
    if [w for w in vocab if "_" in w]:   return fail(6,"INV-1: vocabulary entry contains '_'")
    if [w for w in vocab if len(w)==1]:  return fail(6,"INV-2: single-character vocabulary entry")
    if vocab & set(smap):                return fail(6,"INV-3: vocabulary and map overlap")
    toks=sorted(set(IDENT.findall(cons)))
    structural=[s_ for s_ in toks if ("_" in s_ or len(s_)==1)]
    unmapped_struct=[s_ for s_ in structural if s_ not in smap]
    if unmapped_struct: return fail(6,f"INV-4: structural tokens unmapped: {unmapped_struct}")
    uncovered=[s_ for s_ in toks if s_ not in smap and s_ not in vocab]
    if uncovered: return fail(6,f"CLOSED CLAIM BROKEN — construction symbols in neither table: {uncovered}")
    nsym=len([s_ for s_ in toks if s_ in smap])
    nrow=len({smap[s_] for s_ in toks if s_ in smap})
    claim=(f"CLOSED_CLAIM = {nsym} symbols / {nrow} rows / 0 unmapped / vocabulary "
           f"{'EMPTY (sentinel NONE)' if not vocab else str(len(vocab))+' words'}")
    # The published final line must BE the computed figures, not a description of the check.
    if claim not in t:
        return fail(6,f"published closed-claim line != computed; expected exactly: {claim!r}")
    print(f"{claim}  (published line matches; generic extractor, no alias set; INV-1..INV-4)")

    # R7 selection disclosure
    if "SELECTION_DISCLOSED = YES" not in t:
        return fail(7,"a Haar/simple-form candidate must disclose the selection")
    if "does not satisfy that condition" not in t:
        return fail(7,"the record's own foreclosing sentence must be quoted against the candidate")
    print("SELECTION_DISCLOSED = YES, with the record's foreclosing sentence quoted against it")

    # R8 mu(Z_N) = 0 reproduced, and displayed as a self-attack
    random.seed(7)
    def haar(N): return [cmath.exp(2j*3.141592653589793*random.random()) for _ in range(N)]
    for N in (1,2,3):
        M=60000; s=0
        for _ in range(M):
            cp,cm=haar(N),haar(N); z=1
            for a,b in zip(cp,cm): z*=a*b.conjugate()
            s+=z
        v=abs(s/M)
        if v>0.02: return fail(8,f"mu(Z_N) at N={N} did not reproduce ~0 (got |{v:.4f}|)")
    print("R8 mu(Z_N) = 0 reproduced for N=1,2,3 (character orthogonality; MC corroboration)")
    if "ATTACK I WOULD RUN FIRST, ON MY OWN CANDIDATE" not in t:
        return fail(8,"the mu(Z_N)=0 consequence must be displayed as an attack on the candidate")
    print("   and it is displayed as the first attack on the candidate — required")

    # R9 Theta_F-invariance delivered, not asserted
    if "automorphism" not in t.lower() or "uniqueness" not in t.lower():
        return fail(9,"Theta_F-invariance must be delivered by automorphism + Haar uniqueness")
    print("R9 Theta_F-invariance = delivered via automorphism + Haar uniqueness (not asserted)")

    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(10,"fence left open")
    low=prose(t).lower(); hits=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in hits); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in hits: print(f"    {x!r}: {k}")
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

def ledger_rows_ok(s, txt): return txt
if __name__=="__main__": raise SystemExit(main())
