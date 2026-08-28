# Module 01 – Sắp xếp

> Lesson package MVP đầu tiên của khóa học iKHEDU C++ Bảng B – Level 1.

## Package identity

| Trường | Giá trị |
|---|---|
| `lesson_id` | `L1-M01-SORT` |
| `title` | Sắp xếp – Khi thứ tự giúp bài toán dễ hơn |
| `group` | iKHEDU C++ Bảng B – Level 1 |
| `session` | Chưa chốt; dự kiến 7 buổi trong bản outline |
| `level` | Level 1 – Thuật toán cơ bản |
| `audience` | Học sinh đã được làm quen với Level 0 và bắt đầu học thuật toán |
| `prerequisites` | Mảng/`vector`, vòng lặp, so sánh, đổi chỗ, `max/min`, độ phức tạp cơ bản |
| `source_ids` | `SRC-001`, `SRC-002`, `SRC-004` |
| `status` | `draft` |
| `version` | `0.1.0` |

## Mục tiêu module

Module giúp học sinh hiểu sắp xếp như một bước biến đổi dữ liệu để tạo trật tự, từ đó làm các bước tìm kiếm, ghép cặp, chọn lựa hoặc kiểm tra trở nên đơn giản hơn. Học sinh cần hiểu mục đích của việc sắp xếp trước khi sử dụng `sort` hoặc comparator.

## Learning outcomes

Sau module, học sinh có thể:

- giải thích được vì sao thứ tự dữ liệu có thể giúp giải bài toán;
- mô phỏng một quy trình sắp xếp đơn giản bằng tay và bằng code;
- sử dụng `sort` cho mảng/`vector` theo thứ tự tăng hoặc giảm;
- viết comparator đơn giản trên dãy số nguyên theo một hoặc hai quy tắc;
- nhận biết rằng sắp xếp có thể làm thay đổi vị trí ban đầu của phần tử;
- phân tích cơ bản sự khác nhau giữa `O(N²)` và `O(N log N)`;
- giải thích được bước sắp xếp đóng vai trò gì trong một lời giải;
- hoàn thành một bài biến thể mà không sao chép nguyên mẫu.

## Chuỗi artifact chuẩn

```text
README.md → Ly_Thuyet.md → Bai_Tap.md → code/test
```

| Artifact | Path | Status |
|---|---|---|
| Package index | `README.md` | `draft` – file này |
| Lý thuyết cho học sinh | [`Ly_Thuyet.md`](Ly_Thuyet.md) | `draft` – đã tạo, chờ review |
| Bài tập thực hành | [`Bai_Tap.md`](Bai_Tap.md) | `draft` – đã tạo, chờ review |
| Code tham chiếu | [`code_reference.cpp`](code_reference.cpp) | `draft` – đã compile smoke test, chờ teacher review |
| Test/fixture | Chưa chốt | Chưa tạo; cần quyết định sau review |
| Outline chương | [`../../curriculum/level1/IKHEDU_Level1_Textbook_Outline.md`](../../curriculum/level1/IKHEDU_Level1_Textbook_Outline.md) | `draft` |
| Level 0 tham chiếu | [`../../curriculum/level0/IKHEDU_Level0_Foundation.md`](../../curriculum/level0/IKHEDU_Level0_Foundation.md) | `draft` |

## Cấu trúc buổi học dự kiến

| Buổi | Nội dung | Bằng chứng học tập | Status |
|---:|---|---|---|
| 1 | Vì sao cần sắp xếp; hoạt động sắp xếp bằng tay | Pseudocode và giải thích mục đích | planned |
| 2 | Selection Sort để hiểu bản chất | Tracing và code mô phỏng | planned |
| 3 | `sort`, tăng/giảm và khoảng iterator | Bài code trực tiếp | planned |
| 4 | Comparator trên dãy số nguyên | Code với hai quy tắc sắp xếp | planned |
| 5 | Sắp xếp như bước tiền xử lý | Phân tích bài mẫu | planned |
| 6 | Luyện tập phân tầng và sửa code | Bài cơ bản/chuẩn/biến thể | planned |
| 7 | Kiểm tra module và bài chuyển giao | Coding + giải thích bằng lời | planned |

## Ôn nhanh Level 0

- `vector` và chỉ số mảng.
- Vòng lặp `for` để duyệt dữ liệu.
- So sánh hai giá trị.
- Biến tạm và `swap`.
- `max`, `min` và lưu vị trí.
- Độ phức tạp của một và hai vòng lặp.
- Kiểm tra chỉ số, kiểu dữ liệu và kết quả trung gian.

## Basic patterns đang sử dụng

| Pattern | Cách dùng trong module |
|---|---|
| Traversal | Duyệt các phần tử của mảng/vector |
| Comparison | Quyết định phần tử nào đứng trước |
| Max/Min | Chọn phần tử tốt nhất trong phần chưa xử lý |
| Swap/Position | Đổi chỗ; nhận biết vị trí có thể thay đổi |
| Function/Comparator | Đóng gói quy tắc sắp xếp |
| Complexity | So sánh cách sắp xếp đơn giản với `std::sort` |

## Kiến thức sẽ dùng về sau

> `pair`, `struct` và sắp xếp nhiều thuộc tính không thuộc phần bắt buộc của module nhập môn này. Chúng sẽ được giới thiệu ở một module mở rộng sau khi học sinh đã chắc nền tảng dãy số nguyên.


- **Tham lam:** sắp xếp theo tiêu chí phù hợp trước khi chọn.
- **Hai con trỏ:** khai thác trật tự để di chuyển hai đầu mút.
- **Tìm kiếm nhị phân:** tìm kiếm hiệu quả trên dữ liệu đã có thứ tự.
- **Mảng tiền tố và truy vấn:** xử lý dữ liệu sau bước tiền xử lý.
- **Sắp xếp nhiều tiêu chí:** nền tảng cho các bài lịch, lịch trình và xếp hạng.

## Assessment map

| Assessment ID | Hình thức | Outcome | Expected evidence | Status |
|---|---|---|---|---|
| `SORT-F01` | Formative check | Hiểu thứ tự và swap | Tracing đúng một bước sắp xếp | planned |
| `SORT-F02` | Coding | Dùng `sort` tăng/giảm | Code chạy đúng sample và test biên | planned |
| `SORT-F03` | Coding | Comparator trên số nguyên | Comparator nhất quán, output đúng | planned |
| `SORT-T01` | Bài chuyển giao | Nhận ra vai trò của sorting | Giải thích được “sắp xếp để làm gì” trước khi code | planned |

## QA và review

| Artifact | Path | Status |
|---|---|---|
| QA record | [`QA_Review.md`](QA_Review.md) | `draft` / `needs-human-review` |


- **Source/provenance:** sử dụng các source ID đã đăng ký; không đưa thông tin vận hành nhạy cảm vào output.
- **Pedagogy:** kiểm tra prerequisite, learning outcomes, hoạt động và assessment có alignment.
- **Code:** chỉ gọi là verified sau khi có code khớp lý thuyết và được kiểm thử.
- **Release status:** tài liệu hiện là `draft`, chưa phải bản phát hành.
- **Reviewer:** TBD – chủ dự án xác nhận.

## Next action

Bước tiếp theo là review `Ly_Thuyet.md`, `Bai_Tap.md`, `QA_Review.md`, chốt thời lượng thực tế, tạo test/assessment nếu cần và chỉ sau đó mới cân nhắc chuyển package sang `review-needed` hoặc `final`.
