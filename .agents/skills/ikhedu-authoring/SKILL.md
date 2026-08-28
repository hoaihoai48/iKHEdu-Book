---
name: ikhedu-authoring
description: Biên soạn và kiểm định nội dung iKHEDU gồm sách, giáo trình, lesson, module, README nhóm, bài tập, problem statement, teacher guide, solution và test. Dùng khi người dùng yêu cầu tạo, sửa, nghiên cứu, dịch, lập curriculum, viết giáo án, thiết kế bài toán hoặc phát hành học liệu trong project ikhEdu_lessons; luôn đọc context/source trước khi viết.
license: Proprietary project skill; use with project owner approval
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
metadata:
  version: "1.0.0"
  when_to_use: "Khi tạo, sửa, nghiên cứu, dịch, review hoặc phát hành sách, giáo trình, lesson, module, README nhóm, problem statement, teacher guide, solution hoặc test trong project ikhEdu_lessons."
  domain: "ikhedu-educational-authoring"
  language: "vi"
---

# iKHEDU Authoring

Làm việc như một nhóm gồm chủ biên, chuyên gia môn học, instructional designer, giáo viên, copy editor và reviewer. Mục tiêu không phải chỉ tạo văn bản hay code, mà là tạo học liệu **đúng source, đúng người học, đúng cấu trúc, có thể kiểm tra và có trạng thái trung thực**.

## 1. Luật nạp context — bắt buộc trước mọi thao tác

Đọc theo thứ tự:

1. `../../context/project-context.md`
2. `../../context/source-index.md`
3. `../../context/evidence-ledger.md`
4. `../../context/decision-log.md`
5. `../../context/open-questions.md`
6. Chỉ đọc phần liên quan của source được source index chỉ ra.

Trong `ikhEdu_lessons`, ba source nội dung project là:

- `IKHEDU_Knowledge_Base.md` — nguồn tham chiếu nội bộ/read-only.
- `ikhEdu_foundation_framework_report.md` — nguồn định hướng curriculum/read-only.
- `/Users/vu/Developer/ikhEdu_lessons/Lo_trinh_hoc_tap_bangB_level1.jpg` — roadmap/read-only.

`DKTECHVN/ebook-ikh` là `REF-001`, chỉ là reference-only cho cấu trúc; không lấy nội dung của nó làm sự thật và không tự sao chép nội dung vào project.

Nếu context thiếu, source không tồn tại, nguồn xung đột hoặc một quyết định chưa rõ có thể làm đổi nội dung, dừng và hỏi chủ dự án. Không lấp khoảng trống bằng trí nhớ hoặc văn phong chắc chắn.

## 2. Chọn đúng profile trước khi viết

| Profile | Mục đích | Artifact canonical |
|---|---|---|
| `group-index` | Điều hướng một nhóm có nhiều buổi/bài | `README.md` hoặc index cấp nhóm |
| `lesson-package` | Dạy khái niệm/buổi học | README/index, `Ly_Thuyet.md`, `Bai_Tap.md`, code tham chiếu, `test/` nếu có |
| `problem-package` | Bài toán chấm tự động | `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp`, `test/` |
| `chapter-module` | Chương/module tổng quát | `chapter-template.md` và ma trận alignment |

Không ép problem package vào lesson template. Không đưa lời giải đầy đủ vào statement học sinh. Nếu có `.docx` và `.md`, chọn một bản canonical và ghi trong source index.

Đọc reference tương ứng trước khi tạo file:

- `references/group-index-template.md`
- `references/lesson-package-template.md`
- `references/problem-package-template.md`
- `references/chapter-template.md`
- `references/qa-checklist.md`
- `references/print-production-spec-template.md` khi `output_target` là `print` hoặc `both`.

## 3. Quy trình chuẩn

### Bước A — Brief

Xác định `document_type`, `output_target` (`digital|print|both`), khổ thành phẩm nếu in, đối tượng, level, prerequisite, learning outcomes, thời lượng, ngôn ngữ, giọng điệu, phạm vi, format, license, reviewer và trạng thái. Tách yêu cầu đã xác nhận khỏi giả định bằng mã `ASM-...`. Nếu người dùng chỉ muốn sửa nhỏ, giữ nguyên ý định và không redesign ngoài phạm vi.

### Bước B — Source map và evidence

Đọc source index trước. Với mỗi claim quan trọng, ghi `claim_id`, `source_id`, path/URL, vị trí, paraphrase, loại claim, status `verified|partial|unverified|conflict`, giới hạn và nơi sử dụng vào evidence ledger. Không bịa citation, số liệu, DOI, trích dẫn hoặc vị trí. Claim chưa xác minh phải ghi `[CHƯA XÁC MINH]` hoặc không đưa vào phát hành.

### Bước C — Architecture và backward design

Làm theo thứ tự: learning outcomes đo được → evidence/assessment → activities/content. Tạo chapter/module map và prerequisite map. Không để outcome không có bằng chứng đánh giá; không để nội dung không phục vụ outcome nếu chưa giải thích lý do. Khi có nhiều buổi, cập nhật group README/index để liên kết buổi, chủ đề, file, bài tập, code/test và trạng thái.

### Bước D — Draft theo profile

`group-index`: README phải là lớp điều hướng, gồm mục tiêu nhóm, đối tượng, learning path, file map, assessment map và status; không sao chép toàn bộ nội dung lesson.

`lesson-package`: `Ly_Thuyet.md` đi theo ý nghĩa → cú pháp/mô hình → ví dụ nhỏ → code → lỗi/trường hợp biên → tự kiểm tra → tóm tắt. `Bai_Tap.md` tách riêng, dùng mã phân cấp như `Bài X.Y`, có mục tiêu, yêu cầu, Input/Output hoặc expected output, ví dụ, gợi ý và tiêu chí tự kiểm tra. Bài tập tăng dần từ thao tác trực tiếp đến bài biến thể.

`problem-package`: `De_Bai.md` gồm bối cảnh, nhiệm vụ, Input, Output, giới hạn, subtasks, samples và giải thích sample. `Huong_Dan_Giang_Day.md` gồm mục tiêu, prerequisite, phân tích đề, câu hỏi dẫn dắt, trực giác, invariant/correctness, complexity, misconception, code và bài transfer. `solution.cpp` phải khớp statement, xử lý boundary case, đúng complexity và không debug output. `test/` phải có mục đích test và manifest/coverage nếu project yêu cầu.

### Bước E — Print-ready gate

Nếu `output_target` là `print` hoặc `both`, coi bản in là một deliverable thật, không phải việc chuyển đổi sau cùng. Chốt trước khổ thành phẩm, hướng trang, lề trong/lề ngoài và gutter theo gáy, bleed nếu có, hệ màu, font được phép nhúng, quy tắc header/footer, đánh số trang, style heading, caption, bảng, code và ngắt chương. Không dùng khoảng trắng hoặc xuống dòng thủ công để dàn trang.

Giữ một bản nội dung canonical có cấu trúc; xem PDF/Word/LaTeX/InDesign là artifact dẫn xuất và ghi quan hệ đó trong source index. Chuẩn bị front matter (bìa, thông tin xuất bản, lời nói đầu nếu có, mục lục), body matter (chương/lesson/problem) và back matter (glossary, tài liệu tham khảo, đáp án/phụ lục nếu phạm vi cho phép). Mỗi hình/bảng phải có caption, số thứ tự, nguồn và vị trí tham chiếu; code và bảng không được tràn lề hoặc bị cắt khi xuất.

Trước khi gọi là `print-ready`, render bản proof và kiểm tra: mục lục/số trang; font nhúng; heading và cross-reference; không có trang trắng ngoài chủ ý; không có widow/orphan hoặc tiêu đề bị treo; hình/bảng/công thức/code không bị cắt; tương phản khi in xám; lề gáy; hyperlink/URL quan trọng; lỗi chính tả sau dàn trang. Kiểm tra trực quan các trang đầu, trang có bảng/hình/code dài, trang chuyển chương, trang chẵn/lẻ và trang cuối. Nếu có thể, in thử một tập mẫu và ghi kết quả proof vào báo cáo QA. Chỉ phát hành PDF sau khi có người duyệt proof.

### Bước F — Review gates

Kiểm tra theo thứ tự: source/provenance; fact và logic; correctness/code; alignment sư phạm; độ khó/scaffolding; thuật ngữ/ký hiệu; ngôn ngữ; accessibility; license/attribution; cross-artifact consistency. Ghi lỗi theo `blocker|major|minor|polish` với vị trí, bằng chứng và trạng thái sửa.

Đối chiếu các chuỗi liên kết:

- Lesson: `README → Ly_Thuyet → Bai_Tap → code/test`.
- Problem: `De_Bai → Huong_Dan_Giang_Day → solution.cpp → test/`.

Chỉ dùng `final` khi không còn blocker/major chưa được chấp nhận, claim quan trọng có provenance phù hợp, outcome–assessment–content đã alignment và human review cần thiết đã hoàn tất. Nếu chưa đạt, dùng `draft`, `review-needed` hoặc `blocked`.

### Bước F — Handoff

Mỗi lần bàn giao phải nêu: `Status`, `Scope`, `Assumptions`, `Sources consulted`, `What changed`, `Evidence/citations`, `Unresolved issues`, `QA gates`, `Next action`. Sau mốc lớn, cập nhật `decision-log.md`, `open-questions.md`, `evidence-ledger.md` và trạng thái trong `project-context.md` khi phù hợp.

## 4. Các lệnh làm việc có thể yêu cầu

- “Dùng `ikhedu-authoring` để lập brief cho …” → chỉ làm brief và câu hỏi chặn.
- “Dùng `ikhedu-authoring` để tạo lesson package …” → chọn `lesson-package` và đọc template liên quan.
- “Dùng `ikhedu-authoring` để tạo bài toán IKH-XXXX …” → chọn `problem-package` và tạo đủ statement/teacher guide/solution/test plan.
- “Dùng `ikhedu-authoring` để review …” → không viết lại ngay; lập review report có severity và provenance.
- “Dùng `ikhedu-authoring` để release …” → chạy QA gates, print-ready gate nếu `output_target` là `print|both`, cập nhật status/changelog và dừng nếu còn blocker.

## 5. Tiêu chí dừng

Dừng và hỏi chủ dự án khi source-of-truth thiếu hoặc xung đột nghiêm trọng; người dùng chưa chốt audience/level nhưng quyết định đó ảnh hưởng nội dung; quyền sử dụng không rõ; statement và solution không thể thống nhất; test chưa đủ để gọi verified; hoặc yêu cầu có thể sửa/di chuyển source read-only. Không bao giờ dùng repository tham khảo, ký ức model hoặc tên file làm bằng chứng chuyên môn nếu chưa được source index và evidence ledger hỗ trợ.
