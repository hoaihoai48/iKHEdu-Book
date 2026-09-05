# Hướng Dẫn Giảng Dạy: Chia Kẹo Học Sinh
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Chia Kẹo Học Sinh** bằng Python 3.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích đề bài, nhận diện dạng dữ liệu, xây dựng cấu trúc tính toán tối ưu.
* **Chuẩn code thi đấu:** Cài đặt code Python 3 chuẩn thi đấu lập trình Python (trong sáng, an toàn, không thừa ký tự).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Đọc hiểu phạm vi các biến số đầu vào và kiểu dữ liệu phù hợp.
* **Bản chất toán học:** Thiết lập biểu thức toán học tương ứng.
* **Trường hợp biên (Edge Cases):** Giá trị cực tiểu, cực đại trong giới hạn đề bài.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Dữ liệu đầu vào của bài toán thuộc kiểu dữ liệu gì (`int`, `float`, `str`)?
2. Cần sử dụng toán tử nào để tính ra đáp án?
3. Bẫy lỗi nào mà học sinh hay mắc phải ở bài toán này?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Áp dụng công thức trực tiếp $\mathcal{O}(1)$.
* **Bất biến thuật toán:** Trạng thái của các biến số luôn bảo toàn đúng quan hệ toán học sau mỗi bước gán.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
| Bước | Hành Động | Trạng Thái Biến | Kết Quả Trung Gian |
| :---: | :--- | :--- | :--- |
| **1** | Nhập dữ liệu đầu vào | Đọc từ bàn phím qua `input()` | Khởi tạo giá trị ban đầu |
| **2** | Thực thi thuật toán | Áp dụng công thức toán học | Cập nhật biến kết quả |
| **3** | Xuất kết quả | Gọi hàm `print()` định dạng chuẩn | In chính xác kết quả đầu ra |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$, chạy tức thì dưới $0.05\text{s}$.
* **Không gian (Space Complexity):** $\mathcal{O}(1)$, bộ nhớ tối thiểu an toàn trong $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. In thừa thông báo giải thích dẫn đến bị máy chấm bắt lỗi `Wrong Answer (WA)`.
2. Quên ép kiểu chuỗi sang số nguyên hoặc số thực.
3. Thiếu dấu ngoặc trong biểu thức phân số.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
n, k = map(int, input().split())
print(n // k)
print(n % k)
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Áp dụng bài toán này để giải quyết các bài toán thực tế tương tự trong các đề thi lập trình các năm trước.
