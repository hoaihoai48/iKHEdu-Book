# Hướng Dẫn Giảng Dạy: Chia Kẹo Cho Học Sinh Đạt Chuẩn
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N gói kẹo và số học sinh K. Mỗi học sinh chỉ nhận kẹo từ cùng 1 gói. Hãy tìm số kẹo X lớn nhất phát đều cho K học sinh.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 6 15 8 10 7)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 6 15 8 10 7` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Nếu mỗi em nhận X = 5 chiếc kẹo: - Thùng 1 (15 kẹo) chia được 15/5 = 3 em. - Thùng 2 (8 kẹo) chia được 8/5 = 1 em. - Thù... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Nếu mỗi em nhận X = 5 chiếc kẹo:

- Thùng 1 (15 kẹo) chia được 15/5 = 3 em.
- Thùng 2 (8 kẹo) chia được 8/5 = 1 em.
- Thùng 3 (10 kẹo) chia được 10/5 = 2 em.
- Thùng 4 (7 kẹo) chia được 7/5 = 1 em.
Tổng số em được nhận là 3 + 1 + 2 + 1 = 7 >= 6 em. Nếu tăng X = 6 sẽ không đủ 6 phần. Vậy X lớn nhất là 5.

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

bool check(long long mid, const vector<long long>& a, long long k) {
    long long count = 0;
    for (long long x : a) {
        count += (x / mid);
    }
    return count >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    long long low = 1, high = max_val, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, a, k)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
