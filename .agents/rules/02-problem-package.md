---
name: 02-problem-package
version: 2.1.0
priority: P0
trigger: always_on
---

# iKHEDU Problem Package (cp-solve, Teacher Guide 9 phần)

Mọi problem tuân thủ workflow `cp-solve` (đúng chính tả, không phải `cp-slove`).

## De_Bai.md (student-facing, không spoil)
`# Tiêu đề` gợi hình đời sống; `## Bối cảnh` cốt truyện thực tế (cấm 1 dòng toán cụt lủn); `## Nhiệm vụ` tách bạch "Cho... Hãy lập trình..."; `## Input` chi tiết từng dòng/kích thước; `## Output` format + vô nghiệm; `## Sample 1` gồm Input/Output/Giải thích; `## Ràng buộc` ($1.0\text{s}$, $256\text{MB}$). Cấm dòng `Mã bài toán`/code trong statement.
`### Giải thích` bắt buộc trace tay từng bước trên số liệu sample, TUYỆT ĐỐI CẤM spoil tên thuật toán, công thức $dp$, `map`/`set`/`tree`, độ phức tạp.

## Huong_Dan_Giang_Day.md (đủ 9 phần)
1. Objectives 2. Phân tích & Edge cases 3. Câu hỏi Socratic 4. Chiến lược tối ưu & Invariant 5. Dry-run table trên sample 6. Complexity $\mathcal{O}$ 7. Bug traps 8. Code tham chiếu (Python không sys/main; C++ 0 `std::`) 9. Transfer & Extensions.

## Solution/Test
C++ `solution.cpp` theo 01-code-standards; Python `solution.py` theo 01-code-standards. Testcase Python là tùy chọn, chỉ tạo khi task/QA yêu cầu; khi tạo phải có test matrix + manifest + coverage.
