# Hướng Dẫn Giảng Dạy: Mua Vở Có Khuyến Mãi
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Áp dụng tư duy gom nhóm số học (Block/Group division) bằng phép chia `/` và chia dư `%`.
- Nhận thức về việc sử dụng `long long` khi giá trị tiền bạc đạt tới $10^{15}$.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- Mỗi khối $6$ quyển (mua $5$ tặng $1$) chỉ cần trả tiền $5$ quyển.
- Số nhóm $6$ quyển đầy đủ là $g = N / 6$. Số quyển lẻ còn lại là $r = N \% 6$.
- Trong phần lẻ $r$ quyển, số quyển phải trả tiền là $\min(r, 5)$ (nếu $r = 5$, ta mua 5 quyển là đủ).
- Tổng số quyển cần trả tiền: $\text{to\_buy} = g \times 5 + \min(r, 5)$.
- Tổng tiền: $\text{total} = \text{to\_buy} \times P$. Với $N \le 10^9, P \le 10^6$, tổng tiền có thể lên tới $10^{15}$, bắt buộc dùng `long long`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Cứ mỗi lần nhận được 6 quyển trên tay, thực chất ta chỉ phải bỏ tiền mua bao nhiêu quyển
- Phép toán nào giúp tìm số lượng nhóm 6 quyển hoàn chỉnh

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Phân tích số quyển thành các nhóm 6 và phần dư.
- Tính trực tiếp trong $\mathcal{O}(1)$ bằng công thức số học, không cần dùng vòng lặp.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $N$ | $P$ | Nhóm $g = N / 6$ | Dư $r = N \% 6$ | Số quyển mua: $g \times 5 + \min(r, 5)$ | Tổng tiền thanh toán |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `5000` | `2` | `1` | `2 * 5 + 1 = 11` | `11 * 5000 = 55000` |
| `5` | `6000` | `0` | `5` | `0 * 5 + 5 = 5` | `5 * 6000 = 30000` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Dùng `int` cho biến kết quả tiền, dẫn đến tràn số nghiêm trọng khi nhân với $P = 10^6$.
- Chia nhầm cho 5 thay vì chia cho 6 (vì mỗi nhóm ưu đãi trọn gói gồm $5 + 1 = 6$ quyển).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long n, p;
if (!(cin >> n >> p)) return 0;

long long groups = n / 6;
long long rem = n % 6;

long long to_buy = groups * 5 + min(rem, 5LL);
long long total_cost = to_buy * p;

cout << total_cost << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- Bài toán khuyến mãi mua $K$ tặng $M$ tổng quát.
