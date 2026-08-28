# Academic Authoring QA Checklist

> Mỗi mục ghi `pass`, `fail`, `na` hoặc `needs-human-review`. Không gắn `final` khi còn `blocker` hoặc `major` chưa được xử lý/chấp nhận.

## A. Scope and context

| Check | Result | Evidence / note |
|---|---|---|
| Đã đọc `project-context.md`, `source-index.md`, `evidence-ledger.md`, `decision-log.md`, `open-questions.md` | pending | |
| Loại tài liệu, độc giả, trình độ, ngôn ngữ và mục tiêu đã rõ | pending | |
| Các giả định được tách khỏi yêu cầu đã xác nhận | pending | |
| Phạm vi bản sửa không vượt quá yêu cầu | pending | |

## B. Source and factual integrity

| Check | Result | Evidence / note |
|---|---|---|
| Source-of-truth đã được ưu tiên đúng | pending | |
| Mỗi claim quan trọng có `claim_id` và `source_id` | pending | |
| Citation/DOI/URL/trang/đoạn đã được xác minh | pending | |
| Không có citation, số liệu, quote hoặc reference bịa | pending | |
| Claim được diễn đạt không vượt quá bằng chứng | pending | |
| Xung đột học thuật và giới hạn nghiên cứu được nêu | pending | |
| Dữ liệu phụ thuộc thời gian có ngày/phiên bản | pending | |

## C. Pedagogy and alignment

| Check | Result | Evidence / note |
|---|---|---|
| Mục tiêu dùng động từ quan sát/đo được khi cần | pending | |
| Mục tiêu, nội dung, hoạt động và đánh giá được map với nhau | pending | |
| Không có mục tiêu quan trọng không có evidence | pending | |
| Có prerequisite và scaffolding phù hợp | pending | |
| Có ví dụ, phản ví dụ/nhầm lẫn và cơ hội luyện tập | pending | |
| Có formative check và feedback/retry khi phù hợp | pending | |
| Bài tập đo đúng năng lực, không chỉ đo khả năng nhớ | pending | |
| Cấu trúc hỗ trợ active learning, transfer và tự đánh giá | pending | |

## D. Subject matter and reasoning

| Check | Result | Evidence / note |
|---|---|---|
| Thuật ngữ, ký hiệu, đơn vị và giả định nhất quán | pending | |
| Lập luận không có bước nhảy logic hoặc circular reasoning | pending | |
| Ví dụ không mâu thuẫn với định nghĩa và source | pending | |
| Phân biệt fact, interpretation, recommendation và hypothetical | pending | |
| Câu hỏi/bài tập có đáp án hoặc rubric phù hợp | pending | |
| Nội dung nhạy cảm có ngữ cảnh và cảnh báo cần thiết | pending | |

## E. Editorial and document consistency

| Check | Result | Evidence / note |
|---|---|---|
| Heading hierarchy, cross-reference và numbering hợp lệ | pending | |
| Giọng điệu, chính tả, thuật ngữ dịch và quy ước viết nhất quán | pending | |
| Summary không đưa claim mới | pending | |
| Glossary khớp với cách dùng trong thân bài | pending | |
| Tất cả hình/bảng có tiêu đề, nguồn và mô tả khi cần | pending | |
| Không còn placeholder ngoài những mục đã đánh dấu rõ | pending | |

## F. Accessibility, inclusion and rights

| Check | Result | Evidence / note |
|---|---|---|
| Nội dung có thể tiếp cận bằng cấu trúc heading, bảng và văn bản thay thế phù hợp | pending | |
| Ví dụ không củng cố thiên lệch không cần thiết | pending | |
| Tôn trọng các bối cảnh văn hóa, ngôn ngữ và người học khác nhau | pending | |
| Text, ảnh, bảng, code và dữ liệu có quyền sử dụng/attribution phù hợp | pending | |
| Nội dung được phép tái sử dụng theo license của dự án | pending | |

## G. Print-ready / book production gate

> Chỉ áp dụng khi `output_target` là `print` hoặc `both`. Nếu không áp dụng, ghi `na` kèm lý do.

| Check | Result | Evidence / note |
|---|---|---|
| Khổ thành phẩm, hướng trang, lề trong/lề ngoài, gutter, bleed và hệ màu đã chốt | pending | |
| Front matter, body matter và back matter đã có cấu trúc rõ | pending | |
| Mục lục, heading, caption, số hình/bảng, cross-reference và số trang khớp | pending | |
| Font được phép sử dụng và được nhúng/đóng gói đúng khi xuất | pending | |
| Hình, bảng, công thức và code không tràn lề, không bị cắt hoặc giảm độ đọc | pending | |
| Ngắt chương, trang trắng, widow/orphan và header/footer đã được kiểm tra | pending | |
| Độ tương phản và khả năng đọc khi in xám/đen trắng đạt yêu cầu | pending | |
| PDF proof đã render và đã kiểm tra trực quan các trang rủi ro | pending | |
| Đã kiểm tra chính tả/thuật ngữ sau dàn trang, không chỉ trên source canonical | pending | |
| Đã ghi rõ source canonical, artifact dẫn xuất và phiên bản phát hành | pending | |
| Proof đã được người duyệt xác nhận hoặc trạng thái được đặt là `review-needed` | pending | |

## H. Release gate

| Check | Result | Evidence / note |
|---|---|---|
| Không còn blocker/major chưa xử lý | pending | |
| Evidence ledger đã cập nhật | pending | |
| Decision log và changelog đã cập nhật | pending | |
| Reviewer con người đã xác nhận các mục cần phê duyệt | pending | |
| Trạng thái cuối là `draft`, `review-needed`, `blocked` hoặc `final` một cách trung thực | pending | |

## Severity

`blocker` ngăn phát hành: sai sự thật nghiêm trọng, nguồn không được phép, mục tiêu/đánh giá lệch hoàn toàn hoặc thiếu context làm đổi ý nghĩa. `major` cần sửa trước release thông thường: claim thiếu bằng chứng, lỗi chuyên môn, lỗi alignment hoặc mâu thuẫn nội bộ. `minor` là lỗi cục bộ không đổi ý nghĩa. `polish` là cải thiện trình bày.
