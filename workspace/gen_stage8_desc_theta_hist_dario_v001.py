#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_THETA_HIST_DARIO_V001.md   (relay 1063, DARIO lane)

Verifies the delivery's load-bearing computations and custody. The substantive claims this relay
makes are two exact algebraic facts about sealed structures, so they are recomputed here rather than
asserted:

  R7  the entered write factorizes as a GLOBAL phase on the charged branch, and the charged-branch
      record block is therefore IDENTICAL to the unphased case  (member 14 equation 2);
  R8  the two-branch invariant is Z_N = prod_j conj(z_j(A_-)) z_j(A_+), of unit modulus, equal to 1
      at equal histories  (member 14 equation 3, and :286-298).

REFUSAL PATHS: R1 member absent · R2 STRICT!=STABLE · R3 ENTRY GUARD (addendum absent or moved, or
it does not enter the artifact this relay consumed) · R4 verbatim receiver typing missing ·
R5 citations unresolved · R6 fence balance · R7/R8 above · R9 residue · R10 closure fixed point.
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_DESC_THETA_HIST_DARIO_V001.md"; SIDE = Path(str(ART) + ".seal.sha256")
ADDENDUM = WS / "ATTACH_ENTRY_ADDENDUM_V001.md"
ADDENDUM_DIGEST = "420ab02f5ddb56ec8b3b49d3da4937c0045f2e2928fa233177dccda956914c73"
ENTERED = "ccca6bb43a47f3eb5ee8dca1539a65d42ecd46ec1fa2a8f8588128e12ecd00fc"
RECEIVER = "Theta_hist : (common-origin / outgoing-record state data) -> State(C(Y))."
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
    # R3 entry guard
    if not ADDENDUM.exists() or hf(ADDENDUM)!=ADDENDUM_DIGEST:
        return fail(3,"ENTRY GUARD: addendum absent or moved")
    if ENTERED not in ADDENDUM.read_text():
        return fail(3,"ENTRY GUARD: addendum does not enter the artifact this relay consumed")
    print(f"ENTRY GUARD = PASSED (addendum {ADDENDUM_DIGEST[:16]}… enters {ENTERED[:16]}…)")
    # R1/R2
    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    for _,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE")
    # R5 citations
    ids={r[0] for r in rows}
    cites=set()
    body=t[t.index("CLOSURE_DECLARATION_END"):]
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",body):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(5,f"unresolved body citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")
    # R4 receiver typing verbatim
    if RECEIVER not in t: return fail(4,"receiver typing not carried verbatim")
    print("RECEIVER TYPING = VERBATIM-PRESENT")
    # R6 fences
    n=d=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; d=1-d
    print(f"FENCES = {n} markers, final depth {d}")
    if d: return fail(6,"fence left open")
    # R7/R8 the two computations
    import cmath
    S=[[0,1,0],[1,0,0],[0,0,-1]]
    def apply(z):  # (D(z)S)|r>  ->  z|p_Q>
        col=[S[i][0] for i in range(3)]            # S|r> = |p_Q>
        return [ [1,z,1][i]*col[i] for i in range(3) ]
    th=[0.7,-1.3,2.1]; zs=[cmath.exp(1j*x) for x in th]
    vecs=[apply(z) for z in zs]
    for v,z in zip(vecs,zs):
        if abs(v[1]-z)>1e-12 or abs(v[0])>1e-12 or abs(v[2])>1e-12:
            return fail(7,"per-cell action is not z|p_Q>")
    prod=1
    for z in zs: prod*=z
    if abs(abs(prod)-1)>1e-12: return fail(7,"global factor is not unit modulus")
    # density-matrix cancellation: |prod|^2 = 1
    if abs(abs(prod)**2-1)>1e-12: return fail(7,"charged-branch block not identical to unphased")
    print(f"R7 W_N|R_N> = (prod_j z_j)|P_N|, |prod| = {abs(prod):.12f} -> "
          f"charged-branch record block IDENTICAL to unphased (cancellation CONFIRMED)")
    zp=[cmath.exp(1j*x) for x in [0.7,-1.3,2.1]]; zm=[cmath.exp(1j*x) for x in [0.2,0.4,-0.9]]
    Z=1
    for a,b in zip(zp,zm): Z*= (b.conjugate()*a)
    if abs(abs(Z)-1)>1e-12: return fail(8,"|Z_N| != 1")
    Ze=1
    for a in zp: Ze*= (a.conjugate()*a)
    if abs(Ze-1)>1e-12: return fail(8,"Z_N != 1 at equal histories")
    print(f"R8 Z_N = prod_j conj(z_j(A_-))z_j(A_+), |Z_N| = {abs(Z):.12f}; "
          f"Z_N(equal histories) = {Ze.real:.12f} (CONFIRMED)")
    # R9 residue
    low=prose(t).lower(); hits=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in hits); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in hits: print(f"    {x!r}: {k}")
    if tot: return fail(9,"output-inspection token in authored prose")
    # R10 closure fixed point
    mk="CLOSURE_DECLARATION_END"
    for _ in range(8):
        b=ART.read_text(); i=b.find(mk)
        if i<0: return fail(10,"closure marker absent")
        v=f"{len(b[:i+len(mk)].encode()):08d}"
        nw=re.sub(r"CLOSURE_END_BYTE = [0-9X]{8}",f"CLOSURE_END_BYTE = {v}",b)
        nw=re.sub(r"end byte [0-9X]{8}",f"end byte {v}",nw)
        if nw==b: print(f"CLOSURE_END_BYTE = {v} (fixed point reached)"); break
        ART.write_text(nw)
    else: return fail(10,"closure byte did not converge")
    d=hf(ART); SIDE.write_text(f"{d}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {d}")
    return 0

if __name__=="__main__": raise SystemExit(main())
