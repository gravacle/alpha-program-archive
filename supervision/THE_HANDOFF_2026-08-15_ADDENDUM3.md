# THE HANDOFF 2026-08-15 — ADDENDUM 3 (custody correction: the S9AD pair was alive)

Supersedes ADDENDUM 2 (4d0e432b) IN ONE PART: its declaration that run
wf_31447492 "died at cutover with ZERO bytes landed" and that "the S9AD RK_LT
paths remain permanently vacant" was true at its write (workspace probed empty,
git tree clean) and is now CORRECTED OF RECORD — the predecessor session's
workflow process was still alive after its last transcript write, and its pair
landed at the commission-distinct S9AD paths: build
STAGE8_RK_LT_BIT_S9AD_V001.md (ff523db5) sealed 01:50; audit
STAGE8_RK_LT_BIT_S9AD_AUDIT_V001.md (2de65d40) sealed 02:04.

CUSTODY, per the Q-1064 discipline (identify the commission from the
artifact's own ledger, never from path or timing): the S9AD pair's own ledger
carries the predecessor commission (THE BIT, run wf_31447492); it is OF this
program's custody at its own path — ADDENDUM 2's "not of this program's
custody" clause is withdrawn. The successor pair (commission T1SR: build
405bcd5e sealed 02:08, audit 873493d5) ran concurrently, FENCE-BARRED from the
S9AD content and left it unconsumed (the build's D-1 flag and the audit's O-1
disclosure display this); the S9AD build sealed before the T1SR build existed
to be read. Independence holds in both directions; the two pairs' verdicts
CONCORD (UNDECIDABLE-TODAY, each pair's audit governing its own build) — the
double-run is booked as independent cross-confirmation, the Q-1064 pattern.

Register head at this addendum: Q-1101 (ACT-3 executed); the bit row registers
next. Fences: alpha_computed=false · proof_authorized=false ·
kappa_record_computed=false.
