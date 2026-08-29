---
name: academic-authoring-always-on
version: 2.1.0
priority: P0
trigger: always_on
---
# iKHEDU Authoring — Always On

Khi yêu cầu liên quan đến sách, giáo trình, chương, bài, lesson, module, README học liệu, bài tập, problem, teacher guide, solution, testcase, curriculum, assessment hoặc tài liệu để in, **tự động áp dụng skill `ikhedu-authoring`** và tuân thủ tuyệt đối **Curriculum Architecture v2** (đặc tả tại `docs/MASTER_MODULE_01_DESIGN.md`). Không yêu cầu người dùng gọi lại skill/workflow cho từng tin nhắn.

Trước khi viết hoặc sửa, luôn đọc theo thứ tự:

1. `@../context/project-context.md`
2. `@../context/source-index.md`
3. `@../context/evidence-ledger.md`
4. `@../context/decision-log.md`
5. `@../context/open-questions.md`
6. `@../../docs/MASTER_MODULE_01_DESIGN.md` (Golden Specification)
7. Chỉ đọc phần liên quan của source được đăng ký trong `source-index.md`.

Luôn coi các source project đã đăng ký là read-only và source-of-truth. Phân biệt dữ kiện có nguồn, suy luận của tác giả và ví dụ minh họa. Không bịa citation, số liệu, quote, test result hoặc trạng thái verified. Nếu thiếu context, source xung đột hoặc quyết định quan trọng chưa rõ, dừng và hỏi chủ dự án.

## 1. Phân cấp 5 tầng (5-Tier Curriculum Hierarchy)
Toàn bộ học liệu và nền tảng DKOJ Web LMS bắt buộc tuân theo cấu trúc:
$$\text{PROGRAM} \longrightarrow \text{MODULE / CHƯƠNG} \longrightarrow \text{LESSON / BÀI HỌC} \longrightarrow \text{CONCEPT / SECTION} \longrightarrow \text{ACTIVITY / PROBLEM}$$

## 2. Định danh Problem độc lập (Problem Identity vs. Lesson Placement)
* **`IKH-xxxx` là Global Unique Problem Code**: Thuộc về Problem Library toàn hệ thống. Trường `Problem.code` là duy nhất (`UNIQUE`), chứa trọn vẹn Statement, 20 Testcases, Solution C++ chuẩn và Editorial.
* **`LessonActivity` là Quan hệ Sử dụng (Placement / Slot)**: Lesson chỉ tham chiếu tới `Problem.code`. Không tạo mã bài duplicate khi cùng một bài toán được tái sử dụng ở nhiều bài học khác nhau.

## 3. Quy chuẩn code C++ (Boilerplate chuẩn thi đấu iKHEDU)
Mọi đoạn code C++ mẫu, code tham chiếu, solution, editorial và testcase generator trong toàn bộ dự án **BẮT BUỘC** tuân thủ 100% cấu trúc chuẩn sau:
1. Header duy nhất: `#include <bits/stdc++.h>` và `using namespace std;`.
2. Fast I/O ở đầu hàm `main()`:
   ```cpp
   ios::sync_with_stdio(false);
   cin.tie(nullptr);
   ```
3. Đọc dữ liệu an toàn (Safe Input / Graceful Exit): Sử dụng mẫu `if (!(cin >> n >> ...)) return 0;` khi đọc các tham số đầu vào chính để chống crash khi EOF / input rỗng.

## 4. Quy chuẩn kiến trúc dữ liệu tối giản (Không nhồi nhét cú pháp)
Trong các chuyên đề nền tảng (Module 01: Sắp xếp, Hai con trỏ, Tham lam...):
* **Ưu tiên tuyệt đối** các bài toán và thao tác trên kiểu dữ liệu nguyên bản (`int`, `long long`, `double`, `char`, `string`, `vector<int>`).
* Khi bài toán bắt buộc phải lưu và sắp xếp nhiều thuộc tính đi cùng nhau (như mốc thời gian `start`, `finish`), **ƯU TIÊN DÙNG `vector<vector<int>>` (vector lồng nhau / mảng 2 chiều)** để học sinh tận dụng kiến thức mảng sẵn có và cơ chế so sánh mặc định của `std::sort`.
* **Về `pair` và `struct`**: Vẫn giữ trong C++ Foundation nhưng **chỉ dùng khi bất đắc dĩ** (như khi cần sắp xếp đa trường có kiểu dữ liệu khác nhau hoặc hàm so sánh đặc thù `a + b > b + a`). Bình thường luôn ưu tiên vector lồng nhau để giảm gánh nặng cú pháp cho học sinh.
* **Ranh giới công cụ (Not Yet Boundary)**: Trong Module 01, **TUYỆT ĐỐI CHƯA DÙNG** `set`, `map`, `deque`, `priority_queue`, `Segment Tree`, `Fenwick Tree`, Quy hoạch động.

## 5. Vòng lặp học tập trong bài (Lesson Learning Loop)
Không nhồi lý thuyết suông. Mỗi Lesson phải vận hành theo chu trình khép kín:
$$\text{Hook / Vấn đề} \to \text{Mô phỏng tay} \to \text{Lý thuyết & Invariant} \to \text{Code C++ & Bẫy lỗi} \to \text{Micro Practice P0} \to \text{Quiz} \to \text{Progressive Practice P1-P3} \to \text{Mastery P4/P5}$$

Với `problem-package`, luôn đọc `@../skills/ikhedu-authoring/references/testcase-generation-standard.md` và tạo theo chuỗi `De_Bai.md → Huong_Dan_Giang_Day.md → solution.cpp → test/`. Test phải có test matrix, generator deterministic, seed cố định, oracle độc lập, `manifest.json`, `.inp/.out`, timeout, coverage và test report.

Trước khi bàn giao, chạy `@../skills/ikhedu-authoring/references/qa-checklist.md`, cập nhật evidence ledger/decision log khi cần.
