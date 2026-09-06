# Bài 02: Toán tử và biểu thức

## 1. Toán tử số học

Các em thân mến, Python có tới **7 phép tính số học**. Quen với các phép này là bước đầu để viết chương trình hay!

### Bảng 7 toán tử số học

| Ký hiệu | Tên gọi | Ví dụ | Kết quả | Ghi chú |
|:---:|---|---|:---:|---|
| **`+`** | Phép cộng | `5 + 3` | `8` | Cộng hai số |
| **`-`** | Phép trừ | `10 - 4` | `6` | Trừ hai số |
| **`*`** | Phép nhân | `6 * 7` | `42` | Nhân hai số |
| **`/`** | Phép chia | `8 / 2` | `4.0` | **Luôn trả về số thực (`float`)** |
| **`%`** | Phép chia lấy dư | `7 % 2` | `1` | Số dư còn lại sau khi chia |
| **`//`** | Phép chia nguyên | `7 // 2` | `3` | Lấy phần nguyên, bỏ phần dư |
| <code>**</code> | Phép lũy thừa | `2 ** 3` | `8` | 2 mũ 3 = 2 × 2 × 2 |

### Một số chi tiết quan trọng

**Phép chia `/` luôn trả về số thực (`float`)**
Đây là chỗ dễ nhầm nhất. Dù 8 chia 2 hết, Python vẫn trả về `4.0` chứ không phải `4`.

```python
print(8 / 2)    # Kết quả: 4.0 (float)
print(10 / 5)   # Kết quả: 2.0 (float)
print(7 / 2)    # Kết quả: 3.5 (float)
```

**Phép chia nguyên `//` lấy phần nguyên**
Muốn kết quả là số nguyên, các em dùng `//`:

```python
print(7 // 2)   # Kết quả: 3 (bỏ phần dư)
print(10 // 3)  # Kết quả: 3
```

**Phép chia lấy dư `%` — "chia lấy dư"**
Phép này cho phần dư còn lại sau khi chia. Ví dụ: 7 chia 2 được 3 phần dư 1, nên `7 % 2 = 1`.

```python
print(7 % 2)    # Kết quả: 1 (7 = 3×2 + 1)
print(10 % 3)   # Kết quả: 1 (10 = 3×3 + 1)
print(8 % 4)    # Kết quả: 0 (chia hết, không dư)
```

**Phép lũy thừa `**`**
Các em đừng dùng dấu `^` nhé! Trong Python, `^` là phép tính khác, không phải lũy thừa. Lũy thừa dùng hai dấu sao `**`.

```python
print(2 ** 3)   # Kết quả: 8 (2 × 2 × 2)
print(5 ** 2)   # Kết quả: 25 (5 × 5)
```

### Mô phỏng: Phân tách số 257 thành từng chữ số

Giả sử ta có số `257` và muốn tách từng chữ số. Ta dùng `%` và `//`:

| Bước | Biến `n` | Phép tính | Kết quả | Ý nghĩa |
|:---:|:---:|---|:---:|---|
| Ban đầu | 257 | — | — | Số cần phân tách |
| 1 | 257 | `don_vi = n % 10` | `don_vi = 7` | Lấy chữ số hàng đơn vị |
| 2 | 257 | `n = n // 10` | `n = 25` | Bỏ chữ số đơn vị đi |
| 3 | 25 | `chuc = n % 10` | `chuc = 5` | Lấy chữ số hàng chục |
| 4 | 25 | `n = n // 10` | `n = 2` | Bỏ chữ số chục đi |
| 5 | 2 | `tram = n % 10` | `tram = 2` | Lấy chữ số hàng trăm |

Kết quả: số 257 có hàng trăm = 2, hàng chục = 5, hàng đơn vị = 7.

---

## 2. Biểu thức và thứ tự ưu tiên

### 2.1. Biểu thức là gì?

**Biểu thức** là sự kết hợp giữa **toán hạng** (số, biến) và **toán tử** (dấu phép tính) để tạo ra một giá trị.

Ví dụ:
- `5 + 3` → giá trị `8`
- `a * 2 + 1` → giá trị tùy vào `a`
- `(diem_thu + diem_tin) / 2` → điểm trung bình

Máy tính sẽ tính biểu thức và trả về **một giá trị duy nhất**.

### 2.2. Tháp thứ tự ưu tiên

Khi có nhiều phép tính trong một dòng, máy tính tính theo **thứ tự ưu tiên** chặt chẽ:

| Ưu tiên | Toán tử | Mô tả |
|:---:|---|---|
| **Cao nhất** | `( )` | Ngoặc tròn — tính trước hết |
| **Thứ 2** | `**` | Lũy thừa |
| **Thứ 3** | `* / // %` | Nhân, chia, chia nguyên, lấy dư — tính từ trái sang phải |
| **Thấp nhất** | `+ -` | Cộng, trừ — tính từ trái sang phải |

> **Mẹo nhớ:** Ngoặc tròn là vua! Khi chưa chắc chắn, các em cứ dùng ngoặc tròn cho rõ ràng.

### 2.3. Chuyển phân số toán học sang Python

Trong sách, phân số có gạch ngang ở giữa. Khi viết Python, các em phải dùng ngoặc tròn để máy tính hiểu đúng:

| Biểu thức toán học | Cách viết SAI | Cách viết ĐÚNG |
|:---:|:---:|:---:|
| $\frac{a + b}{c}$ | `a + b / c` | `(a + b) / c` |
| $\frac{a + b}{c + d}$ | `a + b / c + d` | `(a + b) / (c + d)` |
| $\frac{a \times b}{c \times d}$ | `a * b / c * d` | `(a * b) / (c * d)` |
| $2a + 3b$ | `2a + 3b` | `2 * a + 3 * b` |

### 2.4. Theo dõi từng bước biểu thức phức tạp

Cùng xem máy tính xử lý biểu thức này ra sao:

```python
a = 8
b = 2
c = 5
ket_qua = (a + 4) / (b + 1) + c * 3 - 6 / 2
```

| Bước | Phép tính ưu tiên | Biểu thức còn lại | Kết quả bước này |
|:---:|---|---|:---:|
| Gốc | `(8 + 4) / (2 + 1) + 5 * 3 - 6 / 2` | — | — |
| 1 | Ngoặc `(8 + 4)` | `12 / (2 + 1) + 5 * 3 - 6 / 2` | 12 |
| 2 | Ngoặc `(2 + 1)` | `12 / 3 + 5 * 3 - 6 / 2` | 3 |
| 3 | Chia `12 / 3` | `4.0 + 5 * 3 - 6 / 2` | 4.0 |
| 4 | Nhân `5 * 3` | `4.0 + 15 - 6 / 2` | 15 |
| 5 | Chia `6 / 2` | `4.0 + 15 - 3.0` | 3.0 |
| 6 | Cộng `4.0 + 15` | `19.0 - 3.0` | 19.0 |
| 7 | Trừ `19.0 - 3.0` | `16.0` | 16.0 |

Kết quả cuối: `ket_qua = 16.0`

### 2.5. Biểu thức chuỗi — cộng và nhân chữ

Không chỉ số mới tính được! Chuỗi ký tự cũng có cách tính riêng:
* **Dấu `+` nối hai chuỗi lại với nhau** (gọi là ghép chuỗi).
* **Dấu `*` lặp lại một chuỗi nhiều lần.**

```python
print("Ha" + "Noi")      # Kết quả: HaNoi (ghép dính lại)
print("Ha" + " " + "Noi")  # Kết quả: Ha Noi (thêm dấu cách ở giữa)
print("A" * 3)           # Kết quả: AAA (lặp chữ A 3 lần)
print("Ho" * 2)          # Kết quả: HoHo
```

> **Nhớ nhé:** `+` với số là phép cộng (`2 + 3 = 5`), nhưng `+` với chuỗi là phép ghép (`"2" + "3" = "23"`). Cùng một dấu mà ý nghĩa khác nhau tùy kiểu dữ liệu!

---

## 3. Toán tử gán

Ngoài phép gán `=`, Python còn cho phép **cộng rồi gán**, **trừ rồi gán**... rất gọn!

| Toán tử | Ví dụ | Tương đương | Giải thích |
|:---:|---|---|---|
| `=` | `a = 10` | — | Gán giá trị |
| `+=` | `a += 5` | `a = a + 5` | Cộng 5 rồi gán lại |
| `-=` | `a -= 3` | `a = a - 3` | Trừ 3 rồi gán lại |
| `*=` | `a *= 2` | `a = a * 2` | Nhân 2 rồi gán lại |
| `/=` | `a /= 4` | `a = a / 4` | Chia 4 rồi gán lại |
| `%=` | `a %= 3` | `a = a % 3` | Chia lấy dư 3 rồi gán lại |
| `//=` | `a //= 2` | `a = a // 2` | Chia nguyên 2 rồi gán lại |

Ví dụ minh họa:

```python
a = 10
print(a)     # 10

a += 5       # a = 10 + 5 = 15
print(a)     # 15

a -= 3       # a = 15 - 3 = 12
print(a)     # 12

a *= 2       # a = 12 * 2 = 24
print(a)     # 24
```

Các phép gán này rất tiện khi ta muốn **đổi giá trị biến từng chút một**, ví dụ cộng dồn điểm hay đếm số lượng.

---

## 4. Toán tử so sánh

Toán tử so sánh dùng để **so sánh hai giá trị** với nhau. Kết quả luôn là `True` (đúng) hoặc `False` (sai) — chính là kiểu `bool` ở bài 1!

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|:---:|---|---|:---:|
| `==` | Bằng nhau? | `5 == 5` | `True` |
| `!=` | Khác nhau? | `5 != 3` | `True` |
| `>` | Lớn hơn? | `7 > 3` | `True` |
| `<` | Nhỏ hơn? | `4 < 2` | `False` |
| `>=` | Lớn hơn hoặc bằng? | `5 >= 5` | `True` |
| `<=` | Nhỏ hơn hoặc bằng? | `3 <= 8` | `True` |

### Theo dõi từng bước so sánh trong thực tế

Giả sử điểm của Minh là 8, điểm của Lan là 9:

```python
diem_minh = 8
diem_lan = 9

print(diem_minh == diem_lan)   # False (8 khác 9)
print(diem_minh != diem_lan)   # True (8 khác 9)
print(diem_minh > diem_lan)    # False (8 không lớn hơn 9)
print(diem_minh < diem_lan)    # True (8 nhỏ hơn 9)
print(diem_minh >= 8)          # True (8 bằng 8, nên >= là đúng)
```

> **Lưu ý:** Dấu `=` là phép gán, dấu `==` mới là phép so sánh "bằng nhau" nhé!

---

## 5. Toán tử logic

Toán tử logic dùng để **kết hợp nhiều điều kiện** lại với nhau. Kết quả cũng chỉ là `True` hoặc `False`.

| Toán tử | Ý nghĩa | Kết quả |
|---|---|---|
| `and` | **VÀ** — cả hai điều kiện đều phải đúng | True chỉ khi cả hai đều True |
| `or` | **HOẶC** — chỉ cần một điều kiện đúng | True khi ít nhất một điều đúng |
| `not` | **KHÔNG PHẢI** — đảo ngược kết quả | True biến thành False, và ngược lại |

### Ví dụ đời thường

**Điều kiện được chơi trò chơi:** Phải làm bài xong **VÀ** phải ăn cơm xong.

```python
lam_bai_xong = True
an_com_xong = True

cho_phep_choi = lam_bai_xong and an_com_xong
print(cho_phep_choi)   # True — cả hai đều xong, được chơi!
```

Nếu chỉ ăn cơm xong mà chưa làm bài thì sao?

```python
lam_bai_xong = False
an_com_xong = True

cho_phep_choi = lam_bai_xong and an_com_xong
print(cho_phep_choi)   # False — chưa làm bài, không được chơi!
```

**Điều kiện được ăn bánh:** Được mẹ mua cho **HOẶC** được ông bà cho.

```python
me_mua = False
ong_ba_cho = True

duoc_an_banh = me_mua or ong_ba_cho
print(duoc_an_banh)    # True — dù mẹ không mua, ông bà cho thì vẫn được ăn!
```

**Phủ định:** `not` đảo ngược kết quả.

```python
da_hoc_xong = True
print(not da_hoc_xong)   # False — "chưa học xong" là sai
```

> **Nhìn trước:** Sau này khi học về chuỗi ký tự và danh sách, các em sẽ gặp thêm hai phép rất hay là `in` (có nằm trong không?) và `is` (có phải cùng một thứ không?). Bài này ta quen với 4 nhóm trên trước nhé!

---

## 6. Lỗi hay gặp và cách tránh

### Bẫy 1: Phép chia `/` luôn trả về số thực

Đây là chỗ dễ sai nhất. Ta muốn in số nguyên, nhưng dùng `/` nên bị in ra `8.0` thay vì `8`.

```python
# SAI — in ra 4.0 thay vì 4
ket_qua = 8 / 2
print(ket_qua)    # 4.0

# ĐÚNG — dùng // để lấy phần nguyên
ket_qua = 8 // 2
print(ket_qua)    # 4
```

### Bẫy 2: Chia cho số không — ZeroDivisionError

Phép chia cho 0 là **không hợp lệ**. Chương trình sẽ dừng ngay!

```python
print(10 / 0)   # ZeroDivisionError: division by zero
```

> **Cách tránh:** Luôn kiểm tra mẫu số khác 0 trước khi chia.

### Bẫy 3: Quên dấu `*` trong phép nhân

Trong toán, ta hay viết `2x` hoặc `3(a+b)`. Nhưng Python **không hiểu** kiểu viết đó!

```python
ket_qua = 2 * x    # ĐÚNG — luôn viết dấu * rõ ràng
ket_qua = 2x       # SAI — SyntaxError! Máy tính không hiểu
ket_qua = 3 * (a + b)  # ĐÚNG
```

> **Quy tắc:** Phép nhân luôn phải có dấu `*`.

### Bẫy 4: Dùng dấu phẩy `,` thay dấu chấm `.`

Trong đời sống, ta hay viết số thực bằng dấu phẩy: `3,5`. Nhưng Python bắt buộc dùng dấu chấm!

```python
# SAI — Python hiểu là tuple (3, 5)
diem = 3,5

# ĐÚNG
diem = 3.5
```

### Bẫy 5: Dùng `^` thay `**`

Dấu `^` trong Python là phép tính trên dãy bit, **không phải** lũy thừa!

```python
# SAI — XOR, không phải 2 lũy thừa 3
print(2 ^ 3)    # 1 (không phải 8!)

# ĐÚNG — lũy thừa
print(2 ** 3)   # 8
```

---

## 7. Ví dụ minh họa

### 7.1. Tính diện tích hình chữ nhật

```python
dai = 7
rong = 3
dien_tich = dai * rong
print("Dien tich hinh chu nhat la:", dien_tich)
# Kết quả: Dien tich hinh chu nhat la: 21
```

### 7.2. Đổi phút sang giờ và phút

```python
tong_phut = 125
gio = tong_phut // 60       # 125 // 60 = 2 (phần giờ)
phut_con_lai = tong_phut % 60  # 125 % 60 = 5 (phần phút còn lại)
print(tong_phut, "phut =", gio, "gio", phut_con_lai, "phut")
# Kết quả: 125 phut = 2 gio 5 phut
```

### 7.3. Tính tiền thừa khi mua bánh

```python
tien_du = 50000
gia_banh = 12000
tien_tra = 3 * gia_banh     # Mua 3 bánh
tien_thua = tien_du - tien_tra
print("Tien mua:", tien_tra, "dong")
print("Tien thua:", tien_thua, "dong")
# Kết quả: Tien mua: 36000 dong
#          Tien thua: 14000 dong
```

### 7.4. Tính phần dư để biết chẵn hay lẻ

```python
so = 17
kiem_tra = so % 2
print(kiem_tra)
# Kết quả: 1 (dư 1 nghĩa là số lẻ, dư 0 nghĩa là số chẵn)
```
