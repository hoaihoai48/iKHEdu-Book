# ikhEdu_lessons — Agent Rules (Antigravity / Cursor / Claude / Opencode)

> File này để agent TỰ ĐỘNG đọc mỗi session. Chi tiết đầy đủ nằm trong `.agents/` (Antigravity) và `.agent/` (Opencode, giữ song song).

## 1. Auto-trigger (bắt buộc, không cần user gọi tay)

Khi task liên quan đến sách, giáo trình, chương, bài, lesson, module, README học liệu, bài tập, problem, teacher guide, solution, testcase, curriculum, assessment, tài liệu in:

1. Đọc `.agents/rules/00-ikhedu-router.md` rồi đọc tiếp `01-code-standards.md`, `02-problem-package.md`, `03-print-publish.md`.
2. Đọc `.agents/skills/ikhedu-authoring/SKILL.md` + đúng reference theo profile (lesson/problem/chapter/qa/print/testcase).
3. Đọc theo thứ tự `.agents/context/project-context.md` → `source-index.md` → `evidence-ledger.md` → `decision-log.md` → `open-questions.md` → `docs/MASTER_MODULE_01_DESIGN.md` (Golden Spec).
4. Chỉ dùng source đã đăng ký trong source-index; giữ source read-only; không bịa citation, số liệu, test result, trạng thái verified. Thiếu/xung đột → dừng và hỏi.

## 2. Tóm tắt chuẩn không được phá

- Phân cấp 5 tầng: PROGRAM → MODULE → LESSON → CONCEPT → ACTIVITY/PROBLEM. `IKH-xxxx` là mã global duy nhất; Lesson chỉ tham chiếu.
- C++: `#include <bits/stdc++.h>`, `using namespace std;`, Fast I/O, safe input `if (!(cin >> ...)) return 0;`, cấm `std::`, cấm header lẻ.
- Python: `solution.py` dùng `input()`/`print()`, cấm `sys`/`main`; không tạo `test/` mặc định.
- De_Bai cấm spoil thuật toán trong Giải thích (chỉ trace tay). Teacher Guide đủ 9 phần. Lesson đủ chuỗi README → Ly_Thuyet → Bai_Tap → code/test.
- Word DOCX theo `docs/MASTER_WORD_BUILD_SPECIFICATION.md`; QA theo `qa-checklist.md`; chỉ gắn `final` khi hết blocker/major + đủ human review.

## 3. Tương thích tool

- Antigravity đọc `AGENTS.md` + `GEMINI.md` + `.agents/rules/*.md` + `.agents/skills/*/SKILL.md` (mỗi file <12.000 ký tự).
- Opencode đọc `.agent/` (giữ mirror song song với `.agents/`).
- Nguồn read-only: `IKHEDU_Knowledge_Base.md`, `ikhEdu_foundation_framework_report.md`, `Lo_trinh_hoc_tap_bangB_level1.jpg`.
