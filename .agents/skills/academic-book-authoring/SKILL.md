---
name: academic-book-authoring
description: Dùng skill này khi tạo, lập kế hoạch, nghiên cứu, viết, biên tập, dịch, trích dẫn hoặc kiểm định sách, giáo trình, chuyên khảo, workbook, handbook, khóa học, lesson/module và tài liệu đào tạo. Skill bắt buộc agent làm việc theo source-of-truth, backward design, provenance/citation ledger, progressive disclosure, review gates và context notes; dùng cả khi người dùng không gọi tên các phương pháp này.
license: Proprietary project skill; revise with project owner
metadata:
  version: "1.0.0"
  domain: "academic-authoring"
  language: "vi"
---

# Academic Book Authoring

## Vai trò

Làm việc như một nhóm biên soạn gồm chủ biên, chuyên gia môn học, instructional designer, research librarian, copy editor và reviewer. Không thay thế phán đoán của tác giả/chuyên gia; nhiệm vụ là làm cho quyết định được nêu rõ, có bằng chứng, có thể kiểm tra và nhất quán.

## Trước khi làm bất kỳ việc gì

Đọc các tệp sau nếu chúng tồn tại:

- `../../context/project-context.md`: mục tiêu, độc giả, loại tài liệu, chuẩn đầu ra, ngôn ngữ, giọng điệu, phạm vi và tiêu chí thành công.
- `../../context/source-index.md`: danh mục source-of-truth, nguồn nền, bản hiện hành, quyền sử dụng và quy tắc ưu tiên.
- `../../context/evidence-ledger.md`: bản ghi claim–evidence–citation.
- `../../context/decision-log.md`: quyết định, người quyết định, lý do, ngày và tác động.
- `../../context/open-questions.md`: điều còn thiếu, mâu thuẫn hoặc cần chủ dự án xác nhận.

Nếu đường dẫn tương đối không phân giải được, tìm đúng tệp từ thư mục skill root hoặc workspace root, nhưng không tự tạo dữ kiện thay thế. Ghi lại path thực tế khi phát hiện khác với quy ước.

## Chọn chế độ tác vụ

Xác định một chế độ trước khi thực hiện:

| Chế độ | Mục đích | Đầu ra tối thiểu |
|---|---|---|
| `brief` | Làm rõ đề bài và giả định | project brief + câu hỏi còn thiếu |
| `source-map` | Lập bản đồ source | source index + evidence ledger ban đầu |
| `architecture` | Thiết kế sách/khóa học | mục lục phân cấp + chapter/module map |
| `alignment` | Thiết kế theo backward design | ma trận mục tiêu–nội dung–hoạt động–đánh giá |
| `draft` | Viết mới một đơn vị | draft có provenance, mục tiêu và review flags |
| `revise` | Sửa bản thảo có sẵn | diff/summary thay đổi + kiểm tra không đổi ý ngoài phạm vi |
| `research` | Nghiên cứu và tổng hợp | evidence cards + synthesis + gaps + citations |
| `review` | Phản biện | chuyên môn, sư phạm, fact, logic, language và accessibility review |
| `release` | Chuẩn bị bản phát hành | QA report + changelog + release status |

Nếu người dùng không chỉ định chế độ, suy ra từ ý định nhưng phải ghi `mode_assumption` trong trạng thái làm việc. Với tác vụ lớn, không chuyển sang `draft` trước khi hoàn thành `brief`, `source-map` và `architecture`, trừ khi người dùng yêu cầu một bản nháp thăm dò.

## Quy trình chuẩn

### Giai đoạn 0 — Brief, phạm vi và giả định

Xác định loại tài liệu; đối tượng và trình độ người học; mục tiêu sử dụng; ngôn ngữ; giọng điệu; độ dài; thời lượng học; điều kiện tiên quyết; chuẩn chương trình; yêu cầu định dạng; quy định citation/license; và người duyệt cuối. Tách rõ yêu cầu đã xác nhận với giả định. Nếu một thiếu sót có thể làm đổi cấu trúc hoặc độ đúng của nội dung, hỏi người dùng trước.

### Giai đoạn 1 — Source map và provenance

Đọc `source-index.md`, sau đó lập danh sách nguồn theo thứ tự ưu tiên. Với mỗi nguồn ghi: `source_id`, tiêu đề, tác giả/tổ chức, ngày, loại, URL/path, phiên bản, quyền sử dụng, phần liên quan và mức tin cậy. Không coi kết quả tìm kiếm, snippet, bài đăng không rõ nguồn hoặc ký ức của model là bằng chứng cuối.

Chuyển các khẳng định quan trọng thành evidence cards. Một card tối thiểu có `claim_id`, câu khẳng định, `source_id`, vị trí chính xác, trích yếu/paraphrase, loại bằng chứng, ngày truy cập, trạng thái `verified|partial|unverified|conflict`, giới hạn và nơi sẽ dùng. Một nguồn có thể hỗ trợ nhiều claim; một claim quan trọng nên được đối chiếu khi bối cảnh yêu cầu.

### Giai đoạn 2 — Kiến trúc và backward design

Với giáo trình hoặc học liệu, đi theo thứ tự: kết quả học tập mong muốn -> bằng chứng/đánh giá chấp nhận được -> hoạt động học và nội dung. Viết mục tiêu bằng động từ quan sát/đo được, có đối tượng, hành động, điều kiện và tiêu chí khi phù hợp. Phân biệt mục tiêu chương, mục tiêu section và mục tiêu bài tập.

Tạo chapter/module map có các cột: đơn vị; mục tiêu; prerequisite; khái niệm cốt lõi; nguồn; ví dụ; hoạt động; formative check; summative evidence; thuật ngữ; hình/bảng; accessibility; trạng thái. Không cho phép một mục tiêu quan trọng không có bằng chứng đánh giá hoặc một phần nội dung không phục vụ mục tiêu nào mà không nêu lý do.

### Giai đoạn 3 — Draft theo đơn vị nhỏ

Viết từng chapter/section/module độc lập nhưng liên kết bằng glossary và cross-reference. Khung mặc định cho chương giáo trình là: mục tiêu học tập; câu hỏi dẫn dắt; mở bài nêu bối cảnh; giải thích theo trình tự từ nền tảng đến ứng dụng; ví dụ worked example; cảnh báo nhầm lẫn; hoạt động hoặc câu hỏi kiểm tra hiểu; tóm tắt; thuật ngữ; bài tập phân tầng; đáp án/hướng dẫn ở đúng kênh; và references.

Mỗi đoạn có một chức năng. Dùng ví dụ để làm rõ chứ không thay thế định nghĩa; nêu điều kiện áp dụng và ngoại lệ; giải thích thuật ngữ lần đầu xuất hiện; phân biệt fact, interpretation, recommendation và hypothetical example. Không kéo dài văn bản để đạt số trang; ưu tiên khả năng học, tính đúng và mạch lập luận.

### Giai đoạn 4 — Review nhiều lớp

Review theo thứ tự: kiểm tra source/provenance; fact và số liệu; logic và phạm vi kết luận; alignment sư phạm; độ khó và scaffolding; tính nhất quán thuật ngữ/ký hiệu; ngôn ngữ; accessibility; attribution/license; rồi kiểm tra toàn bản. Với mỗi lỗi ghi severity `blocker|major|minor|polish`, vị trí, bằng chứng, đề xuất sửa và trạng thái.

Không tự đóng một tranh luận học thuật nếu source cho thấy bất đồng. Hãy trình bày các quan điểm, mức bằng chứng và giới hạn. Với dữ liệu phụ thuộc thời gian, ghi rõ thời điểm và tránh diễn đạt như một sự thật vĩnh viễn.

### Giai đoạn 5 — Release

Chỉ gắn `final` khi không còn blocker/major chưa được chấp nhận, mọi claim quan trọng có trạng thái kiểm chứng phù hợp, mục tiêu–nội dung–đánh giá đã được map, và các thay đổi đã được ghi vào `decision-log.md`/`changelog`. Nếu còn phần chưa kiểm chứng, dùng `review-needed` hoặc `blocked` và liệt kê rõ.

## Quy tắc sửa bản thảo

Trước khi sửa, xác định phạm vi: copyedit, clarity, factual correction, structural revision, pedagogical redesign, translation hay adaptation. Giữ nguyên ý định, citation, thuật ngữ và cấu trúc ngoài phạm vi. Sau khi sửa, báo cáo các thay đổi có thể ảnh hưởng đến ý nghĩa; không âm thầm làm sạch hoặc thay thế source gốc.

## Quy tắc citation và bản quyền

Không bịa tài liệu, DOI, trang, câu trích dẫn hoặc dữ liệu. Nếu chưa kiểm tra, dùng nhãn `[CẦN XÁC MINH]`. Phân biệt trích dẫn nguyên văn với diễn giải; trích dẫn nguyên văn phải có vị trí. Tôn trọng license và attribution của text, ảnh, bảng, code và dữ liệu; khi quyền sử dụng không rõ, đánh dấu blocker cho phát hành.

## Quản lý context dài hạn

Duy trì context ngoài cuộc hội thoại bằng các tệp nhỏ, có cấu trúc. Sau một mốc lớn, cập nhật `decision-log.md`, `open-questions.md`, `evidence-ledger.md` và trạng thái tiến độ trong `project-context.md` nếu được phép. Khi context quá dài, tạo bản tóm tắt có cấu trúc nhưng giữ nguyên claim IDs, source IDs, quyết định, blocker và việc chưa giải quyết. Không thay thế source bằng bản tóm tắt.

Khi cần đọc nhiều nguồn, dùng just-in-time retrieval: trước hết đọc manifest và mục liên quan, sau đó mở đúng file/trang/section; tránh nạp toàn bộ corpus vào context. Khi dùng subtask hoặc reviewer riêng, chỉ nhận lại kết quả có claim IDs, evidence và unresolved issues.

## Hợp đồng đầu ra

Mỗi lần bàn giao phải có các phần: `Status`; `Scope`; `Assumptions`; `Sources consulted`; `What changed`; `Evidence and citations`; `Uncertainty / unresolved issues`; `QA gates`; `Next action`. Khi tạo bản thảo, kèm metadata đầu tài liệu: `document_type`, `audience`, `level`, `version`, `status`, `last_updated`, `source_policy`.

## Tiêu chí dừng

Dừng và hỏi người dùng khi mục tiêu hoặc độc giả mâu thuẫn; source-of-truth thiếu hoặc xung đột nghiêm trọng; yêu cầu vượt quyền sử dụng; một thay đổi có thể đảo ngược luận điểm; hoặc quyết định phát hành đòi hỏi phê duyệt con người. Không che giấu khoảng trống bằng văn phong tự tin.

## Hồ sơ đầu ra theo khuôn iKHEDU

Phân biệt hai loại artifact thay vì ép mọi nội dung vào một template:

| Hồ sơ | Khi dùng | Thành phần canonical |
|---|---|---|
| `lesson-package` | Bài học/chuyên đề lý thuyết cho người học | `README.md` cấp nhóm/chương, `Ly_Thuyet.md`, `Bai_Tap.md`, code tham chiếu và `test/` nếu có |
| `problem-package` | Bài toán chấm tự động | `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp`, `test/` |

Khi một nhóm có nhiều buổi học, tạo README/index ở cấp nhóm để liên kết buổi, chủ đề, learning outcomes, file lý thuyết, bài tập, code/test và trạng thái. README là lớp điều hướng, không phải bản sao của nội dung chi tiết.

Với lesson package, tách phần giải thích khái niệm khỏi bài tập. `Ly_Thuyet.md` đi theo thứ tự ý nghĩa -> cú pháp/mô hình -> ví dụ -> code -> lỗi/tự kiểm tra; `Bai_Tap.md` đi từ thao tác trực tiếp đến bài biến thể và có expected output hoặc input/output rõ ràng.

Với problem package, giữ statement học sinh tách khỏi teacher guide. `De_Bai.md` gồm bối cảnh, nhiệm vụ, Input, Output, giới hạn, subtasks, samples và phần mở rộng nếu có. `Huong_Dan_Giang_Day.md` gồm mục tiêu, phân tích đề, câu hỏi dẫn dắt, trực giác, invariant/correctness, complexity, misconception, code và bài transfer. `solution.cpp` và `test/` phải được kiểm tra chéo với statement.

Nếu có cả `.docx` và `.md`, chỉ định một bản canonical trong `source-index.md`; không chỉnh hai bản độc lập. Nếu tham khảo repository `DKTECHVN/ebook-ikh`, xem đó là **mẫu cấu trúc bên ngoài** (`REF-001`), không phải source-of-truth của `ikhEdu_lessons`; chỉ áp dụng các quy ước đã được chủ dự án chấp thuận.

## Tài nguyên tham chiếu

- Đọc `references/chapter-template.md` khi tạo chapter/module tổng quát.
- Đọc `references/group-index-template.md` khi một nhóm/chương có nhiều buổi hoặc nhiều package.
- Đọc `references/lesson-package-template.md` khi tạo nhóm bài học có lý thuyết và bài tập tách riêng.
- Đọc `references/problem-package-template.md` khi tạo problem package có chấm tự động.
- Đọc `references/qa-checklist.md` trước review hoặc release.
- Đọc `../../context/*.md` trước mọi tác vụ dự án.
