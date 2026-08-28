# REVIEW REPORT – MODULE 01: SẮP XẾP

> **Profile:** `lesson-package`  
> **Package:** `L1-M01-SORT`  
> **Ngày review:** 2026-08-27  
> **Reviewer:** Manus AI – preliminary review; cần giáo viên/chủ dự án review chuyên môn  
> **Trạng thái:** `review-needed`

## 1. Phạm vi review

Review này kiểm tra lesson package theo chuẩn iKHEDU, gồm cấu trúc thư mục, metadata, chuỗi artifact, learning outcomes, prerequisite, cấu trúc bài giảng, bài tập, code tham chiếu, provenance và release gate. Review **không chỉnh sửa** các file nội dung đang được kiểm tra và không chỉnh sửa source read-only.

Các file được kiểm tra:

- `README.md`
- `Ly_Thuyet.md`
- `Bai_Tap.md`
- `code_reference.cpp`
- `QA_Review.md`

## 2. Kết luận điều hành

Lesson package đã đạt mức **draft có thể đem ra review sư phạm**, nhưng **chưa đạt mức `final` hoặc sẵn sàng in/phát hành**. Khung hiện tại đúng hướng và có nhiều điểm tốt: artifact được tách đúng vai trò, lý thuyết đi từ trực giác đến code, bài tập có ba tầng độ khó, learning outcomes tương đối rõ, code tham chiếu compile được và trạng thái release được ghi trung thực.

Ba việc cần ưu tiên trước khi tiếp tục mở rộng sang module khác là:

1. Chuẩn hóa schema của từng bài tập để bài nào cũng có mục tiêu, độ khó, yêu cầu, Input/Output, ví dụ, gợi ý và tiêu chí tự kiểm tra.
2. Hoàn thiện phần cuối của `Ly_Thuyet.md` bằng glossary/thuật ngữ và liên kết trực tiếp tới `Bai_Tap.md`.
3. Giữ luồng cơ bản chỉ dùng `int`, `vector<int>`, vòng lặp, so sánh, `swap` và `sort`; mọi ví dụ `struct`/`pair` phải được tách sang phần mở rộng sau.

## 3. Ma trận kiểm tra tổng quát

| Nhóm kiểm tra | Kết quả | Nhận xét |
|---|---|---|
| Cấu trúc package | `pass` | Có README, lý thuyết, bài tập và code tham chiếu đúng thư mục |
| Metadata | `pass` với điều kiện | Có lesson ID, title, group, level, audience, prerequisite, status và version; session/reviewer vẫn TBD |
| Chuỗi artifact | `pass` | `README → Ly_Thuyet → Bai_Tap → code`; test là optional và chưa tạo |
| Learning outcomes | `pass` | Có `LO-S01` đến `LO-S06`, được nhắc lại trong mục tiêu bài tập |
| Scaffolding | `pass` | Có Ôn nhanh Level 0, Selection Sort, `sort`, comparator và bài transfer |
| Schema bài tập | `needs-human-review` | Nhiều bài chưa có đầy đủ Input/Output và độ khó theo cùng một format |
| Code | `pass` ở mức smoke test | Đã compile C++17 với cảnh báo nghiêm ngặt; cần review lại vai trò sư phạm |
| Provenance | `needs-human-review` | Có source IDs nhưng claim-level mapping chưa được bổ sung vào evidence ledger |
| QA/release | `needs-human-review` | Có QA record, nhưng còn reviewer, assessment và test fixture chưa chốt |
| Source protection | `pass` | `IKHEDU_Knowledge_Base.md` không bị chỉnh sửa |

## 4. Các điểm đạt

### 4.1. Cấu trúc đúng profile lesson package

Package nằm tại `courses/cpp-bang-b/lessons/level1-01-sap-xep/` theo cấu trúc project đã thống nhất. Đường dẫn hiện tại đã được kiểm tra và tồn tại đúng; không có lỗi cấu trúc package ở điểm này.

Các artifact chính đã tồn tại và được liên kết từ README. README cũng ghi rõ trạng thái `draft`, prerequisite, learning outcomes, dự kiến 7 buổi, các artifact chưa có và bước tiếp theo. Đây là cách ghi trạng thái phù hợp với quy định không gọi nội dung chưa human-review là `final`.

### 4.2. Trình tự sư phạm của lý thuyết hợp lý

`Ly_Thuyet.md` đi theo trình tự phù hợp với học sinh đang chuyển từ Level 0 sang Level 1:

```text
Ôn nhanh Level 0
→ hiểu Sorting bằng ví dụ
→ mô phỏng bằng tay
→ Selection Sort
→ std::sort
→ comparator
→ nhiều tiêu chí
→ vai trò của sorting trong bài toán
→ độ phức tạp
→ bài mẫu và tự kiểm tra
```

Cách đặt câu hỏi “sắp xếp xong thì bước nào của bài toán trở nên dễ hơn?” là điểm sư phạm tốt, vì nó ngăn học sinh học thuộc `sort` mà không hiểu mục đích.

### 4.3. Bài tập có hướng tăng dần

`Bai_Tap.md` có 12 bài, được chia thành:

- Tầng A: củng cố cú pháp và thao tác trực tiếp.
- Tầng B: vận dụng comparator, vị trí ban đầu và nhiều tiêu chí.
- Tầng C: chuyển giao sang Two Pointers, Greedy và đánh giá việc có cần sorting hay không.

Bài 1.12 là một bài transfer tốt vì yêu cầu học sinh quyết định **có cần sắp xếp hay không**, thay vì mặc định dùng `sort` cho mọi bài.

### 4.4. Code có kiểm tra biên dịch

`code_reference.cpp` đã compile thành công với C++17 và các cờ:

```text
-Wall -Wextra -pedantic
```

Smoke test với dãy `8 3 6 1 5` cho đầu ra tăng dần đúng là `1 3 5 6 8`. Đây chỉ là bằng chứng compile/smoke test, chưa phải bộ test đầy đủ cho toàn bộ module.

## 5. Findings cần xử lý

### MAJOR-01 – Thiếu glossary và liên kết bài tập ở cuối lý thuyết

**Vị trí:** `Ly_Thuyet.md`, phần cuối tài liệu, khoảng dòng 533–570.

Template lesson package yêu cầu lý thuyết kết thúc bằng tóm tắt, thuật ngữ và liên kết tới `Bai_Tap.md`. File hiện có phần tóm tắt và tài liệu tham chiếu, nhưng chưa có mục `Thuật ngữ/Glossary` rõ ràng và chưa có liên kết Markdown trực tiếp tới file bài tập.

**Tác động:** Học sinh đọc xong lý thuyết không có điểm chuyển rõ sang phần luyện tập; giáo viên cũng khó kiểm tra nhanh thuật ngữ chính.

**Đề xuất:** Thêm các mục:

```markdown
## Thuật ngữ cần nhớ

| Thuật ngữ | Ý nghĩa ngắn |
|---|---|
| Sorting | Đưa dữ liệu về một trật tự phù hợp |
| Comparator | Quy tắc quyết định phần tử nào đứng trước |
| Stable order | Giữ thứ tự tương đối của các phần tử bằng nhau |
| Preprocessing | Bước chuẩn bị dữ liệu trước khi giải bài |

## Bài tập thực hành

Xem [Bai_Tap.md](Bai_Tap.md).
```

**Severity:** `major` trước release sách; `minor` nếu chỉ dùng nội bộ để review.

### MAJOR-02 – Schema bài tập chưa đồng nhất

**Vị trí:** `Bai_Tap.md`, các bài 1.1–1.12.

Template yêu cầu mỗi bài có mục tiêu, yêu cầu, Input/Output hoặc expected output, ví dụ, gợi ý phù hợp và tiêu chí tự kiểm tra. Một số bài có đủ phần lớn các mục, nhưng nhiều bài như 1.2, 1.3 và 1.4 chỉ có yêu cầu và ví dụ, chưa có Input/Output riêng; nhiều bài cũng chưa có trường độ khó nhất quán.

**Tác động:** Khi in thành sách, học sinh sẽ gặp cách trình bày không đều giữa các bài. Giáo viên khó giao bài theo mức độ và khó xây assessment map tự động.

**Đề xuất:** Chuẩn hóa mọi bài theo khuôn:

```markdown
## Bài 1.X – [Tên bài]

### Mục tiêu
- `LO-SXX`

### Độ khó
Cơ bản / Chuẩn / Thử thách

### Yêu cầu
...

### Input
...

### Output
...

### Ví dụ
...

### Gợi ý mức 1
...

### Tiêu chí tự kiểm tra
...
```

Với bài không phải coding, có thể thay Input/Output bằng `Expected output` hoặc `Yêu cầu trả lời`. Không nên để học sinh tự đoán format đầu ra.

**Severity:** `major` trước khi phát hành bản in.

### MAJOR-03 – Code tham chiếu từng trộn ví dụ nâng cao vào luồng cơ bản — ĐÃ XỬ LÝ

**Vị trí cũ:** `code_reference.cpp`, khoảng dòng 4–46.

Bản trước đọc một dãy số rồi in thêm một danh sách học sinh hard-coded dùng `struct`, `string` và comparator nhiều tiêu chí. Điều này làm học sinh mới phải tiếp nhận nhiều khái niệm ngoài mục tiêu Sorting cơ bản.

**Cách xử lý:** `code_reference.cpp` hiện chỉ còn một chương trình độc lập dùng `int`, `vector<int>`, vòng lặp và `sort` tăng dần. Phần lý thuyết cũng đã thay ví dụ `struct`/`pair` bằng comparator trên số nguyên và ghi rõ nội dung nhiều thuộc tính là phần mở rộng.

**Trạng thái:** `resolved` ở phạm vi ba file được yêu cầu; outline Level 1 tổng quát vẫn còn mô tả nội dung nâng cao và cần được đồng bộ trong một thay đổi riêng nếu chủ dự án yêu cầu.

**Severity:** `major` trước chỉnh sửa; hiện không còn là blocker của luồng cơ bản.

### MINOR-01 – README chưa liệt kê QA record trong file map chính

**Vị trí:** `README.md`, phần canonical file set.

README đã liên kết tới `QA_Review.md` ở mục QA, nhưng bảng artifact chính chưa liệt kê `QA_Review.md` hoặc `Review_Report.md`. Khi package có nhiều artifact review, nên đưa chúng vào file map để giáo viên biết đâu là bản kiểm định hiện hành.

**Đề xuất:** Thêm dòng:

```markdown
| QA/review | `QA_Review.md`, `Review_Report.md` | draft/review-needed | Hồ sơ kiểm tra và các finding |
```

**Severity:** `minor`.

### MINOR-02 – Thời lượng và reviewer vẫn là placeholder

**Vị trí:** `README.md`, phần metadata; `QA_Review.md`, mục scope/release.

Dự kiến 7 buổi là một giả định hợp lý cho MVP nhưng chưa phải quyết định chính thức. Reviewer chuyên môn, thời lượng thực tế và ngưỡng assessment vẫn chưa được chốt.

**Đề xuất:** Giữ trạng thái `draft`, nhưng trước vòng review lớp học nên ghi rõ số phút mỗi buổi, bài nào làm trên lớp/bài nào về nhà và ai chịu trách nhiệm duyệt.

**Severity:** `minor` trong draft; `major` trước release.

### MINOR-03 – Một số cú pháp phụ vẫn cần được giới thiệu theo nhịp

**Vị trí:** `Ly_Thuyet.md`, các phần dùng range-based `for` và `greater<int>()`.

`struct` và `pair` đã được loại khỏi luồng cơ bản. Range-based `for` và `greater<int>()` vẫn có thể dùng, nhưng nên được giới thiệu sau vòng lặp chỉ số và comparator tự viết, để học sinh hiểu bản chất trước khi dùng cách viết ngắn.

**Severity:** `minor`.

## 6. Kiểm tra alignment learning outcomes – assessment

| Learning outcome | Bằng chứng hiện có | Kết quả |
|---|---|---|
| `LO-S01` – dùng `sort` | Bài 1.1, 1.2, 1.4 và 1.7 | `pass` |
| `LO-S02` – comparator trên số nguyên | Bài 1.5, 1.6 và 1.11 | `pass` |
| `LO-S03` – nhận ra vai trò sorting | Bài 1.3, 1.4, 1.7, 1.9, 1.10 và 1.12 | `pass` |
| `LO-S04` – complexity | Bài 1.7, 1.10 và 1.12; câu hỏi cuối bài | `pass` nhưng cần rubric |
| `LO-S05` – nhận biết vị trí có thể thay đổi | Mục 8 trong lý thuyết và câu hỏi tự kiểm tra | `pass` ở mức nhận biết; chưa dạy cách lưu vị trí |
| `LO-S06` – transfer | Bài 1.10, 1.11 và 1.12 | `pass` ở mức draft |

**Nhận xét:** Alignment tổng thể tốt sau khi phạm vi comparator được thu hẹp về dãy số nguyên. `LO-S04` và `LO-S06` vẫn cần rubric chấm phần giải thích bằng lời, không chỉ chấm output code. Nội dung lưu vị trí ban đầu đã được chuyển thành nhận biết/phần mở rộng, phù hợp với mục tiêu không đưa `pair`/`struct` vào phần cơ bản.

## 7. Provenance và source integrity

Lesson đã khai báo `SRC-001`, `SRC-002` và `SRC-004`. Việc tham khảo bài `IKH-0016` trong Bài 1.10 phù hợp với source nội bộ: knowledge base mô tả bài này là dạng `Two Pointers, Sorting`, trình bày việc sắp xếp hai danh sách rồi dùng hai con trỏ và nêu độ phức tạp `O(N log N + M log M)` trong phần editorial.[1]

Giới hạn cần giữ:

- Roadmap hình chỉ là bản đồ chủ đề, không tự chứng minh toàn bộ thứ tự dạy.[2]
- Knowledge base là nguồn tham chiếu read-only; không sao chép credential hoặc thông tin vận hành nhạy cảm.[3]
- `REF-001` chỉ hỗ trợ cấu trúc artifact, không hỗ trợ tính đúng đắn chuyên môn của nội dung.[4]

**Kết quả provenance:** `needs-human-review`. Trước release, nên thêm claim IDs chi tiết cho các claim chuyên môn quan trọng vào evidence ledger, đặc biệt các claim về complexity, tính chất phần tử kề nhau sau sorting và phần liên hệ với bài `IKH-0016`.

## 8. Release gate

| Gate | Kết quả | Điều kiện còn lại |
|---|---|---|
| Scope/context | `pass` | Audience/level đã rõ ở mức draft; placement chính thức còn TBD |
| Source/factual integrity | `needs-human-review` | Bổ sung claim-level provenance trước release |
| Pedagogy/alignment | `pass` với điều kiện | Chuẩn hóa schema bài tập và rubric transfer |
| Subject matter/code | `pass` với điều kiện | Code cơ bản đã tách khỏi ví dụ nâng cao; tạo test nếu cần |
| Editorial consistency | `needs-human-review` | Thêm glossary, link bài tập và difficulty labels |
| Accessibility/rights | `pass` ở mức hiện tại | Cần rà soát bản in và quyền asset nếu bổ sung hình |
| Release status | `pass` | Đang dùng `draft`/`review-needed`, không gọi `final` |

## 9. Thứ tự sửa đề xuất

### Ưu tiên P0 – trước review với học sinh

- Chuẩn hóa cấu trúc 12 bài tập.
- Giữ `struct`/`pair` ngoài luồng bắt buộc và duy trì code tham chiếu một mục tiêu.
- Bổ sung liên kết `Ly_Thuyet.md` → `Bai_Tap.md` và glossary.

### Ưu tiên P1 – trước khi gọi review-needed chính thức

- Chốt thời lượng 7 buổi và phân bổ bài tập.
- Tạo rubric cho `LO-S04`, `LO-S05` và `LO-S06`.
- Bổ sung test/fixture nếu code được dùng trong chấm tự động.
- Bổ sung claim IDs vào evidence ledger.

### Ưu tiên P2 – trước khi in/phát hành

- Chốt reviewer chuyên môn và reviewer release.
- Chạy kiểm tra bản in, code block, bảng và liên kết.
- Rà soát license/attribution nếu thêm hình, sơ đồ hoặc asset ngoài source project.

## 10. Verdict

**Verdict: `review-needed` – cấu trúc đúng, luồng cơ bản đã phù hợp hơn với học sinh mới, nhưng chưa sẵn sàng phát hành.**

Không cần viết lại module từ đầu. `MAJOR-03` đã được xử lý trong ba file lesson; còn `MAJOR-01` và `MAJOR-02` vẫn cần hoàn thiện trước khi in. Outline Level 1 tổng quát còn mô tả `struct`/`pair`, nên cần một thay đổi đồng bộ riêng nếu muốn outline và lesson cùng phản ánh scaffold mới. Sau vòng review giáo viên, nên kiểm tra học sinh có phân biệt được comparator, sort và mục đích của bước sắp xếp hay không trước khi nhân rộng sang Module 02.

## References

[1]: ../../../../IKHEDU_Knowledge_Base.md "SRC-001 – IKHEDU Knowledge Base; phần IKH-0016, khoảng dòng 3010–3102"
[2]: ../../../../Lo_trinh_hoc_tap_bangB_level1.jpg "SRC-004 – Bảng B Level 1 roadmap"
[3]: ../../../../IKHEDU_Knowledge_Base.md "SRC-001 – chính sách source tham chiếu read-only"
[4]: ../../../../.agents/context/source-index.md "Source index – REF-001 chỉ là structural reference"
