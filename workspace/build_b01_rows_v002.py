#!/usr/bin/env python3
# B01 V002 inventory generator: 32 rows.
#   P-01..P-06  the six Level-1 postulate authorities, digests COMPUTED from their files.
#   S-01..S-26  the 26 value-path premise classes, extracted from the sealed prefreeze result's
#               section 2 table, each carrying its STATUS AS THE SOURCE STATES IT.  Nothing promoted.
# The spine rows are digested against their SOURCE document (the prefreeze result), because the class
# is a row of that table rather than a standalone file -- stated in the artifact, not hidden here.
import hashlib, json
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
SPINE_SRC = 'STAGE8_FROZEN_PRIMITIVE_INVENTORY_PREFREEZE_RESULT_V001.md'
SPINE_DIGEST = sha(SPINE_SRC)
AUTH = [
 ("P-01","FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md","action / field-content rule","microscopic theory premise","Level-1 postulate (V010.json:25-30)"),
 ("P-02","PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md","source-branch inventory","source sector","Level-1 postulate (V010.json:25-30)"),
 ("P-03","PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md","generator-class rule","transport/phase generators","Level-1 postulate, adopted not derived (V010.json:25-30)"),
 ("P-04","PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md","source-record identity hypothesis","source-record pairing","Level-1 postulate; derivation false per standing classification"),
 ("P-05","BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md","relative onset-saturation rule","boundary record onset","Level-1 postulate, adopted not derived (V013.json:31-34)"),
 ("P-06","SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md","zero-flux / no-charged-write rule","record write gate","Level-1 postulate, adopted branch rule (V013.json:31-34)"),
]
print("| id | primitive | mathematical type (kind) | domain (presupposes) | authority | status AS SOURCED | byte digest |")
print("|---|---|---|---|---|---|---|")
for i, f, typ, dom, auth in AUTH:
    print("| `%s` | `%s` | %s | %s | %s | sealed authority row | `%s` |" % (i, f, typ, dom, auth, sha(f)))
for r in json.load(open('spine_rows.json')):
    print("| `S-%02d` | %s | %s | %s | prefreeze result section 2, row %d | **%s** | `%s` |"
          % (r['n'], r['primitive'], r['kind'], r['presupposes'], r['n'], r['status'], SPINE_DIGEST))
