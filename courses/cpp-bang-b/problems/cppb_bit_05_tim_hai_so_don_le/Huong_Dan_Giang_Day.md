# Hướng Dẫn Giảng Dạy: Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm 2N + 2 số nguyên, trong đó mọi phần tử xuất hiện 2 lần trừ đúng 2 phần tử X và Y xuất hiện 1 lần duy nhất. Hãy tìm và in ra X, Y theo thứ tự tăng dần.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 1 2 3 2 1 4)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 1 2 3 2 1 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các số 1 và 2 đều xuất hiện 2 lần. Hai số chỉ xuất hiện 1 lần duy nhất là 3 và 4. Kết quả in theo thứ tự tăng dần: 3 4.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3 4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các số 1 và 2 đều xuất hiện 2 lần. Hai số chỉ xuất hiện 1 lần duy nhất là 3 và 4. Kết quả in theo thứ tự tăng dần: 3 4.

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

    int total_elements = 2 * n + 2;
    vector<long long> a(total_elements);
    long long xor_sum = 0;
    for (int i = 0; i < total_elements; ++i) {
        cin >> a[i];
        xor_sum ^= a[i];
    }

    // Lấy bit 1 phân biệt
    long long diff_bit = xor_sum & (-xor_sum);

    long long num1 = 0, num2 = 0;
    for (long long val : a) {
        if (val & diff_bit) {
            num1 ^= val;
        } else {
            num2 ^= val;
        }
    }

    if (num1 > num2) swap(num1, num2);
    cout << num1 << " " << num2 << "\n";
    return 0;
}
```
