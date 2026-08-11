#!/usr/bin/env python3
"""
build_diag_b_check_pins_v001.py -- pin generator for STAGE8_DESC_DIAG_B_CHECK_DARIO_V001.md
(relay 1027, DARIO lane; cross-check of the OPPOSITE lane's diagnosis arm B).

WHAT THIS IS.  A TOOL, NOT EVIDENCE.  It computes every file digest and byte-span digest the check
artifact pins, so no digest and no offset there is typed by hand.  It verifies provenance and
signature content only.  It evaluates no physical quantity and selects nothing.

DECLARED INPUTS (Q-920): exactly FILES below, at full archive-root paths (Q-913).  Nothing else.
REFUSAL RULE (Q-924): unreadable input, absent OR AMBIGUOUS anchor, or a FIXED span that misses its
upstream digest -> print failure, exit nonzero, EMIT NO TABLE.

USAGE  cd /Users/bgm/MB Work/alpha-program-archive && python3 workspace/build_diag_b_check_pins_v001.py
"""

import hashlib
import sys

FILES = [
    ("M01", "relay_inbox/RELAY_PASTE_1027_ARM_B_CROSSCHECK_DARIO_V001.md"),
    ("M02", "workspace/STAGE8_DESC_DIAG_B_CODEX2_V001.md"),
    ("M03", "workspace/STAGE8_DESC_DIAG_A_DARIO_V001.md"),
    ("M04", "workspace/STAGE8_DESC_B03_DARIO_V001.md"),
    ("M05", "workspace/STAGE8_DESC_DEMAND_DARIO_V008.md"),
    ("M06", "workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md"),
    ("M07", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md"),
    ("M08", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md"),
    ("M09", "workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md"),
    ("M10", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md"),
    ("M11", "workspace/STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md"),
    ("M12", "workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md"),
    ("M13", "workspace/STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md"),
    ("M14", "workspace/STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md"),
    ("M15", "workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md"),
    ("M16", "workspace/STAGE8_AXN_BASE_FAMILY_INVERSE_CODEX2_V001.md"),
    ("M17", "workspace/STAGE8_TASK4A_P3_COMPLETE_U3_PACKAGE_CONSTRUCTION_AND_FOUR_FIELD_STOP_V001.md"),
    ("M18", "workspace/STAGE8_P5_COMMON_ORIGIN_DESCENT_REQUIREMENT_V001.md"),
    ("M19", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md"),
    ("M20", "supervision/PROGRAM_STATE_BRIEF_V005.md"),
    ("M21", "supervision/LOCKED_PROCESS.md"),
    ("M22", "supervision/DECLINE_REGISTER_V002.md"),
    ("M23", "workspace/build_diag_b_check_pins_v001.py"),
]

SPANS = [
    # ---- CLAIM 1: the framing trace, re-derived from the demand's own ground column
    ("A01", "M05", "| 18 | K7: the **base and weighted**", ("line",), "demand row 18, whose ONLY ground is instrument G7"),
    ("A02", "M05", "| 35 | The StatePort placement binding", ("line",), "demand row 35, ground = state-map + instrument SM"),
    ("A03", "M14", None, ("fixed", 40368, 41551, "864b46ca8562526e13972bd186e56d201a0b5898de015178063ebe9acd854f2f"),
        "instrument G7 -- row 18's ground, inside the acceptance gauntlet, [CLAIMED]"),
    ("A04", "M14", None, ("fixed", 36914, 38169, "35030c25f9cd3343bb848cefdd8336e68745a393f5d300833ac89a51c001467a"),
        "instrument SM rows -- row 35's ground"),
    ("A05", "M15", None, ("fixed", 16298, 17631, "2fd79b2e25c7afc381df9b65f7195b8aa0954b729d4b84c37292490a7653e012"),
        "state-map full repair span -- the d_joint/res_B route, [CLAIMED]"),
    ("A06", "M16", None, ("fixed", 7502, 8047, "829581cdd1f29ea25316f6b127cf44daa4ba2178c771df70e087a91f41a09987"),
        "base K7 -- whose cited ground is a later would-build"),
    ("A07", "M17", None, ("fixed", 8238, 9386, "95ddbbcaec43f0b0e297fefe3e831c457e270d4bbf14dcf16c49615849298e0c"),
        "P3 Haar/measure block -- K7's cited ground: a TYPE-U would-build, not a source theorem"),

    # ---- CLAIM 1 + 3: the three older receiving signatures
    ("B01", "M07", None, ("fixed", 37523, 38115, "e16f8b9438c518546fa7eda93c724316f4470f9a8298a50ac8d275eb09d293ad"),
        "OLDER SIGNATURE 1 -- B0 U2 role: positive normalized pre-state, effects, contacts, domains"),
    ("B02", "M08", None, ("fixed", 6266, 6883, "e6093b0f48c11d3f05d3c6fd3692b6ea2c4b320746bb92eebe72ef28ed697efe"),
        "OLDER SIGNATURE 2 -- substitute-admissibility U2, with d_U2 the descent witness"),
    ("B03", "M09", None, ("fixed", 8954, 9569, "8917c67f455bb0b152950c1931891311c3c96029c1ba4100219370038198dbb0"),
        "OLDER SIGNATURE 3 -- producer P5: positive normalized rho_pre from the SAME microscopic source"),

    # ---- CLAIM 3: the authored scaffolding, and its self-declared status
    ("C01", "M10", None, ("fixed", 10824, 11934, "4313fb92fd78f6b26a5eba216e7ae7540f6b0698dc82eddd98236ceee5d7cf1b"),
        "the nine-field StatePort, introduced as 'The smallest state object that can meet the sealed role'"),
    ("C02", "M10", None, ("fixed", 11681, 11929, "37a1e1585bdf144b18f0d14fa6c67118591b9f24b15716aee6bc0f0dcbf64e4d"),
        "the 'choose or derive' status line -- authored in the U2 assembly"),
    ("C03", "M10", "The smallest state object that can meet the sealed role is", ("line",),
        "THE AUTHORING SENTENCE ITSELF -- the assembly declares it is meeting a role, not quoting one"),

    # ---- CLAIM 2: the carrier's disclosed adoption
    ("D01", "M11", None, ("fixed", 8881, 9735, "40140cc98b0e2c37ed158b44c2e0e0772bdecc411d2f62807da8c6d07fc8fc35"),
        "carrier label field -- 'Standing: PROPOSED_NEW_ADOPTION'"),
    ("D02", "M11", None, ("fixed", 11469, 12646, "4ca50ae00875a187e258e0898df1efab4cdfdf4c7bc23224db303bb9a8488809"),
        "algebra/CTP completion -- 'Choose A_F := C*(Lambda)', PROPOSED_NEW_ADOPTION"),
    ("D03", "M11", None, ("fixed", 19837, 22406, "f31e95b4b6168c2923f98ba39a361d12f491493ff4e6f7139a3a375d45acd09e"),
        "the choice table -- seven proposed adoptions WITH alternatives displayed"),
    ("D04", "M12", None, ("fixed", 6680, 8157, "ba3c5741ded604a938483fab8cc9da1f793de1aabf18aa341cfbf4c237b0935f"),
        "the census that rests on that carrier"),
    ("D05", "M12", "CANDIDATE_FAMILY_EXHAUSTIVELY_DECLARED = true | TYPE-P | premises: DoR-008", ("line",),
        "the census's OWN conditional typing -- the record already typed it TYPE-P"),

    # ---- CLAIM 4: the two register misses
    ("E01", "M19", "## Q-212. DoR 008 RATIFIED", ("through", "TYPE-P | premises: DoR-008`."),
        "Q-212 -- ratification AND the principal's VOID condition on everything TYPE-P on it"),
    ("E02", "M19", "## Q-223. The quasifree branch governs", ("through", "nothing sealed answers it."),
        "Q-223 -- different algebras, NO SEALED TRANSPORT, no thermal selector, D6 narrowed"),
    ("E03", "M13", None, ("fixed", 25126, 25677, "0668d9d5943cbe29f5f982c39a3152de04aff1def6e0cea2bc23a8de8114bc10"),
        "the Q-223 artifact's FINAL VERDICT block -- carries D6_DISPOSITION and the survivor shapes"),
    ("E04", "M13", None, ("fixed", 23225, 24348, "d97b846cb0219367a1e7dbb741f55eab0a4fe847e865f4bf01014af3bdd188cb"),
        "its D6 block"),
    ("E05", "M06", "- `STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md`", ("through", "established."),
        "THE SUPPLY MAP'S DECLINE of that artifact -- 'its terminal block is bare fences'"),

    # ---- CLAIM 5: the consistency question
    ("F01", "M05", "| 1 | Four typed descent maps", ("line",), "condition 1 -- ground is P5, an OLDER receiver"),
    ("F02", "M05", "| 7 | State properties: positive", ("line",), "condition 7 -- ground is P5 + the U2 rho_pre span"),
    ("F03", "M05", "| 13 | The U2 role signature", ("line",), "condition 13 -- ground is TWO of the three older signatures"),
    ("F04", "M10", None, ("fixed", 7290, 7829, "f9fb7a84ce4e3b954e5444baedc6703d9cc8ec52fe04f41e1b3b6d915b3d5372"),
        "condition 7's U2 ground: rho_pre positive, trace-class, unit trace -- and NOTHING further"),
    ("F05", "M03", "GAUGE_VERDICT = LOAD-BEARING-AT (spans above)", ("line",), "Arm A's verdict line"),
    ("F06", "M03", "  CONSUMES-STATE                    11", ("line",), "Arm A's CONSUMES-STATE count"),

    # ---- what arm B's finding does to B03, stated against B03's own bytes
    ("G01", "M04", "supplied by the ratified presentation, so the census inherits", ("line",),
        "B03 §3.1 DID type the census TYPE-P | premises: DoR-008"),
    ("G02", "M04", "CONTINUUM = DISPLAYED-AT-BYTES", ("line",),
        "B03's final-lines CONTINUUM header -- which does NOT carry the conditionality"),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(m):
    print("REFUSED: " + m)
    print("INPUT CUSTODY / GROUNDING FAILED -- no table emitted.")
    sys.exit(2)


def main():
    blobs = {}
    print("=" * 78)
    print("DECLARED INPUTS")
    print("=" * 78)
    for mid, path in FILES:
        try:
            d = open(path, "rb").read()
        except OSError as e:
            fail("unreadable: %s (%s)" % (path, e))
        blobs[mid] = d
        print("%s  %s  %d B\n     %s" % (mid, sha(d), len(d), path))

    print("\n" + "=" * 78)
    print("COMPUTED SPANS")
    print("=" * 78)
    nf = 0
    for pid, mid, start, rule, note in SPANS:
        d = blobs[mid]
        if rule[0] == "fixed":
            _, a, b, exp = rule
            if b > len(d):
                fail("%s: [%d,%d) past end of %s" % (pid, a, b, mid))
            got = sha(d[a:b])
            if got != exp:
                fail("%s: [%d,%d) in %s hashes %s, upstream pinned %s" % (pid, a, b, mid, got, exp))
            nf += 1
            kind = "FIXED "
        else:
            anc = start.encode("utf-8")
            f0 = d.find(anc)
            if f0 < 0:
                fail("%s: anchor absent in %s: %r" % (pid, mid, start))
            if d.find(anc, f0 + 1) >= 0:
                fail("%s: anchor AMBIGUOUS in %s: %r" % (pid, mid, start))
            a = f0
            if rule[0] == "line":
                nl = d.find(b"\n", a)
                if nl < 0:
                    fail("%s: no line end in %s" % (pid, mid))
                b = nl + 1
            else:
                e = rule[1].encode("utf-8")
                h = d.find(e, a)
                if h < 0:
                    fail("%s: end anchor absent in %s: %r" % (pid, mid, rule[1]))
                b = h if rule[0] == "to" else h + len(e)
            kind = "      "
        print("%s %s %s [%d,%d) len=%d\n     %s\n     %s"
              % (pid, mid, kind, a, b, b - a, sha(d[a:b]), note))

    print("\n" + "=" * 78)
    print("FILES = %d   SPANS = %d   FIXED-REVERIFIED = %d/%d MATCH" % (len(FILES), len(SPANS), nf, nf))
    print("GROUNDING = COMPLETE")
    print("=" * 78)


if __name__ == "__main__":
    main()
