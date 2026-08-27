# Lesson Package Template — Khuôn bài học iKHEDU

> Dùng cho một bài học/chuyên đề trong giáo trình. Không dùng template này để thay thế problem package có `De_Bai.md` và `Huong_Dan_Giang_Day.md`.

## Package identity

| Trường | Giá trị |
|---|---|
| `lesson_id` | `Bai_XX` |
| `title` | TBD |
| `group` | TBD |
| `session` | `Buổi X` |
| `level` | TBD |
| `audience` | TBD |
| `prerequisites` | TBD |
| `status` | `draft` |
| `version` | `0.1.0` |
| `source_ids` | `SRC-001`, `SRC-002`, `SRC-004` hoặc source được index |

## Canonical file set

Một lesson package chuẩn gồm các artifact sau:

| File | Vai trò | Quy tắc |
|---|---|---|
| `README.md` | Điều hướng cấp nhóm/chương | Chỉ mục các buổi/bài, mục tiêu, file chi tiết và bài tập; không lặp toàn bộ nội dung |
| `Ly_Thuyet.md` | Tài liệu lý thuyết cho người học | Giải thích khái niệm theo thứ tự, ví dụ và code minh họa nhỏ |
| `Bai_Tap.md` | Bài tập thực hành | Tách bài theo mã phân cấp; nêu yêu cầu, input/output hoặc expected output, ví dụ và độ khó |
| `solution.cpp` hoặc code tương ứng | Code tham chiếu | Biên dịch được, có comment vừa đủ, khớp với lý thuyết và bài tập |
| `test/` nếu có chấm tự động | Test/fixture | Có manifest và quy tắc kiểm tra; không gọi là verified nếu chưa chạy kiểm thử |

Nếu có bản `.docx` và `.md`, phải chỉ định một bản canonical trong `source-index.md`; bản còn lại là bản xuất/đối chiếu, tránh sửa hai nơi độc lập.

## README cấp nhóm/chương

README phải trả lời nhanh: nhóm này dạy ai, mục tiêu gì, gồm những buổi/bài nào, file chi tiết ở đâu, prerequisite là gì, và bài tập/assessment nào gắn với mỗi buổi. Dùng bảng điều hướng:

| Buổi/Bài | Chủ đề | Learning outcomes | File lý thuyết | File bài tập | Code/test | Status |
|---|---|---|---|---|---|---|
| `Buổi 1` | TBD | `LO-01` | `Ly_Thuyet.md` | `Bai_Tap.md` | TBD | draft |

Không dùng README làm nơi chứa source-of-truth thứ hai. Nếu nội dung trong README khác file chi tiết, ghi conflict và chọn bản canonical.

## Ly_Thuyet.md

1. Nêu mục tiêu học tập và kiến thức tiên quyết.
2. Mở bằng vấn đề hoặc thao tác mà người học muốn thực hiện; không đưa thuật ngữ mới mà chưa giải thích.
3. Giải thích từng khái niệm theo trình tự: ý nghĩa -> cú pháp/mô hình -> ví dụ nhỏ -> code -> cách tự kiểm tra.
4. Với mỗi code block, giải thích vai trò của dòng hoặc đoạn quan trọng; tránh comment thay cho phần giải thích.
5. Thêm lỗi thường gặp, trường hợp biên và một câu tự giải thích.
6. Kết thúc bằng tóm tắt, thuật ngữ và liên kết tới `Bai_Tap.md`.

## Bai_Tap.md

Mỗi bài tập dùng cấu trúc:

```markdown
## Bài X.Y — [Tên bài]

### Mục tiêu
- LO-XX

### Yêu cầu
...

### Input / Output hoặc Expected output
...

### Ví dụ
...

### Gợi ý mức 1 (nếu phù hợp)
...

### Tiêu chí tự kiểm tra
...
```

Sắp xếp bài từ thao tác trực tiếp đến bài biến thể. Không đưa lời giải đầy đủ vào bản người học nếu mục tiêu là tự giải; đáp án/giáo án có thể đặt ở artifact giáo viên riêng. Mỗi bài phải liên kết về learning outcome và có trạng thái review.

## Đồng bộ giữa các artifact

Trước release, kiểm tra rằng tên biến, ký hiệu, thuật ngữ, expected output, code và bài tập khớp nhau. Nếu lý thuyết thay đổi API/cú pháp, rà lại bài tập và code. Nếu bài tập thay đổi yêu cầu, rà lại learning outcome và solution. Ghi thay đổi vào decision log.
