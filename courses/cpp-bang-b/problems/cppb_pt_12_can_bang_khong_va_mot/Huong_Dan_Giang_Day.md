# Hướng Dẫn Giảng Dạy: Đoạn Con Cân Bằng Số Lượng 0 và 1
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng nhị phân gồm N phần tử chỉ chứa các số 0 và 1. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có số lượng số 0 bằng số lượng số 1.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
  - Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
  - Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 0 1 0 0 1 1)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 0 1 0 0 1 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Toàn bộ mảng gồm 6 phần tử có 3 số 0 và 3 số 1 (số lượng số 0 bằng số lượng số 1). Do đó đoạn con cân bằng dài nhất có đ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Toàn bộ mảng gồm 6 phần tử có 3 số 0 và 3 số 1 (số lượng số 0 bằng số lượng số 1). Do đó đoạn con cân bằng dài nhất có độ dài bằng 6.

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
    if (!(cin >> n)) return 0;

    // Tiền tố có thể chạy từ -N đến +N, offset = n
    vector<int> first_pos(2 * n + 1, -2);
    first_pos[0 + n] = 0; // P[0] = 0 tại vị trí 0

    int current_sum = 0;
    int max_len = 0;

    for (int i = 1; i <= n; ++i) {
        int x;
        cin >> x;
        current_sum += (x == 1 ? 1 : -1);

        int idx = current_sum + n;
        if (first_pos[idx] != -2) {
            max_len = max(max_len, i - first_pos[idx]);
        } else {
            first_pos[idx] = i;
        }
    }

    cout << max_len << "\n";
    return 0;
}
```
