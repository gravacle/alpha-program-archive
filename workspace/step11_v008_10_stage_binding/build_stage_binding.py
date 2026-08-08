#!/usr/bin/env python3
"""Probe sealed stage identities and run the existing compiler fail-closed."""
from __future__ import annotations
import argparse, hashlib, json, os, re, subprocess, sys
from pathlib import Path
from typing import Any

NODES=["SPEC-SEAL","CORE-RESULT-SEAL","PARENT-COMPARISON","HOLDOUT-UNIVERSE-SEAL","QSPEC-SPEC-SEAL","PREDICTION-MAP-SEAL","THOMSON-RESULT-SEAL","ALPHA-RESULT-SEAL","HOLDOUT-RESULT-SEAL","END-TO-END-RECONSTRUCTION-SEAL","FINAL-CLAIM-SEAL"]
STATUS={"SPEC-SEAL":"BID_v011_specification_sealed","CORE-RESULT-SEAL":"BID_core_result_sealed","PARENT-COMPARISON":"BID_parent_comparison_completed","HOLDOUT-UNIVERSE-SEAL":"holdout_universe_sealed","QSPEC-SPEC-SEAL":"Qspec_specification_sealed","PREDICTION-MAP-SEAL":"prediction_map_sealed","THOMSON-RESULT-SEAL":"Thomson_result_sealed","ALPHA-RESULT-SEAL":"alpha_result_sealed","HOLDOUT-RESULT-SEAL":"holdout_result_sealed","END-TO-END-RECONSTRUCTION-SEAL":"independent_end_to_end_reconstruction_sealed","FINAL-CLAIM-SEAL":"BID_final_claim_sealed"}
TEXT_SUFFIX={".md",".json",".txt",".sha256",".yaml",".yml",".py"}

def canon(v:Any)->bytes:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def dig(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def file_sha(p:Path)->str:return dig(p.read_bytes())
def norm(s:str)->str:return re.sub(r"[^a-z0-9]","",s.lower())
def write_new(p:Path,b:bytes)->str:
    if p.exists():raise SystemExit(f"OUTPUT_COLLISION {p}")
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);return dig(b)
def span(data:bytes,start:int,end:int,want:str)->None:
    if not 0<=start<=end<=len(data) or dig(data[start:end])!=want:raise SystemExit("SPAN_PIN")

def scan_space(root:Path)->dict[str,Any]:
    files=0;text_files=0;skipped_large=0;name_hits={n:[] for n in NODES};field_hits={n:[] for n in NODES};text_hits={n:0 for n in NODES};root_term=[]
    if not root.exists():return {"root":str(root),"available":False}
    for p in root.rglob("*"):
        if not p.is_file():continue
        if "step11_v008_10_stage_binding" in p.parts:continue
        files+=1
        base=p.name
        base0=base[:-12] if base.endswith(".seal.sha256") else p.stem
        for n in NODES:
            if norm(base0)==norm(n):name_hits[n].append(str(p))
        if p.suffix.lower() not in TEXT_SUFFIX:continue
        try:
            if p.stat().st_size>5_000_000:skipped_large+=1;continue
            b=p.read_bytes();s=b.decode("utf-8")
        except (OSError,UnicodeDecodeError):continue
        text_files+=1
        if re.search(r"parent[_ -]map[_ -]root",s,re.I):root_term.append(str(p))
        for n in NODES:
            if n in s:text_hits[n]+=1
            q=re.compile(r'"(?:stage|stage_id)"\s*:\s*"'+re.escape(n)+r'"')
            if q.search(s):field_hits[n].append(str(p))
    return {"root":str(root),"available":True,"files_seen":files,"text_files_scanned":text_files,"large_text_files_skipped":skipped_large,"direct_filename_hits":name_hits,"exact_stage_field_hits":field_hits,"exact_name_reference_file_counts":text_hits,"parent_map_root_term_hits":sorted(root_term)}

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument("--cleanroom",type=Path,required=True);ap.add_argument("--archive",type=Path,required=True);ap.add_argument("--program",type=Path,required=True);ap.add_argument("--output-root",type=Path,required=True);ns=ap.parse_args()
    root=ns.cleanroom.resolve();out=ns.output_root.resolve()
    if out.exists() and any(out.iterdir()):raise SystemExit("OUTPUT_COLLISION")
    out.mkdir(parents=True,exist_ok=True)
    prov=root/"provenance/boundary_incidence_dynamics_preregistration_v011.json";data=prov.read_bytes();want="13cf1e178a9fdced88590998984ec04e84ed83c0681b68dccd11b4e37d6afacd"
    if dig(data)!=want:raise SystemExit("PROVENANCE_HASH")
    span(data,18920,19830,"889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86");span(data,23996,30395,"b368767d8f9f1034ac39b392389e32910f09737684dd722f0f2b2715ad6ad1d3")
    obj=json.loads(data);adj=obj["review_stage_semantics"]["stage_dependencies"];stat=obj["status"]
    if list(adj)!=NODES:raise SystemExit("NODE_ORDER")
    searches=[scan_space(root),scan_space(ns.archive.resolve()),scan_space(ns.program.resolve())]
    for n in NODES:
        if stat.get(STATUS[n]) is not False:raise SystemExit(f"STATUS_NOT_FALSE {n}")
        for s in searches:
            if s.get("available") and s["exact_stage_field_hits"][n]:raise SystemExit(f"SELF_IDENTIFIED_STAGE_CANDIDATE_REQUIRES_ADJUDICATION {n}")
    formula_hits=sorted({p for s in searches if s.get("available") for p in s["parent_map_root_term_hits"]})
    spec_seal=root/"stage8_execution/spec_seal.sha256";spec_seal_bytes=spec_seal.read_bytes()
    if dig(spec_seal_bytes)!="57890038a7b60d8c328e8b305cfe5a9d9498af49a2306a8d16567dd2856ec715":raise SystemExit("NEAR_MATCH_PIN")
    search_record={"schema":"rd22.step11.v008-10.stage-search.v001","searched_spaces":searches,"object_names":NODES,"acceptance_rule":"exact self-identifying stage or exact stage-named artifact plus sidecar/packet-manifest/sealed-inventory attachment; reference-only and false-status near matches rejected","status_source":{"relative_path":"provenance/boundary_incidence_dynamics_preregistration_v011.json","sha256":want,"span":[23996,30395],"span_sha256":"b368767d8f9f1034ac39b392389e32910f09737684dd722f0f2b2715ad6ad1d3"},"near_matches":[{"stage_id":"SPEC-SEAL","relative_path":"stage8_execution/spec_seal.sha256","sha256":"57890038a7b60d8c328e8b305cfe5a9d9498af49a2306a8d16567dd2856ec715","points_to":"STAGE8_GATE5_KAPPA_RECORD_THEOREM_BATTERY_SPEC_AUTHORITY_FABLE_V002.md","points_to_sha256":"ddb36cbfe4edfc2a0520e9ae58063295214c64afed5cad5a64e9f311826358f5","disposition":"REJECTED_NEAR_MATCH","reason":"the target is a Gate-5 battery specification whose own ceiling says SPEC-SEAL is unattainable and BID_core_result_sealed remains false; it is not a BID SPEC-SEAL realization"}],"stage_outcomes":[{"stage_id":n,"status_field":STATUS[n],"status_value":False,"direct_realization_hits":0,"disposition":"ABSENT_OF_RECORD"} for n in NODES],"root_formula_probe":{"term_hit_files":formula_hits,"disposition":"GAP_NO_SEALED_FORMULA","reason":"hits declare or discuss a parent_map_root field; none supplies a sealed serialization/hash formula for this BX03 root"},"summary":{"located":0,"absent_of_record":11},"chain_invoked":False}
    search_sha=write_new(out/"search_record.generated.json",canon(search_record))
    stages=[{"stage_id":n,"parents":adj[n],"artifact":None,"artifact_status":"ABSENT_OF_RECORD","seal_attachment":None,"status_field":STATUS[n],"status_value":False,"parent_artifact_sha256s":[None for _ in adj[n]]} for n in NODES]
    inst={"schema":"rd22.step11.v008-10.stage-binding-partial.v002","target_id":"CS:C-B-V008-10:seal-stage-graph","box_schema_id":"urn:rd22:step11:v008-10:content-addressed-parent-map:v001","completeness":"PARTIAL","source_bindings":[{"relative_path":"provenance/boundary_incidence_dynamics_preregistration_v011.json","source_sha256":want,"span":[18920,19830],"span_sha256":"889515d30cedf7d3af5da1a9e1ff7c7a88a1bf0d9227bdf37d64113302dfcb86"},{"relative_path":"provenance/boundary_incidence_dynamics_preregistration_v011.json","source_sha256":want,"span":[23996,30395],"span_sha256":"b368767d8f9f1034ac39b392389e32910f09737684dd722f0f2b2715ad6ad1d3"}],"stages":stages,"parent_map_root":None,"root_status":"GAP_NO_SEALED_FORMULA","admission":"BARRED_STEP11_SUBGATE","chain_invoked":False}
    inst_rel="step11_v008_10_stage_binding/CS_C-B-V008-10_seal-stage-graph.partial.v002.json";inst_path=root/inst_rel;inst_sha=write_new(inst_path,canon(inst))
    tooling=root/"step11_tooling_family1";compiler=tooling/"compile_carriers.py";contract=tooling/"contracts/tooling_family1.schema.json";delta=root/"STAGE8_7A_BOX_SCHEMA_DELTA_CODEX2_V001.json";targets=tooling/"targets.generated.json";sources=json.loads((tooling/"sources.generated.json").read_text());entry=next(x for x in sources["entries"] if x["target_id"]==inst["target_id"]);entry.update({"available":True,"instance_relative_path":inst_rel,"instance_sha256":inst_sha,"missing_owner":"ABSENT_STAGE_SEALS_AND_PARENT_MAP_ROOT_FORMULA"});source_path=out/"compiler.sources.json";source_sha=write_new(source_path,canon(sources))
    cmd=[sys.executable,str(compiler),"compile","--contract",str(contract),"--contract-sha256",file_sha(contract),"--schema-delta",str(delta),"--schema-delta-sha256",file_sha(delta),"--targets",str(targets),"--targets-sha256",file_sha(targets),"--sources",str(source_path),"--sources-sha256",source_sha,"--source-root",str(root),"--output-root",str(out/"compiler_output")]
    cp=subprocess.run(cmd,capture_output=True,check=False);stdout_sha=write_new(out/"compiler.stdout.txt",cp.stdout);stderr_sha=write_new(out/"compiler.stderr.txt",cp.stderr)
    if cp.returncode!=2 or b"REFUSE SCHEMA_CONFORMANCE" not in cp.stderr:raise SystemExit(f"COMPILER_UNEXPECTED {cp.returncode} {cp.stderr!r}")
    result={"schema":"rd22.step11.v008-10.stage-binding-result.v001","instance_sha256":inst_sha,"search_record_sha256":search_sha,"compiler_sha256":file_sha(compiler),"source_manifest_sha256":source_sha,"compile":{"exit":2,"status":"SCHEMA_CONFORMANCE","stdout_sha256":stdout_sha,"stderr_sha256":stderr_sha,"component_bound":False,"remaining_fields":["11 stage realization artifacts","digest-parent bindings","sealed parent_map_root formula/value","sealed mapping from 11-node adjacency to BX03 three-stage schema"]},"admission":"BARRED_STEP11_SUBGATE","chain_invoked":False}
    result_sha=write_new(out/"binding_result.generated.json",canon(result))
    inv=[];inventory=out/"inventory.generated.json"
    for p in sorted(x for x in out.rglob("*") if x.is_file() and x!=inventory):
        b=p.read_bytes();inv.append({"relative_path":p.relative_to(out).as_posix(),"byte_length":len(b),"sha256":dig(b)})
    write_new(inventory,canon({"schema":"rd22.step11.v008-10.stage-binding-inventory.v001","inventory_self_excluded":True,"files":inv}))
    print(json.dumps({"located":0,"absent":11,"root":"GAP_NO_SEALED_FORMULA","compile":"SCHEMA_CONFORMANCE","instance_sha256":inst_sha,"result_sha256":result_sha},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
