# Hướng Dẫn Giảng Dạy: Lũy Thừa Cầu Thang
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững toán tử lũy thừa `**` trong Python qua bài toán tính $a^n$ (`PYA-L02-P13`).
* **Tư duy thuật toán:** Hiểu lũy thừa là phép nhân lặp lại, phân biệt `**` với `^` và `*`.
* **Chuẩn code thi đấu:** Đọc 2 số bằng `input()`, ép kiểu `int`, in đúng một số bằng `print()`.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Cơ số $a$ ($1 \le a \le 10$), số mũ $n$ ($0 \le n \le 10$). Kết quả tối đa $10^{10}$ vừa trong số nguyên Python.
* **Bản chất toán học:** $a^n = a \times a \times \dots \times a$ ($n$ lần). Quy ước $a^0 = 1$.
* **Trường hợp biên (Edge Cases):**
  * $n = 0$: kết quả luôn là $1$ (kể cả $a$ bất kỳ).
  * $a = 1$: kết quả luôn là $1$.
  * $n = 1$: kết quả bằng chính $a$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Muốn tính $3^4$ em sẽ viết phép nhân dài thế nào? Có cách viết ngắn gọn trong Python không?
2. Ký hiệu `^` trong Python có phải là lũy thừa không? Vì sao cô lại cấm dùng nó?
3. Khi số mũ bằng 0 thì kết quả là bao nhiêu? Em thử đoán rồi kiểm tra bằng máy tính?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Tính trực tiếp bằng toán tử `**` với độ phức tạp $\mathcal{O}(1)$, không cần vòng lặp vì $n \le 10$.
* **Bất biến thuật toán (Invariant):**
  > Biểu thức `a ** n` luôn bằng tích của $n$ thừa số $a$, và quy ước tích rỗng ($n = 0$) bằng $1$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
3
4
```
* **Output:**
```text
81
```
* **Giải thích:** $3^4 = 3 \times 3 \times 3 \times 3 = 81$. Tầng cao nhất của cầu thang có 81 khối gỗ.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc cơ số | `a = 3` | Khởi tạo cơ số |
| **2** | Đọc số mũ | `n = 4` | Khởi tạo số mũ |
| **3** | Tính `a ** n` | `3 ** 4 = 81` | Ra kết quả 81 |
| **4** | In kết quả | `print(81)` | Đúng Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa yêu cầu giới hạn $1.0\text{s}$ của kỳ thi).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ tối thiểu, đảm bảo an toàn tuyệt đối trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Dùng `^` thay cho `**`:** `3 ^ 4 = 7` (phép XOR bit), không phải $81$.
2. **Quên ép kiểu:** Dùng trực tiếp chuỗi từ `input()` để tính `**` gây lỗi `TypeError`.
3. **In thừa giải thích:** Viết `print("Ket qua la:", ans)` thay vì chỉ in `ans` gây `Wrong Answer (WA)`.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
a = int(input())
n = int(input())
print(a ** n)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Tính tổng các tầng cầu thang $a^1 + a^2 + \dots + a^n$ (chuẩn bị cho vòng lặp Bài 7).
* **Mở rộng 2:** So sánh $2^{10}$ với $10^3$ để cảm nhận tốc độ tăng của lũy thừa cơ số 2.
