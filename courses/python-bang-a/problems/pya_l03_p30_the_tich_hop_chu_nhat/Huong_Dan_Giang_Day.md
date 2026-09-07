# Hướng Dẫn Giảng Dạy: Thể Tích Hộp Chữ Nhật
Chuyên đề: **Công thức hình học không gian — Thể tích**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Thể Tích Hộp Chữ Nhật** (`PYA-L03-P12`) bằng Python ở mức `Luyện tập`.
* **Tư duy thuật toán:** Rèn luyện phản xạ mở rộng công thức diện tích 2D thành thể tích 3D $V = d \times r \times c$.
* **Chuẩn code chuẩn:** Đọc 3 dòng `input()` liên tiếp, nhân 3 số, in đúng 1 dòng.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Trường hợp đặc biệt)
* **Phân tích tham số:** Ba số tự nhiên $d, r, c$ ($1 \le d, r, c \le 1000$), tích tối đa $10^9$ vừa trong `int` Python.
* **Bản chất toán học:** Thể tích bằng diện tích đáy nhân chiều cao: $(d \times r) \times c$.
* **Trường hợp biên (Trường hợp đặc biệt):**
 * Hộp nhỏ nhất $1 \times 1 \times 1$ cho thể tích $1$.
 * Hộp lớn nhất $1000^3 = 10^9$.
 * Học sinh dễ nhập thiếu 1 cạnh hoặc nhân chỉ 2 số.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Diện tích mặt đáy $d \times r$ là bao nhiêu? Chồng các lớp cao $c$ lên thì nhân thêm gì?
2. Thứ tự nhập $d, r, c$ có quan trọng không? Vì sao phép nhân có tính giao hoán?
3. Với sample $5, 3, 2$ thì từng bước nhân cho ra số nào?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Đọc 3 số, tính trực tiếp $d \times r \times c$, in kết quả $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
 > Tích trung gian sau mỗi phép nhân luôn bằng thể tích của khối hộp từng phần, không đổi khi hoán đổi thứ tự nhân.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
5
3
2
```
* **Output:**
```text
30
```
* **Giải thích:** Thể tích $5 \times 3 \times 2 = 30$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `d, r, c` | `d=5, r=3, c=2` | Đủ 3 kích thước |
| **2** | Tính `d * r` | `5 * 3 = 15` | Diện tích đáy |
| **3** | Nhân tiếp `* c` | `15 * 2 = 30` | Thể tích khối hộp |
| **4** | `print(30)` | Xuất kết quả | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, chỉ 3 biến nguyên trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **In thừa giải thích:** `print("The tich:", v)` gây `kết quả sai`.
2. **Quên ép kiểu 1 dòng:** Cộng chuỗi `"5" * "3"` báo lỗi `TypeError`.
3. **Đọc sai số dòng:** Dùng 1 `input()` tách `split()` trong khi đề cho 3 dòng riêng.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
d = int(input())
r = int(input())
c = int(input())
print(d * r * c)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Tính thể tích hình lập phương cạnh $a$ và so sánh với hộp chữ nhật.
* **Mở rộng 2:** Cho thể tích và 2 cạnh, tìm cạnh còn lại bằng phép chia nguyên.
