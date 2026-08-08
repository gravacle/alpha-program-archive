#!/usr/bin/env python3
"""Verify Batch-1 outputs and generate closed row, self-check, and inventory records."""
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path
from typing import Any

def canon(v: Any)->bytes: return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def dig(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def load(p:Path)->Any: return json.loads(p.read_text())
def write_new(p:Path,v:Any)->str:
    if p.exists(): raise SystemExit(f"OUTPUT_COLLISION {p}")
    b=canon(v); p.write_bytes(b); return dig(b)

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--cleanroom",type=Path,required=True); ap.add_argument("--batch-root",type=Path,required=True); ns=ap.parse_args(); root=ns.cleanroom.resolve(); batch=ns.batch_root.resolve()
    manifest=load(batch/"generated/instances.generated.json"); attempts=load(batch/"compile_attempts/compile_attempts.generated.json")
    attempt_by={x["target_id"]:x for x in attempts["attempts"]}; row_map={}
    checked=0
    for rec in manifest["targets"]:
        p=root/rec["instance_relative_path"]; data=p.read_bytes()
        if dig(data)!=rec["instance_sha256"]: raise SystemExit(f"INSTANCE_HASH {p}")
        inst=json.loads(data); checked+=1
        for g in inst["grounded_elements"]:
            q=batch/"generated"/g["payload_relative_path"]; b=q.read_bytes()
            if dig(b)!=g["payload_sha256"] or len(b)!=g["payload_byte_length"]: raise SystemExit(f"PAYLOAD {q}")
        a=attempt_by[rec["target_id"]]
        if a["compiler_status"]!="SCHEMA_CONFORMANCE" or a["component_bound"]: raise SystemExit("COMPILER_STATUS")
        entry=row_map.setdefault(rec["row_id"],{"row_id":rec["row_id"],"new_status":"PARTIAL_INSTANCE_PRESENT_SCHEMA_INCOMPLETE","target_ids":[],"partial_instance_sha256":[],"components_produced":[],"missing_owners":set(),"compiler_refusal_sha256":[],"admission":"BARRED_STEP11_SUBGATE"})
        entry["target_ids"].append(rec["target_id"]); entry["partial_instance_sha256"].append(rec["instance_sha256"]); entry["compiler_refusal_sha256"].append(a["stderr_sha256"]); entry["missing_owners"].update(m["owner"] for m in inst["missing_elements"])
    rows=[]
    for entry in row_map.values():
        entry["target_ids"].sort(); entry["partial_instance_sha256"].sort(); entry["compiler_refusal_sha256"].sort(); entry["missing_owners"]=sorted(entry["missing_owners"]); rows.append(entry)
    rows.sort(key=lambda x:x["row_id"])
    row_record={"schema":"rd22.step11.instance-batch1-row-status.v001","rows":rows,"summary":{"rows_advanced":len(rows),"components_bound":0},"admission":"BARRED_STEP11_SUBGATE","chain_invoked":False}
    row_sha=write_new(batch/"row_status.generated.json",row_record)
    syntax=[]
    for name in ["author_partial_instances.py","run_compile_attempts.py","finalize_batch.py"]:
        ast.parse((batch/name).read_text()); syntax.append(name)
    self_check={"schema":"rd22.step11.instance-batch1-self-check.v001","passed":True,"checks":{"python_ast":syntax,"instances_hash_verified":checked,"payloads_hash_verified":len(list((batch/"generated/payloads").glob("*.bin"))),"compiler_attempts":len(attempts["attempts"]),"compiler_refusals_schema_conformance":sum(x["compiler_status"]=="SCHEMA_CONFORMANCE" for x in attempts["attempts"]),"components_bound":0,"row_status_sha256":row_sha,"admission":"BARRED_STEP11_SUBGATE"},"chain_invoked":False}
    write_new(batch/"self_check.generated.json",self_check)
    inventory_path=batch/"inventory.generated.json"; files=[]
    for p in sorted(x for x in batch.rglob("*") if x.is_file() and x!=inventory_path):
        b=p.read_bytes(); files.append({"relative_path":p.relative_to(batch).as_posix(),"byte_length":len(b),"sha256":dig(b)})
    write_new(inventory_path,{"schema":"rd22.step11.instance-batch1-inventory.v001","inventory_self_excluded":True,"files":files})
    print(json.dumps({"files":len(files),"rows":len(rows),"instances":checked,"bound":0},sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
