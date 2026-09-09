# Hướng Dẫn Giảng Dạy: Đếm Số Cặp Nghịch Thế (Inversion Count)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N sao cho A[i] > A[j].

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 2 4 1 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Các cặp nghịch thế gồm: (2, 1) tại vị trí (1, 3); (4, 1) tại vị trí (2, 3); và (4, 3) tại vị trí (2, 4). Tổng cộng có 3 ... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Các cặp nghịch thế gồm: (2, 1) tại vị trí (1, 3); (4, 1) tại vị trí (2, 3); và (4, 3) tại vị trí (2, 4). Tổng cộng có 3 cặp nghịch thế.

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

long long countInversions(vector<long long> &a, vector<long long> &temp, int l, int r) {
if (l >= r) return 0;
int mid = l + (r - l) / 2;
long long inv = 0;
inv += countInversions(a, temp, l, mid);
inv += countInversions(a, temp, mid + 1, r);

int i = l, j = mid + 1, k = l;
while (i <= mid && j <= r) {
if (a[i] <= a[j]) {
temp[k++] = a[i++];
} else {
temp[k++] = a[j++];
inv += (mid - i + 1);
}
}
while (i <= mid) temp[k++] = a[i++];
while (j <= r) temp[k++] = a[j++];
for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
return inv;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int n;
if (!(cin >> n)) return 0;
vector<long long> a(n), temp(n);
for (int i = 0; i < n; ++i) cin >> a[i];
cout << countInversions(a, temp, 0, n - 1) << "\n";
return 0;
}
```
