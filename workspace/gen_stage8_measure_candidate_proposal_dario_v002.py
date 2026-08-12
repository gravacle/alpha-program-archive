#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_MEASURE_CANDIDATE_PROPOSAL_DARIO_V002.md   (relay 1079, DARIO lane)

Carries every refusal path the MEASURE SUPPLY MANDATE makes mandatory, plus the three repairs the
opposite-lane check of V001 ordered:

  * the EXTRACTOR REPAIR.  The check found that the identifier class never reaches an operator and
    that the load-bearing product operation WAS an operator.  R6 no longer promises coverage: it
    PROVES it, by refusing any construction block containing a character outside [A-Za-z0-9_] and
    whitespace.  Every non-whitespace character then lies inside an identifier token, so totality of
    the extractor is a property of the block rather than a claim about the regex.
  * the NUMERIC PATH DELETION.  The check ruled V001's Monte-Carlo a fence defect.  It is deleted,
    not tightened, and R10 scans THIS FILE's own source to keep it deleted.
  * the LEDGER GATE.  R11 recomputes the published forced/authored counts from the tables and
    refuses if a FORCED row rests on a DARIO-authored member.

REFUSAL PATHS:
  R1  a declared member is absent
  R2  STRICT != STABLE on a declared member (digest computed at the path, never from a display)
  R3  MANDATE absent or moved — authoring omega_phys is unlawful without it
  R4  the verbatim PROPOSED_NOT_ADOPTED header is missing
  R5  a body member-number citation does not resolve
  R6  CLOSED CLAIM — character-class totality, total map, INV-1..INV-4, published receipt
  R7  SELECTION DISCLOSURE, with the record's own foreclosing sentence quoted against the candidate
  R8  the predecessor (V001) is not byte-identical — supersession must be append-only
  R9  a pinned span does not rehash at its own path and bounds
  R10 a numeric-evaluation path exists in this generator's own source
  R11 the published ledger counts disagree with the tables, or a FORCED row cites a DARIO member
  R12 DESCENT = STOP without the full cost display
  R13 fence depth-walk
  R14 residue scan
  R15 closure fixed point
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_MEASURE_CANDIDATE_PROPOSAL_DARIO_V002.md"; SIDE = Path(str(ART)+".seal.sha256")
SELF = Path(__file__)
MANDATE = WS / "MEASURE_SUPPLY_MANDATE_DECISION_OF_RECORD_V001.md"
MANDATE_DIGEST = "b9716661d1a03a16ec7fd06c836de2f74dbae0acafa0564c9241f96e791b420c"
PRED = WS / "STAGE8_MEASURE_CANDIDATE_PROPOSAL_DARIO_V001.md"
PRED_DIGEST = "c64c44fbc07248038d6005280dfc128e9faf60e985fc9a0c7cc7817438d0870f"
HEADER = ("PROPOSED_NOT_ADOPTED — PENDING PRINCIPAL ENTRY "
          "(MEASURE_SUPPLY_MANDATE_DECISION_OF_RECORD_V001, b9716661d1a0…)")
LEDGER_ROWS = {f"F{i}" for i in range(1,16)} | {"A1","A2"}
DARIO_MEMBERS = {"03","05","11","14","16","22"}   # my own lane's outputs — never forcing grounds
IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
BLOCK_CLASS = re.compile(r"[^A-Za-z0-9_\s]")
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
def block(t,a,b):
    ma=re.search(rf"^{re.escape(a)}\s*$",t,re.M); mb=re.search(rf"^{re.escape(b)}\s*$",t,re.M)
    if not ma or not mb or mb.start()<=ma.end(): raise ValueError("delimiters")
    return t[ma.end():mb.start()]

def main():
    if not ART.exists(): return fail(1,"artifact absent")
    t=ART.read_text()

    # R10 first: a generator that could compute must not be trusted to say it did not.
    # The scan region is this file's CODE: every string literal is stripped first, so the refusal
    # list and the residue table cannot satisfy the scan that looks for them. A real numeric path
    # appears as code (an import, an attribute, a numeric literal), never as a quoted datum.
    code=re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits=[k for k in NUMERIC_PATH if k in code]
    if hits: return fail(10,f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code): return fail(10,"numeric literal in generator code")
    print("NO_NUMERIC_PATH = CLEAN (generator scanned its own source; nothing is computed)")

    if not MANDATE.exists() or hf(MANDATE)!=MANDATE_DIGEST:
        return fail(3,"MEASURE SUPPLY MANDATE absent or moved; authoring omega_phys is unlawful")
    print(f"MANDATE = LIVE ({MANDATE_DIGEST[:16]}…)")
    if not PRED.exists() or hf(PRED)!=PRED_DIGEST:
        return fail(8,"predecessor V001 is absent or has moved; supersession must be append-only")
    print(f"PREDECESSOR = BYTE-UNTOUCHED ({PRED_DIGEST[:16]}…)")
    if HEADER not in t: return fail(4,"verbatim PROPOSED_NOT_ADOPTED header missing")
    print("HEADER = VERBATIM-PRESENT")

    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    paths={}
    for num,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
        paths[num]=p
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE (computed at path)")

    # R9 pinned spans — bounds and digest recomputed from the member's own bytes
    spans=re.findall(r"^\s*member (\d{2}) \[(\d+),(\d+)\)\s+([0-9a-f]{64})\s*$",t,re.M)
    if not spans: return fail(9,"no pinned spans declared")
    for num,a,b,dg in spans:
        if num not in paths: return fail(9,f"span cites unclosed member {num}")
        raw=paths[num].read_bytes()[int(a):int(b)]
        if len(raw)!=int(b)-int(a): return fail(9,f"span [{a},{b}) out of range in member {num}")
        got=hashlib.sha256(raw).hexdigest()
        if got!=dg: return fail(9,f"span digest mismatch member {num} [{a},{b}): {got}")
    print(f"PINNED_SPANS = {len(spans)}/{len(spans)} recomputed at path and matched")

    ids={r[0] for r in rows}
    doc=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",doc):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(5,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")

    # R6 CLOSED CLAIM — the extractor repair the check ordered
    cons=block(t,"CONSTRUCTION_BEGIN","CONSTRUCTION_END")
    off=BLOCK_CLASS.findall(cons)
    if off: return fail(6,f"construction block carries {len(off)} character(s) outside the "
                          f"identifier class — the extractor cannot be proved total: {sorted(set(off))}")
    print("EXTRACTOR = PRODUCT-OP-COVERED (0 characters outside [A-Za-z0-9_] and whitespace; "
          "every non-whitespace character lies in an identifier token, so totality is a property "
          "of the block, not a promise about the regex)")
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
    unmapped=[s for s in toks if "_" in s or len(s)==1]
    unmapped=[s for s in unmapped if s not in smap]
    if unmapped: return fail(6,f"INV-4: structural tokens unmapped: {unmapped}")
    uncovered=[s for s in toks if s not in smap and s not in vocab]
    if uncovered: return fail(6,f"CLOSED CLAIM BROKEN — symbols in neither table: {uncovered}")
    idle=sorted(set(smap)-set(toks))
    if idle: return fail(6,f"map declares symbols the construction does not use: {idle}")
    nsym=len(toks); nrow=len({smap[s] for s in toks})
    claim=(f"CLOSED_CLAIM = {nsym} symbols / {nrow} rows / 0 unmapped / vocabulary "
           f"{'EMPTY (sentinel NONE)' if not vocab else str(len(vocab))+' words'}")
    if claim not in t:
        return fail(6,f"published closed-claim line != computed; expected exactly: {claim!r}")
    print(f"{claim}  (published line matches)")

    # R11 ledger gate — counts recomputed, and no FORCED row may rest on my own lane
    frows=re.findall(r"^\|\s*F(\d+)\s*\|(.*)$",t,re.M)
    arows=re.findall(r"^\|\s*\*\*(A\d+)\*\*\s*\|",t,re.M)
    if not frows or not arows: return fail(11,"ledger tables not found")
    for n,rest in frows:
        cited=set(re.findall(r"members?\s+(\d{2})",rest)) | set(re.findall(r"\band (\d{2})\b",rest))
        selfcite=sorted(cited & DARIO_MEMBERS)
        if selfcite: return fail(11,f"FORCED row F{n} rests on DARIO-authored member(s) {selfcite}")
    nf,na=len(frows),len(set(arows))
    published=f"LEDGER = {nf}-FORCED / {na}-AUTHORED"
    if published not in t:
        return fail(11,f"published ledger != computed; expected exactly: {published!r}")
    print(f"{published} (recomputed from the tables; no FORCED row cites a DARIO member)")

    # R12 an unqualified STOP is not admissible
    if "DESCENT = STOP" in t:
        missing=[c for c in ("COST-1","COST-2","COST-3") if c not in t]
        if missing: return fail(12,f"STOP declared without its cost display: {missing}")
        print("DESCENT = STOP with COST-1..COST-3 displayed — admissible")

    # R7 selection disclosure
    if "SELECTION_DISCLOSED = YES" not in t:
        return fail(7,"a Haar/simple-form candidate must disclose the selection")
    if "does not satisfy that condition" not in t:
        return fail(7,"the record's own foreclosing sentence must be quoted against the candidate")
    print("SELECTION_DISCLOSED = YES, with the record's foreclosing sentence quoted against it")

    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(13,"fence left open")
    low=prose(t).lower(); h=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in h); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in h: print(f"    {x!r}: {k}")
    if tot: return fail(14,"output-inspection token in authored prose")

    mk="CLOSURE_DECLARATION_END"
    for _ in range(8):
        b=ART.read_text(); i=b.find(mk)
        if i<0: return fail(15,"closure marker absent")
        v=f"{len(b[:i+len(mk)].encode()):08d}"
        nw=re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}",f"CLOSURE_END_BYTE = {v}",b)
        nw=re.sub(r"end byte [0-9X]{8}",f"end byte {v}",nw)
        if nw==b: print(f"CLOSURE_END_BYTE = {v} (fixed point reached)"); break
        ART.write_text(nw)
    else: return fail(15,"closure byte did not converge")
    if hf(PRED)!=PRED_DIGEST: return fail(8,"predecessor moved during the run")
    print(f"PREDECESSOR = BYTE-UNTOUCHED after sealing ({PRED_DIGEST[:16]}…)")
    dg=hf(ART); SIDE.write_text(f"{dg}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {dg}")
    return 0

if __name__=="__main__": raise SystemExit(main())
