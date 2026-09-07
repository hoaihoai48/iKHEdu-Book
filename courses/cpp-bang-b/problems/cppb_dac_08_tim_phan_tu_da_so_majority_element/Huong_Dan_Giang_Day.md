# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Đa Số (Majority Element) D&C
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên. Hãy tìm phần tử đa số (xuất hiện > N / 2 lần). Nếu không tồn tại, in ra -1.

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 2 2 1 1 1 2 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `7 2 2 1 1 1 2 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số 2 xuất hiện 4 lần trên tổng số 7 phần tử (4 > 7/2 = 3.5). Do đó phần tử đa số là 2.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số 2 xuất hiện 4 lần trên tổng số 7 phần tử (4 > 7/2 = 3.5). Do đó phần tử đa số là 2.

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

int countInRange(const vector<long long> &a, long long target, int l, int r) {
    int cnt = 0;
    for (int i = l; i <= r; ++i) if (a[i] == target) cnt++;
    return cnt;
}

long long majorityDac(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    long long left_maj = majorityDac(a, l, mid);
    long long right_maj = majorityDac(a, mid + 1, r);

    if (left_maj == right_maj) return left_maj;

    int left_count = countInRange(a, left_maj, l, r);
    int right_count = countInRange(a, right_maj, l, r);

    return (left_count > right_count) ? left_maj : right_maj;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    long long cand = majorityDac(a, 0, n - 1);
    int total_cnt = 0;
    for (long long x : a) if (x == cand) total_cnt++;
    if (total_cnt > n / 2) {
        cout << cand << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
```
