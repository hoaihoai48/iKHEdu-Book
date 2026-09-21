# Bài 11: ƯỚC SỐ, BỘI SỐ VÀ SỐ NGUYÊN TỐ

## 1. Bản Chất Toán Học Của Ước Số & Bội Số Trong Lập Trình

Trong số học, số nguyên dương $d$ được gọi là **ước số** của số nguyên dương $N$ (và $N$ là **bội số** của $d$) nếu $N$ chia hết cho $d$ mà không còn dư:
$$\text{Điều kiện trong Scratch: } < ((N) \text{ mod } (d)) = (0) >$$

- *Ví dụ:* Các ước số của $12$ là: $1, 2, 3, 4, 6, 12$ (tổng cộng 6 ước số).

---

## 2. Định Nghĩa Số Nguyên Tố & Thuật Toán Cơ Bản

**Số nguyên tố** là số tự nhiên lớn hơn 1 và **chỉ có đúng 2 ước số** là 1 và chính nó ($2, 3, 5, 7, 11, 13, 17, \dots$).
- Số $0$ và số $1$ **KHÔNG PHẢI** là số nguyên tố.
- Số $2$ là số nguyên tố chẵn duy nhất (và cũng là số nguyên tố nhỏ nhất).

### Cách 1: Thuật toán đếm ước (Duyệt trâu)
Cho biến $i$ chạy từ $1$ đến $N$, nếu $N \pmod i = 0$ thì tăng biến `dem_uoc` lên 1.
Sau vòng lặp: nếu `dem_uoc = 2` $\implies N$ là số nguyên tố!

---

## 3. Thuật Toán Tối Ưu Với Biến Cờ Dừng Sớm & Căn Bậc Hai $\sqrt{N}$

Khi $N$ lớn (ví dụ $N = 1000000$), việc cho vòng lặp chạy $1$ triệu lần sẽ làm chương trình Scratch chạy rất chậm. Ta áp dụng 2 nguyên lý toán học tối ưu đỉnh cao:

1. **Nguyên lý căn bậc hai:** Nếu $N$ có một ước số lớn hơn $\sqrt{N}$, thì chắc chắn nó phải có một ước số tương ứng nhỏ hơn $\sqrt{N}$. Do đó, ta chỉ cần kiểm tra các số $d$ thỏa mãn $d \times d \le N$!

2. **Nguyên lý dừng sớm bằng biến cờ:** Ngay khi phát hiện ra một số $d \ge 2$ chia hết cho $N$, ta khẳng định ngay $N$ là hợp số, lập tức đặt cờ `la_nguyen_to = 0` và dừng vòng lặp ngay lập tức!

![Thuật toán kiểm tra số nguyên tố tối ưu căn N](assets/rendered_blocks/l11_prime_check_vi.png)

---

## 4. Bảng Mô Phỏng Kiểm Tra Số $N = 37$ (Dry Run Table)

| Vòng lặp | Biến `d` | Kiểm tra điều kiện lặp `< d * d <= N >` | Kiểm tra chia hết `< N mod d = 0 >` | Biến cờ `la_nguyen_to` | Kết luận bước |
|:---:|:---:|:---:|:---:|:---:|---|
| *Khởi tạo* | $d = 2$ | $2 \times 2 = 4 \le 37$ $\to$ **ĐÚNG** | $37 \bmod 2 = 1 \ne 0$ | **$1$** | Không chia hết, tăng $d = 3$ |
| **Vòng 1** | $d = 3$ | $3 \times 3 = 9 \le 37$ $\to$ **ĐÚNG** | $37 \bmod 3 = 1 \ne 0$ | $1$ | Không chia hết, tăng $d = 4$ |
| **Vòng 2** | $d = 4$ | $4 \times 4 = 16 \le 37$ $\to$ **ĐÚNG** | $37 \bmod 4 = 1 \ne 0$ | $1$ | Không chia hết, tăng $d = 5$ |
| **Vòng 3** | $d = 5$ | $5 \times 5 = 25 \le 37$ $\to$ **ĐÚNG** | $37 \bmod 5 = 2 \ne 0$ | $1$ | Không chia hết, tăng $d = 6$ |
| **Vòng 4** | $d = 6$ | $6 \times 6 = 36 \le 37$ $\to$ **ĐÚNG** | $37 \bmod 6 = 1 \ne 0$ | $1$ | Không chia hết, tăng $d = 7$ |
| **Dừng** | $d = 7$ | $7 \times 7 = 49 > 37$ $\to$ **DỪNG** | — | **$1$** | Vòng lặp kết thúc |

$\implies$ Sau khi dừng, cờ `la_nguyen_to` vẫn giữ nguyên giá trị **$1$**. Kết luận: $37$ là số nguyên tố (in ra `YES`). Chỉ cần kiểm tra $5$ lần thay vì $37$ lần!

---

## 5. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên xử lý trường hợp đặc biệt $N < 2$**
> - *Hiện tượng:* Với $N = 1$ hoặc $N = 0$, nếu không chặn trước, chương trình sẽ kết luận nhầm $1$ là số nguyên tố!
> - *Khắc phục:* Luôn có khối kiểm tra đầu tiên: `nếu < N < 2 > thì đặt [la_nguyen_to v] thành 0`.

> **Bẫy 2: Chạy kiểm tra ước bắt đầu từ $d = 1$**
> - *Hậu quả:* Mọi số đều chia hết cho $1$ ($N \pmod 1 = 0$), nếu bắt đầu từ 1 thì cờ bị bật về 0 ngay lập tức, dẫn đến kết luận không có số nào là số nguyên tố!
> - *Khắc phục:* Biến chia `d` bắt buộc phải **khởi tạo từ số 2**.

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Điều kiện nào trong Scratch chứng tỏ số nguyên $d$ là một ước số của số nguyên $N$?**
   - A. `< ((N) mod (d)) = (0) >` *(Đáp án đúng)*
   - B. `< ((d) mod (N)) = (0) >`
   - C. `< ((N) / (d)) = (0) >`
   - D. `< N = d >`

2. **Số nguyên tố nhỏ nhất là số nào?**
   - A. 0
   - B. 1
   - C. 2 *(Đáp án đúng)*
   - D. 3

3. **Số nào sau đây KHÔNG PHẢI là số nguyên tố?**
   - A. 2
   - B. 3
   - C. 9 *(Đáp án đúng: 9 có 3 ước là 1, 3, 9)*
   - D. 11

4. **Để kiểm tra số $N$ có phải nguyên tố không, ta chỉ cần thử chia $N$ cho các số từ 2 đến:**
   - A. $N / 2$
   - B. Căn bậc hai của $N$ ($\sqrt{N}$) *(Đáp án đúng: d * d <= N)*
   - C. $N - 1$
   - D. 10

5. **Số 1 có phải là số nguyên tố không?**
   - A. Có
   - B. Không *(Đáp án đúng: vì số 1 chỉ có đúng 1 ước số)*
   - C. Tùy từng trường hợp
   - D. Là số nguyên tố đặc biệt

6. **Số lượng ước số của số 12 là bao nhiêu?**
   - A. 4
   - B. 5
   - C. 6 *(Đáp án đúng: 1, 2, 3, 4, 6, 12)*
   - D. 7

7. **Khi kiểm tra tính nguyên tố của $N = 100$, chỉ cần thử các ước số $d$ tối đa đến số mấy?**
   - A. 10 *(Đáp án đúng: vì 10 * 10 = 100)*
   - B. 50
   - C. 99
   - D. 20

8. **Một số nguyên dương lớn hơn 1 không phải là số nguyên tố thì được gọi là:**
   - A. Số chẵn
   - B. Số lẻ
   - C. Hợp số *(Đáp án đúng)*
   - D. Số hoàn hảo

9. **Nếu số $N$ chia hết cho biến $d$ ($2 \le d < N$), ta có thể kết luận ngay $N$ là:**
   - A. Số nguyên tố
   - B. Hợp số *(Đáp án đúng: vì đã tìm thấy thêm ước thứ 3)*
   - C. Số chính phương
   - D. Số âm

10. **Cặp số nguyên tố nào sau đây được gọi là số nguyên tố sinh đôi (Twin Primes - hơn kém nhau 2 đơn vị)?**
    - A. 2 và 3
    - B. 3 và 5 *(Đáp án đúng)*
    - C. 7 và 11
    - D. 9 và 11
