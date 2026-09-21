# Bài 09: QUY LUẬT DÃY SỐ VÀ TAM GIÁC SỐ

## 1. Bản Chất Các Bài Toán Quy Luật Dãy Số Trong Lập Trình

Khi lập trình, bài toán về dãy số xuất hiện với tần suất rất cao:

- **Dãy số cách đều (Cấp số cộng):** $1, 4, 7, 10, 13, \dots$ (mỗi số cách nhau khoảng cách $d$).
- **Dãy số Fibonacci:** $1, 1, 2, 3, 5, 8, 13, 21, \dots$ (số sau bằng tổng hai số liền trước).
- **Quy luật lũy tiến:** $1, 3, 6, 10, 15, \dots$ (khoảng cách tăng dần: $+2, +3, +4, +5$).

Thay vì học vẹt công thức, học sinh cần rèn luyện tư duy: **Xác định giá trị khởi đầu $\to$ Tìm quy luật chuyển đổi giữa 2 bước liên tiếp $\to$ Đưa vào vòng lặp**.

---

## 2. Kỹ Thuật Biến Lăn (Rolling Variables) — Thuật Toán Fibonacci

Để tính số Fibonacci thứ $N$, ta không cần lưu toàn bộ dãy số vào bộ nhớ mà chỉ cần duy trì đúng **hai biến nhớ liền kề (`a` và `b`)**:

- Ban đầu: `a = 1, b = 1`.
- Ở mỗi bước lặp:
  1. Tính số tiếp theo: `c = a + b`.
  2. Dịch chuyển ô nhớ: gán `a = b` và gán `b = c`.

![Thuật toán Fibonacci bằng biến lăn](assets/rendered_blocks/l09_fibonacci_vi.png)

---

## 3. Kỹ Thuật Hai Vòng Lặp Lồng Nhau — In Tam Giác Sao

Khi bài toán yêu cầu in hình dạng 2 chiều (ví dụ: tam giác sao, bảng cửu chương, ma trận ô số):

- **Vòng lặp ngoài (Outer Loop):** Điều khiển **Dòng** chạy từ $1$ đến $N$.
- **Vòng lặp trong (Inner Loop):** Điều khiển **Cột** (số lượng dấu sao trên dòng đó) chạy từ $1$ đến `dong`.

![Hai vòng lặp lồng nhau in tam giác sao](assets/rendered_blocks/l09_nested_triangle_vi.png)

### Cơ chế ghép chuỗi dòng:

- Đầu mỗi dòng: khởi tạo `dong_chu = ""` (chuỗi rỗng).
- Vòng lặp trong: cứ mỗi cột, nối thêm ký tự `*` vào dòng: `đặt [dong_chu v] thành (kết hợp (dong_chu) [*])`.
- Hết vòng lặp trong: nạp cả dòng hoàn chỉnh vào Danh sách hiển thị.

---

## 4. Bảng Mô Phỏng Từng Bước Dãy Fibonacci Đến $N = 6$ (Dry Run Table)

| Vòng lặp | Biến `a` (Số trước) | Biến `b` (Số hiện tại) | Tính `c = a + b` | Dịch `a = b` | Dịch `b = c` | Giá trị phần tử sinh ra |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *Khởi tạo* | **$1$** | **$1$** | — | — | — | Số thứ 1: $1$, Số thứ 2: $1$ |
| **Vòng 1** | $1$ | $1$ | $1 + 1 = \mathbf{2}$ | $a \leftarrow 1$ | $b \leftarrow \mathbf{2}$ | **Số thứ 3: $2$** |
| **Vòng 2** | $1$ | $2$ | $1 + 2 = \mathbf{3}$ | $a \leftarrow 2$ | $b \leftarrow \mathbf{3}$ | **Số thứ 4: $3$** |
| **Vòng 3** | $2$ | $3$ | $2 + 3 = \mathbf{5}$ | $a \leftarrow 3$ | $b \leftarrow \mathbf{5}$ | **Số thứ 5: $5$** |
| **Vòng 4** | $3$ | $5$ | $3 + 5 = \mathbf{8}$ | $a \leftarrow 5$ | $b \leftarrow \mathbf{8}$ | **Số thứ 6: $8$** |

$\implies$ Sau 4 lượt lặp (ứng với $N - 2$), biến `b` chứa chính xác số Fibonacci thứ 6 là **$8$**.

---

## 5. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Sai thứ tự dịch chuyển biến làm mất giá trị**
> - *Sai lầm:* `đặt [a v] thành (b)` trước rồi mới tính `c = a + b`.
> - *Hậu quả:* Lúc này `a` đã bị đè thành `b`, nên `c = b + b = 2b`, toàn bộ dãy số bị sai lệch!
> - *Khắc phục:* Phải tính số mới `c` trước, hoặc dùng biến tạm.

> **Bẫy 2: Quên làm sạch dòng chữ ở đầu mỗi dòng mới**
> - *Hiện tượng:* Không đặt `dong_chu = ""` trước vòng lặp trong.
> - *Hậu quả:* Dòng sau sẽ nối dài tiếp từ dòng trước, tam giác biến thành một dải dài vô tận!

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Số tiếp theo trong dãy số Fibonacci $1, 1, 2, 3, 5, 8, \dots$ là:**
   - A. 11
   - B. 12
   - C. 13 *(Đáp án đúng: 5 + 8 = 13)*
   - D. 15

2. **Để tính số Fibonacci thứ $N$ ($N \ge 3$), vòng lặp cần chạy bao nhiêu lần nếu đã khởi tạo 2 số đầu?**
   - A. $N$ lần
   - B. $N - 1$ lần
   - C. $N - 2$ lần *(Đáp án đúng)*
   - D. 2 lần

3. **Trong kỹ thuật in tam giác sao bằng hai vòng lặp lồng nhau, vòng lặp ngoài điều khiển:**
   - A. Số cột
   - B. Số dòng *(Đáp án đúng)*
   - C. Kích thước dấu sao
   - D. Màu sắc

4. **Khi in dòng thứ $i$ của tam giác vuông cân sao, vòng lặp bên trong cần lặp bao nhiêu lần?**
   - A. 1 lần
   - B. $i$ lần *(Đáp án đúng)*
   - C. $N$ lần
   - D. $i + 1$ lần

5. **Dãy số cách đều $3, 7, 11, 15, \dots$ có khoảng cách bước nhảy là:**
   - A. 3
   - B. 4 *(Đáp án đúng: 7 - 3 = 4)*
   - C. 5
   - D. 7

6. **Công thức toán học tính số hạng thứ $N$ của dãy cách đều có số đầu $u_1$ và khoảng cách $d$ là:**
   - A. $u_n = u_1 + N \times d$
   - B. $u_n = u_1 + (N - 1) \times d$ *(Đáp án đúng)*
   - C. $u_n = N \times d$
   - D. $u_n = u_1 \times d$

7. **Trước khi bắt đầu ghép các dấu sao cho một dòng mới, biến `dong_chu` cần được đặt thành:**
   - A. Dấu cách
   - B. Chuỗi rỗng `""` *(Đáp án đúng)*
   - C. Dấu sao `*`
   - D. Số 0

8. **Tổng của dãy số tự nhiên $S = 1 + 2 + 3 + \dots + N$ có công thức tính nhanh là:**
   - A. $N \times (N + 1) / 2$ *(Đáp án đúng)*
   - B. $N \times N / 2$
   - C. $(N + 1) / 2$
   - D. $N \times (N - 1) / 2$

9. **Nếu một tam giác sao có 5 dòng, tổng số dấu sao được in ra là:**
   - A. 10
   - B. 15 *(Đáp án đúng: 1 + 2 + 3 + 4 + 5 = 15)*
   - C. 20
   - D. 25

10. **Đặc điểm của biến lăn (Rolling Variables) là:**
    - A. Cần dùng rất nhiều biến
    - B. Chỉ cần số lượng biến cố định để tính trạng thái tiếp theo *(Đáp án đúng: tiết kiệm bộ nhớ)*
    - C. Không thể dùng trong Scratch
    - D. Luôn chạy chậm hơn
