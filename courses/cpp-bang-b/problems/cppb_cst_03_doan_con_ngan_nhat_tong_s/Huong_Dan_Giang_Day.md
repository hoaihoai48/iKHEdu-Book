# Hướng Dẫn Giảng Dạy: Đoạn Con Ngắn Nhất Có Tổng Đạt S
Chuyên đề: **Kỹ Thuật Cửa Sổ Trượt (Sliding Window)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho dãy số nguyên dương $A$ và số nguyên dương $S$. Tìm độ dài nhỏ nhất của một đoạn con liên tiếp có tổng các phần tử $\ge S$. Nếu không tồn tại đoạn nào, in `0`.
- **Kỹ thuật Cửa sổ trượt biến thiên (Variable-size Sliding Window):**
- Vì tất cả các phần tử $A_i$ đều là số nguyên dương ($A_i > 0$), mảng có tính chất đơn điệu: khi mở rộng cửa sổ sang phải thì tổng luôn tăng, khi thu hẹp cửa sổ bên trái thì tổng luôn giảm.
- Sử dụng 2 con trỏ $L = 0, R = 0$ và biến tích lũy `cur_sum = 0`:
1. Mở rộng biên phải $R$: Cộng `cur_sum += a[R]`.
2. Trong khi `cur_sum >= S`: Ta đã tìm thấy một đoạn hợp lệ có độ dài $R - L + 1$. Cập nhật `min_len = min(min_len, R - L + 1)`. Sau đó thử thu hẹp biên trái bằng cách trừ `cur_sum -= a[L]` và tăng `L++` để tìm đoạn ngắn hơn.
- Mỗi phần tử đi vào cửa sổ qua $R$ đúng 1 lần và ra khỏi cửa sổ qua $L$ tối đa 1 lần $\implies$ Tổng số thao tác con trỏ không quá $2N$. Độ phức tạp thời gian: $\mathcal{O}(N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử: $N = 6, S = 7$, mảng `a = [2, 3, 1, 2, 4, 3]`.

| Bước | Con trỏ $R$ | Thêm $a[R]$ | `cur_sum` | `cur_sum >= 7` | Thu hẹp con trỏ $L$ & Cập nhật `min_len` |
|---|---|---|---|---|---|
| 1 | $R=0$ | $+2$ | 2 | Chưa | $L=0$ |
| 2 | $R=1$ | $+3$ | 5 | Chưa | $L=0$ |
| 3 | $R=2$ | $+1$ | 6 | Chưa | $L=0$ |
| 4 | $R=3$ | $+2$ | 8 | $8 \ge 7$ | Đoạn $[2, 3, 1, 2]$ dài 4. `min_len = 4`. Trừ $a[0]=2 \implies cur = 6, L=1$. |
| 5 | $R=4$ | $+4$ | 10 | $10 \ge 7$ | Đoạn $[3, 1, 2, 4]$ dài 4. Trừ $a[1]=3 \implies cur=7, L=2$.<br>Lại có $7 \ge 7 \implies$ đoạn $[1, 2, 4]$ dài 3. `min_len = 3`. Trừ $a[2]=1 \implies cur=6, L=3$. |
| 6 | $R=5$ | $+3$ | 9 | $9 \ge 7$ | Đoạn $[2, 4, 3]$ dài 3. Trừ $a[3]=2 \implies cur=7, L=4$.<br>Lại có $7 \ge 7 \implies$ đoạn $[4, 3]$ dài 2! `min_len = 2`. Trừ $a[4]=4 \implies cur=3, L=5$. |

Kết quả: Đoạn ngắn nhất có độ dài `2` (chính là đoạn $[4, 3]$).

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Mảng có số âm hoặc số 0:** Thuật toán 2 con trỏ chỉ áp dụng được khi các phần tử đều dương ($A_i > 0$). Nếu có số âm, tính đơn điệu bị phá vỡ, phải dùng Mảng tiền tố + Binary Search / Deque.
- **Bẫy 2 — Không có đoạn nào thỏa mãn:** Khởi tạo `min_len = N + 1`. Nếu kết thúc vòng lặp mà `min_len > N` thì in `0`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
long long s;
if (!(cin >> n >> s)) return 0;

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

int l = 0;
long long cur_sum = 0;
int min_len = n + 1;

for (int r = 0; r < n; ++r) {
cur_sum += a[r];
while (cur_sum >= s) {
min_len = min(min_len, r - l + 1);
cur_sum -= a[l];
l++;
}
}

if (min_len > n) {
cout << 0 << "\n";
} else {
cout << min_len << "\n";
}

return 0;
}
```