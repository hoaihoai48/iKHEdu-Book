# Hướng Dẫn Giảng Dạy: Đổi Độ C Sang Độ F
Chuyên đề: **Đổi đơn vị nhiệt độ — Biểu thức hỗn hợp**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Đổi Độ C Sang Độ F** (`PYA-L03-P14`) bằng Python ở mức `Luyện tập`.
* **Tư duy thuật toán:** Rèn luyện phản xạ cài đặt đúng thứ tự ưu tiên $C \times 9 // 5 + 32$ và xử lý số âm.
* **Chuẩn code thi đấu:** Đọc 1 số nguyên (kể cả âm), dùng chia nguyên an toàn, in số nguyên.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Một số nguyên $C$ ($-50 \le C \le 50$, chia hết cho $5$) nên $C \times 9$ luôn chia hết cho $5$.
* **Bản chất toán học:** Hàm bậc nhất $F = \frac{9C}{5} + 32$; vì tử số chia hết cho 5 nên dùng `//` cho kết quả nguyên exact.
* **Trường hợp biên (Edge Cases):**
  * Nhiệt độ âm nhỏ nhất $C = -50$ cho $F = -58$.
  * Điểm đặc biệt $C = -40$ cho $F = -40$ (hai thang trùng nhau).
  * Học sinh dễ viết `C * (9 // 5)` bằng `C * 1` vì chia trước nhân sau.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Theo quy tắc nhân chia trước cộng sau, máy tính thực hiện phép nào trong $C \times 9 // 5 + 32$ trước?
2. Vì sao không được viết `C * (9 // 5)`? $9 // 5$ bằng mấy?
3. Với $C = 30$ thì $30 \times 9$, chia $5$, cộng $32$ lần lượt cho số nào?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Đọc $C$, tính $(C \times 9) // 5 + 32$ từ trái sang phải, in kết quả $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Phép nhân $C \times 9$ luôn thực hiện trước phép chia cho $5$, giữ đúng quan hệ phân số $\frac{9C}{5}$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
30
```
* **Output:**
```text
86
```
* **Giải thích:** $30 \times 9 : 5 + 32 = 270 : 5 + 32 = 54 + 32 = 86$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `c` | `c = 30` | Nhiệt độ độ C |
| **2** | Tính `c * 9` | `270` | Tử số phân số |
| **3** | Chia `// 5` rồi `+ 32` | `54 + 32 = 86` | Nhiệt độ độ F |
| **4** | `print(86)` | Xuất kết quả | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, một biến nguyên trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Sai thứ tự ưu tiên:** Viết `c * (9 // 5) + 32` thành `c + 32` vì $9 // 5 = 1$.
2. **Dùng `/` ra số thực:** In `86.0` thay vì `86` gây sai khớp đáp án.
3. **Quên số âm:** Nghĩ nhiệt độ luôn dương nên bối rối khi `%`/`//` gặp số âm (may mắn đề cho chia hết nên an toàn).

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
c = int(input())
print(c * 9 // 5 + 32)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Đổi ngược từ độ F sang độ C với công thức $(F - 32) \times 5 : 9$.
* **Mở rộng 2:** Kiểm tra nhiệt độ nước đóng băng ($0$ độ C) và sôi ($100$ độ C) trên cả hai thang đo.
