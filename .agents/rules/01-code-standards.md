---
name: 01-code-standards
version: 2.1.0
priority: P0
trigger: always_on
---

# iKHEDU Code & Trình bày chuẩn

## C++ (khóa C++, bắt buộc 100%)
1. Header duy nhất `#include <bits/stdc++.h>` + `using namespace std;`.
2. Fast I/O đầu `main()`: `ios::sync_with_stdio(false); cin.tie(nullptr);`
3. Safe input: `if (!(cin >> n >> ...)) return 0;`
4. Cấm tiền tố `std::`, cấm nhắc header lẻ `<algorithm>`, `<vector>`. Gọi trực tiếp `sort`, `vector`, `lower_bound`, `min`, `cin`.

## Python (khóa Python Bảng A)
`solution.py`: Python 3, đọc/ghi bằng `input()`/`print()` trực tiếp. Cấm `import sys`/`sys.stdin`/`sys.stdout`, cấm `def main()`, cấm `if __name__ == "__main__":`. Không tạo `test/` mặc định trừ khi task yêu cầu.

## Dữ liệu & Markdown/KaTeX
- Ưu tiên kiểu nguyên bản + `vector<vector<long long>>` để dùng `sort` mặc định. `pair`/`struct` chỉ khi bất đắc dĩ (đa trường khác kiểu, comparator `a+b>b+a`).
- Module 01/02: TUYỆT ĐỐI CHƯA DÙNG `set`, `map`, `deque`, `priority_queue`, Segment Tree, Fenwick, DP.
- Không vẽ ASCII (`│┌└`). Minh họa bằng Markdown Table + KaTeX. Callout tiếng Việt đơn giản (`> ⚠️ **Lưu ý:**`, `> 💡 **Mẹo nhớ:**`), cấm `> [!CAUTION]`.

## Learning loop mỗi Lesson
Hook/Vấn đề -> Mô phỏng tay -> Lý thuyết & Invariant -> Code & Bẫy lỗi -> Micro P0 -> Quiz -> P1-P3 -> Mastery P4/P5. 1 Lesson = 1 đơn vị kiến thức lớn, >=10 Quiz và >=14 bài tập là ngưỡng tối thiểu.
