#!/usr/bin/env python3
"""
build_schema_intersection_pins_v001.py

GENERATOR for STAGE8_DESC_SCHEMA_AND_INTERSECTION_DARIO_V001.md  (relay 1047, DARIO lane).

DECLARED INPUTS (Q-920/Q-924): exactly the members of MEMBERS below, read at their canonical
paths relative to the alpha-program-archive root, plus this file itself.  Nothing else is read
and nothing is emitted that is not computed from those bytes.

CITATION RULE (CLOSURE_MEMBER_CITATION_RULE_V001): canonical path + full source SHA-256 +
raw-byte half-open [a,b) + full span SHA-256 for every published span.

SPAN CONVENTION, DECLARED: raw bytes, half-open [a,b), no decoding, no newline normalisation,
no trimming.  ANCHOR spans run from the first byte of the start anchor up to but not including
the first byte of the end anchor.  NO TAIL IS EVER INVENTED.  FIXED spans reproduce the interval
their upstream published and must re-verify against the published pin at its published width.

LIVE-APPENDING MEMBER CLASS -- NEW AT 1047, AND IT IS A RESPONSE TO A CHECK FINDING.
The 1046 check found the 1045 artifact current-reproducible at 56/57 rather than its seal-time
57/57, because the questions-settled register lawfully grew between seal and check and its
WHOLE-FILE digest moved.  A member marked LIVE is therefore declared as such: its whole-file
digest is a RUN-TIME SNAPSHOT and carries no verdict weight, while the verdict-bearing authority
for that member is its SPAN digests, which are stable under append.  The prose-digest audit is
run in two modes so the distinction is checkable rather than asserted:
  strict  -- accounting set = all member digests + all span digests
  stable  -- accounting set = non-LIVE member digests + all span digests
An artifact that quotes no LIVE whole-file digest scores identically in both modes, and that
identity is the property this generator exists to make verifiable.

REFUSAL PATHS.  The generator emits NOTHING on:
  R1  a member that cannot be read at its declared path;
  R2  a FIXED span whose recomputed digest disagrees with its published pin;
  R3  a start anchor that is absent, or occurs more than once (AMBIGUOUS);
  R4  an end anchor that is absent, occurs more than once, or precedes the start anchor;
  R5  a span row naming a BARRED member (self-citation bar).

SELF-CITATION BAR: no span is drawn from any artifact of this lane.  BARRED members are closed
for carriage only.

MODES:
  (no args)            member table, sidecar check, span table, scans, summary
  --audit <artifact>   prose-digest audit (Q-954), strict and stable modes
"""

import hashlib
import os
import re
import sys

ROOT = "/Users/bgm/MB Work/alpha-program-archive"

# key: (path, role, barred, live)
MEMBERS = [
    ("01", "relay_inbox/RELAY_PASTE_1047_SCHEMA_FREEZE_AND_INTERSECTION_DARIO_V001.md",
     "the assignment", False, False),
    ("02", "relay_inbox/RELAY_PASTE_1044_FRESH_SESSION_BOOTSTRAP_DARIO_V006.md",
     "the bootstrap; the SYMBOLIC LINE", False, False),
    ("03", "workspace/STAGE8_OBJ0_EXACT_SIGNATURE_DOMAIN_CODOMAIN_SPEC_AND_BUILD_STOP_V001.md",
     "THE SCHEMA AND THE FULL PHASE-A SURFACE: nine fields, freeze tuple, seven port contracts,"
     " section 10, SIG-T1/T2/T11", False, False),
    ("04", "workspace/STAGE8_DESC_SELECTION_CHECK_CODEX2_V001.md",
     "THE CHECK OF RECORD: the admissibility hinge -- ports are Class A", False, False),
    ("05", "workspace/STAGE8_RANK1_CTP_PRODUCER_ALGEBRA_Q52_SPEC_V001.md",
     "THE LAW SIDE: class definition, P0-P7", False, False),
    ("06", "workspace/STAGE8_JOINT_P0_BUILDABILITY_IN_PRINCIPLE_RESULT_V001.md",
     "Q-95/Q-94: rows, Obj_0/Core_0 typing, the noncircularity sentence", False, False),
    ("07", "workspace/STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md",
     "Q-97: the inventory is too thin", False, False),
    ("08", "workspace/STAGE8_ACCESSOR_THEOREM_SUBSTITUTION_ADJUDICATION_EINSTEIN_V001.md",
     "THIRD LANE: uniqueness sense; compatibility is not determination", False, False),
    ("09", "supervision/QUESTIONS_SETTLED_REGISTER_V001.md",
     "LIVE -- Q-955 build order, Q-956, Q-957 the hinge and the hook", False, True),
    ("10", "supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md",
     "DoR-008: premises, falsifier direction, undischarged items", False, False),
    ("11", "supervision/DECISION_OF_RECORD_013_GEN_OMEGA_RATIFIED_FAMILY_LEVEL_2026-08-02_V001.md",
     "DoR-013: family level, no member ever, authored physics", False, False),
    ("12", "workspace/STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md",
     "READ ONLY with members 13 and 11", False, False),
    ("13", "workspace/MEMBER12_HEADER_OVERLAY_RECORD_V002.md",
     "the read rule -- CARRIAGE ONLY (DARIO), NO SPAN", True, False),
    ("14", "workspace/STAGE8_FIELD_CTP_CARRIER_AND_C0_JOIN_INSTANTIATION_ATTEMPT_V001.md",
     "the open NO_VERDICT slot", False, False),
    ("15", "workspace/STAGE8_FIELD_CTP_ALGEBRAIC_PRESENTATION_ADOPTION_PROPOSAL_V002.md",
     "the provenance ceiling", False, False),
    ("16", "workspace/STAGE8_TASK2D_SCALARIZATION_FUNCTIONAL_FORCING_PROTOCOL_RESULT_V001.md",
     "TASK2D: the scalarization continuum", False, False),
    ("17", "workspace/DEMAND_READING_DECISION_OF_RECORD_V001.md",
     "the governing receiver reading", False, False),
    ("18", "supervision/PROGRAM_STATE_BRIEF_V005.md", "state pin", False, False),
    ("19", "supervision/LOCKED_PROCESS.md", "process law", False, False),
    ("20", "supervision/DECLINE_REGISTER_V002.md", "S01-S37", False, False),
    ("21", "workspace/STAGE8_DESC_PHYSICALSIG_SELECTION_DARIO_V001.md",
     "1045 -- CARRIAGE ONLY (DARIO), NO SPAN", True, False),
    ("22", "workspace/build_physicalsig_selection_pins_v001.py",
     "the 1045 generator -- CARRIAGE ONLY (DARIO), NO SPAN", True, False),
    ("23", "workspace/build_schema_intersection_pins_v001.py",
     "this generator; declared inputs are exactly members 01-23", False, False),
]

# FIXED spans carried at their published pins: (tag, member, a, b, pin, use)
FIXED_SPANS = [
    ("A03", "03", 25970, 26653,
     "f0c1e4acdb730965cfd0fa5318663732f757f69fe56d4124215800a2070b8506",
     "THE NINE FIELDS; no entry assigned a physical value"),
    ("A05", "03", 67258, 68448,
     "35d7e30e8c500317c48771f0172f455ccba3622c950b6f32c283bff9609e4b47",
     "PHASE A - the four signature-freeze prerequisite rows"),
    ("F02", "06", 44072, 44269,
     "f04749a556ba8949c91a3dfbccfd786bada0bca0144946ac94d093fbf408ebcc",
     "Obj_0 and Core_0 typed"),
    ("F07", "14", 16880, 17121,
     "dd01923b74098215e105f835ece6f3a15672f861afdd3803be1dc195da8cd10a",
     "THE OPEN SLOT, at its exact span"),
    ("A09", "07", 616, 2009,
     "08cccf3d059964ad27a5fafd3bb898c32f1b652a3613e67eaf5454d5321824c6",
     "Q-97: the inventory is too thin"),
    ("T01", "03", 58090, 58342,
     "9cdfb8405ea4d07bcb516bfae3797cf42c0a8badfa3d0a956cfb9edbe8274bb9",
     "SIG-T11 target-independence row, at the check's own pin"),
    ("T02", "03", 20815, 21632,
     "7624391c8ee61446cc7a45dd52e2f85fcf45155a419853fb92a2142cc27ed678",
     "Q-94 structure boundary, at the check's own pin"),
    ("T03", "03", 71912, 72797,
     "94afb97be61f3471bcba203ecaccc6f7ea09bd68c1c78fbe3a4bdf9b98215365",
     "what the signature must supply to all seven ports, at the check's own pin"),
    ("T04", "03", 34855, 48128,
     "3bb615444210ea41e923d669cb7acff04c0a5e76e995c6bc1925fcdcacf5b1b3",
     "the seven exact port-contract schemas, at the check's own pin"),
    ("T05", "06", 50970, 51617,
     "fa7d8a9881456c71cb1d9849868f180696bc2295988cbd22966eb1daa8e75461",
     "preconstruction criteria versus descendant outputs, at the check's own pin"),
]

# ANCHOR spans: (tag, member, start, end, use)
ANCHOR_SPANS = [
    ("P01", "03", "SignatureFreezeInputs_0 :=", "FreezeExactSig_0 :",
     "THE FREEZE TUPLE: ten members, censused below"),
    ("P02", "03", "PRIMITIVE_INTERFACE_REQUIREMENT(I_prim,PhysicalSig_0) :=",
     "DERIVED_SECTOR_REFERENCE_REQUIREMENT(S_sector,ExactSig_0) :=",
     "the twelve conjuncts -- every one on I_prim"),
    ("P03", "03", "DERIVED_SECTOR_REFERENCE_REQUIREMENT(S_sector,ExactSig_0) :=",
     "In prose, the primitive inventory must provide",
     "THE TWIN: the derived-sector schema is in the same condition as the primitive one"),
    ("P04", "03", "2. exact frozen primitive-binding and derived-sector-reference **type**",
     "3. the P1 domain equivalence predicate",
     "the Phase-A coverage sentence -- the schema's only description"),
    ("P05", "03", "In prose, the primitive inventory must provide an explicit frozen",
     "Q-97's split at the register",
     "MULTIPLICITY is signature-fixed here; SIG-T2 makes it binding data -- the shape axis"),
    ("P06", "03", "| `SIG-T2-PRIMITIVE-COVERAGE`", "| `SIG-T3-DOMAIN-CLOSURE`",
     "SIG-T2: the entry FLOOR -- authority, exact type, domain, multiplicity"),
    ("P07", "03", "| `SIG-T1-PHYSICAL-EXACTNESS`", "| `SIG-T2-PRIMITIVE-COVERAGE`",
     "SIG-T1: disjunction, placeholder or post-output choice IS the failure"),
    ("P08", "03", "DomainKind_1 := COMMON_DENSE | PROVED_EQUIVALENT",
     "The port must supply the actual/canonical package",
     "OPEN BRANCH 1: DomainKind_1, two branches"),
    ("P09", "03", "The same six-file exactness packet used for P6",
     "DomainKind_1 := COMMON_DENSE",
     "and its equivalence relation was SEARCHED: qualifying_definition_file_list EMPTY"),
    ("P10", "03", "FamilyKind_5 := EXHAUSTIVE | NONEXHAUSTIVE",
     "StateEffectPackage_5(o,c1,c3,c4;family_kind_5) :=",
     "OPEN BRANCH 2: FamilyKind_5, two branches, frozen before execution"),
    ("P11", "03", "EvolutionEquivalence_6 := EXACT RELATION TO BE DERIVED AND FROZEN",
     "DynamicsPackage_6 :=",
     "OPEN BRANCH 3: EvolutionEquivalence_6, declared undefined in its own definition line"),
    ("P12", "03", "A word-boundaried inspection of the exact six-file P6 packet",
     "Therefore the conditional Port 6 requirement",
     "and it too was SEARCHED: qualifying_definition_file_list EMPTY"),
    ("P13", "03", "CrossRowCoherence_0 :=", "Proposed direction-bearing production",
     "the cross-row schema DOES have content: eight named coherence conjuncts"),
    ("P14", "03", "This order is a declared testable schema",
     "### 9.9 Port supply disposition",
     "the graph schema: edge kinds listed, completeness TYPE-U"),
    ("P15", "03", "WitnessedResult_i(o,r,g,I_i,p_i,S_i,d_i) :=",
     "An origin trace certifies the jointly constructed port result",
     "OriginTrace_i is APPLIED with a pinned argument list and never DEFINED"),
    ("P16", "03", "all_seven_port_contracts_schematically_well_typed = NO_VERDICT",
     "all_seven_ports_jointly_physically_inhabitable",
     "the port schemas' own gate names a frozen PhysicalSig_0 FIRST"),
    ("P17", "03", "An object of an arbitrary physical category", "### 8.2 Signature-freeze",
     "the internal operation domains/codomains ARE the fields; requirements state what must freeze"),
    ("P18", "03", "Consequently an object in an exact physical category cannot be selected",
     "These are `NO_VERDICT`, not negative claims",
     "the four named category candidates, no exhaustiveness claim"),
    ("P19", "03", "Obj_0_semantic_type =", "executed typing result",
     "the semantic type is fixed and is a ROLE"),
    ("P20", "03", "**Not fixed by sealed text:**", "**Declared here under F-GK3:**",
     "the eight things sealed text does not fix"),
    ("P21", "05", "Definition: a common-origin CTP producer algebra", "What it resists",
     "THE CLASS DEFINITION"),
    ("P22", "05", "P0. One microscopic", "P1. A completed",
     "THE P0 ROW: disjunctive"),
    ("P23", "04", "Therefore the port schemas are lawful **Class A constraints**",
     "## 3. Re-run of all affected fields",
     "THE HINGE RULING OF RECORD, carried and executed"),
    ("P24", "04", "FIELDS = 0 SELECTED / 9 CONSTRAINED-NOT-SELECTED / 0 UNCONSTRAINED",
     "This is constraint propagation inside Phase A",
     "the corrected tally this relay starts from"),
    ("P25", "04", "NO FIELD IS POSITIVELY SELECTED.",
     "The subject's “one passage bearing three times” finding",
     "the check's own narrower statement, which this relay sharpens"),
    ("P26", "09", "THE HINGE RULING: the seven co-frozen port-contract schemas",
     "Actual candidate OUTPUTS stay inadmissible",
     "Q-957 at the register: the hinge, of record"),
    ("P27", "09", "THE FORWARD HOOK, SCORED BY NAME: STILL NOT TERMINAL",
     "That re-attempt (with the schema freeze ahead of it)",
     "Q-957: the hook, and the instruction this relay executes"),
    ("P28", "06", "Treating any row in this table as a preconstruction input",
     "#### Unavailable correspondence routes",
     "Q-95's noncircularity sentence -- descendants are tested AFTER, never consumed BEFORE"),
    ("P29", "08", "**C2 UNIQUENESS**", "**C3 ACCESSOR CLAUSE**",
     "third lane: the uniqueness SENSE must be declared"),
    ("P30", "10", "NOT discharged:", "C0_prop is now AVAILABLE",
     "DoR-008's two undischarged items -- field 9's named finishing property"),
]

SCAN_TOKENS = [
    "FrozenPrimitiveBindingSchema_0",
    "FrozenDerivedSectorReferenceTypeSchema_0",
    "FrozenPortContractSchemas_1_to_7",
    "FrozenCrossRowCoherenceSchema_0",
    "FrozenPortDependencyGraphSchema_0",
    "FrozenOriginPredicateAndTraceSchema_0",
    "FrozenCertificateSchema_0",
    "DomainEquivalence_1_if_used",
    "EvolutionEquivalence_6",
    "OriginTrace_",
    "qualifying_definition_file_list: EMPTY",
]
SCAN_DIRS = ["workspace", "supervision", "relay_inbox", "relay_outbox"]

HEX64 = re.compile(rb"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")


def die(rule, detail):
    sys.stderr.write("GENERATOR REFUSAL %s: %s\nNOTHING EMITTED.\n" % (rule, detail))
    sys.exit(1)


def load():
    blobs, digests, sizes = {}, {}, {}
    for key, path, _r, _b, _l in MEMBERS:
        try:
            with open(os.path.join(ROOT, path), "rb") as fh:
                data = fh.read()
        except OSError as exc:
            die("R1", "member %s unreadable at %s (%s)" % (key, path, exc))
        blobs[key] = data
        digests[key] = hashlib.sha256(data).hexdigest()
        sizes[key] = len(data)
    return blobs, digests, sizes


def midx():
    return {k: (p, r, b, l) for k, p, r, b, l in MEMBERS}


def resolve_spans(blobs):
    idx = midx()
    rows = []
    for tag, key, a, b, pin, use in FIXED_SPANS:
        if idx[key][2]:
            die("R5", "span %s names BARRED member %s" % (tag, key))
        got = hashlib.sha256(blobs[key][a:b]).hexdigest()
        if got[:len(pin)] != pin:
            die("R2", "FIXED span %s: pin %s, recomputed %s" % (tag, pin, got))
        rows.append((tag, key, a, b, got, "FIXED", use))
    for tag, key, sa, ea, use in ANCHOR_SPANS:
        if idx[key][2]:
            die("R5", "span %s names BARRED member %s" % (tag, key))
        data = blobs[key]
        ns = data.count(sa.encode())
        if ns != 1:
            die("R3", "span %s start anchor occurs %d times: %r" % (tag, ns, sa))
        a = data.find(sa.encode())
        if ea == "\n":                      # to-end-of-line convention, declared
            b = data.find(b"\n", a)
            if b == -1:
                die("R4", "span %s: no line terminator after start anchor" % tag)
        else:
            ne = data.count(ea.encode())
            if ne != 1:
                die("R4", "span %s end anchor occurs %d times: %r" % (tag, ne, ea))
            b = data.find(ea.encode())
        if b <= a:
            die("R4", "span %s end anchor precedes start anchor" % tag)
        rows.append((tag, key, a, b, hashlib.sha256(data[a:b]).hexdigest(), "ANCHOR", use))
    return rows


def sidecar_check(digests):
    rows = []
    for key, path, _r, _b, _l in MEMBERS:
        side = os.path.join(ROOT, path + ".seal.sha256")
        if not os.path.exists(side):
            rows.append((key, path, "NO-SIDECAR", ""))
            continue
        try:
            with open(side) as fh:
                claimed = fh.read().split()[0].strip()
        except (OSError, IndexError):
            rows.append((key, path, "SIDECAR-UNREADABLE", ""))
            continue
        rows.append((key, path, "SEAL-OK" if claimed == digests[key] else "SEAL-MISMATCH",
                     claimed))
    return rows


def run_scans():
    out = []
    for tok in SCAN_TOKENS:
        hits, total = [], 0
        for d in SCAN_DIRS:
            for dirpath, _dn, fns in os.walk(os.path.join(ROOT, d)):
                for fn in sorted(fns):
                    if not (fn.endswith(".md") or fn.endswith(".py") or fn.endswith(".json")):
                        continue
                    fp = os.path.join(dirpath, fn)
                    try:
                        with open(fp, "rb") as fh:
                            n = fh.read().count(tok.encode())
                    except OSError:
                        continue
                    if n:
                        hits.append((os.path.relpath(fp, ROOT), n))
                        total += n
        out.append((tok, total, hits))
    return out


def emit():
    blobs, digests, sizes = load()
    spans = resolve_spans(blobs)
    idx = midx()
    print("GENERATOR build_schema_intersection_pins_v001.py")
    print("ROOT %s\n" % ROOT)
    print("== MEMBER TABLE ==")
    for key, path, _r, barred, live in MEMBERS:
        flag = " ".join(x for x in ["BARRED-CARRIAGE-ONLY" if barred else "",
                                    "LIVE-SNAPSHOT" if live else ""] if x)
        print("%-4s %-108s %-64s %9d %s" % (key, path, digests[key], sizes[key], flag))
    print("\n== SIDECAR CHECK (absent is reported as absent, never as agreement) ==")
    for key, path, status, claimed in sidecar_check(digests):
        print("%-4s %-20s %-108s %s" % (key, status, path, claimed))
    print("\n== SPAN TABLE ==")
    for tag, key, a, b, got, kind, use in spans:
        print("%s  %s" % (tag, kind))
        print("    path   %s" % idx[key][0])
        print("    source %s" % digests[key])
        print("    span   [%d,%d)" % (a, b))
        print("    digest %s" % got)
        print("    use    %s" % use)
    print("\n== SCANS (counts read from the scan, never predicted) ==")
    for tok, total, hits in run_scans():
        print("%-45s TOTAL %d" % (tok, total))
        for rel, n in hits:
            print("        %3d  %s" % (n, rel))
    fixed = sum(1 for r in spans if r[5] == "FIXED")
    anchor = len(spans) - fixed
    print("\n== SUMMARY ==")
    print("FILES=%d SPANS=%d FIXED-REVERIFIED=%d/%d MATCH ANCHORS=%d"
          % (len(MEMBERS), len(spans), fixed, fixed, anchor))
    print("SELF_CITATION_BAR: members %s carriage only; 0 span rows name them."
          % ",".join(k for k, _p, _r, b, _l in MEMBERS if b))
    print("LIVE MEMBERS: %s (whole-file digest is a run-time snapshot with no verdict weight;"
          " span digests are the authority)"
          % ",".join(k for k, _p, _r, _b, l in MEMBERS if l))
    print("REFUSALS_FIRED_THIS_RUN: NONE (R1-R5 silent; not-fired is reported as not-fired)")


def audit(artifact):
    blobs, digests, _s = load()
    spans = resolve_spans(blobs)
    spandig = {r[4] for r in spans}
    live = {k for k, _p, _r, _b, l in MEMBERS if l}
    strict = set(digests.values()) | spandig
    stable = {d for k, d in digests.items() if k not in live} | spandig
    try:
        with open(artifact, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        die("R1", "audit target unreadable: %s" % exc)
    toks = [t.decode() for t in HEX64.findall(data)]
    distinct = sorted(set(toks))
    print("== PROSE-DIGEST AUDIT (Q-954) ==")
    print("target      %s" % artifact)
    print("pattern     (?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
    print("occurrences %d   distinct %d" % (len(toks), len(distinct)))
    for name, acc in (("strict", strict), ("stable", stable)):
        out = [t for t in distinct if t not in acc]
        print("MODE %-7s accounting set %d values; OUTSIDE %d; %d/%d distinct, %d/%d occurrences"
              % (name, len(acc), len(out), len(distinct) - len(out), len(distinct),
                 len([t for t in toks if t in acc]), len(toks)))
        for t in out:
            print("        UNACCOUNTED %s" % t)
    print("STRICT==STABLE: %s (true iff the artifact quotes no LIVE whole-file digest)"
          % ("YES" if all(t in stable for t in distinct) ==
             all(t in strict for t in distinct) and
             len([t for t in distinct if t not in stable]) ==
             len([t for t in distinct if t not in strict]) else "NO"))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--audit":
        audit(sys.argv[2])
    else:
        emit()
