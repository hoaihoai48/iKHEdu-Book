# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất
Chuyên đề: **Bài 06: Phép toán BIT & biểu diễn trạng thái**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng gồm 2N + 1 số nguyên, trong đó mọi phần tử đều xuất hiện đúng 2 lần trừ 1 phần tử xuất hiện đúng 1 lần. Hãy tìm phần tử duy nhất đó.

- **Phương pháp tiếp cận — Phép toán BIT & Bitmask:**
- Biểu diễn tập hợp hoặc trạng thái bật/tắt bằng các bit của số nguyên 64-bit.
- Sử dụng các toán tử bitwise `&, |, ^, ~, <<, >>` để thao tác đồng thời trong $\mathcal{O}(1)$ chu kỳ máy.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `2 4 1 2 1 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các số 1 và 2 đều xuất hiện 2 lần. Số 4 chỉ xuất hiện 1 lần duy nhất. Phép XOR toàn bộ mảng triệt tiêu các cặp giống nha... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các số 1 và 2 đều xuất hiện 2 lần. Số 4 chỉ xuất hiện 1 lần duy nhất. Phép XOR toàn bộ mảng triệt tiêu các cặp giống nhau và giữ lại đúng số 4. Kết quả in ra: 4.

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

int total_elements = 2 * n + 1;
long long ans = 0;
for (int i = 0; i < total_elements; ++i) {
long long x;
cin >> x;
ans ^= x;
}

cout << ans << "\n";
return 0;
}
```
