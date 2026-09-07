# Hướng Dẫn Giảng Dạy: Median Của Hai Mảng Đã Sắp Xếp
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho 2 mảng tăng dần A (kích thước N) và B (kích thước M). Hãy tìm giá trị trung vị của mảng hợp nhất với độ chính xác 1 chữ số thập phân trong thời gian O(log(min(N, M))).

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 1 1 3 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 1 1 3 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng hợp nhất: [1, 2, 3] có 3 phần tử, phần tử ở giữa là 2. Trung vị là 2.0.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2.0` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng hợp nhất: [1, 2, 3] có 3 phần tử, phần tử ở giữa là 2. Trung vị là 2.0.

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

long long findKth(const vector<long long> &A, int a_l, const vector<long long> &B, int b_l, int k) {
    if (a_l >= (int)A.size()) return B[b_l + k - 1];
    if (b_l >= (int)B.size()) return A[a_l + k - 1];
    if (k == 1) return min(A[a_l], B[b_l]);

    int a_mid = a_l + k / 2 - 1;
    int b_mid = b_l + k / 2 - 1;

    long long a_val = (a_mid < (int)A.size()) ? A[a_mid] : 2e18;
    long long b_val = (b_mid < (int)B.size()) ? B[b_mid] : 2e18;

    if (a_val <= b_val) {
        return findKth(A, a_l + k / 2, B, b_l, k - k / 2);
    } else {
        return findKth(A, a_l, B, b_l + k / 2, k - k / 2);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];
    int total = n + m;
    int k = (total % 2 == 1) ? (total / 2 + 1) : (total / 2);
    cout << findKth(a, 0, b, 0, k) << "\n";
    return 0;
}
```
