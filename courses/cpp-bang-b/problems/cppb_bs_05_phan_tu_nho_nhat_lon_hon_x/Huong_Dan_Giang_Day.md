# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Nhỏ Nhất Lớn Hơn X
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên đã sắp xếp tăng dần. Với mỗi truy vấn X, hãy tìm phần tử nhỏ nhất trong mảng có giá trị nghiêm ngặt lớn hơn X. Nếu không có, in ra -1.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân:**
- Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
- Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 2 3 5 6 8 4 2 8` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - Với X = 4: phần tử nhỏ nhất > 4 là 5. - Với X = 2: phần tử nhỏ nhất > 2 là 3. - Với X = 8: không có phần tử nào > 8 ->... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `5 3 -1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - Với X = 4: phần tử nhỏ nhất > 4 là 5.

- Với X = 2: phần tử nhỏ nhất > 2 là 3.
- Với X = 8: không có phần tử nào > 8 -> in -1.

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

int n, q;
if (!(cin >> n >> q)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) {
cin >> a[i];
}

while (q--) {
long long x;
cin >> x;
auto it = upper_bound(a.begin(), a.end(), x);
if (it == a.end()) {
cout << -1 << "\n";
} else {
cout << *it << "\n";
}
}

return 0;
}
```
