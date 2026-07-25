# Hostile Pre-Execution Review — ER Insensitivity Spec V001: NOT_READY
Claude lane · 2026-07-25 (late evening) · fresh-context lane return.
The sealed spec (277654ee…) is PRESERVED AS A FAILED DRAFT per discipline;
repair is by append-only successor V002. The review's three BLOCKING findings
are all confirmed correct by the construction lane.

## Blocking findings (all accepted)

1. |Z(0)| >= 1/4 fence REFUTED by the spec's own pinned sealed data: witnessed
   N=96 completed-amplitude moduli on the carrier are 5.918e-4 (ER-A mixed),
   6.467e-3 (ER-A pure), 6.265e-3 (ER-B mixed), 6.791e-2 (ER-B pure) — 3.7x
   to 422x below 1/4. Every execution would return GATE_BLOCKED before any
   verdict. Root cause: two incompatible amplitude conventions (raw sealed
   table rows vs BID-normalized Z_h = a_h(A)/a_h(0)) coexist in one spec.
2. theta_kappa doubly defective: the written "exact rational 2000/49"
   contradicts the written decimal 4.0816e-2 (= 2/49) by 1000x (construction
   lane's arithmetic error), AND the propagation misses a factor (needs the
   stencil coefficient sum AND the log amplification: 16e/h^2 on its own
   premise), AND is 15x-1690x under the honest per-state floor computed from
   witnessed moduli (0.60 ER-B pure … ~69-75 ER-A mixed).
3. D1 factually misdescribes the sealed comparison as an a=+7/100 execution;
   the sealed v002 comparison executor contains NO connection term (its rows
   are a=0). Literal D1 either spuriously drift-blocks or forces silent
   reinterpretation.

Conditions: theta_amp=5e-5 is the finite comparison lane's tolerance, NOT the
battery's resolution (battery demands 1e-8 certified enclosures) — a MOOT
verdict at 5e-5 would NOT show the battery cannot resolve the fork; four
integrator-assembly choices unpinned (Strang placement, eigenvalue-0 history
shortcut invalid at a != 0, B_D quadrature, Richardson formula); the
amplitude-arm disjunct forewrites RESOLVABLE from already-sealed data and must
be separated from the genuinely new kappa arm.

Positive findings: no-selection architecture watertight; verdict partition
exhaustive; battery-discipline conflicts none; prediction hygiene otherwise
clean; connection J fully defined at operator level by the Phase-A spec
restricted to this carrier (the underdefinedness is numerical assembly only);
n=2 ell=1 narrowing principled (only independently verified carrier).

## Structural consequence adopted for the successor

Because the battery is strictly finer than the finite comparison lane, this
carrier/precision can certify RESOLVABLE_BY_BATTERY (a fortiori) but can
NEVER certify battery-moot. The successor therefore has two live verdicts
only: RESOLVABLE_BY_BATTERY and NOT_RESOLVED_AT_FINITE_LANE_PRECISION
(explicitly not moot), plus BLOCKED. True MOOT would require battery-grade
exact enclosures — a separate decision for Brian only if the finite lane
fails to certify RESOLVABLE.

Calibration ledger note: this is the second sealed-claim defect authored by
this lane and caught by hostile review in one day (R2 fabrication-economics;
theta_kappa/fence). Both caught pre-execution — the layered-review topology
is functioning — but spec-authoring arithmetic now gets an explicit
pre-seal self-check pass (recompute every frozen constant two independent
ways before sealing).
