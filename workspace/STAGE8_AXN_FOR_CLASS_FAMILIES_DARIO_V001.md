CLOSURE_DECLARATION_BEGIN

```text
CLOSURE_STATUS = DECLARED-FIRST
CLOSURE_BEGIN_BYTE = 00000000
PREDECLARATION_REGION = EMPTY (closure opens at byte 0; no text precedes it)
PREDECLARATION_OUTPUT_SCAN = 0 hits in authored prose (27-token sweep)
VERDICT_BEARING_SET = exactly the 8 content-addressed members below
UNDECLARED_SEARCH_SURFACE_VERDICT_WEIGHT = forbidden
LANE = DARIO   ROLE_THIS_RELAY = BUILDER (not verifier)
ALL_FAMILIES = CLAIMED until the opposite-lane check
```

| # | Closed member | SHA-256 | Role |
|---:|---|---|---|
| 01 | `relay_inbox/RELAY_PASTE_961_FOR_CLASS_FAMILIES_DARIO_V001.md` | `db95c14176e68557b595c0626b7c46112934780ae4ebf67a9330d5c1d896bc91` | assignment |
| 02 | `STAGE8_AXN_ANCHOR_INSTRUMENT_CODEX2_V003.md` | `79f0c35161204f846666badb38f28398ae317d56a64d8fe70f7f29e2ee01072e` | the governing `for_class` schema |
| 03 | `STAGE8_AXN_ENTERED_OBJECTS_BUILD_CODEX2_V002.md` | `fd2625a079c77fbc0a102a54a0dd8ba1d97dcfb393035c2b691b0475de254444` | the booked pairing, `E_joint`, and its four certificates |
| 04 | `STAGE8_AXN_STAGE_RULE_CONSTRUCTION_CODEX2_V002.md` | `f450b0a356b249509fb59b897c4f6a14e6996ba7da5ea513e69112a89907eed9` | the stage payload and the seven receipts |
| 05 | `JOINT_ANCHOR_DECISION_INSTANCE_V003.md` | `089af246cbc0d66e6ce70971dbb14d355a78ee0f5e294706a1acaeacd0d4236d` | the completed instance |
| 06 | `R3_4_COMPLETE_CAUSAL_SUPERCONNECTION_PARENT_SPEC_V001.md` | `40890e753463b8c4c49844864f3f4811f15ec5f71fe9c044f9eb7d91428899a9` | `R_c=span{|r_c>,|p_c>,|e_c>}` — the one leg with a named ordered basis |
| 07 | `STAGE8_GEN_OMEGA_GENERATIVE_ORIGIN_RULE_ADOPTION_PROPOSAL_V003.md` | `1be5f6a7e40c34586f3b5ab78f9129de0b5d2041cb6695b0e549443ddd6c6ee0` | the `A0_FINITE_SCALAR_SOURCE_REALIZATION` — a named decomposition, no named basis |
| 08 | `PROGRAM_STATE_BRIEF_V005.md`; `LOCKED_PROCESS.md`; `DECLINE_REGISTER_V002.md` | `e26f0d16055f3e833307c893704561cfb683065f0798e80e1dc0a9db7ed7799c`; `38149496a2b5d89d20b614d972bffef1867d7cde573b26d77dfb207ece3446fb`; `957476c8c605a37015d51e209ae3197ef3f7c2275fcdea6682f8074edac3802a` | state pin, process law, S01-S37 authority |

```text
EVERY GROUND CITED BELOW IS A BOOKED OBJECT DIGEST OR A SEALED SPAN.  NO NEW MATHEMATICAL
OBJECT IS INTRODUCED.  BLIND HELD: the fiber remains an opaque pointer and is cited nowhere.
```

CLOSURE_DECLARATION_END

# STAGE 8 — AXN `for_class` REPLAY FAMILIES — DARIO LANE — V001
## RELAY 961 — `[PLAN:AXN-BUILD-D60]` — FIVE BUILT, THREE ROUTED ON ONE FREEDOM

Date: 2026-08-10
Status: **5/8 BUILT (FC-04..FC-08). 3/8 STOPPED (FC-01, FC-02, FC-03) — and all three trace to a
SINGLE freedom, which is the useful part of this result. CLAIMED.**

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

## 1. Family 1 — the determination the whole relay turns on [PROVABLE — SELECTOR-ROUTED]

The relay's instruction is exact: derive the basis family canonically **only** if a canonical
construction exists with zero freedom; if a genuine basis choice is free, **stop and route it**. A
basis is the classic place a construction consumes a freedom while feeling like derivation, so I
tested the three legs of `Delta_0^joint` separately.

`Delta_0^joint` at stage `N` sits inside `Fix(E_joint) = Fix(E_ch) (x) R_N (x) B_N` — the booked
fixed-space result — intersected with the kernel of `Tr_joint`. A basis of it needs a basis of each leg.

| Leg | Does the record name an ordered basis? |
|---|---|
| record `R_N` | **YES.** Member 06 seals `R_c = span{|r_c>, |p_c>, |e_c>}`, a named basis in a named order. |
| history/field `B_N` | **Partly.** `A_F,N = C*(Z^N)` has the canonical group-element family `{U_lambda}`, but an **order** on `Z^N` is not sealed, and "exact ordered basis" demands one. |
| source `Fix(E_ch)` | **NO.** Member 07 seals the *decomposition* `H_src^A := P_0 H_src (+) P_ch H_src` with `dim < infinity`, and seals `P_0, P_ch` as orthogonal projectors summing to `I_src`. **It names no basis within either block.** |

**A named decomposition is not a named basis, and I refuse to let the first pass as the second.** I
searched for one in exact-name mode: across the ten sealed files mentioning `H_src^A`, none carries a
basis or span line for `P_0 H_src` or `P_ch H_src`; `span{P_0,P_ch}` is a span of the two *projectors*,
not of either block.

I also tested the one sealed ordering convention that could have supplied the missing order —
*"identifying `n~-n` by requiring the first nonzero component to be positive, ordered by
`(norm(n)^2,n)` lexicographically"*. **It does not apply here.** That convention orders candidate
momenta `n in {-1,0,1}^4\{0}` in the boundary-incidence dynamics, a different object on a different
index set. Checking it rather than assuming it transferred is exactly the query-shape discipline this
lane has been corrected on before.

```text
BASIS = SELECTOR-ROUTED.  FC-01 STOPS.
THE FREEDOM, NAMED EXACTLY: an ordered basis of Delta_0^joint requires (a) a basis of each source
block P_0 H_src and P_ch H_src, which the record decomposes but does not span, and (b) an order on
the label group Z^N, for which no sealed convention exists.  Neither is derivable from the entered
or booked material; both are selections.  I do not choose either.
```

## 2. The cascade, and why it is one freedom rather than three [PROVABLE]

The schema types `phi_restriction_matrix` as *"exact matrix **in that basis**"*. So:

| Family | Status | Reason |
|---|---|---|
| **FC-01** `delta0_basis_family` | **STOPPED** | the freedom of §1 |
| **FC-02** `phi_restriction_matrix_family` | **STOPPED** | matrix-presented **in the basis of FC-01**; gated, not independently free |
| **FC-03** `factorization_and_inverse_family` | **STOPPED** | a factorization *of that matrix*; gated on FC-02 |

**All three stops have one freedom behind them**, and that is the operationally useful finding: the
principal has **one** selector to consider, not three. FC-02 and FC-03 introduce no freedom of their
own — the moment a basis is fixed, both become mechanical.

## 3. The five families that are basis-independent, built [PROVABLE]

Families 4-8 assert properties of maps and subspaces, which carry no basis. Each is grounded **only**
in booked object digests and sealed spans. Declared closed tuple, disclosed rather than hidden:

```text
JAC14-FC-FAMILY|v=001|id|quantifier|inputs|procedure|accept
```

### FC-04 — CPTP

```text
JAC14-FC-FAMILY|v=001|id=FC-04-CPTP|quantifier=all-N>=1-on-the-F_cyl-bounded-class|inputs=EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8;COND-EXP-CERT@0010388acbf2a97c0db1c2f772b54af2a092d3134889ff3ef06155110a1df01e;TOTAL-TYPING-CERT@262cc0d76b59d3c9bebde2f6f25f40e129da7ff7d984bada9c42039cde7c8c77;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|procedure=at-each-N-restrict-E_joint-to-A_C0,N-and-replay-the-booked-unital-completely-positive-idempotence-identities-factorwise-then-transport-along-J_NM-by-the-booked-stage-maps|accept=E_joint-restricted-to-stage-N-is-unital-completely-positive-and-J_NM-intertwines-the-restrictions-for-every-N<=M
```

### FC-05 — charge covariance

```text
JAC14-FC-FAMILY|v=001|id=FC-05-CHARGE-COVARIANCE|quantifier=all-N>=1-on-the-F_cyl-bounded-class|inputs=EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8;COMMUTATION-CERT@b6bc91777da3a69691f1b00ac4b30cfe61a472a7c55466098701018d4735d864;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|procedure=replay-the-booked-commutation-identities-E_joint-compose-i_src=i_src-compose-E_ch-and-E_joint-compose-i_R=i_R-and-E_joint-compose-i_B=i_B-at-each-stage-embedding-and-check-stability-under-J_NM|accept=the-charge-action-commutes-with-every-stage-restriction-and-with-J_NM-for-every-N<=M
```

### FC-06 — superselection commutation

```text
JAC14-FC-FAMILY|v=001|id=FC-06-SUPERSELECTION-COMMUTATION|quantifier=all-N>=1-on-the-F_cyl-bounded-class|inputs=EJOINT-BUNDLE@d7ce42de8e2e569aeea9f1b3d57e3dde045e739c8f85dcb488d78141863f2512;COMMUTATION-CERT@b6bc91777da3a69691f1b00ac4b30cfe61a472a7c55466098701018d4735d864;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269;RECEIPT-ROOT@9451020e12f72fe5ede31a7e75692e784c559a3854981db00105657d9d6bdb41|procedure=take-the-four-booked-per-object-certificates-as-the-stage-N-ground-and-propagate-by-the-seven-universal-restriction-and-limit-square-receipts-whose-ordered-root-is-cited|accept=the-superselection-commutation-holds-at-every-stage-and-passes-to-the-limit-square
```

### FC-07 — fixed space and mixing

```text
JAC14-FC-FAMILY|v=001|id=FC-07-FIXED-SPACE-AND-MIXING|quantifier=all-N>=1-on-the-F_cyl-bounded-class|inputs=EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8;FIXED-SPACE-CERT@7019826c3febf445b22892198d6e98839579f464a4f3d4be0e903c43c0ee3a45;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|procedure=replay-Fix(E_joint)=Fix(E_ch)-graded-tensor-R_N-graded-tensor-B_N-at-each-N-as-a-SUBSPACE-statement-carrying-no-basis-and-check-J_NM-maps-fixed-space-into-fixed-space|accept=the-fixed-space-is-the-displayed-tensor-form-at-every-N-and-is-J_NM-stable-with-mixing-asserted-only-as-basis-free-complementary-decay-of-the-non-fixed-part
```

Note the deliberate restraint: the fixed space is asserted as a **subspace** identity carrying no
basis, and *mixing* is asserted only as basis-free complementary decay. Had I stated either in matrix
form it would have inherited FC-01's gate.

### FC-08 — the BI anchor family

```text
JAC14-FC-FAMILY|v=001|id=FC-08-BI-ANCHOR|quantifier=all-N>=1-on-the-F_cyl-bounded-class|inputs=PAIRING@aaa3b217d945c7c788eebacdb11814eca125a8966c5cfa3de3c75d01fc1288d3;FAITHFULNESS-CERT@53bc1baf0da9eb353426bff5cebfa448b2561faac2e1b30cde191e24cf3106fa;DELTA0@58b966ed371b23b29b9e3ceed280eb30c804484becb2b17ca6ea465668e951bc:[14222,14296)#bb73a8ec8816bddc9c84d84e48ca81bd8d315f316092cdf295dc8fb474e2826f;EJOINT@67e4d12b4053291b2c13d709d5e66f073d0ad7a483f3ae3a97a2d2f75b4b57b8;STAGE@42b6850c16422783217e7a4fa1c85113fbe96977bcfc25dc3b0b16ca8ce95269|procedure=at-each-N-state-the-entered-BI-equations-Phi_joint(I_C0)=I_C0-with-input-faithfulness-on-Delta_0^joint-at-the-pinned-definition-bytes-and-carry-them-along-J_NM|accept=the-BI-equations-hold-at-every-stage-of-the-class-and-are-J_NM-stable-with-tag-class-remaining-exactly-BI
```

The adopted tag class is `{BI}` and the BI equations are the entered content; this family certifies
them per class and selects nothing.

### 3.1 Digest ledger and ordered root

| Family | Bytes | SHA-256 |
|---|---:|---|
| `FC-04` | 695 | `1a14255f7f40f58bd539325a2f7d33c40f8d7a22b519ba057b94fdda1f233236` |
| `FC-05` | 622 | `8d5ae19237917d13bd95be33f9ce84b74775b51340f14957fa70e909a1a78df9` |
| `FC-06` | 691 | `acabc0534123d03b905806ddd82028548705b5a4aaa58fb383d94d41ddd019c5` |
| `FC-07` | 673 | `a6cfa698ef82bbc24583d82731a1dc5c06e4528cae6869631773863c4da88486` |
| `FC-08` | 827 | `0c13577e78d5f2132d522b9775f9cb6cf0979699e9c5a5880c7bfc9600dad0b8` |

```text
JAC14-FC-LIST|v=001|count=5|built=FC-04,FC-05,FC-06,FC-07,FC-08|stopped=FC-01,FC-02,FC-03|items=FC-04:1a14255f7f40f58bd539325a2f7d33c40f8d7a22b519ba057b94fdda1f233236;FC-05:8d5ae19237917d13bd95be33f9ce84b74775b51340f14957fa70e909a1a78df9;FC-06:acabc0534123d03b905806ddd82028548705b5a4aaa58fb383d94d41ddd019c5;FC-07:a6cfa698ef82bbc24583d82731a1dc5c06e4528cae6869631773863c4da88486;FC-08:0c13577e78d5f2132d522b9775f9cb6cf0979699e9c5a5880c7bfc9600dad0b8
```

```text
FOR_CLASS_PARTIAL_LIST_SHA256 = 0497742e60a81b0aed4deb93e3e747d546332dc5b4ef3c18ca5ee3dc2452d4ed
```

The list carrier states **both** the built set and the stopped set, so the partial cannot be read as
a complete eight.

## 4. FREEDOMS-CONSUMED

```text
JOINT_ANCHOR_INPUT = ADOPTED-AND-FROZEN
JOINT_ANCHOR_DERIVED = false

CARRIED-AS-PARAMETER:
  the booked pairing, E_joint and its four certificates; the stage payload and receipts root;
  the pinned Delta_0^joint definition bytes; R_c's named ordered basis; the source decomposition.

SUBSTITUTED:
  NOTHING.  I chose no basis, no order on the label group, no matrix, and no factorization.

STOPPED AND ROUTED:
  FC-01 on the named freedom of section 1; FC-02 and FC-03 as gated consequences of it.

SCALING WEIGHTS: NONE CONSUMED; NONE FIXED; NONE SUBSTITUTED.
```

## 5. Flattening, custody, byte audit

- **S01-S37 FLATTENING CHECK:** walked. A named *decomposition* was not identified with a named
  *basis* (§1) — the load-bearing refusal here. A canonical spanning family was not identified with an
  *ordered* basis, since the order is what `Z^N` lacks. A sealed ordering convention for a different
  index set was not identified with one for this one. A property certificate was not identified with a
  matrix presentation (§3, FC-07 especially). A partial was not identified with a complete set — the
  list carrier names the stopped families.
- **F_PLDEC:** digests and symbolic operator statements only. No physical quantity evaluated.
- **BLIND:** held. No rank, no ratio, no fiber comparison; the fiber is cited nowhere.
- **PE-1..PE-14:** pointer-only, zero verdict weight.
- **BUILDER-NEVER-VERIFIES:** every family is **CLAIMED**. The opposite lane should press §1's
  determination first — if a basis *is* forced by something I missed, three families unlock at once.
- **CHAIN:** no anchor act, member binding, fixed-point execution, end test, gauntlet run, numerical
  evaluation, or comparison with a measured constant was invoked.

```text
CLOSURE_BEGIN_BYTE = 0
CLOSURE_END_BYTE = 2357
PREDECLARATION_OUTPUT_SCAN = 0 hits
FAMILIES_BUILT = 5 ; FAMILIES_STOPPED = 3 ; DISTINCT_FREEDOMS_BEHIND_THE_STOPS = 1
GROUNDS = booked digests and sealed spans only ; NEW_OBJECTS = 0
```

Self verb audit: "built" applies to the five families whose payloads and digests are displayed and
replayable from booked grounds. "Stopped" and "routed" apply to three, with one freedom named exactly
and no choice made. "Selector-routed" is used of the basis because the record decomposes the source
without spanning it and seals no order on the label group — both checked in exact-name mode rather
than assumed. `VERB_AUDIT_SELF = CLEAN`.

## 6. Final lines

```text
CLOSURE = declared-first (byte position 0, closure end 2357; scan 0 hits)
FAMILIES = 5/8 BUILT (FC-04 CPTP, FC-05 charge covariance, FC-06 superselection commutation, FC-07 fixed-space/mixing, FC-08 BI anchor) / 3 STOPPED (FC-01 delta0_basis_family, FC-02 phi_restriction_matrix_family, FC-03 factorization_and_inverse_family) — and ALL THREE STOPS TRACE TO ONE FREEDOM, which is the operationally useful part: the principal has ONE selector to consider, not three, and FC-02/FC-03 become mechanical the moment a basis is fixed
BASIS = SELECTOR-ROUTED. A basis of Delta_0^joint needs a basis of each leg. The RECORD leg has one — member 06 seals R_c = span{|r_c>,|p_c>,|e_c>}, named and ordered. The HISTORY/FIELD leg has the canonical group family {U_lambda} but NO sealed order on Z^N, and the schema demands an ORDERED basis. The SOURCE leg has NONE: member 07 seals the decomposition H_src^A := P_0 H_src (+) P_ch H_src with dim < infinity and seals P_0, P_ch as orthogonal projectors, but names no basis within either block — and across the ten sealed files mentioning H_src^A there is no basis or span line for either, while span{P_0,P_ch} spans the two PROJECTORS, not the blocks. A NAMED DECOMPOSITION IS NOT A NAMED BASIS. I also tested the one sealed ordering convention that might have supplied the missing order — "first nonzero component to be positive, ordered by (norm(n)^2,n) lexicographically" — and it does NOT apply: it orders candidate momenta in {-1,0,1}^4\{0} for the boundary-incidence dynamics, a different object on a different index set. Checked rather than assumed
GROUNDS = BOOKED-ONLY-VERIFIED (every input is a booked object digest — the pairing, E_joint, its four certificates, the ejoint bundle, the faithfulness certificate — or a sealed span: the stage payload, the receipts root, the pinned Delta_0^joint bytes. No new mathematical object is introduced)
FORMAT = JAC-14-REPLAY. Closed tuple declared and disclosed: JAC14-FC-FAMILY|v=001|id|quantifier|inputs|procedure|accept. Digests: FC-04 1a14255f7f40f58b (695 B), FC-05 8d5ae19237917d13 (622 B), FC-06 acabc0534123d03b (691 B), FC-07 a6cfa698ef82bbc2 (673 B), FC-08 0c13577e78d5f213 (827 B); ordered list carrier 450 B with root 0497742e60a81b0aed4deb93e3e747d546332dc5b4ef3c18ca5ee3dc2452d4ed. THE LIST CARRIER NAMES BOTH THE BUILT AND THE STOPPED SETS, so the partial cannot be read as a complete eight
NEW_CONTENT = NONE-BEYOND-DERIVATION. FC-07 is the place restraint mattered most: the fixed space is asserted as a SUBSPACE identity carrying no basis and mixing only as basis-free complementary decay — stating either in matrix form would have silently inherited FC-01's gate and turned a stop into a quiet choice
BLIND = HELD (the fiber remains an opaque pointer and is cited in no family)
NUMERAL_GREP = RUN (the 5/8 and 3/8 counts, the single-freedom count, every payload byte length and digest, and the root re-derived from command output rather than carried)
CHAIN_INVOKED = false
VERB_AUDIT_SELF = CLEAN
alpha_computed = false ; proof_authorized = false ; kappa_record_computed = false
```
