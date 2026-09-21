# Bài 08: Vòng lặp while và biến cờ

## 1. Bản Chất Vòng Lặp Khi Chưa Biết Trước Số Lần Lặp

Trong nhiều bài toán thực tế, ta **không thể biết trước được công việc cần lặp lại chính xác bao nhiêu lần**:

- *Ví dụ 1:* Bác thợ mộc cưa một khúc gỗ dài $N$ mét cho đến khi độ dài còn lại nhỏ hơn $1$ mét.
- *Ví dụ 2:* Nhập mật khẩu từ bàn phím cho đến khi người dùng nhập đúng thì thôi.
- *Ví dụ 3:* Bóc tách các chữ số của số nguyên $N$ cho đến khi số $N$ giảm về $0$.

Khi số lần lặp phụ thuộc vào một điều kiện động, khối lệnh chuẩn mực nhất trong Scratch là **`lặp lại cho đến khi <điều_kiện>`** (trong nhóm **Điều khiển** màu cam).

![Minh họa vòng lặp cho đến khi](assets/rendered_blocks/l08_repeat_until_vi.png)

---

## 2. Bẫy Ngược Logic Của Khối `lặp lại cho đến khi`

| Khối lệnh | Cơ chế kiểm tra điều kiện | Ý nghĩa hành động |
|:---:|---|---|
| `lặp lại cho đến khi <điều_kiện>` | **LẶP KHI ĐIỀU KIỆN SAI** | Điều kiện còn Sai thì còn lặp tiếp; **khi điều kiện trở thành ĐÚNG THÌ DỪNG LẠI NGAY**! |

> **BÍ QUYẾT XÁC ĐỊNH ĐIỀU KIỆN DỪNG:**
> - Hãy tự hỏi: *"Khi nào thì kịch bản này PHẢI DỪNG LẠI?"*
> - Ví dụ: Muốn trừ dần $N$ cho đến khi $N$ bằng 0 thì dừng $\implies$ Điều kiện đặt vào khối là `< (N) = (0) >`.
> - Nếu đặt nhầm điều kiện còn chạy (như `< (N) > (0) >`), chương trình sẽ dừng ngay từ bước đầu tiên và không lặp lần nào!

---

## 3. Các Mẫu Thuật Toán Vòng Lặp Điều Kiện Kinh Điển

### 3.1. Mẫu 1: Thuật toán Dãy số Collatz ($3n + 1$)
Bài toán: Cho số nguyên dương $N$. Nếu $N$ chẵn thì chia đôi $N = N / 2$; nếu $N$ lẻ thì biến đổi thành $N = 3N + 1$. Lặp lại quá trình này cho đến khi $N$ giảm về $1$.

![Thuật toán Collatz](assets/rendered_blocks/l08_collatz_vi.png)

### 3.2. Mẫu 2: Kỹ thuật Biến Cờ Dừng (Sentinel Flag)
Bài toán: Kiểm tra xem số $N$ có phải là số chính phương hay không ($N = i \times i$).
- Khởi tạo biến cờ: `đặt [tim_thay v] thành 0`.
- Cho `i` chạy từ 1, lặp lại cho đến khi **đã tìm thấy cờ** HOẶC **$i > N$**:

![Kỹ thuật biến cờ dừng sớm](assets/rendered_blocks/l08_sentinel_flag_vi.png)

---

## 4. Bảng Mô Phỏng Biến Đổi Collatz Với $N = 6$ (Dry Run Table)

| Vòng lặp | Giá trị $N$ hiện tại | Kiểm tra điều kiện dừng `< N = 1 >` | Kiểm tra chẵn/lẻ | Phép tính thực thi | Giá trị $N$ mới |
|:---:|:---:|:---:|:---:|---|:---:|
| *Bắt đầu* | **$6$** | $6 = 1$ $\to$ **SAI** (Lặp tiếp) | $6$ chẵn | $6 / 2 = \mathbf{3}$ | $3$ |
| **Vòng 1** | **$3$** | $3 = 1$ $\to$ **SAI** (Lặp tiếp) | $3$ lẻ | $3 \times 3 + 1 = \mathbf{10}$ | $10$ |
| **Vòng 2** | **$10$** | $10 = 1$ $\to$ **SAI** (Lặp tiếp) | $10$ chẵn | $10 / 2 = \mathbf{5}$ | $5$ |
| **Vòng 3** | **$5$** | $5 = 1$ $\to$ **SAI** (Lặp tiếp) | $5$ lẻ | $5 \times 3 + 1 = \mathbf{16}$ | $16$ |
| **Vòng 4** | **$16$** | $16 = 1$ $\to$ **SAI** (Lặp tiếp) | $16$ chẵn | $16 / 2 = \mathbf{8}$ | $8$ |
| **Vòng 5** | **$8$** | $8 = 1$ $\to$ **SAI** (Lặp tiếp) | $8$ chẵn | $8 / 2 = \mathbf{4}$ | $4$ |
| **Vòng 6** | **$4$** | $4 = 1$ $\to$ **SAI** (Lặp tiếp) | $4$ chẵn | $4 / 2 = \mathbf{2}$ | $2$ |
| **Vòng 7** | **$2$** | $2 = 1$ $\to$ **SAI** (Lặp tiếp) | $2$ chẵn | $2 / 2 = \mathbf{1}$ | $1$ |
| **Vòng 8** | **$1$** | $1 = 1$ $\to$ **ĐÚNG** (DỪNG NGAY) | — | Thoát vòng lặp | **$1$** |

$\implies$ Sau đúng 8 bước lặp, số $N$ chạm về 1 và vòng lặp kết thúc hoàn toàn.

---

## 5. Tử Huyệt & Các Bẫy Lỗi Kinh Điển (Bug Traps)

> **Bẫy 1: Treo đơ chương trình do Vòng lặp vô tận (Infinite Loop)**
> - *Hiện tượng:* Bên trong vòng lặp không có bất kỳ câu lệnh nào làm thay đổi điều kiện dừng.
> - *Hậu quả:* Điều kiện dừng mãi mãi là SAI, máy tính lặp đi lặp lại không có điểm dừng, trình duyệt bị treo cứng!
> - *Khắc phục:* Luôn đảm bảo có khối làm biến số tiến dần về phía điều kiện dừng.

> **Bẫy 2: Viết nhầm điều kiện dừng thành điều kiện chạy**
> - *Sai lầm:* Muốn lặp khi $N > 0$ nhưng lại viết `lặp lại cho đến khi < N > 0 >`.
> - *Hậu quả:* Ngay tại bước đầu tiên, vì $N$ đang lớn hơn 0 nên điều kiện trả về ĐÚNG, máy tính **không chạy vòng lặp lấy một lần nào**!

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối lệnh `lặp lại cho đến khi <>` sẽ dừng lại khi điều kiện lục giác bên trong trả về:**
   - A. Đúng (True) *(Đáp án đúng: gặp Đúng thì Dừng)*
   - B. Sai (False)
   - C. Bằng 0
   - D. Bằng 1

2. **Muốn thực hiện lặp khi biến $N$ còn lớn hơn 0, điều kiện trong khối `lặp lại cho đến khi` của Scratch phải là:**
   - A. `< (N) > (0) >`
   - B. `< (N) <= (0) >` hoặc `< (N) = (0) >` *(Đáp án đúng: phủ định của N > 0)*
   - C. `< (N) > (1) >`
   - D. `< không phải < (N) = (0) > >`

3. **Hiện tượng "Treo vòng lặp vô tận" xảy ra khi nào?**
   - A. Điều kiện dừng không bao giờ đạt được giá trị Đúng *(Đáp án đúng)*
   - B. Số lần lặp vượt quá 100 lần
   - C. Khởi tạo biến quá lớn
   - D. Dùng lệnh nói bên trong vòng lặp

4. **Kỹ thuật "Biến cờ dừng" thường được khởi tạo giá trị ban đầu là bao nhiêu để báo hiệu chưa tìm thấy?**
   - A. 0 *(Đáp án đúng)*
   - B. 1
   - C. 100
   - D. -1

5. **Trong thuật toán Collatz, quá trình biến đổi sẽ dừng lại khi số $N$ bằng mấy?**
   - A. 0
   - B. 1 *(Đáp án đúng)*
   - C. 2
   - D. 3

6. **Đoạn lệnh: `đặt [x v] thành 10`, `lặp lại cho đến khi < x = 0 > { thay đổi [x] một lượng (-2) }`. Số lần lặp được thực thi là:**
   - A. 4 lần
   - B. 5 lần *(Đáp án đúng: 10 -> 8 -> 6 -> 4 -> 2 -> 0)*
   - C. 10 lần
   - D. Vô tận

7. **Nếu viết `đặt [x v] thành 5`, `lặp lại cho đến khi < x > 0 > { thay đổi [x] một lượng (1) }`, điều gì sẽ xảy ra?**
   - A. Vòng lặp chạy 5 lần
   - B. Vòng lặp chạy vô tận
   - C. Vòng lặp không chạy lần nào cả *(Đáp án đúng: vì x = 5 > 0 ngay từ đầu)*
   - D. Báo lỗi

8. **Để đếm xem một số nguyên $N$ có bao nhiêu chữ số, mỗi lần lặp ta giảm $N$ đi 10 lần và dừng khi:**
   - A. `< (N) = (0) >` *(Đáp án đúng)*
   - B. `< (N) > (0) >`
   - C. `< (N) = (1) >`
   - D. `< (N) < (0) >`

9. **Khi kiểm tra một số có phải nguyên tố không, nếu phát hiện một ước số thì ta nên:**
   - A. Tiếp tục chạy hết vòng lặp
   - B. Bật biến cờ lên 0 và dừng sớm vòng lặp *(Đáp án đúng)*
   - C. Xóa biến
   - D. Báo lỗi

10. **Sự khác biệt cơ bản nhất giữa `lặp lại () lần` và `lặp lại cho đến khi <>` là:**
    - A. Một bên biết trước số lần lặp, một bên dừng theo điều kiện động *(Đáp án đúng)*
    - B. Một bên dùng số, một bên dùng chữ
    - C. Một bên chạy nhanh hơn
    - D. Không có sự khác biệt
