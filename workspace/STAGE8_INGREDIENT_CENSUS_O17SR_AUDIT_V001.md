# STAGE 8 — AUDIT OF THE INGREDIENT CENSUS (O17SR)

Commission: O17SR. Lane: CENSUS-AUDIT. Date: 2026-08-15.
Posture: DEFAULT-REFUTE. Testimony carries zero weight; every claim re-derived at bytes.
ALL_RESULTS = CLAIMED until checked.

## 0. STEP 0 — TARGET PROBE AND SEAL

```text
TARGET      STAGE8_INGREDIENT_CENSUS_O17SR_V001.md            PRESENT (49383 bytes)
SIDECAR     STAGE8_INGREDIENT_CENSUS_O17SR_V001.md.seal.sha256 PRESENT
SEAL CHECK  shasum -a 256 -c STAGE8_INGREDIENT_CENSUS_O17SR_V001.md.seal.sha256
            run FROM /Users/bgm/MB Work/alpha-program-archive/workspace
            => STAGE8_INGREDIENT_CENSUS_O17SR_V001.md: OK
OUTPUT PATH STAGE8_INGREDIENT_CENSUS_O17SR_AUDIT_V001.md — probed ABSENT before write.
```

```text
GATES  alpha_computed = false ; proof_authorized = false ;
       kappa_record_computed = false.
FENCES HELD: no value, no number, no measured-constant comparison; no git action;
       no register / tracker / road / plan / continuation file read; scoped reads
       and declared scoped sweeps only. DETERMINATION ONLY — this audit types and
       inventories; it proposes nothing and adopts nothing.
NOTE   This auditor is NOT under the blindness bar. The barred band was opened
       for the sole purpose of testing the build for leakage (§5).
```

## 0.1 DECLARED SWEEP AND CUTOFF (THIS AUDIT)

```text
ROOTS   R1  /Users/bgm/MB Work/alpha-program-archive/workspace      (primary)
        R2  /Users/bgm/Documents/New project/gravity_emergence_evidence_program/
            alpha_fundamental_record_action_cleanroom_v003          (secondary)
CUTOFF  2026-08-15, at audit time. R1 top level now: 3588 entries, 1758 *.md,
        1704 *.seal.sha256. The census recorded 3581 / 1754 / 1701. The drift is
        four *.md written after the census sealed; it is disclosed, not charged.

A-SWEEP  the census's own S-A regex, re-run verbatim and uncapped at R1.
B-SWEEP  wider output-side verb band, mine, not the census's:
         (assigns|yields|produces|constructs|returns|outputs|generates|emits|
          builds|creates|delivers)[^.]{0,60}(causal |record |common |primitive )?cells?
         and the same verb set against record / algebra / complex.
C-SWEEP  the barred band opened and searched for leakage signatures.
EXPECTED-UNLOCATABLE: "Q-..." items. Not sought.
```

---
