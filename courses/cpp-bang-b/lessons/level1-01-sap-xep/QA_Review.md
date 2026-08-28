# QA REVIEW – MODULE 01: SẮP XẾP

> **Trạng thái:** `draft` / `needs-human-review`  
> **Package:** `L1-M01-SORT`  
> **Ngày kiểm tra:** 2026-08-27

## 1. Phạm vi và context

| Kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Đã đọc project context, source index, evidence ledger, decision log và open questions | `pass` | Context project nằm trong `.agents/context/` |
| Đúng profile lesson package | `pass` | Có README, lý thuyết, bài tập và code tham chiếu |
| Audience và level được nêu | `pass` | Học sinh đã làm quen Level 0, bắt đầu Level 1 |
| Prerequisites được nêu | `pass` | Mảng/vector, vòng lặp, so sánh, swap, max/min, complexity cơ bản |
| Thời lượng chính thức | `needs-human-review` | README đang ghi dự kiến 7 buổi; chưa phải quyết định cuối |

## 2. Source và provenance

| Kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Knowledge base được giữ read-only | `pass` | Không chỉnh sửa `IKHEDU_Knowledge_Base.md` |
| Roadmap được dùng đúng vai trò bản đồ chủ đề | `pass` | Không coi roadmap là thứ tự dạy hoàn chỉnh |
| Nguồn cấu trúc được phân biệt với nguồn chuyên môn | `pass` | `REF-001` chỉ tham khảo artifact structure |
| Claim quan trọng có source ID hoặc là ví dụ giảng dạy | `needs-human-review` | Cần bổ sung claim IDs chi tiết vào evidence ledger trước release |
| Thông tin vận hành nhạy cảm được loại bỏ | `pass` | Không sao chép credential hoặc dữ liệu vận hành |

## 3. Alignment sư phạm

| Kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Learning outcomes dùng động từ quan sát được | `pass` | Giải thích, mô phỏng, sử dụng, viết, phân tích, tự giải |
| Nội dung khớp learning outcomes | `pass` | Có sorting cơ bản, `sort`, comparator trên số nguyên và transfer; dữ liệu nhiều thuộc tính không nằm trong phần bắt buộc |
| Có scaffolding từ Level 0 | `pass` | Hộp Ôn nhanh và câu hỏi tự kiểm tra ở đầu bài |
| Có formative checks | `pass` | Tracing, câu hỏi trước code, tự giải thích và phiếu tự đánh giá |
| Scaffold cho học sinh mới | `pass` | Luồng cơ bản chỉ dùng `int`, `vector<int>`, vòng lặp, so sánh, `swap` và `sort`; `struct`/`pair` không còn trong ba artifact chính |
| Bài tập tăng dần độ khó | `pass` | Tầng A, B, C: cú pháp → vận dụng → chuyển giao |
| Có bài biến thể/transfer | `pass` | Bài 1.10, 1.11 và 1.12 |

## 4. Subject matter và code

| Kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Thuật ngữ và ký hiệu nhất quán | `pass` | Sorting, comparator, `vector`, `sort`, `O(N²)`, `O(N log N)` |
| Có nêu lỗi thường gặp và boundary cases | `pass` | Chỉ số, khoảng iterator, comparator, vị trí ban đầu và dữ liệu lớn |
| Code tham chiếu biên dịch với C++17 | `pass` | Đã compile với `-Wall -Wextra -pedantic` |
| Code tham chiếu khớp mục đích minh họa | `pass` | Chỉ minh họa sort tăng dần trên `vector<int>`, một mục tiêu duy nhất |
| Bộ test tự động | `needs-human-review` | Chưa tạo test/fixture; code cơ bản đã có smoke test |

## 5. Editorial và accessibility

| Kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Heading hierarchy và bảng điều hướng | `pass` | Có section rõ và link từ README |
| Đoạn giải thích ngắn, ví dụ nhỏ | `pass` | Phù hợp học sinh đang xây nền tảng |
| Không đưa lời giải đầy đủ vào file bài tập | `pass` | Bài tập có gợi ý mức 1, không có solution hoàn chỉnh |
| Có mô tả thuật ngữ bằng tiếng Việt | `pass` | Thuật ngữ C++/English được giải thích khi cần |
| Hình ảnh/asset và quyền sử dụng | `needs-human-review` | Package hiện không nhúng asset mới |

## 6. Release gate

Package chưa đủ điều kiện `final` vì còn các blocker cấp phát hành cần human review:

- Chốt thời lượng thực tế và reviewer chuyên môn.
- Kiểm tra lại các ví dụ, mức độ bài tập và thứ tự 7 buổi với lớp học.
- Bổ sung test/fixture nếu cần chấm tự động.
- Cập nhật evidence ledger với claim IDs chi tiết nếu lesson được dùng làm bản phát hành.
- Đối chiếu teacher guide và problem package nếu tách riêng cho giáo viên.

## 7. Handoff

- **Status:** `draft` / `needs-human-review`.
- **Scaffold correction:** `resolved` — đã loại bỏ `struct`/`pair` khỏi luồng cơ bản trong ba artifact chính; các nội dung nhiều thuộc tính được để cho phần mở rộng sau.
- **Scope:** Module 01 – Sắp xếp; chưa tạo problem package riêng.
- **Sources consulted:** `SRC-001`, `SRC-002`, `SRC-004`, `REF-001` cho cấu trúc.
- **What changed:** Tinh chỉnh `Ly_Thuyet.md` và `Bai_Tap.md` để phần cơ bản chỉ dùng số nguyên/vector; viết lại `code_reference.cpp` thành demo sort cơ bản; cập nhật QA record.
- **Next action:** Giáo viên review nội dung; sau đó chỉnh theo phản hồi và tạo assessment/problem package nếu cần.
