#!/usr/bin/env python3
"""
build_b03_v002_pins_v001.py -- pin generator for STAGE8_DESC_B03_DARIO_V002.md
(relay 1029, DARIO lane; the reframed port).

A TOOL, NOT EVIDENCE.  Computes every file digest and byte-span digest V002 pins, so none is typed.
Reads structure and signatures only; evaluates no physical quantity; selects nothing.

DECLARED INPUTS (Q-920): exactly FILES below, full archive-root paths (Q-913).  Nothing else.
REFUSAL (Q-924): unreadable input, absent OR AMBIGUOUS anchor, or a FIXED span missing its upstream
digest -> print failure, exit nonzero, EMIT NO TABLE.

USAGE  cd /Users/bgm/MB Work/alpha-program-archive && python3 workspace/build_b03_v002_pins_v001.py
"""

import hashlib
import sys

FILES = [
    ("M01", "relay_inbox/RELAY_PASTE_1029_B03_V002_REFRAME_DARIO_V001.md"),
    ("M02", "workspace/STAGE8_DESC_B03_DARIO_V001.md"),
    ("M03", "workspace/STAGE8_DESC_B03_CHECK_CODEX2_V001.md"),
    ("M04", "workspace/STAGE8_DESC_DIAG_B_CODEX2_V001.md"),
    ("M05", "workspace/STAGE8_DESC_DIAG_A_DARIO_V001.md"),
    ("M06", "workspace/STAGE8_DESC_DIAG_B_CHECK_DARIO_V001.md"),
    ("M07", "workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md"),
    ("M08", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md"),
    ("M09", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md"),
    ("M10", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_SUBSTITUTE_ADMISSIBILITY_ADJUDICATION_V001.md"),
    ("M11", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md"),
    ("M12", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md"),
    ("M13", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md"),
    ("M14", "workspace/STAGE8_AXN_ORIGIN_PRODUCER_CODEX2_V001.md"),
    ("M15", "workspace/STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md"),
    ("M16", "workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md"),
    ("M17", "workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md"),
    ("M18", "workspace/STAGE8_TASK2D_QUASIFREE_BRANCH_RHO_PRE_GOVERNANCE_AUDIT_V001.md"),
    ("M19", "workspace/STAGE8_DESC_DEMAND_DARIO_V008.md"),
    ("M20", "workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md"),
    ("M21", "workspace/STAGE8_DESC_B02_DARIO_V001.md"),
    ("M22", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md"),
    ("M23", "supervision/PROGRAM_STATE_BRIEF_V005.md"),
    ("M24", "supervision/LOCKED_PROCESS.md"),
    ("M25", "supervision/DECLINE_REGISTER_V002.md"),
    ("M26", "workspace/build_b03_v002_pins_v001.py"),
]

SPANS = [
    # ---------- THE REFRAMED DEMAND, at the older receivers only
    ("D1", "M07", "P0. One microscopic source-record-field", ("to", "P2."),
        "THE COMPLETED OBJECT DEFINED: P1 = a completed source-record-field carrier/algebra A_SRF_CTP"),
    ("D2", "M07", None, ("fixed", 8954, 9569, "8917c67f455bb0b152950c1931891311c3c96029c1ba4100219370038198dbb0"),
        "PRODUCER P5 -- 'A positive normalized rho_pre ON THE COMPLETED OBJECT ... same microscopic source'"),
    ("D3", "M08", None, ("fixed", 7290, 7829, "f9fb7a84ce4e3b954e5444baedc6703d9cc8ec52fe04f41e1b3b6d915b3d5372"),
        "v004's rho_pre: 'on the FULL SOURCE-RECORD-FIELD Hilbert space' -- and the completed Hilbert space ABSENT"),
    ("D4", "M09", None, ("fixed", 37523, 38115, "e16f8b9438c518546fa7eda93c724316f4470f9a8298a50ac8d275eb09d293ad"),
        "B0 U2 role -- positive normalized pre-state, effects, contacts, domains"),
    ("D5", "M10", None, ("fixed", 6266, 6883, "e6093b0f48c11d3f05d3c6fd3692b6ea2c4b320746bb92eebe72ef28ed697efe"),
        "substitute-admissibility U2 -- and the descent witness d_U2 the demand requires"),

    # ---------- THE FORCED OBJECT
    ("F1", "M11", None, ("fixed", 22842, 24541, "84a5b7050188448e2a0cc526de0131b297cb734bc96b292968e1e37080b61cf0"),
        "THE FORCED OBJECT: d_state := the unique normalized fixed state of P_src (READ WITH M12+M13)"),
    ("F2", "M11", None, ("fixed", 22882, 22958, "65dfdedb8e8dc7a513904f4443ab215c08aa9d6c59d5a42ae75eb1395ede0662"),
        "overlay pin #7 -- a STALE surface lying INSIDE F1; carried openly, not trimmed"),
    ("F3", "M13", None, ("fixed", 355, 992, "bc83e53db7e46f27b570b1492ebd9ea53f168c344e1b06d1b82b45bb36a00750"),
        "DoR-013 -- the ratification, family level, no member ever"),
    ("F4", "M14", None, ("fixed", 8902, 10649, "20b0b65035f4dbf75ae72f2c62983f881a71cb8bca69fe568e9d9eaa83c7e77f"),
        "THE SCOPE VERDICT: 'PASS ONLY AT SOURCE-SECTOR SCOPE; not a joint-state certificate'"),
    ("F5", "M15", "1. `P_src` is a normal CPTP preparation channel", ("through", "in `State(A_src)`."),
        "P_src acts on the SOURCE carrier -- so the forced state lives there"),
    ("F6", "M12", "  status(member 02) := RATIFIED_FAMILY_LEVEL_BY_DOR_013", ("line",),
        "the read rule governing every citation of M11"),

    # ---------- NARROWING 1: the proof dependency, restated
    ("N1", "M16", None, ("fixed", 6680, 8157, "ba3c5741ded604a938483fab8cc9da1f793de1aabf18aa341cfbf4c237b0935f"),
        "THE ONE EXHAUSTIVE PROOF -- and the receiver B iso C(Y) that the extension theorem imports"),
    ("N2", "M17", None, ("fixed", 15554, 15965, "e9dafa5963128305d212f83b8c6617bfa47293f70bf91f5d7c0729fdb6828532"),
        "THE EXTENSION THEOREM -- which RESTS ON N1's receiver, not independent of it"),

    # ---------- NARROWING 2: the five span digests V001 generated and did not publish
    ("P05", "M20", None, ("fixed", 27077, 27288, "b1328f6ffe1dcbf6f7202d1929528089bc3f3f34b10f5679d81f363afef59bfa"),
        "V001 S05 -- audit row 19, now PUBLISHED"),
    ("P16", "M16", None, ("fixed", 17311, 17617, "5a81d03d2c628d39b920aef863688ec21204adccb0efbf6b86b478e2ce02f7d8"),
        "V001 S16 -- coverage proved / physical subfamily TYPE-U, now PUBLISHED"),
    ("P22", "M17", None, ("fixed", 20615, 21172, "ea287648c57fe67944612dc0f0fc819196902acc5f5b5746f83d4560aec3cb2f"),
        "V001 S22 -- 'selector trajectory: not opened', now PUBLISHED"),
    ("P23", "M17", None, ("fixed", 17252, 17629, "37f573355e9ddd08fa59d883fae490149543fbea952507ffb649409c6fe83d8e"),
        "V001 S23 -- MISSING_COMPOSITION, now PUBLISHED"),
    ("P34", "M21", None, ("fixed", 32608, 33541, "5575f6ba332dc8a73083e46b0f8138b235b0a6246333de6173051d26c1b7637b"),
        "V001 S34 -- B02's G2 selector gap, now PUBLISHED"),

    # ---------- NARROWING 3: P's two record spans, from which the composed P was assembled
    ("R1", "M16", "## 7. Failure conditions and reopen condition", ("to", "## 8. Custody"),
        "P's COLLAPSE CORE -- the record's own falsifier item 2"),
    ("R2", "M16", "The honest residual ask is not a choice", ("through", "no such narrowing is supplied\nhere."),
        "P's RESIDUAL PACKAGE -- the record's own residual ask"),

    # ---------- Q-223 and the consumers
    ("Q1", "M18", None, ("fixed", 25126, 25677, "0668d9d5943cbe29f5f982c39a3152de04aff1def6e0cea2bc23a8de8114bc10"),
        "Q-223's verdict block -- D6 narrowed; survivor shapes"),
    ("Q2", "M22", "## Q-223. The quasifree branch governs", ("through", "nothing sealed answers it."),
        "Q-223 -- DIFFERENT ALGEBRAS, NO SEALED TRANSPORT; no thermal selector in scope"),
    ("Q3", "M22", "## Q-212. DoR 008 RATIFIED", ("through", "TYPE-P | premises: DoR-008`."),
        "Q-212 -- the VOID condition on everything TYPE-P on DoR-008"),
    ("C1", "M05", "  CONSUMES-STATE                    11", ("line",),
        "Arm A's eleven, whose count 1027 withdrew as frame-dependent"),
    ("C2", "M06", "ARMS = CONSISTENT (combined picture)", ("line",),
        "the cross-check's combined picture, which this reframe executes"),
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
