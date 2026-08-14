# R-L4a-N CLAUSE — V002 (PREPARED) — the audit-required repair applied — 2026-08-14

**STATUS: PROPOSED-NOT-ADOPTED. Adoption is the principal's alone (clause N.8; no
lane adoption exists).** Prepared by the registrar as the mechanical execution of the
one adoption-blocking repair the audit named. Fences live: alpha_computed = false ·
proof_authorized = false · kappa_record_computed = false. No value is asserted
anywhere in this file; kappa_n is asserted nowhere (N.4 governs).

## PROVENANCE
- Clause V001 = STAGE8_R1_NAMING_CANDIDATE_V001.md §3 (workspace/), digest
  e1da7446242de98a4997b778eaad5e791e192084852d4a8e4024e4b87c690ed6, verified at path.
  Staged by register row Q-1059 as PROPOSED-NOT-ADOPTED with one audit-required repair.
- Audit = STAGE8_R1_NAMING_CANDIDATE_AUDIT_V001.md (workspace/), digest
  48015ac23d8023ae8a031dc04f2423654bb30edfbe12741cc8815befa4736772, verified at path.
  Verdict CONFIRMED-WITH-CORRECTIONS; its correction c-3 (flag f-2) is the repair
  applied here, in the audit's own repair text.

## THE DELTA (sole change from V001; every other clause byte identical to e1da7446 :543-706)
N.5's fire list gains one condition:
    (F-d) exhibits, at some point of the closed pair polydisc, failure of the
          full-family vanishing det(1 + A_n(a)) -> 0 at this naming.
(and F-c's terminal period becomes "; or"). This closes the audit's named r-3-axis
gap: a sealed refutation of the polydisc-identical vanishing at this naming with the
baseline intact (det_n(0) -> 0 but det(1 + A_n(a*)) not-> 0 at some a* on the closed
pair polydisc) would otherwise leave R-L4b FALSE at the naming with the void/reopen
clause never firing. Consumer safety was intact either way (audit f-2); the repair
makes the clause's honesty promise self-executing on that hazard. "iff" is RETAINED:
with F-d the fire list covers both the hazard of record (audit f-1, Branch-2) and the
structurally named r-3-axis hazard (audit f-2). Audit v-5: a V-N5-style fire-list
guard is subsumed by this repair. Falsifiers V-N1..V-N5 are unchanged and in force
from adoption.

## NOTED, NOT APPLIED (the principal's option at adoption; audit f-3, a non-correction
with no operative effect): in N.5(iv), for an F-c fire at non-nested spectra the exact
completion label is "NOT-VANISHING-AS-A-LIMIT (no limit exists)" rather than
"NON-VANISHING at this regularization"; a one-word tightening if the principal wants it.

---

```text
=====================================================================
CANDIDATE CLAUSE R-L4a-N — THE REGULARIZATION NAMING
STATUS: PROPOSED-NOT-ADOPTED
=====================================================================

N.1  THE NAMING. For R-L4a and R-L4b (E1 :766-790), the regularization
     is NAMED as THE CARRIER COMPRESSION OF RECORD: the n-indexed
     family {C_n} of compressions onto the sealed carrier subspaces —
     the same family in which the record's own fixed-n objects live,
     A_{mu lambda, n}(a) = C_n(V_{mu lambda}(a) - 1)C_n (ZF §4.1(b);
     the PA carrier construction, 789338ad; the n-indexed family of
     record at ZF §4.1(c) and 52f2490b). Regularized baseline objects:
     A_n(0) = -2 C_n P C_n on ran C_n (opposite-phase pairs; the exact
     collapse algebra of E1 :746-748 untouched);
     det_n(0) := det_{ran C_n}(1 - 2 C_n P C_n) = prod_i (1 - 2 s_i),
     s_i the eigenvalues of C_n P C_n on ran C_n (of record, R-L1
     block-triangular identity). The R-L4a determination and the
     R-L4b vanishing are statements about the family {det(1 + A_n(a))}
     as n -> infinity, at the FULL-family quantifier (no subsequence).
     NO new carrier, cellulation, truncation, or numeric datum is
     introduced: the family is the one of record.

N.2  DOMAIN. Per admitted state (M-3), per admitted cell of D3, per
     OPPOSITE-PHASE record-colour pair, on the closed pair polydisc
     (M-2); baseline point a = 0 as displayed at E1 :746-762. The
     surviving sector is untouched (V(0) = I exactly there); this
     naming administers ONLY the opposite-phase sector's Carleman
     route. ADMISSIBILITY CONFORMITY, exhibited: AR-1 — each member is
     finite rank, hence 2 C_n P C_n is trace class per member and both
     Carleman factors are defined (det_n exists at every fixed n; CAS
     N4); AR-2 — the compression acts on the carrier axis only; M(t)
     and 1_{D_t} are consumed SHARP (D6' honored by construction);
     AR-3 — no number is frozen; AR-4 — the index n lives in the NAMED
     FAMILY, never in a certified constant; consumption is at the
     family/limit quantifier only; AR-5 — the full-family limit binds.

N.3  INTERACTION WITH THE SEALED kappa_n DICHOTOMY (consumption
     interface; NO hypothesis below is asserted). With kappa_n :=
     ||[C_n, P]||_2^2 = 2 sum_i s_i(1 - s_i) (of record):
     (B1) a SEALED input "kappa_n -> infinity" discharges the
          regularized vanishing at the baseline point: det_n(0) -> 0
          (|det_n(0)|^2 <= exp(-2 kappa_n), of record) — the honest
          "det = 0 regularized" recovery of E1 :779-781.
     (B2) a SEALED input "sup_n kappa_n = 2M < infinity AND uniform
          1/2-avoidance (exists delta > 0: |s_i - 1/2| >= delta for
          all i, n)" REFUTES R-L4b at this naming:
          |det_n(0)| >= (4 delta^2)^{M/(2U)} > 0, U := 1/4 - delta^2
          (of record). The FALSE branch, N.5, then fires.
     (B3) bounded kappa_n WITHOUT uniform 1/2-avoidance: UNDECIDED of
          record (the check's n-1: the two branches are sufficient
          conditions, NOT a partition); no consumption is licensed.
     R-L4b is DISCHARGED at this naming only by a (B1)-type sealed
     input PLUS the joint-rate input on the polydisc (r-3 of record):
     ||R_n Delta_n(a)||_1 = o(-log|det_n(0)|) uniformly on the closed
     pair polydisc, in the exact factorization frame
     det(1 + A_n(a)) = det(1 + A_n(0)) det(1 + R_n Delta_n(a)) where
     1 + A_n(0) is invertible (CAS C3). NEITHER input is supplied,
     presumed, or valued here.

N.4  WHAT THE NAMING DOES NOT DO. It asserts NOTHING about kappa_n —
     not (B1), not (B2), not (B3): r-2 is unsealed on both branches
     and stays a named estimate obligation on no discharged artifact.
     It freezes no value (no value of D or of any limit; no delta, no
     M). It flips no flag, retires no witness (the registrar's), moves
     no gate. It does not touch the stricken display (E1 :773-778),
     which remains consumable only as its own clause permits. It does
     not decide, weaken, or touch R-L2b, H-R, C-L2/G_cm, summed-S2',
     R-L0, or R-L0b. It introduces no datum beyond the record.

N.5  THE FALSE BRANCH (void/reopen clause; the compression-
     regularization hazard, LIVE of record). This clause FIRES iff a
     sealed artifact, checked, does any of:
       (F-a) certifies the (B2) hypotheses at this naming; or
       (F-b) exhibits liminf_n |det_n(0)| > 0; or
       (F-c) exhibits non-convergence of det_n(0) (e.g. sign
             alternation at non-vanishing modulus — a live shape: the
             sign is (-1)^{#{s_i > 1/2}} of record); or
       (F-d) exhibits, at some point of the closed pair polydisc,
             failure of the full-family vanishing det(1 + A_n(a)) -> 0
             at this naming.
     THEN, all of the following, and nothing else:
     (i)   R-L4b is FALSE AT THIS REGULARIZATION (of record, CERT
           §2.3(d)/§2.4). The exclusion may NOT be consumed.
     (ii)  Every consumer of the exclusion REOPENS to the full 9-pair
           architecture: the 5/4 census, N_surv(0) = 1/2, the weights
           c = (1/2, 1/8 x 4), kappa_bal = 1, the R-L0 threshold
           display's kappa_bal factor, and R-L0b's convexity footing
           (the sealed failure mode, CERT §2.2 / check C6, governs).
     (iii) NO value is thereby assigned to the opposite sector: the
           reopen is to OBLIGATIONS, never to values (E1 :773-778;
           F'-3). The stricken display stays stricken.
     (iv)  This candidate's R-L4b-service interface (the N.3
           consumption of the exclusion) is VOID. The naming itself
           survives only as the R-L4a determination interface, whose
           determination then completes with the honest answer
           NON-VANISHING at this regularization (R-L4a answered;
           R-L4b failed at it). Whether to name a DIFFERENT
           regularization is a new adoption act and returns to the
           principal (V-N4 territory; no lane may make that call).

N.6  FALSIFIERS (adopted V-1 style; refutation of a load-bearing claim
     at its own quantifier VOIDS the candidate):
     V-N1 ADMISSIBILITY: a sealed derivation that some member fails —
          2 C_n P C_n not trace class on ran C_n, or det_n(0)
          undefined at some n — VOIDS the candidate.
     V-N2 UNIQUENESS-OF-RECORD: a sealed regularized family on the
          discharged basis, distinct from the carrier compression and
          antedating this candidate, VOIDS the narrowing premise; the
          naming returns to the principal at the wider class.
     V-N3 THE INTERFACE: refutation, at its own quantifier, of
          det_n(0) = prod(1 - 2 s_i), of the (B1) sufficiency, or of
          the (B2) lower bound, VOIDS the candidate.
     V-N4 DERIVE-BEFORE-AUTHOR SUPERSESSION: a sealed derivation that
          FORCES the regularization choice, or makes R-L4b's
          consumers regularization-independent, VOIDS the candidate
          as MOOT (the lemma supersedes the act; §2 of this artifact
          exhibits why no such derivation exists on the current
          sealed basis).
     V-N5 FALSE-BRANCH INTEGRITY: a sealed derivation that N.5(ii)'s
          reopen list omits a consumer of the exclusion VOIDS the
          candidate until repaired.

N.7  CHOICE LEDGER (Actual-Surface Guard V001; every unforced choice
     in this candidate's chain, classified):
     CH-1 THE NAMING SELECTION ITSELF (carrier compression of record
          vs any admissible new-datum family): PREMISE(named). Every
          claim of this candidate visibly conditions on it ("AT THIS
          REGULARIZATION" throughout). What would prove it
          IMMATERIAL: a sealed derivation that every admissible
          regularization yields the same R-L4b truth value (i.e. the
          unsealed r-2/r-3 content universally quantified over the
          admissible class). What would prove it FORCED: a sealed
          clause closing the admissible class to families of record
          (uniqueness-of-record, §2.2, would then force C_n).
          Neither exists sealed (§2).
     CH-2 FULL-FAMILY QUANTIFIER (no subsequence): FORCED by the
          consumer — the exclusion assigns the census ONE value; a
          subsequential naming leaves it two-valued (the NV model's
          (-1)^n exhibit, CAS N5e). Ground exhibited, §2.1 AR-5.
     CH-3 THE a = 0 + JOINT-RATE DECOMPOSITION of R-L4b: FORCED of
          record (the factorization identity, CAS C3; CERT §2.4).
     CH-4 OBLIGATIONS-REOPEN (not value-assignment) on the FALSE
          branch: FORCED by the sealed strictures (E1 :773-778 no
          value of D; F'-3 no defaults).
     CH-5 ONE REGULARIZATION SERVING BOTH CLAUSES: FORCED at E1 :784
          ("with the regularization of R-L4a").
     MACHINERY/RELEVANCE (guard append): the compression family is
     apparatus consumed from the sealed constructions with a booked
     surface trace (the PA carrier the response functions live on;
     ZF §4.1(b)(c)) — SURFACE-DERIVED, not surface-native; its
     apparatus origin is exactly why CH-1 is a PREMISE and N.5 is
     live, and it may never silently anchor a surface verdict beyond
     the named conditional. TOY_SEPARATION: self-assessment CLAIMED
     clean at the stated quantifiers (every instance-grade exhibit in
     the supporting artifact is marked witness-family grade; no
     instance is quoted wider than its derivation); the RULING is the
     audit's, not this artifact's.

N.8  STATUS AND ADOPTION. PROPOSED-NOT-ADOPTED. Adoption is the
     principal's alone; no lane adoption exists. On adoption: the
     naming becomes the regularization of R-L4a at :768's own demand;
     witnesses E1_BASELINE_DETERMINANT_EXISTENCE_UNCERTIFIED,
     E1_OPPOSITE_PHASE_SECTOR_VANISHING_UNCERTIFIED, and
     E1_BASELINE_COLLAPSE_UNCERTIFIED all STAND until the r-2 and r-3
     inputs are sealed and checked; the falsifiers V-N1..V-N5 are in
     force from adoption.
=====================================================================
```

---

Prepared and sealed by the registrar, 2026-08-14. The clause above is byte-identical
to V001 (e1da7446 :543-706) except the F-d insertion displayed in THE DELTA.
