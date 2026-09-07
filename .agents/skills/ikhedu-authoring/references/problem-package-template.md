# Problem Package Template — Khuôn bài toán chấm tự động iKHEDU

> Dùng cho thư mục bài toán dạng `IKH-XXXX - [Tên bài]`. Đây là artifact đánh giá/chấm tự động, không phải lesson lý thuyết độc lập.

## Package identity

| Trường | Giá trị |
|---|---|
| `problem_id` | `IKH-XXXX` |
| `title` | TBD |
| `topic/skill` | TBD |
| `difficulty/rating` | TBD |
| `target_level` | TBD |
| `prerequisites` | TBD |
| `source_ids` | `SRC-001`, `SRC-002`, `SRC-004` hoặc source được index |
| `status` | `draft` / `review-needed` / `verified` |

## Canonical package tree

```text
IKH-XXXX - [Tên bài]/
├── De_Bai.md
├── Huong_Dan_Giang_Day.md
├── solution.cpp
└── test/
    ├── manifest.md hoặc init.yml
    ├── test01.in
    ├── test01.out
    └── ...
```

## `De_Bai.md` — Student-facing statement

Giữ cấu trúc tối thiểu và không đưa lời giải thuật toán vào bản người học:

1. `# Tiêu đề` (không đặt mã bài trong tiêu đề hoặc một heading riêng).
2. `## Bối cảnh`.
3. `## Nhiệm vụ`.
4. `## Input`.
5. `## Output`.
6. `## Sample 1` với `### Input`, `### Output`, `### Giải thích`; thêm `## Sample 2` nếu có sample thứ hai.
7. `## Ràng buộc` gồm giới hạn dữ liệu, thời gian và bộ nhớ.
8. Subtasks, góc kiến thức hoặc challenge question chỉ thêm khi được yêu cầu.

Không đưa `Mã bài toán`, gợi ý thuật toán, pseudocode hoặc solution vào `De_Bai.md`. Mã bài chỉ nằm ở package identity, tên thư mục hoặc metadata quản trị.

Bối cảnh có thể thực tế nhưng không được làm mơ hồ mô hình toán học. Kiểm tra mọi ký hiệu, chỉ số, đơn vị, giới hạn và expected output với solution/reference.

## `Huong_Dan_Giang_Day.md` — Teacher-facing guide

Dùng cấu trúc:

1. Mục tiêu học tập và prerequisite.
2. Phân tích đề: dữ liệu, yêu cầu, trường hợp biên.
3. Câu hỏi dẫn dắt tư duy theo từng bước.
4. Ý tưởng trực giác trước thuật toán.
5. Chiến lược/định lý hoặc invariant cần hiểu.
6. Pseudocode hoặc trace trên sample.
7. Phân tích độ đúng.
8. Phân tích độ phức tạp.
9. Các lỗi thường gặp và test để lộ lỗi.
10. Code tham chiếu hoặc liên kết tới `solution.cpp`.
11. Bài biến thể/transfer và câu hỏi tự giải thích.

Không viết “100% AC” nếu chưa thực sự chạy kiểm thử phù hợp. Tách rõ phần dành cho giáo viên với phần có thể chia sẻ cho học sinh.

## `solution.cpp` — Reference solution

Solution phải khớp hoàn toàn với statement, dùng kiểu dữ liệu phù hợp, xử lý boundary case, có complexity tương ứng với constraints và không chứa debug output. Khi sửa statement hoặc solution, phải kiểm tra artifact còn lại.

## `test/` — Test contract

Mỗi test phải có mục đích: sample, minimum, maximum/near-maximum, boundary, degenerate, duplicate, adversarial hoặc random. `manifest.md`/`init.yml` phải mô tả quy ước tên, generator nếu có, expected output và phạm vi coverage. Không khẳng định verified nếu solution chưa được compile/run trên toàn bộ test đã công bố.

Nếu project yêu cầu bộ test cố định, ghi rõ số lượng thực tế và command/reproduction steps trong review record thay vì giả định. Các test chứa dữ liệu bí mật phải được bảo vệ và không đưa vào tài liệu public.

## Release checklist

| Artifact | Kiểm tra |
|---|---|
| Statement | Input/output/constraints/sample khớp solution |
| Teaching guide | Có prerequisite, dẫn dắt, correctness, complexity và misconception |
| Solution | Compile sạch, đúng chuẩn ngôn ngữ và không debug output |
| Tests | Có coverage theo mục đích, expected output được kiểm tra |
| Cross-artifact | ID, title, thuật ngữ, notation và version khớp |
| Provenance | Claim/ý tưởng lấy từ source nào được ghi trong ledger |
| Status | Chỉ gắn `verified` sau khi có bằng chứng kiểm thử/review |
