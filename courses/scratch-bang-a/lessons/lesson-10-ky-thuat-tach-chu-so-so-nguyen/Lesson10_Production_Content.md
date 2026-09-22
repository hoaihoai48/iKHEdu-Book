# Bài 10: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while

## 1. Hai bước tách chữ số bằng phép toán

Trong các bài toán lập trình, xử lý các con số (tính tổng các chữ số, đếm số lượng chữ số chẵn/lẻ, kiểm tra số đối xứng, tạo số đảo ngược) là một trong những dạng đề bài kinh điển nhất.

Để "bóc tách" từng chữ số của một số nguyên $N$ từ phải qua trái mà không cần chuyển sang chuỗi văn bản, ta sử dụng **Bí thuật 2 bước số học**:

![Minh họa bóc tách chữ số Scratch Tiếng Việt](assets/rendered_blocks/l10_digit_extraction_vi.png)

### Bước 1 — Lấy chữ số tận cùng bên phải:
$$\text{chữ\_số} = N \pmod{10}$$
Khối lệnh Scratch:
`đặt [chu_so v] thành ((N) mod (10))`

- Ví dụ: $358 \pmod{10} = 8$.

### Bước 2 — Cắt bỏ chữ số cuối cùng để thu nhỏ số $N$:
$$N = \lfloor N / 10 \rfloor$$
Khối lệnh Scratch:
`đặt [N v] thành ([làm tròn xuống v] của ((N) / (10)))`

- Ví dụ: $\lfloor 358 / 10 \rfloor = 35$. Số $N$ từ 3 chữ số đã được thu gọn thành 2 chữ số!

---

## 2. Khung mẫu vòng lặp xử lý chữ số

Kết hợp bí thuật 2 bước với vòng lặp `lặp lại cho đến khi < (N) = (0) >`:

- Trước vòng lặp: chuẩn bị biến tích lũy (ví dụ: `tong_chu_so = 0`).

- Trong thân lặp:
  1. Tách chữ số cuối: `chu_so = N mod 10`.
  2. Xử lý bài toán với `chu_so` (cộng vào tổng, kiểm tra chẵn/lẻ...).
  3. Cắt bỏ chữ số cuối: `N = floor(N / 10)`.

- Khi $N = 0$: toàn bộ các chữ số đã được bóc tách xong, vòng lặp dừng tự động.

---

## 3. Thuật toán tạo số đảo ngược

Bài toán: Cho số nguyên dương $N = 1234$, hãy tạo ra số đảo ngược $4321$.

![Thuật toán tạo số đảo ngược](assets/rendered_blocks/l10_digit_reverse_vi.png)

### Cơ chế dồn hàng đơn vị thành hàng chục:
Mỗi khi bóc tách được một chữ số mới, ta nhân số đảo ngược hiện tại với $10$ rồi cộng thêm chữ số mới vào:
$$\text{dao\_nguoc} = \text{dao\_nguoc} \times 10 + \text{chu\_so}$$

- Ban đầu: `dao_nguoc = 0`.

- Lần 1: bóc số 4 $\implies 0 \times 10 + 4 = 4$.

- Lần 2: bóc số 3 $\implies 4 \times 10 + 3 = 43$.

- Lần 3: bóc số 2 $\implies 43 \times 10 + 2 = 432$.

- Lần 4: bóc số 1 $\implies 432 \times 10 + 1 = 4321$.

---

## 4. Bảng mô phỏng tách chữ số $N = 358$ (Dry run)

| Vòng lặp | $N$ trước bóc | Tách `chu_so = N mod 10` | Thu nhỏ `N = floor(N / 10)` | Cộng `tong = tong + chu_so` | Biến `dao_nguoc` | Kiểm tra dừng `< N = 0 >` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| *Bắt đầu* | **$358$** | — | — | $0$ | $0$ | $358 = 0$ $\to$ **SAI** |
| **Vòng 1** | $358$ | $358 \bmod 10 = \mathbf{8}$ | $\lfloor 358 / 10 \rfloor = \mathbf{35}$ | $0 + 8 = \mathbf{8}$ | $0 \times 10 + 8 = \mathbf{8}$ | $35 = 0$ $\to$ **SAI** |
| **Vòng 2** | $35$ | $35 \bmod 10 = \mathbf{5}$ | $\lfloor 35 / 10 \rfloor = \mathbf{3}$ | $8 + 5 = \mathbf{13}$ | $8 \times 10 + 5 = \mathbf{85}$ | $3 = 0$ $\to$ **SAI** |
| **Vòng 3** | $3$ | $3 \bmod 10 = \mathbf{3}$ | $\lfloor 3 / 10 \rfloor = \mathbf{0}$ | $13 + 3 = \mathbf{16}$ | $85 \times 10 + 3 = \mathbf{853}$ | $0 = 0$ $\to$ **ĐÚNG (DỪNG)** |

$\implies$ Sau 3 vòng lặp: Tổng các chữ số là **$16$**, số đảo ngược là **$853$**.

---

## 5. Các bẫy lỗi thường gặp (Bug Traps)

> **Bẫy 1: Làm mất giá trị gốc của số $N$ ban đầu**
> - *Hậu quả:* Quá trình bóc tách sẽ làm số $N$ giảm dần về $0$. Nếu đề bài yêu cầu so sánh số đảo ngược với số ban đầu (để kiểm tra số đối xứng / Palindrome), ta không còn giá trị gốc của $N$ nữa!
> - *Khắc phục:* Luôn sao lưu vào một biến nhớ tạm trước khi bóc tách: `đặt [goc v] thành (N)`.

> **Bẫy 2: Quên bước cắt bỏ chữ số cuối `N = floor(N / 10)`**
> - *Hậu quả:* Số $N$ không bao giờ giảm, vòng lặp trở thành vô tận và chương trình bị treo cứng!

---

## 6. Bộ câu hỏi trắc nghiệm củng cố (Concept Quizzes)

1. **Khối lệnh nào dùng để lấy ra chữ số hàng đơn vị của số nguyên dương $N$?**
   - A. `(N) / (10)`
   - B. `(N) mod (10)` *(Đáp án đúng)*
   - C. `[làm tròn xuống] của (N / 10)`
   - D. `(N) - (10)`

2. **Muốn cắt bỏ chữ số cuối cùng của số nguyên dương $N$, ta gán lại $N$ bằng:**
   - A. `(N) mod (10)`
   - B. `[làm tròn xuống v] của ((N) / (10))` *(Đáp án đúng)*
   - C. `(N) - (10)`
   - D. `(N) / (10)`

3. **Vòng lặp bóc tách chữ số chuẩn mực sẽ dừng lại khi biến $N$ bằng bao nhiêu?**
   - A. 1
   - B. 0 *(Đáp án đúng)*
   - C. 10
   - D. -1

4. **Cho $N = 407$. Sau lệnh `đặt [chu_so v] thành ((N) mod (10))`, biến `chu_so` có giá trị là:**
   - A. 4
   - B. 0
   - C. 7 *(Đáp án đúng)*
   - D. 40

5. **Để kiểm tra một số có phải là số đối xứng (Palindrome) hay không, ta so sánh số ban đầu với:**
   - A. Tổng các chữ số
   - B. Số đảo ngược của nó *(Đáp án đúng: ví dụ 121 đảo ngược vẫn là 121)*
   - C. Số lượng chữ số
   - D. Số chữ số chẵn

6. **Công thức dồn chữ số để tạo số đảo ngược là:**
   - A. `dao_nguoc = dao_nguoc + chu_so`
   - B. `dao_nguoc = dao_nguoc * 10 + chu_so` *(Đáp án đúng)*
   - C. `dao_nguoc = dao_nguoc * chu_so`
   - D. `dao_nguoc = chu_so * 10`

7. **Số $N = 2026$ có tổng các chữ số bằng bao nhiêu?**
   - A. 8
   - B. 10 *(Đáp án đúng: 2 + 0 + 2 + 6 = 10)*
   - C. 12
   - D. 14

8. **Để đếm xem số $N$ có bao nhiêu chữ số chẵn, sau khi tách `chu_so`, ta kiểm tra điều kiện:**
   - A. `< ((chu_so) mod (2)) = (0) >` *(Đáp án đúng)*
   - B. `< ((N) mod (2)) = (0) >`
   - C. `< chu_so > 2 >`
   - D. `< chu_so = 2 >`

9. **Tại sao cần tạo biến `goc = N` trước khi bước vào vòng lặp tách chữ số?**
   - A. Để chương trình chạy nhanh hơn
   - B. Vì biến N sẽ bị giảm về 0 sau vòng lặp, cần lưu lại để sử dụng sau này *(Đáp án đúng)*
   - C. Để Scratch không bị báo lỗi
   - D. Bắt buộc theo quy tắc Scratch

10. **Số nguyên nào sau đây là số đối xứng?**
    - A. 123
    - B. 1221 *(Đáp án đúng)*
    - C. 1231
    - D. 2026
