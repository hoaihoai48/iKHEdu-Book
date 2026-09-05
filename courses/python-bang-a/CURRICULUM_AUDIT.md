# CURRICULUM AUDIT — PYTHON BẢNG A LEVEL 1

## Quyết định phạm vi

Khóa học giữ nguyên **6 chương / 16 bài**, tập trung vào Python 3 và tư duy giải bài cho Python Bảng A. Đây là khóa Python định hướng thuật toán, không phải khóa Python tổng quát.

Các nội dung như `def`, `return`, `dict`, `set`, tuple, module, file I/O, exception nâng cao và comprehension không phải chuẩn bắt buộc của Level 1. Có thể giới thiệu ở Level 2 hoặc phụ lục khi cần.

## Tiêu chí kiểm tra từng bài

| Tiêu chí | Câu hỏi kiểm tra |
|---|---|
| Prerequisite | Học sinh cần biết gì trước khi bắt đầu bài? |
| Core Knowledge | Kiến thức nào bắt buộc đạt sau bài? |
| Algorithm Pattern | Học sinh có nhận ra mẫu giải có thể chuyển giao không? |
| Practice Coverage | Bài tập có đi từ cơ bản đến thử thách theo độ khó hợp lý không? |
| Exit Skill | Học sinh có thể tự làm được việc gì sau bài? |

## Ma trận audit

| Bài | Prerequisite | Core Knowledge | Algorithm Pattern | Practice Coverage | Exit Skill |
|:---:|---|---|---|---|---|
| 01 | Không | `print`, `input`, biến, kiểu dữ liệu | Input → process → output | Cơ bản đến luyện tập | Viết chương trình nhập, tính và in kết quả |
| 02 | Bài 01 | Toán tử, `//`, `%`, `**` | Công thức trực tiếp, modulo | Cơ bản đến vận dụng | Chọn đúng phép toán cho bài toán |
| 03 | Bài 02 | Hình học, đổi đơn vị/thời gian, làm tròn | Tách đại lượng và ghép công thức | Cơ bản đến vận dụng | Mô hình hóa bài toán thực tế bằng công thức |
| 04 | Bài 01–03 | So sánh, Boolean, `if/elif/else`, `and/or/not` | Decision + Classification + Boolean expression | Cơ bản đến thử thách | Viết rẽ nhánh nhiều hướng và điều kiện ghép đúng |
| 05 | Bài 02 | `for`, `range` | Sum / accumulator | Cơ bản đến thử thách | Duyệt một khoảng và tích lũy kết quả |
| 06 | Bài 04–05 | `while`, `break`, `continue` | Sentinel / flag | Cơ bản đến vận dụng | Điều khiển vòng lặp chưa biết trước số lượt |
| 07 | Bài 05–06 | Dãy số, Fibonacci, nested loop | Rolling variables / pattern | Bắt buộc và thử thách | Sinh dãy và in mẫu bằng vòng lặp |
| 08 | Bài 02, 06 | Tách chữ số bằng `// 10`, `% 10` | Digit extraction | Bắt buộc và thử thách | Xử lý từng chữ số của số nguyên |
| 09 | Bài 02, 05 | Ước, bội, nguyên tố, GCD | Divisor scan | Bắt buộc và thử thách | Kiểm tra và đếm tính chất số học |
| 10 | Bài 08–09 | Số đặc biệt và đếm theo đoạn | Predicate + counting | Bắt buộc và thử thách | Đếm phần tử thỏa điều kiện |
| 11 | Bài 05, 13 | List, index, mutable, thao tác cơ bản | List traversal | Cơ bản đến vận dụng | Duyệt và cập nhật danh sách |
| 12 | Bài 11 | Thống kê, sắp xếp, trùng lặp | Statistics / ordering | Bắt buộc và thử thách | Tóm tắt và sắp xếp dữ liệu |
| 13 | Bài 01 | Index, slice, chuỗi là sequence | Sequence access | Cơ bản đến vận dụng | Lấy và cắt đúng phần chuỗi |
| 14 | Bài 13 | Duyệt, biến đổi ký tự, `split/join`, `ord/chr` | String traversal + Tokenize → transform → join | Cơ bản đến vận dụng | Duyệt và biến đổi chuỗi theo quy tắc |
| 15 | Bài 01–14 | Đọc đề, test biên, chiến lược thi | Pattern selection | Cơ bản đến vận dụng | Chọn mô hình giải và tự kiểm thử |
| 16 | Bài 01–15 | Đề contest giấu pattern, subtask, phân bổ thời gian | Pattern selection + vét điểm subtask | Đề thi thử (đang biên soạn) | Tự làm đề thi thử trong giới hạn thời gian |

## Mức độ bài tập

- **Cơ bản:** làm quen và áp dụng trực tiếp kiến thức mới.
- **Luyện tập:** biến đổi dữ liệu hoặc điều kiện trong bài quen thuộc.
- **Vận dụng:** chuyển kiến thức sang bối cảnh mới.
- **Thử thách:** bài mở rộng, không dùng làm điều kiện loại học sinh khỏi Level 1.

## Pattern card dùng xuyên suốt

Các pattern chuẩn được đặt trong [`ALGORITHM_PATTERNS.md`](ALGORITHM_PATTERNS.md) và được gọi lại trong lesson phù hợp: input/process/output, counting, sum, maximum, flag, digit extraction, nested loop, rolling variables, string traversal, list traversal và complexity check.

## Kết luận audit

Phạm vi kiến thức đủ để chốt Level 1. Giai đoạn tiếp theo là chuẩn hóa ví dụ, giảm claim không có nguồn, đánh dấu Core/Challenge và kiểm tra từng bài theo ma trận trên; không mở rộng thêm chương.