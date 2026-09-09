# Hướng Dẫn Giảng Dạy: Tìm Min Trên Đoạn Bằng Chia Để Trị (RMQ D&C Cơ Bản)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên và Q truy vấn [L, R]. Hãy tìm giá trị nhỏ nhất trong đoạn [L, R] bằng đệ quy chia để trị.

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 2 3 1 4 2 5 1 3 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - Đoạn [1, 3] gồm {3, 1, 4} có min = 1. - Đoạn [3, 5] gồm {4, 2, 5} có min = 2.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - Đoạn [1, 3] gồm {3, 1, 4} có min = 1.

- Đoạn [3, 5] gồm {4, 2, 5} có min = 2.

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

long long queryMin(const vector<long long> &a, int l, int r) {
if (l == r) return a[l];
int mid = l + (r - l) / 2;
return min(queryMin(a, l, mid), queryMin(a, mid + 1, r));
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int n;
if (!(cin >> n)) return 0;
vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];
cout << queryMin(a, 0, n - 1) << "\n";
return 0;
}
```
