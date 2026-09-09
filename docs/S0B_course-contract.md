# S0B — Course Contract (Step 0B)

> Status: `draft`. Source duy nhat: `courses/python-bang-a/python-level-1.docx` (ban full). Khong viet lesson/problem content o step nay.

## 1. G0 decisions

- **G0.1 Profile:** `scratch-lesson-package` — profile/domain extension co contract rieng (Curriculum/Lesson/Exercise/Block/Pattern/DSL + interaction-check), tai su dung convention chung repo: De_Bai khong spoil, Teacher Guide 9 phan, chuoi README → Ly_Thuyet → Bai_Tap → code, Word spec + QA checklist, severity blocker/major/minor/polish. Khong ep Scratch vao struct C++/Python khi semantics khac.
- **G0.2 Taxonomy:** Disposition `KEEP/MERGE/SPLIT/REWRITE/EXCLUDE` (+ `exclude_reason` khi EXCLUDE) × Transformation `DIRECT/STRUCTURAL_MAPPING/ALGORITHMIC_RECONSTRUCTION/SIMPLIFY/EXTEND` × Semantic `SEMANTIC_PRESERVE/SEMANTIC_PARTIAL/SEMANTIC_CHANGE`. Mechanism mo ta cach chuyen, khong mo ta do kho. Chi tiet tai `docs/PLAN_PYTHON_TO_SCRATCH_LEVEL1.md`.
- **G0.3 ID/versioning:** `IKH-xxxx` = global unique (giu theo AGENTS.md, cap khi tao problem Scratch chinh thuc); `prob_*` = problem contract language-neutral (lam viec noi bo); `pya_*` = ma Python goc (chi de trace, khong doi ten); ma Scratch `SCA-Lxx-Pyy` cho problem package (`problems/sca_l01_p01_...`). Schema version `0.1.0`, tang minor khi doi contract, major khi doi taxonomy.
- **G0.4 Rubric tuoi 8–11:** CORE = lam duoc bang block co ban + doc hieu san khau; EXTENSION = can dan them (ASCII/slicing nang cao); CHALLENGE = bai nang cao co scaffold day du; EXCLUDE kem reason (dac biet B14: ASCII/ord-chr/split-join phuc tap).

## 2. Course slug + cay thu muc

- Slug: `courses/scratch-bang-a-level1/` (chua tao thu muc o step nay; tao khi bat dau Step 1/3 co content that).

```text
courses/scratch-bang-a-level1/
├── README.md                    ← group-index (dieu huong, khong chua theory)
├── BOOK_MASTER.md               ← ban thao canonical xuat ban (khi co)
├── CURRICULUM_AUDIT.md          ← G-SCALE audit
├── S00_source-inventory.md      ← link ve docs/S00 (khong copy)
├── reference/
├── assets/                      ← svg/png render local, co caption/so thu tu
├── lessons/lesson-01/ ... lesson-14/   (so lesson cuoi theo audit, khong mac dinh 14)
│   ├── LessonXX_Production_Content.md
│   ├── Bai_Tap.md
│   ├── lesson.yaml / problems.yaml / exercises.yaml (machine-readable, gom theo lesson)
│   └── solutions/ (*.dsl canonical + render generated)
├── problems/sca_lxx_pyy_ten-bai/
│   ├── De_Bai.md
│   ├── Huong_Dan_Giang_Day.md
│   ├── solution.dsl (+ render)
│   └── interaction-check/ (manifest + scenarios)
└── assessments/
```

- File canonical hoc sinh: `LessonXX_Production_Content.md`, `Bai_Tap.md`, `De_Bai.md`. Contract yaml la ho tro machine-readable. Render (svg/png/DOCX/PDF) la generated.

## 3. Draft Curriculum Contract

```yaml
curriculum:
  id: scratch-bang-a-level1
  title: iKHEDU Scratch Bang A – Level 1
  target_age: 8–11
  target_grade: lop 3–5
  pedagogical_goal: tu duy lap trinh qua block truc quan; ke thua gia tri Python L1 nhung la curriculum Scratch doc lap
  source_curriculum: courses/python-bang-a/python-level-1.docx (5 chuong/14 bai/287 bai, verified Step 0A)
  chapters: giu 5 chuong Python lam diem xuat phat; so lesson cuoi theo audit (khong mac dinh 14)
  core_competencies: [sequence, variables, operators, branching, counted-loop, condition-loop, counter, accumulator, flag, sentinel, list-1based, string-traversal, debugging-dryrun]
  excluded_competencies: [python-syntax-detail, sep-end-advanced, ascii-ord-chr-deep, split-join-full, slicing-nang-cao]  # co the dieu chinh o audit; EXCLUDE phai co reason
```

- Nguyen tac cao nhat: hoi "hoc sinh hoc duoc gi?" truoc "chuyen the nao?".
- KPI: coverage, progression, age-appropriateness, algorithmic depth, quality, dedup, difficulty progression. Khong KPI 287→287.

## 4. Gate 0B

- Xong 0B khi: slug + cay + canonical + G0.1–G0.4 + draft Curriculum Contract duoc chu du an duyet.
- Tiep theo: Step 1 — 3–5 Problem Contract B01 that tu ban full (kem `expected_behavior` so bo), khong DSL.
