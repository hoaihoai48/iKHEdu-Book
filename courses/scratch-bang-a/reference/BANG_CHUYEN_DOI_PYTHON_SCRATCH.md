# BẢNG ĐỐI CHIẾU CHUYỂN GIAO THUẬT TOÁN: PYTHON → SCRATCH

> Căn cứ: [`docs/LO_TRINH_SCRATCH.md`](file:///Users/vu/Developer/ikhEdu_lessons/docs/LO_TRINH_SCRATCH.md) (Mục 2).
> Tài liệu này quy định **12 phép biến đổi kinh điển** khi chuyển giao các bài toán thuật toán từ Python sang Scratch 3.0.

---

| # | Thao tác lập trình | Python 3 | Scratch 3.0 (DSL Text) | Tử huyệt & Bẫy lỗi sư phạm |
|:---:|---|---|---|---|
| **1** | **Nhập dữ liệu (Input)** | `x = int(input())` | `ask [Nhap x:] and wait`<br>`set [x v] to (answer)` | **Bẫy ghi đè `answer`:** Câu lệnh `ask` mới sẽ xóa ngay kết quả của câu `ask` trước đó. Học sinh **bắt buộc phải `set` giá trị vào biến số ngay lập tức** sau mỗi câu hỏi. |
| **2** | **Xuất dữ liệu 1 dòng** | `print("Tong:", s)` | `say (join [Tong: ] (s))` | **Bẫy dính chữ:** Khối `join` không tự động thêm dấu cách như dấu phẩy `,` trong Python. Bắt buộc thêm dấu cách thủ công sau nhãn (`join [Tong: ]`). Cấm dùng 2 lệnh `say` liên tiếp thay cho 1 dòng vì lệnh sau sẽ đè mất lệnh trước. |
| **3** | **Xuất nhiều dòng** | `print(a)`<br>`print(b)` | `say (a) for (2) secs`<br>`say (b) for (2) secs` | Dùng nhiều lệnh `say ... for ... secs` để học sinh kịp nhìn kết quả từng dòng. |
| **4** | **Hoán đổi 2 biến** | `a, b = b, a` | `set [tam v] to (a)`<br>`set [a v] to (b)`<br>`set [b v] to (tam)` | Scratch không có cơ chế tuple unpacking đồng thời như Python; bắt buộc sử dụng **biến phụ `tam`** để hoán đổi. |
| **5** | **Chia nguyên & Chia dư** | `a // b`<br>`a % b` | `([floor v] of ((a) / (b)))`<br>`((a) mod (b))` | Scratch không có toán tử `//` riêng; phép chia nguyên phải dùng hàm `floor` (làm tròn xuống) của phép chia thường `(a / b)`. Phép chia dư dùng toán tử `mod`. |
| **6** | **Lũy thừa nguyên** | `a ** 2`<br>`a ** 3` | `((a) * (a))`<br>`(((a) * (a)) * (a))` | Với số mũ nhỏ ($2, 3$), dùng phép nhân trực tiếp `a * a`. Với số mũ lớn, dùng vòng lặp nhân dồn. |
| **7** | **Làm tròn thập phân** | `round(x, 2)` | `((round ((x) * (100))) / (100))` | Nhân 100 $\to$ làm tròn về số nguyên $\to$ chia lại cho 100. Các bài toán yêu cầu ép in 2 chữ số thập phân (như `3.00`) được đơn giản hóa chấp nhận `3`. |
| **8** | **Vòng lặp xác định** | `for i in range(1, n+1):` | `set [i v] to [1]`<br>`repeat (n)`<br>`  ...`<br>`  change [i v] by (1)`<br>`end` | Phải khởi tạo biến đếm `i = 1` trước vòng lặp và đặt lệnh tăng biến `change i by 1` ở **cuối cùng** của thân vòng lặp `repeat`. |
| **9** | **Vòng lặp điều kiện** | `while condition:` | `repeat until <not <condition>>` | **Bẫy tư duy ngược:** Lệnh `while` chạy khi điều kiện **ĐÚNG**, còn lệnh `repeat until` lặp khi điều kiện **SAI** và chỉ dừng khi điều kiện **ĐÚNG**. Do đó điều kiện trong Scratch luôn là **phủ định logic** của Python. |
| **10** | **Truy cập phần tử mảng/danh sách** | `a[0]` (0-based) | `(item (1) of [a v])` (1-based) | **Bẫy lệch 1 đơn vị (Off-by-one):** Chỉ số danh sách trong Scratch bắt đầu từ **1**, không phải từ **0** như Python. Phần tử đầu tiên là `item 1`. |
| **11** | **Kích thước / Độ dài** | `len(lst)`<br>`len(s)` | `(length of [lst v])`<br>`(length of (s))` | Dùng khối `length of` cho cả danh sách và chuỗi ký tự. |
| **12** | **Ký tự trong chuỗi** | `s[i]` | `(letter (i) of (s))` | Lấy ký tự thứ `i` (chỉ số tính từ 1) của chuỗi `s`. |
