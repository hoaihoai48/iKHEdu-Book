# Hướng Dẫn Giảng Dạy: Đổi Đô La Sang Tiền Việt
Chuyên đề: **Đổi đơn vị tiền tệ — Phép nhân tỉ lệ**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Đổi Đô La Sang Tiền Việt** (`PYA-L03-P13`) bằng Python ở mức `Luyện tập`.
* **Tư duy thuật toán:** Rèn luyện phản xạ đổi đơn vị bằng phép nhân với tỉ giá cố định $25000$.
* **Chuẩn code thi đấu:** Đọc 1 số, nhân số lớn tới $2.5 \times 10^{10}$, in chính xác không dấu phẩy.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Một số tự nhiên $D$ ($1 \le D \le 10^6$), kết quả $D \times 25000$ tối đa $2.5 \times 10^{10}$.
* **Bản chất toán học:** Hàm tuyến tính một biến: mỗi đô la tương ứng $25000$ đồng.
* **Trường hợp biên (Edge Cases):**
  * Đổi ít nhất $D = 1$ được $25000$ đồng.
  * Đổi nhiều nhất $D = 10^6$ được $25000000000$ đồng.
  * Học sinh dễ viết thiếu số 0 ($2500$ thay vì $25000$).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. $1$ đô la đổi được bao nhiêu đồng? $2$ đô la thì gấp mấy lần?
2. Vì sao bài này chỉ cần một phép nhân, không cần `//` hay `%`?
3. Số tiền $100000$ có bao nhiêu chữ số 0? Làm sao kiểm tra mình không viết thiếu?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Đọc $D$, tính $D \times 25000$, in kết quả $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Tỉ lệ tiền Việt trên đô la luôn bảo toàn $25000 : 1$ trước và sau phép tính.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
4
```
* **Output:**
```text
100000
```
* **Giải thích:** $4 \times 25000 = 100000$ đồng.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `d` | `d = 4` | Số đô la cần đổi |
| **2** | Tính `d * 25000` | `4 * 25000 = 100000` | Số tiền Việt |
| **3** | `print(100000)` | Xuất kết quả | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, một biến nguyên trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Sai tỉ giá:** Nhân với $2500$ hoặc $250000$ vì đếm nhầm số 0.
2. **In kèm đơn vị:** Viết `print("100000 dong")` gây `Wrong Answer (WA)`.
3. **Quên ép kiểu:** Tính `"4" * 25000` tạo chuỗi khổng lồ thay vì số học.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
d = int(input())
print(d * 25000)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Đổi ngược từ tiền Việt sang đô la bằng phép chia nguyên và tính tiền thừa.
* **Mở rộng 2:** So sánh hai chuyến đổi tiền với hai tỉ giá khác nhau để chọn ngân hàng lợi hơn.
