# Hướng Dẫn Giảng Dạy: Sinh Tất Cả Xâu Nhị Phân Độ Dài N
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương $N$. Hãy áp dụng mô hình thuật toán Quay lui chuẩn mực (`Choose` $\to$ `Explore` $\to$ `Unchoose`) để sinh và in ra tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển tăng dần.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với độ dài $N = 3$, không gian trạng thái nhị phân gồm $2^3 = 8$ xâu. Bắt đầu từ cấu hình nhỏ nhất theo từ điển là `000`... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `000 001 010 011 100 101 110 111` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với độ dài $N = 3$, không gian trạng thái nhị phân gồm $2^3 = 8$ xâu. Bắt đầu từ cấu hình nhỏ nhất theo từ điển là `000` và kết thúc ở cấu hình lớn nhất là `111`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int n;
string cur = "";

void backtrack(int step) {
    if (step > n) {
        cout << cur << "\n";
        return;
    }
    for (char c : {'0', '1'}) {
        cur.push_back(c);
        backtrack(step + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    backtrack(1);
    return 0;
}
```
