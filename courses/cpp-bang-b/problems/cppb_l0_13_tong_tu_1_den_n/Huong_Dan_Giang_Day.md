# Hướng Dẫn Giảng Dạy: Bảng Nhân & Tính Tổng Từ 1 Đến N
Chuyên đề: **Chương 01 — Bài 02: Cấu Trúc Rẽ Nhánh & Cấu Trúc Vòng Lặp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Nắm vững cú pháp vòng lặp `for (khởi tạo; điều kiện; bước nhảy)`.
- Thực hành mẫu tích lũy (Accumulation pattern) cơ bản nhất: cộng dồn vào biến `sum`.
- Nhận biết nguy cơ tràn số khi $N = 10^6$ thì $S \approx \frac{10^6 \times 10^6}{2} = 5 \times 10^{11}$, vượt quá giới hạn `int`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Công thức Gauss: $S = \frac{N(N + 1)}{2}$.
- Với bài tập này, mục tiêu sư phạm là rèn luyện cho học sinh cách điều khiển vòng lặp `for` và biến tích lũy `sum = 0`.
- Khởi tạo `long long sum = 0;` là bắt buộc vì nếu để rác bộ nhớ thì kết quả sẽ sai lệch hoàn toàn.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Trước khi cộng, biến `sum` phải có giá trị ban đầu là bao nhiêu
- Vòng lặp bắt đầu từ số mấy và kết thúc ở số mấy
- Tại sao $N = 10^6$ lại cần `long long` cho biến `sum`

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $N$. Khởi tạo `long long sum = 0;`.
- Vòng lặp `for (int i = 1; i <= n; i++) sum += i;`.
- Xuất giá trị `sum`.

---

## 5. Mô Phỏng Từng Bước Trên Sample ($N = 5$)

| Bước lặp $i$ | Thao tác cộng dồn | Giá trị biến `sum` |
|:---:|:---:|:---:|
| Khởi tạo | — | `0` |
| $i = 1$ | `sum = 0 + 1` | `1` |
| $i = 2$ | `sum = 1 + 2` | `3` |
| $i = 3$ | `sum = 3 + 3` | `6` |
| $i = 4$ | `sum = 6 + 4` | `10` |
| $i = 5$ | `sum = 10 + 5` | `15` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(N)$ (với $N \le 10^6$, máy tính chạy trong khoảng $0.005\text{s}$, hoàn toàn dưới giới hạn $1.0\text{s}$).
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Khai báo `int sum = 0;` dẫn đến tràn số thành số âm khi $N = 10^6$.
- Quên khởi tạo `sum = 0`, để biến chứa giá trị rác ngẫu nhiên của bộ nhớ RAM.
- Điều kiện dừng viết `i < n` thay vì `i <= n` (bỏ sót số cuối cùng).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n;
if (!(cin >> n)) return 0;

long long sum = 0;
for (int i = 1; i <= n; i++) {
sum += i;
}

cout << sum << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Mở rộng tính tổng bình phương: $S = 1^2 + 2^2 + \dots + N^2$.
- Tính tổng các số lẻ trong đoạn từ $1$ đến $N$.
