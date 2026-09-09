# Hướng Dẫn Giảng Dạy: Đếm Số Đoạn Con Tổng Trong Đoạn [L, R]
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên và hai ngưỡng Lower, Upper. Hãy đếm số lượng đoạn con liên tiếp có tổng nằm trong đoạn [Lower, Upper].

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 -2 2 0 -3 -3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Đoạn con [0] ở vị trí 1 có tổng là 0 nằm trong khoảng [-2, 2]. Tổng cộng có 1 đoạn con thỏa mãn.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Đoạn con [0] ở vị trí 1 có tổng là 0 nằm trong khoảng [-2, 2]. Tổng cộng có 1 đoạn con thỏa mãn.

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

long long countSubarraysDac(vector<long long> &prefix, vector<long long> &temp, int l, int r, long long lower, long long upper) {
if (l >= r) return 0;
int mid = l + (r - l) / 2;
long long cnt = 0;
cnt += countSubarraysDac(prefix, temp, l, mid, lower, upper);
cnt += countSubarraysDac(prefix, temp, mid + 1, r, lower, upper);

int j1 = mid + 1, j2 = mid + 1;
for (int i = l; i <= mid; ++i) {
while (j1 <= r && prefix[j1] - prefix[i] < lower) j1++;
while (j2 <= r && prefix[j2] - prefix[i] <= upper) j2++;
cnt += (j2 - j1);
}

int i = l, j = mid + 1, k = l;
while (i <= mid && j <= r) {
if (prefix[i] <= prefix[j]) temp[k++] = prefix[i++];
else temp[k++] = prefix[j++];
}
while (i <= mid) temp[k++] = prefix[i++];
while (j <= r) temp[k++] = prefix[j++];
for (int idx = l; idx <= r; ++idx) prefix[idx] = temp[idx];

return cnt;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
int n;
long long lower, upper;
if (!(cin >> n >> lower >> upper)) return 0;
vector<long long> a(n);
vector<long long> prefix(n + 1, 0), temp(n + 1, 0);
for (int i = 0; i < n; ++i) {
cin >> a[i];
prefix[i + 1] = prefix[i] + a[i];
}
cout << countSubarraysDac(prefix, temp, 0, n, lower, upper) << "\n";
return 0;
}
```
