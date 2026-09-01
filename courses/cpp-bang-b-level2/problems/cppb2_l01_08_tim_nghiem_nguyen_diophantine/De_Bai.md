# TÌM NGHIỆM NGUYÊN PHƯƠNG TRÌNH DIOPHANTINE
## Mã bài toán: `CPPB2-L01-08` | Khóa học C++ Bảng B (Level 2)

---

## 📖 1. Bối Cảnh & Nhiệm Vụ

Phương trình Diophantine tuyến tính có dạng:
$$A \cdot x + B \cdot y = C$$
trong đó $A, B, C$ là các số nguyên cho trước, ta cần tìm cặp nghiệm nguyên $(x, y)$ hoặc kết luận vô nghiệm.

Theo **Định lý Bézout**, phương trình trên có nghiệm nguyên khi và chỉ khi $\gcd(A, B)$ chia hết $C$.

Cho $T$ bộ dữ liệu, mỗi bộ gồm ba số nguyên $A, B, C$. Hãy kiểm tra phương trình $Ax + By = C$ có nghiệm nguyên hay không. Nếu có, in ra một cặp nghiệm $(x_0, y_0)$.

---

## 📥 2. Định Dạng Đầu Vào (Input)

* Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10^5$).
* $T$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $A$, $B$, $C$ ($-10^9 \le A, B, C \le 10^9$), cách nhau bởi dấu cách.

---

## 📤 3. Định Dạng Đầu Ra (Output)

* Gồm $T$ dòng:
  * Nếu phương trình vô nghiệm, in `NO`.
  * Nếu có nghiệm, in `YES x0 y0` với $(x_0, y_0)$ là một cặp nghiệm nguyên bất kỳ.

---

## 📌 4. Ví Dụ Mẫu (Sample)

### Sample 1:
**Input:**
```text
3
2 3 7
4 6 3
0 0 0
```

**Output:**
```text
YES -7 7
NO
YES 0 0
```

### Giải thích Sample 1:
* $2x + 3y = 7$: $\gcd(2, 3) = 1 \mid 7 \implies$ có nghiệm. Nghiệm $(x_0, y_0) = (-7, 7)$: $2(-7) + 3(7) = -14 + 21 = 7$ ✓.
* $4x + 6y = 3$: $\gcd(4, 6) = 2 \nmid 3 \implies$ vô nghiệm.
* $0x + 0y = 0$: $0 = 0 \implies$ mọi $(x, y)$ đều là nghiệm, in $(0, 0)$.

---

## ⚙️ 5. Ràng Buộc Kỹ Thuật (Constraints)

* Giới hạn thời gian (Time Limit): $1.0\text{s}$.
* Giới hạn bộ nhớ (Memory Limit): $256\text{MB}$.
* $1 \le T \le 10^5$.
* $-10^9 \le A, B, C \le 10^9$.
* Nếu phương trình có nghiệm, đảm bảo tồn tại cặp $(x_0, y_0)$ nằm trong phạm vi `long long`.
