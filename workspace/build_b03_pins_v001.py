#!/usr/bin/env python3
"""
build_b03_pins_v001.py -- pin generator for STAGE8_DESC_B03_DARIO_V001.md (relay 1020, DARIO lane).

WHAT THIS IS.  A TOOL, NOT EVIDENCE.  It computes every file digest and every byte-span digest that
the B03 artifact pins, so that no digest and no byte offset in that artifact is typed by hand.
Span boundaries are located by ANCHOR STRINGS and the offsets are COMPUTED, then printed; the
artifact quotes the printed offsets.  Nothing here constructs, selects, adopts, ranks, or evaluates
any descent object, state, measure, or selector value.  It performs no arithmetic on any physical
quantity.  It reads no downstream object.

DECLARED INPUTS (Q-920 input-custody rule: no undeclared, unsealed input).
  Every file this script opens is listed in FILES below, at its FULL PATH from the
  alpha-program-archive root (Q-913 path rule).  It reads NOTHING ELSE -- no JSON sidecar, no
  environment, no network, no directory walk.  Run it from the archive root.

REFUSAL RULE (Q-924: a generator refuses to emit what it cannot ground).
  If any declared input is missing, any anchor is absent or ambiguous at its declared occurrence,
  or any FIXED span fails to reproduce the upstream digest it re-verifies, this script prints the
  failure and EXITS NONZERO WITHOUT EMITTING A TABLE.  A partial table is not emitted.

USAGE
  cd /Users/bgm/MB Work/alpha-program-archive && python3 workspace/build_b03_pins_v001.py
"""

import hashlib
import sys

# ---------------------------------------------------------------- declared inputs (full paths)

FILES = [
    ("M01", "relay_inbox/RELAY_PASTE_1020_B03_BUILD_DARIO_V001.md"),
    ("M02", "relay_inbox/RELAY_PASTE_1023_FRESH_SESSION_BOOTSTRAP_DARIO_V003.md"),
    ("M03", "relay_outbox/1020_DEFERRED.md"),
    ("M04", "supervision/PROGRAM_STATE_BRIEF_V005.md"),
    ("M05", "supervision/LOCKED_PROCESS.md"),
    ("M06", "supervision/DECLINE_REGISTER_V002.md"),
    ("M07", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md"),
    ("M08", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md"),
    ("M09", "workspace/STAGE8_DESC_AUDIT_CODEX2_V002.md"),
    ("M10", "workspace/STAGE8_DESC_DEMAND_DARIO_V008.md"),
    ("M11", "workspace/STAGE8_DESC_B02_DARIO_V001.md"),
    ("M12", "workspace/STAGE8_DESC_B01_DARIO_V003.md"),
    ("M13", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md"),
    ("M14", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md"),
    ("M15", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V001.md"),
    ("M16", "workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md"),
    ("M17", "workspace/STAGE8_AXN_STATE_ALGEBRA_MAP_CODEX2_V001.md"),
    ("M18", "workspace/STAGE8_CTP_PHYS_INPUT_PACKAGE_U2_DOR008_PREMISE_LEVEL_PARTIAL_ASSEMBLY_DETERMINATION_V001.md"),
    ("M19", "workspace/STAGE8_AXN_ORIGIN_PRODUCER_CODEX2_V001.md"),
    ("M20", "workspace/STAGE8_AXN_LIVE_FAMILIES_CODEX2_V001.md"),
    ("M21", "workspace/STAGE8_AXN_PINNING_CHECK_CODEX2_V001.md"),
    ("M22", "workspace/STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V004.md"),
    ("M23", "workspace/build_b03_pins_v001.py"),
]

# ------------------------------------------------------------------------------ span locators
#
# Each entry: (pin_id, member_id, start_anchor, end_rule, note)
#   ("line",)            -> span ends AFTER the newline terminating the anchor's line
#   ("to", anchor)       -> span ends AT the first occurrence of anchor at-or-after start
#   ("through", anchor)  -> span ends AFTER the first occurrence of anchor at-or-after start
#   ("fixed", a, b, d)   -> literal [a,b), used ONLY to RE-VERIFY a span an upstream sealed
#                           artifact already pinned; d is that upstream digest and a mismatch
#                           is a refusal, not a note.
#
# THE ROW CONVENTION IS INHERITED, NOT INVENTED: a table-row span runs from its leading pipe
# THROUGH its terminating newline.  B02 fixed it by recomputing B01's row to B01's own pin; the
# two FIXED audit-row spans below re-verify it a third time against the handover's pins.

SPANS = [
    # --- the assignment's own row and the selector row: FIXED, re-verifying the handover
    ("S01", "M09", None, ("fixed", 26859, 27077,
        "43c7de164f96e46a45e1f96787efccacf00524970c8e94b1f08bd4a7b162e2b4"),
        "audit selector row 18 -- the SELECTOR typing and the continuum sentence"),
    ("S02", "M09", None, ("fixed", 32547, 32848,
        "b232586ff2599b937b0ee1bca8e7005011fa8a3aa18ef284b663e859d3285474"),
        "audit basis row B03 -- this relay's row"),
    ("S03", "M09", "3. If a SELECTOR is reached", ("through", "STOP as SELECTOR-UNFROZEN."),
        "stop-rule clause 3 -- the clause that fires"),
    ("S04", "M09", "| 23 | target-independent admissibility manifest", ("line",),
        "audit row 23 -- the manifest, INPUT, member set not chosen by current law"),
    ("S05", "M09", "| 19 | `H_omega`, `pi_omega`, `rho_pre`", ("line",),
        "audit row 19 -- the port's own fields, MIXED"),

    # --- the two named source spans: FIXED, re-verifying the assignment
    ("S06", "M18", None, ("fixed", 11681, 11929,
        "37a1e1585bdf144b18f0d14fa6c67118591b9f24b15716aee6bc0f0dcbf64e4d"),
        "U2 status block -- 'choose or derive', the would-build"),
    ("S07", "M17", None, ("fixed", 16822, 17244,
        "7b1ee5198923d54eb03d3f0942acfa8a8dfed7d96fa7edbdf2b20658da06ee47"),
        "placement square -- both sides, and 'no such equation has both sides instantiated'"),
    ("S08", "M18", None, ("fixed", 10824, 11934,
        "4313fb92fd78f6b26a5eba216e7ae7540f6b0698dc82eddd98236ceee5d7cf1b"),
        "StatePort_U2_008 -- the nine fields an inhabitant must carry"),

    # --- THE CONTINUUM, as the record proves it
    ("S09", "M16", None, ("fixed", 6680, 8157,
        "ba3c5741ded604a938483fab8cc9da1f793de1aabf18aa341cfbf4c237b0935f"),
        "B iso C(Y); Riesz-Markov census; F_1 <-> Prob(Y); cardinality EXACTLY the continuum"),
    ("S10", "M16", "RAW_POSITIVE_SCALARIZATION_FAMILY", ("through", "CONTINUUM_RESIDUAL_FAMILY__STATE_PORT_REMAINS_UNBUILT"),
        "the lead determination block -- UNIQUE_SCALARIZATION_FORCED = false | TYPE-R"),
    ("S11", "M16", "### 2.4 An explicit continuum inside the family", ("to", "## 3. Step 2"),
        "the omega_t separation witness -- pairwise inequivalent, separated by b_lambda"),
    ("S12", "M16", "U1_EQUIVALENCE_COLLAPSES_CONTINUUM_FAMILY", ("through", "U1_COMPATIBLE_NORMALIZED_FAMILY_CARDINALITY = CONTINUUM"),
        "U1 reality does not collapse -- TYPE-R"),
    ("S13", "M16", "RHO_PRE_TYPE_CONSTRAINT_CUTS_A_SCALARIZATION", ("through", "would-build: the release object just stated"),
        "rho_pre type-only existence cuts nothing -- TYPE-R"),
    ("S14", "M16", "ONE_CELL_C0_SCOPE_RESTRICTION = PASS_FOR_ALL_NORMALIZED_CANDIDATES", ("through", "supplied by the finite C0 authority"),
        "one-cell restriction consumes omega only through omega(1)=1 -- TYPE-R"),
    ("S15", "M16", "INCLUSIVE_IDENTITY_NORMALIZATION = PASS_FOR_OMEGA_T_FAMILY", ("through", "test: omega_t(1_B)=1 for every t in [0,1]"),
        "inclusive-identity normalization does not reduce the simplex to a point -- TYPE-R"),
    ("S16", "M16", "ALGEBRAIC_SCALARIZATION_COVERAGE_PROVED", ("through", "manifest"),
        "coverage proved at the algebraic level; the physical subfamily is TYPE-U"),
    ("S17", "M16", "| Stage | Survivor class | Size/status |", ("to", "Therefore the protocol does not derive"),
        "THE SURVIVOR LEDGER -- five constraints, continuum after each, then NO_VERDICT"),
    ("S18", "M16", "## 7. Failure conditions and reopen condition", ("to", "## 8. Custody"),
        "THE RECORD'S OWN FALSIFIER LIST -- item 2 is property P"),
    ("S19", "M16", "The honest residual ask is not a choice", ("through", "no such narrowing is supplied\nhere."),
        "the record states its own residual ask in its own words"),

    # --- the second, independent continuum result: the product-extension witness
    ("S20", "M17", None, ("fixed", 15554, 15965,
        "e9dafa5963128305d212f83b8c6617bfa47293f70bf91f5d7c0729fdb6828532"),
        "THE NON-UNIQUENESS THEOREM -- pinned and VERIFIED by the opposite lane at M21"),
    ("S21", "M17", "| `SM-1` |", ("to", "`SM-3` and `SM-4` are the missing commuting square"),
        "SM-1..SM-8, the map constraint system"),
    ("S22", "M17", "### 6.2 Selector trajectory: not opened", ("to", "### 6.3 K4"),
        "the four bullets: the algebraic fragments do not narrow the history simplex"),
    ("S23", "M17", "MISSING_COMPOSITION =", ("through", "and stronger than “the algebras coexist.”"),
        "the exact missing composition"),

    # --- inhabitance, at the receiver
    ("S24", "M19", None, ("fixed", 8902, 10649,
        "20b0b65035f4dbf75ae72f2c62983f881a71cb8bca69fe568e9d9eaa83c7e77f"),
        "field-by-field inhabitance audit -- omega_phys UNBOUND; the port has zero inhabitants"),

    # --- the ratified origin, and the one orbit-collapsing anchor the record owns
    ("S25", "M08", None, ("fixed", 355, 992,
        "bc83e53db7e46f27b570b1492ebd9ea53f168c344e1b06d1b82b45bb36a00750"),
        "DoR-013's adopted content -- family level, NO MEMBER SELECTED EVER, p_ch-neutrality"),
    ("S26", "M08", "## HONESTY OF RECORD", ("through", "premises: DoR-008, DoR-009, DoR-013."),
        "THE ANCHOR IS AUTHORED PHYSICS, CONFIRMED NON-DERIVABLE -- where P would have to live"),
    ("S27", "M20", "The successful counterexample is different.", ("through", "cannot do the requested work."),
        "THE SHAPE OF A COLLAPSE THAT WORKED -- and why richness without an orbit-collapsing anchor cannot"),
    ("S28", "M20", "This direction **consumes** `omega_B`", ("through", "require a source-record state."),
        "the slice consumes omega_B and cannot produce one"),
    ("S29", "M20", "### 3.3 Purification and abstract extension", ("to", "## 4."),
        "purification and abstract extension do not close the producer"),
    ("S30", "M20", "| record marginal plus slice |", ("line",),
        "the no-go table's own row: a marginal does not force the other factor's state"),

    # --- the one rule of record that DOES determine omega_phys
    ("S31", "M22", None, ("fixed", 38169, 39014,
        "ae1f79d9b7f24d2e0899f1116e38db3b51f72f0d89cc9983f8a00399f0076cee"),
        "G4 -- res_B construction; 'no independent omega_B may enter'; CONDITIONAL on Omega_C0"),

    # --- the opposite lane's verification, and the necessity ruling
    ("S32", "M21", "## 5. Non-uniqueness: verified", ("to", "## 6. The three levels"),
        "NONUNIQUENESS_THEOREM = VERIFIED; VOID_TARGET named"),
    ("S33", "M21", "SECTION_CURRENT_INSTRUMENT = remains closed", ("through", "COUNTERFACTUAL = live, principal-visible, not exercised"),
        "SECTION_WALL_TO_WALL_RECORD_NECESSITY = not established"),

    # --- the stop this relay inherits
    ("S34", "M11", "**G2 — THE SELECTOR GAP", ("through", "TRACE_STOP = SELECTOR-UNFROZEN at omega_phys (stop rule clause 3)\n```"),
        "B02's G2 -- the selector gap, reading-independent and scope-independent"),

    # --- the demand conditions that bind this object
    ("S35", "M10", "| 35 | The StatePort placement binding", ("line",),
        "condition 35 -- the placement binding and its common-origin certificate"),
    ("S36", "M10", "| 7 | State properties: positive", ("line",),
        "condition 7 -- positive, trace-class where applicable, normalized"),
    ("S37", "M10", "| 12 | Provenance: shared primitive inputs", ("line",),
        "condition 12 -- provenance, no post hoc import"),

    # --- the read rule of record for member 12
    ("S38", "M14", "  status(member 02) := RATIFIED_FAMILY_LEVEL_BY_DOR_013", ("line",),
        "overlay V002's status predicate, ruled EXACT by the opposite lane"),
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
            with open(path, "rb") as fh:
                data = fh.read()
        except OSError as exc:
            fail("declared input unreadable: %s (%s)" % (path, exc))
        blobs[mid] = data
        print("%s  %s  %d B\n     %s" % (mid, sha(data), len(data), path))

    print()
    print("=" * 78)
    print("COMPUTED SPANS -- offsets located, never typed")
    print("=" * 78)
    rows = []
    for pid, mid, start_anchor, end_rule, note in SPANS:
        data = blobs[mid]
        if end_rule[0] == "fixed":
            _, a, b, expect = end_rule
            if b > len(data):
                fail("%s: fixed span [%d,%d) runs past end of %s" % (pid, a, b, mid))
            got = sha(data[a:b])
            if got != expect:
                fail("%s: fixed span [%d,%d) in %s hashes %s, upstream pinned %s"
                     % (pid, a, b, mid, got, expect))
        else:
            anchor = start_anchor.encode("utf-8")
            first = data.find(anchor)
            if first < 0:
                fail("%s: start anchor absent in %s: %r" % (pid, mid, start_anchor))
            if data.find(anchor, first + 1) >= 0:
                fail("%s: start anchor AMBIGUOUS in %s (>1 occurrence): %r"
                     % (pid, mid, start_anchor))
            a = first
            if end_rule[0] == "line":
                nl = data.find(b"\n", a)
                if nl < 0:
                    fail("%s: no line terminator after anchor in %s" % (pid, mid))
                b = nl + 1
            elif end_rule[0] in ("to", "through"):
                endanchor = end_rule[1].encode("utf-8")
                hit = data.find(endanchor, a)
                if hit < 0:
                    fail("%s: end anchor absent at-or-after start in %s: %r"
                         % (pid, mid, end_rule[1]))
                b = hit if end_rule[0] == "to" else hit + len(endanchor)
            else:
                fail("%s: unknown end rule %r" % (pid, end_rule[0]))
        rows.append((pid, mid, a, b, b - a, sha(data[a:b]), note))

    for pid, mid, a, b, n, d, note in rows:
        kind = "FIXED" if any(s[0] == pid and s[3][0] == "fixed" for s in SPANS) else "     "
        print("%s %s %s [%d,%d) len=%d\n     %s\n     %s" % (pid, mid, kind, a, b, n, d, note))

    nfixed = sum(1 for s in SPANS if s[3][0] == "fixed")
    print()
    print("=" * 78)
    print("FILES = %d   SPANS = %d   FIXED-SPANS-REVERIFIED-AGAINST-UPSTREAM = %d/%d MATCH"
          % (len(FILES), len(SPANS), nfixed, nfixed))
    print("GROUNDING = COMPLETE (every anchor found, unique, and in range)")
    print("=" * 78)


if __name__ == "__main__":
    main()
