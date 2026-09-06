# Bài 03: Phép chia nguyên, chia dư và lũy thừa

## 1. Phép chia lấy phần nguyên `//`

### 1.1. Hiểu đơn giản phép chia nguyên
Ký hiệu `//` chia hai số rồi **bỏ hết phần lẻ, chỉ giữ phần nguyên**:

* `17 // 5` nghĩa là: 17 chia 5 được 3,4 → bỏ phần `,4` đi → còn `3`.
* Nói cách khác: `//` cho biết "chia được mấy phần trọn vẹn".

| Biểu thức | Kết quả | Kiểu dữ liệu | Giải thích chi tiết |
|:---------:|:-------:|:------------:|---------------------|
| `17 // 5` | `3` | `int` | $17$ chia $5$ được $3.4$, phần nguyên trọn vẹn là $3$ |
| `20 // 4` | `5` | `int` | $20$ chia hết cho $4$, kết quả là số nguyên $5$ (không có `.0`) |
| `7 // 2` | `3` | `int` | $7$ chia $2$ được $3.5$, phần nguyên là $3$ |
| `5 // 10` | `0` | `int` | Số bị chia nhỏ hơn số chia, không chia trọn vẹn được lần nào |

### 1.2. Cẩn thận khi chia nguyên với số âm
Với số âm, phép `//` luôn **làm tròn xuống** (lấy số nguyên nhỏ hơn):
* `(-7) // 2` cho kết quả là `-4` (vì $-7 / 2 = -3.5$, làm tròn xuống thành $-4$, không phải $-3$).
* `(-10) // 3` cho kết quả là `-4` (vì $-10 / 3$ xấp xỉ $-3.33$, làm tròn xuống thành $-4$).

---

## 2. Phép chia lấy phần dư `%`

### 2.1. Định nghĩa và ý nghĩa thực tế
Toán tử `%` trả về **phần còn dư lại** sau khi đã chia hết thành các phần nguyên:

```python
print(17 % 5)  # Kết quả: 2 (vì 17 = 5 * 3 + 2)
print(20 % 4)  # Kết quả: 0 (chia hết, không còn phần dư)
print(7 % 2)   # Kết quả: 1 (7 chia 2 dư 1)
print(5 % 10)  # Kết quả: 5 (5 chia 10 được 0 lần, còn nguyên 5)
```

### 2.2. Công thức luôn đúng của phép chia
Với hai số tự nhiên $A$ và $B$ ($B > 0$), ta luôn có công thức:

$$\mathbf{A = (A // B) \times B + (A \% B)}$$

Nói bằng lời: **số bị chia = (thương nguyên × số chia) + số dư**. Phần dư luôn nhỏ hơn số chia.

* **Thử với $A = 17, B = 5$:**
 $$(17 // 5) \times 5 + (17 \% 5) = 3 \times 5 + 2 = 15 + 2 = 17 \quad (\text{Đúng y số ban đầu!})$$

![Bản chất phép chia nguyên và chia dư](../../assets/l02_modulo_visual.svg?v=1788575106)

---

## 3. Các bài toán ứng dụng thực tế kinh điển

### 3.1. Nhận diện tính chẵn lẻ và tính chia hết
* **Kiểm tra chẵn lẻ:** Số nguyên $N$ là số chẵn khi `N % 2 == 0`, là số lẻ khi `N % 2 != 0` (hoặc `N % 2 == 1`).
* **Kiểm tra tính chia hết:** Số $A$ chia hết cho $B$ khi phần dư bằng 0: `A % B == 0`.
* **Ví dụ thực tế:**
 ```python
  n = int(input())
  print(n % 2)
  # Nhập 8 in ra 0 (dư 0 nghĩa là số chẵn)
  # Nhập 7 in ra 1 (dư 1 nghĩa là số lẻ)
  ```

### 3.2. Kỹ thuật bóc tách từng chữ số của một số nguyên
Đây là kỹ thuật rất hay, dùng được trong nhiều bài tập (tính tổng các chữ số, tìm chữ số lớn nhất, kiểm tra số đọc xuôi ngược giống nhau):
* **Lấy chữ số hàng đơn vị (chữ số cuối cùng):** `chu_so_cuoi = n % 10`
* **Cắt bỏ chữ số hàng đơn vị:** `n = n // 10`

![Mô hình bóc tách từng chữ số](../../assets/l03_digit_extraction.svg?v=1788575106)

* **Code minh họa bóc tách số có 3 chữ số $N = 257$:**
 ```python
  n = 257
  don_vi = n % 10       # 257 % 10 = 7
  n = n // 10           # 257 // 10 = 25 (cắt bỏ số 7)
  chuc = n % 10          # 25 % 10 = 5
  n = n // 10           # 25 // 10 = 2 (cắt bỏ số 5)
  tram = n % 10          # 2 % 10 = 2
  print(f"Chữ số: Trăm={tram}, Chục={chuc}, Đơn vị={don_vi}")
  ```

### 3.3. Bài toán chu kỳ thời gian và tuần hoàn lịch
* **Chu kỳ 24 giờ của đồng hồ:** Hiện tại là $H$ giờ, sau $X$ giờ nữa đồng hồ sẽ chỉ:
 $$\text{gio\_moi} = (H + X) \% 24$$
* **Chu kỳ 7 ngày trong tuần:** Quy ước thứ Hai là $0$, thứ Ba là $1$, ..., Chủ nhật là $6$. Nếu hôm nay là ngày $D$, sau $K$ ngày nữa sẽ là ngày:
 $$\text{ngay\_moi} = (D + K) \% 7$$

![Ứng dụng phép chia dư chu kỳ thời gian và lịch](../../assets/l03_clock_cycle.svg?v=1788575106)

* **Ví dụ thực tế:**
 ```python
  # Hiện tại 9 giờ sáng, sau 50 giờ nữa là mấy giờ?
  gio_hien_tai = 9
  gio_sau_50h = (gio_hien_tai + 50) % 24
  print(f"Sau 50 giờ là: {gio_sau_50h} giờ")  # In ra: 11 giờ

  # Hôm nay là thứ Ba (mã 1), sau 100 ngày nữa là thứ mấy?
  thu_hien_tai = 1
  thu_sau_100_ngay = (thu_hien_tai + 100) % 7
  print(f"Mã thứ sau 100 ngày: {thu_sau_100_ngay}")  # In ra: 3 (tức thứ Năm)
  ```

### 3.4. Quy đổi thời gian từ tổng số giây sang Giờ - Phút - Giây
* $1\text{ giờ} = 3600\text{ giây}$.
* $1\text{ phút} = 60\text{ giây}$.

![Mô hình quy đổi thời gian](../../assets/l03_time_conversion.svg?v=1788575106)

* **Các bước tính:**
 ```python
  T = 3725
  gio = T // 3600              # 3725 // 3600 = 1 giờ
  so_giay_con_lai = T % 3600   # 3725 % 3600 = 125 giây
  phut = so_giay_con_lai // 60 # 125 // 60 = 2 phút
  giay = so_giay_con_lai % 60  # 125 % 60 = 5 giây
  print(f"{T} giây = {gio} giờ {phut} phút {giay} giây")
  # Kết quả: 3725 giây = 1 giờ 2 phút 5 giây
  ```

### 3.5. Bài toán đóng gói, xếp hàng và chia đều
* **Đóng thùng hàng:** Có $M$ sản phẩm, mỗi thùng chứa tối đa $K$ sản phẩm.
 * Số thùng được đóng đầy: `so_thung_day = M // K`
 * Số sản phẩm bị lẻ thừa ra: `so_san_pham_thua = M % K`
 * Số thùng ít nhất để chở hết toàn bộ sản phẩm (kể cả thùng chưa đầy):
  $$\text{tong\_so\_thung} = (M + K - 1) // K$$

* **Ví dụ cụ thể — chia kẹo:** Cô giáo có 100 cái kẹo, chia đều cho 35 bạn trong lớp.
 ```python
  keo = 100
  ban = 35
  moi_ban = keo // ban   # 100 // 35 = 2 (mỗi bạn được 2 cái nguyên)
  thua = keo % ban       # 100 % 35 = 30 (còn thừa 30 cái)
  print("Moi ban duoc:", moi_ban, "cai")
  print("So keo thua:", thua, "cai")
  # Kết quả: Moi ban duoc: 2 cai
  #          So keo thua: 30 cai
  ```
 Thử lại bằng công thức ở mục 2.2: $2 \times 35 + 30 = 70 + 30 = 100$ — đúng y số kẹo ban đầu!

---

## 4. Phép nâng lên lũy thừa `**`

### 4.1. Lũy thừa là gì?
Toán tử `**` tính lũy thừa $A^B$ (lấy $B$ thừa số $A$ nhân với nhau):

```python
print(2 ** 3)   # 2 * 2 * 2 = 8
print(10 ** 4)  # 10000
print(5 ** 0)   # 1 (Mọi số khác 0 có số mũ 0 đều bằng 1)
print(9 ** 0.5) # 3.0 (Lũy thừa 0.5 chính là căn bậc hai của 9)
```

### 4.2. Tính chất kết hợp từ phải sang trái
Khác với các phép tính khác tính lần lượt từ trái sang phải, phép lũy thừa có thứ tự ưu tiên **tính từ phải sang trái**:
* Biểu thức `2 ** 3 ** 2` sẽ được máy tính tính `3 ** 2 = 9` trước, sau đó mới tính `2 ** 9 = 512`.
* Muốn tính $(2^3)^2$, bắt buộc phải dùng dấu ngoặc: `(2 ** 3) ** 2 = 8 ** 2 = 64`.

### 4.3. Cẩn thận: Ký hiệu `^` không phải là lũy thừa!
> **LỖI NHIỀU BẠN MẮC NHẤT:**
> * Trong vở toán, mình hay viết $2^3$. Nhiều bạn quen tay gõ `2 ^ 3` vào máy.
> * Nhưng trong Python, dấu `^` là một phép tính hoàn toàn khác, cho ra kết quả rất lạ!
>  - Lệnh `print(2 ^ 3)` sẽ in ra số `1` (chứ không phải `8` đâu nhé!).
>  - Nếu viết `s = a ^ 2` để tính diện tích hình vuông cạnh $a$, kết quả sẽ sai hoàn toàn.
> * **Quy tắc nhớ:** Tính lũy thừa trong Python **phải dùng hai dấu sao liền nhau: `**`**.

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Mô phỏng chi tiết: Bóc tách chữ số của số nguyên $N = 257$

```python
n = 257
don_vi = n % 10
n = n // 10
chuc = n % 10
n = n // 10
tram = n % 10
```

| Dòng lệnh thực thi | Thao tác máy tính thực hiện | Giá trị biến `n` | Giá trị `don_vi` | Giá trị `chuc` | Giá trị `tram` |
|---|---|:---:|:---:|:---:|:---:|
| `n = 257` | Khởi tạo giá trị ban đầu vào ô nhớ `n` | **257** | — | — | — |
| `don_vi = n % 10` | Lấy phần dư $257 \% 10$ | 257 | **7** | — | — |
| `n = n // 10` | Cắt bỏ chữ số cuối: $257 // 10$ | **25** | 7 | — | — |
| `chuc = n % 10` | Lấy phần dư $25 \% 10$ | 25 | 7 | **5** | — |
| `n = n // 10` | Cắt bỏ chữ số cuối: $25 // 10$ | **2** | 7 | 5 | — |
| `tram = n % 10` | Lấy phần dư $2 \% 10$ | 2 | 7 | 5 | **2** |

> **Kết luận sau khi chạy vết:** Từ số $257$ ban đầu, qua các bước chia nguyên và chia dư, ta đã trích xuất thành công 3 biến độc lập: `tram = 2`, `chuc = 5`, `don_vi = 7`.

### Mô phỏng chi tiết: Đổi $T = 3725$ giây ra Giờ - Phút - Giây

```python
T = 3725
gio = T // 3600
so_giay_con_lai = T % 3600
phut = so_giay_con_lai // 60
giay = so_giay_con_lai % 60
```

| Dòng lệnh thực thi | Thao tác máy tính thực hiện | Giá trị `gio` | Giá trị `so_giay_con_lai` | Giá trị `phut` | Giá trị `giay` |
|---|:---:|:---:|:---:|:---:|:---:|
| `T = 3725` | Khởi tạo tổng số giây | — | — | — | — |
| `gio = T // 3600` | $3725 // 3600$ (mỗi 3600 giây được 1 giờ) | **1** | — | — | — |
| `so_giay_con_lai = T % 3600` | $3725 \% 3600$ (giây còn thừa sau khi trừ giờ) | 1 | **125** | — | — |
| `phut = so_giay_con_lai // 60` | $125 // 60$ (mỗi 60 giây được 1 phút) | 1 | 125 | **2** | — |
| `giay = so_giay_con_lai % 60` | $125 \% 60$ (giây lẻ còn lại) | 1 | 125 | 2 | **5** |

> **Kết luận:** $3725$ giây = **1 giờ 2 phút 5 giây**.

---

## 6. Lỗi hay gặp và cách tránh

### Lỗi 1: Nhầm lẫn giữa chia thực `/` và chia nguyên `//`
* Khi bài hỏi số lượng nguyên (mấy cái bánh, mấy chiếc xe), nếu dùng `/` sẽ in ra số có phần thập phân `.0` (ví dụ `4.0` thay vì `4`), nhìn rất sai!
* Luôn dùng `//` khi đáp án phải là số nguyên.

### Lỗi 2: Lỗi chia cho số không (`ZeroDivisionError`)
* Cả hai phép tính `//` và `%` đều không chấp nhận số chia bằng $0$.
* Lệnh `10 // 0` hoặc `10 % 0` sẽ lập tức làm chương trình gặp sự cố dừng khẩn cấp.
* Luôn kiểm tra số chia phải khác 0 trước khi tính.

### Lỗi 3: Quên bọc ngoặc khi tính công thức chia lấy trần
* Để tính số xe cần thiết chở $N$ người với mỗi xe chở $K$ người:
 * **Cách viết đúng:** `(n + k - 1) // k`
 * **Cách viết sai:** `n + k - 1 // k` (Do `//` có thứ tự ưu tiên cao hơn `+` và `-` nên máy tính sẽ lấy `1 // k` trước!).

---

## 7. Mẫu code áp dụng thực tế

### Mẫu 1: Nhập vào tổng số giây, đổi ra Giờ - Phút - Giây
```python
t = int(input())
gio = t // 3600
phut = (t % 3600) // 60
giay = t % 60
print(f"{gio} gio {phut} phut {giay} giay")
```

### Mẫu 2: Tính tổng các chữ số của một số có 3 chữ số
```python
n = int(input())
don_vi = n % 10
chuc = (n // 10) % 10
tram = n // 100
tong = tram + chuc + don_vi
print(tong)
```

### Mẫu 3: Tính số lượng xe chở học sinh đi dã ngoại
```python
# Mỗi xe chở tối đa 45 bạn, tính số xe ít nhất cần thuê
n = int(input())
so_xe = (n + 45 - 1) // 45
print(so_xe)
```
