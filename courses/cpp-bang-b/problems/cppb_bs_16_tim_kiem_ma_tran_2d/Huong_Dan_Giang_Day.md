# Hướng Dẫn Giảng Dạy: Tìm Kiếm Trên Ma Trận 2D Đã Sắp Xếp (Matrix Search)
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận N x M đã sắp xếp theo quy tắc trên và số nguyên X. Hãy kiểm tra xem X có tồn tại trong ma trận không. In YES nếu có, ngược lại in NO.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 4 3 1 3 5 7 10 11 16 20)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 4 3 1 3 5 7 10 11 16 20 23 30 34 ` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số X = 3 nằm ở hàng 1, cột 2 của ma trận -> in YES.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số X = 3 nằm ở hàng 1, cột 2 của ma trận -> in YES.

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

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<long long>> a(n, vector<long long>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    while (q--) {
        long long target;
        cin >> target;

        int low = 0, high = n * m - 1;
        bool found = false;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int r = mid / m;
            int c = mid % m;

            if (a[r][c] == target) {
                found = true;
                break;
            } else if (a[r][c] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        cout << (found ? "YES\n" : "NO\n");
    }

    return 0;
}
```
