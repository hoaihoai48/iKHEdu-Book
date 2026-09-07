# Hướng Dẫn Giảng Dạy: Bài Toán Tổng Tập Con Bằng S (Subset Sum)
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy gồm N số nguyên dương và số nguyên dương S. Hãy kiểm tra xem có tồn tại một tập con có tổng đúng bằng S hay không. In YES nếu có, ngược lại in NO.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 9 3 34 4 12)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 9 3 34 4 12` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các tập con có thể tạo được từ {3, 34, 4, 12} có tổng lần lượt là: 0, 3, 34, 37, 4, 7, 38, 41, 12, 15, 46, 49, 16, 19, 5... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `NO` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các tập con có thể tạo được từ {3, 34, 4, 12} có tổng lần lượt là: 0, 3, 34, 37, 4, 7, 38, 41, 12, 15, 46, 49, 16, 19, 50, 53. Không có tập con nào có tổng bằng 9. Vì vậy in NO.

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
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int total_masks = (1 << n);
    for (int mask = 0; mask < total_masks; ++mask) {
        long long current_sum = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_sum += a[i];
            }
        }
        if (current_sum == s) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}
```
