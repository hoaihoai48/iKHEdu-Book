# TRUY VẤN TỔNG MA TRẬN CON 2D
## Mã bài toán: `CPPB2-L04-01` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho ma trận $A$ kích thước $N \times M$. Có $Q$ truy vấn tính tổng hình chữ nhật từ $(x_1, y_1)$ đến $(x_2, y_2)$.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng 1: $N, M, Q$ ($1 \le N, M \le 1000, 1 \le Q \le 10^5$). $N$ dòng tiếp theo chứa ma trận. $Q$ dòng sau: $x_1, y_1, x_2, y_2$.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra tổng mỗi hình chữ nhật con trên một dòng.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
3 3 2
1 2 3
4 5 6
7 8 9
1 1 2 2
2 2 3 3
```

**Output:**
```text
12
28
```

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
