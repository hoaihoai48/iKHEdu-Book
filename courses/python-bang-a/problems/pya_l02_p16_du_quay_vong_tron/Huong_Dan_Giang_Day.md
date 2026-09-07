# Hướng Dẫn Giảng Dạy: Đu Quay Vòng Tròn
Chuyên đề: **Cỗ Máy Tính Toán & Bí Thuật Chia Dư**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Vận dụng tổng hợp `//` và `%` với chu kỳ $C$ thay đổi theo đầu vào (`PYA-L02-P16`).
* **Tư duy thuật toán:** Nhận diện dạng chu kỳ vòng tròn tổng quát: số vòng trọn $+$ phần dư.
* **Chuẩn code chuẩn:** Đọc 2 số lớn tới $10^9$, in 2 số trên một dòng, Python xử lý số lớn tức thì.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Trường hợp đặc biệt)
* **Phân tích tham số:** $N$ ($1 \le N \le 10^9$) là tổng thời gian, $C$ ($1 \le C \le 10^9$) là thời gian một vòng.
* **Bản chất toán học:** $\text{vòng} = N // C$, $\text{dư} = N \% C$. Luôn có $N = \text{vòng} \times C + \text{dư}$.
* **Trường hợp biên (Trường hợp đặc biệt):**
 * $N < C$: chưa đủ một vòng, kết quả `0 N`.
 * $N$ chia hết cho $C$: dư bằng 0, ví dụ $N = 120, C = 60 \to$ `2 0`.
 * $N, C$ tới $10^9$: Python vẫn tính chính xác, không tràn số.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Nếu một vòng mất 60 phút và bạn ngồi 250 phút thì đi được mấy vòng trọn? Còn lẻ mấy phút?
2. Phép toán nào cho biết số vòng trọn, phép nào cho biết số phút lẻ?
3. Làm sao kiểm tra lại đáp án của mình bằng công thức vàng $N = \text{vòng} \times C + \text{dư}$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Tính trực tiếp `N // C` và `N % C`, độ phức tạp $\mathcal{O}(1)$, không mô phỏng từng vòng quay.
* **Bất biến thuật toán (Invariant):**
 > Luôn bảo toàn $N = (N // C) \times C + (N \% C)$ với $0 \le N \% C < C$.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
250
60
```
* **Output:**
```text
4 10
```
* **Giải thích:** $250 = 4 \times 60 + 10$. Sóc Nâu đã đi được 4 vòng trọn vẹn và đang ở phút thứ 10 của vòng thứ năm.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc tổng thời gian | `N = 250` | Khởi tạo đầu vào |
| **2** | Đọc chu kỳ vòng | `C = 60` | Khởi tạo chu kỳ |
| **3** | Tính vòng và dư | `250 // 60 = 4`, `250 % 60 = 10` | Được cặp (4, 10) |
| **4** | In kết quả | `print(4, 10)` | Đúng Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa yêu cầu giới hạn $1.0\text{s}$ của kỳ thi).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$ bộ nhớ tối thiểu, đảm bảo an toàn tuyệt đối trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Cố định chu kỳ 100:** Copy công thức bài vòng chạy `N // 100` mà quên chu kỳ $C$ do người dùng nhập.
2. **Dùng `/` thay cho `//`:** In ra `4.166...` dạng số thực, sai định dạng số vòng nguyên.
3. **In thừa giải thích:** Viết `print("So vong:", ...)` thay vì chỉ in 2 số gây `kết quả sai`.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
n = int(input())
c = int(input())
print(n // c, n % c)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Đu quay quay ngược chiều âm hoặc thời gian $N$ cực lớn $10^{18}$ để thấy Python không tràn số.
* **Mở rộng 2:** Chuyển sang bài đồng hồ 12 giờ và sân chạy 400m để thấy cùng một bản chất chu kỳ $N \% C$.
