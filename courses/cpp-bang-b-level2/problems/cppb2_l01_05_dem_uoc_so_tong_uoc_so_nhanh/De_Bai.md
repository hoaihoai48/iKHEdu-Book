# ĐẾM ƯỚC SỐ & TỔNG ƯỚC SỐ NHANH
## Mã bài toán: `CPPB2-L01-05` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $N$ ($2 \le N \le 10^6$). Với mỗi $N$, hãy tính:
1. **Số lượng ước số** $d(N)$ — tổng số ước dương của $N$.
2. **Tổng các ước số** $\sigma(N)$ — tổng tất cả các ước dương của $N$.

Sử dụng phân tích thừa số nguyên tố qua mảng SPF: nếu $N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}$ thì:
$$d(N) = \prod_{i=1}^k (a_i + 1) \qquad \sigma(N) = \prod_{i=1}^k \frac{p_i^{a_i + 1} - 1}{p_i - 1}$$

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^5$).
* $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $N$ ($2 \le N \le 10^6$).

---

## 📤 3. Định Dạng Đầu Ra (Output)

* Gồm $Q$ dòng, mỗi dòng in ra hai số nguyên $d(N)$ và $\sigma(N)$ cách nhau bởi một dấu cách.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
4
12
28
7
100
```

**Output:**
```text
6 28
6 56
2 8
9 217
```

### Giải thích Sample 1:
* $12 = 2^2 \times 3^1$: ước là $\{1,2,3,4,6,12\}$, $d = 6$, $\sigma = 28$.
* $28 = 2^2 \times 7^1$: ước là $\{1,2,4,7,14,28\}$, $d = 6$, $\sigma = 56$.
* $7 = 7^1$: $d = 2$, $\sigma = 8$.
* $100 = 2^2 \times 5^2$: $d = (2+1)(2+1) = 9$, $\sigma = \frac{8-1}{1} \cdot \frac{125-1}{4} = 7 \times 31 = 217$.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* $1 \le Q \le 10^5$.
* $2 \le N \le 10^6$.
