#!/usr/bin/env python3
"""Run the sealed Family-1 compiler once per Batch-1 partial instance."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path
from typing import Any

def canon(v: Any) -> bytes:
    return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()
def safe(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]","_",s)

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--cleanroom",type=Path,required=True); ap.add_argument("--batch-root",type=Path,required=True); ns=ap.parse_args()
    root=ns.cleanroom.resolve(); batch=ns.batch_root.resolve(); attempts=batch/"compile_attempts"
    if attempts.exists() and any(attempts.iterdir()): raise SystemExit("OUTPUT_COLLISION")
    attempts.mkdir(parents=True,exist_ok=True)
    tooling=root/"step11_tooling_family1"; compiler=tooling/"compile_carriers.py"; contract=tooling/"contracts/tooling_family1.schema.json"; delta=root/"STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json"; targets=tooling/"targets.generated.json"; base_sources=json.loads((tooling/"sources.generated.json").read_text()); manifest=json.loads((batch/"generated/instances.generated.json").read_text())
    rows=[]
    for rec in manifest["targets"]:
        tid=rec["target_id"]; tag=safe(tid); source=json.loads(json.dumps(base_sources))
        entry=next(x for x in source["entries"] if x["target_id"]==tid)
        entry.update({"available":True,"instance_relative_path":rec["instance_relative_path"],"instance_sha256":rec["instance_sha256"],"missing_owner":"PARTIAL_INSTANCE_NOT_FULL_BOX_SCHEMA"})
        source_path=attempts/f"{tag}.sources.json"; source_path.write_bytes(canon(source)); stderr_path=attempts/f"{tag}.stderr.txt"; stdout_path=attempts/f"{tag}.stdout.txt"; out=attempts/f"{tag}.output"
        cmd=[sys.executable,str(compiler),"compile","--contract",str(contract),"--contract-sha256",sha(contract),"--schema-delta",str(delta),"--schema-delta-sha256",sha(delta),"--targets",str(targets),"--targets-sha256",sha(targets),"--sources",str(source_path),"--sources-sha256",sha(source_path),"--source-root",str(root),"--output-root",str(out)]
        cp=subprocess.run(cmd,capture_output=True,check=False); stdout_path.write_bytes(cp.stdout); stderr_path.write_bytes(cp.stderr)
        refusal="SCHEMA_CONFORMANCE" if b"REFUSE SCHEMA_CONFORMANCE" in cp.stderr else "UNEXPECTED"
        if cp.returncode!=2 or refusal!="SCHEMA_CONFORMANCE": raise SystemExit(f"UNEXPECTED_COMPILER_RESULT {tid} exit={cp.returncode} stderr={cp.stderr!r}")
        rows.append({"target_id":tid,"compiler_exit":cp.returncode,"compiler_status":refusal,"source_manifest_sha256":sha(source_path),"stdout_sha256":sha(stdout_path),"stderr_sha256":sha(stderr_path),"component_bound":False,"admission":"BARRED_STEP11_SUBGATE"})
    result={"schema":"rd22.step11.instance-batch1-compile-attempts.v001","compiler_sha256":sha(compiler),"contract_sha256":sha(contract),"schema_delta_sha256":sha(delta),"target_manifest_sha256":sha(targets),"attempts":rows,"summary":{"attempted":len(rows),"bound":0,"refused_schema_conformance":len(rows)},"admission":"BARRED_STEP11_SUBGATE","chain_invoked":False}
    (attempts/"compile_attempts.generated.json").write_bytes(canon(result)); print(json.dumps(result["summary"],sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
