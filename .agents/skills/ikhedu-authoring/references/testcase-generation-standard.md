# iKHEDU Testcase Generation Standard

> Dùng cho `problem-package` khi bài có chấm tự động. Đây là chuẩn tổ chức và kiểm chứng; generator phải được viết riêng theo semantics của từng bài.

## 1. Nguyên tắc không thương lượng

Không dùng lời giải của thí sinh làm oracle duy nhất. Mỗi bộ test phải có một trong các nguồn đáp án sau: brute-force/reference solver độc lập cho miền nhỏ, oracle đã chứng minh đúng cho miền lớn, hoặc output được reviewer xác nhận. Nếu chỉ có một implementation, trạng thái chỉ là `needs-human-review`, không phải `verified`.

Testcase phải tái lập được. Generator dùng seed cố định cho từng case, ghi seed và generator version vào manifest, không phụ thuộc thời gian hệ thống, thứ tự file hoặc dữ liệu ngoài package. Không đưa thông tin riêng của solution vào generator theo cách làm mất khả năng bắt lỗi solution.

## 2. Cấu trúc package khuyến nghị

```text
problem-package/
├── De_Bai.md
├── Huong_Dan_Giang_Day.md
├── solution.cpp
└── test/
    ├── README.md
    ├── manifest.json
    ├── generators/
    │   └── generate.py
    ├── oracle/
    │   └── reference.cpp|.py
    ├── test01/
    │   ├── problem.inp
    │   └── problem.out
    ├── test02/
    │   ├── problem.inp
    │   └── problem.out
    └── ...
```

Nếu hệ thống chấm của project yêu cầu tên phẳng, dùng `problem_01.inp` và `problem_01.out`; ghi convention đó trong manifest. Không trộn `.inp/.out` với tên không có quy luật.

## 3. Test matrix tối thiểu

| Nhóm | Mục tiêu | Ví dụ |
|---|---|---|
| Sample | Khớp đề bài công bố | Mọi sample trong statement |
| Minimum | Biên nhỏ nhất hợp lệ | `N=1`, rỗng hợp lệ, giá trị nhỏ nhất |
| Maximum | Cận lớn nhất | `N=max`, giá trị max, tổng/ tích lớn |
| Boundary | Điểm chuyển điều kiện | `N=K`, `K±1`, duplicate, âm/0 |
| Degenerate | Cấu trúc suy biến | tất cả bằng nhau, tăng/giảm, một nhóm |
| Adversarial | Bắt lỗi thuật toán phổ biến | greedy sai, overflow, off-by-one, TLE |
| Random-small | Đối chiếu brute-force | seed cố định, nhiều phân bố |
| Stress-large | Kiểm tra complexity | input gần max, thời gian và bộ nhớ |

Mặc định có thể bắt đầu với 20 case giống convention của `code-testcase`, nhưng số lượng phải phục vụ coverage chứ không được coi 20 là quy tắc cứng. Mỗi case phải có `category`, `subtask`, `seed` (nếu random), `expected_source`, `bug_targets` và `status`.

## 4. Manifest contract

```json
{
  "problem_id": "IKH-XXXX",
  "format": "problem_XX.inp/problem_XX.out",
  "generator": "generators/generate.py",
  "generator_version": "0.1.0",
  "oracle": "oracle/reference.cpp",
  "seed_policy": "fixed-per-case",
  "cases": [
    {
      "id": "T01",
      "file_stem": "problem_01",
      "category": "sample",
      "subtask": "S1",
      "seed": null,
      "expected_source": "statement",
      "bug_targets": ["format"],
      "status": "verified"
    }
  ]
}
```

Manifest là bản đồ kiểm thử, không thay thế file input/output. Nếu output được sinh lại, cập nhật generator/oracle version và ghi decision log.

## 5. Quy trình sinh và xác minh

1. Đọc statement, constraints, subtasks và intended solution; lập test matrix trước khi code generator.
2. Viết generator deterministic, tách hàm tạo từng category; validate mọi input sinh ra theo constraints của statement.
3. Viết hoặc chỉ định oracle độc lập. Với case nhỏ, đối chiếu oracle tối ưu với brute-force; không dùng cùng bug-prone logic của solution.
4. Sinh input vào thư mục tạm, chạy oracle tạo output, kiểm tra exit code, timeout, stderr và định dạng output.
5. Chạy solution cần kiểm thử trên tất cả case với timeout/memory policy của project; so sánh output bằng checker phù hợp, không mặc định trim whitespace nếu whitespace có ý nghĩa.
6. Ghi kết quả vào `test/README.md` và manifest: số case, category coverage, oracle version, command, runtime, failure và timestamp/version.
7. Chạy mutation/thought experiment hoặc tạo các solution sai có chủ ý nếu có thể để chứng minh test bắt lỗi: off-by-one, overflow, bỏ boundary, greedy/DP sai, complexity quá chậm.
8. Chỉ đánh dấu `verified` khi input hợp lệ, output có provenance, solution pass, coverage hợp lý và reviewer chấp nhận các giới hạn còn lại.

## 6. An toàn thực thi

Chạy generator, oracle và solution trong thư mục tạm hoặc worktree riêng; không ghi đè source-of-truth. Dùng timeout, giới hạn output, kiểm tra exit code và dọn binary sinh ra. Không chạy code tải từ nguồn bên ngoài nếu chưa được chủ dự án cho phép. Không tự chạy test suite lớn trên máy người dùng nếu chưa báo phạm vi và tài nguyên dự kiến.

## 7. Liên kết với tài liệu học liệu

`De_Bai.md` phải mô tả constraints và format khớp với mọi input trong manifest. `Huong_Dan_Giang_Day.md` nên chỉ ra các nhóm edge case và lý do chọn chúng nhưng không tiết lộ đáp án của từng test nếu không cần. `solution.cpp` phải pass toàn bộ test. `test/README.md` là nơi ghi test contract, coverage và lệnh tái tạo.

## 8. Handoff

Bàn giao tối thiểu: đường dẫn generator, oracle, manifest, số lượng case, category coverage, lệnh chạy, kết quả solution, giới hạn chưa được cover, trạng thái `draft|review-needed|verified|blocked` và human review cần thiết.
