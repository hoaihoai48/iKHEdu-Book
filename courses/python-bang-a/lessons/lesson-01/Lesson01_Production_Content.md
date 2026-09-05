# Bài 01: Lệnh xuất nhập, biến số và kiểu dữ liệu

## 1. Bản chất chương trình máy tính & Luồng dữ liệu I/O

Trong khoa học máy tính và lập trình, một chương trình máy tính thực chất là một **chuỗi các chỉ thị có trật tự** điều khiển phần cứng thực thi để biến đổi dữ liệu đầu vào thành kết quả đầu ra theo yêu cầu bài toán.

Mọi bài toán trong các kỳ thi lập trình đều vận hành nghiêm ngặt theo **luồng dữ liệu 3 bước khép kín (Đầu vào $\to$ Xử lý $\to$ Đầu ra)**:

![Mô hình luồng xử lý I/O](../../assets/l01_io_pipeline.svg?v=1788575106)

1. **Đầu vào:** Nhận dữ liệu do đề bài cung cấp từ bàn phím (luồng dữ liệu chuẩn `stdin`) thông qua lệnh `input()`.
2. **Xử lý:** Dữ liệu được nạp vào bộ nhớ RAM dưới dạng các **biến số**. Bộ vi xử lý (CPU) áp dụng các công thức tính toán, phép biến đổi dữ liệu hoặc thuật toán để tính ra kết quả.
3. **Đầu ra:** Xuất kết quả cuối cùng lên màn hình (luồng dữ liệu chuẩn `stdout`) thông qua lệnh `print()`.

---

## 2. Lệnh xuất dữ liệu `print()` toàn tập

Lệnh `print()` là công cụ cơ bản nhất trong Python dùng để hiển thị dữ liệu ra màn hình. Lệnh này có khả năng in văn bản, in giá trị số học và in trực tiếp kết quả của các biểu thức.

### 2.1. Cú pháp in các loại dữ liệu cơ bản

* **In chuỗi ký tự (Văn bản):** Nội dung bắt buộc phải được đặt trong cặp dấu nháy kép `"` hoặc nháy đơn `'`.
  ```python
  print("Chao mung ban den voi ngon ngu lap trinh Python!")
  ```
* **In giá trị số:** Các con số được viết trực tiếp, tuyệt đối không đặt trong dấu nháy.
  ```python
  print(2026)
  ```
* **In kết quả của phép tính:** Máy tính sẽ tính toán giá trị của biểu thức trước, sau đó in con số kết quả ra màn hình.
  ```python
  print(15 + 25)  # Màn hình hiển thị số 40
  ```

> ⚠️ **Lưu ý phân biệt dấu nháy:**
> - `print("15 + 25")` $\implies$ In ra dòng chữ nguyên bản: `15 + 25`.
> - `print(15 + 25)` $\implies$ Máy tính thực hiện phép cộng và in ra kết quả: `40`.

### 2.2. In nhiều đối số trên một dòng

Trong Python, ta có thể in nhiều món dữ liệu khác nhau trên cùng một dòng bằng cách đặt chúng cách nhau bởi **dấu phẩy `,`**.

```python
diem = 10
print("Diem thi lap trinh cua Minh la:", diem, "diem.")
```
**Kết quả hiển thị trên màn hình:**
```text
Diem thi lap trinh cua Minh la: 10 diem.
```
* **Quy tắc ngầm định của Python:** Khi sử dụng dấu phẩy `,` giữa các đối số, Python sẽ tự động chèn thêm **một khoảng trắng (dấu cách)** vào giữa các món dữ liệu đó.

### 2.3. Hai tham số điều khiển cao cấp: `sep` và `end`

Lệnh `print()` cung cấp hai tham số tùy chỉnh cực kỳ quan trọng thường xuyên gặp trong lập trình:

| Tham Số | Giá Trị Mặc Định | Ý Nghĩa Kỹ Thuật | Ví Dụ Cài Đặt | Kết Quả Hiển Thị |
|---|:---:|---|---|---|
| **`sep`** | `" "` *(Một dấu cách)* | Ký tự dùng để ngăn cách giữa các đối số trên cùng một dòng. | `print(1, 2, 3, sep="-")` | `1-2-3` |
| **`end`** | `"\n"` *(Ký tự xuống dòng)* | Ký tự được in ra ở vị trí cuối cùng sau khi đã in hết các đối số. | `print("A", end=" ")`<br>`print("B")` | `A B` *(Cùng 1 dòng)* |

#### Ví dụ ứng dụng thực tế:
1. **In dãy số liền nhau không có dấu cách:**
   ```python
   print(1, 2, 3, 4, 5, sep="")  # In ra: 12345
   ```
2. **In ngày tháng năm định dạng chuẩn `dd/mm/yyyy`:**
   ```python
   ngay = 4
   thang = 9
   nam = 2026
   print(ngay, thang, nam, sep="/")  # In ra: 4/9/2026
   ```

---

## 3. Biến số và Bản chất Bộ nhớ RAM

### 3.1. Bản chất kỹ thuật của Biến số

Biến số không phải là một con số cố định. Trong khoa học máy tính, **Biến số là tên định danh gán cho một ô nhớ trong bộ nhớ RAM** dùng để lưu trữ dữ liệu trong suốt quá trình chương trình vận hành.

![Bản chất biến số trong RAM](../../assets/l01_variable_ram.svg?v=1788575106)

* **Cú pháp khai báo và gán giá trị:**
  ```python
  ten_bien = gia_tri
  ```
  Dấu `=` ở đây được gọi là **toán tử gán**, không phải là dấu bằng trong toán học.
* **Cơ chế vận hành của toán tử gán `=`:**
  1. Máy tính luôn tính toán giá trị của biểu thức nằm ở **vế bên phải** trước.
  2. Sau khi đã có kết quả cụ thể, máy tính mới nạp giá trị này vào ô nhớ của biến nằm ở **vế bên trái**.

### 3.2. Quy tắc đặt tên biến chuẩn mực

Python kiểm soát quy tắc đặt tên biến rất nghiêm ngặt. Đặt tên biến sai sẽ dẫn đến lỗi cú pháp `SyntaxError`:

| Tiêu Chí | Quy Tắc Bắt Buộc | Tên Hợp Lệ ✅ | Tên Bị Lỗi ❌ (Lý Do) |
|---|---|---|---|
| **Ký tự cho phép** | Chỉ gồm chữ cái tiếng Anh (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới `_`. | `tong`, `so_luong_1` | `so-luong` *(Dấu gạch ngang bị hiểu nhầm là phép trừ)* |
| **Ký tự bắt đầu** | **Bắt buộc** bắt đầu bằng chữ cái hoặc dấu `_`. **Tuyệt đối không bắt đầu bằng chữ số**. | `a1`, `_tong` | `1chieu_dai` *(Bắt đầu bằng chữ số 1)* |
| **Khoảng trắng** | **Không được** chứa dấu cách trong tên biến. | `chieu_dai` | `chieu dai` *(Chứa dấu cách giữa 2 chữ)* |
| **Từ khóa hệ thống** | Không được đặt tên trùng với các từ khóa đã dành riêng của Python. | `my_print`, `so_if` | `print`, `if`, `for`, `while`, `True` |
| **Phân biệt hoa - thường**| Python phân biệt chữ hoa và chữ thường (phân biệt chữ hoa và chữ thường). | `Diem` và `diem` là 2 biến hoàn toàn khác nhau. | |

### 3.3. Cơ chế gán đè và Hoán đổi hai biến

Trong quá trình chạy, biến số có thể thay đổi giá trị nhiều lần. Mỗi lần gán mới, giá trị cũ lưu trong ô nhớ RAM sẽ bị xóa bỏ hoàn toàn:

```python
x = 10     # RAM lưu số 10
x = x + 5  # Máy tính lấy 10 + 5 = 15, sau đó nạp đè 15 vào x
x = 99     # RAM xóa 15, nạp đè số 99 vào x
print(x)   # Màn hình in ra 99
```

#### Kỹ thuật hoán đổi giá trị của hai biến:
Trong toán học hoặc các ngôn ngữ khác, để đổi chỗ hai biến `a` và `b`, ta phải mượn một biến trung gian `tam`. Tuy nhiên, Python cung cấp cú pháp gán đồng thời (đóng gói và mở gói dữ liệu) cực kỳ ngắn gọn:
```python
a = 5
b = 10
# Hoán đổi giá trị giữa a và b trên cùng một dòng:
a, b = b, a
print(a, b)  # Màn hình in ra: 10 5
```

---

## 4. Các kiểu dữ liệu cơ bản trong Python

Máy tính cần biết dữ liệu thuộc loại nào để phân bổ dung lượng bộ nhớ RAM và áp dụng các phép toán tương ứng. Python quản lý các kiểu dữ liệu cốt lõi sau:

| Kiểu Dữ Liệu | Tên Trong Python | Ý Nghĩa & Bản Chất | Ví Dụ Giá Trị | Thao Tác / Ứng Dụng |
|:---:|:---:|---|---|:---:|
| **Số nguyên** | `int` | Tập hợp các số nguyên $\mathbb{Z}$ (âm, dương, số 0). Trong Python, số nguyên có thể dài hàng nghìn chữ số mà không lo bị tràn số. | `-15`, `0`, `42`, `1000000` | Thực hiện đầy đủ các phép tính số học: `+`, `-`, `*`, `//`, `%`, `**` |
| **Số thực** | `float` | Tập hợp các số thập phân có dấu chấm `.`. | `3.14`, `-0.5`, `2.0` | Thực hiện các phép tính số học và làm tròn số |
| **Chuỗi ký tự** | `str` | Dãy các ký tự văn bản đặt trong dấu nháy kép hoặc nháy đơn. | `"Ha Noi"`, `'2026'`, `"A"` | Dấu `+` dùng để nối chuỗi, dấu `*` dùng để lặp lại chuỗi |
| **Kiểu dữ liệu logic** | `bool` | Chỉ gồm đúng hai trạng thái: Đúng hoặc Sai. | `True`, `False` | Dùng làm điều kiện trong rẽ nhánh và vòng lặp |
| **Danh sách** | `list` | Tập hợp gồm nhiều phần tử được xếp thứ tự trong cặp ngoặc vuông `[ ]`. | `[1, 2, 3]`, `["An", "Binh"]` | Lưu trữ dãy số, bảng điểm; giới thiệu mở đầu, học sâu tại Bài 11 |

* **Kiểm tra kiểu dữ liệu với hàm `type()`:**
  ```python
  print(type(100))        # Kết quả: <class 'int'>
  print(type(3.14))       # Kết quả: <class 'float'>
  print(type("Python"))   # Kết quả: <class 'str'>
  print(type(True))       # Kết quả: <class 'bool'>
  print(type([1, 2, 3]))  # Kết quả: <class 'list'>
  ```

---

## 5. Lệnh nhập dữ liệu `input()` & Đổi kiểu dữ liệu

### 5.1. Bí mật sống còn: `input()` luôn trả về kiểu Chuỗi (`str`)

Lệnh `input()` tạm dừng chương trình và chờ người dùng nhập một dòng văn bản từ bàn phím, kết thúc khi nhấn phím `Enter`.

![Bí mật đổi kiểu dữ liệu](../../assets/l01_type_casting.svg?v=1788575106)

> ❌ **LỖI KINH ĐIỂN CỦA HỌC SINH:**
> Nếu viết mã như sau:
> ```python
> a = input()  # Học sinh nhập số 5 từ bàn phím
> b = input()  # Học sinh nhập số 3 từ bàn phím
> print(a + b)
> ```
> Màn hình sẽ **KHÔNG IN RA 8**, mà in ra: `53`!
> 
> **Nguyên nhân:** Vì `input()` luôn đọc dữ liệu vào dưới dạng chuỗi ký tự (`str`), nên biến `a` thực chất lưu chữ `"5"` và biến `b` lưu chữ `"3"`. Toán tử `+` khi áp dụng trên chuỗi sẽ thực hiện thao tác **ghép dính chuỗi lại với nhau**: `"5" + "3" = "53"`.

### 5.2. Kỹ thuật đổi kiểu sang số nguyên `int()` và số thực `float()`

Để máy tính hiểu rằng đây là các con số cần tính toán, ta bắt buộc phải đưa dữ liệu chuỗi qua **chuyển đổi kiểu dữ liệu**:

* **Đổi kiểu nhập số nguyên:**
  ```python
  n = int(input())
  ```
* **Đổi kiểu nhập số thực:**
  ```python
  x = float(input())
  ```

#### Chương trình chuẩn mực nhập 2 số nguyên và in tổng:
```python
# Bước 1: Nhập dữ liệu và đổi kiểu dữ liệu
a = int(input())
b = int(input())

# Bước 2: Tính toán
tong = a + b

# Bước 3: Xuất kết quả
print(tong)
```

### 5.3. Kỹ thuật nhập nhiều số trên cùng một dòng (`split`)

Trong đề thi lập trình, dữ liệu đầu vào thường được đặt trên cùng một dòng, cách nhau bởi dấu cách (Ví dụ: dòng 1 chứa 2 số nguyên $A$ và $B$). Nếu dùng hai lệnh `input()` rời rạc, chương trình sẽ đọc nhầm dòng tiếp theo.

* **Cú pháp chuẩn mực đọc 2 số nguyên trên cùng một dòng:**
  ```python
  a, b = map(int, input().split())
  ```
  - `input()`: Đọc trọn vẹn cả dòng dữ liệu văn bản.
  - `.split()`: Cắt dòng văn bản thành các mẩu chuỗi nhỏ dựa theo dấu cách.
  - `map(int, ...)`: Tự động đem từng mẩu chuỗi đó chuyển sang kiểu số nguyên `int`.
  - `a, b = ...`: Lần lượt nạp 2 số nguyên vào 2 biến `a` và `b`.

---

## 6. Bảng mô phỏng biến thiên ô nhớ qua từng bước

Xét đoạn chương trình sau:
```python
a = int(input())   # Nhập 12
b = int(input())   # Nhập 8
hieu = a - b
a = a + 10
tong = a + b
```

### Bảng theo dõi giá trị biến trong bộ nhớ RAM qua từng dòng lệnh:

| Thứ Tự | Dòng Lệnh Thực Thi | Thao Tác Máy Tính Thực Hiện | Biến `a` trong RAM | Biến `b` trong RAM | Biến `hieu` | Biến `tong` |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **1** | `a = int(input())` | Đọc chuỗi `"12"`, ép sang số nguyên `12`, nạp vào `a` | **12** | Chưa có | Chưa có | Chưa có |
| **2** | `b = int(input())` | Đọc chuỗi `"8"`, ép sang số nguyên `8`, nạp vào `b` | 12 | **8** | Chưa có | Chưa có |
| **3** | `hieu = a - b` | Tính $12 - 8 = 4$, nạp vào biến `hieu` | 12 | 8 | **4** | Chưa có |
| **4** | `a = a + 10` | Đọc $a = 12$, tính $12 + 10 = 22$, ghi đè vào biến `a` | **22** | 8 | 4 | Chưa có |
| **5** | `tong = a + b` | Đọc $a = 22, b = 8$, tính $22 + 8 = 30$, nạp vào `tong` | 22 | 8 | 4 | **30** |

---

## 7. Tử huyệt và Các bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: IN THỪA CÂU CHỮ TRONG lập trình**
> * **Đoạn code sai lầm:**
>   ```python
>   n = int(input("Moi ban nhap vao so n: "))
>   print("Ket qua la:", n * 2)
>   ```
> * **Hậu quả:** chương trình so sánh từng ký tự đầu ra. Việc in các thông báo như `"Moi ban nhap..."` hoặc `"Ket qua la: "` sẽ khiến kết quả bị sai lệch và nhận ngay 0 điểm.
> * **Cách viết đúng phổ biến:**
>   ```python
>   n = int(input())
>   print(n * 2)
>   ```

> ❌ **BẪY LỖI 2: ĐẶT TÊN BIẾN SAI QUY TẮC**
> * Viết `2_ban = 10` $\implies$ Báo lỗi `SyntaxError: invalid decimal literal` (Không được bắt đầu bằng chữ số).
> * Viết `diem toan = 9` $\implies$ Báo lỗi `SyntaxError: invalid syntax` (Không được chứa khoảng trắng).
> * **Cách sửa chuẩn:** Đặt là `ban_2 = 10` và `diem_toan = 9`.

> ❌ **BẪY LỖI 3: QUÊN ĐỔI KIỂU DỮ LIỆU KHI ĐỌC SỐ**
> * Viết `x = input()`, sau đó tính `y = x - 5` $\implies$ Báo lỗi `TypeError: unsupported operand type(s) for -: 'str' and 'int'`. Chuỗi không thể thực hiện phép trừ với số nguyên.

---

## 8. Mẫu code thường gặp

```python
# Mẫu 1: Nhập 2 số trên 2 dòng riêng biệt và in tổng
a = int(input())
b = int(input())
print(a + b)

# Mẫu 2: Nhập 2 số trên cùng 1 dòng cách nhau dấu cách và in tổng
x, y = map(int, input().split())
print(x + y)
```

---

## 9. Concept Quiz: 15 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Nhận diện cú pháp):
Lệnh nào sau đây dùng để hiển thị giá trị của biến `k` lên màn hình máy tính?
- **A.** `input(k)`
- **B.** **[Đáp án đúng]** `print(k)`
- **C.** `read(k)`
- **D.** `echo(k)`
> *Giải thích:* Lệnh `print()` có chức năng in dữ liệu ra màn hình.

#### Câu 2 (Dự đoán output — Dấu phẩy trong lệnh `print`):
Đoạn code sau đây sẽ in ra màn hình nội dung gì?
```python
x = "Tin"
y = "Hoc"
print(x, y)
```
- **A.** `TinHoc`
- **B.** **[Đáp án đúng]** `Tin Hoc`
- **C.** `x y`
- **D.** `x, y`
> *Giải thích:* Dấu phẩy giữa các đối số trong hàm `print()` sẽ tự động chèn một khoảng trắng vào giữa.

#### Câu 3 (Dự đoán output — Cộng chuỗi vs Cộng số):
Đoạn code sau đây sẽ in ra kết quả gì?
```python
m = input()
n = input()
print(m + n)
```
(Giả sử người dùng nhập vào dòng 1 là `10` và dòng 2 là `20`).
- **A.** `30`
- **B.** **[Đáp án đúng]** `1020`
- **C.** Báo lỗi `TypeError`
- **D.** `m + n`
> *Giải thích:* `input()` không ép kiểu sẽ lưu trữ dữ liệu dạng chuỗi (`str`). Phép `+` giữa hai chuỗi sẽ nối chúng lại thành `"1020"`.

#### Câu 4 (Bản chất biến số — Gán đè):
Sau khi thực hiện chuỗi lệnh sau, giá trị cuối cùng của biến `a` là bao nhiêu?
```python
a = 5
b = 10
a = a + b
a = 100
```
- **A.** `15`
- **B.** `115`
- **C.** **[Đáp án đúng]** `100`
- **D.** `5`
> *Giải thích:* Lệnh cuối cùng gán đè `a = 100`, mọi giá trị tính toán trước đó của `a` đều bị hủy bỏ.

#### Câu 5 (Bắt bẫy quy tắc — Tên biến hợp lệ):
Tên biến nào sau đây là **HOÀN TOÀN HỢP LỆ** trong Python?
- **A.** `1_diem_toan`
- **B.** `chieu dai`
- **C.** `so-hoc`
- **D.** **[Đáp án đúng]** `_chieu_dai_1`
> *Giải thích:* Tên biến có thể bắt đầu bằng dấu gạch dưới `_`, không được bắt đầu bằng chữ số (loại A), không chứa dấu cách (loại B), không chứa dấu trừ (loại C).

#### Câu 6 (Bản chất ép kiểu):
Để đọc một số thực $X$ từ bàn phím và lưu vào biến, câu lệnh chuẩn xác nhất là gì?
- **A.** `X = input()`
- **B.** `X = int(input())`
- **C.** **[Đáp án đúng]** `X = float(input())`
- **D.** `X = str(input())`
> *Giải thích:* Kiểu số thực trong Python được ép bằng hàm `float()`.

#### Câu 7 (Dự đoán output — Tham số `sep`):
Đoạn code sau sẽ in ra màn hình kết quả gì?
```python
print("20", "11", "2026", sep="-")
```
- **A.** `20 11 2026`
- **B.** **[Đáp án đúng]** `20-11-2026`
- **C.** `20-11-2026-`
- **D.** `20112026`
> *Giải thích:* Tham số `sep="-"` quy định ký tự nằm giữa các đối số là dấu gạch nối.

#### Câu 8 (Dự đoán output — Tham số `end`):
Đoạn code sau đây sẽ in ra nội dung gì?
```python
print("Lop 4A", end=" ")
print("Vo dich!")
```
- **A.** Hai dòng: Dòng 1 `Lop 4A`, Dòng 2 `Vo dich!`
- **B.** **[Đáp án đúng]** Một dòng: `Lop 4A Vo dich!`
- **C.** `Lop 4AVo dich!`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Tham số `end=" "` thay thế ký tự xuống dòng mặc định bằng một khoảng trắng, khiến lệnh in tiếp theo nối liền trên cùng dòng.

#### Câu 9 (Bản chất bộ nhớ — Hoán đổi biến):
Cho hai biến `a = 3`, `b = 7`. Sau khi chạy lệnh `a, b = b, a`, giá trị của `a` và `b` lần lượt là:
- **A.** `a = 3, b = 7`
- **B.** **[Đáp án đúng]** `a = 7, b = 3`
- **C.** `a = 7, b = 7`
- **D.** `a = 3, b = 3`
> *Giải thích:* Lệnh `a, b = b, a` thực hiện hoán đổi đồng thời giá trị giữa 2 biến.

#### Câu 10 (Nhận diện kiểu dữ liệu):
Hàm `type(15.0)` sẽ trả về kết quả nào?
- **A.** `<class 'int'>`
- **B.** **[Đáp án đúng]** `<class 'float'>`
- **C.** `<class 'str'>`
- **D.** `<class 'number'>`
> *Giải thích:* Số có dấu chấm thập phân `.0` luôn thuộc kiểu số thực `float`.

#### Câu 11 (Bắt bẫy cú pháp — Từ khóa hệ thống):
Vì sao ta không nên đặt tên biến là `print = 10`?
- **A.** Máy tính sẽ báo lỗi cú pháp ngay lập tức.
- **B.** **[Đáp án đúng]** Tên biến sẽ ghi đè lên hàm `print()` có sẵn của hệ thống, khiến từ sau đó không thể dùng lệnh `print()` để in được nữa.
- **C.** Không ảnh hưởng gì cả.
- **D.** Giá trị của biến sẽ tự động chuyển thành chuỗi.
> *Giải thích:* `print` là tên hàm dựng sẵn, nếu gán đè biến mang tên `print`, ta sẽ làm mất chức năng in ấn.

#### Câu 12 (Dự đoán output — Nhập 1 dòng nhiều biến):
Người dùng nhập từ bàn phím một dòng duy nhất: `5 12`.
Đoạn code sau:
```python
x, y = map(int, input().split())
print(x * y)
```
sẽ in ra kết quả là:
- **A.** `5 12`
- **B.** `512`
- **C.** **[Đáp án đúng]** `60`
- **D.** Báo lỗi `ValueError`
> *Giải thích:* `map(int, input().split())` tách được $x = 5$ và $y = 12$. Phép nhân $5 \times 12 = 60$.

#### Câu 13 (Bắt bẫy kiểu dữ liệu Boolean):
Giá trị nào sau đây biểu diễn giá trị logic Đúng trong Python?
- **A.** `true`
- **B.** **[Đáp án đúng]** `True`
- **C.** `"True"`
- **D.** `1.0`
> *Giải thích:* Python viết hoa chữ cái đầu tiên của từ khóa Boolean: `True` và `False`. Viết thường `true` sẽ bị báo lỗi chưa định nghĩa biến.

#### Câu 14 (Dự đoán output — Nhân bản chuỗi):
Đoạn code sau đây sẽ in ra màn hình kết quả gì?
```python
chuoi = "Ba"
print(chuoi * 3)
```
- **A.** Báo lỗi `TypeError` vì không thể nhân chữ với số.
- **B.** **[Đáp án đúng]** `BaBaBa`
- **C.** `Ba 3`
- **D.** `9`
> *Giải thích:* Trong Python, toán tử `*` giữa chuỗi và số nguyên dương sẽ nhân bản chuỗi đó nhiều lần liên tiếp.

#### Câu 15 (Tư duy lập trình):
Khi đề bài yêu cầu in ra tổng của 2 số, cách viết nào sau đây là gọn gàng nhất?
- **A.** `print("Tong 2 so la:", a + b)`
- **B.** `print("Ket qua =", a + b)`
- **C.** **[Đáp án đúng]** `print(a + b)`
- **D.** `print("a + b =", a + b)`
> *Giải thích:* Luôn in ra chính xác đáp số đầu ra theo đúng định dạng đề bài yêu cầu, tuyệt đối không in thừa bất kỳ thông báo giải thích nào.
