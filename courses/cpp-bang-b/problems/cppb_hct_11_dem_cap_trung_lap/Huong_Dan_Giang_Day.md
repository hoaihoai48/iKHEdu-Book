# Hướng Dẫn Giảng Dạy: Đếm Cặp Tổng S Trên Mảng Trùng Lặp
Chuyên đề: **Bài 02: Kỹ thuật hai con trỏ**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên có thể chứa nhiều phần tử trùng lặp và số nguyên S. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] + A[j] = S.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 6 3 3 3 3 3 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 6 3 3 3 3 3 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng gồm 6 phần tử đều bằng 3 và mục tiêu S = 6. Vì mọi cặp chỉ số (i, j) với 1 <= i < j <= 6 đều có tổng A[i] + A[j] = ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `15` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng gồm 6 phần tử đều bằng 3 và mục tiêu S = 6. Vì mọi cặp chỉ số (i, j) với 1 <= i < j <= 6 đều có tổng A[i] + A[j] = 3 + 3 = 6, nên số lượng cặp thỏa mãn chính là số cách chọn 2 phần tử từ 6 phần tử: C(6, 2) = 6 * 5 / 2 = 15 cặp.

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

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    sort(a.begin(), a.end());

    int l = 0, r = n - 1;
    long long ans = 0;

    while (l < r) {
        long long sum = a[l] + a[r];
        if (sum == s) {
            if (a[l] == a[r]) {
                long long cnt = r - l + 1;
                ans += cnt * (cnt - 1) / 2;
                break;
            } else {
                long long c1 = 1, c2 = 1;
                while (l + 1 < r && a[l + 1] == a[l]) { ++c1; ++l; }
                while (r - 1 > l && a[r - 1] == a[r]) { ++c2; --r; }
                ans += c1 * c2;
                ++l;
                --r;
            }
        } else if (sum < s) {
            ++l;
        } else {
            --r;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
