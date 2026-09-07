# Hướng Dẫn Giảng Dạy: Sinh Tất Cả Tổ Hợp Chập K Của N
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 16$). Hãy sử dụng thuật toán Quay lui có điều kiện chặn dưới tăng dần để sinh và in ra tất cả các tổ hợp chập $K$ của tập $\{1, 2, \dots, N\}$ theo thứ tự từ điển tăng dần.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số lượng tổ hợp chập 2 của 4 chuyên gia là $C(4, 2) = \frac{4!}{2!2!} = 6$ tiểu ban. Các tiểu ban được liệt kê lần lượt ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2 1 3 1 4 2 3 2 4 3 4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số lượng tổ hợp chập 2 của 4 chuyên gia là $C(4, 2) = \frac{4!}{2!2!} = 6$ tiểu ban. Các tiểu ban được liệt kê lần lượt theo thứ tự từ điển: `1 2`, `1 3`, `1 4`, `2 3`, `2 4`, `3 4`.

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

int n, k;
vector<int> cur;

void backtrack(int step, int start_val) {
    if (step > k) {
        for (int i = 0; i < k; ++i) cout << cur[i] << (i + 1 == k ? "" : " ");
        cout << "\n";
        return;
    }
    for (int val = start_val; val <= n - (k - step); ++val) {
        cur.push_back(val);
        backtrack(step + 1, val + 1);
        cur.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> k)) return 0;
    backtrack(1, 1);
    return 0;
}
```
