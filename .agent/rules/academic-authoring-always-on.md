---
name: academic-authoring-always-on
version: 2.0.0
priority: P0
trigger: always_on
---
# iKHEDU Authoring — Always On

Khi yêu cầu liên quan đến sách, giáo trình, chương, bài, lesson, module, README học liệu, bài tập, problem, teacher guide, solution, testcase, curriculum, assessment hoặc tài liệu để in, **tự động áp dụng skill `ikhedu-authoring`**. Không yêu cầu người dùng gọi lại skill/workflow cho từng tin nhắn.

Trước khi viết hoặc sửa, luôn đọc theo thứ tự:

1. `@../context/project-context.md`
2. `@../context/source-index.md`
3. `@../context/evidence-ledger.md`
4. `@../context/decision-log.md`
5. `@../context/open-questions.md`
6. Chỉ đọc phần liên quan của source được đăng ký trong `source-index.md`.

Luôn coi các source project đã đăng ký là read-only và source-of-truth. Phân biệt dữ kiện có nguồn, suy luận của tác giả và ví dụ minh họa. Không bịa citation, số liệu, quote, test result hoặc trạng thái verified. Nếu thiếu context, source xung đột hoặc quyết định quan trọng chưa rõ, dừng và hỏi chủ dự án.

Trước khi tạo output, xác định `output_target: digital|print|both` và chọn profile `group-index`, `chapter-module`, `lesson-package` hoặc `problem-package`. Tổ chức theo cấu trúc sách → phần → chương → bài/lesson → mục → bài tập khi yêu cầu là giáo trình.

Mỗi cuốn sách/giáo trình phải có **một và chỉ một** bản thảo tổng hợp canonical là `BOOK_MASTER.md` ở book root. Mọi nội dung dành để xuất bản phải được đưa vào master theo đúng thứ tự phần–chương–bài; README, lesson, teacher guide, solution và testcase chỉ là artifact hỗ trợ, không tạo thêm bản thảo song song. Nếu đã có master thì cập nhật nó, không tạo master thứ hai.

Với `problem-package`, luôn đọc `@../skills/ikhedu-authoring/references/testcase-generation-standard.md` và tạo theo chuỗi `De_Bai.md → Huong_Dan_Giang_Day.md → solution.cpp → test/`. Test phải có test matrix, generator deterministic, seed cố định, oracle độc lập, `manifest.json`, `.inp/.out`, timeout, coverage và test report. Không dùng solution đang kiểm thử làm oracle duy nhất.

Với `print|both`, đọc `@../skills/ikhedu-authoring/references/print-production-spec-template.md`, chốt khổ sách/lề/gutter/font/caption/header/footer, giữ một bản canonical, render proof và không gọi là `print-ready` khi chưa kiểm tra dàn trang và có human proof review.

Trước khi bàn giao, chạy `@../skills/ikhedu-authoring/references/qa-checklist.md`, cập nhật evidence ledger/decision log/open questions khi cần, kiểm tra `BOOK_MASTER.md` là bản duy nhất dùng để convert sang Word/PDF, và ghi rõ `Status`, `Scope`, `Master path`, `Sources`, `What changed`, `Unresolved issues`, `QA gates`, `Next action`. Chỉ dùng `final` khi các cổng QA phù hợp đã đạt.

Nếu yêu cầu không liên quan đến học liệu, không ép áp dụng quy trình này.
