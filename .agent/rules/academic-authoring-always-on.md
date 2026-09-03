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

## 3. Quy chuẩn code theo ngôn ngữ

### 3.1. C++ (Boilerplate chuẩn thi đấu iKHEDU)
Mọi đoạn code C++ mẫu, code tham chiếu, solution, editorial và testcase generator trong các khóa C++ **BẮT BUỘC** tuân thủ 100% cấu trúc chuẩn sau:
1. Header duy nhất: `#include <bits/stdc++.h>` và `using namespace std;`.
2. Fast I/O ở đầu hàm `main()`:
   ```cpp
   ios::sync_with_stdio(false);
   cin.tie(nullptr);
   ```
3. Đọc dữ liệu an toàn (Safe Input / Graceful Exit): Sử dụng mẫu `if (!(cin >> n >> ...)) return 0;` khi đọc các tham số đầu vào chính để chống crash khi EOF / input rỗng.
4. **Tuyệt đối không dùng tiền tố `` và không nhắc header riêng lẻ:** Vì đã có `#include <bits/stdc++.h>` và `using namespace std;`, cấm viết `sort`, `vector`, `lower_bound`, `upper_bound`, `min`, `cin`... và cấm nhắc đến `<algorithm>`, `<vector>`, `<iostream>`. Luôn gọi trực tiếp: `sort`, `vector`, `lower_bound`, `min`, `cin`... để tinh gọn cú pháp tối đa cho học sinh.

### 3.2. Python (Khóa Python Bảng A)
Mọi problem package Python phải dùng `solution.py`: Python 3 chuẩn, không `import sys`/`sys.stdin`/`sys.stdout`, không `def main()` và không `if __name__ == "__main__":`. Đọc/ghi bằng `input()` và `print()` trực tiếp, không in dữ liệu thừa.
Testcase Python không tạo mặc định; chỉ tạo `test/`, generator, oracle hoặc manifest khi task yêu cầu riêng hoặc QA gate cần.

## 4. Quy chuẩn kiến trúc dữ liệu & trình bày Markdown/KaTeX
* **Kiến trúc dữ liệu tối giản:** Ưu tiên tuyệt đối các kiểu dữ liệu nguyên bản (`int`, `long long`, `double`, `char`, `string`, `vector<int>`). Khi cần sắp xếp nhiều trường số, **ƯU TIÊN DÙNG `vector<vector<long long>>` (vector lồng nhau / mảng 2 chiều)** để học sinh tận dụng cơ chế so sánh mặc định của `sort`.
* **Về `pair` và `struct`**: Vẫn giữ trong C++ Foundation nhưng **chỉ dùng khi bất đắc dĩ** (khi cần sắp xếp đa trường có kiểu dữ liệu khác nhau hoặc hàm so sánh đặc thù `a + b > b + a`).
* **Ranh giới công cụ (Not Yet Boundary)**: Trong Module 01 và Module 02, **TUYỆT ĐỐI CHƯA DÙNG** `set`, `map`, `deque`, `priority_queue`, `Segment Tree`, `Fenwick Tree`, Quy hoạch động.
* **Quy chuẩn hiển thị Markdown & KaTeX:** Tuyệt đối không vẽ sơ đồ bằng ký tự ASCII (`│`, `┌`, `└`, `text` block) gây vỡ giao diện Web LMS. Mọi minh họa dữ liệu bắt buộc dùng **Markdown Tables chuẩn kết hợp KaTeX math notation**. Các lưu ý/tử huyệt lập trình dùng **callout tiếng Việt đơn giản** (`> ⚠️ **Lưu ý:** ...`, `> 💡 **Mẹo nhớ:** ...`), **không dùng cú pháp GitHub Alert (`> [!CAUTION]`, `> [!IMPORTANT]`)** vì học sinh không hiểu.

## 5. Vòng lặp học tập trong bài (Lesson Learning Loop)
Không nhồi lý thuyết suông. Mỗi Lesson phải vận hành theo chu trình khép kín:
$$\text{Hook / Vấn đề} \to \text{Mô phỏng tay} \to \text{Lý thuyết & Invariant} \to \text{Code C++ & Bẫy lỗi} \to \text{Micro Practice P0} \to \text{Quiz} \to \text{Progressive Practice P1-P3} \to \text{Mastery P4/P5}$$

## 6. Bản chất Đơn vị Kiến thức Lớn & Định mức Tối thiểu
* **1 Lesson = 1 Đơn vị Kiến thức Lớn (Large Conceptual Unit)**: Không đồng nhất cứng 1 Lesson với 1 buổi học cơ học. Mỗi Lesson trên LMS là một khối tri thức hoàn chỉnh, giáo viên có thể linh hoạt chia thành 2–4 buổi giảng dạy trực tiếp tùy theo trình độ học sinh.
* **Định mức Tối thiểu (Minimum Baseline)**: $\ge 10$ câu Concept Quiz và $\ge 14$ bài tập thực hành là **ngưỡng tối thiểu**, không phải giới hạn trần cố định. Tùy thuộc vào phạm vi và độ sâu của đơn vị kiến thức lớn, số lượng Quiz và Bài tập được mở rộng linh hoạt để bao quát toàn bộ các biến thể bài toán.

## 7. Quy chuẩn Problem Package theo chuẩn cp-solve & Teacher Guide 9 Phần
Mọi Problem Package phải tuân thủ workflow `cp-solve` (tên đúng là `cp-solve`, không phải `cp-slove`) và tạo các thành phần phù hợp với ngôn ngữ:
1. **`De_Bai.md`**: Statement student-facing theo đúng khuôn chung của khóa C++: `# Tiêu đề` → `## Bối cảnh` → `## Nhiệm vụ` → `## Input` → `## Output` → `## Sample 1` (`### Input`, `### Output`, `### Giải thích`) → `## Ràng buộc`. Không đưa dòng `Mã bài toán`, gợi ý thuật toán hoặc lời giải vào statement. Nếu chưa có sample được duyệt, ghi nhận thiếu sample trong QA thay vì tự bịa dữ liệu.
2. **`Huong_Dan_Giang_Day.md` (Bắt buộc đủ 9 phần sư phạm chuyên sâu)**:
   * (1) Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
   * (2) Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
   * (3) Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
   * (4) Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
   * (5) Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
   * (6) Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)
   * (7) Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
   * (8) Mã Nguồn Tham Chiếu theo ngôn ngữ (Python không `sys`, không `main`; C++ sạch 0 `std::`)
   * (9) Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
3. **Solution theo ngôn ngữ**: C++ dùng `solution.cpp` theo mục 3.1; Python dùng `solution.py` theo mục 3.2.
4. **Testcase tùy chọn**: Không mặc định tạo `test/`, generator, oracle hay 20 testcase cho Python. Chỉ tạo khi task ghi rõ hoặc QA/release gate yêu cầu; khi đã tạo thì phải tuân thủ chuẩn kiểm thử độc lập và manifest.

Trước khi bàn giao, chạy `@../skills/ikhedu-authoring/references/qa-checklist.md`, cập nhật evidence ledger/decision log khi cần.

