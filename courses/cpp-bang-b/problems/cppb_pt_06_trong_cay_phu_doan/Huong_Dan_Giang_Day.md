# Hướng Dẫn Giảng Dạy: Trồng Cây Phủ Đoạn Tối Ưu
Chuyên đề: **Bài 04: Mảng tiền tố & mảng hiệu**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N vị trí và Q đoạn [L, R]. Hãy đếm số lượt phủ của mỗi vị trí từ 1 đến N sau Q lần thao tác.

- **Phương pháp tiếp cận — Mảng tiền tố & Mảng hiệu:**
  - Dựng mảng cộng dồn `pref[i] = pref[i-1] + a[i]`. Khi đó tổng đoạn $[L, R]$ được tính tức thì bằng `pref[R] - pref[L-1]` trong $\mathcal{O}(1)$.
  - Với các thao tác cộng dồn đoạn, sử dụng mảng hiệu `diff[L] += V, diff[R+1] -= V` rồi cộng dồn để phục hồi mảng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 1 3 2 4 2 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 3 2 4 2 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mỗi đoạn [L, R] tương ứng với thao tác cộng 1 vào đoạn [L, R]. Mảng hiệu ghi nhận số lượt tưới tại từng vị trí lần lượt ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 3 3 2 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mỗi đoạn [L, R] tương ứng với thao tác cộng 1 vào đoạn [L, R]. Mảng hiệu ghi nhận số lượt tưới tại từng vị trí lần lượt là: vị trí 1 được 1 lượt, vị trí 2 được 3 lượt, vị trí 3 được 3 lượt, vị trí 4 được 2 lượt, vị trí 5 được 1 lượt. Kết quả in ra: 1 3 3 2 1.

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

    int n, q, k;
    if (!(cin >> n >> q >> k)) return 0;

    vector<int> d(n + 2, 0);
    while (q--) {
        int l, r;
        cin >> l >> r;
        d[l]++;
        d[r + 1]--;
    }

    int count_ge_k = 0;
    int current = 0;
    for (int i = 1; i <= n; ++i) {
        current += d[i];
        if (current >= k) {
            count_ge_k++;
        }
    }

    cout << count_ge_k << "\n";
    return 0;
}
```
