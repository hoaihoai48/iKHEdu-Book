# Hướng Dẫn Giảng Dạy: Dãy Số Bội Chung Của 3 Và 5 Đẹp Mắt
Chuyên đề: **Chiến Lược Giải Đề Thi lập trình Bảng A**

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Nắm vững và làm chủ kỹ thuật giải quyết bài toán **Dãy Số Bội Chung Của 3 Và 5 Đẹp Mắt** (`PYA-L18-P08`) bằng Python.
* **Tư duy thuật toán:** Rèn luyện phản xạ phân tích đề bài, nhận diện dạng dữ liệu, xây dựng cấu trúc điều khiển hoặc cấu trúc dữ liệu tối ưu, không lặp code thừa thãi.
* **Chuẩn code thi đấu:** Cài đặt code Python 3 chuẩn thi đấu lập trình Python (rõ ràng, chạy nhanh, xử lý vào/ra an toàn, không thừa ký tự ngoài luồng).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Đọc hiểu phạm vi các biến số đầu vào và kiểu dữ liệu phù hợp (chú ý số nguyên lớn, số thực làm tròn, chuỗi có khoảng trắng thừa).
* **Bản chất toán học:** Nhận diện công thức giải tích hoặc quy luật biến đổi trạng thái của bài toán.
* **Trường hợp biên (Edge Cases):**
  * Dữ liệu cực tiểu ($N = 0$, $N = 1$ hoặc số phần tử tối thiểu).
  * Các số âm, số 0 hoặc các số có giá trị bằng nhau.
  * Chuỗi rỗng hoặc chuỗi chỉ chứa ký tự đặc biệt.

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Dữ liệu đầu vào của bài toán thuộc kiểu dữ liệu gì (`int`, `float`, `str` hay `list`)? Cần ép kiểu như thế nào?
2. Có thể tính trực tiếp bằng công thức toán học $\mathcal{O}(1)$ được không, hay bắt buộc phải duyệt vòng lặp?
3. Bẫy lỗi nào mà các bạn học sinh hay mắc phải nhất ở bài toán này?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Mô phỏng chính xác luồng dữ liệu, sử dụng biến đếm tích lũy hoặc công thức tính trực tiếp để đạt độ phức tạp tối ưu.
* **Bất biến thuật toán (Invariant):**
  > Trạng thái của các biến số luôn bảo toàn đúng quan hệ toán học sau mỗi bước lặp hoặc sau mỗi lệnh rẽ nhánh điều kiện.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
7
```
* **Output:**
```text
15
```
* **Giải thích:** Số thứ 7 là 15.

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Nhập dữ liệu đầu vào | Đọc từ bàn phím qua `input()` | Khởi tạo giá trị ban đầu |
| **2** | Thực thi thuật toán | Áp dụng công thức / vòng lặp / rẽ nhánh | Cập nhật biến tích lũy / biến kết quả |
| **3** | Xuất kết quả | Gọi hàm `print()` định dạng chuẩn | In chính xác kết quả đầu ra |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$, đảm bảo chạy tức thì dưới $0.1\text{s}$ (vượt xa yêu cầu giới hạn $1.0\text{s}$ của kỳ thi).
* **Không gian (Space Complexity):** $\mathcal{O}(1)$ hoặc $\mathcal{O}(N)$ bộ nhớ tối thiểu, đảm bảo an toàn tuyệt đối trong ngưỡng $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **In thừa thông báo giải thích:** Viết `print("Ket qua la:", ans)` thay vì chỉ in đúng `ans` dẫn đến bị máy chấm bắt lỗi `Wrong Answer (WA)`.
2. **Quên ép kiểu:** Dùng trực tiếp giá trị chuỗi từ `input()` để tính toán số học dẫn đến lỗi `TypeError`.
3. **Tràn thời gian (TLE):** Dùng vòng lặp lồng nhau không cần thiết khi số $N$ lớn.

---

## 8. Mã Nguồn Tham Chiếu Python 3 Chuẩn Thi Đấu
```python
k = int(input().strip())
cnt = 0
cur = 1
while True:
    if cur % 3 == 0 or cur % 5 == 0:
        cnt += 1
        if cnt == k:
            print(cur)
            exit()
    cur += 1
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* **Mở rộng 1:** Thử thách học sinh giải bài toán khi số lượng truy vấn $Q$ lớn (yêu cầu tối ưu hóa công thức).
* **Mở rộng 2:** Áp dụng thuật toán này để giải quyết các bài toán thực tế tương tự trong đề thi lập trình các năm trước.
