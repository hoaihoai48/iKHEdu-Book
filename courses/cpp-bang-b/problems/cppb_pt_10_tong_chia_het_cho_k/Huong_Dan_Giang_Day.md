# Hướng Dẫn Giảng Dạy: Đoạn Con Có Tổng Chia Hết Cho K
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm N số nguyên và số nguyên dương K. Hãy đếm số lượng đoạn con liên tiếp có tổng chia hết cho K.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
  - Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
  - Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 1 2 3 4 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các đoạn con liên tiếp có tổng chia hết cho 3 là: [1, 2] (tổng 3), [3] (tổng 3), [4, 5] (tổng 9), và [1, 2, 3] (tổng 6).... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các đoạn con liên tiếp có tổng chia hết cho 3 là: [1, 2] (tổng 3), [3] (tổng 3), [4, 5] (tổng 9), và [1, 2, 3] (tổng 6). Tổng cộng có 4 đoạn con thỏa mãn.

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
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> cnt(k, 0);
    cnt[0] = 1; // P[0] = 0

    long long current_sum = 0;
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        current_sum += x;
        long long rem = (current_sum % k + k) % k;
        cnt[rem]++;
    }

    long long total_pairs = 0;
    for (int r = 0; r < k; ++r) {
        total_pairs += cnt[r] * (cnt[r] - 1) / 2;
    }

    cout << total_pairs << "\n";
    return 0;
}
```
