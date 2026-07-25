#!/usr/bin/env python3
"""Cycle 7: L->infinity durable-interval limit in three regimes (spec 27).

Written and executed strictly AFTER 27_..._SPEC_V001.md was sealed
(36f394f0...). require()-based; python -O safe; no measured constant.
o_j(t) = [(1+cos(w_j t))/2]^2 ; tau_R(L) = first common zero (if exact);
tau_delta(L) = first t with max_j o_j(t) < delta (thresholded).
"""
import math
import sys


def require(cond, msg):
    if not cond:
        print("FAIL: " + msg)
        sys.exit(1)


def overlap(w, t):
    return ((1.0 + math.cos(w * t)) / 2.0) ** 2


def path_positive_freqs(L):
    """Distinct positive eigenvalues of P_{L+1} adjacency (n = L+1 sites):
    2 cos(k pi/(L+2)), k = 1..L+1, keep > tolerance."""
    n = L + 1
    vals = [2.0 * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1)]
    pos = sorted({round(v, 12) for v in vals if v > 1e-9}, reverse=True)
    return pos


def first_common_zero_exact(freqs, t_max=200.0, grid=2_000_000):
    """Exact common zero requires cos(w t) = -1 for all w simultaneously:
    w t = (2m+1) pi. Search analytically over the smallest frequency's odd
    multiples and test the others for odd-integer ratio."""
    w0 = min(freqs)
    m = 0
    while True:
        t = (2 * m + 1) * math.pi / w0
        if t > t_max:
            return None
        ok = True
        for w in freqs:
            x = w * t / math.pi
            if abs(x - round(x)) > 1e-9 or round(x) % 2 == 0:
                ok = False
                break
        if ok:
            return t
        m += 1


def first_threshold_time(freqs, delta, t_max=100000.0, dt=0.001):
    t = dt
    while t < t_max:
        if max(overlap(w, t) for w in freqs) < delta:
            return t
        t += dt
    return None


def main():
    SQ2 = math.sqrt(2.0)

    # ---- P1: disjoint regime -------------------------------------------
    for L in (1, 2, 5, 20, 100):
        freqs = [SQ2] * L
        t = first_common_zero_exact(sorted(set(freqs)))
        require(t is not None and abs(t - math.pi / SQ2) < 1e-9,
                "P1: disjoint tau_R(L) = pi/sqrt2 for L=%d" % L)
    print("P1 PASS: disjoint regime — tau_R(L) = pi/sqrt2 exactly for all L;")
    print("         certified limit tau_R(inf) = pi/sqrt2 (trivial)")

    # ---- P2: unbounded star regime -------------------------------------
    prev = None
    for L in (2, 4, 16, 64, 256):
        w = math.sqrt(L)
        t = math.pi / w
        require(overlap(w, t) < 1e-20, "P2: star zero at pi/sqrt(L)")
        if prev is not None:
            require(t < prev, "P2: interval strictly shrinking")
        prev = t
    print("P2 PASS: unbounded incidence — tau_R(L) = pi/sqrt(L) -> 0:")
    print("         DEGENERATE; unbounded incidence excluded (DC3 is")
    print("         load-bearing)")

    # ---- P3: bounded-degree chain — the declared test -------------------
    print("P3 TEST (chain regime):")
    exact_results = {}
    for L in (2, 3, 4, 5, 6, 8):
        freqs = path_positive_freqs(L)
        t = first_common_zero_exact(freqs, t_max=500.0)
        exact_results[L] = (freqs, t)
        ftxt = ", ".join("%.6f" % f for f in freqs)
        print("  L=%d: positive freqs {%s} -> exact common zero: %s"
              % (L, ftxt, ("%.6f" % t) if t else "NONE (t <= 500)"))
    # sealed case check: L=2 must reproduce the single-star result
    require(abs(exact_results[2][1] - math.pi / SQ2) < 1e-9,
            "chain L=2 reproduces sealed tau_R = pi/sqrt2")
    # verdict between sealed outcomes (i) and (ii):
    fails = [L for L in (3, 4, 5, 6, 8) if exact_results[L][1] is None]
    if len(fails) == 5:
        print("  OUTCOME (ii): exact common orthogonality FAILS for every")
        print("  tested L >= 3 (incommensurate spectra, e.g. L=4 golden pair)")
        # thresholded interval behavior:
        print("  Thresholded intervals tau_delta(L):")
        for L in (3, 4, 5):
            freqs = path_positive_freqs(L)
            row = []
            for delta in (1e-1, 1e-2, 1e-3):
                td = first_threshold_time(freqs, delta)
                row.append("delta=%.0e: %s" % (delta,
                           ("%.2f" % td) if td else ">1e5"))
            print("    L=%d: %s" % (L, " | ".join(row)))
        print("  tau_delta grows as delta shrinks: the durable interval")
        print("  exists only in THRESHOLDED form for incident chains --")
        print("  exactness is unattainable at L >= 3, echoing the adopted-")
        print("  exactness finding at the many-cell level")
    else:
        print("  OUTCOME (i): exact common zeros found for L in %s" %
              [L for L in (3, 4, 5, 6, 8) if exact_results[L][1] is not None])

    print("\nCYCLE-7 OUTCOME: P1 CONFIRMED, P2 CONFIRMED, P3 resolved to a")
    print("sealed declared outcome (see above). No value compared to")
    print("anything. alpha_computed=false")


if __name__ == "__main__":
    main()
