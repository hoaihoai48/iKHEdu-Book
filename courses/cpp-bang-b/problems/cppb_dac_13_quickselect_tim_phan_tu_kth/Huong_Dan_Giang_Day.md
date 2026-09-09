# Hướng Dẫn Giảng Dạy: Thuật Toán QuickSelect Tìm K-th Element
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên và số nguyên K (1 <= K <= N). Hãy tìm giá trị của phần tử nhỏ thứ K bằng thuật toán QuickSelect.

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `6 3 3 2 1 5 6 4` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng có thứ tự: [1, 2, 3, 4, 5, 6]. Phần tử nhỏ thứ K = 3 là số 3. Kết quả in ra: 3.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `3` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng có thứ tự: [1, 2, 3, 4, 5, 6]. Phần tử nhỏ thứ K = 3 là số 3. Kết quả in ra: 3.

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

int partition(vector<long long> &a, int l, int r) {
int pivot_idx = l + rand() % (r - l + 1);
swap(a[pivot_idx], a[r]);
long long pivot = a[r];
int i = l;
for (int j = l; j < r; ++j) {
if (a[j] <= pivot) {
swap(a[i], a[j]);
i++;
}
}
swap(a[i], a[r]);
return i;
}

long long quickSelect(vector<long long> &a, int l, int r, int k) {
if (l == r) return a[l];
int p = partition(a, l, r);
int rank = p - l + 1;
if (rank == k) return a[p];
if (k < rank) return quickSelect(a, l, p - 1, k);
return quickSelect(a, p + 1, r, k - rank);
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
srand(42);
int n, k;
if (!(cin >> n >> k)) return 0;
vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];
cout << quickSelect(a, 0, n - 1, k) << "\n";
return 0;
}
```
