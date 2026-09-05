# Bài 03: Phép chia nguyên, chia dư và lũy thừa

## 1. Bản chất của phép chia nguyên, chia dư và lũy thừa

Trong số học thi đấu, nếu như các phép cộng, trừ, nhân, chia cơ bản giúp ta xử lý các tính toán định lượng thông thường, thì bộ ba công cụ **chia lấy phần nguyên (`//`)**, **chia lấy phần dư (`%`)** và **phép lũy thừa (`**`)** chính là chiếc chìa khóa vạn năng để bóc tách cấu trúc số học:
* Phép chia nguyên `//` giải quyết bài toán chia đồ vật, đóng thùng, tính số chuyến xe.
* Phép chia dư `%` giải quyết bài toán kiểm tra chẵn lẻ, chia hết, chu kỳ đồng hồ và bóc tách từng chữ số.
* Phép lũy thừa `**` tính tích của các thừa số bằng nhau và là tử huyệt số 1 khi học sinh gõ nhầm dấu mũ `^`.

---

## 2. Phép chia lấy phần nguyên `//`

### 2.1. Định nghĩa toán học
* Ký hiệu `//` thực hiện phép chia và lấy **phần nguyên lớn nhất không vượt quá thương số**:
  $$A // B = \lfloor \frac{A}{B} \rfloor$$
* Ví dụ:
  - `7 // 2 = 3` (Vì $7 = 2 \times 3 + 1$).
  - `17 // 5 = 3` (17 chia 5 được 3 dư 2).
  - `20 // 4 = 5` (Chia hết, kết quả là số nguyên `5`).

### 2.2. Ý nghĩa thực tế trong các bài toán đố
* **Bài toán chia kẹo:** Có $17$ chiếc kẹo chia đều cho $5$ bạn nhỏ. Hỏi mỗi bạn nhận được trọn vẹn bao nhiêu chiếc kẹo?
  $$\text{so\_keo} = 17 // 5 = 3 \text{ (chiếc)}$$
* **Bài toán xếp xe chở học sinh:** Có $100$ học sinh, mỗi xe chở được đúng $30$ em. Hỏi có bao nhiêu chuyến xe chở đủ kín chỗ?
  $$\text{so\_chuyen\_day} = 100 // 30 = 3 \text{ (chuyến)}$$

---

## 3. Phép chia lấy phần dư `%`

### 3.1. Định nghĩa toán học
* Ký hiệu `%` trả về **phần còn dư lại** sau khi đã chia hết thành các phần nguyên:
  - `7 % 2 = 1` (Phần dư khi 7 chia 2).
  - `17 % 5 = 2` (Phần dư khi 17 chia 5).
  - `20 % 4 = 0` (Chia hết thì phần dư luôn bằng 0).

### 3.2. Mối quan hệ vàng bất biến của phép chia
Trong khoa học máy tính và số học, với hai số tự nhiên $A$ và $B$ ($B > 0$), luôn tồn tại một **đẳng thức bất biến**:
$$\mathbf{A = (A // B) \times B + (A \% B)} \quad \text{với} \quad 0 \le (A \% B) < B$$

* **Thử lại với ví dụ $A = 17, B = 5$:**
  $$(17 // 5) \times 5 + (17 \% 5) = 3 \times 5 + 2 = 15 + 2 = 17 \quad (\text{Chính xác tuyệt đối!})$$

![Bản chất phép chia nguyên và chia dư](../../assets/l02_modulo_visual.svg?v=1788575106)

---

## 4. Bốn ứng dụng cốt lõi của Modulo trong lập trình thi đấu

### 4.1. Kiểm tra tính chẵn lẻ của một số
* Một số nguyên $N$ là **số chẵn** khi chia hết cho 2: `N % 2 == 0`.
* Một số nguyên $N$ là **số lẻ** khi chia 2 dư 1: `N % 2 == 1`.

### 4.2. Kiểm tra tính chia hết
* Số $A$ chia hết cho số $B$ khi và chỉ khi phần dư bằng 0: `A % B == 0`.
* Số $A$ không chia hết cho số $B$: `A % B != 0`.

### 4.3. Lấy và cắt bỏ chữ số hàng đơn vị
* **Lấy chữ số hàng đơn vị:** Phép chia cho 10 lấy dư luôn trả về chữ số cuối cùng:
  $$\text{chu\_so\_cuoi} = N \% 10$$
  *(Ví dụ: $2026 \% 10 = 6$)*
* **Cắt bỏ chữ số hàng đơn vị:** Phép chia nguyên cho 10 sẽ vứt bỏ chữ số cuối cùng:
  $$\text{phan\_con\_lai} = N // 10$$
  *(Ví dụ: $2026 // 10 = 202$)*

### 4.4. Bài toán chu kỳ thời gian và tuần hoàn (Đồng hồ)
* Một ngày có 24 giờ. Nếu bây giờ là 10 giờ sáng, hỏi sau 50 giờ nữa là mấy giờ?
* Thay vì phải cộng trừ thủ công, ta dùng phép chia dư cho chu kỳ 24:
  $$\text{gio\_moi} = (10 + 50) \% 24 = 60 \% 24 = 12 \text{ (Tức 12 giờ trưa)}$$
* Một tuần có 7 ngày (từ thứ Hai đến Chủ nhật). Bài toán tìm ngày trong tuần sau $K$ ngày nữa cũng áp dụng phép tính `% 7`.

---

## 5. Phép nâng lên lũy thừa `**`

Toán tử `**` dùng để tính lũy thừa $A^B$ ($B$ thừa số $A$ nhân với nhau):
```python
print(2 ** 3)   # 2 * 2 * 2 = 8
print(10 ** 4)  # 10000
print(5 ** 0)   # 1 (Mọi số khác 0 có số mũ 0 đều bằng 1)
```

> ❌ **TỬ HUYỆT PHÒNG THI BẮT BUỘC PHẢI NHỚ: TOÁN TỬ `^` KHÔNG PHẢI LÀ LŨY THỪA!**
> * Trong toán học, ta hay quen tay gõ `2 ^ 3` để biểu diễn $2^3$.
> * Tuy nhiên trong Python, ký hiệu `^` là **phép toán logic trên bit**:
>   - Lệnh `print(2 ^ 3)` sẽ in ra số `1` (do $0010_2 \oplus 0011_2 = 0001_2$).
>   - Rất nhiều học sinh gõ `a ^ 2` để tính $a^2$ và nhận kết quả sai hoàn toàn mà không hiểu vì sao!
> * **Quy tắc vàng:** Trong Python, tính lũy thừa **bắt buộc dùng hai dấu sao liền nhau: `**`**.

---

## 6. Bảng mô phỏng biến thiên ô nhớ

Xét đoạn chương trình xử lý một số nguyên:
```python
n = 257
don_vi = n % 10
n = n // 10
chuc = n % 10
tram = n // 10
```

### Bảng theo dõi giá trị các biến trong bộ nhớ RAM:

| Dòng lệnh | Thao tác máy tính thực hiện | `n` | `don_vi` | `chuc` | `tram` |
|---|---|:---:|:---:|:---:|:---:|
| `n = 257` | Nạp số ban đầu vào ô nhớ `n` | **257** | Chưa có | Chưa có | Chưa có |
| `don_vi = n % 10` | Lấy phần dư $257 \% 10 = 7$ | 257 | **7** | Chưa có | Chưa có |
| `n = n // 10` | Cắt bỏ chữ số cuối: $257 // 10 = 25$ | **25** | 7 | Chưa có | Chưa có |
| `chuc = n % 10` | Lấy phần dư $25 \% 10 = 5$ | 25 | 7 | **5** | Chưa có |
| `tram = n // 10` | Cắt tiếp lấy hàng trăm: $25 // 10 = 2$ | 25 | 7 | 5 | **2** |

---

## 7. Concept Quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép tính `17 // 4` trong Python cho kết quả là:
- **A.** 4.25
- **B.** **[Đáp án đúng]** 4
- **C.** 1
- **D.** 4.0
- > *Giải thích:* Phép chia nguyên `//` lấy thương nguyên, $17 = 4 \times 4 + 1$ nên thương nguyên là 4.

#### Câu 2: Phép tính `17 % 4` trong Python cho kết quả là:
- **A.** 4
- **B.** **[Đáp án đúng]** 1
- **C.** 4.25
- **D.** 0
- > *Giải thích:* $17$ chia $4$ dư $1$.

#### Câu 3: Toán tử nào dùng để tính lũy thừa $A^B$ trong Python?
- **A.** `^`
- **B.** `*`
- **C.** **[Đáp án đúng]** `**`
- **D.** `exp`
- > *Giải thích:* Trong Python, lũy thừa là hai dấu sao liền nhau `**`.

#### Câu 4: Khi chạy lệnh `print(2 ^ 3)` trong Python, màn hình sẽ hiển thị:
- **A.** 8
- **B.** 6
- **C.** **[Đáp án đúng]** 1
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Dấu `^` là phép toán bitwise XOR, $2 \oplus 3 = 1$.

#### Câu 5: Để lấy chữ số hàng đơn vị của số nguyên dương $N$, ta dùng công thức:
- **A.** `N // 10`
- **B.** **[Đáp án đúng]** `N % 10`
- **C.** `N / 10`
- **D.** `N * 10`
- > *Giải thích:* Phần dư khi chia cho 10 chính là chữ số hàng đơn vị.

#### Câu 6: Để cắt bỏ chữ số hàng đơn vị của số $N$, ta dùng công thức:
- **A.** `N % 10`
- **B.** **[Đáp án đúng]** `N // 10`
- **C.** `N - 10`
- **D.** `N / 10`
- > *Giải thích:* Chia nguyên cho 10 sẽ làm mất chữ số cuối cùng.

#### Câu 7: Điều kiện nào kiểm tra số tự nhiên $N$ là số chẵn?
- **A.** `N % 2 == 1`
- **B.** `N // 2 == 0`
- **C.** **[Đáp án đúng]** `N % 2 == 0`
- **D.** `N / 2 == 0`
- > *Giải thích:* Số chẵn là số chia hết cho 2 (phần dư bằng 0).

#### Câu 8: Hiện tại là 8 giờ sáng, sau 30 giờ nữa là mấy giờ?
- **A.** 10 giờ sáng
- **B.** **[Đáp án đúng]** 14 giờ (2 giờ chiều)
- **C.** 38 giờ
- **D.** 6 giờ chiều
- > *Giải thích:* $(8 + 30) \% 24 = 38 \% 24 = 14$.

#### Câu 9: Biểu thức `10 ** 0` có giá trị bằng:
- **A.** 0
- **B.** **[Đáp án đúng]** 1
- **C.** 10
- **D.** Báo lỗi
- > *Giải thích:* Bất kỳ số nào khác 0 nâng lên lũy thừa 0 đều bằng 1.

#### Câu 10: Cho $A = 26, B = 6$. Kết quả của `(A // B) * B + (A % B)` là:
- **A.** 24
- **B.** **[Đáp án đúng]** 26
- **C.** 2
- **D.** 30
- > *Giải thích:* Theo định lý bất biến phép chia, biểu thức luôn trả về chính số bị chia $A$.

#### Câu 11: Phép tính `5 // 10` có kết quả là:
- **A.** 0.5
- **B.** **[Đáp án đúng]** 0
- **C.** 5
- **D.** 1
- > *Giải thích:* $5 < 10$ nên thương nguyên là 0.

#### Câu 12: Phép tính `5 % 10` có kết quả là:
- **A.** 0
- **B.** **[Đáp án đúng]** 5
- **C.** 0.5
- **D.** 2
- > *Giải thích:* $5$ chia $10$ được $0$ dư $5$.

#### Câu 13: Kết quả của `2 ** 3 ** 2` là:
- **A.** 64
- **B.** **[Đáp án đúng]** 512
- **C.** 12
- **D.** 36
- > *Giải thích:* Phép lũy thừa kết hợp từ phải qua trái: `3 ** 2 = 9`, sau đó `2 ** 9 = 512`.

#### Câu 14: Biểu thức `100 % 25` bằng:
- **A.** 4
- **B.** **[Đáp án đúng]** 0
- **C.** 25
- **D.** 1
- > *Giải thích:* 100 chia hết cho 25 nên phần dư bằng 0.

#### Câu 15: Một hộp kẹo có 20 chiếc kẹo chia cho 6 bạn. Số kẹo còn thừa lại là:
- **A.** `20 // 6`
- **B.** **[Đáp án đúng]** `20 % 6`
- **C.** `20 / 6`
- **D.** `20 - 6`
- > *Giải thích:* Số kẹo thừa chính là phần dư của phép chia: $20 \% 6 = 2$.

#### Câu 16: Phép tính `4 ** 0.5` cho kết quả là:
- **A.** **[Đáp án đúng]** 2.0
- **B.** 2
- **C.** 1.0
- **D.** 8.0
- > *Giải thích:* Lũy thừa $0.5$ chính là căn bậc hai: $\sqrt{4} = 2.0$.

#### Câu 17: Phép tính `(-7) // 2` trong Python làm tròn xuống nên cho kết quả là:
- **A.** -3
- **B.** **[Đáp án đúng]** -4
- **C.** -3.5
- **D.** 3
- > *Giải thích:* Phép chia `//` trong Python là floor division (làm tròn xuống số nguyên nhỏ hơn), $-3.5$ làm tròn xuống là $-4$.

#### Câu 18: Cho số nguyên dương $N$. Biểu thức `(N // 10) % 10` dùng để lấy:
- **A.** Chữ số hàng đơn vị
- **B.** **[Đáp án đúng]** Chữ số hàng chục
- **C.** Chữ số hàng trăm
- **D.** Tổng các chữ số
- > *Giải thích:* Cắt bỏ hàng đơn vị (`N // 10`), sau đó lấy phần dư chia 10 sẽ được chữ số hàng chục.
