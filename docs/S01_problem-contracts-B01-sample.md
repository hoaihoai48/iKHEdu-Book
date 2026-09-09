# S01 — 3 Problem Contract mau B01 (Step 1, chua DSL)

> Status: `draft` — de duyet khung, chua phai content final. Source: `python-level-1.docx` (ban full), B01.

## prob_l01_p01 — Loi chao robot

```yaml
id: prob_l01_p01
source_trace:
  source_file: courses/python-bang-a/python-level-1.docx
  source_lesson: Bai 01
  source_problem_id: pya_l01_p01_loi_chao_robot
  source_heading: 'Bai 01 [pya_l01_p01_loi_chao_robot]: Loi chao robot'
title: Loi chao robot
learning_objectives: [program-output, sequence]
algorithmic_concepts: [sequence]
context: Robot khoi dong, hien 1 dong chao co dinh.
input_scenario: khong co input (chuong trinh chay la hien ngay)
expected_behavior: nhan vat hien dung 1 dong 'Xin chao cac ban! Toi la Robot Python.' (chap nhan lech cau chao khi viet De_Bai tieng Viet, nhung phai khop De_Bai da chot)
constraints: {lines: 1, exact_text: true}
disposition: KEEP
transformation: DIRECT
semantic_status: SEMANTIC_PRESERVE
```

## prob_l01_p02 — Cau doi ngay tet

```yaml
id: prob_l01_p02
source_trace:
  source_file: courses/python-bang-a/python-level-1.docx
  source_lesson: Bai 01
  source_problem_id: pya_l01_p02_cau_doi_tet
  source_heading: 'Bai 02 [pya_l01_p02_cau_doi_tet]: Cau doi ngay tet'
title: Cau doi ngay tet
learning_objectives: [program-output, sequence-multiline]
algorithmic_concepts: [sequence]
context: Bang dien tu hien 2 ve cau doi, moi ve 1 dong.
input_scenario: khong co input
expected_behavior: hien dung 2 dong theo thu tu (dong 1 / dong 2 nhu De_Bai); khong doi thu tu, khong gop 1 dong
constraints: {lines: 2, order: strict}
disposition: KEEP
transformation: DIRECT
semantic_status: SEMANTIC_PRESERVE
```

## prob_l01_p03 — Doc va in so nguyen (echo so)

```yaml
id: prob_l01_p03
source_trace:
  source_file: courses/python-bang-a/python-level-1.docx
  source_lesson: Bai 01
  source_problem_id: pya_l01_p05_doc_in_so_nguyen
  source_heading: 'Bai 03 [pya_l01_p05_doc_in_so_nguyen]: Doc va in so nguyen'
title: Doc va in so nguyen
learning_objectives: [program-input, variable-echo, int-type]
algorithmic_concepts: [sequence, variable_assignment]
context: May dem ve nhan ma so roi hien lai ma do.
input_scenario: 1 so nguyen N (-1e9..1e9); Scratch: ask 1 lan
expected_behavior: sau khi nhap N, bien luu N va hien lai dung N (vi du nhap 2026 → hien 2026); bat buoc luu answer ngay sau ask (answer-overwrite guard)
constraints: {asks: 1, range: [-1000000000, 1000000000]}
disposition: KEEP
transformation: STRUCTURAL_MAPPING   # input() -> ask + set; print() -> say
semantic_status: SEMANTIC_PRESERVE
```

## Gate Step 1 (mau)

- Ca 3 giu duoc semantics + objective + trace nguoc ve ma `pya_*` + heading goc.
- `expected_behavior` da co tu Step 1 (formalize day du o Step 5).
- Chua co DSL, chua De_Bai, chua quyet P0–P3/Observe–Create (de Step 3).
