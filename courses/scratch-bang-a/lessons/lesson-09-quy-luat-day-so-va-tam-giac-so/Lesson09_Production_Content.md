# Bài 09: QUY LUẬT DÃY SỐ VÀ TAM GIÁC SỐ

## 1. Công Thức Quy Luật Dãy Số Cách Đều

Xét dãy số cách đều: $3, 7, 11, 15, 19, \dots$
- Số đầu tiên: $u_1 = 3$
- Khoảng cách giữa 2 số liên tiếp: $d = 4$
- Số hạng thứ $n$:
  $$u_n = 3 + (n - 1) \times 4$$
- Biểu thức Scratch:
  `((3) + (((n) - (1)) * (4)))`
> Không cần dùng vòng lặp, tính thẳng bằng 1 phép toán siêu nhanh!

---

## 2. Thuật Toán Sinh Dãy Fibonacci

Dãy số: $1, 1, 2, 3, 5, 8, 13, 21, \dots$

```text
đặt [f1 v] thành (1)
đặt [f2 v] thành (1)
lặp lại ((N) - (2)) lần
    đặt [f_moi v] thành ((f1) + (f2))
    đặt [f1 v] thành (f2)
    đặt [f2 v] thành (f_moi)
nói (f2)
```

---

## 3. Kỹ Thuật Hai Vòng Lặp Lồng Nhau In Tam Giác Sao

In tam giác có $H$ hàng, hàng thứ $r$ có $r$ ngôi sao `*`:
- Hàng 1: `*`
- Hàng 2: `**`
- Hàng 3: `***`

Quy trình ghép dòng:
```text
đặt [r v] thành (1)
lặp lại (H) lần
    đặt [dong v] thành []
    đặt [c v] thành (1)
    lặp lại (r) lần
        đặt [dong v] thành (kết hợp (dong) [*])
        thay đổi [c v] một lượng (1)
    nói (dong) trong (1) giây
    thay đổi [r v] một lượng (1)
```

---

## 4. Bẫy Lỗi Thường Gặp Khi Lập Trình Dãy Số (Bug Traps)

> **Bẫy 1: Quên khởi tạo lại dòng trước khi vào vòng lặp trong**
> - *Hiện tượng:* Đặt khối `đặt [dong] thành []` ở ngoài vòng lặp hàng.
> - *Hậu quả:* Các ngôi sao của hàng trước không bị xóa, hàng sau sẽ cộng dồn cả hàng trước tạo thành hình chữ nhật khổng lồ!
> - *Khắc phục:* Bắt buộc reset `dong = rỗng` ở đầu mỗi hàng mới.

> **Bẫy 2: Lệch 1 đơn vị công thức số hạng thứ N (Off-by-one)**
> - *Hiện tượng:* Viết công thức $u_n = u_1 + n \times d$.
> - *Hậu quả:* Với $n = 1$ sẽ ra $u_1 + d$ (thành số thứ 2 mất rồi!).
> - *Khắc phục:* Luôn là $(n - 1) \times d$.

---

## 5. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Số hạng thứ 10 của dãy số $2, 5, 8, 11\dots$ là bao nhiêu?**
   - A. 29 *(Đáp án đúng: 2 + (10 - 1)*3 = 29)*
   - B. 32
   - C. 26
   - D. 30

2. **Dãy Fibonacci bắt đầu bằng hai số $1, 1$. Số tiếp theo là:**
   - A. 2 *(Đáp án đúng)*
   - B. 3
   - C. 4
   - D. 0

3. **Khi in hình chữ nhật kích thước $M$ hàng và $N$ cột, vòng lặp ngoài chạy bao nhiêu lần?**
   - A. $M$ lần *(Đáp án đúng: quản lý số hàng)*
   - B. $N$ lần
   - C. $M \times N$ lần
   - D. 1 lần

4. **Biến `dong` tích lũy chuỗi ký tự ban đầu phải được gán:**
   - A. Chuỗi rỗng `[]` *(Đáp án đúng)*
   - B. Số 0
   - C. Dấu cách
   - D. `*`

5. **Để ghép thêm một ngôi sao vào biến `dong`, ta dùng:**
   - A. `đặt [dong] thành (kết hợp (dong) [*])` *(Đáp án đúng)*
   - B. `thay đổi [dong] một lượng (1)`
   - C. `đặt [dong] thành [*]`
   - D. `dong + *`

6. **Trong dãy số $1, 4, 9, 16, 25\dots$, số hạng thứ $N$ có công thức là:**
   - A. $N \times N$ *(Đáp án đúng: các số chính phương)*
   - B. $2N$
   - C. $N + 3$
   - D. $N \times 3$

7. **Khoảng cách giữa hai số liên tiếp trong dãy $10, 15, 20, 25$ là:**
   - A. 5 *(Đáp án đúng)*
   - B. 10
   - C. 15
   - D. 20

8. **Khi lồng 2 vòng lặp, vòng ngoài lặp 5 lần, vòng trong lặp 5 lần. Có tất cả bao nhiêu lần chạy vòng trong?**
   - A. 25 lần *(Đáp án đúng)*
   - B. 10 lần
   - C. 5 lần
   - D. 20 lần

9. **Tam giác số có hàng 1 là `1`, hàng 2 là `1 2`, hàng 3 là `1 2 3`. Số lượng số trên hàng $k$ là:**
   - A. $k$ số *(Đáp án đúng)*
   - B. $k - 1$ số
   - C. $2k$ số
   - D. Hằng số 3

10. **Tổng các số từ 1 đến 10 là:**
    - A. 55 *(Đáp án đúng)*
    - B. 50
    - C. 45
    - D. 100
