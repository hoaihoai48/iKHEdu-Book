# Hướng Dẫn Giảng Dạy: Tập Hợp Độc Lập Về Bit Lớn Nhất
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho tập hợp N số nguyên dương (N <= 22). Hãy tìm kích thước lớn nhất của một tập con mà hai phần tử bất kỳ trong tập con đều có tích bit AND bằng 0.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 1 2 4 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 1 2 4 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Tập con {1, 2, 4} gồm 3 số có các bit 1 độc lập từng đôi một: (1&2=0, 1&4=0, 2&4=0). Số lượng phần tử lớn nhất là 3.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Tập con {1, 2, 4} gồm 3 số có các bit 1 độc lập từng đôi một: (1&2=0, 1&4=0, 2&4=0). Số lượng phần tử lớn nhất là 3.

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

    int max_size = 0;
    int total_masks = (1 << n);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long used_bits = 0;
        bool valid = true;
        int current_count = 0;

        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                if (used_bits & a[i]) {
                    valid = false;
                    break;
                }
                used_bits |= a[i];
                current_count++;
            }
        }

        if (valid) {
            max_size = max(max_size, current_count);
        }
    }

    cout << max_size << "\n";
    return 0;
}
```
