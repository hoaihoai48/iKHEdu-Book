# Bài 12: ĐẾM SỐ THEO QUY LUẬT VÀ SỐ ĐẶC BIỆT

## 1. Bản Chất Bài Toán Đếm Số Theo Quy Luật

Khi lập trình giải các bài toán, dạng toán **đếm số lượng số thỏa mãn một tính chất nào đó trong một khoảng $[A, B]$** là một trong những dạng toán kinh điển và xuất hiện nhiều nhất:

- Đếm số lượng số chia hết cho $K$ trong đoạn từ $A$ đến $B$.
- Đếm số lượng số lẻ, số chẵn, hoặc số có chữ số tận cùng là 5.
- Đếm các số đặc biệt: số chính phương, số hoàn hảo, số tự mãn (Armstrong / Narcissistic).

Tùy thuộc vào giới hạn của bài toán ($B - A \le 10^5$ hay $B \le 10^{12}$), chúng ta có 2 phương pháp tiếp cận hoàn toàn khác nhau.

---

## 2. Kỹ Thuật Đếm Trong Đoạn Bằng Vòng Lặp Duyệt Từng Số

Khi khoảng cách giữa $A$ và $B$ nhỏ (dưới vài chục nghìn số), máy tính có thể duyệt qua từng số một cách nhanh chóng.

### 2.1. Quy tắc tính số lần lặp trong đoạn $[A, B]$
Muốn duyệt từ số $A$ đến số $B$ (tính cả 2 đầu mút $A$ và $B$), số lượng số cần kiểm tra là:
$$\text{Số lần lặp} = B - A + 1$$

> **Ví dụ:** Từ số $3$ đến số $7$ có bao nhiêu số?
> - Phép tính sai lầm: $7 - 3 = 4$ số.
> - Thực tế đếm tay: $3, 4, 5, 6, 7$ $\implies$ Có đúng **5 số** ($7 - 3 + 1 = 5$).

### 2.2. Khối lệnh Scratch đếm số chia hết cho $K$ trong $[A, B]$

![Thuật toán đếm số trong khoảng A đến B](assets/rendered_blocks/l12_count_range_vi.png)

**Các bước thuật toán:**

1. Khởi tạo biến đếm: `đặt [dem v] thành (0)`.

2. Bắt đầu từ số nhỏ nhất: `đặt [i v] thành (A)`.

3. Lặp đúng `(B - A + 1)` lần:

   - Nếu số hiện tại chia hết cho $K$ (`< (i mod K) = 0 >`) thì tăng biến đếm lên 1.
   - Luôn tăng biến `i` lên 1 để chuyển sang số kế tiếp.

4. Thông báo kết quả qua biến `dem`.

---

## 3. Công Thức Đếm Toán Học Siêu Tốc $\mathcal{O}(1)$

Khi $A$ và $B$ là các con số khổng lồ (ví dụ đếm số chia hết cho 7 từ $1$ đến $1\,000\,000\,000$), việc chạy vòng lặp $1$ tỷ lần sẽ làm máy tính bị treo (Time Limit Exceeded). Ta dùng công thức toán học tính ngay lập tức trong **1 phép tính**:

### 3.1. Nguyên lý đếm từ $1$ đến $N$
Số lượng các số chia hết cho $K$ trong đoạn $[1, N]$ chính là phần nguyên của phép chia $N$ cho $K$:
$$\text{Count}(1, N) = \lfloor N / K \rfloor$$
Trong Scratch: `[làm tròn xuống v] của ((N) / (K))`.

> **Ví dụ:** Từ 1 đến 20 có bao nhiêu số chia hết cho 3?
> - Các số đó là: $3, 6, 9, 12, 15, 18$ (tổng cộng 6 số).
> - Tính nhanh: $\lfloor 20 / 3 \rfloor = 6$.

### 3.2. Nguyên lý bù trừ cho đoạn bất kỳ $[A, B]$
Để đếm trong đoạn $[A, B]$, ta lấy số lượng số chia hết từ $1 \to B$ trừ đi số lượng số chia hết từ $1 \to (A - 1)$:
$$\text{Count}(A, B) = \lfloor B / K \rfloor - \lfloor (A - 1) / K \rfloor$$

Khối phép toán trong Scratch:
`(([làm tròn xuống v] của ((B) / (K))) - ([làm tròn xuống v] của (((A) - (1)) / (K))))`

---

## 4. Các Dạng Số Đặc Biệt Thường Gặp Trong Lập Trình

### 4.1. Số Chính Phương (Perfect Square)
Số chính phương là số tự nhiên có căn bậc hai là một số nguyên (nghĩa là bằng bình phương của một số tự nhiên: $0, 1, 4, 9, 16, 25, 36, 49, \dots$).
- **Cách kiểm tra trong Scratch:** Lấy căn bậc hai của $N$, làm tròn xuống rồi bình phương lại xem có bằng chính $N$ không:
  $$< (([làm tròn xuống v] của ([căn bậc hai v] của (N))) \times ([làm tròn xuống v] của ([căn bậc hai v] của (N)))) = (N) >$$

### 4.2. Số Hoàn Hảo (Perfect Number)
Số hoàn hảo là số nguyên dương có **tổng tất cả các ước số thực sự của nó (ngoại trừ chính nó) bằng chính nó**.
- Số hoàn hảo nhỏ nhất là $6$: các ước nhỏ hơn 6 là $1, 2, 3$, và $1 + 2 + 3 = 6$.
- Số hoàn hảo tiếp theo là $28$: các ước nhỏ hơn 28 là $1, 2, 4, 7, 14$, và $1 + 2 + 4 + 7 + 14 = 28$.

### 4.3. Số Tự Mãn (Số Armstrong / Narcissistic)
Là số có $k$ chữ số, và tổng lũy thừa bậc $k$ của từng chữ số bằng chính nó.
- Ví dụ số 3 chữ số: $153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.
- Ta kết hợp thuật toán tách chữ số (Bài 10) và tích lũy thừa (Bài 05) để kiểm tra.

---

## 5. Bảng Mô Phỏng Đếm Số Chia Hết Cho 3 Trong Đoạn $[4, 12]$ (Dry Run Table)

Giả sử $A = 4, B = 12, K = 3$. Số lần lặp $= 12 - 4 + 1 = 9$ lần.

| Bước | Giá trị `i` | Điều kiện `< (i mod 3) = 0 >` | Biến đếm `dem` | Hành động tiếp theo |
|:---:|:---:|:---:|:---:|---|
| *Bắt đầu* | $i = 4$ | — | **$0$** | Bắt đầu vòng lặp |
| **1** | $i = 4$ | $4 \bmod 3 = 1 \ne 0$ $\to$ SAI | $0$ | Tăng $i = 5$ |
| **2** | $i = 5$ | $5 \bmod 3 = 2 \ne 0$ $\to$ SAI | $0$ | Tăng $i = 6$ |
| **3** | $i = 6$ | $6 \bmod 3 = 0$ $\to$ **ĐÚNG** | **$1$** | Đếm số 6! Tăng $i = 7$ |
| **4** | $i = 7$ | $7 \bmod 3 = 1 \ne 0$ $\to$ SAI | $1$ | Tăng $i = 8$ |
| **5** | $i = 8$ | $8 \bmod 3 = 2 \ne 0$ $\to$ SAI | $1$ | Tăng $i = 9$ |
| **6** | $i = 9$ | $9 \bmod 3 = 0$ $\to$ **ĐÚNG** | **$2$** | Đếm số 9! Tăng $i = 10$ |
| **7** | $i = 10$ | $10 \bmod 3 = 1 \ne 0$ $\to$ SAI | $2$ | Tăng $i = 11$ |
| **8** | $i = 11$ | $11 \bmod 3 = 2 \ne 0$ $\to$ SAI | $2$ | Tăng $i = 12$ |
| **9** | $i = 12$ | $12 \bmod 3 = 0$ $\to$ **ĐÚNG** | **$3$** | Đếm số 12! Tăng $i = 13$ |

$\implies$ Kết quả: `dem = 3` (các số $6, 9, 12$).
- Kiểm tra lại bằng công thức toán: $\lfloor 12 / 3 \rfloor - \lfloor (4 - 1) / 3 \rfloor = 4 - 1 = 3$ số (hoàn toàn chuẩn xác!).

---

## 6. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên trừ 1 ở đầu mút $A$ trong công thức toán $\mathcal{O}(1)$**
> - *Hiện tượng:* Tính `floor(B / K) - floor(A / K)`.
> - *Hậu quả:* Nếu chính số $A$ chia hết cho $K$ (như $A = 6, B = 12, K = 3$), ta có $12/3 - 6/3 = 4 - 2 = 2$ số (trong khi thực tế có 3 số là $6, 9, 12$). Phép trừ đã làm biến mất luôn chính số $A$!
> - *Khắc phục:* Luôn luôn là `floor((A - 1) / K)`.

> **Bẫy 2: Số lần lặp trong đoạn $[A, B]$**
> - *Hiện tượng:* Cho vòng lặp chạy `B - A` lần.
> - *Hậu quả:* Bị thiếu mất 1 số ở cuối mút.
> - *Khắc phục:* Số lần lặp luôn là `((B) - (A)) + (1)`.

> **Bẫy 3: Đặt khối tăng biến đếm `i` nằm bên trong khối `nếu...thì`**
> - *Hậu quả:* Chỉ khi nào số đó thỏa điều kiện thì `i` mới tăng, nếu gặp số không thỏa thì `i` đứng yên vĩnh viễn $\implies$ Vòng lặp vô tận, đơ chương trình!
> - *Khắc phục:* Khối `thay đổi [i v] một lượng 1` phải luôn nằm **bên ngoài** khối `nếu...thì`.

---

## 7. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Từ số 1 đến số 10 có bao nhiêu số nguyên?**
   - A. 9
   - B. 10 *(Đáp án đúng: $10 - 1 + 1 = 10$)*
   - C. 11
   - D. 8

2. **Từ 1 đến 100 có bao nhiêu số chia hết cho 5?**
   - A. 20 *(Đáp án đúng: $\lfloor 100 / 5 \rfloor = 20$)*
   - B. 19
   - C. 25
   - D. 10

3. **Công thức toán tính nhanh số lượng số chia hết cho $K$ trong đoạn $[A, B]$ là:**
   - A. `(B / K) - (A / K)`
   - B. `floor(B / K) - floor((A - 1) / K)` *(Đáp án đúng)*
   - C. `floor(B / K) - floor(A / K)`
   - D. `(B - A) / K`

4. **Số nào sau đây là một số chính phương?**
   - A. 12
   - B. 24
   - C. 49 *(Đáp án đúng: $7 \times 7 = 49$)*
   - D. 50

5. **Số hoàn hảo nhỏ nhất là số nào?**
   - A. 1
   - B. 2
   - C. 6 *(Đáp án đúng: $1 + 2 + 3 = 6$)*
   - D. 28

6. **Điều kiện nào trong Scratch kiểm tra số $N$ là số chẵn?**
   - A. `< ((N) mod (2)) = (0) >` *(Đáp án đúng)*
   - B. `< ((N) mod (2)) = (1) >`
   - C. `< ((N) / (2)) = (0) >`
   - D. `< (N) > (2) >`

7. **Trong đoạn từ $10$ đến $30$, có bao nhiêu số chia hết cho $10$?**
   - A. 2
   - B. 3 *(Đáp án đúng: 10, 20, 30)*
   - C. 4
   - D. 1

8. **Nếu muốn duyệt các số chẵn từ $A$ (với $A$ chẵn) đến $B$, sau mỗi bước ta nên tăng biến `i` một lượng:**
   - A. 1
   - B. 2 *(Đáp án đúng: nhảy cách 2 đơn vị)*
   - C. 3
   - D. A

9. **Số 153 là một số đặc biệt thuộc loại nào?**
   - A. Số nguyên tố
   - B. Số hoàn hảo
   - C. Số Armstrong / Tự mãn *(Đáp án đúng: $1^3 + 5^3 + 3^3 = 153$)*
   - D. Số chính phương

10. **Khi viết vòng lặp kiểm tra các số từ $A$ đến $B$, nếu $A > B$ thì vòng lặp đếm `B - A + 1` lần sẽ:**
    - A. Chạy lùi về $B$
    - B. Không chạy hoặc gây lỗi vì số lần lặp bị âm *(Đáp án đúng)*
    - C. Tự động đổi chỗ $A$ và $B$
    - D. In ra kết quả 0
