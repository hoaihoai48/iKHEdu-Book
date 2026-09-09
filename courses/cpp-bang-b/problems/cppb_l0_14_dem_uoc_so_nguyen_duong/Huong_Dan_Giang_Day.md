# Hướng Dẫn Giảng Dạy: Đếm Số Lượng Ước Số Nguyên Dương
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Thành thạo mẫu tích lũy dạng Đếm (`cnt++`) kết hợp cấu trúc `if` bên trong vòng lặp `for`.
- Nắm vững định nghĩa ước số: $i$ là ước của $N$ khi và chỉ khi $N \% i == 0$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Với $N \le 10^5$, cách tiếp cận tự nhiên và cơ bản nhất cho học sinh mới bắt đầu là duyệt toàn bộ các số $i$ từ $1$ đến $N$, kiểm tra nếu $N \% i == 0$ thì tăng biến đếm lên 1 đơn vị.
- Khởi tạo biến đếm ban đầu `cnt = 0`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Một số $i$ được gọi là ước của $N$ khi phép chia $N$ cho $i$ có phần dư bằng mấy
- Khi tìm thấy một ước số, ta làm gì với biến đếm

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Duyệt vòng lặp $i$ từ $1$ đến $N$.
- Nếu `n % i == 0`, thực hiện `cnt++`. Sau vòng lặp in ra `cnt`.

---

## 5. Mô Phỏng Từng Bước Trên Sample ($N = 12$)

| $i$ | Kiểm tra $12 \% i == 0$ | Thao tác biến đếm | Giá trị `cnt` |
|:---:|:---:|:---:|:---:|
| 1 | $12 \% 1 == 0$ (Đúng) | `cnt++` | 1 |
| 2 | $12 \% 2 == 0$ (Đúng) | `cnt++` | 2 |
| 3 | $12 \% 3 == 0$ (Đúng) | `cnt++` | 3 |
| 4 | $12 \% 4 == 0$ (Đúng) | `cnt++` | 4 |
| 5 | $12 \% 5 \ne 0$ (Sai) | Bỏ qua | 4 |
| 6 | $12 \% 6 == 0$ (Đúng) | `cnt++` | 5 |
| 7..11 | Không chia hết | Bỏ qua | 5 |
| 12 | $12 \% 12 == 0$ (Đúng) | `cnt++` | 6 |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$. Với $N \le 10^5$, số bước lặp là $10^5$, thời gian chạy $< 0.001\text{s}$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Bắt đầu vòng lặp từ $i = 0$ dẫn đến lỗi chia cho 0 (`Floating point exception / Runtime Error`).
- Quên khởi tạo `cnt = 0`.

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;

int cnt = 0;
for (int i = 1; i <= n; i++) {
if (n % i == 0) {
cnt++;
}
}

cout << cnt << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Tính tổng các ước số nguyên dương của $N$.
- Tối ưu thuật toán đếm ước trong $\mathcal{O}(\sqrt{N})$ khi học ở Chương Số học (Chương 04).
