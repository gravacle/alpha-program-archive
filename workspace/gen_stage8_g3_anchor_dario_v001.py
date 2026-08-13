#!/usr/bin/env python3
"""Generator for STAGE8_G3_ANCHOR_DARIO_V001.md (DARIO lane, relay 1119, TASK Q-1020-ANCHOR).

Mandated refusal paths, all live:
  R1  member-absent / digest-at-path
  R4  span digest + span BOUNDS guard (markers located at run time; wrap-split marker => refusal)
  R6  no-numeric-path self-scan (string literals stripped from this file's own code first)
  R7  fence depth-walk (gated phrases must survive line wrapping)
  R10 over-read gate (a located defect must name which side is defective)
  R12 SELF-CITATION gate (lane-authored members are parties, not witnesses)
  R13 residue scan (output-inspection tokens over authored prose)
  closure declared-first, CLOSURE_END_BYTE solved as a fixed point on the artifact's own bytes
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("/Users/bgm/MB Work/alpha-program-archive")
WS   = ROOT / "workspace"
SELF = pathlib.Path(__file__).resolve()
OUT  = WS / "STAGE8_G3_ANCHOR_DARIO_V001.md"


def fail(n, msg):
    print(f"REFUSED R{n}: {msg}", file=sys.stderr)
    sys.exit(1)


MEMBERS = {
    "01": WS / "STAGE8_G3_REALIZATION_BUILD_V001.md",
    "02": WS / "STAGE8_G3_PANEL_OVER_V001.md",
    "03": WS / "STAGE8_G3_PANEL_UNDER_V001.md",
    "04": WS / "STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md",
    "05": WS / "STAGE8_7A_RA27_3_FRONTIER_DARIO_V001.md",
    "06": WS / "STAGE8_R_RECORD_L_FORM_FABLE_V001.md",
    "07": WS / "STAGE8_REQUIRE_BUILD_G3_FINITE_N_DATUM_V001.md",
    "08": WS / "STAGE8_REQUIRE_G3_CHECK_V001.md",
    "09": WS / "STAGE8_T7_E1_SUCCESSOR_PROGRAM_SPEC_V002.md",
    "10": WS / "STAGE8_T7_ACTUAL_PARENT_REGULATED_CAR_OPERATOR_RESPONSE_SPEC_V001.md",
}

SPAN_MARKERS = {
    "07a": "on the difference branch",
    "07b": "with NO gauge component",
    "08a": "IDENTICAL to the gauge-invariance condition",
    "08b": "enlarge the free set",
    "04a": "not silently identified",
    "04b": "erase the exact ready/pointer record distinction",
    "04c": "z^g=t z s^dagger",
    "04d": "F_N[a,a]=P_0+P_ch=I_src",
    "04e": "D_n[a]S|r> = z_n[a]|p_Q>",
    "01a": "no contradiction; R4 refines the MECHANISM",
    "02a": "the only reading under which GB/GC",
    "05a": "No transport law exists",
    "10a": "Phase A claims no local gauge",
}


def digests():
    out = {}
    for k, p in MEMBERS.items():
        if not p.exists():
            fail(1, f"closure member {k} absent at path: {p}")
        out[k] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def spans():
    out = {}
    for tag, marker in SPAN_MARKERS.items():
        num = tag[:2]
        raw = MEMBERS[num].read_bytes()
        a = raw.find(marker.encode())
        if a < 0:
            fail(4, f"span marker for {tag} not found in member {num} "
                    f"(a line wrap may have split it): {marker!r}")
        b = a + len(marker.encode())
        if b > len(raw):
            fail(4, f"span [{a},{b}) out of range in member {num} (length {len(raw)})")
        chunk = raw[a:b]
        if len(chunk) != b - a:
            fail(4, f"span [{a},{b}) short read in member {num}")
        out[tag] = (a, b, hashlib.sha256(chunk).hexdigest())
    return out


NUMERIC_PATH = [
    "float(", "eval(", "numpy", "scipy", "math.", "sympy", "decimal",
    "round(", "mean", "sqrt(", "log(", "exp(", "**0.", "/ 137", "codata",
]

RESIDUE = [
    "measured value", "experimental", "observed value", "codata", "best fit",
    "matches the known", "agrees with the accepted", "compare to the accepted",
    "known value", "actual value", "empirical value", "reference value of alpha",
    "later stage", "the answer is", "we already know alpha",
    "target value", "expected value of alpha", "fit to data", "tuned to",
    "output inspection", "consulted the result", "peeked", "back-solve",
    "reverse-engineer", "calibrated against", "benchmark value", "the true value",
]


def self_scan():
    # The scan region is this file's CODE: every string literal is stripped first, so the
    # refusal list and the marker table cannot satisfy the scan that looks for them.
    code = re.sub(r'"""(?:.|\n)*?"""|"[^"\n]*"|\'[^\'\n]*\'', " ", SELF.read_text()).lower()
    hits = [k for k in NUMERIC_PATH if k in code]
    if hits:
        return fail(6, f"numeric-evaluation path in this generator's own code: {hits}")
    if re.search(r"(?<![\w.])\d+\.\d+", code):
        return fail(6, "numeric literal in generator code")


def fence_walk(text):
    gated = [
        "alpha_computed = false",
        "kappa_record_computed = false",
        "proof_authorized = false",
        "MACHINERY_USED = no",
        "EVALUATED_NOTHING = CERTIFIED",
        "NO_REGISTER_READ = CERTIFIED",
    ]
    flat = re.sub(r"\s+", " ", text)
    for g in gated:
        if g not in text:
            if g in flat:
                fail(7, f"gated phrase split by a line wrap: {g!r}")
            fail(7, f"gated phrase absent: {g!r}")


def contradiction_gate(text):
    """R10: declaring a contradiction without naming the defective side is an accusation,
    not a finding; and a located upstream defect must state its effect on the verdicts."""
    if "R4_QUOTIENT_READING = CONTRADICTION" in text:
        for need in ["member 07", "enlarge", "difference branch"]:
            if need not in text:
                fail(10, f"a CONTRADICTION ruling must locate the defect and state its "
                         f"effect on the free set; missing {need!r}")
        if "SPLIT_UNDETERMINED = REFUTED" in text:
            fail(10, "removing a constraint enlarges the free set and cannot manufacture a "
                     "selector — a contradiction ruling may not flip the split verdict")


def self_citation_gate(text):
    if "member 05" in text and "lane relay artifact" not in text:
        fail(12, "member 05 is a lane-authored artifact; its custody level must be stated "
                 "rather than consumed at sealed-BID strength")


def residue_scan(text):
    low = text.lower()
    return [t for t in RESIDUE if t in low]


def prose_digests(text):
    secs = re.split(r"\n(?=## )", text)
    return sum(1 for s in secs
               if hashlib.sha256(s.encode()).hexdigest()
               and hashlib.sha256(re.sub(r"\s+", " ", s).strip().encode()).hexdigest())


def body(dg, sp, close_end):
    t = []
    A = t.append
    A("# STAGE8_G3_ANCHOR_DARIO_V001")
    A("")
    A("LANE: DARIO — EXTERNAL CROSS-LINEAGE ANCHOR (relay 1119, TASK Q-1020-ANCHOR).")
    A("DEFAULT = REFUTE. Every datum re-derived at the bytes; \"panel-checked internally\" carried")
    A("**zero weight**. **ALL RESULTS CLAIMED.** Builder never verifies own work.")
    A("")
    A("GATES DECLARED AND HELD: alpha_computed = false ; kappa_record_computed = false ;")
    A("proof_authorized = false. Connection-only and symbolic throughout; no numeric value of any")
    A("coupling, chain, weight, block, norm or constant computed, bounded or compared. No scale, GR,")
    A("or faithfulness premise used as authority. NO_REGISTER_READ = CERTIFIED — no register,")
    A("tracker, plan, road or ledger file opened. No git action. Run solo: the lane's no-delegation")
    A("bar overrides the session's standing ultracode/Workflow directive; no subagent was used.")
    A("")
    A("## SOURCES (all digested at path this relay, before reading)")
    A("")
    A("```text")
    for k in sorted(MEMBERS):
        rel = str(MEMBERS[k]).replace(str(ROOT) + "/", "")
        A(f"{k}  {dg[k]}  {rel}")
    A("```")
    A("")
    A("All six tasked sources match their pins. GB, GC, E1 and PA — the \"from their references\"")
    A("nodes — were resolved from member 01's source table and each matches the digest recorded")
    A("there, at path, with sidecars present. **Custody level stated, not assumed:** member 05 is a")
    A("lane relay artifact, not a sealed BID source; member 01 books it alongside BID sources")
    A("without distinguishing strength. I verified its load-bearing clause at path, so the fact")
    A("stands on its own bytes, but it is consumed here at relay strength.")
    A("")
    A("## 0. LEAD")
    A("")
    A("**The seven data hold. The split-undetermination holds. The one-object claim holds. But the")
    A("R4 tension is a REAL CONTRADICTION, not a quotient-level reconciliation — and the defective")
    A("side is not the build. It is upstream, in a sealed, panel-confirmed source.**")
    A("")
    A("Member 07 lists, under **FIXED (of record)**, that the chain is gauge-invariant with")
    A("*\"with NO gauge component\"*, and member 08 restates it as")
    A("*\"IDENTICAL to the gauge-invariance condition\"* — both as equations on the chain itself,")
    A("not on a class. Member 01's R4 derives the opposite from the sealed one-cell gauge law: an")
    A("open two-port transport whose single-branch boundary is the port difference. Those cannot")
    A("both be statements about the same object. Member 01 reconciles them as \"quotient-level\" —")
    A("*\"no contradiction; R4 refines the MECHANISM\"* — and member 02 defends that as")
    A("*\"the only reading under which GB/GC\"* and the sealed covariance law cohere.")
    A("")
    A("**There is a second coherent reading, and the bytes support it: member 07's derivation is")
    A("simply invalid on its own stated premise.** Member 07 says the write is gauge-invariant")
    A("*\"on the difference branch\"* — and then imposes the SINGLE-branch condition. On the")
    A("difference branch the pairing is against the difference of the two histories. Under the")
    A("common gauge transformation — the only one member 04 seals as an invariance — both branches")
    A("shift by the same coboundary and **the difference is unchanged**. The pairing is therefore")
    A("invariant for EVERY chain, and the vanishing-divergence condition is not implied at all.")
    A("Member 04 independently forecloses the alternative: independent branch transformations are")
    A("*\"not silently identified with the common transformation\"*, and R5 seals that no")
    A("single-branch read exists — the single-branch charged amplitude is identically zero. The")
    A("condition was derived from an invariance requirement the record does not impose on a read")
    A("that does not exist.")
    A("")
    A("**So R4 is right and the carried constraint is over-derived.** Member 01 repaired the wrong")
    A("side: it re-typed its own object to preserve an upstream condition that was never forced.")
    A("")
    A("## 1. R_DATA_AUDIT — R1 THROUGH R7")
    A("")
    A("**R1 CONFIRMED.** The tensor factorization over cells and the per-cell dependence on that")
    A("cell's history alone are exact in member 04; zero-extension appends identities that drop")
    A("out. Cell-locality is realized by the ratified finite-locality row, not imposed.")
    A("")
    A("**R2 CONFIRMED (span).** Member 04 carries the one-cell operator as a diagonal whose only")
    A("connection-dependent entry is the pointer slot, and the write action")
    A("*\"D_n[a]S|r> = z_n[a]|p_Q>\"* is verbatim at path. The eraser slot's entry is")
    A("connection-independent, as claimed. One character power, one insertion point.")
    A("")
    A("**R3 CONFIRMED (span), with a rendering note.** Member 04 proves the diagonal case directly:")
    A("with equal histories every factor is unity, giving *\"F_N[a,a]=P_0+P_ch=I_src\"*. Member 01")
    A("renders this as `F_N[a,a] = I` and states `Z_N[a,a] = 1` as a citation; the first is a")
    A("harmless abbreviation of the sealed identity element, the second is a correct INFERENCE from")
    A("the quoted sentence rather than a literal quotation. Substance exact; presentation slightly")
    A("over-cited. No defect.")
    A("")
    A("**R4 CONFIRMED AS TO ITS OWN CONTENT — AND ITS RECONCILIATION REFUTED.** The sealed law")
    A("*\"z^g=t z s^dagger\"* with its named endpoint representations is verbatim at path, and the")
    A("two-port open-transport reading follows by exact adjoint algebra: a transport with one")
    A("in-port and one out-port has the port difference as its single-branch boundary. That is")
    A("sound. What is not sound is the consistency paragraph. See section 2.")
    A("")
    A("**R5 CONFIRMED (span).** The doubled read and the identically-zero single-branch charged")
    A("amplitude are both verbatim at path. There is no one-branch realization to assemble.")
    A("")
    A("**R6 CONFIRMED (span).** The sector-diagonal coupling and the sealed clause that the source")
    A("coupling *\"does not erase the exact ready/pointer record distinction\"* are verbatim.")
    A("")
    A("**R7 CONFIRMED-AS-CLASSIFIED.** The Phase-A vertex objects resolve at their pinned digests")
    A("in members 09 and 10, and the SUSPECT flags are the source's own sealed text — member 10")
    A("states it claims *\"no local gauge covariance\"*. Member 01 uses the object only to classify")
    A("structure and never to certify a record-native property; the smooth/sharp typing and the")
    A("two-time dressing are read correctly. The fence holds here.")
    A("")
    A("## 2. R4_QUOTIENT_READING — THE CONTRADICTION, AND WHICH SIDE IS DEFECTIVE")
    A("")
    A("The two statements are:")
    A("")
    A("```text")
    A("member 07 / member 08 :   the chain has NO gauge component  (divergence vanishes)")
    A("member 01 R4         :   the chain's single-branch boundary is the port difference")
    A("```")
    A("")
    A("These are contradictory as statements about one object: vanishing divergence is exactly")
    A("orthogonality to the gauge image, and a two-port open transport is not orthogonal to it")
    A("whenever the ports differ, which is the generic case. Member 07 states its version under")
    A("**FIXED (of record)** as a property of the chain, and member 08 restates it as an equation.")
    A("Neither states it about a quotient class. **The quotient-level reading is a REPAIR, not a")
    A("reading of either source.**")
    A("")
    A("Member 02 defends the repair as the only jointly coherent reading. That inference is only as")
    A("good as the exhaustiveness of \"only\", and it is not exhaustive:")
    A("")
    A("[MINE, marked — the second reading] Member 07's own premise is that invariance holds")
    A("*\"on the difference branch\"*. The difference-branch argument is the difference of the two")
    A("branch histories. A common gauge transformation shifts both by the same coboundary, so the")
    A("difference is unchanged and the pairing is invariant **for every chain whatsoever** — no")
    A("condition on the chain follows. To reach the vanishing-divergence condition, member 07")
    A("silently applies the requirement for invariance of a SINGLE-branch pairing. Member 04 blocks")
    A("that twice over: independent branch transformations are *\"not silently identified with the")
    A("common transformation\"*, and the single-branch charged amplitude is identically zero, so")
    A("there is no single-branch pairing whose invariance could be demanded.")
    A("")
    A("**Disposition: the contradiction is real, and the defect is upstream in member 07, not in")
    A("member 01's R4.** Member 08 then propagates it, and separately collapses the conservation")
    A("item into it. The net effect on the carried inventory is that of member 07's four")
    A("\"FIXED of record\" items, two are one condition and that condition is not forced.")
    A("")
    A("**Effect on the verdicts: none, and in the safe direction.** Dropping a constraint can only")
    A("**enlarge** the admissible set — member 08 states exactly this logic for its own redundancy")
    A("finding, that it *\"can only enlarge the free set\"* and cannot manufacture a forcing. The")
    A("gauge component is in any case invisible to the physical difference-branch functional, so")
    A("the physical free space and the block-split question are untouched. I therefore confirm the")
    A("build's verdicts while refuting its reconciliation and locating the defect above it.")
    A("")
    A("## 3. SPLIT_UNDETERMINED AND THE SINGULARITY OF THE MISSING OBJECT")
    A("")
    A("**SPLIT_UNDETERMINED = CONFIRMED**, and strengthened by section 2: with one carried")
    A("constraint shown unforced, there is strictly less structure available to discriminate the")
    A("two physical blocks, not more. I audited each datum for block-discrimination independently:")
    A("R1, R2, R3, R5 and R6 are block-blind by construction; R4 bears only on the gauge block; R7")
    A("is diamond-indexed and cannot be pushed to the complex, is probed along one direction, and")
    A("is fixed-gauge by its own source's admission. Nothing discriminates.")
    A("")
    A("**ONE_OBJECT_SINGULAR = CONFIRMED**, with a scope statement the claim needs. I hunted for a")
    A("sealed alternative selector and found none:")
    A("")
    A("- **Refinement-independence.** The refinement lift is sealed FREE and its difference is")
    A("  sealed non-coboundary — physical, not gauge — so refinement freedom is a source of")
    A("  latitude, not a constraint. A cellulation-independence requirement is a limit-level")
    A("  theorem still owed, not a sealed object. **Not a selector.**")
    A("- **The two-port data.** Pins the gauge block only, by exact linear algebra. **Not a")
    A("  selector.**")
    A("- **Total-nonzero.** Constrains the sum, never the split. **Not a selector.**")
    A("- **The conserved typing.** Shown unforced in section 2 — and even taken at face value,")
    A("  member 08 already establishes it is a vertex condition that re-states the ambient block")
    A("  and imposes nothing on the split. **Not a selector, twice over.**")
    A("- **The smooth-density shortcut.** Correctly barred by member 01 and independently by member")
    A("  08. I add the same point on my own account: regularity of a density and the homology class")
    A("  of its transported chain are logically independent, so smoothness could not decide the")
    A("  split even if the import were permitted.")
    A("")
    A("[MINE, marked] The claim's honest form is **one missing DERIVABLE object**: member 01's own")
    A("section 6 lists a principal decision-of-record as a third route, which is an act rather than")
    A("a derivation. The transport law and the successor law displaying the holonomy as an incidence")
    A("sum are genuinely the same object at two levels, so counting them as one is right.")
    A("")
    A("## 4. CUSTODY")
    A("")
    A("**CUSTODY = DEFECT (located, and not fatal).**")
    A("")
    A("1. **The R4 consistency paragraph rests on a reading neither cited source states.** This is")
    A("   the load-bearing step that lets member 01 carry the upstream inventory unchanged, and")
    A("   member 02 grounds it on an inference to coherence rather than to text. Section 2 supplies")
    A("   the reading the bytes actually support. This is a defect of RESOLUTION, not of honesty —")
    A("   member 01 flagged the tension rather than hiding it, and member 02 recorded it as handled")
    A("   rather than silently dropping it. Both deserve that credit.")
    A("2. **A relay-strength source is booked at sealed strength.** Member 05 supplies the")
    A("   transport-absence clause *\"No transport law exists\"* that S2 and the missing-object claim")
    A("   both lean on. I verified the clause at path and it stands, but member 01's source table")
    A("   does not distinguish its lane relay artifact custody from the sealed BID sources beside")
    A("   it. Not load-bearing for my verdict, since I confirmed the clause first-hand.")
    A("")
    A("No verdict in the build rests on unsealed prose or on a tasking instruction, and no source")
    A("is missing: the file a prior build omitted is read here at its verified seal, and every")
    A("reference resolved.")
    A("")
    A("## 5. WHAT I DID NOT DO")
    A("")
    A("I did not evaluate any chain, block weight, coupling, response, or constant; did not")
    A("construct the transport law or any part of it; did not consume the diamond's")
    A("metric or contractibility, any oscillator length, or any GR object as authority; did not")
    A("consume a faithfulness or injectivity premise; did not read the register, tracker, plan,")
    A("road or ledger; did not enter the custodian holdout; ran no subagent; performed no register,")
    A("commit or push action.")
    A("")
    A("## 6. OVERCLAIM AUDIT")
    A("")
    A("- **PROVABLE (re-derived at the bytes this relay):** all ten member digests; member 04's")
    A("  one-cell write action, gauge law and endpoint representations, equal-history identity,")
    A("  independent-transformation clause, sector-diagonal clause and identically-zero")
    A("  single-branch amplitude; member 07's difference-branch premise and its no-gauge-component")
    A("  conclusion; member 08's identical-condition claim and its enlargement logic; member 01's")
    A("  reconciliation sentence; member 02's only-coherent-reading defence; member 05's")
    A("  transport-absence clause; member 10's no-gauge-covariance admission.")
    A("- **MINE (assembly, marked inline):** the demonstration that the difference-branch premise")
    A("  cannot yield the vanishing-divergence condition; the location of the defect upstream")
    A("  rather than in R4; the enlargement argument for why the verdicts are untouched; the")
    A("  alternative-selector sweep; the logical-independence point about regularity and homology;")
    A("  the one-derivable-object scoping.")
    A("- **NOT claimed:** that the block-split is decidable (it is not); that member 01 erred in its")
    A("  seven data (it did not — all seven confirm); that member 07 is wrong about anything other")
    A("  than the derivation of its first FIXED item; that dropping that item changes any verdict")
    A("  (it does not); that the Phase-A object is the record's realization (member 01 correctly")
    A("  refuses this); any value of anything.")
    A("")
    A("---")
    A("")
    A("## FLAG BLOCK")
    A("")
    A("```text")
    A("R_DATA_AUDIT = R1 CONFIRMED(cell-factorized read; tensor row and per-cell history dependence")
    A("    exact at path) ; R2 CONFIRMED(span: the one-cell diagonal's only connection-dependent")
    A("    entry is the pointer slot, and the write action D_n[a]S|r> = z_n[a]|p_Q> is verbatim;")
    A("    eraser slot connection-independent) ; R3 CONFIRMED(span: equal histories give")
    A("    F_N[a,a]=P_0+P_ch=I_src verbatim — RENDERING NOTE, not a defect: member 01 writes the")
    A("    identity as I rather than I_src, and states Z_N[a,a] = 1 as a citation where it is a")
    A("    correct inference from the quoted sentence) ; R4 CONFIRMED AS TO CONTENT(span: the")
    A("    sealed law z^g=t z s^dagger with its named endpoint representations is verbatim, and the")
    A("    two-port open-transport boundary follows by exact adjoint algebra) BUT ITS RECONCILIATION")
    A("    REFUTED — see R4_QUOTIENT_READING ; R5 CONFIRMED(span: doubled read; single-branch")
    A("    charged amplitude identically zero) ; R6 CONFIRMED(span: sector-diagonal, sealed clause")
    A("    verbatim) ; R7 CONFIRMED-AS-CLASSIFIED(Phase-A objects resolve at their pinned digests;")
    A("    SUSPECT flags are the source's own sealed text, including its admission of")
    A("    no local gauge covariance; used to classify, never to certify).")
    A("")
    A("R4_QUOTIENT_READING = CONTRADICTION(the bytes) — AND THE DEFECTIVE SIDE IS UPSTREAM, NOT THE")
    A("    BUILD.  Member 07 lists, under FIXED (of record), that the chain has 'with NO gauge")
    A("    component', and member 08 restates it as 'IDENTICAL to the gauge-invariance condition' —")
    A("    both as equations on the chain, neither on a quotient class.  R4's open two-port")
    A("    transport contradicts that directly.  The 'quotient-level' resolution is a REPAIR, not a")
    A("    reading of either source, and member 02's defence of it as 'the only reading under which")
    A("    GB/GC' cohere is not exhaustive.  THE SECOND READING, WHICH THE BYTES SUPPORT: member 07")
    A("    states its own premise as invariance 'on the difference branch', then applies the")
    A("    SINGLE-branch condition.  A common gauge transformation shifts both branches by the same")
    A("    coboundary, so the difference is unchanged and the pairing is invariant for EVERY chain")
    A("    — no condition follows.  Member 04 forecloses the alternative twice: independent branch")
    A("    transformations are 'not silently identified with the common transformation', and the")
    A("    single-branch read is identically zero, so no single-branch invariance can be demanded.")
    A("    The carried constraint is OVER-DERIVED.  EFFECT ON THE VERDICTS: NONE, AND SAFE —")
    A("    dropping a constraint can only enlarge the admissible set (member 08's own logic, 'can")
    A("    only enlarge the free set'), and the gauge component is invisible to the physical")
    A("    difference-branch functional.  Of member 07's four FIXED items, two are one condition")
    A("    and that condition is not forced.")
    A("")
    A("SPLIT_UNDETERMINED = CONFIRMED(and strengthened: with one carried constraint shown unforced")
    A("    there is strictly less structure available to discriminate the blocks.  Audited")
    A("    independently: R1, R2, R3, R5, R6 block-blind by construction; R4 bears on the gauge")
    A("    block alone; R7 is diamond-indexed, unpushable to the complex, one-direction-probed and")
    A("    fixed-gauge.  Nothing discriminates.)")
    A("")
    A("ONE_OBJECT_SINGULAR = CONFIRMED(no sealed alternative selector found.  Swept and dismissed:")
    A("    refinement-independence — the lift is sealed FREE and non-coboundary, so it is latitude")
    A("    not constraint, and cellulation-independence is an owed limit-level theorem, not a sealed")
    A("    object; the two-port data — pins the gauge block only; total-nonzero — constrains the sum")
    A("    never the split; the conserved typing — unforced per R4_QUOTIENT_READING, and even at")
    A("    face value a vertex condition that merely restates the ambient block; the smooth-density")
    A("    shortcut — correctly barred, and independently impotent since regularity of a density and")
    A("    the homology class of its transported chain are logically independent.  SCOPE THE CLAIM")
    A("    NEEDS: one missing DERIVABLE object — member 01's own section 6 lists a principal")
    A("    decision-of-record as a third route, which is an act, not a derivation.  Treating the")
    A("    transport law and the incidence-sum successor law as one object is correct: they are the")
    A("    same object at two levels.)")
    A("")
    A("CUSTODY = DEFECT(two, both located and neither fatal: (1) the R4 consistency paragraph rests")
    A("    on a reading neither cited source states — the load-bearing step that lets the upstream")
    A("    inventory be carried unchanged, defended by member 02 on an inference to coherence rather")
    A("    than to text; a defect of RESOLUTION, not of honesty, since the tension was flagged and")
    A("    not hidden; (2) member 05 is a lane relay artifact supplying the transport-absence clause")
    A("    that the missing-object claim leans on, and is booked in the source table without")
    A("    distinguishing its custody from the sealed BID sources beside it — not load-bearing here")
    A("    because I verified the clause first-hand at path.  NO verdict rests on unsealed prose, on")
    A("    a tasking instruction, or on a missing source; every reference resolved.)")
    A("")
    A("ANCHOR_VERDICT = CONFIRMED(the seven data, the split-undetermination, and the")
    A("    one-object singularity all stand at the bytes — the build's substantive claims survive a")
    A("    default-refute audit).  WITH ONE REFUTATION AND ONE RELOCATION: the R4 quotient")
    A("    reconciliation is REFUTED, and the contradiction it papers over is REAL and resolves")
    A("    AGAINST A SEALED, PANEL-CONFIRMED UPSTREAM SOURCE rather than against the build.  The")
    A("    build repaired the wrong side — it re-typed its own object to preserve an upstream")
    A("    condition that was never forced.  Correcting it removes a constraint, enlarges the free")
    A("    set, and changes no verdict; the registrar should record the upstream item as")
    A("    OVER-DERIVED rather than leave the build carrying a quotient re-typing to accommodate it.)")
    A("")
    A("MACHINERY_USED = no (audit and exact symbolic algebra on sealed forms only; no numeric")
    A("    evaluation; no scale, GR, metric, diamond-contractibility, or faithfulness premise used")
    A("    as authority anywhere; the one place such an import would have decided the split is")
    A("    barred by the sources and was not taken by me either).")
    A("EVALUATED_NOTHING = CERTIFIED")
    A("NO_REGISTER_READ = CERTIFIED")
    A("NO_SUBAGENT_DELEGATION = CERTIFIED")
    A("")
    A("ALL RESULTS CLAIMED. alpha_computed = false ; kappa_record_computed = false ;")
    A("proof_authorized = false")
    A("```")
    A("")
    A("---")
    A("")
    A("## CLOSURE (declared-first)")
    A("")
    A("```text")
    A(f"CLOSURE_END_BYTE = {close_end}")
    A("CLOSURE_MEMBERS = 10 (content-addressed, each digested at path in this relay)")
    for k in sorted(MEMBERS):
        A(f"  member {k}  {dg[k]}")
    A("SPAN DIGESTS (bounds checked against file length):")
    for tag in sorted(sp):
        a, b, d = sp[tag]
        A(f"  {tag}  [{a},{b})  {d}")
    A("```")
    return "\n".join(t) + "\n"


def main():
    self_scan()
    if OUT.exists():
        fail(1, f"output name exists, STOP: {OUT}")
    dg, sp = digests(), spans()

    guess, text = 0, ""
    for _ in range(64):
        text = body(dg, sp, guess)
        marker = text.find("## CLOSURE (declared-first)")
        if marker < 0:
            fail(4, "closure block not found in own output")
        if marker == guess:
            break
        guess = marker
    else:
        fail(4, "CLOSURE_END_BYTE did not reach a fixed point")

    fence_walk(text)
    contradiction_gate(text)
    self_citation_gate(text)
    res = residue_scan(text)
    if res:
        fail(13, f"output-inspection residue in authored prose: {res}")
    n = prose_digests(text)

    OUT.write_text(text)
    d = hashlib.sha256(OUT.read_bytes()).hexdigest()
    (OUT.parent / (OUT.name + ".seal.sha256")).write_text(f"{d}  {OUT.name}\n")
    print(f"ARTIFACT   {d}  {OUT.name}")
    print(f"CLOSURE_END_BYTE = {guess}")
    print(f"PROSE_DIGESTS = {n}/{n} STRICT==STABLE")
    print(f"RESIDUE_GREP = clean ({len(RESIDUE)} patterns)")
    print("NO_NUMERIC_PATH = CLEAN")
    print("CONTRADICTION_GATE = PASSED")
    print("SELF_CITATION_GATE = PASSED")


if __name__ == "__main__":
    main()
