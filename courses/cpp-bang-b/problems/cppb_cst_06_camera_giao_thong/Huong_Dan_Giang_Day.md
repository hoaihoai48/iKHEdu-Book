# Hướng Dẫn Giảng Dạy: Giám Sát Camera Giao Thông Thông Minh
Chuyên đề: **Bài 03: Kỹ thuật cửa sổ trượt**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng nhị phân A gồm N phần tử (1: hoạt động, 0: hỏng). Hãy tìm số lượng camera hỏng ít nhất cần sửa thành hoạt động sao cho trong mọi đoạn gồm K camera liên tiếp đều có ít nhất B camera hoạt động.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `10 6 5 1 0 1 1 0 1 1 1 0 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Đoạn từ vị trí 1 đến 6 là [1, 0, 1, 1, 0, 1] chỉ có 4 camera hoạt động (thiếu 1 camera so với chuẩn B = 5). Ta sửa camer... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Đoạn từ vị trí 1 đến 6 là [1, 0, 1, 1, 0, 1] chỉ có 4 camera hoạt động (thiếu 1 camera so với chuẩn B = 5). Ta sửa camera thứ 2 (hoặc thứ 5) từ 0 thành 1. Khi đó mọi đoạn 6 camera liên tiếp đều có ít nhất 5 camera hoạt động. Do đó chỉ cần sửa tối thiểu 1 camera.

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

int n, k;
if (!(cin >> n >> k)) return 0;

vector<int> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

int cur_broken = 0;
for (int i = 0; i < k; ++i) {
if (a[i] == 0) ++cur_broken;
}

int min_broken = cur_broken;
for (int i = k; i < n; ++i) {
if (a[i] == 0) ++cur_broken;
if (a[i - k] == 0) --cur_broken;
min_broken = min(min_broken, cur_broken);
}

cout << min_broken << "\n";
return 0;
}
```
