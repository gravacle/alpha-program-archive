#!/usr/bin/env python3
"""
build_arrow_necessity_pins_v001.py  --  pin generator for STAGE8_DESC_ARROW_NECESSITY_DARIO_V001.md

LANE: DARIO.  RELAY 1037.  [PLAN:DESC-27].

DECLARED INPUTS (Q-920/Q-924): exactly the members in MEMBERS below, each named by its FULL path
from the alpha-program-archive root and rehashed at that path at run time.  Nothing else is read.

CITATION RULE IN FORCE -- CLOSURE_MEMBER_CITATION_RULE_V001, specified by
workspace/STAGE8_DESC_B03_V003_CHECK_CODEX2_V001.md section 6 and ordered by relay 1037:
every published span carries CANONICAL PATH + FULL SOURCE SHA-256 + HALF-OPEN [a,b) + FULL SPAN
SHA-256.  Member numbers below are a closure-local convenience ONLY; this generator emits the
path/digest/span/span-digest tuple for every row so no consumer needs to rebind a number.

REFUSAL DISCIPLINE (Q-920/Q-924): emits NO table if any of the following holds.
  R1  a declared member is unreadable at its declared path;
  R2  a FIXED span's recomputed digest does not equal the upstream pin it re-verifies;
  R3  an ANCHOR span's start anchor is absent, or occurs more than once (AMBIGUOUS);
  R4  an ANCHOR span's end anchor is absent at or after the start anchor.

SPAN CONVENTIONS, DECLARED: byte offsets into raw file bytes, half-open [a,b), no decoding and no
newline normalisation.  FIXED = a literal [a,b) carried from an upstream pin, recomputed and
compared; a mismatch is a REFUSAL.  ANCHOR = an interval fixed by a UNIQUE start anchor running
through the last byte of a named end anchor.

SELF-CITATION BAR: no span is taken from any DARIO-lane artifact of relays 1034 or 1037.  The
hypothetical arrows displayed in STAGE8_DESC_B03_DARIO_V003.md are this lane's own text and are NOT
record witnesses; the opposite-lane check ruled the same at its section 3.  They are excluded here
by construction -- V003 is a member for supersession/carriage purposes only and no span is drawn
from it.

NO OUTPUT INSPECTION: digests over sealed record bytes only; no downstream object consulted.
BLIND HELD: no physical quantity read, formed, evaluated, or compared.  Every scale symbolic.
"""

import hashlib
import os
import sys

ARCHIVE_ROOT = "/Users/bgm/MB Work/alpha-program-archive"

MEMBERS = {
    "01": ("relay_inbox/RELAY_PASTE_1037_ARROW_NECESSITY_DARIO_V001.md", "the assignment"),
    "02": ("relay_inbox/RELAY_PASTE_1033_FRESH_SESSION_BOOTSTRAP_DARIO_V004.md", "the bootstrap; the SYMBOLIC LINE"),
    "03": ("workspace/STAGE8_DESC_B03_DARIO_V003.md", "the 1034 derivation (carriage only; NO span drawn from it)"),
    "04": ("workspace/STAGE8_DESC_B03_V003_CHECK_CODEX2_V001.md", "the check: STOPS CONFIRMED; the citation rule"),
    "05": ("workspace/STAGE8_AXN_ENTRY_DECISION_INSTRUMENT_CODEX2_V002.md", "THE INSTRUMENT carrying the identification clause"),
    "06": ("workspace/STAGE8_AXN_ENTRY_CANDIDATE_SURVEY_DARIO_V001.md", "the instrument's cited ground (its member 05)"),
    "07": ("workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md", "THE LAW SIDE: P0-P7, and its single C0 mention"),
    "08": ("workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md", "v004's rho_pre clause"),
    "09": ("workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md", "L5: the d_U2 descent witness signature"),
    "10": ("workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md", "L4: the U2 role content"),
    "11": ("workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md", "A_C0's typing, B, res_B, and the K4 handoff"),
    "12": ("workspace/STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md", "the port signatures and their execution order"),
    "13": ("workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md", "WHERE B iso C(Y) IS FORCED -- the K4 receiver, record-side"),
    "14": ("supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md", "DoR-008"),
    "15": ("supervision/DECLINE_REGISTER_V002.md", "S01-S37"),
    "16": ("supervision/LOCKED_PROCESS.md", "process law"),
    "17": ("supervision/PROGRAM_STATE_BRIEF_V005.md", "state pin"),
    "18": ("workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md", "the overlay of record; the read rule"),
    "19": ("supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md", "the ratification, by digest"),
    "20": ("workspace/build_arrow_necessity_pins_v001.py", "this generator; declared inputs are exactly members 01-20"),
}

SPANS = [
    # ---------------- Q1: the provenance trace
    ("Q1-A", "05", "FIXED", (10322, 10545),
     "602ab0bff8d0d3d442271fe0850a6141f15fc1f139acb5b0311f13f63eaa26ff",
     "THE CLAUSE: joint i_src EMPTY -- author the carrier identification and typed embedding"),
    ("Q1-B", "05", "ANCHOR",
     (b"Status: **DRAFT FOR PRINCIPAL ENTRY", b"nine principal fields total."), None,
     "WHAT THE INSTRUMENT IS: a draft for principal ENTRY, nine fields; no entry made"),
    ("Q1-C", "05", "ANCHOR",
     (b"| 13 | `STAGE8_OBJ0_EXACT", b"third wrong-codomain `i_src` declaration |"), None,
     "THE DECIDING SENTENCE: the instrument types the LAW SIDE's own producer spec as a WRONG-CODOMAIN declaration"),
    ("Q1-D", "06", "FIXED", (7028, 7663),
     "43f3129a8b5059caa7979ab9ab0274296ec49c0cbd995c1785ab66d087af764d",
     "the instrument's cited ground: all three i_src declarations land in A_SRF_CTP"),
    ("Q1-E", "06", "ANCHOR",
     (b"three sealed declarations exist but ALL have codomain", b"NOT deriving this one"), None,
     "the survey's own framing: A_SRF_CTP is the deviation, A_C0 the target -- schema-side, not law-side"),
    ("Q1-F", "07", "ANCHOR",
     (b"4. a principal ruling that the rank-1 object", b"producer verdict."), None,
     "THE LAW SIDE'S ONLY C0 MENTION -- and it is a REFUTATION CONDITION, not a target"),
    ("Q1-G", "07", "FIXED", (8085, 8283),
     "375dd96a7b7c3806c063075f7346685efa8fbd8c1eddab9bbb19c5e723157d6d",
     "P1 -- the demand names A_SRF_CTP and no other carrier"),
    ("Q1-H", "07", "FIXED", (8954, 9569),
     "8917c67f455bb0b152950c1931891311c3c96029c1ba4100219370038198dbb0",
     "P5 -- rho_pre on the completed object; no C0"),

    # ---------------- Q2: the SRF-native route
    ("Q2-A", "08", "FIXED", (7290, 7829),
     "f9fb7a84ce4e3b954e5444baedc6703d9cc8ec52fe04f41e1b3b6d915b3d5372",
     "L1/L2/L3's receiver: the FULL source-record-field Hilbert space -- SRF-native"),
    ("Q2-B", "09", "FIXED", (6266, 6883),
     "e6093b0f48c11d3f05d3c6fd3692b6ea2c4b320746bb92eebe72ef28ed697efe",
     "L5 -- THE ONE LEG WHOSE RECEIVER NAMES C0: d_U2 : (B0_candidate,C0) -> U2"),
    ("Q2-C", "12", "ANCHOR",
     (b"The first draft placed P2 before P5", b"not a physical derivation:"), None,
     "THE DIRECTION: P2/i_src executes AFTER P5 and CONSUMES rho_pre -- it tests a state, never builds one"),
    ("Q2-D", "12", "FIXED", (38867, 39276),
     "56a575d104416d75ef19aa289eee9639c3650135f429cf1fbabccf1c068902c0",
     "i_rec and its SIX required witnesses -- a proposed port signature against a c1 that does not exist"),
    ("Q2-E", "11", "FIXED", (10436, 11034),
     "b9c7a355890def386696ac4a075b1da79420d2b03e1f0d026e83983b5e18566d",
     "B := A_F_CTP -- the THIRD factor.  i_rec's domain is the RECORD sector, which is not B"),
    ("Q2-F", "11", "ANCHOR",
     (b"B isomorphic to C(Y),\nState(B) isomorphic", b"Prob_reg_Borel(Y)."), None,
     "State(B) = the regular Borel probability measures -- K4's receiver IS the history factor"),
    ("Q2-G", "11", "FIXED", (21194, 21565),
     "e76be5c6f0536f2573c79f5d02a46e94f497cac5e87b744613ccf9c0636d011d",
     "K4's handoff: omega_hist = Omega_C0 compose i_B -- the restriction runs INTO B"),
    ("Q2-H", "11", "FIXED", (14039, 14411),
     "438e92aecb461348646cdb13c4faec51fa445b68aeee0bf5d11717078a869341",
     "res_B : State(A_C0) -> State(B), exact on its typed domain"),
    ("Q2-I", "13", "ANCHOR",
     (b"X := Hom(Lambda,U(1))", b"B isomorphic to C(Y)."), None,
     "WHERE B IS FORCED, RECORD-SIDE: and A_F is sealed COMMUTATIVE AND NUCLEAR"),
    ("Q2-J", "14", "ANCHOR",
     (b"Everything built on this presentation is TYPE-P", b"under these marks."), None,
     "the premise mark both legs still carry"),
]


def refuse(code, detail):
    sys.stderr.write("GENERATOR REFUSAL [%s]: %s\n" % (code, detail))
    sys.stderr.write("NO TABLE EMITTED.\n")
    sys.exit(2)


def main():
    blobs, digests = {}, {}
    for mid in sorted(MEMBERS):
        rel, _ = MEMBERS[mid]
        path = os.path.join(ARCHIVE_ROOT, rel)
        try:
            with open(path, "rb") as fh:
                data = fh.read()
        except OSError as exc:
            refuse("R1", "member %s unreadable at %s (%s)" % (mid, path, exc))
        blobs[mid], digests[mid] = data, hashlib.sha256(data).hexdigest()

    rows, fixed_total, fixed_match = [], 0, 0
    for label, mid, shape, spec, pin, note in SPANS:
        data = blobs[mid]
        if shape == "FIXED":
            a, b = spec
            if pin is None:
                refuse("R2", "%s is FIXED with no upstream pin" % label)
            if b > len(data):
                refuse("R2", "%s [%d,%d) exceeds member %s (%d bytes)" % (label, a, b, mid, len(data)))
            got = hashlib.sha256(data[a:b]).hexdigest()
            fixed_total += 1
            if got != pin:
                refuse("R2", "%s member %s [%d,%d) recomputed %s but upstream pin is %s"
                       % (label, mid, a, b, got, pin))
            fixed_match += 1
        elif shape == "ANCHOR":
            start, end = spec
            i = data.find(start)
            if i < 0:
                refuse("R3", "%s start anchor absent in member %s" % (label, mid))
            if data.find(start, i + 1) >= 0:
                refuse("R3", "%s start anchor AMBIGUOUS in member %s" % (label, mid))
            j = data.find(end, i)
            if j < 0:
                refuse("R4", "%s end anchor absent at or after start in member %s" % (label, mid))
            a, b = i, j + len(end)
            got = hashlib.sha256(data[a:b]).hexdigest()
        else:
            refuse("R3", "%s unknown shape %s" % (label, shape))
        rows.append((label, mid, shape, a, b, got, note))

    out = ["MEMBER DIGEST TABLE -- rehashed at full archive-root paths at run time", ""]
    for mid in sorted(MEMBERS):
        rel, role = MEMBERS[mid]
        out.append("| %s | `%s` | `%s` | %s |" % (mid, rel, digests[mid], role))
    out += ["", "SPAN TABLE -- full citation tuple per CLOSURE_MEMBER_CITATION_RULE_V001", ""]
    for label, mid, shape, a, b, got, note in rows:
        rel, _ = MEMBERS[mid]
        out.append("| %s | `%s` | `%s` | `[%d,%d)` | %s | `%s` | %s |"
                   % (label, rel, digests[mid], a, b, shape, got, note))
    out += ["", "FILES=%d  SPANS=%d  FIXED-REVERIFIED=%d/%d MATCH"
            % (len(MEMBERS), len(rows), fixed_match, fixed_total)]
    print("\n".join(out))


if __name__ == "__main__":
    main()
