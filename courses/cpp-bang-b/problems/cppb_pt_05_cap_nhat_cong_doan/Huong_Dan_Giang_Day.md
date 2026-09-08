# Hướng Dẫn Giảng Dạy: Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên ban đầu toàn số 0. Thực hiện Q thao tác cộng giá trị X vào đoạn [L, R]. Hãy in ra mảng kết quả cuối cùng sau Q thao tác bằng kỹ thuật Mảng hiệu.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
  - Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
  - Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 1 3 2 2 5 3 3 4 -1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 3 2 2 5 3 3 4 -1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Sử dụng mảng hiệu D kích thước N + 2: - Cộng 2 vào [1, 3]: D[1] += 2, D[4] -= 2. - Cộng 3 vào [2, 5]: D[2] += 3, D[6] -=... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 5 4 2 3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Sử dụng mảng hiệu D kích thước N + 2:

- Cộng 2 vào [1, 3]: D[1] += 2, D[4] -= 2.
- Cộng 3 vào [2, 5]: D[2] += 3, D[6] -= 3.
- Cộng -1 vào [3, 4]: D[3] -= 1, D[5] += 1.
Tính tổng tiền tố của D để thu được mảng kết quả: 2 5 4 2 3.

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

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> d(n + 2, 0);

    while (q--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;
        d[l] += v;
        d[r + 1] -= v;
    }

    long long current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        cout << current << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
