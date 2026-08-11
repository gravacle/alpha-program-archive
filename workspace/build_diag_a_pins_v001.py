#!/usr/bin/env python3
"""
build_diag_a_pins_v001.py -- pin generator for STAGE8_DESC_DIAG_A_DARIO_V001.md
(relay 1025, DARIO lane, PE-17 diagnosis arm A).

WHAT THIS IS.  A TOOL, NOT EVIDENCE.  It computes every file digest and every byte-span digest the
diagnosis artifact pins, so that no digest and no byte offset there is typed by hand.  It reads
STRUCTURE only: which sealed object declares that it consumes which other object.  It evaluates no
physical quantity, opens no downstream value, and constructs, selects, ranks or names nothing.

DECLARED INPUTS (Q-920).  Exactly the files in FILES, at full archive-root paths (Q-913).  Nothing
else is opened -- no directory walk, no environment, no network.  Run from the archive root.

REFUSAL RULE (Q-924).  If a declared input is unreadable, a start anchor is absent OR AMBIGUOUS, or
a FIXED span fails to reproduce the upstream digest it re-verifies, this script prints the failure
and EXITS NONZERO WITHOUT EMITTING A TABLE.  A partial table is never emitted.

USAGE
  cd /Users/bgm/MB Work/alpha-program-archive && python3 workspace/build_diag_a_pins_v001.py
"""

import hashlib
import sys

FILES = [
    ("M01", "relay_inbox/RELAY_PASTE_1025_DIAGNOSIS_ARM_A_DARIO_V001.md"),
    ("M02", "workspace/STAGE8_DESC_B03_DARIO_V001.md"),
    ("M03", "workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md"),
    ("M04", "workspace/STAGE8_DESC_DEMAND_DARIO_V008.md"),
    ("M05", "workspace/STAGE8_DESC_B02_DARIO_V001.md"),
    ("M06", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md"),
    ("M07", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md"),
    ("M08", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md"),
    ("M09", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_B0_LOAD_BEARING_STOP_SPEC_V001.md"),
    ("M10", "workspace/STAGE8_TASK4A_P3_COMPLETE_U3_PACKAGE_CONSTRUCTION_AND_FOUR_FIELD_STOP_V001.md"),
    ("M11", "workspace/STAGE8_AXN_BASE_FAMILY_INVERSE_CODEX2_V001.md"),
    ("M12", "workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md"),
    ("M13", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md"),
    ("M14", "workspace/STAGE8_AXN_ORIGIN_PRODUCER_CODEX2_V001.md"),
    ("M15", "workspace/STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md"),
    ("M16", "workspace/STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md"),
    ("M17", "supervision/PROGRAM_STATE_BRIEF_V005.md"),
    ("M18", "supervision/LOCKED_PROCESS.md"),
    ("M19", "supervision/DECLINE_REGISTER_V002.md"),
    ("M20", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md"),
    ("M21", "workspace/build_diag_a_pins_v001.py"),
]

# ROW convention inherited from B01/B02/B03: leading pipe THROUGH terminating newline.
SPANS = [
    # ---------------- the twelve basis rows that are the ledger's subjects
    ("L04", "M03", "| `B04` | complete `StatePort_U2_008`", ("line",), "basis row B04"),
    ("L05", "M03", "| `B05` | complete U2 reference", ("line",), "basis row B05"),
    ("L06", "M03", "| `B06` | S1 branch-joint", ("line",), "basis row B06"),
    ("L07", "M03", "| `B07` | S2 common-origin", ("line",), "basis row B07"),
    ("L08", "M03", "| `B08` | S3 joint physical", ("line",), "basis row B08"),
    ("L09", "M03", "| `B09` | S4 complete write-plus-tail", ("line",), "basis row B09"),
    ("L10", "M03", "| `B10` | closed U3 aggregation", ("line",), "basis row B10"),
    ("L11", "M03", "| `B11` | total right-domain", ("line",), "basis row B11"),
    ("L12", "M03", "| `B12` | total right-domain", ("line",), "basis row B12"),
    ("L13", "M03", "| `B13` | total right-domain", ("line",), "basis row B13"),
    ("L14", "M03", "| `B14` | total right-domain", ("line",), "basis row B14"),
    ("L15", "M03", "| `B15` | one closed certificate", ("line",), "basis row B15"),

    # ---------------- THE ROLE CONTENTS: what each descendant role actually carries
    ("R01", "M09", None, ("fixed", 37523, 38115,
        "e16f8b9438c518546fa7eda93c724316f4470f9a8298a50ac8d275eb09d293ad"),
        "C0/U1/U2/U3 role contents -- C0 and U1 STATE-FREE; U2 carries the pre-state; U3 the measure"),
    ("R02", "M09", None, ("fixed", 38121, 38437,
        "cb264602a0537a07948c31d2763094395c5670a5001ea8378d9e7f83b67ed72c"),
        "the four descent arrows and the no-undeclared-supplement rule"),

    # ---------------- the four-field would-builds: where the state enters U3
    ("F01", "M10", None, ("fixed", 8708, 9198,
        "7b0f4b369db09bd9ec96dc22c727ef86248a8d073c20eb8d1e975e15e0c6ce63"),
        "MEASURE would-build -- 'generated from the common-origin action/STATE/history-domain package'"),
    ("F02", "M10", None, ("fixed", 10691, 11236,
        "270b89250019266c07c0c3f28c2c0a339492c03cd72763e0fa105f19d5188265"),
        "CONTOUR would-build -- analytic/operator/regulator data; names NO state datum"),
    ("F03", "M10", None, ("fixed", 12613, 13281,
        "037d0b1bcf79350966bb0b2925ce5c3818b9839e44f3bdd0698b62501e902815"),
        "BOUNDARY would-build -- 'compatibility with dmu_C and the interacting contour'"),
    ("F04", "M10", None, ("fixed", 14191, 14909,
        "3c0a264b42eec07c9d43ce61131dfacc74ef4ce987b8dc540ca9181813ffc95f"),
        "DOMAIN would-build -- 'on a SCALAR PHYSICAL REPRESENTATION', which is the omega-dependent one"),

    # ---------------- K7's own requirement
    ("K01", "M11", None, ("fixed", 7502, 8047,
        "829581cdd1f29ea25316f6b127cf44daa4ba2178c771df70e087a91f41a09987"),
        "K7 -- 'must arise from the frozen common-origin action/STATE/history-domain package'"),
    ("K02", "M12", "`K4` requires an actual `omega_hist`", ("through", "weighted-projectivity comparison."),
        "K4 -- requires an ACTUAL omega_hist, hence an actual projective finite base family"),

    # ---------------- the port, the square, and the invariance theorem
    ("P01", "M13", None, ("fixed", 10824, 11934,
        "4313fb92fd78f6b26a5eba216e7ae7540f6b0698dc82eddd98236ceee5d7cf1b"),
        "StatePort -- omega_phys is field 1; H_omega is the completion of E_C0/N_omega"),
    ("P02", "M13", None, ("fixed", 11681, 11929,
        "37a1e1585bdf144b18f0d14fa6c67118591b9f24b15716aee6bc0f0dcbf64e4d"),
        "the port's status block: SPECIFIED true TYPE-P premises DoR-008; INSTANTIATED false TYPE-U"),
    ("P03", "M12", None, ("fixed", 16822, 17244,
        "7b1ee5198923d54eb03d3f0942acfa8a8dfed7d96fa7edbdf2b20658da06ee47"),
        "the placement square"),
    ("P04", "M12", None, ("fixed", 15554, 15965,
        "e9dafa5963128305d212f83b8c6617bfa47293f70bf91f5d7c0729fdb6828532"),
        "THE INVARIANCE THEOREM -- what the record marginal CANNOT see"),
    ("P05", "M16", None, ("fixed", 38169, 39014,
        "ae1f79d9b7f24d2e0899f1116e38db3b51f72f0d89cc9983f8a00399f0076cee"),
        "G4 -- omega_hist := Omega_C0 compose i_B"),

    # ---------------- demand conditions that name the joint state
    ("D01", "M04", "| 1 | Four typed descent maps", ("line",), "condition 1 -- d_state and the four maps"),
    ("D07", "M04", "| 7 | State properties: positive", ("line",), "condition 7 -- the state's own properties"),
    ("D13", "M04", "| 13 | The U2 role signature", ("line",), "condition 13 -- the U2 role signature"),
    ("D18", "M04", "| 18 | K7: the **base and weighted**", ("line",), "condition 18 -- K7 as receiver"),
    ("D35", "M04", "| 35 | The StatePort placement binding", ("line",), "condition 35 -- the placement binding"),

    # ---------------- QUESTION 2: the provenance of the codomain bar
    ("Q01", "M14", None, ("fixed", 8902, 10649,
        "20b0b65035f4dbf75ae72f2c62983f881a71cb8bca69fe568e9d9eaa83c7e77f"),
        "the inhabitance audit carrying BOTH 'WRONG CODOMAIN' typings"),
    ("Q02", "M07", None, ("fixed", 22842, 24541,
        "84a5b7050188448e2a0cc526de0131b297cb734bc96b292968e1e37080b61cf0"),
        "THE DEFINITION: d_state := the unique normalized fixed state of P_src (READ WITH M06+M08)"),
    ("Q03", "M07", None, ("fixed", 22882, 22958,
        "65dfdedb8e8dc7a513904f4443ab215c08aa9d6c59d5a42ae75eb1395ede0662"),
        "overlay V002 pin #7 -- a STALE status surface lying INSIDE Q02's quoted span"),
    ("Q04", "M15", "1. `P_src` is a normal CPTP preparation channel", ("through", "in `State(A_src)`."),
        "P_src is a channel on the SOURCE carrier -- so its fixed state is a state on A_src"),
    ("Q05", "M15", "### 3.3 Purification and abstract extension", ("to", "## 4."),
        "no canonical transport: purification/extension do not determine the joint state"),
    ("Q06", "M08", None, ("fixed", 355, 992,
        "bc83e53db7e46f27b570b1492ebd9ea53f168c344e1b06d1b82b45bb36a00750"),
        "DoR-013's adopted content -- the three maps ratified as a package"),
    ("Q07", "M06", "  status(member 02) := RATIFIED_FAMILY_LEVEL_BY_DOR_013", ("line",),
        "the read rule's status predicate, governing every citation of M07"),
    ("Q08", "M20", "## Q-900 —", ("line",),
        "Q-900's heading -- the registrar adjudication that fixes the INSTRUMENT-AUTHORED class"),

    # ---------------- B03's two findings, read for their pins only
    ("B01", "M02", "| C34 | **G4's restriction pinning**", ("line",), "B03's C34 row -- read for its pin, not re-argued"),
    ("B02", "M02", "| C18 | **The p_ch-neutrality certificate**", ("line",), "B03's C18 row -- the near-miss this relay adjudicates"),
    ("B03", "M02", "| C19 | **`d_state` (`rho_S`)**", ("line",), "B03's C19 row"),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(msg):
    print("REFUSED: " + msg)
    print("INPUT CUSTODY / GROUNDING FAILED -- no table emitted.")
    sys.exit(2)


def main():
    blobs = {}
    print("=" * 78)
    print("DECLARED INPUTS -- full archive-root paths, rehashed at run time")
    print("=" * 78)
    for mid, path in FILES:
        try:
            data = open(path, "rb").read()
        except OSError as exc:
            fail("declared input unreadable: %s (%s)" % (path, exc))
        blobs[mid] = data
        print("%s  %s  %d B\n     %s" % (mid, sha(data), len(data), path))

    print("\n" + "=" * 78)
    print("COMPUTED SPANS -- offsets located, never typed")
    print("=" * 78)
    nfixed = 0
    for pid, mid, start, rule, note in SPANS:
        data = blobs[mid]
        if rule[0] == "fixed":
            _, a, b, expect = rule
            if b > len(data):
                fail("%s: fixed span [%d,%d) past end of %s" % (pid, a, b, mid))
            got = sha(data[a:b])
            if got != expect:
                fail("%s: fixed [%d,%d) in %s hashes %s, upstream pinned %s"
                     % (pid, a, b, mid, got, expect))
            nfixed += 1
            kind = "FIXED "
        else:
            anc = start.encode("utf-8")
            first = data.find(anc)
            if first < 0:
                fail("%s: start anchor absent in %s: %r" % (pid, mid, start))
            if data.find(anc, first + 1) >= 0:
                fail("%s: start anchor AMBIGUOUS in %s: %r" % (pid, mid, start))
            a = first
            if rule[0] == "line":
                nl = data.find(b"\n", a)
                if nl < 0:
                    fail("%s: no line terminator in %s" % (pid, mid))
                b = nl + 1
            elif rule[0] in ("to", "through"):
                e = rule[1].encode("utf-8")
                hit = data.find(e, a)
                if hit < 0:
                    fail("%s: end anchor absent after start in %s: %r" % (pid, mid, rule[1]))
                b = hit if rule[0] == "to" else hit + len(e)
            else:
                fail("%s: unknown end rule %r" % (pid, rule[0]))
            kind = "      "
        print("%s %s %s [%d,%d) len=%d\n     %s\n     %s"
              % (pid, mid, kind, a, b, b - a, sha(data[a:b]), note))

    print("\n" + "=" * 78)
    print("FILES = %d   SPANS = %d   FIXED-REVERIFIED-AGAINST-UPSTREAM = %d/%d MATCH"
          % (len(FILES), len(SPANS), nfixed, nfixed))
    print("GROUNDING = COMPLETE (every anchor found, unique, and in range)")
    print("=" * 78)


if __name__ == "__main__":
    main()
