#!/usr/bin/env python3
"""Tie-breaker core: is the per-cell response assembly cellulation-dependent
for mu_a, a != 0? Observable means on a child diamond: parent-restricted
vs child-intrinsic. Scratchpad; alpha_used=false."""
import numpy as np
rng = np.random.default_rng(11)
N = 400000
pts = np.column_stack([rng.uniform(0,1,N), rng.uniform(-0.5,0.5,N), rng.uniform(-0.5,0.5,N), rng.uniform(-0.5,0.5,N)])
r = np.linalg.norm(pts[:,1:], axis=1)
t = pts[:,0]
in_parent = (t >= r) & ((1-t) >= r)
in_child  = (t >= r) & ((0.5-t) >= r)          # D[p, m], m=(0.5,0)
P = pts[in_parent & in_child]
tc, rc2 = P[:,0], P[:,1]**2+P[:,2]**2+P[:,3]**2
u_par = np.maximum(tc**2-rc2,0)*np.maximum((1-tc)**2-rc2,0)          # T=1
u_chi = np.maximum(tc**2-rc2,0)*np.maximum((0.5-tc)**2-rc2,0)/0.5**4 # T=0.5
for f_name, f in (("t", tc), ("u_child", u_chi)):
    for a in (0, 2, 6):
        w_par = 1 + a*u_par
        w_chi = 1 + a*u_chi
        m_par = (f*w_par).sum()/w_par.sum()
        m_chi = (f*w_chi).sum()/w_chi.sum()
        dev = abs(m_par-m_chi)/max(abs(m_chi),1e-12)
        print("f=%-8s a=%d: parent-restricted <f>=%.6f  child-intrinsic <f>=%.6f  rel dev=%.4f" % (f_name, a, m_par, m_chi, dev))
print()
print("a=0: assemblies agree exactly (uniform is self-similar).")
print("a>0: per-cell response contributions DIFFER between cellulations —")
print("if the sealed response rule assembles per-cell intrinsic measures,")
print("the inherited cellulation-independence requirement kills a>0.")
