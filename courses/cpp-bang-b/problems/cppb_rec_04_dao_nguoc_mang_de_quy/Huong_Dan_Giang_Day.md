# Hướng Dẫn Giảng Dạy: Đảo Ngược Mảng Bằng Đệ Quy Hai Con Trỏ
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng số nguyên A gồm N phần tử. Hãy sử dụng hàm đệ quy 2 con trỏ reverseArray(A, L, R) để đảo ngược toàn bộ mảng tại chỗ.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
- Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
- Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 1 2 3 4 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng ban đầu [1, 2, 3, 4, 5] sau khi đảo ngược trở thành [5, 4, 3, 2, 1].... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5 4 3 2 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng ban đầu [1, 2, 3, 4, 5] sau khi đảo ngược trở thành [5, 4, 3, 2, 1].

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

void reverseRec(vector<long long> &a, int l, int r) {
if (l >= r) return;
swap(a[l], a[r]);
reverseRec(a, l + 1, r - 1);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int n;
if (!(cin >> n)) return 0;
vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];
reverseRec(a, 0, n - 1);
for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n "" : " ");
cout << "\n";
return 0;
}
```
