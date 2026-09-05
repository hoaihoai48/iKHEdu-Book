# Bài 02: Toán tử và biểu thức

## 1. Toán tử số học

Python cho chúng ta tới **7 phép tính số học** cơ bản. Làm quen với chúng là bước đầu tiên để viết được chương trình hay ho!

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
Đây là bẫy lớn nhất mà mọi người mới học hay gặp. Dù 8 chia 2 hết đi nữa, Python vẫn trả về `4.0` (có số thập phân), chứ không phải `4`.

```python
print(8 / 2)    # Kết quả: 4.0 (float)
print(10 / 5)   # Kết quả: 2.0 (float)
print(7 / 2)    # Kết quả: 3.5 (float)
```

**Phép chia nguyên `//` lấy phần nguyên**
Nếu muốn kết quả là số nguyên (không có số thập phân), dùng `//`:

```python
print(7 // 2)   # Kết quả: 3 (bỏ phần dư)
print(10 // 3)  # Kết quả: 3
```

**Phép chia lấy dư `%` — "chia lấy dư"**
Phép này cho ta phần dư còn lại sau khi chia. Ví dụ: 7 chia 2 được 3 phần dư 1, nên `7 % 2 = 1`.

```python
print(7 % 2)    # Kết quả: 1 (7 = 3×2 + 1)
print(10 % 3)   # Kết quả: 1 (10 = 3×3 + 1)
print(8 % 4)    # Kết quả: 0 (chia hết, không dư)
```

**Phép lũy thừa `**`**
Đừng dùng dấu `^` nhé! `^` trong Python là phép XOR (một phép tính khác), không phải lũy thừa. Phép lũy thừa dùng hai dấu sao `**`.

```python
print(2 ** 3)   # Kết quả: 8 (2 × 2 × 2)
print(5 ** 2)   # Kết quả: 25 (5 × 5)
```

### Mô phỏng: Phân tách số 257 thành từng chữ số

Giả sử ta có số `257` và muốn tách từng chữ số (đơn vị, chục, trăm). Ta dùng phép chia lấy dư `%` và chia nguyên `//`:

| Bước | Biến `n` | Phép tính | Kết quả | Ý nghĩa |
|:---:|:---:|---|:---:|---|
| Ban đầu | 257 | — | — | Số cần phân tách |
| 1 | 257 | `don_vi = n % 10` | `don_vi = 7` | Lấy chữ số hàng đơn vị |
| 2 | 257 | `n = n // 10` | `n = 25` | Bỏ chữ số đơn vị đi |
| 3 | 25 | `chuc = n % 10` | `chuc = 5` | Lấy chữ số hàng chục |
| 4 | 25 | `n = n // 10` | `n = 2` | Bỏ chữ số chục đi |
| 5 | 2 | `tram = n % 10` | `tram = 2` | Lấy chữ số hàng trăm |

Kết quả: số 257 có chữ số hàng trăm = 2, hàng chục = 5, hàng đơn vị = 7. Hay quá phải không?

---

## 2. Biểu thức và thứ tự ưu tiên

### 2.1. Biểu thức là gì?

**Biểu thức** là sự kết hợp giữa **toán hạng** (số, biến) và **toán tử** (dấu phép tính) để tạo ra một giá trị.

Ví dụ:
- `5 + 3` → giá trị `8`
- `a * 2 + 1` → giá trị tùy vào `a`
- `(diem_thu + diem_tin) / 2` → điểm trung bình

Máy tính sẽ tính toán biểu thức và trả về **một giá trị duy nhất**.

### 2.2. Tháp thứ tự ưu tiên

Khi có nhiều phép tính trong một dòng, máy tính không tính bừa từ trái sang phải. Máy tính tuân thủ **thứ tự ưu tiên** nghiêm ngặt:

| Ưu tiên | Toán tử | Mô tả |
|:---:|---|---|
| **Cao nhất** | `( )` | Ngoặc tròn — tính trước hết |
| **Thứ 2** | `**` | Lũy thừa |
| **Thứ 3** | `* / // %` | Nhân, chia, chia nguyên, lấy dư — tính từ trái sang phải |
| **Thấp nhất** | `+ -` | Cộng, trừ — tính từ trái sang phải |

> **Mẹo nhớ:** Ngoặc tròn là vua! Khi không chắc chắn, cứ dùng ngoặc tròn cho rõ ràng.

### 2.3. Chuyển phân số toán học sang Python

Trong sách giáo khoa, phân số có gạch ngang ở giữa. Khi viết Python, mình phải dùng ngoặc tròn để máy tính hiểu đúng:

| Biểu thức toán học | Cách viết SAI | Cách viết ĐÚNG |
|:---:|:---:|:---:|
| $\frac{a + b}{c}$ | `a + b / c` | `(a + b) / c` |
| $\frac{a + b}{c + d}$ | `a + b / c + d` | `(a + b) / (c + d)` |
| $\frac{a \times b}{c \times d}$ | `a * b / c * d` | `(a * b) / (c * d)` |
| $2a + 3b$ | `2a + 3b` | `2 * a + 3 * b` |

### 2.4. Dry-run: Truy vết biểu thức phức tạp

Xem máy tính xử lý biểu thức này như thế nào:

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

Không chỉ số mới tính được! Chuỗi ký tự cũng có biểu thức riêng:
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

Ngoài phép gán đơn giản `=`, Python còn cho phép **cộng rồi gán**, **trừ rồi gán**... rất tiện lợi!

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

Những toán tử gán này rất hữu ích khi mình muốn **thay đổi giá trị biến dần dần** trong quá trình tính toán, ví dụ đếm điểm, cộng dồn tiền, ...

---

## 4. Toán tử so sánh

Toán tử so sánh dùng để **so sánh hai giá trị** với nhau. Kết quả luôn là `True` (đúng) hoặc `False` (sai) — chính là kiểu `bool` mà chúng ta đã học ở bài 1!

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|:---:|---|---|:---:|
| `==` | Bằng nhau? | `5 == 5` | `True` |
| `!=` | Khác nhau? | `5 != 3` | `True` |
| `>` | Lớn hơn? | `7 > 3` | `True` |
| `<` | Nhỏ hơn? | `4 < 2` | `False` |
| `>=` | Lớn hơn hoặc bằng? | `5 >= 5` | `True` |
| `<=` | Nhỏ hơn hoặc bằng? | `3 <= 8` | `True` |

### Dry-run: So sánh trong thực tế

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

**Điều kiện được chơi game:** Phải làm bài xong **VÀ** phải ăn cơm xong.

```python
lam_bai_xong = True
an_com_xong = True

cho_phep_choi = lam_bai_xong and an_com_xong
print(cho_phep_choi)   # True — cả hai đều xong, được chơi!
```

Nếu chỉ ăn cơm xong mà chưa làm bài?

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

> **Nhìn trước:** Sau này khi học về chuỗi ký tự và danh sách, các em sẽ gặp thêm hai toán tử rất hay là `in` (có nằm trong không?) và `is` (có phải cùng một thứ không?). Bài này mình làm quen với 4 nhóm trên trước đã nhé!

---

## 6. Lỗi hay gặp và cách tránh

### Bẫy 1: Phép chia `/` luôn trả về số thực

Đây là lỗi "kinh điển" nhất. Các em đang viết chương trình in điểm integer, nhưng dùng `/` nên bị in ra `8.0` thay vì `8`.

```python
# SAI — in ra 4.0 thay vì 4
ket_qua = 8 / 2
print(ket_qua)    # 4.0

# ĐÚNG — dùng // để lấy phần nguyên
ket_qua = 8 // 2
print(ket_qua)    # 4
```

### Bẫy 2: Chia cho số không — ZeroDivisionError

Phép chia cho 0 là **không hợp lệ**. Chương trình sẽ bị dừng ngay lập tức!

```python
print(10 / 0)   # ZeroDivisionError: division by zero
```

> **Cách tránh:** Luôn kiểm tra mẫu số khác 0 trước khi chia.

### Bẫy 3: Quên dấu `*` trong phép nhân

Trong toán học, mình hay viết `2x` hoặc `3(a+b)`. Nhưng Python **không hiểu** kiểu viết đó!

```python
ket_qua = 2 * x    # ĐÚNG — luôn viết dấu * rõ ràng
ket_qua = 2x       # SAI — SyntaxError! Máy tính không hiểu
ket_qua = 3 * (a + b)  # ĐÚNG
```

> **Quy tắc:** Phép nhân luôn phải có dấu `*`.

### Bẫy 4: Dùng dấu phẩy `,` thay dấu chấm `.`

Trong tiếng Việt, mình hay viết số thực bằng dấu phẩy: `3,5`. Nhưng Python bắt buộc dùng dấu chấm!

```python
# SAI — Python hiểu là tuple (3, 5)
diem = 3,5

# ĐÚNG
diem = 3.5
```

### Bẫy 5: Dùng `^` thay `**`

Dấu `^` trong Python là phép XOR (bitwise), **không phải** lũy thừa!

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

---

## 8. Concept Quiz: 20 câu trắc nghiệm

#### Câu 1: Phép chia `10 / 2` trong Python trả về kết quả nào?
- **A.** `5` (kiểu int)
- **B.** **[Đáp án đúng]** `5.0` (kiểu float)
- **C.** `5.00`
- **D.** Báo lỗi
- > *Giải thích:* Phép chia `/` trong Python **luôn luôn** trả về kiểu số thực `float`, kể cả khi chia hết.

#### Câu 2: Biểu thức `2 + 3 * 4` có kết quả là bao nhiêu?
- **A.** 20
- **B.** **[Đáp án đúng]** 14
- **C.** 24
- **D.** 10
- > *Giải thích:* Phép nhân `*` được tính trước: `3 * 4 = 12`, rồi `2 + 12 = 14`.

#### Câu 3: Để viết phân số $\frac{a + b}{c + d}$ trong Python, cách nào đúng?
- **A.** `a + b / c + d`
- **B.** `(a + b) / c + d`
- **C.** `a + b / (c + d)`
- **D.** **[Đáp án đúng]** `(a + b) / (c + d)`
- > *Giải thích:* Cần ngoặc tròn bọc cả tử và mẫu để máy tính tính tổng trước khi chia.

#### Câu 4: Khi chạy `print(10 / 0)`, điều gì xảy ra?
- **A.** In ra `0`
- **B.** In ra `inf`
- **C.** **[Đáp án đúng]** Báo lỗi `ZeroDivisionError`
- **D.** Chương trình tự bỏ qua
- > *Giải thích:* Chia cho 0 là không hợp lệ, gây lỗi dừng chương trình.

#### Câu 5: Biểu thức `"Ho" * 2` trong Python cho kết quả là?
- **A.** `"Ho2"`
- **B.** `"2Ho"`
- **C.** **[Đáp án đúng]** `"HoHo"`
- **D.** Báo lỗi
- > *Giải thích:* Dấu `*` giữa chuỗi và số nguyên lặp lại chuỗi đó: `"Ho"` lặp 2 lần thành `"HoHo"`.

#### Câu 6: Biểu thức `(10 - 2) * (3 + 1)` cho kết quả bằng?
- **A.** 16
- **B.** 22
- **C.** **[Đáp án đúng]** 32
- **D.** 28
- > *Giải thích:* Tính ngoặc trước: `8 * 4 = 32`.

#### Câu 7: Khi viết `x = 2(a + b)` trong Python, máy tính sẽ báo lỗi?
- **A.** Tự động hiểu là nhân
- **B.** **[Đáp án đúng]** Báo lỗi cú pháp `SyntaxError`
- **C.** In ra kết quả bình thường
- **D.** Gán 2 vào x
- > *Giải thích:* Python không hỗ trợ phép nhân ngầm, phải viết `2 * (a + b)`.

#### Câu 8: `7 % 2` cho kết quả bằng bao nhiêu?
- **A.** 3
- **B.** **[Đáp án đúng]** 1
- **C.** 3.5
- **D.** 2
- > *Giải thích:* 7 chia 2 được 3 phần dư 1, nên `7 % 2 = 1`.

#### Câu 9: `2 ** 4` cho kết quả bằng bao nhiêu?
- **A.** 8
- **B.** 6
- **C.** **[Đáp án đúng]** 16
- **D.** 24
- > *Giải thích:* `2 ** 4 = 2 × 2 × 2 × 2 = 16`.

#### Câu 10: Biểu thức `10 - 3 * 2` có kết quả là?
- **A.** 14
- **B.** **[Đáp án đúng]** 4
- **C.** 7
- **D.** 24
- > *Giải thích:* Nhân trước: `3 * 2 = 6`, rồi `10 - 6 = 4`.

#### Câu 11: `8 // 3` cho kết quả bằng bao nhiêu?
- **A.** 2.666
- **B.** **[Đáp án đúng]** 2
- **C.** 3
- **D.** 1
- > *Giải thích:* Phép chia nguyên `//` lấy phần nguyên, bỏ dư: `8 // 3 = 2`.

#### Câu 12: Biểu thức `20 / (5 - 5)` sẽ gây ra lỗi gì?
- **A.** `ValueError`
- **B.** `TypeError`
- **C.** **[Đáp án đúng]** `ZeroDivisionError`
- **D.** Không có lỗi
- > *Giải thích:* `5 - 5 = 0`, rồi `20 / 0` gây lỗi chia cho 0.

#### Câu 13: Biểu thức nào sau đây cho kết quả là số thực (float)?
- **A.** `5 + 3`
- **B.** `10 - 2`
- **C.** `4 * 2`
- **D.** **[Đáp án đúng]** `8 / 4`
- > *Giải thích:* Chỉ có phép chia `/` luôn trả về `float`.

#### Câu 14: Kết quả `(6 + 2) / 2` là?
- **A.** 7
- **B.** **[Đáp án đúng]** 4.0
- **C.** 4
- **D.** 7.0
- > *Giải thích:* Tính ngoặc trước: `8 / 2 = 4.0` (float vì là phép chia `/`).

#### Câu 15: Biểu thức `6 + 2 / 2` cho kết quả là?
- **A.** 4.0
- **B.** **[Đáp án đúng]** 7.0
- **C.** 7
- **D.** 4
- > *Giải thích:* Chia trước: `2 / 2 = 1.0`, rồi `6 + 1.0 = 7.0`.

#### Câu 16: `a = 10`, sau đó `a += 7`. Giá trị mới của `a` là?
- **A.** 7
- **B.** 10
- **C.** **[Đáp án đúng]** 17
- **D.** 107
- > *Giải thích:* `a += 7` nghĩa là `a = a + 7 = 10 + 7 = 17`.

#### Câu 17: Kết quả so sánh `5 == 5.0` trong Python là?
- **A.** `False`
- **B.** **[Đáp án đúng]** `True`
- **C.** Báo lỗi
- **D.** `5`
- > *Giải thích:* Python so sánh giá trị, 5 và 5.0 là bằng nhau nên trả về `True`.

#### Câu 18: Biểu thức `True and False` có kết quả là?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `None`
- **D.** Báo lỗi
- > *Giải thích:* `and` yêu cầu cả hai đều True mới cho True. Một trong hai False → kết quả False.

#### Câu 19: `not True` cho kết quả là?
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `0`
- **D.** Báo lỗi
- > *Giải thích:* `not` đảo ngược giá trị bool: `True` biến thành `False`.

#### Câu 20: Cho `x = 5`. Biểu thức nào sau đây đúng để kiểm tra x có lớn hơn 3 không?
- **A.** `x > 3 = True`
- **B.** `x >> 3`
- **C.** **[Đáp án đúng]** `x > 3`
- **D.** `x => 3`
- > *Giải thích:* Toán tử so sánh "lớn hơn" là `>`. Kết quả `x > 3` sẽ là `True`.
