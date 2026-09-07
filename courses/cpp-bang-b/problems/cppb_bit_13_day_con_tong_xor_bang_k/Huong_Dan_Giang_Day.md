# Hướng Dẫn Giảng Dạy: Tìm Dãy Con Có Tổng XOR Bằng K
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho tập hợp gồm N số nguyên dương và số nguyên K. Hãy kiểm tra xem có tồn tại một dãy con khác rỗng có tổng XOR bằng K hay không. In YES nếu có, ngược lại in NO.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
  - Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
  - Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4 7 1 2 4 8)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `4 7 1 2 4 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Chọn tập con gồm 3 phần tử {1, 2, 4} có tổng XOR là 1 ^ 2 ^ 4 = 7 đúng bằng K. Kết quả in ra: YES.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `YES` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Chọn tập con gồm 3 phần tử {1, 2, 4} có tổng XOR là 1 ^ 2 ^ 4 = 7 đúng bằng K. Kết quả in ra: YES.

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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int count_k = 0;
    int total_masks = (1 << n);

    for (int mask = 1; mask < total_masks; ++mask) {
        long long current_xor = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                current_xor ^= a[i];
            }
        }
        if (current_xor == k) {
            count_k++;
        }
    }

    cout << count_k << "\n";
    return 0;
}
```
