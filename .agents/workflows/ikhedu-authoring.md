# iKHEDU Authoring

## Description

Kích hoạt quy trình biên soạn và kiểm định iKHEDU cho sách, giáo trình, lesson, module, README nhóm, bài tập, problem statement, teacher guide, solution và test. Workflow này nạp skill `ikhedu-authoring`, bắt buộc đọc context/source của project và chọn đúng khuôn trước khi tạo hoặc sửa nội dung.

## Steps

1. Đọc `@../skills/ikhedu-authoring/SKILL.md` trước khi làm bất kỳ thao tác nội dung nào.
2. Đọc theo thứ tự `@../context/project-context.md`, `@../context/source-index.md`, `@../context/evidence-ledger.md`, `@../context/decision-log.md` và `@../context/open-questions.md`.
3. Xác nhận loại tác vụ: `group-index`, `lesson-package`, `problem-package`, `chapter-module`, `review`, `research` hoặc `release`. Nếu audience, level, source, license hoặc reviewer còn thiếu và có thể làm đổi đầu ra, dừng để hỏi chủ dự án.
4. Với `group-index`, đọc `@../skills/ikhedu-authoring/references/group-index-template.md`. Với `lesson-package`, đọc `@../skills/ikhedu-authoring/references/lesson-package-template.md`. Với `problem-package`, đọc `@../skills/ikhedu-authoring/references/problem-package-template.md`. Với `chapter-module`, đọc `@../skills/ikhedu-authoring/references/chapter-template.md`.
5. Chỉ dùng ba source project được đăng ký trong source index: `IKHEDU_Knowledge_Base.md`, `ikhEdu_foundation_framework_report.md` và `/Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level1.jpg`. Giữ chúng read-only. `DKTECHVN/ebook-ikh` chỉ là reference cấu trúc `REF-001`, không dùng làm source-of-truth và không sao chép nội dung.
6. Thực hiện brief → source map/provenance → architecture/backward design → draft theo profile → review gates → QA → handoff. Mỗi claim quan trọng phải có evidence trong `evidence-ledger.md`; không bịa citation, số liệu, test result hoặc trạng thái verified.
7. Khi tạo lesson, giữ chuỗi `README/index → Ly_Thuyet.md → Bai_Tap.md → code/test`. Khi tạo problem, giữ chuỗi `De_Bai.md → Huong_Dan_Giang_Day.md → solution.cpp → test/`.
8. Trước khi hoàn tất, đọc và áp dụng `@../skills/ikhedu-authoring/references/qa-checklist.md`. Chỉ dùng trạng thái `final` khi không còn blocker/major chưa được chấp nhận và human review cần thiết đã xong.
9. Bàn giao theo các mục: `Status`, `Scope`, `Assumptions`, `Sources consulted`, `What changed`, `Evidence/citations`, `Unresolved issues`, `QA gates`, `Next action`. Cập nhật decision log, open questions, evidence ledger và project context khi phù hợp.
