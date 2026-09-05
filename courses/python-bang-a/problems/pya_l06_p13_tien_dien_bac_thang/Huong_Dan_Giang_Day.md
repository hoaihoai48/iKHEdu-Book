# Hướng Dẫn Giảng Dạy: Tiền Điện Bậc Thang
Chuyên đề: **Toán thực tế — Giá bậc thang có điều kiện**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Tiền Điện Bậc Thang** (`PYA-L03-P16`) bằng Python ở mức `Vận dụng`.
* **Tư duy thuật toán:** Rèn luyện phản xạ rẽ nhánh `if-else` theo ngưỡng $100$ số điện và cộng hai bậc giá.
* **Chuẩn code thi đấu:** Đọc 1 số, chia hai trường hợp, tính đúng tiền tới $3.2 \times 10^9$ đồng, in 1 dòng.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Một số tự nhiên $N$ ($1 \le N \le 10^6$); bậc 1 giá $2000$, bậc 2 giá $3500$.
* **Bản chất toán học:** Hàm từng khúc: $N \le 100 \Rightarrow 2000N$; $N > 100 \Rightarrow 200000 + 3500(N - 100)$.
* **Trường hợp biên (Edge Cases):**
  * Ngay ngưỡng: $N = 100$ cho $200000$; $N = 101$ cho $203500$.
  * Cực đại: $N = 10^6$ cho $3350000000$ đồng.
  * Học sinh dễ tính cả $N$ số theo giá bậc 2 hoặc quên trừ $100$.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. $100$ số đầu hết bao nhiêu tiền? Số điện thứ $101$ giá bao nhiêu?
2. Với $120$ số thì có mấy số tính giá rẻ, mấy số tính giá đắt?
3. Vì sao công thức bậc 2 phải viết $(N - 100)$ mà không phải $N$?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Rẽ nhánh theo $N \le 100$; nhánh rẻ nhân trực tiếp, nhánh đắt cộng $200000$ với phần vượt ngưỡng $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Mọi số điện từ 1 đến 100 luôn tính giá $2000$, mọi số từ 101 trở đi luôn tính giá $3500$, không số nào bị tính hai lần hay bỏ sót.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
120
```
* **Output:**
```text
270000
```
* **Giải thích:** $100 \times 2000 = 200000$; $20 \times 3500 = 70000$; tổng $270000$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `n` | `n = 120` | Tổng số điện đã dùng |
| **2** | Kiểm tra `n <= 100`? | `False` → nhánh bậc thang | $120 > 100$ |
| **3** | Tính `200000 + 20*3500` | `200000 + 70000` | Cộng hai bậc giá |
| **4** | `print(270000)` | Xuất kết quả | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, một phép so sánh và vài phép nhân, dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, một biến nguyên trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Quên trừ ngưỡng:** Viết `200000 + n * 3500` khiến 100 số đầu bị tính hai lần.
2. **Sai điều kiện biên:** Dùng `n < 100` thay vì `n <= 100` làm $N = 100$ rơi nhầm nhánh đắt.
3. **In kèm đơn vị:** Viết `print(tien, "dong")` gây `Wrong Answer (WA)`.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
n = int(input())
if n <= 100:
    print(n * 2000)
else:
    print(100 * 2000 + (n - 100) * 3500)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thêm bậc 3: từ số 201 trở đi giá $5000$ đồng một số.
* **Mở rộng 2:** Tính tiền taxi/cước điện thoại bậc thang tương tự và so sánh tổng tiền hai hộ gia đình.
