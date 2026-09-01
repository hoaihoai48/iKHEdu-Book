# TRUY VẤN SO KHỚP XÂU CON HASHING
## Mã bài toán: `CPPB2-L15-01` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho xâu $S$ và $Q$ truy vấn kiểm tra xem hai xâu con $S[a..b]$ và $S[c..d]$ có giống nhau hay không.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng 1: Xâu $S$ ($|S| \le 10^5$). Dòng 2: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $a, b, c, d$ (1-based).

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra `YES` nếu hai xâu con bằng nhau, `NO` nếu khác nhau.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
abacaba
2
1 3 5 7
1 3 2 4
```

**Output:**
```text
YES
NO
```

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
