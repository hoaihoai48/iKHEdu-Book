# Hướng Dẫn Giảng Dạy: Lũy Thừa Ma Trận Chia Để Trị 2x2
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho ma trận vuông 2x2 gồm các hệ số a, b, c, d và số nguyên N. Hãy tính A^N mod (10^9 + 7).

- **Phương pháp tiếp cận — Chia để trị:**
- Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
- Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `1 1 1 0 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | A^2 = [[1, 1], [1, 0]] * [[1, 1], [1, 0]] = [[2, 1], [1, 1]].... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 1 1 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* A^2 = [[1, 1], [1, 0]] * [[1, 1], [1, 0]] = [[2, 1], [1, 1]].

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

struct Matrix {
long long mat[2][2];
};

Matrix multiply(const Matrix &A, const Matrix &B, long long m) {
Matrix C;
for (int i = 0; i < 2; ++i) {
for (int j = 0; j < 2; ++j) {
C.mat[i][j] = 0;
for (int k = 0; k < 2; ++k) {
C.mat[i][j] = (C.mat[i][j] + (A.mat[i][k] % m) * (B.mat[k][j] % m)) % m;
}
}
}
return C;
}

Matrix powerMatrix(Matrix A, long long n, long long m) {
Matrix res = {{{1 % m, 0}, {0, 1 % m}}};
while (n > 0) {
if (n & 1) res = multiply(res, A, m);
A = multiply(A, A, m);
n >>= 1;
}
return res;
}

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);
Matrix A;
if (!(cin >> A.mat[0][0] >> A.mat[0][1] >> A.mat[1][0] >> A.mat[1][1])) return 0;
long long n, m;
if (!(cin >> n >> m)) return 0;
Matrix ans = powerMatrix(A, n, m);
cout << ans.mat[0][0] << " " << ans.mat[0][1] << "\n";
cout << ans.mat[1][0] << " " << ans.mat[1][1] << "\n";
return 0;
}
```
