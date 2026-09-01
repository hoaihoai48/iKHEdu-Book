# TRUY VẤN TỔNG ĐOẠN FENWICK TREE
## Mã bài toán: `CPPB2-L13-01` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Cho mảng $N$ phần tử. Có $Q$ thao tác: `1 u v` (cộng $v$ vào $A[u]$) và `2 l r` (tính tổng $A[l..r]$).

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng 1: $N, Q$. Dòng 2: $N$ số $A_i$. $Q$ dòng tiếp theo: các truy vấn.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* In ra kết quả của các truy vấn loại 2.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
5 3
1 2 3 4 5
2 1 5
1 3 2
2 1 5
```

**Output:**
```text
15
17
```

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
