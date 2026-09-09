# Hướng Dẫn Giảng Dạy: Đếm Số Tam Giác Có Thể Tạo Thành
Chuyên đề: **Kỹ Thuật Hai Con Trỏ (Two Pointers)**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho $N$ thanh gỗ có độ dài $A_1, A_2, \dots, A_N$. Đếm số bộ ba thanh gỗ có thể ghép thành một tam giác không suy biến.
- **Bất đẳng thức tam giác trên mảng đã sắp xếp:**
- Ba cạnh $(a, b, c)$ tạo thành tam giác khi: $a + b > c, a + c > b, b + c > a$.
- Nếu ta sắp xếp tăng dần $A_i \le A_j \le A_k$, ta luôn có $A_k + A_i > A_j$ và $A_k + A_j > A_i$.
- Điều kiện duy nhất cần kiểm tra là:
$$A_i + A_j > A_k$$

- **Thuật toán Hai con trỏ $\mathcal{O}(N^2)$:**
- Cố định cạnh lớn nhất $k$ chạy ngược từ $N - 1$ về $2$.
- Với mỗi $k$, đặt $L = 0$ và $R = k - 1$:
- Nếu $A_L + A_R > A_k$: Vì mảng tăng dần nên mọi phần tử từ $L$ đến $R - 1$ khi ghép với $A_R$ đều thỏa mãn $> A_k$.
- Do đó có đúng **$R - L$ tam giác hợp lệ**. Cộng `ans += (R - L)` và giảm `R--`.
- Nếu $A_L + A_R \le A_k$: Tổng quá nhỏ, tăng `L++`.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử: $N = 5$, các cạnh đã xếp `[2, 3, 4, 5, 6]`.

| Cố định $k$ | Cạnh lớn nhất $A_k$ | Hai con trỏ $(L, R)$ | $A_L + A_R > A_k$ | Số tam giác cộng dồn |
|---|---|---|---|---|
| $k=4$ | $A_4 = 6$ | $L=0, R=3 (2, 5)$ | $2 + 5 = 7 > 6$ | Cặp (3, 4, 5) với 5 $\implies$ cộng $3 - 0 = 3$. $R=2$. |
| — | $A_4 = 6$ | $L=0, R=2 (2, 4)$ | $2 + 4 = 6 \le 6$ | $L=1$. |
| — | $A_4 = 6$ | $L=1, R=2 (3, 4)$ | $3 + 4 = 7 > 6$ | Cộng $2 - 1 = 1$. $R=1 \implies$ dừng $k=4$. (Được 4 tam giác) |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy tam giác suy biến:** Điều kiện là $a + b > c$ (lớn hơn nghiêm ngặt), nếu $a + b == c$ ba điểm thẳng hàng, không tạo thành tam giác.
- **Biến đếm `ans`:** Phải dùng `long long ans = 0` vì số tam giác tối đa là $\binom{N}{3} \approx 1.6 \cdot 10^{11}$ khi $N = 10^4$.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n) || n < 3) { cout << 0 << "\n"; return 0; }

vector<long long> a(n);
for (int i = 0; i < n; ++i) cin >> a[i];

sort(a.begin(), a.end());

long long count = 0;
for (int k = n - 1; k >= 2; --k) {
int l = 0, r = k - 1;
while (l < r) {
if (a[l] + a[r] > a[k]) {
count += (r - l);
r--;
} else {
l++;
}
}
}

cout << count << "\n";
return 0;
}
```