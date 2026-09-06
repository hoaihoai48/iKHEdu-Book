# LỜI NÓI ĐẦU

Chào mừng các em học sinh và quý thầy cô đến với bộ giáo trình **Khóa học Python cơ bản — QUYỂN 1: NỀN TẢNG LẬP TRÌNH**.

Bộ tài liệu này được biên soạn dành riêng cho học sinh tiểu học mới bắt đầu làm quen với lập trình. Mọi khái niệm đều được giải thích bằng lời văn gần gũi, kèm ví dụ đời thường và hình minh họa trực quan.

Phần nội dung này gồm **2 Chương trọng tâm (Chương 01 đến Chương 02)** với **6 Bài học** và **157 bài tập thực hành**. Học xong quyển này, các em sẽ tự tay viết được những chương trình hoàn chỉnh: tính toán, so sánh, ra quyết định và lặp lại công việc.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm và bản chất:** Giải thích trực quan, dễ hiểu kèm ví dụ minh họa sinh động.
- **Mô hình bài toán quen thuộc:** Các dạng bài gần gũi với đời sống hằng ngày của các em.
- **Mẫu code thường gặp:** Đoạn code Python ngắn gọn, trong sáng, đúng chuẩn để các em học theo.
- **Hệ thống bài tập thực hành:** Phân tầng từ dễ đến khó (P0 đến P3) để các em luyện tập từng bước.
- **Lời giải tham khảo chi tiết:** Phụ lục B cung cấp mã nguồn Python hoàn chỉnh cho toàn bộ bài tập trong sách.

Chúc các em học tập vui vẻ và ngày càng yêu thích môn Tin học!


# CHƯƠNG 01: TÍNH TOÁN CƠ BẢN


# Bài 01: Lệnh xuất nhập, biến số và kiểu dữ liệu

## 1. Bản chất chương trình máy tính & Luồng dữ liệu I/O

Các em thân mến, một chương trình máy tính chính là một **chuỗi các chỉ thị có trật tự**, điều khiển phần cứng để biến đổi dữ liệu đầu vào thành kết quả đầu ra theo yêu cầu của bài tập.

Mọi bài tập đều chạy khép kín theo **luồng 3 bước (Đầu vào $\to$ Xử lý $\to$ Đầu ra)**:



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l01_io_pipeline.png)



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l01_variable_ram.png)



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l01_type_casting.png)



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


## Bài tập thực hành


### Bài 01 [pya_l01_p01_loi_chao_robot]: Lời chào robot

Bối cảnh: Khi một hệ thống tự hành hoặc robot công nghiệp được khởi động trong phòng thực hành lập trình, hệ thống cần gửi thông điệp chào mừng đầu tiên ra thiết bị đầu ra tiêu chuẩn.

Nhiệm vụ: Viết chương trình in ra chính xác dòng thông điệp: `Xin chao cac ban! Toi la Robot Python.`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra một dòng chứa câu chào đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
|  | Xin chao cac ban! Toi la Robot Python. |

**Giải thích:**

In chính xác câu chào ra màn hình theo đúng quy định.



### Bài 02 [pya_l01_p02_cau_doi_tet]: Câu đối ngày tết

Bối cảnh: Trong ứng dụng hiển thị bảng điện tử chào mừng năm mới, hệ thống cần in hai vế câu đối truyền thống trên hai dòng riêng biệt.

Nhiệm vụ: In ra đúng hai dòng chữ, mỗi dòng là một vế câu đối:
  - Dòng 1: `Chuc mung nam moi`
  - Dòng 2: `Van su nhu y`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra hai dòng theo đúng quy định.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
|  | Chuc mung nam moi <br> Van su nhu y |

**Giải thích:**

Sử dụng hai lệnh `print()` liên tiếp để in trên hai dòng riêng biệt.



### Bài 03 [pya_l01_p05_doc_in_so_nguyen]: Đọc và in số nguyên

Bối cảnh: Máy đếm vé tham quan cần nhận vào mã số may mắn của khách và hiển thị lại mã số đó.

Nhiệm vụ: Nhập một số nguyên $N$ từ bàn phím và in số nguyên đó ra màn hình.

**Đầu vào (Input):**

Một dòng duy nhất chứa số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số nguyên $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2026 | 2026 |

**Giải thích:**

Nhập vào số 2026 và in lại đúng số 2026.



### Bài 04 [pya_l01_p03_in_so_sep]: In số trên một hàng với sep

Bối cảnh: Thầy giáo yêu cầu in 5 chữ số đầu tiên từ 1 đến 5 được nối với nhau bằng dấu gạch ngang `-`.

Nhiệm vụ: Viết chương trình in ra dòng chữ: `1-2-3-4-5`.

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In ra dòng chữ `1-2-3-4-5` bằng cách tận dụng tham số `sep`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
|  | 1-2-3-4-5 |

**Giải thích:**

Các số từ 1 đến 5 được in cách nhau bằng dấu `-`.



### Bài 05 [pya_l01_p25_nhan_doi_gia_tri]: Nhân đôi giá trị

Bối cảnh: Bác Tư là một nông dân giỏi nổi tiếng ở vùng Đồng Tháp Mười. Năm đầu tiên bác trồng thử nghiệm một giống cây ăn trái mới và thu hoạch được $N$ quả. Nhờ áp dụng kỹ thuật chăm sóc tiên tiến, mỗi năm tiếp theo sản lượng lại tăng gấp đôi so với năm trước. Bác muốn dự đoán sản lượng thu hoạch sau đúng một năm tới để lên kế hoạch bán hàng cho đại lý.

Nhiệm vụ: Nhập số nguyên $N$ từ bàn phím. In ra giá trị gấp đôi của $N$ (tức $N \times 2$).

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($0 \le N \le 10^9$).

**Đầu ra (Output):**

In ra giá trị $N \times 2$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 75 | 150 |

**Giải thích:**

Gấp đôi của 75 là $75 \times 2 = 150$.



### Bài 06 [pya_l01_p19_in_end_cung_dong]: In không xuống dòng với end

Bối cảnh: Máy tính cần in hai từ ghép thành một khẩu hiệu trên cùng một dòng bằng hai lệnh `print()` riêng biệt.

Nhiệm vụ: Viết chương trình dùng hai lệnh `print()` có tham số `end` để in ra trên một dòng: `Lap trinh rat vui!`

**Đầu vào (Input):**

Không có dữ liệu vào.

**Đầu ra (Output):**

In khẩu hiệu trên một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
|  | Lap trinh rat vui! |

**Giải thích:**

Lệnh thứ nhất in `Lap trinh ` có `end=" "`, lệnh thứ hai in `rat vui!`.



### Bài 07 [pya_l01_p11_hoan_doi_hai_bien]: Hoán đổi vị trí hai biến

Bối cảnh: Hai bạn An và Bình có hai thẻ số mang giá trị $A$ và $B$. Hai bạn muốn đổi thẻ cho nhau.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. Thực hiện hoán đổi giá trị của hai biến, sau đó in ra $A$ và $B$ sau khi hoán đổi trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Hai dòng chứa hai số nguyên $A$ và $B$ ($-10^9 \le A, B \le 10^9$).

**Đầu ra (Output):**

Một dòng in ra giá trị mới của $A$ và $B$ cách nhau dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br>  99 | 99 10 |

**Giải thích:**

Ban đầu $A = 10, B = 99$. Sau khi đổi chỗ, $A = 99$ và $B = 10$.



### Bài 08 [pya_l01_p21_tong_hai_so_2_dong]: Tổng hai số nguyên 2 dòng

Bối cảnh: Bạn Minh có $A$ viên bi, bạn Nam có $B$ viên bi. Cần tính tổng số bi của cả hai bạn.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ lần lượt trên 2 dòng riêng biệt. In ra tổng $A + B$.

**Đầu vào (Input):**

- Dòng 1: Số nguyên $A$ ($0 \le A \le 10^9$).
 - Dòng 2: Số nguyên $B$ ($0 \le B \le 10^9$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng $A + B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 <br>  25 | 40 |

**Giải thích:**

Tổng $15 + 25 = 40$.



### Bài 09 [pya_l01_p22_hieu_hai_so]: Hiệu hai số nguyên

Bối cảnh: Bác thợ may có cuộn vải dài $A$ mét, đã cắt may hết $B$ mét. Cần tính độ dài vải còn lại.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra hiệu $A - B$.

**Đầu vào (Input):**

Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le B \le A \le 10^9$).

**Đầu ra (Output):**

In ra số nguyên là kết quả của $A - B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 <br>  35 | 65 |

**Giải thích:**

Vải còn lại là $100 - 35 = 65$ mét.



### Bài 10 [pya_l01_p23_tich_hai_so]: Tích hai số nguyên

Bối cảnh: Tại nhà máy sản xuất bánh kẹo xuất khẩu Đại Phát, dây chuyền đóng gói hoạt động tự động theo quy trình nghiêm ngặt. Mỗi thùng carton tiêu chuẩn chứa đúng $A$ hộp sản phẩm, và bên trong mỗi hộp lại được xếp gọn gàng $B$ chiếc kẹo thơm ngon. Trước mỗi ca xuất hàng, hệ thống quản lý kho cần tính toán chính xác tổng số lượng kẹo thực tế có trong một thùng để đối soát với phiếu giao hàng.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra tích $A \times B$.

**Đầu vào (Input):**

Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le A, B \le 10^4$).

**Đầu ra (Output):**

In ra số nguyên là tích $A \times B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 <br>  8 | 96 |

**Giải thích:**

Tổng số kẹo là $12 \times 8 = 96$ chiếc.



### Bài 11 [pya_l01_p04_cap_so_nhan_doi]: Cặp số nhân đôi

Bối cảnh: Trong module xử lý tín hiệu số, mạch khuếch đại nhận một tín hiệu đầu vào có biên độ $A$ và nhân đôi biên độ đó lên gấp 2 lần.

Nhiệm vụ: Nhập vào số nguyên $A$. Hãy tính và in ra giá trị của tín hiệu sau khi nhân đôi ($A \times 2$).

**Đầu vào (Input):**

Gồm một số tự nhiên $A$ ($0 \le A \le 10^6$).

**Đầu ra (Output):**

In ra một số nguyên là kết quả nhân đôi ($A \times 2$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | 30 |

**Giải thích:**

Giá trị đầu vào là $15$. Khi nhân đôi, ta có: $15 \times 2 = 30$. Do đó, kết quả in ra màn hình là `30`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 0 | 0 |



### Bài 12 [pya_l01_p18_tuoi_cua_be_sau_5_nam]: Tuổi của bé sau 5 năm

Bối cảnh: Trong hệ thống quản lý hồ sơ nhân khẩu học, độ tuổi của một đối tượng được tính toán và dự đoán theo các mốc thời gian trong tương lai.

Nhiệm vụ: Cho số tuổi hiện tại $N$ ($1 \le N \le 12$). Hãy tính và in ra số tuổi của người đó sau 5 năm nữa.

**Đầu vào (Input):**

Một dòng duy nhất chứa số tự nhiên $N$ ($1 \le N \le 12$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số tuổi của Bo sau 5 năm.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | 13 |

**Giải thích:**

Học sinh 8 tuổi, sau 5 năm nữa nhỏ: $8 + 5 = 13$ tuổi



### Bài 13 [pya_l01_p12_chuc_sinh_nhat]: Lời chúc sinh nhật cá nhân hóa

Bối cảnh: Bạn muốn viết một chương trình in ra thiệp chúc mừng sinh nhật theo tên và tuổi của bạn bè.

Nhiệm vụ: Nhập dòng 1 là tên bạn (chuỗi ký tự), dòng 2 là số tuổi $T$ (số nguyên). In ra dòng chữ: `Chuc mung sinh nhat <Ten>, ban tron <Tuoi> tuoi!`

**Đầu vào (Input):**

- Dòng 1: Chuỗi ký tự không dấu $Ten$.
 - Dòng 2: Số nguyên $Tuoi$ ($1 \le Tuoi \le 100$).

**Đầu ra (Output):**

In ra câu chúc đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Nam <br>  10 | Chuc mung sinh nhat Nam, ban tron 10 tuoi! |

**Giải thích:**

Ghép tên và tuổi vào đúng vị trí của câu chúc.



### Bài 14 [pya_l01_p07_chiec_hop_hoan_doi_bi_mat]: Chiếc hộp hoán đổi bí mật

Bối cảnh: Giờ ra chơi, bạn Tèo có hai chiếc hộp xinh xắn: hộp $A$ đựng số kẹo của Tèo, hộp $B$ đựng số kẹo của Tí. Hai bạn cười khúc khích và đố nhau đổi kẹo cho nhau (số kẹo trong hộp $A$ chuyển sang hộp $B$, và số kẹo trong hộp $B$ chuyển sang hộp $A$). Cả hai loay hoay mãi chưa đổi xong. Hãy giúp hai bạn hoán đổi hai hộp kẹo này.

Nhiệm vụ: Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của 2 biến và in ra giá trị mới của $A$ và $B$ sau khi hoán đổi (cách nhau một dấu cách).

**Đầu vào (Input):**

Dòng 1 chứa số $A$, dòng 2 chứa số $B$ ($0 \le A, B \le 10^9$).

**Đầu ra (Output):**

In ra hai số $A$ và $B$ sau khi hoán đổi trên cùng một dòng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br> 12 | 12 7 |

**Giải thích:**

Ban đầu $A=7, B=12$. Sau khi đổi: $A=12, B=7$.



### Bài 15 [pya_l01_p17_tam_danh_thiep_thong_minh]: Tấm danh thiếp thông minh

Bối cảnh: Hệ thống quản lý thông tin hội thảo cần in thẻ danh thiếp tự động cho người tham dự sau khi nhập tên.

Nhiệm vụ: Nhập vào tên của một người (chuỗi ký tự). Hãy in ra thông điệp chào mừng theo mẫu: `Xin chao ban [Ten]!`

**Đầu vào (Input):**

Một dòng duy nhất chứa chuỗi ký tự tên của người dùng.

**Đầu ra (Output):**

In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Nam | Xin chao ban Nam! |

**Giải thích:**

Với tên nhập vào là `"Nam"`, chương trình ghép chuỗi `"Xin chao ban "` với `"Nam"` và thêm dấu chấm than `!` ở cuối, tạo thành dòng chữ `Xin chao ban Nam!`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| Bao Anh | Xin chao ban Bao Anh! |



### Bài 16 [pya_l01_p06_cua_hang_banh_ran]: Cửa hàng bánh rán

Bối cảnh: Hệ thống máy tính tiền tự động tại căng-tin cần tính tổng giá trị hóa đơn khi khách hàng mua nhiều sản phẩm cùng loại với đơn giá cố định.

Nhiệm vụ: Nhập vào đơn giá mỗi sản phẩm $a$ (nghìn đồng) và số lượng sản phẩm $b$. Hãy tính tổng số tiền (nghìn đồng) cần thanh toán.

**Đầu vào (Input):**

Nhập vào 2 số tự nhiên $a$ và $b$ mỗi số trên một dòng ($1 \le a \le 100, 1 \le b \le 100$).

**Đầu ra (Output):**

In ra số tiền Doraemon cần trả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 <br> 5 | 60 |

**Giải thích:**

Mua 5 chiếc bánh, mỗi chiếc 12 nghìn đồng: $12 \times 5 = 60$.



### Bài 17 [pya_l01_p15_phep_nhan_bang]: In bảng phép nhân cơ bản

Bối cảnh: Học sinh học bảng nhân muốn in một dòng phép tính dạng `A x B = C` thật đẹp mắt.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra chính xác theo định dạng: `A x B = C` (với $C = A \times B$).

**Đầu vào (Input):**

Hai dòng, dòng 1 là $A$, dòng 2 là $B$ ($1 \le A, B \le 100$).

**Đầu ra (Output):**

In ra dòng phép tính theo đúng mẫu, các thành phần cách nhau bởi dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 <br>  9 | 7 x 9 = 63 |

**Giải thích:**

Tính $7 \times 9 = 63$ và in theo mẫu `7 x 9 = 63`.



### Bài 18 [pya_l01_p09_tong_hai_so_cung_dong]: Tổng hai số trên cùng 1 dòng

Bối cảnh: Trong đề thi chuẩn, hai số $A$ và $B$ thường được nhập trên cùng 1 dòng ngăn cách bởi dấu cách.

Nhiệm vụ: Nhập hai số nguyên $A, B$ trên cùng một dòng. In ra tổng $A + B$.

**Đầu vào (Input):**

Một dòng duy nhất chứa hai số nguyên $A$ và $B$ cách nhau một dấu cách ($-10^9 \le A, B \le 10^9$).

**Đầu ra (Output):**

In ra tổng $A + B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 45 55 | 100 |

**Giải thích:**

Đọc bằng `map(int, input().split())` và in ra $45 + 55 = 100$.



### Bài 19 [pya_l01_p20_doi_thuoc_ke_milimet]: Đổi thước kẻ milimet

Bối cảnh: Trong thiết kế cơ khí chính xác, kích thước của chi tiết gia công gồm phần kích thước chẵn $a\text{ cm}$ và phần sai số dư $b\text{ mm}$.

Nhiệm vụ: Cho biết $1\text{ cm} = 10\text{ mm}$. Hãy quy đổi toàn bộ độ dài gồm $a\text{ cm}$ và $b\text{ mm}$ sang đơn vị milimet ($\text{mm}$).

**Đầu vào (Input):**

* Dòng 1: Chứa số tự nhiên $a$ ($1 \le a \le 1000$).
 * Dòng 2: Chứa số tự nhiên $b$ ($1 \le b \le 1000$).

**Đầu ra (Output):**

Một số tự nhiên duy nhất là độ dài của thước tính theo đơn vị milimet ($\text{mm}$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 5 | 25 |

**Giải thích:**

$2\text{ cm} = 20\text{ mm}$. Tổng cộng là: $20 + 5 = 25\text{ mm}$.



### Bài 20 [pya_l01_p14_ghep_ngay_thang_nam]: Ghép ngày tháng năm định dạng chuẩn

Bối cảnh: Hệ thống cần nhận 3 số nguyên là Ngày, Tháng, Năm và in ra dạng chuẩn hiển thị trên lịch.

Nhiệm vụ: Nhập 3 số nguyên $D, M, Y$ trên cùng một dòng. In ra theo định dạng: `D/M/Y`.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $D, M, Y$ cách nhau dấu cách ($1 \le D \le 31$, $1 \le M \le 12$, $1900 \le Y \le 2100$).

**Đầu ra (Output):**

In ra dạng `D/M/Y`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 9 2026 | 4/9/2026 |

**Giải thích:**

Tận dụng lệnh `print(d, m, y, sep="/")`.



### Bài 21 [pya_l01_p08_doan_tau_toa_xe_ghep_so]: Đoàn tàu toa xe ghép số

Bối cảnh: Sáng sớm ở ga xe lửa, có 2 toa xe chở 2 con số $a$ và $b$ vừa chạy vào sân ga. Bác trưởng ga vui tính muốn nhìn thấy cả hai kết quả:
 1. Nếu ghép 2 toa tàu lại thành một dãy số (Ghép chữ).
 2. Nếu cộng giá trị của 2 toa tàu lại với nhau (Cộng số học).
Bác loay hoay mãi với cuốn sổ ghi chép. Hãy giúp bác trưởng ga làm cả hai việc này.

Nhiệm vụ: Nhập vào 2 số tự nhiên $a$ và $b$. Dòng 1 in ra kết quả khi ghép chuỗi chữ. Dòng 2 in ra kết quả khi cộng số.

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a, b$ ($1 \le a, b \le 100$) trên 2 dòng.

**Đầu ra (Output):**

* Dòng 1: Chuỗi ghép dính $a$ và $b$.
 * Dòng 2: Tổng giá trị số học $a + b$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 25 <br> 30 | 2530 <br> 55 |

**Giải thích:**

Dòng 1 ghép chữ: `"25" + "30" = "2530"`.
Dòng 2 cộng số: $25 + 30 = 55$.



### Bài 22 [pya_l01_p16_chenh_lech_tuoi]: Chênh lệch tuổi của hai anh em

Bối cảnh: Anh hơn em một số tuổi. Biết tuổi của anh là $A$ và tuổi của em là $E$. Cần tính số tuổi anh hơn em và in câu thông báo.

Nhiệm vụ: Nhập hai số nguyên $A$ và $E$ trên cùng 1 dòng ($1 \le E \le A \le 100$). In ra một dòng có nội dung: `Anh hon em <so_tuoi> tuoi.`

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A$ và $E$ cách nhau dấu cách.

**Đầu ra (Output):**

In ra câu kết luận đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 7 | Anh hon em 5 tuoi. |

**Giải thích:**

Hiệu số tuổi $12 - 7 = 5$. In ra `Anh hon em 5 tuoi.`.



### Bài 23 [pya_l01_p13_bon_phep_tinh]: Bốn phép tính đồng thời

Bối cảnh: Máy tính cầm tay cần hiển thị bảng kết quả 3 phép tính cơ bản giữa hai số nguyên.

Nhiệm vụ: Nhập hai số nguyên $A$ và $B$ trên cùng 1 dòng. In ra 3 dòng:

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A$ và $B$ cách nhau dấu cách ($-10^4 \le A, B \le 10^4$).

**Đầu ra (Output):**

3 dòng lần lượt chứa tổng, hiệu và tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 5 | 13 <br> 3 <br> 40 |

**Giải thích:**

$8 + 5 = 13$, $8 - 5 = 3$, $8 \times 5 = 40$.



### Bài 24 [pya_l01_p10_co_may_thoi_gian_3_the_he]: Cỗ máy thời gian 3 thế hệ

Bối cảnh: Trong bài toán phân tích nhân khẩu học, tuổi của ba thành viên trong một gia đình thuộc ba thế hệ liên tiếp được ghi nhận.

Nhiệm vụ: Cho số tuổi của người con là $a$, người bố hơn con $b$ tuổi, và người ông hơn bố $c$ tuổi. Hãy tính tuổi của bố, tuổi của ông và tổng tuổi của cả ba người.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số nguyên $a, b, c$ ($1 \le a \le 20, 20 \le b \le 40, 20 \le c \le 40$).

**Đầu ra (Output):**

Gồm 3 dòng tương ứng với 3 yêu cầu của bài toán.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 30 <br> 25 | 40 <br> 65 <br> 115 |

**Giải thích:**

- Tuổi Nam: $10$.
- Tuổi Bố: $10 + 30 = 40$.
- Tuổi Ông: $40 + 25 = 65$.
- Tổng cả 3 người: $10 + 40 + 65 = 115$.



### Bài 25 [pya_l01_p24_ve_tham_quan_chua_huong]: Vé tham quan chùa hương

Bối cảnh: Cuối tuần này, một đoàn khách nhỏ chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền rồi đi cáp treo ngắm cảnh núi rừng:
 * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
 * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
 * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
Cô hướng dẫn viên cần tính tiền để mua vé cho cả đoàn. Hãy giúp cô tính tổng số tiền cần chuẩn bị.

Nhiệm vụ: Hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.

**Đầu vào (Input):**

Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 <br> 10 <br> 50 <br> 30 <br> 10 <br> 4 | 580 |

**Giải thích:**

- Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.
- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.
- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.
- Tổng tiền: $160 + 420 = 580$ nghìn đồng.



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


## Bài tập thực hành


### Bài 01 [pya_l02_p02_luy_thua_bac_hai]: Lũy thừa bậc hai

Bối cảnh: Trong buổi học toán về hình học không gian, cô giáo Lan yêu cầu học sinh tính diện tích của một mặt bàn hình vuông có cạnh dài $A$ xen-ti-mét. Công thức diện tích hình vuông chính là $A^2$ — hay còn gọi là "bình phương" của $A$. Em hãy giúp các bạn viết chương trình tự động hóa phép tính này để kiểm tra đáp số nhanh chóng.

Nhiệm vụ: Nhập số nguyên $N$. In ra giá trị bình phương $N^2$ bằng cách dùng toán tử `**`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($-10^4 \le N \le 10^4$).

**Đầu ra (Output):**

In ra $N^2$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | 64 |

**Giải thích:**

$8^2 = 64$.



### Bài 02 [pya_l02_p03_lap_phuong]: Lập phương của một số

Bối cảnh: Xưởng gia công gỗ nghệ thuật Phú Quý nhận được đơn đặt hàng một lô hộp quà tặng cao cấp hình lập phương. Mỗi hộp có cạnh dài đúng $A$ xen-ti-mét. Để ước lượng nguyên vật liệu và chi phí vận chuyển, bộ phận kỹ thuật cần tính chính xác thể tích bên trong mỗi chiếc hộp. Em hãy lập trình tính thể tích khối lập phương với cạnh cho trước.

Nhiệm vụ: Nhập số nguyên dương $A$. In ra giá trị $A^3$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $A$ ($1 \le A \le 1000$).

**Đầu ra (Output):**

In ra $A^3$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 125 |

**Giải thích:**

$5^3 = 125$.



### Bài 03 [pya_l02_p04_chu_so_tan_cung]: Lấy chữ số tận cùng

Bối cảnh: Tại hội chợ Xuân, mỗi du khách được phát một tấm vé số may mắn mang một số nguyên dương. Theo luật chơi, giải thưởng phụ thuộc vào chữ số cuối cùng (hàng đơn vị) của tấm vé: nếu tận cùng là 0 hoặc 5 thì trúng quà, còn lại thì không. Hệ thống cần trích xuất chính xác chữ số hàng đơn vị từ số trên tấm vé để tự động phân loại trúng thưởng.

Nhiệm vụ: Nhập số nguyên dương $N$. In ra chữ số hàng đơn vị của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

In ra chữ số tận cùng của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2026 | 6 |

**Giải thích:**

$2026 \% 10 = 6$.



### Bài 04 [pya_l02_p09_hai_chu_so_cuoi]: Lấy hai chữ số tận cùng

Bối cảnh: Để xét giải khuyến khích số may mắn, người ta cần lấy 2 chữ số tận cùng của mã vé.

Nhiệm vụ: Nhập số nguyên $N$ ($N \ge 100$). In ra giá trị của hai chữ số tận cùng của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($100 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số tạo bởi 2 chữ số cuối (Ví dụ: `2026` in ra `26`, `105` in ra `5`).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1945 | 45 |

**Giải thích:**

$1945 \% 100 = 45$.



### Bài 05 [pya_l02_p11_bieu_thuc_bac_nhat]: Giá trị biểu thức bậc nhất

Bối cảnh: Trong bài kiểm tra toán học cuối kỳ, đề thi yêu cầu học sinh tính giá trị của hàm số bậc nhất $y = 3x + 5$ tại nhiều điểm $x$ khác nhau. Thay vì tính bằng tay từng trường hợp, bạn Linh nảy ra ý tưởng viết một chương trình Python để tự động hóa: chỉ cần nhập giá trị $x$, máy sẽ trả về ngay kết quả $y$ tương ứng. Em hãy giúp Linh hoàn thành chương trình này.

Nhiệm vụ: Nhập số nguyên $x$. In ra giá trị của $y = 3x + 5$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $x$ ($-10^6 \le x \le 10^6$).

**Đầu ra (Output):**

In ra giá trị của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 17 |

**Giải thích:**

$3 \times 4 + 5 = 17$.



### Bài 06 [pya_l02_p25_xoa_chu_so_cuoi]: Xóa chữ số tận cùng

Bối cảnh: Bạn Hùng đang nhập liệu bảng thống kê sĩ số các lớp trên máy tính thì vô tình bấm thêm một chữ số thừa ở cuối. Thay vì nhập $12$ thì Hùng đã gõ thành $123$. May mắn thay, thao tác "xóa lùi" sẽ loại bỏ chữ số cuối cùng và trả lại số ban đầu. Em hãy mô phỏng thao tác này bằng chương trình: cho một số nguyên dương, hãy trả về số mới sau khi xóa đi chữ số cuối cùng.

Nhiệm vụ: Nhập số nguyên dương $N$ ($N \ge 10$). In ra số $N$ sau khi đã cắt bỏ chữ số hàng đơn vị.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

In ra số $N$ sau khi bỏ chữ số cuối.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3458 | 345 |

**Giải thích:**

$3458 // 10 = 345$.



### Bài 07 [pya_l02_p28_xep_ban_hoc]: Xếp hàng vào bàn học

Bối cảnh: Phòng thi Olympic Tin học cấp thành phố được bố trí toàn bộ bàn đôi — mỗi bàn ngồi đúng 2 thí sinh. Năm nay có $N$ thí sinh đăng ký dự thi. Ban tổ chức cần tính toán số lượng bàn tối thiểu phải chuẩn bị sao cho tất cả thí sinh đều có chỗ ngồi, kể cả trường hợp số thí sinh là số lẻ thì bàn cuối cùng vẫn phải kê ra dù chỉ ngồi 1 người.

Nhiệm vụ: Có $N$ bạn thí sinh. Hỏi cần ít nhất bao nhiêu bàn đôi để tất cả các bạn đều có chỗ ngồi? (Nếu lẻ 1 bạn vẫn cần thêm 1 bàn).

**Đầu vào (Input):**

Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

In ra số bàn học tối thiểu cần dùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | 8 |

**Giải thích:**

15 bạn xếp được 7 bàn đôi đầy đủ, còn 1 bạn ngồi riêng 1 bàn $\implies$ Cần 8 bàn. Công thức: `(N + 1) // 2`.



### Bài 08 [pya_l02_p13_luy_thua_cau_thang]: Lũy thừa cầu thang

Bối cảnh: Bạn Thỏ Nâu rất thích xếp các khối gỗ thành một chiếc cầu thang toán học. Tầng đầu tiên cần $a$ khối gỗ, mỗi tầng tiếp theo lại gấp $a$ lần số khối của tầng trước đó. Thỏ Nâu đếm được chiếc cầu thang của mình có tất cả $n$ tầng. Hãy giúp bạn Thỏ tính xem tầng cao nhất có bao nhiêu khối gỗ.

Nhiệm vụ: Cho hai số nguyên $a$ và $n$, em hãy tính giá trị lũy thừa $a^n$.

**Đầu vào (Input):**

Gồm 2 dòng, mỗi dòng một số nguyên: dòng đầu là cơ số $a$, dòng sau là số mũ $n$ ($1 \le a \le 10$, $0 \le n \le 10$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là giá trị của $a^n$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 4 | 81 |

**Giải thích:**

$3^4 = 3 \times 3 \times 3 \times 3 = 81$. Tầng cao nhất của cầu thang có 81 khối gỗ.



### Bài 09 [pya_l02_p07_dong_hop_banh]: Đóng hộp bánh ngọt

Bối cảnh: Xưởng bánh Hương Quê vừa sản xuất xong một mẻ gồm $M$ chiếc bánh quy bơ thơm ngon. Theo quy cách đóng gói, mỗi hộp quà tặng chứa cố định đúng 6 chiếc bánh. Bộ phận kho vận cần biết chính xác hai thông tin: cần bao nhiêu hộp đầy đủ để đóng gói, và sau khi đóng xong thì còn dư bao nhiêu chiếc bánh lẻ chưa đủ một hộp.

Nhiệm vụ: Nhập số nguyên dương $M$. In ra số hộp bánh đóng được đầy đủ và số bánh lẻ còn sót lại.

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$ ($1 \le M \le 10^6$).

**Đầu ra (Output):**

Hai số nguyên cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 50 | 8 2 |

**Giải thích:**

$50 // 6 = 8$ hộp, dư $50 \% 6 = 2$ bánh lẻ.



### Bài 10 [pya_l02_p10_chu_so_hang_chuc]: Chữ số hàng chục

Bối cảnh: Tại trạm kiểm soát tốc độ trên quốc lộ, camera ghi nhận biển số xe dưới dạng một số nguyên. Để phân loại phương tiện theo nhóm, hệ thống cần trích xuất chữ số ở hàng chục (vị trí thứ hai từ phải sang) của số đó. Ví dụ: số $1234$ có chữ số hàng chục là $3$, số $507$ có chữ số hàng chục là $0$. Em hãy lập trình giải quyết bài toán trích xuất này.

Nhiệm vụ: Nhập số nguyên $N$ ($N \ge 10$). In ra chữ số hàng chục của $N$.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

In ra chữ số hàng chục.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 378 | 7 |

**Giải thích:**

Bỏ chữ số tận cùng: $378 // 10 = 37$. Lấy chữ số cuối của 37: $37 \% 10 = 7$.



### Bài 11 [pya_l02_p14_doi_phut_ra_gio_phut]: Đổi phút ra giờ phút

Bối cảnh: Bạn Mèo Cam vừa bấm giờ chạy bộ quanh công viên và chiếc đồng hồ chỉ tổng cộng $T$ phút. Mèo Cam muốn khoe với cả lớp rằng mình đã chạy được mấy giờ mấy phút cho thật oai. Nhưng bạn ấy chỉ biết cộng trừ đơn giản, chưa biết cách đổi phút ra giờ. Hãy giúp Mèo Cam đổi số phút thành giờ và phút.

Nhiệm vụ: Cho tổng số phút $T$, em hãy tính số giờ trọn vẹn và số phút còn lẻ.

**Đầu vào (Input):**

Một số nguyên duy nhất $T$ trên một dòng ($0 \le T \le 10000$).

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau một dấu cách: số giờ và số phút còn dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 135 | 2 15 |

**Giải thích:**

$135$ phút $= 2$ giờ trọn vẹn ($2 \times 60 = 120$ phút) và còn dư $135 - 120 = 15$ phút.



### Bài 12 [pya_l02_p22_nhan_doi_luy_thua]: Nhân đôi lũy thừa

Bối cảnh: Trong mô hình sinh trưởng tế bào vi sinh, số lượng cá thể ban đầu là $1$ và nhân đôi sau mỗi chu kỳ thời gian.

Nhiệm vụ: Cho số nguyên $N$ ($0 \le N \le 30$). Hãy tính số lượng cá thể sau $N$ chu kỳ nhân đôi ($2^N$).

**Đầu vào (Input):**

Một số tự nhiên $n$ ($1 \le n \le 30$).

**Đầu ra (Output):**

In ra số lượng tế bào sau $n$ giờ ($2^n$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 16 |

**Giải thích:**

Sau 4 giờ: $2^4 = 16$ tế bào.



### Bài 13 [pya_l02_p27_vong_chay_dien_kinh]: Vòng chạy điền kinh

Bối cảnh: Hội khỏe trường em tổ chức chạy điền kinh thật vui. Sân vận động có một đường chạy hình chữ nhật có chu vi đúng $100\text{ mét}$. Vận động viên An xuất phát từ vạch số 0 và chạy liên tục theo một chiều dọc theo mép sân được tổng quãng đường là $N\text{ mét}$. Các bạn cổ vũ reo hò mà chưa biết An đã chạy được mấy vòng. Hãy giúp tổ trọng tài tính giúp An.

Nhiệm vụ: Hãy cho biết:
 1. An đã chạy được bao nhiêu vòng sân trọn vẹn?
 2. Hiện tại An đang dừng lại ở vị trí cách vạch xuất phát bao nhiêu mét?

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Hai số nguyên trên một dòng cách nhau dấu cách lần lượt là số vòng chạy trọn vẹn và khoảng cách tính từ vạch xuất phát.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 250 | 2 50 |

**Giải thích:**

$250 = 2 \times 100 + 50$. Đã chạy 2 vòng trọn vẹn và đang ở mét thứ 50.



### Bài 14 [pya_l02_p05_bong_den_vien_bien_hieu]: Bóng đèn viền biển hiệu

Bối cảnh: Phố phường sắp đến hội hoa đăng, người ta muốn mắc các bóng đèn màu rực rỡ trang trí xung quanh viền của một bảng quảng cáo hình vuông. Bảng quảng cáo có chiều dài cạnh là $a\text{ dm}$. Các bóng đèn được mắc liên tiếp nhau và cách nhau đúng $5\text{ cm}$ dọc theo chu vi hình vuông (bao gồm cả các góc). Bác thợ điện leo thang mà chưa biết cần bao nhiêu bóng. Hãy giúp bác tính số bóng đèn cần mắc.

Nhiệm vụ: Hãy tính số lượng bóng đèn cần mắc.
* **Biết rằng:** $1\text{ dm} = 10\text{ cm}$.

**Đầu vào (Input):**

Một số nguyên dương $a$ ($1 \le a \le 10^7$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số bóng đèn cần mắc.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 | 8 |

**Giải thích:**

Cạnh $1\text{ dm} = 10\text{ cm}$. Chu vi bảng hình vuông là $10 \times 4 = 40\text{ cm}$.
Khoảng cách giữa các đèn là $5\text{ cm}$. Số đèn mắc là: $40 : 5 = 8$ bóng đèn.



### Bài 15 [pya_l02_p16_du_quay_vong_tron]: Đu quay vòng tròn

Bối cảnh: Khu vui chơi vừa mở một chiếc đu quay khổng lồ, mỗi vòng quay trọn vẹn kéo dài đúng $C$ phút. Bạn Sóc Nâu ngồi trên đu quay suốt $N$ phút không chịu xuống vì mải ngắm thành phố từ trên cao. Bác quản trò muốn biết Sóc Nâu đã đi được bao nhiêu vòng trọn vẹn và đang dở dang bao nhiêu phút của vòng hiện tại. Hãy giúp bác quản trò tính nhanh.

Nhiệm vụ: Cho tổng thời gian $N$ và thời gian một vòng $C$, em hãy tính số vòng quay trọn vẹn và số phút dư.

**Đầu vào (Input):**

Gồm 2 dòng, mỗi dòng một số nguyên: $N$ ($1 \le N \le 10^9$) và $C$ ($1 \le C \le 10^9$).

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau một dấu cách: số vòng trọn vẹn và số phút dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 250 <br> 60 | 4 10 |

**Giải thích:**

$250 = 4 \times 60 + 10$. Sóc Nâu đã đi được 4 vòng trọn vẹn và đang ở phút thứ 10 của vòng thứ năm.



### Bài 16 [pya_l02_p23_so_keo_con_thua]: Số kẹo còn thừa

Bối cảnh: Trong bài toán chia tài nguyên máy chủ, một lượng gồm $a$ gói tài nguyên được chia đều cho $b$ tiến trình đang xử lý.

Nhiệm vụ: Cho hai số nguyên dương $a$ và $b$. Hãy xác định lượng tài nguyên dư thừa không thể chia đều cho các tiến trình.

**Đầu vào (Input):**

Gồm 2 dòng lần lượt chứa hai số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

In ra số viên kẹo còn thừa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 <br> 8 | 4 |

**Giải thích:**

Với $a = 17$ và $b = 5$, phép chia dư cho kết quả: $17 \% 5 = 2$. Lượng còn dư không chia hết là 2.



### Bài 17 [pya_l02_p20_phuc_hoi_so_bi_chia]: Bất biến chia kẹo và phục hồi số bị chia

Bối cảnh: Nam đem một số kẹo bí mật chia cho $B$ bạn thì mỗi bạn được $Q$ chiếc kẹo và Nam còn thừa lại $R$ chiếc kẹo.

Nhiệm vụ: Nhập 3 số nguyên $B, Q, R$ trên cùng 1 dòng ($B > R \ge 0$, $Q \ge 0$). Hãy tìm lại tổng số kẹo ban đầu mà Nam có.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $B, Q, R$ ($1 \le B, Q \le 10^6$, $0 \le R < B$).

**Đầu ra (Output):**

In ra số kẹo ban đầu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 8 3 | 51 |

**Giải thích:**

Áp dụng định lý bất biến phép chia: $A = B \times Q + R = 6 \times 8 + 3 = 51$.



### Bài 18 [pya_l02_p32_da_thuc_bac_hai]: Đa thức bậc hai

Bối cảnh: Giáo sư Nguyễn đang nghiên cứu quỹ đạo bay của một quả bóng tennis được ném lên cao. Vị trí độ cao tại thời điểm $x$ giây được mô tả bởi đa thức bậc hai $P(x) = 2x^2 - 4x + 9$ (đơn vị: mét). Để phục vụ việc phân tích dữ liệu thí nghiệm, giáo sư cần tính nhanh giá trị $P(x)$ với nhiều mốc thời gian khác nhau. Em hãy lập trình giúp giáo sư.

Nhiệm vụ: Nhập số nguyên $x$. In ra giá trị của đa thức.

**Đầu vào (Input):**

Một dòng chứa số nguyên $x$ ($-1000 \le x \le 1000$).

**Đầu ra (Output):**

In ra giá trị của $P(x)$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 15 |

**Giải thích:**

$2 \times (3^2) - 4 \times 3 + 9 = 2 \times 9 - 12 + 9 = 15$.



### Bài 19 [pya_l02_p26_trong_cay_dai_lo]: Trồng cây đại lộ

Bối cảnh: Thành phố vừa khánh thành một đại lộ thẳng tắp dài $N$ mét. Mùa hè sắp đến, để có bóng mát cho người đi bộ, đội cây xanh quyết định trồng một hàng cây ngay ngắn ở một bên đường. Cây đầu tiên được trồng ngay tại điểm xuất phát (mét thứ 0), rồi cứ cách đúng $K$ mét lại trồng tiếp một cây nữa. Trước khi ra quân, đội trưởng muốn biết chính xác cần chuẩn bị bao nhiêu cây, và em chính là người giúp đội tính con số đó!

Nhiệm vụ: Hãy tính tổng số lượng cây xanh được trồng trên đoạn đường từ mét thứ 0 đến mét thứ $N$.

**Đầu vào (Input):**

Gồm 2 số tự nhiên $N$ và $K$ ($1 \le N, K \le 10^6$) mỗi số trên một dòng.

**Đầu ra (Output):**

Một số nguyên duy nhất là số cây trồng được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 3 | 4 |

**Giải thích:**

Các cây được trồng tại các vị trí mét thứ: 0, 3, 6, 9. Tổng cộng có 4 cây.



### Bài 20 [pya_l02_p15_gia_tri_bieu_thuc_pemdas]: Giá trị biểu thức PEMDAS

Bối cảnh: Lớp học của bạn Ong Vàng hôm nay thi xem ai là nhà tính nhẩm nhanh nhất. Cô giáo viết lên bảng một biểu thức bí mật gồm ba con số $a$, $b$, $c$ với quy tắc tính là $a + b \times c^2$. Bạn nào tính đúng thứ tự ưu tiên ngoặc, mũ, nhân chia rồi mới cộng trừ sẽ giành chiến thắng. Hãy giúp bạn Ong Vàng tính giá trị biểu thức này thật chính xác.

Nhiệm vụ: Cho ba số nguyên $a$, $b$, $c$, em hãy tính giá trị của biểu thức $a + b \times c^2$.

**Đầu vào (Input):**

Gồm 3 dòng, mỗi dòng một số nguyên: $a$, $b$, $c$ ($1 \le a, b, c \le 100$).

**Đầu ra (Output):**

In ra một số nguyên duy nhất là giá trị của biểu thức.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 3 <br> 4 | 50 |

**Giải thích:**

Ưu tiên lũy thừa trước: $c^2 = 4^2 = 16$. Tiếp theo nhân: $b \times 16 = 3 \times 16 = 48$. Cuối cùng cộng: $2 + 48 = 50$.



### Bài 21 [pya_l02_p24_doi_gio_ra_phut_giay]: Đổi giờ ra phút giây

Bối cảnh: Bạn Tít được tặng một chiếc đồng hồ điện tử xinh xắn hiển thị thời gian gồm $H$ giờ, $M$ phút và $S$ giây. Tít khoe với bạn thân và đố bạn đoán xem cả khoảng thời gian đó là bao nhiêu giây. Hai bạn đếm xuôi đếm ngược mãi chưa ra. Hãy giúp hai bạn đổi thời gian ra giây.

Nhiệm vụ: Hãy tính xem tổng cộng khoảng thời gian đó tương đương với bao nhiêu giây?
* **Biết rằng:** $1\text{ giờ} = 60\text{ phút} = 3600\text{ giây}$, $1\text{ phút} = 60\text{ giây}$.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $H, M, S$ ($0 \le H \le 23, 0 \le M, S \le 59$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng số giây.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 20 <br> 15 | 4815 |

**Giải thích:**

$1 \times 3600 + 20 \times 60 + 15 = 3600 + 1200 + 15 = 4815$ giây.



### Bài 22 [pya_l02_p29_tach_chu_so_tan_cung]: Tách chữ số tận cùng

Bối cảnh: Na có một mã số may mắn là một số tự nhiên $N$ viết trên chiếc vòng tay. Hôm nay Na chơi trò thám tử cùng bạn thân, muốn tìm ra chữ số hàng đơn vị và chữ số hàng chục của số này để mở chiếc hộp bí mật. Hai bạn xoay chiếc vòng mãi mà chưa tách được. Hãy giúp Na tách hai chữ số đó ra.

Nhiệm vụ: Cho số tự nhiên $N$, hãy tách và in ra chữ số hàng đơn vị và chữ số hàng chục của $N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($10 \le N \le 10^9$).

**Đầu ra (Output):**

* Dòng 1: Chữ số hàng đơn vị của $N$.
 * Dòng 2: Chữ số hàng chục của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 857 | 7 <br> 5 |

**Giải thích:**

Chữ số hàng đơn vị là 7, hàng chục là 5.



### Bài 23 [pya_l02_p30_dao_nguoc_so_2_chu_so]: Đảo ngược số 2 chữ số

Bối cảnh: Câu lạc bộ thám tử nhí vừa nhận được một mật thư bí ẩn, trong đó các con số 2 chữ số đã bị đảo ngược vị trí hai chữ số cho nhau (ví dụ số 27 bị biến thành 72). Đội trưởng đố cả đội giải mã được con số thật. Các thám tử nhí soi kính lúp mà vẫn bối rối. Hãy giúp đội thám tử đảo ngược con số về đúng vị trí.

Nhiệm vụ: Nhập vào một số tự nhiên $N$ có đúng 2 chữ số ($10 \le N \le 99$). Hãy in ra số sau khi đảo ngược hai chữ số.

**Đầu vào (Input):**

Một số tự nhiên $N$.

**Đầu ra (Output):**

Số nguyên sau khi đảo ngược. (Lưu ý: Nếu số là 30 thì đảo lại là 3).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 49 | 94 |

**Giải thích:**

Hàng chục là 4, hàng đơn vị là 9 $\to$ Đảo lại thành 94.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 50 | 5 |

**Giải thích:**

Hàng chục là 5, đơn vị là 0 $\to$ Đảo lại thành $0 \times 10 + 5 = 5$.



### Bài 24 [pya_l02_p33_tich_hai_tong]: Biểu thức có dấu ngoặc

Bối cảnh: Trong giờ thực hành đại số, cô giáo đưa ra bài toán ứng dụng: cho bốn số nguyên $a$, $b$, $c$, $d$, hãy tính tích của hai tổng $T = (a + b) \times (c - d)$. Đây là phép toán kết hợp giữa cộng, trừ và nhân — đòi hỏi học sinh phải hiểu rõ thứ tự ưu tiên phép tính khi viết biểu thức trong Python. Em hãy viết chương trình tính giá trị $T$ từ bốn số nhập vào.

Nhiệm vụ: Nhập 4 số nguyên $a, b, c, d$ trên cùng 1 dòng cách nhau dấu cách. In ra giá trị của $T$.

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên $a, b, c, d$ ($-10^4 \le a, b, c, d \le 10^4$).

**Đầu ra (Output):**

In ra giá trị số nguyên $T$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 10 6 | 32 |

**Giải thích:**

$(5 + 3) \times (10 - 6) = 8 \times 4 = 32$.



### Bài 25 [pya_l02_p34_dong_ho_24h]: Đồng hồ 24 giờ

Bối cảnh: Hiện tại đồng hồ đang chỉ $H$ giờ. Cần xác định xem sau $K$ giờ nữa thì đồng hồ chỉ mấy giờ?

Nhiệm vụ: Nhập hai số nguyên $H$ và $K$ trên 1 dòng ($0 \le H \le 23$, $0 \le K \le 10^9$). In ra số giờ mà đồng hồ sẽ hiển thị (từ 0 đến 23).

**Đầu vào (Input):**

Một dòng chứa $H$ và $K$.

**Đầu ra (Output):**

In ra giờ mới.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 10 | 6 |

**Giải thích:**

$20 + 10 = 30$ giờ. $30 \% 24 = 6$ giờ sáng.



### Bài 26 [pya_l02_p35_ngay_trong_tuan]: Ngày trong tuần

Bối cảnh: Quy ước Chủ Nhật là ngày 0, Thứ Hai là ngày 1, ..., Thứ Bảy là ngày 6. Hôm nay là ngày $D$.

Nhiệm vụ: Nhập ngày hiện tại $D$ ($0 \le D \le 6$) và số ngày trôi qua $N$ ($0 \le N \le 10^9$). In ra thứ tương ứng sau $N$ ngày.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $D$ và $N$.

**Đầu ra (Output):**

In ra mã số ngày trong tuần (từ 0 đến 6).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 10 | 4 |

**Giải thích:**

Thứ Hai là ngày 1. Sau 10 ngày nữa: $(1 + 10) \% 7 = 11 \% 7 = 4$ (tức Thứ Năm).



### Bài 27 [pya_l02_p01_chia_deu_banh_quy]: Chia đều bánh quy

Bối cảnh: Tiệm bánh Hạnh Phúc vừa ra lò một mẻ gồm $a$ chiếc bánh quy bơ thơm phức. Cô chủ tiệm muốn chia đều số bánh vào $b$ đĩa trưng bày để phục vụ khách, sao cho mỗi đĩa có số bánh bằng nhau và nhiều nhất có thể. Những chiếc bánh còn dư không đủ xếp thêm một đĩa nữa sẽ được cất riêng vào hộp giữ tươi.

Nhiệm vụ: Cho hai số nguyên dương $a$ (tổng số bánh) và $b$ (số đĩa). Hãy lập trình tính số bánh trên mỗi đĩa (phần nguyên của phép chia $a : b$) và số bánh còn dư lại.

**Đầu vào (Input):**

Nhập vào 2 số nguyên dương $a$ và $b$ trên 2 dòng ($1 \le a, b \le 1000$).

**Đầu ra (Output):**

In ra 2 số trên một dòng cách nhau một dấu cách: số bánh trên mỗi đĩa và số bánh còn dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 17 <br> 5 | 3 2 |

**Giải thích:**

$17 : 5 = 3$ dư $2$. Mỗi đĩa 3 cái, còn dư 2 cái bánh.



### Bài 28 [pya_l02_p31_xe_buyt_cho_hoc_sinh]: Xe buýt chở học sinh

Bối cảnh: Trường học sinh tổ chức một chuyến dã ngoại thật vui cho $N$ học sinh. Nhà trường thuê các xe buýt loại $K$ chỗ ngồi, mỗi xe buýt chở được tối đa $K$ bạn học sinh. Sáng khởi hành, các bạn xếp hàng ngay ngắn, tay vẫy cờ đỏ sao vàng. Thầy hiệu trưởng muốn không bạn nào bị ở lại trường. Hãy giúp thầy tính số xe buýt cần thuê.

Nhiệm vụ: Hỏi nhà trường cần thuê **ít nhất bao nhiêu xe buýt** để chở hết toàn bộ $N$ học sinh (không để bạn nào phải ở lại trường)?

**Đầu vào (Input):**

Nhập vào 2 số nguyên dương $N$ và $K$ ($1 \le N, K \le 10^6$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng xe buýt tối thiểu cần thuê.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 25 <br> 10 | 3 |

**Giải thích:**

Hai xe đầu chở được 20 bạn, còn 5 bạn nữa nên cần thuê thêm một xe.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 30 <br> 10 | 3 |



### Bài 29 [pya_l02_p19_chuyen_xe_hoc_sinh]: Tính số chuyến xe cần thiết

Bối cảnh: Trường trung học cơ sở Ngôi Sao Sáng tổ chức chuyến dã ngoại tham quan bảo tàng cho $N$ học sinh. Nhà trường thuê xe khách loại nhỏ, mỗi xe chở tối đa $K$ em. Ban tổ chức cần tính chính xác số xe tối thiểu phải thuê sao cho tất cả học sinh đều có chỗ ngồi, kể cả khi xe cuối cùng không chở đủ $K$ em vẫn phải thuê nguyên chiếc.

Nhiệm vụ: Nhập hai số nguyên dương $N$ và $K$ trên 1 dòng. In ra số lượng xe tối thiểu cần thuê để chở hết tất cả học sinh.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $N, K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

In ra số xe tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 41 10 | 5 |

**Giải thích:**

4 xe chở được 40 em, còn 1 em vẫn cần thêm 1 xe nữa $\implies$ Cần 5 xe. Công thức làm tròn lên chuẩn: `(N + K - 1) // K`.



### Bài 30 [pya_l02_p21_chia_nguyen_chia_du]: Phép chia nguyên và chia dư cơ bản

Bối cảnh: Trong giờ thực hành lập trình tại phòng máy tính của trường, thầy giáo Minh giao cho học sinh bài tập thú vị: cho hai số nguyên dương bất kỳ, hãy tính đồng thời kết quả phép chia nguyên (phần nguyên) và phép chia lấy dư (phần dư). Hai phép toán này là nền tảng quan trọng trong rất nhiều bài toán tin học, từ tách chữ số đến kiểm tra tính chẵn lẻ.

Nhiệm vụ: Nhập hai số nguyên dương $A$ và $B$ trên 1 dòng. In ra thương nguyên $A // B$ và phần dư $A \% B$ trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $A, B$ ($1 \le B \le A \le 10^9$).

**Đầu ra (Output):**

Một dòng in ra $A // B$ và $A \% B$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 17 5 | 3 2 |

**Giải thích:**

$17 // 5 = 3$ và $17 \% 5 = 2$.



### Bài 31 [pya_l02_p08_kim_dong_ho_12_gio]: Kim đồng hồ 12 giờ

Bối cảnh: Trên tường lớp học treo một chiếc đồng hồ kim tròn xinh có 12 số đánh dấu từ 1 đến 12. Hiện tại kim giờ đang chỉ vào đúng số $H$. Cô giáo đố cả lớp: nếu chờ thêm đúng $K$ giờ nữa thì kim giờ sẽ nhích tới số mấy. Các bạn ngó nghiêng mãi chưa chắc chắn. Hãy giúp cả lớp tìm câu trả lời.

Nhiệm vụ: Sau đúng $K$ giờ nữa, hỏi kim giờ sẽ chỉ vào số mấy?

**Đầu vào (Input):**

Nhập vào 2 số nguyên $H$ ($1 \le H \le 12$) và $K$ ($1 \le K \le 10^9$).

**Đầu ra (Output):**

In ra một số nguyên từ 1 đến 12 là số mà kim giờ đang chỉ.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 5 | 3 |

**Giải thích:**

Lúc 10 giờ, sau 5 giờ nữa là 15 giờ. Trên đồng hồ 12 số tương ứng số 3.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 9 <br> 3 | 12 |

**Giải thích:**

Lúc 9 giờ, sau 3 giờ nữa là 12 giờ.



### Bài 32 [pya_l02_p06_chia_keo_hoc_sinh]: Chia kẹo cho các bạn

Bối cảnh: Nhân dịp tổng kết cuối năm, cô giáo chủ nhiệm lớp 6A mua $N$ chiếc kẹo sô-cô-la để thưởng cho $K$ bạn học sinh xuất sắc. Cô muốn chia đều kẹo cho các bạn sao cho mỗi bạn nhận được số kẹo bằng nhau, phần kẹo dư ra (nếu có) cô sẽ giữ lại để lần sau. Em hãy tính xem mỗi bạn được bao nhiêu chiếc kẹo và còn dư lại bao nhiêu chiếc.

Nhiệm vụ: Nhập hai số nguyên dương $N$ và $K$ trên 1 dòng. In ra 2 dòng:

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $N, K$ ($1 \le N, K \le 10^9$).

**Đầu ra (Output):**

Hai dòng lần lượt là thương nguyên và số kẹo dư.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 25 4 | 6 <br> 1 |

**Giải thích:**

Mỗi bạn được 6 kẹo, thừa lại 1 kẹo.



### Bài 33 [pya_l02_p12_ban_co_caro_vo_tan]: Bàn cờ Ca-rô vô tận

Bối cảnh: Giờ giải lao, hai bạn Bi và Bo rủ nhau chơi trên một bàn cờ ô vuông vô tận được chia thành các hàng, mỗi hàng có đúng $W$ ô vuông. Các ô vuông được đánh số liên tiếp bắt đầu từ $1$:
 * Hàng 1 gồm các ô: $1, 2, \dots, W$.
 * Hàng 2 gồm các ô: $W+1, W+2, \dots, 2W$.
 * Cứ như vậy tiếp tục cho các hàng tiếp theo.
Đến lượt đi, Bi chỉ vào một ô và đố Bo tìm vị trí của nó. Hãy tìm xem ô đó ở hàng mấy, cột mấy.

Nhiệm vụ: Cho biết số thứ tự của một ô là $K$. Hãy xác định xem ô đó nằm ở **Hàng thứ mấy** và **Cột thứ mấy** (Cột tính từ 1 đến $W$)?

**Đầu vào (Input):**

Gồm hai số tự nhiên $K$ và $W$ ($1 \le K, W \le 10^6$) mỗi số trên một dòng.

**Đầu ra (Output):**

In ra hai số nguyên trên một dòng cách nhau dấu cách: `hang cot`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 11 <br> 4 | 3 3 |

**Giải thích:**

Mỗi hàng có 4 ô.
Hàng 1: 1, 2, 3, 4
Hàng 2: 5, 6, 7, 8
Hàng 3: 9, 10, 11, 12.
Ô số 11 nằm ở Hàng 3, Cột 3.



### Bài 34 [pya_l02_p17_tong_ba_chu_so]: Tổng các chữ số của số có 3 chữ số

Bối cảnh: Bạn Tâm tham gia cuộc thi đố vui toán học với thử thách: nhìn vào một số nguyên dương có đúng 3 chữ số, phải nhanh chóng cộng tổng cả ba chữ số lại. Ví dụ với số $496$, tổng các chữ số là $4 + 9 + 6 = 19$. Thay vì tính nhẩm, Tâm muốn viết một chương trình Python giúp tự động tách ba chữ số hàng trăm, hàng chục, hàng đơn vị rồi cộng lại.

Nhiệm vụ: Nhập số nguyên $N$ ($100 \le N \le 999$). In ra tổng của 3 chữ số hàng trăm, hàng chục và hàng đơn vị.

**Đầu vào (Input):**

Một dòng chứa số nguyên $N$.

**Đầu ra (Output):**

In ra tổng các chữ số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 385 | 16 |

**Giải thích:**

Chữ số hàng trăm $385 // 100 = 3$. Chữ số hàng chục $(385 // 10) \% 10 = 8$. Chữ số hàng đơn vị $385 \% 10 = 5$. Tổng $= 3 + 8 + 5 = 16$.



### Bài 35 [pya_l02_p36_phan_so_dai_so]: Tính phân số đại số

Bối cảnh: Trong phòng thí nghiệm vật lý, hai nhóm học sinh đo được các thông số $a$, $b$, $c$, $d$ từ thí nghiệm đo quang phổ. Công thức tổng hợp kết quả cuối cùng là một biểu thức phân số: $S = \frac{a + b}{c + d}$. Thầy giáo yêu cầu mỗi nhóm viết chương trình Python để tính tự động giá trị $S$, đảm bảo kết quả là số thực (phép chia thực) chứ không phải phép chia nguyên.

Nhiệm vụ: Nhập 4 số nguyên $a, b, c, d$ trên 1 dòng. In ra giá trị $S$ (làm tròn 2 chữ số thập phân).

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên ($c + d \ne 0$).

**Đầu ra (Output):**

In ra giá trị số thực dạng `f"{S:.2f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 8 2 3 | 3.00 |

**Giải thích:**

$(7 + 8) / (2 + 3) = 15 / 5 = 3.00$.



### Bài 36 [pya_l02_p18_so_dao_nguoc_3_chu_so]: Số đảo ngược 3 chữ số

Bối cảnh: Trong trò chơi "Gương thần kỳ diệu" tại lễ hội trường, mỗi thí sinh viết một số nguyên dương có đúng 3 chữ số lên bảng. Tấm gương ma thuật sẽ "phản chiếu" số đó — tức là đảo ngược thứ tự các chữ số. Ví dụ: số $123$ qua gương trở thành $321$, số $400$ trở thành $004$ (tức là $4$). Em hãy lập trình mô phỏng tấm gương thần này.

Nhiệm vụ: Nhập số nguyên $N$ gồm 3 chữ số ($100 \le N \le 999$, chữ số tận cùng khác 0). In ra số đảo ngược của $N$.

**Đầu vào (Input):**

Một dòng chứa số $N$.

**Đầu ra (Output):**

In ra số đảo ngược.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 472 | 274 |

**Giải thích:**

Tách trăm $= 4$, chục $= 7$, đơn vị $= 2$. Số đảo ngược là $2 \times 100 + 7 \times 10 + 4 = 274$.



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l02_modulo_visual.png)



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l03_digit_extraction.png)



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l03_clock_cycle.png)



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



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l03_time_conversion.png)



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


## Bài tập thực hành


### Bài 01 [pya_l03_p31_doi_do_la_sang_tien_viet]: Đổi đô la sang tiền việt

Bối cảnh: Bác Hùng đi công tác ở nước ngoài về và mang theo $D$ tờ đô la Mỹ, mỗi tờ trị giá $1$ đô la. Bác muốn đổi hết sang tiền Việt Nam để mua quà cho cả nhà. Biết rằng ngân hàng đổi $1$ đô la lấy $25000$ đồng. Hãy giúp bác Hùng tính xem bác sẽ nhận được bao nhiêu tiền Việt Nam.

Nhiệm vụ: Hãy tính số tiền Việt Nam (đồng) đổi được từ $D$ đô la Mỹ.

**Đầu vào (Input):**

Nhập 1 số tự nhiên $D$ ($1 \le D \le 10^6$) trên 1 dòng.

**Đầu ra (Output):**

Số tiền Việt Nam tính bằng đồng (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 100000 |

**Giải thích:**

- Mỗi đô la đổi được $25000$ đồng.
- $4$ đô la đổi được: $4 \times 25000 = 100000$ đồng.



### Bài 02 [pya_l03_p01_hinh_vuong]: Chu vi và diện tích hình vuông

Bối cảnh: Bác thợ mộc Năm ở xưởng nội thất Hoàng Gia nhận được đơn hàng gia công một lô mặt bàn trà hình vuông cao cấp. Theo bản vẽ thiết kế, mỗi mặt bàn có cạnh dài $A$ mét. Trước khi cắt gỗ, bác cần tính chính xác chu vi (để dán viền bao quanh) và diện tích (để ước lượng lượng sơn phủ bề mặt) của mỗi tấm mặt bàn.

Nhiệm vụ: Nhập một số nguyên dương $A$ là cạnh hình vuông. In ra chu vi và diện tích của hình vuông trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa số nguyên dương $A$ ($1 \le A \le 10^4$).

**Đầu ra (Output):**

In ra chu vi và diện tích cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | 24 36 |

**Giải thích:**

Chu vi $6 \times 4 = 24$, Diện tích $6 \times 6 = 36$.



### Bài 03 [pya_l03_p06_doi_don_vi_dai]: Đổi mét sang centimet và milimet

Bối cảnh: Trên công trường xây dựng cầu vượt, kỹ sư trưởng nhận được bản vẽ ghi kích thước bằng đơn vị mét, nhưng máy cắt thép CNC lại yêu cầu nhập liệu theo xen-ti-mét. Anh cần một công cụ chuyển đổi nhanh giữa các đơn vị đo chiều dài: $1$ mét $= 100$ xen-ti-mét, $1$ ki-lô-mét $= 1000$ mét. Em hãy lập trình thực hiện phép chuyển đổi đơn vị chiều dài.

Nhiệm vụ: Nhập số nguyên dương $M$ (đơn vị mét). In ra 2 số trên 1 dòng cách nhau dấu cách: độ dài tương ứng theo centimet ($\text{cm}$) và milimet ($\text{mm}$).

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$ ($1 \le M \le 1000$).

**Đầu ra (Output):**

In ra hai số nguyên cách nhau dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 300 3000 |

**Giải thích:**

$3\text{m} = 300\text{cm} = 3000\text{mm}$.



### Bài 04 [pya_l03_p20_khung_tranh_hinh_vuong]: Khung tranh hình vuông

Bối cảnh: Trong quy trình gia công khung nhôm kính, người thợ cần chuẩn bị thanh nẹp viền bao quanh một tấm kính hình vuông có cạnh độ dài $a$.

Nhiệm vụ: Cho độ dài cạnh hình vuông $a$. Hãy tính chu vi của khung hình vuông ($4 \times a$).

**Đầu vào (Input):**

Một số tự nhiên $a$ ($1 \le a \le 10^4$).

**Đầu ra (Output):**

In ra 2 số nguyên cách nhau một khoảng trắng: Chu vi và Diện tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | 32 64 |

**Giải thích:**

Cạnh hình vuông có độ dài $a = 6$. Chu vi của hình vuông được tính bằng $4 \times 6 = 24$. Kết quả in ra là `24`.



### Bài 05 [pya_l03_p14_doi_do_c_sang_do_f]: Đổi độ C sang độ F

Bối cảnh: Trong giờ học khoa học, cô giáo đố cả lớp một điều thú vị. Ở Việt Nam, nhiệt độ được đo bằng độ C, còn ở nước Mỹ người ta lại dùng độ F. Hôm nay trời nóng $C$ độ C, và $C$ luôn chia hết cho $5$. Hãy giúp cả lớp đổi nhiệt độ này sang độ F để kể cho người dùng ở Mỹ nghe.

Nhiệm vụ: Hãy đổi nhiệt độ $C$ độ C sang độ F theo công thức $F = C \times 9 : 5 + 32$.

**Đầu vào (Input):**

Nhập 1 số nguyên $C$ ($-50 \le C \le 50$, $C$ chia hết cho $5$) trên 1 dòng.

**Đầu ra (Output):**

Nhiệt độ tính bằng độ F (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 30 | 86 |

**Giải thích:**

- Đổi sang độ F: $30 \times 9 : 5 + 32 = 270 : 5 + 32 = 54 + 32 = 86$.



### Bài 06 [pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat]: Cạnh còn lại của hình chữ nhật

Bối cảnh: Ngoài làng có một cái ao cá hình chữ nhật rất mát, một cạnh của ao bằng $a\text{ mét}$ và chu vi của ao là $P\text{ mét}$ ($P$ là số chẵn). Cuối tuần, các người dùng rủ nhau ra ao câu cá và đố nhau tìm cạnh còn lại của ao. Hãy giúp các bạn tính độ dài cạnh còn lại.

Nhiệm vụ: Hãy tính và in ra độ dài của cạnh còn lại của hình chữ nhật.

**Đầu vào (Input):**

Gồm 2 dòng: dòng 1 chứa chu vi $P$ ($P$ chẵn, $P \le 10^6$), dòng 2 chứa độ dài cạnh đã biết $a$ ($1 \le a < P // 2$).

**Đầu ra (Output):**

Một số tự nhiên là độ dài cạnh còn lại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 30 <br> 5 | 10 |

**Giải thích:**

Nửa chu vi là: $30 : 2 = 15$. Cạnh còn lại: $15 - 5 = 10$.



### Bài 07 [pya_l03_p11_dien_tich_tam_giac_vuong]: Diện tích tam giác vuông

Bối cảnh: Na có một miếng bánh hình tam giác vuông rất xinh. Hai cạnh góc vuông của miếng bánh dài $a\text{ cm}$ và $h\text{ cm}$. Tích $a \times h$ luôn là số chẵn. Na muốn biết miếng bánh của mình rộng bao nhiêu để khoe với cả lớp. Hãy tính diện tích miếng bánh.

Nhiệm vụ: Hãy tính diện tích của hình tam giác vuông có hai cạnh góc vuông là $a$ và $h$.

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a$ và $h$ ($1 \le a, h \le 1000$, tích $a \times h$ chia hết cho $2$) trên 2 dòng.

**Đầu ra (Output):**

Diện tích của hình tam giác vuông (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 <br> 4 | 12 |

**Giải thích:**

- Tích hai cạnh góc vuông: $6 \times 4 = 24$.
- Diện tích tam giác: $24 : 2 = 12$.



### Bài 08 [pya_l03_p21_chu_vi_tam_giac_abc]: Chu vi tam giác ABC

Bối cảnh: Trong giờ học hình học vui nhộn, thầy giáo vẽ một hình tam giác $ABC$ lên bảng và đố cả lớp. Thầy cho 3 số tự nhiên $a, b, c$ lần lượt là độ dài 3 cạnh của tam giác $ABC$. Các bạn thi nhau giơ tay xung phong tính chu vi. Hãy giúp cả lớp tính chu vi của tam giác $ABC$.

Nhiệm vụ: Hãy lập trình tính và đưa ra chu vi của tam giác $ABC$.

**Đầu vào (Input):**

Ba dòng lần lượt ghi 3 số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^8$).

**Đầu ra (Output):**

In ra một số tự nhiên duy nhất là chu vi tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 4 <br> 5 | 12 |

**Giải thích:**

Chu vi: $3 + 4 + 5 = 12$.



### Bài 09 [pya_l03_p30_the_tich_hop_chu_nhat]: Thể tích hộp chữ nhật

Bối cảnh: Một khối hộp vừa được tặng một hộp sữa dâu hình hộp chữ nhật. Hộp sữa có chiều dài $d\text{ cm}$, chiều rộng $r\text{ cm}$ và chiều cao $c\text{ cm}$. Một khối hộp tò mò muốn biết hộp sữa của mình chứa được bao nhiêu sữa. Hãy giúp bài toán tính thể tích của hộp sữa.

Nhiệm vụ: Hãy tính thể tích của hình hộp chữ nhật có ba kích thước $d, r, c$.

**Đầu vào (Input):**

Nhập 3 số tự nhiên $d, r, c$ ($1 \le d, r, c \le 1000$) trên 3 dòng.

**Đầu ra (Output):**

Thể tích của hình hộp chữ nhật (số nguyên).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 3 <br> 2 | 30 |

**Giải thích:**

- Thể tích hộp: $5 \times 3 \times 2 = 30$.



### Bài 10 [pya_l03_p19_manh_vuon_chu_nhat]: Mảnh vườn chữ nhật

Bối cảnh: Cuối làng có bác nông dân chăm chỉ với một mảnh vườn trồng rau hình chữ nhật có chiều dài $a\text{ mét}$ và chiều rộng $b\text{ mét}$. Mỗi sáng, bác ra vườn tưới rau xanh mướt, nhưng bác muốn rào quanh vườn và tính diện tích để trồng thêm rau mới. Hãy giúp bác tính chu vi và diện tích của mảnh vườn.

Nhiệm vụ: Hãy tính chu vi và diện tích của mảnh vườn đó.

**Đầu vào (Input):**

Gồm 2 dòng lần lượt chứa 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$).

**Đầu ra (Output):**

In ra trên một dòng 2 số nguyên cách nhau một dấu cách lần lượt là: Chu vi và Diện tích của mảnh vườn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 6 | 32 60 |

**Giải thích:**

Chu vi: $(10 + 6) \times 2 = 32$. Diện tích: $10 \times 6 = 60$.



### Bài 11 [pya_l03_p10_dien_tich_bon_hoa_chu_thap]: Diện tích bồn hoa chữ thập

Bối cảnh: Trong công viên xanh mát có một bồn hoa hình chữ thập (dấu cộng) rất đẹp được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
 * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
 * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
 * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
Cô công nhân muốn biết diện tích thật để gieo hạt, vì phần giao nhau ở giữa không được tính hai lần. Hãy giúp cô tính diện tích bồn hoa.

Nhiệm vụ: Hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).

**Đầu vào (Input):**

Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.

**Đầu ra (Output):**

Diện tích thực tế của bồn hoa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 3 | 51 |

**Giải thích:**

- Luống ngang: $10 \times 3 = 30$.
- Luống dọc: $3 \times 10 = 30$.
- Phần giao nhau ở giữa: $3 \times 3 = 9$.
- Diện tích bồn hoa: $30 + 30 - 9 = 51$.



### Bài 12 [pya_l03_p08_thuan_di_gap_anh]: Thuận đi gặp ánh

Bối cảnh: Chiều nắng đẹp, hai bạn Thuận và Ánh sống trên một con đường làng thẳng có các mốc tọa độ tính bằng kilomet. Thuận đang đứng ở vị trí $x$, còn Ánh đang đứng ở vị trí $y$ ($x < y$). Thuận nhảy lên xe đạp và phóng về phía nhà Ánh với vận tốc không đổi là $v\text{ km/h}$ để rủ bạn đi đá bóng.
* **Biết rằng:** Khoảng cách $y - x$ chia hết cho vận tốc $v$.
Ánh đứng chờ ở cổng, hồi hộp không biết bao lâu bạn tới. Hãy giúp hai bạn tính thời gian Thuận đi gặp Ánh.

Nhiệm vụ: Sau bao nhiêu giờ thì Thuận sẽ gặp được Ánh?

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $x, y, v$ ($0 \le x < y \le 10^9, 1 \le v \le 10^9$).

**Đầu ra (Output):**

Số giờ để Thuận gặp Ánh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 70 <br> 15 | 4 |

**Giải thích:**

Khoảng cách giữa 2 bạn: $70 - 10 = 60\text{ km}$.
Thời gian gặp nhau: $60 : 15 = 4$ giờ.



### Bài 13 [pya_l03_p23_ho_ca_sau_va_dao_nho]: Hồ cá sấu và đảo nhỏ

Bối cảnh: Ở một trang trại vui vẻ có một hồ nước hình vuông cạnh $A$ nuôi những chú cá sấu con hiền lành. Ở chính giữa hồ, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$ để cá sấu bò lên phơi nắng (hòn đảo nằm trọn trong hồ nước và không chạm vào bờ hồ). Các người dùng thắc mắc mặt nước còn lại rộng bao nhiêu để cá bơi lội. Hãy giúp các bạn tính diện tích mặt nước còn lại.

Nhiệm vụ: Hãy tính diện tích phần mặt nước còn lại sau khi đã xây hòn đảo nhỏ.

**Đầu vào (Input):**

Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le B, C < A \le 10^4$).

**Đầu ra (Output):**

Một số nguyên duy nhất là diện tích mặt nước còn lại.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 3 <br> 4 | 88 |

**Giải thích:**

Diện tích hồ: $10 \times 10 = 100$. Diện tích đảo: $3 \times 4 = 12$.
Mặt nước còn lại: $100 - 12 = 88$.



### Bài 14 [pya_l03_p03_chu_vi_tam_giac]: Chu vi hình tam giác

Bối cảnh: Đội thi đấu robotics của trường cần thiết kế một tấm chắn bảo vệ hình tam giác cho robot chiến đấu. Ba cạnh của tấm chắn có độ dài lần lượt là $a$, $b$ và $c$ xen-ti-mét. Để mua đủ thanh nhôm gia cố viền ngoài, đội trưởng cần tính chính xác chu vi của tấm chắn tam giác này.

Nhiệm vụ: Nhập 3 số nguyên dương $A, B, C$ trên cùng một dòng. In ra chu vi của bồn hoa đó.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^4$).

**Đầu ra (Output):**

In ra chu vi hình tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 8 | 20 |

**Giải thích:**

Chu vi $= 5 + 7 + 8 = 20$.



### Bài 15 [pya_l03_p09_phut_sang_gio_phut]: Đổi phút sang giờ và phút

Bối cảnh: Tại trung tâm huấn luyện thể thao quốc gia, huấn luyện viên ghi lại thời gian thi đấu của vận động viên bằng tổng số phút (ví dụ: $135$ phút). Để báo cáo lên ban huấn luyện, anh cần quy đổi sang dạng "$X$ giờ $Y$ phút" cho trực quan. Em hãy viết chương trình chuyển đổi từ tổng số phút sang dạng giờ-phút.

Nhiệm vụ: Nhập số nguyên dương $M$ ($1 \le M \le 10^6$). In ra định dạng `X gio Y phut`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $M$.

**Đầu ra (Output):**

In ra định dạng `X gio Y phut`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 135 | 2 gio 15 phut |

**Giải thích:**

$135 // 60 = 2$ giờ và $135 \% 60 = 15$ phút.



### Bài 16 [pya_l03_p33_tinh_van_toc_lam_tron]: Tính vận tốc làm tròn

Bối cảnh: Cuối tuần, bạn Mít đạp xe đi thăm bà ngoại. Quãng đường từ nhà Mít đến nhà bà dài $D\text{ km}$, và bạn Mít đạp xe hết $T$ giờ. Mẹ dặn bạn Mít phải ghi lại vận tốc trung bình của chuyến đi, làm tròn đến đúng $2$ chữ số sau dấu chấm thập phân. Hãy giúp bạn Mít tính vận tốc của chuyến đi.

Nhiệm vụ: Hãy tính vận tốc trung bình $V = D : T$ (km/h) và in ra kết quả làm tròn đến $2$ chữ số thập phân.

**Đầu vào (Input):**

Nhập 2 số trên 2 dòng: quãng đường $D$ ($1 \le D \le 10^4$) và thời gian $T$ ($1 \le T \le 10^4$). Cả hai đều là số nguyên.

**Đầu ra (Output):**

Vận tốc trung bình làm tròn đến $2$ chữ số thập phân.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 <br> 6 | 16.67 |

**Giải thích:**

- Vận tốc: $100 : 6 = 16.666\ldots$.
- Làm tròn đến $2$ chữ số thập phân được $16.67$ km/h.



### Bài 17 [pya_l03_p25_lat_gach_san_truong]: Lát gạch sân trường

Bối cảnh: Sân trường của trường học sinh iKHEDU có hình chữ nhật dài $D\text{ mét}$ và rộng $R\text{ mét}$, nơi các bạn chơi nhảy dây mỗi giờ ra chơi. Hè này, nhà trường muốn lát gạch men cho toàn bộ sân trường bằng các viên gạch hình vuông có cạnh là $K\text{ mét}$ ($D$ và $R$ đều chia hết cho $K$). Bác lao công đã chở gạch đến đầy sân. Hãy giúp bác đếm số viên gạch cần dùng.

Nhiệm vụ: Tính số lượng viên gạch men cần dùng để lát kín mặt sân.

**Đầu vào (Input):**

Ba dòng lần lượt chứa 3 số tự nhiên $D, R, K$ ($1 \le K \le R \le D \le 1000$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số viên gạch.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 <br> 10 <br> 2 | 50 |

**Giải thích:**

Diện tích sân: $20 \times 10 = 200$. Diện tích 1 viên gạch: $2 \times 2 = 4$.
Số gạch cần: $200 : 4 = 50$ viên.



### Bài 18 [pya_l03_p27_rao_quanh_vuon_hoa_co_cua]: Rào quanh vườn hoa có cửa

Bối cảnh: Bác thợ làm vườn có một vườn hoa rực rỡ hình chữ nhật với chiều dài $a\text{ mét}$, chiều rộng $b\text{ mét}$, thơm ngát mùi hoa hồng. Bác muốn dựng một hàng rào thép gai xung quanh vườn hoa, nhưng chừa lại một lối đi ở một góc vườn làm cổng ra vào rộng đúng $c\text{ mét}$ (không rào cửa).
* **Biết giá thành làm rào:** Mỗi mét hàng rào tốn $15$ nghìn đồng.
Bác đã chuẩn bị tiền nhưng chưa biết có đủ không. Hãy giúp bác tính tổng số tiền mua rào.

Nhiệm vụ: Tính tổng số tiền (nghìn đồng) bác thợ cần dùng để mua đủ rào thép.

**Đầu vào (Input):**

Ba dòng lần lượt là $a, b, c$ ($1 \le a, b \le 10^4, 1 \le c < (a + b) * 2$).

**Đầu ra (Output):**

Một số nguyên là số tiền (nghìn đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 <br> 8 <br> 2 | 570 |

**Giải thích:**

Chu vi cả vườn: $(12 + 8) \times 2 = 40\text{ m}$.
Độ dài rào cần mua: $40 - 2 = 38\text{ m}$.
Số tiền: $38 \times 15 = 570$ nghìn đồng.



### Bài 19 [pya_l03_p02_hinh_chu_nhat]: Chu vi và diện tích hình chữ nhật

Bối cảnh: Sân bóng rổ đa năng của trường trung học cơ sở Lê Quý Đôn vừa được tân trang lại. Theo bản đo đạc, sân có chiều dài $A$ mét và chiều rộng $B$ mét. Ban quản lý cơ sở vật chất cần tính chu vi sân để mua đủ lưới rào bảo vệ, đồng thời tính diện tích sân để đặt mua sơn kẻ vạch sân thi đấu theo tiêu chuẩn.

Nhiệm vụ: Nhập hai số nguyên dương $A$ và $B$ trên cùng 1 dòng. In ra chu vi và diện tích của sân bóng rổ trên cùng một dòng cách nhau dấu cách.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên dương $A, B$ ($1 \le B \le A \le 10^4$).

**Đầu ra (Output):**

In ra chu vi và diện tích.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 6 | 32 60 |

**Giải thích:**

Chu vi $2 \times (10 + 6) = 32$, Diện tích $10 \times 6 = 60$.



### Bài 20 [pya_l03_p07_doi_khoi_luong]: Đổi tạ và yến sang kilogram

Bối cảnh: Tại cảng xuất khẩu nông sản Cát Lái, mỗi container hàng ghi trọng lượng bằng đơn vị gam. Tuy nhiên, phiếu hải quan yêu cầu khai báo bằng ki-lô-gam và tấn. Nhân viên kho vận cần một chương trình chuyển đổi nhanh giữa các đơn vị khối lượng: $1$ ki-lô-gam $= 1000$ gam, $1$ tấn $= 1000$ ki-lô-gam. Em hãy giúp họ tự động hóa việc quy đổi.

Nhiệm vụ: Nhập hai số nguyên $T$ và $Y$ trên cùng 1 dòng. In ra tổng khối lượng thóc tính bằng kilogram ($\text{kg}$).

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $T, Y$ ($0 \le T, Y \le 1000$).

**Đầu ra (Output):**

In ra tổng khối lượng theo $\text{kg}$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 3 | 530 |

**Giải thích:**

$5\text{ tạ} = 500\text{kg}$, $3\text{ yến} = 30\text{kg}$. Tổng $= 500 + 30 = 530\text{kg}$.



### Bài 21 [pya_l03_p32_hang_rao_manh_dat]: Hàng rào quanh mảnh đất

Bối cảnh: Bác Năm có mảnh vườn hình chữ nhật dài $A$ mét, rộng $B$ mét. Bác muốn làm hàng rào lưới thép xung quanh, chừa lại một cổng ra vào rộng $C$ mét.

Nhiệm vụ: Nhập 3 số nguyên $A, B, C$ trên cùng 1 dòng ($C < 2 \times (A + B)$). In ra tổng chiều dài hàng rào lưới thép cần mua.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, C$ ($1 \le A, B \le 10^4$, $1 \le C \le 100$).

**Đầu ra (Output):**

In ra chiều dài hàng rào.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 15 3 | 67 |

**Giải thích:**

Chu vi mảnh vườn $= 2 \times (20 + 15) = 70\text{m}$. Trừ cổng $3\text{m} \implies 70 - 3 = 67\text{m}$.



### Bài 22 [pya_l03_p18_chay_bo_gap_nhau]: Bài toán chạy bộ hai người ngược chiều

Bối cảnh: Hai bạn An và Bình ở hai đầu một con đường thẳng dài $S$ mét. Cùng lúc, hai bạn chạy lại phía nhau: An chạy với vận tốc $V_1$ mét/giây, Bình chạy với vận tốc $V_2$ mét/giây.

Nhiệm vụ: Nhập 3 số nguyên $S, V_1, V_2$ trên cùng 1 dòng. In ra thời gian (tính bằng giây) kể từ lúc bắt đầu chạy cho đến khi hai bạn gặp nhau, làm tròn 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên dương $S, V_1, V_2$ ($1 \le S \le 10^5$, $1 \le V_1, V_2 \le 100$).

**Đầu ra (Output):**

In ra thời gian gặp nhau dạng `f"{t:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 150 2 3 | 30.0 |

**Giải thích:**

Vận tốc tiếp cận $= 2 + 3 = 5\text{m/s}$. Thời gian gặp nhau $= 150 / 5 = 30.0$ giây.



### Bài 23 [pya_l03_p22_dien_tich_tam_giac_vuong]: Diện tích tam giác vuông

Bối cảnh: Kiến trúc sư Hà đang thiết kế một khu vườn trang trí trước sảnh tòa nhà văn phòng. Khu vườn có dạng hình tam giác vuông với hai cạnh góc vuông lần lượt dài $a$ mét và $b$ mét. Để ước tính lượng cỏ nhân tạo cần trải và chi phí thi công, cô cần tính chính xác diện tích khu vườn tam giác vuông này.

Nhiệm vụ: Nhập hai số nguyên dương $A, B$ trên cùng 1 dòng. In ra diện tích lá cờ dưới dạng số thực lấy đúng 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa hai số nguyên $A, B$ ($1 \le A, B \le 10^4$).

**Đầu ra (Output):**

In ra diện tích định dạng `f"{S:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 7 | 17.5 |

**Giải thích:**

Diện tích $= (5 \times 7) / 2 = 17.5$.



### Bài 24 [pya_l03_p29_doi_sang_tong_giay]: Đổi giờ - phút - giây sang tổng số giây

Bối cảnh: Bài toán ngược lại: Cần quy đổi thời gian hiển thị `H giờ M phút S giây` về một số giây duy nhất để máy tính dễ so sánh.

Nhiệm vụ: Nhập 3 số nguyên $H, M, S$ trên cùng 1 dòng ($0 \le H \le 1000$, $0 \le M, S < 60$). In ra tổng số giây.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $H, M, S$.

**Đầu ra (Output):**

In ra một số nguyên là tổng số giây.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 15 30 | 8130 |

**Giải thích:**

$2 \times 3600 + 15 \times 60 + 30 = 7200 + 900 + 30 = 8130$.



### Bài 25 [pya_l03_p17_son_tuong_phong]: Tính tiền mua sơn quét tường

Bối cảnh: Một bức tường hình chữ nhật có chiều dài $A$ mét và chiều cao $H$ mét. Trên tường có một cửa sổ hình chữ nhật kích thước $X \times Y$ mét không cần quét sơn. Biết mỗi mét vuông tường tốn $G$ đồng tiền sơn.

Nhiệm vụ: Nhập 5 số nguyên $A, H, X, Y, G$ trên cùng 1 dòng. In ra tổng số tiền sơn cần chuẩn bị.

**Đầu vào (Input):**

Một dòng chứa 5 số nguyên dương ($X < A, Y < H$, $1 \le A, H \le 100$, $1 \le G \le 10^5$).

**Đầu ra (Output):**

In ra tổng số tiền sơn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 3 2 1 50000 | 800000 |

**Giải thích:**

Diện tích tường $= 6 \times 3 = 18\text{m}^2$. Diện tích cửa sổ $= 2 \times 1 = 2\text{m}^2$. Diện tích cần sơn $= 18 - 2 = 16\text{m}^2$. Tổng tiền $= 16 \times 50000 = 800000$ đồng.



### Bài 26 [pya_l03_p05_dien_tich_hinh_thang]: Diện tích hình thang

Bối cảnh: Thửa ruộng nhà ông Ba ở Cần Thơ có hình dạng hình thang cân, với đáy lớn dài $a$ mét, đáy nhỏ dài $b$ mét và chiều cao $h$ mét. Cuối vụ mùa, hợp tác xã cần tính diện tích thửa ruộng để quy đổi sản lượng lúa thu hoạch trên mỗi mét vuông và lập báo cáo năng suất nông nghiệp.

Nhiệm vụ: Nhập 3 số nguyên dương $A, B, H$ trên cùng một dòng. In ra diện tích thửa ruộng dưới dạng số thực lấy đúng 1 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, H$ ($1 \le B \le A \le 10^4$, $1 \le H \le 10^4$).

**Đầu ra (Output):**

In ra diện tích định dạng `f"{S:.1f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 8 5 | 50.0 |

**Giải thích:**

Diện tích $= ((12 + 8) \times 5) / 2 = 50.0$.



### Bài 27 [pya_l03_p26_van_toc_trung_binh]: Tính vận tốc trung bình

Bối cảnh: Xe buýt tuyến 01 khởi hành từ bến xe Miền Đông đi bến xe Miền Tây, quãng đường dài $S$ ki-lô-mét và xe chạy hết $T$ giờ (kể cả thời gian dừng đón trả khách). Công ty vận tải cần tính vận tốc trung bình thực tế của chuyến xe để đánh giá hiệu suất và điều chỉnh lịch trình cho phù hợp.

Nhiệm vụ: Nhập hai số nguyên $S$ và $T$ ($1 \le T \le 100$, $1 \le S \le 10^5$). In ra vận tốc trung bình của ô tô làm tròn 2 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa $S$ và $T$.

**Đầu ra (Output):**

In ra vận tốc dạng `f"{v:.2f}"` (đơn vị $\text{km/h}$).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 100 3 | 33.33 |

**Giải thích:**

$100 / 3 \approx 33.3333... \implies 33.33$.



### Bài 28 [pya_l03_p24_doi_giay_sang_gio_phut_giay]: Đổi giây sang giờ phút giây

Bối cảnh: Trong hệ thống theo dõi quỹ đạo trạm không gian, đồng hồ đo ghi nhận thời gian hoàn thành một vòng quỹ đạo là tổng cộng $S$ giây. Hệ thống cần hiển thị giá trị này dưới dạng tường minh: gồm bao nhiêu giờ ($H$), bao nhiêu phút ($M$) và bao nhiêu giây ($S$).

Nhiệm vụ: Nhập vào tổng số giây $S$. Hãy phân rã thành $H$ giờ, $M$ phút, $S$ giây.

**Đầu vào (Input):**

Một số nguyên $S$ ($0 \le S \le 10^8$).

**Đầu ra (Output):**

In ra ba số nguyên $H, M, S$ cách nhau một khoảng trắng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3665 | 1 1 5 |

**Giải thích:**

3665 giây = 1 giờ (3600s) + 1 phút (60s) + 5 giây.



### Bài 29 [pya_l03_p12_khoang_cach_thoi_gian]: Khoảng thời gian giữa hai thời điểm trong ngày

Bối cảnh: Bạn Minh bắt đầu học bài lúc $H_1$ giờ $M_1$ phút và kết thúc lúc $H_2$ giờ $M_2$ phút (trong cùng một ngày).

Nhiệm vụ: Nhập 4 số nguyên $H_1, M_1, H_2, M_2$ trên 1 dòng. In ra khoảng thời gian học tính theo đơn vị phút.

**Đầu vào (Input):**

Một dòng chứa 4 số nguyên ($0 \le H_1 \le H_2 \le 23$, $0 \le M_1, M_2 < 60$, thời điểm 2 không sớm hơn thời điểm 1).

**Đầu ra (Output):**

In ra số phút chênh lệch.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 30 10 15 | 105 |

**Giải thích:**

Từ 8h30 đến 10h15 là 1 giờ 45 phút $= 60 + 45 = 105$ phút.



### Bài 30 [pya_l03_p15_lat_gach_nen_nha]: Lát nền phòng học

Bối cảnh: Phòng học hình chữ nhật có chiều dài $L$ mét và chiều rộng $W$ mét. Người ta dùng các viên gạch hoa hình vuông cạnh $D$ centimet để lát nền.

Nhiệm vụ: Nhập 3 số nguyên dương $L, W, D$ trên cùng 1 dòng ($L, W$ tính bằng mét, $D$ tính bằng centimet). Giả sử phòng học vừa khít các viên gạch, hãy in ra tổng số viên gạch cần dùng.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $L, W, D$ ($1 \le L, W \le 100$, $10 \le D \le 100$).

**Đầu ra (Output):**

In ra số viên gạch cần dùng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 4 50 | 96 |

**Giải thích:**

Đổi $L = 600\text{cm}, W = 400\text{cm}$. Diện tích sàn $= 600 \times 400 = 240000\text{cm}^2$. Diện tích 1 viên gạch $= 50 \times 50 = 2500\text{cm}^2$. Số gạch $= 240000 // 2500 = 96$ viên.



### Bài 31 [pya_l03_p28_doi_giay_sang_gio_phut_giay]: Đổi tổng số giây sang giờ, phút, giây

Bối cảnh: Đồng hồ bấm giờ trong cuộc thi chạy marathon ghi nhận tổng thời gian là $T$ giây.

Nhiệm vụ: Nhập số nguyên dương $T$ ($1 \le T \le 10^9$). In ra theo định dạng `H:M:S`.

**Đầu vào (Input):**

Một dòng chứa số nguyên $T$.

**Đầu ra (Output):**

In ra chuỗi `H:M:S` (với $H$ là giờ, $M$ là phút, $S$ là giây).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3665 | 1:1:5 |

**Giải thích:**

1 giờ 1 phút 5 giây.



### Bài 32 [pya_l03_p13_diem_trung_binh]: Điểm trung bình môn học

Bối cảnh: Cuối học kỳ, hệ thống quản lý điểm số của trường tự động tính điểm trung bình từ các bài kiểm tra. Một học sinh có điểm ba môn chính lần lượt là $a$, $b$ và $c$. Điểm trung bình được tính bằng công thức $\text{TB} = \frac{a + b + c}{3}$. Em hãy lập trình tính điểm trung bình và in kết quả với số thập phân chính xác.

Nhiệm vụ: Nhập 3 số thực là điểm của 3 môn trên cùng 1 dòng. In ra điểm trung bình cộng làm tròn đúng 2 chữ số thập phân.

**Đầu vào (Input):**

Một dòng chứa 3 số thực ($0 \le d_1, d_2, d_3 \le 10$).

**Đầu ra (Output):**

In ra điểm trung bình dạng `f"{dtb:.2f}"`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8.5 9.0 7.5 | 8.33 |

**Giải thích:**

$(8.5 + 9.0 + 7.5) / 3 = 25.0 / 3 \approx 8.3333... \implies 8.33$.



### Bài 33 [pya_l03_p16_loi_di_quanh_ho]: Diện tích lối đi quanh hồ nước

Bối cảnh: Trong công viên có một hồ nước hình chữ nhật kích thước dài $A$ mét, rộng $B$ mét. Xung quanh hồ, người ta làm một lối đi dạo có bề rộng đồng đều là $D$ mét.

Nhiệm vụ: Nhập 3 số nguyên $A, B, D$ trên cùng 1 dòng. Hãy tính diện tích của lối đi dạo đó.

**Đầu vào (Input):**

Một dòng chứa 3 số nguyên $A, B, D$ ($1 \le A, B \le 10^4$, $1 \le D \le 100$).

**Đầu ra (Output):**

In ra diện tích lối đi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 8 2 | 88 |

**Giải thích:**

Kích thước cả hồ và lối đi là $(10 + 2 \times 2) = 14\text{m}$ và $(8 + 2 \times 2) = 12\text{m}$. Diện tích toàn phần $= 14 \times 12 = 168\text{m}^2$. Diện tích hồ $= 10 \times 8 = 80\text{m}^2$. Diện tích lối đi $= 168 - 80 = 88\text{m}^2$.



# CHƯƠNG 02: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP


# Bài 04: Cấu trúc rẽ nhánh

## 1. Bản chất của cấu trúc rẽ nhánh trong khoa học máy tính

Trong chương trình tuần tự, các dòng lệnh được máy tính thực thi từ trên xuống dưới một cách máy móc. Nhưng trong thực tế, máy tính cần biết **ra quyết định**: *nếu điều kiện đúng thì làm việc A, nếu sai thì làm việc B*.

Cấu trúc cho phép máy tính đổi hướng thực thi dựa trên điều kiện gọi là **cấu trúc rẽ nhánh**.



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l04_branching_visual.png)



---

## 2. Thiết lập điều kiện so sánh trong câu lệnh `if`

Ở Bài 02, chúng ta đã làm quen với các phép toán so sánh trả về kết quả Đúng (`True`) hoặc Sai (`False`). Trong cấu trúc rẽ nhánh, biểu thức so sánh đóng vai trò là **"người gác cổng"** quyết định máy tính có bước vào thực thi khối lệnh hay không:

| Phép so sánh | Ký hiệu | Cú pháp trong `if` | Ý nghĩa điều kiện |
|:---:|:---:|---|---|
| **Bằng nhau** | `==` | `if n == 0:` | Đúng khi giá trị của `n` bằng 0 |
| **Khác nhau** | `!=` | `if n != 0:` | Đúng khi giá trị của `n` khác 0 |
| **Lớn hơn** | `>` | `if diem > 5:` | Đúng khi `diem` lớn hơn 5 |
| **Nhỏ hơn** | `<` | `if diem < 5:` | Đúng khi `diem` nhỏ hơn 5 |
| **Lớn hơn hoặc bằng** | `>=` | `if tuoi >= 18:` | Đúng khi `tuoi` từ 18 trở lên |
| **Nhỏ hơn hoặc bằng** | `<=` | `if tuoi <= 10:` | Đúng khi `tuoi` từ 10 trở xuống |

> **LỖI BẮT BUỘC PHẢI NHỚ: NHẦM LẪN GIỮA DẤU GÁN `=` VÀ DẤU SO SÁNH `==`**
>
> * Dấu `=` (Một dấu bằng): Là **phép gán giá trị** từ vế phải vào biến ở vế trái (`x = 10`).
> * Dấu `==` (Hai dấu bằng liền nhau): Là **phép so sánh bằng**, trả về `True` hoặc `False`.
> * Nếu viết `if a = 5:` $\implies$ Máy tính sẽ báo lỗi cú pháp ngay lập tức: `SyntaxError: invalid syntax`.

---

## 3. Quy tắc Thụt lề — Linh hồn của cú pháp Python

Trong nhiều ngôn ngữ khác, người ta dùng cặp ngoặc nhọn `{ }` hoặc cặp từ khóa `begin ... end` để gom các dòng lệnh thành một khối.

Python bỏ hết các cặp ngoặc rườm rà này và dùng **quy tắc Thụt lề**:
* Các dòng lệnh trong cùng một khối lệnh con **bắt buộc thụt vào trong cùng một khoảng cách** (chuẩn là **4 dấu cách / 1 phím Tab**).
* Hết khối lệnh con, dòng tiếp theo lùi ra bằng lề với câu lệnh cha.
* Dấu hai chấm `:` cuối dòng điều kiện là **bắt buộc**, báo cho Python biết sắp bắt đầu một khối lệnh thụt lề mới.

```python
diem = 8
if diem >= 5:
    print("Chuc mung!")       # Thuộc khối lệnh IF (Thụt lề 4 dấu cách)
    print("Ban da qua mon.")  # Thuộc khối lệnh IF (Thụt lề 4 dấu cách)
print("Ket thuc chuong trinh.") # Không thuộc IF, luôn luôn được in
```

---

## 4. 3 Dạng cấu trúc rẽ nhánh từ cơ bản đến phức tạp

### 4.1. Dạng 1: Cấu trúc `if` đơn (Khuyết thiếu)
Chỉ làm một việc khi điều kiện đúng; nếu sai thì bỏ qua và đi tiếp.

```python
n = int(input())
if n < 0:
    n = -n  # Nếu n là số âm, đổi dấu thành số dương
print(n)
```

### 4.2. Dạng 2: Cấu trúc `if - else` (Đầy đủ)
Hai nhánh đối lập nhau: điều kiện `True` thì làm khối `if`, `False` thì làm khối `else`.

```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```

### 4.3. Dạng 3: Cấu trúc đa nhánh `if - elif - else`
Dùng khi có từ 3 lựa chọn trở lên. Từ khóa `elif` là viết tắt của *Else If (Nếu không thì xét tiếp)*:
* Python xét các điều kiện lần lượt từ trên xuống dưới.
* Gặp điều kiện đúng đầu tiên, Python chạy khối lệnh đó rồi **bỏ qua toàn bộ các nhánh `elif` và `else` còn lại**.

```python
# Ví dụ: Xếp loại học tập theo thang điểm
diem = float(input())
if diem >= 8.0:
    print("GIOI")
elif diem >= 6.5:
    print("KHA")
elif diem >= 5.0:
    print("TRUNG BINH")
else:
    print("YEU")
```

---

## 5. Kỹ thuật ghép nhiều điều kiện: `and`, `or`, `not`

Khi một quyết định đòi hỏi kết hợp nhiều yếu tố, ta dùng các liên từ logic đã học ở Bài 02 để nối các biểu thức điều kiện:

| Liên từ | Ý nghĩa trong `if` | Khi nào nhánh `if` được chạy? | Ví dụ thực tế |
|:---:|---|---|---|
| **`and`** | **ĐỒNG THỜI** (Và) | Khi **tất cả** các điều kiện con đều đúng | `if diem >= 8 and hanh_kiem == "Tot":` |
| **`or`** | **HOẶC** (Ít nhất một) | Khi **có ít nhất một** điều kiện con đúng | `if thu == "Bay" or thu == "Chu Nhat":` |
| **`not`** | **PHỦ ĐỊNH** (Đảo ngược) | Khi điều kiện bên trong bị sai | `if not hop_le:` |

### Thứ tự ưu tiên logic:
1. Phép so sánh số học: `>`, `<`, `==`, ...
2. `not`
3. `and`
4. `or`
* **Lời khuyên an toàn:** Luôn dùng ngoặc tròn `( )` để gom nhóm các điều kiện phức tạp, giúp đoạn lệnh trong sáng và không bị hiểu nhầm thứ tự ưu tiên (ví dụ: `if (a > 0 and b > 0) or c > 0:`).

---

## 6. Các bài toán thuật toán kinh điển khi làm bài

### 6.1. Tìm số lớn nhất giữa 2 số
```python
a, b = map(int, input().split())
if a > b:
    max_val = a
else:
    max_val = b
print(max_val)
```

### 6.2. Tìm số lớn nhất giữa 3 số (Kỹ thuật Lính canh - Sentinel)
```python
a, b, c = map(int, input().split())
# Đặt a làm lính canh giữ ngôi vị lớn nhất tạm thời
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(max_val)
```

### 6.3. Kiểm tra 3 cạnh có tạo thành tam giác hợp lệ
Theo định lý Bất đẳng thức tam giác, 3 cạnh $a, b, c$ ($a, b, c > 0$) tạo thành một tam giác khi **tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại**:
$$\begin{cases} a + b > c \\ a + c > b \\ b + c > a \end{cases}$$

```python
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```

### 6.4. Bài toán kiểm tra Năm Nhuận
Một năm $Y$ là năm nhuận khi và chỉ khi:
* Năm đó chia hết cho 400.
* **HOẶC** (Năm đó chia hết cho 4 và không chia hết cho 100).

```python
nam = int(input())
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print("NAM NHUAN")
else:
    print("KHONG NHUAN")
```

---

## 7. Bảng mô phỏng biến thiên ô nhớ

Xét đoạn chương trình xếp loại học lực với `diem = 7.2`:
```python
diem = 7.2
if diem >= 8.0:
    loai = "GIOI"
elif diem >= 6.5:
    loai = "KHA"
elif diem >= 5.0:
    loai = "TB"
else:
    loai = "YEU"
```

### Bảng theo dõi luồng điều khiển của CPU:

| Bước | Điều Kiện Được Đánh Giá | Biểu Thức Tính Toán | Kết Quả Boolean | Hành Động Của CPU |
|:---:|---|---|:---:|---|
| **1** | Nhánh `if diem >= 8.0` | `7.2 >= 8.0` | `False` | Bỏ qua khối lệnh `"GIOI"`, nhảy xuống xét nhánh `elif` kế tiếp |
| **2** | Nhánh `elif diem >= 6.5` | `7.2 >= 6.5` | **`True`** | **Khớp điều kiện!** Thực thi lệnh `loai = "KHA"` |
| **3** | Các nhánh còn lại bên dưới | `diem >= 5.0`, `else` | *(Bỏ qua)* | **Thoát ngay lập tức khỏi toàn bộ cấu trúc if**, không xét tiếp |

$$\implies \text{Kết quả cuối cùng lưu trong biến } loai = \text{"KHA"}$$

---

## 8. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: QUÊN DẤU HAI CHẤM `:` Ở ĐẦU CÂU LỆNH**
> * Viết `if x > 0` $\implies$ Báo lỗi `SyntaxError: expected ':'`.

> **BẪY LỖI 2: THỤT LỀ KHÔNG ĐỒNG ĐỀU (`IndentationError`)**
> * Dòng trên thụt 4 dấu cách, dòng dưới thụt 2 dấu cách trong cùng một khối lệnh sẽ bị chương trình kiểm tra dừng ngay lập tức: `IndentationError: unindent does not match any outer indentation level`.

> **BẪY LỖI 3: DÙNG NHIỀU `if` ĐỘC LẬP THAY VÌ CHUỖI `elif`**
> * Hãy xem đoạn code sai lầm sau:
>  ```python
>   if diem >= 5.0:
>       print("DAT")
>   if diem >= 8.0:
>       print("XUAT SAC")
>   ```
>  Nếu học sinh được `9.0` điểm, chương trình sẽ in ra **CẢ HAI DÒNG**: `DAT` và `XUAT SAC`!
> * **Cách viết đúng:** Luôn dùng chuỗi `if - elif` để đảm bảo các điều kiện được sắp xếp theo thứ tự phân loại chặt chẽ.

---

## 9. Mẫu code thường gặp

```python
# Mẫu kiểm tra số chẵn lẻ và số âm dương
n = int(input())
if n > 0:
    if n % 2 == 0:
        print("DUONG CHAN")
    else:
        print("DUONG LE")
elif n < 0:
    print("SO AM")
else:
    print("SO KHONG")
```


## Bài tập thực hành


### Bài 01 [pya_l04_p04_so_lon_nhat_trong_hai_so]: Số lớn nhất trong hai số

Bối cảnh: Bộ vi xử lý cần thực hiện thao tác so sánh logic giữa hai thanh ghi dữ liệu $A$ và $B$ để giữ lại giá trị cực đại phục vụ tính toán tiếp theo.

Nhiệm vụ: Cho hai số nguyên $A$ và $B$. Hãy tìm và in ra giá trị lớn nhất trong hai số đó.

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Một số nguyên là giá trị lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| -15 <br> 8 | 8 |

**Giải thích:**

Hai số đầu vào là $25$ và $42$. Số lớn hơn là $42$. Kết quả in ra: `42`.



### Bài 02 [pya_l04_p09_tri_tuyet_doi_cua_mot_so]: Trị tuyệt đối của một số

Bối cảnh: Trong tính toán tọa độ và độ lệch kỹ thuật số, giá trị tuyệt đối $|x|$ thể hiện khoảng cách từ điểm đo đến mốc tham chiếu số 0.

Nhiệm vụ: Cho số nguyên $x$. Hãy tính và in ra giá trị tuyệt đối $|x|$ của số đó.

**Đầu vào (Input):**

Một số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

Giá trị tuyệt đối của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| -25 | 25 |

**Giải thích:**

Số đầu vào là $-15$. Giá trị tuyệt đối của $-15$ là $|-15| = 15$. Kết quả in ra: `15`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 10 |



### Bài 03 [pya_l04_p02_ve_vao_cong_vien]: Vé vào công viên

Bối cảnh: Tại trạm kiểm soát tự động của công viên nước, hệ thống cảm biến quang học đo chiều cao $h$ (cm) của khách hàng để phân loại vé hợp lệ.

Nhiệm vụ: Nếu chiều cao $h \ge 130\text{ cm}$, in ra `VE NGUOI LON`. Nếu $h < 130\text{ cm}$, in ra `VE TRE EM`.

**Đầu vào (Input):**

Một số nguyên $h$ ($1 \le h \le 200$).

**Đầu ra (Output):**

`VE NGUOI LON` hoặc `VE TRE EM`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 135 | VE NGUOI LON |

**Giải thích:**

Chiều cao đo được là $135\text{ cm}$. Do $135 \ge 130$, khách hàng cần áp dụng mức vé người lớn. Kết quả in ra: `VE NGUOI LON`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 120 | VE TRE EM |



### Bài 04 [pya_l04_p01_kiem_tra_so_chan_le]: Kiểm tra số chẵn lẻ

Bối cảnh: Trong thuật toán phân nhánh xử lý luồng dữ liệu mạng, các gói tin mang số định danh chẵn và lẻ được chuyển tiếp qua hai kênh truyền tải khác nhau.

Nhiệm vụ: Cho số tự nhiên $N$. Hãy kiểm tra nếu $N$ là số chẵn in ra `CHAN`, ngược lại in ra `LE`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($0 \le N \le 10^9$).

**Đầu ra (Output):**

Chuỗi `CHAN` hoặc `LE`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 18 | CHAN |

**Giải thích:**

Số đầu vào là $18$. Vì $18$ chia hết cho $2$ ($18 \% 2 = 0$), nên đây là số chẵn. Kết quả in ra: `CHAN`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 | LE |



### Bài 05 [pya_l04_p06_dien_phep_tinh_lon_nhat]: Điền phép tính lớn nhất

Bối cảnh: Trong giờ toán vui, cô giáo viết lên bảng một số tự nhiên $A$ và biểu thức bí ẩn sau: $A \text{ ? } A = B$. Cô đố cả lớp hãy chọn một dấu trong ba dấu cộng, trừ, nhân để lấp vào chỗ dấu hỏi chấm. Thí sinh nào tìm được số $B$ to nhất sẽ được thưởng một tràng pháo tay. Hãy giúp cả lớp tìm ra số $B$ lớn nhất có thể.

Nhiệm vụ: Hãy dùng một trong các phép tính $+$, $-$, $\times$ điền vào dấu $?$ để giá trị $B$ đạt được là **lớn nhất**. In ra số $B$ lớn nhất tìm được.

**Đầu vào (Input):**

Một số tự nhiên $A$ ($0 \le A \le 100$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số $B$ lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 9 |

**Giải thích:**

$3 + 3 = 6$, $3 - 3 = 0$, $3 \times 3 = 9$. Số lớn nhất là 9.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 | 2 |

**Giải thích:**

$1 + 1 = 2$, $1 - 1 = 0$, $1 \times 1 = 1$. Số lớn nhất là 2!



### Bài 06 [pya_l04_p07_giam_gia_sieu_thi]: Giảm giá siêu thị

Bối cảnh: Cuối tuần, mẹ dẫn Bi đi siêu thị mua đồ thật vui. Siêu thị đang có chương trình khuyến mãi: khách hàng mua đơn hàng có tổng giá trị từ $500$ nghìn đồng trở lên sẽ được giảm giá ngay $50$ nghìn đồng, còn các đơn hàng dưới $500$ nghìn đồng thì giữ nguyên giá. Bi xung phong ra quầy tính tiền giúp mẹ. Hãy tính xem phải trả bao nhiêu tiền.

Nhiệm vụ: Nhập vào tổng tiền đơn hàng $N$ (nghìn đồng). Hãy in ra số tiền thực tế khách hàng phải trả sau khi đã áp dụng khuyến mãi.

**Đầu vào (Input):**

Một số nguyên dương $N$ ($1 \le N \le 10^6$).

**Đầu ra (Output):**

Số tiền phải trả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 620 | 570 |

**Giải thích:**

Được giảm 50 nghìn: $620 - 50 = 570$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 450 | 450 |

**Giải thích:**

Dưới 500 nghìn, không được giảm.



### Bài 07 [pya_l06_p03_ngay_nghi_cuoi_tuan]: Ngày nghỉ cuối tuần

Bối cảnh: Cô giáo chủ nhiệm dán thời khóa biểu tuần lên bảng và dạy cả lớp cách nhớ các ngày bằng số: `2` là Thứ Hai, `3` là Thứ Ba, cứ thế đến `7` là Thứ Bảy và `8` là Chủ Nhật. Bạn Cún thích nhất hai ngày cuối tuần vì được nghỉ học đi chơi với ông bà. Sáng nào Cún cũng nhìn vào con số trên lịch và đoán xem hôm nay thế nào. Hãy giúp Cún xem hôm đó được nghỉ hay phải đi học.

Nhiệm vụ: Nhập vào một số nguyên $d$ đại diện cho một ngày. Nếu $d$ là Thứ Bảy hoặc Chủ Nhật thì in `NGHI HOC`, ngược lại in `DI HOC`.

**Đầu vào (Input):**

Một số nguyên $d$ ($2 \le d \le 8$).

**Đầu ra (Output):**

`NGHI HOC` hoặc `DI HOC`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 7 | NGHI |

**Giải thích:**

Ngày 7 là thứ Bảy nên được nghỉ học.



### Bài 08 [pya_l04_p03_ai_cao_hon]: Ai cao hơn?

Bối cảnh: Trong hệ thống dữ liệu kiểm tra thể lực, số đo chiều cao của hai ứng viên Minh ($a\text{ cm}$) và Nam ($b\text{ cm}$) được ghi nhận.

Nhiệm vụ: Biết rằng $a \ne b$, hãy xác định và in ra tên của người có chiều cao lớn hơn (`Minh` hoặc `Nam`).

**Đầu vào (Input):**

Hai số tự nhiên $a$ và $b$ trên 2 dòng ($50 \le a, b \le 200, a \ne b$).

**Đầu ra (Output):**

Tên bạn cao hơn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 142 <br> 138 | Minh |

**Giải thích:**

Chiều cao của Minh là $142\text{ cm}$ và Nam là $138\text{ cm}$. Vì $142 > 138$, bạn Minh cao hơn. Kết quả in ra: `Minh`.



### Bài 09 [pya_l06_p01_so_chan_co_hai_chu_so]: Số chẵn có hai chữ số

Bối cảnh: Bạn Minh đang sưu tập các số chẵn có đúng hai chữ số để trang trí bảng tin lớp học. Hãy giúp Minh liệt kê tất cả các số đó.

Nhiệm vụ: Nhập vào một số tự nhiên $N$. Kiểm tra xem $N$ có phải là **số chẵn có đúng hai chữ số** hay không? Nếu đúng in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 24 | YES |

**Giải thích:**

24 là số chẵn và có 2 chữ số.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | NO |

**Giải thích:**

8 là số chẵn nhưng chỉ có 1 chữ số.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 35 | NO |

**Giải thích:**

35 có 2 chữ số nhưng là số lẻ.



### Bài 10 [pya_l05_p06_mario_cuu_cong_chua]: Mario cứu công chúa

Bối cảnh: Trong khu vườn trò chơi, bạn Mario có $K$ năng lượng còn Công chúa có $P$ năng lượng. Giữa hai người là một chiếc cầu thang có đỉnh cao $N$ bậc: Mario đứng ở chân cầu thang bên trái (cần đi lên $N$ bậc và đi xuống $N$ bậc), Công chúa đứng ở chân cầu thang bên phải (cần đi lên $N$ bậc). Mỗi bậc thang Mario đi tốn $1$ năng lượng, còn mỗi bậc thang Công chúa đi tốn $2$ năng lượng. Cả hai đều mong gặp được nhau trên cầu thang. Hãy giúp hai bạn xem với sức của mình có gặp được nhau không.

Nhiệm vụ: Hỏi với mức năng lượng hiện có, Mario và Công chúa có thể gặp được nhau ở một điểm nào đó trên cầu thang hay không? Nếu gặp được in `YES`, ngược lại in `NO`.
* **Biết rằng:** Tổng số bậc cầu thang từ chân bên này sang chân bên kia là $2N$. Để gặp nhau, tổng số bậc mà Mario leo được cộng với tổng số bậc mà Công chúa leo được phải $\ge 2N$.

**Đầu vào (Input):**

Ba số tự nhiên $K, P, N$ ($1 \le K, P, N \le 1000$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 3 <br> 2 | YES |

**Giải thích:**

Cầu thang $2N = 4$ bậc. Mario đi được $\min(3, 4) = 3$ bậc. Công chúa có 3 năng lượng đi được $3 // 2 = 1$ bậc. Tổng số bậc đi được là $3 + 1 = 4 \ge 4 \implies$ Gặp nhau!



### Bài 11 [pya_l06_p13_tien_dien_bac_thang]: Tiền điện bậc thang

Bối cảnh: Gia đình bạn Bông vừa nhận hóa đơn tiền điện tháng này. Nhà bạn đã dùng hết $N$ số điện. Giá điện được tính rất đơn giản: $100$ số điện đầu tiên có giá $2000$ đồng một số, từ số điện thứ $101$ trở đi có giá $3500$ đồng một số. Hãy giúp bạn Bông tính tổng số tiền điện cả nhà phải trả.

Nhiệm vụ: Hãy tính tổng tiền điện (đồng) phải trả cho $N$ số điện theo bảng giá trên.

**Đầu vào (Input):**

Nhập 1 số tự nhiên $N$ ($1 \le N \le 10^6$) trên 1 dòng.

**Đầu ra (Output):**

Tổng số tiền điện phải trả (số nguyên, tính bằng đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 120 | 270000 |

**Giải thích:**

- $100$ số đầu: $100 \times 2000 = 200000$ đồng.
- $20$ số còn lại: $20 \times 3500 = 70000$ đồng.
- Tổng cộng: $200000 + 70000 = 270000$ đồng.



### Bài 12 [pya_l04_p10_bac_tho_moc_cat_go]: Bác thợ mộc cắt gỗ

Bối cảnh: Trong xưởng gia công nội thất, một thanh gỗ có chiều dài $L$ được cưa thành các đoạn nhỏ có chiều dài đúng bằng $k$.

Nhiệm vụ: Cho hai số nguyên dương $L$ và $k$. Hãy tính số đoạn gỗ cưa được và phần chiều dài gỗ vụn còn thừa.

**Đầu vào (Input):**

Hai số tự nhiên $L$ và $K$ trên 2 dòng ($1 \le L, K \le 10^9$).

**Đầu ra (Output):**

Hai số cách nhau dấu cách `so_doan go_thua` hoặc in chữ `KHONG DU`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 17 <br> 5 | 3 2 |

**Giải thích:**

Thanh gỗ dài $17\text{ cm}$ cưa thành các đoạn $5\text{ cm}$. Số đoạn cưa được là $17 // 5 = 3$ đoạn, phần gỗ vụn còn thừa là $17 \% 5 = 2\text{ cm}$. Kết quả in ra: `3 2`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 10 | KHONG DU |



### Bài 13 [pya_l06_p04_diem_nam_trong_hinh_chu_nhat]: Điểm nằm trong hình chữ nhật

Bối cảnh: Trong giờ vẽ, Mít vẽ một khu vườn hình chữ nhật trên giấy ô ly. Bạn đặt góc dưới-trái của vườn tại điểm $(0, 0)$ và góc trên-phải tại điểm $(W, H)$ trong mặt phẳng tọa độ. Mít còn chấm một chú bướm đậu ở đâu đó và đố bạn xem bướm đậu trong vườn hay bay ra ngoài. Hãy giúp Mít kiểm tra chú bướm có nằm trong vườn không.

Nhiệm vụ: Nhập vào $W, H$ và tọa độ của một điểm $(x, y)$. Kiểm tra xem điểm $(x, y)$ có nằm bên trong hoặc trên mép biên của hình chữ nhật hay không? Nếu có in `TRONG`, ngược lại in `NGOAI`.

**Đầu vào (Input):**

Bốn số tự nhiên $W, H, x, y$ trên 4 dòng ($1 \le W, H \le 1000, 0 \le x, y \le 1000$).

**Đầu ra (Output):**

`TRONG` hoặc `NGOAI`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 3 5 5 | TRONG |

**Giải thích:**

Điểm (2, 3) nằm trọn vẹn bên trong hình chữ nhật từ (0, 0) đến (5, 5).



### Bài 14 [pya_l06_p02_boi_chung_cua_3_va_5]: Bội chung của 3 và 5

Bối cảnh: Trong trò chơi FizzBuzz phổ biến trên toàn thế giới, người chơi cần nhận biết các số chia hết cho 3, cho 5 hoặc cho cả hai. Hãy lập trình kiểm tra.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Nếu $N$ chia hết cho cả 3 và 5 thì in `FIZZBUZZ`. Ngược lại in `KHONG`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

`FIZZBUZZ` hoặc `KHONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | YES |

**Giải thích:**

Số 15 vừa chia hết cho 3 vừa chia hết cho 5.



### Bài 15 [pya_l06_p05_ba_canh_tam_giac_hop_le]: Ba cạnh tam giác hợp lệ

Bối cảnh: Thí sinh có ba que tính với các độ dài khác nhau. Bạn ấy muốn biết liệu ba que tính đó có thể ghép thành một hình tam giác hay không. Hãy giúp kiểm tra.

Nhiệm vụ: Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.

**Đầu vào (Input):**

Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).

**Đầu ra (Output):**

`HOP LE` hoặc `KHONG HOP LE`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 4 <br> 5 | HOP LE |

**Giải thích:**

$3+4>5$, $3+5>4$, $4+5>3$ đều đúng.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 3 <br> 6 | KHONG HOP LE |

**Giải thích:**

$2 + 3 = 5 < 6$ (Sai bất đẳng thức tam giác).



### Bài 16 [pya_l06_p06_kiem_tra_nam_nhuan]: Kiểm tra năm nhuận

Bối cảnh: Lịch treo tường năm nay có 365 hay 366 ngày? Để biết được, em cần xác định năm đó có phải năm nhuận hay không. Hãy viết chương trình kiểm tra.

Nhiệm vụ: Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.

**Đầu vào (Input):**

Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).

**Đầu ra (Output):**

`NAM NHUAN` hoặc `NAM THUONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2024 | NAM NHUAN |

**Giải thích:**

Với dữ liệu đầu vào là `2024`, kết quả thu được tương ứng là `NAM NHUAN`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1900 | NAM THUONG |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2000 | NAM NHUAN |



### Bài 17 [pya_l06_p09_rut_the_may_man]: Rút thẻ may mắn

Bối cảnh: Ngày hội chợ xuân, sân trường rộn ràng tiếng cười nói. Mỗi người dùng được bốc một chiếc thẻ có ghi một số tự nhiên $N$. Cô tổng phụ trách reo lên rằng chiếc thẻ được coi là "Thẻ Trúng Thưởng" nếu số $N$ chia hết cho 7, **HOẶC** số $N$ có chữ số tận cùng là 7. Bạn Tèo run run mở chiếc thẻ trên tay, hồi hộp không biết mình có trúng thưởng không. Hãy giúp Tèo xem chiếc thẻ có trúng thưởng không.

Nhiệm vụ: Nhập vào số $N$ trên thẻ. In ra `TRUNG THUONG` nếu trúng thưởng, ngược lại in `CHUC MAY MAN LAN SAU`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Thông báo tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 14 | TRUNG THUONG |

**Giải thích:**

Số 14 chia hết cho 7 nên chiếc thẻ trúng thưởng.



### Bài 18 [pya_l05_p03_so_lon_nhat_trong_ba_so]: Số lớn nhất trong ba số

Bối cảnh: Ba bạn học sinh thi chạy 100 mét. Mỗi bạn chạy được một thành tích khác nhau. Hãy tìm bạn có thành tích tốt nhất (số lớn nhất).

Nhiệm vụ: Nhập vào 3 số nguyên $a, b, c$ mỗi số trên một dòng. Hãy tìm và in ra số có giá trị lớn nhất trong 3 số đó.

**Đầu vào (Input):**

Ba số nguyên $a, b, c$ ($-10^9 \le a, b, c \le 10^9$).

**Đầu ra (Output):**

Một số nguyên duy nhất là số lớn nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 <br> 28 <br> 9 | 28 |

**Giải thích:**

Với dữ liệu đầu vào là `15
28
9`, kết quả thu được tương ứng là `28`.



### Bài 19 [pya_l05_p02_dau_cua_so_nguyen]: Dấu của số nguyên

Bối cảnh: Trong bài kiểm tra toán, thầy giáo yêu cầu phân loại các số nguyên thành ba nhóm: số dương, số âm và số không. Hãy viết chương trình phân loại tự động.

Nhiệm vụ: Nhập vào số nguyên $N$. Hãy in ra:
 * `DUONG` nếu $N > 0$.
 * `AM` nếu $N < 0$.
 * `KHONG` nếu $N == 0$.

**Đầu vào (Input):**

Một số nguyên $N$ ($-10^9 \le N \le 10^9$).

**Đầu ra (Output):**

Chuỗi kết quả.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| -15 | AM |

**Giải thích:**

Số -15 nhỏ hơn 0 nên in ra AM.



### Bài 20 [pya_l05_p09_thuan_di_tim_anh_da_van_toc]: Thuận đi tìm ánh đa vận tốc

Bối cảnh: Một buổi chiều đẹp trời, bạn Thuận đứng ở vị trí $x$ còn bạn Ánh đứng ở vị trí $y$ trong sân trường rộng. Thuận rất nhớ bạn nên đi bộ về phía Ánh với vận tốc $v\text{ km/h}$. Cả hai hồi hộp không biết bao giờ thì gặp được nhau. Hãy giúp hai bạn xem khi nào thì gặp nhau.

Nhiệm vụ: Hãy phân tích các tình huống:
 * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
 * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
 * Nếu $x \ne y$ và $v > 0$:
 * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
 * Nếu không chia hết: in `GAP NHAU LE GIO`.

**Đầu vào (Input):**

Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).

**Đầu ra (Output):**

Thông báo tương ứng hoặc số giờ nguyên.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | XE DAP |

**Giải thích:**

Vận tốc 15 km/h nằm trong khoảng từ 10 đến 30 km/h nên Thuận đi xe đạp.



### Bài 21 [pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai]: Cửa hàng bánh bột lọc khuyến mãi

Bối cảnh: Cuối tuần, cô chủ nhỏ mở một cửa hàng bánh bột lọc thơm ngon trước cổng trường. Cô treo bảng ưu đãi số lượng thật hấp dẫn: mua dưới 10 cái giá $5$ nghìn đồng một cái, mua từ 10 đến 49 cái giá $4$ nghìn đồng một cái, còn mua từ 50 cái trở lên giá chỉ còn $3$ nghìn đồng một cái. Các người dùng xếp hàng dài chờ mua bánh mang về liên hoan. Hãy giúp cô chủ nhỏ tính tiền cho khách.

Nhiệm vụ: Nhập vào số lượng bánh $N$ mà khách muốn mua. Tính tổng số tiền khách phải trả.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

Tổng số tiền (nghìn đồng).

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 25 | 100000 |

**Giải thích:**

Mua 25 chiếc (từ 20 chiếc trở lên) được giá 4000 đ/chiếc: 25 x 4000 = 100000 đ.



### Bài 22 [pya_l04_p11_canh_thu_tu_hinh_chu_nhat]: Cạnh thứ tư hình chữ nhật

Bối cảnh: Sau giờ thủ công, bạn Nam nhặt được 3 thanh gỗ có độ dài là $A, B, C$ ở góc lớp học. Cô giáo mỉm cười cho biết chắc chắn 3 thanh này là 3 cạnh của một hình chữ nhật, mà một hình chữ nhật luôn có 4 cạnh tạo thành 2 cặp cạnh đối bằng nhau (2 chiều dài bằng nhau và 2 chiều rộng bằng nhau). Nam muốn tìm thêm đúng một thanh gỗ nữa để ghép vừa khít thành khung hình. Hãy giúp bạn Nam tìm độ dài thanh gỗ còn thiếu.

Nhiệm vụ: Hãy tìm độ dài thanh gỗ thứ 4 còn thiếu để ghép vừa khít thành hình chữ nhật.

**Đầu vào (Input):**

Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le A, B, C \le 1000$).

**Đầu ra (Output):**

Độ dài cạnh thứ 4.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 5 <br> 3 | 5 |

**Giải thích:**

Đã có 2 cạnh bằng 3, vậy cạnh còn lại phải là 5.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 <br> 6 <br> 8 | 6 |

**Giải thích:**

Cạnh còn lại là 6.



### Bài 23 [pya_l04_p05_chia_keo_cong_bang]: Chia kẹo công bằng

Bối cảnh: Hôm liên hoan lớp, cô giáo mang đến một túi có $a$ chiếc kẹo thơm ngon để chia cho $b$ bạn học sinh. Cô muốn chia thật công bằng sao cho tất cả các bạn đều nhận được số kẹo bằng nhau và không còn thừa cái nào, để không bạn nào phải buồn. Cả lớp nín thở chờ xem túi kẹo có chia vừa khít hay không. Hãy giúp cô kiểm tra xem số kẹo có chia đều được không.

Nhiệm vụ: Kiểm tra xem số kẹo có chia đều được hay không? Nếu chia đều được thì in `YES`, ngược lại in `NO`.

**Đầu vào (Input):**

Hai số nguyên dương $a, b$ ($1 \le a, b \le 10^6$).

**Đầu ra (Output):**

`YES` hoặc `NO`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 <br> 4 | YES |

**Giải thích:**

20 chia hết cho 4, mỗi bạn 5 cái kẹo.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 20 <br> 6 | NO |

**Giải thích:**

20 không chia hết cho 6 (dư 2).



### Bài 24 [pya_l05_p10_thu_may_trong_tuan]: Thứ mấy trong tuần?

Bối cảnh: Đầu năm mới, Bin treo một tờ lịch thật đẹp trong phòng học. Mẹ đố Bin rằng ngày mùng 1 tháng Giêng năm nay là ngày **Thứ Hai**. Bin rất thích lật từng tờ lịch và đếm xem các ngày tiếp theo rơi vào thứ mấy. Hãy giúp Bin trả lời ngày thứ $K$ là thứ mấy.

Nhiệm vụ: Cho biết ngày thứ $K$ trong năm đó là thứ mấy?
 * Biết rằng: ngày 1 là Thứ Hai, ngày 2 là Thứ Ba, ..., ngày 7 là Chủ Nhật, ngày 8 lại quay về Thứ Hai.

**Đầu vào (Input):**

Một số tự nhiên $K$ ($1 \le K \le 365$).

**Đầu ra (Output):**

In ra một trong các chuỗi: `THU HAI`, `THU BA`, `THU TU`, `THU NAM`, `THU SAU`, `THU BAY`, `CHU NHAT`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 | THU 2 |

**Giải thích:**

Ngày thứ 2 trong tuần là Thứ Hai.



### Bài 25 [pya_l05_p08_phan_loai_tam_giac]: Phân loại tam giác

Bối cảnh: Trong giờ thủ công, Na cắt được một miếng bìa hình tam giác có 3 cạnh dài $a, b, c$ và cô giáo bảo đó là một tam giác hợp lệ. Cả lớp tò mò không biết miếng bìa của Na thuộc loại tam giác nào. Na muốn khoe với mẹ mà chưa gọi đúng tên hình. Hãy giúp bạn Na gọi đúng tên loại tam giác.

Nhiệm vụ: Hãy phân loại tam giác đó:
 * Nếu 3 cạnh bằng nhau ($a == b == c$): in `TAM GIAC DEU`.
 * Nếu có 2 cạnh bằng nhau ($a == b$ hoặc $b == c$ hoặc $c == a$): in `TAM GIAC CAN`.
 * Các trường hợp còn lại: in `TAM GIAC THUONG`.

**Đầu vào (Input):**

Ba số tự nhiên $a, b, c$ trên 3 dòng ($1 \le a, b, c \le 1000$).

**Đầu ra (Output):**

Tên phân loại tam giác.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 3 3 | DEU |

**Giải thích:**

Ba cạnh có độ dài bằng nhau nên tam giác là tam giác đều.



### Bài 26 [pya_l05_p07_tinh_cuoc_taxi_bac_thang]: Tính cước taxi bậc thang

Bối cảnh: Hôm nay cả lớp đi dã ngoại bằng chiếc taxi "Rùa Con" rất dễ thương. Bác tài xế dán bảng giá lên cửa xe: giá mở cửa cho $1\text{ km}$ đầu tiên là $10$ nghìn đồng, từ kilomet thứ 2 đến kilomet thứ 10 giá $8$ nghìn đồng mỗi km, còn từ kilomet thứ 11 trở đi giá $6$ nghìn đồng mỗi km. Mi ngồi ghế đầu, tay cầm đồng hồ đo quãng đường và muốn tính tiền giúp cả lớp. Hãy tính tổng tiền cước.

Nhiệm vụ: Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Tổng tiền cước taxi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 | 10 |

**Giải thích:**

Đúng 1 km đầu: 10 nghìn.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 42 |

**Giải thích:**

1 km đầu: 10k + 4 km tiếp theo: $4 \times 8 = 32$k $\implies 10 + 32 = 42$k.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 | 94 |

**Giải thích:**

1 km đầu (10k) + 9 km tiếp theo ($9 \times 8 = 72$k) + 2 km cuối ($2 \times 6 = 12$k) $\implies 10 + 72 + 12 = 94$k.



### Bài 27 [pya_l05_p04_xep_loai_hoc_luc]: Xếp loại học lực

Bối cảnh: Cuối học kỳ, cô giáo cần xếp loại học lực cho từng học sinh dựa vào điểm trung bình. Hãy giúp cô giáo viết chương trình xếp loại tự động.

Nhiệm vụ: Nhập vào điểm trung bình môn Tin học của một người dùng (số thực $0.0 \le diem \le 10.0$).
 * Điểm $\ge 9.0$: in `XUAT SAC`.
 * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
 * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
 * Điểm $< 6.5$: in `CAN CO GANG`.

**Đầu vào (Input):**

Một số thực $diem$.

**Đầu ra (Output):**

Xếp loại tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8.5 | GIOI |

**Giải thích:**

Điểm 8.5 thuộc thang điểm giỏi (từ 8.0 trở lên).



### Bài 28 [pya_l06_p07_so_ngay_trong_thang]: Số ngày trong tháng

Bối cảnh: Bạn Lan muốn biết tháng sinh nhật của mình có bao nhiêu ngày. Mỗi tháng trong năm có số ngày khác nhau, đặc biệt tháng 2 còn phụ thuộc vào năm nhuận. Hãy giúp Lan.

Nhiệm vụ: Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
 * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
 * Tháng 4, 6, 9, 11 có đúng 30 ngày.
 * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.

**Đầu vào (Input):**

Hai dòng lần lượt là $M$ và $Y$.

**Đầu ra (Output):**

Một số nguyên duy nhất là số ngày của tháng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 2024 | 29 |

**Giải thích:**

Với dữ liệu đầu vào là `2
2024`, kết quả thu được tương ứng là `29`.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 2023 | 28 |

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 2025 | 30 |



### Bài 29 [pya_l06_p11_cap_doi_cung_dau_hay_trai_dau]: Cặp đôi cùng dấu hay trái dấu

Bối cảnh: Hai số nguyên được gọi là "cùng dấu" nếu cả hai đều dương hoặc cả hai đều âm. Ngược lại chúng "trái dấu". Hãy kiểm tra cặp số.

Nhiệm vụ: Nhập vào hai số nguyên $a$ và $b$ (có thể âm, dương hoặc bằng 0).
 * In `CO SO KHONG` nếu có ít nhất một số bằng 0 ($a == 0$ hoặc $b == 0$).
 * In `CUNG DAU` nếu cả hai số cùng mang dấu dương hoặc cùng mang dấu âm ($a \times b > 0$).
 * In `TRAI DAU` nếu một số dương và một số âm ($a \times b < 0$).

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Thông báo theo quy định.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 10 | CUNG DAU |

**Giải thích:**

Cả hai số 5 và 10 đều là số dương nên cùng dấu.



### Bài 30 [pya_l04_p08_cap_so_bang_nhau_hay_khac]: Cặp số bằng nhau hay khác?

Bối cảnh: Trong trò chơi ghép đôi, hai lá bài được lật lên. Nếu hai lá bài có cùng giá trị thì người chơi được cộng điểm. Hãy kiểm tra xem hai số có bằng nhau không.

Nhiệm vụ: Nhập vào 2 số nguyên $a$ và $b$. Hãy so sánh và in ra màn hình một trong ba thông báo:
 * `a LON HON b` (nếu $a > b$)
 * `a NHO HON b` (nếu $a < b$)
 * `HAI SO BANG NHAU` (nếu $a == b$)

**Đầu vào (Input):**

Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).

**Đầu ra (Output):**

Một dòng thông báo theo đúng mẫu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 28 | a NHO HON b |

**Giải thích:**

Số 15 nhỏ hơn số 28 nên in ra a NHO HON b.



### Bài 31 [pya_l04_p12_tro_choi_oan_tu_ti]: Trò chơi oẳn tù tì

Bối cảnh: Giờ ra chơi, hai bạn Tí và Tèo rủ nhau chơi trò Oẳn Tù Tì thật sôi nổi. Hai bạn quy ước các lựa chọn bằng số: `1` là Búa (Đấm), `2` là Kéo, `3` là Bao (Lá). Luật chơi là: Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1), còn nếu ra cùng số thì hòa nhau. Cả hai cùng hô to và ra tay mà chưa biết ai thắng. Hãy giúp hai bạn xem ai là người thắng cuộc.

Nhiệm vụ: Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.

**Đầu vào (Input):**

Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).

**Đầu ra (Output):**

`TI THANG`, `TEO THANG` hoặc `HOA`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 2 | TI THANG |

**Giải thích:**

Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 3 | TEO THANG |

**Giải thích:**

Tí ra Búa (1), Tèo ra Bao (3) $\to$ Tèo thắng.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 2 | HOA |

**Giải thích:**

Cả hai cùng ra Kéo.



### Bài 32 [pya_l05_p01_den_giao_thong_nga_tu]: Đèn giao thông ngã tư

Bối cảnh: Tại ngã tư gần trường, đèn giao thông điều khiển lưu lượng xe. Mỗi màu đèn có ý nghĩa khác nhau: đỏ thì dừng, vàng thì chuẩn bị, xanh thì đi. Hãy lập trình mô phỏng hệ thống đèn giao thông.

Nhiệm vụ: Nhập vào một chữ cái in hoa đại diện cho màu đèn: `D` (Đỏ), `V` (Vàng), `X` (Xanh).
 * Nếu là `D`: in ra `DUNG LAI`.
 * Nếu là `V`: in ra `DI CHAM`.
 * Nếu là `X`: in ra `DUOC DI`.

**Đầu vào (Input):**

Một ký tự `D`, `V` hoặc `X`.

**Đầu ra (Output):**

Thông báo tương ứng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| do | DUNG LAI |

**Giải thích:**

Màu đèn là "do" nên in ra thông báo DUNG LAI.



### Bài 33 [pya_l06_p12_giao_nhau_cua_hai_doan_thang]: Giao nhau của hai đoạn thẳng

Bối cảnh: Trong giờ chơi xếp hình, hai bạn An và Bình mỗi bạn có một đoạn dây thun màu căng trên cây thước dài. Trên trục số thực, đoạn dây thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$), đoạn dây thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$). Hai bạn thắc mắc không biết hai đoạn dây có chồng lên nhau ở chỗ nào không. Hãy giúp hai bạn kiểm tra xem hai đoạn dây có điểm chung không.

Nhiệm vụ: Hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
 * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
 * Nếu không giao nhau: in `KHONG GIAO NHAU`.

**Đầu vào (Input):**

Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).

**Đầu ra (Output):**

`GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 6 <br> 4 <br> 9 | GIAO NHAU 2 |

**Giải thích:**

Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 3 <br> 5 <br> 8 | KHONG GIAO NHAU |

**Giải thích:**

Hai đoạn rời nhau hoàn toàn.



### Bài 34 [pya_l05_p05_ve_gui_xe_ben_bai]: Vé gửi xe bến bãi

Bối cảnh: Sáng chủ nhật, cả nhà Bo đến khu vui chơi gửi xe ở bãi giữ xe thông minh. Bác bảo vệ vui tính chỉ bảng giá vé theo loại phương tiện: loại `1` (Xe đạp) giá $2$ nghìn đồng, loại `2` (Xe máy) giá $5$ nghìn đồng, loại `3` (Xe ô tô) giá $30$ nghìn đồng, còn các loại khác thì máy báo `LOI PHUONG TIEN`. Bo xung phong đọc mã loại xe giúp bác. Hãy tính đúng giá vé.

Nhiệm vụ: Nhập vào mã loại xe và in ra giá vé tương ứng; nếu mã không thuộc `1`, `2`, `3` thì in `LOI PHUONG TIEN`.

**Đầu vào (Input):**

Một số nguyên mã loại xe.

**Đầu ra (Output):**

Số tiền gửi xe hoặc chữ `LOI PHUONG TIEN`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| xe may | 5000 |

**Giải thích:**

Phương tiện gửi là xe máy có mức phí 5000 đồng.



### Bài 35 [pya_l05_p12_bon_mua_trong_nam]: Bốn mùa trong năm

Bối cảnh: Trong giờ khoa học, cô giáo treo bức tranh bốn mùa thật đẹp lên bảng. Cô giảng rằng một năm có 12 tháng được chia thành 4 mùa: **Mùa Xuân** gồm tháng 1, 2, 3; **Mùa Hạ (Hè)** gồm tháng 4, 5, 6; **Mùa Thu** gồm tháng 7, 8, 9; còn **Mùa Đông** gồm tháng 10, 11, 12. Su thích nhất mùa hè vì được đi biển cùng gia đình. Hãy xác định một tháng bất kỳ thuộc mùa nào.

Nhiệm vụ: Nhập vào một số nguyên $M$.
 * Nếu $1 \le M \le 12$, hãy in ra tên mùa tương ứng (`XUAN`, `HA`, `THU`, `DONG`).
 * Nếu $M$ không nằm từ 1 đến 12, in ra `THANG KHONG HOP LE`.

**Đầu vào (Input):**

Một số nguyên $M$ ($-100 \le M \le 100$).

**Đầu ra (Output):**

Tên mùa hoặc thông báo lỗi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | HA |

**Giải thích:**

Tháng 4 thuộc mùa hạ (mùa hè).



### Bài 36 [pya_l06_p08_tam_giac_vuong_hay_khong]: Tam giác vuông hay không?

Bối cảnh: Trong giờ toán hình, cô giáo kể về định lý Pytago nổi tiếng: tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$). Bạn Tôm rất thích xếp que tính thành hình tam giác và đoán xem hình nào có góc vuông. Tôm loay hoay mãi chưa chắc chắn. Hãy giúp Tôm kiểm tra xem ba que tính có tạo thành tam giác vuông không.

Nhiệm vụ: Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.

**Đầu vào (Input):**

Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).

**Đầu ra (Output):**

`VUONG` hoặc `KHONG VUONG`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 4 <br> 5 | VUONG |

**Giải thích:**

$3^2 + 4^2 = 9 + 16 = 25 = 5^2$.



### Bài 37 [pya_l06_p10_ngay_ke_tiep_trong_nam]: Ngày kế tiếp trong năm

Bối cảnh: Bạn Bông có một cuốn lịch để bàn rất xinh và ngày nào cũng tự tay xé một tờ. Hôm nay tờ lịch ghi một ngày hợp lệ gồm 3 số: ngày $D$, tháng $M$, năm $Y$. Bông tò mò muốn biết lật sang tờ tiếp theo sẽ là ngày tháng năm nào. Mẹ dặn rằng phải nhớ cả tháng dài tháng ngắn và năm nhuận nữa. Hãy giúp Bông tìm ra ngày kế tiếp ngay sau đó.

Nhiệm vụ: Hãy tính và in ra ngày, tháng, năm của **ngày kế tiếp ngay sau đó**.

**Đầu vào (Input):**

Ba số tự nhiên $D, M, Y$ trên 3 dòng.

**Đầu ra (Output):**

Ba số nguyên cách nhau một dấu cách `D_tiep M_tiep Y_tiep`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 31 <br> 12 <br> 2024 | 1 1 2025 |

**Giải thích:**

Ngày cuối năm chuyển sang ngày đầu năm mới!

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 28 <br> 2 <br> 2024 | 29 2 2024 |

**Giải thích:**

Năm 2024 là năm nhuận nên tháng 2 có ngày 29.

**Ví dụ mẫu (Sample 3):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 28 <br> 2 <br> 2023 | 1 3 2023 |

**Giải thích:**

Năm 2023 thường nên sau 28/2 là sang 1/3.



# Bài 05: Vòng lặp for và hàm range

## 1. Bản chất của vòng lặp trong khoa học máy tính

Trong lập trình, có những công việc phải làm đi làm lại hàng trăm, hàng nghìn lần (ví dụ: tính tổng các số từ 1 đến 1000, in danh sách tên, kiểm tra từng phần tử).

Nếu không có vòng lặp, các em phải gõ tay hàng nghìn dòng lệnh giống hệt nhau — không thể làm được! **Vòng lặp** giúp các em chỉ viết khối lệnh một lần rồi nhờ máy tính tự lặp lại.

Khi đã **biết trước chính xác số lần lặp**, công cụ chuẩn nhất trong Python là **vòng lặp `for` kết hợp với hàm `range()`**.

---

## 2. Chiếc thước đo `range()` toàn tập

Hàm `range()` rất đặc biệt: nó không tạo sẵn cả dãy số trong bộ nhớ, mà giống như một **máy nhả số tự động** — mỗi lần lặp cần một số mới, `range()` mới tính và đưa ra.



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l05_range_ruler.png)



### 2.1. Ba dạng sử dụng của hàm `range()`

| Dạng Cú Pháp | Số Tham Số | Ý Nghĩa Kỹ Thuật | Dãy Số Sinh Ra | Số Lần Lặp |
|---|:---:|---|---|:---:|
| `range(stop)` | 1 tham số | Bắt đầu từ số `0`, bước nhảy mặc định là `+1`, **dừng trước `stop`**. | `0, 1, 2, ..., stop - 1` | Đúng `stop` lần |
| `range(start, stop)` | 2 tham số | Bắt đầu từ `start`, bước nhảy mặc định `+1`, **dừng trước `stop`**. | `start, start + 1, ..., stop - 1` | `stop - start` lần |
| `range(start, stop, step)` | 3 tham số | Bắt đầu từ `start`, mỗi bước tăng/giảm `step`, **dừng trước `stop`**. | Các số cách đều nhau một khoảng `step` | Tính theo công thức |

> **ĐIỀU BẮT BUỘC PHẢI NHỚ: CẬN TRÊN `stop` LUÔN BỊ LOẠI TRỪ!**
> * Trong toán học, đoạn số thường lấy cả hai đầu mút $[1, 10]$.
> * Nhưng trong hàm `range(1, 10)`, số `10` **KHÔNG BAO GIỜ ĐƯỢC CHẠM TỚI**! Dãy số chỉ chạy đến số `9` là dừng lại.
> * Nếu muốn lặp qua các số từ $1$ đến $N$ đầy đủ, cận trên trong `range` bắt buộc phải là:
>  $$\mathbf{range(1, N + 1)}$$

### 2.2. Kỹ thuật duyệt số bước nhảy âm (Chạy lùi)

Khi `step` là số âm, `range()` sẽ đếm lùi từ số lớn về số bé. Số bắt đầu `start` phải lớn hơn số dừng `stop`:
```python
# Đếm ngược từ 5 về 1 để phóng tên lửa:
for i in range(5, 0, -1):
    print(i, end=" ")
print("PHONG!")
```
**Màn hình in ra:**
```text
5 4 3 2 1 PHONG!
```

---

## 3. Cú pháp vòng lặp `for` và Biến lặp

* **Cú pháp chuẩn mực:**
 ```python
  for bien_lap in range(start, stop, step):
      # Khoi lenh duoc lap lai (Thut le 4 dau cach)
  ```
* **Cơ chế hoạt động:**
 1. Ở vòng đầu tiên, `bien_lap` nhận giá trị đầu tiên do `range` sinh ra (`start`).
 2. Toàn bộ khối lệnh bên trong được thực thi.
 3. Chạy xong lệnh cuối, máy quay lên đầu và gán giá trị tiếp theo cho `bien_lap`.
 4. Lặp liên tục cho đến khi chạm giới hạn `stop` thì dừng.

---

## 4. Các mẫu thuật toán tích lũy kinh điển

Khi làm bài tập, vòng lặp `for` gần như luôn đi cùng kỹ thuật **tích lũy giá trị**.

### 4.1. Mẫu 1: Thuật toán Tính Tổng tích lũy
Bài toán: Tính tổng $S = 1 + 2 + 3 + \dots + N$.

```python
n = int(input())
# Bước 1: Khởi tạo biến tích lũy tổng ban đầu bằng 0
tong = 0

# Bước 2: Duyệt qua từng số i từ 1 đến N
for i in range(1, n + 1):
    tong += i  # Cộng dồn i vào biến tong

# Bước 3: In kết quả sau khi vòng lặp đã kết thúc hoàn toàn
print(tong)
```

### 4.2. Mẫu 2: Thuật toán Tính Tích giai thừa
Bài toán: Tính tích $P = 1 \times 2 \times 3 \times \dots \times N$ ($N!$).

```python
n = int(input())
# BẮT BUỘC: Khởi tạo biến tích bằng 1 (Nếu để bằng 0 thì mọi tích đều ra 0!)
tich = 1

for i in range(1, n + 1):
    tich *= i

print(tich)
```

### 4.3. Mẫu 3: Thuật toán Đếm số phần tử thỏa mãn điều kiện
Bài toán: Đếm xem trong đoạn từ $1$ đến $N$ có bao nhiêu số chia hết cho 3.

```python
n = int(input())
dem = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        dem += 1  # Mỗi lần phát hiện số thỏa mãn, tăng đếm lên 1

print(dem)
```

---

## 5. Bảng mô phỏng từng bước

Xét chương trình tính tổng với $N = 4$:
```python
tong = 0
for i in range(1, 5):
    tong = tong + i
print(tong)
```

### Bảng theo dõi biến thiên ô nhớ RAM qua từng vòng lặp:

| Vòng Lặp | Giá Trị Biến `i` | Biểu Thức Tính Toán | Giá Trị Cũ Của `tong` | Giá Trị Mới Của `tong` |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | *(Chưa có)* | `tong = 0` | *(Khởi đầu)* | **0** |
| **Vòng 1** | **`1`** | `tong = 0 + 1` | 0 | **1** |
| **Vòng 2** | **`2`** | `tong = 1 + 2` | 1 | **3** |
| **Vòng 3** | **`3`** | `tong = 3 + 3` | 3 | **6** |
| **Vòng 4** | **`4`** | `tong = 6 + 4` | 6 | **10** |
| **Dừng lặp** | *(Chạm cận 5)* | Thoát khỏi vòng `for` | 10 | **10** |

$$\implies \text{Kết quả in ra màn hình sau vòng lặp: } \mathbf{10}$$

---

## 6. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: ĐẶT LỆNH IN KẾT QUẢ VÀO BÊN TRONG THÂN VÒNG LẶP**
> * Xem đoạn code sai:
>  ```python
>   tong = 0
>   for i in range(1, n + 1):
>       tong += i
>       print(tong)  # Bị thụt lề vào trong vòng lặp!
>   ```
> * **Hậu quả:** Thay vì in ra 1 dòng kết quả duy nhất ở cuối, chương trình sẽ in ra $N$ dòng kết quả trung gian sau mỗi vòng lặp $\implies$ Bị chương trình kiểm tra chấm lỗi **kết quả sai** ngay lập tức!
> * **Quy tắc:** Lệnh in kết quả cuối cùng phải được **lùi ra ngoài ngang hàng với từ khóa `for`**.

> **BẪY LỖI 2: KHỞI TẠO BIẾN TÍCH BẰNG 0**
> * Khi tính tích hoặc giai thừa, nếu khởi tạo `tich = 0` thì $0 \times \text{bất kỳ số nào}$ cũng luôn bằng $0$. Kết quả cuối cùng sẽ luôn là $0$.
> * Luôn khởi tạo: `tong = 0` và `tich = 1`.

> **BẪY LỖI 3: QUÊN CỘNG 1 Ở CẬN TRÊN `range(1, n)`**
> * Viết `range(1, n)` sẽ chỉ chạy từ $1$ đến $n - 1$, dẫn đến thiếu mất số $n$ cuối cùng trong phép tính.

---

## 7. Mẫu code thường gặp

```python
# Mẫu tính tổng các số chẵn trong đoạn [A, B]
a, b = map(int, input().split())
tong_chan = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tong_chan += i

print(tong_chan)
```


## Bài tập thực hành


### Bài 01 [pya_l07_p14_tong_day_sieu_lon_khong_lap]: Tổng dãy siêu lớn không lặp

Bối cảnh: Trong hội thi lập trình của trường, ban giám khảo đố cả lớp một số $N$ cực lớn lên tới $10^9$ ($1$ tỷ) bạn nào cũng tròn mắt ngạc nhiên. Cô giáo dặn rằng nếu em dùng vòng lặp `for i in range(1, N + 1):` thì chương trình sẽ bị chạy quá thời gian quy định (Time Limit Exceeded - TLE) vì máy tính phải lặp 1 tỷ lần mất hơn 10 giây! Cả lớp đang loay hoay chưa biết làm sao cho nhanh. Hãy giúp cả lớp tìm cách tính thật nhanh.

Nhiệm vụ: Hãy tính tổng $S = 1 + 2 + \dots + N$ với thời gian chạy tức thì ($< 0.001$ giây) bằng công thức toán học.

**Đầu vào (Input):**

Một số nguyên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Giá trị tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1000000000 | 500000000500000000 |

**Giải thích:**

Với dữ liệu đầu vào là `1000000000`, kết quả thu được tương ứng là `500000000500000000`.



### Bài 02 [pya_l07_p01_dem_sao_len_troi]: Đếm sao lên trời

Bối cảnh: Đêm hè, người dùng ngước nhìn bầu trời đầy sao và bắt đầu đếm: 1, 2, 3... Hãy giúp in dãy số đếm sao từ 1 đến $N$.

Nhiệm vụ: Nhập vào một số tự nhiên $N$. Hãy in các số từ $1$ đến $N$ trên cùng một dòng, mỗi số cách nhau một khoảng trắng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Dãy số từ 1 đến $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 1 2 3 4 5 |

**Giải thích:**

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `1 2 3 4 5`.



### Bài 03 [pya_l07_p02_dem_nguoc_phong_ten_lua]: Đếm ngược phóng tên lửa

Bối cảnh: Trạm phóng tên lửa bắt đầu đếm ngược: 10, 9, 8... 1, PHONG! Hãy lập trình mô phỏng đếm ngược phóng tên lửa.

Nhiệm vụ: Trước khi phóng tàu vũ trụ, đồng hồ đếm ngược từ $N$ về 1, cuối cùng in ra chữ `PHONG!`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 20$).

**Đầu ra (Output):**

Mỗi số trên một dòng, dòng cuối in `PHONG!`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 3 <br> 2 <br> 1 <br> PHONG! |

**Giải thích:**

Với dữ liệu đầu vào là `3`, kết quả thu được tương ứng là `3
2
1
PHONG!`.



### Bài 04 [pya_l07_p03_tong_cac_so_tu_nhien]: Tổng các số tự nhiên

Bối cảnh: Nhà toán học Gauss khi còn đã tìm ra cách tính nhanh tổng các số từ 1 đến 100. Hãy viết chương trình tính tổng $1 + 2 + \dots + N$.

Nhiệm vụ: Nhập số nguyên dương $N$. Hãy tính tổng $S = 1 + 2 + 3 + \dots + N$.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | 10 |

**Giải thích:**

$1 + 2 + 3 + 4 = 10$.



### Bài 05 [pya_l07_p13_tam_giac_vuong_dau_sao]: Tam giác vuông dấu sao

Bối cảnh: Thí sinh muốn vẽ một tam giác vuông bằng dấu sao, mỗi hàng tăng thêm một ngôi sao. Hãy giúp bạn ấy.

Nhiệm vụ: Nhập vào chiều cao $N$ của tam giác vuông. Hãy in ra tam giác vuông cân gồm các dấu sao theo mẫu:
 * Dòng 1 có 1 dấu `*`
 * Dòng 2 có 2 dấu `*`
 * ...
 * Dòng $N$ có $N$ dấu `*`.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 50$).

**Đầu ra (Output):**

Tam giác vuông dấu `*`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 | * <br> ** <br> *** <br> **** |

**Giải thích:**

Với dữ liệu đầu vào là `4`, kết quả thu được tương ứng là `*
**
***
****`.



### Bài 06 [pya_l07_p12_hang_cot_dau_sao]: Hàng cột dấu sao

Bối cảnh: Trong giờ tin học, thầy giáo yêu cầu vẽ một hình chữ nhật bằng dấu sao `*`. Hãy viết chương trình vẽ hình.

Nhiệm vụ: Nhập vào số hàng $R$ và số cột $C$. Hãy in ra một hình chữ nhật đặc gồm các dấu sao `*` có kích thước $R$ hàng và $C$ cột.

**Đầu vào (Input):**

Hai số tự nhiên $R$ và $C$ ($1 \le R, C \le 50$).

**Đầu ra (Output):**

Hình chữ nhật dấu `*`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 5 | ***** <br> ***** <br> ***** |

**Giải thích:**

Với dữ liệu đầu vào là `3
5`, kết quả thu được tương ứng là `*****
*****
*****`.



### Bài 07 [pya_l07_p07_tinh_giai_thua_n]: Tính giai thừa $N!$

Bối cảnh: Cuối tuần, bạn Tý mở một gian hàng kẹo nhỏ trước cổng trường. Tý xếp kẹo thành từng hàng vui nhộn: hàng có số tự nhiên $N$ thì Tý nhân tất cả các số tự nhiên từ 1 đến $N$ với nhau. Cách nhân dồn này được gọi là giai thừa, ký hiệu là $N!$, và được tính bằng công thức:
 $$N! = 1 \times 2 \times 3 \times \dots \times N$$
Hôm nay khách đông quá, Tý tính không kịp. Hãy giúp Tý tính nhanh giá trị $N!$.

Nhiệm vụ: Nhập số tự nhiên $N$ ($1 \le N \le 20$). Hãy tính và in ra giá trị $N!$.

**Đầu vào (Input):**

Một số tự nhiên $N$.

**Đầu ra (Output):**

Giá trị $N!$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 120 |

**Giải thích:**

$1 \times 2 \times 3 \times 4 \times 5 = 120$.



### Bài 08 [pya_l07_p10_tong_binh_phuong]: Tổng bình phương

Bối cảnh: Nhà toán học muốn tính tổng bình phương của các số từ 1 đến $N$: $1^2 + 2^2 + 3^2 + \dots + N^2$. Hãy viết chương trình tính.

Nhiệm vụ: Nhập vào số nguyên dương $N$. Hãy tính tổng:
 $$S = 1^2 + 2^2 + 3^2 + \dots + N^2$$

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 1000$).

**Đầu ra (Output):**

Một số nguyên duy nhất là tổng $S$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 | 14 |

**Giải thích:**

$1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$.



### Bài 09 [pya_l07_p04_bang_cuu_chuong]: Bảng cửu chương

Bối cảnh: Trong giờ Toán, cô giáo yêu cầu học sinh in bảng cửu chương của một số $K$ bất kỳ. Hãy viết chương trình in bảng nhân tự động.

Nhiệm vụ: Nhập vào một số nguyên $K$ ($1 \le K \le 9$). Hãy in ra bảng cửu chương nhân của số $K$ từ 1 đến 10 theo đúng mẫu.

**Đầu vào (Input):**

Một số nguyên $K$.

**Đầu ra (Output):**

Gồm 10 dòng, mỗi dòng có định dạng: `K x i = [ket_qua]`.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 5 x 1 = 5 <br> 5 x 2 = 10 <br> 5 x 3 = 15 <br> 5 x 4 = 20 <br> 5 x 5 = 25 <br> 5 x 6 = 30 <br> 5 x 7 = 35 <br> 5 x 8 = 40 <br> 5 x 9 = 45 <br> 5 x 10 = 50 |

**Giải thích:**

Với dữ liệu đầu vào là `5`, kết quả thu được tương ứng là `5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50`.



### Bài 10 [pya_l07_p05_tong_so_chan_trong_doan]: Tổng số chẵn trong đoạn

Bối cảnh: Thí sinh muốn tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$. Hãy giúp bạn ấy viết chương trình tính nhanh.

Nhiệm vụ: Cho hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy tính tổng tất cả các số chẵn nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$ nếu chúng là số chẵn).

**Đầu vào (Input):**

Hai số tự nhiên $A$ và $B$ trên 2 dòng ($1 \le A \le B \le 10^4$).

**Đầu ra (Output):**

Tổng các số chẵn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 3 <br> 8 | 18 |

**Giải thích:**

Các số chẵn là: 4, 6, 8. Tổng: $4 + 6 + 8 = 18$.



### Bài 11 [pya_l07_p11_doc_sach_moi_ngay]: Đọc sách mỗi ngày

Bối cảnh: Nghỉ hè, bạn Hoa mượn ở thư viện một cuốn truyện thật dày có tổng cộng $N$ trang để rèn thói quen đọc sách mỗi ngày. Ngày thứ nhất Hoa đọc được 1 trang thật ngon lành.
 * Ngày thứ hai Hoa đọc được 2 trang.
 * Ngày thứ ba Hoa đọc được 3 trang.
 * Cứ như vậy, ngày thứ $k$ Hoa đọc được $k$ trang.
Hoa háo hức muốn biết mình đọc hết truyện sau mấy ngày. Hãy đếm số ngày.

Nhiệm vụ: Hỏi sau đúng bao nhiêu ngày thì Hoa sẽ đọc hết (hoặc vượt quá) $N$ trang của cuốn sách?

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

Số ngày ít nhất để Hoa đọc xong cuốn sách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 4 |

**Giải thích:**

Ngày 1: 1 trang; ngày 2: 2 trang (tổng 3); ngày 3: 3 trang (tổng 6); ngày 4: 4 trang (tổng 10 $\ge 10$). Sau 4 ngày đọc xong.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 11 | 5 |

**Giải thích:**

Sau 4 ngày mới đọc 10 trang, phải sang ngày thứ 5 mới đọc hết.



### Bài 12 [pya_l07_p08_day_so_cach_deu]: Dãy số cách đều

Bối cảnh: Lớp bạn Na chơi trò nhảy ô số rất vui trên sân trường. Cả lớp thống nhất chọn số bắt đầu là số $a$, rồi mỗi bước nhảy phải dài đúng $d$ đơn vị, nghĩa là số tiếp theo hơn số đứng trước nó đúng $d$ đơn vị. Các bạn xếp thành một hàng dài và đọc to từng số mình nhảy tới. Na đếm mãi mà quên mất, hãy Na viết tiếp dãy số này.

Nhiệm vụ: Nhập vào số bắt đầu $a$, khoảng cách $d$ và số lượng phần tử cần in $n$. Hãy in ra $n$ số đầu tiên của dãy trên một dòng, cách nhau dấu cách.

**Đầu vào (Input):**

Ba số tự nhiên $a, d, n$ ($1 \le a, d, n \le 100$).

**Đầu ra (Output):**

Dãy số gồm $n$ phần tử.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2 <br> 3 <br> 5 | 2 5 8 11 14 |

**Giải thích:**

Với dữ liệu đầu vào là `2
3
5`, kết quả thu được tương ứng là `2 5 8 11 14`.



### Bài 13 [pya_l07_p06_dem_boi_so_cua_k]: Đếm bội số của K

Bối cảnh: Cô giáo hỏi: "Trong đoạn từ $A$ đến $B$, có bao nhiêu số chia hết cho $K$?". Hãy viết chương trình đếm nhanh.

Nhiệm vụ: Nhập vào 3 số tự nhiên $A, B, K$ ($A \le B$). Hãy đếm xem có bao nhiêu số trong đoạn $[A, B]$ chia hết cho $K$.

**Đầu vào (Input):**

Ba số $A, B, K$ trên 3 dòng ($1 \le A \le B \le 10^5, 1 \le K \le 100$).

**Đầu ra (Output):**

Số lượng số chia hết cho $K$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 1 <br> 10 <br> 3 | 3 |

**Giải thích:**

Gồm các số: 3, 6, 9. Tổng cộng 3 số.



### Bài 14 [pya_l07_p09_tim_uoc_so_cua_n]: Tìm ước số của N

Bối cảnh: Thí sinh đang học về ước số trong giờ Toán. Hãy viết chương trình liệt kê tất cả các ước số của một số $N$ cho trước.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy in ra tất cả các ước số dương của $N$ theo thứ tự tăng dần trên một dòng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^4$).

**Đầu ra (Output):**

Các ước số của $N$ cách nhau một dấu cách.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 12 | 1 2 3 4 6 12 |

**Giải thích:**

Với dữ liệu đầu vào là `12`, kết quả thu được tương ứng là `1 2 3 4 6 12`.



# Bài 06: Vòng lặp while và biến cờ

## 1. Bản chất của vòng lặp `while` trong khoa học máy tính

Vòng lặp `for` rất hợp khi các em **đã biết trước chính xác số lần lặp**. Nhưng thực tế có nhiều việc **chưa biết trước số lần lặp**:
* Chơi một trò chơi đến khi nào thua thì dừng lại.
* Nhập các số liên tiếp đến khi nào gặp số 0 thì kết thúc.
* Rút tiền cho đến khi số dư không còn đủ.
* Chia một số cho 10 liên tục cho đến khi số đó chỉ còn bằng 0.

Ở các việc trên, khi nào dừng không do một con số cố định quyết định, mà do **một điều kiện** quyết định. Công cụ chuẩn cho trường hợp này là **vòng lặp `while` (lặp khi điều kiện còn đúng)**.



![](/Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/assets_png/l06_while_loop.png)



---

## 2. Cấu trúc 3 thành phần bắt buộc của vòng lặp `while`

Mọi vòng lặp `while` chuẩn đều gồm **3 bộ phận**:

```python
# THÀNH PHẦN 1: Khởi tạo biến điều khiển trước vòng lặp
i = 1

# THÀNH PHẦN 2: Điều kiện duy trì vòng lặp (Kiểm tra ở đầu mỗi vòng)
while i <= 5:
    print(i)
    # THÀNH PHẦN 3: Cập nhật biến điều khiển bên trong thân vòng lặp
    i += 1
```

* **Cơ chế hoạt động:**
 1. Trước khi vào vòng lặp, máy kiểm tra điều kiện sau từ khóa `while`.
 2. Nếu điều kiện là `True`, toàn bộ thân lệnh bên trong được chạy.
 3. Chạy xong, máy **quay lại đầu câu lệnh `while`** để kiểm tra lại điều kiện.
 4. Điều kiện còn `True` thì lặp tiếp. Điều kiện thành `False` thì dừng và chạy lệnh tiếp theo bên dưới.

---

## 3. Thảm họa Vòng lặp vô tận

> **LỖI NGUY HIỂM NHẤT CỦA VÒNG LẶP WHILE:**
> Hãy quan sát đoạn mã sai lầm sau:
> ```python
> i = 1
> while i <= 5:
>     print(i)
>     # QUÊN LỆNH: i += 1 !
> ```
> * **Hiện tượng:** Biến `i` mãi giữ giá trị bằng `1`. Điều kiện `1 <= 5` luôn là `True`!
> * **Hậu quả:** Chương trình in số `1` liên tục không bao giờ dừng, máy tính bị treo.
> * **Quy tắc an toàn:** Mỗi khi viết lệnh `while`, điều đầu tiên cần tự hỏi là: *"Câu lệnh nào bên trong vòng lặp sẽ làm cho điều kiện này trở thành False để thoát ra?"*

---

## 4. Hai lệnh điều khiển luồng lặp mạnh mẽ: `break` và `continue`

Khi vòng lặp đang chạy, các em có thể can thiệp bằng hai từ khóa đặc biệt:

### 4.1. Lệnh `break` (Bẻ gãy và Thoát vòng lặp ngay lập tức)
Gặp lệnh `break`, Python **hủy ngay vòng lặp hiện tại** và nhảy ra ngoài, dù điều kiện của `while` vẫn đang là `True`.

```python
# Tìm số đầu tiên chia hết cho 7 lớn hơn 50:
n = 51
while True:  # Vòng lặp vô tận có chủ đích
    if n % 7 == 0:
        print("So tim thay la:", n)
        break  # Đã tìm thấy, thoát vòng lặp ngay lập tức!
    n += 1
```
*Kết quả in ra:* `So tim thay la: 56`

### 4.2. Lệnh `continue` (Bỏ qua lượt lặp hiện tại)
Gặp lệnh `continue`, Python **bỏ qua mọi câu lệnh còn lại bên dưới** của vòng hiện tại và nhảy ngay lên đầu để bắt đầu lượt tiếp theo.

```python
# In các số từ 1 đến 5, trừ số 3:
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Bỏ qua số 3, không in
    print(i, end=" ")
```
*Kết quả in ra:* `1 2 4 5 `

---

## 5. Kỹ thuật Biến cờ và Lính canh

### 5.1. Kỹ thuật Biến cờ
Biến cờ là biến kiểu `bool` (thường đặt tên là `found`, `co_hieu`, `da_tim_thay`), dùng để ghi nhận xem **một việc đặc biệt đã xảy ra hay chưa**.

```python
# Kiểm tra xem số N có phải là số nguyên tố hay không bằng biến cờ:
n = int(input())
la_nguyen_to = True  # Cắm cờ ban đầu: Giả định n là số nguyên tố

if n < 2:
    la_nguyen_to = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_nguyen_to = False  # Hạ cờ: Đã tìm thấy ước số
            break
        i += 1

if la_nguyen_to:
    print("YES")
else:
    print("NO")
```

### 5.2. Kỹ thuật Lính canh dừng nhập
Bài toán: Đọc liên tiếp các số nguyên cho đến khi gặp số 0 thì dừng, in ra tổng các số vừa nhập.

```python
tong = 0
while True:
    x = int(input())
    if x == 0:  # Số 0 đóng vai trò lính canh báo hiệu kết thúc
        break
    tong += x

print(tong)
```

---

## 6. Bảng mô phỏng từng bước

Xét thuật toán tính tổng các chữ số của $N = 258$ bằng vòng lặp `while`:
```python
n = 258
tong = 0
while n > 0:
    chu_so = n % 10
    tong += chu_so
    n //= 10
```

### Bảng theo dõi biến thiên ô nhớ RAM qua từng vòng lặp:

| Vòng Lặp | Điều Kiện `n > 0` | Tách Chữ Số Cuối `chu_so = n % 10` | Tích Lũy `tong += chu_so` | Cắt Bỏ Chữ Số Cuối `n //= 10` |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | *(Bắt đầu)* | Chưa có | `tong = 0` | `n = 258` |
| **Vòng 1** | `258 > 0` (True) | `258 % 10 = 8` | `tong = 0 + 8 = 8` | `n = 258 // 10 = 25` |
| **Vòng 2** | `25 > 0` (True) | `25 % 10 = 5` | `tong = 8 + 5 = 13` | `n = 25 // 10 = 2` |
| **Vòng 3** | `2 > 0` (True) | `2 % 10 = 2` | `tong = 13 + 2 = 15` | `n = 2 // 10 = 0` |
| **Vòng 4** | `0 > 0` (**False!**) | *(Dừng lặp, thoát ra ngoài)* | Giữ nguyên `15` | Giữ nguyên `0` |

$$\implies \text{Tổng các chữ số thu được: } 8 + 5 + 2 = \mathbf{15}$$

---

## 7. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: ĐẶT SAI VỊ TRÍ CỦA LỆNH TĂNG BIẾN ĐIỀU KHIỂN KHI DÙNG CONTINUE**
> * Quan sát đoạn code bị treo vô tận:
>  ```python
>   i = 0
>   while i < 5:
>       if i == 3:
>           continue  # Nhảy lên đầu vòng lặp ngay!
>       i += 1        # Khi i == 3, dòng này KHÔNG BAO GIỜ được chạy tới!
>   ```
> * **Hậu quả:** Khi $i = 3$, lệnh `continue` nhảy ngay lên kiểm tra điều kiện, bỏ qua lệnh tăng `i += 1`. Biến $i$ mãi bằng 3 $\implies$ Treo máy!
> * **Khắc phục:** Luôn cập nhật biến điều khiển `i += 1` trước câu lệnh `continue`.

> **BẪY LỖI 2: NHẦM LẪN GIỮA ĐIỀU KIỆN TIẾP TỤC VÀ ĐIỀU KIỆN DỪNG**
> * Trong tiếng Việt ta nói: *"Lặp cho đến khi $x > 10$ thì dừng"*.
> * Rất nhiều bạn viết nhầm thành: `while x > 10:`.
> * **Bản chất của while:** Vòng lặp chạy khi điều kiện **ĐÚNG**. Muốn dừng khi $x > 10$, nghĩa là phải chạy khi $x \le 10$:
>  $$\mathbf{while \ x <= 10:}$$

---

## 8. Mẫu code thường gặp

```python
# Mẫu đếm số chữ số của một số nguyên dương N
n = int(input())
dem = 0

while n > 0:
    dem += 1
    n //= 10

print(dem)
```


## Bài tập thực hành


### Bài 01 [pya_l08_p08_tim_luy_thua_cua_2_lon_hon_n]: Tìm lũy thừa của 2 lớn hơn N

Bối cảnh: Tìm lũy thừa nhỏ nhất của 2 mà lớn hơn hoặc bằng số $N$ cho trước. Đây là bài toán cơ bản trong khoa học máy tính liên quan đến cấp phát bộ nhớ.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy tìm số có dạng lũy thừa của 2 ($1, 2, 4, 8, 16, 32, \dots$) **nhỏ nhất mà lớn hơn $N$**.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Số lũy thừa của 2 tìm được.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 16 |

**Giải thích:**

Lũy thừa của 2 gồm 1, 2, 4, 8, 16... Số nhỏ nhất $> 10$ là 16.

**Ví dụ mẫu (Sample 2):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 16 | 32 |

**Giải thích:**

Số phải lớn hơn 16 nên là 32.



### Bài 02 [pya_l08_p06_gap_doi_to_giay_len_mat_trang]: Gấp đôi tờ giấy lên mặt trăng

Bối cảnh: Trong giờ thủ công, bạn Mít lấy ra một tờ giấy siêu mỏng ban đầu có độ dày là $1\text{ mm}$ để làm thí nghiệm vui. Mít gấp đôi tờ giấy lại, và lạ chưa: cứ mỗi lần gấp đôi tờ giấy lại, độ dày của nó lại tăng gấp đôi ($2\text{ mm}, 4\text{ mm}, 8\text{ mm}, \dots$). Mít mơ ước chồng giấy của mình sẽ cao chạm tới mặt trăng. Hãy giúp Mít đếm số lần gấp.

Nhiệm vụ: Hỏi cần phải gấp đôi tờ giấy ít nhất bao nhiêu lần để độ dày của nó đạt hoặc vượt quá độ cao $H\text{ mm}$?

**Đầu vào (Input):**

Một số tự nhiên $H$ ($1 \le H \le 10^9$).

**Đầu ra (Output):**

Số lần gấp đôi tối thiểu.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 | 4 |

**Giải thích:**

Lần 1: 2mm, lần 2: 4mm, lần 3: 8mm, lần 4: 16mm ($\ge 10$). Cần 4 lần.



### Bài 03 [pya_l08_p07_ong_heo_mua_xe_may]: Ống heo mua xe máy

Bối cảnh: Bác Nam có một chú heo đất thật xinh đặt ở góc nhà. Bác muốn tiết kiệm tiền để mua một chiếc xe máy có giá $P$ nghìn đồng cho cả gia đình đi chơi.
 * Ngày thứ nhất bác bỏ vào ống heo 1 nghìn đồng.
 * Ngày thứ hai bác bỏ vào 2 nghìn đồng.
 * Ngày thứ $k$ bác bỏ vào đúng $k$ nghìn đồng.
Mỗi tối bác đều lắc heo nghe kêu leng keng rất vui. Hãy giúp bác Nam đếm xem sau mấy ngày thì đủ tiền.

Nhiệm vụ: Hỏi sau bao nhiêu ngày thì tổng số tiền trong ống heo của bác Nam đạt hoặc vượt quá $P$ nghìn đồng?

**Đầu vào (Input):**

Một số tự nhiên $P$ ($1 \le P \le 10^7$).

**Đầu ra (Output):**

Số ngày ít nhất.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 15 | 5 |

**Giải thích:**

Ngày 1: 1k, ngày 2: 2k (tổng 3k), ngày 3: 3k (tổng 6k), ngày 4: 4k (tổng 10k), ngày 5: 5k (tổng 15k $\ge 15$). Sau 5 ngày.



### Bài 04 [pya_l08_p10_dem_so_luong_chu_so_cua_n]: Đếm số lượng chữ số của N

Bối cảnh: Cho một số nguyên dương $N$. Hãy đếm xem số đó có bao nhiêu chữ số. Ví dụ: $12345$ có $5$ chữ số.

Nhiệm vụ: Nhập vào một số nguyên dương $N$. Dùng vòng lặp `while` và phép chia nguyên `// 10`, hãy đếm xem số $N$ có bao nhiêu chữ số.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

**Đầu ra (Output):**

Số lượng chữ số của $N$.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 2026 | 4 |

**Giải thích:**

Với dữ liệu đầu vào là `2026`, kết quả thu được tương ứng là `4`.



### Bài 05 [pya_l08_p01_dem_xuoi_bang_while]: Đếm xuôi bằng while

Bối cảnh: Bạn robot đang tập đếm số từ 1 đến $N$ bằng vòng lặp `while`. Hãy giúp robot hoàn thành nhiệm vụ.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Dùng vòng lặp `while`, hãy in ra các số từ $1$ đến $N$ trên một dòng.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 100$).

**Đầu ra (Output):**

Dãy số từ 1 đến $N$.
 ```python
 N = int(input())
 i = 1
 while i <= N:
 print(i, end=" ")
 i = i + 1
 ```

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 | 1 2 3 4 5 |

**Giải thích:**

In các số từ 1 đến 5 trên một dòng cách nhau khoảng trắng.



### Bài 06 [pya_l08_p03_nhap_so_den_khi_gap_so_0]: Nhập số đến khi gặp số 0

Bối cảnh: Trò chơi nhập số: Người chơi nhập liên tục các số, chương trình đếm tổng số lượng số đã nhập cho đến khi gặp số 0 thì dừng lại.

Nhiệm vụ: Viết chương trình nhập liên tiếp các số nguyên từ bàn phím. Việc nhập kết thúc khi người dùng nhập số 0. Hãy đếm xem người dùng đã nhập **bao nhiêu số** (không tính số 0 cuối cùng).

**Đầu vào (Input):**

Một dãy các số nguyên, kết thúc bằng số 0.

**Đầu ra (Output):**

Một số nguyên duy nhất là số lượng các số đã nhập trước số 0.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 12 <br> 8 <br> 0 | 3 |

**Giải thích:**

Có 3 số: 5, 12, 8 đã được nhập trước khi gặp 0.



### Bài 07 [pya_l08_p04_tong_day_so_ket_thuc_bang_0]: Tổng dãy số kết thúc bằng 0

Bối cảnh: Thí sinh nhập liên tiếp các số nguyên. Khi nhập số 0, chương trình dừng lại và in ra tổng tất cả các số đã nhập trước đó.

Nhiệm vụ: Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 0. Hãy tính và in ra **tổng của tất cả các số** đã nhập.

**Đầu vào (Input):**

Một dãy số nguyên kết thúc bằng 0.

**Đầu ra (Output):**

Tổng các số.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 20 <br> 5 <br> 0 | 35 |

**Giải thích:**

$10 + 20 + 5 = 35$.



### Bài 08 [pya_l08_p11_tro_choi_doan_so_nhi_phan]: Trò chơi đoán số nhị phân

Bối cảnh: Giờ ra chơi, bạn An nghĩ ra một số bí mật từ 1 đến $N$ rồi đố cả lớp cùng đoán. Bạn Bình xung phong với chiến thuật rất hay tên là "Chặt đôi khoảng tìm kiếm" (Tìm kiếm nhị phân) để đoán số: mỗi câu hỏi Bình chia đôi khoảng đang xét ($N = N // 2$). Cả lớp nín thở theo dõi từng lượt đoán của Bình. Hãy giúp Bình tính trước xem mình cần đoán mấy lượt.

Nhiệm vụ: Hỏi trong trường hợp xấu nhất, Bình phải đoán **nhiều nhất bao nhiêu lần** thì chắc chắn tìm ra số của An (lặp cho đến khi khoảng chỉ còn 1 số: $N == 1$)?

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^9$).

**Đầu ra (Output):**

Số bước đoán tối đa.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 8 | 4 |

**Giải thích:**

Các bước: $8 \to 4 \to 2 \to 1$ (cần 4 bước).



### Bài 09 [pya_l08_p02_rut_tham_den_khi_trung]: Rút thăm đến khi trúng

Bối cảnh: Giờ ra chơi, Bo tổ chức trò bốc thăm trúng thưởng cho cả lớp thật rộn ràng. Bo bỏ vào hộp thật nhiều lá phiếu có ghi số, rồi bốc lên từng lá một. Cả lớp reo hò vì ai cũng mong chờ, và Bo sẽ dừng lại ngay khi bốc trúng lá phiếu ghi số **7**. Trò chơi vui quá nên ai cũng muốn biết kết quả. Hãy giúp Bo công bố kết quả bốc thăm.

Nhiệm vụ: Nhập liên tục các số nguyên từ bàn phím cho đến khi gặp số 7 thì dừng lại. Hãy in ra dòng chữ: `DA TRUNG THUONG!`

**Đầu vào (Input):**

Một dãy các số nguyên, mỗi số trên một dòng, số cuối cùng chắc chắn là số 7.

**Đầu ra (Output):**

In `DA TRUNG THUONG!` sau khi vòng lặp dừng.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 10 <br> 25 <br> 7 | DA TRUNG THUONG! |

**Giải thích:**

Sau khi nhập hai số 10 và 25, số thứ ba nhập vào là 7 nên vòng lặp dừng và in ra thông báo `DA TRUNG THUONG!`.



### Bài 10 [pya_l08_p12_day_so_collatz_3n_1]: Dãy số Collatz (3n + 1)

Bối cảnh: Bạn Tí vừa đọc được một câu đố toán học kỳ bí tên là giả thuyết Collatz trong quyển truyện tranh khoa học ở thư viện. Trò biến hình số bắt đầu từ số tự nhiên $N > 0$ như sau:
 * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
 * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
 * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
Tí khoe với cả lớp mà chưa bạn nào đếm đúng số bước. Hãy giúp Tí đếm số bước biến hình.

Nhiệm vụ: Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.

**Đầu vào (Input):**

Một số tự nhiên $N$ ($1 \le N \le 10^5$).

**Đầu ra (Output):**

Số bước biến đổi.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 6 | 8 |

**Giải thích:**

Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi).



### Bài 11 [pya_l08_p05_dem_so_chan_den_khi_gap_0]: Đếm số chẵn đến khi gặp 0

Bối cảnh: Trong trò chơi đếm số, người dùng nhập các số liên tục. Chương trình đếm xem có bao nhiêu số chẵn đã được nhập, cho đến khi gặp số 0 thì dừng.

Nhiệm vụ: Nhập liên tiếp các số nguyên từ bàn phím cho đến khi nhập số 0. Hãy đếm xem có bao nhiêu số chẵn trong các số đã nhập (không tính số 0).

**Đầu vào (Input):**

Dãy số nguyên kết thúc bằng 0.

**Đầu ra (Output):**

Số lượng số chẵn.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 4 <br> 7 <br> 8 <br> 12 <br> 0 | 3 |

**Giải thích:**

Có 3 số chẵn là 4, 8, 12.



### Bài 12 [pya_l08_p09_chu_oc_sen_leo_cot_co]: Chú ốc sên leo cột cờ

Bối cảnh: Sáng nay, chú ốc sên chăm chỉ thức dậy dưới chân một cột cờ cao $H$ mét trong sân trường và quyết tâm leo lên đỉnh để ngắm mây trời.
 * Ban ngày, chú ốc sên bò lên được $A$ mét.
 * Ban đêm, khi ngủ chú bị tụt xuống $B$ mét ($B < A$).
 * Khi chú chạm tới hoặc vượt qua đỉnh cột cờ vào ban ngày, chú sẽ dừng lại và cắm cờ (không bị tụt nữa).
Các bạn kiến đứng dưới cổ vũ ầm ĩ. Hãy giúp chú ốc sên tính xem mình leo mất mấy ngày.

Nhiệm vụ: Hỏi chú ốc sên mất bao nhiêu ngày để leo lên tới đỉnh cột cờ?

**Đầu vào (Input):**

Ba số tự nhiên $H, A, B$ trên 3 dòng ($1 \le B < A \le H \le 10^6$).

**Đầu ra (Output):**

Số ngày để ốc sên chạm đỉnh.

**Ví dụ mẫu (Sample 1):**

| Đầu vào (Input) | Đầu ra (Output) |
|---|---|
| 5 <br> 3 <br> 1 | 2 |

**Giải thích:**

Ngày 1: leo lên 3m, đêm tụt 1m còn 2m.
Ngày 2: từ 2m leo thêm 3m lên 5m (chạm đỉnh ngay trong ngày!). Vậy mất 2 ngày.



# Phụ lục A: Nền tảng Python
## 1. KHUNG TƯ DUY CỦA MỌI BÀI LẬP TRÌNH
### Mô hình Input – Process – Output
| Bước | Em tự hỏi | Ghi ra giấy |
|------|-----------|-------------|
| Đầu vào | Đề cho gì? | Tên từng số, từng dòng |
| Xử lý | Tính gì, theo bước nào? | Công thức từng bước |
| Đầu ra | In ra cái gì? | Đúng thứ tự cần in |
```python
n = int(input())
tong = n + 10
print(tong)
```
### Công thức trước code
| Bước | Việc làm |
|------|----------|
| 1 | Gạch chân các số đề cho |
| 2 | Viết cách tính bằng lời của em |
| 3 | Tính tay một ví dụ nhỏ rồi mới viết code |
### Chuỗi ghi nhớ nền tảng
> Đọc vào — tính toán — in ra — thử lại.
```python
a = int(input())
b = int(input())
print(a + b)
```
## 2. KHUNG CHƯƠNG TRÌNH PYTHON TỐI THIỂU
| Việc | Mẫu |
|------|-----|
| Đọc vào | `n = int(input())` |
| Tính toán | `ket_qua = n + 5` |
| In ra | `print(ket_qua)` |
Hai số trên một dòng, cách nhau bằng dấu cách:
```python
a, b = map(int, input().split())
print(a + b)
```
## 3. BIẾN VÀ KIỂU DỮ LIỆU
### Quy tắc đặt tên biến
| Quy tắc | Đúng | Chưa đúng |
|---------|------|-----------|
| Chữ, số, dấu gạch dưới | `diem_toan` | `điểm-toán` |
| Bắt đầu bằng chữ | `tong_1` | `1_tong` |
| Ngắn mà rõ nghĩa, không trùng từ của Python | `tuoi` | `print` |
```python
tuoi = 10
ten = "Na"
print(tuoi)
```
### Các kiểu int, float, str, bool, list
| Kiểu | Nghĩa | Ví dụ |
|------|-------|-------|
| `int` | Số nguyên | `5`, `-3` |
| `float` | Số có phần lẻ | `2.5` |
| `str` | Chuỗi chữ | `"xin chào"` |
| `bool` | Đúng hoặc sai | `True`, `False` |
| `list` | Nhiều giá trị | `[2, 4, 6]` |
```python
tuoi = 10
ten = "Na"
diem = [8, 9, 10]
print(ten)
```
### Khởi tạo biến tích lũy
| Muốn làm gì | Viết lúc đầu |
|-------------|--------------|
| Tính tổng | `tong = 0` |
| Đếm số lượng | `dem = 0` |
| Tìm số to nhất | `lon_nhat = 0` |
| Ghép chữ | `cau = ""` |
## 4. NHẬP VÀ XUẤT DỮ LIỆU
### Ba lưu ý thường gặp
| Lưu ý | Mẫu đúng |
|-------|----------|
| Chữ đọc vào luôn là chuỗi | `ten = input()` |
| Muốn tính phải đổi kiểu | `n = int(input())` |
| Một dòng nhiều số thì tách ra | `a, b = map(int, input().split())` |
```python
n = int(input())
print(n + 1)
```
Đọc số có phần lẻ, đọc hai số một dòng, in theo ý muốn:
```python
x = float(input())
a, b = map(int, input().split())
print(3, 4, 5, sep="-")
print("xin", end=" ")
print("chào")
```
In kèm lời giải thích:
```python
tuoi = 10
print(f"Năm nay em {tuoi} tuổi.")
```
## 5. TOÁN TỬ VÀ BIỂU THỨC
### Toán tử số học
| Viết | Nghĩa | Kết quả của `5` và `2` |
|------|-------|------------------------|
| `+ - * /` | Cộng trừ nhân chia | `7, 3, 10, 2.5` |
| `//` | Chia lấy phần nguyên | `5 // 2` cho `2` |
| `%` | Chia lấy phần dư | `5 % 2` cho `1` |
| `**` | Lũy thừa | `2 ** 3` cho `8` |
```python
print(3 + 2)
print(5 // 2)
print(2 ** 3)
```
### Chia nguyên và phần dư
| Muốn biết | Dùng |
|-----------|------|
| Mỗi bạn được mấy cái | `7 // 2` cho `3` |
| Còn thừa mấy cái | `7 % 2` cho `1` |
| Số có chẵn không | `n % 2 == 0` |
### Toán tử so sánh
| Viết | Nghĩa |
|------|-------|
| `==` / `!=` | Bằng nhau / khác nhau |
| `>` / `<` | Lớn hơn / nhỏ hơn |
| `>=` / `<=` | Lớn hơn hoặc bằng / nhỏ hơn hoặc bằng |
```python
print(5 > 3)
print(4 == 5)
```
### Toán tử logic
| Viết | Nghĩa | Ví dụ |
|------|-------|-------|
| `and` | Cả hai đều đúng | `a > 0 and b > 0` |
| `or` | Một cái đúng là đủ | `a > 0 or b > 0` |
| `not` | Đổi đúng thành sai | `not (a > 0)` |
```python
tuoi = 10
print(tuoi > 5 and tuoi < 15)
```
### Thứ tự ưu tiên
| Trước | Sau |
|-------|-----|
| Ngoặc `( )`, rồi `**` | Nhân chia `* / // %` |
| Cộng trừ `+ -` | So sánh, `not`, `and`, `or` |
```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```
## 6. ĐIỀU KIỆN — RẼ NHÁNH
### Mẫu if / if-else / if-elif-else
| Mẫu | Khi nào dùng |
|-----|--------------|
| `if` | Chỉ làm khi đúng |
| `if-else` | Chọn một trong hai |
| `if-elif-else` | Xếp nhiều mức |
```python
diem = int(input())
if diem >= 9:
    print("giỏi")
elif diem >= 7:
    print("khá")
else:
    print("cố gắng thêm")
```
### Quy tắc thụt lề
| Quy tắc | Nhớ |
|---------|-----|
| Sau dấu `:` thụt vào 4 dấu cách | Dòng trong nhánh lùi vào |
| Cùng nhánh thì thẳng hàng | Hết nhánh thì hết thụt lề |
```python
n = int(input())
if n > 0:
    print("số dương")
print("xong")
```
### Lỗi thường gặp
| Lỗi | Cách sửa |
|-----|----------|
| Quên dấu `:` sau `if` | Thêm `:` cuối dòng điều kiện |
| Viết `=` khi so sánh | So sánh viết `==` |
| Thụt lề lệch nhau | Căn thẳng hàng, mỗi lần 4 dấu cách |
```python
n = 5
if n == 5:
    print("đúng rồi")
```
## 7. VÒNG LẶP
### for và range
| Viết | Chạy qua |
|------|----------|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 6)` | `1, 2, 3, 4, 5` |
| `range(2, 10, 2)` | `2, 4, 6, 8` |
```python
tong = 0
for i in range(1, 101):
    tong = tong + i
print(tong)
```
### while
```python
n = 5
while n > 0:
    print(n)
    n = n - 1
```
### break và continue
| Lệnh | Nghĩa |
|------|-------|
| `break` | Dừng hẳn vòng lặp |
| `continue` | Bỏ lượt này, sang lượt sau |
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
### Vòng lặp lồng nhau
```python
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()
```
## 8. BỐN MẪU TÍCH LŨY
| Mẫu | Bắt đầu | Trong vòng lặp |
|-----|---------|----------------|
| Tổng | `tong = 0` | `tong = tong + x` |
| Đếm | `dem = 0` | `dem = dem + 1` |
| To nhất | `lon_nhat = 0` | `if x > lon_nhat:` rồi gán |
| Nhỏ nhất | `nho_nhat = danh_sach[0]` | `if x < nho_nhat:` rồi gán |
### Tính tổng
```python
tong = 0
for i in range(1, 6):
    tong = tong + i
print(tong)
```
### Đếm phần tử
```python
dem = 0
for i in range(1, 11):
    if i % 2 == 0:
        dem = dem + 1
print(dem)
```
### Tìm giá trị lớn nhất
```python
lon_nhat = 0
for x in [3, 7, 2, 9, 4]:
    if x > lon_nhat:
        lon_nhat = x
print(lon_nhat)
```
### Tìm giá trị nhỏ nhất
```python
danh_sach = [3, 7, 2, 9, 4]
nho_nhat = danh_sach[0]
for x in danh_sach:
    if x < nho_nhat:
        nho_nhat = x
print(nho_nhat)
```
## 9. DANH SÁCH VÀ CHUỖI
### Danh sách và chỉ số
Vị trí đầu là `0`, vị trí cuối là `-1`.
```python
ban = ["An", "Bình", "Chi"]
print(ban[0])
print(ban[-1])
print(len(ban))
```
### Đọc và duyệt danh sách
```python
n = int(input())
danh_sach = []
for i in range(n):
    danh_sach.append(int(input()))
for i in range(len(danh_sach)):
    print(i, danh_sach[i])
```
### Các thao tác cơ bản
| Muốn làm gì | Mẫu |
|-------------|-----|
| Thêm vào cuối | `danh_sach.append(x)` |
| Cộng tổng / to nhất / nhỏ nhất | `sum(...)` / `max(...)` / `min(...)` |
| Sắp xếp / đếm số lượng | `sort()` / `len(...)` |
### Xử lý chuỗi
| Muốn làm gì | Mẫu |
|-------------|-----|
| Đếm số chữ / lấy chữ đầu | `len(ten)` / `ten[0]` |
| Tách câu thành từ | `cau.split()` |
| So sánh hai chuỗi | `if a == b:` |
```python
cau = input()
tu = cau.split()
print(len(tu))
print(tu)
```
## 10. GỠ LỖI VÀ KIỂM THỬ
### In giá trị trung gian
```python
n = int(input())
print(n)
tong = n * 2
print(tong)
```
| Muốn xem gì | In thêm dòng nào |
|-------------|------------------|
| Giá trị đọc vào | `print(n)` sau `input()` |
| Trong vòng lặp | `print(i, tong)` trong vòng lặp |
### Bộ test tối thiểu
| Nhóm | Ví dụ với bài chẵn lẻ |
|------|-----------------------|
| Nhỏ nhất | `1` |
| Hay gặp | `4`, `7` |
| Chỗ dễ đổi kết quả | `0`, số âm `-2` |
```python
n = int(input())
if n % 2 == 0:
    print("số chẵn")
else:
    print("số lẻ")
```
## TÓM TẮT MỘT TRANG
| Việc cần làm | Mẫu nhanh |
|--------------|-----------|
| Đọc một số nguyên / hai số một dòng | `n = int(input())` / `a, b = map(int, input().split())` |
| In kết quả / in kèm chữ | `print(kq)` / `print(f"Tổng là {tong}")` |
| Cộng trừ nhân chia / nguyên, dư | `+ - * /` / `// %` |
| So sánh / kết hợp | `== != > < >= <=` / `and or not` |
| Rẽ nhánh / lặp | `if / elif / else:` / `for i in range(n):` / `while ...:` |
| Dừng hẳn / bỏ lượt này | `break / continue` |
| Tổng / đếm / to nhất, nhỏ nhất | `tong + x` / `dem + 1` / `max(...) min(...)` |
| Danh sách / số lượng | `append(x)` / `len(...)` |


# Phụ lục B: Lời giải bài tập tham khảo


> Phần này cung cấp mã nguồn Python 3 tham khảo hoàn chỉnh cho toàn bộ bài tập trong sách.


## Chương 01 — Bài 01: Lệnh xuất nhập, biến số và kiểu dữ liệu


### pya_l01_p01_loi_chao_robot — Lời chào robot


```python
print("Xin chao cac ban! Toi la Robot Python.")
```


### pya_l01_p02_cau_doi_tet — Câu đối ngày tết


```python
print("Chuc mung nam moi")
print("Van su nhu y")
```


### pya_l01_p05_doc_in_so_nguyen — Đọc và in số nguyên


```python
n = int(input())
print(n)
```


### pya_l01_p03_in_so_sep — In số trên một hàng với sep


```python
print(1, 2, 3, 4, 5, sep="-")
```


### pya_l01_p25_nhan_doi_gia_tri — Nhân đôi giá trị


```python
n = int(input())
print(n * 2)
```


### pya_l01_p19_in_end_cung_dong — In không xuống dòng với end


```python
print("Lap trinh", end=" ")
print("rat vui!")
```


### pya_l01_p11_hoan_doi_hai_bien — Hoán đổi vị trí hai biến


```python
a = int(input())
b = int(input())
a, b = b, a
print(a, b)
```


### pya_l01_p21_tong_hai_so_2_dong — Tổng hai số nguyên 2 dòng


```python
a = int(input())
b = int(input())
print(a + b)
```


### pya_l01_p22_hieu_hai_so — Hiệu hai số nguyên


```python
a = int(input())
b = int(input())
print(a - b)
```


### pya_l01_p23_tich_hai_so — Tích hai số nguyên


```python
a = int(input())
b = int(input())
print(a * b)
```


### pya_l01_p04_cap_so_nhan_doi — Cặp số nhân đôi


```python
a = int(input().strip())
print(a * 2)
```


### pya_l01_p18_tuoi_cua_be_sau_5_nam — Tuổi của bé sau 5 năm


```python
n = int(input().strip())
print(n + 5)
```


### pya_l01_p12_chuc_sinh_nhat — Lời chúc sinh nhật cá nhân hóa


```python
ten = input()
tuoi = int(input())
print(f"Chuc mung sinh nhat {ten}, ban tron {tuoi} tuoi!")
```


### pya_l01_p07_chiec_hop_hoan_doi_bi_mat — Chiếc hộp hoán đổi bí mật


```python
a = int(input().strip())
b = int(input().strip())
a, b = b, a
print(a, b)
```


### pya_l01_p17_tam_danh_thiep_thong_minh — Tấm danh thiếp thông minh


```python
ten = input().strip()
print("Xin chao ban " + ten + "!")
```


### pya_l01_p06_cua_hang_banh_ran — Cửa hàng bánh rán


```python
a = int(input().strip())
b = int(input().strip())
print(a * b)
```


### pya_l01_p15_phep_nhan_bang — In bảng phép nhân cơ bản


```python
a = int(input())
b = int(input())
print(f"{a} x {b} = {a * b}")
```


### pya_l01_p09_tong_hai_so_cung_dong — Tổng hai số trên cùng 1 dòng


```python
a, b = map(int, input().split())
print(a + b)
```


### pya_l01_p20_doi_thuoc_ke_milimet — Đổi thước kẻ milimet


```python
a = int(input().strip())
b = int(input().strip())
print(a * 10 + b)
```


### pya_l01_p14_ghep_ngay_thang_nam — Ghép ngày tháng năm định dạng chuẩn


```python
d, m, y = map(int, input().split())
print(d, m, y, sep="/")
```


### pya_l01_p08_doan_tau_toa_xe_ghep_so — Đoàn tàu toa xe ghép số


```python
s1 = input().strip()
s2 = input().strip()
print(s1 + s2)
print(int(s1) + int(s2))
```


### pya_l01_p16_chenh_lech_tuoi — Chênh lệch tuổi của hai anh em


```python
a, e = map(int, input().split())
print(f"Anh hon em {a - e} tuoi.")
```


### pya_l01_p13_bon_phep_tinh — Bốn phép tính đồng thời


```python
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
```


### pya_l01_p10_co_may_thoi_gian_3_the_he — Cỗ máy thời gian 3 thế hệ


```python
a = int(input())
b = int(input())
c = int(input())
tuoi_bo = a + b
tuoi_ong = tuoi_bo + c
print(tuoi_bo)
print(tuoi_ong)
print(a + tuoi_bo + tuoi_ong)
```


### pya_l01_p24_ve_tham_quan_chua_huong — Vé tham quan chùa hương


```python
a = int(input())
b = int(input())
x = int(input())
y = int(input())
n = int(input())
m = int(input())
so_tre_em = m
so_nguoi_lon = n - m
tong_tien = so_nguoi_lon * (a + x) + so_tre_em * (b + y)
print(tong_tien)
```


## Chương 01 — Bài 02: Toán tử và biểu thức


### pya_l02_p02_luy_thua_bac_hai — Lũy thừa bậc hai


```python
n = int(input())
print(n ** 2)
```


### pya_l02_p03_lap_phuong — Lập phương của một số


```python
a = int(input())
print(a ** 3)
```


### pya_l02_p04_chu_so_tan_cung — Lấy chữ số tận cùng


```python
n = int(input())
print(n % 10)
```


### pya_l02_p09_hai_chu_so_cuoi — Lấy hai chữ số tận cùng


```python
n = int(input())
print(n % 100)
```


### pya_l02_p11_bieu_thuc_bac_nhat — Giá trị biểu thức bậc nhất


```python
x = int(input())
print(3 * x + 5)
```


### pya_l02_p25_xoa_chu_so_cuoi — Xóa chữ số tận cùng


```python
n = int(input())
print(n // 10)
```


### pya_l02_p28_xep_ban_hoc — Xếp hàng vào bàn học


```python
n = int(input())
print((n + 1) // 2)
```


### pya_l02_p13_luy_thua_cau_thang — Lũy thừa cầu thang


```python
a = int(input())
n = int(input())
print(a ** n)
```


### pya_l02_p07_dong_hop_banh — Đóng hộp bánh ngọt


```python
m = int(input())
print(m // 6, m % 6)
```


### pya_l02_p10_chu_so_hang_chuc — Chữ số hàng chục


```python
n = int(input())
print((n // 10) % 10)
```


### pya_l02_p14_doi_phut_ra_gio_phut — Đổi phút ra giờ phút


```python
t = int(input())
print(t // 60, t % 60)
```


### pya_l02_p22_nhan_doi_luy_thua — Nhân đôi lũy thừa


```python
n = int(input().strip())
print(2 ** n)
```


### pya_l02_p27_vong_chay_dien_kinh — Vòng chạy điền kinh


```python
n = int(input())
print(n // 100, n % 100)
```


### pya_l02_p05_bong_den_vien_bien_hieu — Bóng đèn viền biển hiệu


```python
a = int(input())
canh_cm = a * 10
print(canh_cm * 4 // 5)
```


### pya_l02_p16_du_quay_vong_tron — Đu quay vòng tròn


```python
n = int(input())
c = int(input())
print(n // c, n % c)
```


### pya_l02_p23_so_keo_con_thua — Số kẹo còn thừa


```python
a = int(input().strip())
b = int(input().strip())
print(a % b)
```


### pya_l02_p20_phuc_hoi_so_bi_chia — Bất biến chia kẹo và phục hồi số bị chia


```python
b, q, r = map(int, input().split())
print(b * q + r)
```


### pya_l02_p32_da_thuc_bac_hai — Đa thức bậc hai


```python
x = int(input())
print(2 * (x ** 2) - 4 * x + 9)
```


### pya_l02_p26_trong_cay_dai_lo — Trồng cây đại lộ


```python
l = int(input().strip())
d = int(input().strip())
print(l // d + 1)
```


### pya_l02_p15_gia_tri_bieu_thuc_pemdas — Giá trị biểu thức PEMDAS


```python
a = int(input())
b = int(input())
c = int(input())
print(a + b * c ** 2)
```


### pya_l02_p24_doi_gio_ra_phut_giay — Đổi giờ ra phút giây


```python
h = int(input())
m = int(input())
s = int(input())
print(h * 3600 + m * 60 + s)
```


### pya_l02_p29_tach_chu_so_tan_cung — Tách chữ số tận cùng


```python
n = int(input())
print(n % 10)
print(n // 10 % 10)
```


### pya_l02_p30_dao_nguoc_so_2_chu_so — Đảo ngược số 2 chữ số


```python
N = int(input())
chuc = N // 10
don_vi = N % 10
dao_nguoc = don_vi * 10 + chuc
print(dao_nguoc)
```


### pya_l02_p33_tich_hai_tong — Biểu thức có dấu ngoặc


```python
a, b, c, d = map(int, input().split())
print((a + b) * (c - d))
```


### pya_l02_p34_dong_ho_24h — Đồng hồ 24 giờ


```python
h, k = map(int, input().split())
print((h + k) % 24)
```


### pya_l02_p35_ngay_trong_tuan — Ngày trong tuần


```python
d, n = map(int, input().split())
print((d + n) % 7)
```


### pya_l02_p01_chia_deu_banh_quy — Chia đều bánh quy


```python
a = int(input().strip())
b = int(input().strip())
print(a // b, a % b)
```


### pya_l02_p31_xe_buyt_cho_hoc_sinh — Xe buýt chở học sinh


```python
n = int(input().strip())
k = int(input().strip())
print((n + k - 1) // k)
```


### pya_l02_p19_chuyen_xe_hoc_sinh — Tính số chuyến xe cần thiết


```python
n, k = map(int, input().split())
print((n + k - 1) // k)
```


### pya_l02_p21_chia_nguyen_chia_du — Phép chia nguyên và chia dư cơ bản


```python
a, b = map(int, input().split())
print(a // b, a % b)
```


### pya_l02_p08_kim_dong_ho_12_gio — Kim đồng hồ 12 giờ


```python
h = int(input().strip())
k = int(input().strip())
print((h + k - 1) % 12 + 1)
```


### pya_l02_p06_chia_keo_hoc_sinh — Chia kẹo cho các bạn


```python
n, k = map(int, input().split())
print(n // k)
print(n % k)
```


### pya_l02_p12_ban_co_caro_vo_tan — Bàn cờ Ca-rô vô tận


```python
k = int(input())
w = int(input())
hang = (k - 1) // w + 1
cot = (k - 1) % w + 1
print(hang, cot)
```


### pya_l02_p17_tong_ba_chu_so — Tổng các chữ số của số có 3 chữ số


```python
n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
print(tram + chuc + don_vi)
```


### pya_l02_p36_phan_so_dai_so — Tính phân số đại số


```python
a, b, c, d = map(int, input().split())
print(f"{(a + b) / (c + d):.2f}")
```


### pya_l02_p18_so_dao_nguoc_3_chu_so — Số đảo ngược 3 chữ số


```python
n = int(input())
tram = n // 100
chuc = (n // 10) % 10
don_vi = n % 10
print(don_vi * 100 + chuc * 10 + tram)
```


## Chương 01 — Bài 03: Phép chia nguyên, chia dư và lũy thừa


### pya_l03_p31_doi_do_la_sang_tien_viet — Đổi đô la sang tiền việt


```python
d = int(input())
print(d * 25000)
```


### pya_l03_p01_hinh_vuong — Chu vi và diện tích hình vuông


```python
a = int(input())
print(4 * a, a * a)
```


### pya_l03_p06_doi_don_vi_dai — Đổi mét sang centimet và milimet


```python
m = int(input())
print(m * 100, m * 1000)
```


### pya_l03_p20_khung_tranh_hinh_vuong — Khung tranh hình vuông


```python
a = int(input())
print(4 * a, a * a)
```


### pya_l03_p14_doi_do_c_sang_do_f — Đổi độ C sang độ F


```python
c = int(input())
print(c * 9 // 5 + 32)
```


### pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat — Cạnh còn lại của hình chữ nhật


```python
p = int(input())
a = int(input())
print(p // 2 - a)
```


### pya_l03_p11_dien_tich_tam_giac_vuong — Diện tích tam giác vuông


```python
a = int(input())
h = int(input())
print(a * h // 2)
```


### pya_l03_p21_chu_vi_tam_giac_abc — Chu vi tam giác ABC


```python
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```


### pya_l03_p30_the_tich_hop_chu_nhat — Thể tích hộp chữ nhật


```python
d = int(input())
r = int(input())
c = int(input())
print(d * r * c)
```


### pya_l03_p19_manh_vuon_chu_nhat — Mảnh vườn chữ nhật


```python
a = int(input())
b = int(input())
chu_vi = (a + b) * 2
dien_tich = a * b
print(chu_vi, dien_tich)
```


### pya_l03_p10_dien_tich_bon_hoa_chu_thap — Diện tích bồn hoa chữ thập


```python
a = int(input())
b = int(input())
print(2 * a * b - b * b)
```


### pya_l03_p08_thuan_di_gap_anh — Thuận đi gặp ánh


```python
x = int(input())
y = int(input())
v = int(input())
print((y - x) // v)
```


### pya_l03_p23_ho_ca_sau_va_dao_nho — Hồ cá sấu và đảo nhỏ


```python
a = int(input())
b = int(input())
c = int(input())
print(a * a - b * c)
```


### pya_l03_p03_chu_vi_tam_giac — Chu vi hình tam giác


```python
a, b, c = map(int, input().split())
print(a + b + c)
```


### pya_l03_p09_phut_sang_gio_phut — Đổi phút sang giờ và phút


```python
m = int(input())
print(f"{m // 60} gio {m % 60} phut")
```


### pya_l03_p33_tinh_van_toc_lam_tron — Tính vận tốc làm tròn


```python
d = int(input())
t = int(input())
print(f"{d / t:.2f}")
```


### pya_l03_p25_lat_gach_san_truong — Lát gạch sân trường


```python
d = int(input())
r = int(input())
k = int(input())
print(d * r // (k * k))
```


### pya_l03_p27_rao_quanh_vuon_hoa_co_cua — Rào quanh vườn hoa có cửa


```python
a = int(input())
b = int(input())
c = int(input())
print(((a + b) * 2 - c) * 15)
```


### pya_l03_p02_hinh_chu_nhat — Chu vi và diện tích hình chữ nhật


```python
a, b = map(int, input().split())
print(2 * (a + b), a * b)
```


### pya_l03_p07_doi_khoi_luong — Đổi tạ và yến sang kilogram


```python
t, y = map(int, input().split())
print(t * 100 + y * 10)
```


### pya_l03_p32_hang_rao_manh_dat — Hàng rào quanh mảnh đất


```python
a, b, c = map(int, input().split())
print(2 * (a + b) - c)
```


### pya_l03_p18_chay_bo_gap_nhau — Bài toán chạy bộ hai người ngược chiều


```python
s, v1, v2 = map(int, input().split())
print(f"{s / (v1 + v2):.1f}")
```


### pya_l03_p22_dien_tich_tam_giac_vuong — Diện tích tam giác vuông


```python
a, b = map(int, input().split())
print(f"{(a * b) / 2:.1f}")
```


### pya_l03_p29_doi_sang_tong_giay — Đổi giờ - phút - giây sang tổng số giây


```python
h, m, s = map(int, input().split())
print(h * 3600 + m * 60 + s)
```


### pya_l03_p17_son_tuong_phong — Tính tiền mua sơn quét tường


```python
a, h, x, y, g = map(int, input().split())
s_son = (a * h) - (x * y)
print(s_son * g)
```


### pya_l03_p05_dien_tich_hinh_thang — Diện tích hình thang


```python
a, b, h = map(int, input().split())
print(f"{((a + b) * h) / 2:.1f}")
```


### pya_l03_p26_van_toc_trung_binh — Tính vận tốc trung bình


```python
s, t = map(int, input().split())
print(f"{s / t:.2f}")
```


### pya_l03_p24_doi_giay_sang_gio_phut_giay — Đổi giây sang giờ phút giây


```python
tong_giay = int(input())
gio = tong_giay // 3600
giay_du = tong_giay % 3600
phut = giay_du // 60
giay = giay_du % 60
print(gio, phut, giay)
```


### pya_l03_p12_khoang_cach_thoi_gian — Khoảng thời gian giữa hai thời điểm trong ngày


```python
h1, m1, h2, m2 = map(int, input().split())
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
print(t2 - t1)
```


### pya_l03_p15_lat_gach_nen_nha — Lát nền phòng học


```python
l, w, d = map(int, input().split())
s_san = (l * 100) * (w * 100)
s_gach = d * d
print(s_san // s_gach)
```


### pya_l03_p28_doi_giay_sang_gio_phut_giay — Đổi tổng số giây sang giờ, phút, giây


```python
t = int(input())
gio = t // 3600
phut = (t % 3600) // 60
giay = t % 60
print(f"{gio}:{phut}:{giay}")
```


### pya_l03_p13_diem_trung_binh — Điểm trung bình môn học


```python
d1, d2, d3 = map(float, input().split())
print(f"{(d1 + d2 + d3) / 3:.2f}")
```


### pya_l03_p16_loi_di_quanh_ho — Diện tích lối đi quanh hồ nước


```python
a, b, d = map(int, input().split())
s_ngoai = (a + 2 * d) * (b + 2 * d)
s_ho = a * b
print(s_ngoai - s_ho)
```


## Chương 02 — Bài 04: Cấu trúc rẽ nhánh


### pya_l04_p04_so_lon_nhat_trong_hai_so — Số lớn nhất trong hai số


```python
a = int(input())
b = int(input())
print(max(a, b))
```


### pya_l04_p09_tri_tuyet_doi_cua_mot_so — Trị tuyệt đối của một số


```python
n = int(input().strip())
print(abs(n))
```


### pya_l04_p02_ve_vao_cong_vien — Vé vào công viên


```python
h = int(input())
if h >= 130:
    print("VE NGUOI LON")
else:
    print("VE TRE EM")
```


### pya_l04_p01_kiem_tra_so_chan_le — Kiểm tra số chẵn lẻ


```python
n = int(input())
if n % 2 == 0:
    print("CHAN")
else:
    print("LE")
```


### pya_l04_p06_dien_phep_tinh_lon_nhat — Điền phép tính lớn nhất


```python
a = int(input())
cong = a + a
nhan = a * a
if nhan >= cong:
    print(nhan)
else:
    print(cong)
```


### pya_l04_p07_giam_gia_sieu_thi — Giảm giá siêu thị


```python
tien = int(input().strip())
if tien >= 500:
    print(tien - 50)
else:
    print(tien)
```


### pya_l06_p03_ngay_nghi_cuoi_tuan — Ngày nghỉ cuối tuần


```python
d = int(input().strip())
if d == 1 or d == 7:
    print("NGHI")
else:
    print("DI HOC")
```


### pya_l04_p03_ai_cao_hon — Ai cao hơn?


```python
a = int(input().strip())
b = int(input().strip())
if a > b:
    print("Minh")
else:
    print("Nam")
```


### pya_l06_p01_so_chan_co_hai_chu_so — Số chẵn có hai chữ số


```python
n = int(input())
if n >= 10 and n <= 99 and n % 2 == 0:
    print("YES")
else:
    print("NO")
```


### pya_l05_p06_mario_cuu_cong_chua — Mario cứu công chúa


```python
k = int(input())
p = int(input())
n = int(input())
if k + p >= 2 * n:
    print("YES")
else:
    print("NO")
```


### pya_l06_p13_tien_dien_bac_thang — Tiền điện bậc thang


```python
n = int(input())
if n <= 100:
    print(n * 2000)
else:
    print(100 * 2000 + (n - 100) * 3500)
```


### pya_l04_p10_bac_tho_moc_cat_go — Bác thợ mộc cắt gỗ


```python
l = int(input())
k = int(input())
if l < k:
    print("KHONG DU")
else:
    print(l // k, l % k)
```


### pya_l06_p04_diem_nam_trong_hinh_chu_nhat — Điểm nằm trong hình chữ nhật


```python
# Nhap x, y va HCN (0, 0) den (W, H)
parts = list(map(int, input().split()))
x, y, w, h = parts[0], parts[1], parts[2], parts[3]
if 0 <= x <= w and 0 <= y <= h:
    print("TRONG")
else:
    print("NGOAI")
```


### pya_l06_p02_boi_chung_cua_3_va_5 — Bội chung của 3 và 5


```python
n = int(input().strip())
if n % 3 == 0 and n % 5 == 0:
    print("YES")
else:
    print("NO")
```


### pya_l06_p05_ba_canh_tam_giac_hop_le — Ba cạnh tam giác hợp lệ


```python
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("HOP LE")
else:
    print("KHONG HOP LE")
```


### pya_l06_p06_kiem_tra_nam_nhuan — Kiểm tra năm nhuận


```python
y = int(input())
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("NAM NHUAN")
else:
    print("NAM THUONG")
```


### pya_l06_p09_rut_the_may_man — Rút thẻ may mắn


```python
n = int(input().strip())
if (n % 2 == 0 and n > 50) or (n % 7 == 0):
    print("TRUNG THUONG")
else:
    print("CHUC MAY MAN")
```


### pya_l05_p03_so_lon_nhat_trong_ba_so — Số lớn nhất trong ba số


```python
line = input().split()
if len(line) == 3:
    a, b, c = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
    c = int(input().strip())
print(max(a, b, c))
```


### pya_l05_p02_dau_cua_so_nguyen — Dấu của số nguyên


```python
n = int(input().strip())
if n > 0:
    print("DUONG")
elif n < 0:
    print("AM")
else:
    print("KHONG")
```


### pya_l05_p09_thuan_di_tim_anh_da_van_toc — Thuận đi tìm ánh đa vận tốc


```python
v = float(input().strip())
if v < 10:
    print("DI BO")
elif v <= 30:
    print("XE DAP")
else:
    print("XE MAY")
```


### pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai — Cửa hàng bánh bột lọc khuyến mãi


```python
n = int(input().strip())
gia = 5000
if n >= 20:
    gia = 4000
elif n >= 10:
    gia = 4500
print(n * gia)
```


### pya_l04_p11_canh_thu_tu_hinh_chu_nhat — Cạnh thứ tư hình chữ nhật


```python
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)
```


### pya_l04_p05_chia_keo_cong_bang — Chia kẹo công bằng


```python
dong1 = input().split()
if len(dong1) >= 2:
    a = int(dong1[0])
    b = int(dong1[1])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
if a % b == 0:
    print("YES")
else:
    print("NO")
```


### pya_l05_p10_thu_may_trong_tuan — Thứ mấy trong tuần?


```python
d = int(input().strip())
if d == 1:
    print("CHU NHAT")
elif 2 <= d <= 7:
    print(f"THU {d}")
```


### pya_l05_p08_phan_loai_tam_giac — Phân loại tam giác


```python
a, b, c = map(int, input().split())
if a == b == c:
    print("DEU")
elif a == b or b == c or a == c:
    print("CAN")
else:
    print("THUONG")
```


### pya_l05_p07_tinh_cuoc_taxi_bac_thang — Tính cước taxi bậc thang


```python
n = int(input())
if n <= 1:
    print(10)
elif n <= 10:
    print(10 + (n - 1) * 8)
else:
    print(10 + 9 * 8 + (n - 10) * 6)
```


### pya_l05_p04_xep_loai_hoc_luc — Xếp loại học lực


```python
d = float(input().strip())
if d >= 8.0:
    print("GIOI")
elif d >= 6.5:
    print("KHA")
elif d >= 5.0:
    print("TRUNG BINH")
else:
    print("YEU")
```


### pya_l06_p07_so_ngay_trong_thang — Số ngày trong tháng


```python
m = int(input())
y = int(input())
if m in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif m in [4, 6, 9, 11]:
    print(30)
else:
    print(29 if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 28)
```


### pya_l06_p11_cap_doi_cung_dau_hay_trai_dau — Cặp đôi cùng dấu hay trái dấu


```python
a, b = map(int, input().split())
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("CUNG DAU")
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    print("TRAI DAU")
else:
    print("CO SO KHONG")
```


### pya_l04_p08_cap_so_bang_nhau_hay_khac — Cặp số bằng nhau hay khác?


```python
line = input().split()
if len(line) == 2:
    a, b = map(int, line)
else:
    a = int(line[0])
    b = int(input().strip())
if a > b:
    print("a LON HON b")
elif a < b:
    print("a NHO HON b")
else:
    print("HAI SO BANG NHAU")
```


### pya_l04_p12_tro_choi_oan_tu_ti — Trò chơi oẳn tù tì


```python
dong1 = input().split()
if len(dong1) >= 2:
    ti = int(dong1[0])
    teo = int(dong1[1])
else:
    ti = int(dong1[0])
    teo = int(input().split()[0])
if ti == teo:
    print("HOA")
elif (ti == 1 and teo == 2) or (ti == 2 and teo == 3) or (ti == 3 and teo == 1):
    print("TI THANG")
else:
    print("TEO THANG")
```


### pya_l05_p01_den_giao_thong_nga_tu — Đèn giao thông ngã tư


```python
den = input().strip().upper()
if den == "D" or den == "DO":
    print("DUNG LAI")
elif den == "V" or den == "VANG":
    print("DI CHAM")
elif den == "X" or den == "XANH":
    print("DUOC DI")
```


### pya_l06_p12_giao_nhau_cua_hai_doan_thang — Giao nhau của hai đoạn thẳng


```python
dong1 = input().split()
if len(dong1) >= 4:
    l1 = int(dong1[0])
    r1 = int(dong1[1])
    l2 = int(dong1[2])
    r2 = int(dong1[3])
else:
    l1 = int(dong1[0])
    r1 = int(input().split()[0])
    l2 = int(input().split()[0])
    r2 = int(input().split()[0])
if l1 >= l2:
    trai = l1
else:
    trai = l2
if r1 <= r2:
    phai = r1
else:
    phai = r2
if trai <= phai:
    print("GIAO NHAU", phai - trai)
else:
    print("KHONG GIAO NHAU")
```


### pya_l05_p05_ve_gui_xe_ben_bai — Vé gửi xe bến bãi


```python
pt = input().strip().lower()
if pt == "1" or pt == "xe dap":
    print(2000)
elif pt == "2" or pt == "xe may":
    print(5000)
elif pt == "3" or pt == "o to":
    print(30000)
else:
    print("LOI PHUONG TIEN")
```


### pya_l05_p12_bon_mua_trong_nam — Bốn mùa trong năm


```python
t = int(input().strip())
if t in [1, 2, 3]:
    print("XUAN")
elif t in [4, 5, 6]:
    print("HA")
elif t in [7, 8, 9]:
    print("THU")
elif t in [10, 11, 12]:
    print("DONG")
```


### pya_l06_p08_tam_giac_vuong_hay_khong — Tam giác vuông hay không?


```python
dong1 = input().split()
if len(dong1) >= 3:
    a = int(dong1[0])
    b = int(dong1[1])
    c = int(dong1[2])
else:
    a = int(dong1[0])
    b = int(input().split()[0])
    c = int(input().split()[0])
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("VUONG")
else:
    print("KHONG VUONG")
```


### pya_l06_p10_ngay_ke_tiep_trong_nam — Ngày kế tiếp trong năm


```python
d = int(input().split()[0])
m = int(input().split()[0])
y = int(input().split()[0])
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    nhuan = True
else:
    nhuan = False
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    ngay_trong_thang = 31
elif m == 4 or m == 6 or m == 9 or m == 11:
    ngay_trong_thang = 30
elif nhuan:
    ngay_trong_thang = 29
else:
    ngay_trong_thang = 28
if d < ngay_trong_thang:
    print(d + 1, m, y)
elif m < 12:
    print(1, m + 1, y)
else:
    print(1, 1, y + 1)
```


## Chương 02 — Bài 05: Vòng lặp for và hàm range


### pya_l07_p14_tong_day_sieu_lon_khong_lap — Tổng dãy siêu lớn không lặp


```python
n = int(input())
print(n * (n + 1) // 2)
```


### pya_l07_p01_dem_sao_len_troi — Đếm sao lên trời


```python
n = int(input().strip())
print(" ".join(str(i) for i in range(1, n + 1)))
```


### pya_l07_p02_dem_nguoc_phong_ten_lua — Đếm ngược phóng tên lửa


```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
print("PHONG!")
```


### pya_l07_p03_tong_cac_so_tu_nhien — Tổng các số tự nhiên


```python
n = int(input().strip())
print(n * (n + 1) // 2)
```


### pya_l07_p13_tam_giac_vuong_dau_sao — Tam giác vuông dấu sao


```python
n = int(input())
for i in range(1, n + 1):
    print('*' * i)
```


### pya_l07_p12_hang_cot_dau_sao — Hàng cột dấu sao


```python
r = int(input())
c = int(input())
for i in range(r):
    print('*' * c)
```


### pya_l07_p07_tinh_giai_thua_n — Tính giai thừa $N!$


```python
n = int(input())
gt = 1
for i in range(1, n + 1):
    gt = gt * i
print(gt)
```


### pya_l07_p10_tong_binh_phuong — Tổng bình phương


```python
n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i * i
print(s)
```


### pya_l07_p04_bang_cuu_chuong — Bảng cửu chương


```python
n = int(input().strip())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```


### pya_l07_p05_tong_so_chan_trong_doan — Tổng số chẵn trong đoạn


```python
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        s += i
print(s)
```


### pya_l07_p11_doc_sach_moi_ngay — Đọc sách mỗi ngày


```python
n = int(input())
tong = 0
for ngay in range(1, n + 2):
    tong = tong + ngay
    if tong >= n:
        print(ngay)
        break
```


### pya_l07_p08_day_so_cach_deu — Dãy số cách đều


```python
a = int(input())
d = int(input())
n = int(input())
for i in range(n):
    print(a + i * d, end='')
    if i < n - 1:
        print(' ', end='')
print()
```


### pya_l07_p06_dem_boi_so_cua_k — Đếm bội số của K


```python
data = []
for _ in range(3):
    data.append(int(input()))
a, b, k = data
count = 0
for i in range(a, b + 1):
    if i % k == 0:
        count = count + 1
print(count)
```


### pya_l07_p09_tim_uoc_so_cua_n — Tìm ước số của N


```python
n = int(input())
first = True
for i in range(1, n + 1):
    if n % i == 0:
        if not first:
            print(' ', end='')
        print(i, end='')
        first = False
print()
```


## Chương 02 — Bài 06: Vòng lặp while và biến cờ


### pya_l08_p08_tim_luy_thua_cua_2_lon_hon_n — Tìm lũy thừa của 2 lớn hơn N


```python
n = int(input())
lt = 1
while lt <= n:
    lt = lt * 2
print(lt)
```


### pya_l08_p06_gap_doi_to_giay_len_mat_trang — Gấp đôi tờ giấy lên mặt trăng


```python
h = int(input())
day = 1
count = 0
while day < h:
    day = day * 2
    count = count + 1
print(count)
```


### pya_l08_p07_ong_heo_mua_xe_may — Ống heo mua xe máy


```python
p = int(input())
tong = 0
ngay = 0
while tong < p:
    ngay = ngay + 1
    tong = tong + ngay
print(ngay)
```


### pya_l08_p10_dem_so_luong_chu_so_cua_n — Đếm số lượng chữ số của N


```python
N = int(input())
dem = 0
while N > 0:
      N = N // 10
      dem = dem + 1
print(dem)
```


### pya_l08_p01_dem_xuoi_bang_while — Đếm xuôi bằng while


```python
n = int(input().strip())
i = 1
res = []
while i <= n:
    res.append(str(i))
    i += 1
print(" ".join(res))
```


### pya_l08_p03_nhap_so_den_khi_gap_so_0 — Nhập số đến khi gặp số 0


```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    count = count + 1
print(count)
```


### pya_l08_p04_tong_day_so_ket_thuc_bang_0 — Tổng dãy số kết thúc bằng 0


```python
tong = 0
while True:
    x = int(input())
    if x == 0:
        break
    tong = tong + x
print(tong)
```


### pya_l08_p11_tro_choi_doan_so_nhi_phan — Trò chơi đoán số nhị phân


```python
n = int(input())
count = 0
while True:
    count = count + 1
    if n == 1:
        break
    n = n // 2
print(count)
```


### pya_l08_p02_rut_tham_den_khi_trung — Rút thăm đến khi trúng


```python
while True:
    try:
        x = int(input().strip())
        if x == 7 or x == 77:
            break
    except:
        break
print("DA TRUNG THUONG!")
```


### pya_l08_p12_day_so_collatz_3n_1 — Dãy số Collatz (3n + 1)


```python
n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    count = count + 1
print(count)
```


### pya_l08_p05_dem_so_chan_den_khi_gap_0 — Đếm số chẵn đến khi gặp 0


```python
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x % 2 == 0:
        count = count + 1
print(count)
```


### pya_l08_p09_chu_oc_sen_leo_cot_co — Chú ốc sên leo cột cờ


```python
h = int(input())
a = int(input())
b = int(input())
cao = 0
ngay = 0
while True:
    ngay = ngay + 1
    cao = cao + a
    if cao >= h:
        break
    cao = cao - b
print(ngay)
```


# Mục lục

