# ƯỚC CHUNG & BỘI CHUNG CƠ BẢN
## Mã bài toán: `CPPB2-L01-01` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Trong các kỳ thi lập trình thi đấu, việc tìm **Ước chung lớn nhất ($\gcd$)** và **Bội chung nhỏ nhất ($\text{lcm}$)** là một trong những khối xử lý cơ sở nền tảng nhất. Tuy nhiên, khi các số đầu vào có giá trị lớn (lên tới $10^9$), việc tính toán bất cẩn phép nhân trong $\text{lcm}$ rất dễ dẫn đến lỗi tràn số nguyên 64-bit (`long long`).

Cho $T$ bộ dữ liệu, mỗi bộ gồm hai số nguyên dương $A$ và $B$. Nhiệm vụ của bạn là tính và in ra $\gcd(A, B)$ và $\text{lcm}(A, B)$.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$) — số lượng bộ dữ liệu cần xử lý.
* $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^9$), cách nhau bởi một dấu cách.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* Gồm $T$ dòng, mỗi dòng in ra hai số nguyên cách nhau bởi một dấu cách: số đầu tiên là $\gcd(A, B)$, số thứ hai là $\text{lcm}(A, B)$.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
3
12 18
6 9
1000000000 1000000000
```

**Output:**
```text
6 36
3 18
1000000000 1000000000
```

### Giải thích Sample 1:
* Với cặp $(12, 18)$: $\gcd(12, 18) = 6$, $\text{lcm}(12, 18) = \frac{12}{6} \times 18 = 36$.
* Với cặp $(6, 9)$: $\gcd(6, 9) = 3$, $\text{lcm}(6, 9) = \frac{6}{3} \times 9 = 18$.
* Với cặp $(10^9, 10^9)$: $\gcd = 10^9, \text{lcm} = 10^9$.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* $1 \le T \le 10^5$.
* $1 \le A, B \le 10^9$.
* Đảm bảo giá trị $\text{lcm}(A, B) \le 10^{18}$ nằm trọn vẹn trong kiểu dữ liệu `long long`.
