#!/usr/bin/env python3
"""Cycle 11: Gate-2 first-opening accounting + r=3 uniqueness (spec 39).

Written and executed strictly AFTER 39_..._SPEC_V001.md was sealed
(845f4c67...). require()-based; python -O safe; no measured constant.
"""
import itertools
import math
import sys
import numpy as np


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


def connected(v, edges):
    if not edges and v > 1:
        return False
    seen = {0}
    frontier = [0]
    adj = {i: [] for i in range(v)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    while frontier:
        x = frontier.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return len(seen) == v


def canon(v, edges, root):
    """Canonical form of (rooted graph) under vertex relabeling fixing root."""
    others = [x for x in range(v) if x != root]
    best = None
    for perm in itertools.permutations(others):
        mapping = {root: 0}
        for i, x in enumerate(perm):
            mapping[x] = i + 1
        es = tuple(sorted(tuple(sorted((mapping[a], mapping[b])))
                          for a, b in edges))
        if best is None or es < best:
            best = es
    return (v, best)


def main():
    # ---- P1: exhaustive minimality enumeration --------------------------
    minimizers = []
    best_key = None
    for v in range(2, 7):
        all_pairs = list(itertools.combinations(range(v), 2))
        for ne in range(1, 7):
            for edges in itertools.combinations(all_pairs, ne):
                if not connected(v, edges):
                    continue
                for root in range(v):
                    deg = sum(1 for a, b in edges if root in (a, b))
                    if deg < 3:
                        continue  # cannot host 3 independent root-incident
                    key = (ne, v)
                    if best_key is None or key < best_key:
                        best_key = key
                        minimizers = [(v, edges, root)]
                    elif key == best_key:
                        minimizers.append((v, edges, root))
    require(best_key == (3, 4), "P1: minimal hosting complex has |E|=3, |V|=4")
    classes = {canon(v, e, r) for v, e, r in minimizers}
    require(len(classes) == 1, "P1: unique minimal iso-class (found %d)"
            % len(classes))
    v0, es0 = next(iter(classes))
    require(es0 == ((0, 1), (0, 2), (0, 3)),
            "P1: the unique class is the rooted star K_{1,3}")
    print("P1 PASS: exhaustive enumeration (|V| <= 6, |E| <= 6, all roots):")
    print("         the unique minimal connected complex hosting three")
    print("         independent root-incident comparisons is K_{1,3} —")
    print("         r = 3 is a THEOREM given the adopted three-axis layer")

    # ---- P2: accounting on K_{1,3} --------------------------------------
    # incidence: C_1 (3 edges) -> C_0 (4 vertices): del(e_i) = leaf_i - root
    D = np.zeros((4, 3))
    for i in range(3):
        D[0, i] = -1.0
        D[i + 1, i] = 1.0
    require(D.shape == (4, 3), "P2: dims C0=4, C1=3 (total 7)")
    rank = np.linalg.matrix_rank(D)
    require(rank == 3, "P2: rank(del) = 3")
    require(3 - rank == 0, "P2: ker(del)|C1 = 0 (tree)")
    require(4 - rank == 1, "P2: H_0 = 1 (connected)")
    require(4 - 3 == 1, "P2: Euler characteristic 1")
    DtD = D.T @ D
    ev = sorted(np.linalg.eigvalsh(DtD))
    require(np.allclose(ev, [1.0, 1.0, 4.0], atol=1e-12),
            "P2: del^T del = I + J eigenvalues {1,1,4}")
    svals = sorted(np.sqrt(ev))
    require(np.allclose(svals, [1.0, 1.0, 2.0], atol=1e-12),
            "P2: full-star singular values {1,1,2}")
    B = np.zeros((7, 7))
    B[:4, 4:] = D
    B[4:, :4] = D.T
    bev = sorted(np.linalg.eigvalsh(B))
    require(np.allclose(bev, [-2, -1, -1, 0, 1, 1, 2], atol=1e-12),
            "P2: 7-dim B spectrum {+-2, +-1, +-1, 0}")
    # handle-conditioned operator: sealed char poly lambda(lambda^2 - 2)
    Bh = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
    hev = sorted(np.linalg.eigvalsh(Bh))
    require(np.allclose(hev, [-math.sqrt(2), 0.0, math.sqrt(2)], atol=1e-12),
            "P2: handle-conditioned spectrum {-sqrt2, 0, sqrt2}")
    print("P2 PASS: accounting exact — dims (4,3,7); rank 3; tree kernel 0;")
    print("         H0 = 1; Euler 1; svals {2,1,1}; B spectrum")
    print("         {+-2,+-1,+-1,0}; conditioned spectrum {-sqrt2,0,sqrt2} —")
    print("         every value matches its sealed counterpart")

    # ---- P3: flag relocation (statement) --------------------------------
    print("P3: with P1, the first-opening star is DERIVED given the adopted")
    print("    three-axis layer; the premise's target-awareness collapses")
    print("    onto the disclosed MPCP adoption. REAFFIRMED (not")
    print("    overturned): seven_dimensional_carrier_counts_as_new_evidence")
    print("    = false — the 7-count is a consequence of the adopted axis")
    print("    count and is evidence for nothing.")

    print("\nCYCLE-11 OUTCOME: P1, P2 CONFIRMED; P3 relocation recorded;")
    print("P4 conditionality (three-axis adoption, first=minimal reading,")
    print("root-incidence premise) carried. No value compared to anything.")
    print("alpha_computed=false")


if __name__ == "__main__":
    main()
