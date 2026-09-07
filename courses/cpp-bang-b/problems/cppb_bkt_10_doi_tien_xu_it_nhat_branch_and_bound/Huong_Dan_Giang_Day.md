# Hướng Dẫn Giảng Dạy: Đổi Tiền Xu Ít Nhất (B&B Coin Change)
Chuyên đề: **Bài 12: Thuật toán quay lui & nhánh cận**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho $N$ mệnh giá tiền xu $C_1, C_2, \dots, C_N$ và số tiền cần đổi $S$. Hãy áp dụng thuật toán Nhánh Cận (Branch and Bound) với hàm cận dưới tối ưu để tìm số lượng đồng xu ít nhất cần dùng để đổi đúng số tiền $S$. Nếu không có phương án đổi tiền nào hợp lệ, in ra `-1`.

- **Phương pháp tiếp cận — Quay lui & Nhánh cận (Backtracking):**
  - Xây dựng không gian trạng thái dạng cây tìm kiếm.
  - Thử từng khả năng, nếu vi phạm điều kiện ràng buộc thì tỉa nhánh sớm (nhánh cận) để giảm số trạng thái cần duyệt.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 11 1 2 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 11 1 2 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Với số tiền $S = 11$ và các mệnh giá $\{1, 2, 5\}$, phương án tối ưu nhất là chọn hai đồng mệnh giá 5 và một đồng mệnh g... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Với số tiền $S = 11$ và các mệnh giá $\{1, 2, 5\}$, phương án tối ưu nhất là chọn hai đồng mệnh giá 5 và một đồng mệnh giá 1 ($5 + 5 + 1 = 11$). Tổng số đồng xu sử dụng là 3 đồng.

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
long long S;
vector<long long> c;
long long best_coins = 1e9;

void branchAndBound(int idx, long long remain, long long count) {
    // Optimality Pruning
    if (count + (remain + c[0] - 1) / c[0] >= best_coins) return;

    if (remain == 0) {
        best_coins = min(best_coins, count);
        return;
    }
    if (idx >= n) return;

    long long max_use = remain / c[idx];
    for (long long k = max_use; k >= 0; --k) {
        if (count + k + (remain - k * c[idx] + c[0] - 1) / c[0] < best_coins) {
            branchAndBound(idx + 1, remain - k * c[idx], count + k);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> S)) return 0;
    c.resize(n);
    for (int i = 0; i < n; ++i) cin >> c[i];
    sort(c.rbegin(), c.rend());
    branchAndBound(0, S, 0);
    if (best_coins > 1e8) cout << -1 << "\n";
    else cout << best_coins << "\n";
    return 0;
}
```
