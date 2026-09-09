# PLAN — Chuyen Python Level 1 → Scratch Level 1

> Status: `baseline v1.0` — du truong thanh de bat dau Step 0A (evidence mode). Khong them abstraction lon moi; chi sua khi evidence bat buoc.
> Trang thai review ngoai (ChatGPT, 9.5/10 kien truc + quy trinh): architecture/process approved, implementation chua chay hang loat.
> Scope: 5 chuong / 14 bai / 287 bai tap tu `courses/python-bang-a/python-level-1.docx` → pipeline curriculum Scratch Level 1 (8–11 tuoi, lop 3–5, dinh huong Tin hoc tre Bang A).
> Master path: file nay. Source Python giu read-only. Khong claim verified khi chua co evidence.

## 0. Review & danh gia baseline (tom tat)

### 0.1. Diem dung — giu nguyen

1. **Transformation, khong phai translation 1:1.** Giu semantics/learning objective, doi representation. Vi du `input()` → `ask...and wait + set...to (answer)` la chuan.
2. **Kien truc tach lop:** Source → Contract → Transformation → Representation (Lesson/Exercise/Block/DSL) → Validation → Rendering (SVG) → Publishing (DOCX/PDF/Web). Khong de AI gen DOCX/SVG truc tiep.
3. **Scratch DSL la canonical representation cua code,** khong phai toan bo curriculum. AI sinh DSL → validator check → renderer render → publisher embed.
4. **SVG embed local (scratchblocks-cli → SVG/PNG → DOCX),** khong lay remote URL lam artifact sach. Ly do reproducible/offline/in an da neu la dung.
5. **Wording:** dung `Scratch 3 visual style / Scratch-compatible blocks`, khong claim `100% identical to Scratch MIT UI`.
6. **Problem Contract language-neutral (`prob_l01_p21`),** tach khoi implementation Scratch/Python/C++. Co `source_trace` nguoc ve lesson/problem/file Python.
7. **Transformation taxonomy duoc tach thanh 3 chieu theo G0.2:** Disposition (`KEEP/MERGE/SPLIT/REWRITE/EXCLUDE`) + Transformation mechanism (`DIRECT/STRUCTURAL_MAPPING/ALGORITHMIC_RECONSTRUCTION/SIMPLIFY/EXTEND`) + Semantic status (`SEMANTIC_PRESERVE/SEMANTIC_PARTIAL/SEMANTIC_CHANGE`). Khong dung taxonomy cu (`SEMANTIC_PRESERVE / SEMANTIC_MAPPING / ALGORITHMIC / SIMPLIFY / EXTEND / EXCLUDE`) nhu mot taxonomy don.
8. **Khong ep Python API 1:1** (`split/replace/ord/chr/set` → reconstruct bang duyet ky tu, phat hien khoang trang, list). Qua suc → EXTENSION/EXCLUDE.
9. **Problem vs Exercise tach nhau;** 4 muc scaffolding Observe → Arrange → Complete → Create la he scaffolding, khong bat buoc bai nao cung du 4 dang.
10. **Block Contract co signature (shape/inputs/output),** lam co so cho shape/type/nesting validation.
11. **Validation layer + answer-overwrite guard + dry-run dang bang chay thu** (khong day CPU/RAM cho tieu hoc) la dung huong.
12. **Bo sung Lesson Contract** (objectives, prerequisites, concepts, teaching_sequence, blocks, examples, dry_runs, common_mistakes, exercises, extensions) vi Problem Contract khong mo ta du lesson experience.
13. **Golden Spec/Golden Test truoc khi scale; chon B01 → B05 → B14 lam stress-test** (basic / control-algorithm / language-limitation). Hop ly.

### 0.2. Diem can sua / lam ro truoc khi lock schema (historical review — quyet dinh hien hanh nam tai G0.x va cac Step)

> Cac issue duoi day la lich su phat hien o baseline truoc; chi giu de audit/history, khong dung lam decision hien hanh.

1. **`PRESERVE` de gay hieu nham.** Trong summary muc 9, 11, 14 dung `PRESERVE` lan lon `SEMANTIC_PRESERVE/ALGORITHMIC`. Quyet: chi dung `SEMANTIC_PRESERVE` (giu semantics/objective) hoac `ALGORITHMIC_PRESERVE` (giu thuat toan, doi representation). Bo nhan `PRESERVE` tran.
2. **Scope Matrix muc 11 dang gan 1 nhan/lesson (B07–B10 = PRESERVE...).** Trai voi nguyen tac muc 11 tu neu (moi bai co the CORE+EXTENSION+CHALLENGE). Quyet: matrix phai xuong muc concept/problem, khong phan loai ca lesson bang 1 nhan.
3. **`SEMANTIC_MAPPING` vs `ALGORITHMIC` chua co dinh nghia phan biet du de validator/audit dung.** Can dinh nghia operational + vi du + tieu chi audit o Step 2.
4. **B03 (`//`, `%`, luy thua): rule "dung primitive neu co" chua du.** Can liet ke primitive Scratch thuc te co (`mod`, `floor`, phep `^`? khong co luy thua nguyen thuy) va quyet truoc: cai nao primitive, cai nao reconstruct bang loop, cai nao EXCLUDE o Level 1.
5. **Variable-init rule:** da sua dung (missing init → WARNING, khong REJECT vi Scratch co default). Can ghi thanh decision chinh thuc, ke ca ngoai le (counter/accumulator/flag/list-index thi WARNING manh hoac REQUIRE o dang Complete/Create).
6. **Pedagogy level khong phai thuoc tinh cua Problem** (muc 29) — can ap nhat quan: pedagogy level nam o Exercise Instance + Lesson teaching_sequence, khong nam o Problem Contract.
7. **Thieu chuan id/versioning:** `prob_l01_p21` chua gan voi `IKH-xxxx` (global unique theo AGENTS.md) va chua ro quan he voi `pya_l01_pxx` hien co. Can quyet mapping ID o Step 1.
8. **Thieu nguong EXCLUDE cu the cho B14** (ASCII/ord/chr/split/join...). Can rubric CORE/EXTENSION/EXCLUDE theo tuoi 8–11 truoc khi lam B14.
9. **Chua co dinh nghia test/semantic equivalence:** testcases trong Problem Contract dang la input/output Python-console; Scratch `ask/say` khong co stdin/stdout batch. Can dinh nghia cach map testcase → hanh vi Scratch co the kiem (step 5).
10. **Risk ve scratchblocks-cli version/font/spacing** moi chi dung o wording; can pin version + proof in thu o Step 6.

### 0.3.Conflict voi chuan repo hien hanh (can resolve)

- Repo dang chuan C++/Python (AGENTS.md, 01-code-standards, 02-problem-package: De_Bai 7 muc + Teacher Guide 9 phan, solution/test). Pipeline Scratch de xuat them Lesson Contract / Exercise Instance / Block Contract / DSL — chua co trong rule. Can quyet: day la profile moi `scratch-lesson-package` hay mo rong problem-package hien co. Khong tu y xem proposal la chuan.
- De_Bai cam spoil thuat toan; Teacher Guide du 9 phan; Lesson du chuoi README → Ly_Thuyet → Bai_Tap → code/test. Scratch Observe/Arrange/Complete/Create + dry-run + block hinh can duoc map vao chuoi nay, khong tao song song.
- Print: moi DOCX tuan `docs/MASTER_WORD_BUILD_SPECIFICATION.md` + `docs/PLAN_CHINH_WORD_IN_MAU.md`; hinh Scratch SVG/PNG can co caption, so thu tu, nguon, vi tri tham chieu; code/block khong tran le. Chua co spec embed SVG Scratch trong Word spec → Step 6 phai bo sung phu luc, khong tu sua spec goc.

## 1. Quyet dinh can chot truoc Step 1 (gate G0)

- G0.1. Profile Scratch: la profile/domain extension co contract rieng (`scratch-lesson-package`), tai su dung convention chung repo (De_Bai khong spoil, Teacher Guide 9 phan, chuoi README → Ly_Thuyet → Bai_Tap → code/test, Word spec + QA). Khong ep Scratch vao struct C++/Python khi semantics khac.
- G0.2. Hai taxonomy rieng (P0.1, chot truoc Step 1, thay cho list don cu): (a) **Disposition** (quyet bai Python di dau): `KEEP / MERGE / SPLIT / REWRITE / EXCLUDE` (EXCLUDE bat buoc kem `exclude_reason`: `AGE_INAPPROPRIATE / NO_NATIVE_SCRATCH_EQUIVALENT / HIGH_IMPLEMENTATION_COST / LOW_PEDAGOGICAL_VALUE / DUPLICATE_CONCEPT / OUT_OF_SCOPE / PRINT_COMPLEXITY`); (b) **Transformation mechanism** (chuyen kieu gi): `DIRECT / STRUCTURAL_MAPPING / ALGORITHMIC_RECONSTRUCTION / SIMPLIFY / EXTEND` — **nguyen tac: mechanism mo ta cach chuyen doi, khong mo ta do kho su pham** (vi du `x**3 → repeatNhan` la ALGORITHMIC_RECONSTRUCTION nhung van co the la bai Core de, khong tu dong thanh EXTENSION/CHALLENGE); (c) **Semantic status** (ket qua ngu nghia): `SEMANTIC_PRESERVE / SEMANTIC_PARTIAL / SEMANTIC_CHANGE`. Bo nhan `PRESERVE` tran. `SEMANTIC_MAPPING` cu hieu la `STRUCTURAL_MAPPING`; cho phep 1 bai mang 2 nhan mechanism (vi du for-range vua STRUCTURAL_MAPPING vua ALGORITHMIC_RECONSTRUCTION). Xuong muc concept/problem, khong gan 1 nhan/lesson.
- G0.3. Quy tac ID + versioning (P0, chot truoc khi tao artifact hang loat): quan he `IKH-xxxx` (global unique) ↔ `prob_*` (language-neutral) ↔ `pya_*` (Python hien co) ↔ ma Scratch (`SC-...`); version schema/contracts.
- G0.4. Rubric CORE/EXTENSION/CHALLENGE/EXCLUDE theo do tuoi 8–11.
- G0.5. Output target: `digital|print|both` — OPTIONAL/DEFERRED. Chua can block Step 1; chi bat buoc truoc Step 6.

Assumptions tam thoi: `ASM-S01`: giu 5 chuong/14 bai Python lam source map, NHUNG Python la source curriculum, khong phai template bat buoc — output Scratch co the khac so lesson (vi du 12 lessons, hoac B05 tach B05.1/B05.2, B14 tach Core/Challenge); `ASM-S02`: Scratch Level 1 uu tien tu duy thuat toan hon bao phu API; `ASM-S03`: DSL dang text scratchblocks-compatible.
- Nguyen tac P0 (source fidelity ≠ structural fidelity): Scratch trung thanh voi learning objectives/concepts/intended difficulty/problem semantics; khong bat buoc trung thanh voi so lesson, so exercise, thu tu tuyet doi, Python API, Python implementation.
- Nguyen tac cao nhat: khong hoi "Lam the nao de chuyen Python nay sang Scratch?" truoc khi hoi "Hoc sinh can hoc duoc dieu gi tu bai Python nay?" → `Learning Objective → Concept → Problem Semantics → Scratch Representation → Pedagogical Scaffolding → DSL → Validation → Render`.

### 1b. Bo sung P0 tu review ngoai (bat buoc truoc lock)

1. **Curriculum Contract** (tra loi: Scratch Level 1 muon hoc sinh dat duoc gi): `id/title/target_age/target_grade/pedagogical_goal/source_curriculum/chapters/lessons/core_competencies/excluded_competencies`. Neu thieu tang nay, 287 bai dung van chua chac thanh khoa hoc tot. Vi tri: Step 0.
2. **Coverage Matrix** (Python concept → Scratch concept → Core/Extension/Challenge/Exclude + status mapped/reconstructed/optional/excluded). Nhin coverage toan cuc khong can doc 287 bai. Vi tri: Step 2.
3. **Semantic Equivalence Contract** (the nao la "bai Scratch tuong duong" bai Python): khong so `stdout == say text` may moc. Dinh nghia: Problem Contract → Input Scenario → Scratch Interaction (ask/answer/say) → State Changes → Expected Final State/Output; cho phep lech formatting (vi du `say "40"` vs `say "Ket qua la 40"` deu co the dung). **Bat dau tu Step 1 duoi dang tieu chi chap nhan so bo (`expected_behavior` trong moi Problem Contract), formalize day du + Golden o Step 5.**
4. **Khong mac dinh 287 → 287 (design principle).** Ap **Disposition** `KEEP/MERGE/SPLIT/REWRITE/EXCLUDE` cho tung bai (thay cho cum Preserve/Transform/Merge/Exclude cu); **Transformation mechanism** ghi rieng theo G0.2. Output co the 240/310/khac. KPI la coverage, progression, age-appropriateness, algorithmic depth, quality, dedup, difficulty progression — khong phai so luong.
5. **Packaging + canonical vs generated (P1.2):** giu architecture nhung gom theo lesson (`lesson.yaml + problems.yaml + exercises.yaml + blocks.yaml + solutions/`) thay vi hang nghin file. Phan biet cung: `solution.dsl + Ly_Thuyet/Bai_Tap/De_Bai` la canonical; `*.svg/*.png/DOCX/PDF` la generated — cam sua render tay (sua SVG thay DSL la anti-pattern). Chot truoc Step 3.

### 1c. Khung khoa hoc/lesson/problem bat buoc theo source (end-to-end, khong chi pipeline giua)

Plan truoc day focus vao transformation pipeline (giua). Phan nay bo sung dau (course/lesson content) va cuoi (book/print/QA) theo dung skill `ikhedu-authoring` + template repo hien co, ap cho khoa Scratch `courses/scratch-bang-a/` (ten du kien, chot o Step 0):

1. **Course scaffolding (theo `group-index-template` + Brief Step A):**
  - `courses/scratch-bang-a/README.md`: dieu huong nhom (doi tuong 8–11, muc tieu, learning path 5 chuong/14 bai du kien, file map, assessment map, status). Khong copy toan bo lesson vao README.
  - `courses/scratch-bang-a/BOOK_MASTER.md` (neu xuat ban sach, theo `book-master-template`): ban thao canonical duy nhat; lesson/problem la artifact ho tro, noi dung xuat ban dong bo vao master trong cung tac vu. Word/PDF la dan xuat, khong thanh source moi.
  - `CURRICULUM_AUDIT.md` + `reference/KIEN_THUC_TRONG_TAM_CAN_NHO.md` + `assets/*.svg` (hinh block Scratch render local, co caption/so thu tu/nguon/vi tri tham chieu).
2. **Lesson package (theo `lesson-package-template`, 2 file bat buoc + code):**
  - `lessons/lesson-XX/LessonXX_Production_Content.md` (= `Ly_Thuyet.md` vai tro): cau truc ap cho Scratch — Muc tieu + prerequisite → Van de thuc te (san khau/nhan vat) → Y nghia → Khoi lenh/mohinh (block nao, o nhom nao, hinh dang gi) → Vi du nho + DSL + hinh render → Bang chay thu (buoc/bien/answer/thong diep) → Bay loi kinh dien (answer overwrite, bien chua khoi tao, off-by-one, list index 1-based, dieu kien repeat-until nguoc) → Tu kiem tra → Tom tat + link `Bai_Tap.md`. Tuan tu tang dan: thao tac truc tiep → bien the. Khong dua loi giai day du vao ban hoc sinh neu muc tieu tu giai.
  - `lessons/lesson-XX/Bai_Tap.md`: theo mau `Bai X.Y` (Muc tieu/LO — Yeu cau — Input Scenario/Expected final state — Vi du — Goi y muc 1 — Tieu chi tu kiem tra), phan tang P0→P3 nhu khoa Python (P0 khoi dong, P1 co ban, P2 luyen tap, P3 van dung), moi bai gan LO + do kho + ma bai. **P0–P3 (difficulty/progression) va Observe/Arrange/Complete/Create (cognitive support: high→low) la hai truc doc lap (P0.3); cam dong nhat P0=Observe... Bai_Tap ghi ca hai chieu cho moi bai.**
  - Code tham chieu: `solution.dsl` (canonical) + hinh render `*.svg/png` (generated) + (neu can) file `.sb3` tham khao; khong de AI ve SVG tay.
3. **Problem package Scratch (mo rong `problem-package-template`, khong ep giong het Python/C++):**
  - Cay chuan: `problems/sca_l01_pXX_ten-bai/De_Bai.md + Huong_Dan_Giang_Day.md + solution.dsl (+ render) + interaction-check/ (thay cho test/ console)`.
  - `De_Bai.md` (student-facing, khong spoil): Tieu de goi hinh doi song → Boi canh san khau → Nhiem vu (Cho... Hay lap trinh...) → Input Scenario (ask may lan, dieu kien) → Output/State mong doi (say/the doi bien, chap nhan lech formatting theo Semantic Equivalence Contract) → Sample (Input scenario + Hanh vi Scratch + Giai thich trace tay, cam spoil ten thuat toan) → Rang buoc (mien gia tri, so lan lap toi da). Cam dong `Ma bai toan`/code trong statement; ma chi o identity/ten thu muc/metadata.
  - `Huong_Dan_Giang_Day.md` du 9 phan theo rule 02 (Objectives → Phan tich & Edge → Socratic → Chien luoc & Invariant → Dry-run table → Complexity O → Bug traps → Code DSL tham chieu → Transfer), code DSL tuan Block Contract + validation.
  - `interaction-check/`: thay `test/*.in/*.out` console bang kich ban kiem thuong tac (input scenario → state/output ky vong + pham vi coverage sample/min/max/boundary/degenerate/adversarial); manifest mo ta quy uoc + reproduction; khong gan `verified` neu chua chay/doi chieu that.
4. **Mapping skill workflow A→F ap cho moi lesson Scratch:** A Brief (document_type/output_target/audience/level/LO/thoi luong/license/reviewer/status; tach ASM) → B Master + source map (BOOK_MASTER + source-index/evidence-ledger cho moi claim) → C Architecture + backward design (LO → evidence/assessment → activities; chapter/prerequisite map; khong LO thua, khong content thua) → D Draft theo profile (lesson/problem nhu tren) → E Print-ready gate neu output print/both (khau Word spec + proof) → F Review gates + Handoff (Status/Scope/Master path/Assumptions/Sources/Changed/Evidence/Unresolved/QA/Next; cap nhat decision-log/open-questions/evidence-ledger/project-context).
5. **Chuoi lien ket bat buoc truoc release:** Lesson `README → Ly_Thuyet → Bai_Tap → code(DLS/render)/interaction-check`; Problem `De_Bai → Huong_Dan_Giang_Day → solution.dsl → interaction-check`. Moi thay doi Ly_Thuyet (block/API) phai ra lai Bai_Tap + solution; thay doi Bai_Tap phai ra lai LO + solution.

## 2. Plan chi tiet tung step

### Step 0A — Source Inventory (fact-finding, khong sang tac)

- Muc tieu: xac nhan source-of-truth, dem/scan that B01–B14 tu `python-level-1.docx`, ghi nhan docx nao la canonical (dang co 4 file `.docx`/`.bak` trong `courses/python-bang-a/`).
- Input: cac file docx + README khoa Python + MASTER_ALL_LESSONS (neu dung).
- Output: `S00_source-inventory.md` (file/bai/problem count verify that, khong copy so lieu summary khi chua dem) + dang ky source IDs moi vao source-index.
- Gate: so luong 5/14/287 chi duoc khang dinh sau khi dem that; thieu/xung dot → dung va hoi. Chua xong 0A thi khong sang 0B.

### Step 0B — Project / Course Contract (thiet ke output ton tai the nao)

- Muc tieu: chot G0.1–G0.4 (G0.5 deferred) + draft Curriculum Contract + course slug + cay thu muc + file canonical (muc 1c.1).
- Gate: chua co course slug/cay file thi khong sang Step 1.

### Step 1 — Problem Contract + Concept Map + Source Trace (tren giay, chua DSL)

- Muc tieu: mo ta bai toan (khong mo ta cach giai Scratch), gan learning_objectives, algorithmic_concepts, constraints, testcases, disposition + transformation mechanism + semantic status (G0.2), source_trace, va **tieu chi chap nhan ngu nghia so bo `expected_behavior`** (P0.4: Input Scenario → Scratch Interaction → State Changes → Expected Final State).
- Output mau: 3–5 contract B01; pedagogy khong nam o day.
- Gate: moi contract phai trace duoc Scratch → Exercise → Problem → Python problem/lesson/file. ID language-neutral + mapping ve `IKH-xxxx`.
- Trao doi sau: duyet 3–5 contract mau cua B01 truoc khi lam hang loat.

### Step 2 — Transformation Spec (semantic mapping + algorithmic reconstruction)

- Muc tieu: dinh nghia operational cho Disposition + Transformation mechanism + Semantic status (G0.2); liet ke primitive Scratch thuc te; quyet B03/B04/B05/B06/B11–B14 theo tung concept (khong nhan ca lesson 1 nhan).
- Output: bang mapping concept-level + **Coverage Matrix** (muc 1b.2) + **Pattern Contract/Pattern Library** (P1.1: `id/concept/purpose/preconditions/blocks/invariant/dry_run_template/common_mistakes`; Block Contract noi block lam gi, Pattern Contract noi dung block the nao; taxonomy Pattern Library theo hierarchy: CONTROL FLOW → FOR/COUNTED LOOP (`repeat N`, counter, accumulator, range-like progression, off-by-one bug pattern) / WHILE/CONDITION-CONTROLLED (`sentinel`, flag, `repeat until`, termination condition) — counter/accumulator la variable/state pattern, off-by-one la bug pattern, khong de ngang hang tuy tien) + quy tac: primitive-first; khong tu bien moi thu thanh loop; flag/sentinel/loop_counter/accumulator/off-by-one/nested-loop pattern; list index 0-based→1-based note; string slicing → `letter/length` reconstruction. Bang B03 toi thieu: `+,-,*,/` direct; `%→mod` direct; `//→floor+division` mapping (kiem behavior that so nguyen/am/rounding/float, don gian hoa neu Level 1 chi so nguyen duong); `**→algorithmic/extension` (quyet rieng, khong cam tinh). Pattern Library la canonical — AI chi chon pattern phu hop, khong tu phat minh neu concept da co pattern chuan (dac biet B05/B06: for/range/counter/accumulator/nested/off-by-one).
- Gate: B05 (for/range) va B06 (while/flag, `repeat until` + dao dieu kien) phai co pattern chuan + dry-run mau.
- Trao doi sau: chot tu dien + pattern library + coverage matrix.

### Step 3 — Scratch Model: Lesson Contract + Exercise Instance + Block Contract + DSL

- Muc tieu: Lesson Contract mo ta lesson experience; Exercise Instance mo ta tung dang Observe/Arrange/Complete/Create; Block Contract mo ta signature; DSL la representation canonical cua code.
- Quy tac: Observe→Arrange→Complete→Create la muc do ho tro nhan thuc (cognitive support), khong phai format bat buoc; pedagogy level nam o Exercise + teaching_sequence; skeleton Complete phai ro cho trong; Create chi dung khi concept da quen. Packaging theo muc 1b.5 (gom yaml theo lesson, khong phan manh file).
- Block Contract toi thieu de validator dung duoc: `id/opcode/category/shape/inputs(name/type/required)/output(type)/body(type)/constraints`. Phai mo ta duoc `if/repeat/repeat until/forever/set/change` chua gi, nam dau, noi the nao.
- Gate: 1 Lesson Contract mau (nen la B01) + 2–3 Exercise mau + toi thieu Block Contracts cho blocks duoc dung + DSL tuong ung + **draft `LessonXX_Production_Content.md` + `Bai_Tap.md` + 1 problem package Scratch mau (De_Bai/Huong_Dan/solution.dsl/interaction-check) theo muc 1c.2–1c.3**. Contract machine-readable (yaml) co the gom theo lesson de tranh phan manh, nhung noi dung hoc sinh (Ly_Thuyet/Bai_Tap/De_Bai) bat buoc la file .md rieng theo template.
- Trao doi sau: duyet B01 end-to-end tren giay truoc khi render.

### Step 4 — Validation Layer (spec + rule test, lam that nhung gon)

- Muc tieu: validator 4 tier, khong xay "Scratch compiler" hoan chinh ngay: Tier 1 Structural (block ton tai/shape/nesting/input) → Tier 2 Type (Boolean/Number/String/Variable/List) → Tier 3 Pedagogical semantic (answer overwrite, init bien, loop kha nang sai) → Tier 4 Runtime semantic (chi lam sau khi co ROI).
- Quy tac bien theo loai (thay cho chu `index` chung chung): `accumulator → REQUIRE explicit init; loop_counter → REQUIRE hoac strong WARNING; flag → REQUIRE explicit init; list_index → rule rieng (chu y 1-based); temporary_variable → tuy context`. `repeat until <number>` → REJECT; ask→consume/store→next ask.
- Output: bo rule test (pass/fail vi du cu the) chay duoc bang tay hoac script don gian.
- Trao doi sau: duyet rule list + vi du vi pham.

### Step 5 — Golden Spec / Golden Test (Phase 0.5)

- Muc tieu: viet/duyet thu cong 1 bo reference nho (B01 core + 1 mau B05 loop + 1 mau B14 boundary). Golden la **reference behavior** (contract + semantics + pedagogical constraints), khong phai reference implementation — khong compare string DSL; hai solution khac nhau van deu dung neu cung dat contract.
- Gate: golden gom Problem Contract + Lesson Contract + Exercise + DSL + dry-run + expected validation result + **Semantic Equivalence Contract formal** (muc 1b.3, ke thua `expected_behavior` tu Step 1).
- Trao doi sau: chot golden + semantic equivalence truoc khi cho AI gen hang loat.

### Step 6 — Rendering + Publishing proof (B01 that)

- Muc tieu: chay that `DSL → scratchblocks-cli (pin version) → SVG(/PNG fallback) → embed DOCX → PDF`; kiem tra font/spacing/caption/so thu tu/in xam/tran le theo Word spec + QA checklist. Dong bo noi dung B01 vao `BOOK_MASTER.md` trong cung tac vu (theo book-master-template + maintenance rules); Word/PDF la dan xuat.
- Output: 1 Lesson B01 proof (Ly_Thuyet + Bai_Tap + problem mau + render) + bao cao QA (blocker/major/minor/polish) + phu luc embed Scratch (khong sua spec goc khi chua approve).
- Gate: chi goi `print-ready`/`final` khi het blocker/major + human review theo skill + **release consistency: artifact hien tai OK va moi dependency (Bai_Tap/solution.dsl/SVG/BOOK_MASTER) deu pass, cross-artifact khop** (muc 1c.5).
- Trao doi sau: duyet proof giay/in thu roi moi sang B05.

### Step 7 — Stress-test B05 roi B14, G-SCALE audit, sau do scale

- Xem B01/B05/B14 nhu 3 validation dimensions (nen / control-algorithm / language-limitation), khong nhat thiet 3 phase tuyen tinh hoan toan. Moi bai lap lai Step 1–6 o quy mo hep.
- Quy tac so luong (muc 1b.4): khong mac dinh 287 → 287. Ap **Disposition** `KEEP/MERGE/SPLIT/REWRITE/EXCLUDE` cho tung bai; EXCLUDE dung cung la ket qua curriculum tot (dac biet B14).
- **G-SCALE — Curriculum Audit + release gate that (GO/REWORK, truoc scale hang loat):** flow `B01 proof → B05 stress → B14 stress → G-SCALE audit → GO/REWORK → Scale B01–B14`. Kiem: thieu concept? lap thua? lesson qua dai? vuot tuoi? API Python bi ep? gap algorithm/pedagogy? difficulty jump? Neu fail → REWORK ve step tuong ung (thieu pattern → Step 2; DSL loi → Step 3/4; semantic equivalence → Step 5; render loi → Step 6; curriculum qua dai → Step 0B/2/3). Chi scale khi pipeline pass + audit pass.
- **Change Impact Matrix (QA governance):** Lesson objective → Lesson+Exercises; Block/API explanation → Lesson+Exercises+Solution; Problem statement → Solution+Interaction Check; Solution DSL → SVG+DOCX/PDF; Block Contract → all dependent DSL; Transformation rule → all affected Problems; Curriculum objective → Lesson/Exercise coverage.
- Output cuoi: course README + BOOK_MASTER dong bo + lesson packages (Ly_Thuyet/Bai_Tap/code, so lesson theo audit, khong mac dinh 14) + problem packages Scratch + Contracts + DSL validated + SVG/DOCX/PDF/Web tu single source. Moi step co handoff A→F (muc 1c.4) + QA checklist.

## 3. Thu tu trao doi de xuat (moi lan 1 step)

1. Step 0A (inventory) → 2. Step 0B (G0 + course contract) → 3. Step 1 (contract mau B01 + expected_behavior) → 4. Step 2 (pattern/coverage) → 5. Step 3 (lesson/exercise/DSL B01) → 6. Step 4 (rules) → 7. Step 5 (golden) → 8. Step 6 (proof in) → 9. Step 7 (B05, B14, G-SCALE audit, scale). Khong them abstraction lon moi; chuyen sang evidence mode tu Step 0A.

## 4. QA gates ap dung moi step

- Source/provenance → fact/logic → correctness → alignment su pham → scaffolding → thuat ngu → ngon ngu → license/attribution → cross-artifact consistency.
- Loi theo `blocker|major|minor|polish` kem vi tri + bang chung. Chua dat → `draft/review-needed/blocked`, khong dung `final`.

## 5. Open questions (can chu du an quyet)

- `Q-S01`: Profile Scratch chinh thuc + quan he `IKH-xxxx`/`prob_*`/`pya_*`?
- `Q-S02`: File docx Python nao la canonical trong 4 file hien co?
- `Q-S03`: Output target (`digital|print|both`) + kho giay neu in?
- `Q-S04`: Nguong EXCLUDE cu the cho B14 (ASCII/ord/chr/split/join...)?
- `Q-S05`: Cach map testcase console → hanh vi Scratch (`ask/say`) de kiem semantic equivalence?
- `Q-S06`: Pin version scratchblocks-cli + font thay the khi in?
