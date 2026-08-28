---
name: cp-solve
description: Tạo problem package iKHEDU và bộ testcase competitive programming có generator, oracle, manifest, verification và teacher guide.
version: 1.0.0
requires_skills: ikhedu-authoring
artifact_outputs: De_Bai.md, Huong_Dan_Giang_Day.md, solution.cpp, generator, oracle, manifest, test-report
---
# /cp-solve - iKHEDU Problem + Testcase Builder
$ARGUMENTS

## Purpose

Dùng khi người dùng muốn biến một đề bài thuật toán thành package hoàn chỉnh để dạy, chấm tự động và có thể đưa vào sách. Workflow này tham khảo cấu trúc `DKTECHVN/ebook-ikh` và quy trình cp-solve của `code-testcase`, nhưng không sao chép nội dung hoặc coi các repository đó là source-of-truth.

## Steps

1. Đọc `@../skills/ikhedu-authoring/SKILL.md`, `@../context/project-context.md`, `@../context/source-index.md`, `@../context/evidence-ledger.md`, `@../context/decision-log.md` và `@../context/open-questions.md`.
2. Đọc `@../skills/ikhedu-authoring/references/problem-package-template.md` và `@../skills/ikhedu-authoring/references/testcase-generation-standard.md`.
3. Lập problem brief: `problem_id`, title, topic, target level, prerequisite, constraints, subtasks, time/memory limit, language, checker policy, output target và license. Nếu thiếu thông tin làm đổi thuật toán hoặc test, dừng để hỏi.
4. Tạo `De_Bai.md` theo góc nhìn học sinh, không tiết lộ lời giải. Tạo `Huong_Dan_Giang_Day.md` theo góc nhìn giáo viên, gồm câu hỏi dẫn dắt, trực giác, invariant/correctness, complexity, misconception và transfer.
5. Lập test matrix trước khi viết generator: sample, minimum, maximum/near-maximum, boundary, degenerate, duplicate/structured, adversarial, random-small và stress-large. Gắn mỗi case với subtask và bug target.
6. Tạo package:

```text
IKH-XXXX - [Tên bài]/
├── De_Bai.md
├── Huong_Dan_Giang_Day.md
├── solution.cpp
└── test/
    ├── README.md
    ├── manifest.json
    ├── generators/generate.py
    ├── oracle/reference.cpp hoặc reference.py
    ├── test01/problem.inp
    ├── test01/problem.out
    └── ...
```

7. Viết generator deterministic, seed cố định theo case, có validation input. Viết hoặc chỉ định oracle độc lập; không dùng duy nhất `solution.cpp` đang kiểm thử để sinh output. Ghi generator version, oracle version, seed, category, subtask, expected source và bug targets vào `manifest.json`.
8. Compile/run oracle và solution trong thư mục tạm với timeout, kiểm tra exit code/stderr/output checker. Chạy sample trước, sau đó toàn bộ test. Nếu có thể, đối chiếu miền nhỏ với brute-force và tạo mutant solution để kiểm tra test có bắt được lỗi.
9. Ghi `test/README.md` và test report: command tái tạo, số lượng case, category coverage, runtime, failure, giới hạn chưa cover và trạng thái `draft|review-needed|verified|blocked`.
10. Chạy QA cho statement–guide–solution–tests. Nếu `output_target` là `print|both`, chạy thêm print-ready gate và proof PDF theo `@../skills/ikhedu-authoring/references/print-production-spec-template.md`.
11. Bàn giao với các mục: `Status`, `Scope`, `Sources consulted`, `Package tree`, `Generator/oracle`, `Test matrix`, `Verification evidence`, `Print status`, `Unresolved issues`, `Next action`.

## Safety and boundaries

Không sửa source read-only. Không chạy script tải từ bên ngoài nếu chưa được cho phép. Không ghi secret tests vào tài liệu public. Không gọi `verified` chỉ vì generator chạy thành công; cần chứng minh input hợp lệ, oracle có provenance, solution pass và coverage đủ cho mục tiêu.
