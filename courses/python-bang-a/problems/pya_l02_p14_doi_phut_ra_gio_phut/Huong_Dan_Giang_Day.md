# Hướng Dẫn Giảng Dạy: Đổi Phút Ra Giờ Phút
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Thành thạo cặp đôi `//` và `%` với số chia 60 để đổi phút ra giờ phút (`PYA-L02-P14`).
* **Tư duy thuật toán:** Hiểu mối quan hệ $T = \text{giờ} \times 60 + \text{phút dư}$.
* **Chuẩn code thi đấu:** Đọc 1 số, in 2 số trên một dòng cách nhau dấu cách.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** $T$ ($0 \le T \le 10000$) là tổng số phút, số nguyên không âm.
* **Bản chất toán học:** $\text{giờ} = T // 60$, $\text{phút} = T \% 60$. Đây là phép chia nguyên cho 60.
* **Trường hợp biên (Edge Cases):**
  * $T = 0$: kết quả `0 0`.
  * $T < 60$: giờ bằng 0, ví dụ $T = 45 \to$ `0 45`.
  * $T$ chia hết cho 60: phút dư bằng 0, ví dụ $T = 120 \to$ `2 0`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Một giờ có bao nhiêu phút? Vậy 135 phút chứa được mấy giờ trọn vẹn?
2. Sau khi lấy ra các giờ trọn vẹn, phần còn lẻ tính bằng phép toán nào (`//` hay `%`)?
3. Nếu dùng phép `/` thì kết quả in ra thế nào? Vì sao máy chấm lại bắt lỗi?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Dùng công thức trực tiếp `T // 60` và `T % 60`, độ phức tạp $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Luôn giữ đúng đẳng thức $T = (T // 60) \times 60 + (T \% 60)$ với $0 \le T \% 60 < 60$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
135
```
* **Output:**
```text
2 15
```
* **Giải thích:** $135$ phút $= 2$ giờ trọn vẹn ($2 \times 60 = 120$ phút) và còn dư $135 - 120 = 15$ phút.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc tổng phút | `T = 135` | Khởi tạo đầu vào |
| **2** | Tính giờ | `135 // 60 = 2` | Được 2 giờ |
| **3** | Tính phút dư | `135 % 60 = 15` | Dư 15 phút |
| **4** | In kết quả | `print(2, 15)` | Đúng Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa yêu cầu giới hạn $1.0\text{s}$ của kỳ thi).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ tối thiểu, đảm bảo an toàn tuyệt đối trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Dùng `/` thay cho `//`:** `135 / 60 = 2.25` in ra số thực, sai định dạng giờ nguyên.
2. **In mỗi số một dòng:** Đề yêu cầu in trên một dòng `2 15`, in 2 dòng bị `Wrong Answer (WA)`.
3. **Quên ép kiểu:** Tính toán trực tiếp trên chuỗi từ `input()` gây lỗi `TypeError`.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
t = int(input())
print(t // 60, t % 60)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Đổi tổng số giây $S$ ra giờ, phút, giây (kết hợp `// 3600`, `% 3600`).
* **Mở rộng 2:** Đổi ngược lại từ giờ phút ra tổng phút để kiểm tra đẳng thức $T = H \times 60 + M$.
