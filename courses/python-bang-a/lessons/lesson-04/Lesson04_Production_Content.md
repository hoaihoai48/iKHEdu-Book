# Bài 04: Rẽ nhánh có điều kiện với if-else

---

## 1. Khởi động: Khi robot biết đưa ra quyết định

Ở các bài học trước, bạn Robot của chúng ta chỉ biết làm việc theo một đường thẳng tắp: làm việc 1 rồi đến việc 2, việc 3.
Thế nhưng trong thế giới thực, cuộc sống luôn có những **ngã rẽ quyết định**:
* **NẾU** trời mưa **THÌ** em mang ô, **NGƯỢC LẠI** thì em đội mũ nón.
* **NẾU** điểm thi của em $\ge 9$ **THÌ** được khen thưởng, **NGƯỢC LẠI** thì phải cố gắng hơn.
* **NẾU** đèn giao thông màu đỏ **THÌ** dừng lại, **NGƯỢC LẠI** thì được đi tiếp.

Trong lập trình, cấu trúc giúp Robot có khả năng "suy nghĩ và lựa chọn" chính là **Cấu trúc rẽ nhánh `if - else`**!

---

## 2. Các phép toán so sánh trong Python: Chiếc cân công lý

Để Robot biết được một điều gì đó là **ĐÚNG (True)** hay **SAI (False)**, chúng ta sử dụng **các phép so sánh**:

| Ký hiệu Python | Tên phép so sánh | Ví dụ minh họa | Kết quả | Ý nghĩa bản chất |
|:---:|---|:---:|:---:|---|
| `==` | **Bằng nhau** | `5 == 5` | `True` | **Dùng 2 dấu bằng `==`!** (1 dấu `=` là phép gán) |
| `!=` | **Khác nhau** | `5 != 3` | `True` | Dấu chấm than `!` mang ý nghĩa là "Không" |
| `>` | **Lớn hơn** | `7 > 4` | `True` | So sánh giá trị bên trái lớn hơn bên phải |
| `<` | **Nhỏ hơn** | `3 < 2` | `False` | So sánh giá trị bên trái nhỏ hơn bên phải |
| `>=` | **Lớn hơn hoặc bằng** | `6 >= 6` | `True` | Chỉ cần lớn hơn HOẶC bằng là đúng |
| `<=` | **Nhỏ hơn hoặc bằng** | `4 <= 5` | `True` | Chỉ cần nhỏ hơn HOẶC bằng là đúng |

> ⚠️ **Tử huyệt bắt bẫy số 1:**
> * `a = 5`: Nghĩa là cất số 5 vào chiếc hộp tên là `a` (Phép gán).
> * `a == 5`: Nghĩa là hỏi máy tính *"Giá trị trong hộp `a` có bằng số 5 hay không?"* (Phép so sánh).
> Viết nhầm `if a = 5:` sẽ bị Python "phạt thẻ đỏ" ngay lập tức (`SyntaxError`)!

---

## 3. Cú pháp `if - else` & quy tắc thụt lề thần thánh (indentation)

### 3.1. Cú pháp chuẩn
```python
if <Điều kiện>:
    # Khối lệnh chạy khi điều kiện ĐÚNG (True)
else:
    # Khối lệnh chạy khi điều kiện SAI (False)
```

### 3.2. Quy tắc thụt lề (indentation rule) — trái tim của Python!
Trong Python, máy tính phân biệt câu lệnh nào thuộc về `if`, câu lệnh nào thuộc về `else` bằng cách **THỤT LỀ VÀO TRONG (thường là 4 dấu cách hoặc 1 phím Tab)**.

```python
diem = 9

if diem >= 5:
    print("Chuc mung!")
    print("Ban da vuot qua bai kiem tra!")
else:
    print("Rat tiec!")
    print("Ban can co gang hon o lan sau.")

print("Ket thuc chuong trinh.") # Câu lệnh này không thụt lề, lúc nào cũng chạy!
```

* **Dấu hai chấm `:`**: Bắt buộc phải có ở cuối dòng `if` và dòng `else`. Dấu hai chấm giống như cánh cửa mở ra một căn phòng chứa các câu lệnh thụt lề bên trong.
* Nếu quên dấu hai chấm `:` hoặc quên thụt lề, Python sẽ báo lỗi `IndentationError` ngay lập tức.

---

## 4. Các dạng bài toán rẽ nhánh kinh điển

### Dạng 1: Kiểm tra số chẵn lẻ
```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```

### Dạng 2: Tìm số lớn nhất (max) giữa 2 số $a$ và $b$
```python
a = int(input())
b = int(input())

if a > b:
    so_lon = a
else:
    so_lon = b

print("So lon nhat la:", so_lon)
```
*(Hoặc dùng hàm có sẵn siêu tốc của Python: `print(max(a, b))`)*.

---

## 5. Bảng tổng kết bẫy lỗi bài 4

| Lỗi sai thường gặp | Thông báo lỗi của Python | Nguyên nhân | Cách khắc phục |
|---|---|---|---|
| `if a = 10:` | `SyntaxError: invalid syntax` | Dùng 1 dấu `=` trong điều kiện | Sửa thành `if a == 10:` |
| `if a > 0` | `SyntaxError: expected ':'` | Quên dấu hai chấm `:` ở cuối | Sửa thành `if a > 0:` |
| `if a > 0:` <br> `print("Duong")` | `IndentationError: expected an indented block` | Quên nhấn phím Tab/thụt lề | Thụt dòng `print` vào 1 khoảng cách |

---

## 6. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép toán nào sau đây dùng để so sánh hai giá trị có bằng nhau không trong Python?
- **A.** `=`
- **B.** **[Đáp án đúng]** `==`
- **C.** `===`
- **D.** `equal`
> *Giải thích:* Trong Python, `==` là phép so sánh bằng, còn `=` là phép gán giá trị.

#### Câu 2: Kết quả của biểu thức so sánh `10 != 10` là:
- **A.** `True`
- **B.** **[Đáp án đúng]** `False`
- **C.** `10`
- **D.** Báo lỗi
> *Giải thích:* `!=` là phép so sánh khác. Vì $10$ bằng $10$, nên khẳng định $10$ khác $10$ là sai (`False`).

#### Câu 3: Ký tự bắt buộc phải có ở cuối dòng lệnh `if` và `else` là:
- **A.** Dấu chấm phẩy `;`
- **B.** **[Đáp án đúng]** Dấu hai chấm `:`
- **C.** Dấu chấm `.`
- **D.** Dấu mũi tên `->`
> *Giải thích:* Python quy định sau điều kiện `if` và sau từ khóa `else` bắt buộc phải có dấu hai chấm `:`.

#### Câu 4: Đoạn code sau sẽ in ra gì?
```python
x = 7
if x > 5:
    print("A")
else:
    print("B")
```
- **A.** `B`
- **B.** **[Đáp án đúng]** `A`
- **C.** Cả `A` và `B`
- **D.** Không in gì cả
> *Giải thích:* Vì $7 > 5$ là đúng (`True`), máy tính thực hiện khối lệnh của `if`, in ra `A`.

#### Câu 5: Đoạn code sau gặp lỗi gì?
```python
tuoi = 8
if tuoi >= 6:
print("Vao lop 1")
```
- **A.** `SyntaxError`
- **B.** **[Đáp án đúng]** `IndentationError`
- **C.** `TypeError`
- **D.** `NameError`
> *Giải thích:* Lệnh `print` dưới `if` không được thụt lề vào trong, vi phạm quy tắc Indentation của Python.

#### Câu 6: Biểu thức kiểm tra số tự nhiên $A$ có chia hết cho 3 hay không là:
- **A.** `A / 3 == 0`
- **B.** `A // 3 == 0`
- **C.** **[Đáp án đúng]** `A % 3 == 0`
- **D.** `A % 3 != 0`
> *Giải thích:* $A$ chia hết cho 3 khi và chỉ khi phần dư bằng 0: `A % 3 == 0`.

#### Câu 7: Đoạn code sau in ra gì khi nhập $n = 10$?
```python
n = int(input())
if n % 2 == 0:
    print("Chan")
print("Xong")
```
- **A.** `Chan`
- **B.** **[Đáp án đúng]** `Chan` và `Xong` (trên 2 dòng)
- **C.** `Xong`
- **D.** Báo lỗi
> *Giải thích:* Vì $10$ là số chẵn nên in `Chan`. Dòng `print("Xong")` không thụt lề nên là lệnh độc lập, luôn được thực thi.

#### Câu 8: Khi nào thì khối lệnh bên trong `else:` được thực thi?
- **A.** Luôn luôn được thực thi
- **B.** **[Đáp án đúng]** Khi điều kiện trong `if` có giá trị là `False`
- **C.** Khi điều kiện trong `if` có giá trị là `True`
- **D.** Khi chương trình xảy ra lỗi
> *Giải thích:* Khối `else` chỉ chạy khi điều kiện của `if` bị sai (`False`).

#### Câu 9: Trong Python, biểu thức so sánh `5 >= 5` trả về giá trị gì?
- **A.** **[Đáp án đúng]** `True`
- **B.** `False`
- **C.** `5`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phép so sánh lớn hơn hoặc bằng `>=` thỏa mãn khi số bên trái bằng số bên phải.

#### Câu 10: Đoạn code nào tìm giá trị nhỏ nhất giữa 2 số $a$ và $b$ đúng chuẩn?
- **A.** `if a < b: min_val = b else: min_val = a`
- **B.** **[Đáp án đúng]** `if a < b: min_val = a else: min_val = b`
- **C.** `min_val = a > b`
- **D.** `if a == b: min_val = a`
> *Giải thích:* Nếu $a < b$ thì $a$ là số nhỏ hơn, ngược lại $b$ là số nhỏ hơn.

#### Câu 11: Cho đoạn code sau:
```python
a = 15
if a % 5 == 0:
    a = a + 5
else:
    a = a - 5
print(a)
```
Giá trị in ra màn hình là:
- **A.** `10`
- **B.** `15`
- **C.** **[Đáp án đúng]** `20`
- **D.** `25`
> *Giải thích:* $15$ chia hết cho $5$ ($15 \% 5 == 0$ là `True`), nên thực hiện `a = a + 5 = 20`.

#### Câu 12: Điều gì xảy ra nếu viết `if (a = 5):` trong Python?
- **A.** Máy hiểu là so sánh `a` với 5.
- **B.** **[Đáp án đúng]** Báo lỗi `SyntaxError: invalid syntax`.
- **C.** Gán `a = 5` rồi luôn chạy nhánh `if`.
- **D.** In ra số 5.
> *Giải thích:* Python cấm dùng toán tử gán `=` bên trong điều kiện của lệnh `if`.

#### Câu 13: Có bao nhiêu dấu cách (spaces) chuẩn thường dùng để thụt lề trong Python?
- **A.** 1 dấu cách
- **B.** 2 dấu cách
- **C.** **[Đáp án đúng]** 4 dấu cách (hoặc 1 lần nhấn phím Tab)
- **D.** 8 dấu cách
> *Giải thích:* Chuẩn PEP 8 của Python quy định thụt lề chuẩn là 4 dấu cách.

#### Câu 14: Lệnh `else` có thể đứng một mình mà không có `if` ở trước không?
- **A.** Được phép
- **B.** **[Đáp án đúng]** Không được phép (Báo lỗi `SyntaxError`)
- **C.** Chỉ được phép khi có vòng lặp
- **D.** Tùy trường hợp
> *Giải thích:* `else` là nhánh phủ định bắt buộc phải đi kèm với một cấu trúc điều kiện `if` trước đó.

#### Câu 15: Kết quả của đoạn code sau:
```python
diem = 10
if diem == 10:
    print("Xuat sac")
if diem >= 8:
    print("Gioi")
```
- **A.** Chỉ in `Xuat sac`
- **B.** Chỉ in `Gioi`
- **C.** **[Đáp án đúng]** In cả hai dòng: `Xuat sac` và `Gioi`
- **D.** Báo lỗi
> *Giải thích:* Đây là hai lệnh `if` độc lập nhau. Cả hai điều kiện đều thỏa mãn nên cả hai câu lệnh đều được thực thi!
