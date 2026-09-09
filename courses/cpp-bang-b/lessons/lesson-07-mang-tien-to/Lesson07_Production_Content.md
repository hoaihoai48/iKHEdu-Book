# Bài 07: Mảng tiền tố & mảng hiệu


## 1. Khái niệm & bản chất của mảng tiền tố (Prefix Sum 1D)

**Mảng tiền tố (Prefix Sum)** là một kỹ thuật tiền xử lý dữ liệu mảng ban đầu thành một mảng cộng dồn tích lũy, cho phép tính toán tổng của bất kỳ đoạn con liên tiếp $[L \dots R]$ nào chỉ trong **$\mathcal{O}(1)$ thời gian**, thay vì phải duyệt vòng lặp $\mathcal{O}(N)$.

### 1.1. Công thức xây dựng mảng tiền tố
Cho mảng số nguyên $A$ gồm $N$ phần tử. Quy ước đánh số chỉ số từ $1$ đến $N$ (**1-based indexing**):

* Khởi tạo: $P_0 = 0$.
* Công thức truy hồi với $i$ từ $1$ đến $N$:
$$P_i = P_{i-1} + A_i \quad \Longleftrightarrow \quad P_i = \sum_{k=1}^{i} A_k$$

### 1.2. Công thức truy vấn tổng đoạn con trong $\mathcal{O}(1)$
Tổng các phần tử trong đoạn từ chỉ số $L$ đến chỉ số $R$ ($1 \le L \le R \le N$) được tính bằng hiệu của hai giá trị tiền tố:
$$\text{Sum}(L, R) = \sum_{k=L}^{R} A_k = P_R - P_{L-1}$$

### 1.3. Chứng minh toán học
Theo định nghĩa:
$$P_R = A_1 + A_2 + \cdots + A_{L-1} + A_L + \cdots + A_R$$
$$P_{L-1} = A_1 + A_2 + \cdots + A_{L-1}$$

Lấy hiệu hai vế:
$$P_R - P_{L-1} = (A_1 + \cdots + A_{L-1} + A_L + \cdots + A_R) - (A_1 + \cdots + A_{L-1}) = A_L + A_{L+1} + \cdots + A_R = \text{Sum}(L, R)$$

> **Bất biến toán học:** Phép trừ $P_R - P_{L-1}$ đã loại bỏ chính xác đoạn tiền tố thừa từ $1$ đến $L-1$, chỉ giữ lại trọn vẹn đoạn con $[L \dots R]$ cần tính.

#### Ví dụ minh họa 1: Xây dựng và truy vấn Prefix Sum 1D
Cho mảng $N = 6$ phần tử: $A = [3, 1, 4, 1, 5, 9]$ (1-based indexing).

| Chỉ số $i$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Mảng gốc $A[i]$** | — | $3$ | $1$ | $4$ | $1$ | $5$ | $9$ |
| **Tiền tố $P[i]$** | $\mathbf{0}$ | $\mathbf{3}$ | $\mathbf{4}$ | $\mathbf{8}$ | $\mathbf{9}$ | $\mathbf{14}$ | $\mathbf{23}$ |

*Quy tắc cộng dồn:* $P[0] = 0$, $P[i] = P[i-1] + A[i]$ (ví dụ: $P[3] = 4 + 4 = 8, P[6] = 14 + 9 = 23$).

* **Truy vấn 1:** Tính tổng đoạn từ $L = 2$ đến $R = 5$ (đoạn $[1, 4, 1, 5]$):
$$\text{Sum}(2, 5) = P[5] - P[2 - 1] = P[5] - P[1] = 14 - 3 = \mathbf{11}$$
(Kiểm tra trực tiếp: $1 + 4 + 1 + 5 = 11$ — Hoàn toàn chính xác trong $\mathcal{O}(1)$).

* **Truy vấn 2:** Tính tổng toàn bộ mảng từ $L = 1$ đến $R = 6$:
$$\text{Sum}(1, 6) = P[6] - P[0] = 23 - 0 = \mathbf{23}$$

## 2. Kỹ thuật mảng tiền tố hai chiều (Prefix Sum 2D)

### 2.1. Bản chất nguyên lý bao hàm - Loại trừ (inclusion-exclusion principle)
Trên ma trận 2 chiều kích thước $N \times M$, gọi $P[i][j]$ là tổng của tất cả các phần tử trong hình chữ nhật có góc trái trên tại $(1, 1)$ và góc phải dưới tại $(i, j)$:
$$P[i][j] = \sum_{r=1}^{i} \sum_{c=1}^{j} A[r][c]$$

### 2.2. Công thức xây dựng bảng tiền tố 2D trong $\mathcal{O}(N \times M)$
Tại mỗi ô $(i, j)$:
$$P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + A[i][j]$$
(Giải thích: Cộng vùng phía trên và vùng bên trái, trừ đi phần giao nhau bị cộng lặp $P[i-1][j-1]$, rồi cộng thêm giá trị ô hiện tại $A[i][j]$).

### 2.3. Công thức truy vấn tổng hình chữ nhật $(x_1, y_1) \to (x_2, y_2)$ trong $\mathcal{O}(1)$
$$\text{Sum}((x_1, y_1), (x_2, y_2)) = P[x_2][y_2] - P[x_1-1][y_2] - P[x_2][y_1-1] + P[x_1-1][y_1-1]$$

#### Ví dụ minh họa 2: Truy vấn hình chữ nhật trên ma trận $3 \times 3$
Cho ma trận $A$:
$$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} \quad \xrightarrow{\text{Xây dựng } P} \quad P = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 3 & 6 \\ 0 & 5 & 12 & 21 \\ 0 & 12 & 27 & 45 \end{bmatrix}$$

Cần tính tổng hình chữ nhật từ $(x_1=2, y_1=2)$ đến $(x_2=3, y_2=3)$ (vùng các ô $\begin{bmatrix} 5 & 6 \\ 8 & 9 \end{bmatrix}$):
$$\begin{aligned}
\text{Sum} &= P[3][3] - P[1][3] - P[3][1] + P[1][1] \\
&= 45 - 6 - 12 + 1 = \mathbf{28}
\end{aligned}$$
(Kiểm tra trực tiếp: $5 + 6 + 8 + 9 = 28$ — Tính toán trong đúng 4 phép toán $\mathcal{O}(1)$).

## 3. Kỹ thuật mảng hiệu (Difference Array 1D)

### 3.1. Bài toán đặt ra
Cho mảng ban đầu gồm $N$ phần tử (toàn số 0 hoặc có giá trị sẵn). Thực hiện $Q$ thao tác, mỗi thao tác yêu cầu: **Cộng thêm một giá trị $V$ vào tất cả các phần tử từ chỉ số $L$ đến $R$**. Sau $Q$ thao tác, in ra mảng kết quả cuối cùng.

* **Cách tiếp cận ngây thơ:** Với mỗi thao tác, dùng vòng lặp chạy từ $L$ đến $R$ để cộng. Tổng thời gian: $\mathcal{O}(Q \times N) \approx 10^5 \times 10^5 = 10^{10}$ phép tính $\implies$ **Time Limit Exceeded (TLE)**.
* **Tối ưu bằng Mảng hiệu:** Thực hiện mỗi thao tác cộng đoạn trong **$\mathcal{O}(1)$ thời gian**.

### 3.2. Cơ chế hoạt động của mảng hiệu
Xây dựng mảng hiệu $D$ thỏa mãn: $A_i = \sum_{k=1}^{i} D_k$ (Mảng ban đầu chính là mảng tiền tố của mảng hiệu).
Để cộng giá trị $V$ vào mọi phần tử trong đoạn $[L \dots R]$, ta chỉ cần thực hiện 2 thao tác điểm:

* **Tại điểm bắt đầu đoạn $L$:** $D[L] \mathrel{+}= V$
* **Tại điểm sau kết thúc đoạn $R + 1$:** $D[R + 1] \mathrel{-}= V$

### 3.3. Khôi phục mảng kết quả sau $Q$ thao tác
Sau khi hoàn thành tất cả $Q$ thao tác cập nhật $\mathcal{O}(1)$, ta khôi phục lại mảng kết quả $A$ bằng một lần chạy tiền tố duy nhất trong **$\mathcal{O}(N)$ thời gian**:
$$A_i = A_{i-1} + D_i \quad (i = 1 \dots N)$$

#### Ví dụ minh họa 3: Mảng hiệu trên dãy $N = 5$ phần tử
Ban đầu dãy toàn số 0: $A = [0, 0, 0, 0, 0]$, mảng hiệu $D = [0, 0, 0, 0, 0, 0, 0]$ (kích thước $N+2$).

1. **Thao tác 1:** Cộng $V = 3$ vào đoạn $[1 \dots 3] \implies D[1] += 3, D[4] -= 3$.
$$D = [0, \mathbf{+3}, 0, 0, \mathbf{-3}, 0, 0]$$

2. **Thao tác 2:** Cộng $V = 2$ vào đoạn $[2 \dots 5] \implies D[2] += 2, D[6] -= 2$.
$$D = [0, +3, \mathbf{+2}, 0, -3, 0, \mathbf{-2}]$$

**Bước khôi phục mảng kết quả $A$ bằng Prefix Sum trên $D$:**

* $A_1 = D_1 = 3$
* $A_2 = A_1 + D_2 = 3 + 2 = 5$
* $A_3 = A_2 + D_3 = 5 + 0 = 5$
* $A_4 = A_3 + D_4 = 5 + (-3) = 2$
* $A_5 = A_4 + D_5 = 2 + 0 = 2$

> **Kết quả cuối cùng:** $A = [3, 5, 5, 2, 2]$

## 4. Kỹ thuật mảng hiệu hai chiều (Difference Array 2D)

Để cộng thêm giá trị $V$ vào tất cả các ô trong hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$ trên ma trận $N \times M$, ta chỉ cần tác động lên **4 điểm góc** của mảng hiệu $2D$ trong $\mathcal{O}(1)$:

| Điểm Góc Tác Động | Tọa Độ Ô Mảng Hiệu | Thao Tác Cập Nhật $\mathcal{O}(1)$ |
|---|:---:|:---:|
| **Góc trên - trái** | $(x_1, y_1)$ | `D[x1][y1] += V` |
| **Góc trên - phải** | $(x_1, y_2 + 1)$ | `D[x1][y2 + 1] -= V` |
| **Góc dưới - trái** | $(x_2 + 1, y_1)$ | `D[x2 + 1][y1] -= V` |
| **Góc dưới - phải** | $(x_2 + 1, y_2 + 1)$ | `D[x2 + 1][y2 + 1] += V` |

Sau khi thực hiện xong $Q$ thao tác, khôi phục ma trận gốc bằng công thức Prefix Sum 2D trong $\mathcal{O}(N \times M)$.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive template)

### Mẫu 1: Prefix Sum 1D (truy vấn tổng đoạn)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, q;
if (!(cin >> n >> q)) return 0;

vector<long long> a(n + 1);

vector<long long> p(n + 1, 0);

// Bước 1: Đọc dữ liệu và xây dựng mảng tiền tố O(N)
for (int i = 1; i <= n; ++i) {
cin >> a[i];

p[i] = p[i - 1] + a[i];
}

// Bước 2: Trả lời từng truy vấn trong O(1)
while (q--) {
int l, r;
cin >> l >> r;

cout << p[r] - p[l - 1] << "\n";
}

return 0;
}
```

### Mẫu 2: Difference Array 1D (cập nhật đoạn)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, q;
if (!(cin >> n >> q)) return 0;

// Khởi tạo mảng hiệu kích thước n + 2 để an toàn khi truy cập r + 1
vector<long long> d(n + 2, 0);

// Bước 1: Tiếp nhận Q thao tác cập nhật O(1)
while (q--) {
int l, r;
long long v;
cin >> l >> r >> v;

d[l] += v;
d[r + 1] -= v;
}

// Bước 2: Khôi phục mảng kết quả bằng tiền tố O(N)
vector<long long> a(n + 1, 0);

for (int i = 1; i <= n; ++i) {
a[i] = a[i - 1] + d[i];
cout << a[i] << (i == n "" : " ");
}
cout << "\n";

return 0;
}
```

## 6. Các bẫy lỗi lập trình thường gặp

1. **Bẫy chỉ số 0-based vs 1-based:** Khi dùng chỉ số 0-based, truy vấn đoạn bắt đầu từ $L=0$ sẽ phải tính $P[R] - P[-1]$ dẫn đến lỗi truy cập vùng nhớ ngoài biên. **Khuyến nghị chuẩn:** Luôn chuyển toàn bộ mảng tiền tố và mảng hiệu sang **1-based indexing** với $P[0] = 0$.
2. **Bẫy tràn số nguyên 32-bit khi cộng dồn:** Mảng $N = 2 \cdot 10^5$ phần tử với $A_i = 10^9$ sẽ có tổng tiền tố lên tới $2 \cdot 10^{14}$, vượt ngưỡng $2 \cdot 10^9$ của `int`. Khai báo toàn bộ mảng $P$ và $D$ kiểu `long long`.
3. **Bẫy tràn biên $R + 1$ trong mảng hiệu:** Khi đoạn cập nhật có $R = N$, thao tác $D[R+1] -= V$ sẽ ghi vào vị trí $N + 1$. Bắt buộc phải cấp phát mảng hiệu có kích thước tối thiểu là `N + 2`.

## 7. Ranh giới áp dụng: Khi nào nên & không nên dùng

* **KHI NÀO ÁP DỤNG TỐI ƯU:**
* **Mảng tĩnh (Static Queries):** Toàn bộ dữ liệu mảng cố định, chỉ nhận các truy vấn tính tổng đoạn liên tiếp $\implies$ **Prefix Sum đạt $\mathcal{O}(1)$ tuyệt đối**.
* **Cập nhật Offline (Batch Updates):** Nhận toàn bộ $Q$ thao tác cộng đoạn $[L, R]$ trước, sau đó mới cần in kết quả một lần ở cuối $\implies$ **Difference Array đạt $\mathcal{O}(Q + N)$**.

* **KHI NÀO KHÔNG ÁP DỤNG ĐƯỢC (Bẫy Lỗi KỸ THUẬT):**
* **Cập nhật và truy vấn xen kẽ Online:** Nếu chương trình vừa yêu cầu cập nhật giá trị một phần tử/đoạn, vừa yêu cầu truy vấn tổng đoạn ngay lập tức lặp đi lặp lại $Q$ lần:
* Dùng Prefix Sum sẽ tốn $\mathcal{O}(N)$ để cập nhật lại mảng $P \implies$ Tổng thời gian $\mathcal{O}(Q \times N)$ (TLE).
* Dùng Difference Array sẽ tốn $\mathcal{O}(N)$ để khôi phục mỗi khi có truy vấn $\implies$ Tổng thời gian $\mathcal{O}(Q \times N)$ (TLE).
* **Giải pháp chuẩn thi đấu:** Khi có cập nhật và truy vấn xen kẽ liên tục, bắt buộc phải sử dụng các cấu trúc dữ liệu cây động như **Cây chỉ số nhị phân (Fenwick Tree)** hoặc **Cây phân đoạn (Segment Tree)** (thuộc Module 08).

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Nhận diện — Recognize):

Mảng tiền tố $P$ của mảng `A = [4, 1, 7, 3, 2]` (đánh số từ 1 đến 5) là dãy số nào sau đây

- **A.** `P = [0, 4, 5, 12, 15, 17]`

- **B.** **[Đáp án đúng]** `P = [0, 4, 5, 12, 15, 17]` với `P0 = 0, P1 = 4, P2 = 5, P3 = 12, P4 = 15, P5 = 17`.

- **C.** `P = [4, 5, 12, 15, 17, 0]`.

- **D.** `P = [17, 13, 12, 5, 2, 0]`.

> *Giải thích:* $P0 = 0, P1 = 4, P2 = 4+1=5, P3 = 5+7=12, P4 = 12+3=15, P5 = 15+2=17$.

#### Câu 2 (Dự đoán — Predict):

Cho mảng tiền tố `P = [0, 3, 8, 14, 20, 25]`. Tổng của đoạn từ vị trí `L = 2` đến `R = 4` được tính bằng biểu thức nào

- **A.** $P[4] - P[2] = 20 - 8 = 12$.

- **B.** **[Đáp án đúng]** $P[4] - P[1] = 20 - 3 = 17$.

- **C.** $P[4] + P[2] = 20 + 8 = 28$.

- **D.** $P[5] - P[2] = 25 - 8 = 17$.

> *Giải thích:* Công thức tính tổng đoạn $[L \dots R]$ là $P[R] - P[L-1]$. Với `L=2, R=4`, ta có $Sum = P[4] - P[2-1] = P[4] - P[1] = 20 - 3 = 17$.

#### Câu 3 (Bản chất — Explain):

Tại sao khi thao tác trên mảng hiệu $D$ để cộng giá trị $V$ vào đoạn $[L \dots R]$, ta lại phải thực hiện $D[R+1] mathrel-= V$

- **A.** Để giảm bớt giá trị của phần tử đứng ngay sau $R$.

- **B.** **[Đáp án đúng]** Để triệt tiêu lượng tăng $V$ khi lấy tổng tiền tố từ vị trí $R+1$ trở đi, đảm bảo các phần tử ngoài đoạn $[L \dots R]$ không bị tăng thêm giá trị.

- **C.** Để tránh tràn số nguyên khi tính toán.

- **D.** Vì trình biên dịch C++ yêu cầu các thao tác mảng phải đối xứng.

> *Giải thích:* Khi lấy tổng tiền tố, thao tác $+V$ tại $L$ sẽ lan truyền tới tất cả các vị trí từ `L to N`. Do đó ta phải đặt $-V$ tại $R+1$ để chặn sự lan truyền này từ vị trí $R+1$ trở đi.

#### Câu 4 (Chuyển giao — Transfer):

Nếu có $Q = 10^5$ thao tác cập nhật cộng đoạn trên mảng $N = 10^5$ phần tử, việc sử dụng Mảng hiệu giúp giảm độ phức tạp thời gian từ bao nhiêu xuống bao nhiêu

- **A.** Từ $\mathcal{O}(N \log N)$ xuống $\mathcal{O}(N)$.

- **B.** **[Đáp án đúng]** Từ $O(Q * N) ≈ 10^10$ phép tính xuống $O(Q + N) ≈ 2 \cdot 10^5$ phép tính.

- **C.** Từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N \log N)$.

- **D.** Từ $\mathcal{O}(1)$ xuống `O(Q)`.

> *Giải thích:* Mỗi thao tác cập nhật mất $\mathcal{O}(1)$ (tổng $Q$ thao tác mất `O(Q)`), bước khôi phục mảng mất $\mathcal{O}(N)$. Tổng thời gian là $\mathcal{O}(Q + N)$, chạy dưới `0.05` giây.

#### Câu 5 (Prefix Sum 2D — Geometry):

Trong công thức tính tổng hình chữ nhật $2D$: $Sum = P[x2][y2] - P[x1-1][y2] - P[x2][y1-1] + P[x1-1][y1-1]$, tại sao lại có dấu cộng $+ P[x1-1][y1-1]$ ở cuối

- **A.** Vì đây là công thức tính đường chéo hình chữ nhật.

- **B.** **[Đáp án đúng]** Vì vùng hình chữ nhật góc $(1, 1) to (x1-1, y1-1)$ đã bị trừ 2 lần ở hai số hạng phía trước, nên cần cộng bù lại 1 lần theo nguyên lý Bao hàm - Loại trừ.

- **C.** Vì ô $(x1-1, y1-1)$ mang giá trị âm.

- **D.** Vì góc trên bên trái luôn phải có trọng số gấp đôi.

> *Giải thích:* Cả hai vùng bị trừ là $P[x1-1][y2]$ và $P[x2][y1-1]$ đều cùng chứa vùng giao nhau $(1, 1) to (x1-1, y1-1)$. Việc trừ cả hai vùng đã trừ vùng giao 2 lần, bắt buộc phải cộng bù lại 1 lần.

#### Câu 6 (Mảng hiệu 2D — Technique):

Để cộng giá trị $V$ vào tất cả các ô trong hình chữ nhật `(x1, y1) to (x2, y2)` trên ma trận bằng mảng hiệu $2D$, cần cập nhật bao nhiêu ô và dấu như thế nào

- **A.** Cập nhật 2 ô: $+V$ tại `(x1, y1)` và $-V$ tại `(x2, y2)`.

- **B.** **[Đáp án đúng]** Cập nhật 4 ô: $+V$ tại `(x1, y1)` và $(x2+1, y2+1)$; $-V$ tại $(x1, y2+1)$ và $(x2+1, y1)$.

- **C.** Cập nhật tất cả các ô nằm trên biên của hình chữ nhật.

- **D.** Cập nhật 4 ô với dấu $+V$ ở tất cả các góc.

> *Giải thích:* Đây là công thức mảng hiệu 2 chiều chuẩn mực để khi lấy Prefix Sum 2D khôi phục ma trận, chỉ có các ô bên trong hình chữ nhật nhận giá trị $+V$.

#### Câu 7 (Đoạn con tổng bằng 0 — Logic):

Nếu tồn tại hai chỉ số `i < j` trong mảng tiền tố thỏa mãn $P[i] = P[j]$, ta có thể rút ra kết luận gì về mảng ban đầu

- **A.** Tất cả các phần tử từ $i$ đến $j$ đều bằng 0.

- **B.** **[Đáp án đúng]** Đoạn con liên tiếp từ vị trí $i+1$ đến $j$ có tổng đúng bằng 0 ($Sum(i+1, j) = P[j] - P[i] = 0$).

- **C.** Mảng ban đầu đối xứng qua tâm.

- **D.** Toàn bộ mảng có tổng bằng 0.

> *Giải thích:* $Sum(i+1, j) = P[j] - P[i]$. Nếu `P[j] = P[i]` thì hiệu này bằng 0, nghĩa là tổng các phần tử trong đoạn $[i+1 \dots j]$ bằng 0.

#### Câu 8 (Đồng dư tiền tố — Prefix Modulo):

Để đếm số lượng đoạn con có tổng chia hết cho $K$, ta tính mảng tiền tố lấy dư `M[i] = P[i] bmod K`. Đoạn con $[L \dots R]$ có tổng chia hết cho $K$ khi và chỉ khi điều kiện nào thỏa mãn

- **A.** $M[R] + M[L-1] = K$.

- **B.** **[Đáp án đúng]** $M[R] = M[L-1]$ (hai vị trí có cùng số dư khi chia cho $K$).

- **C.** $M[R] - M[L-1] = 1$.

- **D.** $M[R] * M[L-1] = 0$.

> *Giải thích:* $(P[R] - P[L-1]) ≡ 0 mod K iff P[R] ≡ P[L-1] mod K iff M[R] = M[L-1]$.

#### Câu 9 (Bẫy chỉ số mảng hiệu — Bug Traps):

Khi làm việc với mảng hiệu 1D cho dãy có $N$ phần tử, tại sao mảng $D$ bắt buộc phải được khai báo với kích thước tối thiểu là $N + 2$

- **A.** Để lưu trữ giá trị trung bình ở cuối mảng.

- **B.** **[Đáp án đúng]** Vì khi đoạn cập nhật kết thúc tại `R = N`, câu lệnh $D[R+1] mathrel-= V$ sẽ ghi vào vị trí $N + 1$; nếu mảng chỉ có kích thước $N+1$ sẽ gây lỗi tràn bộ nhớ (Out of Bounds).

- **C.** Vì mảng hiệu luôn cần 2 ô nhớ trống ở đầu và cuối để chạy đa luồng.

- **D.** Vì số lượng thao tác $Q$ có thể lớn hơn $N$.

> *Giải thích:* $R$ có thể đạt giá trị cực đại là $N$, khi đó $R+1 = N+1$. Với 1-based indexing, mảng cần các chỉ số từ $0 \dots N+1$, tức kích thước tối thiểu phải là $N+2$.

#### Câu 10 (Tràn số dữ liệu lớn — Data Types):

Cho bài toán gồm $Q = 10^5$ truy vấn tổng đoạn trên ma trận $N * M = 1000 * 1000$, mỗi phần tử $A[i][j] \le 10^9$. Bảng tiền tố `P[i][j]` có thể đạt giá trị tối đa là bao nhiêu và cần kiểu dữ liệu gì

- **A.** $10^9$, dùng kiểu `int`.

- **B.** $2 \times 10^9$, dùng kiểu `int`.

- **C.** **[Đáp án đúng]** $10^6 \cdot 10^9 = 10^15$, bắt buộc phải khai báo bảng $P$ bằng kiểu `long long`.

- **D.** $10^{18}$, bắt buộc dùng kiểu `__int128`.

> *Giải thích:* Tổng của toàn bộ $1000 1000 = 10^6$ ô, mỗi ô có giá trị $10^9$, là $10^15$. Giá trị này vượt xa giới hạn $2.14 10^9$ của kiểu `int` 32-bit, bắt buộc phải dùng `long long` 64-bit.

#### Câu 11 (Nén chiều ma trận — 2D Submatrix Compression):

Để tìm ma trận con hình chữ nhật có tổng lớn nhất trên ma trận $N \times M$, kỹ thuật tối ưu kết hợp Mảng tiền tố và Thuật toán Kadane giảm độ phức tạp từ $O(N^2 M^2)$ xuống bao nhiêu

- **A.** $\mathcal{O}(N \times M)$

- **B.** **[Đáp án đúng]** $O(N^2 * M)$ (Cố định 2 hàng `r1, r2`, dùng tiền tố cột nén thành mảng 1D rồi chạy Kadane).

- **C.** $O(N^3 * M^3)$

- **D.** $O((N + M) log(NM))$

> *Giải thích:* Cố định 2 hàng `r1, r2` mất $\mathcal{O}(N^2)$, tổng các cột giữa 2 hàng này được tính trong $\mathcal{O}(1)$ bằng tiền tố cột, sau đó chạy Kadane 1D mất `O(M) implies` Tổng thời gian $O(N^2 M)$.

#### Câu 12 (Cân bằng đa trạng thái — Multidimensional Balance):

Để tìm đoạn con dài nhất chứa số lượng 3 loại ký tự 'A', 'B', 'C' bằng nhau, ta cần lưu trữ và so khớp giá trị nào tại mỗi vị trí tiền tố $i$

- **A.** Tổng số lượng $cntA + cntB + cntC$.

- **B.** **[Đáp án đúng]** Cặp hiệu hai chiều $(cntA[i] - cntB[i], cntB[i] - cntC[i])$.

- **C.** Tích $cntA[i] * cntB[i] * cntC[i]$.

- **D.** Chỉ số `i bmod 3`.

> *Giải thích:* Ba đại lượng bằng nhau $X = Y = Z iff X - Y = 0$ và $Y - Z = 0$. Khi lấy hiệu giữa hai mốc $R$ và $L-1$, điều này tương đương với $(cntA - cntB)$ và $(cntB - cntC)$ tại $R$ và $L-1$ phải bằng nhau.

## Ma trận bài tập thực hành (P0 → P5)

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-PT-01` | **Truy Vấn Tổng Đoạn Con 1D** | `P0` | `N, Q <= 10^5` | Prefix sum cơ bản `P[R] - P[L-1]` |
| 02 | `CPPB-PT-02` | **Đếm Số Lượng Số Chẵn Trong Đoạn** | `P1` | `N, Q <= 10^5` | Tiền tố trên mảng điều kiện logic |
| 03 | `CPPB-PT-03` | **Tìm Vị Trí Cân Bằng Của Mảng** | `P1` | $N \le 2 \times 10^5$ | Tổng trái bằng tổng phải |
| 04 | `CPPB-PT-04` | **Đoạn Con Có Tổng Bằng 0** | `P2` | $N \le 10^5$ | Nhận diện `P[i] == P[j]` |
| 05 | `CPPB-PT-05` | **Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)** | `P2` | `N, Q <= 2 * 10^5` | Difference Array 1D cơ bản |
| 06 | `CPPB-PT-06` | **Trồng Cây Phủ Đoạn Tối Ưu** | `P3` | `N <= 10^5, Q <= 10^5` | Mảng hiệu kết hợp quét mảng |
| 07 | `CPPB-PT-07` | **Truy Vấn Tổng Hình Chữ Nhật 2D** | `P1` | `N, M <= 1000, Q <= 10^5` | Prefix sum 2D nguyên bản |
| 08 | `CPPB-PT-08` | **Tìm Hình Vuông `K * K` Có Tổng Lớn Nhất** | `P2` | `N, M <= 1000, K <= min(N,M)` | Quét cửa sổ 2D kết hợp Prefix 2D |
| 09 | `CPPB-PT-09` | **Cập Nhật Cộng Hình Chữ Nhật (Mảng Hiệu 2D)** | `P3` | `N, M <= 1000, Q <= 10^5` | Difference Array 2D (4 góc) |
| 10 | `CPPB-PT-10` | **Đoạn Con Có Tổng Chia Hết Cho K** | `P3` | `N <= 2 * 10^5, K <= 10^5` | Mảng tiền tố kết hợp đồng dư |
| 11 | `CPPB-PT-11` | **Mảng Tiền Tố XOR Đoạn Con** | `P3` | `N, Q <= 2 * 10^5` | Tính chất `A XOR A = 0` trên Prefix XOR |
| 12 | `CPPB-PT-12` | **Đoạn Con Cân Bằng Số Lượng 0 và 1** | `P4` | $N \le 2 \times 10^5$ | Biến đổi `0 to -1` đưa về bài toán tổng 0 |
| 13 | `CPPB-PT-13` | **Truy Vấn Ma Trận Đa Vùng Cực Đại** | `P4` | `N, M <= 1500, Q <= 10^5` | Tối ưu hóa bộ nhớ và truy vấn 2D |
| 14 | `CPPB-PT-14` | **Phân Phối Tài Nguyên Không Gian Tuyến Tính** | `P5` | `N, Q <= 2 * 10^5` | Mảng hiệu 2 tầng (Arithmetic Progression Update) |
| 15 | `CPPB-PT-15` | **Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix)** | `P4` | `N, M <= 400` | Nén 2D về 1D + Thuật toán Kadane kết hợp Prefix Sum |
| 16 | `CPPB-PT-16` | **Cân Bằng Tiền Tố Đa Chiều** | `P5` | $N \le 10^5$ | Cân bằng 3 trạng thái đồng thời |
