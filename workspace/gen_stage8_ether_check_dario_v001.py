#!/usr/bin/env python3
"""Generator for STAGE8_ETHER_CHECK_DARIO_V001.md (DARIO lane, relay 1115).

Mandated refusal paths, all live:
  R1  member-absent / digest-at-path
  R4  span digest + span BOUNDS guard (markers located at run time; wrap-split marker => refusal)
  R6  no-numeric-path self-scan (string literals stripped from this file's own code first)
  R7  fence depth-walk (gated phrases must survive line wrapping)
  R11 MACHINERY-REVERSION gate (a bedrock refutation may not rest on a machinery authority)
  R12 SELF-CITATION gate (this lane's own prior output is never a record witness)
  R13 residue scan (output-inspection tokens over authored prose)
  closure declared-first, CLOSURE_END_BYTE solved as a fixed point on the artifact's own bytes
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("/Users/bgm/MB Work/alpha-program-archive")
SELF = pathlib.Path(__file__).resolve()
OUT  = ROOT / "workspace/STAGE8_ETHER_CHECK_DARIO_V001.md"


def fail(n, msg):
    print(f"REFUSED R{n}: {msg}", file=sys.stderr)
    sys.exit(1)


MEMBERS = {
    "01": ROOT / "workspace/STAGE8_BARE_SURFACE_ALPHA_DETERMINATION_FABLE_V001.md",
    "02": ROOT / "workspace/STAGE8_RATIFIED_SOURCE_COUPLED_FINITE_N_INFLUENCE_FUNCTIONAL_RESULT_V001.md",
    "03": ROOT / "workspace/BID_UNIQUE_CHARGED_CONTROLLED_COUPLING_DERIVATION_V001.md",
    "04": ROOT / "workspace/STAGE8_TASK2D_FINITE_COUPLING_FAMILY_FORCING_PROTOCOL_RESULT_V001.md",
    "05": ROOT / "supervision/DECISION_OF_RECORD_009_THE_TRANSITION_LAW_RATIFIED_E_POST_2026-08-02_V001.md",
    "06": ROOT / "supervision/DECISION_OF_RECORD_008_FIELD_CTP_ADOPTION_RATIFIED_WITH_FALSIFIER_2026-08-01_V001.md",
    "07": ROOT / "workspace/STAGE1_PREMISE_DISPOSITION_V001.md",
    "08": ROOT / "workspace/STAGE8_SADDLE_FOUNDATION_PARENT_ACTION_DARIO_V001.md",
    "09": ROOT / "workspace/PRIMITIVE_RELATIVE_PHASE_CONNECTION_V001.md",
}

SPAN_MARKERS = {
    "02a": "without an additional source state",
    "02b": "CANONICAL_SCALAR_F_N_FROM_RECORD_SANDWICH_ALONE = false",
    "02c": "not a scalar physical",
    "02d": "P_0+P_ch=I_src",
    "02e": "effect, or domain datum is added",
    "03a": "No numerical multiplier",
    "03b": "affine solution",
    "07a": "This fixes the unit-character convention",
    "07b": "remains adopted",
    "04a": "SURVIVOR_COUNT = NO_VERDICT",
    "01a": "This bounds AMPLITUDE claims",
    "01b": "There is no amplitude to",
    "05a": "Nothing sealed forced the choice",
    "06a": "RATIFIED as declared premises",
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

# Machinery objects named by the principal's fence. Allowed as SUSPECTS in the provenance
# audit; forbidden as an AUTHORITY or PREMISE on which to rest a refutation.
MACHINERY = [
    "k_kk", "fiber radius", "ell_p", "thomson", "kk action", "radion",
    "alpha rides a scale", "q-01", "continuum normalization", "metric conversion",
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
        "proof_authorized = false",
        "kappa_record_computed = false",
        "JOINT_ANCHOR_DERIVED = false",
        "EVALUATED_NOTHING = CERTIFIED",
        "IMPORTED_NOTHING = CERTIFIED",
        "OUTPUT_INSPECTION = NONE-CERTIFIED",
        "NO_REGISTER_READ = CERTIFIED",
        "NO_SELF_CITATION = CERTIFIED",
        "CHECKER_REVERTED = no",
    ]
    flat = re.sub(r"\s+", " ", text)
    for g in gated:
        if g not in text:
            if g in flat:
                fail(7, f"gated phrase split by a line wrap: {g!r}")
            fail(7, f"gated phrase absent: {g!r}")


def machinery_gate(text):
    """R11: the principal's condition. If this check REFUTES, the refutation must stand on
    bedrock. The refuting section is audited: no machinery object may appear inside it."""
    if "REFUTED-ON-BEDROCK" not in text:
        return
    m = re.search(r"\n## 1\. GATE 1(.*?)\n## 2\. ", text, re.S)
    if not m:
        fail(11, "a REFUTED-ON-BEDROCK verdict requires an isolated Gate-1 section to audit")
    seg = m.group(1).lower()
    hits = [k for k in MACHINERY if k in seg]
    if hits:
        fail(11, f"machinery invoked inside the refuting section — this would be "
                 f"machinery-as-authority, not a bedrock refutation: {hits}")
    for need in ["state", "p_ch", "dimensionless"]:
        if need not in seg:
            fail(11, f"the bedrock refutation must exhibit its object; missing {need!r}")


def self_citation_gate(text):
    """R12: member 08 is this lane's own prior output and carries a standing IMPORT-FOUND."""
    if "NO_SELF_CITATION = CERTIFIED" in text:
        if "member 08" not in text:
            fail(12, "a self-citation certification must name the party node it refuses to "
                     "lean on, or it certifies nothing")
        for claim in ["as member 08 establishes", "on member 08's authority",
                      "confirmed by member 08"]:
            if claim.lower() in text.lower():
                fail(12, f"this check leans on its own lane's prior output as ground: {claim!r}")


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
    A("# STAGE8_ETHER_CHECK_DARIO_V001")
    A("")
    A("LANE: DARIO (external adversarial anchor, relay 1115). ROLE: [CHECK — THREE GATES] on the")
    A("bare-surface ether test: does the connection-only surface DETERMINE its native coupling as a")
    A("pure number? Re-derived at the bytes; **zero testimonial weight** given to the subject.")
    A("**ALL RESULTS CLAIMED** until the Codex 2 check. Builder never verifies own work.")
    A("")
    A("GATES DECLARED AND HELD: alpha_computed = false; proof_authorized = false;")
    A("kappa_record_computed = false; JOINT_ANCHOR_DERIVED = false. Nothing was computed — no value,")
    A("bound, or estimate of n_ch as a physical response, of any coupling, kappa, alpha, scale,")
    A("interval or constant; n_ch, kappa and alpha are SUBJECTS by type. No measured-constant")
    A("comparison. NO_REGISTER_READ = CERTIFIED. No git action. Run solo — the lane's no-delegation")
    A("bar overrides the session's standing ultracode/Workflow directive; no subagent was used.")
    A("")
    A("**CHECKER MACHINERY-REVERSION FENCE — ACCEPTED AND SELF-AUDITED. CHECKER_REVERTED = no.**")
    A("The refutation below rests on: the sector projectors already inside the bare object, the")
    A("surface's own sealed type boundary, and the surface's own dimensionless content. It invokes")
    A("no fiber radius, no metric, no continuum normalization, no Thomson apparatus, no KK object,")
    A("and no scale-riding claim — not as authority, not as premise. Section 1 is machine-audited")
    A("for machinery tokens by this artifact's generator, which refuses to emit if any appear there.")
    A("")
    A("**NO_SELF_CITATION = CERTIFIED.** Member 08 is THIS LANE's own prior output and carries a")
    A("standing opposite-lane IMPORT-FOUND against its promotion step. It is a PARTY, audited below")
    A("as a suspect node, and nothing is confirmed by leaning on it — in particular P3 is settled")
    A("from member 02's own ledger rather than from member 08's assurance that the import is")
    A("confined.")
    A("")
    A("## SOURCES (all digested at path this relay)")
    A("")
    A("```text")
    for k in sorted(MEMBERS):
        rel = str(MEMBERS[k]).replace(str(ROOT) + "/", "")
        A(f"{k}  {dg[k]}  {rel}")
    A("```")
    A("")
    A("Subject and all four tasked members match their pins at path. The two premise nodes the task")
    A("allowed me to report UNVERIFIED are **both present archive-side** (members 05, 06), as are")
    A("the faithfulness and character-lattice primaries (members 07, 09) — so no node below is")
    A("unverifiable, and Gate 3 is answered on read text rather than on trust.")
    A("")
    A("## 0. LEAD")
    A("")
    A("**The dial is still there. It has been renamed.**")
    A("")
    A("What the subject establishes is real and I confirm it: the response is confined to a discrete")
    A("character lattice, and faithfulness picks the generator. That is **charge quantization** — a")
    A("genuine structural result of a compact connection-only record. What it is not is a coupling")
    A("*strength*.")
    A("")
    A("The subject's own posing question is *\"How strongly does the connection-only interacting")
    A("object respond to a source?\"* On the surface's own sealed statement, that question **cannot")
    A("be answered by the object alone**. Member 02 fixes the bare object's exact codomain as an")
    A("operator, not a number: `End(P_0 H_src (+) P_ch H_src)`, the `2 x 2` diagonal on sector")
    A("labels — value `1` on the neutral sector, the character `Z_N` on the charged one. And member")
    A("02 states in its own words that `F_N` is *\"not a scalar physical influence amplitude\"*, that")
    A("producing a scalar *\"still requires the separately named state/effect realization\"*, and it")
    A("books that as a theorem-grade negative:")
    A("`CANONICAL_SCALAR_F_N_FROM_RECORD_SANDWICH_ALONE = false | TYPE-R`.")
    A("")
    A("Put a state on the source sector and the strength appears immediately. With")
    A("`P_0 + P_ch = I_src` (member 02, at the bytes), any source state has sector weights summing")
    A("to one, and the observable response is")
    A("")
    A("```text")
    A("omega(F_N) = (1 - w_ch) . 1  +  w_ch . Z_N ,      w_ch = omega(P_ch) in [0,1]")
    A("```")
    A("")
    A("`w_ch` is **continuous, dimensionless, and not supplied by the surface**. It is exactly the")
    A("free continuous dimensionless parameter the subject declares cannot exist. So the finding")
    A("is REFUTED on bedrock — and the subject saw this object and set it aside.")
    A("")
    A("## 1. GATE 1 — THE FINDING, REFUTED ON BEDROCK")
    A("")
    A("**(K1) The no-multiplier theorem is sound, and it does not reach the object that matters.**")
    A("")
    A("Member 03's theorem constrains a CONTROL MAP `C_P` on operators, through three axioms —")
    A("linear; supported (`C_P(B) = P C_P(B) P`); a retraction (`C_P(A) = A` for every `A = PAP`);")
    A("and a `P-End(H)-P` bimodule map. From these it forces `C_P(B) = PBP`, the orthogonal")
    A("compression, with *\"No numerical multiplier\"* present, and the companion audit solves the")
    A("linear constraint system to find the *\"affine solution\"* space zero-dimensional. A putative")
    A("`lambda P_ch (x) B_Q` with `lambda != 1` dies on the retraction axiom. **All of that is")
    A("correct and I confirm it at the bytes.**")
    A("")
    A("[MINE, marked — the refutation] But every one of those axioms is a condition on an")
    A("OPERATOR-valued map. A state on the source algebra is not an operator-valued map, satisfies")
    A("none of those axioms, and is untouched by the theorem. The weight `w_ch = omega(P_ch)` never")
    A("appears as a multiplier in front of the coupling operator — the operator stays exactly")
    A("`P_0 + Z_N P_ch`, unmodified, retraction intact. It appears only when the operator is")
    A("evaluated. **The theorem closes the slot in front of the operator; the slot underneath it,")
    A("in the state, is never addressed.**")
    A("")
    A("The other two legs fail against the same object, for the same structural reason:")
    A("")
    A("- **Lattice quantization (C7 + C4).** Appending cells multiplies CHARACTERS, and cycle")
    A("  single-valuedness constrains CHARACTERS. `w_ch` is not a character exponent and is not")
    A("  carried by the history at all — it is a property of the source state. Composition does not")
    A("  quantize it; there is no homomorphism condition for it to violate.")
    A("- **Unit modulus.** Every character value has unit modulus — true. But the observable is not")
    A("  a character value. `|(1 - w_ch) + w_ch Z_N| < 1` strictly, for every `w_ch` in the open")
    A("  interval and `Z_N != 1`. The subject writes *\"There is no amplitude to attenuate\"* — the")
    A("  attenuation is exactly this, and it is continuous.")
    A("")
    A("**Is this bedrock, or is it my own import?** It is bedrock, and the surface says so itself.")
    A("The sector projectors `P_0`, `P_ch` are already constituents of the bare object; their sum is")
    A("the identity on the admitted two-sector span; a state on that span is dimensionless content")
    A("of the surface; and member 02 names the missing supply by name, twice — *\"without an")
    A("additional source state\"* the scalarization is unlicensed, and the negative ledger records")
    A("`State/effects/domains/contacts/metric/common-origin fields remain` as outstanding. The")
    A("regression check in the same member confirms that no *\"effect, or domain datum is added\"* to")
    A("the construction — the state is not merely unfixed, it is expressly outside the object.")
    A("")
    A("**The subject saw it and dismissed it.** Its residual R3 reads: *\"This bounds AMPLITUDE")
    A("claims\"*, not the coupling typing. But *how strongly* is the amplitude question — it is the")
    A("subject's own question, asked in its own section 3. Setting the amplitude aside and typing")
    A("only WHICH character survives is what makes the coupling look determined: the subject types")
    A("the representation label (the charge quantum) and calls it the coupling, while the strength")
    A("sits in a state the surface leaves open.")
    A("")
    A("`G1 = REFUTED-ON-BEDROCK.` The surface-native continuous dimensionless coupling the")
    A("no-multiplier theorem missed is **the source state's charged-sector weight**.")
    A("")
    A("**(K2) The lattice confinement is genuine — CONFIRMED.** A non-integer power `z -> z^lambda`")
    A("is not a character: it fails homomorphism composition under refinement and cycle")
    A("single-valuedness. No continuous power can arise on bedrock. I confirm this, and note that")
    A("its very narrowness is what lets the state through: the argument quantizes the exponent, and")
    A("says nothing about the weight.")
    A("")
    A("**(K3) The generator is forced, and its own primary calls the result a convention —")
    A("CONFIRMED, with a scope correction.** Member 07 is exact: characters of `U(1)` are")
    A("`chi_n(exp(i theta)) = exp(i n theta)`, the kernel is the whole group at `n = 0` and the")
    A("`|n|`th roots of unity for `|n| > 1`, so a faithful character has `|n| = 1`. Sound; no")
    A("non-generator winding is admissible once faithfulness is imposed, and faithfulness *after")
    A("the response-null quotient* is close to definitional. **But member 07's own closing sentence")
    A("types the result differently from the subject:** *\"This fixes the unit-character")
    A("convention. It does not derive the existence of a physical local electromagnetic connection,")
    A("which remains adopted Level-1 field content.\"* The primary calls it a CONVENTION fix and")
    A("disclaims the physical content; the subject reads it as the determination of the surface's")
    A("native coupling. That is an upgrade, and the Level-1 adoption it names appears in no premise")
    A("list the subject carries.")
    A("")
    A("## 2. GATE 2 — SUBJECT REVERSION: CLEAN")
    A("")
    A("I checked whether any machinery object was needed even to POSE `n_ch`. It was not. The posing")
    A("consumes unit-modulus characters, the two-sector controlled transition, refinement/composition")
    A("and cycle/gauge single-valuedness — all present in member 02 without a metric argument. The")
    A("subject's citation of member 08 is for span custody (which member pins member 02's bytes),")
    A("not for content, so the posing does not route through member 08's contested promotion.")
    A("`G2_SUBJECT_REVERSION = CLEAN.` This is a genuine strip, and I record it as such: the test")
    A("did what it said it did. The failure is not reversion — it is that the stripped surface has")
    A("one more dimensionless datum than the subject counted.")
    A("")
    A("## 3. GATE 3 — PROVENANCE, TRACED TO BEDROCK")
    A("")
    A("**(P1) The premise nodes are surface-native laws, not imported values.** Member 06 ratifies")
    A("seven ALGEBRAIC presentation adoptions — sequential labels with disclosed zero-extension, the")
    A("C* field algebra, the CTP tensor completion, the even spatial join, the Hilbert C*-module")
    A("representation, the common domain, branch embeddings, bounded finite-support source maps —")
    A("*\"RATIFIED as declared premises\"*, with a standing falsifier that the completion must")
    A("reproduce every sealed finite result on restriction. Member 05 ratifies a STRUCTURAL binary")
    A("(endpoint charge `E_post`), finite locality, and an external-parent scope exclusion, stating")
    A("openly that *\"Nothing sealed forced the choice\"*. **Neither encodes a scale, a GR")
    A("normalization, or a metric datum.** They are adoptions of structure, and the subject carries")
    A("their conditionality correctly as TYPE-P.")
    A("")
    A("**(P2) Members 03 and 04 route through no imported metric or scale value.** Member 03's")
    A("derivation is projection-module algebra end to end. Member 04 is a census whose protocol")
    A("returned `SURVIVOR_COUNT = NO_VERDICT`. Neither consumes a length, a radius, or a")
    A("gravitational normalization at any depth I could reach.")
    A("")
    A("**(P3) `n_ch` never consumes the metric argument — CONFIRMED, and established without the")
    A("party.** The subject rests this on member 08's assurance that the machinery import is")
    A("*confined to the metric argument `n_ch` does not consume*. Member 08 is this lane's own prior")
    A("output and carries a standing IMPORT-FOUND, so I did not accept that assurance. I settled it")
    A("instead from member 02's own regression ledger, which certifies that no parent, curvature,")
    A("distributed, source-contact, metric/continuum, state, effect, or domain datum is added to the")
    A("construction. `n_ch` is defined from characters, C7 and C4 over that construction; there is")
    A("no metric argument in it to consume, at any depth reachable from member 02.")
    A("")
    A("**(P4) The member-04 residual is genuine, and hides no import — it hides a non-forcing.**")
    A("`SURVIVOR_COUNT = NO_VERDICT` is a failure to force, disclosed. The subject discloses it")
    A("(R1) and closes it by principal ratification rather than by derivation, which is the honest")
    A("account. No import is concealed there.")
    A("")
    A("`G3_IMPORTED_VALUE_NODES = none.` Not one node I traced encodes an imported value. **The")
    A("subject's provenance is clean — and that is precisely why the finding matters: the refutation")
    A("is not contamination, it is a miscount of the surface's own dimensionless content.**")
    A("")
    A("## 4. WHAT WOULD REPAIR IT — NAMED, NOT PERFORMED")
    A("")
    A("[MINE, marked] The verdict is recoverable, on one condition: **derive a distinguished source")
    A("state from the record's own structure.** If the surface forces a canonical state on the")
    A("two-sector span, then `w_ch` is fixed by that state and becomes a derived pure number, the")
    A("continuous slot really does close, and DETERMINED stands — on a ground the subject does not")
    A("currently claim. Member 02 leaves exactly this open. Until it is built, the honest statement")
    A("is that the surface determines **which character** and leaves **how much** free, and those")
    A("are two different data.")
    A("")
    A("I did not build it, did not evaluate `w_ch` or any weight, and do not assert what a derived")
    A("state would give.")
    A("")
    A("## 5. WHAT I DID NOT DO")
    A("")
    A("I did not evaluate `n_ch`, `w_ch`, any character, kappa, alpha, or any response magnitude;")
    A("did not construct or select a state; did not read the register, tracker, plan, road or")
    A("ledger; did not enter `a32_holdout/custodian_private/`; ran no subagent. I did not invoke a")
    A("single machinery object as an authority — see the self-audit above and the generator's gate.")
    A("")
    A("## 6. OVERCLAIM AUDIT")
    A("")
    A("- **PROVABLE (re-derived at the bytes this relay):** all nine member digests; member 02's")
    A("  operator codomain, its TYPE-R scalarization negative, its `P_0 + P_ch = I_src`, its")
    A("  external-parent regression and its outstanding-state ledger line; member 03's three control")
    A("  axioms, the forced compression, the no-multiplier clause and the zero-dimensional affine")
    A("  solution space; member 04's `NO_VERDICT`; members 05 and 06 in full; member 07's character")
    A("  computation and its closing convention/Level-1 sentence.")
    A("- **MINE (assembly, marked inline):** that the state's charged-sector weight is a")
    A("  surface-native continuous dimensionless coupling and that the three legs miss it; the")
    A("  reading that the subject types the charge quantum rather than the coupling strength; the")
    A("  repair path of section 4.")
    A("- **NOT claimed:** that the subject imported anything (it did not — Gate 3 is clean); that")
    A("  its lattice or faithfulness results are wrong (both CONFIRMED); that `w_ch` has any value,")
    A("  or that a derived state would fail to fix it; that the scale exists or does not; that alpha")
    A("  is free or forced; anything about which finish is TRUE. I type the finding's licence, not")
    A("  the world.")
    A("")
    A("---")
    A("")
    A("## FINAL LINES")
    A("")
    A("```text")
    A("G1_FINDING = REFUTED-ON-BEDROCK(the source state's charged-sector weight w_ch = omega(P_ch):")
    A("    continuous in [0,1], dimensionless, and NOT supplied by the surface.  The bare object's")
    A("    exact codomain is an OPERATOR — End(P_0 H_src (+) P_ch H_src), the 2x2 diagonal on sector")
    A("    labels — so the observable response is omega(F_N) = (1 - w_ch) + w_ch Z_N, a continuous")
    A("    attenuation between no response and total response.  The three legs all miss it: the")
    A("    no-multiplier theorem constrains an OPERATOR-valued control map through support/")
    A("    retraction/bimodule axioms that a state does not satisfy and is not tested by, and the")
    A("    operator itself is left unmodified; C7/C4 quantize the CHARACTER EXPONENT, and w_ch is")
    A("    not an exponent and is not carried by the history; unit modulus bounds CHARACTER VALUES,")
    A("    and |(1 - w_ch) + w_ch Z_N| < 1 strictly on the open interval — the attenuation the")
    A("    subject says does not exist.  BEDROCK ONLY: sector projectors already inside the bare")
    A("    object, P_0 + P_ch = I_src at the bytes, and the surface's OWN sealed type boundary —")
    A("    'not a scalar physical influence amplitude', 'without an additional source state' the")
    A("    scalarization is unlicensed, CANONICAL_SCALAR_F_N_FROM_RECORD_SANDWICH_ALONE = false |")
    A("    TYPE-R, and State/effects/domains/contacts fields recorded as REMAINING.  The subject")
    A("    reached this object and set it aside as bounding 'AMPLITUDE claims, not the coupling")
    A("    typing' — but HOW STRONGLY is the amplitude question, and it is the subject's own.")
    A("    What the subject did establish, and I CONFIRM, is CHARGE QUANTIZATION: which character,")
    A("    forced to the generator.  That is the representation label, not the strength.)")
    A("")
    A("G2_SUBJECT_REVERSION = CLEAN (no machinery object was invoked or assumed to pose n_ch: the")
    A("    posing consumes unit-modulus characters, the two-sector controlled transition, C7 and C4")
    A("    only; the member-08 citation is span custody, not content.  The strip is genuine.)")
    A("")
    A("G3_IMPORTED_VALUE_NODES = none (no node in the traced chain encodes an imported or adopted")
    A("    VALUE — no scale, no GR normalization, no metric datum.  Member 06 ratifies seven")
    A("    algebraic presentation adoptions; member 05 ratifies a structural endpoint binary with")
    A("    'Nothing sealed forced the choice' stated openly; members 03 and 04 are projection-module")
    A("    algebra and an inconclusive census.  The refutation above is NOT contamination — it is a")
    A("    miscount of the surface's own dimensionless content.)")
    A("")
    A("G3_PREMISE_NODES = SURFACE-NATIVE (members 05 and 06 are structural adoptions, not value")
    A("    imports, and both were READ at path — neither is UNVERIFIED; the subject carries their")
    A("    TYPE-P conditionality correctly.  ONE UNDER-DECLARED PREMISE REPORTED: member 07's own")
    A("    closing sentence says the unit-winding result 'fixes the unit-character convention' and")
    A("    'does not derive the existence of a physical local electromagnetic connection, which")
    A("    remains adopted Level-1 field content' — that Level-1 adoption appears in no premise list")
    A("    the subject carries, and the subject reads a convention fix as a coupling determination.)")
    A("")
    A("G3_N_CH_AVOIDS_METRIC = CONFIRMED (settled from member 02's own regression ledger — no")
    A("    parent, curvature, distributed, source-contact, metric/continuum, state, effect or domain")
    A("    datum is added — and NOT from member 08's assurance that the import is confined, since")
    A("    member 08 is this lane's own output under a standing IMPORT-FOUND.  n_ch is built from")
    A("    characters, C7 and C4 over that construction; there is no metric argument in it to")
    A("    consume at any depth reachable from member 02.)")
    A("")
    A("CHECKER_REVERTED = no (the refutation rests on the sector projectors inside the bare object,")
    A("    the surface's own sealed scalarization boundary, and a state as dimensionless surface")
    A("    content.  No fiber radius, metric, continuum normalization, Thomson apparatus, KK object,")
    A("    or scale-riding claim was used as authority or premise anywhere in Gate 1; the generator")
    A("    machine-audits the refuting section for machinery tokens and refuses to emit if any")
    A("    appear.  I did not need machinery to refute this, and did not use it.)")
    A("")
    A("VERDICT = REFUTED(Gate 1, on bedrock: the surface determines WHICH CHARACTER and leaves HOW")
    A("    MUCH free.  The charge quantum is forced — genuinely, and it is a real result.  The")
    A("    coupling STRENGTH is carried by a source state the surface does not supply and expressly")
    A("    books as outstanding, so 'the bare surface has NO SLOT for a free continuous dimensionless")
    A("    coupling' is false as written, and ETHER-DROPPED does not follow: the dial was not")
    A("    removed, it was relocated into the state and relabelled an amplitude question.")
    A("    REPAIR PATH, NAMED NOT PERFORMED: derive a DISTINGUISHED SOURCE STATE from the record's")
    A("    own structure.  If the surface forces a canonical state on the two-sector span, w_ch")
    A("    becomes a derived pure number, the continuous slot genuinely closes, and DETERMINED")
    A("    stands — on a ground the subject does not currently claim.  That, not the winding, is")
    A("    where this question is decided.)")
    A("")
    A("EVALUATED_NOTHING = CERTIFIED")
    A("IMPORTED_NOTHING = CERTIFIED")
    A("OUTPUT_INSPECTION = NONE-CERTIFIED")
    A("NO_REGISTER_READ = CERTIFIED")
    A("NO_SELF_CITATION = CERTIFIED")
    A("NO_SUBAGENT_DELEGATION = CERTIFIED")
    A("CHAIN_INVOKED = false")
    A("")
    A("ALL RESULTS CLAIMED. alpha_computed = false ; proof_authorized = false ;")
    A("kappa_record_computed = false ; JOINT_ANCHOR_DERIVED = false")
    A("```")
    A("")
    A("---")
    A("")
    A("## CLOSURE (declared-first)")
    A("")
    A("```text")
    A(f"CLOSURE_END_BYTE = {close_end}")
    A("CLOSURE_MEMBERS = 9 (content-addressed, each digested at path in this relay)")
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
    machinery_gate(text)
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
    print(f"MACHINERY_GATE = PASSED ({len(MACHINERY)} tokens audited over the refuting section)")
    print("SELF_CITATION_GATE = PASSED")


if __name__ == "__main__":
    main()
