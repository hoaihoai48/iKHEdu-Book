---
name: 00-ikhedu-router
version: 2.1.0
priority: P0
trigger: always_on
---

# iKHEDU Router — Always On

Khi yêu cầu liên quan đến sách, giáo trình, chương, bài, lesson, module, README học liệu, bài tập, problem, teacher guide, solution, testcase, curriculum, assessment, tài liệu in: TỰ ĐỘNG áp dụng toàn bộ rule `0*.md` trong thư mục này + skill `ikhedu-authoring`, không cần user gọi tay.

Thứ tự đọc bắt buộc trước khi viết/sửa:

1. `.agents/context/project-context.md`
2. `.agents/context/source-index.md`
3. `.agents/context/evidence-ledger.md`
4. `.agents/context/decision-log.md`
5. `.agents/context/open-questions.md`
6. `docs/MASTER_MODULE_01_DESIGN.md` (Golden Spec, Curriculum Architecture v2)
7. Chỉ đọc phần liên quan của source trong source-index (read-only, không bịa citation/số liệu/test result).

Chi tiết xem thêm:
- `01-code-standards.md` — boilerplate C++/Python, KaTeX, Not Yet Boundary, learning loop
- `02-problem-package.md` — De_Bai 7 mục, Teacher Guide 9 phần, solution/test
- `03-print-publish.md` — spec Word DOCX in ấn + QA gate

Nếu thiếu context, source xung đột, hoặc quyết định quan trọng chưa rõ: dừng và hỏi chủ dự án. Phân cấp 5 tầng bắt buộc: PROGRAM -> MODULE -> LESSON -> CONCEPT -> ACTIVITY/PROBLEM. `IKH-xxxx` là mã global duy nhất; Lesson chỉ tham chiếu (Placement), không duplicate.
