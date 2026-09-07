# Hướng Dẫn Giảng Dạy: Tìm Hình Vuông K x K Có Tổng Lớn Nhất
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận A kích thước N x M và số nguyên dương K (K <= min(N, M)). Hãy tìm tổng lớn nhất của một ma trận con hình vuông kích thước K x K.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
  - Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
  - Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 3 2 1 1 1 1 2 2 1 2 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 2 1 1 1 1 2 2 1 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Hình vuông kích thước 2 x 2 ở góc dưới phải gồm các ô: {2, 2, 2, 3} có tổng là 2 + 2 + 2 + 3 = 9. Đây là hình vuông kích... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `9` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Hình vuông kích thước 2 x 2 ở góc dưới phải gồm các ô: {2, 2, 2, 3} có tổng là 2 + 2 + 2 + 3 = 9. Đây là hình vuông kích thước 2 x 2 có tổng lớn nhất.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<long long>> p(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long val;
            cin >> val;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + val;
        }
    }

    long long max_sum = -4e18; // Khởi tạo âm vô cùng
    for (int i = k; i <= n; ++i) {
        for (int j = k; j <= m; ++j) {
            long long current = p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k];
            max_sum = max(max_sum, current);
        }
    }

    cout << max_sum << "\n";
    return 0;
}
```
