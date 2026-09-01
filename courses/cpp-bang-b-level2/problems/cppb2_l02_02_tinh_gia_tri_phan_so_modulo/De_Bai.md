# TÍNH GIÁ TRỊ PHÂN SỐ MODULO
## Mã bài toán: `CPPB2-L02-02` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho hai số nguyên $P, Q$ ($Q \not\equiv 0 \pmod{10^9+7}$). Hãy tính $(P \times Q^{-1}) \bmod (10^9+7)$.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng 1: $T$ ($1 \le T \le 10^5$). $T$ dòng sau: $P, Q$ ($0 \le P \le 10^9, 1 \le Q \le 10^9$).

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra $(P / Q) \bmod (10^9+7)$ trên mỗi dòng.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
2
1 2
3 7
```

**Output:**
```text
500000004
428571432
```

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
