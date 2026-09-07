# Hướng Dẫn Giảng Dạy: Đếm Số Cặp Có Tổng Bằng Lũy Thừa Của 2
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên dương. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] + A[j] là một lũy thừa của 2.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 1 1 3 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 1 1 3 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cặp chỉ số $(i, j)$ có tổng là lũy thừa của 2 gồm 3 cặp: - $(1, 3)$: tổng $1 + 3 = 4 = 2^2$. - $(1, 7)$: tổng $1 + 7... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cặp chỉ số $(i, j)$ có tổng là lũy thừa của 2 gồm 3 cặp:
- $(1, 3)$: tổng $1 + 3 = 4 = 2^2$.
- $(1, 7)$: tổng $1 + 7 = 8 = 2^3$.
- $(1, 15)$: tổng $1 + 15 = 16 = 2^4$.
Vậy có đúng 3 cặp thỏa mãn.

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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());

    long long total_pairs = 0;

    for (int i = 0; i < n; ++i) {
        for (int k = 1; k <= 30; ++k) {
            long long target = (1LL << k) - a[i];
            if (target <= 0) continue;

            auto it1 = lower_bound(a.begin() + i + 1, a.end(), target);
            auto it2 = upper_bound(a.begin() + i + 1, a.end(), target);
            total_pairs += (it2 - it1);
        }
    }

    cout << total_pairs << "\n";
    return 0;
}
```
