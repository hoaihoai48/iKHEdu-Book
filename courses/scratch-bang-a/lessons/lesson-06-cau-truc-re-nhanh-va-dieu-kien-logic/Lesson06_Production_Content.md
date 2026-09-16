# Bài 06: CẤU TRÚC RẼ NHÁNH VÀ ĐIỀU KIỆN LOGIC

## 1. Các Khối Lệnh Rẽ Nhánh Trong Scratch 3.0

Trong nhóm **Điều khiển (Control)** màu vàng cam, Scratch cung cấp 2 khối bao quanh hình chữ C:

![Minh họa khối lệnh rẽ nhánh Tiếng Việt](../../assets/rendered_blocks/l06_branching_vi.png)

### 1.1. Cấu trúc rẽ nhánh khuyết: `nếu < > thì`
- Dùng khi chỉ cần can thiệp nếu gặp trường hợp đặc biệt.
- Nếu điều kiện lục giác trả về `Đúng` (True), máy tính sẽ chạy các khối lệnh kẹp giữa hai càng chữ C.
- Nếu điều kiện trả về `Sai` (False), máy tính bỏ qua và chạy tiếp các khối phía dưới.

### 1.2. Cấu trúc rẽ nhánh đủ: `nếu < > thì ... nếu không thì`
- Dùng khi bài toán có 2 con đường bắt buộc chọn 1:
  - Nếu điều kiện ĐÚNG: Chạy nhánh trên (`thì`).
  - Nếu điều kiện SAI: Chạy nhánh dưới (`nếu không thì`).
- Ví dụ kiểm tra số chẵn lẻ:
  - Nếu `((n) mod (2)) = (0)` thì nói `Số chẵn`
  - Nếu không thì nói `Số lẻ`

---

## 2. Các Toán Tử So Sánh & Ghép Điều Kiện Logic

Trong nhóm **Các phép toán (Operators)**:

| Khối lục giác Scratch | Tương đương toán học | Ý nghĩa | Ví dụ |
|:---:|:---:|---|---|
| `< (A) > (B) >` | $A > B$ | So sánh lớn hơn | `< (diem) > (5) >` |
| `< (A) < (B) >` | $A < B$ | So sánh nhỏ hơn | `< (tuoi) < (18) >` |
| `< (A) = (B) >` | $A = B$ | So sánh bằng *(chú ý chỉ 1 dấu `=`)* | `< ((n) mod (2)) = (0) >` |
| `< < > và < > >` | $\text{and}$ | Cả 2 cùng đúng | `< (a > 0) và (a < 100) >` |
| `< < > hoặc < > >` | $\text{or}$ | Một trong hai đúng | `< (thang = 1) hoặc (thang = 3) >` |
| `< không phải < > >` | $\text{not}$ | Phủ định điều kiện | `< không phải < (tuoi) < (6) > >` |

---

## 3. Kỹ Thuật Lồng Nhánh Tìm Số Lớn Nhất Trong 3 Số ($A, B, C$)

Để tìm giá trị lớn nhất `max` của 3 số, ta dùng kỹ thuật **"Đặt vương miện giả định"**:
1. Giả sử số đầu tiên lớn nhất: `đặt [max v] thành (A)`.
2. So sánh với $B$: `nếu < (B) > (max) > thì: đặt [max v] thành (B)`.
3. So sánh tiếp với $C$: `nếu < (C) > (max) > thì: đặt [max v] thành (C)`.
4. Cuối cùng, biến `max` chắc chắn giữ giá trị lớn nhất của cả 3 số!

---

## 4. Bẫy Lỗi Thường Gặp Khi Lập Trình Rẽ Nhánh (Bug Traps)

> **Bẫy 1: Dùng chuỗi khối `nếu...thì` độc lập thay vì `nếu...nếu không thì`**
> - *Hiện tượng:* Xếp 2 khối `nếu` cạnh nhau:
>   - `nếu < (diem) >= (5) > thì: nói [Đỗ]`
>   - `nếu < (diem) < (5) > thì: nói [Trượt]`
> - *Nguy cơ:* Nếu xử lý không cẩn thận các dấu so sánh (bỏ sót dấu `=` hoặc trùng cả hai), chương trình sẽ nói cả Đỗ lẫn Trượt!
> - *Khắc phục:* Luôn dùng cấu trúc đủ `nếu ... thì ... nếu không thì`.

> **Bẫy 2: Nhầm lẫn giữa `và` (AND) với `hoặc` (OR)**
> - *Ví dụ:* Điều kiện để một tam giác có 3 cạnh $a, b, c$ hợp lệ:
>   $$\text{ĐÚNG: } (a + b > c) \text{ VÀ } (b + c > a) \text{ VÀ } (c + a > b)$$
>   Nếu học sinh chọn khối `hoặc`, tam giác $1, 2, 100$ cũng bị coi là hợp lệ!

> **Bẫy 3: Viết điều kiện kép như toán học `3 < x < 10`**
> - Scratch **không cho phép** nhét 3 số vào 1 khối so sánh. Bắt buộc phải tách ra:
>   `< < (x) > (3) > và < (x) < (10) > >`

---

## 5. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối lệnh nào được thực hiện khi điều kiện trong `nếu < > thì` có giá trị SAI?**
   - A. Khối lệnh bên trong càng chữ C
   - B. Chương trình dừng lại
   - C. Bỏ qua và chạy tiếp khối lệnh ngay phía dưới *(Đáp án đúng)*
   - D. Báo lỗi đỏ

2. **Muốn kiểm tra số $N$ vừa chia hết cho 3 vừa chia hết cho 5, ta ghép:**
   - A. `< ((N mod 3) = 0) hoặc ((N mod 5) = 0) >`
   - B. `< ((N mod 3) = 0) và ((N mod 5) = 0) >` *(Đáp án đúng)*
   - C. `< không phải < (N mod 15) = 0 > >`
   - D. `< (N mod 3) = (N mod 5) >`

3. **Khối `< không phải < (A) > (B) > >` tương đương với điều kiện nào sau đây?**
   - A. `< (A) < (B) >`
   - B. `< (A) = (B) >`
   - C. `< (A) nhỏ hơn hoặc bằng (B) >` *(Đáp án đúng)*
   - D. `< (A) khác (B) >`

4. **Cho $A = 7, B = 10$. Biểu thức `< (A > 5) và (B < 8) >` trả về:**
   - A. Đúng (True)
   - B. Sai (False) *(Đáp án đúng: vì B < 8 là Sai)*
   - C. 7
   - D. 10

5. **Để tìm số lớn hơn giữa hai số $A$ và $B$, ta dùng cấu trúc:**
   - A. `nếu < A > B > thì đặt max thành A, nếu không thì đặt max thành B` *(Đáp án đúng)*
   - B. `lặp lại A lần`
   - C. `đặt max thành A + B`
   - D. `nói A và B`

6. **Điều kiện nào kiểm tra 3 cạnh $a, b, c$ lập thành một tam giác?**
   - A. `(a + b > c) hoặc (b + c > a)`
   - B. `(a + b > c) và (b + c > a) và (a + c > b)` *(Đáp án đúng)*
   - C. `a = b = c`
   - D. `a + b + c > 0`

7. **Trong Scratch, dấu so sánh bằng là:**
   - A. `==`
   - B. `=` *(Đáp án đúng)*
   - C. `===`
   - D. `:=`

8. **Khi nào nhánh `nếu không thì` được thực thi?**
   - A. Khi điều kiện ở trên bị Sai *(Đáp án đúng)*
   - B. Khi điều kiện ở trên Đúng
   - C. Luôn luôn được thực thi
   - D. Khi người dùng bấm phím cách

9. **Kết quả của biểu thức `< (10 > 5) hoặc (3 > 8) >` là:**
   - A. Đúng (True) *(Đáp án đúng: chỉ cần 1 vế đúng)*
   - B. Sai (False)
   - C. Không xác định
   - D. Báo lỗi

10. **Một năm $Y$ là năm nhuận nếu:**
    - A. Chia hết cho 4 nhưng không chia hết cho 100, HOẶC chia hết cho 400 *(Đáp án đúng)*
    - B. Chỉ cần chia hết cho 4
    - C. Chia hết cho 100
    - D. Không chia hết cho 4
