# Hướng Dẫn Giảng Dạy: Tính Vận Tốc Làm Tròn
Chuyên đề: **Quãng đường – Vận tốc – Thời gian + Làm tròn**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Tính Vận Tốc Làm Tròn** (`PYA-L03-P15`) bằng Python ở mức `Vận dụng`.
* **Tư duy thuật toán:** Rèn luyện phản xạ dùng phép chia thực $V = D / T$ rồi định dạng `f-string` `:.2f`.
* **Chuẩn code chuẩn:** Đọc 2 số nguyên, chia thực, in đúng 2 chữ số thập phân kể cả số 0 ở cuối.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Trường hợp đặc biệt)
* **Phân tích tham số:** Hai số nguyên $D, T$ ($1 \le D, T \le 10^4$), kết quả là số thực cần làm tròn 2 chữ số.
* **Bản chất toán học:** Vận tốc trung bình bằng quãng đường chia thời gian; phần thập phân vô hạn cần làm tròn.
* **Trường hợp biên (Trường hợp đặc biệt):**
 * Chia hết: $D = 100, T = 4$ phải in `25.00` chứ không phải `25.0` hay `25`.
 * Số lớn: $D = T = 10000$ cho `1.00`.
 * Học sinh dễ dùng `//` ra số nguyên hoặc `round()` thiếu số 0 đệm.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Vận tốc bằng quãng đường chia hay nhân thời gian? $100 : 6$ được khoảng bao nhiêu?
2. Vì sao phải dùng `/` mà không dùng `//` ở bài này?
3. `f"{x:.2f}"` có nghĩa là gì? Nếu kết quả là `25` thì máy in ra mấy chữ số sau dấu chấm?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Đọc $D, T$; tính $D / T$ kiểu `float`; in bằng `f"{v:.2f}"` $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
 > Chuỗi in ra luôn có đúng 2 chữ số sau dấu chấm, là dạng làm tròn gần nhất của thương $D : T$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
100
6
```
* **Output:**
```text
16.67
```
* **Giải thích:** $100 : 6 = 16.666\ldots$, làm tròn 2 chữ số được $16.67$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `d, t` | `d=100, t=6` | Quãng đường và thời gian |
| **2** | Tính `d / t` | `16.6666...` | Thương số thực |
| **3** | Định dạng `:.2f` | `"16.67"` | Làm tròn 2 chữ số |
| **4** | `print("16.67")` | Xuất kết quả | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, hai biến số trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Dùng `//`:** Ra `16` thay vì `16.67` vì chia nguyên bỏ phần dư.
2. **Dùng `round()` trần:** `print(round(v, 2))` in `25.0` thay vì `25.00` khi chia hết.
3. **Quên ép kiểu:** Chia hai chuỗi `"100" / "6"` báo lỗi `TypeError`.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
d = int(input())
t = int(input())
print(f"{d / t:.2f}")
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Tính quãng đường $S = V \times T$ khi biết vận tốc thập phân và thời gian.
* **Mở rộng 2:** So sánh vận tốc hai bạn nhỏ và cho biết bạn nào nhanh hơn bao nhiêu km/h (làm tròn 2 chữ số).
