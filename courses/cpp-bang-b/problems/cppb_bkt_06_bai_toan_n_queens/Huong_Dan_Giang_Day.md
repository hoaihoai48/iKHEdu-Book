# Hướng Dẫn Giảng Dạy: Bài Toán N-Queens (Đếm Số Cách)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho số nguyên dương $N$. Hãy áp dụng thuật toán Quay lui kết hợp các mảng đánh dấu cột, đường chéo chính và đường chéo phụ để đếm tổng số cách đặt $N$ quân hậu hợp lệ lên bàn cờ $N \times N$.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Trên bàn cờ kích thước $4 \times 4$, có đúng 2 cấu hình hợp lệ không quân hậu nào khống chế nhau: hàng 1 đặt ở cột 2, hà... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Trên bàn cờ kích thước $4 \times 4$, có đúng 2 cấu hình hợp lệ không quân hậu nào khống chế nhau: hàng 1 đặt ở cột 2, hàng 2 cột 4, hàng 3 cột 1, hàng 4 cột 3 (tức `[2, 4, 1, 3]`) và cấu hình đối xứng qua gương `[3, 1, 4, 2]`.

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
long long ans = 0;
vector<bool> col_used, diag1, diag2;

void backtrack(int row) {
    if (row > n) {
        ans++;
        return;
    }
    for (int col = 1; col <= n; ++col) {
        if (!col_used[col] && !diag1[row - col + n] && !diag2[row + col]) {
            col_used[col] = diag1[row - col + n] = diag2[row + col] = true;
            backtrack(row + 1);
            col_used[col] = diag1[row - col + n] = diag2[row + col] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n)) return 0;
    col_used.assign(n + 1, false);
    diag1.assign(2 * n + 1, false);
    diag2.assign(2 * n + 1, false);
    backtrack(1);
    cout << ans << "\n";
    return 0;
}
```
