# Bài 02: Phép toán số học, chia nguyên và chia dư

## 1. Kiến thức chuyên sâu dành cho học sinh Tiểu học
Python cung cấp 7 phép toán số học. Trong đó, bộ đôi **Chia lấy phần nguyên (`//`)** và **Chia lấy phần dư (`%`)** là nền tảng cốt lõi của mọi bài thi Tin học trẻ:

```
Phép chia: A : B  (Ví dụ: 17 chia cho 5)
17 = 5 x 3 + 2
       │     │
       │     └─► 17 % 5  = 2 (Số dư - Modulo)
       └───────► 17 // 5 = 3 (Thương nguyên - Floor Division)
```

### A. Phép chia thực (`/`)
- Ký hiệu một dấu gạch chéo `/`.
- **Đặc điểm sống còn:** Kết quả luôn luôn là số thực (`float`), kể cả khi chia hết. Ví dụ: `8 / 2` cho ra `4.0` chứ không phải `4`. Nếu đề bài yêu cầu in ra số nguyên, dùng `/` sẽ bị trừ điểm!

### B. Phép chia lấy phần nguyên (`//`)
- Ký hiệu hai dấu gạch chéo liền nhau `//`.
- **Ý nghĩa:** Trả lời câu hỏi *"Có thể chia được trọn vẹn bao nhiêu phần bằng nhau?"*.
- Bỏ hoàn toàn phần thập phân, chỉ giữ lại số nguyên: `19 // 4 = 4` (vì $19 : 4 = 4.75$, lấy phần nguyên là $4$).

### C. Phép chia lấy phần dư (`%`)
- Ký hiệu dấu phần trăm `%`.
- **Ý nghĩa:** Trả lời câu hỏi *"Sau khi chia đều hết mức có thể, còn thừa ra bao nhiêu?"*.
- `19 % 4 = 3` (vì $4 	\times 4 = 16$, còn dư $19 - 16 = 3$).

### D. Định lý chia có dư Toán Tiểu học trong Python
$$\mathbf{A} = (\mathbf{A} // \mathbf{B}) 	\times \mathbf{B} + (\mathbf{A} \% \mathbf{B})$$

### E. Thứ tự ưu tiên tính toán (Quy tắc PEMDAS)
$$	\text{Ngoặc } () \longrightarrow 	\text{Lũy thừa } ** \longrightarrow 	\text{Nhân, Chia } (*, /, //, \%) \longrightarrow 	\text{Cộng, Trừ } (+, -)$$
*Lưu ý:* Các phép toán cùng cấp độ được thực hiện lần lượt từ **Trái sang Phải**.

## 2. Sổ tay 6 kỹ thuật ứng dụng thực chiến của `//` và `%`

### Kỹ thuật 1: Kiểm tra tính chẵn lẻ
- Số chẵn là số chia hết cho 2 (dư 0): `n % 2 == 0`.
- Số lẻ là số chia cho 2 dư 1: `n % 2 == 1` (hoặc `n % 2 != 0`).

### Kỹ thuật 2: Kiểm tra tính chia hết
- Số $A$ là bội số của $B$ (hay $A$ chia hết cho $B$): `A % B == 0`.

### Kỹ thuật 3: Bóc tách chữ số hàng đơn vị và hàng chục
- Lấy chữ số hàng đơn vị (chữ số cuối cùng): `don_vi = n % 10`.
- Gọt bỏ chữ số hàng đơn vị: `tam = n // 10`.
- Lấy chữ số hàng chục của số $N$: `chuc = (n // 10) % 10`.

### Kỹ thuật 4: Kỹ thuật làm tròn lên (Ceiling Division)
- *Bài toán:* Có $N$ học sinh, cần thuê xe chở học sinh, mỗi xe chở được $K$ bạn. Cần ít nhất bao nhiêu xe để không bạn nào bị bỏ lại?
- Nếu dùng `N // K`, với $N = 25, K = 10$ sẽ ra $2$ (thiếu 1 xe chở 5 bạn còn lại!).
- **Công thức làm tròn lên chuẩn thi đấu:**
  $$\mathbf{so\_xe = (N + K - 1) // K}$$
  *Kiểm tra:* $(25 + 10 - 1) // 10 = 34 // 10 = 3$ xe (Tuyệt đối chính xác!).

### Kỹ thuật 5: Bài toán chu kỳ vòng tròn (Đồng hồ, Vòng chạy)
- Một vòng có $M$ trạng thái (từ 0 đến $M-1$). Di chuyển thêm $K$ bước:
  $$\mathbf{vi\_tri\_moi = (vi\_tri\_cu + K) \% M}$$
- Đồng hồ 12 giờ: Sau $K$ giờ nữa kim chỉ số mấy?
  `gio_moi = (gio_hien_tai + K) % 12`. Nếu `gio_moi == 0` thì kết quả là `12`.
  *Hoặc mẹo 1 dòng:* `(gio_hien_tai + K - 1) % 12 + 1`.

### Kỹ thuật 6: Đổi số thứ tự $K$ sang tọa độ (Hàng, Cột) trên bàn cờ
- Một bảng ô vuông có chiều rộng mỗi hàng là $W$ ô. Ô thứ $K$ ($K$ tính từ 1):
  - `idx = K - 1` (Chuyển về mốc 0)
  - `hang = (idx // W) + 1`
  - `cot = (idx % W) + 1`

## 3. Bảng bẫy lỗi phòng thi thường gặp
| Code sai | Báo lỗi / Hiện tượng | Nguyên nhân | Cách sửa đúng |
|---|---|---|---|
| `a / b` | In ra `3.0` thay vì `3` | Dùng chia thực `/` | Dùng chia nguyên `a // b` |
| `a % 0` hoặc `a // 0` | `ZeroDivisionError` | Mẫu số chia bằng 0 | Đảm bảo mẫu số $> 0$ |
| `a ^ b` | Kết quả sai hoàn toàn | `^` là phép XOR bit, không phải mũ | Viết `a ** b` |
| `a x b` | `SyntaxError` | Dùng chữ `x` làm dấu nhân | Viết `a * b` |

## 4. Concept quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

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

#### Câu 16 (thứ tự ưu tiên PEMDAS):
Giá trị của biểu thức `2 + 3 * 4 ** 2` trong Python là bao nhiêu?
- **A.** `80`
- **B.** `56`
- **C.** **[Đáp án đúng]** `50`
- **D.** `36`
> *Giải thích:* Thứ tự PEMDAS: lũy thừa trước $4 ** 2 = 16$, rồi nhân $3 * 16 = 48$, cuối cùng cộng $2 + 48 = 50$. Muốn cộng trước phải thêm ngoặc: $(2 + 3) * 16 = 80$.

#### Câu 17 (phân biệt `//` và `/`):
Kết quả của hai biểu thức `7 / 2` và `7 // 2` trong Python lần lượt là:
- **A.** `3` và `3`
- **B.** `3.5` và `3.5`
- **C.** **[Đáp án đúng]** `3.5` và `3`
- **D.** `3` và `3.5`
> *Giải thích:* Phép `/` luôn trả về số thực $7 / 2 = 3.5$, còn phép `//` chỉ giữ phần nguyên $7 // 2 = 3$.

#### Câu 18 (lũy thừa `**`):
Kết quả của biểu thức `2 ** 3 ** 2` trong Python là bao nhiêu?
- **A.** `64`
- **B.** `36`
- **C.** **[Đáp án đúng]** `512`
- **D.** `12`
> *Giải thích:* Toán tử `**` có tính kết hợp từ phải sang trái nên $2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512$. Đây là bẫy kinh điển khi viết lũy thừa chồng!
