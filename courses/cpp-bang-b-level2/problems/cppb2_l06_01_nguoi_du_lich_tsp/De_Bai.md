# BÀI TOÁN NGƯỜI DU LỊCH (TSP)
## Mã bài toán: `CPPB2-L06-01` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho ma trận khoảng cách giữa $N$ thành phố ($N \le 18$). Tìm chi phí nhỏ nhất xuất phát từ thành phố 0, thăm tất cả các thành phố đúng 1 lần rồi quay về 0.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng 1: $N$. $N$ dòng tiếp theo: Ma trận khoảng cách $C_{i, j}$.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra chi phí nhỏ nhất.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

**Output:**
```text
80
```

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
