#!/usr/bin/env python3
# Generates the B01 inventory rows with digests COMPUTED from the sealed files,
# so no digest in the artifact is transcribed by hand.
import hashlib
sha = lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
ROWS = [
 ("P-01","FUNDAMENTAL_BOUNDARY_RECORD_ACTION_PRINCIPLE_V002.md",
  "action / field-content rule","microscopic theory premise","Level-1 postulate, CURRENT_AUTHORITY_LEDGER_V010.json:25-30"),
 ("P-02","PRIMITIVE_VECTORLIKE_CHARGED_SOURCE_BRANCH_V003.md",
  "source-branch inventory","source sector","Level-1 postulate, CURRENT_AUTHORITY_LEDGER_V010.json:25-30"),
 ("P-03","PRIMITIVE_TRANSPORT_ONLY_PHASE_COMPLETE_GENERATOR_PRINCIPLE_V001.md",
  "generator-class rule","transport/phase generators","Level-1 postulate (adopted, not derived), V010.json:25-30"),
 ("P-04","PRIMITIVE_SOURCE_RECORD_PAIRED_RETURN_IDENTIFICATION_PRINCIPLE_V002.md",
  "source-record identity hypothesis","source-record pairing","Level-1 postulate; derivation false per standing classification"),
 ("P-05","BOUNDARY_RECORD_ONSET_SATURATION_ACTION_GATE_V003.md",
  "relative onset-saturation rule","boundary record onset","Level-1 postulate (adopted, not derived), V013.json:31-34"),
 ("P-06","SOURCE_FLUX_CONDITIONED_RECORD_WRITE_GATE_V003.md",
  "zero-flux / no-charged-write rule","record write gate","Level-1 postulate (adopted branch rule), V013.json:31-34"),
]
print("| id | primitive (authority file) | mathematical type | domain | authority status | byte digest (computed) |")
print("|---|---|---|---|---|---|")
for i,f,typ,dom,auth in ROWS:
    print("| `%s` | `%s` | %s | %s | %s | `%s` |" % (i,f,typ,dom,auth,sha(f)))
