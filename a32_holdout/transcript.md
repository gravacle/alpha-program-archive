# A32 Registry Collection Transcript (collector_v001)

- Status: COMPLETED
- Canonical source URL: https://physics.nist.gov/cuu/Constants/Table/allascii.txt
- source_id: NIST_CODATA_2022_allascii
- Collector script: /Users/bgm/MB Work/a32_holdout/collector_v001.py
- Collector version hash (SHA-256 of collector_v001.py): 645c5d2c67b1fc39588fbf237c645784abb18834cce014453e3ee87d4f8990e2
- Raw bytes SHA-256 (raw_allascii.txt): 77fb90e66c40db3e6eb16630bc9c88e4c7c8beddbe5e71be406f2f26e3f67e67

## Steps (UTC)

- 2026-07-28T23:36:35Z -- Collection started. Output directory prepared; custodian_private/ set to mode 700.
- 2026-07-28T23:36:35Z -- curl attempt 1 of 4 against canonical URL.
- 2026-07-28T23:36:36Z -- curl attempt 1 succeeded with HTTP 200.
- 2026-07-28T23:36:36Z -- Raw bytes saved unmodified to raw_allascii.txt; SHA-256 recorded.
- 2026-07-28T23:36:36Z -- Vintage check passed. Header line: '2022 CODATA adjustment'
- 2026-07-28T23:36:36Z -- Column header found at line 9 (0-based); value/uncertainty/unit column offsets 65/87/109; data region starts at line 11.
- 2026-07-28T23:36:36Z -- Parse complete: 355 lines in data region, 355 parsed, 0 excluded with machine reason codes.
- 2026-07-28T23:36:36Z -- Canonical value-free records built for 355 rows; canonical_id = SHA-256 of sorted-key compact UTF-8 serialization. Observed values did not enter records or ids.
- 2026-07-28T23:36:36Z -- Dedup complete: 355 clusters, 355 kept, 0 suppressed.
- 2026-07-28T23:36:36Z -- candidates.jsonl written (value-free); exclusions.jsonl and duplicates.jsonl written.
- 2026-07-28T23:36:36Z -- Custodian commitments written: custodian_private/custodian.jsonl (mode 600, the ONLY file containing values/uncertainties) and public commitments.jsonl (canonical_id + commitment hex only).
- 2026-07-28T23:36:36Z -- flags.jsonl written with 2 ALPHA_DATUM_NAME_MATCH entries. Lineage exclusion is executed later at the eligibility stage under the frozen rule; this file only pre-flags name matches. No row was dropped for content.
- 2026-07-28T23:36:36Z -- Collector version hash recorded (SHA-256 of collector_v001.py).
- 2026-07-28T23:36:36Z -- All output file hashes computed. No outcome payload was disclosed outside custodian_private/. The collector accessed no research corpus file.

## Row counts

- alpha_name_flagged: 2
- candidates_kept: 355
- duplicates_suppressed: 0
- rows_in_data_region: 355
- rows_parse_excluded: 0
- rows_parsed: 355

## File SHA-256 hashes

- /Users/bgm/MB Work/a32_holdout/candidates.jsonl: 36ca855600ba64392085286b623cad3c0b5fcc53257ca27b35ccb85e5f10192c
- /Users/bgm/MB Work/a32_holdout/collector_v001.py: 645c5d2c67b1fc39588fbf237c645784abb18834cce014453e3ee87d4f8990e2
- /Users/bgm/MB Work/a32_holdout/commitments.jsonl: 66ac4250ded20e569a1b05a8658d42252c1098e250d73dfae21f52361197a752
- /Users/bgm/MB Work/a32_holdout/custodian_private/custodian.jsonl: 8488c1a1ad3b73eb3ae2a143af155645c02472c4902f9d57b0aeb99c4e441364
- /Users/bgm/MB Work/a32_holdout/duplicates.jsonl: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- /Users/bgm/MB Work/a32_holdout/exclusions.jsonl: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- /Users/bgm/MB Work/a32_holdout/flags.jsonl: e3e0af6c422b460c63768d748c1baa6d59e745011e497cea642892eddbb821ec
- /Users/bgm/MB Work/a32_holdout/raw_allascii.txt: 77fb90e66c40db3e6eb16630bc9c88e4c7c8beddbe5e71be406f2f26e3f67e67
- /Users/bgm/MB Work/a32_holdout/transcript.md: (own hash; computed after this transcript is finalized and reported by the runner)

## Flag-file note (frozen rule 9)

Lineage exclusion is executed later at the eligibility stage under the frozen rule; this file only pre-flags name matches. No row was dropped for content.

## Attestation

No outcome payload was disclosed outside custodian_private/. The collector accessed no research corpus file.
