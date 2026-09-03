# Bài 02: Phép toán số học, chia nguyên và chia dư

---

## 1. Khởi động: Chiếc máy tính bỏ túi siêu đẳng bên trong Python

Ở Bài 1, chúng ta đã biết cách tạo ra các "chiếc hộp biến số" và dùng lệnh `print()` để in kết quả. Nhưng một bạn Robot lập trình thì không thể chỉ biết đứng yên chào hỏi, bạn ấy phải là một **nhà toán học thiên tài**!

Trong cuộc sống hàng ngày, các em thường gặp rất nhiều bài toán thú vị:
* Có 17 chiếc kẹo chia đều cho 5 bạn, mỗi bạn được mấy cái và còn thừa mấy cái?
* Một đoàn vận động viên chạy vòng quanh sân vận động 400m, nếu chạy được 1500m thì đang dừng ở vị trí nào của vòng chạy?
* Cứ 4 năm lại có một năm nhuận, làm sao máy tính biết được năm 2028 có phải năm nhuận không?

Tất cả những bí mật này đều được giải quyết gọn gàng chỉ bằng **các phép toán số học trong Python**, đặc biệt là **bộ đôi quyền năng: Phép chia lấy nguyên (`//`) và Phép chia lấy dư (`%`)**!

---

## 2. Bảng tổng hợp 7 phép toán số học thần kỳ trong Python

Python cung cấp đầy đủ các phép tính từ quen thuộc đến các phép toán chuyên dụng cho lập trình thi đấu:

| Ký hiệu trong Python | Tên phép toán | Phép toán trong Toán học | Ví dụ code Python | Kết quả | Ý nghĩa bản chất |
|:---:|---|:---:|---|:---:|---|
| `+` | **Cộng** | $a + b$ | `12 + 5` | `17` | Tính tổng hai số |
| `-` | **Trừ** | $a - b$ | `12 - 5` | `7` | Tính hiệu hai số |
| `*` | **Nhân** | $a \times b$ | `12 * 5` | `60` | Dùng dấu sao `*`, không dùng chữ `x` |
| `/` | **Chia thực** | $a : b$ | `12 / 5` | `2.4` | **Luôn luôn trả về số thực (`float`)** |
| `//` | **Chia lấy phần nguyên** | $\lfloor a / b \rfloor$ | `12 // 5` | `2` | Bỏ hết phần thập phân, chỉ giữ lại số nguyên |
| `%` | **Chia lấy phần dư** | $a \bmod b$ | `12 % 5` | `2` | Lấy số dư còn lại sau khi chia nguyên |
| `**` | **Lũy thừa (Mũ)** | $a^b$ | `2 ** 3` | `8` | $2^3 = 2 \times 2 \times 2 = 8$ |

---

## 3. Khám phá chuyên sâu: Bộ đôi phép chia `//` và `%`

Đây là **vũ khí quan trọng nhất** trong các kỳ thi Tin học trẻ Tiểu học! Hãy cùng giải mã từng phép toán:

### 3.1. Phép chia lấy phần nguyên: `//` (double slash)
* Khi em lấy một số chia cho một số khác, phần nguyên cho biết: **Ta có thể chia được trọn vẹn bao nhiêu phần bằng nhau?**
* **Ví dụ:** Có 14 chiếc bánh pizza, xếp vào các hộp, mỗi hộp chứa được 4 chiếc bánh.
  * Phép tính: `14 // 4` cho kết quả là `3`.
  * Nghĩa là: Ta xếp được trọn vẹn **3 chiếc hộp đầy bánh**.

```python
so_banh = 14
banh_moi_hop = 4
so_hop_day = so_banh // banh_moi_hop
print("Số hộp xếp được là:", so_hop_day) # In ra 3
```

### 3.2. Phép chia lấy phần dư: `%` (modulo / mod)
* Phép chia dư `%` cho biết: **Sau khi đã chia đều hết mức có thể, còn dư lại (thừa ra) bao nhiêu phần tử chưa thể chia?**
* Tiếp tục với ví dụ 14 chiếc bánh pizza ở trên:
  * Đã xếp 3 hộp đầy (mất $3 \times 4 = 12$ chiếc bánh).
  * Số bánh còn thừa lại là: $14 - 12 = 2$ chiếc bánh.
  * Phép tính trong Python: `14 % 4` cho kết quả chính xác là `2`!

```python
banh_con_thua = so_banh % banh_moi_hop
print("Số bánh còn thừa là:", banh_con_thua) # In ra 2
```

> 🌟 **Công thức vàng của toán học Tiểu học được tái hiện trong Python:**
> $$\text{Số bị chia } = \text{ Thương } \times \text{ Số chia } + \text{ Số dư}$$
> $$\mathbf{A} = (\mathbf{A} // \mathbf{B}) \times \mathbf{B} + (\mathbf{A} \% \mathbf{B})$$
> *Ví dụ kiểm tra lại:* $14 = (14 // 4) \times 4 + (14 \% 4) = 3 \times 4 + 2 = 12 + 2 = 14$ (Tuyệt đối chính xác!).

---

## 4. Bốn ứng dụng kỳ diệu của phép chia dư `%` trong đề thi Tin học trẻ

Tại sao các đề thi Tin học trẻ Bảng A lại xuất hiện phép `%` nhiều đến thế? Bởi vì nó giải quyết được 4 bài toán kinh điển:

### Ứng dụng 1: Kiểm tra tính chẵn lẻ
* Một số là **số chẵn** nếu số đó chia hết cho 2 (số dư bằng 0) $\implies$ `n % 2 == 0`.
* Một số là **số lẻ** nếu số đó chia cho 2 dư 1 $\implies$ `n % 2 == 1`.

### Ứng dụng 2: Kiểm tra tính chia hết
* Đề bài hỏi: *"Số $A$ có phải là bội số của số $B$ hay không?"*
* Câu trả lời: Nếu `A % B == 0` thì $A$ chia hết cho $B$.

### Ứng dụng 3: Bài toán chu kỳ vòng tròn (chạy bộ, đồng hồ, đèn tín hiệu)
* Đồng hồ có 12 giờ. Nếu bây giờ là 10 giờ, thì 5 giờ nữa là mấy giờ?
  * Học sinh ngây thơ tính: $10 + 5 = 15$ giờ (đồng hồ kim không có số 15!).
  * Lập trình viên Python tính: `(10 + 5) % 12 = 15 % 12 = 3` giờ chiều!
* Bài toán sân chạy vòng tròn: Một sân chạy dài 400m, bạn An chạy quãng đường $N$ mét. Sau khi chạy xong nhiều vòng, An đang cách điểm xuất phát bao xa?
  * Đáp án siêu tốc: `vi_tri = N % 400`.

### Ứng dụng 4: Kỹ thuật tách chữ số hàng đơn vị
* Muốn lấy chữ số cuối cùng của số $2026$, ta làm thế nào?
  * Chỉ cần lấy số đó chia dư cho 10: `2026 % 10` cho kết quả ngay lập tức là `6`!
  * Muốn bỏ chữ số cuối cùng đi, chỉ giữ lại phần đằng trước: `2026 // 10` cho kết quả là `202`!
  *(Đây là chìa khóa vàng cho toàn bộ Chương 4 sau này!)*

---

## 5. Thứ tự ưu tiên của các phép toán (quy tắc pemdas)

Cũng giống như môn Toán ở trường Tiểu học, máy tính tuân thủ quy tắc ưu tiên nghiêm ngặt từ trái sang phải:

$$\text{Ngoặc tròn } () \longrightarrow \text{Lũy thừa } ** \longrightarrow \text{Nhân, Chia } (*, /, //, \%) \longrightarrow \text{Cộng, Trừ } (+, -)$$

**Ví dụ phân tích từng bước:**
```python
ket_qua = 2 + 3 * 4 ** 2
```
* **Bước 1 (Ưu tiên cao nhất):** Tính lũy thừa $4 ** 2 = 16$.
* **Bước 2:** Tính phép nhân $3 * 16 = 48$.
* **Bước 3:** Tính phép cộng $2 + 48 = 50$.
* Kết quả in ra là `50`. Nếu muốn máy tính cộng trước, em bắt buộc phải dùng ngoặc tròn: `(2 + 3) * 4 ** 2 = 5 * 16 = 80`.

---

## 6. Phân tích bẫy lỗi kinh điển bài 2

| Lỗi phổ biến | Hiện tượng | Nguyên nhân | Cách khắc phục |
|---|---|---|---|
| `ZeroDivisionError: division by zero` | Chương trình dừng đột ngột (Crash) | Chia cho số 0 (Ví dụ: `10 / 0` hoặc `10 % 0`) | Không bao giờ được để mẫu số chia bằng 0! |
| Dùng nhầm `/` thay vì `//` | Kết quả ra `3.0` thay vì `3` | Phép `/` luôn tạo ra số thực (`float`), khi in ra sẽ dính đuôi `.0` không đúng yêu cầu số nguyên | Dùng phép `//` để nhận kết quả số nguyên chuẩn |
| Nhầm dấu nhân `x` | `SyntaxError: invalid syntax` | Trong Python, phép nhân bắt buộc phải là dấu sao `*`, không dùng chữ cái `x` hay `X` | Đổi `a x b` thành `a * b` |
| Quên ngoặc khi tính trung bình cộng | `a + b / 2` tính sai | Máy tính sẽ chia `b / 2` trước rồi mới cộng `a` | Phải viết có ngoặc: `(a + b) / 2` |

---

## 7. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (nhận diện phép toán):
Trong Python, ký hiệu nào sau đây dùng để thực hiện phép chia lấy phần nguyên?
- **A.** `/`
- **B.** **[Đáp án đúng]** `//`
- **C.** `%`
- **D.** `\`
> *Giải thích:* Ký hiệu `//` là phép chia lấy phần nguyên. Ký hiệu `/` là chia thực, còn `%` là chia lấy phần dư.

#### Câu 2 (dự đoán output — chia nguyên):
Kết quả của biểu thức `19 // 4` trong Python là bao nhiêu?
- **A.** `4.75`
- **B.** **[Đáp án đúng]** `4`
- **C.** `3`
- **D.** `5`
> *Giải thích:* $19 : 4 = 4$ dư $3$. Phép `//` chỉ lấy phần nguyên là $4$.

#### Câu 3 (dự đoán output — chia dư):
Kết quả của biểu thức `19 % 4` trong Python là bao nhiêu?
- **A.** `4`
- **B.** **[Đáp án đúng]** `3`
- **C.** `0.75`
- **D.** `1`
> *Giải thích:* $19 : 4 = 4$ dư $3$. Phép `%` lấy số dư là $3$.

#### Câu 4 (bắt bẫy kiểu dữ liệu của phép chia `/`):
Kết quả của phép tính `8 / 2` trong Python là gì?
- **A.** Số nguyên `4`
- **B.** **[Đáp án đúng]** Số thực `4.0`
- **C.** Chuỗi `"4"`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Trong Python 3, phép chia đơn `/` luôn luôn trả về kiểu số thực (`float`), dù phép chia đó có chia hết hay không.

#### Câu 5 (ứng dụng — lũy thừa):
Để tính $3^4$ ($3$ mũ $4 = 3 \times 3 \times 3 \times 3 = 81$), câu lệnh Python nào sau đây viết đúng?
- **A.** `3 ^ 4`
- **B.** **[Đáp án đúng]** `3 ** 4`
- **C.** `3 * 4`
- **D.** `pow = 3 * 4`
> *Giải thích:* Toán tử lũy thừa trong Python là hai dấu sao liền nhau `**`. Ký hiệu `^` trong Python là phép toán XOR trên bit, không phải phép tính lũy thừa!

#### Câu 6 (bắt bẫy thứ tự ưu tiên):
Giá trị của biểu thức `10 - 2 * 3 + 4` là:
- **A.** `28`
- **B.** **[Đáp án đúng]** `8`
- **C.** `0`
- **D.** `16`
> *Giải thích:* Nhân trước: $2 \times 3 = 6$. Sau đó tính từ trái sang phải: $10 - 6 + 4 = 4 + 4 = 8$.

#### Câu 7 (kiểm tra số chẵn lẻ):
Điều kiện nào sau đây dùng để kiểm tra số nguyên $N$ có phải là số chẵn hay không?
- **A.** `N // 2 == 0`
- **B.** **[Đáp án đúng]** `N % 2 == 0`
- **C.** `N / 2 == 0`
- **D.** `N % 2 == 1`
> *Giải thích:* Số chẵn là số chia hết cho 2, nghĩa là số dư khi chia cho 2 phải bằng 0 (`N % 2 == 0`).

#### Câu 8 (tách chữ số cuối cùng):
Làm thế nào để lấy ra chữ số hàng đơn vị của một số nguyên dương $A = 987$?
- **A.** `A // 10`
- **B.** `A / 10`
- **C.** **[Đáp án đúng]** `A % 10`
- **D.** `A % 100`
> *Giải thích:* $987 \% 10 = 7$, đây chính là chữ số hàng đơn vị. Còn $987 // 10 = 98$ là phần số đứng trước.

#### Câu 9 (nhận diện lỗi crash — zerodivisionerror):
Câu lệnh nào sau đây sẽ khiến chương trình bị dừng ngay lập tức do lỗi `ZeroDivisionError`?
- **A.** `print(0 / 5)`
- **B.** `print(0 // 5)`
- **C.** **[Đáp án đúng]** `print(5 % 0)`
- **D.** `print(5 ** 0)`
> *Giải thích:* Không có phép chia cho số 0 trong toán học và lập trình. Biểu thức `5 % 0` chia cho 0 nên gây lỗi nghiêm trọng. Còn `0 / 5 = 0.0` và `5 ** 0 = 1` hoàn toàn hợp lệ.

#### Câu 10 (ứng dụng — chia kẹo):
Cô giáo có $M$ cái kẹo chia đều cho $K$ học sinh. Số kẹo còn thừa lại không đủ chia đều cho các bạn được tính bằng công thức nào?
- **A.** `M // K`
- **B.** **[Đáp án đúng]** `M % K`
- **C.** `M / K`
- **D.** `M - K`
> *Giải thích:* Số kẹo dư thừa sau khi chia đều chính là phần dư của phép chia: `M % K`.

#### Câu 11 (bắt bẫy biểu thức trung bình cộng):
Để tính trung bình cộng của 3 số nguyên $a, b, c$, cách viết nào sau đây là **CHÍNH XÁC**?
- **A.** `tbc = a + b + c / 3`
- **B.** **[Đáp án đúng]** `tbc = (a + b + c) / 3`
- **C.** `tbc = (a + b + c) // 3`
- **D.** `tbc = a + (b + c) / 3`
> *Giải thích:* Phải dùng ngoặc `(a + b + c)` để tính tổng 3 số trước rồi mới chia cho 3. Phép `/` cho giá trị trung bình chính xác (kể cả khi ra số thập phân).

#### Câu 12 (dự đoán output — chia số âm):
Trong Python, kết quả của biểu thức `-7 // 2` là bao nhiêu?
- **A.** `-3`
- **B.** **[Đáp án đúng]** `-4`
- **C.** `-3.5`
- **D.** `3`
> *Giải thích:* Phép chia nguyên `//` trong Python làm tròn xuống số nguyên nhỏ hơn gần nhất (Floor division). Vì $-3.5$ nằm giữa $-4$ và $-3$, số nguyên nhỏ hơn là $-4$.

#### Câu 13 (đảo ngược số chục):
Cho số có 2 chữ số $N = 83$. Biểu thức nào sau đây cho kết quả là số đảo ngược $38$?
- **A.** `(N % 10) + (N // 10)`
- **B.** **[Đáp án đúng]** `(N % 10) * 10 + (N // 10)`
- **C.** `(N // 10) * 10 + (N % 10)`
- **D.** `N % 10 * N // 10`
> *Giải thích:* Chữ số hàng đơn vị là $N \% 10 = 3$. Chữ số hàng chục là $N // 10 = 8$. Để tạo thành số $38$, ta lấy hàng đơn vị nhân 10 cộng hàng chục: $3 \times 10 + 8 = 38$.

#### Câu 14 (chu kỳ thời gian):
Một trận bóng đá bắt đầu lúc $H$ giờ và kéo dài đúng 15 giờ liên tục. Giờ kết thúc theo đồng hồ 24 giờ được tính theo công thức:
- **A.** `H + 15`
- **B.** **[Đáp án đúng]** `(H + 15) % 24`
- **C.** `(H + 15) // 24`
- **D.** `24 - (H + 15)`
> *Giải thích:* Một ngày có 24 giờ, khi thời gian vượt qua 24 giờ thì đồng hồ quay lại từ 0, do đó ta lấy phần dư cho 24: `(H + 15) % 24`.

#### Câu 15 (số lớn không giới hạn trong Python):
Điều gì xảy ra khi bạn tính `2 ** 100` trong Python?
- **A.** Bị lỗi tràn số (Overflow Error) giống C++ 32-bit.
- **B.** **[Đáp án đúng]** Python tính toán chính xác ra một con số khổng lồ gồm hơn 30 chữ số.
- **C.** Máy tính bị đơ và treo máy.
- **D.** Trả về kết quả `Infinity`.
> *Giải thích:* Đây là đặc sản của Python! Python tự động hỗ trợ tính toán số nguyên lớn vô hạn (Arbitrary-precision arithmetic), không bao giờ lo bị tràn số như kiểu `int` trong các ngôn ngữ khác.
