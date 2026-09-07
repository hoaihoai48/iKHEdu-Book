# Hướng Dẫn Giảng Dạy: Gộp Hai Mảng Đã Sắp Xếp (Merge Step)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 mảng tăng dần A (kích thước N) và B (kích thước M). Hãy gộp hai mảng thành một dãy tăng dần duy nhất.

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 3 1 4 7 2 5 6)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 3 1 4 7 2 5 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Gộp hai mảng [1, 4, 7] và [2, 5, 6] ta được mảng tăng dần hoàn chỉnh: 1 2 4 5 6 7.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2 4 5 6 7` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Gộp hai mảng [1, 4, 7] và [2, 5, 6] ta được mảng tăng dần hoàn chỉnh: 1 2 4 5 6 7.

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
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    int i = 0, j = 0;
    bool first = true;
    while (i < n && j < m) {
        if (!first) cout << " ";
        if (a[i] <= b[j]) {
            cout << a[i++];
        } else {
            cout << b[j++];
        }
        first = false;
    }
    while (i < n) {
        if (!first) cout << " ";
        cout << a[i++];
        first = false;
    }
    while (j < m) {
        if (!first) cout << " ";
        cout << b[j++];
        first = false;
    }
    cout << "\n";
    return 0;
}
```
