# Hướng Dẫn Giảng Dạy: Đếm Cặp Có Tích Bit AND Bằng 0
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên không âm. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn: A[i] & A[j] == 0.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 1 2 4 8)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 1 2 4 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các số 1 (0001_2), 2 (0010_2), 4 (0100_2), 8 (1000_2) đều có các bit 1 ở vị trí hoàn toàn khác nhau. Do đó tích bit AND ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `6` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các số 1 (0001_2), 2 (0010_2), 4 (0100_2), 8 (1000_2) đều có các bit 1 ở vị trí hoàn toàn khác nhau. Do đó tích bit AND giữa hai số bất kỳ đều bằng 0. Số cặp là C(4, 2) = 6 cặp.

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

    const int MAX_VAL = 4096;
    vector<long long> cnt(MAX_VAL, 0);

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    long long total_pairs = 0;

    // Trường hợp u == 0
    total_pairs += cnt[0] * (cnt[0] - 1) / 2;
    for (int v = 1; v < MAX_VAL; ++v) {
        total_pairs += cnt[0] * cnt[v];
    }

    // Trường hợp 1 <= u < v
    for (int u = 1; u < MAX_VAL; ++u) {
        if (cnt[u] == 0) continue;
        for (int v = u + 1; v < MAX_VAL; ++v) {
            if ((u & v) == 0) {
                total_pairs += cnt[u] * cnt[v];
            }
        }
    }

    cout << total_pairs << "\n";
    return 0;
}
```
