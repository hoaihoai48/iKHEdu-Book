# SÀNG ƯỚC SỐ NGUYÊN TỐ NHỎ NHẤT (SPF)
## Mã bài toán: `CPPB2-L01-03` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Trong các bài toán xử lý số học nhiều truy vấn, việc tìm **ước số nguyên tố nhỏ nhất** ($\text{Smallest Prime Factor} - \text{SPF}$) của một số là bước tiền xử lý nền tảng giúp phân tích thừa số nguyên tố, đếm ước số, tính hàm nhân tính và tìm các số nguyên tố cùng nhau trong thời gian logarit $\mathcal{O}(\log N)$.

Cho $Q$ truy vấn, mỗi truy vấn gồm một số nguyên dương $X$ ($2 \le X \le 10^6$). Hãy tìm ước số nguyên tố nhỏ nhất của $X$ (ký hiệu là $\text{spf}[X]$).

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số nguyên dương $Q$ ($1 \le Q \le 10^6$) — số lượng truy vấn.
* $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên dương $X$ ($2 \le X \le 10^6$).

---

## 📤 3. Định Dạng Đầu Ra (Output)

* Gồm $Q$ dòng, mỗi dòng in ra ước số nguyên tố nhỏ nhất $\text{spf}[X]$ của số $X$ tương ứng.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
5
2
9
15
84
999983
```

**Output:**
```text
2
3
3
2
999983
```

### Giải thích Sample 1:
* $X = 2$: là số nguyên tố $\implies \text{spf}[2] = 2$.
* $X = 9 = 3^2 \implies \text{spf}[9] = 3$.
* $X = 15 = 3 \times 5 \implies \text{spf}[15] = 3$.
* $X = 84 = 2^2 \times 3 \times 7 \implies \text{spf}[84] = 2$.
* $X = 999983$: là số nguyên tố $\implies \text{spf}[999983] = 999983$.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* $1 \le Q \le 10^6$.
* $2 \le X \le 10^6$.
