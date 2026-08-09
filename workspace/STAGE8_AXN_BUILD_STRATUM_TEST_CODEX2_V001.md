# STAGE 8 / AXN-BUILD-A3 — S_rot/S_BF STRATUM TEST
## CODEX 2 LANE — V001

Relay 836. `PICKUP-ACK` and lane guard passed: the sealed inbox names
CODEX 2. `ALL HEADLINE ITEMS ARE CLAIMED.`

## 0. Custody, jurisdiction, and gates

The unique relay file
`relay_inbox/RELAY_PASTE_836_STRATUM_TEST_CODEX2_V001.md` verified against
its adjacent sidecar before its body was read:

```text
SHA-256 = 2e83a680ff9b606f70c6affc1dc38a86c1e5b033c2cd58674e384ba87fb69259
```

`relay_outbox/836_ACK.md` was written before task work. The required state
brief `PROGRAM_STATE_BRIEF_V005.md` verified and was read first:

```text
SHA-256 = e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c
```

The governing cross-check and source chain verified before use:

| ID | Source | SHA-256 | Exact span used |
|---|---|---|---|
| X833 | `STAGE8_AXN_BUILD_SKELETON_CROSSCHECK_DARIO_V001.md` | `3069554eb280062b9213914b5ec3113a1148138292b79b0bc0a46484d2868534` | lines 24–58, bytes `[1271,3483)`, span SHA `38a809590528ad06375170a499a364d8f8f242b9eacacc629aa286d1aee5ca58` |
| ERR | `STAGE8_ACTION_COMPLETION_COUNT_ERRATUM_V001.md` | `ee2d9490c4759078c6cc2f307dd62ea09f6fc4ce0893052a4b6e2c6627b3801e` | lines 37–78, bytes `[929,2386)`, span SHA `3d66449e0549be84f9180930474456f3206a6683d2909594154374074cf3a96b` |
| EXH | cleanroom-v001 `ACTION_CARRIER_CLASSIFICATION.md` | `b3f96a02b1b70ed3e1950cc025f795400a7c4880edd4fa5cd866e743ddbc64ac` | lines 79–113, bytes `[2379,3578)`, span SHA `2954f3a0d178f78bf4ff558fa2588cc0c7a7520f29f40f5831d24bcd28998d24` |
| A05 | `COMPLETE_PARENT_ACTION_UNDERDETERMINATION_GATE_V001.md` | `67816cfeec8d61e4bcafec90c6c8a10fa239f91355c95f424b75621f6e2f3bd6` | lines 9–59, bytes `[221,1461)`, span SHA `a2dee1cf1e912f24cf394b077e14b3a0e90e18c4f18d54fa83379217e418fc9f` |
| SKEL | `STAGE8_AXN_BUILD_SKELETON_CODEX2_V001.md` | `5a51b94039bc4a9e078e4f11cc8b74b05973d1b8e547e78fd1f4728d586af76c` | lines 93–142, bytes `[6964,10505)`, span SHA `9b92dacbd93a51a998afef6c871a35ca30664ae1ffccc9cec467cb36487b38bd` |
| CHARTER | `AXN_BUILD_CHARTER_V001.md` | `c0ad6decf156ef06c34bc8886d433487dfdf518c650dd67d5de283febeb14542` | lines 12–30, bytes `[547,1799)`, span SHA `aac1bec13c5b91cbcac57247be4ea1155b48062230c72ac7370bbce57fa80e31` |

Law 8 was applied without pretending a nonexistent sidecar exists. `EXH` has
no adjacent sidecar in either spelling and is not a packet-manifest member.
Its exact whole-file bytes nevertheless match the path and SHA-256 incorporated
by the adjacent-sealed `ERR`, which identifies lines 79–113 as the two
direct-ancestor exhibits. This report consumes only that content-addressed
incorporated span. The custody mode is stated explicitly rather than renamed
as an adjacent seal.

The output name and both sidecar spellings were absent before writing. The
current decline register `DECLINE_REGISTER_V002.md` verified at
`957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a`;
all S01–S37 rows were walked in §6.

Gates declared and held:

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
member_bound = false
fixed_point_executed = false
end_test_run = false
physical_quantity_numerically_evaluated = false
measured_constant_compared = false
smooth_import = false
EM_identification = false
```

PE-1 through PE-11 remained pointer-only: unopened, unconsulted, and assigned
zero verdict weight. No register, plan, tracker, git, production, response, or
chain action was taken.

## 1. Law-9 exhibit census

### 1.1 Two enumerations, not one completeness claim

`A05` displays the two source-record parent controls:

```text
S_0
  = integral d^4x sqrt(-g)
      i hbar bar(psi) gamma^mu D_mu psi
    + S_record[R,a,g],

S_1
  = S_0
    + hbar ell_*
      integral d^4x sqrt(-g)
        bar(psi) sigma^(mu nu) psi F_(mu nu).
```

`ERR` supplies the sibling enumeration the original two-member count missed.
It content-addresses `EXH` and corrects the displayed completion census to the
lower bound

```text
S_0, S_1, S_rot, S_BF.
```

The two additional displays are:

```text
S_rot/hbar
  = (1/(2 l_P)) integral_Sigma sqrt(|h|)
      h^(ab)(partial_a theta-A_a)(partial_b theta-A_b) d^3y,

S_BF/hbar
  = (1/(2 pi)) integral_Sigma b wedge (d a-pullback(F)).
```

`EXH` calls these parameter-free boundary theories and countermodels to
uniqueness, not proposed physical actions. `ERR`, later and sealed, counts
them as two additional direct-ancestor completions in the exhibited
parent-action lower bound. Both statements are retained: they belong to the
governing displayed exhibit, while their survival under the later packet-parent
binding predicate remains untested.

Law 9 stops the census at exactly its authority:

```text
DISPLAYED_EXHIBIT = {S_0,S_1,S_rot,S_BF}
DISPLAYED_COUNT = 4
COMPLETE_ACTION_FAMILY_ENUMERATED = false
NO_OUTSIDE_PROOF = absent
LAWFUL CLAIM = at least four, never exactly four
```

No fifth member is inferred and none of the four is selected.

## 2. The attack, executed

### 2.1 Presence table

The receiving predicate is exact syntactic occurrence of the T01 additive
term

```text
S_D = integral d^4x sqrt(-g)
        i hbar bar(psi) gamma^mu D_mu psi.
```

| Displayed member | `S_D` present? | Byte evidence | Classification voice |
|---|---:|---|---|
| `S_0` | YES | `A05` displays `S_D + S_record[R,a,g]` | source-record parent control |
| `S_1` | YES | `A05` displays `S_1=S_0+Pauli` | source-record parent control |
| `S_rot` | **NO** | `EXH` lines 84–96, bytes `[2558,2990)`, span SHA `c990980a3b7da5a5cab44005735e6b266b79ea29d19faf11621c266484dc5a69`; its complete display is the compact phase boundary action above | boundary-record countermodel |
| `S_BF` | **NO** | `EXH` lines 98–113, bytes `[2991,3578)`, span SHA `bc29aad4c6c56fa53c6ad76a620345e92cb5d14db3a3c38c24f51d6901caabab`; its complete display is the BF boundary action above | boundary-record countermodel |

The two negative rows are not absence-by-summary. Across each complete
display, the exact source tokens `psi`, `bar(psi)`, `gamma`, `D_mu`, `Dirac`,
and `d^4x` occur zero times. More importantly, the displayed integrands are
whole and are different typed objects on `Sigma`; neither contains `S_0` by
reference.

### 2.2 Intersections

Let `Terms(S)` denote the displayed additive terms of a member, without
identifying distinct operators by shared words such as “compact” or
“connection.” Then

```text
S_D in Terms(S_0) intersection Terms(S_1),

S_D notin Terms(S_rot),
S_D notin Terms(S_BF),

S_D notin intersection_(S in {S_0,S_1,S_rot,S_BF}) Terms(S).
```

Indeed, no exact additive action term is common to all four displayed
members. The broad lower-bound exhibit therefore has an empty exact term
intersection at the level shown.

This defeats a widening of T01 to the displayed four-member exhibit. It does
not make the original byte statement false: `S_0` and `S_1` still share
`S_D` exactly. The correct trichotomy outcome is therefore:

```text
T01 = NARROWED.
```

The scope is exactly the exhibited source-parent pair

```text
E_D := {S_0,S_1},
```

not the action exhibit

```text
E_4 := {S_0,S_1,S_rot,S_BF},
```

and not the unenumerated complete family. `S_rot` and `S_BF` are the displayed
members that prevent widening.

## 3. Consequence for the skeleton row

The skeleton's prose already says “on the displayed `S_0/S_1` source-sector
stratum” and warns that it proves no universality over `S_rot/S_BF`. That
scope disclosure was correct. The word `FORCED`, however, is too strong for
a census row that downstream work may read at family scope.

The exact replacement reading is:

```text
T01 | first-order Dirac source term S_D
    | COMMON-ON-EXHIBITED-SOURCE-PAIR / NOT FAMILY-FORCED
    | S_D is the exact intersection of S_0 and S_1;
      S_rot and S_BF omit it; no-outside proof absent.
```

No edit to the sealed skeleton is made here. This report supplies the
governing correction for its consumer: keep the formula and the two-member
intersection proof, remove T01 from any count of terms forced over the
displayed action family.

Thus the family-scope term ledger reads

```text
FORCED_TERMS_OVER_E_4 = 0
PAIR_COMMON_TERMS_OVER_E_D includes S_D
```

The result is `NARROWED`, not an absolute refutation of `S_D`: the packet
parent itself requires one shared charged source. The later
`BIND_PACKET_PARENT` test may exclude the two boundary-only countermodels or
may require a larger action containing them as record sectors. That test has
not run, and neither outcome is assumed.

## 4. Closure-round starting point

The hole-closure round may not begin with `S_D` as a universally forced
action-family term. It begins with a typed split:

```text
SOURCE-PARENT SUB-STRATUM E_D:
  S_D is common; Pauli/source mutations and the other holes remain.

BROADER DISPLAYED EXHIBIT E_4:
  no common exact additive term is displayed.

FIRST PRESSURE TEST:
  apply the packet-parent binding predicate and the corrected descendant/
  falsifier interface to every admitted candidate; derive, do not assume,
  whether S_rot/S_BF are excluded, embedded as record sectors, or survive.
```

If the binding predicate derives that every surviving complete action must
contain the shared Dirac source term, T01 can later be promoted by that
theorem. Today it is only a pair-common starting datum. Conversely, if a
lawful packet-binding completion without `S_D` survives, the future theorem
candidate is refuted. The present test chooses neither branch.

This shifts the closure round's initial pressure from “close five holes around
one forced term” to “first derive the admissible parent-binding stratum, then
close the holes inside it.” Dario's `BOX_gravity` finding and the three
premise/adoption-absence label corrections remain governing adjacent items;
this bounded relay neither edits nor relitigates them.

## 5. FREEDOMS-CONSUMED

```text
CARRIED, NOT SELECTED:
  S_0 and S_1                    displayed source-parent controls
  S_rot and S_BF                displayed boundary-record countermodels
  E_D and E_4                    audit sets defined from sealed displays only
  BIND_PACKET_PARENT             future pressure test; not executed here
  the unenumerated action family open beyond the four-member lower bound

STRUCTURALLY DETERMINED HERE:
  the four-row T01 presence table
  intersection over E_D contains S_D
  intersection over E_4 does not contain S_D
  exact T01 scope = E_D only

NOT SELECTED OR ADOPTED:
  no action member or stratum as the physical one
  no embedding of S_rot/S_BF into a larger action
  no exclusion of S_rot/S_BF from the packet-parent receiver
  no minimality, equal-action, or response-based selector
  no coefficient, scale, topology, support, or environment completion
  no smooth carrier or electromagnetic identification

SCALING WEIGHTS CONSUMED = none
SUBSTITUTED = none
```

## 6. FLATTENING CHECK

All 37 rows of `DECLINE_REGISTER_V002.md` were walked. Load-bearing rows:

| Row | Fence | Disposition |
|---|---|---|
| S03 | related `U(1)` structures are not interchangeable | **CLEAN.** The `A`/`a` symbols in the boundary actions are not identified with the parent comparison group or public response. |
| S05 | source/record co-location is not the missing complete field/CTP extension | **CLEAN.** Boundary-record countermodels are not silently tensored with `S_D` to manufacture full actions. |
| S12 | status/census labels are not proof objects | **LIVE / CLEAN.** “FORCED” is retyped to a two-member intersection fact; no family theorem is claimed. |
| S24 | no clustering axiom | **NOT TRIGGERED.** No limit route occurs. |
| S25 | no equal-action/reparameterization selector | **CLEAN.** No member is compared by action value or selected. |
| S26 | `C_ref` barred as a source | **CLEAN.** No smooth or refinement source enters. |
| S28 | constrain action freedoms only by boundary closure plus induced action before comparison | **CLEAN.** The packet-parent binding/falsifier test is named as the next derivation; no construction-end selection is made. |
| S34 | absolute scale requires a unique parent-derived stable solution | **NOT TRIGGERED.** No scale is fixed. |

The remaining rows are not activated. Distinctions retained:

```text
pair-common term             != family-forced term
four displayed members       != complete family census
boundary-record countermodel != packet-binding full parent action
absence from a display       != derived universal exclusion
future binding test          != present verdict on membership
```

`FLATTENING_CHECK = clean (37/37 rows walked).`

## 7. Battery and verb audit

`F_PLDEC` and anti-tuning passed. No physical quantity was evaluated; no
target, measured constant, response, or action value was used. M-2 checked
exact names, underscore/hyphen/reflow forms, status versus object, and
semantic-equivalent descriptions (“compact phase record,” “rotor,” “compact
topological record,” “BF”). Both sibling enumerations were used under law 9.

PRE-SEAL PIN CHECK: the governing artifacts, erratum, incorporated exhibit
digest, gate, skeleton, charter, and decline register all rehashed to their
stated pins; every cited span was recomputed from its source bytes; output and
sidecar names were absent before write.

Verb audit scope includes headings, tables, displays, and final lines.
“Narrowed” means only that the positive T01 intersection survives on
`E_D={S_0,S_1}` and fails to widen to `E_4`; it does not select a stratum or
declare either boundary countermodel a packet-parent inhabitant. “Located”
means content-addressed bytes matching `ERR`, with the direct-sidecar absence
disclosed in §0.

EXHIBIT = located (members enumerated under law 9: S_0, S_1, S_rot, S_BF; lower bound at least four, no-outside proof absent)
T01 = NARROWED (scope exact: common on E_D={S_0,S_1}; S_rot and S_BF omit S_D, so not forced over E_4 or the unenumerated family)
FORCED_ROW = retype to COMMON-ON-EXHIBITED-SOURCE-PAIR / NOT FAMILY-FORCED; closure starts by deriving the packet-binding stratum before hole pressure
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN (+3 scope disclosures: exhibit incorporated by sealed erratum rather than direct sidecar; four is a lower bound; S_rot/S_BF packet-parent membership remains untested)
