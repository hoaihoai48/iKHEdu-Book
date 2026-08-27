# Write Book / Textbook

## Description

Chạy quy trình có kiểm soát để tạo hoặc sửa một sách, giáo trình, module, chapter hoặc tài liệu đào tạo dựa trên source của workspace.

## Preconditions

Đọc các tệp sau trước khi làm: `@../context/project-context.md`, `@../context/source-index.md`, `@../context/evidence-ledger.md`, `@../context/decision-log.md` và `@../context/open-questions.md`. Nếu các tệp chưa được điền, tạo một brief thiếu dữ liệu và hỏi các câu hỏi chặn; không tự bịa context.

## Steps

1. Xác định `document_type`, độc giả, trình độ, mục tiêu, phạm vi, ngôn ngữ, độ dài, chuẩn đầu ra, citation style, license và reviewer. Ghi giả định bằng mã `ASM-...`.
2. Kiểm tra source-of-truth và lập/ cập nhật `source-index.md`. Đọc just-in-time các source liên quan; không nạp toàn bộ corpus nếu không cần.
3. Lập kiến trúc: mục lục, chapter/module map, prerequisite map và danh sách thuật ngữ. Với học liệu, làm backward design: outcomes -> evidence/assessment -> activities/content.
4. Tạo ma trận alignment. Bảo đảm mỗi learning outcome có assessment/evidence và mỗi phần nội dung có mục đích.
5. Viết hoặc sửa từng chapter/section theo `@../skills/academic-book-authoring/references/chapter-template.md`. Đánh dấu claim bằng `CLAIM-...`; cập nhật evidence ledger ngay khi dùng source.
6. Chạy review nhiều lớp: source/fact; chuyên môn; logic; pedagogy/alignment; terminology; language; accessibility; copyright/license. Ghi lỗi theo severity và không gọi output là final khi còn blocker/major.
7. Đọc và hoàn thành `@../skills/academic-book-authoring/references/qa-checklist.md`. Đối chiếu glossary, cross-reference, bảng/hình, câu hỏi và đáp án.
8. Cập nhật `decision-log.md`, `open-questions.md`, evidence ledger và changelog/status. Ghi rõ phần chưa xác minh, conflict, cần human review và bước tiếp theo.
9. Bàn giao theo hợp đồng: `Status`, `Scope`, `Assumptions`, `Sources consulted`, `What changed`, `Evidence/citations`, `Unresolved issues`, `QA gates`, `Next action`.

## Branches

Nếu người dùng chỉ yêu cầu copyedit, bỏ qua redesign nhưng vẫn chạy context, source và consistency checks. Nếu người dùng yêu cầu research/literature review, ưu tiên evidence cards và citation verification trước khi synthesis. Nếu source xung đột hoặc quyền sử dụng không rõ, chuyển trạng thái `blocked` hoặc `needs-human-review`; không tự quyết.

## Completion criteria

Hoàn tất khi output đúng loại tài liệu, bám project context, có provenance cho claim quan trọng, đạt alignment, qua QA phù hợp và trạng thái phản ánh trung thực mức độ hoàn thành. Nếu chưa đạt, bàn giao draft/review-needed/blocked cùng danh sách việc còn lại.
