# Bài 07: VÒNG LẶP ĐẾM LẦN VÀ BIẾN ĐẾM THỦ CÔNG

## 1. Kỹ Thuật Lập Trình Vòng Lặp Đếm Lần Trong Scratch

Trong Scratch không có lệnh `for` tự động tăng biến như Python/C++. Ta xây dựng mô hình đếm tay chuẩn:

![Minh họa vòng lặp đếm lần có biến đếm](../../assets/rendered_blocks/l07_repeat_counter_vi.png)

### 1.1. Cấu trúc 3 bước vàng của vòng lặp có biến đếm
```text
đặt [i v] thành (1)            <-- BƯỚC 1: Khởi tạo giá trị bắt đầu
lặp lại (N) lần                 <-- BƯỚC 2: Số lần lặp
    // Xử lý công việc với i
    thay đổi [tong v] một lượng (i)
    thay đổi [i v] một lượng (1)   <-- BƯỚC 3: Tăng biến đếm ở cuối vòng lặp!
```

---

## 2. Mô Phỏng Từng Bước Tính Tổng $S = 1 + 2 + 3 + 4$ (Dry Run Table)

Với $N = 4$, vòng lặp `lặp lại 4 lần`:

| Vòng lặp số | Khối lệnh thực thi | Biến `i` | Biến `tong` | Ý nghĩa toán học |
|:---:|---|:---:|:---:|---|
| *Trước lặp* | `đặt [tong] thành 0`, `đặt [i] thành 1` | $1$ | $0$ | Khởi tạo ban đầu |
| **Vòng 1** | `cộng i vào tong`, `tăng i lên 1` | $1 \to 2$ | $0 + 1 = \mathbf{1}$ | Cộng số 1 |
| **Vòng 2** | `cộng i vào tong`, `tăng i lên 1` | $2 \to 3$ | $1 + 2 = \mathbf{3}$ | Cộng số 2 |
| **Vòng 3** | `cộng i vào tong`, `tăng i lên 1` | $3 \to 4$ | $3 + 3 = \mathbf{6}$ | Cộng số 3 |
| **Vòng 4** | `cộng i vào tong`, `tăng i lên 1` | $4 \to 5$ | $6 + 4 = \mathbf{10}$ | Cộng số 4 |
| *Sau lặp* | Thoát vòng lặp, nói biến `tong` | $5$ | **$10$** | Mèo nói: `10` |

---

## 3. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên khối `thay đổi [i v] một lượng (1)`**
> - *Hiện tượng:* Không cho biến `i` tăng sau mỗi vòng lặp.
> - *Hậu quả:* Biến `i` mãi mãi giữ giá trị $1$, dẫn đến tính tổng $1 + 1 + 1 + 1$ sai hoàn toàn!
> - *Khắc phục:* Luôn kiểm tra khối tăng biến `i` ở cuối thân vòng lặp.

> **Bẫy 2: Đặt khối khởi tạo `tong = 0` hoặc `i = 1` VÀO BÊN TRONG vòng lặp**
> - *Hiện tượng:* Kéo nhầm khối `đặt [tong] thành 0` vào trong vòng lặp `lặp lại`.
> - *Hậu quả:* Cứ mỗi lần lặp, tổng lại bị xóa về 0!
> - *Khắc phục:* Mọi khối chuẩn bị (khởi tạo biến ban đầu) **BẮT BUỘC ĐẶT Ở NGOÀI** trước khi vào vòng lặp.

> **Bẫy 3: Khởi tạo biến tích lũy phép nhân bằng 0**
> - *Hiện tượng:* Tính tích $P = 1 \times 2 \times \dots \times N$ mà đặt `tich = 0`.
> - *Hậu quả:* $0$ nhân với bất kỳ số nào cũng bằng $0$!
> - *Khắc phục:* Tính tổng bắt đầu từ $0$, tính tích (giai thừa) bắt đầu từ **$1$**.

---

## 4. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối lệnh nào trong Scratch tương đương với `range(n)`?**
   - A. `lặp lại (n) lần` *(Đáp án đúng)*
   - B. `lặp lại mãi mãi`
   - C. `nếu < > thì`
   - D. `đợi (n) giây`

2. **Muốn duyệt các số chẵn từ $2$ đến $20$, sau mỗi vòng lặp ta tăng biến `i` một lượng:**
   - A. `1`
   - B. `2` *(Đáp án đúng)*
   - C. `0`
   - D. `4`

3. **Khi tính tổng tích lũy $S = a_1 + a_2 + \dots$, biến $S$ phải được đặt giá trị ban đầu là:**
   - A. `1`
   - B. `0` *(Đáp án đúng)*
   - C. `10`
   - D. `Không cần đặt`

4. **Khi tính tích tích lũy $P = a_1 \times a_2 \times \dots$, biến $P$ phải được đặt giá trị ban đầu là:**
   - A. `0`
   - B. `1` *(Đáp án đúng)*
   - C. `-1`
   - D. `100`

5. **Nếu `lặp lại (5) lần` với `đặt i thành 1` và cuối mỗi vòng `thay đổi i một lượng 1`, sau khi thoát vòng lặp biến `i` có giá trị:**
   - A. `5`
   - B. `6` *(Đáp án đúng: vì ở vòng cuối i=5 được tăng lên 6 trước khi kết thúc)*
   - C. `4`
   - D. `1`

6. **Khối `thay đổi [biến] một lượng (-1)` có tác dụng gì?**
   - A. Giảm biến đi 1 đơn vị (đếm lùi) *(Đáp án đúng)*
   - B. Tăng biến lên 1
   - C. Đặt biến bằng -1
   - D. Xóa biến

7. **Vị trí đúng của khối `thay đổi [i] một lượng 1` là:**
   - A. Phía trên vòng lặp
   - B. Ở dòng cuối cùng bên trong vòng lặp *(Đáp án đúng)*
   - C. Phía dưới vòng lặp
   - D. Đặt ở đâu cũng được

8. **Đoạn kịch bản: `lặp lại (10) lần: nói [A]` sẽ nói chữ A bao nhiêu lần?**
   - A. 9 lần
   - B. 10 lần *(Đáp án đúng)*
   - C. 11 lần
   - D. 1 lần

9. **Công thức tính nhanh tổng $1 + 2 + \dots + N$ không cần vòng lặp là:**
   - A. `N * (N + 1) / 2` *(Đáp án đúng)*
   - B. `N * N`
   - C. `N * (N - 1)`
   - D. `(N + 1) / 2`

10. **Khi lồng 2 vòng lặp: vòng ngoài lặp 3 lần, vòng trong lặp 4 lần. Tổng số lần thân vòng trong chạy là:**
    - A. 7 lần
    - B. 12 lần *(Đáp án đúng: 3 * 4 = 12)*
    - C. 4 lần
    - D. 3 lần
