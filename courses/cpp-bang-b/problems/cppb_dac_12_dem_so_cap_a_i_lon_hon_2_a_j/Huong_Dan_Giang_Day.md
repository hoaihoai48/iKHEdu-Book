# Hướng Dẫn Giảng Dạy: Đếm Số Cặp A_i > 2 * A_j (Significant Inversions)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên. Hãy đếm số cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn A[i] > 2 * A[j].

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 1 3 2 3 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 1 3 2 3 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cặp thỏa mãn là: (3, 1) tại vị trí (2, 5) vì 3 > 2*1; và (3, 1) tại vị trí (4, 5) vì 3 > 2*1. Tổng cộng có 2 cặp.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cặp thỏa mãn là: (3, 1) tại vị trí (2, 5) vì 3 > 2*1; và (3, 1) tại vị trí (4, 5) vì 3 > 2*1. Tổng cộng có 2 cặp.

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

long long countSignificant(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long cnt = 0;
    cnt += countSignificant(a, temp, l, mid);
    cnt += countSignificant(a, temp, mid + 1, r);

    // Bước đếm 2 con trỏ trước khi merge
    int j = mid + 1;
    for (int i = l; i <= mid; ++i) {
        while (j <= r && a[i] > 2LL * a[j]) j++;
        cnt += (j - (mid + 1));
    }

    // Merge bình thường
    int i = l, k = l;
    j = mid + 1;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << countSignificant(a, temp, 0, n - 1) << "\n";
    return 0;
}
```
