# Hướng Dẫn Giảng Dạy: Giá Trị Biểu Thức PEMDAS
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững thứ tự ưu tiên PEMDAS: ngoặc → lũy thừa `**` → nhân chia → cộng trừ (`PYA-L02-P15`).
* **Tư duy thuật toán:** Biết mô phỏng tay biểu thức $a + b \times c^2$ trước khi viết code.
* **Chuẩn code thi đấu:** Đọc 3 số trên 3 dòng, viết đúng một biểu thức Python duy nhất.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** $a, b, c$ ($1 \le a, b, c \le 100$). Kết quả tối đa $100 + 100 \times 100^2 = 1000100$.
* **Bản chất toán học:** Tính $c^2$ trước, rồi nhân với $b$, cuối cùng cộng $a$.
* **Trường hợp biên (Edge Cases):**
  * $c = 1$: $c^2 = 1$, biểu thức thành $a + b$.
  * $a, b, c$ tối đa $100$: kiểm tra số có 7 chữ số vẫn in nguyên vẹn.
  * Học sinh quên thứ tự sẽ tính $(a + b) \times c^2$ cho ra số lớn hơn nhiều.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Trong biểu thức $2 + 3 \times 4^2$, phép nào phải làm trước: cộng, nhân hay lũy thừa?
2. Nếu cô thêm ngoặc $(2 + 3) \times 4^2$ thì kết quả thay đổi thế nào?
3. Trong Python, em viết $c^2$ bằng ký hiệu nào? Có được viết `c ^ 2` không?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Viết đúng một dòng `a + b * c ** 2`, để Python tự áp dụng PEMDAS, độ phức tạp $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Thứ tự tính luôn là $c^2 \to b \times c^2 \to a + (b \times c^2)$, không bao giờ cộng trước nhân.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
2
3
4
```
* **Output:**
```text
50
```
* **Giải thích:** Ưu tiên lũy thừa trước: $c^2 = 4^2 = 16$. Tiếp theo nhân: $b \times 16 = 3 \times 16 = 48$. Cuối cùng cộng: $2 + 48 = 50$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc 3 số | `a=2, b=3, c=4` | Khởi tạo đầu vào |
| **2** | Lũy thừa | `c ** 2 = 16` | Ưu tiên cao nhất |
| **3** | Nhân | `3 * 16 = 48` | Ưu tiên thứ hai |
| **4** | Cộng và in | `2 + 48 = 50` | Đúng Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa yêu cầu giới hạn $1.0\text{s}$ của kỳ thi).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ tối thiểu, đảm bảo an toàn tuyệt đối trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Thêm ngoặc sai:** Viết `(a + b) * c ** 2` cho ra $80$ thay vì $50$ với sample.
2. **Dùng `^` cho lũy thừa:** `c ^ 2` là phép XOR bit, cho kết quả hoàn toàn sai.
3. **Tách phép tính sai thứ tự:** Tính `a + b` trước rồi mới nhân với `c ** 2` do hiểu nhầm trái-sang-phải.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
a = int(input())
b = int(input())
c = int(input())
print(a + b * c ** 2)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Tính biểu thức có ngoặc $(a + b) \times c^2$ rồi so sánh với $a + b \times c^2$ để thấy sức mạnh của ngoặc.
* **Mở rộng 2:** Mở rộng thành $a + b \times c^2 - d // e$ để luyện cả 7 phép toán trong một biểu thức.
