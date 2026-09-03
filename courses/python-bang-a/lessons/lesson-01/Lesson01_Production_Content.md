# Bài 01: Lệnh xuất nhập và biến số

---

## 1. Khởi động (hook đời sống): Máy tính hiểu chúng ta nói gì?

Chào mừng các bạn nhỏ bước vào thế giới kỳ diệu của **lập trình Python**!

Các em hãy tưởng tượng máy tính giống như một bạn **Robot siêu thông minh nhưng lại rất ngây thơ**. Bạn Robot có thể tính nhẩm một tỷ phép tính chỉ trong một cái chớp mắt, nhưng bạn ấy lại **không tự biết phải làm gì** nếu không có một người chỉ huy.

Để chỉ huy bạn Robot làm việc, chúng ta cần nói chuyện với bạn ấy bằng một ngôn ngữ mà bạn ấy hiểu được. Ngôn ngữ đó chính là **Python** — ngôn ngữ lập trình phổ biến nhất thế giới hiện nay, được dùng để tạo ra các trò chơi, các phần mềm thông minh và cả trí tuệ nhân tạo (AI)!

Hôm nay, chúng ta sẽ học **những câu lệnh chỉ huy đầu tiên** để giao tiếp với bạn Robot:
1. Ra lệnh cho Robot cất tiếng chào hoặc hiển thị kết quả lên màn hình (`print`).
2. Yêu cầu Robot lắng nghe câu trả lời của người dùng từ bàn phím (`input`).
3. Tặng cho Robot những **chiếc hộp thần kỳ dán nhãn** để ghi nhớ thông tin (biến số - `Variable`).

---

## 2. Lệnh xuất màn hình: `print()` — chiếc loa phát thanh của robot

### 2.1. Bản chất của `print()`
Lệnh `print()` giống như một **chiếc loa phát thanh**. Bất cứ thứ gì em đặt vào bên trong dấu ngoặc đơn `( ... )`, Robot sẽ lập tức in nội dung đó ra màn hình cho chúng ta nhìn thấy.

* **Khi muốn in một câu văn, lời chào, chữ viết (Dạng chuỗi - String):** Em bắt buộc phải bọc chữ đó trong **cặp dấu nháy kép `"` hoặc nháy đơn `'`**. Cặp dấu nháy giống như hai bức tường bảo vệ, báo cho Python biết: *"Đây là một đoạn chữ, hãy giữ nguyên và in ra màn hình!"*.
* **Khi muốn in một con số hoặc kết quả phép tính (Dạng số - Number):** Em **không được dùng dấu nháy**, chỉ cần viết số hoặc phép tính trực tiếp.

```python
# Ví dụ 1: In lời chào ra màn hình
print("Xin chào! Mình là Python!")
print('Chúc các bạn một ngày học thật vui!')

# Ví dụ 2: In số và phép tính
print(2026)
print(10 + 5)
```

**Màn hình hiển thị kết quả:**
```text
Xin chào! Mình là Python!
Chúc các bạn một ngày học thật vui!
2026
15
```

> ⚠️ **Bẫy lỗi kinh điển số 1 (Dấu nháy thần kỳ):**
> * Nếu em viết: `print(10 + 5)` $\to$ Màn hình in ra số: `15` (Robot tính toán giúp em).
> * Nhưng nếu em viết: `print("10 + 5")` $\to$ Màn hình in ra chữ: `10 + 5` (Robot coi đây là chữ viết và không tính).

### 2.2. In nhiều món đồ cùng một lúc bằng dấu phẩy `,`
Lệnh `print()` rất thông minh, em có thể in nhiều chữ và số cùng trên một dòng bằng cách ngăn cách chúng bằng **dấu phẩy `,`**. Python sẽ tự động chèn một dấu cách ở giữa các món đồ!

```python
print("Năm nay em", 10, "tuổi.")
print("Tổng của 8 và 9 là:", 8 + 9)
```

**Kết quả:**
```text
Năm nay em 10 tuổi.
Tổng của 8 và 9 là: 17
```

---

## 3. Biến số (variable): Chiếc hộp thần kỳ có dán nhãn

### 3.1. Biến số là gì?
Trong đời sống, để đồ đạc trong phòng không bị lộn xộn, em thường xếp đồ vào từng chiếc hộp và dán nhãn bên ngoài: hộp *"Đồ chơi"*, hộp *"Bút màu"*, hộp *"Sách vở"*.

Trong lập trình, **Biến số (Variable)** chính là một **chiếc hộp chứa dữ liệu trong bộ nhớ máy tính**. Mỗi chiếc hộp sẽ có:
1. **Tên biến (Nhãn dán của hộp):** Để chúng ta gọi tên khi cần dùng (Ví dụ: `tuoi`, `diem_toan`, `ten`).
2. **Giá trị (Đồ vật đặt bên trong hộp):** Dữ liệu mà chiếc hộp đang lưu giữ (Ví dụ: số `10`, chữ `"An"`).

Dấu bằng `=` trong Python không phải là phép so sánh bằng nhau trong toán học, mà mang ý nghĩa là **Phép gán (Đặt đồ vào hộp)**:
$$\text{Tên\_Biến} = \text{Giá\_Trị}$$

```python
# Tạo chiếc hộp tên là 'tuoi' và đặt số 10 vào trong
tuoi = 10

# Tạo chiếc hộp tên là 'ten' và đặt chữ "Bảo Nam" vào trong
ten = "Bảo Nam"

# In nội dung trong hộp ra màn hình
print("Học sinh:", ten)
print("Số tuổi:", tuoi)
```

### 3.2. Bảng dry run: Giá trị trong hộp thay đổi như thế nào?
Một chiếc hộp chỉ chứa được **một món đồ tại một thời điểm**. Khi em gán giá trị mới, giá trị cũ sẽ biến mất và được thay thế bằng giá trị mới!

Hãy quan sát đoạn chương trình sau và bảng theo dõi bộ nhớ (Dry Run Table):

```python
diem = 8
print("Điểm lần 1:", diem)

diem = 10
print("Điểm lần 2:", diem)

diem = diem + 2
print("Điểm lần 3:", diem)
```

| Dòng code chạy | Thao tác trên chiếc hộp `diem` | Giá trị hiện tại trong hộp | Màn hình in ra |
|:---:|---|:---:|---|
| Dòng 1: `diem = 8` | Đặt số 8 vào hộp | **8** | *(Chưa in)* |
| Dòng 2: `print(...)` | Đọc số trong hộp ra màn hình | 8 | `Điểm lần 1: 8` |
| Dòng 4: `diem = 10` | Bỏ số 8 đi, đặt số 10 vào hộp | **10** | *(Chưa in)* |
| Dòng 5: `print(...)` | Đọc số trong hộp ra màn hình | 10 | `Điểm lần 2: 10` |
| Dòng 7: `diem = diem + 2` | Lấy 10 ra cộng 2 bằng 12, đặt 12 vào hộp | **12** | *(Chưa in)* |
| Dòng 8: `print(...)` | Đọc số trong hộp ra màn hình | 12 | `Điểm lần 3: 12` |

### 3.3. Quy tắc đặt tên biến để không bị "phạt thẻ vàng"
Tên biến giống như biển tên của em, cần phải rõ ràng và tuân theo luật của Python:
* ✅ **ĐƯỢC:** Dùng chữ cái cái tiếng Anh thường/hoa (`a` đến `z`, `A` đến `Z`), chữ số (`0` đến `9`) và dấu gạch dưới `_`. Ví dụ: `chieu_dai`, `so_luong`, `diem1`, `tong_tien`.
* ❌ **CẤM:**
  1. Không được bắt đầu bằng chữ số (Sai: `1diem`, `2ban`).
  2. Không được có khoảng trắng (Sai: `chieu dai`, `so luong`).
  3. Không được chứa ký tự đặc biệt như `@`, `#`, `$`, `%`, `-`.
  4. Không được trùng với các từ khóa riêng của Python (`print`, `input`, `if`, `for`).
  5. Đặt tên biến phải có ý nghĩa, tránh đặt tên lung tung như `x1`, `aaa`, `xyz` vì sau này đọc lại sẽ không hiểu mình đang lưu cái gì!

---

## 4. Ba kiểu dữ liệu cơ bản nhất trong Python

Python chia thông tin thành các loại đồ vật khác nhau để dễ quản lý:

| Kiểu dữ liệu | Tên viết tắt trong Python | Bản chất đời sống | Ví dụ cụ thể |
|---|:---:|---|---|
| **Số nguyên** | `int` *(Integer)* | Các số đếm nguyên vẹn, không có phần thập phân | `-5`, `0`, `7`, `100`, `2026` |
| **Số thực** | `float` *(Floating-point)* | Các số có phần lẻ thập phân (dùng dấu chấm `.`) | `3.14`, `0.5`, `9.75`, `1.68` |
| **Chuỗi ký tự** | `str` *(String)* | Dòng chữ, câu văn, ký tự đặt trong dấu nháy | `"Việt Nam"`, `'Lớp 4A'`, `"123"` |

> 💡 **Bí mật thú vị:** `"123"` có dấu nháy là **chuỗi chữ**, còn `123` không có dấu nháy là **con số tính toán được**!

---

## 5. Lệnh nhập dữ liệu: `input()` — chiếc tai lắng nghe của robot

### 5.1. Cách dùng `input()`
Để chương trình có thể tương tác với người dùng (nhập số từ bàn phím), ta dùng lệnh `input()`. Khi gặp lệnh này, máy tính sẽ tạm dừng lại và chờ em gõ phím rồi nhấn `Enter`.

```python
ten_ban = input()
print("Xin chào bạn", ten_ban)
```

### 5.2. Tử huyệt cần nhớ: `input()` luôn luôn trả về một chuỗi ký tự (`str`)!
Đây là một lỗi rất phổ biến với người mới học lập trình.

Giả sử em muốn viết chương trình tính tổng hai số $a$ và $b$:
```python
# Chương trình VIẾT SAI (Bị dính bẫy)
a = input()  # Em gõ vào số 5
b = input()  # Em gõ vào số 3
tong = a + b
print(tong)
```

**Em mong đợi kết quả là:** `8` ($5 + 3 = 8$).
**Nhưng máy tính lại in ra là:** `53`!

**Tại sao lại như vậy?**
Bởi vì `input()` coi số `5` em vừa nhập là chuỗi chữ `"5"`, và số `3` là chuỗi chữ `"3"`.
Trong Python, khi em dùng phép cộng `+` giữa hai chuỗi chữ, Python sẽ **dán dính hai chữ lại với nhau** (Nối chuỗi):
$$\text{"5"} + \text{"3"} = \text{"53"}$$

### 5.3. Bí kíp giải bẫy: Ép kiểu dữ liệu (`int()` và `float()`)
Để biến chuỗi chữ thành số nguyên thực sự nhằm tính toán cộng trừ nhân chia, em phải dùng "chiếc búa ma thuật" **`int()`** để bọc lấy `input()`:

```python
# Chương trình VIẾT ĐÚNG CHUẨN:
a = int(input())   # Nhận chữ "5" -> Búa int() biến thành số nguyên 5
b = int(input())   # Nhận chữ "3" -> Búa int() biến thành số nguyên 3
tong = a + b       # Số 5 + Số 3 = Số 8
  print(tong)        # Màn hình in ra: 8
```

* Nếu số nhập vào là số thập phân, em dùng `float(input())`.
* Khi đi thi Tin học trẻ, đề bài thường yêu cầu đọc dữ liệu trên từng dòng hoặc cùng dòng, học sinh Tiểu học nắm chắc `int(input())` là đã giải quyết được hơn 80% các bài toán mở màn!

---

## 6. Tổng kết bảng bẫy lỗi lập trình bài 1

| Tình huống code sai | Lỗi hiển thị | Nguyên nhân bản chất | Cách sửa đúng |
|---|---|---|---|
| `print("Chào bạn)` | `SyntaxError: unterminated string literal` | Mở nháy kép nhưng quên đóng nháy kép | `print("Chào bạn")` |
| `1tuoi = 10` | `SyntaxError: invalid decimal literal` | Tên biến bắt đầu bằng chữ số | `tuoi_1 = 10` hoặc `tuoi = 10` |
| `a = input()` <br> `b = input()` <br> `print(a + b)` | In ra `12` thay vì `3` | `input()` tạo ra kiểu chuỗi, dấu `+` làm nhiệm vụ nối chữ | `a = int(input())` <br> `b = int(input())` <br> `print(a + b)` |
| `print(tuoi)` *(khi chưa tạo biến `tuoi`)* | `NameError: name 'tuoi' is not defined` | Chiếc hộp `tuoi` chưa được tạo mà đã đòi mang ra dùng | Gán giá trị trước: `tuoi = 10` rồi mới `print(tuoi)` |

---

## 7. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (nhận diện — cú pháp):
Lệnh nào sau đây dùng để hiển thị dòng chữ `Học Python thật vui` lên màn hình máy tính?
- **A.** `echo("Học Python thật vui")`
- **B.** **[Đáp án đúng]** `print("Học Python thật vui")`
- **C.** `input("Học Python thật vui")`
- **D.** `printf("Học Python thật vui");`
> *Giải thích:* Trong Python, lệnh `print()` có chức năng in dữ liệu ra màn hình. Lệnh `input()` dùng để nhập dữ liệu.

#### Câu 2 (dự đoán output — phép cộng chuỗi):
Đoạn code sau đây sẽ in ra màn hình kết quả gì?
```python
x = "20"
y = "26"
print(x + y)
```
- **A.** `46`
- **B.** **[Đáp án đúng]** `2026`
- **C.** Báo lỗi chương trình (Error)
- **D.** `x + y`
> *Giải thích:* Cả `x` và `y` đều nằm trong dấu nháy kép nên là kiểu chuỗi (`str`). Phép toán `+` giữa hai chuỗi sẽ nối dính chúng lại với nhau thành `"2026"`.

#### Câu 3 (bản chất biến số — gán đè giá trị):
Sau khi thực hiện 3 dòng lệnh sau, giá trị cuối cùng lưu trong biến `k` là bao nhiêu?
```python
k = 5
k = k + 3
k = 10
```
- **A.** `8`
- **B.** `18`
- **C.** **[Đáp án đúng]** `10`
- **D.** `15`
> *Giải thích:* Ban đầu $k = 5$, sau đó $k = 5 + 3 = 8$. Nhưng ở dòng lệnh cuối cùng, ta gán đè $k = 10$, do đó giá trị cũ bị xóa và biến $k$ giữ giá trị $10$.

#### Câu 4 (bắt bẫy quy tắc — đặt tên biến):
Tên biến nào sau đây là **HỢP LỆ** và chạy được trong Python mà không bị báo lỗi cú pháp?
- **A.** `2_ban_than`
- **B.** `diem toan`
- **C.** **[Đáp án đúng]** `chieu_dai_1`
- **D.** `so-luong`
> *Giải thích:* Tên biến không được bắt đầu bằng chữ số (loại A), không được có khoảng trắng (loại B), không được chứa dấu gạch ngang trừ `-` (loại D). Chỉ có C dùng dấu gạch dưới `_` là hoàn toàn hợp lệ.

#### Câu 5 (bắt bẫy kiểu dữ liệu — ép kiểu):
Để nhập một số nguyên $N$ từ bàn phím để tính toán, cách viết nào sau đây là **chuẩn nhất**?
- **A.** `N = input()`
- **B.** **[Đáp án đúng]** `N = int(input())`
- **C.** `N = str(input())`
- **D.** `N = print(input())`
> *Giải thích:* `input()` nhận vào chuỗi ký tự, cần bọc ngoài bằng `int()` để chuyển thành số nguyên.

#### Câu 6 (dự đoán output — dấu phẩy trong lệnh `print`):
Đoạn chương trình sau sẽ in ra màn hình nội dung gì?
```python
ten = "Minh"
tuoi = 9
print("Ban", ten, "nam nay", tuoi, "tuoi.")
```
- **A.** `BanMinhnamnay9tuoi.`
- **B.** **[Đáp án đúng]** `Ban Minh nam nay 9 tuoi.`
- **C.** `Ban, Minh, nam nay, 9, tuoi.`
- **D.** Báo lỗi `TypeError`
> *Giải thích:* Khi dùng dấu phẩy `,` giữa các đối số trong `print()`, Python tự động chèn một khoảng trắng giữa các phần tử.

#### Câu 7 (nhận diện kiểu dữ liệu):
Giá trị `3.14` trong Python thuộc kiểu dữ liệu nào?
- **A.** `int`
- **B.** `str`
- **C.** **[Đáp án đúng]** `float`
- **D.** `bool`
> *Giải thích:* Các số có phần thập phân phân tách bằng dấu chấm `.` được gọi là số thực, ký hiệu là `float`.

#### Câu 8 (bắt bẫy logic — dấu nháy):
Bạn An viết chương trình:
```python
print("5 * 4 = ", 5 * 4)
```
Màn hình sẽ hiển thị kết quả là:
- **A.** `20 = 20`
- **B.** `5 * 4 = 5 * 4`
- **C.** **[Đáp án đúng]** `5 * 4 =  20`
- **D.** Báo lỗi cú pháp
> *Giải thích:* Phần `"5 * 4 = "` nằm trong nháy nên giữ nguyên, phần `5 * 4` không nằm trong nháy nên máy tính tính ra $20$.

#### Câu 9 (bắt bẫy thứ tự gán giá trị):
Quan sát đoạn mã sau:
```python
a = 15
b = a
a = 20
print(b)
```
Màn hình sẽ in ra giá trị của `b` là bao nhiêu?
- **A.** `20`
- **B.** **[Đáp án đúng]** `15`
- **C.** `35`
- **D.** `b`
> *Giải thích:* Khi chạy dòng `b = a`, giá trị $15$ của `a` được sao chép vào `b`. Sau đó đổi $a = 20$ thì giá trị trong chiếc hộp `b` vẫn là $15$, không bị ảnh hưởng.

#### Câu 10 (nhận diện thông báo lỗi — nameerror):
Khi chạy đoạn code sau:
```python
diem = 10
print(Diem)
```
Chương trình sẽ xảy ra hiện tượng gì?
- **A.** In ra số 10 bình thường.
- **B.** **[Đáp án đúng]** Báo lỗi `NameError: name 'Diem' is not defined`.
- **C.** In ra chữ `Diem`.
- **D.** In ra số 0.
> *Giải thích:* Python phân biệt chữ hoa và chữ thường (Case-sensitive). Biến `diem` (chữ thường) khác hoàn toàn với `Diem` (chữ hoa). Vì chưa tạo biến `Diem` nên máy báo lỗi không tìm thấy tên biến.

#### Câu 11 (chuyển đổi kiểu dữ liệu):
Kết quả của câu lệnh `print(type(100))` trong Python là gì?
- **A.** `<class 'str'>`
- **B.** `<class 'float'>`
- **C.** **[Đáp án đúng]** `<class 'int'>`
- **D.** `100`
> *Giải thích:* Hàm `type()` dùng để kiểm tra kiểu dữ liệu của một giá trị. Số $100$ là số nguyên nên thuộc lớp `int`.

#### Câu 12 (tư duy lập trình — ứng dụng):
Một bài toán yêu cầu: *"Nhập vào số lượng học sinh $N$, sau đó in ra số lượng kẹo cần mua biết mỗi bạn được chia 3 cái kẹo"*. Đoạn code nào sau đây giải đúng bài toán?
- **A.** `N = input(); print(N * 3)`
- **B.** **[Đáp án đúng]** `N = int(input()); print(N * 3)`
- **C.** `N = int(input()); print("N * 3")`
- **D.** `print(int(input) * 3)`
> *Giải thích:* Nếu không ép kiểu `int(input())`, khi nhập `4`, lệnh `N * 3` ở đáp án A sẽ in ra chuỗi `"444"`. Chỉ có đáp án B ép kiểu thành công $4 \times 3 = 12$.
