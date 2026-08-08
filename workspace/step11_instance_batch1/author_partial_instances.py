#!/usr/bin/env python3
"""Author only grounded partial Step-11 instances; never fill an absent field."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from typing import Any

HEX64 = re.compile(r"^[0-9a-f]{64}$")

def canon(v: Any) -> bytes:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()

def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def under(root: Path, rel: str) -> Path:
    p=(root/rel).resolve(); base=root.resolve()
    if Path(rel).is_absolute() or ".." in Path(rel).parts or not p.is_relative_to(base): raise ValueError(f"PATH {rel}")
    return p

def verify_span(root: Path, ref: dict[str, Any]) -> bytes:
    p=under(root, ref["relative_path"]); data=p.read_bytes()
    if digest(data)!=ref["source_sha256"]: raise ValueError(f"SOURCE_HASH {p}")
    a,b=ref["span"]
    if not (0<=a<=b<=len(data)): raise ValueError(f"SPAN_BOUNDS {p}")
    piece=data[a:b]
    if digest(piece)!=ref["span_sha256"]: raise ValueError(f"SPAN_HASH {p}:{a}:{b}")
    return piece

def validate_partial(v: dict[str, Any]) -> None:
    required={"schema","target_id","box_id","row_id","box_schema_id","completeness","source_bindings","grounded_elements","missing_elements","admission"}
    if set(v)!=required or v["schema"]!="rd22.step11.partial-box-instance.v001" or v["completeness"]!="PARTIAL" or v["admission"]!="BARRED_STEP11_SUBGATE": raise ValueError("PARTIAL_SHAPE")
    if not v["source_bindings"] or not v["missing_elements"]: raise ValueError("PARTIAL_EMPTY")
    for x in v["source_bindings"]:
        if set(x)!={"relative_path","source_sha256","span","span_sha256","role"} or not HEX64.fullmatch(x["source_sha256"]) or not HEX64.fullmatch(x["span_sha256"]): raise ValueError("BINDING_SHAPE")

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--cleanroom",type=Path,required=True); ap.add_argument("--plan",type=Path,required=True); ap.add_argument("--output-root",type=Path,required=True); ns=ap.parse_args()
    root=ns.cleanroom.resolve(); out=ns.output_root.resolve()
    if out.exists() and any(out.iterdir()): raise SystemExit("OUTPUT_COLLISION")
    out.mkdir(parents=True,exist_ok=True); (out/"payloads").mkdir()
    plan=json.loads(ns.plan.read_text()); records=[]
    for target in plan["targets"]:
        bindings=[]; grounded=[]
        for item in target["grounded"]:
            ref=item["source"]; piece=verify_span(root,ref); index=len(bindings)
            bindings.append({**ref,"role":"GROUNDING"})
            name=f"payloads/{ref['span_sha256']}.bin"; p=out/name
            if p.exists() and p.read_bytes()!=piece: raise ValueError("PAYLOAD_COLLISION")
            if not p.exists(): p.write_bytes(piece)
            grounded.append({"field_path":item["field_path"],"payload_relative_path":name,"payload_sha256":digest(piece),"payload_byte_length":len(piece),"source_binding_index":index})
        absence=target["absence_source"]; verify_span(root,absence); absence_index=len(bindings)
        bindings.append({**absence,"role":"ABSENCE_FINDING"})
        missing=[{**m,"absence_binding_index":absence_index} for m in target["missing"]]
        value={"schema":"rd22.step11.partial-box-instance.v001","target_id":target["target_id"],"box_id":target["box_id"],"row_id":target["row_id"],"box_schema_id":target["box_schema_id"],"completeness":"PARTIAL","source_bindings":bindings,"grounded_elements":grounded,"missing_elements":missing,"admission":"BARRED_STEP11_SUBGATE"}
        validate_partial(value); data=canon(value); safe=re.sub(r"[^A-Za-z0-9_.-]","_",target["target_id"]); rel=f"instances/{safe}.partial.json"; p=out/rel; p.parent.mkdir(exist_ok=True); p.write_bytes(data)
        records.append({"target_id":target["target_id"],"row_id":target["row_id"],"completeness":"PARTIAL","instance_relative_path":f"step11_instance_batch1/generated/{rel}","instance_sha256":digest(data),"grounded_count":len(grounded),"missing_count":len(missing),"admission":"BARRED_STEP11_SUBGATE"})
    manifest={"schema":"rd22.step11.instance-batch1-manifest.v001","targets":records,"summary":{"authored":len(records),"complete":0,"partial":len(records)},"admission":"BARRED_STEP11_SUBGATE","chain_invoked":False}
    (out/"instances.generated.json").write_bytes(canon(manifest))
    print(json.dumps(manifest["summary"],sort_keys=True))
    return 0
if __name__=="__main__": raise SystemExit(main())
