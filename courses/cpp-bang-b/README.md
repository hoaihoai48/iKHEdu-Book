# iKHEDU C++ BẢNG B – LEVEL 1

> Trang chủ quản lý khóa học và điều hướng các module, lesson package, problem package, assessment và tài liệu giáo viên.

## Trạng thái khóa học

| Trường | Giá trị |
|---|---|
| **Tên khóa học** | iKHEDU C++ Bảng B – Level 1 |
| **Mã khóa học** | `cpp-bang-b-level1` |
| **Đối tượng** | Học sinh đang xây nền tảng C++ và bắt đầu học thuật toán |
| **Ngôn ngữ** | Tiếng Việt; thuật ngữ và code dùng quy ước C++/English khi cần |
| **Mục tiêu tổng quát** | Biết nhận dạng, giải thích và vận dụng các thuật toán/cấu trúc dữ liệu cơ bản trong các bài toán phù hợp |
| **Prerequisites** | Level 0 – Nền tảng C++ & Tư duy lập trình; xem tài liệu tra cứu nhanh trong `source/level0/` |
| **Số chủ đề roadmap** | 21 chủ đề |
| **BOOK_MASTER** | [`BOOK_MASTER.md`](BOOK_MASTER.md) — bản thảo canonical, trạng thái `draft`, đã có coverage 21 chương |
| **Module MVP đầu tiên** | Module 01 – Sắp xếp |
| **Status** | `draft` |
| **Version** | `0.1.0` |
| **Reviewer** | TBD – chủ dự án xác nhận |

## BOOK_MASTER — Bản thảo canonical

Bản thảo sách tổng hợp được quản lý tại [`BOOK_MASTER.md`](BOOK_MASTER.md). Đây là file canonical để chuẩn bị bản in/bản digital; các lesson trong `lessons/` là artifact chi tiết phục vụ biên soạn và thực hành. Quy trình bắt buộc là: cập nhật tài liệu gốc trong `source/` → review nội dung → đồng bộ phần đã chốt vào `BOOK_MASTER.md`. Không viết ngược trực tiếp vào BOOK_MASTER rồi mới tạo source.

## 1. Mục tiêu khóa học

Khóa học giúp học sinh chuyển từ việc sử dụng các viên gạch Level 0 sang tư duy thuật toán có hệ thống. Học sinh không chỉ nhớ cú pháp hoặc chép template, mà cần biết đọc đề, mô hình hóa dữ liệu, nhận ra dấu hiệu của dạng bài, lựa chọn hướng giải, phân tích độ phức tạp, kiểm thử và biến đổi lời giải sang bài toán tương tự.

Level 0 được dùng như **nền tảng và hệ thống tra cứu xuyên suốt**. Mỗi module Level 1 sẽ gọi lại kiến thức cần thiết thông qua các mục `Ôn nhanh`, `Kỹ năng nền đang sử dụng`, `Cần chú ý` và `Kiến thức sẽ dùng về sau`.

## 2. Nguyên tắc tổ chức

| Nguyên tắc | Cách áp dụng |
|---|---|
| Roadmap không đồng nhất với thứ tự dạy | 21 chủ đề là bản đồ phạm vi; thứ tự dạy cụ thể sẽ được xác định bằng prerequisite và teaching sequence |
| Học kiến thức qua bài toán | Mỗi kỹ thuật mới bắt đầu từ vấn đề, ví dụ bằng tay, cách làm trực tiếp rồi mới tối ưu |
| Gọi lại Level 0 | Mỗi chương/bài có hộp ôn nhanh, pattern nền và lỗi thường gặp |
| Học sinh phải chuyển giao | Bài tập gồm bài trực tiếp, bài chuẩn và bài biến thể |
| Tách artifact theo mục đích | Lý thuyết, bài tập, teacher guide, solution và test không trộn vào một file duy nhất |
| Trạng thái trung thực | Tài liệu chưa qua review giữ trạng thái `draft` hoặc `review-needed`, không gọi là `final` |

## 3. Learning path dự kiến

Thứ tự dưới đây là **teaching sequence tạm thời** để xây dựng khóa học. Đây chưa phải quyết định cuối cùng cho toàn bộ 21 chủ đề; prerequisite map và phản hồi từ lớp học có thể làm thay đổi thứ tự.

| Thứ tự | Module/chủ đề | Kỹ năng chính | Prerequisite chính | Learning outcome | Tài liệu hiện có | Status |
|---:|---|---|---|---|---|---|
| 0 | Phần 0 – Cách học và tư duy giải bài | Input–Process–Output, đọc đề, pseudocode, test, debug, complexity | Không | Biết biến đề bài thành các bước xử lý có thể lập trình | [Level 0 Foundation](source/level0/IKHEDU_Level0_Foundation.md) | draft |
| 1 | **Sắp xếp** | `sort`, comparator, nhiều tiêu chí, tiền xử lý | Mảng, `vector`, vòng lặp, so sánh, swap | Biết dùng thứ tự để làm bài toán đơn giản hơn | [Tài liệu gốc Chương 1 — Sắp xếp](source/level1/IKHEDU_Chapter01_Sorting_Source.md) | **MVP – draft** |
| 2 | **Tham lam** | Quyết định cục bộ, chứng minh lựa chọn | Sắp xếp, so sánh, `vector`, comparator | Nhận diện, triển khai và kiểm tra chiến lược tham lam | [Tài liệu gốc Chương 2 — Tham lam](source/level1/IKHEDU_Chapter02_Greedy_Source.md) | **approved – content; human proof pending** |
| 3 | Số học | Ước, bội, GCD/LCM, số nguyên tố | Vòng lặp, modulo, hàm | Vận dụng tính chất số học cơ bản | [Tài liệu gốc Chương 3 — Số học](source/level1/IKHEDU_Chapter03_NumberTheory_Source.md) | chapter-source-framework |
| 4 | Đếm phân phối | Bảng tần suất, nguyên lý Dirichlet | Đếm, mảng, tần suất | Chọn phương pháp đếm phù hợp | [Tài liệu gốc Chương 4 — Đếm phân phối](source/level1/IKHEDU_Chapter04_FrequencyCount_Source.md) | chapter-source-framework |
| 5 | Tìm kiếm nhị phân | Binary Search, Lower/Upper Bound, Chặt nhị phân kết quả | Sắp xếp, so sánh, hàm `check`, complexity | Nhận diện tính đơn điệu và viết kiểm tra | [Tài liệu gốc Chương 5 — Tìm kiếm nhị phân](source/level1/IKHEDU_Chapter05_BinarySearch_Source.md) | chapter-source-framework |
| 6 | Mảng tiền tố | Prefix Sum 1D/2D, Prefix XOR, Difference Array | Mảng, vòng lặp, tích lũy | Trả lời truy vấn tổng nhanh hơn | [Tài liệu gốc Chương 6 — Mảng tiền tố](source/level1/IKHEDU_Chapter06_PrefixSum_Source.md) | chapter-source-framework |
| 7 | Hai con trỏ | Two Pointers, Sliding Window | Mảng, sắp xếp, điều kiện đơn điệu | Duy trì một đoạn dữ liệu hiệu quả | [Tài liệu gốc Chương 7 — Hai con trỏ](source/level1/IKHEDU_Chapter07_TwoPointers_Source.md) | chapter-source-framework |
| 8 | Xử lý xâu cơ bản | Duyệt, đếm 26 chữ cái, substring, palindrome | `string`, vòng lặp, điều kiện | Xử lý xâu theo mẫu cơ bản | [Tài liệu gốc Chương 8 — Xử lý xâu cơ bản](source/level1/IKHEDU_Chapter08_BasicStrings_Source.md) | chapter-source-framework |
| 9 | Đệ quy và chia để trị | Hàm, trạng thái, Merge Sort, lũy thừa nhị phân | Hàm, vòng lặp, complexity | Mô tả bài toán bằng các bài toán con | [Tài liệu gốc Chương 9 — Đệ quy & Chia để trị](source/level1/IKHEDU_Chapter09_RecursionDivideConquer_Source.md) | chapter-source-framework |
| 10 | Modulo | Phép chia dư, lũy thừa nhanh, nghịch đảo modulo | Toán tử, số học, kiểu dữ liệu | Tính toán an toàn với số lớn | [Tài liệu gốc Chương 10 — Modulo](source/level1/IKHEDU_Chapter10_ModuloArithmetic_Source.md) | chapter-source-framework |
| 11 | Tổ hợp cơ bản | Hoán vị, tổ hợp, Pascal, Euler Stars and Bars | Tích lũy, modulo, đệ quy | Đếm cấu hình trong bài toán | [Tài liệu gốc Chương 11 — Tổ hợp cơ bản](source/level1/IKHEDU_Chapter11_BasicCombinatorics_Source.md) | chapter-source-framework |
| 12 | STL C++ | `vector`, `set`, `multiset`, `map`, `unordered_map`, nén số | C++ Level 0 | Chọn công cụ dữ liệu phù hợp | [Tài liệu gốc Chương 12 — STL C++](source/level1/IKHEDU_Chapter12_STLContainers_Source.md) | chapter-source-framework |
| 13 | Quy hoạch động cơ bản | Trạng thái, chuyển trạng thái, LIS, Knapsack, Grid DP | Mảng, vòng lặp, max/min, complexity | Mô hình hóa kết quả của bài toán con | [Tài liệu gốc Chương 13 — Quy hoạch động](source/level1/IKHEDU_Chapter13_DynamicProgramming_Source.md) | chapter-source-framework |
| 14 | Đồ thị | Danh sách kề, BFS, DFS, liên thông, lưới 2D | `vector<vector<int>>`, queue, stack | Mô hình hóa quan hệ và duyệt đồ thị | [Tài liệu gốc Chương 14 — Đồ thị](source/level1/IKHEDU_Chapter14_GraphBasics_Source.md) | chapter-source-framework |
| 15 | Stack và Queue | LIFO, FIFO, dãy ngoặc đúng, Monotonic Stack | STL nhập môn | Chọn cấu trúc theo quy tắc xử lý | [Tài liệu gốc Chương 15 — Stack & Queue](source/level1/IKHEDU_Chapter15_StackQueue_Source.md) | chapter-source-framework |
| 16 | Segment Tree | Build, Point Update, Range Query, RMQ/Sum | Mảng, đệ quy, hàm, complexity | Hiểu cấu trúc dữ liệu truy vấn đoạn | [Tài liệu gốc Chương 16 — Segment Tree](source/level1/IKHEDU_Chapter16_SegmentTree_Source.md) | chapter-source-framework |
| 17 | Digit DP | Trạng thái theo chữ số, cờ tight, leading zero | DP cơ bản, modulo, đệ quy | Mô hình hóa bài đếm theo chữ số | [Tài liệu gốc Chương 17 — Digit DP](source/level1/IKHEDU_Chapter17_DigitDP_Source.md) | chapter-source-framework |
| 18 | String Hashing | Polynomial Hash, Double Hashing, hash đoạn $\mathcal{O}(1)$ | String, modulo, mảng tiền tố | So sánh xâu/đoạn xâu nhanh | [Tài liệu gốc Chương 18 — String Hashing](source/level1/IKHEDU_Chapter18_StringHashing_Source.md) | chapter-source-framework |
| 19 | Số nguyên lớn | Biểu diễn số lớn, cộng, trừ, nhân, chia, Horner | Mảng, string, phép toán | Xử lý số vượt kiểu dữ liệu chuẩn | [Tài liệu gốc Chương 19 — Số nguyên lớn](source/level1/IKHEDU_Chapter19_BigInteger_Source.md) | chapter-source-framework |
| 20 | Phép toán trên bit | Bitwise, 4 thao tác bitmask, duyệt $2^N$, Bitmask DP | Số nguyên, điều kiện, tập con | Biểu diễn trạng thái bằng bit | [Tài liệu gốc Chương 20 — Phép toán trên bit](source/level1/IKHEDU_Chapter20_Bitmask_Source.md) | chapter-source-framework |
| 21 | Fenwick Tree | Lowbit `x & -x`, Update/Query $\mathcal{O}(\log N)$, đếm nghịch thế | Mảng tiền tố, bit, complexity | Xử lý cập nhật/truy vấn hiệu quả | [Tài liệu gốc Chương 21 — Fenwick Tree](source/level1/IKHEDU_Chapter21_FenwickTree_Source.md) | chapter-source-framework |

## 4. Trạng thái bản thảo Level 1

`BOOK_MASTER.md` hiện đã có coverage của toàn bộ 21 chương Level 1. Chương 1 – Sắp xếp được viết chi tiết hơn; các chương còn lại đã có mục tiêu, prerequisite, ý tưởng cốt lõi, bài tập gợi ý và lỗi thường gặp ở mức bản thảo khung. Cần mở rộng từng chương theo ưu tiên giảng dạy trước khi gọi là bản in hoàn chỉnh.

## 5. Module MVP: Sắp xếp

### Lý do chọn

**Sắp xếp** được chọn làm module MVP đầu tiên vì đây là chủ đề mở đầu trong roadmap Level 1 và có quan hệ trực tiếp với kiến thức Level 0: mảng, `vector`, vòng lặp, so sánh, đổi chỗ, tìm max/min và phân tích độ phức tạp. Chủ đề này cũng tạo cầu nối tự nhiên sang Tham lam, Hai con trỏ và Tìm kiếm nhị phân.

### Mục tiêu MVP

Sau module thử nghiệm, cần kiểm chứng được rằng cấu trúc sách có giúp học sinh:

- gọi lại kiến thức Level 0 trước khi học kỹ thuật mới;
- hiểu vì sao thứ tự dữ liệu có thể làm bài toán dễ hơn;
- phân biệt sắp xếp tăng/giảm và viết comparator đơn giản;
- sắp xếp theo nhiều tiêu chí;
- giải thích được mục đích của bước sắp xếp;
- chuyển giao được sang một bài biến thể;
- tự phát hiện các lỗi cơ bản về chỉ số, comparator và kiểu dữ liệu.

### Artifact MVP dự kiến

| Artifact | Vị trí dự kiến | Trạng thái |
|---|---|---|
| Tài liệu gốc Chương 1 | `source/level1/IKHEDU_Chapter01_Sorting_Source.md` | Có, draft |
| Lesson package | [`lessons/level1-01-sap-xep/`](lessons/level1-01-sap-xep/README.md) | `draft` – đã tạo |
| Lý thuyết | `lessons/level1-01-sap-xep/Ly_Thuyet.md` | `draft` – đã tạo |
| Bài tập | `lessons/level1-01-sap-xep/Bai_Tap.md` | `draft` – đã tạo |
| Teacher guide | Trong lesson package hoặc artifact riêng sau khi chốt profile | Chưa tạo |
| Problem package | `problems/` | Chưa tạo |
| Assessment | `assessments/level1-01-sap-xep/` | Chưa tạo |

## 6. File map

| Loại | Path | Canonical | Mô tả |
|---|---|---:|---|
| Course index | `README.md` | yes | Trang chủ khóa học, learning path và assessment map |
| Book master | [`BOOK_MASTER.md`](BOOK_MASTER.md) | yes | Bản thảo canonical tổng hợp để chuẩn bị bản in/digital |
| Level 0 reference | `source/level0/IKHEDU_Level0_Foundation.md` | draft | Tài liệu nền tảng và tra cứu nhanh hiện có |
| Tài liệu gốc Chương 1 — Sắp xếp | `source/level1/IKHEDU_Chapter01_Sorting_Source.md` | draft | Nội dung gốc đã viết cho Chương 1 – Sắp xếp |
| Lesson packages | `lessons/` | planned | Các gói bài học theo chuẩn `README → Ly_Thuyet → Bai_Tap → code/test` |
| Problem packages | `problems/` | planned | Các gói bài toán theo chuẩn `De_Bai → Huong_Dan_Giang_Day → solution → test` |
| Assessments | `assessments/` | planned | Placement test, formative check, module test và certification |
| Assets | `assets/` | planned | Hình ảnh, sơ đồ và asset được phép sử dụng |

## 7. Assessment map cấp khóa học

| Assessment ID | Phạm vi | Outcome được đo | Hình thức | Evidence dự kiến | Status |
|---|---|---|---|---|---|
| `ASSESS-00` | Trước Level 1 | Kiến thức C++ và tư duy Level 0 | Placement test | Đọc code, viết chương trình ngắn, debug, Input–Process–Output | planned |
| `ASSESS-01` | Sau Module 01 | Nhận dạng và vận dụng Sorting | Quiz + coding + bài biến thể | Code đúng, giải thích comparator, phân tích complexity | planned |
| `ASSESS-02` | Sau nhóm module cơ bản | Kết hợp các pattern và thuật toán | Problem set | Lời giải độc lập và bài transfer | planned |
| `ASSESS-03` | Cuối Level 1 | Tổng hợp các chủ đề đã học | Contest/review | Bài giải, phân tích, kiểm thử và tự đánh giá | planned |

## 8. Quy ước liên kết nội dung

Mỗi chương hoặc lesson Level 1 cần giữ các mục sau ở đầu hoặc gần đầu tài liệu:

```text
Mục tiêu
Ôn nhanh
Kỹ năng nền đang sử dụng
Cần chú ý
Kiến thức mới
Kiến thức sẽ dùng về sau
```

Mỗi lesson package khi được tạo phải có chuỗi điều hướng:

```text
README.md → Ly_Thuyet.md → Bai_Tap.md → code/test
```

Mỗi problem package phải có chuỗi:

```text
De_Bai.md → Huong_Dan_Giang_Day.md → solution.cpp → test/
```

README này chỉ làm nhiệm vụ điều hướng và quản lý trạng thái; không sao chép toàn bộ nội dung lý thuyết từ các file canonical.

## 9. Nguồn và chính sách bảo toàn

| Source ID | Nguồn | Cách sử dụng |
|---|---|---|
| `SRC-001` | `IKHEDU_Knowledge_Base.md` | Nguồn tham chiếu nội dung; read-only |
| `SRC-002` | `ikhEdu_foundation_framework_report.md` | Nguồn định hướng curriculum; read-only |
| `SRC-004` | `Lo_trinh_hoc_tap_bangB_level1.jpg` | Roadmap 21 chủ đề; read-only |
| `REF-001` | `DKTECHVN/ebook-ikh` | Chỉ tham khảo cấu trúc artifact; không dùng làm source-of-truth |

Không đưa thông tin vận hành nhạy cảm từ knowledge base vào README, lesson, bài tập hoặc output công khai.

## 10. Những điểm còn cần xác nhận

- Người duyệt chuyên môn và người duyệt release.
- Thời lượng chính thức của từng module.
- Teaching sequence cuối cùng của 21 chủ đề.
- Chuẩn đầu ra và ngưỡng đánh giá Level 0/Level 1.
- Citation style, license và attribution policy.
- Có bổ sung teacher guide, problem package và assessment chi tiết cho Module 01 sau vòng review đầu tiên.

## 11. Release notes

- **Version:** `0.1.0`
- **Last updated:** 2026-08-28
- **Changed:** Tạo course index, BOOK_MASTER canonical và bổ sung coverage cốt lõi cho toàn bộ 21 chủ đề Level 1.
- **Known gaps:** Các chương 2–21 hiện là bản thảo khung ngắn hơn Chương 1; chưa có problem package, assessment thực thi và reviewer được chỉ định.
- **Status:** `draft`
- **Reviewer:** TBD
