# Hướng Dẫn Giảng Dạy: Diện Tích Tam Giác Vuông
Chuyên đề: **Công thức hình học — Diện tích tam giác**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Diện Tích Tam Giác Vuông** (`PYA-L03-P11`) bằng Python ở mức `Luyện tập`.
* **Tư duy thuật toán:** Rèn luyện phản xạ chuyển công thức $S = (a \times h) : 2$ thành code có ngoặc và phép chia nguyên an toàn.
* **Chuẩn code thi đấu:** Đọc 2 số bằng `input()`, ép kiểu `int`, chỉ in đúng 1 số, không in thừa.

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Hai số tự nhiên $a, h$ ($1 \le a, h \le 1000$), tích $a \times h$ luôn chẵn nên kết quả là số nguyên.
* **Bản chất toán học:** Diện tích tam giác vuông bằng nửa tích hai cạnh góc vuông.
* **Trường hợp biên (Edge Cases):**
  * Giá trị cực tiểu: $a = 1, h = 2$ cho kết quả $1$.
  * Giá trị cực đại: $a = h = 1000$ cho kết quả $500000$.
  * Học sinh dễ quên chia cho 2 hoặc dùng `/` ra số thực `12.0`.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Diện tích hình chữ nhật $a \times h$ là bao nhiêu? Tam giác vuông bằng mấy phần của hình chữ nhật đó?
2. Vì sao đề bài dặn tích $a \times h$ luôn chẵn? Nếu dùng `/` thì máy in ra gì khác `//`?
3. Nếu nhập $a = 6, h = 4$ thì từng dòng code cho ra số nào?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Đọc 2 số, tính trực tiếp $(a \times h) // 2$, in kết quả — công thức $\mathcal{O}(1)$.
* **Bất biến thuật toán (Invariant):**
  > Biến kết quả luôn bằng đúng $(a \times h) : 2$ sau lệnh tính, không bao giờ chứa giá trị chuỗi hay số thực dư `.0`.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
6
4
```
* **Output:**
```text
12
```
* **Giải thích:** Tích hai cạnh $6 \times 4 = 24$; diện tích $24 : 2 = 12$.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc `a` | `a = 6` | Khởi tạo cạnh thứ nhất |
| **2** | Đọc `h` | `h = 4` | Khởi tạo cạnh thứ hai |
| **3** | Tính `a * h // 2` | `6 * 4 // 2 = 12` | Diện tích nguyên |
| **4** | `print(12)` | Xuất ra màn hình | Khớp Sample Output |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.1\text{s}$ (vượt xa giới hạn $1.0\text{s}$).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, chỉ dùng 2 biến số nguyên trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **In thừa giải thích:** Viết `print("Dien tich:", ans)` thay vì chỉ `print(ans)` gây `Wrong Answer (WA)`.
2. **Quên ép kiểu:** Dùng `a = input()` rồi tính `a * h` tạo chuỗi lặp thay vì số học.
3. **Dùng `/` thay `//`:** In ra `12.0` thay vì `12`, máy chấm so khớp chuỗi sẽ trừ điểm.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
a = int(input())
h = int(input())
print(a * h // 2)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Tính diện tích tam giác thường khi biết đáy và chiều cao với kết quả làm tròn 1 chữ số thập phân.
* **Mở rộng 2:** Ghép 2 tam giác vuông thành hình chữ nhật và kiểm tra $S_{chữ nhật} = 2 \times S_{tam giác}$.
