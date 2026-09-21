# Bài 07: Vòng lặp for và hàm range

## 1. Bản Chất Của Vòng Lặp Trong Khoa Học Máy Tính

Trong lập trình, có những công việc cần thực hiện lặp đi lặp lại hàng chục, hàng trăm, thậm chí hàng triệu lần (ví dụ: tính tổng các số từ 1 đến 1000, in bảng cửu chương, duyệt qua danh sách thí sinh). 

Nếu không có vòng lặp, con người sẽ phải ghép hàng nghìn khối lệnh thủ công. **Vòng lặp ra đời để giải phóng sức lao động**: ta chỉ cần lập trình công việc một lần và ra lệnh cho máy tính tự động lặp lại.

Khi đã **biết trước chính xác số lần lặp**, khối lệnh chuẩn mực nhất trong Scratch là **`lặp lại () lần`** kết hợp với **biến đếm thủ công (Manual Counter)**.

![Minh họa vòng lặp đếm lần có biến đếm](assets/rendered_blocks/l07_repeat_counter_vi.png)

---

## 2. Kỹ Thuật Thiết Lập Biến Đếm 3 Bước Vàng

Trong Scratch, khối `lặp lại () lần` chỉ lặp lại hành động mà không tự động tăng một biến đếm nào cả. Do đó, để quản lý số thứ tự các lần lặp, chúng ta áp dụng **Quy tắc 3 bước vàng**:

1. **Bước 1 — Khởi tạo giá trị bắt đầu (Initialization):** Đặt ở bên ngoài, ngay trước khi bước vào vòng lặp.
   `đặt [i v] thành (1)`

2. **Bước 2 — Xác định số lần lặp:** Thả số vòng cần chạy vào ô tròn của khối `lặp lại () lần`.

3. **Bước 3 — Tăng biến đếm (Increment):** Đặt ở **dòng cuối cùng bên trong vòng lặp** để chuẩn bị giá trị mới cho vòng kế tiếp.
   `thay đổi [i v] một lượng (1)`

---

## 3. Các Mẫu Thuật Toán Tích Lũy Kinh Điển

### 3.1. Mẫu 1: Thuật toán Tính Tổng tích lũy ($S = 1 + 2 + \dots + N$)
- Khởi tạo biến tổng bằng 0: `đặt [tong v] thành (0)`.
- Trong mỗi vòng lặp, cộng dồn giá trị của `i` vào `tong`:
  `thay đổi [tong v] một lượng (i)`.

![Thuật toán tính tổng tích lũy](assets/rendered_blocks/l07_accumulator_vi.png)

### 3.2. Mẫu 2: Thuật toán Tính Tích giai thừa ($N! = 1 \times 2 \times \dots \times N$)
- **BẮT BUỘC:** Khởi tạo biến tích lũy phép nhân bằng 1 (nếu khởi tạo bằng 0 thì mọi phép nhân đều bằng 0!).
- Trong mỗi vòng lặp, nhân dồn `i` vào biến `giai_thua`:
  `đặt [giai_thua v] thành ((giai_thua) * (i))`.

![Thuật toán tính tích giai thừa](assets/rendered_blocks/l07_factorial_vi.png)

---

## 4. Bảng Mô Phỏng Từng Bước Tính Tổng $S = 1 + 2 + 3 + 4$ ($N = 4$) (Dry Run Table)

| Vòng lặp số | Khối lệnh thực thi trong thân lặp | Biến `i` trước lặp | Biến `tong` sau cộng | Biến `i` sau khi tăng | Ý nghĩa phép toán |
|:---:|---|:---:|:---:|:---:|---|
| *Khởi tạo* | `đặt [tong] thành 0`, `đặt [i] thành 1` | — | **$0$** | **$1$** | Chuẩn bị trước vòng lặp |
| **Vòng 1** | `thay đổi [tong] một lượng (i)` $\to$ `tăng i` | $1$ | $0 + 1 = \mathbf{1}$ | $1 + 1 = \mathbf{2}$ | Cộng số 1 vào tổng |
| **Vòng 2** | `thay đổi [tong] một lượng (i)` $\to$ `tăng i` | $2$ | $1 + 2 = \mathbf{3}$ | $2 + 1 = \mathbf{3}$ | Cộng số 2 vào tổng |
| **Vòng 3** | `thay đổi [tong] một lượng (i)` $\to$ `tăng i` | $3$ | $3 + 3 = \mathbf{6}$ | $3 + 1 = \mathbf{4}$ | Cộng số 3 vào tổng |
| **Vòng 4** | `thay đổi [tong] một lượng (i)` $\to$ `tăng i` | $4$ | $6 + 4 = \mathbf{10}$ | $4 + 1 = \mathbf{5}$ | Cộng số 4 vào tổng |
| *Sau lặp* | Thoát khỏi vòng lặp, hiển thị kết quả | $5$ | **$10$** | — | Chú Mèo nói: `10` |

---

## 5. Tử Huyệt & Các Bẫy Lỗi Kinh Điển (Bug Traps)

> **Bẫy 1: Quên khối `thay đổi [i v] một lượng (1)`**
> - *Hiện tượng:* Biến `i` mãi mãi nhận giá trị $1$.
> - *Hậu quả:* Máy tính tính tổng $1 + 1 + 1 + 1$ thay vì $1 + 2 + 3 + 4$, kết quả sai lệch hoàn toàn!
> - *Khắc phục:* Luôn luôn kiểm tra bước 3 ở đáy vòng lặp.

> **Bẫy 2: Kéo nhầm khối `đặt [tong v] thành 0` VÀO TRONG vòng lặp**
> - *Hiện tượng:* Đặt lệnh khởi tạo bên trong miệng chữ C.
> - *Hậu quả:* Cứ mỗi vòng lặp mới, biến tổng lại bị xóa sạch về 0. Kết thúc vòng lặp, tổng chỉ bằng giá trị của vòng lặp cuối cùng!
> - *Khắc phục:* Mọi lệnh khởi tạo biến ban đầu **BẮT BUỘC ĐẶT Ở BÊN NGOÀI**.

> **Bẫy 3: Khởi tạo biến tích bằng 0**
> - *Hiện tượng:* `đặt [tich v] thành 0`.
> - *Hậu quả:* Số 0 nhân với bất kỳ số nào cũng bằng 0.

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối lệnh nào trong Scratch tương đương với vòng lặp biết trước số lần lặp?**
   - A. `lặp lại () lần` *(Đáp án đúng)*
   - B. `lặp lại liên tục`
   - C. `lặp lại cho đến khi <>`
   - D. `nếu <> thì`

2. **Để biến đếm `i` tăng dần sau mỗi vòng lặp, ta đặt khối lệnh nào ở cuối thân vòng lặp?**
   - A. `đặt [i v] thành (1)`
   - B. `thay đổi [i v] một lượng (1)` *(Đáp án đúng)*
   - C. `thay đổi [i v] một lượng (-1)`
   - D. `đặt [i v] thành (i)`

3. **Khi tính tổng tích lũy $S = 1 + 2 + \dots + N$, giá trị khởi tạo an toàn nhất cho biến `tong` trước khi vào vòng lặp là:**
   - A. 1
   - B. 0 *(Đáp án đúng)*
   - C. N
   - D. -1

4. **Khi tính tích lũy giai thừa $P = 1 \times 2 \times \dots \times N$, giá trị khởi tạo bắt buộc cho biến `tich` là:**
   - A. 0
   - B. 1 *(Đáp án đúng: vì nếu là 0 thì tích luôn bằng 0)*
   - C. 2
   - D. 10

5. **Nếu vòng lặp `lặp lại (5) lần` chạy xong, biến `i` bắt đầu từ 1 và mỗi vòng tăng 1, thì sau khi thoát khỏi vòng lặp, giá trị của `i` là:**
   - A. 4
   - B. 5
   - C. 6 *(Đáp án đúng: sau lần lặp thứ 5, i được tăng lên 6 rồi mới dừng)*
   - D. 0

6. **Đoạn lệnh: `đặt [tong v] thành 0`, lặp lại 3 lần `thay đổi [tong v] một lượng 5`. Kết quả của biến `tong` là:**
   - A. 5
   - B. 10
   - C. 15 *(Đáp án đúng: 5 * 3 = 15)*
   - D. 20

7. **Vị trí đúng của khối lệnh khởi tạo biến tích lũy ban đầu là ở đâu?**
   - A. Bên trong vòng lặp ở đầu thân lặp
   - B. Ngay phía trước khi bước vào vòng lặp *(Đáp án đúng)*
   - C. Ở cuối vòng lặp
   - D. Sau khi chương trình kết thúc

8. **Muốn lặp qua các số chẵn $2, 4, 6, 8, \dots$, ta khởi tạo `i = 2` và mỗi lần lặp thay đổi `i` một lượng:**
   - A. 1
   - B. 2 *(Đáp án đúng)*
   - C. 3
   - D. 4

9. **Nếu muốn đếm lùi từ 10 về 1, ta khởi tạo `i = 10` và sau mỗi lần lặp dùng khối:**
   - A. `thay đổi [i v] một lượng (1)`
   - B. `thay đổi [i v] một lượng (-1)` *(Đáp án đúng)*
   - C. `đặt [i v] thành (i - 1)`
   - D. Cả B và C đều đúng

10. **Khi cần đếm xem có bao nhiêu số chia hết cho 3 từ 1 đến N, mỗi khi gặp số thỏa mãn, ta dùng khối:**
    - A. `đặt [dem v] thành (1)`
    - B. `thay đổi [dem v] một lượng (1)` *(Đáp án đúng)*
    - C. `thay đổi [dem v] một lượng (3)`
    - D. `đặt [dem v] thành (dem + 3)`
