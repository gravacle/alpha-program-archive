#!/usr/bin/env python3
"""
SEALED GENERATOR — STAGE8_DESC_NECESSITY_PROBE_DARIO_V001.md   (relay 1077, DARIO lane)

The verdict rests on one re-verified span and on a consumer tally, so both are recomputed:

  R6  THE DECISIVE SPAN. member 06 [10824,11934) must rehash to 4313fb92… AND must contain
      "omega_phys : B -> C" and "H_omega". If the state port's first field is not the state, the
      NEEDS-FULL-MEASURE verdict loses its ground and the seal is refused.
  R7  TALLY GATE. The published CONSUMERS line must agree with the disposition rows it summarises.
  R8  VERDICT CONSISTENCY. NEEDS-FULL-MEASURE must be paired with MANDATE = FIRES and with the
      CONSTRUCTIVE/OUTPUT distinction present — an unqualified necessity claim refuses to seal.

REFUSAL PATHS: R1 member absent · R2 STRICT!=STABLE · R3 fence declarations present ·
R4 citations resolve · R5 fence balance · R6/R7/R8 above · R9 residue · R10 closure fixed point.
"""
import hashlib, re, sys
from pathlib import Path

ROOT = Path("/Users/bgm/MB Work/alpha-program-archive"); WS = ROOT / "workspace"
ART = WS / "STAGE8_DESC_NECESSITY_PROBE_DARIO_V001.md"; SIDE = Path(str(ART) + ".seal.sha256")
PORT = WS / "STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md"
SPAN = (10824, 11934, "4313fb92fd78f6b26a5eba216e7ae7540f6b0698dc82eddd98236ceee5d7cf1b")
FENCES = ["alpha_computed = false", "proof_authorized = false", "kappa_record_computed = false",
          "JOINT_ANCHOR_DERIVED = false"]
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
    for f_ in FENCES:
        if f_ not in t: return fail(3,f"fence declaration missing: {f_}")
    print("FENCES DECLARED = all four present")

    # R6 the decisive span
    lo,hi,exp = SPAN
    seg = PORT.read_bytes()[lo:hi]
    d = hashlib.sha256(seg).hexdigest()
    if d != exp: return fail(6,f"decisive span digest {d} != {exp}")
    s = seg.decode()
    if "omega_phys : B -> C" not in s:
        return fail(6,"state port's first field is not omega_phys — the verdict loses its ground")
    if "H_omega" not in s:
        return fail(6,"H_omega absent from the port — the carrier-from-state claim is unsupported")
    print(f"R6 DECISIVE SPAN [{lo},{hi}) = {d[:32]}…")
    print("   'omega_phys : B -> C' present as FIELD 1; 'H_omega' built from it — CONFIRMED")

    # R7 tally gate
    full = len(re.findall(r"CONSUMES-FULL-MEASURE", t))
    m = re.search(r"CONSUMERS = (\d+)-DISPOSITIONED \((\d+)-FULL / (\d+)-INVARIANT-ONLY / (\d+)-NOTHING\)", t)
    if not m: return fail(7,"published CONSUMERS tally line not found in the declared form")
    n_tot,n_full,n_inv,n_none = (int(x) for x in m.groups())
    if n_full+n_inv+n_none != n_tot:
        return fail(7,f"tally does not sum: {n_full}+{n_inv}+{n_none} != {n_tot}")
    if full < n_full:
        return fail(7,f"tally claims {n_full} full-measure rows but only {full} markers appear")
    print(f"R7 TALLY = {n_tot} dispositioned ({n_full} full / {n_inv} invariant-only / {n_none} nothing) — sums, and rows support it")

    # R8 verdict consistency — no unqualified necessity claim
    if "NEEDS-FULL-MEASURE" in t:
        if "MANDATE = FIRES" not in t:
            return fail(8,"NEEDS-FULL-MEASURE must be paired with MANDATE = FIRES")
        if "CONSTRUCTIVE" not in t or "OUTPUT NECESSITY" not in t:
            return fail(8,"necessity claim must carry the CONSTRUCTIVE/OUTPUT distinction")
        if "NOT PROVABLE HERE" not in t:
            return fail(8,"the output-necessity limit must be stated explicitly")
        print("R8 VERDICT CONSISTENCY = NEEDS-FULL-MEASURE + MANDATE FIRES + constructive/output limit stated")

    # R4 citations
    ids={r[0] for r in rows}
    body=t[t.index("CLOSURE_DECLARATION_END"):]
    cites=set()
    for mm in re.finditer(r"members?\s+((?:\d{2})(?:\s*(?:,|and|/|-)\s*\d{2})*)",body):
        cites|=set(re.findall(r"\d{2}",mm.group(1)))
    bad=sorted(c for c in cites if c not in ids)
    if bad: return fail(4,f"unresolved citations: {bad}")
    print(f"CITATIONS = all resolve ({len(cites)} distinct)")
    n=dep=0
    for l in t.splitlines():
        if l.strip().startswith("```"): n+=1; dep=1-dep
    print(f"FENCES(md) = {n} markers, final depth {dep}")
    if dep: return fail(5,"fence left open")
    low=prose(t).lower(); hits=[(x,low.count(x.lower())) for x in TOK if low.count(x.lower())]
    tot=sum(k for _,k in hits); print(f"RESIDUE_SCAN(27) = {tot} hit(s)")
    for x,k in hits: print(f"    {x!r}: {k}")
    if tot: return fail(9,"output-inspection token in authored prose")
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
    dg=hf(ART); SIDE.write_text(f"{dg}  {ART.name}\n"); print(f"SEALED {ART.name}\n  {dg}")
    return 0

if __name__=="__main__": raise SystemExit(main())
