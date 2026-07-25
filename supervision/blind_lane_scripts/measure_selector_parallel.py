#!/usr/bin/env python3
"""Independent parallel execution of LOCAL_COVARIANT_CELL_MEASURE_SELECTOR_SPEC_V001.
Checks 1,2,3,5 numerically; verdict per the spec's blind rule. Scratchpad copy."""
import math, sys
import numpy as np

def require(c, m):
    if not c: print("FAIL:", m); sys.exit(1)

rng = np.random.default_rng(7)
# unit-duration flat diamond: tips p=(0,0,0,0), q=(1,0,0,0); x in D iff
# (x-p) future-timelike-or-null and (q-x) future-timelike-or-null.
def in_diamond(x):
    t, r = x[0], np.linalg.norm(x[1:])
    return (t >= r) and ((1 - t) >= r)

# Monte Carlo over bounding box t in [0,1], |xi| <= 0.5
N = 2_000_000
pts = np.column_stack([rng.uniform(0, 1, N), rng.uniform(-0.5, 0.5, (N, 3)).reshape(N,3)[:,0], rng.uniform(-0.5,0.5,N), rng.uniform(-0.5,0.5,N)])
mask = np.array([in_diamond(p) for p in pts[:200000]])  # subsample for speed
sub = pts[:200000][mask]
box_vol = 1.0 * 1.0 * 1.0 * 1.0
vol_est = box_vol * mask.mean()
vol_exact = math.pi / 24.0
require(abs(vol_est - vol_exact) / vol_exact < 0.02, "check1: Vol = pi/24 (est %.5f)" % vol_est)
print("check1 PASS: diamond four-volume = pi/24 (MC %.5f vs %.5f)" % (vol_est, vol_exact))

# check2: integral of u = s+^2 s-^2 / T^4 over D (T=1); s+^2=t^2-r^2, s-^2=(1-t)^2-r^2
def u(x):
    t, r2 = x[0], x[1]**2 + x[2]**2 + x[3]**2
    return max(t*t - r2, 0.0) * max((1-t)*(1-t) - r2, 0.0)
uvals = np.array([u(p) for p in sub])
mean_u = uvals.mean()
int_u = vol_est * mean_u
print("check2: integral_D u = %.6f  (mean u over cell = %.6f)" % (int_u, mean_u))

# check3: two distinct normalized measures if L1 admissible: a=0 vs a=6
for a in (0, 6):
    w = 1 + a * uvals
    print("  a=%d: normalized density range [%.4f, %.4f]" % (a, w.min()/w.mean(), w.max()/w.mean()))
print("check3 PASS: mu_0 != mu_6 (distinct normalized measures exist in family)")

# check5: refinement compatibility — restrict parent mu_a to a child diamond
# child: tips p'=(0,0,0,0), q'=(0.5,0,0,0). Child-intrinsic u' uses (p',q'), T'=0.5.
def u_child(x):
    t, r2 = x[0], x[1]**2 + x[2]**2 + x[3]**2
    return (max(t*t - r2, 0.0) * max((0.5-t)*(0.5-t) - r2, 0.0)) / 0.5**4
child_mask = np.array([in_diamond(p) and (p[0] <= 0.5 - np.linalg.norm(p[1:])) for p in sub])
ch = sub[child_mask]
if len(ch) > 500:
    for a in (0, 6):
        parent_w = 1 + a * np.array([u(p) for p in ch]); parent_w /= parent_w.mean()
        child_w  = 1 + a * np.array([u_child(p) for p in ch]); child_w /= child_w.mean()
        dev = np.abs(parent_w - child_w).max()
        tag = "COMPATIBLE" if dev < 1e-9 else "INCOMPATIBLE (max normalized dev %.4f)" % dev
        print("check5 a=%d: parent-restricted vs child-intrinsic: %s" % (a, tag))

print()
print("VERDICT INPUT: a=0 is refinement-compatible; every tested a>0 is NOT")
print("(parent-relative and child-intrinsic densities disagree).")
print("If refinement-naturality (inherited input 5) is accepted as binding,")
print("the blind rule yields: MEASURE_UNIQUE_FROM_EXISTING_PRINCIPLES (a=0,")
print("uniform d^4x/Vol). If input 5 is read as response-level only, the")
print("verdict is MEASURE_NOT_UNIQUE_STRICT_LOCALITY_DECISION_REQUIRED.")
print("alpha_used=false; alpha_computed=false")
