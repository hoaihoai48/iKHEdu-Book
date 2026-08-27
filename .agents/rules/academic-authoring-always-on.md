# Academic Authoring — Always On

Bạn đang làm việc trong một dự án viết sách, giáo trình, khóa học, tài liệu học thuật hoặc tài liệu đào tạo. Hãy coi đây là một dự án biên soạn có kiểm soát, không phải một lần sinh văn bản độc lập.

## Luật nạp ngữ cảnh bắt buộc

Trước khi phân tích, viết, sửa, tóm tắt, dịch hoặc tạo cấu trúc mới, hãy đọc theo thứ tự:

1. `@../context/project-context.md`
2. `@../context/source-index.md`
3. `@../context/evidence-ledger.md`
4. `@../context/decision-log.md`
5. `@../context/open-questions.md`
6. Các source liên quan được chỉ ra trong `source-index.md`, chỉ đọc phần cần thiết.

Nếu một tệp context còn là mẫu trống, hãy nói rõ thiếu dữ liệu và dùng nó như một khoảng trống cần bổ sung; không tự bịa mục tiêu, đối tượng học, tiêu chuẩn, nguồn hay quyết định của người dùng. Nếu source-index chỉ tới một nguồn không tồn tại, hãy dừng phần kết luận phụ thuộc vào nguồn đó và báo lỗi đường dẫn.

Sau mỗi mốc lớn, hãy cập nhật các ghi chú trạng thái thích hợp. Không đưa toàn bộ lịch sử hội thoại vào context nếu một bản ghi ngắn, có cấu trúc và có ngày cập nhật đã đủ.

## Luật ưu tiên nguồn

`source/` hoặc các thư mục nguồn do người dùng chỉ định là **source-of-truth**. Tài liệu tham khảo chỉ để đối chiếu, không được âm thầm ghi đè source của dự án. Không sửa, đổi tên, di chuyển hoặc định dạng lại source gốc nếu chưa được yêu cầu rõ ràng. Tách bạch ba lớp: dữ kiện có nguồn, suy luận của tác giả và nội dung minh họa.

Mọi khẳng định có thể kiểm chứng phải có provenance trong `evidence-ledger.md`: mã nguồn, đường dẫn hoặc DOI/URL, vị trí trang/đoạn nếu có, trạng thái kiểm chứng và phạm vi khẳng định. Không tạo citation, số liệu, trích dẫn nguyên văn, DOI hoặc tài liệu tham khảo từ trí nhớ. Khi chưa xác minh, gắn nhãn `[CHƯA XÁC MINH]` thay vì làm cho câu chữ có vẻ chắc chắn.

## Luật thiết kế học liệu

Với giáo trình hoặc tài liệu dạy học, làm theo backward design: xác định kết quả học tập đo được trước; xác định bằng chứng/đánh giá; rồi mới chọn nội dung, hoạt động, ví dụ và tài liệu. Kiểm tra alignment giữa mục tiêu, đánh giá và nội dung. Mỗi chương hoặc module phải có mục tiêu, khái niệm cốt lõi, giải thích theo trình tự, ví dụ hoặc ứng dụng, điểm kiểm tra hiểu, tóm tắt, thuật ngữ và tài liệu tham khảo phù hợp với loại tài liệu.

Phân biệt rõ sách chuyên khảo, giáo trình, workbook, lecture notes, handbook và tài liệu đào tạo. Khi loại tài liệu, trình độ người học, ngôn ngữ, thời lượng hoặc chuẩn đầu ra chưa rõ, hãy hỏi hoặc ghi giả định trước khi viết lớn.

Trong project này, phân biệt hai hồ sơ đầu ra. Với `lesson-package`, dùng README/index cấp nhóm hoặc chương, `Ly_Thuyet.md`, `Bai_Tap.md`, code tham chiếu và `test/` nếu có. Với `problem-package`, dùng `De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.cpp` và `test/`. Không ép problem package vào cấu trúc lesson, cũng không đưa lời giải đầy đủ vào statement học sinh. Đọc template tương ứng trong `@../skills/academic-book-authoring/references/` trước khi tạo file.

Repository `DKTECHVN/ebook-ikh` chỉ là `REF-001`, một mẫu cấu trúc bên ngoài đã được chủ dự án cho phép tham khảo; không được coi nó là source-of-truth của project và không tự sao chép nội dung vào đây.

## Luật quy trình

Không nhảy thẳng vào viết toàn bộ bản thảo. Hãy đi qua các cổng: brief và giả định; bản đồ nguồn; kiến trúc mục lục; ma trận mục tiêu–nội dung–đánh giá; draft theo module; kiểm chứng fact/citation; phản biện sư phạm và chuyên môn; biên tập ngôn ngữ; kiểm tra consistency và accessibility; rồi mới đóng gói bản phát hành.

Mỗi đầu ra quan trọng phải nêu: mục tiêu, phạm vi đã làm, nguồn đã dùng, phần chưa chắc chắn, các quyết định mới và bước tiếp theo. Nếu yêu cầu chỉ là sửa câu chữ, không tự ý thay đổi luận điểm, cấu trúc, thuật ngữ, citation hoặc ý định sư phạm.

## Luật chất lượng và an toàn

Không dùng văn phong khẳng định vượt quá bằng chứng. Nêu bất đồng học thuật, giới hạn phương pháp, thời điểm của dữ liệu và giả định liên quan. Kiểm tra thiên lệch, tính bao trùm, ví dụ văn hóa, accessibility và rủi ro đạo văn/copyright. Chỉ sử dụng nội dung được phép hoặc trích dẫn theo quy định; ghi attribution/license khi cần.

Trước khi hoàn tất, chạy hoặc thực hiện checklist trong `@../skills/academic-book-authoring/references/qa-checklist.md`. Nếu chưa đạt, không gọi là “final”; dùng trạng thái `draft`, `review-needed` hoặc `blocked`.

## Kích hoạt skill

Khi tác vụ liên quan đến viết, lập kế hoạch, nghiên cứu, biên tập, trích dẫn, thiết kế chương, giáo trình, lesson/module, assessment hoặc kiểm định học liệu, hãy kích hoạt skill `academic-book-authoring` và dùng workflow `/write-book` khi người dùng muốn đi qua quy trình đầy đủ.
