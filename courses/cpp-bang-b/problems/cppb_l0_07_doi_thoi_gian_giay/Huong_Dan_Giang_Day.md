# Hướng Dẫn Giảng Dạy: Đổi Giây Sang Giờ Phút Giây
Chuyên đề: **Chương 01 — Bài 01: Biến, Kiểu Dữ Liệu, Toán Tử & Nhập Xuất An Toàn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra
- Vận dụng phối hợp nhiều lần phép chia nguyên và chia dư để đổi đơn vị đo lường.
- Xuất dữ liệu kèm các ký tự đặc biệt như dấu hai chấm `:`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học
- $1\text{ giờ} = 3600\text{ giây}$.
- Số giờ $h = T / 3600$.
- Phần giây dư chưa đủ 1 giờ là $R = T \% 3600$.
- Từ $R$ giây dư, số phút là $m = R / 60$.
- Số giây còn lại sau khi trừ phút là $s = R \% 60$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt
- Trong 1 giờ có bao nhiêu giây
- Khi tính xong số giờ, ta dùng phép toán nào để biết còn dư bao nhiêu giây

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán
- Đọc $T$ kiểu `long long` (do $T$ có thể lên tới $10^9$).
- Lần lượt tính $h, m, s$ và in theo định dạng `h:m:s`.

---

## 5. Mô Phỏng Từng Bước Trên Sample

| $T$ | $h = T / 3600$ | $R = T \% 3600$ | $m = R / 60$ | $s = R \% 60$ | Định dạng in |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `3665` | `1` | `65` | `1` | `5` | `1:1:5` |
| `125` | `0` | `125` | `2` | `5` | `0:2:5` |

---

## 6. Phân Tích Độ Phức Tạp
- Thời gian: $\mathcal{O}(1)$.
- Không gian: $\mathcal{O}(1)$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển
- Tính số phút bằng `t / 60` (sai vì chưa trừ đi số giờ đã quy đổi).
- Dùng kiểu `int` cho biến $T = 10^9$ (mặc dù $10^9$ vừa vặn `int`, nhưng việc dùng `long long` là thói quen an toàn).

---

## 8. Mã Nguồn Tham Chiếu
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

long long t;
if (!(cin >> t)) return 0;

long long h = t / 3600;
long long rem = t % 3600;
long long m = rem / 60;
long long s = rem % 60;

cout << h << ':' << m << ':' << s << '\n';
return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao
- In định dạng đồng hồ điện tử đủ 2 chữ số (ví dụ `01:01:05`) bằng cách thêm `setw(2)` và `setfill('0')`.
