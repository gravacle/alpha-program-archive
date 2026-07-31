# Stage 8 Graph Rule Tests: Authority Edges And Prose Extraction V001

LANE: CODEX 1. CHARTER: Paste 174. DATE: 2026-07-31.
REGISTER HEAD AT ISSUE: Q-75. STATUS: TEST RECORD / NOT A RULING.

```text
alpha_computed = false
proof_authorized = false
kappa_record_computed = false
```

No alpha, `kappa_record`, `kappa_Thomson`, coupling, scale, root, eigenvalue,
beta function, `E_R`, `T_R`, `k_R`, absolute interval, or measured constant
comparison was computed or evaluated. `a32_holdout/custodian_private/` was not
opened. The uncommitted B0 artifact present in the shared tree was not read;
Paste 174 permits using B0 as graph input only once committed.

## Lead

Two proposed graph rules were tested only on their provable halves.

1. The authority-edge cycle-manufacture rationale is not supported by the
   experiment. Merging the extracted JSON authority edges into the scratch
   enlarged graph produced zero cycles.
2. The prose-extraction rule is high precision but lossy, and it misses the
   exemplar that motivated it. On the deterministic 80-sentence sample:
   precision `25/(25+0) = 1.000`; recall `25/(25+14) = 0.641`.

Neither rule is adopted, rejected, or repaired here. The judgment halves remain
the principal's.

## Generated Records

Machine-readable records:

```text
workspace/STAGE8_GRAPH_RULE_TESTS_SAMPLE_AND_AUTHORITY_EDGES_V001.jsonl
workspace/STAGE8_Q64_RECONSTRUCTED_EDGE_TABLE_V001.jsonl
```

The second file is deliberately marked:

```text
RECONSTRUCTED_CURRENT_STATE_NOT_ORIGINAL_Q64_EDGE_TABLE
```

because Q-64's original complete machine-readable edge table was not committed
as a standalone edge list. This file repairs future diffability from this run
forward; it does not pretend to be the missing original byte-for-byte table.

## Test 1. Authority Edges And Cycles

Source authority inventory:

```text
Codex 1 relay-170 sweep:
workspace/STAGE8_JSON_AUTHORITY_LEDGER_SWEEP_V001.md
```

That sweep verified exactly thirteen JSON authority ledgers:

```text
CURRENT_AUTHORITY_LEDGER family, V001 through V013
```

It also recorded that the ledgers contain authority/result-binding edges but no
construction dependency edges:

```text
ledger_construction_dependency_edge_found = false | TYPE-S
ledger_authority_edges_exist = true
dependency_graph_needs_authority-edge_decision = true
```

### Extraction

All 13 ledgers were parsed structurally. The extraction yielded 333 authority
edges:

| Type | Count |
|---|---:|
| authority-tuple | 84 |
| result-binding | 94 |
| supersession | 108 |
| other | 47 |

The sole `current_authority.ledger = CURRENT_AUTHORITY_LEDGER_V013.json`
self-declaration was held out as a self-identification, not a graph dependency
edge.

Typing rule used for the experiment:

| Ledger section | Edge type |
|---|---|
| `sealed_pre_alpha_authority`, `current_authority`, `parent_authority` | authority-tuple |
| `current_results`, `current_derived_results`, `new_sealed_results`, `subordinate_result_bindings` | result-binding |
| `current_level_1_postulates`, `new_level_1_postulates` | authority-tuple |
| `superseded_results`, `superseded_or_retired_results`, `superseded_or_rejected_since_v010` | supersession |
| external audits, conditional/diagnostic sections | other |

Execution-state flags were not merged with the objects that would discharge
them. Q-69 forbids that operation.

### Merge Experiment

Scratch graph input:

```text
reconstructed current-state would-build edges: 283
Paste-172 bridge/prose edges added for context: 4
JSON authority edges: 333
```

Cycle detection:

```text
merged_authority_cycle_count = 0 | TYPE-R | test: Tarjan SCC over the scratch merged graph
```

No cycle path exists to list. Therefore the stated rationale that merging
authority edges "manufactures cycles" is wrong on this tested corpus and
direction convention. The semantic argument for keeping authority as an overlay
may still survive, but the cycle-manufacture argument did not.

## Test 2. Prose Rule Precision And Recall

Proposed rule tested:

```text
A prose statement is direction-bearing iff it asserts that A must exist or be
determined before B can be written, computed, fixed, or derived; both objects
must be named explicitly; direction must be unambiguous from the sentence alone.
```

### Population And Sample

Population:

```text
1626 line-level candidate sentence units
```

Roots:

```text
/Users/bgm/MB Work/alpha-program-archive/workspace
/Users/bgm/MB Work/alpha-program-archive/supervision
```

Exclusions:

```text
a32_holdout/custodian_private/
the uncommitted/off-limits B0 artifact
```

Candidate patterns:

```text
appears in the equation
enters the
is required by
cannot be written without
is built from
carries the
feeds into
is an input to
is fixed by
is derived from
depends on
upstream of
gated by
requires
must exist before
prerequisite
blocked by
```

Sampling method:

```text
deterministic random.sample, seed =
sha256("PASTE174-Q75-prose-sample-v1") first 64 bits =
14132988783777448190
sample size = 80
```

Labeling order:

1. Each sampled sentence unit was labeled independently as `yes`, `no`, or
   `unclear` for whether it asserted a real construction dependency.
2. Only after that label was fixed was the proposed sentence-alone rule applied.

### Confusion Matrix

`unclear` independent labels are tracked but excluded from precision/recall
denominators.

| | Independent yes | Independent no | Independent unclear |
|---|---:|---:|---:|
| Rule extracts edge | 25 | 0 | 0 |
| Rule does not extract edge | 14 | 28 | 13 |

Metrics:

```text
precision = 25 / (25 + 0) = 1.000
recall    = 25 / (25 + 14) = 0.6410256410
```

Classification:

```text
prose_rule_low_precision = false | TYPE-R | test: 0 false positives in the judged sample
prose_rule_low_recall = true | TYPE-R | test: 14 false negatives among 39 independently-positive judged sentences
```

This confirms the conservative bias as costly-but-safe on the sample. It does
not justify adopting the rule; acceptable recall loss is a principal decision.

### Disagreements

False positives:

```text
none
```

False negatives:

The exact paths and text snippets for all 80 sampled sentences are in
`STAGE8_GRAPH_RULE_TESTS_SAMPLE_AND_AUTHORITY_EDGES_V001.jsonl`. The markdown
lists disagreements by sample id to avoid creating a second prose hardwire of
versioned evidence paths.

| Sample | Why the rule missed it |
|---:|---|
| 06 | exact-witness dependency, but proposed rule lacks named B object |
| 09 | ordering block stated, but missing input not named from sentence alone |
| 10 | blocked-by relation; missing complete object truncated |
| 11 | route amendments are dependencies, but objects are broad/compound |
| 13 | repair-artifact dependency embedded in long audit prose, not clean sentence rule |
| 20 | exemplar-style edge; rule as written does not say must-exist-before |
| 27 | pass condition but dependent object not explicit beyond `Pass` |
| 30 | requires enclosures but dependent object only deictic below |
| 40 | derivation-order prohibition; not two named objects in sentence rule |
| 51 | pass condition dependency, but dependent object only `Pass` |
| 67 | numeric activation blocked by E1 but no unambiguous pair |
| 75 | blocked behind/missing object but line fragment insufficient |
| 78 | gate requires all five but list absent from sentence |
| 79 | requires continuation but the required object is below/outside sentence |

### Exemplar Check

The originating exemplar is:

```text
The closure residual is built from an action carrying the `A_4` log, so
`k_R` -- the floor -- appears in the equation that fixes `K_*`.
```

Independent label:

```text
real edge: k_R -> K_*
```

Rule result:

```text
exemplar_caught_by_rule_as_written = false | TYPE-R | test: the sentence states participation in the fixing equation, not that `k_R` must exist or be determined before `K_*` can be fixed
```

Therefore the rule as written misses the motivating case. That is not a reason
to widen it automatically. Widening it is the judgment half, and remains the
principal's.

## Q-64 Edge Table Repair

Paste 174 also required a standalone machine-readable Q-64 edge table. The
original table was not available to commit:

```text
q64_original_exact_edge_table_found = false | TYPE-S
roots: archive workspace/supervision
query: edge table, edge_table, machine-readable, machine readable, graph, edges
finding: no standalone original Q-64 edge table found
```

The committed JSON table is a current-state reconstruction from the Q-64
`would-build` grammar plus the Paste-172 bridge context. It is not an adopted
graph and not the missing original Q-64 table.

## Typed Negatives

```text
merged_authority_cycle_count_zero = true | TYPE-R | test: Tarjan SCC over scratch merged graph returned zero SCCs of size >1 and no self-loop after self-declaration holdout
authority_cycle_manufacture_rationale_holds = false | TYPE-R | test: the merge produced zero cycles
prose_rule_low_precision = false | TYPE-R | test: 0 false positives in the judged sample
prose_rule_low_recall = true | TYPE-R | test: 14 false negatives among 39 independently-positive judged sentences
exemplar_caught_by_rule_as_written = false | TYPE-R | test: rule applied to the originating `k_R -> K_*` sentence
q64_original_exact_edge_table_found = false | TYPE-S | roots: archive workspace/supervision | query: edge table, edge_table, machine-readable, machine readable, graph, edges
B0_contents_read = false | TYPE-C | constraint: Paste 174 off-limits until B0 committed | release: committed B0 or principal instruction
custodian_private_opened = false | terminal fence declaration
```

## Discipline

The merged graph was scratch only. It is not committed as the graph and no
authority edge is adopted into the construction DAG. The two proposed rules
remain proposed rules; this artifact reports measurements only.
