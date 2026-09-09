# Hướng Dẫn Giảng Dạy: Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên đã sắp xếp tăng dần và số nguyên X. Hãy tìm vị trí (1-indexed) của X bằng đệ quy chia để trị. Nếu không tìm thấy, in ra -1.

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 7 1 3 5 7 9` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Số 7 nằm ở vị trí thứ 4 trong mảng đã sắp xếp. Kết quả in ra: 4.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Số 7 nằm ở vị trí thứ 4 trong mảng đã sắp xếp. Kết quả in ra: 4.

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

int binarySearchDac(const vector<long long> &a, int l, int r, long long x) {
if (l > r) return -1;
int mid = l + (r - l) / 2;
if (a[mid] == x) {
int left_res = binarySearchDac(a, l, mid - 1, x);
if (left_res != -1) return left_res;
return mid;
}
if (a[mid] > x) return binarySearchDac(a, l, mid - 1, x);
return binarySearchDac(a, mid + 1, r, x);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int n;
long long x;
if (!(cin >> n >> x)) return 0;
vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];
int ans = binarySearchDac(a, 0, n - 1, x);
if (ans != -1) ans += 1;
cout << ans << "\n";
return 0;
}
```
