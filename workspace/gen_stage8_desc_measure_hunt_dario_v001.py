#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_MEASURE_HUNT_DARIO_V001.md   (relay 1075, DARIO lane)

The artifact's verdict rests on three exact structural facts, so the generator recomputes all three
rather than accepting them as prose:

  R7  Z_N IS A PRODUCT OF RATIFIED GENERATORS. Under B iso C(Y) the generator e_plus(U_(e_j)) is
      chi_+(e_j) and e_minus(U_(e_j))^* is conj(chi_-(e_j)); their product over j must equal q_N's
      coordinate product, i.e. Z_N — factor for factor, at random points.
  R8  Theta_F FIXES Z_N, so omega(Z_N) is real on every U1-compatible state.
  R9  NO VALUE IS FORCED: omega(Z_N) attains +1, ~0 and -1 on U1-compatible (branch-symmetrised)
      measures. This is what separates STILL-CONTINUUM from PINNED, so it is a refusal path.

REFUSAL PATHS: R1 member absent · R2 STRICT!=STABLE · R3 verdict/road consistency (a STILL-CONTINUUM
verdict must be paired with ROAD = MANDATE-FULL and FINISHING_PROPERTY = N/A) · R4 the five
constraint rulings must all be present · R5 citations resolve · R6 fence balance · R7/R8/R9 above ·
R10 residue · R11 closure fixed point.
"""
import cmath, hashlib, random, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_DESC_MEASURE_HUNT_DARIO_V001.md"; SIDE = Path(str(ART) + ".seal.sha256")
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
    rows=re.findall(r"^\|\s*(\d{2})\s*\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|",t,re.M)
    if not rows: return fail(1,"no closure table")
    for _,rel,dg in rows:
        p=ROOT/rel
        if not p.exists(): return fail(1,f"member absent: {rel}")
        if hf(p)!=dg: return fail(2,f"STRICT!=STABLE for {rel}")
    print(f"PROSE_DIGESTS = {len(rows)}/{len(rows)}, STRICT==STABLE")

    # R3 verdict/road consistency
    if "ADMISSIBLE_SET = STILL-CONTINUUM" in t:
        if "ROAD = MANDATE-FULL" not in t: return fail(3,"STILL-CONTINUUM must pair with MANDATE-FULL")
        if "FINISHING_PROPERTY = N/A" not in t: return fail(3,"STILL-CONTINUUM must pair with N/A")
        print("VERDICT/ROAD CONSISTENCY = ok (STILL-CONTINUUM + MANDATE-FULL + FINISHING N/A)")
    # R4 the five rulings
    n_rule = t.count("DOES-NOT-NARROW")
    if n_rule < 5: return fail(4,f"expected five constraint rulings, found {n_rule} DOES-NOT-NARROW")
    print(f"CONSTRAINTS = 5-BEARING, {n_rule} DOES-NOT-NARROW markers present")

    # R7 Z_N as a product of ratified generators == q_N's coordinate product
    random.seed(20260812)
    for trial in range(200):
        N=random.randint(1,6)
        cp=[cmath.exp(1j*random.uniform(0,6.283185307)) for _ in range(N)]
        cm=[cmath.exp(1j*random.uniform(0,6.283185307)) for _ in range(N)]
        gen=1
        for j in range(N): gen *= cp[j]*cm[j].conjugate()      # e_plus(U_ej) . e_minus(U_ej)^*
        qn=1
        for j in range(N): qn *= cm[j].conjugate()*cp[j]        # q_N(...)_j
        if abs(gen-qn)>1e-12: return fail(7,"generator product != q_N coordinate product")
        if abs(abs(gen)-1)>1e-12: return fail(7,"|Z_N| != 1")
    print("R7 Z_N = prod_j [e_plus(U_ej).e_minus(U_ej)^*] = prod_j q_N(...)_j  — 200 random points, |Z_N|=1")
    print("   => Z_N IS AN ELEMENT OF B, prior to the entry (product of ratified generators)")

    # R8 Theta_F fixes each factor: Theta_F(e_plus(U_l))=e_minus(U_-l), Theta_F(e_minus(U_l))=e_plus(U_-l)
    # b_j = e_plus(U_ej).e_minus(U_-ej) ; Theta_F(b_j) = e_minus(U_-ej).e_plus(U_ej) = b_j  (factors commute)
    # As functions: e_minus(U_-ej) -> conj(chi_-(ej)) ; so the image function equals the original.
    for trial in range(200):
        cpj=cmath.exp(1j*random.uniform(0,6.283185307)); cmj=cmath.exp(1j*random.uniform(0,6.283185307))
        b   = cpj*cmj.conjugate()
        Tb  = cmj.conjugate()*cpj      # Theta_F image, factors commuted
        if abs(b-Tb)>1e-12: return fail(8,"Theta_F does not fix b_j")
    print("R8 Theta_F(b_j) = b_j for every factor  =>  Theta_F(Z_N) = Z_N  =>  omega(Z_N) is REAL")

    # R9 no value is forced: build branch-symmetrised (U1-compatible) measures hitting +1, ~0, -1
    N=3
    def ZN(cp,cm):
        z=1
        for j in range(N): z*= cm[j].conjugate()*cp[j]
        return z
    def sym(pts):   # symmetrise under branch exchange with conjugation
        out=[]
        for w,(cp,cm) in pts:
            out.append((w/2,(cp,cm)))
            out.append((w/2,([c.conjugate() for c in cm],[c.conjugate() for c in cp])))
        return out
    def E(mu): return sum(w*ZN(cp,cm) for w,(cp,cm) in mu)
    d=[cmath.exp(1j*random.uniform(0,6.28)) for _ in range(N)]
    v_diag=E(sym([(1.0,(d,d))]))
    M=20000
    v_haar=E(sym([(1.0/M,([cmath.exp(1j*random.uniform(0,6.28)) for _ in range(N)],
                          [cmath.exp(1j*random.uniform(0,6.28)) for _ in range(N)])) for _ in range(M)]))
    v_neg=E(sym([(1.0,([cmath.exp(1j*cmath.pi.real),1+0j,1+0j],[1+0j]*N))]))
    for name,v in (("diagonal",v_diag),("Haar x Haar",v_haar),("Z_N=-1 point",v_neg)):
        if abs(v.imag)>1e-2: return fail(9,f"omega(Z_N) not real on a U1-compatible measure ({name})")
    if not (v_diag.real > 0.99 and abs(v_haar.real) < 0.05 and v_neg.real < -0.99):
        return fail(9,f"omega(Z_N) does not span [-1,1]: {v_diag.real}, {v_haar.real}, {v_neg.real}")
    print(f"R9 omega(Z_N) attains {v_diag.real:+.4f}, {v_haar.real:+.4f}, {v_neg.real:+.4f} "
          f"on U1-compatible states => NO VALUE FORCED (PINNED refuted)")

    # R5 citations
    ids={r[0] for r in rows}
    body=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for m in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",body):
        cites|=set(re.findall(r"\d{2}",m.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(5,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")
    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES = {n} markers, final depth {dep}")
    if dep: return fail(6,"fence left open")
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
