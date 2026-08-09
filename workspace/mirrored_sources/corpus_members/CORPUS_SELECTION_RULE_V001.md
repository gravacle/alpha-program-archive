# THE CORPUS-MEMBER SELECTION RULE — V001 (2026-08-08, under decision 0dfc6e7b…)

Deterministic procedure the registrar executes to GENERATE candidate member
sets for Step-11 corpus instances. Every run is regenerable; both lanes verify
each output for wrong inclusion AND wrong exclusion before any M2 query runs.

## 1. The search space

The full program space per the standing census (~7,425 files; never
memory-bank), enumerated at run time with the enumeration count stated.
A candidate member must be SEALED, with its attachment mode recorded:
  S1 sidecar (.seal.sha256 / .sha256 whose digest matches the bytes)
  S2 packet-manifest membership (named with digest in a sealed packet manifest)
  S3 sealed-inventory membership (named with digest in a sealed package or
     baseline inventory)
A file matching content but sealed no way is listed in the instance's
EXCLUDED-UNSEALED table — visible, not silently dropped.

## 2. Corpus typing (mechanical, from the descriptor's own operand)

  CLAIM-SCOPED: the M2 operand names a claim family (e.g. "FS/uniqueness
  claims"). PROBE TERMS derive from the descriptor bytes alone: the corpus
  name's tokens split on '/', '-', '_' plus every backticked or quoted object
  name in the row's M2 clause; each term expanded four-mode (fixed-string;
  whitespace-normalized; hyphen/space/underscore and apostrophe variants;
  object-vocabulary aliases recorded in the sealed alias tables). No term is
  added from anyone's memory of the subject.
  PROVENANCE-SCOPED: the operand names a source relation of a specific sealed
  artifact (preseal_sources, output_claim_sources, selector_sources,
  selection_sources). MEMBERS = the citation closure of that artifact's sealed
  bytes: every source it names with digest or path+span, transitively through
  sealed citations only, closure depth recorded. Content matching plays no role.

## 3. The output

One instance per corpus in V007's rd22.sealed-corpus-definition.v001 schema:
members[] content-addressed (path, sha256, seal-attachment mode), the probe
terms or closure root displayed, the searched space stated with counts, the
EXCLUDED-UNSEALED table attached. Status DRAFT until BOTH lanes' verification
artifacts seal; only then may the instance be pinned by any envelope.

## 4. Fail-closed

A corpus whose descriptor underdetermines its typing or terms is returned
UNDETERMINED with the missing datum named — never guessed.

## V002 AMENDMENT (2026-08-08, registrar-authored, surfaced): THE CONJUNCTION CLAUSE

For CLAIM-SCOPED corpora, a candidate member must match EVERY corpus-name token
(each token in any of its four-mode variants) — a conjunction, not a
disjunction. Rationale of record: generic single tokens (alpha, occurrence,
claim) produce candidate sets no verification can meaningfully prune; the
conjunction of the name's own tokens is deterministic, derived from the same
descriptor bytes, and usable. The M2 clause's backticked object names remain
recorded with each instance for the verifying lanes. This amendment is
registrar-authored under the principal's authority decision (0dfc6e7b…) and
surfaced in the register; both lanes' verification checks the amendment as
part of the rule.

## V003 AMENDMENT (2026-08-08, registrar-authored, surfaced): THE REGISTRY TYPE

A third corpus type joins claim-scoped and provenance-scoped: REGISTRY — a
corpus whose members ACCRUE BY DECISION rather than existing to be found
(licenses, selections, entered aliases). Its lawful instantiation is the
CURRENT REGISTRY STATE — empty if nothing has been licensed — with the
accrual authority declared (who may license an entry; the registrar seals
each accrual as a surfaced addition). A claim-sweep over a registry corpus is
WRONG-TYPED: it collects mentions of the registry's name, not members of it.
Incident of record: the BX07 sweep returned 267 mention-candidates before the
typing was seen; the sweep output is retained as the negative control.
Typing is determined from the corpus's defining use in sealed bytes (BX07:
"must be separately licensed and entered in the alias corpus" — an accrual
registry by its own verb). Both lanes' verification checks the typing.
