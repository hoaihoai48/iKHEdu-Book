# Bài 01: Lệnh xuất nhập, biến số và kiểu dữ liệu

## 1. Bản chất chương trình máy tính & Luồng dữ liệu I/O

Các em thân mến, một chương trình máy tính chính là một **chuỗi các chỉ thị có trật tự**, điều khiển phần cứng để biến đổi dữ liệu đầu vào thành kết quả đầu ra theo yêu cầu của bài tập.

Mọi bài tập đều chạy khép kín theo **luồng 3 bước (Đầu vào $\to$ Xử lý $\to$ Đầu ra)**:

![Mô hình luồng xử lý I/O](../../assets/l01_io_pipeline.svg?v=1788575106)

1. **Đầu vào:** Nhận dữ liệu từ bàn phím (luồng dữ liệu chuẩn `stdin`) bằng lệnh `input()`.
2. **Xử lý:** Dữ liệu được đưa vào bộ nhớ dưới dạng các **biến số**. Bộ vi xử lý áp dụng công thức tính toán để tìm ra kết quả.
3. **Đầu ra:** Đưa kết quả lên màn hình (luồng dữ liệu chuẩn `stdout`) bằng lệnh `print()`.

---

## 2. Lệnh xuất dữ liệu `print()` toàn tập

Lệnh `print()` dùng để hiển thị dữ liệu ra màn hình: văn bản, số và kết quả của biểu thức.

### 2.1. Cú pháp in các loại dữ liệu cơ bản

* **In chuỗi ký tự (Văn bản):** Nội dung đặt trong cặp dấu nháy kép `"` hoặc nháy đơn `'`.
 ```python
  print("Chao mung ban den voi ngon ngu lap trinh Python!")
  ```
* **In giá trị số:** Các con số viết trực tiếp, không đặt trong dấu nháy.
 ```python
  print(2026)
  ```
* **In kết quả của phép tính:** Máy tính tính giá trị biểu thức trước, rồi in kết quả ra màn hình.
 ```python
  print(15 + 25)  # Màn hình hiển thị số 40
  ```

> **Lưu ý phân biệt dấu nháy:**
> - `print("15 + 25")` $\implies$ In ra dòng chữ nguyên bản: `15 + 25`.
> - `print(15 + 25)` $\implies$ Máy tính thực hiện phép cộng và in ra kết quả: `40`.

### 2.2. In nhiều đối số trên một dòng

Ta in nhiều món dữ liệu trên cùng một dòng bằng cách ngăn chúng bởi **dấu phẩy `,`**.

```python
diem = 10
print("Diem thi lap trinh cua Minh la:", diem, "diem.")
```
**Kết quả hiển thị trên màn hình:**
```text
Diem thi lap trinh cua Minh la: 10 diem.
```
* **Quy tắc ngầm định của Python:** Khi dùng dấu phẩy `,` giữa các đối số, Python tự chèn thêm **một khoảng trắng (dấu cách)** vào giữa các món dữ liệu đó.

### 2.3. Hai tham số điều khiển cao cấp: `sep` và `end`

Lệnh `print()` có hai tham số tùy chỉnh rất hay gặp khi làm bài:

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

Các em nhớ nhé: **biến số là tên gọi của một ô nhớ trong bộ nhớ**, dùng để giữ dữ liệu trong lúc chương trình chạy.

![Bản chất biến số trong RAM](../../assets/l01_variable_ram.svg?v=1788575106)

* **Cú pháp khai báo và gán giá trị:**
 ```python
  ten_bien = gia_tri
  ```
 Dấu `=` ở đây gọi là **toán tử gán**, khác với dấu bằng trong toán học.
* **Cơ chế của toán tử gán `=`:**
 1. Máy tính tính giá trị của biểu thức ở **vế bên phải** trước.
 2. Rồi nạp kết quả vào ô nhớ của biến ở **vế bên trái**.

### 3.2. Quy tắc đặt tên biến chuẩn mực

Đặt tên sai sẽ bị lỗi cú pháp `SyntaxError`, các em cẩn thận nhé:

| Tiêu Chí | Quy Tắc Bắt Buộc | Tên Hợp Lệ | Tên Bị Lỗi (Lý Do) |
|---|---|---|---|
| **Ký tự cho phép** | Chỉ gồm chữ cái tiếng Anh (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới `_`. | `tong`, `so_luong_1` | `so-luong` *(Dấu gạch ngang bị hiểu nhầm là phép trừ)* |
| **Ký tự bắt đầu** | **Bắt buộc** bắt đầu bằng chữ cái hoặc dấu `_`. **Tuyệt đối không bắt đầu bằng chữ số**. | `a1`, `_tong` | `1chieu_dai` *(Bắt đầu bằng chữ số 1)* |
| **Khoảng trắng** | **Không được** chứa dấu cách trong tên biến. | `chieu_dai` | `chieu dai` *(Chứa dấu cách giữa 2 chữ)* |
| **Từ khóa hệ thống** | Không được đặt tên trùng với các từ khóa đã dành riêng của Python. | `my_print`, `so_if` | `print`, `if`, `for`, `while`, `True` |
| **Phân biệt hoa - thường**| Python phân biệt chữ hoa và chữ thường (phân biệt chữ hoa và chữ thường). | `Diem` và `diem` là 2 biến hoàn toàn khác nhau. | |

### 3.3. Cơ chế gán đè và Hoán đổi hai biến

Biến có thể đổi giá trị nhiều lần. Mỗi lần gán mới, giá trị cũ trong ô nhớ sẽ bị xóa hẳn:

```python
x = 10     # RAM lưu số 10
x = x + 5  # Máy tính lấy 10 + 5 = 15, sau đó nạp đè 15 vào x
x = 99     # RAM xóa 15, nạp đè số 99 vào x
print(x)   # Màn hình in ra 99
```

#### Kỹ thuật hoán đổi giá trị của hai biến:
Muốn đổi chỗ hai biến `a` và `b`, Python cho phép gán đồng thời rất gọn:
```python
a = 5
b = 10
# Hoán đổi giá trị giữa a và b trên cùng một dòng:
a, b = b, a
print(a, b)  # Màn hình in ra: 10 5
```

---

## 4. Các kiểu dữ liệu cơ bản trong Python

Máy tính cần biết dữ liệu thuộc loại nào để xếp chỗ trong bộ nhớ và chọn phép tính phù hợp:

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

Lệnh `input()` dừng chương trình để chờ ta gõ một dòng chữ từ bàn phím, rồi kết thúc khi ta nhấn phím `Enter`.

![Bí mật đổi kiểu dữ liệu](../../assets/l01_type_casting.svg?v=1788575106)

> **LỖI KINH ĐIỂN CỦA HỌC SINH:**
> Nếu viết mã như sau:
> ```python
> a = input()  # Học sinh nhập số 5 từ bàn phím
> b = input()  # Học sinh nhập số 3 từ bàn phím
> print(a + b)
> ```
> Màn hình sẽ **KHÔNG IN RA 8**, mà in ra: `53`!
>
> **Nguyên nhân:** Vì `input()` luôn đọc dữ liệu vào dưới dạng chuỗi ký tự (`str`), nên biến `a` giữ chữ `"5"` và biến `b` giữ chữ `"3"`. Dấu `+` với chuỗi sẽ **ghép dính chuỗi lại với nhau**: `"5" + "3" = "53"`.

### 5.2. Kỹ thuật đổi kiểu sang số nguyên `int()` và số thực `float()`

Muốn máy tính tính toán đúng, ta phải đổi chuỗi chữ thành số:

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

Khi làm bài, các số thường nằm chung một dòng và ngăn nhau bằng dấu cách (ví dụ: dòng 1 có 2 số $A$ và $B$). Dùng hai lệnh `input()` rời nhau sẽ đọc nhầm dòng.

* **Cú pháp chuẩn mực đọc 2 số nguyên trên cùng một dòng:**
 ```python
  a, b = map(int, input().split())
  ```
 - `input()`: Đọc trọn vẹn cả dòng văn bản.
 - `.split()`: Cắt dòng văn bản thành các mẩu nhỏ theo dấu cách.
 - `map(int, ...)`: Đổi từng mẩu chữ sang số nguyên `int`.
 - `a, b = ...`: Nạp 2 số nguyên vào 2 biến `a` và `b`.

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

### Bảng theo dõi giá trị biến trong bộ nhớ qua từng dòng lệnh:

| Thứ Tự | Dòng Lệnh Thực Thi | Thao Tác Máy Tính Thực Hiện | Biến `a` trong RAM | Biến `b` trong RAM | Biến `hieu` | Biến `tong` |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **1** | `a = int(input())` | Đọc chuỗi `"12"`, ép sang số nguyên `12`, nạp vào `a` | **12** | Chưa có | Chưa có | Chưa có |
| **2** | `b = int(input())` | Đọc chuỗi `"8"`, ép sang số nguyên `8`, nạp vào `b` | 12 | **8** | Chưa có | Chưa có |
| **3** | `hieu = a - b` | Tính $12 - 8 = 4$, nạp vào biến `hieu` | 12 | 8 | **4** | Chưa có |
| **4** | `a = a + 10` | Đọc $a = 12$, tính $12 + 10 = 22$, ghi đè vào biến `a` | **22** | 8 | 4 | Chưa có |
| **5** | `tong = a + b` | Đọc $a = 22, b = 8$, tính $22 + 8 = 30$, nạp vào `tong` | 22 | 8 | 4 | **30** |

---

## 7. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: IN THỪA CÂU CHỮ KHI LÀM BÀI**
> * **Đoạn code sai lầm:**
>  ```python
>   n = int(input("Moi ban nhap vao so n: "))
>   print("Ket qua la:", n * 2)
>   ```
> * **Hậu quả:** chương trình so sánh từng ký tự đầu ra. Việc in các thông báo như `"Moi ban nhap..."` hoặc `"Ket qua la: "` sẽ khiến kết quả bị sai lệch và nhận ngay 0 điểm.
> * **Cách viết đúng phổ biến:**
>  ```python
>   n = int(input())
>   print(n * 2)
>   ```

> **BẪY LỖI 2: ĐẶT TÊN BIẾN SAI QUY TẮC**
> * Viết `2_ban = 10` $\implies$ Báo lỗi `SyntaxError: invalid decimal literal` (Không được bắt đầu bằng chữ số).
> * Viết `diem toan = 9` $\implies$ Báo lỗi `SyntaxError: invalid syntax` (Không được chứa khoảng trắng).
> * **Cách sửa chuẩn:** Đặt là `ban_2 = 10` và `diem_toan = 9`.

> **BẪY LỖI 3: QUÊN ĐỔI KIỂU DỮ LIỆU KHI ĐỌC SỐ**
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
