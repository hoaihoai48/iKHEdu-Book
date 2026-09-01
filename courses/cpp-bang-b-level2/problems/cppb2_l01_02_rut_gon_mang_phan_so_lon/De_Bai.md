# RÚT GỌN MẢNG PHÂN SỐ LỚN
## Mã bài toán: `CPPB2-L01-02` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Trong toán học và lập trình thi đấu, việc chuẩn hóa phân số về dạng **tối giản** là thao tác then chốt để so sánh và tính toán chính xác mà không gặp sai số dấu phẩy động (`floating-point error`).

Một phân số $\frac{A}{B}$ được gọi là tối giản chuẩn khi:
1. $\gcd(|P|, |Q|) = 1$ với phân số tối giản $\frac{P}{Q}$.
2. Mẫu số luôn dương: $Q > 0$. Nếu phân số âm, dấu âm phải được đặt ở tử số ($P < 0$).
3. Nếu tử số bằng $0$, phân số tối giản luôn biểu diễn là `0 1`.

Cho $N$ phân số, mỗi phân số có dạng $\frac{A_i}{B_i}$ ($B_i \ne 0$). Hãy rút gọn từng phân số về dạng tối giản chuẩn.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng phân số cần rút gọn.
* $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $A_i$ và $B_i$ ($-10^9 \le A_i \le 10^9$, $1 \le |B_i| \le 10^9$, $B_i \ne 0$), cách nhau bởi một dấu cách.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* Gồm $N$ dòng, mỗi dòng in ra hai số nguyên $P_i$ và $Q_i$ cách nhau bởi một dấu cách, biểu diễn phân số tối giản $\frac{P_i}{Q_i}$ tương ứng ($Q_i > 0$).

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
4
12 18
-6 8
15 -25
0 -100
```

**Output:**
```text
2 3
-3 4
-3 5
0 1
```

### Giải thích Sample 1:
* $\frac{12}{18}$: $\gcd(12, 18) = 6 \implies \frac{12/6}{18/6} = \frac{2}{3}$.
* $\frac{-6}{8}$: $\gcd(6, 8) = 2 \implies \frac{-6/2}{8/2} = \frac{-3}{4}$.
* $\frac{15}{-25}$: $\gcd(15, 25) = 5 \implies \frac{15/5}{-25/5} = \frac{3}{-5} \implies$ chuẩn hóa mẫu dương thành $\frac{-3}{5}$.
* $\frac{0}{-100}$: chuẩn hóa thành `0 1`.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* $1 \le N \le 10^5$.
* $-10^9 \le A_i \le 10^9$.
* $1 \le |B_i| \le 10^9$, $B_i \ne 0$.
