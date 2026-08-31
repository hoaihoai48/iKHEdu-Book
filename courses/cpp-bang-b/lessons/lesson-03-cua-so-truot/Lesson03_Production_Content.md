# KỸ THUẬT CỬA SỔ TRƯỢT
## Tối Ưu Hóa Đoạn Con Tuyến Tính O(N) Trong C++

---

## 1. Khái Niệm & Bản Chất Của Kỹ Thuật Cửa Sổ Trượt

**Kỹ thuật Cửa sổ trượt (Sliding Window Technique)** là phương pháp tối ưu hóa trên cấu trúc dữ liệu mảng hoặc chuỗi nhằm giải quyết các bài toán liên quan đến **đoạn con liên tiếp (Contiguous Subarray / Substring)**.

Thay vì phải tính toán lại từ đầu hàm mục tiêu trên từng đoạn con $[i \dots j]$ với độ phức tạp $\mathcal{O}(K)$ hoặc $\mathcal{O}(N)$, kỹ thuật này duy trì một "khung cửa sổ" $[L \dots R]$ và cập nhật trạng thái mục tiêu trong **$\mathcal{O}(1)$ thời gian** bằng cách:
$$\text{State}_{\text{mới}} = \text{State}_{\text{cũ}} + \text{Phần tử nạp vào } A_R - \text{Phần tử nhả ra } A_{L-1}$$

---

## 2. Cơ Chế Chuyển Dịch & Phân Tích Độ Phức Tạp $\mathcal{O}(N)$

### 2.1. Cơ chế hai con trỏ cùng chiều ($L \longrightarrow R$)
* **Con trỏ phải $R$ (Right / Lead pointer):** Mở rộng biên phải để nạp thêm phần tử $A_R$ vào cửa sổ nhằm thỏa mãn điều kiện bài toán.
* **Con trỏ trái $L$ (Left / Trail pointer):** Co hẹp biên trái để loại bỏ phần tử $A_L$ ra khỏi cửa sổ nhằm tối ưu hóa kích thước hoặc khôi phục tính hợp lệ của cửa sổ.

### 2.2. Phân tích chi phí khấu hao (Amortized Complexity Analysis)
Mặc dù thuật toán thường được cài đặt dưới dạng một vòng lặp `while` lồng bên trong một vòng lặp `for`:
* Con trỏ $R$ duyệt từ $0$ đến $N - 1$ (thực hiện đúng $N$ bước tăng).
* Con trỏ $L$ duyệt từ $0$ đến $N$ (thực hiện tối đa $N$ bước tăng).
* **Mỗi phần tử trong mảng chỉ đi vào cửa sổ đúng 1 lần và ra khỏi cửa sổ tối đa 1 lần**.

Do đó, tổng số thao tác thêm/bớt phần tử trong toàn bộ chương trình không bao giờ vượt quá $2N$. Độ phức tạp thời gian đạt **$\mathcal{O}(N)$ tuyến tính tuyệt đối**.

---

## 3. Phân Loại Hai Dạng Cửa Sổ Trượt Chuẩn Mực

### 3.1. Dạng 1: Cửa Sổ Cố Định Độ Dài $K$ (Fixed-Size Window)
Áp dụng cho các bài toán yêu cầu khảo sát mọi đoạn con liên tiếp có độ dài đúng bằng $K$.

* **Công thức trượt $\mathcal{O}(1)$:**
  * Khởi tạo: $\text{Current\_Sum} = \sum_{i=0}^{K-1} A_i$.
  * Trượt từ vị trí $i = K$ đến $N - 1$:
    $$\text{Current\_Sum} \leftarrow \text{Current\_Sum} + A_i - A_{i-K}$$
  * Cập nhật giá trị cực trị: $\text{Ans} = \max(\text{Ans}, \text{Current\_Sum})$.

#### Ví Dụ Minh Họa 1: Tìm tổng đoạn con $K = 3$ lớn nhất trên dãy $A = [2, 1, 5, 1, 3, 2]$

| Chỉ số ($i$) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Giá trị $A_i$** | $2$ | $1$ | $5$ | $1$ | $3$ | $2$ |

**Bảng mô phỏng quá trình trượt cửa sổ:**

| Vị Trí $i$ | Đoạn Con Đang Xét | Phần Tử Thêm Mới ($A_i$) | Phần Tử Bị Loại Bỏ ($A_{i-K}$) | Tổng Cửa Sổ Mới ($\text{Sum}$) | $\text{Max\_Sum}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo ($i=2$)** | $[2, 1, 5]$ (chỉ số $0..2$) | — | — | $2 + 1 + 5 = \mathbf{8}$ | $\mathbf{8}$ |
| **$i = 3$** | $[1, 5, 1]$ (chỉ số $1..3$) | $+ A_3 (1)$ | $- A_0 (2)$ | $8 + 1 - 2 = \mathbf{7}$ | $8$ |
| **$i = 4$** | $[5, 1, 3]$ (chỉ số $2..4$) | $+ A_4 (3)$ | $- A_1 (1)$ | $7 + 3 - 1 = \mathbf{9}$ | $\mathbf{9}$ |
| **$i = 5$** | $[1, 3, 2]$ (chỉ số $3..5$) | $+ A_5 (2)$ | $- A_2 (5)$ | $9 + 2 - 5 = \mathbf{6}$ | $9$ |

$$\implies \text{Kết quả: Tổng lớn nhất của đoạn dài 3 là } \mathbf{9} \text{ (đoạn } [5, 1, 3]\text{), trượt trong đúng } \mathcal{O}(1) \text{ mỗi bước!}$$

---

### 3.2. Dạng 2: Cửa Sổ Biến Thiên (Variable-Size Window)
Áp dụng cho các bài toán tìm đoạn con liên tiếp dài nhất/ngắn nhất hoặc đếm số lượng đoạn con thỏa mãn điều kiện $f([L \dots R])$.

| Dạng Bài Toán | Chiến Lược Điều Khiển Con Trỏ | Công Thức Cập Nhật Kết Quả |
|---|---|---|
| **Đoạn con ngắn nhất có tổng $\ge S$** | Mở $R$ cho đến khi $\text{Sum} \ge S$, sau đó co $L$ tối đa để tìm $\min(R - L + 1)$ | $\text{Min\_Len} = \min(\text{Min\_Len}, R - L + 1)$ |
| **Đoạn con dài nhất có tổng $\le S$** | Mở $R$, nếu $\text{Sum} > S$ thì co $L$ cho đến khi $\text{Sum} \le S$ | $\text{Max\_Len} = \max(\text{Max\_Len}, R - L + 1)$ |
| **Đếm số lượng đoạn con có tổng $\le S$** | Mở $R$, co $L$ cho đến khi $\text{Sum} \le S$. Mọi đoạn con kết thúc tại $R$ bắt đầu từ $[L \dots R]$ đều thỏa mãn | $\text{Total} \leftarrow \text{Total} + (R - L + 1)$ |

#### Ví Dụ Minh Họa 2: Tìm đoạn con ngắn nhất có tổng $\ge S = 7$ trên $A = [2, 3, 1, 2, 4, 3]$

| Bước ($R$) | Nạp $A_R$ | Tổng Cửa Sổ | Điều Kiện $\ge 7$ | Thao Tác Co $L$ | Độ Dài Cửa Sổ | $\text{Min\_Len}$ |
|:---:|:---:|:---:|:---:|---|:---:|:---:|
| $R = 0$ | $A_0 = 2$ | $2$ | Chưa đủ | — | — | $\infty$ |
| $R = 1$ | $A_1 = 3$ | $5$ | Chưa đủ | — | — | $\infty$ |
| $R = 2$ | $A_2 = 1$ | $6$ | Chưa đủ | — | — | $\infty$ |
| $R = 3$ | $A_3 = 2$ | $8$ | **Thỏa mãn ($\ge 7$)** | $L=0 \to 1$ (bỏ $A_0=2$, tổng còn $6 < 7$) | Đoạn $[3, 1, 2]$ dài $3$ | **$3$** |
| $R = 4$ | $A_4 = 4$ | $10$ | **Thỏa mãn ($\ge 7$)** | $L=1 \to 2$ (bỏ $A_1=3$, tổng còn $7 \ge 7$ dài $3$) $\to L=3$ (bỏ $A_2=1$, tổng còn $6 < 7$) | Đoạn $[2, 4]$ dài $2$ | **$2$** |
| $R = 5$ | $A_5 = 3$ | $9$ | **Thỏa mãn ($\ge 7$)** | $L=3 \to 4$ (bỏ $A_3=2$, tổng còn $7 \ge 7$ dài $2$) $\to L=5$ (bỏ $A_4=4$, tổng còn $3 < 7$) | Đoạn $[4, 3]$ dài $2$ | **$2$** |

$$\implies \text{Kết quả: Độ dài ngắn nhất là } \mathbf{2} \text{ (đoạn } [2, 4] \text{ hoặc } [4, 3]\text{)!}$$

---

## 4. Điều Kiện Áp Dụng & Giới Hạn Thất Bại Khi Mảng Có Số Âm

### 4.1. Điều kiện tiên quyết: Tính đơn điệu của hàm trạng thái
Cửa sổ trượt biến thiên **bắt buộc yêu cầu hàm mục tiêu phải có tính đơn điệu**:
* Khi mở rộng $R$ ($R \to R + 1$): Trạng thái phải tăng dần (hoặc không giảm).
* Khi co hẹp $L$ ($L \to L + 1$): Trạng thái phải giảm dần (hoặc không tăng).

Đối với bài toán tổng đoạn con, điều này tương đương với điều kiện: **Tất cả các phần tử trong mảng phải là số không âm ($A_i \ge 0$)**.

### 4.2. Giới hạn: Vì sao Sliding Window thất bại khi có số âm?
Xét mảng $A = [2, -5, 10, -2, 8]$ với mục tiêu tìm đoạn con ngắn nhất có tổng $\ge 8$.
* Khi $R$ nạp thêm số âm $-5$, tổng cửa sổ bị giảm.
* Khi $L$ dịch qua số âm $-5$, tổng cửa sổ lại tăng lên.
* Tính chất đơn điệu bị phá vỡ $\implies$ Con trỏ $L$ không thể đưa ra quyết định di chuyển một chiều chắc chắn $\implies$ Bỏ sót nghiệm tối ưu.
* **Giải pháp chuẩn:** Chuyển sang sử dụng **Mảng cộng dồn (Prefix Sum)** kết hợp **Hàng đợi hai đầu (Deque) / Cây chỉ số Fenwick / Segment Tree**.

---

## 5. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Template)

### Mẫu: Đoạn con liên tiếp ngắn nhất có tổng $\ge S$ ($A_i \ge 0$)

```cpp
# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int l = 0;
    long long current_sum = 0;
    int min_len = n + 1; // Khởi tạo vô cực

    // Duyệt con trỏ R tuyến tính O(N)
    for (int r = 0; r < n; ++r) {
        current_sum += a[r]; // Nạp a[r] vào cửa sổ

        // Co hẹp con trỏ L khi cửa sổ đã thỏa mãn điều kiện
        while (current_sum >= s) {
            min_len = min(min_len, r - l + 1); // Cập nhật độ dài nhỏ nhất
            current_sum -= a[l];               // Nhả a[l] ra khỏi cửa sổ
            ++l;                               // Dịch chuyển biên trái
        }
    }

    if (min_len > n) {
        cout << 0 << "\n"; // Không tồn tại đoạn thỏa mãn
    } else {
        cout << min_len << "\n";
    }

    return 0;
}
```

---

## 6. Kỹ Thuật Cửa Sổ Trượt Với Bảng Đếm Ký Tự / Trạng Thái

Khi xử lý bài toán chuỗi ký tự (như Đoạn con dài nhất chứa tối đa $K$ ký tự khác nhau):
* Sử dụng mảng đếm tần suất `int count[256]` hoặc `int count[26]` và biến `distinct_count` lưu số ký tự khác nhau hiện có trong cửa sổ.
* Khi nạp ký tự $S[R]$: nếu `count[S[R]] == 0`, tăng `distinct_count`. Tăng `count[S[R]]++`.
* Khi `distinct_count > K`: co con trỏ $L$, giảm `count[S[L]]--`; nếu `count[S[L]] == 0`, giảm `distinct_count`. Tăng `++L`.

---

## 7. Các Bẫy Lỗi Thường Gặp (Bug Traps)

1. **Bẫy tràn số nguyên khi tính tổng cửa sổ:** Tổng đoạn con của mảng $N = 10^5$ phần tử với $A_i = 10^9$ có thể lên tới $10^{14}$. Khai báo biến `current_sum` kiểu `long long`.
2. **Bẫy điều kiện khởi tạo kết quả cực trị:** Khi tìm $\min$, khởi tạo `ans = n + 1` (hoặc $\infty$); khi không tìm thấy nghiệm phải in ra `0` hoặc `-1` theo đúng quy cách đề bài.
3. **Bẫy chỉ số âm khi trượt cửa sổ cố định:** Luôn đảm bảo chỉ thực hiện phép trừ `a[i - k]` khi chỉ số $i \ge K$.

---

# CÂU HỎI TRẮC NGHIỆM ĐO LƯỜNG TƯ DUY (CONCEPT QUIZ)

#### Câu 1 (Nhận diện — Recognize):
Kỹ thuật Cửa sổ trượt biến thiên (mở `R`, co `L`) áp dụng an toàn nhất trên tập dữ liệu nào sau đây?
* A. Mảng số nguyên có cả số dương lớn và số âm nhỏ.
* B. **(Đáp án đúng)** Mảng các số nguyên không âm (`A_i >= 0`).
* C. Mảng các chuỗi ký tự ngẫu nhiên đã được đảo ngược.
* D. Mảng 2 chiều kích thước `N * N`.
> *Giải thích:* Tính không âm đảm bảo rằng khi mở rộng `R` thì tổng luôn tăng hoặc giữ nguyên, và khi co `L` thì tổng luôn giảm hoặc giữ nguyên (tính chất đơn điệu).

---

#### Câu 2 (Dự đoán — Predict):
Cho mảng `A = [1, 4, 2, 10, 2, 3, 1, 0, 20]` và cửa sổ cố định kích thước `K = 4`. Tổng của cửa sổ đầu tiên `[1, 4, 2, 10]` là `17`. Khi trượt cửa sổ sang phải để xét đoạn `[4, 2, 10, 2]`, tổng mới được tính nhanh nhất bằng phép toán nào?
* A. Cộng lại từ đầu: `4 + 2 + 10 + 2 = 18`.
* B. **(Đáp án đúng)** Lấy tổng cũ trừ phần tử rời đi và cộng phần tử mới: `17 - 1 + 2 = 18`.
* C. Nhân đôi tổng cũ rồi chia cho 4.
* D. Lấy `17` cộng thêm `4`.
> *Giải thích:* Quy tắc trượt cửa sổ cố định: `sum = sum - A[i-K] + A[i]` chỉ mất $\mathcal{O}(1)$ thời gian.

---

#### Câu 3 (Bản chất — Explain):
Mặc dù có vòng lặp `while` lồng bên trong vòng lặp `for`, tại sao thuật toán Cửa sổ trượt trên mảng `N` phần tử vẫn đạt độ phức tạp thời gian $\mathcal{O}(N)$?
* A. Vì vòng lặp `while` chỉ chạy đúng 1 lần duy nhất trong toàn bộ chương trình.
* B. Vì trình biên dịch C++ tự động tối ưu hóa vòng lặp `while` thành câu lệnh `if`.
* C. **(Đáp án đúng)** Vì con trỏ `L` chỉ dịch chuyển sang phải và mỗi phần tử chỉ bị loại bỏ khỏi cửa sổ tối đa đúng 1 lần.
* D. Vì số phép tính của vòng `while` luôn bị giới hạn bởi hằng số 10.
> *Giải thích:* `R` duyệt từ `0 to N-1` (`N` bước) và `L` duyệt từ `0 to N` (tối đa `N` bước). Tổng số bước di chuyển của cả 2 con trỏ không bao giờ vượt quá $2N$.

---

#### Câu 4 (Chuyển giao — Transfer):
Nếu đề bài yêu cầu tìm đoạn con ngắn nhất có tổng `>= S` nhưng trong mảng có xuất hiện các số âm, tại sao ta **không được dùng** kỹ thuật Cửa sổ trượt đơn thuần?
* A. Vì số âm làm tràn bộ nhớ của mảng.
* B. **(Đáp án đúng)** Vì số âm phá vỡ tính chất đơn điệu của tổng, khiến việc co con trỏ `L` có thể làm tăng tổng và bỏ sót nghiệm tối ưu.
* C. Vì hàm `min()` trong C++ không so sánh được số âm.
* D. Vì vòng lặp `for` sẽ bị lặp vô tận.
> *Giải thích:* Khi có số âm, việc mở rộng `R` chưa chắc làm tăng tổng và việc co `L` chưa chắc làm giảm tổng, khiến 2 con trỏ không thể đưa ra quyết định di chuyển một chiều chắc chắn.

---

#### Câu 5 (Chiến lược điều khiển — Control Flow):
Trong bài toán tìm **đoạn con dài nhất có tổng `<= S`** (`A_i >= 0`), vòng lặp `while` co con trỏ `L` được kích hoạt khi nào?
* A. Khi tổng cửa sổ `current_sum <= S`.
* B. **(Đáp án đúng)** Khi tổng cửa sổ `current_sum > S` (cửa sổ vi phạm điều kiện, cần co `L` cho đến khi tổng `<= S` trở lại).
* C. Khi con trỏ `R` chạm đến cuối mảng.
* D. Sau mỗi lần tăng con trỏ `R`.
> *Giải thích:* Với bài toán tìm `max` độ dài thỏa mãn `sum <= S`, ta chỉ co `L` khi tổng đang bị vượt quá ngưỡng cho phép (`> S`) để đưa cửa sổ về trạng thái hợp lệ.

---

#### Câu 6 (Đếm tổ hợp đoạn con — Combinatorial Counting):
Trong bài toán **Đếm số lượng đoạn con liên tiếp có tổng `<= S`** (`A_i >= 0`), sau khi co `L` để đảm bảo tổng đoạn `[L ... R] <= S`, số lượng đoạn con hợp lệ kết thúc tại `R` được tính bằng công thức nào?
* A. `1`
* B. `R - L`
* C. **(Đáp án đúng)** $R - L + 1$ (gồm các đoạn `[R ... R], [R-1 ... R], ..., [L ... R]`).
* D. `((R - L + 1) * (R - L + 2))/(2)`
> *Giải thích:* Vì đoạn dài nhất `[L ... R]` có tổng `<= S` và mảng không âm, nên mọi đoạn con kết thúc tại `R` bắt đầu từ bất kỳ vị trí nào từ `L` đến `R` đều có tổng `<= S`. Có đúng $R - L + 1$ đoạn như vậy.

---

#### Câu 7 (Cửa sổ chuỗi ký tự — Frequency Map):
Để tìm **đoạn con dài nhất chứa tối đa $K$ ký tự phân biệt** trên chuỗi chỉ gồm chữ cái thường tiếng Anh, ta nên quản lý trạng thái cửa sổ như thế nào tối ưu nhất?
* A. Quét lại toàn bộ cửa sổ để đếm số ký tự khác nhau trong mỗi bước ($\mathcal{O}(K)$).
* B. **(Đáp án đúng)** Sử dụng một mảng đếm tần suất `int count[26] = {0}` và một biến đếm `distinct_chars` ($\mathcal{O}(1)$ thời gian cho mỗi thao tác nạp/nhả).
* C. Khởi tạo mảng mới tại mỗi bước lặp.
* D. Sắp xếp lại chuỗi ký tự trước khi chạy.
> *Giải thích:* Bảng đếm tần suất kích thước cố định `26` cho phép cập nhật số lượng ký tự phân biệt trong $\mathcal{O}(1)$, đảm bảo toàn bộ thuật toán chạy trong $\mathcal{O}(N)$ thời gian và $\mathcal{O}(1)$ bộ nhớ phụ trợ.

---

#### Câu 8 (Cửa sổ bao phủ tối thiểu — Minimum Window):
Trong bài toán tìm **đoạn con ngắn nhất chứa đầy đủ tất cả các ký tự của một tập hợp `T`**, điều kiện để bắt đầu co con trỏ `L` là gì?
* A. Khi độ dài cửa sổ đạt tới độ dài của `T`.
* B. **(Đáp án đúng)** Khi cửa sổ hiện tại `[L ... R]` đã chứa đủ tần suất của mọi ký tự trong tập `T`.
* C. Khi con trỏ `R` duyệt đến cuối chuỗi.
* D. Khi gặp một ký tự không thuộc tập `T`.
> *Giải thích:* Khi cửa sổ đã bao phủ đủ các ký tự yêu cầu (đạt trạng thái hợp lệ), ta tiến hành co `L` để tìm kiếm độ dài ngắn nhất có thể mà vẫn duy trì tính bao phủ đầy đủ.

---

#### Câu 9 (Xử lý giới hạn dữ liệu lớn — Large Constraints):
Một bài toán yêu cầu tìm đoạn con có tổng lớn nhất trong mảng $N = 10^5$ phần tử với $A_i \le 10^9$. Biến tính tổng cửa sổ `current_sum` có thể đạt giá trị tối đa là bao nhiêu và cần kiểu dữ liệu gì?
* A. $10^9$, dùng kiểu `int`.
* B. $2 \times 10^9$, dùng kiểu `int`.
* C. **(Đáp án đúng)** $10^{14}$, bắt buộc dùng kiểu `long long` (64-bit).
* D. $10^{18}$, bắt buộc dùng kiểu `__int128`.
> Giải thích: Tổng của $10^5$ phần tử có giá trị $10^9$ là `10^5  10^9 = 10^14`, vượt xa giới hạn khoảng `2.14  10^9` của kiểu `int` 32-bit.

---

#### Câu 10 (Kỹ thuật hiệu đếm đoạn con — Interval Counting Trick):
Để đếm số lượng đoạn con liên tiếp có tổng nằm trong khoảng `[A, B]` (tức `A <= sum <= B`) trên mảng số nguyên dương, kỹ thuật chuẩn mực là gì?
* A. Chạy 2 vòng lặp lồng nhau duyệt mọi đoạn con.
* B. **(Đáp án đúng)** Gọi `F(X)` là số lượng đoạn con có tổng `<= X`. Kết quả cần tìm chính là `F(B) - F(A - 1)`, trong đó hàm `F(X)` được tính bằng Sliding Window trong $\mathcal{O}(N)$.
* C. Sử dụng cây Segment Tree với độ phức tạp `O(N log^2 N)`.
* D. Nhân đôi mảng và áp dụng Two Pointers đối đầu.
> *Giải thích:* Quy bài toán đếm đoạn trong khoảng `[A, B]` về hiệu của hai bài toán đếm tiền tố `<= X` giúp tận dụng trọn vẹn thuật toán Sliding Window tuyến tính $\mathcal{O}(N)$ mà không cần cấu trúc dữ liệu phức tạp.

---

# DANH SÁCH BÀI TẬP THỰC HÀNH

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Ràng Buộc Dữ Liệu | Mục Tiêu Rèn Luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `CPPB-CST-01` | **Tổng Cửa Sổ Cố Định K** | `P0` | `N <= 10^5, K $\le N$` | Trượt cố định $\mathcal{O}(1)$ mỗi bước |
| 02 | `CPPB-CST-02` | **Giá Trị Trung Bình Lớn Nhất Của Đoạn K** | `P1` | `N <= 10^5, K $\le N$` | Cửa sổ cố định với số thực |
| 03 | `CPPB-CST-03` | **Đoạn Con Ngắn Nhất Có Tổng Đạt S** | `P1` | `N <= 10^5, S <= 10^14` | Cửa sổ co giãn tìm `min` length |
| 04 | `CPPB-CST-04` | **Đoạn Con Dài Nhất Có Tổng Không Quá S** | `P2` | `N <= 2 * 10^5, S <= 10^14` | Cửa sổ co giãn tìm `max` length |
| 05 | `CPPB-CST-05` | **Đoạn Con Chứa Tối Đa K Số 0 (Lật Bit)** | `P3` | `N <= 10^5, K $\le N$` | Cửa sổ đếm trạng thái nhị phân |
| 06 | `CPPB-CST-06` | **Giám Sát Camera Giao Thông Thông Minh** | `P4` | `N <= 10^5, K $\le N$` | Tối ưu hóa cửa sổ thực tế |
| 07 | `CPPB-CST-07` | **Tìm Min Trong Mọi Cửa Sổ Độ Dài K** | `P1` | `N <= 10^4, K $\le N$` | Kiểm tra cửa sổ liên tiếp |
| 08 | `CPPB-CST-08` | **Đếm Số Lượng Đoạn Con Có Tổng Không Quá S** | `P2` | `N <= 2 * 10^5, S <= 10^14` | Cộng dồn `(R - L + 1)` đoạn con |
| 09 | `CPPB-CST-09` | **Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S** | `P2` | `N <= 2 * 10^5, A_i > 0` | Đếm đoạn trên mảng đơn điệu |
| 10 | `CPPB-CST-10` | **Đoạn Con Dài Nhất Chứa Tối Đa K Ký Tự Khác Nhau** | `P3` | `N <= 10^5, K <= 26` | Cửa sổ ký tự với mảng đếm tần suất |
| 11 | `CPPB-CST-11` | **Đoạn Con Ngắn Nhất Chứa Đủ Mọi Ký Tự Của Tập Hợp** | `P3` | `N <= 10^5, M <= 26` | Bài toán Minimum Window Substring |
| 12 | `CPPB-CST-12` | **Phủ Sóng Trạm Phát Sóng Wifi Đô Thị** | `P4` | `N <= 10^5, X_i <= 10^14` | Hai con trỏ + Tham lam vị trí |
| 13 | `CPPB-CST-13` | **Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K** | `P4` | $N \le 5000$ | Khống chế biên độ trong cửa sổ |
| 14 | `CPPB-CST-14` | **Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵** | `P5` | `N <= 2 * 10^5, A_i > 0` | Kỹ thuật hiệu `F(B) - F(A - 1)` |
